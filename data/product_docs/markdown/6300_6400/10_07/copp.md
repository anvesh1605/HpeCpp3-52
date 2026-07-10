AOS-CX 10.07 CoPP Guide

6200, 6300, 6400 Switch Series

Part Number: 5200-7841
Published: April 2021
Edition: 1

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
| Contents                            |                                |          |           | 3   |
| ----------------------------------- | ------------------------------ | -------- | --------- | --- |
| About                               | this                           | document |           | 4   |
| Applicableproducts                  |                                |          |           | 4   |
| Latestversionavailableonline        |                                |          |           | 4   |
| Commandsyntaxnotationconventions    |                                |          |           | 4   |
| Abouttheexamples                    |                                |          |           | 5   |
| Identifyingswitchportsandinterfaces |                                |          |           | 5   |
| Identifyingmodularswitchcomponents  |                                |          |           | 6   |
| Control                             | Plane                          | Policing | (CoPP)    | 7   |
| Overview                            |                                |          |           | 7   |
| ConfiguringCoPP                     |                                |          |           | 7   |
|                                     | Example                        |          |           | 7   |
| Actualratesinhardware               |                                |          |           | 8   |
| CoPPcommands                        |                                |          |           | 8   |
|                                     | Classesoftraffic               |          |           | 8   |
|                                     | applycopp-policy               |          |           | 10  |
|                                     | class                          |          |           | 11  |
|                                     | clearcopp-policystatistics     |          |           | 12  |
|                                     | copp-policy                    |          |           | 13  |
|                                     | default-class                  |          |           | 14  |
|                                     | resetcopp-policy               |          |           | 15  |
|                                     | showcopp-policy                |          |           | 16  |
|                                     | showcopp-policyfactory-default |          |           | 17  |
|                                     | showcopp-policystatistics      |          |           | 19  |
|                                     | showtechcopp                   |          |           | 20  |
| Support                             | and                            | Other    | Resources | 22  |
| AccessingArubaSupport               |                                |          |           | 22  |
| AccessingUpdates                    |                                |          |           | 22  |
|                                     | ArubaSupportPortal             |          |           | 22  |
|                                     | MyNetworking                   |          |           | 23  |
| WarrantyInformation                 |                                |          |           | 23  |
| RegulatoryInformation               |                                |          |           | 23  |
| DocumentationFeedback               |                                |          |           | 23  |
3
AOS-CX10.07CoPPGuide| 6200,6300,6400SwitchSeries

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

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

AOS-CX 10.07 CoPP Guide | 6200, 6300, 6400 Switch Series

4

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

On the 6200 Switch Series

About this document | 5

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

AOS-CX 10.07 CoPP Guide | 6200, 6300, 6400 Switch Series

6

Control Plane Policing (CoPP)

Chapter 2

Control Plane Policing (CoPP)

Overview
CoPP provides a way for administrators to protect the management processor on the switch from high
packet loads (generated by malicious or nonmalicious sources) that might interfere with its ability to keep
data plane traffic flowing. For example, a denial of service attack can result in excessive traffic that would
slow down the management processor and negatively affect switch throughput.

A CoPP policy is composed of one or more classes. Each class defines one or more target protocols and how
their traffic is managed. Every policy also has a default class to regulate packets that do not match any other
class. The following actions can be applied for all packets matching a class:

n Drop the packets. (Excluding the default class.)

n Set the processing priority in the range 0 to 6 (0 - highest priority and 6 - lowest priority).

n Set the maximum data rate in packets per second (pps) at which each line module can send packets to the

management processor.

n Set the maximum burst size in packets at which each line module can send packets to the management

processor.

Up to 32 CoPP policies can be defined, but only one can be active on the switch at a time.

A CoPP policy must always be active on the switch. By default, the switch has a CoPP policy named default
which is automatically applied at first boot.

When a line module is hot-swapped or a new line module comes up after boot on a 6400 switch, the CoPP
policy that is actively applied to the switch will be applied.

When the switch is rebooted, the CoPP policy that was actively applied to the switch before the reboot
occurred will be applied if it was saved to the startup configuration with the copy running-config startup-
config command.

For GRE tunneled traffic, CoPP policies match on the payload.

CoPP policies do not regulate traffic received from the Out-of-Band-Management (OOBM) Ethernet port.

Configuring CoPP

Procedure

1. Configure the default CoPP policy, edit an existing policy, or create a policy with the command copp-

policy.

2. Add, edit, or remove classes in the policy with the command class.

3.

If the policy is not the active policy on the switch, apply it with the command apply copp-policy.
(Changes made to an active policy take effect immediately and do not need to be applied.)

4. Review the CoPP policy configuration settings with the command show copp-policy.

Example

AOS-CX 10.07 CoPP Guide | 6200, 6300, 6400 Switch Series

7

Thisexamplecreatesthefollowingconfiguration:
DefinesanewpolicynamedMy_CoppPolicy.
n
n Addstwoclassestothepolicy.
n Activatesthepolicy.
n Displayspolicyconfigurationsettings.
| switch(config)#      |      | copp-policy |       | My_CoppPolicy |               |           |      |            |          |
| -------------------- | ---- | ----------- | ----- | ------------- | ------------- | --------- | ---- | ---------- | -------- |
| switch(config-copp)# |      |             | class | igmp          | priority      | 6 rate    | 5000 | burst 60   |          |
| switch(config-copp)# |      |             | class | lacp          | priority      | 2 rate    | 2000 | burst 2050 |          |
| switch(config-copp)# |      |             | exit  |               |               |           |      |            |          |
| switch(config)#      |      | apply       |       | copp-policy   | My_CoppPolicy |           |      |            |          |
| switch(config)#      |      | exit        |       |               |               |           |      |            |          |
| switch#              | show | copp-policy |       | My_CoppPolicy |               |           |      |            |          |
| class                |      |             |       | drop priority | rate          | pps burst | pkts | hardware   | rate pps |
--------------------- ---- -------- -------- ---------- -----------------
| igmp    |       |     |          | 6   | 5000 | 60   |     | 5000 |     |
| ------- | ----- | --- | -------- | --- | ---- | ---- | --- | ---- | --- |
| lacp    |       |     |          | 2   | 2000 | 2050 |     | 2000 |     |
| default |       |     |          | 1   | 6000 | 70   |     | 6000 |     |
| Actual  | rates | in  | hardware |     |      |      |     |      |     |
Currently,theactualrateinhardwareisdeterminedbyamappingbasedontheconfiguredrate,shownby
thefollowingtableofthefirstnineactualrates.
| | Configured |     | Rate (pps) | |   | Actual | Rate in Hardware | (pps) |     | |   |     |
| ------------ | --- | ---------- | --- | ------ | ---------------- | ----- | --- | --- | --- |
|-----------------------|-------------------------------|
| | 25-49   |     |     | |   | 25  |     |     |     | |   |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | 50-74   |     |     | |   | 50  |     |     |     | |   |     |
| | 75-99   |     |     | |   | 75  |     |     |     | |   |     |
| | 100-124 |     |     | |   | 100 |     |     |     | |   |     |
| | 125-149 |     |     | |   | 125 |     |     |     | |   |     |
| | 150-174 |     |     | |   | 150 |     |     |     | |   |     |
| | 175-199 |     |     | |   | 175 |     |     |     | |   |     |
| | 200-224 |     |     | |   | 200 |     |     |     | |   |     |
| | 225-249 |     |     | |   | 225 |     |     |     | |   |     |
Theprecedingtableshowsthefirstnineactualratesavailableinhardware.Higherratesareavailable.The
'show copp-policy statistics class <CLASS>'commandcanbeusedtoshowtheactualratein
hardwareforaspecificclass.The'show copp-policy <NAME>'commandcanbeusedtoshowtheactual
ratesforallclassesconfiguredinaspecificCoPPpolicy,ifthepolicyisactivelyapplied.
| CoPP    | commands |         |     |     |     |     |     |     |     |
| ------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| Classes | of       | traffic |     |     |     |     |     |     |     |
Thedifferentclassesoftrafficthatcanbeindividuallyconfiguredare:
n acl-logging:AccessControlListloggingpackets.
n arp-broadcast:AddressResolutionProtocolpacketswithabroadcastdestinationMACaddress.
n arp-protect:AddressResolutionProtocolpacketsinterceptedandinspectedforARPprotection.
n arp-unicast:AddressResolutionProtocolpacketswithaswitchsystemdestinationMACaddress.
bfd-control:BidirectionalForwardingDetection(BFD)controlpacketswithadestinationIPaddress
n
ownedbytheswitch.
ControlPlanePolicing(CoPP)|8

The bfd-control class is not supported for 6200 switch.

n bgp: Border Gateway Protocol packets with a destination IPv4 or IPv6 address owned by the switch.

The bgp class is not supported for 6200 switch.

n captive-portal: Packets intercepted in support of the Captive Portal feature.

n dhcp: Dynamic Host Configuration Protocol packets. Also includes snooped DHCP packets if DHCP

snooping is enabled.

n erps: Ethernet Ring Protection Switching control packets with the destination MAC address

01:19:a7:00:00:XX, where XX can be any value.

n icmp-broadcast-ipv4: Internet Control Message Protocol packets with a broadcast or multicast

destination IPv4 address.

n icmp-multicast-ipv6: Internet Control Message Protocol packets with a well-known multicast

destination IPv6 address.

n icmp-security-ipv6: IPv6 Internet Control Message Protocol packets intercepted and inspected.

n icmp-unicast-ipv4: Internet Control Message Protocol packets with a destination IPv4 address owned

by the switch

n icmp-unicast-ipv6: Internet Control Message Protocol packets with a destination IPv6 address owned

by the switch.

n ieee-8021x: IEEE 802.1X protocol packets with EtherType 0x0888E.

n igmp: Internet Group Management Protocol packets.

n ip-exceptions: Routable packets that would exceed the MTU for the egress interface, packets that

trigger ICMP redirects, and packets with TTL/hop_limit=1 that are discarded when routing through the
switch.

n ip-lockdown: Packets denied and logged due to violation of allowed "IP address/VLAN/port/MAC

address" association.

n ip-tracker: Track packets received for client IP address tracking.

The ip-tracker class is not supported for 6300 and 6400 switches.

n ipsec: Internet Protocol Security IPv4 or IPv6, unicast or configured multicast. All IPsec traffic received

by the CPU will be regulated by the ipsec class regardless of the encapsulated protocol.

n ipv4-options: Unicast IPv4 packets including option headers.

n lacp: Link Aggregation Control Protocol packets with the destination MAC address 01:80:c2:00:00:02.

n lldp: Link Layer Discovery Protocol packets with the destination MAC address 01:80:c2:00:00:0e.

n loop-protect: Loop Protection packets with the destination MAC address 09:00:09:09:13:a6.

n mac-lockout: Packets denied and logged due to locked-out MAC address.

n manageability: Unicast IP packets addressed to the switch for specific protocols that do not have a

dedicated CoPP class like HTTP, SSH, RADIUS.

n mirror-to-cpu: Packets from mirroring session configured to deliver to the console.

n mld: Multicast Listener Discovery packets of type V1 or V2 with an IPv6 address of FF00::/8, FF02::16 or

FF02::2.

AOS-CX 10.07 CoPP Guide | 6200, 6300, 6400 Switch Series

9

n mvrp: Multiple VLAN Registration Protocol packets with the destination MAC address 01:80:c2:00:00:20

or 01:80:c2:00:00:21

n ntp: Network Time Protocol packets with a destination IP address owned by the switch.

n ospf-multicast: Open Shortest Path First packets with the multicast destination IPv4 address 224.0.0.5

or 224.0.0.6, or IPv6 address FF02::5 or FF02::6.

n ospf-unicast: Open Shortest Path First packets with a local destination IPv4 address or IPv6 address.

n pim: Protocol Independent Multicast packets with the destination IPv4 address 224.0.0.13 or IPv6

address FF02::D, or with a destination IP address owned by the switch.

n secure-learn: Packets intercepted and inspected to see if source MAC address is allowed on the port.

n sflow: Packet headers sampled by the switch that will be sent to the sFlow collector.

n stp: Spanning Tree Protocol (STP) packets with the destination MAC address 01:80:c2:00:00:00 or Per-

VLAN Spanning Tree (PVST) packets with the destination MAC address 01:00:0c:cc:cc:cd.

n udld: Unidirectional Link Detection packets with the destination MAC address 01:00:0c:cc:cc:cc or

00:e0:52:00:00:00, or Cisco Discovery Protocol packets with the destination MAC address
01:00:0c:cc:cc:cc.

n unknown-multicast: Packets with an unknown multicast destination IP address.

n unresolved-ip-unicast: Packets to be software forwarded by the management processor.

n vrrp: Virtual Router Redundancy Protocol packets with the destination IPv4 address 224.0.0.18 or IPv6

address FF02::12, or VSX-Keepalive packets.

To regulate any other traffic destined for the CPU, every CoPP policy has a class named default that can
also be configured to regulate other traffic to the CPU or prevent other traffic from being delivered.

All IPsec traffic received by the CPU will be regulated by the ipsec class regardless of the encapsulated protocol.

When ARP protection is enabled on the system, all ARP traffic will be regulated by the arp-protect class,
regardless of the ARP destination and configuration of arp-broadcast or arp-unicast CoPP classes.

Packets for each of the CoPP classes above may have arrived through a tunnel, if tunneling was enabled.

apply copp-policy

Syntax

apply copp-policy { <NAME> | default }
no apply copp-policy <NAME>

Description

Applies a CoPP policy to the switch, replacing the policy that is in effect. There may be a brief interruption in
traffic flow to the management processor while the switch implements the change.

Enter the no apply copp-policy <NAME> command with the name of a CoPP policy to unapply a CoPP
policy and apply the default CoPP policy. This will only take effect if the specified policy is actively applied.
Since there must always be a CoPP policy applied, this command effectively attempts to replace the applied
CoPP policy with the default CoPP policy. The default CoPP policy cannot be unapplied using this command.

Command context

config

Parameters

<NAME>

Control Plane Policing (CoPP) | 10

Specifies the name of the policy to apply. Length: 1 to 64 characters.

default

Applies the default policy.

Authority

Administrators or local user group members with execution rights for this command.

Usage

If the new policy cannot be applied (for example, due to a lack of hardware resources), the previous policy
remains in effect. Use the show copp-policy command to determine which policy is in effect.

Examples

Applying a policy named My_CoppPolicy:

switch(config)# apply copp-policy My_CoppPolicy

Applying the default policy:

switch(config)# apply copp-policy default

Unapplying a policy named My_CoppPolicy:

switch(config)# no apply copp-policy My_CoppPolicy

class

Syntax

class <CLASS> {drop | priority <PRIORITY> rate <RATE> [burst <BURST>]}

no class <CLASS> {drop | priority <PRIORITY> rate <RATE> [burst <BURST>]}

Description

Adds a class to a CoPP policy. If the class exists, the existing class is modified. Changes made to an active
(applied) policy take effect immediately.

When adding or modifying a class in an active policy, CoPP immediately activates the change on the switch.
In cases where insufficient hardware resources exist to support a class or its action, CoPP fails to activate the
changed class on the switch. When this failure occurs, the active configuration on the switch will be out of
sync with its definition. To diagnose and remedy this situation:

n Use the show copp-policy command to determine which classes are out of sync between the active

policy and its definition.

n Use the reset copp-policy command to synchronize the active policy with its definition. This
synchronization changes the classes in the definition to match the classes in the active policy.

The no form of this command removes the configuration for the class. Traffic for the class will be prioritized
and regulated using the factory default configuration for the class. Use the show copp-policy factory-
default command to display the factory default CoPP policy. To stop a class of traffic from reaching the
processor, set the class action to drop.

AOS-CX 10.07 CoPP Guide | 6200, 6300, 6400 Switch Series

11

Command context

config-copp

Parameters

<CLASS>

Specifies the class to add or edit.

drop

Drop packets matching the selected class.

priority <PRIORITY>

Specifies the priority for packets matching the selected class. Range: 0 to 6.

rate <RATE>

Specifies the maximum rate, in packets per second (pps), for packets matching the selected class. Range:
25 to 99999.
burst <BURST>

Specifies the maximum burst size, in packets, for packets matching the selected class. Range: 1 to 9999.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Adding a class to handle LACP traffic with priority of 2 and rate of 2000:

switch(config-copp)# class lacp priority 2 rate 2000

Modifying the class to drop LLDP packets:

switch(config-copp)# class lldp drop

Removing the class that handles LLDP packets.

switch(config-copp)# no class lldp

clear copp-policy statistics

Syntax

clear copp-policy statistics

Description

Resets statistics for all CoPP classes to zero.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Control Plane Policing (CoPP) | 12

Displayingandthenresettingstatisticsforallclassesintheactivepolicy:
| switch#    |     | show copp-policy |             | statistics |            |     |     |
| ---------- | --- | ---------------- | ----------- | ---------- | ---------- | --- | --- |
| Statistics |     | for              | CoPP policy |            | 'default': |     |     |
Totals:
|            | packets       | passed            | :           | 1000       |            | packets dropped | : 1500 |
| ---------- | ------------- | ----------------- | ----------- | ---------- | ---------- | --------------- | ------ |
| Class:     | default       |                   |             |            |            |                 |        |
|            | packets       | passed            | :           | 400        |            | packets dropped | : 600  |
| Class:     | acl-logging   |                   |             |            |            |                 |        |
|            | packets       | passed            | :           | 100        |            | packets dropped | : 100  |
| Class:     | arp-broadcast |                   |             |            |            |                 |        |
|            | packets       | passed            | :           | 500        |            | packets dropped | : 800  |
|            |               | <--OUTPUT         | OMITTED     | FOR        | BREVITY--> |                 |        |
| switch#    |               | clear copp-policy |             | statistics |            |                 |        |
| switch#    |               | show copp-policy  |             | statistics |            |                 |        |
| Statistics |               | for               | CoPP policy |            | 'default': |                 |        |
Totals:
|        | packets       | passed | :   | 0   |     | packets dropped | : 0 |
| ------ | ------------- | ------ | --- | --- | --- | --------------- | --- |
| Class: | default       |        |     |     |     |                 |     |
|        | packets       | passed | :   | 0   |     | packets dropped | : 0 |
| Class: | acl-logging   |        |     |     |     |                 |     |
|        | packets       | passed | :   | 0   |     | packets dropped | : 0 |
| Class: | arp-broadcast |        |     |     |     |                 |     |
|        | packets       | passed | :   | 0   |     | packets dropped | : 0 |
copp-policy
Syntax
| copp-policy    |     | {<NAME> | | default |     | [revert]} |     |     |
| -------------- | --- | ------- | --------- | --- | --------- | --- | --- |
| no copp-policy |     | <NAME>  |           |     |           |     |     |
Description
CreatesaCoPPpolicyandswitchestotheconfig-coppcontextforthepolicy.Or,ifthespecifiedpolicy
exists,switchestotheconfig-coppcontextforthepolicy.Apredefinedpolicy,nameddefault,contains
factorydefaultclassesandisappliedtotheswitchatfirststartup.Thispolicycannotbedeleted,butits
configurationcanbechanged.
ThenoformofthiscommandremovesaCoPPpolicy.Ifapolicyisactive(applied),itcannotberemoved.It
mustbereplacedwithanotherpolicybeforeitcanberemoved.
Commandcontext
config
Parameters
<NAME>
Specifiesthenameofthepolicytoaddoredit.Length:1to64characters.Thenamemustnotbea
substringofanyofthefollowingreservedwords:default,factory-default,commands,configuration,or
statistics.
default
SpecifiesthedefaultCoPPpolicy.Usethisdefaultpolicytoconfigurethedefaultpolicy.
revert
SetsthedefaultCoPPpolicytoitsfactorysettings.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
AOS-CX10.07CoPPGuide|6200,6300,6400SwitchSeries 13

Examples

Creating a policy named My_CoppPolicy:

switch(config)# copp-policy My_CoppPolicy
switch(config-copp)#

Removing a policy named My_CoppPolicy:

switch(config)# no copp-policy My_CoppPolicy

Setting the default policy to its factory settings:

switch(config)# copp-policy default revert

Unapplying the policy named My_CoppPolicy:

switch(config)# no apply copp-policy My_CoppPolicy

default-class

Syntax

default-class priority <PRIORITY> rate <RATE> [burst <BURST>]

Description

Configures the default class that is automatically defined for all CoPP policies. The default class cannot be
removed, but its configuration can be changed. The default class is applied to traffic that does not match
any other class defined for a policy.

Command context

config-copp

Parameters

priority <PRIORITY>

Specifies the priority for packets matching the selected class. Range: 0 to 6.

rate <RATE>

Specifies the maximum rate, in packets per second (pps), for packets matching the selected class. Range:
25 to 99999.
burst <BURST>

Specifies the maximum burst size, in packets, for packets matching the selected class. Range: 1 to 9999.

Authority

Administrators or local user group members with execution rights for this command.

Example

Setting the default class to a priority of 2 and rate of 2000:

Control Plane Policing (CoPP) | 14

| switch(config-copp)# |     | default-class |     | priority |     | 2 rate | 2000 |     |     |
| -------------------- | --- | ------------- | --- | -------- | --- | ------ | ---- | --- | --- |
reset copp-policy
Syntax
| reset copp-policy | { <NAME> |     | | default | }   |     |     |     |     |     |
| ----------------- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- |
Description
ResetsanactiveCoPPpolicytomatchthesettingsthatarecurrentlyineffectfortheactivepolicyonthe
switch.Changesmadetotheactivepolicythatcouldnotbeactivatedareremovedfromtheactivepolicy.
WhentheswitchfailstoaddormodifyaclassinanactiveCoPPpolicy,itispossibletheactivepolicysettings
ontheswitchmaybeoutofsyncwiththosedefinedinthepolicy.
Commandcontext
config
Parameters
<NAME>
Specifiesthenameofthepolicytoreset.Length:1to64characters.
default
Resetsthedefaultpolicytomatchitsactivesettings.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ResettingapolicynamedMy_CoppPolicy:
| switch# show | copp-policy |      | My_CoppPolicy |      |     |       |      |          |          |
| ------------ | ----------- | ---- | ------------- | ---- | --- | ----- | ---- | -------- | -------- |
| class        |             | drop | priority      | rate | pps | burst | pkts | hardware | rate pps |
--------------------- ---- -------- -------- ---------- -----------------
| igmp                 |             |       | 6                | 5000 |               | 60    |       | 5000     |          |
| -------------------- | ----------- | ----- | ---------------- | ---- | ------------- | ----- | ----- | -------- | -------- |
| lacp                 |             |       | 2                | 2000 |               | 2050  |       | 2000     |          |
| default              |             |       | 1                | 6000 |               | 70    |       | 6000     |          |
| switch# config       | terminal    |       |                  |      |               |       |       |          |          |
| switch(config)#      | copp-policy |       | My_CoppPolicy    |      |               |       |       |          |          |
| switch(config-copp)# |             | class | stp priority     |      | 4 rate        | 4000  | burst | 60       |          |
| switch(config-copp)# |             | do    | show copp-policy |      | My_CoppPolicy |       |       |          |          |
| class                |             | drop  | priority         | rate | pps           | burst | pkts  | hardware | rate pps |
--------------------- ---- -------- -------- ---------- -----------------
| igmp    |     |     | 6   | 5000 |     | 60   |     | 5000 |     |
| ------- | --- | --- | --- | ---- | --- | ---- | --- | ---- | --- |
| lacp    |     |     | 2   | 2000 |     | 2050 |     | 2000 |     |
| default |     |     | 1   | 6000 |     | 70   |     | 6000 |     |
% Warning: user-specified classes in CoPP policy My_CoppPolicy do not match
| active configuration. |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
switch(config-copp)# do show copp-policy My_CoppPolicy configuration
| class                 |     | drop | priority | rate     | pps | burst      | pkts | applied |     |
| --------------------- | --- | ---- | -------- | -------- | --- | ---------- | ---- | ------- | --- |
| --------------------- |     | ---- | -------- | -------- |     | ---------- |      | ------- |     |
| igmp                  |     |      | 6        | 5000     |     | 60         |      | yes     |     |
| lacp                  |     |      | 2        | 2000     |     | 2050       |      | yes     |     |
| stp                   |     |      | 4        | 4000     |     | 60         |      | no      |     |
| default               |     |      | 1        | 6000     |     | 70         |      | yes     |     |
% Warning: user-specified classes in CoPP policy My_CoppPolicy do not match
AOS-CX10.07CoPPGuide|6200,6300,6400SwitchSeries 15

active configuration.

switch(config-copp)# exit
switch(config)# reset copp-policy My_CoppPolicy
switch(config)# do show copp-policy My_CoppPolicy
class
drop priority rate pps burst pkts hardware rate pps
--------------------- ---- -------- -------- ---------- -----------------
igmp
lacp
default

60
2050
70

5000
2000
6000

5000
2000
6000

6
2
1

Resetting the default policy:

switch(config)# reset copp-policy default

show copp-policy

Syntax

show copp-policy [<NAME> | default] [commands] [configuration] [vsx-peer]

Description

Shows CoPP policy settings for a specific CoPP policy. When entered without specifying either a name or the
default parameter, shows all the CoPP policy settings that are active on the switch and have successfully
been programmed into the hardware.

A warning is displayed if:

n The active and user-specified applications of a policy do not match.

n The active and user-specified configurations of a policy do not match.

Command context

Operator (>) or Manager (#)

Parameters

<NAME>

Specifies the name of the policy for which to display settings. Length: 1 to 64 characters.

default

Displays CoPP settings for the default policy.

commands

Displays output as CLI commands.

configuration

Displays user-specified CoPP settings and not the active settings.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Control Plane Policing (CoPP) | 16

DisplayingtheCoPPpoliciesdefinedintheconfigurationandtheactiveapplication:
| switch# | show             | copp-policy |     |     |     |     |     |     |     |     |
| ------- | ---------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| applied | copp_policy_name |             |     |     |     |     |     |     |     |     |
| ------- | ---------------- |             |     |     |     |     |     |     |     |     |
My_CoppPolicy
| applied | default |     |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
switch#
DisplayingtheactiveconfigurationofallCoPPpoliciesasCLIcommands:
| switch#     | show          | copp-policy   |          | commands |                |        |            |            |     |     |
| ----------- | ------------- | ------------- | -------- | -------- | -------------- | ------ | ---------- | ---------- | --- | --- |
| copp-policy |               | My_CoppPolicy |          |          |                |        |            |            |     |     |
|             | class         | igmp          | priority | 6        | rate 5000      | burst  | 60         |            |     |     |
|             | class         | lacp          | priority | 2        | rate 2000      | burst  | 2050       |            |     |     |
|             | default-class |               | priority |          | 1 rate         | 6000   | burst      | 70         |     |     |
| copp-policy |               | default       |          |          |                |        |            |            |     |     |
|             | class         | acl-logging   |          | priority | 0              | rate   | 25 burst   | 3          |     |     |
|             | class         | arp-broadcast |          | priority |                | 2 rate | 1250       | burst 1250 |     |     |
|             | class         | arp-protect   |          | priority | 2              | rate   | 2075 burst | 2075       |     |     |
|             | class         | arp-unicast   |          | priority | 3              | rate   | 825 burst  | 825        |     |     |
|             | class         | bfd-control   |          | priority | 5              | rate   | 850 burst  | 850        |     |     |
|             | <--OUTPUT     |               | OMITTED  |          | FOR BREVITY--> |        |            |            |     |     |
|             | default-class |               | priority |          | 2 rate         | 4225   | burst      | 528        |     |     |
| apply       | copp-policy   |               | default  |          |                |        |            |            |     |     |
switch#
Displayingthedefaultpolicy:
switch#
|       | show | copp-policy |     | default |          |      |     |            |          |          |
| ----- | ---- | ----------- | --- | ------- | -------- | ---- | --- | ---------- | -------- | -------- |
| class |      |             |     | drop    | priority | rate | pps | burst pkts | hardware | rate pps |
--------------------- ---- -------- -------- ---------- -----------------
| acl-logging   |             |         |     |                 | 0          | 25   |     | 3    | 25   |     |
| ------------- | ----------- | ------- | --- | --------------- | ---------- | ---- | --- | ---- | ---- | --- |
| arp-broadcast |             |         |     |                 | 2          | 1250 |     | 1250 | 1250 |     |
| arp-protect   |             |         |     |                 | 2          | 2075 |     | 2075 | 2075 |     |
| arp-unicast   |             |         |     |                 | 3          | 825  |     | 825  | 825  |     |
| bfd-control   |             |         |     |                 | 5          | 850  |     | 850  | 850  |     |
|               | <--OUTPUT   | OMITTED |     | FOR             | BREVITY--> |      |     |      |      |     |
| default       |             |         |     |                 | 2          | 4225 |     | 528  | 4225 |     |
| show          | copp-policy |         |     | factory-default |            |      |     |      |      |     |
Syntax
| show | copp-policy | factory-default |     |     | [commands] |     | [vsx-peer] |     |     |     |
| ---- | ----------- | --------------- | --- | --- | ---------- | --- | ---------- | --- | --- | --- |
Description
Displaytheconfigurationforthefactory-defaultCoPPpolicy.
Commandcontext
Operator(>)orManager(#)
Parameters
commands
DisplaysoutputasCLIcommands.
AOS-CX10.07CoPPGuide|6200,6300,6400SwitchSeries 17

[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Displayingthefactory-defaultpolicy:
| switch# show          | copp-policy | factory-default |            |          |            |      |     |
| --------------------- | ----------- | --------------- | ---------- | -------- | ---------- | ---- | --- |
| class                 |             | drop            | priority   | rate pps | burst      | pkts |     |
| --------------------- |             | ----            | --------   | -------- | ---------- |      |     |
| acl-logging           |             |                 | 0          | 25       | 3          |      |     |
| arp-broadcast         |             |                 | 2          | 1250     | 1250       |      |     |
| arp-protect           |             |                 | 2          | 2075     | 2075       |      |     |
| arp-unicast           |             |                 | 3          | 825      | 825        |      |     |
| bfd-control           |             |                 | 5          | 850      | 850        |      |     |
| <--OUTPUT             | OMITTED     | FOR             | BREVITY--> |          |            |      |     |
| default               |             |                 | 2          | 4225     | 528        |      |     |
DisplayingtheactiveconfigurationofMy_CoppPolicy(My_CoppPolicyisapplied):
| switch# config  | terminal |                  |          |               |       |               |          |
| --------------- | -------- | ---------------- | -------- | ------------- | ----- | ------------- | -------- |
| switch(config)# | apply    | copp-policy      |          | My_CoppPolicy |       |               |          |
| switch(config)# | do       | show copp-policy |          | My_CoppPolicy |       |               |          |
| class           |          | drop             | priority | rate pps      | burst | pkts hardware | rate pps |
--------------------- ---- -------- -------- ---------- -----------------
| igmp    |     |     | 6   | 5000 | 60   | 5000 |     |
| ------- | --- | --- | --- | ---- | ---- | ---- | --- |
| lacp    |     |     | 2   | 2000 | 2050 | 2000 |     |
| default |     |     | 1   | 6000 | 70   | 6000 |     |
DisplayingtheactiveconfigurationofMy_CoppPolicyasCLIcommands:
| switch# show      | copp-policy   | My_CoppPolicy |           | commands   |      |     |     |
| ----------------- | ------------- | ------------- | --------- | ---------- | ---- | --- | --- |
| copp-policy       | My_CoppPolicy |               |           |            |      |     |     |
| class             | igmp priority | 6             | rate 5000 | burst      | 60   |     |     |
| class             | lacp priority | 2             | rate 2000 | burst      | 2050 |     |     |
| default-class     | priority      |               | 1 rate    | 6000 burst | 70   |     |     |
| apply copp-policy | My_CoppPolicy |               |           |            |      |     |     |
Displayingtheuser-specifiedconfigurationofMy_CoppPolicy:
| switch# show          | copp-policy | My_CoppPolicy |          | configuration |            |              |     |
| --------------------- | ----------- | ------------- | -------- | ------------- | ---------- | ------------ | --- |
| class                 |             | drop          | priority | rate pps      | burst      | pkts applied |     |
| --------------------- |             | ----          | -------- | --------      | ---------- | -------      |     |
| igmp                  |             |               | 6        | 5000          | 60         | yes          |     |
| lacp                  |             |               | 2        | 2000          | 2050       | yes          |     |
| default               |             |               | 1        | 6000          | 70         | yes          |     |
Displayingtheuser-specifiedconfigurationofMy_CoppPolicyasCLIcommands:
ControlPlanePolicing(CoPP)|18

| switch#           | show          | copp-policy   | My_CoppPolicy |      | commands configuration |
| ----------------- | ------------- | ------------- | ------------- | ---- | ---------------------- |
| copp-policy       | My_CoppPolicy |               |               |      |                        |
| class             | igmp          | priority      | 6 rate        | 5000 | burst 60               |
| class             | lacp          | priority      | 2 rate        | 2000 | burst 2050             |
| default-class     |               | priority      | 1 rate        | 6000 | burst 70               |
| apply copp-policy |               | My_CoppPolicy |               |      |                        |
| show copp-policy  |               | statistics    |               |      |                        |
Syntax
show copp-policy statistics [class <CLASS> | default-class | non-zero] [vsx-peer]
Description
Displaysstatisticsforallclasses,asingleclass,orallclasseswithnon-zerostatisticsintheactiveCoPPpolicy.
Commandcontext
Operator(>)orManager(#)
Parameters
<CLASS>
Specifiestheclassforwhichtodisplaystatistics.
default-class
Displaysstatisticsforthedefaultclass.
non-zero
Displaysstatisticsforallclasseswithnon-zerostatistics.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
Ifasingleclassisspecified,thepriority,rate,andburstsizethathasbeenprogrammedinhardwareforthat
classwillbeshown.
Examples
ApplyingthedefaultCoPPpolicyanddisplayingstatisticsforallclassesintheactivelyappliedpolicy:
Theratedisplayedistheactualrateinhardware.
| switch#         | config | terminal    |             |         |     |
| --------------- | ------ | ----------- | ----------- | ------- | --- |
| switch(config)# |        | apply       | copp-policy | default |     |
| switch(config)# |        | exit        |             |         |     |
| switch#         | show   | copp-policy | statistics  |         |     |
| Statistics      | for    | CoPP policy | 'default':  |         |     |
Totals:
AOS-CX10.07CoPPGuide|6200,6300,6400SwitchSeries 19

| packets |     | passed |     | : 1000 |     |     | packets dropped | : 1500 |
| ------- | --- | ------ | --- | ------ | --- | --- | --------------- | ------ |
Class: default
| packets |     | passed |     | : 400 |     |     | packets dropped | : 600 |
| ------- | --- | ------ | --- | ----- | --- | --- | --------------- | ----- |
Class: acl-logging
| packets |     | passed |     | : 100 |     |     | packets dropped | : 100 |
| ------- | --- | ------ | --- | ----- | --- | --- | --------------- | ----- |
Class: arp-broadcast
| packets |           | passed |         | : 500 |            |     | packets dropped | : 800 |
| ------- | --------- | ------ | ------- | ----- | ---------- | --- | --------------- | ----- |
|         | <--OUTPUT |        | OMITTED | FOR   | BREVITY--> |     |                 |       |
Displayingstatisticsforthedefaultclassintheactivepolicy:
| switch(config)# |     |     | show | copp-policy |            | statistics | default-class |     |
| --------------- | --- | --- | ---- | ----------- | ---------- | ---------- | ------------- | --- |
| Statistics      |     | for | CoPP | policy      | 'default': |            |               |     |
Class: default
| Description: |       | Default |        |       |      |     |                 |       |
| ------------ | ----- | ------- | ------ | ----- | ---- | --- | --------------- | ----- |
| priority     |       |         |        | :     | 2    |     |                 |       |
| rate         | (pps) |         |        | :     | 4225 |     |                 |       |
| burst        |       | size    | (pkts) | :     | 528  |     |                 |       |
| packets      |       | passed  |        | : 400 |      |     | packets dropped | : 600 |
Displayingstatisticsfortheclassarp-broadcastintheactivelyappliedpolicy:
| switch#    | show | copp-policy |      | statistics |            | class | arp-broadcast |     |
| ---------- | ---- | ----------- | ---- | ---------- | ---------- | ----- | ------------- | --- |
| Statistics |      | for         | CoPP | policy     | 'default': |       |               |     |
Class: arp-broadcast
| Description: |       | Address |        | Resolution | Protocol |     | broadcast       |       |
| ------------ | ----- | ------- | ------ | ---------- | -------- | --- | --------------- | ----- |
| priority     |       |         |        | :          | 2        |     |                 |       |
| rate         | (pps) |         |        | :          | 1250     |     |                 |       |
| burst        |       | size    | (pkts) | :          | 1250     |     |                 |       |
| packets      |       | passed  |        | : 500      |          |     | packets dropped | : 800 |
| show tech    |       | copp    |        |            |          |     |                 |       |
Syntax
show tech copp
Description
DisplaystheoutputofallshowcommandssupportedbyCoPP.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Capturingthecommandoutputintoalocalfile:
| switch# | show | tech | copp | local-file |     |     |     |     |
| ------- | ---- | ---- | ---- | ---------- | --- | --- | --- | --- |
Show Tech output stored in local-file. Please use 'copy show-tech local-file' to
| copy-out | this | file.     |     |            |     |     |     |     |
| -------- | ---- | --------- | --- | ---------- | --- | --- | --- | --- |
| switch#  | copy | show-tech |     | local-file |     | ?   |     |     |
ControlPlanePolicing(CoPP)|20

REMOTE_URL

URL of syntax
{tftp://|sftp://USER@}{IP|HOST}[:PORT][;blocksize=VAL]/FILE

STORAGE_URL URL of syntax usb:/file

switch# copy show-tech local-file

AOS-CX 10.07 CoPP Guide | 6200, 6300, 6400 Switch Series

21

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

AOS-CX 10.07 CoPP Guide | 6200, 6300, 6400 Switch Series

22

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

Support and Other Resources | 23