AOS-CX 10.06 IP Services Guide
6100 Switch Series

Part Number: 5200-7777
Published: January 2021
Edition: 1

© Copyright 2021 Hewlett Packard Enterprise Development LP

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
Enterprise has no control over and is not responsible for information outside the Hewlett Packard Enterprise
website.

Acknowledgments

Intel®, Itanium®, Optane™, Pentium®, Xeon®, Intel Inside®, and the Intel Inside logo are trademarks of Intel
Corporation in the U.S. and other countries.

Microsoft® and Windows® are either registered trademarks or trademarks of Microsoft Corporation in the
United States and/or other countries.

Adobe® and Acrobat® are trademarks of Adobe Systems Incorporated.

Java® and Oracle® are registered trademarks of Oracle and/or its affiliates.

UNIX® is a registered trademark of The Open Group.

All third-party marks are property of their respective owners.

Contents

Chapter 1 About this document...................................................................... 6
Applicable products........................................................................................................................................6
Latest version available online......................................................................................................................6
Command syntax notation conventions..................................................................................................... 6
About the examples....................................................................................................................................... 7
Identifying switch ports and interfaces .......................................................................................................7

Chapter 2 IRDP..................................................................................................... 9
Configuring IRDP.......................................................................................................................................... 10
IRDP commands .......................................................................................................................................... 11
diag-dump irdp basic................................................................................................................11
ip irdp............................................................................................................................................. 12
ip irdp holdtime.........................................................................................................................12
ip irdp maxadvertinterval.................................................................................................... 13
ip irdp minadvertinterval.................................................................................................... 13
ip irdp preference.................................................................................................................... 14
show ip irdp..................................................................................................................................15

Chapter 3 IPv6 Router Advertisement......................................................... 16
Configuring IPv6 RA......................................................................................................................................16
IPv6 RA scenario........................................................................................................................................... 18
IPv6 RA commands.......................................................................................................................................18
ipv6 address <global-unicast-address>......................................................................... 18
ipv6 address autoconfig......................................................................................................... 19
ipv6 address link-local......................................................................................................... 20
ipv6 nd cache-limit.................................................................................................................. 21
ipv6 nd dad attempts................................................................................................................21
ipv6 nd hop-limit...................................................................................................................... 22
ipv6 nd mtu.................................................................................................................................... 22
ipv6 nd ns-interval.................................................................................................................. 23
ipv6 nd prefix............................................................................................................................. 23
ipv6 nd ra dns search-list.................................................................................................. 25
ipv6 nd ra dns server............................................................................................................. 25
ipv6 nd ra lifetime.................................................................................................................. 26
ipv6 nd ra managed-config-flag......................................................................................... 27
ipv6 nd ra max-interval......................................................................................................... 28
ipv6 nd ra min-interval......................................................................................................... 29
ipv6 nd ra other-config-flag..............................................................................................29
ipv6 nd ra reachable-time.................................................................................................... 30
ipv6 nd ra retrans-timer.......................................................................................................31
ipv6 nd router-preference.................................................................................................... 31
ipv6 nd suppress-ra.................................................................................................................. 32
show ipv6 nd global traffic................................................................................................ 33
show ipv6 nd interface........................................................................................................... 34
show ipv6 nd interface prefix........................................................................................... 36
show ipv6 nd ra dns search-list....................................................................................... 37

Contents

3

show ipv6 nd ra dns server.................................................................................................. 38

Chapter 4 sFlow................................................................................................. 39
sFlow agent................................................................................................................................................... 39
Configuring the sFlow agent....................................................................................................................... 40
sFlow scenario.............................................................................................................................................. 41
sFlow scenario 2........................................................................................................................................... 42
sFlow agent commands .............................................................................................................................. 44
sflow..................................................................................................................................................44
sflow agent-ip............................................................................................................................. 45
sflow collector........................................................................................................................... 46
sflow disable............................................................................................................................... 47
sflow header-size...................................................................................................................... 47
sflow max-datagram-size......................................................................................................... 48
sflow polling............................................................................................................................... 48
sflow sampling............................................................................................................................. 49
show sflow...................................................................................................................................... 50

Chapter 5 DHCP client......................................................................................52
DHCP client commands............................................................................................................................... 52
ip dhcp............................................................................................................................................. 52

Chapter 6 Internet Control Message Protocol (ICMP).............................. 53
ICMP message types.................................................................................................................................... 53
When ICMP messages are sent.................................................................................................................. 54
ICMP redirect messages.............................................................................................................................. 54
When ICMP redirect messages are sent.................................................................................................... 54
ICMP commands.......................................................................................................................................... 54
ip icmp redirect.........................................................................................................................54
ip icmp throttle.........................................................................................................................55
ip icmp unreachable.................................................................................................................. 55

Chapter 7 DNS....................................................................................................57
DNS client...................................................................................................................................................... 57
Configuring the DNS client.......................................................................................................................... 57
DNS client commands .................................................................................................................................58
ip dns domain-list.................................................................................................................... 58
ip dns domain-name.................................................................................................................... 59
ip dns host.................................................................................................................................... 59
ip dns server address............................................................................................................. 60
show ip dns.................................................................................................................................... 61

Chapter 8 ARP.................................................................................................... 62
ARP commands.............................................................................................................................................63
arp cache-limit........................................................................................................................... 63
arp inspection............................................................................................................................. 64
arp inspection trust................................................................................................................64
arp ipv4 mac..................................................................................................................................65
clear arp........................................................................................................................................ 65
ipv6 neighbor mac...................................................................................................................... 66

4

AOS-CX 10.06 IP Services Guide

show arp...........................................................................................................................................67
show arp inspection interface........................................................................................... 67
show arp inspection statistics......................................................................................... 68
show arp state............................................................................................................................. 69
show arp summary.........................................................................................................................70
show arp timeout.........................................................................................................................71
show arp vrf..................................................................................................................................72
show ipv6 neighbors.................................................................................................................. 73
show ipv6 neighbors state.................................................................................................... 74

Chapter 9 Support and other resources...................................................... 76
Accessing Aruba Support............................................................................................................................ 76
Accessing updates........................................................................................................................................ 76
Warranty information.................................................................................................................................. 77
Regulatory information............................................................................................................................... 77
Documentation feedback............................................................................................................................ 77

Contents

5

Chapter 1
About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and other resources.

Command syntax notation conventions

Convention

example-text

Usage

Identifies commands and their options and operands, code examples,
filenames, pathnames, and output displayed in a command window.
Items that appear like the example text in the previous column are to be
entered exactly as shown and are required unless enclosed in brackets
([ ]).

example-text

In code and screen examples, indicates text entered by a user.

Any of the following:

• <example-text>

• <example-text>

• example-text

•

example-text

|

{ }

Identifies a placeholder—such as a parameter or a variable—that you
must substitute with an actual value in a command or in code:

•

•

For output formats where italic text cannot be displayed, variables
are enclosed in angle brackets (< >). Substitute the text—including
the enclosing angle brackets—with an actual value.

For output formats where italic text can be displayed, variables might
or might not be enclosed in angle brackets. Substitute the text
including the enclosing angle brackets, if any, with an actual value.

Vertical bar. A logical OR that separates multiple items from which you
can choose only one.

Any spaces that are on either side of the vertical bar are included for
readability and are not a required part of the command syntax.

Braces. Indicates that at least one of the enclosed items is required.

Table Continued

6

AOS-CX 10.06 IP Services Guide

Convention

Usage

[ ]

… or

...

Brackets. Indicates that the enclosed item or items are optional.

Ellipsis:

•

•

In code and screen examples, a vertical or horizontal ellipsis indicates
an omission of information.

In syntax using brackets and braces, an ellipsis indicates items that
can be repeated. When an item followed by ellipses is enclosed in
brackets, zero or more items can be specified.

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

Chapter 1 About this document

7

On the 6100 Switch Series

• member: Always 1. VSF is not supported on this switch.

•

slot: Always 1. This is not a modular switch, so there are no slots.

• port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

8

AOS-CX 10.06 IP Services Guide

Chapter 2
IRDP

ICMP Router Discovery Protocol (IRDP), an extension of the ICMP, is independent of any routing protocol. It
allows hosts to discover the IP addresses of neighboring routers that can act as default gateways to reach
devices on other IP networks.

NOTE: On the switches covered by this guide, IRDP is configured on a VLAN interface.

IRDP operation

IRDP uses the following types of ICMP messages:

• Router advertisement (RA): Sent by a router to advertise IP addresses (including the primary and

secondary IP addresses) and preference.

• Router solicitation (RS): Sent by a host to request the IP addresses of routers on the subnet.

An interface with IRDP enabled periodically broadcasts or multicasts an RA message to advertise its IP
addresses. A receiving host adds the IP addresses to its routing table, and selects the IP address with the
highest preference as the default gateway.

When a host attached to the subnet starts up, the host multicasts an RS message to request immediate
advertisements. If the host does not receive any advertisements, it retransmits the RS several times. If the
host does not discover the IP addresses of neighboring routers because of network problems, the host can
still discover them from periodic RAs.

IRDP allows hosts to discover neighboring routers, but it does not suggest the best route to a destination. If
a host sends a packet to a router that is not the best next hop, the host will receive an ICMP redirect
message from the router.

IP address preference

Every IP address advertised in RAs has a preference value. A larger preference value represents a higher
preference. The IP address with the highest preference is selected as the default gateway address.

You can specify the preference for IP addresses to be advertised on a router interface.

An address with the minimum preference value (-2147483648) will not be used as a default gateway
address.

Lifetime of an IP address

An RA contains a lifetime field that specifies the lifetime of advertised IP addresses. If the host does not
receive a new RA for an IP address within the address lifetime, the host removes the route entry.

All the IP addresses advertised by an interface have the same lifetime.

Advertising interval

A router interface with IRDP enabled sends out RAs randomly between the minimum and maximum
advertising intervals. This mechanism prevents the local link from being overloaded by a large number of
RAs sent simultaneously from routers.

As a best practice, shorten the advertising interval on a link that suffers high packet loss rates

Chapter 2 IRDP

9

Destination address of RA

An RA uses either of the following destination IP addresses:

• Broadcast address 255.255.255.255.

• Multicast address 224.0.0.1, which identifies all hosts on the local link.

By default, the destination IP address of an RA is the multicast address. If all listening hosts in a local area
network support IP multicast, specify 224.0.0.1 as the destination IP address.

Proxy-advertised IP addresses

By default, an interface advertises its primary and secondary IP addresses. You can specify IP addresses of
other gateways for an interface to proxy-advertise.

VRF support

In IP-based computer networks, virtual routing and forwarding (VRF) is a technology that allows multiple
instances of a routing table to co-exist within the same router at the same time. Because the routing
instances are independent, the same or overlapping IP addresses can be used without conflicting with each
other.

IRDP is VRF aware. As the router advertisements and solicit processing occurs on the interface, packet is
through the interface and corresponding VRF.

VSX synchronization

IRDP supports VSX synchronization. For more information on using VSX, see the Virtual Switching Extension
(VSX) Guide for your switch and software version

Configuring IRDP

Prerequisites
A layer 3 interface.

Procedure

1. Enable IRDP on an interface with the command .

2. Set the maximum hold time with the command .

3. Set the maximum router advertisement interval with the command .

4. Set the minimum router advertisement interval with the command .

5. Set the IRDP preference level with the command .

6. Review IRDP configuration settings with the command .

Example

This example creates the following configuration:

• Enables IRDP on the layer 3 VLAN interface 2 with packet type set to broadcast.

• Sets the hold time to 5000 seconds.

• Sets the advertisement interval to 30 seconds.

10

AOS-CX 10.06 IP Services Guide

• Sets the minimum advertisement interval to 25 seconds.

• Sets the IRDP preference level to 25.

switch(config)# interface vlan 2
switch(config-if-vlan)# ip irdp broadcast
switch(config-if-vlan)# ip irdp holdtime 5000
switch(config-if-vlan)# ip irdp maxadvertinterval 30
switch(config-if-vlan)# ip irdp minadvertinterval 25
switch(config-if-vlan)# ip irdp preference 25

IRDP commands

diag-dump irdp basic

Syntax

diag-dump irdp basic

Description

Displays diagnostic information for IRDP.

Command context

Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# diag-dump irdp basic
=========================================================================
[Start] Feature irdp Time : Thu Jan  7 04:46:25 2021
=========================================================================
-------------------------------------------------------------------------
[Start] Daemon hpe-rdiscd
-------------------------------------------------------------------------
Interface: vlan2 (state : Down)
rdisc ipv4 (enabled: 1, max:600, min:450, hold:1800, pref:0, isBcast:0)
No advertisable IPv4 addresses on the interface
Interface: vlan1 (state : Down)
rdisc ipv4 (enabled: 0, max:600, min:450, hold:1800, pref:0, isBcast:0)
No advertisable IPv4 addresses on the interface

-------------------------------------------------------------------------
[End] Daemon hpe-rdiscd
-------------------------------------------------------------------------
=========================================================================
[End] Feature irdp
=========================================================================
Diagnostic-dump captured for feature irdp

Chapter 2 IRDP

11

ip irdp

Syntax

ip irdp [broadcast | multicast]

no ip irdp

Description

Enables IRDP on an interface and specifies the packet type that is used to send advertisements. By default,
the packet type is set to multicast. IRDP is only supported on layer 3 interfaces.

The no form of this command disables IRDP on an interface.

Command context

config-if

Parameters
broadcast

Advertisements are sent as broadcast packets to IP address 255.255.255.255.

multicast

Advertisements are sent as multicast packets to the multicast group with IP address 24.0.0.1. Default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling IRDP on interface vlan 2 with packet type set to the default value (multicast).

switch(config)# interface vlan 2
switch(config-if-vlan)# ip irdp

Enabling IRDP on interface vlan 2 with packet type set to broadcast.

switch(config)# interface vlan 2
switch(config-if-vlan)# ip irdp broadcast

Disabling IRDP.

switch(config)# interface vlan 2
switch(config-if-vlan)# no ip irdp

ip irdp holdtime

Syntax

ip irdp holdtime <TIME>

Description
Specifies the maximum amount of time the host will consider an advertisement to be valid until a newer
advertisement arrives. When a new advertisement arrives, hold time is reset. Hold time must be greater
than or equal to the maximum advertisement interval. Therefore, if the hold time for an advertisement
expires, the host can reasonably conclude that the router interface that sent the advertisement is no longer
available. The default hold time is three times the maximum advertisement interval.

12

AOS-CX 10.06 IP Services Guide

Command context

config-if

Parameters
<TIME>

Specifies the lifetime of router advertisements sent from this interface. Range: 4 to 9000 seconds.
Default: 1800 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Example

Setting the hold time for VLAN interface 2 to 5000 seconds:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip irdp holdtime 5000

ip irdp maxadvertinterval

Syntax

ip irdp maxadvertinterval <TIME>

Description
Specifies the maximum router advertisement interval.

Command context

config-if

Parameters
<TIME>

Specifies the maximum time allowed between the sending of unsolicited router advertisements. Range:
4 to 1800 seconds. Default: 600 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Example

Setting the advertisement interval for VLAN interface 2 to 30 seconds:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip irdp maxadvertinterval 30

ip irdp minadvertinterval

Syntax

ip irdp minadvertinterval <TIME>

Chapter 2 IRDP

13

Description

Specifies the minimum amount of time the switch waits between sending router advertisements. By default,
this value is automatically set by the switch to be 75% of the value configured for maximum router
advertisement interval. Use this command to override the automatically configured value.

Command context

config-if

Parameters
<TIME>

Specifies the minimum time allowed between the sending of unsolicited router advertisements. Range: 3
to 1800 seconds. Default: 450 seconds (75% of the default value for maximum router advertisement
interval).

Authority

Administrators or local user group members with execution rights for this command.

Example

Setting the minimum advertisement interval for VLAN interface 2 to 25 seconds:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip irdp minadvertinterval 25

ip irdp preference

Syntax

ip irdp preference <LEVEL>

Description

Specifies the IRDP preference level. If a host receives multiple router advertisement messages from different
routers, the host selects the router that sent the message with the highest preference as the default
gateway.

Command context

config-if

Parameters
<LEVEL>

Specifies the IRDP preference level. Range: -2147483648 to 2147483647. Default: 0.

Authority

Administrators or local user group members with execution rights for this command.

Example

Setting the IRDP preference level for VLAN interface 2 to 25.

switch(config)# interface vlan 2
switch(config-if-vlan)# ip irdp preference 25

14

AOS-CX 10.06 IP Services Guide

show ip irdp

Syntax

show ip irdp [vsx-peer]

Description

Displays IRDP configuration settings.

Command context

Manager (#)

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch# sh ip irdp

 ICMP Router Discovery Protocol

 Interface       Status   Advertising Minimum  Maximum  Holdtime Preference
                          Address     Interval Interval
 --------------- -------- ----------- -------- -------- -------- -----------
 vlan1           Disabled multicast   450      600      1800     0
 bridge_normal   Disabled multicast   450      600      1800     0

Chapter 2 IRDP

15

Chapter 3
IPv6 Router Advertisement

IPV6 RA provides a method for local IPV6 hosts to automatically configure their own IP address (and other
settings such as a preferred DNS server) based on information advertised by switches/routers operating on
the network.

IPv6 flags

Behavior of IPv6 hosts to IPv6 RA messages is controlled by the managed address configuration flag (M flag),
and other stateful configuration flag (O flag).

M flag O flag Description

0

0

1

1

0

1

0

1

Indicates that no information is available via DHCPv6.

Indicates that other configuration information is available via DHCPv6. Examples of such
information are DNS-related information or information on other servers within the
network.

Indicates that addresses are available via Dynamic Host Configuration Protocol (DHCPv6).

If the M flag is set, the O flag is redundant and can be ignored because DHCPv6 will return
all available configuration information.

Configuring IPv6 RA

Procedure

1. Enable transmission of IPv6 router advertisements with the command no ipv6 nd suppress-ra.

2. Optionally, configure IPv6 unicast address prefixes with the command ipv6 nd prefix.

3. Optionally, configure support for DNS name resolution with the commands ipv6 nd ra dns server

and ipv6 nd ra dns search-list.

4. For most deployments, the default values for the following features do not need to be changed. If your

deployment requires different settings, change the default values with the indicated command:

IPv6 RA setting

Default value

Command to change it

Number of neighbor
solicitations to be sent when
performing DAD.

1

ipv6 nd dad attempts

Number of neighbor entries
in the ND cache.

131072

ipv6 nd cache-limit

Hop limit to be sent in the RA
messages.

64

ipv6 nd hop-limit

MTU value to be sent in the
RA messages.

1500 bytes

ipv6 nd mtu

Neighbor solicitation interval

1000 milliseconds

ipv6 nd ns-interval

Table Continued

16

AOS-CX 10.06 IP Services Guide

IPv6 RA setting

Default value

Command to change it

Lifetime of a default router.

1800 seconds

ipv6 nd ra lifetime

Retrieval of an IPv6 address
by devices.

Maximum interval between
transmissions of IPv6 RAs.

Minimum interval between
transmissions of IPv6 RAs.

Time that an interface
considers a device to be
reachable.

Retry period between ND
solicitations.

Disabled

ipv6 nd ra managed-config-flag

600 seconds

ipv6 nd ra max-interval

200 seconds

ipv6 nd ra min-interval

0 milliseconds (no
limit)

0 (Use locally
configured NS-
interval)

ipv6 nd ra reachable-time

ipv6 nd ra retrans-timer

Default routing preference for
an interface.

Medium

ipv6 nd router-preference

5. Review IPv6 RA configuration settings with the commands show ipv6 nd interface, show ipv6 nd
interface prefix, show ipv6 nd ra dns server, and show ipv6 nd ra dns search-list.

Example

This example creates the following configuration:

• Enables IPV6 RA on interface interface vlan 2.

• Sets the recursive DNS server address to 4001::1 with a lifetime of 400 seconds.

• Sets the minimum interval between transmissions to 3 seconds.

• Sets the maximum interval between transmissions to 13 seconds.

• Sets the lifetime of a default router to 1900 seconds.

switch(config)# interface vlan 2
switch(config-if)# no ipv6 nd suppress-ra
switch(config-if)# ipv6 nd ra dns server 4001::1 lifetime 400
switch(config-if)# ipv6 nd ra min-interval 3
switch(config-if)# ipv6 nd ra max-interval 13
switch(config-if)# ipv6 nd ra lifetime 1900
switch(config-if)# end
switch# show ipv6 nd interface vlan 2
Interface vlan2 is up
  Admin state is up
  IPv6 address:
    2006::1/64 [VALID]
  IPv6 link-local address: fe80::98f2:b321:368:6dc6/64 [VALID]
  ICMPv6 active timers:
      Last Router-Advertisement sent: 0 Secs
      Next Router-Advertisement sent in: 13 Secs
  Router-Advertisement parameters:
      Periodic interval: 3 to 13 secs
      Router Preference: medium
      Send "Managed Address Configuration" flag: false
      Send "Other Stateful Configuration" flag: false

Chapter 3 IPv6 Router Advertisement

17

      Send "Current Hop Limit" field: 64
      Send "MTU" option value: 1500
      Send "Router Lifetime" field: 1900
      Send "Reachable Time" field: 0
      Send "Retrans Timer" field: 0
      Suppress RA: false
      Suppress MTU in RA: true
  ICMPv6 error message parameters:
      Send redirects: false
  ICMPv6 DAD parameters:
      Current DAD attempt: 1
switch# show ipv6 nd ra dns server
Recursive DNS Server List on: vlan2
     Suppress DNS Server List: No
     DNS Server 1: 2001::1    lifetime 400

IPv6 RA scenario
In this scenario, two host computers are auto-configured with IP addresses using IPv6 RA. In addition, the
switch provides the hosts with an address of a recursive DNS server.

Procedure

1. Configure the VLAN interfaces with IPv6 addresses.

switch# config
switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 address 2001::1/64
switch(config)# interface vlan 3
switch(config-if-vlan)# ipv6 address 3001::1/64
switch(config)# interface vlan 4
switch(config-if-vlan)# ipv6 address 4001::1/64

2. Enable transmission of all IPv6 RA messages.

switch(config-if-vlan)# no ipv6 nd suppress-ra

IPv6 RA commands

ipv6 address <global-unicast-address>

Syntax

ipv6 address <global-unicast-address>

no ipv6 address <global-unicast-address>

Description

Sets a global unicast address on the interface.

The no form of this command removes the global unicast address on the interface.

NOTE: This command automatically creates an IPv6 link-local address on the interface.
However, it does not add the command to the running configuration. If you remove the IPv6
address, the link-local address is also removed. To maintain the link-local address, you must
manually execute the command.

18

AOS-CX 10.06 IP Services Guide

Command context

config-if

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Enabling a global unicast address:

switch(config)# interface vlan 2
switch(config-if-vlan)#  ipv6 address 3731:54:65fe:2::a7

Disabling a global unicast address:

switch(config)# interface vlan 2
switch(config-if-vlan)#  no ipv6 address 3731:54:65fe:2::a7

ipv6 address autoconfig

Syntax

ipv6 address autoconfig

no ipv6 address autoconfig

Description

Enables the interface to automatically obtain an IPv6 address using router advertisement information and
the EUI-64 identifier.

The no form of this command disables address auto-configuration.

NOTE:

• A maximum of 15 autoconfigured addresses are supported.

• This command automatically creates an IPv6 link-local address on the interface. However, it

does not add the command to the running configuration. If you remove the IPv6 address, the
link-local address is also removed. To maintain the link-local address, you must manually
execute the command.

Command context

config-if

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

The IPv6 SLAAC feature lets the router obtain the IPv6 address for the interface it is configured through the
SLAAC method. This feature is not available on the mgmt VRF.

Example

Enabling unicast autoconfiguring:

Chapter 3 IPv6 Router Advertisement

19

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 address autoconfig

Disabling unicast autoconfiguring:

switch(config)# interface vlan 2
switch(config-if-vlan)# no ipv6 address autoconfig

ipv6 address link-local

Syntax

ipv6 address link-local [<IPV6-ADDR>/<MASK>]

Description

Enables IPv6 on the current interface. If no address is specified, an IPv6 link-local address is auto-generated
for the interface. If an address is specified, auto-configuration is disabled and the specified address/mask is
assigned to the interface.

To disable IPv6 link-local on the interface, remove ipv6 address link-local, ipv6 address <global-
ipv6-address>, and ipv6 address autoconfig from the interface.

NOTE: This feature is not available on the management VRF.

Command context

config-if

Parameters
<IPV6-ADDR>

Specifies the IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F. You can use two colons (::) to represent consecutive zeros (but only
once), remove leading zeros, and collapse a hextet of four zeros to a single 0. For example, this address
2222:0000:3333:0000:0000:0000:4444:0055 becomes 2222:0:3333::4444:55.

<MASK>

Specifies the number of bits in the address mask in CIDR format (x), where x is a decimal number from 0
to 128.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Enabling IPv6 link-local on the interface:

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 address link-local

20

AOS-CX 10.06 IP Services Guide

ipv6 nd cache-limit

Syntax

ipv6 nd cache-limit <CACHELIMIT>

no ipv6 nd cache-limit [<CACHELIMIT>]

Description

Configures the limit on the number of neighbor entries in the ND cache.

The no form of this command sets the cache limit to the default value.

Command context

config

Parameters
<CACHELIMIT>

Specifies the neighbor cache entries limit. Range: 1-131072. Default: 131072.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the cache limit to 20.

switch(config)# ipv6 nd cache-limit 20

ipv6 nd dad attempts

Syntax

ipv6 nd dad attempts <NUM-ATTEMPTS>

no ipv6 nd dad attempts [<NUM-ATTEMPTS>]

Description

Configures the number of neighbor solicitations to be sent when performing duplicate address detection
(DAD) for a unicast address configured on an interface.

The no form of this command sets the number of attempts to the default value.

Command context

config-if

Parameters
dad attempts <NUM-ATTEMPTS>

Specifies the number of neighbor solicitations to send. Range: 0-15. Default: 1.

Authority

Administrators or local user group members with execution rights for this command.

Chapter 3 IPv6 Router Advertisement

21

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd dad attempts 5

ipv6 nd hop-limit

Syntax

ipv6 nd hop-limit <HOPLIMIT>

no ipv6 nd hop-limit [<HOPLIMIT>]

Description

Configures the hop limit to be sent in RAs.

The no form of this command resets the hop limit to 0. This reset eliminates the hop limit from the RAs that
originate on the interface, so the host determines the hop limit.

Command context

config-if

Parameters
hop-limit <HOPLIMIT>

Specifies the hop limit. Range: 0-255. Default: 64.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd hop-limit 64

ipv6 nd mtu

Syntax

ipv6 nd mtu <MTU-VALUE>

no ipv6 nd mtu [<MTU-VALUE>]

Description

Configures the MTU size to be sent in the RA messages.

The no form of this command sets hop limit to the default value.

Command context

config-if

Parameters
<MTU-VALUE>

Specifies the MTU size. Range: 1280-65535 bytes. Default: 1500 bytes.

22

AOS-CX 10.06 IP Services Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd mtu 1300

ipv6 nd ns-interval

Syntax

ipv6 nd ns-interval <TIME>

no ipv6 nd ns-interval [<TIME>]

Description

Configures the ND time between DAD neighbor solicitations sent for an unresolved destination, or between
duplicate address detection neighbor solicitation requests. Increase this setting when neighbor solicitation
retries or failures are occurring, or in a slow (WAN) network.

The no form of this command sets the ns-interval to the default value.

Command context

config-if

Parameters
<TIME>

Specifies the neighbor solicitation interval. Range: 1000-3600000 milliseconds. Default: 1000
milliseconds.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd ns-interval 1200

ipv6 nd prefix

Syntax

ipv6 nd prefix <IPV6-ADDR>/<PREFIX-LEN>
     [no-advertise | [valid <LIFETIME-VALUE> preferred
     <LIFETIME-VALUE>] | no-autoconfig | no-onlink]

no ipv6 nd prefix <IPV6-ADDR>/<PREFIX-LEN> [no-advertise
     | [valid <LIFETIME-VALUE> preferred <LIFETIME-VALUE>
     ] | no-autoconfig | no-onlink]

ipv6 nd prefix default [no-advertise | [valid <LIFETIME-VALUE>
     preferred <LIFETIME-VALUE>] | no-autoconfig | no-onlink]}

Chapter 3 IPv6 Router Advertisement

23

no ipv6 nd prefix default [no-advertise | [valid <LIFETIME-VALUE>
     preferred <LIFETIME-VALUE>] | no-autoconfig | no-onlink]}

Description

Specifies prefixes for the routing switch to include in RAs transmitted on the interface. IPv6 hosts use the
prefixes in RAs to autoconfigure themselves with global unicast addresses. The autoconfigured address of a
host is composed of the advertised prefix and the interface identifier in the current link-local address of the
host.

By default, advertise, autoconfig, and onlink are set.

The no form of this command removes the configuration on the interface.

Command context

config-if

Parameters
<IPV6-ADDR>/<PREFIX-LEN>

Specifies the IPv6 prefix to advertise in RA. Format: X:X::X:X/M

default

Specifies apply configuration to all on-link prefixes that are not individually set by the ipv6 ra prefix
<IPV6-ADDR>/<PREFIX-LEN> command. It applies the same valid and preferred lifetimes, link state,
autoconfiguration state, and advertise options to the advertisements sent for all on-link prefixes that are
not individually configured with a unique lifetime. This also applies to the prefixes for any global unicast
addresses configured later on the same interface.

Using default once, and then using it again with any new parameter values results in the new values
replacing the former values in advertisements. If default is used without the no–advertise, no–
autoconfig, or no-onlink parameter, the advertisement setting for the absent parameter is returned
to its default setting.

no-advertise

Specifies do not advertise prefix in RA.

valid <LIFETIME-VALUE>

Specifies the total time, in seconds, the prefix remains available before becoming unusable. After
preferred-lifetime expiration, any autoconfigured address is deprecated and used only for transactions
only before preferred-lifetime expires. If the valid lifetime expires, the address becomes invalid.

You can enter a value in seconds or enter valid infinite which sets infinite lifetime. Default:
2,592,000 seconds which is 30 days. Range: 0–4294967294 seconds.

preferred <LIFETIME-VALUE>

Specifies the span of time during which the address can be freely used as a source and destination for
traffic. This setting must be less than or equal to the corresponding valid–lifetime setting.

You can enter a value in seconds or enter preferred infinite which sets infinite lifetime. Default:
604,800 seconds which is seven days. Range: 0–4294967294 seconds.

no-autoconfig

Specifies do not use prefix for autoconfiguration.

no-onlink

Specifies do not use prefix for onlink determination.

24

AOS-CX 10.06 IP Services Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd prefix 4001::1/64 valid 30 preferred 10 no-autoconfig no-onlink

ipv6 nd ra dns search-list

Syntax

ipv6 nd ra dns search-list <DOMAIN-NAME>  [lifetime <TIME>]

no ipv6 nd ra dns search-list <DOMAIN-NAME>

Description

Configures the DNS Search List (DNSSL) to include in Router Advertisements (RAs) transmitted on the
interface.

The no form of this command removes the DNS Search List from the RAs transmitted on the interface.

Command context

config-if

Parameters
<DOMAIN-NAME>

Specifies the domain names for DNS queries.

lifetime <TIME>

Specifies lifetime in seconds. Range: 4-4294967295 seconds. Default: 1800 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

• DNSSL contains the domain names of DNS suffixes or IPv6 hosts to append to short, unqualified domain

names for DNS queries.

• Multiple DNS domain names can be added to the DNSSL by using the command repeatedly.

• A maximum of eight server addresses are allowed.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd ra dns search-list test.com lifetime 500

ipv6 nd ra dns server

Syntax

ipv6 nd ra dns server <IPV6-ADDR>  [lifetime <TIME>]

no ipv6 nd ra dns server <IPV6-ADDR>

Chapter 3 IPv6 Router Advertisement

25

Description

Configures the IPv6 address of a preferred Recursive DNS Server (RDNSS) to be included in Router
Advertisements (RAs) transmitted on the interface.

The no form of this command removes the configured DNS server from the RAs transmitted on the
interface.

Command context

config-if

Parameters
<IPV6-ADDR>

Specifies the RDNSS address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x
is a hexadecimal number from 0 to F. You can use two colons (::) to represent consecutive zeros (but only
once), remove leading zeros, and collapse a hextet of four zeros to a single 0. For example, this address
2222:0000:3333:0000:0000:0000:4444:0055 becomes 2222:0:3333::4444:55.

lifetime <TIME>

Specifies IPv6 DNS server lifetime in seconds. Range: 4-4294967295 seconds. Default: 1800 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

•

Including RDNSS information in RAs provides DNS server configuration for connected IPv6 hosts without
requiring DHCPv6.

• Multiple servers can be configured on the interface by using the command repeatedly.

• A maximum of eight server addresses are allowed.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd ra dns server 2001::1 lifetime 400

ipv6 nd ra lifetime

Syntax

ipv6 nd ra lifetime <TIME>

no ipv6 nd ra lifetime [<TIME>]

Description

Configures the lifetime, in seconds, for the routing switch to be used as a default router by hosts on the
current interface.

The no form of this command sets lifetime to the default of 1800 seconds.

Command context

config-if

26

AOS-CX 10.06 IP Services Guide

Parameters
<TIME>

Specifies lifetime in seconds of a default router. A setting of 0 for default router lifetime in an RA
indicates that the routing switch is not a default router on the interface. Range: 0-9000 seconds. Default:
1800 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

• A given host on an interface refreshes the default router lifetime for a specific router each time the host

receives an RA from that router.

• A specific router ceases to be a default router candidate for a given host if the default router lifetime

expires before the host is updated with a new RA from the router.

Examples

switch(config)# intervace vlan 2
switch(config-if-vlan)# ipv6 nd ra lifetime 1200

ipv6 nd ra managed-config-flag

Syntax

ipv6 nd ra managed-config-flag

no ipv6 nd ra managed-config-flag

Description

Controls the M flag setting in RAs the router transmits on the current interface. Enable the M flag to indicate
that hosts can obtain IP address through DHCPv6. The M flag is disabled by default.

The no form of this command turns off (disables) the M flag.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Usage

• Enabling the M flag directs hosts to acquire their IPv6 addressing for the current interface from a DHCPv6

server.

• When the M-bit is enabled, receiving hosts ignore the O flag setting, which is configured using the

command ipv6 nd ra other-config-flag.

• When the M-bit is disabled (the default), receiving hosts expect to receive their IPv6 addresses from RA.

Chapter 3 IPv6 Router Advertisement

27

M flag O flag Description

Indicates that no information is available via DHCPv6.

Indicates that other configuration information is available via DHCPv6. Examples of
such information are DNS-related information or information on other servers within
the network.

Indicates that addresses are available via Dynamic Host Configuration Protocol
(DHCPv6).

If the M flag is set, the O flag is redundant and can be ignored because DHCPv6 will
return all available configuration information.

0

0

1

1

0

1

0

1

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd ra managed-config-flag

ipv6 nd ra max-interval

Syntax

ipv6 nd ra max-interval <TIME>

no ipv6 nd ra max-interval [<TIME>]

Description

Configures the maximum interval between transmissions of IPv6 RAs on the interface. The interval between
RA transmissions on an interface is a random value that changes every time an RA is sent. The interval is
calculated to be a value between the current max-interval and min-interval settings.

The no form of this command returns the setting to its default, provided the default value is less than the
default lifetime value.

Command context

config-if

Parameters
<TIME>

Specifies the maximum advertisement time in seconds. Range: 4-1800. Default: 600 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

• This value has one setting per interface. The setting does not apply to RAs sent in response to a router

solicitation received from another device.

• Attempting to set max-interval to a value that is not sufficiently larger than the current min-interval also

results in an error message.

28

AOS-CX 10.06 IP Services Guide

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd ra max-interval 30

ipv6 nd ra min-interval

Syntax

ipv6 nd ra min-interval <TIME>

no ipv6 nd ra min-interval [<TIME>]

Description

Configures the minimum interval between transmissions of IPv6 RAs on the interface. The interval between
RA transmissions on an interface is a random value that changes every time an RA is sent. The interval is
calculated to be a value between the current max-interval and min-interval settings.

The no form of this command returns the setting to its default, provided the default value is less than the
current max-interval setting.

Command context

config-if

Parameters
<TIME>

Specifies a minimum advertisement time in seconds. Range: 3-1350. Default: 200 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

• This value has one setting per interface and does not apply to RAs sent in response to a router

solicitation received from another device.

• The min-interval must be less than the max-interval. Attempting to set min-interval to a higher value

results in an error message.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd ra  min-interval 25

ipv6 nd ra other-config-flag

Syntax

ipv6 nd ra other-config-flag

no ipv6 nd ra other-config-flag

Chapter 3 IPv6 Router Advertisement

29

Description

Controls the O-bit in RAs the router transmits on the current interface; but is ignored unless the M-bit is
disabled in RAs. Configure to set the O-bit in RA messages for host to obtain network parameters through
DHCPv6. The other-config-flag is disabled by default.

For more information on configuring the M-bit, see ipv6 nd ra managed-config-flag.

The no form of this command turns off (disables) the setting for this command in RAs.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Usage

Enabling the O-bit while the M-bit is disabled directs hosts on the interface to acquire their other
configuration information from DHCPv6. Examples of such information are DNS-related information or
information on other servers within the network.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd ra other-config-flag

ipv6 nd ra reachable-time

Syntax

ipv6 nd ra reachable-time <TIME>

no ipv6 nd ra reachable-time [<TIME>]

Description

Sets the amount of time that the interface considers a device to be reachable after receiving a reachability
confirmation from the device.

The no form of this command sets the reachable time to the default value of 0. (no limit).

Command context

config-if

Parameters
<TIME>

Specifies the reachable time in milliseconds. Range: 1000-3600000. Default: 0 (no limit).

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd ra reachable-time 2000

30

AOS-CX 10.06 IP Services Guide

ipv6 nd ra retrans-timer

Syntax

ipv6 nd ra retrans-timer <TIME>

no ipv6 nd ra retrans-timer [<TIME>]

Description

Configures the period (retransmit timer) between ND solicitations sent by a host for an unresolved
destination, or between DAD neighbor solicitation requests. By default, hosts on the interface use their own
locally configured NS-interval settings instead of using the value received in the RAs.

Increase this timer when neighbor solicitation retries or failures are occur, or in a "slow" (WAN) network.

The no form of this command sets the value to the default of 0.

Command context

config-if

Parameters
<TIME>

Specifies the retransmit timer value in milliseconds. Range: 0 - 4294967295 milliseconds. Default: 0 (Use
locally configured NS-interval).

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd ra retrans-timer 400

ipv6 nd router-preference

Syntax

ipv6 nd router-preference {high | medium | low}

no ipv6 nd router-preference [high | medium | low]

Description

Specifies the value that is set in the Default Router Preference (DRP) field of Router Advertisements (RAs)
that the switch sends from an interface. An interface with a DRP value of high will be preferred by other
devices on the network over interfaces with an RA value of medium or low.

The no form of this command set the value to the default of medium.

Command context

config-if

Chapter 3 IPv6 Router Advertisement

31

Parameters
high

Sets DRP to high.

medium

Sets DRP to medium. Default.

low

Sets DRP to low.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd router-preference high

ipv6 nd suppress-ra

Syntax

ipv6 nd suppress-ra [<SUPPRESS-OPTION>]

no ipv6 nd ra supress-ra [<SUPPRESS-OPTION>]

Description

Configures suppression of IPv6 Router Advertisement transmissions on an interface.

The no form of this command restores transmission of IPv6 Router Advertisement and options.

Command context

config-if

Parameters
suppress-ra [<SUPPRESS-OPTION>]

Specifies suppressing RA transmissions. Entering suppress-ra without any options, suppresses all RA
messages (default). Or you can enter one of the following options.

dnssl

Specifies suppressing DNSSL options in RA messages.

mtu

Specifies suppressing MTU options in RA messages.

rdnss

Specifies suppressing RDNSS options in RA messages.

Authority

Administrators or local user group members with execution rights for this command.

32

AOS-CX 10.06 IP Services Guide

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd suppress-ra mtu dnssl rdnss
switch(config-if-vlan)# no ipv6 nd suppress-ra mtu dnssl rdnss

show ipv6 nd global traffic

Syntax

show ipv6 nd global traffic [vsx-peer]

Description

Displays IPV6 Neighbor Discovery traffic details on a device.

Command context

Operator (>) or Manager (#)

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch# show ipv6 nd global traffic
  ICMPv6 packet Statistics (sent/received)
    Total Messages               :        18/0
    Error Messages               :        0/0
    Destination Unreachables     :        0/0
    Time Exceeded                :        0/0
    Parameter Problems           :        0/0
    Echo Request                 :        0/0
    Echo Replies                 :        0/0
    Redirects                    :        0/0
    Packet Too Big               :        0/0
    Router Advertisements        :        4/0
    Router Solicitations         :        0/0
    Neighbor Advertisements      :        0/0
    Neighbor Solicitations       :        3/0
    Duplicate router RA received :        0/0
  ICMPv6 MLD Statistics (sent/received)
    V1 Queries :          0/0
    V2 Queries :          0/0
    V1 Reports :          0/0
    V2 Reports :          11/0
    V1 Leaves  :          0/0

Chapter 3 IPv6 Router Advertisement

33

show ipv6 nd interface

Syntax

show ipv6 nd interface [<IF-NAME> | all-vrfs | vrf <VRF-NAME>]
     [vsx-peer]

Description

Displays neighbor discovery information for an interface. If no options are specified, displays information for
the default VRF.

Command context

Operator (>) or Manager (#)

Parameters
<IF-NAME>

Displays information about the specified IPv6 enabled interface.

all-vrfs

Displays information about interfaces in all VRFs.

vrf <VRF-NAME>

Displays information about interfaces in a particular VRF. Or, if <VRF-NAME> is not specified, information
for the default VRF is displayed.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing information for all VRFs:

switch# show ipv6 nd interface all-vrfs

List of IPv6 Interfaces for VRF default
Interface vlan2 is up
  Admin state is up
  IPv6 address:
  IPv6 link-local address: fe80::7272:cfff:fee7:a8b9/64 [VALID]
  ICMPv6 active timers:
      Last Router-Advertisement sent:
      Next Router-Advertisement sent in:
  Router-Advertisement parameters:
      Periodic interval: 200 to 600 secs
      Router Preference: medium
      Send "Managed Address Configuration" flag: false
      Send "Other Stateful Configuration" flag: false
      Send "Current Hop Limit" field: 64
      Send "MTU" option value: 1500
      Send "Router Lifetime" field: 1800
      Send "Reachable Time" field: 0

34

AOS-CX 10.06 IP Services Guide

      Send "Retrans Timer" field: 0
      Suppress RA: true
      Suppress MTU in RA: true
  ICMPv6 error message parameters:
      Send redirects: false
  ICMPv6 DAD parameters:
      Current DAD attempt: 1

List of IPv6 Interfaces for VRF red
Interface vlan3 is up
  Admin state is up
  IPv6 address:
    2001::1/64 [VALID]
  IPv6 link-local address: fe80::7272:cfff:fee7:a8b9/64 [VALID]
  ICMPv6 active timers:
      Last Router-Advertisement sent:
      Next Router-Advertisement sent in:
  Router-Advertisement parameters:
      Periodic interval: 200 to 600 secs
      Router Preference: medium
      Send "Managed Address Configuration" flag: false
      Send "Other Stateful Configuration" flag: false
      Send "Current Hop Limit" field: 64
      Send "MTU" option value: 1500
      Send "Router Lifetime" field: 1800
      Send "Reachable Time" field: 0
      Send "Retrans Timer" field: 0
      Suppress RA: true
      Suppress MTU in RA: true
  ICMPv6 error message parameters:
      Send redirects: false
  ICMPv6 DAD parameters:
      Current DAD attempt: 1

Showing information for interface vlan 2:

switch# show ipv6 nd interface vlan 2
Interface vlan2 is up
  Admin state is up
  IPv6 address:
  IPv6 link-local address: fe80::7272:cfff:fee7:a8b9/64 [VALID]
  ICMPv6 active timers:
      Last Router-Advertisement sent:
      Next Router-Advertisement sent in:
  Router-Advertisement parameters:
      Periodic interval: 200 to 600 secs
      Router Preference: high
      Send "Managed Address Configuration" flag: false
      Send "Other Stateful Configuration" flag: false
      Send "Current Hop Limit" field: 64
      Send "MTU" option value: 1500
      Send "Router Lifetime" field: 1800
      Send "Reachable Time" field: 0
      Send "Retrans Timer" field: 0
      Suppress RA: true
      Suppress MTU in RA: true
  ICMPv6 error message parameters:
      Send redirects: false
  ICMPv6 DAD parameters:
      Current DAD attempt: 1

Showing information for the default VRF:

Chapter 3 IPv6 Router Advertisement

35

switch# show ipv6 nd interface

List of IPv6 Interfaces for VRF default
Interface vlan2 is up
  Admin state is up
  IPv6 address:
      2001::1/64  [VALID]
  IPv6 link-local address: fe80::7272:cfff:fee7:a8b9/64 [VALID]
  ICMPv6 active timers:
      Last Router-Advertisement sent: 6 Secs
      Next Router-Advertisement sent in: 7 Secs
  Router-Advertisement parameters:
      Periodic interval: 3 to 13 secs
      Router Preference: medium
      Send "Managed Address Configuration" flag: false
      Send "Other Stateful Configuration" flag: false
      Send "Current Hop Limit" field: 64
      Send "MTU" option value: 1500
      Send "Router Lifetime" field: 1900
      Send "Reachable Time" field: 0
      Send "Retrans Timer" field: 0
      Suppress RA: true
      Suppress MTU in RA: true
  ICMPv6 error message parameters:
      Send redirects: false
  ICMPv6 DAD parameters:
      Current DAD attempt: 1

show ipv6 nd interface prefix

Syntax

show ipv6 nd interface prefix [all-vrfs | vrf <VRF-NAME>] [vsx-peer]

Description

Shows IPv6 prefix information for all VRFs or a specific VRF. If no options are specified, shows information
for the default VRF.

Command context

Operator (>) or Manager (#)

Parameters
all-vrfs

Shows prefix information for all VRFs.

vrf <VRF-NAME>

Name of a VRF.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

36

AOS-CX 10.06 IP Services Guide

Examples

Showing prefix information for the default VRF:

switch# show ipv6 nd interface prefix

List of IPv6 Interfaces for VRF default
List of IPv6 Prefix advertised on vlan2
   Prefix : 4545::/65
   Enabled : Yes
   Validlife time : 2592000
   Preferred lifetime : 604800
   On-link : Yes
   Autonomous : Yes

Showing information for VRF red:

switch# show ipv6 nd interface prefix vrf red

List of IPv6 Interfaces for VRF red
List of IPv6 Prefix advertised on vlan3
   Prefix : 2001::/64
   Enabled : Yes
   Validlife time : 2592000
   Preferred lifetime : 604800
   On-link : Yes
   Autonomous : Yes

show ipv6 nd ra dns search-list

Syntax

show ipv6 nd ra dns search-list [vsx-peer]

Description

Displays domain name information on all interfaces.

Command context

Operator (>) or Manager (#)

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd ra dns search-list test.com
switch# show ipv6 nd ra dns search-list
Recursive DNS Search List on: 1

Chapter 3 IPv6 Router Advertisement

37

     Suppress DNS Search List: Yes
     DNS Search 1: test.com    lifetime  1800

show ipv6 nd ra dns server

Syntax

show ipv6 nd ra dns server [vsx-peer]

Description

Displays DNS server information on all interfaces.

Command context

Operator (>) or Manager (#)

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 nd ra dns server 2001::1
switch# show ipv6 nd ra dns server
Recursive DNS Server List on: 1
     Suppress DNS Server List: Yes
     DNS Server 1: 2001::1    lifetime 1800

38

AOS-CX 10.06 IP Services Guide

Chapter 4
sFlow

sFlow is a technology for monitoring traffic in switched or routed networks. The sFlow monitoring system is
comprised of:

• An sFlow Agent that runs on a network device, such as a switch. The agent uses sampling techniques to

capture information about the data traffic flowing through the device and forwards this information to an
sFlow collector.

• An sFlow Collector that receives monitoring information from sFlow agents. The collector stores this

information so that a network administrator can analyze it to understand network data flow patterns.
One sFlow collector can recieve the data from many sFlow agents.

NOTE: The sFlow UDP datagrams sent to a collector are not encrypted, therefore any sensitive
information contained in an sFlow sample is exposed.

sFlow agent
The sFlow agent on the switch provides ingress sampling of all forwarded layer 2 and layer 3 traffic on LAG
and Ethernet ports. High-availability is supported (packet sampling continues to work after switch-over).

The sFlow agent can communicate with up to three sFlow collectors at the same time. The agent
communicates with collectors only on the default VRF.

Although you can configure very high sampling rates, the switch may drop samples if it cannot handle the
rate of sampled packets. High sampling rates may also cause high CPU usage resulting in control plane
performance issues.

A single sFlow datagram sent to a collector contains multiple flow and counter samples. The total number of
samples an sFlow datagram can contain varies depending on the settings for header size and maximum
datagram size.

Default settings

•

sFlow is disabled on all interfaces.

• Collector port: UDP port 6343.

• Sampling rate: 4096.

• Polling interval: 30 seconds.

• Header size: 128 bytes.

• Max datagram size: 1400 bytes.

Supported features

• Global sampling rate

•

Interface counters polling

• Agent IP configuration for IPv4 and IPv6

• Header size configuration

Chapter 4 sFlow

39

• Max datagram size configuration

•

Ingress sampling for all forwarded traffic (L2, L3)

• Enable/Disable sFlow per interface

• Support for three remote collectors

• An out-of-band collector can be defined on the management VRF

• A collector can be defined on the non-default VRF

• Sampling on Ethernet and LAG interfaces

• High availability support (sampling continues to work after switch-over)

• Source IP support (setting source IP for sFlow datagrams sent to a remote collector)

Limitations

• No sampling of egress traffic

• Sampling rate cannot be set per interface (global only)

•

sFlow is not configurable via SNMP

Configuring the sFlow agent

Procedure

1. Configure one or more sFlow collectors with the command sflow collector. This determines where

the sFlow agent sends sFlow information.

2. Enable the sFlow agent on all interfaces, or on a specific interface, with the command sflow.

3. Define the address of the sFlow agent with the command sflow agent-ip.

4. By default, the source IP address for sFlow datagrams is set to the IP address of the outgoing switch

interface on which the sFlow client is communicating with a collector. Since the switch can have multiple
routing interfaces, datagrams can potentially be sent on different paths at different times, resulting in
different source IP addresses for the same client. To resolve this issue, define a single source IP address.
For details, see Single source IP address in the Fundamentals Guide.

5. For most deployments, the default values for the following settings do not need to be changed. If your

deployment requires different settings, change the default values with the indicated commands:

sFlow setting

Default value

Command to change it

Rate at which packets are sampled.

Rate at which the switch sends data to an
sFlow collector.

1 in every 4096
packets

sflow sampling

30 seconds

sflow polling

Size of the sFlow header.

128 bytes

sflow header-size

Maximum size of an sFlow datagram.

1400 bytes

sflow max-datagram-size

6. Review sFlow configuration settings with the command show sflow.

40

AOS-CX 10.06 IP Services Guide

Example

This example creates the following configuration:

• Configures an sFlow collector with the IP address 10.10.20.209 .

• Enables the sFlow agent on all interfaces.

• Defines the sFlow agent IP address to be 10.10.1.5.

switch(config)# sflow collector 10.10.20.209
switch(config)# sflow
switch(config)# sflow agent-ip 10.0.0.1

sFlow scenario
In this scenario, two hosts send sFlow traffic through a switch to an sFlow collector.

Procedure

1. Enable sFlow globally.

switch# config
switch(config)# sflow

2. Set the sFlow agent IP address to 10.10.12.1.

switch(config)# sflow agent-ip 10.10.12.1

3. Set the sFlow collector IP address to 10.10.12.2.

switch(config)# sflow collector 18.2.2.2

4. Configure sFLow sampling rate and polling interval.

switch(config)# sflow sampling 5000
switch(config)# sflow polling 20

5. Configure interface vlan 2 with IP address 10.10.10.1/24.

switch(config)# interface vlan 2
switch(config-if-vlan)# no shutdown
switch(config-if-vlan)# ip address 10.10.10.1/24
switch(config)# quit

6. Configure interface vlan 3 with IP address 10.10.11.1/24.

switch(config)# interface vlan 3
switch(config-if-vlan)# no shutdown
switch(config-if-vlan)# ip address 10.10.11.1/24
switch(config)# quit

7. Configure interface vlan 4 with IP address 10.10.12.1/24.

switch(config)# interface vlan 4
switch(config-if-vlan)# no shutdown

Chapter 4 sFlow

41

switch(config-if-vlan)# ip address 10.10.12.1/24
switch(config)# quit

8. Verify sFlow configuration.

switch# show sflow

sFlow Global Configuration
-----------------------------------------
sFlow                         enabled
Collector IP/Port/Vrf         10.10.12.2/6343/default
Agent Address                 10.10.12.1
Sampling Rate                 5000
Polling Interval              20
Header Size                   128
Max Datagram Size             1400

sFlow Status
-----------------------------------------
Running - Yes

sFlow Statistics
-----------------------------------------
Number of Samples             25

sFlow scenario 2
In this scenario, two hosts connected to different switches send sFlow traffic to a collector. A LAG is used to
connect the two switches.

Procedure

1. Configure switch 1.

a. Enable sFlow globally.

switch# config
switch(config)# sflow

b. Set the sFlow agent IP address to 10.10.12.1.

switch(config)# sflow agent-ip 10.10.12.1

c. Set the sFlow collector IP address to 10.10.12.2.

switch(config)# sflow collector 10.10.12.2

d. Configure sFLow sampling rate and polling interval.

switch(config)# sflow sampling 5000
switch(config)# sflow polling 10

e. Create VLAN 8.

switch(config)# vlan 8
switch(config-vlan-8)# no shutdown
switch(config)# exit

42

AOS-CX 10.06 IP Services Guide

f. Define LAG 100 and assign VLAN vlan 8 to it.

switch(config)# interface lag 100
switch(config-lag-if)# no shutdown
switch(config-lag-if)# vlan access 8
switch(config-lag-if)# lacp mode active

g. Configure interface 1/1/1.

switch(config)# interface 1/1/1
switch(config-if-vlan)# no shutdown
switch(config-lag-if)# no routing
switch(config-if-vlan)# vlan access 8

h. Configure interface 1/1/2 and 1/1/3 as members of LAG 100.

switch# (config)#interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# lag 100
switch(config-if)# exit
switch(config-if-vlan)# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# lag 100
switch(config-if)# exit

i. Configure interface vlan 5 with IP address 10.10.12.1/24.

switch# (config)#interface vlan 5
switch(config-if-vlan)# no shutdown
switch(config-if-vlan)# ip address 10.10.12.1/24
switch(config-if-vlan)# quit

j. Verify sFlow configuration.

switch# show sflow

sFlow Global Configuration
-----------------------------------------
sFlow                         enabled
Collector IP/Port/Vrf         10.10.12.2/6343/default
Agent Address                 10.10.12.1
Sampling Rate                 5000
Polling Interval              10
Header Size                   128
Max Datagram Size             1400

sFlow Status
-----------------------------------------
Running - Yes

sFlow Statistics
-----------------------------------------
Number of Samples             120

2. Configure switch 2.

Chapter 4 sFlow

43

a. Create VLAN 8.

switch(config)# vlan 8
switch(config-vlan-8)# no shutdown
switch(config)# exit

b. Define LAG 100 and assign VLAN vlan 8 to it.

switch(config)# interface lag 100
switch(config-lag-if)# no shutdown
switch(config-lag-if)# vlan access 8
switch(config-lag-if)# lacp mode active

c. Configure interface 1/1/1.

switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# vlan access 8

d. Configure interface 1/1/2 and 1/1/3 as members of LAG 100.

switch# (config)#interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# lag 100
switch(config-if)# exit
switch(config)-if# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# lag 100
switch(config-if)# exit

sFlow agent commands

sflow

Syntax

sflow

no sflow

Description

Enables the sFlow agent.

•

•

In the config context, this command enables the sFlow agent globally on all interfaces.

In an config-if context, this command enables the sFlow agent on a specific interface. sFlow cannot be
enabled on a member of a LAG, only on the LAG.

The sFlow agent is disabled by default.

The no form of this command disables the sFlow agent and deletes all sFlow configuration settings, either
globally, or for a specific interface.

Command context

config

44

AOS-CX 10.06 IP Services Guide

config-if

Parameters
None.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling sFlow globally on all interfaces:

switch(config)# sflow

Disabling sFlow globally on all interfaces:

switch(config)# no sflow

Enabling sFlow on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# sflow

Disabling sFlow on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no sflow

Enabling sFlow on interface lag100:

switch(config)# interface lag100
switch(config-if)# sflow

Disabling sFlow on interface lag100:

switch(config)# interface lag100
switch(config-if)# no sflow

sflow agent-ip

Syntax

sflow agent-ip <IP-ADDR>

no sflow agent-ip [<IP-ADDR>]

Description

Defines the IP address of the sFlow agent to use in sFlow datagrams. This address must be defined for sFlow
to function. HPE recommends that the address:

•

•

can uniquely identify the switch

is reachable by the sFlow collector

• does not change with time

The no form of this command deletes the IP address of the sFlow agent. This causes sFlow to stop working
and no datagrams will be sent to the sFlow collector.

Chapter 4 sFlow

45

Command context

config

Parameters
<IP-ADDR>

Specifies an IP address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255, or IPv6
format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a hexadecimal number from 0 to
F. The agent address is used to identify the switch in all sFlow datagrams sent to sFlow collectors. It is
usually set to an IP address on the switch that is reachable from an sFlow collector.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the agent address to 10.10.10.100:

switch(config)# sflow agent-ip 10.0.0.100

Setting the agent address to 2001:0db8:85a3:0000:0000:8a2e:0370:7334:

switch(config)# sflow agent-ip 2001:0db8:85a3:0000:0000:8a2e:0370:7334

Removing the address configuration from the switch, which results in sFlow being disabled:

switch(config)# no sflow agent-ip

sflow collector

Syntax

sflow collector <IP-ADDR> [port <PORT>] [vrf <VRF>]

no sflow collector <IP-ADDR> [port <PORT>] [vrf <VRF>]

Description

Defines a collector to which the sFlow agent sends data. Up to three collectors can be defined. At least one
collector should be defined, and it must be reachable from the switch for sFlow to work.

Command context

config

Parameters
collector <IP-ADDR>

Specifies the IP address of a collector in IPv4 format (x.x.x.x), where x is a decimal number from 0 to
255, or IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a hexadecimal
number from 0 to F.

port <PORT>

Specifies the UDP port on which to send information to the sFlow collector. Range: 0 to 65536. Default:
6343.
vrf <VRF>

Specifies the VRF on which to send information to the sFlow collector. The VRF must be defined on the
switch. If no VRF is specified, the default VRF (default) is used.

46

AOS-CX 10.06 IP Services Guide

Authority

Administrators or local user group members with execution rights for this command.

Example

Defining a collector with IP address 10.10.10.100 on UDP port 6400:

switch(config)# sflow collector 10.0.0.1 port 6400

sflow disable

Syntax

sflow disable

Description

Disables the sFlow agent, but retains any existing sFlow configuration settings. The settings become active if
the sFlow agent is re-enabled.

Command context

config

Parameters
None.

Authority

Administrators or local user group members with execution rights for this command.

Example

Disabling sFlow support:

switch(config)# sflow disable

sflow header-size

Syntax

sflow header-size <SIZE>

no sflow header-size [<SIZE>]

Description

Sets the sFlow header size in bytes.

The no form of this command sets the header size to the default value of 128.

Command context

config

Parameters
header-size <SIZE>

Specifies the sFlow header size in bytes. Range: 64 to 256. Default: 128.

Chapter 4 sFlow

47

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the header size to 64 bytes:

switch(config)# sflow header-size 64

Setting the header size to the default value of 128 bytes:

switch(config)# no sflow header-size

sflow max-datagram-size

Syntax

sflow max-datagram-size <SIZE>

no sflow max-datagram-size [<SIZE>]

Description

Sets the maximum number of bytes that are sent in one sFlow datagram.

The no form of this command sets maximum number of bytes to the default value of 1400.

Command context

config

Parameters
max-datagram-size <SIZE>

Specifies the maximum datagram size in bytes. Range: 1 to 9000. Default: 1400.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the datagram size to 1000 bytes:

switch(config)# sflow max-datagram-size 1000

Setting the header size to the default value of 1400 bytes:

switch(config)# no sflow max-datagram-size

sflow polling

Syntax

sflow polling <INTERVAL>

no sflow polling [<INTERVAL>]

Description

Defines the global polling interval for sFlow in seconds.

48

AOS-CX 10.06 IP Services Guide

The no form of this command sets the polling interval to the default value of 30 seconds.

Command context

config

Parameters
<INTERVAL>

Specifies the polling interval in seconds. Range: 10 to 3600. Default: 30.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the polling interval to 10:

switch(config)# sflow polling 10

Setting the polling interval to the default value.

switch(config)# no sflow polling

sflow sampling

Syntax

sflow sampling <RATE>

no sflow sampling [<RATE>]

Description

Defines the global sampling rate for sFlow in number of packets. The default sampling rate is 4096, which
means that one in every 4096 packets is sampled. A warning message is displayed when the sampling rate is
set to less than 4096 and proceeds only after user confirmation.

The no form of this command sets the sampling rate to the default value of 4096.

Command context

config

Parameters
sampling <RATE>

Specifies the sampling rate. Range: 1 to 1000000000. Default: 4096.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the sampling rate to 5000:

switch(config)# sflow sampling 5000

Setting the sampling rate to the default:

Chapter 4 sFlow

49

switch(config)# no sflow sampling

Setting the sampling rate to 1000:

switch(config)# sflow sampling 1000
Setting the sFlow sampling rate lower than 4096 is not recommended and might
affect system performance.
Do you want to continue [y/n]? y
switch(config)#

show sflow

Syntax

show sflow [interface <INTERFACE-NAME>] [vsx-peer]

Description

Shows sFlow configuration settings and statistics for all interfaces, or for a specific interface

Command context

Manager (#)

Parameters
interface <INTERFACE-NAME>

Specifies the name of an interface on the switch.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing sFlow information for all interfaces:

switch# show sflow
sFlow Global Configuration
-----------------------------------------
sFlow                         enabled
Collector IP/Port/Vrf         10.0.0.2/6343/default
                              10.0.0.3/6400/default
Agent Address                 10.0.0.1
Sampling Rate                 1024
Polling Interval              30
Header Size                   128
Max Datagram Size             1400

sFlow Status
-----------------------------------------
Running - Yes

sFlow Statistics
-----------------------------------------
Number of Samples             200

50

AOS-CX 10.06 IP Services Guide

- Agent address is not configured.

Showing sFlow information for interface 1/1/1:

switch# show sflow 1/1/1
sFlow configuration - Interface 1
-----------------------------------------
sFlow                         enabled
Sampling Rate                 1024
Number of Samples             30

Chapter 4 sFlow

51

Chapter 5
DHCP client

DHCP client commands

ip dhcp

Syntax

ip dhcp

Description

Enables the DHCP client on the management interface enabling the interface to automatically obtain an IP
address from a DHCP server on the network. By default, the DHCP client is enabled.

Command context

config-if-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

This example enables the DHCP client on the management interface.

switch(config)# interface vlan 1
switch(config-if-vlan)# ip dhcp
switch(config-if-vlan)# no shutdown

If the interface is not enabled, you can enable it by entering the no shutdown command.

52

AOS-CX 10.06 IP Services Guide

Chapter 6
Internet Control Message Protocol (ICMP)

The Internet Control Message Protocol (ICMP) is a supporting protocol in the Internet protocol suite. The
protocol is used by network devices, including routers, to send error messages and operational information.
For example, an ICMP message might indicate that a requested service is not available. Another example of
an ICMP message might be that a host or router could not be reached.

ICMP message types
The type field identifies the type of message sent by the host or gateway.

Type

ICMP messages

0

3

4

5

8

9

10

11

12

13

14

15

16

17

18

Echo Reply (Ping Reply, used with Type 8, Ping
Request)

Destination Unreachable

Source Quench

Redirect

Echo Request (Ping Request, used with Type 0, Ping
Reply)

Router Advertisement (Used with Type 9)

Router Solicitation (Used with Type 10)

Time Exceeded

Parameter Problem

Timestamp Request (Used with Type 14)

Timestamp Reply (Used with Type 13)

Information Request (obsolete) (Used with Type 16)

Information Reply (obsolete) (Used with Type 15)

Address Mask Request (Used with Type 17)

Address Mask Reply (Used with Type 18)

Chapter 6 Internet Control Message Protocol (ICMP)

53

When ICMP messages are sent
ICMP messages are sent when one or more of the following scenarios occur:

• A datagram cannot reach its destination.

• The gateway does not have the buffering capacity to forward a datagram.

• The gateway can direct the host to send traffic on a shorter route.

ICMP redirect messages
ICMP redirect messages are used by routers to notify the hosts on the data link that a better route is
available for a particular destination.

When ICMP redirect messages are sent
The switch is configured to send redirects by default. ICMP redirect messages are sent when one or more of
the following scenarios occur:

• The interface on which the packet comes into the router is the same interface on which the packet gets

routed out.

• The subnet or network of the source IP address is on the same subnet or network of the next-hop IP

address of the routed packet.

• The datagram is not source-routed.

• The destination unicast address is unreachable. In this case, the router generates the ICMP destination

unreachable message to inform the source host about the situation.

ICMP commands

ip icmp redirect

Syntax

ip icmp redirect

no ip icmp redirect

Description

Enables the sending of ICMPv4 and ICMPv6 redirect messages to the source host. Enabled by default.

The no form of this command disables ICMPv4 and ICMPv6 redirect messages to the source host.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ICMP redirect messages:

54

AOS-CX 10.06 IP Services Guide

switch(config)# ip icmp redirect

Disabling ICMP redirect messages:

switch(config)# no ip icmp redirect

ip icmp throttle

Syntax

ip icmp throttle <packet-interval>

no ip icmp throttle

Description

Used to configure the throttle parameter for both ICMPv4 and ICMPv6 error messages and redirect
messages.

The no form of this command disables the throttle parameter for both ICMPv4 and ICMPv6 error messages
and redirect messages.

Command context

config

Parameters
<packet-interval>

Specifies the ICMPv4/v6 packet interval in seconds. Default: 1 second. Range: 1-86400.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling the throttle parameter for both ICMPv4 and ICMPv6 error messages and redirect messages:

switch(config)# ip icmp throttle 3000

Disabling the throttle parameter for both ICMPv4 and ICMPv6 error messages and redirect messages:

switch(config)# no ip icmp throttle

ip icmp unreachable

Syntax

ip icmp unreachable

no ip icmp unreachable

Description

Enables the sending of ICMPv4 and ICMPv6 destination unreachable messages on the switch to a source
host when a specific host is unreachable. The unreachable host address originates from the failed packed.
Default setting.

The no form of this command disables the sending of ICMPv4 and ICMPv6 destination unreachable
messages from the switch to a source host when a specific host is unreachable. This command does not
prevent other hosts from sending an ICMP unreachable message.

Chapter 6 Internet Control Message Protocol (ICMP)

55

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ICMPv4 and ICMPv6 destination unreachable messages to a source host:

switch(config)# ip icmp unreachable

Disabling ICMPv4 and ICMPv6 destination unreachable messages to a source host:

switch(config)# no ip icmp unreachable

56

AOS-CX 10.06 IP Services Guide

Chapter 7
DNS

The Domain Name System (DNS) is the Internet protocol for mapping a hostname to its IP address. DNS
allows users to enter more readily memorable and intuitive hostnames, rather than IP addresses, to identify
devices connected to a network. It also allows a host to keep the same hostname even if it changes its IP
address.

Hostname resolution can be either static or dynamic.

•

In static resolution, a local table is defined on the switch that associates hostnames with their IP
addresses. Static tables can be used to speed up the resolution of frequently queried hosts.

• Dynamic resolution requires that the switch query a DNS server located elsewhere on the network.

Dynamic name resolution takes more time than static name resolution, but requires far less
configuration and management.

DNS client
The DNS client resolves hostnames to IP addresses for protocols that are running on the switch. When the
DNS client receives a request to resolve a hostname, it can do so in one of two ways:

•

Forward the request to a DNS name server for resolution.

• Reply to the request without using a DNS name server, by resolving the name using a statically defined

table of hostnames and their associated IP addresses.

Configuring the DNS client

Procedure

1. Configure one or more DNS name servers with the command ip dns server.

2. To resolve DNS requests by appending a domain name to the requests, either configure a single domain
name with the command ip dns domain-name, or configure a list of up to six domain names with the
command ip dns domain-list.

3. To use static name resolution for certain hosts, associate an IP address to a host with the command ip

dns host.

4. Review your DNS configuration settings with the command show ip dns.

Examples

This example creates the following configuration:

• Defines the domain switch.com to append to all requests.

• Defines a DNS server with IPv4 address of 1.1.1.1.

Chapter 7 DNS

57

• Defines a static DNS host named myhost1 with an IPv4 address of 3.3.3.3.

• DNS client traffic is sent on the default VRF (named default).

switch(config)# ip dns domain-name switch.com
switch(config)# ip dns server-address 1.1.1.1
switch(config)# ip dns host myhost1 3.3.3.3
switch(config)# exit
switch# show ip dns

VRF Name : default
Domain Name: switch.com
Name Server(s): 1.1.1.1

Host Name                                                        Address
--------------------------------------------------------------------------------
myhost1                                                          3.3.3.3
switch#

DNS client commands

ip dns domain-list

Syntax

ip dns domain-list <DOMAIN-NAME> [vrf default]

no ip dns domain-list <DOMAIN-NAME> [vrf default]

Description

Configures one or more domain names that are appended to the DNS request. The DNS client appends
each name in succession until the DNS server replies. Domains can be either IPv4 or IPv6. By default,
requests are forwarded on the default VRF.

The no form of this command removes a domain from the list.

Command context

config

Parameters
list <DOMAIN-NAME>

Specifies a domain name. Up to six domains can be added to the list. Length: 1 to 256 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

This example defines a list with two entries: domain1.com and domain2.com.

switch(config)# ip dns domain-list domain1.com
switch(config)# ip dns domain-list domain2.com

This example removes the entry domain1.com.

58

AOS-CX 10.06 IP Services Guide

switch(config)# no ip dns domain-list domain1.com

ip dns domain-name

Syntax

ip dns domain-name <DOMAIN-NAME> [ vrf <VRF-NAME> ]

no ip dns domain-name <DOMAIN-NAME> [ vrf <VRF-NAME> ]

Description

Configures a domain name that is appended to the DNS request. The domain can be either IPv4 or IPv6. By
default, requests are forwarded on the default VRF. If a domain list is defined with the command ip dns
domain-list, the domain name defined with this command is ignored.

The no form of this command removes the domain name.

Command context

config

Parameters
<DOMAIN-NAME>

Specifies the domain name to append to DNS requests. Length: 1 to 256 characters.

vrf <VRF-NAME>

Specifies a VRF name. Default: default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the default domain name to domain.com:

switch(config)# ip dns domain-name domain.com

Removing the default domain name domain.com:

switch(config)# no ip dns domain-name domain.com

ip dns host

Syntax

ip dns host <HOST-NAME> <IP-ADDR> [ vrf <VRF-NAME> ]

no ip dns host <HOST-NAME> <IP-ADDR> [ vrf <VRF-NAME> ]

Description

Associates a static IP address with a hostname. The DNS client returns this IP address instead of querying a
DNS server for an IP address for the hostname. Up to six hosts can be defined. If no VRF is defined, the
default VRF is used.

The no form of this command removes a static IP address associated with a hostname.

Chapter 7 DNS

59

Command context

config

Parameters
host <HOST-NAME>

Specifies the name of a host. Length: 1 to 256 characters.

<IP-ADDR>

Specifies an IP address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255, or IPv6
format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a hexadecimal number from 0 to
F.

vrf <VRF-NAME>

Specifies a VRF name. Default: default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

This example defines an IPv4 address of 3.3.3.3 for host1.

switch(config)# ip dns host host1 3.3.3.3

This example defines an IPv6 address of b::5 for host 1.

switch(config)# ip dns host host1 b::5

This example defines removes the entry for host 1 with address b::5.

switch(config)# no ip dns host host1 b::5

ip dns server address

Syntax

ip dns server-address <IP-ADDR> [ vrf <VRF-NAME> ]

no ip dns server-address <IP-ADDR> [ vrf <VRF-NAME> ]

Description

Configures the DNS name servers that the DNS client queries to resolve DNS queries. Up to six name
servers can be defined. The DNS client queries the servers in the order that they are defined. If no VRF is
defined, the default VRF is used.

The no form of this command removes a name server from the list.

Command context

config

Parameters
<IP-ADDR>

Specifies an IP address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255, or IPv6
format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a hexadecimal number from 0 to
F.

60

AOS-CX 10.06 IP Services Guide

vrf <VRF-NAME>

Specifies a VRF name. Default: default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

This example defines a name server at 1.1.1.1.

switch(config)# ip dns server-address 1.1.1.1

This example defines a name server at a::1.

switch(config)# ip dns server-address a::1

This example removes a name server at a::1.

switch(config)# no ip dns server-address a::1

show ip dns

Syntax

show ip dns [vrf <VRF-NAME>] [vsx-peer]

Description

Shows all DNS client configuration settings or the settings for a specific VRF.

Command context

Manager (#)

Parameters
vrf <VRF-NAME>

Specifies the VRF for which to show information. If no VRF is defined, the default VRF is used.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Chapter 7 DNS

61

Chapter 8
ARP

ARP (Address Resolution Protocol) is used to map the network address assigned to a device to its physical
address. For example, on an Ethernet network, ARP maps layer 3 IPv4 network addresses to layer 2 MAC
addresses. (ARP does not work with IPv6 addresses. Instead, the Neighbor discovery protocol is used.)

ARP operates at layer 2. ARP requests are broadcast to all devices on the local network segment and are not
forwarded by routers. ARP is enabled by default and cannot be disabled.

Proxy ARP

Proxy ARP allows a routing switch to answer ARP requests from devices on one network on behalf of devices
on another network. The ARP proxy is aware of the location of the traffic destination, and offers its own MAC
address as the final destination.

For example, if Proxy ARP is enabled on a routing switch connected to two subnets (10.10.10.0/24 and
20.20.20.0/24), the routing switch can respond to an ARP request from 10.10.10.69 for the MAC address of
the device with IP address 20.20.20.69.

Typically, the host that sent the ARP request then sends its packets to the switch that has the ARP proxy. This
switch then forwards the packets to the intended host through a mechanism such as a tunnel.

Proxy ARP is supported on L3 physical and VLAN interfaces. It is disabled by default. To enable proxy ARP,
routing must be enabled on the interface.

Local proxy ARP

Local proxy ARP is a technique by which a device on a given network answers the ARP queries for a host
address that is on the same network. It is primarily used to enable layer 3 communication between hosts
within a common subnet that are separated by layer 2 boundaries (Example: PVLAN). Local proxy ARP is
supported on L3 physical and VLAN interfaces.

Local proxy ARP is disabled by default. Routing must be enabled on the interface to enable local proxy ARP.

Dynamic ARP Inspection

ARP is used for resolving IP against MAC addresses on a broadcast network segment like the Ethernet and
was originally defined by Internet Standard RFC 826. ARP does not support any inherent security mechanism
and as such depends on simple datagram exchanges for the resolution, with many of these being broadcast.

Because it is an unreliable and non-secure protocol, ARP is vulnerable to attacks. Some attacks may be
targeted toward the networks whereas other attacks may be targeted toward the switch itself. The attacks
primarily intend to create denial of service (DoS) for the other entities present in the network.

Most of the attacks are carried out in one of the following three forms:

• Overwhelming the switch control plane with too many ARP packets.

• Overwhelming the switch control plane with too many unresolved data packets.

• Masquerading as a trusted gateway/server by wrongly advertising ARPs.

Several defense mechanisms can be put in place on a switch to protect against attacks:

62

AOS-CX 10.06 IP Services Guide

•

Limit the amount of ARP activity allowed from a host or on a port.

• Ensure that all ARP packets are consistent with one or more binding databases, which can be created

through various means.

• Enforce integrity checks on the ARP packets to check against different MAC or IP addresses in the

Ethernet or IP header and ARP header.

This release implements Dynamic ARP Inspection to enforce DHCP snooping binding on all ARP packets and
is limited to the 8400 platform. The feature will be disabled from the code, CLI, and schema by the use of
appropriate config flags for other platforms.

Only the following is supported:

• Enabling and disabling of Dynamic ARP Inspection on a VLAN level (it does not have to be SVI).

• Defining the member ports of a VLAN as either trusted or untrusted.

• Only ARP traffic on untrusted ports subjected to checks.

• Routed ports (RoPs) always treated as trusted.

•

Listening to the DHCP Bindings table and check every ARP packet to match against the binding.

ARP ACLs are not supported in this release and the DHCP snooping table will be the only source of binding.

ARP commands

arp cache-limit

Syntax

arp cache-limit <LIMIT>

Description

Specifies the maximum number of entries in the ARP (Address Resolution Protocol) cache.

Command context

config

Parameters
<LIMIT>

Specifies the maximum number of entries in the ARP cache. Range: 4096 to 131072. Default: 131072.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# arp cache-limit 4097

Chapter 8 ARP

63

arp inspection

Syntax

arp inspection

Description

Enables Dynamic ARP Inspection on the current VLAN, forcing all ARP packets from untrusted ports to be
subjected to a MAC-IP association check against a binding table.

The no form of this command disables Dynamic ARP Inspection on the VLAN.

Command context

config-vlan-<VLAN-ID>

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling dynamic ARP inspection:

switch# configure terminal
switch(config)# vlan 1
switch(config-vlan)# arp inspection

Disabling dynamic ARP inspection:

switch# configure terminal
switch(config)# vlan 1
switch(config-vlan)# no arp inspection

arp inspection trust

Syntax

arp inspection trust

no arp inspection trust

Description

Configures the interface as a trusted. All interfaces are untrusted by default.

The no form of this command returns the interface to the default state (untrusted).

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Example

Setting an interface as trusted:

switch(config-if)# arp inspection trust

64

AOS-CX 10.06 IP Services Guide

arp ipv4 mac

Syntax

arp ipv4 <IPV4_ADDR> mac <MAC_ADDR>

no arp ipv4 <IPV4_ADDR> mac <MAC_ADDR>

Description

Specifies a permanent static neighbor entry in the ARP table (for IPv4 neighbors).

The no form of this command deletes a permanent static neighbor entry from the ARP table.

Command context

config-if

config-if-vlan

Parameters
ipv4 <IPV4-ADDR>

Specifies the IP address of the neighbor or the virtual IP address of the cluster in IPv4 format (x.x.x.x),
where x is a decimal number from 0 to 255. . Range: 4096 to 131072. Default: 131072.

mac <MAC-ADDR>

Specifies the MAC address of the neighbor or the multicast MAC address in IANA format
(xx:xx:xx:xx:xx:xx), where x is a hexadecimal number from 0 to F. Range: 4096 to 131072. Default:
131072.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configuring a static ARP entry on a interface VLAN 10:

switch(config)# interface vlan 10
switch(config-if-vlan)# arp ipv4 2.2.2.2 mac 01:00:5e:00:00:01

Removing a static ARP entry on interface VLAN10:

switch(config)# interface vlan 10
switch(config-if-vlan)# no arp ipv4 2.2.2.2 mac 01:00:5e:00:00:01

clear arp

Syntax

clear arp [port <PORT-ID> | vrf {all-vrfs | <VRF-NAME>}]

Description

Clears IPv4 and IPv6 neighbor entries from the ARP table. If you do not specify any parameters, ARP table
entries are cleared for the default VRF.

Command context

Manager (#)

Chapter 8 ARP

65

Parameters
port <PORT-ID>

Specifies a physical port on the switch. Format: member/slot/port. For example: vlan 2. .

all-vrfs

Selects all VRFs.

<VRF-NAME>

Specifies the name of a VRF. Default: default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Clearing all IPv4 and IPv6 neighbor ARP entries for the default VRF:

switch# clear arp

Clearing all ARP neighbor entries for a port ():

switch# clear arp vlan 2

ipv6 neighbor mac

Syntax

ipv6 neighbor <IPV6-ADDR> mac <MAC-ADDR>

no ipv6 neighbor <IPV6-ADDR> mac <MAC-ADDR>

Description

Specifies a permanent static neighbor entry in the ARP table (for IPv6 neighbors).

The no form of this command deletes a permanent static neighbor entry from the ARP table.

Command context

config-if

Parameters
<IPV6-ADDR>>

Specifies an IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F. Range: 4096 to 131072. Default: 131072.

mac <MAC-ADDR>>

Specifies the MAC address of the neighbor (xx:xx:xx:xx:xx:xx), where x is a hexadecimal number
from 0 to F. Range: 4096 to 131072. Default: 131072.

Authority

Administrators or local user group members with execution rights for this command.

Example

Creates a static ARP entry on interface vlan 2.

66

AOS-CX 10.06 IP Services Guide

switch(config)# interface vlan 2
switch(config-if-vlan)# arp ipv6 neighbor 2001:0db8:85a3::8a2e:0370:7334 mac 00:50:56:96:df:c8

show arp

Syntax

show arp [vsx-peer]

Description

Shows the entries in the ARP (Address Resolution Protocol) table.

Command context

Manager (#)

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Administrators or local user group members with execution rights for this command.

Usage

This command displays information about ARP entries, including the IP address, MAC address, port, and
state.

When no parameters are specified, the show arp command shows all ARP entries for the default VRF
(Virtual Router Forwarding) instance.

Examples

switch# show arp

IPv4 Address     MAC                Port         Physical
Port                        State
-------------------------------------------------------------------------------
192.168.1.2          00:50:56:96:7b:e0  vlan10        1/1/29           stale
192.168.1.3          00:50:56:96:7b:ac  vlan10        1/1/1            reachable

Total Number Of ARP Entries Listed- 2.
-------------------------------------------------------------------------------

show arp inspection interface

Syntax

show arp inspection interface

Description

Displays the current configuration of dynamic ARP inspection on a VLAN or interface.

Command context

Operator (>) or Manager (#)

Chapter 8 ARP

67

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch# show arp inspection interface

---------------------------------------------------------------------------
Interface           Trust-State
---------------------------------------------------------------------------
1/1/1               Untrusted
---------------------------------------------------------------------------

switch# show arp inspection interface vsx-peer

---------------------------------------------------------------------------
Interface           Trust-State
---------------------------------------------------------------------------
1/1/1               Untrusted
lag100              Trusted
---------------------------------------------------------------------------

switch# show arp inspection interface 1/1/1

---------------------------------------------------------------------------
Interface           Trust-State
---------------------------------------------------------------------------
1/1/1               Untrusted
---------------------------------------------------------------------------

show arp inspection statistics

Syntax

show arp inspection statistics

Description

Displays statistics about forwarded and dropped ARP packets.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch# show arp inspection statistics vlan 1-200

-----------------------------------------------------------------
VLAN   Name              Forwarded           Dropped
-----------------------------------------------------------------
1      DEFAULT_VLAN_1    0                   0
-----------------------------------------------------------------

68

AOS-CX 10.06 IP Services Guide

switch# show arp inspection statistics vlan vsx-peer

-----------------------------------------------------------------
VLAN   Name              Forwarded           Dropped
-----------------------------------------------------------------
1      DEFAULT_VLAN_1    0                   0
200    VLAN200           0                   0
-----------------------------------------------------------------

show arp state

Syntax

show arp state {all | failed | incomplete | permanent | reachable | stale} [vsx-peer]

Description

Shows ARP (Address Resolution Protocol) cache entries that are in the specified state.

Command context

Operator (>) or Manager (#)

Parameters
all

Shows the ARP cache entries for all VRF (Virtual Router Forwarding) instances.

failed

Shows the ARP cache entries that are in failed state. The neighbor might have been deleted.

incomplete

Shows the ARP cache entries that are in incomplete state.

An incomplete state means that address resolution is in progress and the link-layer address of the
neighbor has not yet been determined. A solicitation request was sent, and the switch is waiting for a
solicitation reply or a timeout.

permanent

Shows the ARP cache entries that are in permanent state. ARP entries that are in a permanent state can
be removed by administrative action only.

reachable

Shows the ARP cache entries that are in reachable state, meaning that the neighbor is known to have
been reachable recently.

stale

Shows ARP cache entries that are in stale state.

ARP cache entries are in the stale state if the elapsed time is in excess of the ARP timeout in seconds
since the last positive confirmation that the forwarding path was functioning properly.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Chapter 8 ARP

69

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch# show arp state failed

IPv4 Address     MAC                Port         Physical Port    State
---------------------------------------------------------------------------
192.168.1.4                         vlan10                         failed

show arp summary

Syntax

show arp summary [all-vrfs | vrf <VRF-NAME>] [vsx-peer]

Description

Shows a summary of the IPv4 and IPv6 neighbor entries on the switch for all VRFs or a specific VRF.

Command context

Operator (>) or Manager (#)

Parameters
all-vrfs

Selects all VRFs.

vrf <VRF-NAME>

Specifies the name of a VRF.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing summary ARP information for all VRFs:

switch# show arp summary all-vrfs

ARP Entry's State                : IPv4     IPv6
-------------------------------------------------------

Number of Reachable ARP entries  : 2         0

Number of Stale ARP entries      : 0         0

Number of Failed ARP entries     : 2         2

70

AOS-CX 10.06 IP Services Guide

Number of Incomplete ARP entries : 0         0

Number of Permanent ARP entries  : 0         0

-------------------------------------------------------

Total ARP Entries: 6             : 4         2

-------------------------------------------------------

Showing a summary of all IPv4 and IPv6 neighbor entries on the primary and secondary (peer) switches:

vsx-primary# show arp summary
ARP Entry's State                 IPv4        IPv6
---------------------------------------------------------
Number of Reachable ARP entries   25858       32231
Number of Stale ARP entries       0           1
Number of Failed ARP entries      0           257
Number of Incomplete ARP entries  0           0
Number of Permanent ARP entries   0           0
---------------------------------------------------------
Total ARP Entries- 58347          25858       32489

vsx-primary# show arp summary vsx-peer
ARP Entry's State                 IPv4        IPv6
---------------------------------------------------------
Number of Reachable ARP entries   25858       32168
Number of Stale ARP entries       0           3
Number of Failed ARP entries      0           317
Number of Incomplete ARP entries  0           0
Number of Permanent ARP entries   0           0
---------------------------------------------------------
Total ARP Entries- 58346          25858       32488
---------------------------------------------------------

show arp timeout

Syntax

show arp timeout [<INTERFACE>][vsx-peer]

Description

Shows the age-out period for each ARP (Address Resolution Protocol) entry for a port, LAG, or VLAN
interface.

Command context

Operator (>) or Manager (#)

Parameters
<INTERFACE>

Specifies a physical port, VLAN, or LAG on the switch. For physical ports, use the format (for example,
1/3/1).

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Chapter 8 ARP

71

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing ARP timeout information for a VLAN:

switch# show arp timeout vlan2
Port             VRF                              Timeout
----------------------------------------------------------
vlan2            default                          1800

show arp vrf

Syntax

show arp {all-vrfs | vrf <VRF-NAME>} [vsx-peer]

Description

Shows the ARP table for all VRF instances, or for the named VRF.

Command context

Operator (>) or Manager (#)

Parameters
all-vrfs

Specifies all VRFs.

vrf <VRF-NAME>

Specifies the name of a VRF. Length: 1 to 32 alphanumeric characters.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing ARP entries for VRF test.

switch# show arp vrf test
ARP IPv4 Entries:
-------------------------------------------------------
IPv4 Address    MAC                Port    Physical Port  State      VRF
10.20.30.40     00:50:56:bd:6a:c5  1/1/29  1/1/29         reachable  test
-------------------------------------------------------
Total Number Of ARP Entries Listed: 1.
-------------------------------------------------------

switch# show arp all-vrfs
ARP IPv4 Entries:

72

AOS-CX 10.06 IP Services Guide

-------------------------------------------------------
IPv4 Address    MAC                Port    Physical Port  State      VRF
192.168.120.10  00:50:56:bd:10:be  1/1/32  1/1/32         reachable  red
10.20.30.40     00:50:56:bd:6a:c5  1/1/29  1/1/29         reachable  test
-------------------------------------------------------
Total Number Of ARP Entries Listed: 2.
-------------------------------------------------------

Showing ARP entries for all VRFs.

switch# show arp all-vrfs
ARP IPv4 Entries:
-------------------------------------------------------
IPv4 Address    MAC                Port    Physical Port  State      VRF
192.168.120.10  00:50:56:bd:10:be  1/1/32  1/1/32         reachable  red
10.20.30.40     00:50:56:bd:6a:c5  1/1/29  1/1/29         reachable  test
-------------------------------------------------------
Total Number Of ARP Entries Listed: 2.
-------------------------------------------------------

show ipv6 neighbors

Syntax

show ipv6 neighbors {all-vrfs | vrf <VRF-NAME>} [vsx-peer]

Description

Shows entries in the ARP table for all IPv6 neighbors for all VRFs or for a specific VRF.

When no parameters are specified, this command shows all ARP entries for the default VRF, and state
information for reachable and stale entries only.

Command context

Operator (>) or Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Parameters
all-vrfs

Specifies all VRFs.

vrf <VRF-NAME>

Specifies a VRF name. Length: 1 to 32 alphanumeric characters.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Examples

switch# show ipv6 neighbors
IPv6 Entries:

-------------------------------------------------------

IPv6 Address                 MAC                Port      Physical Port  State

Chapter 8 ARP

73

fe80::a21d:48ff:fe8f:2700    a0:1d:48:8f:27:00  vlan2300  1/1/31         reachable

fe80::f603:43ff:fe80:a600    f4:03:43:80:a6:00  vlan2300  1/1/30         reachable

-------------------------------------------------------

Total Number Of IPv6 Neighbors Entries Listed: 2.

-------------------------------------------------------

show ipv6 neighbors state

Syntax

show ipv6 neighbors state {all | failed | incomplete | permanent | reachable | stale} [vsx-peer]

Description

Shows all IPv6 neighbor ARP (Address Resolution Protocol) cache entries, or those cache entries that are in
the specified state.

Command context

Operator (>) or Manager (#)

Parameters
all

Shows all ARP cache entries.

failed

Shows ARP cache entries that are in failed state. The neighbor might have been deleted. Set the
neighbor to be unreachable.

incomplete

Shows ARP cache entries that are in incomplete state.

An incomplete state means that address resolution is in progress and the link-layer address of the
neighbor has not yet been determined. This means that a solicitation request was sent, and you are
waiting for a solicitation reply or a timeout.

permanent

Shows ARP cache entries that are in permanent state.

reachable

Shows ARP cache entries that are in reachable state, meaning that the neighbor is known to have been
reachable recently.

stale

Shows ARP cache entries that are in stale state.

ARP cache entries are in the stale state if the elapsed time is in excess of the ARP timeout in seconds
since the last positive confirmation that the forwarding path was functioning properly.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

74

AOS-CX 10.06 IP Services Guide

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 neighbors state all

IPv6 Address                  MAC                Port     Physical Port    State
--------------------------------------------------------------------------------
100::2                        48:0f:cf:af:f1:cc  lag1     lag1             reachable
300::3                        48:0f:cf:af:33:be  vlan3    1/4/20           reachable
fe80::4a0f:cfff:feaf:f1cc     48:0f:cf:af:f1:cc  lag1     lag1             reachable
200::3                        48:0f:cf:af:33:be  1/4/11   1/4/11           reachable
fe80::4a0f:cfff:feaf:33be     48:0f:cf:af:33:be  vlan3    1/4/20           reachable

Total Number Of IPv6 Neighbors Entries Listed- 5.
---------------------------------------------------------------------------------

Chapter 8 ARP

75

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

• Technical support registration number (if applicable)

• Product name, model or version, and serial number

• Operating system name and version

•

Firmware version

• Error messages

• Product-specific reports and logs

• Add-on products or components

• Third-party products or components

Other useful sites

Other websites that can be used to find information:

Airheads social forums and
Knowledge Base

https://community.arubanetworks.com/

Software licensing

https://lms.arubanetworks.com/

End-of-Life information

https://www.arubanetworks.com/support-services/end-of-life/

Aruba software and
documentation

https://asp.arubanetworks.com/downloads

Accessing updates
To download product updates:

76

AOS-CX 10.06 IP Services Guide

Aruba Support Portal

https://asp.arubanetworks.com/downloads

If you are unable to find your product in the Aruba Support Portal, you may need to search My Networking,
where older networking products can be found:

My Networking

https://www.hpe.com/networking/support

To view and update your entitlements, and to link your contracts and warranties with your profile, go to the
Hewlett Packard Enterprise Support Center More Information on Access to Support Materials page:

https://support.hpe.com/portal/site/hpsc/aae/home/

IMPORTANT: Access to some updates might require product entitlement when accessed
through the Hewlett Packard Enterprise Support Center. You must have an HP Passport set up
with relevant entitlements.

Some software products provide a mechanism for accessing software updates through the product
interface. Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://asp.arubanetworks.com/notifications/subscriptions (requires an active Aruba Support Portal
(ASP) account to manage subscriptions). Security notices are viewable without an ASP account.

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

Chapter 9 Support and other resources

77

