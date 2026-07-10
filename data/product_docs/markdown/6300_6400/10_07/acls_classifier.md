| AOS-CX     |       | 10.07    | ACLs   | and    |
| ---------- | ----- | -------- | ------ | ------ |
| Classifier |       | Policies |        | Guide  |
| 6300,      | 6400, | 8360     | Switch | Series |
PartNumber:5200-7831
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

| 2

Contents
Contents
| Contents                                                |                                        | 3   |
| ------------------------------------------------------- | -------------------------------------- | --- |
| About this                                              | document                               | 5   |
| Applicableproducts                                      |                                        | 5   |
| Latestversionavailableonline                            |                                        | 5   |
| Commandsyntaxnotationconventions                        |                                        | 5   |
| Abouttheexamples                                        |                                        | 6   |
| Identifyingswitchportsandinterfaces                     |                                        | 6   |
| Identifyingmodularswitchcomponents                      |                                        | 7   |
| Access Control                                          | Lists                                  | 8   |
| ACLusagetips                                            |                                        | 9   |
| Aboutaddressandportobjectgroups                         |                                        | 10  |
| ACLandACE-relatedtasks                                  |                                        | 10  |
| Objectgroup-relatedtasks                                |                                        | 12  |
| ActiveACLconfigurationversususer-specifiedconfiguration |                                        | 13  |
| ACLcommands                                             |                                        | 15  |
|                                                         | ACLapplication                         | 15  |
|                                                         | access-listcopy                        | 16  |
|                                                         | access-listip                          | 19  |
|                                                         | access-listipv6                        | 27  |
|                                                         | access-listlog-timer                   | 34  |
|                                                         | access-listmac                         | 36  |
|                                                         | access-listresequence                  | 42  |
|                                                         | access-listreset                       | 44  |
|                                                         | applyaccess-listcontrol-plane          | 46  |
|                                                         | applyaccess-list(tointerfaceorLAG)     | 47  |
|                                                         | applyaccess-list(tointerfaceVLAN)      | 49  |
|                                                         | applyaccess-list(toVLAN)               | 51  |
|                                                         | clearaccess-listhitcounts              | 53  |
|                                                         | clearaccess-listhitcountscontrol-plane | 54  |
|                                                         | object-groupaddressresequence          | 54  |
|                                                         | object-groupaddressreset               | 55  |
|                                                         | object-groupallreset                   | 56  |
|                                                         | object-groupipaddress                  | 56  |
|                                                         | object-groupipv6address                | 58  |
|                                                         | object-groupport                       | 60  |
|                                                         | object-groupportresequence             | 61  |
|                                                         | object-groupportreset                  | 62  |
|                                                         | showaccess-list                        | 62  |
|                                                         | showaccess-listcontrol-plane           | 67  |
|                                                         | showaccess-listhitcounts               | 69  |
|                                                         | showaccess-listhitcountscontrol-plane  | 71  |
|                                                         | showcapacities                         | 71  |
|                                                         | showcapacities-status                  | 73  |
|                                                         | showobject-group                       | 74  |
| ACL configuration                                       | examples                               | 77  |
| IPv4ACLexampleoverview                                  |                                        | 77  |
3
AOS-CX10.07ACLsandClassifierPoliciesGuide| (6300,6400,8360SwitchSeries)

| DefiningandapplyinganIPv4ACL                              |          |     |     | 77  |
| --------------------------------------------------------- | -------- | --- | --- | --- |
| IPv6ACLexampleoverview                                    |          |     |     | 78  |
| DefiningandapplyinganIPv6ACL                              |          |     |     | 79  |
| Classifier                                                | policies |     |     | 81  |
| Trafficpolicing                                           |          |     |     | 81  |
| Typesofpolicyactions                                      |          |     |     | 82  |
| Howpolicymatchingworks                                    |          |     |     | 83  |
| Activeclassconfigurationversususer-specifiedconfiguration |          |     |     | 83  |
Activepolicyconfigurationversususer-specifiedconfiguration 84
| Classifierpolicycommands |                             |     |     | 85  |
| ------------------------ | --------------------------- | --- | --- | --- |
|                          | Classifierpolicyapplication |     |     | 85  |
|                          | applypolicy(Context:config) |     |     | 85  |
applypolicy(Contexts:config-if,config-if-vlan,config-vlan) 86
|                                         | classcopy                            |               |                | 88  |
| --------------------------------------- | ------------------------------------ | ------------- | -------------- | --- |
|                                         | classip                              |               |                | 89  |
|                                         | classipv6                            |               |                | 95  |
|                                         | classmac                             |               |                | 100 |
|                                         | classresequence                      |               |                | 104 |
|                                         | classreset                           |               |                | 106 |
|                                         | clearpolicyhitcounts                 |               |                | 106 |
|                                         | policy                               |               |                | 107 |
|                                         | policycopy                           |               |                | 111 |
|                                         | policyresequence                     |               |                | 112 |
|                                         | policyreset                          |               |                | 113 |
|                                         | showclass                            |               |                | 113 |
|                                         | showpolicy                           |               |                | 115 |
| Classifier                              | policies                             | configuration | example        | 118 |
| Configuringtheclassifierpoliciesexample |                                      |               |                | 118 |
| ACL and                                 | Policy hardware                      | resource      | considerations | 121 |
| TCAMlookups                             |                                      |               |                | 121 |
| Matchingprecedenceorder                 |                                      |               |                | 122 |
| L4portranges                            |                                      |               |                | 122 |
| Contextgroupselectors                   |                                      |               |                | 122 |
| ACLandPolicyhardwareresourcecommands    |                                      |               |                | 124 |
|                                         | showresources(6300,6400SwitchSeries) |               |                | 124 |
|                                         | showresources(8360SwitchSeries)      |               |                | 125 |
| Support                                 | and other                            | resources     |                | 128 |
| AccessingArubaSupport                   |                                      |               |                | 128 |
| AccessingUpdates                        |                                      |               |                | 128 |
|                                         | ArubaSupportPortal                   |               |                | 128 |
|                                         | MyNetworking                         |               |                | 129 |
| WarrantyInformation                     |                                      |               |                | 129 |
| RegulatoryInformation                   |                                      |               |                | 129 |
| DocumentationFeedback                   |                                      |               |                | 129 |
Contents|4

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

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A)

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

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

5

Convention

Usage

{ }

[ ]

… or

...

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

Identifying switch ports and interfaces
Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 6300 Switch Series

About this document | 6

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

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on

physical port 4 in slot 1 on member 1.

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

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

7

Chapter 2

Access Control Lists

Access Control Lists

Access Control Lists (ACLs) let a network administrator permit or deny passage of traffic based on network
addresses, protocols, service ports, and other packet attributes. ACLs are composed of one or more Access
Control Entries (called ACEs). Each ACE defines a filter criteria and an action, either permit or deny. If the
traffic matches the filter criteria, the specified action is taken. The permit action permits the traffic to
continue through the switch. The deny action causes the traffic to be discarded (dropped). ACEs can also log
or count matching traffic.

Three ACL types are supported; IPv4, IPv6, and MAC. Each ACL type is focused on relevant frame or packet
characteristics.

ACLs must be applied (using an apply access-list command) to take effect. ACLs can be applied to
interfaces (including LAGs), VLANs, or the Control Plane.

Access Control Entries (ACEs) are listed according to priority by sequence number and processed in lowest to
highest sequence number order. Each ACE attempts to match on one or more attributes of the particular
traffic type. Attempted ACE matching ceases upon the first successful match. For a match to be considered
successful, a packet must match all the criteria, qualifiers, and attributes of a particular ACE. Higher-
numbered ACEs are only processed if no lower-numbered ACE matches. If the traffic matches no ACE in the
entire ACL, the default action deny is taken, causing the traffic to be discarded (dropped).

When defining an ACE, if the sequence number is omitted, the ACE is auto-assigned a new sequence number
that is 10 greater than the existing highest ACE sequence number. The first auto-assigned sequence number
is 10. If you choose to include the ACE sequence numbers, you can use any number you like, however it is
suggested that you follow the practice of entering them as 10, 20, 30, and so on. Regardless of the order in
which ACEs are entered, they are stored in low-to-high sequence number order. If you enter three ACEs
numbered 10, 30, 20, when creating an ACL, the ACEs are stored in the ACL as 10, 20, 30.

This simple ACL definition permits traffic passage for a particular address range and otherwise counts all
nonmatching (dropped) traffic:

switch(config)# access-list ip network-A-udp-only
switch(config-acl-ip)# 10 permit udp any 172.16.1.0/24
switch(config-acl-ip)# 20 deny any any any count
switch(config-acl-ip)# exit

The main traffic characteristics that ACEs can filter on are as follows (see the full list in the ACE parameters list
of the ACL commands):

n Protocol such as: ICMP, TCP, UDP

n Source and/or destination addresses (IPv4, IPv6, or MAC)

n Source and/or destination TCP/UDP ports (if applicable to the specified protocol)

A few real-world uses of ACLs are as follows:

n Restrict traffic arriving on a routed port, destined to a particular address or subnet by applying an ACL

that matches on a destination IP address or an IP address and a mask.

n Prevent an entire subnet from routing through a port by applying an ACL that matches on IP source

address and a mask.

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

8

n Prevent certain protocols from using a particular multicast MAC address (advertising through a port) by

applying an ACL that matches on the destination MAC address.

n Prevent any IP host from accessing a particular IP port/application on a specific server by applying an ACL

that matches on IP addresses and Layer 4 port.

See also ACL and Policy hardware resource considerations.

ACL usage tips
When using the access-list ip or access-list ipv6 commands, if you enter an existing ACL-NAME, the
existing ACL is modified as follows:

n Any ACE entered with a new sequence-number creates an additional ACE.

n Any ACE entered with an existing sequence-number replaces the existing ACE.

If you modify an ACL that has already been applied, it is possible that packets, blocked by the previous ACL,
will briefly pass through the switch during the ACL reconfiguration.

In a highly secure environment, it is safest to first bring down interfaces and VLANs to which an ACL has been

applied before modifying the ACL. Then bring the targets of ACL application back up after completing the ACL

modification. Respecting this recommendation ensures that an ACL is never partially programmed while traffic is

passing through the switch.

About applying ACLs to interfaces or LAGs

You can apply an ACL to an interface or LAG to affect or control the traffic arriving on that interface or LAG
(inbound) or leaving the interface or LAG (outbound), or both. A given interface or LAG supports the
application of a single ACL per type, per direction. ACLs can be applied to interfaces or LAGs as follows:

n One MAC ACL inbound

n One MAC ACL outbound

n One IPv4 ACL inbound

n One IPv4 ACL outbound

n One IPv6 ACL inbound

n One IPv6 ACL outbound

Different ACLs of the same type can be used in opposite directions for MAC, IPv4, and IPv6. If you apply an
ACL of a particular type, in a direction that is already in use, the switch replaces the current ACL with the new
ACL.

About applying ACLs to VLANs

ACLs can be applied to VLANs in the inbound (ingress) and outbound (egress) directions.

Sequence numbering

If no sequence number is specified, the software appends new ACEs to the end of the ACL with a sequence
number equal to the highest ACE currently in the list plus 10.

The sequence numbers may be resequenced using the access-list resequence command.

Deny ACLs

Access Control Lists | 9

IfmultipleACLsofdifferenttypesareappliedinthesamedirection,adenyACE,whetherexplicitorimplicit,
inoneACLoverridesapermitACLinanother.AdenyACEisanACEwithinanACLthatusesthedenyaction
keyword.
Deniedpingrequests
ApingrequestisdeniedwhenanACLisappliedoningressoregressunlesstherequestisexplicitly
permitted.
| switch# | ping       | 100.1.2.10   |               |        |          |
| ------- | ---------- | ------------ | ------------- | ------ | -------- |
| PING    | 100.1.2.10 | (100.1.2.10) | 100(128)      | bytes  | of data. |
| ping:   | sendmsg:   | Operation    | not permitted |        |          |
| ping:   | sendmsg:   | Operation    | not permitted |        |          |
| ping:   | sendmsg:   | Operation    | not permitted |        |          |
| ping:   | sendmsg:   | Operation    | not permitted |        |          |
| ping:   | sendmsg:   | Operation    | not permitted |        |          |
| About   | address    | and          | port          | object | groups   |
ObjectgroupsareusefulfordefininggroupsofIPaddressesandLayer4portsforuseexclusivelyinthetwo
| ACL-definingcommandsaccess-list |     |     | ipandaccess-list |     | ipv6. |
| ------------------------------- | --- | --- | ---------------- | --- | ----- |
Often,commongroupsofaddressesandportsorportrangesareusedrepeatedlyinmanyACLdefinitions.
Withoutaddressandportobjectgroups,thesameaddressesandportsmustberepeatedineachACL
definitionthatusesthem.
Withaddressandportobjectgroups,theIPaddressesandportscanbedefinedonce,usinganyofthese
commands:
| n object-group |     | ip address   |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- |
| n object-group |     | ipv6 address |     |     |     |
| n object-group |     | port         |     |     |     |
Onceanobjectgroupisdefined,thegroupisavailableforinclusionbynameasthe<ADDRESS-GROUP>and
<PORT-GROUP>parametersintheaccess-list ipandaccess-list ipv6ACL-definitioncommands.
ObjectgroupssimplifytheACLdefinitionprocessandhelpensureconsistentaddressandportspecification
acrossmanyACLs.
Keepinmindthatitispossibletoconsumemanyhardwareresourceentrieswhenusingtheobjectgroup
commands.Forexample,inatypicalsituation,anACEthatusesobjectgroupswith3sourceaddresses,3source
L4ports,3destinationaddresses,and3destinationL4ports,atotalof81hardwareentriesareconsumed(3*3*
3*3=81).
| ACL | and ACE-related |     | tasks |     |     |
| --- | --------------- | --- | ----- | --- | --- |
CommonACLandACE-relatedtasksareasfollows:
Onthe6400SwitchSeries,interfaceidentificationdiffers.
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 10

| Task              | Commandname |     | Example     |                   |               |         |     |
| ----------------- | ----------- | --- | ----------- | ----------------- | ------------- | ------- | --- |
| CreatinganIPv4ACL | access-list | ip  | access-list | ip MY_IP_ACL      |               |         |     |
|                   |             |     | 10 permit   | udp any           | 172.16.1.0/24 |         |     |
|                   |             |     | 20 permit   | tcp 172.16.2.0/16 |               | gt 1023 | any |
|                   |             |     | 30 deny     | any any           | any count     |         |     |
CreatinganIPv6ACL access-list ipv6 access-list ipv6 MY_IPV6_ACL
|                       |                      |     | 10 permit   | udp any             | 2001::1/64 |      |     |
| --------------------- | -------------------- | --- | ----------- | ------------------- | ---------- | ---- | --- |
|                       |                      |     | 20 permit   | tcp 2001:2011::1/64 |            | any  |     |
|                       |                      |     | 30 deny     | any any             | any count  |      |     |
| CreatingaMACACL       | access-list          | mac | access-list | mac MY_MAC_ACL      |            |      |     |
|                       |                      |     | 10 permit   | any any             | appletalk  | vlan | 40  |
|                       |                      |     | 20 deny     | any any             | any count  |      |     |
| ApplyinganIPv6ACLtoan | apply access-list(to |     | interface   | 1/1/1               |            |      |     |
interface interfaceorLAG) apply access-list ipv6 MY_IPV6_ACL in
|                      |                      |     | interface | lag 100     |              |     |     |
| -------------------- | -------------------- | --- | --------- | ----------- | ------------ | --- | --- |
| ApplyinganIPv4ACLtoa | apply access-list(to |     |           |             |              |     |     |
| LAG                  | interfaceorLAG)      |     | apply     | access-list | ip MY_IP_ACL | in  |     |
vlan 10
| ApplyinganIPv4ACLtoa | apply access-list(to |     |         |             |              |     |     |
| -------------------- | -------------------- | --- | ------- | ----------- | ------------ | --- | --- |
|                      |                      |     | apply   | access-list | ip MY_IP_ACL | in  |     |
| VLAN                 | VLAN)                |     |         |             |              |     |     |
| ApplyingaMACACLtoa   |                      |     | vlan 40 |             |              |     |     |
apply access-list(to
|      |       |     | apply | access-list | mac MY_MAC_ACL |     | in  |
| ---- | ----- | --- | ----- | ----------- | -------------- | --- | --- |
| VLAN | VLAN) |     |       |             |                |     |     |
ApplyinganIPv4ACLtothe apply access-list apply access-list ip MY_IP_ACL control-
ControlPlane(OOBM)
|                         | control-plane        |     | plane vrf | mgmt        |      |             |     |
| ----------------------- | -------------------- | --- | --------- | ----------- | ---- | ----------- | --- |
|                         |                      |     | interface | 1/1/1       |      |             |     |
| Removingapplicationofan | apply access-list(to |     |           |             |      |             |     |
|                         |                      |     | no apply  | access-list | ipv6 | MY_IPV6_ACL | in  |
| ACLfromaninterface      | interfaceorLAG)      |     |           |             |      |             |     |
| Removingapplicationofan |                      |     | vlan 40   |             |      |             |     |
apply access-list(to
|              |       |     | no apply | access-list | mac | MY_MAC_ACL | in  |
| ------------ | ----- | --- | -------- | ----------- | --- | ---------- | --- |
| ACLfromaVLAN | VLAN) |     |          |             |     |            |     |
Removingapplicationofan apply access-list no apply access-list ip MY_IP_ACL control-
ACLfromtheControlPlane
|     | control-plane |     | plane vrf | mgmt |     |     |     |
| --- | ------------- | --- | --------- | ---- | --- | --- | --- |
(OOBM)
| ShowingallACLs     | show access-list |     | show access-list |     |      |     |     |
| ------------------ | ---------------- | --- | ---------------- | --- | ---- | --- | --- |
| ShowingallIPv6ACLs | show access-list |     | show access-list |     | ipv6 |     |     |
ShowingallACLsappliedto show access-list show access-list interface 1/1/1
interface1/1/1
ShowingallACLsappliedto show access-list show access-list vlan 10
VLAN10
ShowingallACLsappliedto show access-list show access-list control-plane
| theControlPlane | control-plane |     |     |     |     |     |     |
| --------------- | ------------- | --- | --- | --- | --- | --- | --- |
ShowingaparticularACL show access-list show access-list ip MY_ACL
AccessControlLists|11

| Task |     |     | Commandname |     | Example |     |
| ---- | --- | --- | ----------- | --- | ------- | --- |
ShowinganACLas show access-list show access-list ip MY_ACL commands
commands
ShowingACLhitcountsfor show access-list show access-list hitcounts ip MY_ACL
| anACLappliedtoan |     |     | hitcounts |     | interface | 1/1/1 |
| ---------------- | --- | --- | --------- | --- | --------- | ----- |
interface
ShowingACLhitcountsfor show access-list show access-list hitcounts ip MY_ACL vlan
| anACLappliedtoaVLAN |     |     | hitcounts |     | 10  |     |
| ------------------- | --- | --- | --------- | --- | --- | --- |
ShowingACLhitcountsfor show access-list show access-list hitcounts ip MY_ACL
| anACLappliedtothe |     |     | hitcounts | control- | control-plane | vrf mgmt |
| ----------------- | --- | --- | --------- | -------- | ------------- | -------- |
ControlPlane
plane
ClearingACLhitcounts clear access-list clear access-list hitcounts ip MY_ACL vlan
|     |     |     | hitcounts |     | 10  |     |
| --- | --- | --- | --------- | --- | --- | --- |
ClearingACLhitcountsfor clear access-list clear access-list hitcounts control-plane
| ControlPlane |     |     | hitcounts | control- | vrf mgmt |     |
| ------------ | --- | --- | --------- | -------- | -------- | --- |
plane
CopyinganACL access-list copy access-list ipv6 MY_IPV6_ACL copy MY_IPV6_
ACL2
ResequencingtheACEsof access-list access-list ip MY_IP_ACL resequence 1 1
| anACL |     |     | resequence |     |     |     |
| ----- | --- | --- | ---------- | --- | --- | --- |
ResettinganACL access-list reset access-list ip MY_IP_ACL reset
SettingtheACLlogtimer access-list log- access-list log-timer 30
| frequency |               |     | timer |     |     |     |
| --------- | ------------- | --- | ----- | --- | --- | --- |
| Object    | group-related |     | tasks |     |     |     |
ObjectgroupsareusefulfordefininggroupsofaddressesandportsforuseexclusivelyinthetwoACL-
| definingcommandsaccess-list |     |     | ipandaccess-list |     | ipv6. |     |
| --------------------------- | --- | --- | ---------------- | --- | ----- | --- |
Commonobjectgroup-relatedtasksareasfollows:
Commandname
| Task |     |     |     | Example |     |     |
| ---- | --- | --- | --- | ------- | --- | --- |
CreatinganIPv4 object-group ip object-group ip address my_ipv4_addr_group
| addressobject |     | address |     |     |     |     |
| ------------- | --- | ------- | --- | --- | --- | --- |
group
CreatinganIPv6 object-group object-group ipv6 address my_ipv6_addr_group
| addressobject |     | ipv6 address |     |     |     |     |
| ------------- | --- | ------------ | --- | --- | --- | --- |
group
| Creatingaport |     | object-group |     | object-group | port | my_port_group |
| ------------- | --- | ------------ | --- | ------------ | ---- | ------------- |
objectgroup
port
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 12

Task

Command name

Example

Showing an IPv4
address object
group

Showing all IPv6
address object
groups

show object-
group

show object-
group

Showing a port
object group

show object-
group

Showing all port
object groups as
commands

show object-
group

show object-group ip address my_ipv4_addr_group

show object-group ipv6 address

show object-group port my_port_group

show object-group port commands

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
have been configured. The output of this command may not be the same as what was programmed in the
hardware or what is active on the switch. The situation might occur because of one or more of the following:

n Unsupported command parameters might have been configured.

n Unsupported applications might have been specified.

n Applying an ACL might have been unsuccessful due to lack of hardware resources.

To determine if a discrepancy exists between what was configured and what is active, run the show access-
list command with the configuration parameter.

If the active ACLs and configured ACLs are not the same, the switch shows a warning message in the output
of the show command:

Access Control Lists | 13

! access-list ip MY_IP_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
IftheconfiguredACLisprocessing,theswitchshowsanin-progresswarning.
! access-list ip MY_IP_ACL user configuration currently being processed
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
Iftheswitchshowsawarningmessageorin-progressmessage,additionalchangescanbemadeuntilthe
errormessageisnolongershownintheshowcommand,oryoucanruntheaccess-list {all|ip <ACL-
NAME>|ipv6 <ACL-NAME>|mac <ACL-NAME>} resetcommand.Theaccess-list resetcommandchanges
theuser-specifiedconfigurationtomatchtheactiveconfiguration.Fordetails,seeaccess-listreset.
Theshow running-configcommandalsoshowsawarningaboutACLsthatareinprogressorfailed.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ApplyinganACLwithTCPacknowledgments(ACKs)oningress:
| switch(config-acl)# |     |     | 10  | permit | tcp 172.16.2.0/16 |     | any ack |
| ------------------- | --- | --- | --- | ------ | ----------------- | --- | ------- |
Showingtheuser-specifiedconfiguration:
| switch(config)# |     | do     | show              | access-list |     | ip TEST_ACL |     |
| --------------- | --- | ------ | ----------------- | ----------- | --- | ----------- | --- |
|                 | 10  | permit | tcp 172.16.2.0/16 |             |     | any ack     |     |
| interface       |     | 1/1/1  |                   |             |     |             |     |
! access-list ip TEST_ACL user configuration does not match active
configuration.
! run 'show access-list [commands]' to display active access-list configuration.
|                 | apply  | access-list |               | ip          | TEST_ACL | in       |     |
| --------------- | ------ | ----------- | ------------- | ----------- | -------- | -------- | --- |
| switch(config)# |        | do          | show          | access-list |          | commands |     |
| access-list     |        | ip TEST_ACL |               |             |          |          |     |
| 10              | permit | tcp         | 172.16.2.0/16 |             | any      | ack      |     |
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list all reset' to reset all access-lists to match active
configuration.
| switch(config)# |        | do          | show          | access-list |     | commands | configuration |
| --------------- | ------ | ----------- | ------------- | ----------- | --- | -------- | ------------- |
| access-list     |        | ip TEST_ACL |               |             |     |          |               |
| 10              | permit | tcp         | 172.16.2.0/16 |             | any | ack      |               |
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list all reset' to reset all access-lists to match active
configuration.
| interface       | 1/1/1       |         |      |             |     |     |          |
| --------------- | ----------- | ------- | ---- | ----------- | --- | --- | -------- |
| apply           | access-list |         | ip   | TEST_ACL    | in  |     |          |
| switch(config)# |             | do      | show | access-list |     |     |          |
| Type            |             | Name    |      |             |     |     |          |
| Sequence        |             | Comment |      |             |     |     |          |
|                 |             | Action  |      |             |     | L3  | Protocol |
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 14

|     | Source      | IP Address |            |     | Source      | L4 Port(s) |     |
| --- | ----------- | ---------- | ---------- | --- | ----------- | ---------- | --- |
|     | Destination |            | IP Address |     | Destination | L4 Port(s) |     |
|     | Additional  |            | Parameters |     |             |            |     |
-------------------------------------------------------------------------------
| IPv4 | TEST_ACL  |     |     |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- | --- | --- |
|      | 10 permit |     |     |     | tcp |     |     |
172.16.2.0/16
any
ack
Resettingtheuser-specifiedconfigurationtomatchtheactiveconfiguration:
switch(config)#
|     |     | access-list | all reset |     |     |     |     |
| --- | --- | ----------- | --------- | --- | --- | --- | --- |
Showingtheupdateduser-specifiedconfiguration:
| switch(config)# |           | do show     | access-list   | commands | configuration |     |     |
| --------------- | --------- | ----------- | ------------- | -------- | ------------- | --- | --- |
| access-list     |           | ip TEST_ACL |               |          |               |     |     |
|                 | 10 permit | tcp         | 172.16.2.0/16 | any      | ack           |     |     |
ACL commands
ACL application
ACLscanbeappliedasfollows:
| ACL type             |     |     | IPv4+6      |     | IPv4+6      | MAC | MAC |
| -------------------- | --- | --- | ----------- | --- | ----------- | --- | --- |
| Direction            |     |     | In          |     | Out         | In  | Out |
| L2interface(port)    |     |     | Yes         |     | Yes         | Yes | Yes |
| L2LAG                |     |     | Yes         |     | Yes         | Yes | Yes |
| L3interface(port)    |     |     | Yes         |     | Yes         | Yes | Yes |
| L3LAG                |     |     | Yes         |     | Yes         | Yes | Yes |
| VLAN                 |     |     | Yes         |     | Yes         | Yes | Yes |
| InterfaceVLAN        |     |     | Yes(routed) |     | Yes(routed) |     |     |
| Managementinterface  |     |     | Yes         |     |             |     |     |
| Controlplane(perVRF) |     |     | Yes         |     |             |     |     |
AccessControlLists|15

Thefollowingmatchcriteriaisnotsupported.Ifthismatchcriteriaisattemptedtobeconfigured,anerror
messagewillbedisplayedandtheactionwillnotbecompleted.
| TTL on | IP ACLs |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- |
ToapplyIPv4and/orIPv6ACLstothemanagementinterface,applythemtothecontrolplaneonthemanagement
VRF.
| access-list | copy |     |     |     |     |     |
| ----------- | ---- | --- | --- | --- | --- | --- |
Syntax
| access-list | {ip|ipv6|mac} |     | <ACL-NAME> | copy | <DESTINATION-ACL> |     |
| ----------- | ------------- | --- | ---------- | ---- | ----------------- | --- |
Description
CopiesanIPv4,IPv6,orMACACLtoanewdestinationACLoroverwritesanexistingACL.
Commandcontext
config
Parameters
{ip|ipv6|mac}
SpecifiesthetypeofACL.
<ACL-NAME>
SpecifiesthenameoftheACLtobecopied.
<DESTINATION-ACL>
SpecifiesthenameofthedestinationACL.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CopyingMY_IP_ACLtoMY_IP_ACL2:
| switch(config)#        |             | access-list |                  | ip MY_IP_ACL | copy MY_IP_ACL2 |            |
| ---------------------- | ----------- | ----------- | ---------------- | ------------ | --------------- | ---------- |
| switch(config-acl-ip)# |             |             | exit             |              |                 |            |
| switch(config)#        |             | do          | show access-list |              |                 |            |
| Type                   | Name        |             |                  |              |                 |            |
| Sequence               | Comment     |             |                  |              |                 |            |
|                        | Action      |             |                  |              | L3 Protocol     |            |
|                        | Source      | IP          | Address          |              | Source          | L4 Port(s) |
|                        | Destination |             | IP               | Address      | Destination     | L4 Port(s) |
|                        | Additional  |             | Parameters       |              |                 |            |
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
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 16

|     | 3 permit |     |     | tcp |     |
| --- | -------- | --- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
|     | dscp: AF11 |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- |
ack
syn
|     | 4 deny |     |     | any |     |
| --- | ------ | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
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
|     | dscp: AF11 |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- |
ack
syn
|     | 4 deny |     |     | any |     |
| --- | ------ | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
CopyingMY_IPV6_ACLtoMY_IPV6_ACL2:
| switch(config)# | access-list | ipv6 | MY_IPV6_ACL | copy | MY_IPV6_ACL2 |
| --------------- | ----------- | ---- | ----------- | ---- | ------------ |
switch(config-acl-ip)#
exit
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
|      | 1 permit    |     |     | udp |     |
any
2001::1/64
|     | 2 Permit       | all TCP ephemeral | ports |        |     |
| --- | -------------- | ----------------- | ----- | ------ | --- |
|     | permit         |                   |       | tcp    |     |
|     | 2001:2001::2:1 |                   |       | > 1023 |     |
any
|     | 3 permit |     |     | tcp |     |
| --- | -------- | --- | --- | --- | --- |
2001:2011::1/64
any
|     | 4 deny |     |     | any |     |
| --- | ------ | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL2 |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- |
|      | 1 permit     |     |     | udp |     |
any
AccessControlLists|17

2001::1/64
|     | 2 Permit all   | TCP ephemeral | ports |        |
| --- | -------------- | ------------- | ----- | ------ |
|     | permit         |               |       | tcp    |
|     | 2001:2001::2:1 |               |       | > 1023 |
any
|     | 3 permit |     |     | tcp |
| --- | -------- | --- | --- | --- |
2001:2011::1/64
any
|     | 4 deny |     |     | any |
| --- | ------ | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
CopyingMY_MAC_ACLtoMY_MAC_ACL2:
| switch(config)#         | access-list | mac MY_MAC_ACL   |     | copy MY_MAC_ACL2 |
| ----------------------- | ----------- | ---------------- | --- | ---------------- |
| switch(config-acl-mac)# |             | exit             |     |                  |
| switch(config)#         | do          | show access-list |     |                  |
| Type                    | Name        |                  |     |                  |
| Sequence                | Comment     |                  |     |                  |
|                         | Action      |                  |     | EtherType        |
|                         | Source MAC  | Address          |     |                  |
|                         | Destination | MAC Address      |     |                  |
|                         | Additional  | Parameters       |     |                  |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |     |      |
| --- | ---------- | --- | --- | ---- |
|     | 1 permit   |     |     | ipv6 |
1122.3344.5566/ffff.ffff.0000
any
|     | 2 permit |     |     | any |
| --- | -------- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS Priority | Code Point:   | 4         |           |
| --- | ------------ | ------------- | --------- | --------- |
|     | 3 Permit all | vlan-1 tagged | Appletalk | traffic   |
|     | permit       |               |           | appletalk |
any
any
|     | VLAN: 1 |     |     |     |
| --- | ------- | --- | --- | --- |
|     | 4 deny  |     |     | any |
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL2 |     |     |      |
| --- | ----------- | --- | --- | ---- |
|     | 1 permit    |     |     | ipv6 |
1122.3344.5566/ffff.ffff.0000
any
|     | 2 permit |     |     | any |
| --- | -------- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS Priority | Code Point:   | 4         |           |
| --- | ------------ | ------------- | --------- | --------- |
|     | 3 Permit all | vlan-1 tagged | Appletalk | traffic   |
|     | permit       |               |           | appletalk |
any
any
|     | VLAN: 1 |     |     |     |
| --- | ------- | --- | --- | --- |
|     | 4 deny  |     |     | any |
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 18

access-list ip

Syntax

Syntax to create an IPv4 ACL and enter its context. Plus syntax to remove an ACL:
access-list ip <ACL-NAME>
no access-list ip <ACL-NAME>

Syntax (within the ACL context) for creating or removing ACEs for protocols ah, gre, esp, igmp, ospf, pim (ip
is available as an alias for any):

[<SEQUENCE-NUMBER>]
{permit|deny}
{any|ip|ah|gre|esp|igmp|ospf|pim|<IP-PROTOCOL-NUM>}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count] [log]

no <SEQUENCE-NUMBER>

Syntax (within the ACL context) for creating or removing ACEs for protocols sctp, tcp, udp:

[<SEQUENCE-NUMBER>]
{permit|deny}
{sctp|tcp|udp}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>|group <PORT-GROUP>]
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>|group <PORT-GROUP>]
[urg] [ack] [psh] [rst] [syn] [fin] [established]
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count] [log]

no <SEQUENCE-NUMBER>

Syntax (within the ACL context) for creating or removing ACEs for protocol icmp:

[<SEQUENCE-NUMBER>]
{permit|deny}
{icmp}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
[icmp-type {echo|echo-reply|<ICMP-TYPE-VALUE>}] [icmp-code <ICMP-CODE-VALUE>]
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count] [log]

no <SEQUENCE-NUMBER>

Syntax (within the ACL context) for ACE comments:
[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

no <SEQUENCE-NUMBER> comment

Description

Creates an IPv4 Access Control List (ACL) comprised of one or more Access Control Entries (ACEs) ordered
and prioritized by sequence number. The lowest sequence number is the highest prioritized ACE.

The no form of this command deletes the entire ACL, or deletes an ACE identified by sequence number, or
deletes only the comment from the ACE identified by sequence number.

Command context

config

The access-list ip <ACL-NAME> command takes you into the named ACL context where you enter the
ACEs.

Access Control Lists | 19

Parameters

<ACL-NAME>

Specifies the name of this ACL.

<SEQUENCE-NUMBER>

Specifies a sequence number for the ACE. Range: 1 to 4294967295.

{permit|deny}

Specifies whether to permit or deny traffic matching this ACE.

<IP-PROTOCOL-NUM>

Specifies the protocol as its Internet Protocol number. For example, 2 corresponds to the IGMP protocol.
Range: 0 to 255.

{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}

Specifies the source IPv4 address.

n any - specifies any source IPv4 address.

n <SRC-IP-ADDRESS> - specifies the source IPv4 host address.

o <PREFIX-LENGTH> - specifies the address bits to mask (CIDR subnet mask notation). Range: 1 to 32.

o <SUBNET-MASK> - specifies the address bits to mask (dotted decimal notation).

n <ADDRESS-GROUP> - specifies an IPv4 address group defined with object-group ip address.

{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}

Specifies the destination IPv4 address.

n any - specifies any destination IPv4 address.

n <DST-IP-ADDRESS> - specifies the destination IPv4 host address.

o <PREFIX-LENGTH> - specifies the address bits to mask (CIDR subnet mask notation). Range: 1 to 32.

o <SUBNET-MASK> - specifies the address bits to mask (dotted decimal notation).

n <ADDRESS-GROUP> - specifies an IPv4 address group that you defined earlier with object-group ip

address.

[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>|group <PORT-GROUP>]

Specifies the port, port range, or port group. Port numbers are in the range of 0 to 65535.

n eq <PORT> - specifies the Layer 4 port.

n gt <PORT> - specifies any Layer 4 port greater than the indicated port.

n lt <PORT> - specifies any Layer 4 port less than the indicated port.

n range <MIN-PORT> <MAX-PORT> - specifies the Layer 4 port range.

n group <PORT-GROUP> - specifies the Layer 4 port group that you defined earlier with object-group

port.

Upon application of the ACL, ACEs with L4 port ranges may consume more than one hardware entry.

urg

Specifies matching on the TCP Flag: Urgent.

ack

Specifies matching on the TCP Flag: Acknowledgment.

psh

Specifies matching on the TCP Flag: Push buffered data to receiving application.

rst

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

20

Specifies matching on the TCP Flag: Reset the connection.

syn

Specifies matching on the TCP Flag: Synchronize sequence numbers.

fin

Specifies matching on the TCP Flag: Finish connection.

established

Specifies matching on the TCP Flag: Established connection.

[icmp-type {echo|echo-reply|<ICMP-TYPE-VALUE>}]

Specifies the ICMP type.

n echo - specifies an ICMP echo request packet.

n echo-reply - specifies an ICMP echo reply packet.

n <ICMP-TYPE-VALUE> - specifies an ICMP type value. Range: 0 to 255.

[icmp-code <ICMP-CODE-VALUE>]

Specifies the ICMP code value. Range: 0 to 255.

dscp DSCP-SPECIFIER>

Specifies the Differentiated Services Code Point (DSCP), either a numeric <DSCP-VALUE> (0 to 63) or one
of these keywords:

n AF11 - DSCP 10 (Assured Forwarding Class 1, low drop probability)

n AF12 - DSCP 12 (Assured Forwarding Class 1, medium drop probability)

n AF13 - DSCP 14 (Assured Forwarding Class 1, high drop probability)

n AF21 - DSCP 18 (Assured Forwarding Class 2, low drop probability)

n AF22 - DSCP 20 (Assured Forwarding Class 2, medium drop probability)

n AF23 - DSCP 22 (Assured Forwarding Class 2, high drop probability)

n AF31 - DSCP 26 (Assured Forwarding Class 3, low drop probability)

n AF32 - DSCP 28 (Assured Forwarding Class 3, medium drop probability)

n AF33 - DSCP 30 (Assured Forwarding Class 3, high drop probability)

n AF41 - DSCP 34 (Assured Forwarding Class 4, low drop probability)

n AF42 - DSCP 36 (Assured Forwarding Class 4, medium drop probability)

n AF43 - DSCP 38 (Assured Forwarding Class 4, high drop probability)

n CS0 - DSCP 0 (Class Selector 0: Default)

n CS1 - DSCP 8 (Class Selector 1: Scavenger)

n CS2 - DSCP 16 (Class Selector 2: OAM)

n CS3 - DSCP 24 (Class Selector 3: Signaling)

n CS4 - DSCP 32 (Class Selector 4: Real time)

n CS5 - DSCP 40 (Class Selector 5: Broadcast video)

n CS6 - DSCP 48 (Class Selector 6: Network control)

n CS7 - DSCP 56 (Class Selector 7)

n EF - DSCP 46 (Expedited Forwarding)

ecn <ECN-VALUE>

Specifies an Explicit Congestion Notification value. Range: 0 to 3.

ip-precedence <IP-PRECEDENCE-VALUE>

Specifies an IP precedence value. Range: 0 to 7.

tos <TOS-VALUE>

Specifies the Type of Service value. Range: 0 to 31.

fragment

Access Control Lists | 21

Specifiesafragmentpacket.
vlan <VLAN-ID>
SpecifiesVLANtagtomatchon.802.1QVLANID.
ThisparametercannotbeusedinanyACLthatwillbeappliedtoaVLAN.
ttl <TTL-VALUE>
Specifiesatime-to-live(hoplimit)value.Range:0to255.NotsupportedforACLs.
count
KeepsthehitcountsofthenumberofpacketsmatchingthisACE.
log
KeepsalogofthenumberofpacketsmatchingthisACE.Workswithboth permitand denyactions.
WorkswithACLsappliedoningressoregress,exceptforcontrolplane.
| [<SEQUENCE-NUMBER>] | comment |     | <TEXT-STRING> |     |     |     |
| ------------------- | ------- | --- | ------------- | --- | --- | --- |
AddsacommenttoanACE.ThenoformremovesonlythecommentfromtheACE.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Ifthe<IP-PROTOCOL-NUM>parameterisusedinsteadofaprotocolname,ensurethatanyneededACE-
n
definitionparametersspecifictotheselectedprotocolarealsoprovided.
WhenusingmultipleACLtypes(IPv4,IPv6,orMAC)withloggingonthesameinterface,thefirstpacket
n
thatmatchesanACEwithlogoptionislogged.Untilthelog-timerwait-periodisover,anypackets
matchingotherACLtypesdonotcreatealog.Attheendofthewait-period,theswitchcreatesa
summarylogforalltheACLsthatwerematched,regardlessoftype.
Examples
CreatinganIPv4ACLwithfourentries:
| switch(config)#        | access-list |     | ip MY_IP_ACL |                   |               |             |
| ---------------------- | ----------- | --- | ------------ | ----------------- | ------------- | ----------- |
| switch(config-acl-ip)# |             | 10  | permit       | udp any           | 172.16.1.0/24 |             |
| switch(config-acl-ip)# |             | 20  | permit       | tcp 172.16.2.0/16 |               | gt 1023 any |
switch(config-acl-ip)# 30 permit tcp 172.26.1.0/24 any syn ack dscp 10
| switch(config-acl-ip)# |             | 40          | deny any | any any | count       |            |
| ---------------------- | ----------- | ----------- | -------- | ------- | ----------- | ---------- |
| switch(config-acl-ip)# |             | exit        |          |         |             |            |
| switch(config)#        | show        | access-list |          |         |             |            |
| Type                   | Name        |             |          |         |             |            |
| Sequence               | Comment     |             |          |         |             |            |
|                        | Action      |             |          |         | L3 Protocol |            |
|                        | Source      | IP Address  |          |         | Source      | L4 Port(s) |
|                        | Destination | IP          | Address  |         | Destination | L4 Port(s) |
|                        | Additional  | Parameters  |          |         |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- | --- |
|      | 10 permit |     |     |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 20 permit              |     |     |     | tcp    |     |
| --- | ---------------------- | --- | --- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     |     |     | > 1023 |     |
any
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 22

|     | 30 permit |     |     |     | tcp |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
|     | dscp: | AF11 |     |     |     |     |     |
| --- | ----- | ---- | --- | --- | --- | --- | --- |
ack
syn
|     | 40 deny |     |     |     | any |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- |
any
any
|     | Hit-counts: |     | enabled |     |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- | --- |
AddingacommenttoanexistingIPv4ACE:
| switch(config)#        |             | access-list | ip          | MY_IP_ACL |                   |            |         |
| ---------------------- | ----------- | ----------- | ----------- | --------- | ----------------- | ---------- | ------- |
| switch(config-acl-ip)# |             |             | 20 comment  | Permit    | all TCP ephemeral |            | ports   |
| switch(config-acl-ip)# |             |             | exit        |           |                   |            |         |
| switch(config)#        |             | show        | access-list |           |                   |            |         |
| Type                   | Name        |             |             |           |                   |            |         |
| Sequence               | Comment     |             |             |           |                   |            |         |
|                        | Action      |             |             |           | L3 Protocol       |            |         |
|                        | Source      | IP          | Address     |           | Source            | L4 Port(s) |         |
|                        | Destination |             | IP Address  |           | Destination       | L4         | Port(s) |
|                        | Additional  |             | Parameters  |           |                   |            |         |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- | --- | --- |
|      | 10 permit |     |     |     | udp |     |     |
any
172.16.1.0/255.255.255.0
|     | 20 Permit              | all | TCP ephemeral | ports |        |     |     |
| --- | ---------------------- | --- | ------------- | ----- | ------ | --- | --- |
|     | permit                 |     |               |       | tcp    |     |     |
|     | 172.16.2.0/255.255.0.0 |     |               |       | > 1023 |     |     |
any
|     | 30 permit |     |     |     | tcp |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
|     | dscp: | AF11 |     |     |     |     |     |
| --- | ----- | ---- | --- | --- | --- | --- | --- |
ack
syn
|     | 40 deny |     |     |     | any |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- |
any
any
|     | Hit-counts: |     | enabled |     |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- | --- |
RemovingacommentfromanexistingIPv4ACE:
| switch(config)#        |             | access-list | ip            | MY_IP_ACL |             |            |         |
| ---------------------- | ----------- | ----------- | ------------- | --------- | ----------- | ---------- | ------- |
| switch(config-acl-ip)# |             |             | no 20 comment |           |             |            |         |
| switch(config-acl-ip)# |             |             | exit          |           |             |            |         |
| switch(config)#        |             | show        | access-list   |           |             |            |         |
| Type                   | Name        |             |               |           |             |            |         |
| Sequence               | Comment     |             |               |           |             |            |         |
|                        | Action      |             |               |           | L3 Protocol |            |         |
|                        | Source      | IP          | Address       |           | Source      | L4 Port(s) |         |
|                        | Destination |             | IP Address    |           | Destination | L4         | Port(s) |
|                        | Additional  |             | Parameters    |           |             |            |         |
-------------------------------------------------------------------------------
AccessControlLists|23

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
|     | 40 deny |     |     | any |     |
| --- | ------- | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
AddinganACE(insertline25)toanexistingIPv4ACL:
| switch(config)#        | access-list | ip        | MY_IP_ACL          |     |     |
| ---------------------- | ----------- | --------- | ------------------ | --- | --- |
| switch(config-acl-ip)# |             | 25 permit | icmp 172.16.2.0/16 |     | any |
switch(config-acl-ip)#
exit
| switch(config)# | show        | access-list |     |             |            |
| --------------- | ----------- | ----------- | --- | ----------- | ---------- |
| Type            | Name        |             |     |             |            |
| Sequence        | Comment     |             |     |             |            |
|                 | Action      |             |     | L3 Protocol |            |
|                 | Source      | IP Address  |     | Source      | L4 Port(s) |
|                 | Destination | IP Address  |     | Destination | L4 Port(s) |
|                 | Additional  | Parameters  |     |             |            |
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
| switch(config)#        | access-list | ip        | MY_IP_ACL          |     |     |
| ---------------------- | ----------- | --------- | ------------------ | --- | --- |
| switch(config-acl-ip)# |             | 25 permit | icmp 172.17.1.0/16 |     | any |
| switch(config-acl-ip)# |             | exit      |                    |     |     |
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 24

| switch(config)# | show        | access-list |             |            |
| --------------- | ----------- | ----------- | ----------- | ---------- |
| Type            | Name        |             |             |            |
| Sequence        | Comment     |             |             |            |
|                 | Action      |             | L3 Protocol |            |
|                 | Source      | IP Address  | Source      | L4 Port(s) |
|                 | Destination | IP Address  | Destination | L4 Port(s) |
|                 | Additional  | Parameters  |             |            |
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
switch(config-acl-ip)#
exit
| switch(config)# | show        | access-list |             |            |
| --------------- | ----------- | ----------- | ----------- | ---------- |
| Type            | Name        |             |             |            |
| Sequence        | Comment     |             |             |            |
|                 | Action      |             | L3 Protocol |            |
|                 | Source      | IP Address  | Source      | L4 Port(s) |
|                 | Destination | IP Address  | Destination | L4 Port(s) |
|                 | Additional  | Parameters  |             |            |
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
AccessControlLists|25

| switch(config)# | access-list |             | ip MY_IP_ACL | copy MY_IP_ACL2 |            |
| --------------- | ----------- | ----------- | ------------ | --------------- | ---------- |
| switch(config)# | show        | access-list |              |                 |            |
| Type            | Name        |             |              |                 |            |
| Sequence        | Comment     |             |              |                 |            |
|                 | Action      |             |              | L3 Protocol     |            |
|                 | Source      | IP Address  |              | Source          | L4 Port(s) |
|                 | Destination | IP Address  |              | Destination     | L4 Port(s) |
|                 | Additional  | Parameters  |              |                 |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- |
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
| switch(config)# | no      | access-list | ip MY_IP_ACL |     |     |
| --------------- | ------- | ----------- | ------------ | --- | --- |
| switch(config)# | show    | access-list |              |     |     |
| Type            | Name    |             |              |     |     |
| Sequence        | Comment |             |              |     |     |
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 26

Action
Source IP Address
Destination IP Address
Additional Parameters

L3 Protocol
Source L4 Port(s)
Destination L4 Port(s)

-------------------------------------------------------------------------------
IPv4

MY_IP_ACL2

1 permit
any
172.16.1.0/255.255.255.0

2 permit

172.16.2.0/255.255.0.0
any
3 permit

172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
4 deny
any
any
Hit-counts: enabled

udp

tcp

> 1023

tcp

any

access-list ipv6

Syntax

Syntax to create an IPv6 ACL and enter its context. Plus syntax to remove an ACL:
access-list ipv6 <ACL-NAME>
no access-list ipv6 <ACL-NAME>

Syntax (within the ACL context) for creating or removing ACEs for protocols ah, gre, esp, ospf, pim (ipv6 is
available as an alias for any):
[<SEQUENCE-NUMBER>]
{permit|deny}
{any|ipv6|ah|gre|esp|ospf|pim|<IP-PROTOCOL-NUM>}
{any|<SRC-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}
{any|<DST-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count] [log]

no <SEQUENCE-NUMBER>

Syntax (within the ACL context) for creating or removing ACEs for protocols sctp, tcp, udp:

[<SEQUENCE-NUMBER>]
{permit|deny}
{sctp|tcp|udp}
{any|<SRC-IP-ADDRESS>[/<PREFIX-LENGTH>}]|<ADDRESS-GROUP>}
[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>|group <PORT-GROUP>]
{any|<DST-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}
[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>|group <PORT-GROUP>]
[urg] [ack] [psh] [rst] [syn] [fin] [established]
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count] [log]

no <SEQUENCE-NUMBER>

Syntax (within the ACL context) for creating or removing ACEs for protocol icmpv6:

[<SEQUENCE-NUMBER>]
{permit|deny}
{icmpv6}
{any|<SRC-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}
{any|<DST-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}
[icmp-type {echo|echo-reply|<ICMP-TYPE-VALUE>}] [icmp-code <ICMP-CODE-VALUE>]

Access Control Lists | 27

[dscp <DSCP-SPECIFIER>][ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count] [log]

no <SEQUENCE-NUMBER>

Syntax (within the ACL context) for ACE comments:
[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

no <SEQUENCE-NUMBER> comment

Description

Creates an IPv6 Access Control List (ACL). The ACL is made of one or more Access Control Entries (ACEs)
ordered and prioritized by sequence number. The lowest sequence number is the highest prioritized ACE.

The no form of this command deletes the entire ACL, or deletes an ACE identified by sequence number, or
deletes only the comment from the ACE identified by sequence number.

Command context

config

The access-list ipv6 <ACL-NAME> command takes you into the named ACL context where you enter the
ACEs.

Parameters

<ACL-NAME>

Specifies the name of this ACL.

<SEQUENCE-NUMBER>

Specifies a sequence number for the ACE. Range: 1 to 4294967295.

{permit|deny}

Specifies whether to permit or deny traffic matching this ACE.

<IP-PROTOCOL-NUM>

Specifies the protocol as its Internet Protocol number. For example, 2 corresponds to the IGMP protocol.
Range: 0 to 255.

{any|<SRC-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}

Specifies the source IPv6 address.

n any - specifies any source IPv6 address.

n <SRC-IP-ADDRESS> - specifies the source IPv6 host address.

o <PREFIX-LENGTH> - specifies the address bits to mask (CIDR subnet mask notation). Range: 1 to

128.

n <ADDRESS-GROUP> - specifies an IPv6 address group that you defined earlier with object-group ipv6

address.

{any|<DST-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}

Specifies the destination IPv6 address.

n any - specifies any destination IPv6 address.

n <DST-IP-ADDRESS> - specifies the destination IPv6 host address.

o <PREFIX-LENGTH> - specifies the address bits to mask (CIDR subnet mask notation). Range: 1 to

128.

n <ADDRESS-GROUP> - specifies an IPv6 address group that you defined earlier with object-group ipv6

address.

[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>|group <PORT-GROUP>]

Specifies the port, port range, or port group. Port numbers are in the range of 0 to 65535.

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

28

n eq <PORT> - specifies the Layer 4 port.

n gt <PORT> - specifies any Layer 4 port greater than the indicated port.

n lt <PORT> - specifies any Layer 4 port less than the indicated port.

n range <MIN-PORT> <MAX-PORT> - specifies the Layer 4 port range.

n group <PORT-GROUP> - specifies the Layer 4 port group that you defined earlier with object-group

port.

Upon application of the ACL, ACEs with L4 port ranges may consume more than one hardware entry.

urg, ack, psh, rst, syn, fin, established

These TCP flag-matching parameters are supported for both ingress and egress.

[icmp-type {echo|echo-reply|<ICMP-TYPE-VALUE>}]

Specifies the ICMP type.

n echo - specifies an ICMP echo request packet.

n echo-reply - specifies an ICMP echo reply packet.

n <ICMP-TYPE-VALUE> - specifies an ICMP type value. Range: 0 to 255.

[icmp-code <ICMP-CODE-VALUE>]

Specifies the ICMP code value. Range: 0 to 255.

dscp <DSCP-SPECIFIER>

Specifies the Differentiated Services Code Point (DSCP), either a numeric <DSCP-VALUE> (0 to 63) or one
of these keywords:

n AF11 - DSCP 10 (Assured Forwarding Class 1, low drop probability)

n AF12 - DSCP 12 (Assured Forwarding Class 1, medium drop probability)

n AF13 - DSCP 14 (Assured Forwarding Class 1, high drop probability)

n AF21 - DSCP 18 (Assured Forwarding Class 2, low drop probability)

n AF22 - DSCP 20 (Assured Forwarding Class 2, medium drop probability)

n AF23 - DSCP 22 (Assured Forwarding Class 2, high drop probability)

n AF31 - DSCP 26 (Assured Forwarding Class 3, low drop probability)

n AF32 - DSCP 28 (Assured Forwarding Class 3, medium drop probability)

n AF33 - DSCP 30 (Assured Forwarding Class 3, high drop probability)

n AF41 - DSCP 34 (Assured Forwarding Class 4, low drop probability)

n AF42 - DSCP 36 (Assured Forwarding Class 4, medium drop probability)

n AF43 - DSCP 38 (Assured Forwarding Class 4, high drop probability)

n CS0 - DSCP 0 (Class Selector 0: Default)

n CS1 - DSCP 8 (Class Selector 1: Scavenger)

n CS2 - DSCP 16 (Class Selector 2: OAM)

n CS3 - DSCP 24 (Class Selector 3: Signaling)

n CS4 - DSCP 32 (Class Selector 4: Real time)

n CS5 - DSCP 40 (Class Selector 5: Broadcast video)

n CS6 - DSCP 48 (Class Selector 6: Network control)

n CS7 - DSCP 56 (Class Selector 7)

n EF - DSCP 46 (Expedited Forwarding)

ecn <ECN-VALUE>

Specifies an Explicit Congestion Notification value. Range: 0- 3.

Access Control Lists | 29

| ip-precedence | <IP-PRECEDENCE-VALUE> |     |     |     |     |     |
| ------------- | --------------------- | --- | --- | --- | --- | --- |
SpecifiesanIPprecedencevalue.Range:0-7.
tos <TOS-VALUE>
SpecifiestheTypeofServicevalue.Range:0-31.
fragment
Specifiesafragmentpacket.
vlan <VLAN-ID>
SpecifiesVLANtagtomatchon.802.1QVLANID.
ThisparametercannotbeusedinanyACLthatwillbeappliedtoaVLAN.
ttl <TTL-VALUE>
Notsupported.
count
KeepsthehitcountsofthenumberofpacketsmatchingthisACE.
log
KeepsalogofthenumberofpacketsmatchingthisACE.Workswithbothpermitanddenyactions.
WorkswithACLsappliedoningressoregress,exceptforcontrolplane.
| [<SEQUENCE-NUMBER>] | comment |     | <TEXT-STRING> |     |     |     |
| ------------------- | ------- | --- | ------------- | --- | --- | --- |
AddsacommenttoanACE.ThenoformremovesonlythecommentfromtheACE.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Ifthe<IP-PROTOCOL-NUM>parameterisusedinsteadofaprotocolname,ensurethatanyneededACE-
n
definitionparametersspecifictotheselectedprotocolarealsoprovided.
n WhenusingmultipleACLtypes(IPv4,IPv6,orMAC)withloggingonthesameinterface,thefirstpacket
thatmatchesanACEwithlogoptionislogged.Untilthelog-timerwait-periodisover,anypackets
matchingotherACLtypesdonotcreatealog.Attheendofthewait-period,theswitchcreatesa
summarylogalltheACLsthatwerematched,regardlessoftype.
Examples
CreatinganIPv6ACLwithfourentries:
| switch(config)#          | access-list |     | ipv6      | MY_IPV6_ACL |            |     |
| ------------------------ | ----------- | --- | --------- | ----------- | ---------- | --- |
| switch(config-acl-ipv6)# |             |     | 10 permit | udp any     | 2001::1/64 |     |
switch(config-acl-ipv6)# 20 permit tcp 2001:2001::2:1/128 gt 1023 any
| switch(config-acl-ipv6)# |             |                  | 30 permit | tcp 2001:2011::1/64 |             | any        |
| ------------------------ | ----------- | ---------------- | --------- | ------------------- | ----------- | ---------- |
| switch(config-acl-ipv6)# |             |                  | 40 deny   | any any             | any count   |            |
| switch(config-acl-ipv6)# |             |                  | exit      |                     |             |            |
| switch(config)#          | do          | show access-list |           |                     |             |            |
| Type                     | Name        |                  |           |                     |             |            |
| Sequence                 | Comment     |                  |           |                     |             |            |
|                          | Action      |                  |           |                     | L3 Protocol |            |
|                          | Source      | IP Address       |           |                     | Source      | L4 Port(s) |
|                          | Destination | IP               | Address   |                     | Destination | L4 Port(s) |
|                          | Additional  | Parameters       |           |                     |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- |
|      | 10 permit   |     |     |     | udp |     |
any
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 30

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
AddingacommenttoanexistingIPv6ACE:
| switch(config)# |     | access-list | ipv6 | MY_IPV6_ACL |     |
| --------------- | --- | ----------- | ---- | ----------- | --- |
switch(config-acl-ipv6)# 20 comment Permit all TCP ephemeral ports
| switch(config-acl-ipv6)# |             |                     | exit    |             |            |
| ------------------------ | ----------- | ------------------- | ------- | ----------- | ---------- |
| switch(config)#          |             | do show access-list |         |             |            |
| Type                     | Name        |                     |         |             |            |
| Sequence                 | Comment     |                     |         |             |            |
|                          | Action      |                     |         | L3 Protocol |            |
|                          | Source      | IP Address          |         | Source      | L4 Port(s) |
|                          | Destination | IP                  | Address | Destination | L4 Port(s) |
|                          | Additional  | Parameters          |         |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- |
|      | 10 permit   |     |     | udp |     |
any
2001::1/64
|     | 20 Permit      | all TCP | ephemeral | ports  |     |
| --- | -------------- | ------- | --------- | ------ | --- |
|     | permit         |         |           | tcp    |     |
|     | 2001:2001::2:1 |         |           | > 1023 |     |
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
RemovingacommentfromanexistingIPv6ACE:
| switch(config)#          |             | access-list         | ipv6          | MY_IPV6_ACL |            |
| ------------------------ | ----------- | ------------------- | ------------- | ----------- | ---------- |
| switch(config-acl-ipv6)# |             |                     | no 20 comment |             |            |
| switch(config-acl-ipv6)# |             |                     | exit          |             |            |
| switch(config)#          |             | do show access-list |               |             |            |
| Type                     | Name        |                     |               |             |            |
| Sequence                 | Comment     |                     |               |             |            |
|                          | Action      |                     |               | L3 Protocol |            |
|                          | Source      | IP Address          |               | Source      | L4 Port(s) |
|                          | Destination | IP                  | Address       | Destination | L4 Port(s) |
|                          | Additional  | Parameters          |               |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- |
|      | 10 permit   |     |     | udp |     |
any
AccessControlLists|31

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
| switch(config)#          | access-list | ipv6             | MY_IPV6_ACL         |            |
| ------------------------ | ----------- | ---------------- | ------------------- | ---------- |
| switch(config-acl-ipv6)# |             | 25 permit        | icmpv6 2001::2:1/64 | any        |
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
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 32

|     | 10 permit |     |     | udp |     |
| --- | --------- | --- | --- | --- | --- |
any
2001::1/64
|     | 20 permit      |     |     | tcp    |     |
| --- | -------------- | --- | --- | ------ | --- |
|     | 2001:2001::2:1 |     |     | > 1023 |     |
any
|     | 25 permit |     |     | icmpv6 |     |
| --- | --------- | --- | --- | ------ | --- |
2001::2:1/64
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
RemovinganACEfromanIPv6ACL:
| switch(config)#          | access-list |                  | ipv6 MY_IPV6_ACL |             |            |
| ------------------------ | ----------- | ---------------- | ---------------- | ----------- | ---------- |
| switch(config-acl-ipv6)# |             | no               | 25               |             |            |
| switch(config-acl-ipv6)# |             | exit             |                  |             |            |
| switch(config)#          | do          | show access-list |                  |             |            |
| Type                     | Name        |                  |                  |             |            |
| Sequence                 | Comment     |                  |                  |             |            |
|                          | Action      |                  |                  | L3 Protocol |            |
|                          | Source      | IP Address       |                  | Source      | L4 Port(s) |
|                          | Destination | IP Address       |                  | Destination | L4 Port(s) |
|                          | Additional  | Parameters       |                  |             |            |
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
AccessControlLists|33

1 permit
any
2001::1/64

2 Permit all TCP ephemeral ports

permit
2001:2001::2:1
any
3 permit

2001:2011::1/64
any
4 deny
any
any
Hit-counts: enabled

udp

tcp

> 1023

tcp

any

access-list log-timer

Syntax

access-list log-timer {default|<INTERVAL>}

Description

Sets the log timer interval for all ACEs that have the log parameter configured.

Command context

config

Parameters

default

Resets the log timer to its default 300 seconds.

<INTERVAL>

Specifies the log timer interval in seconds. Range: 30 to 300.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n ACL logging keeps a log of the number of packets matching this ACE. Works with both permit and deny

actions. Works with ACLs applied on ingress or egress, except for control plane.

n The first packet that matches an ACE with the log parameter within an ACL log timer window (configured

with the access-list log-timer command) has its header contents extracted and sent to the
configured logging destination, such as the console and syslog server. Each time the ACL log timer
expires, a summary of all ACEs with log configured are sent to the logging destination. This capability
allows throttling of logging ACL hits.

n If no further log messages are generated in the wait-period, the switch suspends the timer and resets

itself to log as soon as a new match occurs.

n When using multiple ACL types (IPv4, IPv6, or MAC) with logging on the same interface, the first packet

that matches an ACE with the log option is logged. Any packets, matching other ACL types, do not create
a log until the log-timer wait-period is over. At the end of the wait-period, a summary log is made of all
the ACLs that were matched, regardless of type.

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

34

Remarked ACL traffic may lose logging information when a QoS action or a classifier policy with remark is

enabled. A classifier policy with remark takes precedence over QoS actions and QoS actions takes precedence

over ACL remarked traffic.

n You may see a minor discrepancy between the ACL logging statistics and the hit counts statistics due to

the time required to record the log message.

Examples

Although these examples use debug logging, you can alternatively use event logging.

On the 6400 Switch Series, interface identification differs.

Enabling debug logging for the ACL logging module:

switch# debug acl log severity info
switch# show debug
----------------------------------------------------------------
mac instance vrf
module sub_module severity vlan port
----------------------------------------------------------------
---
acl

----- ----- ----- ---- -----

acl_log

info

ip

Setting the debug destination to console with the minimum security level of info:

switch# debug destination console severity info
switch# show debug destination
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

1.1.1.1
1.1.1.2

icmp

Access Control Lists | 35

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

2017-10-10T20:13:36.044+00:00 ops-switchd[875]: debug|LOG_INFO|AMM|1/5|ACL|ACL_LOG|
List MY_IP_ACL, seq# 10 denied icmp 1.1.1.1 -> 1.1.1.2 type 8 code 0,
on vlan 1, port 1/1/1, direction in

When the access list log-timer expires, the summary message is printed on the console. The number 30 is
the number of packets received during the last access list log-timer window.

2017-10-10T20:14:06.051+00:00 ops-switchd[875]: debug|LOG_INFO|AMM|1/5|ACL|ACL_LOG|
MY_IP_ACL on 1/1/1 (in): 30 10 deny icmp 1.1.1.1 1.1.1.2 log count

Resetting the ACL log timer to the default value:

switch(config)# access-list log-timer default

access-list mac

Syntax

access-list mac <ACL-NAME>
no access-list mac <ACL-NAME>

[<SEQUENCE-NUMBER>]
{permit|deny}
{any|<SRC-MAC-ADDRESS>[/<ETHERNET-MASK>}]}
{any|<DST-MAC-ADDRESS>[/<ETHERNET-MASK>}]}
{any|aarp|appletalk|arp|fcoe|fcoe-init|ip|ipv6|

ipx-arpa|ipx-non-arpa|is-is|lldp|mpls-multicast|mpls-unicast|q-in-q|
rbridge|trill|wake-on-lan|<NUMERIC-ETHERTYPE>}

[pcp <PCP-VALUE>] [vlan <VLAN-ID>] [count] [log]
no <SEQUENCE-NUMBER>

[<SEQUENCE-NUMBER>] comment <TEXT-STRING>
no <SEQUENCE-NUMBER> comment

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

36

Description

Creates a MAC Access Control List (ACL). The ACL is made of one or more Access Control Entries (ACEs)
ordered and prioritized by sequence numbers. The lowest sequence number is the highest prioritized ACE.

The no form of this command deletes the entire ACL, or deletes an ACE identified by sequence number, or
deletes only the comment from the ACE identified by sequence number.

Command context

config

The access-list mac <ACL-NAME> command takes you into the named ACL context where you enter the
ACEs.

Parameters

<ACL-NAME>

Specifies the name of this ACL.

<SEQUENCE-NUMBER>

Specifies a sequence number for the ACE. Range: 1 to 4294967295.

{permit|deny}

Specifies whether to permit or deny traffic matching this ACE.

comment

Specifies storing the remaining entered text as an ACE comment.

{any|<SRC-MAC-ADDRESS>[/<ETHERNET-MASK>}]}

Specifies the source host MAC address (xxxx.xxxx.xxxx), OUI, or the keyword any. You can optionally
include the following:

<ETHERNET-MASK> - The address bits to mask (xxxx.xxxx.xxxx).

{any|<DST-MAC-ADDRESS>[/<ETHERNET-MASK>}]}

Specifies the destination host MAC address (xxxx.xxxx.xxxx), OUI, or the keyword any. You can
optionally include the following:

<ETHERNET-MASK> - The address bits to mask (xxxx.xxxx.xxxx).
{any|aarp|appletalk| ... |wake-on-lan|<NUMERIC-ETHERTYPE>

Specifics the protocol encapsulated in the Ethernet frame. The encapsulated protocol is identified by the
EtherType Ethernet field. The EtherType is specified in one of the following three ways:

n any - any EtherType.

n <NUMERIC-ETHERTYPE> - the numerical EtherType protocol number. Range: 0x600 to 0xffff.

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

Access Control Lists | 37

o mpls-unicast
o q-in-q
o
rbridge
o trill
o wake-on-lan
pcp <PCP-VALUE>
Specifies802.1QQoSPriorityCodePointvalue.Range:0to7.
vlan <VID>
SpecifiesaVLANID.TheVLANIDmustexist.
ThisparametercannotbeusedinanyACLthatwillbeappliedtoaVLAN.
count
KeepsthehitcountsofthenumberofpacketsmatchingthisACE.
log
KeepsalogofthenumberofpacketsmatchingthisACE.Workswithbothpermitanddenyactions.
WorkswithACLsappliedoningressoregress.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
WhenusingmultipleACLtypes(IPv4,IPv6,orMAC)withloggingonthesameinterface,thefirstpacketthat
matchesanACEwithlogoptionislogged.Untilthelog-timerwait-periodisover,anypacketsmatching
otherACLtypesdonotcreatealog.Attheendofthewait-period,theswitchcreatesasummarylogallthe
ACLsthatwerematched,regardlessoftype.
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
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 38

|     | 30 permit |     |     |     |     | appletalk |     |     |
| --- | --------- | --- | --- | --- | --- | --------- | --- | --- |
any
any
|     | VLAN:   | 40  |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- |
|     | 40 deny |     |     |     |     | any |     |     |
any
any
|     | Hit-counts: |     | enabled |     |     |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- | --- | --- |
AddingacommenttoanexistingMACACE:
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
AccessControlLists|39

20 permit any
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS Priority | Code Point: | 4   |     |
| --- | ------------ | ----------- | --- | --- |
30 permit appletalk
any
any
VLAN: 1
40 deny any
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
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
| switch(config)#        | access-list | mac       | MY_MAC_ACL         |        |
| ---------------------- | ----------- | --------- | ------------------ | ------ |
| switch(config-acl-ip)# |             | 35 permit | any aabb.cc11.1234 | 0xeeee |
| switch(config-acl-ip)# |             | exit      |                    |        |
switch(config)#
|          | do show | access-list |     |     |
| -------- | ------- | ----------- | --- | --- |
| Type     | Name    |             |     |     |
| Sequence | Comment |             |     |     |
Action EtherType
|     | Source MAC  | Address     |     |     |
| --- | ----------- | ----------- | --- | --- |
|     | Destination | MAC Address |     |     |
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 40

|     | Additional | Parameters |     |
| --- | ---------- | ---------- | --- |
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
|     | 35 permit |     | 0xeeee |
| --- | --------- | --- | ------ |
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
AccessControlLists|41

| Sequence | Comment     |     |             |           |     |
| -------- | ----------- | --- | ----------- | --------- | --- |
|          | Action      |     |             | EtherType |     |
|          | Source      | MAC | Address     |           |     |
|          | Destination |     | MAC Address |           |     |
|          | Additional  |     | Parameters  |           |     |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL2 |     |     |      |     |
| --- | ----------- | --- | --- | ---- | --- |
|     | 1 permit    |     |     | ipv6 |     |
1122.3344.5566/ffff.ffff.0000
any
|     | 2 permit |     |     | any |     |
| --- | -------- | --- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS      | Priority | Code Point:    | 4         |         |
| --- | -------- | -------- | -------------- | --------- | ------- |
|     | 3 Permit | all      | vlan-40 tagged | Appletalk | traffic |
|     | permit   |          |                | appletalk |         |
any
any
|     | VLAN:  | 1   |     |     |     |
| --- | ------ | --- | --- | --- | --- |
|     | 4 deny |     |     | any |     |
any
any
|             | Hit-counts: |     | enabled |     |     |
| ----------- | ----------- | --- | ------- | --- | --- |
| access-list | resequence  |     |         |     |     |
Syntax
access-list {ip|ipv6|mac} <ACL-NAME> resequence <STARTING-SEQUENCE-NUMBER> <INCREMENT>
Description
ResequencestheACEsequencenumbersinanACL.
Commandcontext
config
Parameters
{ip|ipv6|mac}
SpecifiestheACLtype.
<ACL-NAME>
SpecifiestheACLname.
<STARTING-SEQUENCE-NUMBER>
Specifiesthestartingsequencenumber.
<INCREMENT>
Specifiesthesequencenumberincrement.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ResequencinganIPv4ACLtostartat1withanincrementof1:
| switch(config)#        |     | access-list | ip MY_IP_ACL | resequence | 1 1 |
| ---------------------- | --- | ----------- | ------------ | ---------- | --- |
| switch(config-acl-ip)# |     |             | exit         |            |     |
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 42

switch(config)#
|          | do          | show access-list |     |             |            |
| -------- | ----------- | ---------------- | --- | ----------- | ---------- |
| Type     | Name        |                  |     |             |            |
| Sequence | Comment     |                  |     |             |            |
|          | Action      |                  |     | L3 Protocol |            |
|          | Source      | IP Address       |     | Source      | L4 Port(s) |
|          | Destination | IP Address       |     | Destination | L4 Port(s) |
|          | Additional  | Parameters       |     |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- |
|      | 1 permit  |     |     | udp |     |
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
|     | dscp: AF11 |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- |
ack
syn
|     | 4 deny |     |     | any |     |
| --- | ------ | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
ResequencinganIPv6ACLtostartat1withanincrementof1:
| switch(config)#        | access-list | ipv6 | MY_IPV6_ACL | resequence | 1 1 |
| ---------------------- | ----------- | ---- | ----------- | ---------- | --- |
| switch(config-acl-ip)# |             | exit |             |            |     |
switch(config)#
|          | do          | show access-list |     |             |            |
| -------- | ----------- | ---------------- | --- | ----------- | ---------- |
| Type     | Name        |                  |     |             |            |
| Sequence | Comment     |                  |     |             |            |
|          | Action      |                  |     | L3 Protocol |            |
|          | Source      | IP Address       |     | Source      | L4 Port(s) |
|          | Destination | IP Address       |     | Destination | L4 Port(s) |
|          | Additional  | Parameters       |     |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- |
|      | 1 permit    |     |     | udp |     |
any
2001::1/64
|     | 2 Permit       | all TCP ephemeral | ports |        |     |
| --- | -------------- | ----------------- | ----- | ------ | --- |
|     | permit         |                   |       | tcp    |     |
|     | 2001:2001::2:1 |                   |       | > 1023 |     |
any
|     | 3 permit |     |     | tcp |     |
| --- | -------- | --- | --- | --- | --- |
2001:2011::1/64
any
|     | 4 deny |     |     | any |     |
| --- | ------ | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
ResequencingaMACACLtostartat1withanincrementof1:
AccessControlLists|43

| switch(config)# |     | access-list | mac | MY_MAC_ACL | resequence | 1 1 |
| --------------- | --- | ----------- | --- | ---------- | ---------- | --- |
switch(config-acl-mac)#
exit
| switch(config)# |             | do show | access-list |     |           |     |
| --------------- | ----------- | ------- | ----------- | --- | --------- | --- |
| Type            | Name        |         |             |     |           |     |
| Sequence        | Comment     |         |             |     |           |     |
|                 | Action      |         |             |     | EtherType |     |
|                 | Source      | MAC     | Address     |     |           |     |
|                 | Destination |         | MAC Address |     |           |     |
|                 | Additional  |         | Parameters  |     |           |     |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |     |     |      |     |
| --- | ---------- | --- | --- | --- | ---- | --- |
|     | 1 permit   |     |     |     | ipv6 |     |
1122.3344.5566/ffff.ffff.0000
any
|     | 2 permit |     |     |     | any |     |
| --- | -------- | --- | --- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS      | Priority | Code Point:    | 4         |           |     |
| --- | -------- | -------- | -------------- | --------- | --------- | --- |
|     | 3 Permit | all      | vlan-40 tagged | Appletalk | traffic   |     |
|     | permit   |          |                |           | appletalk |     |
any
any
|     | VLAN:  | 1   |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- |
|     | 4 deny |     |     |     | any |     |
any
any
|             | Hit-counts: |     | enabled |     |     |     |
| ----------- | ----------- | --- | ------- | --- | --- | --- |
| access-list | reset       |     |         |     |     |     |
Syntax
access-list {all|ip <ACL-NAME>|ipv6 <ACL-NAME>|mac <ACL-NAME>} reset
Description
Changestheuser-specifiedACLconfigurationtomatchtheactiveACLconfiguration.Usethiscommand
whenadiscrepancyexistsbetweenwhattheuserconfiguredandwhatisactiveandacceptedbythesystem.
Commandcontext
config
Parameters
| all|ip ACL-NAME>|ipv6 |     |     | <ACL-NAME>|mac | <ACL-NAME> |     |     |
| --------------------- | --- | --- | -------------- | ---------- | --- | --- |
Specifiesoneofthefollowing:
aresetofallACLs.
n
n aresetofanamedIPv4ACL.
n aresetofanamedIPv6ACL.
n aresetofanamedMACACL.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 44

Theoutputoftheshow access-listcommanddisplaystheactiveconfigurationoftheproduct.Theactive
configurationistheACLsthathavebeenconfiguredandacceptedbythesystem.Theoutputoftheshow
access-listcommandwiththeconfigurationparameter,displaystheACLsthathavebeenconfigured.
Theoutputofthiscommandmaynotbethesameaswhatwasprogrammedinhardwareorwhatisactive
ontheproduct.
IftheactiveACLsanduser-configuredACLsarenotthesame,awarningmessageisdisplayedintheoutput
oftheshowcommand.Modifytheuser-configuredACLuntilthewarningmessageisnolongerdisplayedor
runtheaccess-list resetcommandtochangetheuser-specifiedconfigurationtomatchtheactive
configuration.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ApplyanACLwithTCPacknowledgments(ACKs)oningress,whichisunsupportedbyhardware:
| switch(config-acl)# |     | 10 permit | tcp | 172.16.2.0/16 | any | ack |
| ------------------- | --- | --------- | --- | ------------- | --- | --- |
Displayingtheuser-specifiedconfiguration:
| switch(config)# | do  | show access-list |     | commands |     |     |
| --------------- | --- | ---------------- | --- | -------- | --- | --- |
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| access-list | ip TEST_ACL |     |     |     |     |     |
| ----------- | ----------- | --- | --- | --- | --- | --- |
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| interface       | 1/1/1       |                  |     |          |               |     |
| --------------- | ----------- | ---------------- | --- | -------- | ------------- | --- |
| apply           | access-list | ip TEST_ACL      |     | in       |               |     |
| switch(config)# | do          | show access-list |     | commands | configuration |     |
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| access-list | ip TEST_ACL |                        |     |     |         |     |
| ----------- | ----------- | ---------------------- | --- | --- | ------- | --- |
| 10 permit   | tcp         | 172.16.2.0/255.255.0.0 |     |     | any ack |     |
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| interface       | 1/1/1       |                  |     |     |             |            |
| --------------- | ----------- | ---------------- | --- | --- | ----------- | ---------- |
| apply           | access-list | ip TEST_ACL      |     | in  |             |            |
| switch(config)# | do          | show access-list |     |     |             |            |
| Type            | Name        |                  |     |     |             |            |
| Sequence        | Comment     |                  |     |     |             |            |
|                 | Action      |                  |     |     | L3 Protocol |            |
|                 | Source      | IP Address       |     |     | Source      | L4 Port(s) |
|                 | Destination | IP Address       |     |     | Destination | L4 Port(s) |
|                 | Additional  | Parameters       |     |     |             |            |
-------------------------------------------------------------------------------
% Warning: TEST_ACL user configuration does not match active configuration.
% run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| IPv4            | TEST_ACL |                  |     |               |     |     |
| --------------- | -------- | ---------------- | --- | ------------- | --- | --- |
| switch(config)# | do       | show access-list |     | configuration |     |     |
| Type            | Name     |                  |     |               |     |     |
| Sequence        | Comment  |                  |     |               |     |     |
AccessControlLists|45

|     | Action      |            |         |     | L3 Protocol |            |
| --- | ----------- | ---------- | ------- | --- | ----------- | ---------- |
|     | Source      | IP Address |         |     | Source      | L4 Port(s) |
|     | Destination | IP         | Address |     | Destination | L4 Port(s) |
|     | Additional  | Parameters |         |     |             |            |
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
-------------------------------------------------------------------------------
| IPv4              | TEST_ACL |               |     |     |     |     |
| ----------------- | -------- | ------------- | --- | --- | --- | --- |
| apply access-list |          | control-plane |     |     |     |     |
Syntax
apply access-list {ip|ipv6} <ACL-NAME> control-plane vrf <VRF-NAME>
no apply access-list {ip|ipv6} <ACL-NAME> control-plane vrf <VRF-NAME>
Description
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 46

Applies an ACL to the specified VRF.

The no form of this command removes application of the ACL from the specified VRF.

Command context

config

Parameters

ip|ipv6

Specifies the ACL type: ip for IPv4, oripv6 for IPv6.

<ACL-NAME>

Specifies the ACL name.

vrf <VRF-NAME>

Specifies the VRF name.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Only one ACL per type (ip, or ipv6) may be applied to a control plane VRF at a time. Therefore, using the
apply access-list control-plane command on a VRF with an already-applied ACL of the same type, will
replace the applied ACL.

Examples

Applying My_ip_ACL to control plane traffic on the default VRF:

switch(config)# apply access-list ip My_ip_ACL control-plane vrf default

Replacing My_ip_ACL with My_Replacement_ACL on the default VRF:

switch(config)# apply access-list ip My_Replacement_ACL control-plane vrf default

Remove (unapply) the My_Replacement_ACL from the default VRF. Any other interfaces or VLANs with My_
Replacement_ACL applied are unaffected.

switch(config)# no apply access-list ip My_Replacement_ACL control-plane vrf default

apply access-list (to interface or LAG)

Syntax

apply access-list {ip | ipv6 | mac} <ACL-NAME> {in | out}
no apply access-list {ip | ipv6 | mac} <ACL-NAME> {in | out}

Description

Applies an ACL to the interface (Individual front plane port) or Link Aggregation Group (LAG) identified by
the current interface or LAG context.

The no form of this command removes application of the ACL from the current interface or LAG identified
by the current interface or LAG context.

Access Control Lists | 47

Command context

config-if
config-lag-if

Parameters

ip|ipv6|mac

Specifies the ACL type: ip for IPv4, ipv6 for IPv6, or mac for MAC ACL.

<ACL-NAME>

Specifies the ACL name.

in

Selects the inbound (ingress) traffic direction.

out

Selects the outbound (egress) traffic direction.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n Each ACL of a given type can be applied to the same interface or LAG once in each direction. Therefore,

using the apply access-list command on an interface or LAG with an already-applied ACL of the same
type and direction will replace the currently applied ACL.

n An ACL can be applied to an individual front plane port or to a Link Aggregation Group (LAG).

n A port that is a member of a LAG with an applied ACL cannot have a different ACL applied to that

member port.

n When the port membership of a LAG with an applied ACL is changed, the LAG ACL is automatically

applied or removed from that port depending on the modification type.

Examples

On the 6400 Switch Series, interface identification differs.

Applying My_IP_ACL to ingress traffic on interface range 1/1/10 to 1/1/12:

switch(config)# int 1/1/10-1/1/12
switch((config-if-<1/1/10-1/1/12>)# apply access-list ip My_IP_ACL in
switch((config-if-<1/1/10-1/1/12>)# exit

Applying MY_IP_ACL to ingress traffic on LAG 100 and egress traffic on interface 1/1/2:

switch(config)# interface lag 100
switch(config-lag-if)# apply access-list ip MY_IP_ACL in
switch(config-lag-if)# exit

switch(config)# interface 1/1/2
switch(config-if)# apply access-list ip MY_IP_ACL out
switch(config-if)# exit
switch(config)#

Applying MY_IPV6_ACL to ingress traffic on interface 1/1/1 and to ingress traffic on LAG 100:

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

48

| switch(config)# | interface | 1/1/1 |     |     |     |     |
| --------------- | --------- | ----- | --- | --- | --- | --- |
switch(config-if)#
|                        | apply     | access-list       | ipv6 | MY_IPV6_ACL      | in  |     |
| ---------------------- | --------- | ----------------- | ---- | ---------------- | --- | --- |
| switch(config-if)#     | exit      |                   |      |                  |     |     |
| switch(config)#        | interface | lag 100           |      |                  |     |     |
| switch(config-lag-if)# |           | apply access-list |      | ipv6 MY_IPV6_ACL |     | in  |
| switch(config-lag-if)# |           | exit              |      |                  |     |     |
switch(config)#
ApplyingMY_MAC_ACLtoingresstrafficoninterface1/1/1andingresstrafficoninterface1/1/2:
| switch(config)# | interface | 1/1/1 |     |     |     |     |
| --------------- | --------- | ----- | --- | --- | --- | --- |
switch(config-if)#
|                    | apply     | access-list | mac | MY_MAC_ACL | in  |     |
| ------------------ | --------- | ----------- | --- | ---------- | --- | --- |
| switch(config-if)# | exit      |             |     |            |     |     |
| switch(config)#    | interface | 1/1/2       |     |            |     |     |
| switch(config-if)# | apply     | access-list | mac | MY_MAC_ACL | in  |     |
| switch(config-if)# | exit      |             |     |            |     |     |
switch(config)#
ReplacingMY_IP_ACLwithMY_REPLACEMENT_ACLoninterface1/1/2:
| switch(config)# | interface | 1/1/2 |     |     |     |     |
| --------------- | --------- | ----- | --- | --- | --- | --- |
switch(config-if)#
|                    | apply | access-list | ip  | MY_REPLACEMENT_ACL |     | out |
| ------------------ | ----- | ----------- | --- | ------------------ | --- | --- |
| switch(config-if)# | exit  |             |     |                    |     |     |
switch(config)#
UnapplyingMY_REPLACEMENT_ACLfrominterface1/1/2(out):
| switch(config)# | interface | 1/1/2 |     |     |     |     |
| --------------- | --------- | ----- | --- | --- | --- | --- |
switch(config-if)# no apply access-list ip MY_REPLACEMENT_ACL out
| switch(config-if)# | exit |     |     |     |     |     |
| ------------------ | ---- | --- | --- | --- | --- | --- |
switch(config)#
| apply access-list | (to | interface | VLAN) |     |     |     |
| ----------------- | --- | --------- | ----- | --- | --- | --- |
Syntax
| apply access-list    | {ip|ipv6} | <ACL-NAME> | {routed-in|routed-out} |                        |     |     |
| -------------------- | --------- | ---------- | ---------------------- | ---------------------- | --- | --- |
| no apply access-list | {ip|ipv6} | <ACL-NAME> |                        | {routed-in|routed-out} |     |     |
Description
AppliesanACLtotheinterfaceVLAN(orrangeofinterfaceVLANs)identifiedbythecurrentinterfaceVLAN
context.Usingtheapply access-listcommandonaninterfaceVLANinterfacewithanalready-applied
ACLofthesamedirectionandtypewillreplacethecurrently-appliedACL.
ThenoformofthiscommandremovesapplicationoftheACLfromtheinterfaceVLAN(orrangeofinterface
VLANs)identifiedbythecurrentinterfaceVLANcontext.
Commandcontext
config-if-vlan
Parameters
ip|ipv6
AccessControlLists|49

SpecifiestheACLtype:ipforIPv4,ipv6forIPv6.
<ACL-NAME>
SpecifiestheACLname.
routed-in
Selectstheroutedinbound(routedingress)trafficdirection.
routed-out
Selectstheroutedoutbound(routedegress)trafficdirection.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
n EachACLofagiventypecanbeappliedtothesameinterfaceVLANonceineachdirection.Therefore,
usingtheapply access-listcommandonaninterfaceVLANwithanalready-appliedACLofthesame
directionandtype,willreplacetheappliedACL.
Applicabletothe6300and6400SwitchSeries:WhenanACLisappliedtoaninterfaceVLAN,itwillcreate
n
hardwareentriesonallstackmembers(6300switch)andlinecards(6400switch)regardlessofwhether
aninterfaceVLANmemberexistsonanyspecificstackmemberorlinecard.
Examples
CreatinganIPv4ACLandapplyingittoroutedingresstrafficoninterfaceVLANvlan100:
| switch(config)#        | access-list | ip test               |           |       |
| ---------------------- | ----------- | --------------------- | --------- | ----- |
| switch(config-acl-ip)# |             | 10 permit any 1.1.1.2 | 2.2.2.2   | count |
| switch(config-acl-ip)# |             | 20 permit any 1.1.1.2 | 2.2.2.1   | count |
| switch(config-acl-ip)# |             | 30 permit any 2.2.2.2 | 1.1.1.2   | count |
| switch(config-acl-ip)# |             | 40 permit any 2.2.2.2 | 1.1.1.1   | count |
| switch(config-acl-ip)# |             | 50 permit any any     | any count |       |
| switch(config-acl-ip)# |             | exit                  |           |       |
switch(config)#
| switch(config)# | interface | vlan100 |     |     |
| --------------- | --------- | ------- | --- | --- |
switch(config-if-vlan)#
|     |     | apply access-list | ip test routed-in |     |
| --- | --- | ----------------- | ----------------- | --- |
ApplyingMy_ip_ACLtoroutedingresstrafficoninterfaceVLAN10:
| switch(config)#         | interface | vlan 10           |              |           |
| ----------------------- | --------- | ----------------- | ------------ | --------- |
| switch(config-if-vlan)# |           | apply access-list | ip My_ip_ACL | routed-in |
ApplyingMy_ipv6_ACLtoroutedingresstrafficoninterfaceVLAN10:
| switch(config)# | interface | vlan 10 |     |     |
| --------------- | --------- | ------- | --- | --- |
switch(config-if-vlan)# apply access-list ipv6 My_ip_ACL routed-in
ApplyingMy_ip_ACLtoroutedingresstrafficoninterfaceVLANs20to25:
| switch(config)# | interface | vlan 20-25 |     |     |
| --------------- | --------- | ---------- | --- | --- |
switch(config-if-vlan-<20-25>)# apply access-list ip My_ip_ACL routed-in
ReplacingMy_ipv6_ACLwithMy_Replacement_ACLoninterfaceVLAN10(followingtheaboveexamples):
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 50

| switch(config)# | interface | vlan | 10  |     |     |     |
| --------------- | --------- | ---- | --- | --- | --- | --- |
switch(config-if-vlan)#
|     |     | apply | access-list | ipv6 | My_Replacement_ACL | routed-in |
| --- | --- | ----- | ----------- | ---- | ------------------ | --------- |
Removing(unapplying)My_Replacement_ACLoninterfaceVLAN10.AnyotherinterfacesorVLANswith
My_Replacement_ACLappliedarenotaffected:
switch(config)#
|     | interface | vlan | 10  |     |     |     |
| --- | --------- | ---- | --- | --- | --- | --- |
switch(config-if-vlan)# no apply access-list ipv6 My_Replacement_ACL routed-in
Removing(unapplying)My_ip_ACLoninterfaceVLANs20to25.AnyotherinterfacesorVLANswithMy_ip_
ACLappliedarenotaffected:
| switch(config)# | interface | vlan | 20-25 |     |     |     |
| --------------- | --------- | ---- | ----- | --- | --- | --- |
switch(config-if-vlan-<20-25>)# no apply access-list ip My_ip_ACL routed-in
ApplyingMy_ip_ACLtoroutedegresstrafficoninterfaceVLAN30:
| switch(config)# | interface | vlan | 30  |     |     |     |
| --------------- | --------- | ---- | --- | --- | --- | --- |
switch(config-if-vlan)# apply access-list ip My_ip_ACL routed-out
ApplyingMy_ip_ACLtoroutedegresstrafficoninterfaceVLANs40to50:
| switch(config)# | interface | vlan | 40-50 |     |     |     |
| --------------- | --------- | ---- | ----- | --- | --- | --- |
switch(config-if-vlan-<40-50>)#
|                   |     |       | apply access-list |     | ip My_ip_ACL | routed-out |
| ----------------- | --- | ----- | ----------------- | --- | ------------ | ---------- |
| apply access-list | (to | VLAN) |                   |     |              |            |
Syntax
| apply access-list    | {ip|ipv6|mac} |     | <ACL-NAME> | {in|out} |     |     |
| -------------------- | ------------- | --- | ---------- | -------- | --- | --- |
| no apply access-list | {ip|ipv6|mac} |     | <ACL-NAME> | {in|out} |     |     |
Description
AppliesanACLtotheVLANidentifiedbythecurrentVLANcontext.
ThenoformofthiscommandremovesapplicationoftheACLfromtheVLANidentifiedbythecurrentVLAN
context.
Commandcontext
config-vlan
Parameters
ip|ipv6|mac
SpecifiestheACLtype:ipforIPv4,ipv6forIPv6,ormacforMACACL.
<ACL-NAME>
SpecifiestheACLname.
in
Selectstheinbound(ingress)trafficdirection.
out
Selectstheoutbound(egress)trafficdirection.
AccessControlLists|51

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
n EachACLofagiventypecanbeappliedtothesameVLANonceineachdirection.Therefore,usingthe
access-listcommandonaVLANwithanalready-appliedACLofthesametype,willreplacethe
apply
appliedACL.
Applicabletothe6300and6400SwitchSeries:WhenanACLisappliedtoaVLAN,itwillcreatehardware
n
entriesonallstackmembers(6300switch)andlinecards(6400switch)regardlessofwhetheraVLAN
memberexistsonanyspecificstackmemberorlinecard.
Examples
ApplyingMy_ip_ACLtoingresstrafficonVLANrange20to25:
| switch(config)# vlan         | 20-25             |              |     |
| ---------------------------- | ----------------- | ------------ | --- |
| switch(config-vlan-<20-25>)# | apply access-list | ip My_ip_ACL | in  |
ApplyingMy_ip_ACLtoegresstrafficonVLANrange40to50:
| switch(config)# vlan         | 40-50             |              |     |
| ---------------------------- | ----------------- | ------------ | --- |
| switch(config-vlan-<40-50>)# | apply access-list | ip My_ip_ACL | out |
ApplyingMy_ip_ACLtoingresstrafficonVLAN10:
| switch(config)# vlan | 10  |     |     |
| -------------------- | --- | --- | --- |
switch(config-vlan-10)#
|     | apply access-list | ip My_ip_ACL | in  |
| --- | ----------------- | ------------ | --- |
ApplyingMy_ipv6_ACLtoingresstrafficonVLAN10:
| switch(config)# vlan    | 10                |                  |     |
| ----------------------- | ----------------- | ---------------- | --- |
| switch(config-vlan-10)# | apply access-list | ipv6 My_ipv6_ACL | in  |
ApplyingMy_mac_ACLtoingresstrafficonVLAN10:
| switch(config)# vlan    | 10                |                |     |
| ----------------------- | ----------------- | -------------- | --- |
| switch(config-vlan-10)# | apply access-list | mac My_mac_ACL | in  |
ReplacingMy_ipv6_ACLwithMy_Replacement_ACLonVLAN10(followingtheprecedingexamples):
| switch(config)# vlan | 10  |     |     |
| -------------------- | --- | --- | --- |
switch(config-vlan-10)# apply access-list ipv6 My_Replacement_ACL in
Removing(unapplying)severalACLsonVLAN10:
| switch(config)# vlan | 10  |     |     |
| -------------------- | --- | --- | --- |
switch(config-vlan-10)# no apply access-list ipv6 My_Replacement_ACL in
| switch(config-vlan-10)# | no apply access-list | mac My_mac_ACL | in  |
| ----------------------- | -------------------- | -------------- | --- |
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 52

clear access-list hitcounts

Syntax

clear access-list hitcounts { all | [{ip|ipv6|mac} <ACL-NAME>] [interface <IF-NAME>| vlan
<VLAN-ID>] [in|out|routed-in|routed-out] }

Description

Clears the hit counts for ACLs with ACEs that include the count keyword.

Command context

Operator (>) or Manager (#)

Parameters

all

Selects all ACLs.

ip|ipv6|mac

Specifies the ACL type: ip for IPv4, ipv6 for IPv6, or mac for MAC.

<ACL-NAME>

Specifies the ACL name.

interface <IF-NAME>

Specifies the interface name (port or LAG).

vlan <VLAN-ID>

Specifies the VLAN.

in

Selects the inbound (ingress) traffic direction.

out

Selects the outbound (egress) traffic direction.

routed-in|routed-out

Selects the routed traffic direction on which the ACL is applied.

This is only available for IPv4 and IPv6 ACLs applied to interface VLANs.

n routed-in selects the routed inbound (routed ingress) traffic direction.

n routed-out selects the routed outbound (routed egress) traffic direction.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

On the 6400 Switch Series, interface identification differs.

Clearing the hit counts for My_ip_ACL applied to port 1/1/2 (egress):

switch# clear access-list hitcounts ip My_ip_ACL interface 1/1/2 out

Clearing the hit counts for My_ip_ACL applied to VLAN 10 (ingress):

switch# clear access-list hitcounts ip My_ip_ACL vlan 10 in

Access Control Lists | 53

Clearing the hit counts for all ACLs:

switch# clear access-list hitcounts all

clear access-list hitcounts control-plane

Syntax

clear access-list hitcounts [{ip|ipv6} <ACL-NAME>] control-plane vrf <VRF-NAME>

Description

Clears the hit counts for ACLs applied to the Control Plane VRF.

Command context

Operator (>) or Manager (#)

Parameters

ip|ipv6

Specifies the ACL type: ip for IPv4, oripv6 for IPv6.

<ACL-NAME>

Specifies the ACL name.

vrf <VRF-NAME>

Specifies the VRF name.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Clearing the hit counts for an IPv4 ACL applied to the Control Plane default VRF:

switch# clear access-list hitcounts ip My_ipv4_ACL control-plane vrf default

Clearing the hit counts for an IPv6 ACL applied to the Control Plane default VRF:

switch# clear access-list hitcounts ipv6 My_ipv6_ACL control-plane vrf default

object-group address resequence

Syntax

object-group {ip|ipv6} address <OBJECT-GROUP-NAME> resequence <STARTING-SEQUENCE-NUMBER>
<INCREMENT>

Description

Reorders the sequence numbers in an address object group.

Command context

config

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

54

Parameters

ip|ipv6

Specifies the object group IP address type, either ip or ipv6.

<OBJECT-GROUP-NAME>

Specifies the address object group name.

<STARTING-SEQUENCE-NUMBER>

Specifies the starting sequence number.

<INCREMENT>

Specifies the sequence number increment.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Resequencing address object group my_ipv4_addr_group to use sequence numbers 5, 10, 15 and so on:

switch(config)# object-group address my_ipv4_addr_group resequence 5 5
switch(config)#

object-group address reset

Syntax

object-group {ip|ipv6} address <OBJECT-GROUP-NAME> reset

Description

Resets the user configuration back to the active configuration. This command takes immediate effect, it is
not saved in the user configuration. Use this command if misconfiguration of an address object group has
occurred.

Command context

config

Parameters

ip|ipv6

Specifies the object group IP address type, either ip or ipv6.

<OBJECT-GROUP-NAME>

Specifies the address object group name.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Resetting IPv4 address object group my_ipv4_group:

switch(config)# object-group ip address my_ip_group reset
switch(config)#

Resetting IPv6 address object group my_ipv6_group:

Access Control Lists | 55

switch(config)# object-group ipv6 address my_ipv6_group reset
switch(config)#

object-group all reset

Syntax

object-group all reset

Description

Resets the user configuration back to the active configuration for all object types (address and port). This
command takes immediate effect, it is not saved in the user configuration. Use this command if
misconfiguration of address object groups and port object groups has occurred. Individual address and port
object groups can be reset respectively with the object-group address reset and object-group port
reset commands.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Resetting the user configuration for all object types (address and port):

switch(config)# object-group all reset
switch(config)#

object-group ip address

Syntax

Syntax to create an IPv4 address object group and enter its context:
object-group ip address <OBJECT-GROUP-NAME>

no object-group ip address <OBJECT-GROUP-NAME>

Syntax (within the address object-group context) for creating or removing IPv4 address entries:

[<SEQUENCE-NUMBER>] <IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]

no <SEQUENCE-NUMBER>

Description

Creates an IPv4 address object group comprised of one or more address entries. Address groups are used
solely as a shorthand way of specifying groups of addresses in the ACEs that make up ACLs. IPv4 address
groups can be used only in the access-list ip command. Entering object-group ip address with an
existing address group name, enables you to modify an existing address group.

The no form of this command deletes the entire address group or deletes a particular address group entry
identified by sequence number.

Command context

config

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

56

Theobject-group ip addresscommandtakesyouintothenamedaddressgroupcontext(withprompt
switch(config-addrgroup-ip)#)whereyouentertheaddresses.
Parameters
<OBJECT-GROUP-NAME>
Specifiestheaddressobjectgroupname.
<SEQUENCE-NUMBER>
Specifiesasequencenumberfortheaddressentry.Range:1to4294967295.Whenomitted,a
sequencenumber10largerthanthecurrenthighestsequencenumberisauto-assigned.Defaultauto-
assignedsequencenumbersare10,20,30,andsoon.
<IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]
SpecifiestheIPv4address.
n <IP-ADDRESS>-specifiestheIPv4hostaddress.
<PREFIX-LENGTH>-specifiestheaddressbitstomask(CIDRsubnetmasknotation).Range:1to32.
n
<SUBNET-MASK>-specifiestheaddressbitstomask(dotteddecimalnotation).
n
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreatinganIPv4addressgroupwithtwoentries:
| switch(config)#              | object-group      | ip address     | my_ipv4_addr_group |
| ---------------------------- | ----------------- | -------------- | ------------------ |
| switch(config-addrgroup-ip)# |                   | 10 192.168.0.1 |                    |
| switch(config-addrgroup-ip)# |                   | 20 192.168.0.2 |                    |
| switch(config-addrgroup-ip)# |                   | exit           |                    |
| switch(config)#              | show object-group |                |                    |
| Type                         | Name              |                |                    |
| Sequence                     | L4 Port(s)/IP     | Address        |                    |
-------------------------------------------------------------------------------
| IPv4 | my_ipv4_addr_group |     |     |
| ---- | ------------------ | --- | --- |
10 192.168.0.1
20 192.168.0.2
AddinganentrytoanexistingIPv4addressgroup:
| switch(config)#              | object-group      | ip address     | my_ipv4_addr_group |
| ---------------------------- | ----------------- | -------------- | ------------------ |
| switch(config-addrgroup-ip)# |                   | 30 192.168.0.3 |                    |
| switch(config-addrgroup-ip)# |                   | exit           |                    |
| switch(config)#              | show object-group |                |                    |
| Type                         | Name              |                |                    |
| Sequence                     | L4 Port(s)/IP     | Address        |                    |
-------------------------------------------------------------------------------
| IPv4 | my_ipv4_addr_group |     |     |
| ---- | ------------------ | --- | --- |
10 192.168.0.1
20 192.168.0.2
30 192.168.0.3
Removinganentry(20)fromanexistingIPv4addressgroup:
AccessControlLists|57

|     | switch(config)# |     | object-group |     | ip address | my_ipv4_addr_group |
| --- | --------------- | --- | ------------ | --- | ---------- | ------------------ |
switch(config-addrgroup-ip)#
|     |                              |      |            |              | no 20 |     |
| --- | ---------------------------- | ---- | ---------- | ------------ | ----- | --- |
|     | switch(config-addrgroup-ip)# |      |            |              | exit  |     |
|     | switch(config)#              |      | show       | object-group |       |     |
|     | Type                         | Name |            |              |       |     |
|     | Sequence                     | L4   | Port(s)/IP | Address      |       |     |
-------------------------------------------------------------------------------
|     | IPv4 | my_ipv4_addr_group |     |     |     |     |
| --- | ---- | ------------------ | --- | --- | --- | --- |
|     |      | 10 192.168.0.1     |     |     |     |     |
|     |      | 30 192.168.0.3     |     |     |     |     |
RemovinganIPv4addressgroup:
|              | switch(config)# |       | no     | object-group | ip address | my_ipv4_addr_group |
| ------------ | --------------- | ----- | ------ | ------------ | ---------- | ------------------ |
|              | switch(config)# |       | show   | object-group |            |                    |
|              | No object       | group | found. |              |            |                    |
| object-group |                 |       | ipv6   | address      |            |                    |
Syntax
SyntaxtocreateanIPv6addressobjectgroupandenteritscontext:
| object-group |              | ipv6 | address      | <OBJECT-GROUP-NAME> |                     |     |
| ------------ | ------------ | ---- | ------------ | ------------------- | ------------------- | --- |
| no           | object-group |      | ipv6 address |                     | <OBJECT-GROUP-NAME> |     |
Syntax(withintheaddressobject-groupcontext)forcreatingorremovingIPv6addressentries:
[<SEQUENCE-NUMBER>] <IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]
no <SEQUENCE-NUMBER>
Description
CreatesanIPv6addressobjectgroupcomprisedofoneormoreaddressentries.Addressgroupsareused
solelyasashorthandwayofspecifyinggroupsofaddressesintheACEsthatmakeupACLs.IPv6address
groupscanbeusedonlyintheaccess-list ipv6command.Enteringobject-group ipv6 addresswithan
existingaddressgroupname,enablesyoutomodifyanexistingaddressgroup.
Thenoformofthiscommanddeletestheentireaddressgroupordeletesaparticularaddressgroupentry
identifiedbysequencenumber.
Commandcontext
config
Theobject-group ipv6 addresscommandtakesyouintothenamedaddressgroupcontext(withprompt
switch(config-addrgroup-ipv6)#)whereyouentertheaddresses.
Parameters
<OBJECT-GROUP-NAME>
Specifiestheaddressobjectgroupname.
<SEQUENCE-NUMBER>
Specifiesasequencenumberfortheaddressentry.Range:1to4294967295.Whenomitted,asequence
number10largerthanthecurrenthighestsequencenumberisauto-assigned.Defaultauto-assigned
sequencenumbersare10,20,30,andsoon.
<IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]
SpecifiestheIPv6address.
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 58

<IP-ADDRESS>-specifiestheIPv6hostaddress.
n
<PREFIX-LENGTH>-specifiestheaddressbitstomask(CIDRsubnetmasknotation).Range:1to128.
o
o <SUBNET-MASK>-specifiestheaddressbitstomask(dotteddecimalnotation).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreatinganIPv6addressgroupwithtwoentries:
| switch(config)#                | object-group | ipv6 address | my_ipv6_addr_group |
| ------------------------------ | ------------ | ------------ | ------------------ |
| switch(config-addrgroup-ipv6)# |              | 10 1000::1   |                    |
| switch(config-addrgroup-ipv6)# |              | 20 1000::2   |                    |
switch(config-addrgroup-ipv6)#
exit
| switch(config)# | show object-group |         |     |
| --------------- | ----------------- | ------- | --- |
| Type            | Name              |         |     |
| Sequence        | L4 Port(s)/IP     | Address |     |
-------------------------------------------------------------------------------
| IPv6 | my_ipv6_addr_group |     |     |
| ---- | ------------------ | --- | --- |
10 1000::1
20 1000::2
AddinganentrytoanexistingIPv6addressgroup:
switch(config)#
|                                | object-group      | ipv6 address | my_ipv6_addr_group |
| ------------------------------ | ----------------- | ------------ | ------------------ |
| switch(config-addrgroup-ipv6)# |                   | 30 1000::3   |                    |
| switch(config-addrgroup-ipv6)# |                   | exit         |                    |
| switch(config)#                | show object-group |              |                    |
| Type                           | Name              |              |                    |
| Sequence                       | L4 Port(s)/IP     | Address      |                    |
-------------------------------------------------------------------------------
| IPv6 | my_ipv6_addr_group |     |     |
| ---- | ------------------ | --- | --- |
10 1000::1
20 1000::2
30 1000::3
Removinganentry(20)fromanexistingIPv6addressgroup:
| switch(config)#                | object-group      | ipv6 address | my_ipv6_addr_group |
| ------------------------------ | ----------------- | ------------ | ------------------ |
| switch(config-addrgroup-ipv6)# |                   | no 20        |                    |
| switch(config-addrgroup-ipv6)# |                   | exit         |                    |
| switch(config)#                | show object-group |              |                    |
| Type                           | Name              |              |                    |
| Sequence                       | L4 Port(s)/IP     | Address      |                    |
-------------------------------------------------------------------------------
| IPv6 | my_ipv6_addr_group |     |     |
| ---- | ------------------ | --- | --- |
10 1000::1
30 1000::3
RemovinganIPv6addressgroup:
| switch(config)# | no object-group   | ipv6 address | my_ipv6_addr_group |
| --------------- | ----------------- | ------------ | ------------------ |
| switch(config)# | show object-group |              |                    |
| No object group | found.            |              |                    |
AccessControlLists|59

object-group port

Syntax

Syntax to create a Layer 4 port object group and enter its context:
object-group port <OBJECT-GROUP-NAME>

no object-group port <OBJECT-GROUP-NAME>

Syntax (within the port object-group context) for creating or removing Layer 4 port entries:

[<SEQUENCE-NUMBER>] { {eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT> }

no <SEQUENCE-NUMBER>

Description

Creates a Layer 4 port object group comprised of one or more port entries. Port groups are used solely as a
shorthand way of specifying groups of ports in the ACEs that make up ACLs. Layer 4 port groups can be
used only in the access-list ip and access-list ipv6 commands. Entering object-group port with an
existing port group name, enables you to modify an existing port group.

The no form of this command deletes the entire port group or deletes a particular port group entry
identified by sequence number.

Command context

config

The object-group ip port command takes you into the named port group context (with prompt switch
(config-portgroup)#) where you specify the ports.

Parameters

<OBJECT-GROUP-NAME>

Specifies the port object group name.

<SEQUENCE-NUMBER>

Specifies a sequence number for the port entry. Range: 1 to 4294967295. When omitted, a sequence
number 10 larger than the current highest sequence number is auto-assigned. Default auto-assigned
sequence numbers are 10, 20, 30, and so on.

{ {eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT> }

Specifies the port or port range. Port numbers are in the range of 0 to 65535.

n eq <PORT> - specifies the Layer 4 port.

n gt <PORT> - specifies any Layer 4 port greater than the indicated port.

n lt <PORT> - specifies any Layer 4 port less than the indicated port.

n range MIN-PORT> <MAX-PORT> - specifies the Layer 4 port range.

When ACLs using ACEs defined with port groups are applied, the same number of hardware resources are

consumed as when the ports are specified directly in the ACEs and not in a group. Keep this in mind when creating

port groups that include many ports. Although hardware resource consumption is the same, with or without port

groups used, it may not be immediately obvious that some port groups that you have defined, include many ports.

It is recommended that you name port groups in a manner that reminds you that a group includes many ports.

Authority

Administrators or local user group members with execution rights for this command.

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

60

Examples
Creatingaportgroupwithtwoentriestocoverport80plusports0through50:
switch(config)#
|                           | object-group      |         | port my_port_group |
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
| switch(config)#           | object-group      |         | port my_port_group |
| ------------------------- | ----------------- | ------- | ------------------ |
| switch(config-portgroup)# |                   | 30      | gt 65525           |
| switch(config-portgroup)# |                   | exit    |                    |
| switch(config)#           | show object-group |         |                    |
| Type                      | Name              |         |                    |
| Sequence                  | L4 Port(s)/IP     | Address |                    |
-------------------------------------------------------------------------------
| Port | my_port_group |     |     |
| ---- | ------------- | --- | --- |
10 eq 80
20 range 0 50
30 gt 65525
Removinganentry(#20)fromtheportgroup:
| switch(config)#           | object-group      |         | port my_port_group |
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
| switch(config)# | no object-group   |     | port my_port_group |
| --------------- | ----------------- | --- | ------------------ |
| switch(config)# | show object-group |     |                    |
| No object group | found.            |     |                    |
| object-group    | port resequence   |     |                    |
Syntax
object-group port <OBJECT-GROUP-NAME> resequence <STARTING-SEQUENCE-NUMBER> <INCREMENT>
Description
Reordersthesequencenumbersinaportobjectgroup.
AccessControlLists|61

Command context

config

Parameters

<OBJECT-GROUP-NAME>

Specifies the port object group name.

<STARTING-SEQUENCE-NUMBER>

Specifies the starting sequence number.

<INCREMENT>

Specifies the sequence number increment.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Resequencing port object group my_port_group to use sequence numbers 110, 120, 130 and so on:

switch(config)# object-group port my_port_group resequence 110 10
switch(config)#

object-group port reset

Syntax

object-group port <OBJECT-GROUP-NAME> reset

Description

Resets the user configuration back to the active configuration. This command takes immediate effect, it is
not saved in the user configuration. Use this command if misconfiguration of a port object group has
occurred.

Command context

config

Parameters

<OBJECT-GROUP-NAME>

Specifies the port object group name.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Resetting port object group my_port_group:

switch(config)# object-group port my_port_group reset
switch(config)#

show access-list

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

62

Syntax

Syntax that filters by ACLs applied to an interface or VLAN:
show access-list [interface <IF-NAME>|vlan <VLAN-ID>] [ip|ipv6|mac]

[in|out|routed-in|routed-out] [commands] [configuration] [vsx-peer]

Syntax that filters by the named ACL:
show access-list [ip|ipv6|mac] [<ACL-NAME>] [commands] [configuration] [vsx-peer]

Description

Shows information about your defined ACLs and where they have been applied. When show access-list is
entered without parameters, information for all ACLs is shown. The parameters filter the list of ACLs for
which information is shown.

Available filtering includes:

n The content of a specific ACL.

n All ACLs of a specific type.

n All ACLs applied to a specific interface (port or LAG).

n All ACLs applied to a specific VLAN.

n All ACLs applied in a particular direction.

n All IPv4 or IPv6 ACLs applied to interface VLANs (routed in or out).

Command context

Operator (>) or Manager (#)

Parameters

interface <IF-NAME>

Specifies the interface name (port or LAG).

vlan <VLAN-ID>

Specifies the VLAN.

ip|ipv6|mac

Specifies the ACL type:

ip for IPv4,
ipv6 for IPv6, or
mac for MAC.

in

Selects the inbound (ingress) traffic direction.

out

Selects the outbound (egress) traffic direction.

routed-in|routed-out

Selects the routed traffic direction on which the ACL is applied.

This is only available for IPv4 and IPv6 ACLs applied to interface VLANs.

n routed-in selects the routed inbound (routed ingress) traffic direction.

n routed-out selects the routed outbound (routed egress) traffic direction.

<ACL-NAME>

Specifies the ACL name.

commands

Access Control Lists | 63

SpecifiesthattheACLdefinitionistobeshownasthecommandsandparametersusedtocreateitrather
thanintabularform.
configuration
Specifiesthattheuser-configuredACLsbeshownasentered,eveniftheACLsarenotactiveduetoACE-
definitioncommandissuesorhardwareissues.Thisparameterisusefulifthereisamismatchbetween
theenteredconfigurationandtheprevioussuccessfullyprogrammed(active)ACLsconfiguration.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
CreatinganIPv4ACL,applyingittoaninterfaceVLAN(routedin),andthenshowingACLinformationfiltered
forthatinterfaceVAN:
| switch(config)#        | access-list |      | ip test            |           |       |
| ---------------------- | ----------- | ---- | ------------------ | --------- | ----- |
| switch(config-acl-ip)# |             | 10   | permit any 1.1.1.2 | 2.2.2.2   | count |
| switch(config-acl-ip)# |             | 20   | permit any 1.1.1.2 | 2.2.2.1   | count |
| switch(config-acl-ip)# |             | 30   | permit any 2.2.2.2 | 1.1.1.2   | count |
| switch(config-acl-ip)# |             | 40   | permit any 2.2.2.2 | 1.1.1.1   | count |
| switch(config-acl-ip)# |             | 50   | permit any any     | any count |       |
| switch(config-acl-ip)# |             | exit |                    |           |       |
switch(config)#
| switch(config)#         | interface |             | vlan100     |         |              |
| ----------------------- | --------- | ----------- | ----------- | ------- | ------------ |
| switch(config-if-vlan)# |           | apply       | access-list | ip test | routed-in    |
| switch(config-if-vlan)# |           | exit        |             |         |              |
| switch(config)#         | show      | access-list | interface   | vlan100 | ip routed-in |
Direction
| Type     | Name    |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- |
| Sequence | Comment |     |     |     |     |
Ac L3 Protocol
|     | Source      | IP Address |         | Source      | L4 Port(s) |
| --- | ----------- | ---------- | ------- | ----------- | ---------- |
|     | Destination | IP         | Address | Destination | L4 Port(s) |
|     | Additional  | Parameters |         |             |            |
-------------------------------------------------------------------------------
Routed Inbound
| IPv4 | test |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- |
10
|     | permit |     |     | any |     |
| --- | ------ | --- | --- | --- | --- |
1.1.1.2
2.2.2.2
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
20
|     | permit |     |     | any |     |
| --- | ------ | --- | --- | --- | --- |
1.1.1.2
2.2.2.1
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
30
|     | permit |     |     | any |     |
| --- | ------ | --- | --- | --- | --- |
2.2.2.2
1.1.1.2
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
40
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 64

|     | permit |     |     | any |     |
| --- | ------ | --- | --- | --- | --- |
2.2.2.2
1.1.1.1
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
50
|     | permit |     |     | any |     |
| --- | ------ | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
-------------------------------------------------------------------------------
ShowinganIPv4ACL:
| switch#  | show access-list | ip MY_ACL  |     |             |            |
| -------- | ---------------- | ---------- | --- | ----------- | ---------- |
| Type     | Name             |            |     |             |            |
| Sequence | Comment          |            |     |             |            |
|          | Action           |            |     | L3 Protocol |            |
|          | Source           | IP Address |     | Source      | L4 Port(s) |
|          | Destination      | IP Address |     | Destination | L4 Port(s) |
|          | Additional       | Parameters |     |             |            |
------------------------------------------------------------------------------
| IPv4 | MY_ACL    |     |     |     |     |
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
172.26.1.0//255.255.255.0
any
syn
ack
dscp 10
|     | 40 deny |     |     | any |     |
| --- | ------- | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
------------------------------------------------------------------------------
ShowinganIPv4ACLascommands:
| switch#     | show access-list | ip MY_ACL                    | commands |             |             |
| ----------- | ---------------- | ---------------------------- | -------- | ----------- | ----------- |
| access-list | ip MY_ACL        |                              |          |             |             |
| 10 permit   | udp              | any 172.16.1.0/255.255.255.0 |          |             |             |
| 20 permit   | tcp              | 172.16.2.0/255.255.0.0       |          | gt 1023 any |             |
| 30 permit   | tcp              | 172.26.1.0/255.255.255.0     |          | any syn     | ack dscp 10 |
| 40 deny     | any any          | any count                    |          |             |             |
ShowingIPv4ACLsappliedtoVLAN10,inbound:
| switch#  | show access-list | vlan 10    | ip in |             |            |
| -------- | ---------------- | ---------- | ----- | ----------- | ---------- |
| Type     | Name             |            |       |             |            |
| Sequence | Comment          |            |       |             |            |
|          | Action           |            |       | L3 Protocol |            |
|          | Source           | IP Address |       | Source      | L4 Port(s) |
AccessControlLists|65

|     | Destination | IP Address |     | Destination | L4 Port(s) |
| --- | ----------- | ---------- | --- | ----------- | ---------- |
|     | Additional  | Parameters |     |             |            |
------------------------------------------------------------------------------
| IPv4 | My_ip_ACL |     |     |     |     |
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
172.26.1.0//255.255.255.0
any
syn
ack
dscp 10
|     | 40 deny |     |     | any |     |
| --- | ------- | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
------------------------------------------------------------------------------
ShowingIPv6ACLsappliedtoLAG128,inbound:
| switch#  | show access-list | interface  | lag128 | ipv6 in     |            |
| -------- | ---------------- | ---------- | ------ | ----------- | ---------- |
| Type     | Name             |            |        |             |            |
| Sequence | Comment          |            |        |             |            |
|          | Action           |            |        | L3 Protocol |            |
|          | Source           | IP Address |        | Source      | L4 Port(s) |
|          | Destination      | IP Address |        | Destination | L4 Port(s) |
|          | Additional       | Parameters |        |             |            |
------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- |
|      | 10 permit   |     |     | udp |     |
any
2001::1/64
|     | 20 permit          |     |     | tcp    |     |
| --- | ------------------ | --- | --- | ------ | --- |
|     | 2001:2001::2:1/128 |     |     | > 1023 |     |
any
|     | 30 permit |     |     | tcp |     |
| --- | --------- | --- | --- | --- | --- |
2001:2011::1/64
|     | 40 deny |     |     | any |     |
| --- | ------- | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
------------------------------------------------------------------------------
ShowinganIPv6ACLascommands:
| switch#     | show access-list | ipv6 MY_IPV6_ACL   |     | commands |     |
| ----------- | ---------------- | ------------------ | --- | -------- | --- |
| access-list | ipv6 MY_IPV6_ACL |                    |     |          |     |
| 10 permit   | udp              | any 2001::1/64     |     |          |     |
| 20 permit   | tcp              | 2001:2001::2:1/128 | gt  | 1023 any |     |
| 40 deny     | any any          | any count          |     |          |     |
ShowingaMACACL:
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 66

| switch#  | show access-list | mac MY_MAC_ACL |     |           |
| -------- | ---------------- | -------------- | --- | --------- |
| Type     | Name             |                |     |           |
| Sequence | Comment          |                |     |           |
|          | Action           |                |     | EtherType |
|          | Source MAC       | Address        |     |           |
|          | Destination      | MAC Address    |     |           |
|          | Additional       | Parameters     |     |           |
------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |     |      |
| --- | ---------- | --- | --- | ---- |
|     | 10 permit  |     |     | ipv6 |
1122.3344.5566/ffff.ffff.0000
any
|     | 20 permit |     |     | any |
| --- | --------- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS Priority | Code Point: | 4   |     |
| --- | ------------ | ----------- | --- | --- |
|     | 30 deny      |             |     | any |
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
------------------------------------------------------------------------------
ShowingaMACACLascommands:
| switch#          | show access-list              | mac MY_MAC_ACL | commands |           |
| ---------------- | ----------------------------- | -------------- | -------- | --------- |
| access-list      | mac MY_MAC_ACL                |                |          |           |
| 10 permit        | 1122.3344.5566/ffff.ffff.0000 |                |          | any ipv6  |
| 20 permit        | aaaa.bbbb.cccc                | 1111.2222.3333 |          | any pcp 4 |
| 30 deny          | any any any                   | count          |          |           |
| show access-list | control-plane                 |                |          |           |
Syntax
show access-list [ip|ipv6] [<ACL-NAME>] control-plane [vrf <VRF-NAME>]
|     | [commands] | [configuration][vsx-peer] |     |     |
| --- | ---------- | ------------------------- | --- | --- |
Description
ShowsinformationaboutyourdefinedACLsthathavebeenappliedtotheControlPlane.Whenshow
access-list control-planeisenteredwithoutparameters,informationforallACLsappliedtotheControl
Planeisshown.TheparametersfilterthelistofACLsforwhichinformationisshown.
Availablefilteringincludes:
n ThecontentofaspecificACLthathasbeenappliedtotheControlPlane.
n AllACLsofaspecifictypethathavebeenappliedtotheControlPlane.
n AllACLsappliedtotheControlPlaneforaspecificVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
ip|ipv6
SpecifiestheACLtype:ipforIPv4,oripv6forIPv6.
<ACL-NAME>
SpecifiestheACLname.
AccessControlLists|67

vrf <VRF-NAME>
SpecifiestheVRFname.
[commands]
SpecifiesthattheACLdefinitionistobeshownasthecommandsandparametersusedtocreateitrather
thanintabularform.
[configuration]
Specifiesthattheuser-configuredACLsbeshownasentered,eveniftheACLsarenotactiveduetoACE-
definitioncommandissuesorhardwareissues.Thisparameterisusefulifthereisamismatchbetween
theenteredconfigurationandtheprevioussuccessfullyprogrammed(active)ACLsconfiguration.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowinganIPv4ACLappliedtotheControlPlanedefaultVRF:
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
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 68

Additional Parameters

------------------------------------------------------------------------------
IPv6

My_ipv6_ACL

10 permit
any
2001::1/64

20 permit

2001:2001::2:1/128
any
30 permit

2001:2011::1/64

40 deny

any
any
Hit-counts: enabled

udp

tcp

> 1023

tcp

any

------------------------------------------------------------------------------

show access-list hitcounts

Syntax

show access-list hitcounts { [{ip|ipv6|mac} <ACL-NAME>] [interface <IF-NAME> |

vlan <VLAN-ID>] [in|out|routed-in|routed-out] [vsx-peer] }

Description

Shows the hit count of the number of times an ACL has matched a packet or frame for ACEs with the count
keyword. For ACEs without the count keyword, a dash is shown in place of a hit count.

Command context

Operator (>) or Manager (#)

Parameters

ip|ipv6|mac

Specifies the ACL type: ip for IPv4, ipv6 for IPv6, or mac for MAC.

<ACL-NAME>

Specifies the ACL name.

interface <IF-NAME>

Specifies the interface name (port or LAG).

vlan <VLAN-ID>

Specifies the VLAN.

in

Selects the inbound (ingress) traffic direction.

out

Selects the outbound (egress) traffic direction.

routed-in|routed-out

Selects the routed traffic direction on which the ACL is applied.

This is only available for IPv4 and IPv6 ACLs applied to interface VLANs.

n routed-in selects the routed inbound (routed ingress) traffic direction.

n routed-out selects the routed outbound (routed egress) traffic direction.

[vsx-peer]

Access Control Lists | 69

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
ACLhitcountsareaggregatedacrossall:
n
o physicalinterfacestowhichtheACLisappliedtooningress,
o physicalinterfacestowhichtheACLisappliedtoonegress,
o VLANstowhichtheACLisappliedtooningress.
o VLANstowhichtheACLisappliedtoonegress.
o InterfaceVLANstowhichtheIPv4orIPv6ACLisappliedonroutedingress
o InterfaceVLANstowhichtheIPv4orIPv6ACLisappliedonroutedegress
IfanACLwithanACEwiththecountkeywordisappliedtomultiplephysicalinterfacesorVLANs,thehit
n
countsareaggregated.ThereisoneaggregationforphysicalinterfacesandanotherforVLANs.
AccumulatedhitcountsforanappliedACLarecleareduponanymodificationoftheACL.
n
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingthehitcountsforMy_ip_ACLappliedtoport1/1/2:
| switch#    | show access-list | hitcounts     | ip My_ip_ACL      |               | interface | 1/1/2       |
| ---------- | ---------------- | ------------- | ----------------- | ------------- | --------- | ----------- |
| Statistics | for ACL          | My_ip_ACL     | (ipv4):           |               |           |             |
| interface  | 1/1/2*           | (in):         |                   |               |           |             |
|            | Hit Count        | Configuration |                   |               |           |             |
|            |                  | - 10 permit   | udp any           | 172.16.1.0/24 |           |             |
|            |                  | - 20 permit   | tcp 172.16.2.0/16 |               | gt 1023   | any         |
|            |                  | - 30 permit   | tcp 172.26.1.0/24 |               | any syn   | ack dscp 10 |
|            |                  | 0 40 deny     | any any any       | count         |           |             |
* access-list statistics are shared among each combination of context type
(interface, VLAN, VRF) and direction (in, out, routed-in, routed-out,
control-plane). Use 'access-list TYPE NAME copy' to create a new access-list
| for separate | statistics. |     |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- | --- |
ShowingthehitcountsforMy_ip_ACLappliedtoVLAN10:
| switch#    | show access-list | hitcounts     | ip My_ip_ACL      |               | vlan 10 |             |
| ---------- | ---------------- | ------------- | ----------------- | ------------- | ------- | ----------- |
| Statistics | for ACL          | My_ip_ACL     | (ipv4):           |               |         |             |
| vlan 10*   | (in):            |               |                   |               |         |             |
|            | Hit Count        | Configuration |                   |               |         |             |
|            |                  | - 10 permit   | udp any           | 172.16.1.0/24 |         |             |
|            |                  | - 20 permit   | tcp 172.16.2.0/16 |               | gt 1023 | any         |
|            |                  | - 30 permit   | tcp 172.26.1.0/24 |               | any syn | ack dscp 10 |
|            |                  | 0 40 deny     | any any any       | count         |         |             |
* access-list statistics are shared among each combination of context type
(interface, VLAN, VRF) and direction (in, out, routed-in, routed-out,
control-plane). Use 'access-list TYPE NAME copy' to create a new access-list
| for separate | statistics. |     |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- | --- |
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 70

| show access-list |     | hitcounts |     | control-plane |     |     |     |
| ---------------- | --- | --------- | --- | ------------- | --- | --- | --- |
Syntax
show access-list hitcounts [{ip|ipv6} <ACL-NAME>] control-plane vrf <VRF-NAME> [vsx-peer]
Description
ShowsthehitcountofthenumberoftimesanACL(appliedtotheControlPlane)hasmatchedapacketfor
ACEswiththecountkeyword.ForACEswithoutthecountkeyword,adashisshowninplaceofahitcount.
Commandcontext
Operator(>)orManager(#)
Parameters
ip|ipv6
SpecifiestheACLtype:ipforIPv4,oripv6forIPv6.
<ACL-NAME>
SpecifiestheACLname.
vrf <VRF-NAME>
SpecifiestheVRFname.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
n ACLhitcountsareaggregatedacrossallVRFstowhichtheACLisappliedtooningress.
n AccumulatedhitcountsforanappliedACLarecleareduponanymodificationoftheACL.
Examples
ShowingthehitcountsforanIPv4ACLappliedtotheControlPlanedefaultVRF:
switch# show access-list hitcounts ip My_ipv4_ACL control-plane vrf default
| Statistics    | for              | ACL My_ipv4_ACL |               | (ipv4):                      |                          |             |         |
| ------------- | ---------------- | --------------- | ------------- | ---------------------------- | ------------------------ | ----------- | ------- |
| VRF default*  | (control-plane): |                 |               |                              |                          |             |         |
|               | Hit              | Count           | Configuration |                              |                          |             |         |
|               |                  | -               | 10 permit     | udp any                      | 172.16.1.0/255.255.255.0 |             |         |
|               |                  | -               | 20 permit     | tcp 172.16.2.0/255.255.0.0   |                          | gt 1023 any |         |
|               |                  | -               | 30 permit     | tcp 172.26.1.0/255.255.255.0 |                          | any syn ack | dscp 10 |
|               |                  | 8               | 40 deny       | any any any                  | count                    |             |         |
| * access-list | statistics       |                 | are           | shared among                 | each combination         | of          |         |
context type (interface, VLAN, VRF) and direction (in, out,control-plane).
use 'access-list TYPE NAME copy' to create a uniquely-named access-list.
| show capacities |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
Syntax
| show capacities | <FEATURE> |     | [vsx-peer] |     |     |     |     |
| --------------- | --------- | --- | ---------- | --- | --- | --- | --- |
AccessControlLists|71

Description
Showssystemcapacitiesandtheirvaluesforallfeaturesoraspecificfeature.
Commandcontext
Manager(#)
Parameters
<FEATURE>
Specifiesafeature.Forexample,aaaorvrrp.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Capacitiesareexpressedinuser-understandableterms.Thustheymaynotmaptoaspecifichardwareor
softwareresourceorcomponent.Theyarenotintendedtodefineafeatureexhaustively.
Examples
ShowingallavailablecapacitiesforBGP:
| switch#            | show capacities | bgp |     |       |
| ------------------ | --------------- | --- | --- | ----- |
| System Capacities: | Filter          | BGP |     |       |
| Capacities         | Name            |     |     | Value |
-----------------------------------------------------------------------------------
| Maximum | number of AS | numbers in as-path | attribute | 32  |
| ------- | ------------ | ------------------ | --------- | --- |
...
Showingallavailablecapacitiesformirroring:
| switch#            | show capacities | mirroring |     |       |
| ------------------ | --------------- | --------- | --- | ----- |
| System Capacities: | Filter          | Mirroring |     |       |
| Capacities         | Name            |           |     | Value |
-----------------------------------------------------------------------------------
| Maximum | number of Mirror  | Sessions configurable | in a system | 4   |
| ------- | ----------------- | --------------------- | ----------- | --- |
| Maximum | number of enabled | Mirror Sessions       | in a system | 4   |
ShowingallavailablecapacitiesforMSTP:
| switch#            | show capacities | mstp |     |       |
| ------------------ | --------------- | ---- | --- | ----- |
| System Capacities: | Filter          | MSTP |     |       |
| Capacities         | Name            |      |     | Value |
-----------------------------------------------------------------------------------
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 72

| Maximum number |     | of mstp | instances | configurable |     | in a system | 64  |
| -------------- | --- | ------- | --------- | ------------ | --- | ----------- | --- |
ShowingallavailablecapacitiesforVLANcount:
| switch#    | show        | capacities | vlan-count |            |     |     |       |
| ---------- | ----------- | ---------- | ---------- | ---------- | --- | --- | ----- |
| System     | Capacities: | Filter     |            | VLAN Count |     |     |       |
| Capacities | Name        |            |            |            |     |     | Value |
-----------------------------------------------------------------------------------
| Maximum                | number | of VLANs | supported | in  | the | system | 4094 |
| ---------------------- | ------ | -------- | --------- | --- | --- | ------ | ---- |
| show capacities-status |        |          |           |     |     |        |      |
Syntax
| show capacities-status |     |     | <FEATURE> | [vsx-peer] |     |     |     |
| ---------------------- | --- | --- | --------- | ---------- | --- | --- | --- |
Description
Showssystemcapacitiesstatusandtheirvaluesforallfeaturesoraspecificfeature.
Commandcontext
Manager(#)
Parameters
<FEATURE>
Specifiesthefeature,forexampleaaaorvrrpforwhichtodisplaycapacities,values,andstatus.
Required.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Showingthesystemcapacitiesstatusforallfeatures:
| switch#    | show       | capacities-status |     |     |     |     |       |
| ---------- | ---------- | ----------------- | --- | --- | --- | --- | ----- |
| System     | Capacities | Status            |     |     |     |     |       |
| Capacities | Status     | Name              |     |     |     |     | Value |
Maximum
------------------------------------------------------------------------------------
-----
| Number | of active | gateway | mac | addresses | in  | a system | 0   |
| ------ | --------- | ------- | --- | --------- | --- | -------- | --- |
16
| Number | of aspath-lists |     | configured |     |     |     | 0   |
| ------ | --------------- | --- | ---------- | --- | --- | --- | --- |
64
| Number | of community-lists |     |     | configured |     |     | 0   |
| ------ | ------------------ | --- | --- | ---------- | --- | --- | --- |
AccessControlLists|73

64
...
ShowingthesystemcapacitiesstatusforBGP:
| switch#    | show       | capacities-status |         |        | bgp |     |       |
| ---------- | ---------- | ----------------- | ------- | ------ | --- | --- | ----- |
| System     | Capacities |                   | Status: | Filter | BGP |     |       |
| Capacities |            | Status            | Name    |        |     |     | Value |
Maximum
------------------------------------------------------------------------------------
-----
| Number | of  | aspath-lists |     | configured |     |     | 0   |
| ------ | --- | ------------ | --- | ---------- | --- | --- | --- |
64
| Number | of  | community-lists |     | configured |     |     | 0   |
| ------ | --- | --------------- | --- | ---------- | --- | --- | --- |
64
| Number | of  | neighbors |     | configured | across all | VRFs | 0   |
| ------ | --- | --------- | --- | ---------- | ---------- | ---- | --- |
50
| Number | of  | peer | groups | configured | across | all VRFs | 0   |
| ------ | --- | ---- | ------ | ---------- | ------ | -------- | --- |
25
| Number | of  | prefix-lists |     | configured |     |     | 0   |
| ------ | --- | ------------ | --- | ---------- | --- | --- | --- |
64
| Number | of  | route-maps |     | configured |     |     | 0   |
| ------ | --- | ---------- | --- | ---------- | --- | --- | --- |
64
| Number | of  | routes | in  | BGP RIB |     |     | 0   |
| ------ | --- | ------ | --- | ------- | --- | --- | --- |
256000
Number of route reflector clients configured across all VRFs 0
16
| show | object-group |     |     |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- | --- | --- |
Syntax
show object-group [{ip|ipv6} address | port] [<OBJECT-GROUP-NAME>] [commands]
[configuration]
Description
Showsinformationaboutyourdefinedobjectgroups.Whenshow object-groupisenteredwithout
parameters,informationforallobjectgroupsisshown.Theparametersfilterthelistofobjectgroupsfor
whichinformationisshown.
Commandcontext
Operator(>)orManager(#)
Parameters
| [{ip|ipv6} | address |     | | port] |     |     |     |     |
| ---------- | ------- | --- | ------- | --- | --- | --- | --- |
Specifiestheobjectgrouptype,eitheraddressforanIPaddress,orport.
<OBJECT-GROUP-NAME>
Specifiestheobjectgroupname.
[commands]
Specifiesthattheobjectgroupdefinitionistobeshownasthecommandsandparametersusedto
createitratherthanintabularform.
[configuration]
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 74

Specifiesthattheuser-configuredobjectgroupsbeshownasconfigured.Theoutputofthecommand
withthisparametermaynotbethesameaswhatisactiveontheswitchduetoamisconfiguredobject
group.SeeExamplesinthistopic.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showingconfiguredobjectgroups:
| switch# show | object-group  |         |
| ------------ | ------------- | ------- |
| Type         | Name          |         |
| Sequence     | L4 Port(s)/IP | Address |
-------------------------------------------------------------------------------
| IPv4 | my_address_group |     |
| ---- | ---------------- | --- |
10 192.168.0.1
20 192.168.0.3
| Port | my_port_group |     |
| ---- | ------------- | --- |
10 eq 80
20 gt 65525
switch#
| switch# show | object-group | commands         |
| ------------ | ------------ | ---------------- |
| object-group | ip address   | my_address_group |
10 192.168.0.1
20 192.168.0.3
| object-group | port my_port_group |     |
| ------------ | ------------------ | --- |
| 10 eq        | 80                 |     |
| 20 gt        | 65525              |     |
Showingamisconfiguredobjectgroup:
| switch# show | object-group  |         |
| ------------ | ------------- | ------- |
| Type         | Name          |         |
| Sequence     | L4 Port(s)/IP | Address |
-------------------------------------------------------------------------------
! object-group ip address My_ip_object_group user configuration does not match
! the active hardware configuration. Run 'object-group ip address NAME reset'
! to reset the object group to match the active hardware configuration.
| IPv4 | my_address_group |     |
| ---- | ---------------- | --- |
switch#
| switch# show | object-group  | configuration |
| ------------ | ------------- | ------------- |
| Type         | Name          |               |
| Sequence     | L4 Port(s)/IP | Address       |
-------------------------------------------------------------------------------
! object-group ip address My_ip_object_group user configuration does not match
! the active hardware configuration. Run 'object-group ip address NAME reset'
! to reset the object group to match the active hardware configuration.
| IPv4 | my_address_group |     |
| ---- | ---------------- | --- |
10 192.168.0.1
20 192.168.0.3
switch#
| switch# show | object-group | commands |
| ------------ | ------------ | -------- |
AccessControlLists|75

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
switch#
| show     | object-group  |         | configuration |
| -------- | ------------- | ------- | ------------- |
| Type     | Name          |         |               |
| Sequence | L4 Port(s)/IP | Address |               |
-------------------------------------------------------------------------------
| IPv4 | my_address_group |     |     |
| ---- | ---------------- | --- | --- |
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 76

Chapter 3
|                   |     |          |     | ACL configuration | examples |
| ----------------- | --- | -------- | --- | ----------------- | -------- |
| ACL configuration |     | examples |     |                   |          |
ThischaptershowsexamplesfordefiningandapplyingIPv4andIPv6ACLs.
| IPv4 ACL | example | overview |     |     |     |
| -------- | ------- | -------- | --- | --- | --- |
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Thisexample:
n DefinesandappliesanACLtointerface1/1/1onSwitchA(seeimageinthistopic)sothatHostAisnot
abletosendtraffictoHostB,butitcancommunicatewithallotherdevicesinthenetwork.
n Countsblockedpackets.
| Defining | and | applying | an IPv4 | ACL |     |
| -------- | --- | -------- | ------- | --- | --- |
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
1. BegindefininganIPv4ACLnamedFILTER_TO_HOST_B:
| switch(config)# |     | access-list | ip FILTER_TO_HOST_B |     |     |
| --------------- | --- | ----------- | ------------------- | --- | --- |
2. AddanACEthatdeniesaccessfromIPaddress192.168.1.2(HostA)to192.168.2.2(HostB):
| switch(config-acl-ip)# |     | deny | any 192.168.1.2 | 192.168.2.2 | log |
| ---------------------- | --- | ---- | --------------- | ----------- | --- |
3. AddanACEthatallowsaccessfromallotherIPaddresses:
| switch(config-acl-ip)# |     | permit | any any | any |     |
| ---------------------- | --- | ------ | ------- | --- | --- |
4. ExittheACLdefinition:
| switch(config-acl-ip)# |     | exit |     |     |     |
| ---------------------- | --- | ---- | --- | --- | --- |
77
| AOS-CX10.07ACLsandClassifierPoliciesGuide| |     |     | (6300,6400,8360SwitchSeries) |     |     |
| ------------------------------------------ | --- | --- | ---------------------------- | --- | --- |

5. EnterthecontextoftheinterfacetowhichyouwillapplytheACL:
|     | switch(config)# | interface |     | 1/1/1 |     |     |     |
| --- | --------------- | --------- | --- | ----- | --- | --- | --- |
6. ApplytheFILTER_TO_HOST_BACLtoinbound(ingress)traffic:
|     | switch(config-if)# |     | apply | access-list | ip FILTER_TO_HOST_B |     | in  |
| --- | ------------------ | --- | ----- | ----------- | ------------------- | --- | --- |
7. ShowyourACL:
|     | switch(config-if)# |                  | exit       |                     |     |             |            |
| --- | ------------------ | ---------------- | ---------- | ------------------- | --- | ----------- | ---------- |
|     | switch#            | show access-list |            | ip FILTER_TO_HOST_B |     |             |            |
|     | Type               | Name             |            |                     |     |             |            |
|     | Sequence           | Comment          |            |                     |     |             |            |
|     |                    | Action           |            |                     |     | L3 Protocol |            |
|     |                    | Source           | IP Address |                     |     | Source      | L4 Port(s) |
|     |                    | Destination      |            | IP Address          |     | Destination | L4 Port(s) |
|     |                    | Additional       |            | Parameters          |     |             |            |
------------------------------------------------------------------------------
-
|     | IPv4 | FILTER_TO_HOST_B |     |     |     |     |     |
| --- | ---- | ---------------- | --- | --- | --- | --- | --- |
10
|     |     | deny |     |     |     | any |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
192.168.1.2
192.168.2.2
|     |     | Logging:    | enabled |         |     |     |     |
| --- | --- | ----------- | ------- | ------- | --- | --- | --- |
|     |     | Hit-counts: |         | enabled |     |     |     |
20
|     |     | permit |     |     |     | any |     |
| --- | --- | ------ | --- | --- | --- | --- | --- |
any
any
------------------------------------------------------------------------------
-
| IPv6 | ACL example |     | overview |     |     |     |     |
| ---- | ----------- | --- | -------- | --- | --- | --- | --- |
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Thisexample:
n DefinesandappliesanACLtointerface1/1/1onSwitchA(seeimageinthistopic)sothatHostAisnot
abletosendtraffictoHostB,butitcancommunicatewithallotherdevicesinthenetwork.
Countsblockedpackets.
n
ACLconfigurationexamples|78

| Defining | and | applying | an  | IPv6 | ACL |     |
| -------- | --- | -------- | --- | ---- | --- | --- |
Onthe6400SwitchSeries,interfaceidentificationdiffers.
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
|     | switch(config-if)# |                  | exit      |     |       |     |
| --- | ------------------ | ---------------- | --------- | --- | ----- | --- |
|     | switch#            | show access-list | interface |     | 1/1/1 |     |
Direction
|     | Type     | Name        |            |     |             |            |
| --- | -------- | ----------- | ---------- | --- | ----------- | ---------- |
|     | Sequence | Comment     |            |     |             |            |
|     |          | Action      |            |     | L3 Protocol |            |
|     |          | Source      | IP Address |     | Source      | L4 Port(s) |
|     |          | Destination | IP Address |     | Destination | L4 Port(s) |
|     |          | Additional  | Parameters |     |             |            |
----------------------------------------------------------------------------
Inbound
|     | IPv6 | V6_INPUT_FILTER |     |     |     |     |
| --- | ---- | --------------- | --- | --- | --- | --- |
10
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 79

deny
1001::2
2001::2
Logging: enabled
Hit-counts: enabled

20

permit
any
any

any

any

----------------------------------------------------------------------------

ACL configuration examples | 80

Chapter 4

Classifier policies

Classifier policies

Classifier policies let a network administrator define sets of rules based on network traffic addressing or
other header content, and use these rules to restrict or alter the passage of traffic through the switch.
Choosing the rule criteria is called Classification, and one such rule, or list, is called a policy. Classification is
achieved by creating a traffic class. The types of classes (MAC, IPv4, and IPv6) are each focused on relevant
frame/packet characteristics. Classes can be configured to match or ignore almost any frame or packet
header field. Network traffic passing through a switch can be classified based on many different
frame/packet characteristics including, but not limited to:

n Frame ingress VLAN ID

n Source and/or destination Ethernet MAC, IPv4, or IPv6 address

n Layer 2 (EtherType) and Layer 3 (IP) protocol

n Layer 4 application ports

A policy contains one or more policy entries, which are listed according to priority by sequence number. A
single policy entry contains a class and corresponding policy action. Policy action is taken on traffic matched
by its corresponding class. A policy can be applied to an individual front plane port, a Link Aggregation Group
(LAG) interface, or a VLAN.

See also ACL and Policy hardware resource considerations.

Traffic policing
Traffic policing supports policing of the inbound traffic. A typical application of traffic policing is to supervise
the specification of traffic entering a network and limit it within a reasonable range. Another application is to
"discipline" the extra traffic to prevent aggressive use of network resources by an application. For example,
you can limit bandwidth for HTTP packets to less than 50% of the total. If the traffic of a session exceeds the
limit, traffic policing can drop the packets or reset the IP precedence of the packets. In the following
illustrated example, outbound traffic is policed:

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

81

Traffic policing is widely used in policing traffic entering the ISP networks. It can classify the policed traffic
and take predefined policing actions on each packet depending on the evaluation result:

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

n Priority Code Point (PCP): 3-bit field in layer 2 802.1Q header refers to a class of service and maps to a

frame priority level.

n IP precedence: 3-bit field in IP header which denotes the importance or priority of the datagram.

n IP Differentiated Services Code Point (DSCP): 6-bit field in IP header for packet classification.

n Local Priority: Change the internal priority used to queue the packets for transmission. Local priority
can be used to rewrite the priority of traffic classes local to the system based on the QoS mapping
settings without changing the IP header or the 802.1Q header. Remark actions other than local priority
only change packets as they leave the switch. The local priority action can be combined with the other
remark actions to remark packets and change the internal priority to reflect the new priority.

Police actions

Traffic policing meters inbound traffic on an interface or VLAN based on the following traffic parameters:

Classifier policies | 82

n Committed information rate (CIR): Bandwidth limit for guaranteed traffic.

n Committed burst size (CBS): Maximum packet size permitted for bursts of data that exceed the CIR.

Based on these parameters, packets are dropped when traffic exceeds the bandwidth limit (CIR) and the
burst size for guaranteed traffic (CBS).

Other actions

Other actions include Drop: Drop the packet, and Mirror: Mirror the packets to a specified mirroring session.
For details, see the Monitoring Guide.

How policy matching works
A policy can be applied to an interface or VLAN to affect/control traffic arriving on that interface or VLAN
(inbound (ingress)). A single policy entry matches on one or more characteristics of the particular traffic type
and has a configured action to continue through the switch. This matching occurs by beginning with the
entry with the lowest sequence number. The entry is then compared against the incoming frame to its
particular match characteristics. If there is a match, the action is taken.

If there is no match, the match characteristics of the next sequence are compared to the relevant
frame/packet details. If there is a match, the specified actions are taken. This process continues until a
match is found; otherwise, the packet is permitted to flow through the switch unaltered. The "implicit
permit" behavior of policy matching differs from the "implicit deny" behavior of ACL matching.

Active class configuration versus user-specified
configuration
The output of the show class command displays the active class configurations. Active class configurations
are the classes that have been configured and accepted by the system.

The output of the show class command with the configuration parameter, displays the classes that have
been configured by the user.

Discrepancies might occur between the active class configurations and the user-specified configurations. In
the user-specified class configurations, unsupported command parameters may have been configured, or
class can be modified after policy application and may have been unsuccessful due to lack of hardware
resources.

To determine if a discrepancy exists between what was configured and what is active, run any variant of the
show class command. If the active classes and configured classes are not the same, a warning message is
displayed.

! class MY_CLASS user configuration does not match active configuration.
! run 'class TYPE NAME reset' to reset class to match active configuration.

If the configured class is processing and you entered the show class command with parameters, the
following in-progress message is displayed:

! class ip MY_CLASS user configuration currently being processed
! run 'class TYPE NAME reset' to reset class to match active configuration.

If the configured class is processing and you entered the show class command without parameters, the
following in-progress message is displayed:

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

83

% Warning: MY_CLASS user configuration currently being processed
% run 'class TYPE NAME reset' to reset class to match active configuration.

If the warning message or in-progress message is displayed, additional changes may be made until the error
message is no longer displayed. Or you can use the class {all|ip <class-name>|ipv6 <class-
name>|mac <class-name>} reset command to change the user-specified configuration to match the active
configuration.

The show running-config command also shows a warning about classes that are in progress or failed.

Example

Resetting the user-specified class configuration to the active configuration:

switch(config)# class all reset

Active policy configuration versus user-specified
configuration
The output of the show policy command displays the active policy configurations. Active policy
configurations are the policies that have been configured and accepted by the system. With applied policies,
the active configuration displays the interfaces on which the policies have successfully been programmed in
hardware.

The output of the show policy command with the configuration parameter, displays the policies that
have been configured by the user.

Discrepancies might exist between the active policy configurations and the user-specified configurations. In
the user-specified policy configurations, unsupported command parameters might have been configured,
or an application of a policy might have been unsuccessful because of a lack of hardware resources.

To determine if a discrepancy exists between the configuration and what is active, run any variant of the
show policy command. If the active policies and configured policies are not the same, a warning message is
displayed in the output of the show command.

! policy MY_POLICY user configuration does not match active configuration.
! run 'policy NAME reset' to reset policy to match active configuration.

The switch displays an in progress message while it processes the configured policy:

! policy MY_POLICY user configuration currently being processed
! run 'policy NAME reset' to reset policy to match active configuration.

If the warning message or in progress message is displayed, additional changes may be made until the error
message is no longer displayed. Or you can use the policy <policy-name> reset command to change the
user-specified configuration to match the active configuration.

Example

Resetting MY_POLICY:

Classifier policies | 84

| switch(config)# | policy | MY_POLICY   | reset |     |     |     |     |
| --------------- | ------ | ----------- | ----- | --- | --- | --- | --- |
| Classifier      | policy | commands    |       |     |     |     |     |
| Classifier      | policy | application |       |     |     |     |     |
Classifierpoliciescanbeappliedasfollows("Rt-In"="Routed-In"):
| Policy    | IPv4 |      | IPv6 |             |        |        |         |
| --------- | ---- | ---- | ---- | ----------- | ------ | ------ | ------- |
|           | IPv4 | IPv4 | IPv6 | IPv6 IPv4+6 | IPv4+6 | IPv4+6 | MAC MAC |
| type      | Rt-  |      | Rt-  |             |        |        |         |
|           | In   | Out  | In   | Out In      | Rt-In  | Out    | In Out  |
| Direction | In   |      | In   |             |        |        |         |
| L2        | Yes  | Yes  | Yes  | Yes Yes     |        | Yes    | Yes Yes |
interface
(port)
| L2LAG | Yes     | Yes | Yes     | Yes Yes |     | Yes | Yes Yes |
| ----- | ------- | --- | ------- | ------- | --- | --- | ------- |
| L3    | Yes Yes | Yes | Yes Yes | Yes Yes | Yes | Yes | Yes Yes |
interface
(port)
| L3LAG     | Yes Yes | Yes | Yes Yes | Yes Yes | Yes   | Yes | Yes Yes |
| --------- | ------- | --- | ------- | ------- | ----- | --- | ------- |
| VLAN      | Yes     | Yes | Yes     | Yes Yes |       | Yes | Yes Yes |
| VLAN      | Yes     |     | Yes     |         | Yes   |     |         |
| interface | (PBR)   |     | (PBR)   |         | (PBR) |     |         |
Thefollowingmatchcriteriaisnotsupported.Ifthismatchcriteriaisattemptedtobeconfigured,anerror
messagewillbedisplayedandtheactionwillnotbecompleted.
| PCP on       | MAC classes |         |     |     |     |     |     |
| ------------ | ----------- | ------- | --- | --- | --- | --- | --- |
| apply policy | (Context:   | config) |     |     |     |     |     |
Syntax
| apply policy    | <POLICY-NAME> | in  |     |     |     |     |     |
| --------------- | ------------- | --- | --- | --- | --- | --- | --- |
| no apply policy | <POLICY-NAME> | in  |     |     |     |     |     |
Description
Appliesapolicytotheglobalconfigcontext.
Onlyonepolicycanbegloballyappliedatatime.Applyingapolicygloballyagain,replacestheprevious
globallyappliedpolicy.
Thenoformofthiscommandremovesapplicationoftheglobalpolicy.
Commandcontext
config
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 85

Parameters
<POLICY-NAME>
Specifiesthepolicytoapply.
in
Selectstheinbound(ingress)trafficdirection.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Applyingpolicyglobal1totheglobalconfigcontext:
| switch(config)# |     | apply | policy | global1 in |
| --------------- | --- | ----- | ------ | ---------- |
Removingapplicationofpolicyglobal1fromtheglobalconfigcontext:
| switch(config)# |     | no apply | policy | global1 in |
| --------------- | --- | -------- | ------ | ---------- |
apply policy (Contexts: config-if, config-if-vlan, config-vlan)
Syntax
| Context: config-if:      |               |               |                    |                    |
| ------------------------ | ------------- | ------------- | ------------------ | ------------------ |
| apply policy             | <POLICY-NAME> |               | {in|out|routed-in} |                    |
| no apply policy          |               | <POLICY-NAME> |                    | {in|out|routed-in} |
| Context: config-if-vlan: |               |               |                    |                    |
| apply policy             | <POLICY-NAME> |               | routed-in          |                    |
| no apply policy          |               | <POLICY-NAME> |                    | routed-in          |
| Context: config-vlan:    |               |               |                    |                    |
| apply policy             | <POLICY-NAME> |               | {in|out}           |                    |
| no apply policy          |               | <POLICY-NAME> |                    | {in|out}           |
Description
AppliesapolicytothecurrentinterfaceorVLANcontext.
OnlyonedirectionofapolicycanbeappliedtoaninterfaceorVLANatatime,thususingtheapply
commandonaninterfaceorVLANwithanalready-appliedpolicyofthesamedirectionwillreplacethe
currentlyappliedpolicy.
TheVLANcontextsupportstheinandoutdirections,whichapplytobothbridgedandroutedtraffic.The
InterfaceVLANcontextonlysupportstherouted-indirectionwhichappliesonlytoroutedtraffic.
ThenoformofthiscommandremovesapolicyfromtheinterfaceorVLANspecifiedbythecurrentcontext.
Commandcontext
config-if
config-if-vlan
config-vlan
Parameters
Classifierpolicies|86

<POLICY-NAME>
Specifiesthepolicytoapply.
in
Selectstheinbound(ingress)trafficdirection.
out
Selectstheoutbound(egress)trafficdirection.
routed-in
Selectsroutedintraffic.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage (appliestoconfig-vlancontext)
OnlyonepolicymaybeappliedtoaVLANatatime.Therefore,usingtheapply policycommandona
n
VLANwithanalready-appliedpolicyofthesametype,willreplacetheappliedpolicy.
6400SwitchSeriesonly:WhenapolicyisappliedtoaVLAN,itwillcreatehardwareentriesonalllinecards
n
andstackmembersregardlessofwhetheraVLANmemberexistsonanyspecificlinecard.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Applyingapolicytoaninterface(ingress):
| switch(config)#    | interface | 1/1/1  |           |     |     |
| ------------------ | --------- | ------ | --------- | --- | --- |
| switch(config-if)# | apply     | policy | MY_POLICY | in  |     |
Applyingapolicytoaninterface(egress):
| switch(config)#    | interface | 1/1/2  |            |     |     |
| ------------------ | --------- | ------ | ---------- | --- | --- |
| switch(config-if)# | apply     | policy | MY_POLICY2 | out |     |
Applyingapolicytoaninterfacerange(egress):
| switch(config)#                  | interface | 1/1/2-1/1/5 |       |                   |     |
| -------------------------------- | --------- | ----------- | ----- | ----------------- | --- |
| switch(config-if-<1/1/2-1/1/5>)# |           |             | apply | policy MY_POLICY3 | out |
Removingapolicyfromaninterfacerange(egress)
| switch(config)# | 1/1/2-1/1/5 |     |     |     |     |
| --------------- | ----------- | --- | --- | --- | --- |
switch(config-if)#
|     | no  | apply policy | MY_POLICY3 | out |     |
| --- | --- | ------------ | ---------- | --- | --- |
ApplyingapolicytoaVLAN(ingress):
| switch(config)#         | vlan | 10    |                  |     |     |
| ----------------------- | ---- | ----- | ---------------- | --- | --- |
| switch(config-vlan-10)# |      | apply | policy MY_POLICY | in  |     |
ApplyingapolicytomultipleVLANs(egress):
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 87

| switch(config)# |     | vlan | 20,30 |     |     |     |     |
| --------------- | --- | ---- | ----- | --- | --- | --- | --- |
switch(config-vlan-<20,30>)#
|     |     |     |     | apply | policy | MY_POLICY2 | out |
| --- | --- | --- | --- | ----- | ------ | ---------- | --- |
ApplyingapolicytoaninterfaceVLANrangerouted(ingress):
| switch(config)#               |     | vlan | 2-5 |       |        |            |           |
| ----------------------------- | --- | ---- | --- | ----- | ------ | ---------- | --------- |
| switch(config-if-vlan-<2-5>)# |     |      |     | apply | policy | MY_POLICY3 | routed-in |
RemovingapolicyfromaVLAN(ingress):
| switch(config)#         |     | vlan | 10  |              |     |           |     |
| ----------------------- | --- | ---- | --- | ------------ | --- | --------- | --- |
| switch(config-vlan-10)# |     |      | no  | apply policy |     | MY_POLICY | in  |
class copy
Syntax
| class {ip|ipv6|mac} |     | <CLASS-NAME> |     | copy | <DESTINATION-CLASS> |     |     |
| ------------------- | --- | ------------ | --- | ---- | ------------------- | --- | --- |
Description
Copiesaclasstoanewdestinationclassoroverwritesanexistingclass.Copyingaclasscopiesallentriesas
well.
Commandcontext
config
Parameters
<CLASS-NAME>
{ip|ipv6|mac}
Specifiesthetypeandnameoftheclasstobecopied.
<DESTINATION-CLASS>
Specifiesthenameofthedestinationclass.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CopyinganIPv4class.Copyingaclasswithentriescopiesallitsentriesaswell:
| switch(config)# |             | class   | ip MY_IP_CLASS |         | copy | MY_IP_CLASS2 |            |
| --------------- | ----------- | ------- | -------------- | ------- | ---- | ------------ | ---------- |
| switch(config)# |             | do show | class          |         |      |              |            |
| Type            | Name        |         |                |         |      |              |            |
| Sequence        | Comment     |         |                |         |      |              |            |
|                 | Action      |         |                |         |      | L3 Protocol  |            |
|                 | Source      | IP      | Address        |         |      | Source       | L4 Port(s) |
|                 | Destination |         | IP             | Address |      | Destination  | L4 Port(s) |
|                 | Additional  |         | Parameters     |         |      |              |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_CLASS |     |     |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- | --- |
| 11   | ignore      |     |     |     |     | udp |     |
any
any
Classifierpolicies|88

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
| switch(config)# | class       | ipv6       | MY_IPV6_CLASS | copy MY_IPV6_CLASS2 |            |
| --------------- | ----------- | ---------- | ------------- | ------------------- | ---------- |
| switch(config)# | do          | show       | class         |                     |            |
| Type            | Name        |            |               |                     |            |
| Sequence        | Comment     |            |               |                     |            |
|                 | Action      |            |               | L3 Protocol         |            |
|                 | Source      | IP Address |               | Source              | L4 Port(s) |
|                 | Destination | IP         | Address       | Destination         | L4 Port(s) |
|                 | Additional  | Parameters |               |                     |            |
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
| switch(config)# | class       | mac         | MY_MAC_CLASS | copy MY_MAC_CLASS2 |     |
| --------------- | ----------- | ----------- | ------------ | ------------------ | --- |
| switch(config)# | do          | show        | class        |                    |     |
| Type            | Name        |             |              |                    |     |
| Sequence        | Comment     |             |              |                    |     |
|                 | Action      |             |              | EtherType          |     |
|                 | Source      | MAC Address |              |                    |     |
|                 | Destination | MAC         | Address      |                    |     |
|                 | Additional  | Parameters  |              |                    |     |
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
any
any
class ip
Syntax
SyntaxtocreateanIPv4classandenteritscontext.Plussyntaxtoremoveaclass:
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 89

class ip <CLASS-NAME>

no class ip <CLASS-NAME>

Syntax (within the class context) for creating or removing class entries for protocols ah, gre, esp, igmp, ospf,
pim (ip is available as an alias for any):

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
[urg] [ack] [psh] [rst] [syn] [fin] [established]
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

[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

no <SEQUENCE-NUMBER> comment

Description

Creates or modifies an IPv4 traffic class to match specified packets. Class is composed of one or more class
entries ordered and prioritized by sequence numbers. With this command, the class can classify traffic
based on IPv4 header information.

The no form of the command can be used to delete either an IPv4 traffic class (use no with the class
command) or an individual IPv4 traffic class entry (use no with the sequence number).

Command context

config

The class ip <CLASS-NAME> command takes you into the config-class-ip context where you enter the
class entries.

Parameters

ip

Classifier policies | 90

Specifies create or modify an IPv4 class.

<CLASS-NAME>

Specifies the name of this class.

<SEQUENCE-NUMBER>

Specifies a sequence number for the class entry. Optional. Range: 1-4294967295.

{match|ignore}

Creates a rule to match or ignore specified packets.

<IP-PROTOCOL-NUM>

Specifies the protocol as its Internet Protocol number. For example, 2 corresponds to the IGMP protocol.
Range: 0 to 255.

{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}

Specifies the source IPv4 address.

n any - specifies any source IPv4 address.

n <SRC-IP-ADDRESS> - specifies the source IPv4 host address.

o <PREFIX-LENGTH> - specifies the address bits to mask (CIDR subnet mask notation). Range: 1 to 32.

o <SUBNET-MASK> - specifies the address bits to mask (dotted decimal notation).

{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}

Specifies the destination IPv4 address.

n any - specifies any destination IPv4 address.

n <DST-IP-ADDRESS> - specifies the destination IPv4 host address.

o <PREFIX-LENGTH> - specifies the address bits to mask (CIDR subnet mask notation). Range: 1 to 32.

o <SUBNET-MASK> - specifies the address bits to mask (dotted decimal notation).

[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>]

Specifies the port or port range. Port numbers are in the range of 0 to 65535.

n eq <PORT> - specifies the Layer 4 port.

n gt <PORT> - specifies any Layer 4 port greater than the indicated port.

n lt <PORT> - specifies any Layer 4 port less than the indicated port.

n range <MIN-PORT> <MAX-PORT> - specifies the Layer 4 port range.

urg

Specifies matching on the TCP Flag: Urgent.

ack

Specifies matching on the TCP Flag: Acknowledgment.

psh

Specifies matching on the TCP Flag: Push buffered data to receiving application.

rst

Specifies matching on the TCP Flag: Reset the connection.

syn

Specifies matching on the TCP Flag: Synchronize sequence numbers.

fin

Specifies matching on the TCP Flag: Finish connection.

established

Specifies matching on the TCP Flag: Established connection.

dscp <DSCP-SPECIFIER>

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

91

Specifies the Differentiated Services Code Point (DSCP), either a numeric <DSCP-VALUE> (0 to 63) or one
of these keywords:

n AF11 - DSCP 10 (Assured Forwarding Class 1, low drop probability)

n AF12 - DSCP 12 (Assured Forwarding Class 1, medium drop probability)

n AF13 - DSCP 14 (Assured Forwarding Class 1, high drop probability)

n AF21 - DSCP 18 (Assured Forwarding Class 2, low drop probability)

n AF22 - DSCP 20 (Assured Forwarding Class 2, medium drop probability)

n AF23 - DSCP 22 (Assured Forwarding Class 2, high drop probability)

n AF31 - DSCP 26 (Assured Forwarding Class 3, low drop probability)

n AF32 - DSCP 28 (Assured Forwarding Class 3, medium drop probability)

n AF33 - DSCP 30 (Assured Forwarding Class 3, high drop probability)

n AF41 - DSCP 34 (Assured Forwarding Class 4, low drop probability)

n AF42 - DSCP 36 (Assured Forwarding Class 4, medium drop probability)

n AF43 - DSCP 38 (Assured Forwarding Class 4, high drop probability)

n CS0 - DSCP 0 (Class Selector 0: Default)

n CS1 - DSCP 8 (Class Selector 1: Scavenger)

n CS2 - DSCP 16 (Class Selector 2: OAM)

n CS3 - DSCP 24 (Class Selector 3: Signaling)

n CS4 - DSCP 32 (Class Selector 4: Realtime)

n CS5 - DSCP 40 (Class Selector 5: Broadcast video)

n CS6 - DSCP 48 (Class Selector 6: Network control)

n CS7 - DSCP 56 (Class Selector 7)

n EF - DSCP 46 (Expedited Forwarding)

ecn <ECN-VALUE>

Specifies an Explicit Congestion Notification value. Range: 0 to 3.

ip-precedence <IP-PRECEDENCE-VALUE>

Specifies an IP precedence value. Range: 0 to 7.

tos <TOS-VALUE>

Specifies the Type of Service value. Range: 0 to 31.

fragment

Specifies a fragment packet.

vlan <VLAN-ID>

Specifies VLAN tag to match on. 802.1Q VLAN ID.

This parameter cannot be used in any class that will be applied to a VLAN.

ttl <TTL-VALUE>

Specifies a time-to-live (hop limit) value. Range: 0 to 255.

count

Keeps the hit counts of the number of packets matching this class entry.

[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

Adds a comment to a class entry. The no form removes only the comment from the class entry.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Classifier policies | 92

Enteringanexisting<CLASS-NAME>valuewillcausetheexistingclasstobemodified,withanynew
n
<SEQUENCE-NUMBER>valuecreatinganadditionalclassentry,andanyexisting<SEQUENCE-NUMBER>value
replacingtheexistingclassentrywiththesamesequencenumber.
n Ifnosequencenumberisspecified,anewclassentrywillbeappendedtotheendoftheclasswitha
sequencenumberequaltothehighestclassentrycurrentlyinthelistplus10.
n Ifthe<IP-PROTOCOL-NUM>parameterisusedinsteadofaprotocolname,ensurethatanyneededclass
entry-definitionparametersspecifictotheselectedprotocolarealsoprovided.
Examples
CreatinganIPv4classwiththreeentries:
| switch(config)#          | class       | ip MY_IP_CLASS |                 |             |             |
| ------------------------ | ----------- | -------------- | --------------- | ----------- | ----------- |
| switch(config-class-ip)# |             | 10 match       | icmp any        | any         |             |
| switch(config-class-ip)# |             | 20 ignore      | udp any         | any         |             |
| switch(config-class-ip)# |             | 30 match       | tcp 192.168.0.1 |             | 192.168.0.2 |
| switch(config-class-ip)# |             | exit           |                 |             |             |
| switch(config)#          | do          | show class     |                 |             |             |
| Type                     | Name        |                |                 |             |             |
| Sequence                 | Comment     |                |                 |             |             |
|                          | Action      |                |                 | L3 Protocol |             |
|                          | Source      | IP Address     |                 | Source      | L4 Port(s)  |
|                          | Destination | IP Address     |                 | Destination | L4 Port(s)  |
|                          | Additional  | Parameters     |                 |             |             |
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
| IPv4 | MY_IP_CLASS |     |     |      |     |
| ---- | ----------- | --- | --- | ---- | --- |
|      | 10 match    |     |     | icmp |     |
any
any
|     | 20 ignore |     |     | udp |     |
| --- | --------- | --- | --- | --- | --- |
any
any
30 myipClass
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 93

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
ReplacinganIPv4classentryinanexistingclass:
| switch(config)#          | class | ip MY_IP_CLASS |         |     |
| ------------------------ | ----- | -------------- | ------- | --- |
| switch(config-class-ip)# |       | 10 match igmp  | any any |     |
switch(config-class-ip)#
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
Classifierpolicies|94

| switch(config)# | class | ip MY_IP_CLASS |     |     |
| --------------- | ----- | -------------- | --- | --- |
switch(config-class-ip)#
no 10
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
| IPv4 | MY_IP_CLASS |     |     |     |
| ---- | ----------- | --- | --- | --- |
20 ignore udp
any
any
30 match tcp
192.168.0.1
192.168.0.2
RemovinganIPv4class.Removingaclasswithentriesremovesallitsentriesaswell.Ifaclassassociated
withapolicyentry(ormultiplepolicyentries)isremoved,thecorrespondingentriesarealsoremoved.
Thecorrespondingentriesareonlyremovediftheclassisunusedbyallpolicyentries.
| switch(config)# | no     | class ip MY_IP_CLASS |     |     |
| --------------- | ------ | -------------------- | --- | --- |
| switch(config)# | do     | show class           |     |     |
| No Class        | found. |                      |     |     |
class ipv6
Syntax
SyntaxtocreateanIPv6classandenteritscontext.Plussyntaxtoremoveaclass:
| class ipv6    | <CLASS-NAME> |     |     |     |
| ------------- | ------------ | --- | --- | --- |
| no class ipv6 | <CLASS-NAME> |     |     |     |
Syntax(withintheclasscontext)forcreatingorremovingclassentriesforprotocolsah,gre,esp,igmp,ospf,
pim(ipv6isavailableasanaliasforany):
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
| [{eq|gt|lt} | <PORT>|range | <MIN-PORT> | <MAX-PORT>] |     |
| ----------- | ------------ | ---------- | ----------- | --- |
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
| [{eq|gt|lt} | <PORT>|range | <MIN-PORT>  | <MAX-PORT>]   |     |
| ----------- | ------------ | ----------- | ------------- | --- |
| [urg] [ack] | [psh] [rst]  | [syn] [fin] | [established] |     |
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 95

[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count]

no <SEQUENCE-NUMBER>

Syntax (within the class context) for creating or removing class entries for protocol icmpv6:

[<SEQUENCE-NUMBER>]
{permit|deny}
{icmpv6}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
[icmp-type {echo|echo-reply|<ICMP-TYPE-VALUE>}] [icmp-code <ICMP-CODE-VALUE>]
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count]

no <SEQUENCE-NUMBER>

Syntax (within the class context) for class entry comments:

[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

no <SEQUENCE-NUMBER> comment

Description

Creates or modifies an IPv6 traffic class to match specified packets. Class is composed of one or more class
entries ordered and prioritized by sequence numbers. With this command, each class can classify traffic
based on IPv6 header information.

The no form of the command deletes either an IPv6 traffic class (use no with the class command) or an
individual IPv6 traffic class entry (use no with the sequence number).

Command context

config

The class ipv6 <CLASS-NAME> command takes you into the config-class-ipv6 command context where
you enter the class entries.

Parameters

ipv6

Specifies create or modify an IPv6 class.

<CLASS-NAME>

Specifies the name of this class.

<SEQUENCE-NUMBER>

Specifies a sequence number for the class entry. Optional. Range: 1-4294967295.

{match|ignore}

Creates a rule to match or ignore specified packets.

<IP-PROTOCOL-NUM>

Specifies the protocol as its Internet Protocol number. For example, 2 corresponds to the IGMP
protocol. Range: 0 to 255.

{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}

Specifies the source IPv6 address.

n any - specifies any source IPv6 address.

n <SRC-IP-ADDRESS> - specifies the source IPv4 host address.

o <PREFIX-LENGTH> - specifies the address bits to mask (CIDR subnet mask notation). Range: 1 to

32.

o <SUBNET-MASK> - specifies the address bits to mask (dotted decimal notation).

{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}

Classifier policies | 96

Specifies the destination IPv4 address.

n any - specifies any destination IPv6 address.

n <DST-IP-ADDRESS> - specifies the destination IPv6 host address.

o <PREFIX-LENGTH> - specifies the address bits to mask (CIDR subnet mask notation). Range: 1 to 32.

o <SUBNET-MASK> - specifies the address bits to mask (dotted decimal notation).

[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>]

Specifies the port or port range. Port numbers are in the range of 0 to 65535.

n eq <PORT> - specifies the Layer 4 port.

n gt <PORT> - specifies any Layer 4 port greater than the indicated port.

n lt <PORT> - specifies any Layer 4 port less than the indicated port.

n range <MIN-PORT> <MAX-PORT> - specifies the Layer 4 port range.

urg, ack, psh, rst, syn, fin, established

These TCP flag matching parameters are not supported.

dscp <DSCP-SPECIFIER>

Specifies the Differentiated Services Code Point (DSCP), either a numeric <DSCP-VALUE> (0 to 63) or one
of these keywords:

n AF11 - DSCP 10 (Assured Forwarding Class 1, low drop probability)

n AF12 - DSCP 12 (Assured Forwarding Class 1, medium drop probability)

n AF13 - DSCP 14 (Assured Forwarding Class 1, high drop probability)

n AF21 - DSCP 18 (Assured Forwarding Class 2, low drop probability)

n AF22 - DSCP 20 (Assured Forwarding Class 2, medium drop probability)

n AF23 - DSCP 22 (Assured Forwarding Class 2, high drop probability)

n AF31 - DSCP 26 (Assured Forwarding Class 3, low drop probability)

n AF32 - DSCP 28 (Assured Forwarding Class 3, medium drop probability)

n AF33 - DSCP 30 (Assured Forwarding Class 3, high drop probability)

n AF41 - DSCP 34 (Assured Forwarding Class 4, low drop probability)

n AF42 - DSCP 36 (Assured Forwarding Class 4, medium drop probability)

n AF43 - DSCP 38 (Assured Forwarding Class 4, high drop probability)

n CS0 - DSCP 0 (Class Selector 0: Default)

n CS1 - DSCP 8 (Class Selector 1: Scavenger)

n CS2 - DSCP 16 (Class Selector 2: OAM)

n CS3 - DSCP 24 (Class Selector 3: Signaling)

n CS4 - DSCP 32 (Class Selector 4: Real time)

n CS5 - DSCP 40 (Class Selector 5: Broadcast video)

n CS6 - DSCP 48 (Class Selector 6: Network control)

n CS7 - DSCP 56 (Class Selector 7)

n EF - DSCP 46 (Expedited Forwarding)

ecn <ECN-VALUE>

Specifies an Explicit Congestion Notification value. Range: 0 to 3.

ip-precedence <IP-PRECEDENCE-VALUE>

Specifies an IP precedence value. Range: 0 to 7.

tos <TOS-VALUE>

Specifies the Type of Service value. Range: 0 to 31.

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

97

fragment
Specifiesafragmentpacket.
vlan <VLAN-ID>
SpecifiesVLANtagtomatchon.802.1QVLANID.
ThisparametercannotbeusedinanyclassthatwillbeappliedtoaVLAN.
ttl <TTL-VALUE>
Specifiesatime-to-live(hoplimit)value.Range:0to255.
count
Keepsthehitcountsofthenumberofpacketsmatchingthisclassentry.
| [<SEQUENCE-NUMBER>] | comment | <TEXT-STRING> |     |     |
| ------------------- | ------- | ------------- | --- | --- |
Addsacommenttoaclassentry.Thenoformremovesonlythecommentfromtheclassentry.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Ifyouenteranexisting<CLASS-NAME>value,theexistingclassismodifiedwithanynew<SEQUENCE-
n
NUMBER>value.Thisactioncreatesanadditionalclassentry.Anyexisting<SEQUENCE-NUMBER>value
replacestheexistingclassentrywiththesamesequencenumber.
n Ifnosequencenumberisspecified,anewclassentryisappendedtotheendoftheclasswithasequence
numberequaltothehighestclassentrycurrentlyinthelistplus10.
n Ifthe<IP-PROTOCOL-NUM>parameterisusedinsteadofaprotocolname,ensurethatanyneededclass
entry-definitionparametersspecifictotheselectedprotocolarealsoprovided.
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
Classifierpolicies|98

| switch(config)# | class | ipv6 | MY_IPV6_CLASS |     |     |     |
| --------------- | ----- | ---- | ------------- | --- | --- | --- |
switch(config-class-ipv6)#
|                            |             |            | 10 match   | icmpv6      | any any     |            |
| -------------------------- | ----------- | ---------- | ---------- | ----------- | ----------- | ---------- |
| switch(config-class-ipv6)# |             |            | 20 ignore  | udp         | any any     |            |
| switch(config-class-ipv6)# |             |            | 20 comment | myipv6class |             |            |
| switch(config-class-ipv6)# |             |            | exit       |             |             |            |
| switch(config)#            | do          | show       | class      |             |             |            |
| Type                       | Name        |            |            |             |             |            |
| Sequence                   | Comment     |            |            |             |             |            |
|                            | Action      |            |            |             | L3 Protocol |            |
|                            | Source      | IP Address |            |             | Source      | L4 Port(s) |
|                            | Destination | IP         | Address    |             | Destination | L4 Port(s) |
|                            | Additional  | Parameters |            |             |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |     |     |        |     |
| ---- | ------------- | --- | --- | --- | ------ | --- |
|      | 10 match      |     |     |     | icmpv6 |     |
any
any
20 myipv6class
|     | ignore |     |     |     | udp |     |
| --- | ------ | --- | --- | --- | --- | --- |
any
any
RemovingacommentfromanexistingIPv6classentry:
| switch(config)#            | class       | ipv6       | MY_IPV6_CLASS |     |             |            |
| -------------------------- | ----------- | ---------- | ------------- | --- | ----------- | ---------- |
| switch(config-class-ipv6)# |             |            | no 20 comment |     |             |            |
| switch(config-class-ipv6)# |             |            | exit          |     |             |            |
| switch(config)#            | do          | show       | class         |     |             |            |
| Type                       | Name        |            |               |     |             |            |
| Sequence                   | Comment     |            |               |     |             |            |
|                            | Action      |            |               |     | L3 Protocol |            |
|                            | Source      | IP Address |               |     | Source      | L4 Port(s) |
|                            | Destination | IP         | Address       |     | Destination | L4 Port(s) |
|                            | Additional  | Parameters |               |     |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |     |     |        |     |
| ---- | ------------- | --- | --- | --- | ------ | --- |
|      | 10 match      |     |     |     | icmpv6 |     |
any
any
|     | 20 ignore |     |     |     | udp |     |
| --- | --------- | --- | --- | --- | --- | --- |
any
any
ReplacinganIPv6classentryinanexistingIPv6class:
| switch(config)#            | class       | ipv6       | MY_IPV6_CLASS |     |             |            |
| -------------------------- | ----------- | ---------- | ------------- | --- | ----------- | ---------- |
| switch(config-class-ipv6)# |             |            | 10 match      | any | any 1020::  |            |
| switch(config-class-ipv6)# |             |            | exit          |     |             |            |
| switch(config)#            | do          | show       | class         |     |             |            |
| Type                       | Name        |            |               |     |             |            |
| Sequence                   | Comment     |            |               |     |             |            |
|                            | Action      |            |               |     | L3 Protocol |            |
|                            | Source      | IP Address |               |     | Source      | L4 Port(s) |
|                            | Destination | IP         | Address       |     | Destination | L4 Port(s) |
|                            | Additional  | Parameters |               |     |             |            |
-------------------------------------------------------------------------------
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 99

| IPv6 | MY_IPV6_CLASS |     |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- |
|      | 10 match      |     |     |     | any |     |
any
1020::
|     | 20 ignore |     |     |     | udp |     |
| --- | --------- | --- | --- | --- | --- | --- |
any
any
RemovinganIPv6classentry:
| switch(config)#            |     | class ipv6 | MY_IPV6_CLASS |     |     |     |
| -------------------------- | --- | ---------- | ------------- | --- | --- | --- |
| switch(config-class-ipv6)# |     |            | no 10         |     |     |     |
switch(config-class-ipv6)#
exit
| switch(config)# |             | do show    | class   |     |             |            |
| --------------- | ----------- | ---------- | ------- | --- | ----------- | ---------- |
| Type            | Name        |            |         |     |             |            |
| Sequence        | Comment     |            |         |     |             |            |
|                 | Action      |            |         |     | L3 Protocol |            |
|                 | Source      | IP Address |         |     | Source      | L4 Port(s) |
|                 | Destination | IP         | Address |     | Destination | L4 Port(s) |
|                 | Additional  | Parameters |         |     |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- |
|      | 20 ignore     |     |     |     | udp |     |
any
any
RemovinganIPv6class.Removingaclasswithentriesremovesallitsentriesaswell.Ifaclassassociated
withapolicyentry(ormultiplepolicyentries)isremoved,thecorrespondingentriesarealsoremoved.
Thecorrespondingentriesareonlyremovediftheclassisunusedbyallpolicyentries.
| switch(config)# |     | no class | ipv6 MY_IPV6_CLASS |     |     |     |
| --------------- | --- | -------- | ------------------ | --- | --- | --- |
switch(config)#
|          |        | do show | class |     |     |     |
| -------- | ------ | ------- | ----- | --- | --- | --- |
| No Class | found. |         |       |     |     |     |
class mac
Syntax
class mac <CLASS-NAME>
[<SEQUENCE-NUMBER>]
{match|ignore}
{any|<SRC-MAC-ADDRESS>[/<ETHERNET-MASK>}]}
{any|<DST-MAC-ADDRESS>[/<ETHERNET-MASK>}]}
{any|aarp|appletalk|arp|fcoe|fcoe-init|ip|ipv6|ipx-arpa|ipx-non-arpa|is-is|
lldp|mpls-multicast|mpls-unicast|q-in-q|rbridge|trill|wake-on-lan|
<NUMERIC-ETHERTYPE>}
| [pcp <PCP-VALUE>]   |     | [vlan   | <VLAN-ID>]    | [count] |     |     |
| ------------------- | --- | ------- | ------------- | ------- | --- | --- |
| [<SEQUENCE-NUMBER>] |     | comment | <TEXT-STRING> |         |     |     |
Description
Classifierpolicies|100

Creates or modifies a MAC traffic class to match specified packets. Class is composed of one or more class
entries ordered and prioritized by sequence numbers. With this command, each class can classify traffic
based on MAC header information.

The no form of the command can be used to delete either a MAC traffic class (use no with the class
command) or an individual MAC traffic class entry (use no with the sequence number).

Command context

config

The class mac <CLASS-NAME> command takes you into the config-class-mac context where you enter the
class entries.

Parameters

mac

Specifies create or modify a MAC class.

<CLASS-NAME>

Specifies the name of this class.

<SEQUENCE-NUMBER>

Specifies a sequence number for the class entry. Optional. Range: 1-4294967295.

{match|ignore}

Creates a rule to match or ignore specified packets.

comment

Stores the remaining entered text as a class comment.

{any|<SRC-MAC-ADDRESS>[/<ETHERNET-MASK>}]}

Specifies the source host MAC address (xxxx.xxxx.xxxx), OUI, or the keyword any. You can optionally
include the following:

<ETHERNET-MASK> - The address bits to mask (xxxx.xxxx.xxxx).

{any|<DST-MAC-ADDRESS>[/<ETHERNET-MASK>}]}

Specifies the destination host MAC address (xxxx.xxxx.xxxx), OUI, or the keyword any. You can
optionally include the following:

<ETHERNET-MASK> - The address bits to mask (xxxx.xxxx.xxxx).

Protocol

Select an ethertype protocol from the following (enter one only):

n any - Any ethertype protocol

n <NUMERIC-ETHERTYPE> - Enter an EtherType protocol number. Range: 0x600-0xffff.

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

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

101

o mpls-multicast
o mpls-unicast
o
q-in-q
o rbridge
o trill
o wake-on-lan
pcp <PCP-VALUE>
Notsupported.
vlan <VLAN-ID>
SpecifiesmatchingonaVLANID.EnteraVLANIDortheVLANname,ifconfigured.
ThisparametercannotbeusedinanyclassthatwillbeappliedtoaVLAN.
count
Keepsthehitcountsofthenumberofpacketsmatchingthisclassentry.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreatingaMACclass:
| switch(config)#           | class mac | MY_MAC_CLASS |             |
| ------------------------- | --------- | ------------ | ----------- |
| switch(config-class-mac)# |           | match any    | any lldp    |
| switch(config-class-mac)# |           | ignore       | any any arp |
| switch(config-class-mac)# |           | exit         |             |
| switch(config)#           | do show   | class        |             |
| Type Name                 |           |              |             |
| Sequence Comment          |           |              |             |
| Action                    |           |              | EtherType   |
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
| switch(config)#           | class mac | MY_MAC_CLASS |                |
| ------------------------- | --------- | ------------ | -------------- |
| switch(config-class-mac)# |           | 10 comment   | MY_CLASS_ENTRY |
| switch(config-class-mac)# |           | exit         |                |
| switch(config)#           | do show   | class        |                |
| Type Name                 |           |              |                |
| Sequence Comment          |           |              |                |
| Action                    |           |              | EtherType      |
Source MAC Address
| Destination |     | MAC Address |     |
| ----------- | --- | ----------- | --- |
Classifierpolicies|102

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
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 103

| switch(config-class-mac)# |     | exit |
| ------------------------- | --- | ---- |
switch(config)#
|                  | do show class |     |
| ---------------- | ------------- | --- |
| Type Name        |               |     |
| Sequence Comment |               |     |
Action EtherType
Source MAC Address
| Destination | MAC | Address |
| ----------- | --- | ------- |
Additional Parameters
-------------------------------------------------------------------------------
| MAC MY_MAC_CLASS |     |     |
| ---------------- | --- | --- |
2 ignore arp
any
any
RemovngaMACclass.Removingaclasswithentriesremovesallitsentriesaswell.Ifaclassassociatedwith
apolicyentry(ormultiplepolicyentries)isremoved,thecorrespondingentriesarealsoremoved.
Thecorrespondingentriesareonlyremovediftheclassisunusedbyallpolicyentries.
| switch(config)# | no class mac  | MY_MAC_CLASS |
| --------------- | ------------- | ------------ |
| switch(config)# | do show class |              |
| No Class found. |               |              |
class resequence
Syntax
class {ip|ipv6|mac} <CLASS-NAME> resequence <STARTING-SEQUENCE-NUMBER> <INCREMENT>
Description
ResequencenumberinginanIPv4,IPv6,orMACclass.
Commandcontext
config
Parameters
| {ip|ipv6|mac} <CLASS-NAME> |     |     |
| -------------------------- | --- | --- |
Specifiestheclasswhereyouwanttoresequenceclassentries.
<STARTING-SEQUENCE-NUMBER>
Specifiesthesequencenumbertostartresequencingfrom.
<INCREMENT>
Specifieshowmuchtoincrementthesequencenumbersby.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ResequencinganIPv4class:
Classifierpolicies|104

| switch(config)# | class | ip  | MY_IP_CLASS | resequence |     | 1 10 |
| --------------- | ----- | --- | ----------- | ---------- | --- | ---- |
switch(config)#
|          | do          | show       | class   |     |             |            |
| -------- | ----------- | ---------- | ------- | --- | ----------- | ---------- |
| Type     | Name        |            |         |     |             |            |
| Sequence | Comment     |            |         |     |             |            |
|          | Action      |            |         |     | L3 Protocol |            |
|          | Source      | IP Address |         |     | Source      | L4 Port(s) |
|          | Destination | IP         | Address |     | Destination | L4 Port(s) |
|          | Additional  | Parameters |         |     |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_CLASS |     |     |     |      |     |
| ---- | ----------- | --- | --- | --- | ---- | --- |
|      | 1 match     |     |     |     | igmp |     |
any
any
| 11  | ignore |     |     |     | udp |     |
| --- | ------ | --- | --- | --- | --- | --- |
any
any
| 21  | match |     |     |     | tcp |     |
| --- | ----- | --- | --- | --- | --- | --- |
192.168.0.1
192.168.0.2
ResequencinganIPv6class:
switch(config)#
|                            | class       | ipv6       | MY_IPV6_CLASS |     | resequence  | 1 1        |
| -------------------------- | ----------- | ---------- | ------------- | --- | ----------- | ---------- |
| switch(config-class-ipv6)# |             |            | exit          |     |             |            |
| switch(config)#            | do          | show       | class         |     |             |            |
| Type                       | Name        |            |               |     |             |            |
| Sequence                   | Comment     |            |               |     |             |            |
|                            | Action      |            |               |     | L3 Protocol |            |
|                            | Source      | IP Address |               |     | Source      | L4 Port(s) |
|                            | Destination | IP         | Address       |     | Destination | L4 Port(s) |
|                            | Additional  | Parameters |               |     |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- |
|      | 1 match       |     |     |     | any |     |
any
1020::
|     | 2 ignore |     |     |     | udp |     |
| --- | -------- | --- | --- | --- | --- | --- |
any
any
ResequencingaMACclass:
| switch(config)# | class | mac | MY_MAC_CLASS | resequence |     | 1 1 |
| --------------- | ----- | --- | ------------ | ---------- | --- | --- |
switch(config)#
|          | do          | show        | class   |     |           |     |
| -------- | ----------- | ----------- | ------- | --- | --------- | --- |
| Type     | Name        |             |         |     |           |     |
| Sequence | Comment     |             |         |     |           |     |
|          | Action      |             |         |     | EtherType |     |
|          | Source      | MAC Address |         |     |           |     |
|          | Destination | MAC         | Address |     |           |     |
|          | Additional  | Parameters  |         |     |           |     |
-------------------------------------------------------------------------------
| MAC | MY_MAC_CLASS |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- |
|     | 1 match      |     |     |     | any |     |
any
any
|     | 2 ignore |     |     |     | arp |     |
| --- | -------- | --- | --- | --- | --- | --- |
any
any
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 105

class reset

Syntax

class { all | ip <CLASS-NAME> | ipv6 <CLASS-NAME> |mac <CLASS-NAME> } reset

Description

Changes the user-specified class configuration to match the active class configuration. Use this command
when there is a discrepancy between what the user configured and what is active and accepted by the
system.

Command context

config

Parameters

{ all | ip <CLASS-NAME>| ipv6 <CLASS-NAME> |mac <CLASS-NAME> }

Specifies either all classes be reset or specifies the type (ip for IPv4, ipv6 for IPv6 or mac for MAC ACL)
and name of the class to be reset.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Resetting the user-specified configuration to the active configuration:

switch(config)# class all reset

clear policy hitcounts

Syntax

clear policy hitcounts { all | [<POLICY-NAME>] [[interface <IF-NAME> [in|out|routed-in]] |
[vlan <VLAN-ID> [in|out]]] | global }

Description

Clears the policy hit count statistics.

Command context

Operator (>) or Manager (#)

Parameters

all

Selects all policies.

<POLICY-NAME>

Specifies the policy name.

interface <IF-NAME>

Specifies the interface name.

vlan <VLAN-ID>

Specifies the VLAN.

in

Specifies the inbound (ingress) traffic direction.

Classifier policies | 106

out

Selects the outbound (egress) traffic direction.

routed-in

Selects the routed in traffic direction. Not applicable to a policy applied to a VLAN.

global

Selects the globally applied policy.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

On the 6400 Switch Series, interface identification differs.

Clearing policy hit counts and then showing the policy hit counts (statistics):

switch# clear policy hitcounts my_policy int 1/1/1 in
switch# show policy hitcounts my_policy
Statistics for Policy my_policy:
Interface 1/1/1* (in):

Hit Count Configuration

10 class ipv6 my_class1 action dscp af21 action drop

0 10 match any any any count

* policy statistics are shared among each context type (interface, VLAN).

For routed ingress, they are only shared within the same VRF.
Use 'policy NAME copy' to create a new policy for separate statistics.

Clearing the globally applied policy hit counts and then showing the global policy hit counts (statistics):

switch# clear policy hitcounts global
switch# show policy hitcounts global
Statistics for Policy global1:
Global Policy:

Hit Count Configuration

10 class ipv6 my_class1 action mirror

0 10 match any any any count

* policy statistics are shared among each context type (interface, VLAN).

For routed ingress, they are only shared within the same VRF.
Use 'policy NAME copy' to create a new policy for separate statistics.

Clearing hit counts for policy MY_IPv6_Policy applied to VLAN 10 (ingress):

switch# clear policy hitcounts My_IPv6_Policy vlan 10 in

Clearing hit counts for all policies:

switch# clear policy hitcounts all

policy

Syntax

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

107

policy <POLICY-NAME>

[<SEQUENCE-NUMBER>]
class {ip|ipv6|mac} <CLASS-NAME>

action {<REMARK-ACTIONS> | <POLICE-ACTIONS> | <OTHER-ACTIONS>}
[{<REMARK-ACTIONS> | <POLICE-ACTIONS> | <OTHER-ACTIONS>}]

[<SEQUENCE-NUMBER>]
comment ...

Description

Creates or modifies classifier policy and policy entries. A policy is made up of one or more policy entries
ordered and prioritized by sequence numbers. Each entry has an IPv4/IPv6/MAC class and zero or more
policy actions associated with it.

A policy must be applied using the apply command.

The no form of the command can be used to delete either a policy (use no with the policy command) or an
individual policy entry (use no with the sequence number).

Command context

config

The policy command takes you into the config-policy context where you enter the policy entries.

Parameters

<POLICY-NAME>

Specifies the name of the policy.

<SEQUENCE-NUMBER>

Specifies a sequence number for the policy entry. Optional. Range: 1 to 4294967295.

comment

Stores the remaining entered text as a policy entry comment.

class {ip|ipv6|mac} <CLASS-NAME>

Specifies a type of class, ip for IPv4, ipv6 for IPv6 and mac for a MAC policy. And specifies a class name.

<REMARK-ACTIONS>

Remark actions can be any of the following options: {pcp <PRIORITY> | ip-precedence <IP-
PRECEDENCE_VALUE> | dscp <DSCP-VALUE> | local-priority <LOCAL-PRIORITY-VALUE>} where:
pcp <PCP-VALUE>

Specifies the Priority Code Point (PCP) value. Range: 0 to 7.

ip-precedence <IP-PRECEDENCE-VALUE>

Specifies the numeric IP precedence value. Range: 0 to 7.

dscp <DSCP-VALUE>

Specifies a Differentiated Services Code Point (DSCP) value. Enter either a numeric value (0 to 63) or a
keyword as follows:

n AF11 - DSCP 10 (Assured Forwarding Class 1, low drop probability)

n AF12 - DSCP 12 (Assured Forwarding Class 1, medium drop probability)

n AF13 - DSCP 14 (Assured Forwarding Class 1, high drop probability)

n AF21 - DSCP 18 (Assured Forwarding Class 2, low drop probability)

n AF22 - DSCP 20 (Assured Forwarding Class 2, medium drop probability)

n AF23 - DSCP 22 (Assured Forwarding Class 2, high drop probability)

n AF31 - DSCP 26 (Assured Forwarding Class 3, low drop probability)

n AF32 - DSCP 28 (Assured Forwarding Class 3, medium drop probability)

Classifier policies | 108

n AF33 - DSCP 30 (Assured Forwarding Class 3, high drop probability)

n AF41 - DSCP 34 (Assured Forwarding Class 4, low drop probability)

n AF42 - DSCP 36 (Assured Forwarding Class 4, medium drop probability)

n AF43 - DSCP 38 (Assured Forwarding Class 4, high drop probability)

n CS0 - DSCP 0 (Class Selector 0: Default)

n CS1 - DSCP 8 (Class Selector 1: Scavenger)

n CS2 - DSCP 16 (Class Selector 2: OAM)

n CS3 - DSCP 24 (Class Selector 3: Signaling)

n CS4 - DSCP 32 (Class Selector 4: Real time)

n CS5 - DSCP 40 (Class Selector 5: Broadcast video)

n CS6 - DSCP 48 (Class Selector 6: Network control)

n CS7 - DSCP 56 (Class Selector 7)

n EF - DSCP 46 (Expedited Forwarding)

local-priority <LOCAL-PRIORITY-VALUE>

Specifies a local priority value. Range: 0 to 7.

<POLICE-ACTIONS>

Police actions can be the following {cir <RATE-BPS> cbs <BYTES> exceed} where:
cir kbps <RATE-KBPS>

Specifies a Committed Information Rate value in Kilobits per second. Range: 1 to 4294967295.

cbs <BYTES>

Specifies a Committed Burst Size value in bytes. Range: 1 to 4294967295.

exceed

Specifies action to take on packets that exceed the rate limit.

<OTHER-ACTIONS>

Other actions can be the following:
drop

Specifies drop traffic.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n An applied policy will process a packet sequentially against policy entries in the list until the last policy

entry in the list has been evaluated or the packet matches an entry.

n Entering an existing <POLICY-NAME> value will cause the existing policy to be modified, with any new

<SEQUENCE-NUMBER> value creating an additional policy entry, and any existing <SEQUENCE-NUMBER> value
replacing the existing policy entry with the same sequence number.

n If no sequence number is specified, a new policy entry will be appended to the end of the entry list with a

sequence number equal to the highest policy entry currently in the list plus 10.

Examples

Creating a policy with several entries:

switch(config)# policy MY_POLICY
switch(config-policy)# 10 class ipv6 MY_CLASS1 action dscp af21 action drop
switch(config-policy)# 20 class ip MY_CLASS3 action mirror 1

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

109

switch(config-policy)# exit
switch(config)# do show policy

Name

Sequence Comment

Class Type

action

-------------------------------------------------------------------------------

10

20

MY_POLICY

MY_CLASS1 ipv6

drop
dscp AF21

MY_CLASS3 ipv4

mirror 1

Adding a comment to an existing policy entry:

switch(config)# policy MY_POLICY
switch(config-policy)# 20 comment MY_TEST_POLICY
switch(config-policy)# exit
switch(config)# do show policy

Name

Sequence Comment

Class Type

action

-------------------------------------------------------------------------------

MY_POLICY

10

MY_CLASS1 ipv6

drop
dscp AF21

20 MY_TEST_POLICY
MY_CLASS3 ipv4

mirror 1

Removing a comment from an existing policy entry:

switch(config)# policy MY_POLICY
switch(config-policy)# no 20 comment
switch(config-policy)# exit
switch(config)# do show policy

Name

Sequence Comment

Class Type

action

-------------------------------------------------------------------------------

10

20

MY_POLICY

MY_CLASS1 ipv6

drop
dscp AF21

MY_CLASS3 ipv4

mirror 1

Adding/Replacing a policy entry in an existing policy:

Classifier policies | 110

| switch(config)# | policy | MY_POLICY |     |     |     |
| --------------- | ------ | --------- | --- | --- | --- |
switch(config-policy)#
|                        |         | 10 class ip MY_CLASS3 | action drop | action dscp | af21 |
| ---------------------- | ------- | --------------------- | ----------- | ----------- | ---- |
| switch(config-policy)# |         | exit                  |             |             |      |
| switch(config)#        | do show | policy                |             |             |      |
Name
| Sequence Comment |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
Class Type
action
-------------------------------------------------------------------------------
MY_POLICY
10
MY_CLASS3 ipv4
drop
|     | dscp | AF21 |     |     |     |
| --- | ---- | ---- | --- | --- | --- |
20
MY_CLASS3 ipv4
|     | mirror | 1   |     |     |     |
| --- | ------ | --- | --- | --- | --- |
Removingapolicyentry:
| switch(config)# | policy | MY_POLICY |     |     |     |
| --------------- | ------ | --------- | --- | --- | --- |
switch(config-policy)#
|                        |         | no 10  |     |     |     |
| ---------------------- | ------- | ------ | --- | --- | --- |
| switch(config-policy)# |         | exit   |     |     |     |
| switch(config)#        | do show | policy |     |     |     |
Name
| Sequence Comment |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
Class Type
action
-------------------------------------------------------------------------------
MY_POLICY
20
MY_CLASS3 ipv4
|     | mirror | 1   |     |     |     |
| --- | ------ | --- | --- | --- | --- |
Removingapolicy:
| switch(config)# | no policy | MY_POLICY |     |     |     |
| --------------- | --------- | --------- | --- | --- | --- |
| switch(config)# | do show   | policy    |     |     |     |
Name
| Sequence Comment |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
Class Type
action
-------------------------------------------------------------------------------
MY_POLICY2
2
MY_CLASS3 ipv4
|     | mirror | 1   |     |     |     |
| --- | ------ | --- | --- | --- | --- |
policy copy
Syntax
| policy <POLICY-NAME> | copy | <DESTINATION-POLICY> |     |     |     |
| -------------------- | ---- | -------------------- | --- | --- | --- |
Description
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 111

Copies a policy to a new destination policy or overwrites an existing policy. Copying a policy copies all its
entries as well.

Command context

config

Parameters

<POLICY-NAME>

Specifies the policy to be copied.

<DESTINATION-POLICY>

Specifies the name of the destination policy.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Copying a policy:

switch(config)# policy MY_POLICY copy MY_POLICY2
switch(config)# do show policy

Name

Sequence Comment

Class Type

action

-------------------------------------------------------------------------------

MY_POLICY

2

my_class3 ipv4

mirror 1

-------------------------------------------------------------------------------

MY_POLICY2

2

my_class3 ipv4

mirror 1

policy resequence

Syntax

policy <POLICY-NAME> resequence <STARTING-SEQ-NUM> <INCREMENT>

Description

Resequences numbering in a policy.

Command context

config

Parameters

<POLICY-NAME>

Specifies the policy where you want to resequence policy entries.

<STARTING-SEQ-NUM>

Specifies the sequence number to start resequencing from.

<INCREMENT>

Classifier policies | 112

Specifies how much to increment the sequence numbers by.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Resequencing a policy:

switch(config)# policy MY_POLICY resequence 1 1
switch(config)# do show policy

Name

Sequence Comment

Class Type

action

-------------------------------------------------------------------------------

1

2

MY_POLICY

MY_CLASS3 ipv4

drop
dscp AF21

MY_CLASS3 ipv4

mirror 1

policy reset

Syntax

policy <POLICY-NAME> reset

Description

Changes the user-specified policy configuration to match the active policy configuration. Use this command
when a discrepancy exists between what the user configured and what is active and accepted by the system.

Command context

config

Parameters

<POLICY-NAME>

Specifies the policy to be reset.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Resetting a policy:

switch(config)# policy MY_POLICY reset

show class

Syntax

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

113

show class [ip | ipv6 | mac] [<CLASS-NAME>] [commands] [configuration] [vsx-peer]
Description
Showsclassconfigurationinformation.
Commandcontext
Operator(>)orManager(#)
Parameters
Allparametersareoptional.
[ip | ipv6 | mac]
Selectstheclasstypeforthedisplay:ipforIPv4,ipv6forIPv6,ormacforMACclasses.
<CLASS-NAME>
Specifiestheclassname.
commands
SpecifieswhethertodisplayoutputastheCLIcommandsshowingtheconfiguredclassentries.
configuration
Specifieswhethertodisplayclassesthathavebeenconfiguredbytheuser,eveniftheyarenotactive
duetoissueswiththecommandparametersorhardwareissues.Thisparameterisusefulduringa
mismatchbetweentheenteredconfigurationandtheprevioussuccessfullyprogrammed(active)classes.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showingallclassconfiguration:
switch# show class
Type Name
Sequence Comment
| action      |            | L3 Protocol |            |
| ----------- | ---------- | ----------- | ---------- |
| Source      | IP address | Source      | L4 Port(s) |
| Destination | IP address | Destination | L4 Port(s) |
| Additional  | Parameters |             |            |
---------------------------------------------------------------
ipv4 MY_IPV4_CLASS
| 10 my first | class entry | comment |     |
| ----------- | ----------- | ------- | --- |
| match       |             | icmp    |     |
192.168.0.1/255.255.255.0
192.168.1.1/255.255.255.0
| VLAN:                     | 1           |         |     |
| ------------------------- | ----------- | ------- | --- |
| 20 my second              | class entry | comment |     |
| ignore                    |             | tcp     |     |
| 10.100.0.10/255.255.255.0 |             | < 3000  |     |
| 10.100.1.10/255.255.255.0 |             | > 2000  |     |
| VLAN:                     | 1           |         |     |
----------------------------------------------------------------------
ShowingclassconfigurationfortheIPv4classMY_IPV4_CLASSasCLIcommands:
Classifierpolicies|114

|     | switch# | show class         | ip MY_IPV4_CLASS |     | commands |     |
| --- | ------- | ------------------ | ---------------- | --- | -------- | --- |
|     | class   | ip "MY_IPV4_CLASS" |                  |     |          |     |
10 match icmp 192.168.0.1/255.255.255.0 192.168.1.1/255.255.255.0 vlan 1
|     | 10  | comment my | first class | entry | comment |     |
| --- | --- | ---------- | ----------- | ----- | ------- | --- |
20 ignore tcp 10.100.0.10/255.255.255.0 lt 3000 10.100.1.10/255.255.255.0 gt
|      |        | 2000 vlan  | 1      |             |         |     |
| ---- | ------ | ---------- | ------ | ----------- | ------- | --- |
|      | 20     | comment my | second | class entry | comment |     |
| show | policy |            |        |             |         |     |
Syntax
Syntaxthatshowsinformationforallpolicies:
| show | policy | [commands] | [configuration] |     | [vsx-peer] |     |
| ---- | ------ | ---------- | --------------- | --- | ---------- | --- |
SyntaxthatfiltersbypoliciesappliedtoaninterfaceorVLAN:
show policy [interface <IF-NAME> [in | out | routed-in] | vlan <VLAN-ID> [in | out]]
|     |     | [commands] | [configuration] |     | [vsx-peer] |     |
| --- | --- | ---------- | --------------- | --- | ---------- | --- |
show policy [interface <IF-NAME> [in | routed-in] | vlan <VLAN-ID> [in]]
|     |     | [commands] | [configuration] |     | [vsx-peer] |     |
| --- | --- | ---------- | --------------- | --- | ---------- | --- |
Syntaxthatfiltersbythenamedpolicy:
| show | policy | <POLICY-NAME> | [commands] |     | [configuration][vsx-peer] |     |
| ---- | ------ | ------------- | ---------- | --- | ------------------------- | --- |
Syntaxthatfiltersbythegloballyappliedpolicy:
| show | policy | global | [commands] | [configuration][vsx-peer] |     |     |
| ---- | ------ | ------ | ---------- | ------------------------- | --- | --- |
Syntaxthatshowsstatisticalinformationintheformofhitcounts:
show policy hitcounts <POLICY-NAME> [interface <IF-NAME> [in | out | routed-in] |
|     |     |     | vlan | <VLAN-ID> | [in | out]] | [vsx-peer] |
| --- | --- | --- | ---- | --------- | ----------- | ---------- |
Syntaxthatshowsstatisticalinformationintheformofhitcountsforthegloballyappliedpolicy:
| show | policy | hitcounts | global | [vsx-peer] |     |     |
| ---- | ------ | --------- | ------ | ---------- | --- | --- |
Description
Showsinformationaboutyourdefinedpoliciesandwheretheyhavebeenapplied.Whenshow policyis
enteredwithoutparameters,informationforallpoliciesisshown.Theparametersfilterthelistofpoliciesfor
whichinformationisshown.
Availablefilteringincludes:
Thecontentofaspecificpolicy.
n
n Allpoliciesappliedtoaspecificinterface.
n AllpoliciesappliedtoaspecificVLAN.
n Thegloballyappliedpolicy.
n Theinbound(ingress)oroutbound(egress)direction.
Todisplaypolicystatistics,usetheshow policy hitcountsformofthiscommand.
Commandcontext
Operator(>)orManager(#)
Parameters
| interface |     | <IF-NAME> |     |     |     |     |
| --------- | --- | --------- | --- | --- | --- | --- |
Specifiestheinterfacename.
vlan <VLAN-ID>
SpecifiestheVLAN.
in
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 115

Selects the inbound (ingress) traffic direction.

out

Selects the outbound (egress) traffic direction.

routed-in

Selects the routed in traffic direction. Not applicable to a policy applied to a VLAN.

<POLICY-NAME>

Specifies the policy name.

commands

Causes the policy definition to be shown as the commands and parameters used to create it rather than
in tabular form.

configuration

Causes the user-configured policies be shown as entered, even if the policies are not active due to policy-
definition command issues or hardware issues. This parameter is useful if there is a mismatch between
the entered configuration and the previous successfully programmed (active) policies configuration.

global

Selects the globally applied policy.

hitcounts

Selects the policy hit counts (statistics).

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

On the 6400 Switch Series, interface identification differs.

Showing information for all policies:

switch# show policy

Name

Sequence Comment

Class Type

action

-------------------------------------------------------------------------------

my_policy

10 This is my QOS class.

class1 ipv4

dscp af21
drop

-------------------------------------------------------------------------------

Showing a policy as commands:

switch# show policy commands
policy my_policy

10 class ip my_class1 action dscp af21 action drop

Showing the globally applied policy:

Classifier policies | 116

| switch# | show | policy | global | commands |     |     |     |
| ------- | ---- | ------ | ------ | -------- | --- | --- | --- |
policy global1
| 10 class     |     | ip my_class1 |     | action | drop |     |     |
| ------------ | --- | ------------ | --- | ------ | ---- | --- | --- |
| apply policy |     | my_policy    | in  |        |      |     |     |
Showingpolicyhitcounts(statistics):
| switch#    | show         | policy | hitcounts     | my_policy |             |       |     |
| ---------- | ------------ | ------ | ------------- | --------- | ----------- | ----- | --- |
| Statistics | for          | Policy | my_policy:    |           |             |       |     |
| Interface  | 1/1/1*       | (in):  |               |           |             |       |     |
|            | Hit          | Count  | Configuration |           |             |       |     |
| 10 class   | ip my_class1 |        | action        | dscp      | af21 action | drop  |     |
|            |              | 20     | 10            | match     | any any any | count |     |
* policy statistics are shared among each context type (interface, VLAN).
| For routed |     | ingress, | they | are | only shared | within | the same VRF. |
| ---------- | --- | -------- | ---- | --- | ----------- | ------ | ------------- |
Use 'policy NAME copy' to create a new policy for separate statistics.
Showingpolicyhitcounts(statistics)forthegloballyappliedpolicy:
| switch#    | show | policy | hitcounts | global |     |     |     |
| ---------- | ---- | ------ | --------- | ------ | --- | --- | --- |
| Statistics | for  | Policy | global1:  |        |     |     |     |
Global Policy:
|          | Hit          | Count | Configuration |        |             |       |     |
| -------- | ------------ | ----- | ------------- | ------ | ----------- | ----- | --- |
| 10 class | ip my_class1 |       | action        | mirror |             |       |     |
|          |              | 20    | 10            | match  | any any any | count |     |
* policy statistics are shared among each context type (interface, vlan, VRF).
| use 'policy |     | NAME | copy' | to create | a uniquely-named |     | policy |
| ----------- | --- | ---- | ----- | --------- | ---------------- | --- | ------ |
Showingpolicyhitcountswithconformratefrommy_policyappliedinbound:
| switch#    | show   | policy | hitcounts     | my_policy |     |     |     |
| ---------- | ------ | ------ | ------------- | --------- | --- | --- | --- |
| Statistics | for    | Policy | my_policy:    |           |     |     |     |
| Interface  | 1/1/1* | (in):  |               |           |     |     |     |
|            | Hit    | Count  | Configuration |           |     |     |     |
10 class ipv6 my_class1 action cir kbps 1024 cbs 2000 exceed drop [1024 kbps conform
]
|     |     |     | - 10 | match | any any any |     |     |
| --- | --- | --- | ---- | ----- | ----------- | --- | --- |
* policy statistics are shared among each context type (interface, VLAN).
| For routed |     | ingress, | they | are | only shared | within | the same VRF. |
| ---------- | --- | -------- | ---- | --- | ----------- | ------ | ------------- |
Use 'policy NAME copy' to create a new policy for separate statistics.
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 117

Chapter 5
|     |     |     | Classifier | policies | configuration |
| --- | --- | --- | ---------- | -------- | ------------- |
example
| Classifier | policies configuration | example |     |     |     |
| ---------- | ---------------------- | ------- | --- | --- | --- |
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Thisexampleconfigurestrafficpolicingon:
n A10-GbitEthernetofSwitchAmeetingthefollowingrequirements:
o Policetherateofpacketsfromtheserverto102,400kbps.Traffic102,400kbpsorlessisforwarded.
Thetrafficmorethan102,400kbpsisdropped.
o PolicetherateofpacketsfromHostAto25,600kbps.Traffic25,600kbpsorlessisforwarded.The
trafficmorethan25,600kbpsisdropped.
n A10-GbitEthernet1/2/1ofSwitchBlimitingtheincomingtrafficrateofHTTPpacketson10-Gbit
Ethernet1/1/1tothedatarateof204,800kbpsanddroppingexcesspackets.
| Configuring | the classifier | policies | example |     |     |
| ----------- | -------------- | -------- | ------- | --- | --- |
Thesestepsarepartoftheclassifierpoliciesconfigurationexample.
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
1. ConfigureSwitchA.
CreatetrafficclassesnamedSERVER_TRAFFICandHOST_A_TRAFFICformatchingthepacketsfrom
theserverandHostA:
switch# configure
|     | switch(config)# class | ip SERVER_TRAFFIC |     |     |     |
| --- | --------------------- | ----------------- | --- | --- | --- |
switch(config-class-ip)#
|     |                          | match any         | 1.1.1.1 any |     |     |
| --- | ------------------------ | ----------------- | ----------- | --- | --- |
|     | switch(config-class-ip)# | exit              |             |     |     |
|     | switch(config)# class    | ip HOST_A_TRAFFIC |             |     |     |
|     | switch(config-class-ip)# | match any         | 1.1.1.2 any |     |     |
|     | switch(config-class-ip)# | exit              |             |     |     |
118
| AOS-CX10.07ACLsandClassifierPoliciesGuide| | (6300,6400,8360SwitchSeries) |     |     |     |     |
| ------------------------------------------ | ---------------------------- | --- | --- | --- | --- |

2. CreateaclassifierpolicynamedRATE_LIMIT_POLICY:
switch(config)#
policy RATE_LIMIT_POLICY
3. ConfigurethepolicyRATE_LIMIT_POLICY,sothat102,400kbpsoftraffic,matchingtheclassSERVER_
TRAFFIC,isforwardedandtheexcessisdropped:
switch(config-policy)# class ip SERVER_TRAFFIC action cir kbps 102400 exceed
drop
4. ConfigurethepolicyRATE_LIMIT_POLICYsothat25,600kbpsoftraffic,matchingtheclassHOST_A_
TRAFFIC,isforwardedandtheexcessisdropped:
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
| switch(config)# | class | ip HTTP_TRAFFIC |     |     |     |
| --------------- | ----- | --------------- | --- | --- | --- |
switch(config-class-ip)#
|                          |     | match | tcp any | any eq 80 |     |
| ------------------------ | --- | ----- | ------- | --------- | --- |
| switch(config-class-ip)# |     | exit  |         |           |     |
Classifierpoliciesconfigurationexample|119

8. CreateaclassifierpolicynamedRATE_LIMIT_HTTP:
| switch(config)# | policy RATE_LIMIT_HTTP |     |     |     |
| --------------- | ---------------------- | --- | --- | --- |
9. ConfigurethepolicyRATE_LIMIT_HTTPsothat204,800kbpsoftraffic,matchingtheclassHTTP_
TRAFFIC,isforwardedandtheexcessisdropped:
switch(config-policy)# class ip HTTP_TRAFFIC action cir kbps 204800 exceed drop
| switch(config-policy)# | exit |     |     |     |
| ---------------------- | ---- | --- | --- | --- |
10. ApplyRATE_LIMIT_HTTPtointerface1/1/1forinboundtraffic:
| switch(config)#    | int 1/1/1 |                        |     |     |
| ------------------ | --------- | ---------------------- | --- | --- |
| switch(config-if)# | apply     | policy RATE_LIMIT_HTTP |     | in  |
| switch(config-if)# | exit      |                        |     |     |
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
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 120

Chapter 6
|     |     |     | ACL and | Policy | hardware | resource |
| --- | --- | --- | ------- | ------ | -------- | -------- |
considerations
| ACL and | Policy hardware | resource | considerations |     |     |     |
| ------- | --------------- | -------- | -------------- | --- | --- | --- |
Switcheshavefinite(TCAMandother)hardwareresourcesusedintheapplicationofACLsandclassifier
policies(includingportaccesspolicies)topacketsbeingprocessedinswitchhardware.ADC(analyticsdata
collection)alsoconsumesTCAMlookups.Taketheconsiderationsdescribedinthischapterintoaccount
whendecidingwhatACLandclassifierpolicy-relatedfeaturestouseatthesametime.
| TCAM | lookups |     |     |     |     |     |
| ---- | ------- | --- | --- | --- | --- | --- |
TCAMlookupsareafinitehardwareresourceusedintheapplicationofACLsandpolicies(includingport
accesspolicies)topacketsbeingprocessedinswitchhardware.ADC(analyticsdatacollection)alsoconsumes
TCAMlookups.TherearealimitednumberofACLandpolicyfeaturesthatcanbeenabledatthesametime.
InthefollowingTCAMlookuplists,"IP"meansbothIPv4andIPv6.
TherearefourTCAMlookupsavailabletouseforthesefeatures.EachofthesefeaturesusesoneTCAM
lookupwhenenabled.Atmost,fourofthesefeaturescanbeenabledatthesametime.
| Ingress | Port IP ACL   |                 |       |     |     |     |
| ------- | ------------- | --------------- | ----- | --- | --- | --- |
| Ingress | Port MAC ACL  |                 |       |     |     |     |
| Ingress | Port Policy   |                 |       |     |     |     |
| Ingress | Routed Port   | Policy          |       |     |     |     |
| Ingress | PAC Policy    |                 |       |     |     |     |
| Ingress | VLAN IP ACL   |                 |       |     |     |     |
| Ingress | Routed VLAN   | IP ACL          |       |     |     |     |
| Ingress | VLAN MAC ACL  |                 |       |     |     |     |
| Ingress | VLAN Policy   |                 |       |     |     |     |
| Ingress | Routed VLAN   | Policy          |       |     |     |     |
| Ingress | Global Policy |                 |       |     |     |     |
| Ingress | IP Analytics  | Data Collection | (ADC) |     |     |     |
| Port    | Access Client | Policy          |       |     |     |     |
Thisfeatureisnotclassifierrelatedbutusesonelookupfromtheabovegroupoffeatures:
| Ingress | L2 Tunnel |     |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- | --- |
TherearefourTCAMlookupsavailableforthesefeatures.EachofthesefeaturesusesoneTCAMlookup
whenenabled.Atmost,fourofthesefeaturescanbeenabledatthesametime.
| Egress | Port IP ACL  |        |     |     |     |     |
| ------ | ------------ | ------ | --- | --- | --- | --- |
| Egress | Port MAC ACL |        |     |     |     |     |
| Egress | Port Policy  |        |     |     |     |     |
| Egress | VLAN IP ACL  |        |     |     |     |     |
| Egress | Routed VLAN  | IP ACL |     |     |     |     |
| Egress | VLAN MAC ACL |        |     |     |     |     |
| Egress | VLAN Policy  |        |     |     |     |     |
121
| AOS-CX10.07ACLsandClassifierPoliciesGuide| |     | (6300,6400,8360SwitchSeries) |     |     |     |     |
| ------------------------------------------ | --- | ---------------------------- | --- | --- | --- | --- |

| Matching |     | precedence | order |
| -------- | --- | ---------- | ----- |
WhenapacketismatchedbymultipleTCAMLookupswiththesameaction,aprecedenceorderisfollowed.
Forexample,ifapacketmatchesanIPv6ACLwithacountactionandaMACACLwithacountaction,the
IPv6countactiontakesprecedenceandtheMACACLwillnotcountthepacket.However,ifapacket
matchesbothanACLandapolicywithcountactions,bothwillbecounted.Regardlessofprecedence,ifa
packetistobedroppedbyaconfiguredfeature,itwillbedropped.Ingresspacketsdonottakeprecedence
overegresspacketsnordoegresspacketstakeprecedenceoveringresspackets.
AmaximumoftwoRedirectaction-capablelookupsareavailable.Theselookupswillbeconservedif
possibleandnotusedforpoliciesthatdonotconfiguretheRedirectaction,butthelookupsmaybe
consumedifneededtoapplyapolicywithoutaRedirectaction.Itisthereforepossibletoconsumethe
Redirect-capablelookupswithnon-Redirectpoliciesinaconfigurationwithmanypoliciesapplied.
Theprecedenceorderfromhighesttolowestisasfollows:
| Meter          | Actions:  |               |                |
| -------------- | --------- | ------------- | -------------- |
| Port Access    |           | Client Policy |                |
| Ingress        | Routed    | Port Policy   |                |
| Port Policy    |           |               |                |
| Routed         | Ingress   | VLAN Policy   |                |
| VLAN Policy    |           |               |                |
| Ingress        | Global    | Policy        |                |
| QoS Actions:   |           |               |                |
| Port Access    |           | Client Policy | Remark         |
| Routed         | Ingress   | Port Policy   | Remark         |
| Ingress/Egress |           | Port Policy   | Remark         |
| Routed         | Ingress   | VLAN Policy   | Remark         |
| Ingress/Egress |           | VLAN Policy   | Remark         |
| Global         | Policy    | Remark        |                |
| QoS DSCP       | Map       | Entry         |                |
| QoS COS        | Map       | Entry         |                |
| QoS Port       | Config    |               |                |
| MAC Port       | ACL       | Logging       |                |
| IP Port        | ACL       | Logging       |                |
| MAC VLAN       | ACL       | Logging       |                |
| IP VLAN        | ACL       | Logging       |                |
| Redirect       | actions:  |               |                |
| Software       | Route     |               |                |
| Policy         | L2 Tunnel |               |                |
| PBR Nexthop    |           |               |                |
| Normal         | Route     | Table Hit     |                |
| PBR Default    |           | Nexthop       |                |
| Default        | Route     | Table Hit     |                |
| Port Access    |           | Client Policy | Captive-portal |
| L4 port        | ranges    |               |                |
AnyACEorclassentrythatuses'lt','gt','range',orportgroupsmayusemorethanonehardwareentryto
representtherangeofL4ports.
| Context | group | selectors |     |
| ------- | ----- | --------- | --- |
ContextgroupselectorsarealimitedhardwareresourcethatarerequiredforapplyingACLsandclassifier
policies.TheselectorsenabletheapplicationofanACLorclassifierpolicytomultipleinstancesofthesame
context(forexample,portsonalinecardorVLANs)withoutconsumingadditionalresources.
ACLandPolicyhardwareresourceconsiderations|122

There are a limited number of available context group selectors for each context group (Ingress Ports,
Ingress VLANs, Egress Ports, Egress VLANs).

IP ACLs require two selectors that are allocated together; one selector for each address family (IPv4 and IPv6).

Context group selectors work on a first-come-first-served basis. IP ACLs and Classes require two selectors
that are allocated together; one selector for each address family (IPv4 and IPv6). Once all the group
selectors for a context group have been used, no new application type of ACL or classifier policy for the
context group can be applied. For example, if an existing configuration has a MAC ACL, IP ACL, and classifier
policy applied on ingress to ports, a policy cannot be applied to a port in the routed-in direction .

Context group selector consumption and availability are as follows:

Type

Selectors

Ingress Port MAC ACL

Ingress Port IP ACL

Ingress Port Policy

Ingress Routed Port Policy

Available Ingress Port Selectors

Ingress VLAN MAC ACL

Ingress VLAN IP ACL

Routed-Ingress VLAN IP ACL

Ingress VLAN Policy

Ingress Routed VLAN Policy

Available Ingress VLAN Selectors

Egress Port MAC ACL

Egress Port IP ACL

Egress Port Policy

Available Egress Port Selectors

Egress VLAN MAC ACL

Egress VLAN IP ACL

Routed-Egress VLAN IP ACL

Egress VLAN Policy

1

2

1

1

4

1

2

2

1

1

4

1

2

1

5

1

2

2

1

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

123

Type

Selectors

Available Egress VLAN Selectors

5

ACL and Policy hardware resource commands

show resources (6300, 6400 Switch Series)

Syntax

show resources [<SLOT-ID>] [vsx-peer]

Description

On the 6300 switch, shows hardware resource consumption for the specified VSF member or for all VSF
members. On the 6400 switch, shows hardware resource consumption for the specified line module or for
all line modules. Resource data is updated every 10 seconds.

Hardware resource consumption information is shown for:

n TCAM entries

n TCAM lookups

n Policers

Command context

Operator (>) or Manager (#)

Parameters

<SLOT-ID>

Specifies the VSF member on the 6300 switch and the member and slot of the line module on the 6400
switch. For example, on the 6400 switch, to specify the line module in member 1, slot 2, enter 1/2.

<SLOT-ID>

Specifies the member and slot of the line module. For example, to specify the line module in member 1,
slot 2, enter 1/2.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

The widths for show resources can have features combined (IPv4 + IPv6) into one TCAM lookup. Therefore,
the table widths for each ACL/classifier policy type are variable depending on what is applied. For example:

"Ingress IP Port ACL" = Ingress v4 Port ACLs + Ingress v6 Port ACLs

= 1 TCAM entry + 4 TCAM entries
= 5 TCAM entries

Widths per feature are as follows:

ACL and Policy hardware resource considerations | 124

| MAC ACL    | 1   |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- |
| IPv4 ACL   | 1   |     |     |     |     |
| IPv6 ACL   | 4   |     |     |     |     |
| MAC Class  | 1   |     |     |     |     |
| IPv4 Class | 2   |     |     |     |     |
| IPv6 Class | 4   |     |     |     |     |
AMACClasswithanethertypeof"any"hasawidthof7becauseitusesoneTCAMentryeachforMAC,IPv4,
andIPv6.SpecifyingtheIPv4(0x0800)orIPv6(0x86DD)ethertypesinaMACClassusesaTCAMentryequal
totheirrespectivesize.IPv4usesawidthof2andIPv6usesawidthof4.
Examples
Showinghardwareresourceconsumptionona6300switch:
| switch#         | show resources |     |     |               |      |
| --------------- | -------------- | --- | --- | ------------- | ---- |
| Resource        | Usage:         |     |     |               |      |
| Mod Description |                |     |     |               |      |
|                 | Resource       |     |     | Used Reserved | Free |
-------------------------------------------------------------------------
| 1/1 Ingress | IP Port      | ACL Lookup |     |     |        |
| ----------- | ------------ | ---------- | --- | --- | ------ |
|             | Ingress TCAM | Entries    |     | 20  | 0 5093 |
Total
|     | Ingress Lookups |     |     | 1   | 0 4 |
| --- | --------------- | --- | --- | --- | --- |
|     | Egress Lookups  |     |     | 0   | 0 4 |
Showinghardwareresourceconsumptionforalllinemodulesona6405switch:
| switch#         | show resources |     |     |      |      |
| --------------- | -------------- | --- | --- | ---- | ---- |
| Resource        | Usage:         |     |     |      |      |
| Mod Description |                |     |     |      |      |
|                 | Resource       |     |     | Used | Free |
-------------------------------------------------------------------------
| 1/3 Total      |                 |        |         |     |     |
| -------------- | --------------- | ------ | ------- | --- | --- |
|                | Ingress Lookups |        |         | 0   | 5   |
|                | Egress Lookups  |        |         | 0   | 4   |
| 1/5 Total      |                 |        |         |     |     |
|                | Ingress Lookups |        |         | 0   | 5   |
|                | Egress Lookups  |        |         | 0   | 4   |
| show resources | (8360           | Switch | Series) |     |     |
Syntax
| show resources | [vsx-peer] |     |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- |
Description
Showshardwareresourceconsumptionontheswitch.Resourcedataisupdatedevery10seconds.
Hardwareresourceconsumptioninformationisshownfor:
AOS-CX10.07ACLsandClassifierPoliciesGuide|(6300,6400,8360SwitchSeries) 125

TCAMentries
n
Policers
n
L4PortRanges
n
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
Usage
Thewidthsforshowresourcescanhavefeaturescombined(IPv4+IPv6)intooneTCAMlookup.Therefore,
thetablewidthsforeachACL/classifierpolicytypearevariabledependingonwhatisapplied.Forexample:
"Ingress IP Port ACL" = Ingress v4 Port ACLs + Ingress v6 Port ACLs
|     |     | = 1 TCAM entry + 4 TCAM entries |     |     |
| --- | --- | ------------------------------- | --- | --- |
= 5 TCAM entries
Widthsperfeatureareasfollows:
| MAC ACL    | 1   |     |     |     |
| ---------- | --- | --- | --- | --- |
| IPv4 ACL   | 1   |     |     |     |
| IPv6 ACL   | 4   |     |     |     |
| MAC Class  | 1   |     |     |     |
| IPv4 Class | 2   |     |     |     |
| IPv6 Class | 4   |     |     |     |
AMACClasswithanethertypeof"any"hasawidthof7becauseitusesoneTCAMentryeachforMAC,IPv4,
andIPv6.SpecifyingtheIPv4(0x0800)orIPv6(0x86DD)ethertypesinaMACClassusesaTCAMentry
equaltotheirrespectivesize.IPv4usesawidthof2andIPv6usesawidthof4.
Example
Showinghardwareresourceconsumption:
| switch# show    | resources |     |     |     |
| --------------- | --------- | --- | --- | --- |
| Resource Usage: |           |     |     |     |
Mod Description
| Resource |     |     | Used Reserved | Free |
| -------- | --- | --- | ------------- | ---- |
-------------------------------------------------------------------------
| 1/1 Ingress | IP Port ACL | Lookup  |     |        |
| ----------- | ----------- | ------- | --- | ------ |
| Ingress     | TCAM        | Entries | 20  | 0 5093 |
Total
ACLandPolicyhardwareresourceconsiderations|126

Ingress Lookups
Egress Lookups

1
0

0
0

4
4

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

127

Support and other resources

Chapter 7

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

Accessing Updates
You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

AOS-CX 10.07 ACLs and Classifier Policies Guide | (6300, 6400, 8360 Switch Series)

128

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

Support and other resources | 129