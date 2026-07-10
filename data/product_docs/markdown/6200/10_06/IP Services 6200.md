AOS-CX 10.06 IP Services Guide
6200 Switch Series

Part Number: 5200-7706
Published: November 2020
Edition: 1

© Copyright 2020 Hewlett Packard Enterprise Development LP

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

Chapter 1 About this document...................................................................... 7
Applicable products........................................................................................................................................7
Latest version available online......................................................................................................................7
Command syntax notation conventions..................................................................................................... 7
About the examples....................................................................................................................................... 8
Identifying switch ports and interfaces .......................................................................................................8

Chapter 2 IRDP...................................................................................................10
Configuring IRDP.......................................................................................................................................... 11
IRDP commands .......................................................................................................................................... 12
diag-dump irdp basic................................................................................................................12
ip irdp............................................................................................................................................. 13
ip irdp holdtime.........................................................................................................................13
ip irdp maxadvertinterval.................................................................................................... 14
ip irdp minadvertinterval.................................................................................................... 14
ip irdp preference.................................................................................................................... 15
show ip irdp..................................................................................................................................16

Chapter 3 IPv6 Router Advertisement......................................................... 17
Configuring IPv6 RA......................................................................................................................................17
IPv6 RA scenario........................................................................................................................................... 19
IPv6 RA commands.......................................................................................................................................19
ipv6 address <global-unicast-address>......................................................................... 20
ipv6 address autoconfig......................................................................................................... 20
ipv6 address link-local......................................................................................................... 21
ipv6 nd cache-limit.................................................................................................................. 22
ipv6 nd dad attempts................................................................................................................23
ipv6 nd hop-limit...................................................................................................................... 23
ipv6 nd mtu.................................................................................................................................... 24
ipv6 nd ns-interval.................................................................................................................. 24
ipv6 nd prefix............................................................................................................................. 25
ipv6 nd ra dns search-list.................................................................................................. 26
ipv6 nd ra dns server............................................................................................................. 27
ipv6 nd ra lifetime.................................................................................................................. 28
ipv6 nd ra managed-config-flag......................................................................................... 29
ipv6 nd ra max-interval......................................................................................................... 29
ipv6 nd ra min-interval......................................................................................................... 30
ipv6 nd ra other-config-flag..............................................................................................31
ipv6 nd ra reachable-time.................................................................................................... 32
ipv6 nd ra retrans-timer.......................................................................................................32
ipv6 nd router-preference.................................................................................................... 33
ipv6 nd suppress-ra.................................................................................................................. 33
show ipv6 nd global traffic................................................................................................ 34
show ipv6 nd interface........................................................................................................... 35
show ipv6 nd interface prefix........................................................................................... 37
show ipv6 nd ra dns search-list....................................................................................... 38

Contents

3

show ipv6 nd ra dns server.................................................................................................. 39

Chapter 4 sFlow................................................................................................. 41
sFlow agent................................................................................................................................................... 41
Configuring the sFlow agent....................................................................................................................... 42
sFlow scenario.............................................................................................................................................. 43
sFlow scenario 2........................................................................................................................................... 44
sFlow agent commands .............................................................................................................................. 47
sflow..................................................................................................................................................47
sflow agent-ip............................................................................................................................. 48
sflow collector........................................................................................................................... 49
sflow disable............................................................................................................................... 50
sflow header-size...................................................................................................................... 50
sflow max-datagram-size......................................................................................................... 51
sflow polling............................................................................................................................... 51
sflow sampling............................................................................................................................. 52
show sflow...................................................................................................................................... 53

Chapter 5 DHCP client......................................................................................55
DHCP client commands............................................................................................................................... 55
ip dhcp............................................................................................................................................. 55

Chapter 6 DHCP snooping............................................................................... 56
DHCPv4 snooping commands.................................................................................................................... 56
clear dhcpv4-snooping binding........................................................................................... 57
clear dhcpv4-snooping statistics.....................................................................................57
dhcpv4-snooping........................................................................................................................... 58
dhcpv4-snooping (in config-vlan context).............................................................................58
dhcpv4-snooping allow-overwrite-binding.....................................................................59
dhcpv4-snooping authorized-server.................................................................................. 60
dhcpv4-snooping external-storage.....................................................................................61
dhcpv4-snooping max-bindings..............................................................................................61
dhcpv4-snooping option 82.................................................................................................... 62
dhcpv4-snooping trust............................................................................................................. 63
dhcpv4-snooping verify mac.................................................................................................. 64
show dhcpv4-snooping................................................................................................................65
show dhcpv4-snooping binding..............................................................................................66
show dhcpv4-snooping statistics....................................................................................... 66
DHCPv6 snooping commands.................................................................................................................... 67
clear dhcpv6-snooping binding........................................................................................... 67
clear dhcpv6-snooping statistics.....................................................................................68
dhcpv6-snooping........................................................................................................................... 68
dhcpv6-snooping (in config-vlan context).............................................................................69
dhcpv6-snooping authorized-server.................................................................................. 69
dhcpv6-snooping external-storage.....................................................................................70
dhcpv6-snooping max-bindings..............................................................................................71
dhcpv6-snooping trust............................................................................................................. 72
show dhcpv6-snooping................................................................................................................73
show dhcpv6-snooping binding..............................................................................................74
show dhcpv6-snooping statistics....................................................................................... 74

4

AOS-CX 10.06 IP Services Guide

Chapter 7 ND snooping....................................................................................76
ND snooping commands.............................................................................................................................76
clear nd-snooping binding.................................................................................................... 76
clear nd-snooping statistics..............................................................................................77
nd-snooping.................................................................................................................................... 78
nd-snooping (in config-vlan context)......................................................................................78
nd-snooping mac-check............................................................................................................. 79
nd-snooping prefix-list......................................................................................................... 79
nd-snooping max-bindings.......................................................................................................80
nd-snooping nd-guard................................................................................................................81
nd-snooping ra-guard ............................................................................................................. 82
nd-snooping ra-drop.................................................................................................................. 83
nd-snooping trust...................................................................................................................... 83
show nd-snooping.........................................................................................................................84
show nd-snooping binding.......................................................................................................85
show nd-snooping prefix-list ........................................................................................... 86
show nd-snooping statistics................................................................................................ 86

Chapter 8 IP tunnels ........................................................................................88
Configuring an IP tunnel..............................................................................................................................88
Creating an IPv6 in IPv4 tunnel for traversing a public network............................................................ 89
Creating an IPv6 in IPv6 tunnel for traversing a public network............................................................ 90
IP tunnels commands.................................................................................................................................. 92
description.................................................................................................................................... 92
destination ip............................................................................................................................. 93
destination ipv6.........................................................................................................................94
interface tunnel.........................................................................................................................94
ip address...................................................................................................................................... 95
ipv6 address..................................................................................................................................96
ip mtu............................................................................................................................................... 97
show interface tunnel............................................................................................................. 98
show running-config interface tunnel............................................................................99
shutdown...........................................................................................................................................99
source ip...................................................................................................................................... 100
source ipv6.................................................................................................................................. 101
ttl.................................................................................................................................................... 101

Chapter 9 Internet Control Message Protocol (ICMP)............................ 103
ICMP message types.................................................................................................................................. 103
When ICMP messages are sent................................................................................................................ 104
ICMP redirect messages............................................................................................................................ 104
When ICMP redirect messages are sent..................................................................................................104
ICMP commands........................................................................................................................................ 104
ip icmp redirect.......................................................................................................................104
ip icmp throttle.......................................................................................................................105
ip icmp unreachable................................................................................................................105

Chapter 10 DNS............................................................................................... 107
DNS client.................................................................................................................................................... 107
Configuring the DNS client........................................................................................................................107

Contents

5

DNS client commands .............................................................................................................................. 108
ip dns domain-list.................................................................................................................. 108
ip dns domain-name.................................................................................................................. 109
ip dns host.................................................................................................................................. 109
ip dns server address........................................................................................................... 110
show ip dns.................................................................................................................................. 111

Chapter 11 ARP................................................................................................113
Configuring proxy ARP...............................................................................................................................114
Configuring local proxy ARP......................................................................................................................114
Dynamic ARP Inspection ...........................................................................................................................115
ARP commands.......................................................................................................................................... 115
arp cache-limit.........................................................................................................................115
arp inspection........................................................................................................................... 116
arp inspection trust..............................................................................................................117
arp ipv4 mac................................................................................................................................117
clear arp...................................................................................................................................... 118
ip local-proxy-arp.................................................................................................................. 118
ipv6 neighbor mac.................................................................................................................... 119
ip proxy-arp................................................................................................................................120
show arp.........................................................................................................................................121
show arp inspection interface......................................................................................... 121
show arp inspection statistics....................................................................................... 122
show arp state........................................................................................................................... 123
show arp summary.......................................................................................................................124
show arp timeout.......................................................................................................................125
show arp vrf................................................................................................................................126
show ipv6 neighbors................................................................................................................127
show ipv6 neighbors state.................................................................................................. 128

Chapter 12 Support and other resources..................................................130
Accessing Aruba Support.......................................................................................................................... 130
Accessing updates......................................................................................................................................130
Warranty information................................................................................................................................ 131
Regulatory information............................................................................................................................. 131
Documentation feedback..........................................................................................................................131

6

AOS-CX 10.06 IP Services Guide

Chapter 1
About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

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

Chapter 1 About this document

7

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

8

AOS-CX 10.06 IP Services Guide

On the 6200 Switch Series

• member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The
primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•

slot: Line module number. Always 1.

• port: Physical number of a port on a line module.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

Chapter 1 About this document

9

Chapter 2
IRDP

ICMP Router Discovery Protocol (IRDP), an extension of the ICMP, is independent of any routing protocol. It
allows hosts to discover the IP addresses of neighboring routers that can act as default gateways to reach
devices on other IP networks.

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

Destination address of RA

An RA uses either of the following destination IP addresses:

10

AOS-CX 10.06 IP Services Guide

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

1. Enable IRDP on an interface with the command ip irdp.

2. Set the maximum hold time with the command ip irdp holdtime.

3. Set the maximum router advertisement interval with the command ip irdp maxadvertinterval.

4. Set the minimum router advertisement interval with the command ip irdp minadvertinterval.

5. Set the IRDP preference level with the command ip irdp preference.

6. Review IRDP configuration settings with the command show ip irdp.

Example

This example creates the following configuration:

• Enables IRDP on the layer 3 interface 1/1/1 with packet type set to broadcast.

• Sets the hold time to 5000 seconds.

• Sets the advertisement interval to 30 seconds.

Chapter 2 IRDP

11

• Sets the minimum advertisement interval to 25 seconds.

• Sets the IRDP preference level to 25.

switch(config)# interface 1/1/1
switch(config-if)# ip irdp broadcast
switch(config-if)# ip irdp holdtime 5000
switch(config-if)# ip irdp maxadvertinterval 30
switch(config-if)# ip irdp minadvertinterval 25
switch(config-if)# ip irdp preference 25

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
[Start] Feature irdp Time : Thu Jun  8 09:50:28 2017

=========================================================================
-------------------------------------------------------------------------
[Start] Daemon hpe-rdiscd
-------------------------------------------------------------------------
Interface: 1/1/1 (state : Up)
rdisc ipv4 (enabled: 0, max:600, min:450, hold:1800, pref:0, isBcast:0)
Router IPs - 192.168.1.2,
Interface: 1/1/2 (state : Up)
rdisc ipv4 (enabled: 0, max:600, min:450, hold:1800, pref:0, isBcast:0)
Router IPs - 192.168.2.2,

-------------------------------------------------------------------------
[End] Daemon hpe-rdiscd
-------------------------------------------------------------------------
=========================================================================
[End] Feature irdp
=========================================================================
Diagnostic dump captured for feature irdp

12

AOS-CX 10.06 IP Services Guide

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

Enabling IRDP on interface 1/1/1 with packet type set to the default value (multicast).

switch(config)# interface 1/1/1
switch(config-if)# ip irdp

Enabling IRDP on interface 1/1/1 with packet type set to broadcast.

switch(config)# interface 1/1/1
switch(config-if)# ip irdp broadcast

Disabling IRDP.

switch(config)# interface 1/1/1
switch(config-if)# no ip irdp

ip irdp holdtime

Syntax

ip irdp holdtime <TIME>

Description
Specifies the maximum amount of time the host will consider an advertisement to be valid until a newer
advertisement arrives. When a new advertisement arrives, hold time is reset. Hold time must be greater
than or equal to the maximum advertisement interval. Therefore, if the hold time for an advertisement
expires, the host can reasonably conclude that the router interface that sent the advertisement is no longer
available. The default hold time is three times the maximum advertisement interval.

Chapter 2 IRDP

13

Command context

config-if

Parameters
<TIME>

Specifies the lifetime of router advertisements sent from this interface. Range: 4 to 9000 seconds.
Default: 1800 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Example

Setting the hold time for interface 1/1/1 to 5000 seconds:

switch(config)# interface 1/1/1
switch(config-if)# ip irdp holdtime 5000

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

Setting the advertisement interval for interface 1/1/1 to 30 seconds:

switch(config)# interface 1/1/1
switch(config-if)# ip irdp maxadvertinterval 30

ip irdp minadvertinterval

Syntax

ip irdp minadvertinterval <TIME>

14

AOS-CX 10.06 IP Services Guide

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

Setting the minimum advertisement interval for interface 1/1/1 to 25 seconds:

switch(config)# interface 1/1/1
switch(config-if)# ip irdp minadvertinterval 25

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

Setting the IRDP preference level for interface 1/1/1 to 25.

switch(config)# interface 1/1/1
switch(config-if)# ip irdp preference 25

Chapter 2 IRDP

15

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

switch# show ip irdp

ICMP Router Discovery Protocol

 Interface Status   Advertising Minimum  Maximum  Holdtime Preference
                    Address     Interval Interval
 --------- -------- ----------- -------- -------- -------- -----------
 1/1/1     Enabled  multicast   6        8        10       10
 1/1/2     Disabled multicast   450      600      1800     0
 1/1/3     Enabled  broadcast   450      600      1800     115

16

AOS-CX 10.06 IP Services Guide

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

Chapter 3 IPv6 Router Advertisement

17

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

• Enables IPV6 RA on interface 1/1/3.

• Sets the recursive DNS server address to 4001::1 with a lifetime of 400 seconds.

• Sets the minimum interval between transmissions to 3 seconds.

• Sets the maximum interval between transmissions to 13 seconds.

• Sets the lifetime of a default router to 1900 seconds.

switch(config)# interface 1/1/3
switch(config)# no ipv6 nd suppress-ra
switch(config-if)# ipv6 nd ra dns server 4001::1 lifetime 400
switch(config-if)# ipv6 nd ra min-interval 3
switch(config-if)# ipv6 nd ra max-interval 13
switch(config-if)# ipv6 nd ra lifetime 1900
switch(config-if)# end
switch# show ipv6 nd interface 1/1/3
Interface 1/1/3 is up
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

18

AOS-CX 10.06 IP Services Guide

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
Recursive DNS Server List on: 1/1/3
     Suppress DNS Server List: No
     DNS Server 1: 2001::1    lifetime 400

IPv6 RA scenario
In this scenario, two host computers are auto-configured with IP addresses using IPv6 RA. In addition, the
switch provides the hosts with an address of a recursive DNS server. The physical topology of the network
looks like this:

Procedure

1. Configure the interfaces with IPv6 addresses.

switch# config
switch(config)# interface 1/1/1
switch(config-if)# ipv6 address 2001::1/64
switch(config)# interface 1/1/2
switch(config-if)# ipv6 address 2001::2/64
switch(config)# interface 1/1/3
switch(config-if)# ipv6 address 2001::3/64

2. Enable transmission of all IPv6 RA messages.

switch(config-if)# no ipv6 nd suppress-ra

IPv6 RA commands

Chapter 3 IPv6 Router Advertisement

19

ipv6 address <global-unicast-address>

Syntax

ipv6 address <global-unicast-address>

no ipv6 address <global-unicast-address>

Description

Sets a global unicast address on the interface.

The no form of this command removes the global unicast address on the interface.

NOTE: This command automatically creates an IPv6 link-local address on the interface.
However, it does not add the ipv6 address link-local command to the running
configuration. If you remove the IPv6 address, the link-local address is also removed. To
maintain the link-local address, you must manually execute the ipv6 address link-local
command.

Command context

config-if

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Enabling a global unicast address:

switch(config)# interface 1/1/1
switch(config-if)#  ipv6 address 3731:54:65fe:2::a7

Disabling a global unicast address:

switch(config)# interface 1/1/1
switch(config-if)#  no ipv6 address 3731:54:65fe:2::a7

ipv6 address autoconfig

Syntax

ipv6 address autoconfig

no ipv6 address autoconfig

Description

Enables the interface to automatically obtain an IPv6 address using router advertisement information and
the EUI-64 identifier.

The no form of this command disables address auto-configuration.

20

AOS-CX 10.06 IP Services Guide

NOTE:

• A maximum of 15 autoconfigured addresses are supported.

• This command automatically creates an IPv6 link-local address on the interface. However, it
does not add the ipv6 address link-local command to the running configuration. If
you remove the IPv6 address, the link-local address is also removed. To maintain the link-
local address, you must manually execute the ipv6 address link-local command.

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

switch(config)# interface 1/1/1
switch(config-if)# ipv6 address autoconfig

Disabling unicast autoconfiguring:

switch(config)# interface 1/1/1
switch(config-if)# no ipv6 address autoconfig

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

Chapter 3 IPv6 Router Advertisement

21

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

switch(config)# interface 1/1/1
switch(config-if)# ipv6 address link-local

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

22

AOS-CX 10.06 IP Services Guide

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

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd dad attempts 5

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

Chapter 3 IPv6 Router Advertisement

23

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd hop-limit 64

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

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd mtu 1300

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

24

AOS-CX 10.06 IP Services Guide

Parameters
<TIME>

Specifies the neighbor solicitation interval. Range: 1000-3600000 milliseconds. Default: 1000
milliseconds.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ns-interval 1200

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

Chapter 3 IPv6 Router Advertisement

25

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

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd prefix 4001::1/64 valid 30 preferred 10 no-autoconfig no-onlink

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

26

AOS-CX 10.06 IP Services Guide

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

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra dns search-list test.com lifetime 500

ipv6 nd ra dns server

Syntax

ipv6 nd ra dns server <IPV6-ADDR>  [lifetime <TIME>]

no ipv6 nd ra dns server <IPV6-ADDR>

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

Chapter 3 IPv6 Router Advertisement

27

Usage

•

Including RDNSS information in RAs provides DNS server configuration for connected IPv6 hosts without
requiring DHCPv6.

• Multiple servers can be configured on the interface by using the command repeatedly.

• A maximum of eight server addresses are allowed.

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra dns server 2001::1 lifetime 400

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

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra lifetime 1200

28

AOS-CX 10.06 IP Services Guide

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

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra managed-config-flag

ipv6 nd ra max-interval

Syntax

ipv6 nd ra max-interval <TIME>

no ipv6 nd ra max-interval [<TIME>]

Chapter 3 IPv6 Router Advertisement

29

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

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra max-interval 30

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

30

AOS-CX 10.06 IP Services Guide

Authority

Administrators or local user group members with execution rights for this command.

Usage

• This value has one setting per interface and does not apply to RAs sent in response to a router

solicitation received from another device.

• The min-interval must be less than the max-interval. Attempting to set min-interval to a higher value

results in an error message.

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra  min-interval 25

ipv6 nd ra other-config-flag

Syntax

ipv6 nd ra other-config-flag

no ipv6 nd ra other-config-flag

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

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra other-config-flag

Chapter 3 IPv6 Router Advertisement

31

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

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra reachable-time 2000

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

32

AOS-CX 10.06 IP Services Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra retrans-timer 400

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

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd router-preference high

ipv6 nd suppress-ra

Syntax

ipv6 nd suppress-ra [<SUPPRESS-OPTION>]

no ipv6 nd ra supress-ra [<SUPPRESS-OPTION>]

Description

Configures suppression of IPv6 Router Advertisement transmissions on an interface.

Chapter 3 IPv6 Router Advertisement

33

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

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd suppress-ra mtu dnssl rdnss
switch(config-if)# no ipv6 nd suppress-ra mtu dnssl rdnss

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

34

AOS-CX 10.06 IP Services Guide

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

Chapter 3 IPv6 Router Advertisement

35

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing information for all VRFs:

switch# show ipv6 nd interface all-vrfs

List of IPv6 Interfaces for VRF default
Interface 1/1/1 is up
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
      Send "Retrans Timer" field: 0
      Suppress RA: true
      Suppress MTU in RA: true
  ICMPv6 error message parameters:
      Send redirects: false
  ICMPv6 DAD parameters:
      Current DAD attempt: 1

List of IPv6 Interfaces for VRF red
Interface 1/1/2 is up
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

Showing information for interface 1/1/1:

36

AOS-CX 10.06 IP Services Guide

switch# show ipv6 nd interface 1/1/1
Interface 1/1/1 is up
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

switch# show ipv6 nd interface

List of IPv6 Interfaces for VRF default
Interface 1/1/1 is up
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

Chapter 3 IPv6 Router Advertisement

37

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

Examples

Showing prefix information for the default VRF:

switch# show ipv6 nd interface prefix

List of IPv6 Interfaces for VRF default
List of IPv6 Prefix advertised on 1/1/1
   Prefix : 4545::/65
   Enabled : Yes
   Validlife time : 2592000
   Preferred lifetime : 604800
   On-link : Yes
   Autonomous : Yes

Showing information for VRF red:

switch# show ipv6 nd interface prefix vrf red

List of IPv6 Interfaces for VRF red
List of IPv6 Prefix advertised on 1/1/2
   Prefix : 2001::/64
   Enabled : Yes
   Validlife time : 2592000
   Preferred lifetime : 604800
   On-link : Yes
   Autonomous : Yes

show ipv6 nd ra dns search-list

Syntax

show ipv6 nd ra dns search-list [vsx-peer]

38

AOS-CX 10.06 IP Services Guide

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

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra dns search-list test.com
switch# show ipv6 nd ra dns search-list
Recursive DNS Search List on: 1
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

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra dns server 2001::1
switch# show ipv6 nd ra dns server
Recursive DNS Server List on: 1

Chapter 3 IPv6 Router Advertisement

39

     Suppress DNS Server List: Yes
     DNS Server 1: 2001::1    lifetime 1800

40

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

41

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

42

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
In this scenario, two hosts send sFlow traffic through a switch to an sFlow collector. The physical topology of
the network looks like this:

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

5. Configure interface 1/1/1 with IP address 10.10.10.1/24.

switch(config)# interface 1/1/1
switch(config-if)# no shutdown

Chapter 4 sFlow

43

switch(config-if)# ip address 10.10.10.1/24
switch(config)# quit

6. Configure interface 1/1/2 with IP address 10.10.11.1/24.

switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# ip address 10.10.11.1/24
switch(config)# quit

7. Configure interface 1/1/3 with IP address 10.10.12.1/24.

switch(config)# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# ip address 10.10.12.1/24
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
connect the two switches. The physical topology of the network looks like this:

44

AOS-CX 10.06 IP Services Guide

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

Chapter 4 sFlow

45

f. Define LAG 100 and assign VLAN vlan 8 to it.

switch(config)# interface lag 100
switch(config-lag-if)# no shutdown
switch(config-lag-if)# vlan access 8
switch(config-lag-if)# lacp mode active

g. Configure interface 1/1/1.

switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# vlan access 8

h. Configure interface 1/1/2 and 1/1/3 as members of LAG 100.

switch# (config)#interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# lag 100
switch(config-if)# exit
switch(config)-if# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# lag 100
switch(config-if)# exit

i. Configure interface 1/1/4 with IP address 10.10.12.1/24.

switch# (config)#interface 1/1/4
switch(config-if)# no shutdown
switch(config-if)# ip address 10.10.12.1/24
switch(config-if)# quit

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

46

AOS-CX 10.06 IP Services Guide

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

Chapter 4 sFlow

47

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

48

AOS-CX 10.06 IP Services Guide

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

Chapter 4 sFlow

49

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

50

AOS-CX 10.06 IP Services Guide

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

Chapter 4 sFlow

51

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

52

AOS-CX 10.06 IP Services Guide

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

Chapter 4 sFlow

53

- Agent address is not configured.

Showing sFlow information for interface 1/1/1:

switch# show sflow 1/1/1
sFlow configuration - Interface 1
-----------------------------------------
sFlow                         enabled
Sampling Rate                 1024
Number of Samples             30

54

AOS-CX 10.06 IP Services Guide

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

config-if-mgmt

Authority

Administrators or local user group members with execution rights for this command.

Examples

This example enables the DHCP client on the management interface.

switch(config)# interface mgmt
switch(config-if-mgmt)# ip dhcp
switch(config-if-mgmt)# no shutdown

If the interface is not enabled, you can enable it by entering the no shutdown command.

Chapter 5 DHCP client

55

Chapter 6
DHCP snooping

Overview

DHCP is a protocol used by DHCP servers in IP networks to dynamically allocate network configuration data
to client devices (DHCP clients). Possible network configuration data includes user IP address, subnet mask,
default gateway IP address, DNS server IP address, and lease duration. The DHCP protocol enables DHCP
clients to be dynamically configured with such network configuration data without any manual setup
process.

DHCP snooping is a security feature that helps avoid problems caused by an unauthorized DHCP server on
the network that provides invalid configuration data to DHCP clients. A user without malicious intent may
cause this problem by unknowingly adding to the network a switch or other device that includes a DHCP
server enabled by default. In some cases, a user with malicious intent adds a DHCP server to the network as
part of their Denial of Service or Man in the Middle attack.

DHCP snooping helps prevent such problems by distinguishing between trusted ports connected to
legitimate DHCP servers, and untrusted ports connected to general users. DHCP packets are forwarded
between trusted ports without inspection. DHCP packets received on other switch ports are inspected
before being forwarded. DHCP Packets from untrusted sources are dropped.

In addition, in support of the separate IP source lockdown feature, DHCP snooping also dynamically collects
client information (VLAN, IPv4 address, MAC address, interface), adding the information to the switch IP
binding database. Alternatively, also in support of IP lockdown, the IP binding database can be statically
updated using the ipv4 source-binding or ipv6 source-binding commands. Statically configured IP
binding information supersedes any dynamically collected information for the same client.

DHCPv4 snooping conditions for dropping DHCPv4 packets

Applies only to DHCPv4 snooping.

Packet types that
are dropped

DHCPOFFER,
DHCPACK,
DHCPNACK

Conditions for dropping the packets

• A packet from a DHCP server is received on an untrusted port.

• The switch is configured with a list of authorized DHCP server addresses and a

packet is received from a DHCP server on a trusted port with a source IP address
that is not in the list of authorized DHCP server addresses.

DHCPRELEASE,
DHCPDECLINE

A broadcast packet that has a MAC address in the DHCP binding database, but the
port in the DHCP binding database does not match the port on which the packet is
received.

All DHCP packet
types

• When enabled (the default) a DHCP packet received on an untrusted port in

which the DHCP client hardware MAC address does not match the source MAC
address in the packet.

• When enabled (the default), a DHCP packet containing DHCP relay information

(option 82) is received from an untrusted port.

DHCPv4 snooping commands

56

AOS-CX 10.06 IP Services Guide

clear dhcpv4-snooping binding

Syntax

clear dhcpv4-snooping binding {all | ip <IPV4-ADDR> vlan <VLAN-ID> |
                                     port <PORT-NUM> | vlan <VLAN-ID>}

Description

Clears DHCPv4 snooping binding entries.

Command context

Operator (>) or Manager (#)

Parameters
all

Specifies that all DHCPv4 binding information is to be cleared.

ip <IPV4-ADDR> vlan <VLAN-ID>

Specifies the IPv4 address and VLAN for which all DHCPv4 binding information is to be cleared.

port <PORT-NUM>

Specifies the port number for which all DHCPv4 binding information is to be cleared.

vlan <VLAN-ID>

Specifies the VLAN for which all DHCPv4 binding information is to be cleared.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Clearing all DHCPv4 binding information for IP address 192.168.2.4 and VLAN 5:

switch(config)# clear dhcpv4-snooping binding ip 192.168.2.4 vlan 5

Clearing all DHCPv4 binding information for port 1/1/1:

switch(config)# clear dhcpv4-snooping binding port 1/1/1

Clearing all DHCPv4 binding information for VLAN 10:

switch(config)# clear dhcpv4-snooping binding vlan 10

Clearing all DHCPv4 binding information:

switch(config)# clear dhcpv4-snooping binding all

clear dhcpv4-snooping statistics

Syntax

clear dhcpv4-snooping statistics

Chapter 6 DHCP snooping

57

Description

Clears all DHCPv4 snooping statistics.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Clear all DHCPv4 snooping statistics:

switch# clear dhcpv4-snooping statistics

dhcpv4-snooping

Syntax

dhcpv4-snooping

no dhcpv4-snooping

Description

Enables DHCPv4 snooping. DHCPv4 snooping is disabled by default. DHCP snooping is not supported on the
management interface.

The no form of the command disables DHCPv4 snooping, flushing all the IP bindings learned since DHCPv4
snooping was enabled.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling DHCPv4 snooping:

switch(config)# dhcpv4-snooping

Disabling DHCPv4 snooping:

switch(config)# no dhcpv4-snooping

dhcpv4-snooping (in config-vlan context)

Syntax

dhcpv4-snooping

no dhcpv4-snooping

58

AOS-CX 10.06 IP Services Guide

Description

Enables DHCPv4 snooping in the config-vlan context. DHCPv4 snooping is disabled by default for all
VLANs.

The no form of the command disables DHCPv4 snooping on the specified VLAN, flushing all the IP bindings
learned for this VLAN since DHCPv4 snooping was enabled for this VLAN.

Command context

config-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling DHCPv4 snooping on VLAN 100:

switch(config)# vlan 100
switch(config-vlan-100)# dhcpv4-snooping
switch(config-vlan-100)# exit
switch(config)#

Disabling DHCPv4 snooping on VLAN 100:

switch(config)# vlan 100
switch(config-vlan-100)# no dhcpv4-snooping
switch(config-vlan-100)# exit
switch(config)#

dhcpv4-snooping allow-overwrite-binding

Syntax

dhcpv4-snooping allow-overwrite-binding

no dhcpv4-snooping allow-overwrite-binding

Description

Allows binding to be overwritten for the same IP address. When enabled, and a DHCP server offers a host an
IP address that is already bound to an existing host in the binding table, the existing binding is overwritten
for the new host if the new host is successfully able to acquire the same IP address. This overwriting is
disabled by default, causing the DHCP server offers to be dropped.

The no form of the command disables DHCPv4 snooping overwrite binding.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling DHCPv4 snooping overwrite binding:

switch(config)# dhcpv4-snooping allow-overwrite-binding

Chapter 6 DHCP snooping

59

Disabling DHCPv4 snooping overwrite binding:

switch(config)# no dhcpv4-snooping allow-overwrite-binding

dhcpv4-snooping authorized-server

Syntax

dhcpv4-snooping authorized-server <IPV4-ADDR> [vrf <VRF-NAME>]

no dhcpv4-snooping authorized-server <IPV4-ADDR> [vrf <VRF-NAME>]

Description

Adds an authorized (trusted) DHCP server to a list of authorized servers for use by DHCPv4 snooping. This
command can be issued multiple times, adding a maximum of 20 authorized servers per VRF. By default,
with an empty list of authorized servers, all DHCP servers are considered to be trusted for DHCPv4 snooping
purposes.

NOTE: The mgmt VRF cannot be used with this command.

The no form of this command deletes the specified DHCP server from the authorized list.

Command context

config

Parameters
<IPV4-ADDR>

Specifies the IPv4 address of the trusted DHCPv4 server.

vrf <VRF-NAME>

Specifies the VRF name. The name must be default.

Authority

Administrators or local user group members with execution rights for this command.

Usage

For authorized server lookup, the VRF is derived from the Switch Virtual Interface (SVI) configured for the
incoming VLAN. If the SVI is not configured, the default VRF is assumed.

Examples

Adding DHCP servers 192.168.2.2, 192.168.2.3, and 192.168.2.10 to the authorized server list:

switch(config)# dhcpv4-snooping authorized-server 192.168.2.2
switch(config)# dhcpv4-snooping authorized-server 192.168.2.3 vrf default
switch(config)# dhcpv4-snooping authorized-server 192.168.2.10 vrf default

Removing DHCP server 192.168.2.3 from the authorized server list:

switch(config)# no dhcpv4-snooping authorized-server 192.168.2.3 vrf default

60

AOS-CX 10.06 IP Services Guide

dhcpv4-snooping external-storage

Syntax

dhcpv4-snooping external-storage volume <VOL-NAME> file <FILE-NAME>

no dhcpv4-snooping external-storage

Description

Configures external storage to be used for backing up IP bindings (used by DHCPv4 snooping) to a file. When
configured, the switch stores all the IP bindings in an external storage file so that they are retained after the
switch restarts. When the switch restarts, it reads the IP bindings from the configured external storage file to
populate its local cache.

The no form of this command disables the saving of IP bindings in an external storage file.

Command context

config

Parameters
volume <VOL-NAME>

Specifies the name of the existing external storage volume where the IP bindings file will be saved.
Before running the dhcpv4-snooping external-storage volume command, first create the
external storage volume using command external-storage <VOLUME-NAME>. See External storage
commands in the Command-Line Interface Guide.

file <FILE-NAME>

Specifies the file name to use for storing IP bindings. Maximum 255 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring IP bindings storage in file dsnoop_ipbindings on existing volume dhcp_snoop:

switch(config)# dhcpv4-snooping external-storage volume dhcp_snoop file dsnoop_ipbindings

Disabling external storage:

switch(config)# no dhcpv4-snooping external-storage

dhcpv4-snooping max-bindings

Syntax

dhcpv4-snooping max-bindings <MAX-BINDINGS>

no dhcpv4-snooping max-bindings

Description

Sets the maximum number of DHCP bindings allowed on the selected interface. For all interfaces on which
this command is not run, the default max bindings applies.

The no form of the command reverts max bindings for the selected interface to its default.

Chapter 6 DHCP snooping

61

Command context

config-if

Parameters
<MAX-BINDINGS>

Specifies the maximum number of DHCP bindings. You can use the show capacities command to see
the maximum available for your switch model.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Set the DHCP max bindings to 512 on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# dhcpv4-snooping max-bindings 512
switch(config-if)# exit
switch(config)#

Revert DHCP max bindings to its default on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# no dhcpv4-snooping max-bindings
switch(config-if)# exit
switch(config)#

dhcpv4-snooping option 82

Syntax

dhcpv4-snooping option 82 [remote-id {mac | subnet-ip | mgmt-ip}]
                          [untrusted-policy {drop | keep | replace}]

no dhcpv4-snooping option 82

Description

Configures the addition of option 82 DHCP relay information to DHCP client packets that are being
forwarded on trusted ports. DHCP relay is enabled by default.

In the switch default state and when this command is entered without parameters (dhcpv4-snooping
option 82), this default configuration is used:

dhcpv4-snooping option 82 remote-id mac untrusted-policy drop

When remote-id is omitted, its default (mac) is used. When untrusted-policy is omitted, its default
(drop) is used.

The no form of this command disables DHCPv4 snooping option 82.

Command context

config

62

AOS-CX 10.06 IP Services Guide

Parameters
remote-id

Specifies what address to use as the remote ID for the replace option of untrusted-policy. Specify
one of these address types:

mac

The default. Uses the switch MAC address as the remote ID.

subnet-ip

Uses the IP address of the client VLAN as the remote ID.

mgmt-ip

Uses the management interface IP address as the remote ID.

untrusted-policy

Specifies what action to take for DHCP packets (with option 82) that are received on untrusted ports.
Specify one of these actions:

drop

The default. Drop DHCP packets (with option 82) without forwarding them.

keep

Forward DHCP packets (with option 82).

replace

Replace the option 82 information in the DHCP packets with whatever is set for remote-id (one of:
mac, subnet-ip, or mgmt-ip) and forward the packets.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring DHCPv4 snooping option 82 with the keep action:

switch(config)# dhcpv4-snooping option 82 untrusted-policy keep

Configuring DHCPv4 snooping option 82 with mgmt-ip as the remote-id and the replace action:

switch(config)# dhcpv4-snooping option 82 remote-id mgmt-ip untrusted-policy replace

Disabling DHCPv4 snooping option 82:

switch(config)# no dhcpv4-snooping option 82

dhcpv4-snooping trust

Syntax

dhcpv4-snooping trust

no dhcpv4-snooping trust

Description

Enables DHCPv4 snooping trust on the selected port. Only server packets received on trusted ports are
forwarded. All the ports are untrusted by default.

Chapter 6 DHCP snooping

63

The no form of the command disables DHCPv4 snooping trust on the selected port.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling DHCPv4 snooping trust on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# dhcpv4-snooping trust
switch(config-if)# exit
switch(config)#

Disabling DHCPv4 snooping trust on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# no dhcpv4-snooping trust
switch(config-if)# exit
switch(config)#

dhcpv4-snooping verify mac

Syntax

dhcpv4-snooping verify mac

no dhcpv4-snooping verify mac

Description

This command enables verification of the hardware address field in DHCP client packets. When enabled, the
DHCP client hardware address field and the source MAC address must be the same for packets received on
untrusted ports or else the packet is dropped. This DHCP snooping MAC verification is enabled by default.

The no form of the command disables DHCPv4 snooping MAC verification.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling DHCPv4 snooping MAC verification:

switch(config)# dhcpv4-snooping verify mac

Disabling DHCPv4 snooping MAC verification:

switch(config)# no dhcpv4-snooping verify mac

64

AOS-CX 10.06 IP Services Guide

show dhcpv4-snooping

Syntax

show dhcpv4-snooping [vsx-peer]

Description

Shows the DHCPv4 snooping configuration.

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

Showing the DHCPv4 snooping configuration:

switch(config)# show dhcpv4-snooping

 DHCPv4-Snooping Information

  DHCPv4-Snooping         : Yes         Verify MAC Address  : Yes
  Allow Overwrite Binding : No          Enabled VLANs       : 1751-2000

 Option 82 Configurations

  Untrusted Policy     : drop           Insertion           : Yes
  Option 82 Remote-id  : mac

 External Storage Information

  Volume Name          :
  File Name            :
  Inactive Since       : -
  Error                : -

 Authorized Server Configurations

  VRF                               Authorized Servers
  ------------                      ------------------

 Port Information

                   Max       Static    Dynamic
  Port      Trust  Bindings  Bindings  Bindings
  --------  -----  --------  --------  --------
  1/1/24    No     512       1         100
  lag13     Yes    0         0         0

Chapter 6 DHCP snooping

65

show dhcpv4-snooping binding

Syntax

show dhcpv4-snooping binding [vsx-peer]

Description

Shows the DHCPv4 snooping binding configuration.

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

Showing the DHCPv4 snooping binding configuration:

switch(config)# show dhcpv4-snooping binding

  MacAddress         IP               VLAN  Interface  Time-Left
  -----------------  ---------------  ----  ---------  ---------
  aa:b1:c1:dd:ee:ff  10.2.3.4         1     1/1/2      582
  aa:b2:c2:dd:ee:ff  10.2.3.5         1     1/1/2      584

show dhcpv4-snooping statistics

Syntax

show dhcpv4-snooping statistics [vsx-peer]

Description

Shows the DHCPv4 snooping statistics.

Command context

Operator (>) or Manager (#)

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

66

AOS-CX 10.06 IP Services Guide

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing the DHCPv4 snooping statistics:

switch(config)# show dhcpv4-snooping statistics

 Packet-Type  Action   Reason                         Count
 -----------  -------  -----------------------------  ---------
 server       forward  from trusted port              5425
 client       forward  to trusted port                3895
 server       drop     received on untrusted port     117
 server       drop     unauthorized server            214
 client       drop     destination on untrusted port  78
 client       drop     untrusted option 82 field      85
 client       drop     bad DHCP release request       0
 client       drop     failed verify MAC check        5
 client       drop     failed on max-binding limit    15

DHCPv6 snooping commands

clear dhcpv6-snooping binding

Syntax

clear dhcpv6-snooping binding {all | ip <IPV6-ADDR> vlan <VLAN-ID> |
                                     interface <IFNAME> | vlan <VLAN-ID>}

Description

Clears DHCPv6 snooping binding entries.

Command context

Operator (>) or Manager (#)

Parameters
all

Specifies that all DHCPv6 binding information is to be cleared.

ip <IPV6-ADDR> vlan <VLAN-ID>

Specifies the IPv6 address and VLAN for which all DHCPv6 binding information is to be cleared.

interface <IFNAME>

Specifies the interface for which all DHCPv6 binding information is to be cleared.

vlan <VLAN-ID>

Specifies the VLAN for which all DHCPv6 binding information is to be cleared. Range: 1 to 4094.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Chapter 6 DHCP snooping

67

Examples

Clearing all DHCPv6 binding information for 5000::1 vlan 1:

switch(config)# clear dhcpv6-snooping binding ip 5000::1 vlan 1

Clearing all DHCPv6 binding information for interface 1/1/10:

switch(config)# clear dhcpv6-snooping binding interface 1/1/10

Clearing all DHCPv6 binding information for VLAN 10:

switch(config)# clear dhcpv6-snooping binding vlan 10

Clearing all DHCPv6 binding information:

switch(config)# clear dhcpv6-snooping binding all

clear dhcpv6-snooping statistics

Syntax

clear dhcpv6-snooping statistics

Description

Clears all DHCPv6 snooping statistics.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Clear all DHCPv6 snooping statistics:

switch# clear dhcpv6-snooping statistics

dhcpv6-snooping

Syntax

dhcpv6-snooping

no dhcpv6-snooping

Description

Enables DHCPv6 snooping. DHCPv6 snooping is disabled by default. DHCPv6 snooping is not supported on
the management interface.

The no form of the command disables DHCPv6 snooping, flushing all the IP bindings learned since DHCPv6
snooping was enabled.

Command context

config

68

AOS-CX 10.06 IP Services Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling DHCPv6 snooping:

switch(config)# dhcpv6-snooping

Disabling DHCPv6 snooping:

switch(config)# no dhcpv6-snooping

dhcpv6-snooping (in config-vlan context)

Syntax

dhcpv6-snooping

no dhcpv6-snooping

Description

Enables DHCPv6 snooping in the config-vlan context. DHCPv6 snooping is disabled by default for all
VLANs.

The no form of the command disables DHCPv6 snooping on the specified VLAN, flushing all the IPv6
bindings learned for this VLAN since DHCPv6 snooping was enabled for this VLAN.

Command context

config-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling DHCPv6 snooping on VLAN 100:

switch(config)# vlan 100
switch(config-vlan-100)# dhcpv6-snooping
switch(config-vlan-100)# exit
switch(config)#

Disabling DHCPv6 snooping on VLAN 100:

switch(config)# vlan 100
switch(config-vlan-100)# no dhcpv6-snooping
switch(config-vlan-100)# exit
switch(config)#

dhcpv6-snooping authorized-server

Syntax

dhcpv6-snooping authorized-server <IPV6-ADDR> [vrf <VRF-NAME>]

no dhcpv6-snooping authorized-server <IPV6-ADDR> [vrf <VRF-NAME>]

Chapter 6 DHCP snooping

69

Description

Adds an authorized (trusted) DHCPv6 server to a list of authorized servers for use by DHCPv6 snooping. This
command can be issued multiple times, adding a maximum of 20 authorized servers per VRF. By default,
with an empty list of authorized servers, all DHCPv6 servers are considered to be trusted for DHCPv6
snooping purposes.

NOTE: The mgmt VRF cannot be used with this command.

NOTE: Configure the link local IPv6 address instead of global IPv6 address of the DHCPv6 server
as the authorized-server. For example:

switch(config)# dhcpv6-snooping authorized-server
fe80::2ca4:fa40:d4cd:bc2f

The no form of this command deletes the specified DHCPv6 server from the authorized list.

Command context

config

Parameters
<IPV6-ADDR>

Specifies the IPv6 address of the trusted DHCPv6 server.

vrf <VRF-NAME>

Specifies the VRF name. The name must be default.

Authority

Administrators or local user group members with execution rights for this command.

Usage

For authorized server lookup, the VRF is derived from the Switch Virtual Interface (SVI) configured for the
incoming VLAN. If the SVI is not configured, the default VRF is assumed.

Examples

Adding DHCP servers ABCD:5ACD::2000, and ABCD:5ACD::2010 to the authorized server list:

switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default
switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2010 vrf default

Removing DHCP server ABCD:5ACD::2000 from the authorized server list:

switch(config)# no dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default

dhcpv6-snooping external-storage

Syntax

dhcpv6-snooping external-storage volume <VOL-NAME> file <FILE-NAME>

no dhcpv6-snooping external-storage

70

AOS-CX 10.06 IP Services Guide

Description

Configures external storage to be used for backing up IPv6 bindings (used by DHCPv6 snooping) to a file.
When configured, the switch stores all the IP bindings in an external storage file so that they are retained
after the switch restarts. When the switch restarts, it reads the IPv6 bindings from the configured external
storage file to populate its local cache.

The no form of this command disables the saving of IPv6 bindings in an external storage file.

Command context

config

Parameters
volume <VOL-NAME>

Specifies the name of the existing external storage volume where the IPv6 bindings file will be saved.
Before running the dhcpv6-snooping external-storage volume command, first create the
external storage volume using command external-storage <VOLUME-NAME>. See External storage
commands in the Command-Line Interface Guide.

file <FILE-NAME>

Specifies the file name to use for storing IPv6 bindings. Maximum 255 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring IPv6 bindings storage in file ipv6Bindings on existing volume dhcp_snoop:

switch(config)# dhcpv6-snooping external-storage volume dhcp_snoop file ipv6Bindings

Disabling external storage:

switch(config)# no dhcpv6-snooping external-storage

dhcpv6-snooping max-bindings

Syntax

dhcpv6-snooping max-bindings <MAX-BINDINGS>

no dhcpv6-snooping max-bindings

Description

Sets the maximum number of DHCPv6 bindings allowed on the selected interface. For all interfaces on
which this command is not run, the default max bindings applies.

The no form of the command reverts max bindings for the selected interface to its default.

Command context

config-if

Chapter 6 DHCP snooping

71

Parameters
<MAX-BINDINGS>

Specifies the maximum number of DHCPv6 bindings. You can use the show capacities command to
see the maximum available for your switch model.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Set the DHCPv6 max bindings to 512 on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# dhcpv6-snooping max-bindings 512
switch(config-if)# exit
switch(config)#

Revert DHCPv6 max bindings to its default on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# no dhcpv6-snooping max-bindings
switch(config-if)# exit
switch(config)#

dhcpv6-snooping trust

Syntax

dhcpv6-snooping trust

no dhcpv6-snooping trust

Description

Enables DHCPv6 snooping trust on the selected interface. Only server packets received on trusted interfaces
are forwarded. All the interfaces are untrusted by default.

The no form of the command disables DHCPv6 snooping trust on the selected interface.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling DHCPv6 snooping trust on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# dhcpv6-snooping trust
switch(config-if)# exit
switch(config)#

Disabling DHCPv6 snooping trust on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# no dhcpv6-snooping trust

72

AOS-CX 10.06 IP Services Guide

switch(config-if)# exit
switch(config)#

show dhcpv6-snooping

Syntax

show dhcpv6-snooping [vsx-peer]

Description

Shows the DHCPv6 snooping configuration.

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

Showing the DHCPv6 snooping configuration:

switch(config)# show dhcpv6-snooping

 DHCPv6-Snooping Information

  DHCPv6-Snooping     : Yes    Enabled VLANs       : 1,5,7,100-110

 External Storage Information

  Volume Name          : dhcp_snoop
  File Name            : ip_binding
  Inactive Since       : 01:23:20 01/01/2019
  Error                : Failed to write external storage

 Authorized Server Configurations

  VRF                               Authorized Servers
  ------------                      ------------------
  default                           2001:0db8:85a3:0000:0000:8a2e:0370:7334
  default                           2002::2
  default                           2004::1
  red                               2002::1
  red                               2002::2
  red                               2002::9
  green                             5000::1
  green                             5000::2
  green                             5000::3
  green                             5000::7
  green                             5000::8

Chapter 6 DHCP snooping

73

 Port Information

                   Max       Static    Dynamic
  Port      Trust  Bindings  Bindings  Bindings
  --------  -----  --------  --------  --------
  1/1/2     Yes    0         0         0
  1/1/3     Yes    0         3         0
  1/1/5     Yes    0         22        0
  1/1/16    No     100       0         20
  10/10/10  No     512       12        7
  lag120    No     256       3         0

show dhcpv6-snooping binding

Syntax

show dhcpv6-snooping binding [vsx-peer]

Description

Shows the DHCPv6 snooping binding configuration.

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

Showing the DHCPv6 snooping binding configuration:

switch# show dhcpv6-snooping binding

 IP Binding Information
 ======================
 MAC-ADDRESS       IPV6-ADDRESS                              VLAN  INTERFACE   TIME-LEFT
 ----------------  ----------------------------------------  ----  ---------  ----------
 00:50:56:96:e4:cf aaaa:bbbb:cccc:dddd:eeee:1234:5678:abcd      1      1/1/1         584
 00:50:56:96:04:4d 1000::3                                    134      1/1/2         435
 00:50:56:96:d8:3d 2000:1000::4                              2002     lag123       21234

show dhcpv6-snooping statistics

Syntax

show dhcpv6-snooping statistics [vsx-peer]

Description

Shows the DHCPv6 snooping statistics.

74

AOS-CX 10.06 IP Services Guide

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

Showing the DHCPv6 snooping statistics:

switch(config)# show dhcpv6-snooping statistics

 Packet-Type  Action   Reason                         Count
 -----------  -------  -----------------------------  ---------
 server       forward  from trusted port              12
 client       forward  to trusted port                20
 server       drop     received on untrusted port     5
 server       drop     unauthorized server            4
 client       drop     destination on untrusted port  2
 client       drop     bad DHCP release request       5
 server       drop     relay reply on untrusted port  2
 client       drop     failed on max-binding limit    5

Chapter 6 DHCP snooping

75

Chapter 7
ND snooping

Overview

ND (Neighbor Discovery) snooping prevents ND attacks. ND snooping drops invalid ND packets, and
together with DIPLDv6 (Dynamic IP Lockdown for IPv6), blocks data traffic from invalid hosts. ND snooping is
used in Layer 2 switching networks. ND snooping learns the source MAC addresses, source IPv6 addresses,
input interfaces, and VLANs of incoming ND messages and data packets to build IP binding entries.

NOTE: When DHCPv6 snooping and ND snooping are both enabled, and DHCPv6 clients request
and IPv6 address, entries are added to the DHCP snooping table and DHCP snooping takes
priority over ND snooping.

ND snooping drops ND packets as follows:

•

•

•

If the Ethernet source MAC address is mismatched with the address contained in the ICMPv6 Target link
layer address field of the ND packet.

If the global IPv6 address in the source address field is mismatched with the ND snooping prefix filter
table.

If the global IPv6 address or the link-local IPv6 address in the source IP address field is mismatched with
the ND snooping binding table.

ND snooping drops RA and RR packets on untrusted ports. To block only RA packets on VLANs with ND
snooping enabled, use nd-snooping ra-drop. RA (Router Advertisement) drop is disabled by default on
VLANs. When enabled (with nd-snooping ra-drop), ND snooping blocks RA packets on both trusted and
untrusted ports. When RA drop is disabled, ND snooping allows RA packets on trusted ports and blocks
them on untrusted ports.

Dynamic IPv6 lockdown is performed for ND snooping entries. Based on the DAD NS received from the
hosts by the switch, ND snooping entries are programmed into the IP binding table and the hardware (as
allowed). And ND Binding table entries are added when NA packets are received from hosts. Therefore, data
packets from invalid hosts and transit traffic are blocked.

NOTE: Statically-configured IP binding information supersedes any information collected
dynamically by ND snooping for the same client.

ND snooping commands

clear nd-snooping binding

Syntax

clear nd-snooping binding {all | ipv6 <IPV6-ADDR> vlan <VLAN-ID> |
                                     port <PORT-NUM> | vlan <VLAN-ID>}

Description

Clears ND snooping binding entries.

76

AOS-CX 10.06 IP Services Guide

Command context

Operator (>) or Manager (#)

Parameters
all

Specifies that all ND binding information is to be cleared.

ip <IPV6-ADDR> vlan <VLAN-ID>

Specifies the IPv6 address and VLAN for which all ND binding information is to be cleared.

port <PORT-NUM>

Specifies the port for which all ND binding information is to be cleared.

vlan <VLAN-ID>

Specifies the VLAN for which all ND binding information is to be cleared. Range: 1 to 4094.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Clearing all ND binding information for 5000::1:

switch(config)# clear nd-snooping binding ipv6 5000::1

Clearing all ND binding information for 5000::1 vlan 1:

switch(config)# clear nd-snooping binding ipv6 5000::1 vlan 1

Clearing all ND binding information for port 1/1/10:

switch(config)# clear nd-snooping binding port 1/1/10

Clearing all ND binding information for VLAN 10:

switch(config)# clear nd-snooping binding vlan 10

Clearing all ND binding information:

switch(config)# clear nd-snooping binding all

clear nd-snooping statistics

Syntax

clear nd-snooping statistics

Description

Clears all ND snooping statistics.

Command context

Operator (>) or Manager (#)

Chapter 7 ND snooping

77

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Clear all ND snooping statistics:

switch# clear nd-snooping statistics

nd-snooping

Syntax

nd-snooping {enable|disable}

no nd-snooping {enable|disable}

Description

Enables or disables ND snooping. ND snooping is disabled by default. ND snooping is not supported on the
management interface.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ND snooping:

switch(config)# nd-snooping enable

Disabling ND snooping:

switch(config)# nd-snooping disable

nd-snooping (in config-vlan context)

Syntax

nd-snooping

no nd-snooping

Description

Enables ND snooping in the config-vlan context. ND snooping is disabled by default for all VLANs.

The no form of the command disables ND snooping on the specified VLAN, flushing all the IPv6 bindings
learned for this VLAN since ND snooping was enabled for this VLAN.

Command context

config-vlan

78

AOS-CX 10.06 IP Services Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ND snooping on VLAN 100:

switch(config)# vlan 100
switch(config-vlan-100)# nd-snooping
switch(config-vlan-100)# exit
switch(config)#

Disabling ND snooping on VLAN 100:

switch(config)# vlan 100
switch(config-vlan-100)# no nd-snooping
switch(config-vlan-100)# exit
switch(config)#

nd-snooping mac-check

Syntax

nd-snooping mac-check

no nd-snooping mac-check

Description

This command enables verification of the hardware address field in ND snooping packets. When enabled,
the ICMPv6 target link layer address field and the source MAC address must be the same for packets
received on untrusted ports or else the packets are dropped. This ND snooping MAC verification is enabled
by default.

The no form of the command disables ND snooping MAC verification.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ND snooping MAC verification:

switch(config)# nd-snooping mac-check

Disabling ND snooping MAC verification:

switch(config)# no nd-snooping mac-check

nd-snooping prefix-list

Syntax

nd-snooping prefix-list <IPV6-ADDR>

no nd-snooping prefix-list <IPV6-ADDR>

Chapter 7 ND snooping

79

Description

Configures the ND snooping prefix list for the selected VLAN and the specified IPv6 address prefix. ND
snooping must be enabled both globally and on this VLAN before this prefix list configuration takes effect.

The no form of this command removes the prefix list configuration for the selected VLAN and IPv6 address.

Command context

config-vlan

Parameters
<IPV6-ADDR>

Specifies the IPv6 address.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Configuring ND snooping prefix-list on VLAN 1:

switch(config)# vlan 1
switch(config-vlan-1)# nd-snooping prefix-list 2001::1/64
switch(config-vlan-1)# exit
switch(config)#

Remove configuration of ND snooping prefix-list on VLAN 100:

switch(config)# vlan 1
switch(config-vlan-1)# no nd-snooping prefix-list 2001::1/64
switch(config-vlan-1)# exit
switch(config)#

nd-snooping max-bindings

Syntax

nd-snooping max-bindings <MAX-BINDINGS>

no nd-snooping max-bindings

Description

Sets the maximum number of ND bindings allowed on the selected interface. For all interfaces on which this
command is not run, the default max bindings applies.

The no form of the command reverts max bindings for the selected interface to its default.

Command context

config-if

Parameters
<MAX-BINDINGS>

Specifies the maximum number of ND bindings. You can use the show capacities command to see
the maximum available for your switch model.

80

AOS-CX 10.06 IP Services Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

Set the ND max bindings to 768 on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# nd-snooping max-bindings 768
switch(config-if)# exit
switch(config)#

Revert ND max bindings to its default on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# no nd-snooping max-bindings
switch(config-if)# exit
switch(config)#

nd-snooping nd-guard

Syntax

nd-snooping nd-guard

no nd-snooping nd-guard

Description

This command enables ND guard on the selected VLAN.

The no form of the command disables ND guard and deletes all the IPv6 bindings learned on the VLAN.

NOTE: ND snooping must be enabled in both the global context and the config-vlan context
before this command can be used.

Command context

config-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ND snooping ND guard on VLAN 100:

switch(config)# nd-snooping enable
switch(config)# vlan 100
switch(config-vlan-100)# nd-snooping nd-guard
switch(config-vlan-100)# exit
switch(config)#

Disabling ND snooping ND guard on VLAN 100:

switch(config)# vlan 100
switch(config-vlan-100)# no nd-snooping nd-guard
switch(config-vlan-100)# exit
switch(config)#

Chapter 7 ND snooping

81

nd-snooping ra-guard

Syntax

nd-snooping ra-guard [log]

no nd-snooping ra-guard

Description

This command enables Routing Advertisement (RA) guard on the selected VLAN. When enabled, ingress
Routing Advertisement (RA) and Routing Redirect (RR) packets on the selected VLAN are blocked on
untrusted ports. The packets are forwarded when received on trusted ports.

The no form of the command disables RA guard on the VLAN.

NOTE: ND snooping must be enabled in both the global context and the config-vlan context
before this command can be used.

Command context

config-vlan

Parameters
[log]

Logs messages along with drop functionality.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ND snooping RA guard on VLAN 100:

switch(config)# nd-snooping enable
switch(config)# vlan 100
switch(config-vlan-100)# nd-snooping ra-guard
switch(config-vlan-100)# exit
switch(config)#

Enabling ND snooping RA guard on VLAN 100 with event logging on dropped packets:

switch(config)# nd-snooping enable
switch(config)# vlan 100
switch(config-vlan-100)# nd-snooping ra-guard log
switch(config-vlan-100)# exit
switch(config)#

Disabling ND snooping RA guard on VLAN 100:

switch(config)# vlan 100
switch(config-vlan-100)# no nd-snooping ra-guard
switch(config-vlan-100)# exit
switch(config)#

82

AOS-CX 10.06 IP Services Guide

nd-snooping ra-drop

Syntax

nd-snooping ra-drop

no nd-snooping ra-drop

Description

This command enables Routing Advertisement (RA) drop on the selected VLAN. When enabled, ingress RA
packets on the selected VLAN are blocked on both trusted and untrusted ports. When disabled, RA packets
are forwarded on the selected VLAN with ND snooping trusted port validation. RA drop is disabled by
default.

NOTE: ND snooping must be enabled in both the config context and the config-vlan context
before this command can be used.

The no form of the command disables ND snooping RA drop on the selected VLAN.

Command context

config-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ND snooping RA drop on VLAN 100:

switch(config)# nd-snooping enable
vlan 100
switch(config-vlan-100)# nd-snooping ra-drop
switch(config-vlan-100)# exit
switch(config)#

Disabling ND snooping RA drop on VLAN 100:

switch(config)# vlan 100
switch(config-vlan-100)# no nd-snooping ra-drop
switch(config-vlan-100)# exit
switch(config)#

nd-snooping trust

Syntax

nd-snooping trust

no nd-snooping trust

Description

Enables ND snooping trust on the selected interface (port). Only server packets received on trusted ports
are forwarded. All the ports are untrusted by default.

The no form of the command disables ND snooping trust on the selected port.

Chapter 7 ND snooping

83

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ND snooping trust on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# nd-snooping trust
switch(config-if)# exit
switch(config)#

Disabling ND snooping trust on interface 2/2/1:

switch(config)# interface 2/2/1
switch(config-if)# no nd-snooping trust
switch(config-if)# exit
switch(config)#

show nd-snooping

Syntax

show nd-snooping [vlan <VLAN-ID>] [vsx-peer]

Description

Shows either all ND snooping configuration or the configuration for the specified VLAN.

Command context

Operator (>) or Manager (#)

Parameters
vlan <VLAN-ID>

Specifies the VLAN for which the ND configuration is to be shown. Range: 1 to 4094.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing all ND snooping configuration:

switch(config)# show nd-snooping

  ND Snooping Information
  ========================

84

AOS-CX 10.06 IP Services Guide

  ND Snooping                  : Enabled
  ND Snooping Enabled VLANs    : 1
  RA Drop Enabled VLANs        : 2-3
  MAC Address Check            : Disabled

  PORT    TRUST  MAX-BINDINGS  CURRENT-BINDINGS
  ------- ------ ------------- -----------------
  1/1/1   Yes    -             -
  1/1/2   Yes    -             -
  1/1/3   No     100           10
  1/1/4   No     200           10
  1/1/5   No     300           10

Showing ND snooping configuration for VLAN 2:

switch(config)# show nd-snooping vlan 2

  ND Snooping Information
  =======================

  ND Snooping       : Enabled
  MAC Address Check : Disabled
  RA Drop           : Disabled

  PORT    TRUST  MAX-BINDINGS  CURRENT-BINDINGS
  ------- ------ ------------- -----------------
  1/1/1   Yes    -             -
  1/1/2   Yes    -             -
  1/1/3   No     100           10

show nd-snooping binding

Syntax

show nd-snooping binding [vsx-peer]

Description

Shows the ND snooping binding configuration.

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

Showing the ND snooping binding configuration:

Chapter 7 ND snooping

85

switch# show nd-snooping binding

  PORT    IPV6-ADDRESS                             MAC-ADDRESS        VLAN  TIME-LEFT STATE
  ------- ---------------------------------------- ------------------ ----- --------- ---------
  1/1/1   2001::1                                  00:00:0A:01:02:03  1     600       Valid
  1/1/2   fe80::250:56ff:fe9a:143c                 00:00:0B:01:02:03  2     -         Tentative
  1/1/3   2001:1111:2222:3333:4444:5555:6666:7777  00:00:0C:01:02:03  4094  -         Testing

show nd-snooping prefix-list

Syntax

show nd-snooping prefix-list [vsx-peer]

Description

Shows the ND snooping prefix list information.

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

Showing the ND snooping prefix list information:

switch# show nd-snooping prefix-list

  VLAN  IPV6-ADDRESS-PREFIX                         SOURCE
  ----- ------------------------------------------- --------
  1     2001::/64                                   Static
  4094  3001::/64                                   Dynamic

show nd-snooping statistics

Syntax

show nd-snooping statistics [vsx-peer]

Description

Shows the global ND snooping statistics.

Command context

Operator (>) or Manager (#)

86

AOS-CX 10.06 IP Services Guide

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing the global ND snooping statistics:

switch(config)# show nd-snooping statistics

  PACKET-TYPE  ACTION   REASON                                          COUNT
  ------------ -------- ----------------------------------------------- --------
  RA           forward  RA packets received on trusted port              20
  RA           drop     RA packets received on untrusted port            45
  NS           forward  NS packets received on trusted port              52
  NS           forward  NS packets received on untrusted port            95
  NS           drop     NS packets failed MAC check                      14
  NS           drop     NS packets failed Prefix check                   12
  NS           drop     NS packets failed on max-binding limit           0
  NS           drop     NS packets failed ND snooping validation checks  20
  NA           forward  NA packets received on trusted port              17
  NA           forward  NA packets received on untrusted port            30
  NA           drop     NA packets failed Prefix check                   15
  NA           drop     NA packets failed on max-binding limit           2
  NA           drop     NA packets failed ND snooping validation checks  5

Chapter 7 ND snooping

87

Chapter 8
IP tunnels

True point-to-point networks are not always possible in corporate networking environment. Many networks
deploy nontraditional methods of connection (for example, DSL or broadband) at remote sites or branch
offices. The branch office, telecommuter, or business traveler then becomes separated from the corporate
network. Some method of tunneling becomes imperative to connect all the network sites together.

Virtual Private Networking (VPN) is often deployed to create private tunnels through the public network
system for passing data to remote sites. While VPN is sufficient for the average business traveler, it is not a
good solution for branch site connectivity. VPN configurations must include statically maintained access lists
to identify traffic through the tunnel. These access lists are often tedious to configure for larger networks
and are prone to errors.

VPNs do not permit multicast traffic to pass; therefore routing protocols such as Routing Information
Protocol (RIP) and Open Shortest Path First (OSPF) are no longer options for dynamic routing updates. All
new additions to the network topology must be manually added to the various configured access lists.
Without dynamic routing from one site to another, network management is severely hampered. Network
managers need their non-heterogeneous networks to function like traditional point-to-point networks so
that traditional management methods (once available only on point-to-point circuits) can apply to the entire
network.

The solution to these challenges is to use IP tunnels. An IP tunnel provides a virtual link between endpoints
on two different networks enabling data to be exchanged as if the endpoints were directly connected on the
same network. Traffic between the devices is isolated from the intervening networks that the tunnel spans.

IP tunnels supported features

Up to 127 tunnels can be defined on a switch shared between different tunnel types.

Unsupported features

• Key support can be added for security and identification purposes when there are multiple applications.

• VPN across public IP network.

Configuring an IP tunnel

Prerequisites

An enabled layer 3 interface with an IP address assigned to it, created with the command interface.

Procedure

1. Create an IP tunnel with the command interface tunnel .

2. Set the IP address for the tunnel. For an IPv6 in IPv4 or an IPv6 in IPv6 tunnel, enter the command ipv6

address.

3. Set the source IP address for the tunnel. For an IPv6 in IPv4 tunnel, enter the command source ip. For

an IPv6 in IPv6 tunnel, enter the command source ipv6.

4. Set the destination IP address for the tunnel. For an IPv6 in IPv4 tunnel, enter the command
destination ip . For an IPv6 in IPv6 tunnel, enter the command destination ipv6.

88

AOS-CX 10.06 IP Services Guide

5. Optionally, set the TTL (hop count) for the tunnel with the command ttl.

6. Optionally, set the MTU for the tunnel with the command ip mtu.

7. Optionally, add a description to the tunnel with the command description.

8. Enable the tunnel with the command no shutdown.

9. Review tunnel settings with the command show interface tunnel.

Creating an IPv6 in IPv4 tunnel for traversing a public
network
This example creates an IPv6 in IPv4 tunnel between two switches, enabling traffic from two networks to
traverse a public network.

Procedure

1. On switch 1:

a. Enable interface 1/1/1 and assign the IP address 10.1.1.1/24 to it.

switch# config
switch(config)# interface 1/1/1
switch(config-if)# ip address 10.1.1.1/24
switch(config-if)# no shutdown

b. Enable interface 1/1/2 and assign the IP address 2080::2/64 to it.

switch# config
switch(config)# interface 1/1/2
switch(config-if)# ipv6 address 2080::2/64
switch(config-if)# no shutdown
switch(config-if)# exit

Chapter 8 IP tunnels

89

c. Create IPv6 in IPv4 tunnel 10 and assign the IP address 2001:DB8::1/32, source address 10.1.1.1,

and destination address 20.1.1.1 to it.

switch(config)# interface tunnel 10 mode ip 6in4
switch(config-ip-if)# ipv6 address 2001:DB8::1/62
switch(config-ip-if)# source ip 10.1.1.1
switch(config-ip-if)# destination ip 20.1.1.1
switch(config-ip-if)# no shutdown
switch(config-ip-if)# exit

d. Defines routes so that traffic from network 1 can reach network 2 through the tunnel.

switch(config)# ip route 20.1.1.0/24 10.1.1.2
switch(config)# ipv6 route 290::0/64 tunnel10

2. On switch 2:

a. Enable interface 1/1/1 and assign the IP address 20.1.1.1/24 to it.

switch# config
switch(config)# interface 1/1/1
switch(config-if)# ip address 20.1.1.1/24
switch(config-if)# no shutdown

b. Enable interface 1/1/2 and assign the IP address 2090::2/64 to it.

switch(config)# interface 1/1/2
switch(config-if)# ipv6 address 2090::2/64
switch(config-if)# no shutdown
switch(config-if)# exit

c. Create IPv6 in IPv4 tunnel 10 and assign the IP address 2001:DB8::2/32, source address 10.1.1.1,

and destination address 20.1.1.1 to it.

switch(config)# interface tunnel 10 mode ip 6in4
switch(config-ip-if)# ipv6 address 2001:DB8::2/62
switch(config-ip-if)# source ip 20.1.1.1
switch(config-ip-if)# destination ip 10.1.1.1
switch(config-ip-if)# no shutdown
switch(config-ip-if)# exit

d. Defines routes so that traffic from network 2 can reach network 1 through the tunnel.

switch(config)# ip route 10.1.1.0/24 20.1.1.2
switch(config)# ip route 2080::0/64 tunnel10

Creating an IPv6 in IPv6 tunnel for traversing a public
network
This example creates an IPv6 in IPv6 tunnel between two switches, enabling traffic from two networks to
traverse a public network.

90

AOS-CX 10.06 IP Services Guide

Procedure

1. On switch 1:

a. Enable interface 1/1/1 and assign the IP address 2001:DB8:5::1/64 to it.

switch# config
switch(config)# interface 1/1/1

switch(config-if)# ipv6 address 2001:DB8:5::1/64
switch(config-if)# no shutdown

b. Enable interface 1/1/2 and assign the IP address 2080::2/64 to it.

switch# config
switch(config)# interface 1/1/2
switch(config-if)# ipv6 address 2080::2/64
switch(config-if)# no shutdown
switch(config-if)# exit

c. Create IPv6 in IPv6 tunnel 10 and assign the IP address 2001:DB8::1/32, source address

2001:DB8:5::1, and destination address 2001:DB8:9::1 to it. (Optional) Set the MTU and TTL
parameters for this tunnel interface.

switch(config)# interface tunnel 10 mode ip 6in6
switch(config-ip-if)# ipv6 address 2001:DB8::1/62
switch(config-ip-if)# source ipv6 2001:DB8:5::1
switch(config-ip-if)# destination ipv6 2001:DB8:9::1
switch(config-ip-if)# no shutdown
switch(config-ip-if)# exit

d. Defines routes so that traffic from network 1 can reach network 2 through the tunnel.

switch(config)# ipv6 route 2001:DB8:9::0/64 2001:DB8:5::2
switch(config)# ipv6 route 2090::0/64 tunnel10

2. On switch 2:

Chapter 8 IP tunnels

91

a. Enable interface 1/1/1 and assign the IP address 2001:DB8:9::1/64 to it.

switch# config
switch(config)# interface 1/1/1
switch(config-if)# ipv6 address 2001:DB8:9::1/64
switch(config-if)# no shutdown

b. Enable interface 1/1/2 and assign the IP address 2090::2/64 to it.

switch(config)# interface 1/1/2
switch(config-if)# ipv6 address 2090::2/64
switch(config-if)# no shutdown
switch(config-if)# exit

c. Create IPv6 in IPv6 tunnel 10 and assign the IP address 2001:DB8::2/32, source address

2001:DB8:5::1, and destination address 2001:DB8:9::1 to it. (Optional) Set the MTU and TTL
parameters for this tunnel interface.

switch(config)# interface tunnel 10 mode ip 6in6
switch(config-ip-if)# ipv6 address 2001:DB8::2/62
switch(config-ip-if)# source ipv6 2001:DB8:9::1
switch(config-ip-if)# destination ipv6 2001:DB8:5::1
switch(config-ip-if)# no shutdown
switch(config-ip-if)# exit

d. Defines routes so that traffic from network 2 can reach network 1 through the tunnel.

switch(config)# ipv6 route 2001:DB8:5::0/64 2001:DB8:9::2
switch(config)# ipv6 route 2080::0/64 tunnel10

IP tunnels commands

description

Syntax

description <DESC>

no description

Description

Associates a text description with an IP tunnel for identification purposes.

The no form of this command removes the description from an IP tunnel.

Command context

config-ip-if

Parameters
<DESC>

Specifies the descriptive text to associate with the IP tunnel. Range: 1 to 64 printable ASCII characters.

Authority

Administrators or local user group members with execution rights for this command.

92

AOS-CX 10.06 IP Services Guide

Examples

Defines a description for IPv6 in IPv4 tunnel 27.

switch(config)# interface tunnel 27 mode ip 6in4
switch(config-ip-if)# description Network 3 Tunnel 27

Removes the description for IPv6 in IPv4 tunnel 27.

switch(config)# interface tunnel 27
switch(config-ip-if)# no description

Defines a description for IPv6 in IPv6 tunnel 8.

switch(config)# interface tunnel 8 mode ip 6in6
switch(config-ip-if)# description Network 4 Tunnel 8

Removes the description for IPv6 in IPv6 tunnel 8.

switch(config)# interface tunnel 8
switch(config-ip-if)# no description

destination ip

Syntax

destination ip <IPV4-ADDR>

no destination ip <IPV4-ADDR>

Description

Sets the destination IP address for an IP tunnel. Specify the address of the interface on the remote device to
which the tunnel will be established.

The no form of this command deletes the destination IP address from an IP tunnel.

Command context

config-gre-if

config-ip-if

Parameters
<IPV4-ADDR>

Specifies the destination IP address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to
255.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines the destination IP address to be 10.10.20.1 for IPv6 in IPv4 tunnel 27.

switch(config)# interface tunnel 27 mode ip 6in4
switch(config-ip-if)# destination ip 10.10.20.1

Deletes the destination IP address 10.10.20.1 from IPv6 in IPv4 tunnel 27.

Chapter 8 IP tunnels

93

switch(config)# interface tunnel 27
 switch(config-ip-if)# no destination ip 10.10.20.1

destination ipv6

Syntax

destination ipv6 <IPVv6-ADDR>

no destination ipv6 <IPV6-ADDR>

Description

Sets the destination IPv6 address for an IP tunnel. Specify the address of the interface on the remote device
to which the tunnel will be established.

The no form of this command deletes the destination IPv6 address from an IP tunnel.

Command context

config-ip-if

Parameters
<IPV6-ADDR>

Specifies the tunnel IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where
x is a hexadecimal number from 0 to F.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines the destination IPv6 address to be 2001:DB8::1 for IPv6 in IPv6 tunnel .

switch(config)# interface tunnel 8 mode ip 6in6
switch(config-ip-if)# destination ipv6 2001:DB8::1

Deletes the destination IPv6 address 2001:DB8::1 from IPv6 in IPv6 tunnel 8.

switch(config)# interface tunnel 8
 switch(config-ip-if)# no destination ipv6 2001:DB8::1

interface tunnel

Syntax

interface tunnel <TUNNEL-NUMBER> mode {gre ipv4 | ip 6in4 | ip 6in6}

interface tunnel <EXISTING-TUNNEL-NUMBER>

no interface tunnel <EXISTING-TUNNEL-NUMBER>

Description

Creates or updates an IP tunnel. After you enter the command, the firmware switches to the configuration
context for the tunnel.

If the specified tunnel exists, this command switches to the context for the tunnel.

By default, all tunnels are automatically assigned to the default VRF when they are created.

94

AOS-CX 10.06 IP Services Guide

The no form of this command deletes an existing IP tunnel.

Command context

config

Parameters
mode {gre ipv4 | ip 6in4 | ip 6in6}

Creates an IP tunnel. Choose one of the following options:

• ip 6in4: Creates an IPv4 tunnel for IPv6 traffic.

• ip 6in6: Creates an IPv6 tunnel for IPv6 traffic.

<TUNNEL-NUMBER>

Specifies the number for a new tunnel. Range: 1 to 127. Numbering is shared between all tunnels, so the
same tunnel number cannot be used for an IPv6 in IPv4 tunnel and a GRE tunnel.

<EXISTING-TUNNEL-NUMBER>

Specifies the number for an existing IP tunnel. Range: 1 to 127.

Command context

config-ip-if

Examples

Defines a new IPv6 in IPv4 tunnel with number 27.

switch(config)# interface tunnel 27 mode ip 6in4
switch(config-ip-if)#

Switches to the config-ip-if context for existing tunnel 27.

switch(config)# interface tunnel 27
switch(config-ip-if)#

DeletesIPv6 in IPv4 tunnel 27.

switch(config)# no interface tunnel 27

Defines a new IPv6 in IPv6 tunnel with number 8.

switch(config)# interface tunnel 8 mode ip 6in6
switch(config-ip-if)#

ip address

Syntax

ip address <IPV4-ADDR>/<MASK>

no ip address <IPV4-ADDR>/<MASK>

Description

Sets the local IP address of a GRE tunnel. This address identifies the tunnel interface for routing. It must be
on the same subnet as the tunnel address assigned on the remote device.

The no form of this command deletes the local IP address assigned to a GRE tunnel.

Chapter 8 IP tunnels

95

Command context

config-gre-if

Parameters
<IPV4-ADDR>

Specifies the tunnel IP address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255.
You can remove leading zeros. For example, the address 192.169.005.100 becomes 192.168.5.100.

<MASK>

Specifies the number of bits in the address mask in CIDR format (x), where x is a decimal number from 0
to 32.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines the local IP address 10.10.10.1 for GRE tunnel 33.

switch(config)# interface tunnel 33 mode gre ipv4
switch(config-gre-if)# ip address 10.10.10.1/24

Deletes the local IP address 10.10.10.1 for GRE tunnel 33.

switch(config)# interface tunnel 33
switch(config-gre-if)# no ip address 10.10.10.1/24

ipv6 address

Syntax

ipv6 address <IPV6-ADDR>/<MASK>

no ipv6 address <IPV6-ADDR>/<MASK>

Description

Sets the local IP address of an IPv6 to IPv4 tunnel or of an IPv6 to IPv6 tunnel. This address identifies the
tunnel interface for routing. It must be on the same subnet as the tunnel address assigned on the remote
device.

The no form of this command deletes the local IP address assigned to an IPv6 to IPv4 tunnel.

Command context

config-ip-if

config-if

Parameters
<IPV6-ADDR>

Specifies the tunnel IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where
x is a hexadecimal number from 0 to F.

<MASK>

Specifies the number of bits in the address mask in CIDR format (x), where x is a decimal number from 0
to 32.

96

AOS-CX 10.06 IP Services Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines the local IP address 2001:DB8:5::1/64 for tunnel 8 for an IPv6 to IPv6 tunnel.

switch(config)# interface tunnel 8 mode ip 6in6
switch(config-ip-if)# ipv6 address 2001:DB8:5::1/64

Deletes the local IP address 2001:DB8::1/32 for tunnel 8.

switch(config)# interface tunnel 8
switch(config-ip-if)# no ipv6 address 2001:DB8:5::1/64

ip mtu

Syntax

ip mtu <VALUE>

Description

Sets the MTU (maximum transmission unit) for an IP interface. The default value is 1500 bytes.

The no form of this command sets the MTU to the default value of 1500 bytes.

Command context

config-ip-if

Parameters
<VALUE>

Specifies the MTU in bytes. Range: 1,280 bytes to 9,192 bytes.

Authority

Administrators or local user group members with execution rights for this command.

Usage

The IP MTU is the largest IP packet that can be sent or received by the interface. For a tunnel, the IP MTU is
the maximum size of the IP payload. To enable jumbo packet forwarding through the tunnel, set the IP MTU
of the tunnel to a value greater than 1500. Also set the MTU and the IP MTU values for the underlying
physical interface that the tunnel is using to a value greater than 1,500 bytes. The IP MTU of the tunnel must
also be greater than or equal to the MTU of the ingress interface on the switch. The IP MTU value of the
tunnel must also be less than or equal to the IP MT of the underlying interface that the tunnel is using.

Examples

Sets the MTU on IPv6 in IPv4 tunnel 27 to 1000 bytes.

switch(config)# interface tunnel 27 mode ip 6in4
switch(config-ip-if)# mtu 1000

Sets the MTU onIPv6 in IPv4 tunnel 27 to the default value.

switch(config)# interface tunnel 27 mode ip 6in4
switch(config-ip-if)# ip mtu

Chapter 8 IP tunnels

97

Sets the MTU on IPv6 in IPv6 tunnel 8 to 900 bytes.

switch(config)# interface tunnel 8 mode ip 6in6
switch(config-ip-if)# ip mtu 9000

Sets the MTU on IPv6 in IPv6 tunnel 8 to the default value.

switch(config)# interface tunnel 8 mode ip 6in6
switch(config-ip-if)# ip mtu

show interface tunnel

Syntax

show interface tunnel[<TUNNEL-NUMBER>] [vsx-peer]

Description

Shows configuration settings for all IP tunnels, or a specific tunnel.

Command context

Manager (#)

Parameters
<TUNNEL-NUMBER>

Specifies the number of an IP tunnel. Range: 1 to 127.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Shows configuration settings for tunnel 12, which is an IPv6 in IPv6 tunnel in the following example.

switch# show interface tunnel12

Interface tunnel12 is up
 Admin state is up
 tunnel type IPv6 in IPv6
 tunnel interface IPv6 address 4::1/64
 tunnel source IPv6 address 2::1
 tunnel destination IPv6 address 2::2
 tunnel ttl 60
 Description: Network2 Tunnel
RX
            0 input packets              0 bytes
            0 dropped

TX
            0 output packets             0 bytes
            0 dropped

98

AOS-CX 10.06 IP Services Guide

show running-config interface tunnel

Syntax

show running-config interface tunnel<TUNNEL-NUMBER> [vsx-peer]

Description

Shows the commands used to configure an IP tunnel.

Command context

Manager (#)

Parameters
<TUNNEL-NUMBER>

Specifies the number of an IP tunnel. Range: 1 to 127.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Shows the configuration for IPv6 in IPv4 tunnel.

switch# show running-config interface tunnel5
  interface tunnel5 mode ip 6in4
  source ip 10.10.10.12
  destination ip 22.20.20.20
  ip6 address 2001:DB8:5::1/64
  ttl 60
  no shutdown
  description Network10

Shows the configuration for IPv6 in IPv6 tunnel.

switch# show running-config interface tunnel1
  interface tunnel 1 mode ip 6in6
  description Network2 Tunnel
  source ipv6 2::1
  destination ipv6 2::2
  ipv6 address 4::1/64
  ttl 60

shutdown

Syntax

shutdown
no shutdown

Chapter 8 IP tunnels

99

Description

This command disables an IP interface. IP interfaces are disabled by default when created.

The no form of this command enables an IP interface.

Command context

config-ip-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enables IPv6 in IPv4 interface 27.

switch(config)# interface tunnel 27 mode ip 6in4
switch(config-ip-if)# no shutdown

Disables IPv6 in IPv4 interface 27.

switch(config)# interface tunnel 27 mode ip 6in4
switch(config-ip-if)# shutdown

source ip

Syntax

source ip <IPV4-ADDR>

no source ip <IPV4-ADDR>

Description

Sets the source IP address for an IP tunnel. Specify the IP address of a layer 3 interface on the switch.
Tunnels can have the same source IP address and different destination IP addresses.

The no form of this command deletes the source IP address for an IP tunnel.

Command context

config-ip-if

Parameters
<IPV4-ADDR>

Specifies the source IP address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines the source IP address to be 10.10.10.1 for IPv6 in IPv4 tunnel 27.

switch(config)# interface tunnel 27 mode ip 6in4
switch(config-ip-if)# source ip 10.10.10.1

Deletes the source IP address 10.1.10.1 from IPv6 in IPv4 tunnel 27.

100

AOS-CX 10.06 IP Services Guide

switch(config)# interface tunnel 27
 switch(config-ip-if)# no source ip 10.10.10.1

source ipv6

Syntax

source ipv6 <IPV6-ADDR>

no source ipv6

Description

Sets the source IPv6 address to be used for the encapsulation.

The no form of this command deletes the source IPv6 address for an IP tunnel.

Command context

config-ip-if

Parameters
<IPV6-ADDR>

Specifies the tunnel IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where
x is a hexadecimal number from 0 to F.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines the source IPv6 address to be 2001:DB8::1 for IPv6 in IPv6 tunnel 8.

switch(config)# interface tunnel 8 mode ip 6in6
switch(config-ip-if)# source ipv6 2001:DB8::1

Deletes the source IP address 2001:DB8::1 from IPv6 in IPv6 tunnel 8.

switch(config)# interface tunnel 8
switch(config-ip-if)# no source ipv6 2001:DB8::1

ttl

Syntax

ttl <COUNT>

no ttl

Description

Sets the TTL (time-to-live), also known as the hop count, for tunneled packets. If not configured, the default
value of 64 is used for the tunnel. (The hop count of the original packets is not changed.) A maximum of four
different TTL values can be used at the same time by all tunnels on the switch. For example, if tunnel-1 has
TTL 10, tunnel-2 has TTL 20, tunnel-3 has TTL 30, and tunnel-4 has TTL 40, then tunnel-5 cannot have a
unique TTL value, it must reuse one of the values assigned to the other tunnels (10, 20, 30, 40).

The no form of this command sets TTL to the default value of 64.

Chapter 8 IP tunnels

101

Command context

config-ip-if

Parameters
<COUNT>

Specifies the hop count. Range: 1 to 255. Default: 64.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines a TTL of 55 for IPv6 in IPv4 tunnel 27.

switch(config)# interface tunnel 27 mode ip 6in4
switch(config-ip-if)# ttl 55

Sets the TTL for IPv6 in IPv4 tunnel 27 to the default value of 64.

switch(config)# interface tunnel 27
switch(config-ip-if)# no ttl

102

AOS-CX 10.06 IP Services Guide

Chapter 9
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

Chapter 9 Internet Control Message Protocol (ICMP)

103

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

Enables the sending of ICMPv4 and ICMPv6 redirect messages to the source host. Enabled by default. ICMP
redirect and active forwarding are mutually exclusive.

The no form of this command disables ICMPv4 and ICMPv6 redirect messages to the source host.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

104

AOS-CX 10.06 IP Services Guide

Examples

Enabling ICMP redirect messages:

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

Chapter 9 Internet Control Message Protocol (ICMP)

105

The no form of this command disables the sending of ICMPv4 and ICMPv6 destination unreachable
messages from the switch to a source host when a specific host is unreachable. This command does not
prevent other hosts from sending an ICMP unreachable message.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ICMPv4 and ICMPv6 destination unreachable messages to a source host:

switch(config)# ip icmp unreachable

Disabling ICMPv4 and ICMPv6 destination unreachable messages to a source host:

switch(config)# no ip icmp unreachable

106

AOS-CX 10.06 IP Services Guide

Chapter 10
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

Chapter 10 DNS

107

• Defines a static DNS host named myhost1 with an IPv4 address of 3.3.3.3.

• DNS client traffic is sent on the default VRF (named default).

switch(config)# ip dns domain-name switch.com
switch(config)# ip dns server-address 1.1.1.1
switch(config)# ip dns host myhost1 3.3.3.3
switch(config)# exit
switch# show ip dns

VRF Name : vrf_mgmt

Host Name                                                        Address
--------------------------------------------------------------------------------

VRF Name : vrf_default
Domain Name : switch.com
DNS Domain list :
Name Server(s) : 1.1.1.1

Host Name                                                        Address
--------------------------------------------------------------------------------
myhost1

DNS client commands

ip dns domain-list

Syntax

ip dns domain-list <DOMAIN-NAME> [vrf <VRF-NAME>]

no ip dns domain-list <DOMAIN-NAME> [vrf <VRF-NAME>]

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

vrf <VRF-NAME>

Specifies a VRF name. Default: default.

Authority

Administrators or local user group members with execution rights for this command.

108

AOS-CX 10.06 IP Services Guide

Examples

This example defines a list with two entries: domain1.com and domain2.com.

switch(config)# ip dns domain-list domain1.com
switch(config)# ip dns domain-list domain2.com

This example removes the entry domain1.com.

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

Chapter 10 DNS

109

Description

Associates a static IP address with a hostname. The DNS client returns this IP address instead of querying a
DNS server for an IP address for the hostname. Up to six hosts can be defined. If no VRF is defined, the
default VRF is used.

The no form of this command removes a static IP address associated with a hostname.

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

110

AOS-CX 10.06 IP Services Guide

Parameters
<IP-ADDR>

Specifies an IP address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255, or IPv6
format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a hexadecimal number from 0 to
F.

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

switch(config)# ip dns domain-name domain.com
switch(config)# ip dns domain-list domain5.com

Chapter 10 DNS

111

switch(config)# ip dns domain-list domain8.com
switch(config)# ip dns server-address 4.4.4.4
switch(config)# ip dns server-address 6.6.6.6
switch(config)# ip dns host host3 5.5.5.5
switch(config)# ip dns host host3 c::12

switch# show ip dns
VRF Name : default

Domain Name : domain.com
DNS Domain list : domain5.com, domain8.com
Name Server(s) : 4.4.4.4, 6.6.6.6

Host Name    Address
-------------------------------
host3            5.5.5.5
host3            c::12

112

AOS-CX 10.06 IP Services Guide

Chapter 11
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

Chapter 11 ARP

113

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

Configuring proxy ARP

Procedure

1. Switch to configuration context with the command config.

2. Switch to an interface VLAN with the command interface vlan.

3. Enable local proxy ARP with the command ip proxy-arp.

Examples

This example configures proxy ARP on interface VLAN 30.

switch# config
switch(config)# interface vlan 30
switch(config-vlan-30)# ip proxy-arp

Configuring local proxy ARP

Procedure

1. Switch to configuration context with the command config.

2. Switch to an interface VLAN with the command interface vlan.

3. Enable local proxy ARP with the command ip local-proxy-arp.

Examples

114

AOS-CX 10.06 IP Services Guide

This example configures local proxy ARP on interface VLAN 30.

switch# config
switch(config)# interface vlan 30
switch(config-vlan-30)# ip local-proxy-arp

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

•

Limit the amount of ARP activity allowed from a host or on a port.

• Ensure that all ARP packets are consistent with one or more binding databases, which can be created

through various means.

• Enforce integrity checks on the ARP packets to check against different MAC or IP addresses in the

Ethernet or IP header and ARP header.

This release implements Dynamic ARP Inspection to enforce DHCP snooping binding on all ARP packets and
is supported on the 6300, 6400, and 8400 platforms. The feature will be disabled from the code, CLI, and
schema by the use of appropriate config flags for other platforms.

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

Chapter 11 ARP

115

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

116

AOS-CX 10.06 IP Services Guide

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

Chapter 11 ARP

117

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

Parameters
port <PORT-ID>

Specifies a physical port on the switch. Format: member/slot/port. For example: 1/1/1. .

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

switch# clear arp 1/1/35

ip local-proxy-arp

Syntax

ip local-proxy-arp

no ip local-proxy-arp

118

AOS-CX 10.06 IP Services Guide

Description

Enables local proxy ARP on the specified interface. Local proxy ARP is supported on Layer 3 physical
interfaces and on VLAN interfaces. To enable local proxy ARP on an interface, routing must be enabled on
that interface.

The no form of this command disables local proxy ARP on the specified interface.

Command context

config-if

config-if-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling local proxy ARP on interface 1/1/1:

switch# interface 1/1/1
switch(config-if)# ip local proxy-arp

Enabling local proxy ARP on interface VLAN 3:

switch# interface vlan 3
switch(config-if-vlan)# ip local-proxy-arp

Disabling local proxy ARP on on interface 1/1/1.

switch# interface 1/1/1
switch(config-if)# no ip local-proxy-arp

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

Chapter 11 ARP

119

Authority

Administrators or local user group members with execution rights for this command.

Example

Creates a static ARP entry on interface 1/1/1.

switch(config)# interface 1/1/1
switch(config-if)# arp ipv6 neighbor 2001:0db8:85a3::8a2e:0370:7334 mac 00:50:56:96:df:c8

ip proxy-arp

Syntax

ip proxy-arp

no ip proxy-arp

Description

Enables proxy ARP for the specified Layer 3 interface. Proxy ARP is supported on Layer 3 physical interfaces,
LAG interfaces, and VLAN interfaces. It is disabled by default. To enable proxy ARP on an interface, routing
must be enabled on that interface.

The no form of this command disables proxy ARP for the specified interface.

Command context

config-if

config-if-vlan

config-lag-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling proxy ARP on interface 1/1/1:

switch# interface 1/1/1
switch(config-if)# ip proxy-arp

Enabling proxy ARP on VLAN 3:

switch# interface vlan 3
switch(config-if-vlan)# ip proxy-arp

Enabling proxy ARP on a LAG 11:

switch(config)# int lag 11
switch(config-lag-if)# ip proxy-arp

Disabling proxy ARP on interface 1/1/1:

switch# interface 1/1/1
switch(config-if)# no ip proxy-arp

120

AOS-CX 10.06 IP Services Guide

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

Chapter 11 ARP

121

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

122

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

Chapter 11 ARP

123

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

124

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

Specifies a physical port, VLAN, or LAG on the switch. For physical ports, use the format member/slot/
port (for example, 1/3/1).

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Chapter 11 ARP

125

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing ARP timeout information for a VLAN:

switch# show arp timeout vlan4

Showing ARP timeout information for a port:

switch# show arp timeout 1/1/1
ARP Timeout:

------------------

Port             VRF                              Timeout

1/1/1            default                          600

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

126

AOS-CX 10.06 IP Services Guide

IPv4 Address    MAC                Port    Physical Port  State      VRF
10.20.30.40     00:50:56:bd:6a:c5  1/1/29  1/1/29         reachable  test
-------------------------------------------------------
Total Number Of ARP Entries Listed: 1.
-------------------------------------------------------

switch# show arp all-vrfs
ARP IPv4 Entries:
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

Chapter 11 ARP

127

Examples

switch# show ipv6 neighbors
IPv6 Entries:

-------------------------------------------------------

IPv6 Address                 MAC                Port      Physical Port  State

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

128

AOS-CX 10.06 IP Services Guide

ARP cache entries are in the stale state if the elapsed time is in excess of the ARP timeout in seconds
since the last positive confirmation that the forwarding path was functioning properly.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

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

Chapter 11 ARP

129

Chapter 12
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

130

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

Chapter 12 Support and other resources

131

