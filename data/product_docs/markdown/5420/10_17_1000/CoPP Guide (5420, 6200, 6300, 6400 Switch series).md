AOS-CX 10.17.xxxx CoPP Guide (5420, 6200, 6300, 6400 Switch
series)

Published: February 2026

AOS-CX 10.17.xxxx CoPP Guide (5420, 6200, 6300, 6400 Switch
series)

Published: February 2026

© Copyright 2026 – Hewlett Packard Enterprise Development LP

Notices

The information provided here is subject to change without notice. Hewlett Packard Enterprise's products
and services are covered only by the express warranty statements that come with them. This document
does not constitute an additional warranty. Hewlett Packard Enterprise is not responsible for any technical
or editorial errors or omissions in this document.

Confidential computer software. You must have a valid license from Hewlett Packard Enterprise to possess,
use, or copy the software. In accordance with FAR 12.211 and 12.212, Commercial Computer Software,
Computer Software Documentation, and Technical Data for Commercial Items are licensed to the U.S.
Government under the vendor's standard commercial license.

Links to third-party websites will take you outside of the Hewlett Packard Enterprise website. Hewlett
Packard Enterprise has no control over and is not responsible for the information outside the Hewlett
Packard Enterprise website.

Open source code

This product includes code licensed under certain open source licenses which require source compliance.
The corresponding source for these components is available upon request. This offer is valid to anyone in
receipt of this information and shall expire three years following the date of the final distribution of this
product version by Hewlett Packard Enterprise Company. To obtain such source code, please check if the
code is available in the HPE Software Center at https://myenterpriselicense.hpe.com/cwp-ui/software
but, if not, send a written request for specific software version and product for which you want the open
source code. Along with the request, please send a check or money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company

Attn: General Counsel

WW Corporate Headquarters

1701 E Mossy Oaks Rd, Spring, TX 77389

United States of America.

Public

AOS-CX 10.17.xxxx CoPP Guide (5420, 6200, 6300, 64...

A
O
S
-
C
X

1
0
.
1
7
.
x
x
x
x

C
o
P
P

G
u
i
d
e

(
5
4
2
0
,

6
2
0
0
,

6
3
0
0
,

6
4
.
.
.

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX 10.17.xxxx CoPP Guide (5420, 6200, 6300, 64...

Table of contents

About this document..................................................................................................................................................................................5

Applicable products........................................................................................................................................................................5

Latest version available online.................................................................................................................................................5

Command syntax notation conventions.............................................................................................................................6

About the examples....................................................................................................................................................................... 7

Identifying switch ports and interfaces...............................................................................................................................8

Identifying modular switch components............................................................................................................................8

Control Plane Policing (CoPP) Overview........................................................................................................................................ 9

Configuring CoPP .....................................................................................................................................................................................10

Actual Rates in Hardware..................................................................................................................................................................... 11

CoPP commands........................................................................................................................................................................................ 11

Classes of traffic.............................................................................................................................................................................12

apply copp-policy ........................................................................................................................................................................15

class ..................................................................................................................................................................................................... 16

clear copp-policy statistics .....................................................................................................................................................18

copp-policy ......................................................................................................................................................................................20

default-class ................................................................................................................................................................................... 22

reset copp-policy ......................................................................................................................................................................... 23

show copp-policy .........................................................................................................................................................................27

show copp-policy factory-default ......................................................................................................................................31

show copp-policy statistics ....................................................................................................................................................35

show tech copp .............................................................................................................................................................................39

Support and Other Resources............................................................................................................................................................40

Accessing HPE Aruba Networking Support..................................................................................................................41

Accessing Updates.......................................................................................................................................................................42

Warranty Information................................................................................................................................................................. 42

Regulatory Information............................................................................................................................................................. 42

Documentation Feedback........................................................................................................................................................43

Public

Table of contents 4

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing HPE Aruba Networking switches on a network.

Subtopics

Applicable products
Latest version available online
Command syntax notation conventions
About the examples
Identifying switch ports and interfaces
Identifying modular switch components

Applicable products

This document applies to the following products:

•  HPE Aruba Networking 5420 Switch Series (S0U67A, S0U55A, S0U63A, S0U64A, S0U65A, S0U75A,

S0U72A, S0U78A, S0U58A, S0U73A, S0U74A, S0U71A, S0U76A, S0U70A, S0U77A, S0U60A,
S0U61A, S0U62A, S0U66A, S0U68A)

•  HPE Aruba Networking 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A,
R8Q68A, R8Q69A, R8Q70A, R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A,
JL724B, JL725B, JL726B, JL727B, JL728B, S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,
S0M87A, S0M88A, S0M89A, S0M90A, S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

•  HPE Aruba Networking 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A,

JL664A, JL665A, JL666A, JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A,
S0X44A, S3L75A, S3L76A, S3L77A, S4P41A,S4P42A, S4P43A, S4P44A, S4P45A, S4P46A, S4P47A,
S4P48A)

•  HPE Aruba Networking 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B,

R0X40C, R0X41A, R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C,
R0X26A, R0X27A, JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

Latest version available online

Public

About this document 5

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

example‐text

example‐text

Any of the following:

•  <example‐text>
•  <example‐text>
•  example‐text
•  example‐text

|

{ }

[ ]

… or

Usage

Identifies commands and their options and operands
, code examples, filenames, pathnames, and output d
isplayed in a command window. Items that appear li
ke the example text in the previous column are to be
entered exactly as shown and are required unless en
closed in brackets ([ ]).

In code and screen examples, indicates text entered
by a user.

Identifies a placeholder—such as a parameter or a va
riable—that you must substitute with an actual valu
e in a command or in code:

•  For output formats where italic text cannot be di
splayed, variables are enclosed in angle brackets
(< >). Substitute the text—including the enclosin
g angle brackets—with an actual value.

•  For output formats where italic text can be displ
ayed, variables might or might not be enclosed i
n angle brackets. Substitute the text including th
e enclosing angle brackets, if any, with an actual
value.

Vertical bar. A logical OR that separates multiple ite
ms from which you can choose only one.

Any spaces that are on either side of the vertical bar
are included for readability and are not a required pa
rt of the command syntax.

Braces. Indicates that at least one of the enclosed ite
ms is required.

Brackets. Indicates that the enclosed item or items a
re optional.

Ellipsis:

Public

Command syntax notation conventions 6

Convention

...

Usage

•

•

In code and screen examples, a vertical or horizo
ntal ellipsis indicates an omission of information.
In syntax using brackets and braces, an ellipsis i
ndicates items that can be repeated. When an ite
m followed by ellipses is enclosed in brackets, ze
ro or more items can be specified.

About the examples

Examples in this document are representative and might not match your particular switch or environment.

The slot and port numbers in this document are for illustration only and might be unavailable on your switch.

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

Public

About the examples 7

Identifying switch ports and interfaces

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format: member/slot/port.

On the HPE Aruba Networking 6200 Switch Series

•  member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the HPE Aruba Networking 6300 Switch Series

•  member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the HPE Aruba Networking 6400 and 5420 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Specifies physical location of a module in the switch chassis.

◦  Management modules are on the front of the switch in slots 1/1 and 1/2.

◦  Line modules are on the front of the switch starting in slot 1/3.

•  port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

Identifying modular switch components

•  Power supplies are on the front of the switch behind the bezel above the management modules. Power

supplies are labeled in software in the format: member/power supply:

Public

Identifying switch ports and interfaces 8

◦  member: 1.

◦  power supply: 1 to 4.

•  Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

◦  member: 1.

◦  tray: 1 to 4.

◦  fan: 1 to 4.

•  Fabric modules are not labeled on the switch but are labeled in software in the format: member/module:

◦  member: 1.

◦  member: 1 or 2.

•  The display module on the rear of the switch is not labeled with a member or slot number.

Control Plane Policing (CoPP) Overview

CoPP provides a way for administrators to protect the management processor on the switch from high
packet loads (generated by malicious or nonmalicious sources) that might interfere with its ability to keep
data plane traffic flowing. For example, a denial of service attack can result in excessive traffic that would
slow down the management processor and negatively affect switch throughput.

A CoPP policy is composed of one or more classes. Each class defines one or more target protocols and how
their traffic is managed. Every policy also has a default class to regulate packets that do not match any other
class. The following actions can be applied for all packets matching a class:

•  Drop the packets. (Excluding the default class.)

•  Set the processing priority in the range 0 to 6 (0 - highest priority and 6 - lowest priority).

•  Set the maximum data rate in packets per second (pps) at which each line module can send packets to

the management processor.

•  Set the maximum burst size in packets at which each line module can send packets to the management

processor.

Up to 32 CoPP policies can be defined, but only one can be active on the switch at a time. A CoPP policy
must always be active on the switch. By default, the switch has a CoPP policy named default which is
automatically applied at first boot.

When a line module is hot-swapped or a new line module comes up after boot on a 6400 switch, the CoPP
policy that is actively applied to the switch will be applied.

Public

Control Plane Policing (CoPP) Overview 9

When the switch reboots, the CoPP policy that was actively applied to the switch before the reboot occurred
s applied if it was saved to the startup configuration with the  copy running-config startup-c
onfig  command.

For GRE tunneled traffic, CoPP policies match on the payload. CoPP policies do not regulate traffic received
from the Out-of-Band-Management (OOBM) Ethernet port.

Configuring CoPP

Procedure

1.  Configure the default CoPP policy, edit an existing policy, or create a policy with the command  copp-p

olicy  .

2.  Add, edit, or remove classes in the policy with the command  class  .

3.

If the policy is not the active policy on the switch, apply it with the command  apply copp-polic
y  . (Changes made to an active policy take effect immediately and do not need to be applied.)

4.  Review the CoPP policy configuration settings with the command  show copp-policy  .

Example

This example creates the following configuration:

•  Defines a new policy named My_CoppPolicy.

•  Adds two classes to the policy.

•  Activates the policy.

•  Displays policy configuration settings.

switch(config)# copp-policy My_CoppPolicy

switch(config-copp)# class igmp priority 6 rate 5000 burst 60

switch(config-copp)# class lacp priority 2 rate 2000 burst 2050

switch(config-copp)# exit

switch(config)# apply copp-policy My_CoppPolicy

switch(config)# exit

switch# show copp-policy My_CoppPolicy

class                 drop priority rate pps burst pkts hardware rate pps

--------------------- ---- -------- -------- ---------- -----------------

igmp                       6        5000     60         5000

lacp                       2        2000     2050       2000

default                    1        6000     70         6000

Public

Configuring CoPP 10

Actual Rates in Hardware

Currently, the actual rate in hardware is determined by a mapping based on the configured rate, shown by
the following table of the first nine actual rates.

| Configured Rate (pps) | Actual Rate in Hardware (pps) |

|-----------------------|-------------------------------|

| 25-49                 | 25                            |

| 50-74                 | 50                            |

| 75-99                 | 75                            |

| 100-124               | 100                           |

| 125-149               | 125                           |

| 150-174               | 150                           |

| 175-199               | 175                           |

| 200-224               | 200                           |

| 225-249               | 225                           |
The preceding table shows the first nine actual rates available in hardware. Higher rates are available. The
'  show copp-policy statistics class <CLASS>  ' command can be used to show the
actual rate in hardware for a specific class. The '  show copp-policy <NAME>  ' command can be
used to show the actual rates for all classes configured in a specific CoPP policy, if the policy is actively
applied.

CoPP commands

Select a command from the list in the left navigation menu.

Subtopics

Classes of traffic
apply copp-policy
class
clear copp-policy statistics
copp-policy
default-class
reset copp-policy
show copp-policy
show copp-policy factory-default
show copp-policy statistics
show tech copp

Public

Actual Rates in Hardware 11

Classes of traffic

The different classes of traffic that can be individually configured are:

Applies to the HPE Aruba Networking 5420, 6200, 6300 and 6400 Switch Series.

•  acl-logging: Access Control List logging packets.

•  arp-broadcast: Address Resolution Protocol packets with a broadcast destination MAC address.

•  arp-protect: Address Resolution Protocol packets intercepted and inspected for ARP protection.

•  arp-unicast: Address Resolution Protocol packets with a switch system destination MAC address.

•  bfd-control: Bidirectional Forwarding Detection (BFD) control packets with a destination IP address

owned by the switch.

NOTE

The bfd-control class is not supported for HPE Aruba Networking 6200 or
5420 Switch series.

•  bgp: Border Gateway Protocol packets with a destination IPv4 or IPv6 address owned by the switch.

NOTE

The bgp class is not supported for HPE Aruba Networking 6200 Switch
series.

•  captive-portal: Packets intercepted in support of the Captive Portal feature.

•  client-onboard: Packets for client onboard protocols such as user-based tunneling.

•  dfp-collector: Packets received for Device FingerPrinting Collector.

•  dhcp: Dynamic Host Configuration Protocol packets. Also includes snooped DHCP packets if DHCP

snooping isenabled.

•  erps: Ethernet Ring Protection Switching control packets with the destination MAC address

01:19:a7:00:00:XX, where XX can be any value or Smartlink packets with the destination MAC address
01:0f:e2:00:00:04.

•  fib-optimization: Packets for Forwarding Information Base (FIB) Optimization.

NOTE

The fib-optimization class is not supported for HPE Aruba Networking 6200
Switch series.

Public

Classes of traffic 12

•

•

icmp-broadcast-ipv4: Internet Control Message Protocol packets with a broadcast or multicast
destination IPv4 address.

icmp-multicast-ipv6: Internet Control Message Protocol packets with a well-known multicast
destination IPv6 address.

•

icmp-security-ipv6: IPv6 Internet Control Message Protocol packets intercepted and inspected.

•

•

icmp-unicast-ipv4: Internet Control Message Protocol packets with a destination IPv4 address owned
by the switch.

icmp-unicast-ipv6: Internet Control Message Protocol packets with a destination IPv6 address owned
by the switch.

•

ieee-8021x: IEEE 802.1X protocol packets with EtherType 0x0888E.

•

igmp: Internet Group Management Protocol packets.

•

ip-exceptions: Routable packets that would exceed the MTU for the egress interface, packets that
trigger ICMP redirects, and packets with TTL/hop_limit=1 that are discarded when routing through the
switch.

•

ip-lockdown: Packets denied and logged due to violation of allowed "IP address/VLAN/port/MAC
address" association.

•

ip-tracker: Packets received for client IP address tracking.

•

ipfix: Packets received for IPFIX (IP Flow Information Export).

NOTE

The ipfix class is not supported for HPE Aruba Networking 6200 Switch
series.

•

ipsec: Internet Protocol Security IPv4 or IPv6, unicast or configured multicast. All IPsec traffic received
by the CPU will be regulated by the 'ipsec' class regardless of the encapsulated protocol.

•

ipv4-options: Unicast IPv4 packets including option headers.

•

lacp: Link Aggregation Control Protocol packets with the destination MAC address 01:80:c2:00:00:02.

•

lldp: Link Layer Discovery Protocol packets with the destination MAC address 01:80:c2:00:00:0e.

•

loop-protect: Loop Protection packets with the destination MAC address 09:00:09:09:13:a6.

•  mac-lockout: Packets denied and logged due to locked-out MAC address.

•  manageability: Unicast IP packets addressed to the switch for specific protocols, like HTTP, SSH, Telnet

and RADIUS that don't have a dedicated CoPP class.

Public

Classes of traffic 13

•  mdns: Multicast Domain Name System packets.

•  mirror-to-cpu: Packets from mirroring session configured to deliver to the console.

•  mld: Multicast Listener Discovery packets of type V1 or V2 with an IPv6 address of FF00::/8, FF02::16 or

FF02::2.

•  mvrp: Multiple VLAN Registration Protocol packets with the destination MAC address

01:80:c2:00:00:0d or 01:80:c2:00:00:21 or Multiple Stream Reservation Protocol with Ether Type
0x22EA.

•  nae-packet-monitor: Network Analytics Engine (NAE) monitored packets.

•  ntp: Network Time Protocol packets with a destination IP address owned by the switch.

•  ospf-multicast: Open Shortest Path First packets with the multicast destination IPv4 address 224.0.0.5

or 224.0.0.6, or IPv6 address FF02::5 or FF02::6, or Routing Information Protocol packets with the
multicast destination IPv4 address 224.0.0.9 or IPv6 address FF02::9, or MPLS Label Distribution
Protocol packets with the multicast destination IPv4 address 224.0.0.2 and destination UDP port 646.
Also includes OSPF multicast packets received from a 6in6 tunnel.

•  ospf-unicast: Open Shortest Path First packets or Routing Information Protocol packets with a local
destination IPv4 address or IPv6 address. Also includes OSPF unicast packets received from a 6in6
tunnel.

•  pim: Protocol Independent Multicast packets with the destination IPv4 address 224.0.0.13 or IPv6
address FF02::D, or Multicast Source Discovery Protocol (MSDP) packets, or with a destination IP
address owned by the switch. Also includes PIM packets received from a 6in6 tunnel.

•  ptp: Precision Time Protocol (PTP) packets to synchronize clocks between networks.

NOTE

The ipfix class is not supported for HPE Aruba Networking 6200 Switch
series.

•  secure-learn: Packets intercepted and inspected to see if source MAC address is allowed on the port.

•  sflow: Packet headers sampled by the switch that will be sent to the sFlow collector.

•  stp: Spanning Tree Protocol (STP) packets with the destination MAC address 01:80:c2:00:00:00 or
Per-VLAN Spanning Tree (PVST) packets with the destination MAC address 01:00:0c:cc:cc:cd.

•  udld: Unidirectional Link Detection packets with the destination MAC address 01:00:0c:cc:cc:cc
or 00:e0:52:00:00:00, or Cisco Discovery Protocol packets with the destination MAC address
01:00:0c:cc:cc:cc.

Public

Classes of traffic 14

•  unknown-multicast: Packets with an unknown multicast destination IP address. Also includes unknown

multicast packets received from a 6in6 tunnel.

•  unresolved-ip-unicast: Packets to be software forwarded by the management processor.

•  vrrp: Virtual Router Redundancy Protocol packets with the destination IPv4 address 224.0.0.18 or IPv6

address FF02::12, or VSX-Keepalive packets.

To regulate any other traffic destined for the CPU, every CoPP policy has a class named  default  that
can also be configured to regulate other traffic to the CPU or prevent other traffic from being delivered.

NOTE
All IPsec traffic received by the CPU will be regulated by the  ipsec  class
regardless of the encapsulated protocol.

When ARP protection is enabled on the system, all ARP traffic will be
regulated by the  arp-protect  class, regardless of the ARP destination and
configuration of  arp-broadcast  or  arp-unicast  CoPP classes.
Packets for each of the CoPP classes above may have arrived through a tunnel, if
tunneling was enabled.

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

Parameter

Description

Specifies the name of the policy to apply. Length: 1 to 64 chara
cters.

<NAME>

Public

apply copp-policy 15

Parameter

default

Usage

Description

Applies the default policy.

If the new policy cannot be applied (for example, due to a lack of hardware resources), the previous policy
remains in effect. Use the show copp-policy command to determine which policy is in effect.

Examples

Applying a policy named My_CoppPolicy:

switch(config)# apply copp-policy My_CoppPolicy

Applying the default policy:

switch(config)# apply copp-policy default

Unapplying a policy named My_CoppPolicy:

switch(config)# no apply copp-policy My_CoppPolicy

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

class

Syntax

class <CLASS> {drop | priority <PRIORITY> rate <RATE> [burst <BURST>]}

no class <CLASS> {drop | priority <PRIORITY> rate <RATE> [burst <BURST>]}

Public

class 16

Description

Adds a class to a CoPP policy. If the class exists, the existing class is modified. Changes made to an active
(applied) policy take effect immediately.

When adding or modifying a class in an active policy, CoPP immediately activates the change on the switch.
In cases where insufficient hardware resources exist to support a class or its action, CoPP fails to activate the
changed class on the switch. When this failure occurs, the active configuration on the switch will be out of
sync with its definition. To diagnose and remedy this situation:

•  Use the show copp-policy command to determine which classes are out of sync between the active

policy and its definition.

•  Use the reset copp-policy command to synchronize the active policy with its definition. This

synchronization changes the classes in the definition to match the classes in the active policy.

The no form of this command removes the configuration for the class. Traffic for the class will be prioritized
and regulated using the factory default configuration for the class. Use the show copp-policy factory-
default command to display the factory default CoPP policy. To stop a class of traffic from reaching the
processor, set the class action to drop.

Parameter

Description

Specifies the class to add or edit.

<CLASS>

drop

Drop packets matching the selected class.

priority <PRIORITY>

Specifies the priority for packets matching the selected class. R
ange: 0 to 6.

rate <RATE>

burst <BURST>

Examples

Specifies the maximum rate, in packets per second (pps), for pa
ckets matching the selected class. Range: 25 to 99999.

Specifies the maximum burst size, in packets, for packets match
ing the selected class. Range: 1 to 9999.

Adding a class to handle LACP traffic with priority of 2 and rate of 2000:

switch(config-copp)# class lacp priority 2 rate 2000

Modifying the class to drop LLDP packets:

switch(config-copp)# class lldp drop

Removing the class that handles LLDP packets.

Public

class 17

switch(config-copp)# no class lldp

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config‐copp

Administrators or local user group members with execution righ
ts for this command.

clear copp-policy statistics

Syntax

clear copp-policy statistics

Description

Resets statistics for all CoPP classes to zero.

Examples

Displaying and then resetting statistics for all classes in the active policy:

switch# show copp-policy statistics

Statistics for CoPP policy 'default':

Totals:

    bytes passed     : 64000              bytes dropped    : 96000

    packets passed   : 1000               packets dropped  : 1500

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

Class: default
    bytes passed     : 25600              bytes dropped    : 38400

    packets passed   : 400                packets dropped  : 600

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

Class: acl-logging

    bytes passed     : 6400               bytes dropped    : 6400

Public

clear copp-policy statistics 18

    packets passed   : 100                packets dropped  : 100

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

Class: arp-broadcast

    bytes passed     : 32000              bytes dropped    : 51200

    packets passed   : 500                packets dropped  : 800

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

        <--OUTPUT OMITTED FOR BREVITY-->

switch# clear copp-policy statistics

switch# show copp-policy statistics

Statistics for CoPP policy 'default':

Totals:

    bytes passed     : 0                  bytes dropped    : 0

    packets passed   : 0                  packets dropped  : 0

    avg_packet_size_passed: 0             avg_packet_size_dropped: 0

Class: default

    bytes passed     : 0                  bytes dropped    : 0

    packets passed   : 0                  packets dropped  : 0

    avg_packet_size_passed: 0             avg_packet_size_dropped: 0

Class: acl-logging

    bytes passed     : 0                  bytes dropped    : 0

    packets passed   : 0                  packets dropped  : 0

    avg_packet_size_passed: 0             avg_packet_size_dropped: 0

Class: arp-broadcast

    bytes passed     : 0                  bytes dropped    : 0

    packets passed   : 0                  packets dropped  : 0

    avg_packet_size_passed: 0             avg_packet_size_dropped: 0

        <--OUTPUT OMITTED FOR BREVITY-->

switch# show copp-policy statistics

Statistics for CoPP policy 'default':

Totals:

    packets passed   : 1000               packets dropped  : 1500

Class: default
    packets passed   : 400                packets dropped  : 600

Class: acl-logging

    packets passed   : 100                packets dropped  : 100

Class: arp-broadcast

    packets passed   : 500                packets dropped  : 800

        <--OUTPUT OMITTED FOR BREVITY-->

switch# clear copp-policy statistics

switch# show copp-policy statistics

Statistics for CoPP policy 'default':

Totals:

    packets passed   : 0                  packets dropped  : 0

Public

clear copp-policy statistics 19

Class: default

    packets passed   : 0                  packets dropped  : 0

Class: acl-logging

    packets passed   : 0                  packets dropped  : 0

Class: arp-broadcast

    packets passed   : 0                  packets dropped  : 0

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

copp-policy

Syntax

copp-policy {<NAME> | default [revert]}

no copp-policy <NAME>

Description

Creates a CoPP policy and switches to the config-copp context for the policy. Or, if the specified policy
exists, switches to the config-copp context for the policy. A predefined policy, named default, contains
factory default classes and is applied to the switch at first startup. This policy cannot be deleted, but its
configuration can be changed.

The no form of this command removes a CoPP policy. If a policy is active (applied), it cannot be removed . It
must be replaced with another policy before it can be removed.

Public

copp-policy 20

Parameter

Description

Specifies the name of the policy to add or edit. Length: 1 to 64
characters. The name must not be a substring of any of the fol
lowing reserved words: default, factory‐default, commands, co
nfiguration, or statistics.

Specifies the default CoPP policy. Use this default policy to conf
igure the default policy.

Sets the default CoPP policy to its factory settings.

<NAME>

default

revert

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

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

Public

copp-policy 21

default-class

Syntax

default-class priority <PRIORITY> rate <RATE> [burst <BURST>]

Description

Configures the default class that is automatically defined for all CoPP policies. The default class cannot be
removed, but its configuration can be changed. The default class is applied to traffic that does not match any
other class defined for a policy.

Parameter

Description

priority <PRIORITY>

Specifies the priority for packets matching the selected class. R
ange: 0 to 6.

rate <RATE>

burst <BURST>

Example

Specifies the maximum rate, in packets per second (pps), for pa
ckets matching the selected class. Range: 25 to 99999.

Specifies the maximum burst size, in packets, for packets match
ing the selected class. Range: 1 to 9999.

Setting the default class to a priority of 2 and rate of 2000:

switch(config-copp)# default-class priority 2 rate 2000

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config‐copp

Administrators or local user group members with execution righ
ts for this command.

Public

default-class 22

reset copp-policy

Syntax

reset copp-policy { <NAME> | default }

Description

Resets an active CoPP policy to match the settings that are currently in effect for the active policy on the
switch. Changes made to the active policy that could not be activated are removed from the active policy.
When the switch fails to add or modify a class in an active CoPP policy, it is possible the active policy
settings on the switch may be out of sync with those defined in the policy.

Parameter

Description

Specifies the name of the policy to reset. Length: 1 to 64 chara
cters.

<NAME>

default

Examples

Resets the default policy to match its active settings.

Resetting a policy named My_CoppPolicy:

switch# show copp-policy My_CoppPolicy

class                 drop priority rate kbps burst kB min-max pps

hardware rate kbps

--------------------- ---- -------- --------- -------- -----------------

------------------

igmp                       6        5000      60       411-9765

5156

lacp                       2        2000      64       164-3906

2343

default                    1        6000      70       494-11718

6093

switch# config terminal

switch(config)# copp-policy My_CoppPolicy

switch(config-copp)# class stp priority 4 rate 4000 burst 60

switch(config-copp)# do show copp-policy My_CoppPolicy

class                 drop priority rate kbps burst kB min-max pps

hardware rate kbps

Public

reset copp-policy 23

--------------------- ---- -------- --------- -------- -----------------

------------------

igmp                       6        5000      60       411-9765

5156

lacp                       2        2000      64       164-3906

2343

default                    1        6000      70       494-11718

6093

% Warning: user-specified classes in CoPP policy My_CoppPolicy do not match

 active configuration.

switch(config-copp)# do show copp-policy My_CoppPolicy configuration

class                 drop priority rate kbps burst kB min-max pps

applied

--------------------- ---- -------- --------- -------- -----------------

-------

igmp                       6        5000      60       411-9765          yes

lacp                       2        2000      64       164-3906          yes

stp                        4        4000      60       329-7812          no

default                    1        6000      70       494-11718         yes

% Warning: user-specified classes in CoPP policy My_CoppPolicy do not match

 active configuration.

switch(config-copp)# exit

switch(config)# reset copp-policy My_CoppPolicy

switch(config)# do show copp-policy My_CoppPolicy

class                 drop priority rate kbps burst kB min-max pps

hardware rate kbps

--------------------- ---- -------- --------- -------- -----------------

------------------

igmp                       6        5000      60       411-9765

5156

lacp                       2        2000      64       164-3906

2343
default                    1        6000      70       494-11718

6093

switch# show copp-policy My_CoppPolicy

class                 drop priority rate pps burst pkts hardware rate pps

--------------------- ---- -------- -------- ---------- -----------------

igmp                       6        5000     60         5000

lacp                       2        2000     1000       2000

default                    1        6000     70         6000

switch# config terminal

switch(config)# copp-policy My_CoppPolicy

switch(config-copp)# class stp priority 4 rate 4000 burst 60

Public

reset copp-policy 24

switch(config-copp)# do show copp-policy My_CoppPolicy

class                 drop priority rate pps burst pkts hardware rate pps

--------------------- ---- -------- -------- ---------- -----------------

igmp                       6        5000     60         5000

lacp                       2        2000     1000       2000

default                    1        6000     70         6000

% Warning: user-specified classes in CoPP policy My_CoppPolicy do not match

 active configuration.

switch(config-copp)# do show copp-policy My_CoppPolicy configuration

class                 drop priority rate pps burst pkts applied

--------------------- ---- -------- -------- ---------- -------

igmp                       6        5000     60         yes

lacp                       2        2000     1000       yes

stp                        4        4000     60         no

default                    1        6000     70         yes

% Warning: user-specified classes in CoPP policy My_CoppPolicy do not match

 active configuration.

switch(config-copp)# exit

switch(config)# reset copp-policy My_CoppPolicy

switch(config)# do show copp-policy My_CoppPolicy

class                 drop priority rate pps burst pkts hardware rate pps

--------------------- ---- -------- -------- ---------- -----------------

igmp                       6        5000     60         5000

lacp                       2        2000     1000       2000

default                    1        6000     70         6000

switch# show copp-policy My_CoppPolicy

class                 drop priority rate pps burst pkts hardware rate pps

--------------------- ---- -------- -------- ---------- -----------------

igmp                       6        5000     60         5000

lacp                       2        2000     2050       2000

default                    1        6000     70         6000

switch# config terminal
switch(config)# copp-policy My_CoppPolicy

switch(config-copp)# class stp priority 4 rate 4000 burst 60

switch(config-copp)# do show copp-policy My_CoppPolicy

class                 drop priority rate pps burst pkts hardware rate pps

--------------------- ---- -------- -------- ---------- -----------------

igmp                       6        5000     60         5000

lacp                       2        2000     2050       2000

default                    1        6000     70         6000

% Warning: user-specified classes in CoPP policy My_CoppPolicy do not match

 active configuration.

switch(config-copp)# do show copp-policy My_CoppPolicy configuration

Public

reset copp-policy 25

class                 drop priority rate pps burst pkts applied

--------------------- ---- -------- -------- ---------- -------

igmp                       6        5000     60         yes

lacp                       2        2000     2050       yes

stp                        4        4000     60         no

default                    1        6000     70         yes

% Warning: user-specified classes in CoPP policy My_CoppPolicy do not match

 active configuration.

switch(config-copp)# exit

switch(config)# reset copp-policy My_CoppPolicy

switch(config)# do show copp-policy My_CoppPolicy

class                 drop priority rate pps burst pkts hardware rate pps

--------------------- ---- -------- -------- ---------- -----------------

igmp                       6        5000     60         5000

lacp                       2        2000     2050       2000

default                    1        6000     70         6000

switch# show copp-policy My_CoppPolicy

class                 drop priority rate pps hardware rate pps

--------------------- ---- -------- -------- -----------------

igmp                       6        5000     5000

lacp                       2        2000     2000

default                    1        6000     6000

switch# config terminal

switch(config)# copp-policy My_CoppPolicy

switch(config-copp)# class stp priority 4 rate 4000

switch(config-copp)# do show copp-policy My_CoppPolicy

class                 drop priority rate pps hardware rate pps

--------------------- ---- -------- -------- -----------------

igmp                       6        5000     5000

lacp                       2        2000     2000

default                    1        6000     6000

% Warning: user-specified classes in CoPP policy My_CoppPolicy do not match
 active configuration.

switch(config-copp)# do show copp-policy My_CoppPolicy configuration

class                 drop priority rate pps applied

--------------------- ---- -------- -------- -------

igmp                       6        5000     yes

lacp                       2        2000     yes

stp                        4        4000     no

default                    1        6000     yes

% Warning: user-specified classes in CoPP policy My_CoppPolicy do not match

 active configuration.

switch(config-copp)# exit

Public

reset copp-policy 26

switch(config)# reset copp-policy My_CoppPolicy

switch(config)# do show copp-policy My_CoppPolicy

class                 drop priority rate pps hardware rate pps

--------------------- ---- -------- -------- -----------------

igmp                       6        5000     5000

lacp                       2        2000     2000

default                    1        6000     6000
Resetting the default policy:

switch(config)# reset copp-policy default

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

show copp-policy

Syntax

show copp-policy  [<NAME> | default] [commands] [configuration] [vsx-peer]

Description

Shows CoPP policy settings for a specific CoPP policy. When entered without specifying either a name
or the  default  parameter, shows all the CoPP policy settings that are active on the switch and have
successfully been programmed into the hardware.

A warning is displayed if:

•  The active and user-specified applications of a policy do not match.

•  The active and user-specified configurations of a policy do not match.

Public

show copp-policy 27

Parameter

Description

Specifies the name of the policy for which to display settings.
Length: 1 to 64 characters.

<NAME>

default

commands

configuration

vsx‐peer

Displays CoPP settings for the default policy.

Displays output as CLI commands.

Displays user‐specified CoPP settings and not the active setti
ngs.

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Example

Displaying the CoPP policies defined in the configuration and the active application:

switch#

            show copp-policy

applied copp_policy_name

------- ----------------

        My_CoppPolicy

applied default

switch#
Displaying the active configuration of all CoPP policies as CLI commands:

switch# show copp-policy commands

copp-policy My_CoppPolicy

    class igmp priority 6 rate 5000 burst 60

    class lacp priority 2 rate 2000 burst 64

    default-class priority 1 rate 6000 burst 70

copp-policy default

    class acl-logging priority 0 rate 468 burst 4

    class arp-broadcast priority 4 rate 1406 burst 4

    class arp-protect priority 4 rate 2343 burst 4

    class arp-unicast priority 5 rate 937 burst 4

    class bfd-control priority 9 rate 937 burst 16

        <--OUTPUT OMITTED FOR BREVITY-->

Public

show copp-policy 28

    default-class priority 1 rate 17343 burst 16

apply copp-policy default

switch#

switch# show copp-policy commands

copp-policy My_CoppPolicy

    class igmp priority 6 rate 5000 burst 60

    class lacp priority 2 rate 2000 burst 1000

    default-class priority 1 rate 6000 burst 70

copp-policy default

    class acl-logging priority 0 rate 50 burst 50

    class arp-broadcast priority 3 rate 7000 burst 7000

    class arp-unicast priority 4 rate 2500 burst 2500

    class bfd priority 7 rate 1000 burst 1000

        <--OUTPUT OMITTED FOR BREVITY-->

    default-class priority 1 rate 1000 burst 500

apply copp-policy default

switch#

switch# show copp-policy commands

copp-policy My_CoppPolicy

    class igmp priority 6 rate 5000 burst 60

    class lacp priority 2 rate 2000 burst 2050

    default-class priority 1 rate 6000 burst 70

copp-policy default

    class acl-logging priority 0 rate 25 burst 3

    class arp-broadcast priority 2 rate 1250 burst 1250

    class arp-protect priority 2 rate 2075 burst 2075

    class arp-unicast priority 3 rate 825 burst 825

    class bfd-control priority 5 rate 850 burst 850

        <--OUTPUT OMITTED FOR BREVITY-->

    default-class priority 2 rate 4225 burst 528

apply copp-policy default

switch#
Displaying the  default  policy:

switch# show copp-policy default

class                 drop priority rate kbps burst kB min-max pps

hardware rate kbps

--------------------- ---- -------- --------- -------- -----------------

------------------

acl-logging                0        468       4        38-906            468
arp-broadcast              4        1406      4        115-2734

1406

arp-protect                4        2343      4        192-4562

2343

Public

show copp-policy 29

arp-unicast                5        937       4        77-1828           937

bfd-control                9        937       16       77-1828           937

    <--OUTPUT OMITTED FOR BREVITY-->

default                    1        17343     16       1427-33859

17343

switch# show copp-policy default

class                 drop priority rate pps burst pkts hardware rate pps

--------------------- ---- -------- -------- ---------- -----------------

acl-logging                0        50       50         50

arp-broadcast              3        7000     7000       7000

arp-unicast                4        2500     2500       2500

bfd                        7        1000     1000       1000

    <--OUTPUT OMITTED FOR BREVITY-->

default                    1        1000     500        1000

switch# show copp-policy default

class                 drop priority rate pps burst pkts hardware rate pps

--------------------- ---- -------- -------- ---------- -----------------

acl-logging                0        25       3          25

arp-broadcast              2        1250     1250       1250

arp-protect                2        2075     2075       2075

arp-unicast                3        825      825        825

bfd-control                5        850      850        850

    <--OUTPUT OMITTED FOR BREVITY-->

default                    2        4225     528        4225

switch# show copp-policy default

class                 drop priority rate pps hardware rate pps

--------------------- ---- -------- -------- -----------------

arp-broadcast              2        1250     1250

arp-unicast                3        825      825

    <--OUTPUT OMITTED FOR BREVITY-->

default                    2        4225     4225

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show copp-policy 30

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show copp-policy factory-default

Syntax

show copp-policy factory-default [commands] [vsx-peer]

Description

Display the configuration for the factory-default CoPP policy.

Parameter

commands

vsx‐peer

Description

Displays output as CLI commands.

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Example

Displaying the factory-default policy:

switch# show copp-policy factory-default

class                 drop priority rate kbps burst kB min-max pps

--------------------- ---- -------- --------- -------- -----------------

acl-logging                0        468       4        38-906

arp-broadcast              4        1406      4        115-2734

arp-protect                4        2343      4        192-4562
arp-unicast                5        937       4        77-1828

bfd-control                9        937       16       77-1828

    <--OUTPUT OMITTED FOR BREVITY-->

default                    1        17343     16       1427-33859

Public

show copp-policy factory-default 31

switch# show copp-policy factory-default

class                 drop priority rate pps burst pkts

--------------------- ---- -------- -------- ----------

acl-logging                0        50       50

arp-broadcast              3        7000     7000

arp-unicast                4        2500     2500

bfd                        7        1000     1000

    <--OUTPUT OMITTED FOR BREVITY-->

default                    1        1000     500

switch# show copp-policy factory-default

class                 drop priority rate pps burst pkts

--------------------- ---- -------- -------- ----------

acl-logging                0        25       3

arp-broadcast              2        1250     1250

arp-protect                2        2075     2075

arp-unicast                3        825      825

bfd-control                5        850      850

    <--OUTPUT OMITTED FOR BREVITY-->

default                    2        4225     528

switch# show copp-policy factory-default

class                 drop priority rate pps

--------------------- ---- -------- --------

arp-broadcast              2        1250

arp-unicast                3        825

    <--OUTPUT OMITTED FOR BREVITY-->

default                    2        4225
Displaying the active configuration of My_CoppPolicy (My_CoppPolicy is applied):

switch# config terminal

switch(config)# apply copp-policy My_CoppPolicy

switch(config)# do show copp-policy My_CoppPolicy

class                 drop priority rate kbps burst kB min-max pps

hardware rate kbps

--------------------- ---- -------- --------- -------- -----------------

------------------

igmp                       6        5000      60       411-9765

5156

lacp                       2        2000      64       164-3906

2343

default                    1        6000      70       494-11718

6093

switch# config terminal

switch(config)# apply copp-policy My_CoppPolicy

switch(config)# do show copp-policy My_CoppPolicy

Public

show copp-policy factory-default 32

class                 drop priority rate pps burst pkts hardware rate pps

--------------------- ---- -------- -------- ---------- -----------------

igmp                       6        5000     60         5000

lacp                       2        2000     1000       2000

default                    1        6000     70         6000

switch# config terminal

switch(config)# apply copp-policy My_CoppPolicy

switch(config)# do show copp-policy My_CoppPolicy

class                 drop priority rate pps burst pkts hardware rate pps

--------------------- ---- -------- -------- ---------- -----------------

igmp                       6        5000     60         5000

lacp                       2        2000     2050       2000

default                    1        6000     70         6000

switch# config terminal

switch(config)# apply copp-policy My_CoppPolicy

switch(config)# do show copp-policy My_CoppPolicy

class                 drop priority rate pps hardware rate pps

--------------------- ---- -------- -------- -----------------

igmp                       6        5000     5000

lacp                       2        2000     2000

default                    1        6000     6000
Displaying the active configuration of My_CoppPolicy as CLI commands:

switch# show copp-policy My_CoppPolicy commands

copp-policy My_CoppPolicy

    class igmp priority 6 rate 5000 burst 60

    class lacp priority 2 rate 2000 burst 64

    default-class priority 1 rate 6000 burst 70

apply copp-policy My_CoppPolicy

switch# show copp-policy My_CoppPolicy commands

copp-policy My_CoppPolicy

    class igmp priority 6 rate 5000 burst 60

    class lacp priority 2 rate 2000 burst 1000

    default-class priority 1 rate 6000 burst 70

apply copp-policy My_CoppPolicy

switch# show copp-policy My_CoppPolicy commands

copp-policy My_CoppPolicy

    class igmp priority 6 rate 5000 burst 60

    class lacp priority 2 rate 2000 burst 2050

    default-class priority 1 rate 6000 burst 70

apply copp-policy My_CoppPolicy

switch# show copp-policy My_CoppPolicy commands

copp-policy My_CoppPolicy

    class igmp priority 6 rate 5000

Public

show copp-policy factory-default 33

    class lacp priority 2 rate 2000

    default-class priority 1 rate 6000

apply copp-policy My_CoppPolicy
Displaying the user-specified configuration of My_CoppPolicy:

switch# show copp-policy My_CoppPolicy configuration

class                 drop priority rate kbps burst kB min-max pps

applied

--------------------- ---- -------- --------- -------- -----------------

-------

igmp                       6        5000      60       411-9765          yes

lacp                       2        2000      64       164-3906          yes

default                    1        6000      70       494-11718         yes

switch# show copp-policy My_CoppPolicy configuration

class                 drop priority rate pps burst pkts applied

--------------------- ---- -------- -------- ---------- -------

igmp                       6        5000     60         yes

lacp                       2        2000     1000       yes

default                    1        6000     70         yes

switch# show copp-policy My_CoppPolicy configuration

class                 drop priority rate pps burst pkts applied

--------------------- ---- -------- -------- ---------- -------

igmp                       6        5000     60         yes

lacp                       2        2000     2050       yes

default                    1        6000     70         yes

switch# show copp-policy My_CoppPolicy configuration

class                 drop priority rate pps applied

--------------------- ---- -------- -------- -------

igmp                       6        5000     yes

lacp                       2        2000     yes

default                    1        6000     yes
Displaying the user-specified configuration of My_CoppPolicy as CLI commands:

switch# show copp-policy My_CoppPolicy commands configuration

copp-policy My_CoppPolicy

    class igmp priority 6 rate 5000 burst 60

    class lacp priority 2 rate 2000 burst 64

    default-class priority 1 rate 6000 burst 70

apply copp-policy My_CoppPolicy

switch# show copp-policy My_CoppPolicy commands configuration
copp-policy My_CoppPolicy

    class igmp priority 6 rate 5000 burst 60

    class lacp priority 2 rate 2000 burst 1000

    default-class priority 1 rate 6000 burst 70

apply copp-policy My_CoppPolicy

Public

show copp-policy factory-default 34

switch# show copp-policy My_CoppPolicy commands configuration

copp-policy My_CoppPolicy

    class igmp priority 6 rate 5000 burst 60

    class lacp priority 2 rate 2000 burst 2050

    default-class priority 1 rate 6000 burst 70

apply copp-policy My_CoppPolicy

switch# show copp-policy My_CoppPolicy commands configuration

copp-policy My_CoppPolicy

    class igmp priority 6 rate 5000

    class lacp priority 2 rate 2000

    default-class priority 1 rate 6000

apply copp-policy My_CoppPolicy

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show copp-policy statistics

Syntax

show copp-policy statistics [class <CLASS> | default-class | non-zero] [vsx-

peer]

Description

Displays statistics for all classes, a single class, or all classes with non-zero statistics in the active CoPP
policy.

Public

show copp-policy statistics 35

Parameter

Description

Specifies the class for which to display statistics.

<CLASS>

default‐class

Displays statistics for the default class.

non‐zero

vsx‐peer

Usage

Displays statistics for all classes with non‐zero statistics.

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

If a single class is specified, the priority, rate, and burst size that has been programmed in hardware for that
class will be shown.

Examples

Applying the default CoPP policy and displaying statistics for all classes in the actively applied policy:

NOTE

The rate displayed is the actual rate in hardware.

switch# config terminal

switch(config)# apply copp-policy default

switch(config)# exit

switch# show copp-policy statistics

Statistics for CoPP policy 'default':
Totals:

    bytes passed     : 64000              bytes dropped    : 96000

    packets passed   : 1000               packets dropped  : 1500

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

Class: default

    bytes passed     : 25600              bytes dropped    : 38400

    packets passed   : 400                packets dropped  : 600

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

Class: acl-logging

    bytes passed     : 6400               bytes dropped    : 6400

    packets passed   : 100                packets dropped  : 100

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

Public

show copp-policy statistics 36

Class: arp-broadcast

    bytes passed     : 32000              bytes dropped    : 51200

    packets passed   : 500                packets dropped  : 800

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

        <--OUTPUT OMITTED FOR BREVITY-->

switch# config terminal

switch(config)# apply copp-policy default

switch(config)# exit

switch# show copp-policy statistics

Statistics for CoPP policy 'default':

Totals:

    packets passed   : 1000               packets dropped  : 1500

Class: default

    packets passed   : 400                packets dropped  : 600

Class: acl-logging

    packets passed   : 100                packets dropped  : 100

Class: arp-broadcast

    packets passed   : 500                packets dropped  : 800

        <--OUTPUT OMITTED FOR BREVITY-->

switch# config terminal

switch(config)# apply copp-policy default

switch(config)# exit

switch# show copp-policy statistics

Statistics for CoPP policy 'default':

Totals:

    packets passed   : 1000               packets dropped  : 1500

Class: default

    packets passed   : 400                packets dropped  : 600

Class: arp-broadcast

    packets passed   : 500                packets dropped  : 800

        <--OUTPUT OMITTED FOR BREVITY-->
Displaying statistics for the default class in the active policy:

switch(config)# show copp-policy statistics default-class

Statistics for CoPP policy 'default':

Class: default

Description: Default

    priority             : 1

    rate (kbps)          : 17343

    burst size (bytes)   : 16
    bytes passed     : 25600              bytes dropped    : 38400

    packets passed   : 400                packets dropped  : 600

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

switch(config)# show copp-policy statistics default-class

Public

show copp-policy statistics 37

Statistics for CoPP policy 'default':

Class: default

Description: Default

    priority             : 1

    rate (pps)           : 1000

    burst size (pkts)    : 500

    bytes passed     : 25600              bytes dropped    : 38400

    packets passed   : 400                packets dropped  : 600

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

switch(config)# show copp-policy statistics default-class

Statistics for CoPP policy 'default':

Class: default

Description: Default

    priority             : 2

    rate (pps)           : 4225

    burst size (pkts)    : 528

    packets passed   : 400                packets dropped  : 600

switch(config)# show copp-policy statistics default-class

Statistics for CoPP policy 'default':

Class: default

Description: Default

    priority             : 2

    rate (pps)           : 4225

    packets passed   : 400                packets dropped  : 600
Displaying statistics for the class arp-broadcast in the actively applied policy:

switch# show copp-policy statistics class arp-broadcast

Statistics for CoPP policy 'default':

Class: arp-broadcast

Description: Address Resolution Protocol broadcast

    priority             : 4

    rate (kbps)          : 1406

    burst size (bytes)   : 4

    bytes passed     : 32000              bytes dropped    : 51200

    packets passed   : 500                packets dropped  : 800

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

switch# show copp-policy statistics class arp-broadcast

Statistics for CoPP policy 'default':

Class: arp-broadcast

Description: Address Resolution Protocol broadcast

    priority             : 3

    rate (pps)           : 7000

    burst size (pkts)    : 7000

    bytes passed     : 32000              bytes dropped    : 51200

Public

show copp-policy statistics 38

    packets passed   : 500                packets dropped  : 800

    avg_packet_size_passed: 64            avg_packet_size_dropped: 64

switch# show copp-policy statistics class arp-broadcast

Statistics for CoPP policy 'default':

Class: arp-broadcast

Description: Address Resolution Protocol broadcast

    priority             : 2

    rate (pps)           : 1250

    burst size (pkts)    : 1250

    packets passed   : 500                packets dropped  : 800

switch# show copp-policy statistics class arp-broadcast

Statistics for CoPP policy 'default':

Class: arp-broadcast

Description: Address Resolution Protocol broadcast

    priority             : 2

    rate (pps)           : 1250

    packets passed   : 500                packets dropped  : 800

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show tech copp

Syntax

show tech copp

Description

Displays the output of all show commands supported by CoPP.

Public

show tech copp 39

Examples

Capturing the command output into a local file:

switch# show tech copp local-file

Show Tech output stored in local-file.  Please use 'copy show-tech local-

file' to copy-out this file.

switch# copy show-tech local-file ?

  REMOTE_URL   URL of syntax

               {tftp://|sftp://USER@}{IP|HOST}[:PORT][;blocksize=VAL]/FILE

  STORAGE_URL  URL of syntax usb:/file

switch# copy show-tech local-file

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

Support and Other Resources

Access HPE Aruba Networking support and updates, and view warranty and regulatory information

Subtopics

Accessing HPE Aruba Networking Support
Accessing Updates
Warranty Information
Regulatory Information
Documentation Feedback

Public

Support and Other Resources 40

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

AOS‐CX Switch Software Documentation Portal

https://www.hpe.com/us/en/networking/hpe‐aru
ba‐networking‐support‐services.html

https://arubanetworking.hpe.com/techdocs/Aruba
DocPortal/content/new-portal/aoscx.html

HPE Aruba Networking Support Portal

https://networkingsupport.hpe.com/home

North America telephone

1‐800‐943‐4526 (US & Canada Toll‐Free Nu
mber)

+1‐650‐750‐0350 (Backup—Toll Number)

International telephone

https://www.hpe.com/psnow/doc/a50011948enw

Be sure to collect the following information before contacting Support:

•  Technical support registration number (if applicable)

•  Product name, model or version, and serial number

•  Operating system name and version

•  Firmware version

•  Error messages

•  Product-specific reports and logs

•  Add-on products or components

•  Third-party products or components

Other useful sites

Other websites that can be used to find information:

HPE Aruba Networking Developer Hub

https://developer.arubanetworks.com/hpe‐aruba
‐networking‐aoscx/docs/about

Airheads social forums and Knowledge Base

https://community.arubanetworks.com/

Public

Accessing HPE Aruba Networking Support 41

AOS‐CX Software Technical Update channel on You
Tube.

Videos on new features introduced in this release
: https://www.youtube.com/playlist?list=PLsYGHu
NuBZcbWPEjjHuVMqP‐Q_UL3CskS

HPE Aruba Networking Hardware Documentation an
d Translations Portal

HPE Aruba Networking software

https://networkingsupport.hpe.com/downloads h
ttps://networkingsupport.hpe.com/downloads

Software licensing and Feature Packs

https://licensemanagement.hpe.com/

End‐of‐Life information

https://networkingsupport.hpe.com/end‐of‐life

Accessing Updates

You can access updates from the HPE Aruba Networking Support Portal at https://
networkingsupport.hpe.com.

Some software products provide a mechanism for accessing software updates through the product interface.
Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://networkingsupport.hpe./notifications/subscriptions (requires an active HPE Aruba Networking
Support Portal account to manage subscriptions). Security notices are viewable without an HPE Aruba
Networking Support Portal account.

Warranty Information

To view warranty information for your product, go to https://www.arubanetworks.com/support-services/
product-warranties/.

Regulatory Information

Public

Accessing Updates 42

To view the regulatory information for your product, view the Safety and Compliance Information for
Server, Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

HPE Aruba Networking is committed to providing our customers with information about the chemical
substances in our products as needed to comply with legal requirements, environmental data (company
programs, product recycling, energy efficiency), and safety information and compliance data, (RoHS and
WEEE). For more information, see https://www.arubanetworks.com/company/about-us/environmental-
citizenship/.

Documentation Feedback

HPE Aruba Networking is committed to providing documentation that meets your needs. To help us improve
the documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition, and
publication date located on the front cover of the document. For online help content, include the product
name, product version, help edition, and publication date located on the legal notices page.

Public

Documentation Feedback 43

