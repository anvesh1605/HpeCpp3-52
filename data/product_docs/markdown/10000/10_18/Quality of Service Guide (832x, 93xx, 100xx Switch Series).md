AOS-CX 10.18.xxxx Quality of Service Guide (832x, 93xx, 100xx
Switch Series)

Published: May 2026

AOS-CX 10.18.xxxx Quality of Service Guide (832x, 93xx, 100xx
Switch Series)

Published: May 2026

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

AOS-CX 10.18.xxxx Quality of Service Guide (832x, ...

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
8
.
x
x
x
x

Q
u
a
l
i
t
y

o
f

S
e
r
v
i
c
e

G
u
i
d
e

(
8
3
2
x
,

.
.
.

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX 10.18.xxxx Quality of Service Guide (832x, ...

Table of contents

About this document..................................................................................................................................................................................8

Applicable products........................................................................................................................................................................8

Latest version available online.................................................................................................................................................8

Command syntax notation conventions.............................................................................................................................9

About the examples.................................................................................................................................................................... 10

Identifying switch ports and interfaces........................................................................................................................... 10

QoS overview............................................................................................................................................................................................... 11

End-to-end QoS behavior........................................................................................................................................................11

Best effort service............................................................................................................................................................12

Class of Service................................................................................................................................................................. 12

Differentiated services..................................................................................................................................................13

QoS on the switch.........................................................................................................................................................................14

QoS trust...............................................................................................................................................................................16

Dynamic QoS trust mode................................................................................................................................18

Port rate limiting...............................................................................................................................................................18

Queue profiles....................................................................................................................................................................18

Schedule profiles.............................................................................................................................................................. 20

Egress queue shaping................................................................................................................................................... 22

Egress port shaping........................................................................................................................................................22

Active Queue Management........................................................................................................................................22

Explicit Congestion Notification (ECN)..................................................................................................23

Weighted Random Early Detection (WRED)....................................................................................... 23

Threshold profiles...............................................................................................................................................23

Queue Monitoring............................................................................................................................................................23

Congestion Event Detection.........................................................................................................................24

Terms...................................................................................................................................................................................... 24

QoS configuration......................................................................................................................................................................................26

Configuring QoS ...........................................................................................................................................................................26

Configuring expedited forwarding for VoIP traffic....................................................................................................31

Configuring rate limiting...........................................................................................................................................................32

Configuring egress queue shaping.....................................................................................................................................34

Configuring egress port shaping......................................................................................................................................... 35

Configuring threshold profiles.............................................................................................................................................. 37

Monitoring queue operation...................................................................................................................................................38

Public

Table of contents 4

Data center bridging for storage and lossless Ethernet..................................................................................................... 40

Data center bridging components...................................................................................................................................... 40

PFC - Priority-based flow control........................................................................................................................... 41

ETS - Enhanced transmission selection..............................................................................................................41

QCN - Quantized congestion notification..........................................................................................................42

DCBx - Data center bridging exchange protocol...........................................................................................42

DCBx guidelines...................................................................................................................................................42

IP ECN.....................................................................................................................................................................................43

Host network interface cards.................................................................................................................................................43

DCB layer 3 configuration task list..................................................................................................................................... 45

DCBx configuration......................................................................................................................................................................46

DCBx configuration considerations.......................................................................................................................46

Enabling DCBx...................................................................................................................................................................47

Priority-based flow control......................................................................................................................................................48

PFC and the QoS pool................................................................................................................................................... 49

Asymmetric PFC............................................................................................................................................................... 50

Configurable flow control buffer thresholds.................................................................................................... 51

XOFF thresholds.................................................................................................................................................. 51

Dynamic XOFF thresholds................................................................................................................ 52

Static XOFF thresholds....................................................................................................................... 52

XON delta.................................................................................................................................................................52

Headroom size......................................................................................................................................................52

Headroom limit........................................................................................................................................53

Cable length value................................................................................................................................. 53

Cable length auto...................................................................................................................................53

Cable length default............................................................................................................................. 53

Configurable port QoS counters..............................................................................................................................54

RoCEv2 protocol counters............................................................................................................................. 54

ECN Counters........................................................................................................................................................ 56

Considerations and prerequisites...........................................................................................................................57

QoS queue profile......................................................................................................................................................................... 57

QoS queue profile configuration............................................................................................................................. 59

QoS schedule profile - enhanced transmission selection...................................................................................... 60

DWRR Calculation............................................................................................................................................................61

QoS schedule profile configuration....................................................................................................................... 62

Overriding the global schedule profile on an interface..............................................................................63

IP explicit congestion notification.......................................................................................................................................66

IP ECN configuration considerations....................................................................................................................69

Public

Table of contents 5

IP ECN configuration procedure..............................................................................................................................69

Lossless QoS pool.........................................................................................................................................................................70

Considerations and prerequisites...........................................................................................................................71

QoS pool configuration.................................................................................................................................................71

QoS trust............................................................................................................................................................................................73

Layer 3 CoS-DSCP markings.....................................................................................................................................74

Verifying trust settings.................................................................................................................................................75

Troubleshooting data center bridging..............................................................................................................................75

QoS commands........................................................................................................................................................................................... 78

apply qos threshold-profile ................................................................................................................................................... 80

clear queue-monitor interface ..............................................................................................................................................81

dcbx application ........................................................................................................................................................................... 83

dwrr queue ...................................................................................................................................................................................... 85

flow-control buffer cable-length .........................................................................................................................................87

forwarding-mode ......................................................................................................................................................................... 89

lldp dcbx disable .......................................................................................................................................................................... 90

lldp dcbx (per interface) ..........................................................................................................................................................91

lldp dcbx (global) .........................................................................................................................................................................93

map queue .......................................................................................................................................................................................94

name queue .................................................................................................................................................................................... 97

qos cos-map ....................................................................................................................................................................................98

qos dscp-map ............................................................................................................................................................................. 100

qos dscp .........................................................................................................................................................................................104

qos egress-rewrite ................................................................................................................................................................... 105

qos egress-rewrite-map ........................................................................................................................................................107

qos pool ..........................................................................................................................................................................................109

qos queue-profile ..................................................................................................................................................................... 112

qos schedule-profile ............................................................................................................................................................... 113

qos shape ...................................................................................................................................................................................... 115

qos threshold-profile .............................................................................................................................................................. 117

qos trust .........................................................................................................................................................................................119

queue action ................................................................................................................................................................................122

queue-monitor ........................................................................................................................................................................... 125

queue-monitor polling-interval seconds .....................................................................................................................127

rate-limit ........................................................................................................................................................................................ 128

show dcbx interface ................................................................................................................................................................ 131

show forwarding-mode ......................................................................................................................................................... 137

show interface qos ...................................................................................................................................................................138

Public

Table of contents 6

show interface qos buffers ..................................................................................................................................................143

show interface queues ...........................................................................................................................................................146

show interface queue-monitor ..........................................................................................................................................148

show interface queue-monitor status ...........................................................................................................................153

show qos cos-map ....................................................................................................................................................................156

show qos dscp-map ................................................................................................................................................................ 157

show qos egress-rewrite-map............................................................................................................................................159

show qos pool .............................................................................................................................................................................161

show qos queue-profile ........................................................................................................................................................ 164

show qos schedule-profile ...................................................................................................................................................166

show qos threshold-profile ................................................................................................................................................. 168

show qos trust ............................................................................................................................................................................171

show queue-monitor status ................................................................................................................................................172

strict queue .................................................................................................................................................................................. 174

Feature and Proactive Troubleshooting....................................................................................................................................176

troubleshoot qos .......................................................................................................................................................................177

Support and Other Resources.........................................................................................................................................................178

Accessing HPE Aruba Networking Support...............................................................................................................179

Accessing Updates....................................................................................................................................................................180

Warranty Information.............................................................................................................................................................. 180

Regulatory Information.......................................................................................................................................................... 181

Documentation Feedback.....................................................................................................................................................181

Public

Table of contents 7

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing HPE Aruba Networking switches on a network.

Subtopics

Applicable products
Latest version available online
Command syntax notation conventions
About the examples
Identifying switch ports and interfaces

Applicable products

This document applies to the following products:

•  HPE Aruba Networking 8320 Switch Series (JL479A, JL579A, JL581A)

•  HPE Aruba Networking 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

•  HPE Aruba Networking 8325H Switch Series (S4B20A, S4B21A, S4B22A, S4B23A, S2T42A, S2T46A,

S2T47A, S2T48A)

•  HPE Aruba Networking 8325P Switch Series (S0G12A, S4A48A)

•  HPE Aruba Networking 9300 Switch Series (R9A29A, R9A30A, R8Z96A, S0F81A, S0F82A, S0F83A)

•  HPE Aruba Networking 9300S Switch Series (S0F81A, S0F82A, S0F83A, S0F84A, S0F85A, S0F86A,

S0F88A, S0F95A, S0F96A)

•  HPE Aruba Networking 10000 Switch Series (R8P13A, R8P14A)

•  HPE Aruba Networking 10040 Switch Series (S4R58A, S4R59A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Public

About this document 8

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

...

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

•

•

In code and screen examples, a vertical or horizo
ntal ellipsis indicates an omission of information.
In syntax using brackets and braces, an ellipsis i
ndicates items that can be repeated. When an ite

Public

Command syntax notation conventions 9

Convention

Usage

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

Identifying switch ports and interfaces

Public

About the examples 10

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format: member/slot/port.

On the HPE Aruba Networking 8xxx, 93xx, and 10xxx Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

NOTE

If using breakout cables, the port designation changes to x:y, where x is the
physical port and y is the lane when split. For example, the logical interface
1/1/4:2 in software is associated with lane 2 on physical port 4 in slot 1 on
member 1.

QoS overview

Quality of Service (QoS) enables network administrators to customize how different types of traffic are
serviced on a network, taking into account the unique characteristics of each traffic type and its importance
within an organization's infrastructure. QoS ensures uniform and efficient traffic handling, keeping the most
important traffic moving at an acceptable speed, regardless of current bandwidth usage. It also provides
methods for administrators to control the priority settings of inbound traffic arriving at each network device.

Subtopics

End-to-end QoS behavior
QoS on the switch

End-to-end QoS behavior

The QoS settings on each network device must be aligned to achieve the desired end-to-end QoS behavior
for a network. Three service types can be used to categorize and prioritize network traffic:

•  Best Effort Service

•  Ethernet Class of Service (CoS)

•

Internet Differentiated Services (DiffServ)

Public

QoS overview 11

For a network as a whole, it is best to select one service type to use as the primary end-to-end behavior, and
then use the other two service types as needed.
Subtopics
Best effort service
Class of Service
Differentiated services

Best effort service
This is the simplest service type. All traffic is treated equally in a first-come, first-served manner. If
the traffic load is low in relation to the capacity of the network links, then there is no need for the
administrative complexity and costs of maintaining a more complex end-to-end policy. This is sometimes
called over-provisioning, as all link speeds are much higher than peak loads on the network.

Class of Service
Class of Service (CoS) is a method for classifying network traffic at layer 2 by marking 802.1Q VLAN
Ethernet frames with one of eight service classes.
| CoS |     | Traffic type           | Example protocols |     |     |
| --- | --- | ---------------------- | ----------------- | --- | --- |
| 7   |     | Network Control        | STP, PVST         |     |     |
| 6   |     | Internetwork Control   | BGP, OSPF, PIM    |     |     |
| 5   |     | Voice (<10ms latency)  | VoIP(UDP)         |     |     |
| 4   |     | Video (<100ms latency) | RTP               |     |     |
| 3   |     | Critical Applications  | SQL RPC, SNMP     |     |     |
| 2   |     | Excellent Effort       | NFS, SMB          |     |     |
| 0   |     | Best Effort            | HTTP, TELNET      |     |     |
| 1   |     | Background             | SMTP, IMAP        |     |     |
CoS 1 is deliberately set as the lowest CoS. This enables a traffic service level below the default (best effort)
traffic level to be specified.
|     | Public |     |     | Best effort service | 12  |
| --- | ------ | --- | --- | ------------------- | --- |

The 3-bit Priority Code Point (PCP) field within the 16-bit Ethernet VLAN tag is used to mark the CoS.

 +--------+--------+--------+----------+-----------+--------
 | mac-da | mac-sa | 0x8100 | VLAN tag | ethertype | data...
 +--------+--------+--------+----------+-----------+--------
                           /            \
                          /              \
                         /                \
                      +-----+-----+---------+
                      | pcp | dei | vlan_id |
                      +-----+-----+---------+

Differentiated services
Differentiated services (DiffServ) is a method for classifying network traffic at layer 3 by marking packets
with one of 64 different service classes. Services classes are identified by the Differentiated services Code
Point (DSCP) value. Some common DSCP values are:
| DSCP       | Name             | Service class           | RFC  |     |
| ---------- | ---------------- | ----------------------- | ---- | --- |
| 48         | CS6              | Network Control         | 2474 |     |
| 46         | EF               | Telephony               | 3246 |     |
| 40         | CS5              | Signaling               | 2474 |     |
| 34, 36, 38 | AF41, AF42, AF43 | Multimedia Conferencing | 2597 |     |
| 32         | CS4              | Real‐Time Interactive   | 2474 |     |
| 26, 28, 30 | AF31, AF32, AF33 | Multimedia Streaming    | 2597 |     |
| 24         | CS3              | Broadcast Video         | 2474 |     |
| 18, 20, 22 | AF21, AF22, AF23 | Low‐Latency Data        | 2597 |     |
| 16         | CS2              | OAM                     | 2474 |     |
| 00         | CS0,BE,DF        | Best Effort             | 2474 |     |
| 10, 12, 14 | AF11, AF12, AF13 | Bulk Data               | 2597 |     |
Low‐Priority Data
| 08  | CS1    |     | 3662                    |     |
| --- | ------ | --- | ----------------------- | --- |
|     | Public |     | Differentiated services | 13  |

DSCP CS1 (08) CoS 1 is deliberately set as the lowest priority. This enables a traffic service level below the
standard (best effort or default forwarding) level to be specified.

The DSCP value is carried within the IPv4 DSCP field or the upper 6-bits of the 8-bit IPv6 Traffic Class (TC)
field.

IPv4

+----+-----+----+----+---+-------+----+------+-------+------+------+-------

|ver |dscp |ecn |len |id |offset |ttl |proto |chksum |ip-sa |ip-da | data..

+----+-----+----+----+---+-------+----+------+-------+------+------+-------

   +------+-----+

   | dscp | ecn |

   +------+-----+

    \         /

     \       /

IPv6  \     /

+-----+-----+-----+-------+-------------+-----------+-------+-------

+--------

| ver | tc  | len | label | next_header

| hop_limit | ip-sa | ip-da | data...

+-----+-----+-----+-------+-------------+-----------+-------+-------

+--------

QoS on the switch

There are five key stages a packet passes through when traversing a switch: ingress, prioritization,
destination determination, egress queuing, and transmission. The following table provides an overview of
each stage, and lists the commands that can be used to configure QoS settings.

NOTE

Switches with at least 52 ports will experience negative performance if a flood
occurs where at least 42 ports are members of the same VLAN and all 52 ports
have QoS rules applied to them.

Public

QoS on the switch 14

Public

QoS on the switch 15

The following diagram shows how different packets might traverse a switch. It also shows how QoS
configuration settings apply at each stage.

Subtopics

QoS trust
Port rate limiting
Queue profiles
Schedule profiles
Egress queue shaping
Egress port shaping
Active Queue Management
Queue Monitoring
Terms

QoS trust

Traffic priorities for networks can be carried in VLAN tags, using the CoS Priority Code Point (PCP), or in
IP packet headers, using the Differentiated Services Code Point (DSCP). Whether these priorities affect how
traffic is serviced, depends on how QoS trust mode is configured on the switch. QoS trust mode specifies

Public

QoS trust 16

how the switch assigns local priority values to ingress packets. Trust mode can be set globally for all
interfaces, or individually for each interface. By default, trust mode is set to  none , meaning that any QoS
information in the packet (CoS or DSCP) is ignored, and local priority values are assigned from the CoS map
value for code point 0. An exception to this can be configured, allowing a QoS remark to be applied to DSCP
values when trust mode is none.

When trust mode is set to CoS or DSCP, the switch translates the QoS settings in VLAN tags (for CoS), or the
DS field in an IP header (for DSCP), to local priority values on the switch. Translation is controlled by the CoS
map or DSCP map tables.

For example:

Subtopics

Dynamic QoS trust mode

Public

QoS trust 17

Dynamic QoS trust mode

The device profile feature can dynamically set the QoS trust mode on an interface based on the LLDP
information exchanged with a link partner. The device profile's trust mode temporarily overrides the static
trust mode configured for an interface. The override remains in place as long as that link partner is
connected and its link state is up. Use command  show interface IFNAME qos  to view the
current QoS trust mode for an interface.

Port rate limiting

Port rate limiting helps control undesirable traffic. Its purpose is to allow enough unicast, broadcast,
multicast, and ICMP traffic for the network to function properly, while preventing flooding and traffic storms.

Some amount of each traffic type is required for normal network operation. For example, broadcast packets
may include ARP and DHCP traffic. Video streams and certain types of network protocol packets are
multicast traffic. Unknown-unicast packets may be intended for devices whose addresses have temporarily
aged out of network forwarding caches. Configuring rate limits can help provide balance between necessary
and flooded traffic.

The amount of permitted traffic (the rate limit) can be specified inpackets-per-second (pps) or as a
percentage of link bandwidth (percent).

Please note that rate limits are enforced separately on each individual member of a LAG, not on the LAG as
a whole. When limits are configured in packets-per-second (pps), larger limits may be needed on high speed
ports in order to allow normal network functionality. A limit of 100 packets- per-second might be reasonable
on a 1 Gigabit port, however would be too restrictive on a port that is 10 Gigabits or faster. Conversely, limits
configured as a percentage of link bandwidth may not be useful on high speed ports. A limit of 1 percent
might be reasonable on a 1 Gigabit port, but too lax on a port that is 10 Gigabits or faster.

Queue profiles

A queue profile defines the queues that are associated with an interface to control the transmission of
packets. Each profile supports up to eight queues, numbered 0 to 7. The larger the queue number, the
higher its priority during transmission scheduling. Packets are assigned to a queue based on their local
priority value (0 to 7). A queue profile must map all eight local priority values to whatever queues are being
used on the switch, and a schedule profile must specify the configuration for those same queues. A queue
without a local priority value assigned to it is not used to store packets.

The switch is automatically provisioned with an initial queue profile named factory-default which assigns
each local priority to the queue of the same number. To see the default queue profile, use the command
show qos queue-profile factory-default:

switch# show qos queue-profile factory-default

queue_num local_priorities name

--------- ---------------- ----

Public

Dynamic QoS trust mode 18

0         0                Scavenger_and_backup_data

1         1

2         2

3         3

4         4

5         5

6         6

7         7

switch# show qos queue-profile factory-default

queue_num cos         name

--------- ----------- ----

0         1           Scavenger_and_backup_data

1         0

2         2

3         3

4         4

5         5

6         6

7         7
More than one local priority value can be assigned to the same queue. For example,

Local Priority

Queue

0

1

2

3

4

5

6

7

0

1

2

3

4

5

5

5

Queues must be consecutively defined starting at queue number zero. For example, a four-queue profile with
priority values defined for queues 0, 1, 2, 3 is valid, but a four-queue profile which defines priority values for
queues 1, 3, 5, and 7 is not.

Public

Queue profiles 19

Table 1. Valid queue
Local Priority

Queue

0

1

2

3

4

5

6

7

0

1

1

1

2

2

3

3

The commonly used commands for working with QoS queues are as follows:

•  qos queue-profile: Creates an empty queue-profile and enters the profile configuration context.

•  name queue: Assigns a descriptive name to a queue.

•  map queue: Assigns a local-priority to a queue.

•  apply qos queue-profile: Applies a queue-profile globally to all interfaces.

Schedule profiles

A schedule profile determines the order in which queues are selected for transmission, and the amount of
service available for each queue. A schedule profile must be configured on every interface at all times. A
schedule profile can be applied globally to all interfaces, or only to specific interfaces.

The following options are available:

•  All queues use weighted fair queuing (WFQ)

•  All queues use strict priority

•  The highest priority queue uses strict priority, and all other queues use WFQ

•  All queues use deficit weighted round robin queuing (DWRR)

•  All queues use strict priority

Public

Schedule profiles 20

•  The highest priority queue uses strict priority, and all other queues use DWRR

•  All queues use guaranteed minimum bandwidth

•  The highest priority queue uses strict priority and all other queues use guaranteed minimum bandwidth

A weighted schedule profile assigns relative servicing for each queue. The amount of service per weight is
relative to the underlying hardware implementation, and to the weights assigned to the other non-empty
queues. Strict scheduling can be used to service queues purely on the basis of highest priority first (at
the risk of starving lower-priority queues during high stress periods). A combination of strict and weighted
scheduling offers more service to the highest priority queue when needed, while preserving scheduling
between the remaining queues, thus decreasing the risk of starvation.

The switch is automatically provisioned with a schedule profile named factory-default, which assigns DWRR
to all queues with a weight of 1. Use the command  show schedule-profile factory-defau
lt  to view the default schedule profile. (Do not use  show running-configuration , as it only
displays changes from the initial settings.)

switch# show qos schedule-profile default

queue_num algorithm weight

--------- --------- ------

0         wfq       1

1         wfq       1

2         wfq       1

3         wfq       1

4         wfq       1

5         wfq       1

6         wfq       1

7         wfq       1

switch# show qos schedule-profile default

queue_num algorithm weight

--------- --------- ------

0         dwrr      1

1         dwrr      1

2         dwrr      1
3         dwrr      1

4         dwrr      1

5         dwrr      1

6         dwrr      1

7         dwrr      1

switch# show qos schedule-profile

profile_status profile_name

-------------- ------------
applied        factory-default

complete       strict

switch# show qos schedule-profile factory-default

queue_num algorithm     percent max-bandwidth_kbps

Public

Schedule profiles 21

--------- ------------- ------- ------------------

0         min-bandwidth 2

1         min-bandwidth 3

2         min-bandwidth 30

3         min-bandwidth 10

4         min-bandwidth 10

5         min-bandwidth 10

6         min-bandwidth 15

7         min-bandwidth 20

Egress queue shaping

Egress queue shaping limits the amount of traffic transmitted per strict output and dwrr queues. The buffer
associated with each egress queue stores excess traffic to absorb bursts and smooths the output rate. For
example, an administrator might limit strict-priority or min-bandwidth queue traffic to prevent low-priority
queue starvation in the event that a device inappropriately sends too many higher-priority packets.

NOTE

Egress queue shaping applies to dwrr queue for platforms in this guide.

Egress queue shaping can be configured on an Ethernet port or on a link aggregation group (LAG). To
configure egress queue shaping, define a schedule profile with the strict priority algorithm assigned to each
queue.

Egress port shaping

Egress port shaping limits the amount of aggregate traffic transmitted through a port. To be effective, the
egress port-shaping rate must be less than the port's line rate. By default, the egress port-shaping rate
is the same as the line-rate of the port. Buffers associated with each port store excess traffic. When both
egress port-shaping and egress queue-shaping are configured on the same interface, the switch respects the
minimum of both configurations.

Active Queue Management

The following features support active queue management.

Subtopics

Explicit Congestion Notification (ECN)

Public

Egress queue shaping 22

Weighted Random Early Detection (WRED)
Threshold profiles

Explicit Congestion Notification (ECN)

Explicit Congestion Notification (ECN) provides a mechanism for two end-points to exchange end-to-end
notification of network congestion. ECN uses a 2-bit field in the IP header to indicate that the traffic load
on network equipment in the path between an ECN-capable sender and receiver is causing packets to be
buffered, as defined by IETF RFC 3168 (https://tools.ietf.org/html/rfc3168).

Weighted Random Early Detection (WRED)

WRED operates by random early-dropping packets, which can be helpful in signaling data path congestion
to certain protocols. Protocols that respond to these drops slow their transmit rate in an effort to reduce
network congestion. WRED drops are randomized in order to avoid potential synchronization between
multiple streams using the same link. If drops occurred on all streams at the same time, multiple senders
might respond by reducing their transmit rates and then increasing. Such synchronized behavior causes link
utilization to fluctuate between high and low, wasting bandwidth. Random dropping ensures that only some
streams detect drops, and that they detect them at different times. This results in better link utilization, as
some senders continue to transmit at a higher rate while others reduce and ramp up again.

Threshold profiles

Threshold profiles configure individual queue utilization thresholds as triggers for taking action (i.e., ECN
marking or WRED dropping) on a packet. A threshold profile is applied per-port and defines the thresholds
and actions for each queue. Omitting configuration for a queue in a threshold profile means that queue will
not be configured with a threshold value or action.

In an environment where responsive transport protocols are in use and congestion management features are
required to reduce latency, ECN can be configured on queues carrying delay-sensitive traffic. The result is
that queue utilization is actively managed, resulting in ECT packets being CE marked when queue utilization
reaches or exceeds a configured threshold.

Queue Monitoring

The queue monitoring feature allows the switch to collect queue statistics at specific time intervals,
then display this information as a queue statistics history. These aggregate statistics can be used to
monitor network health, troubleshoot network issues, and identify normal network behavior patterns and

Public

Explicit Congestion Notification (ECN) 23

performance anomalies. This feature is disabled by default, but can be enabled on a maximum of 52
interfaces per switch. For more information on enabling this feature, see .

Queue statistics history data can be displayed in the command-line interface as a list or a histogram
reflecting the last eight hours of queue statistics history, or as a table showing the previous five minutes of
queue statistics history.

As performance anomalies are identified, the interface queue experiencing the anomaly can further analyzed
to identify the cause of the behavior. For example, traffic patterns for flows competing for network
bandwidth can be examined to determine if corrective action is needed to address potential problems.

The queue depth of an interface changes constantly based on the arrival rate of packets destined to egress
a given queue (the queue fill rate) and the rate at which that queue is able to transmit packets (the queue
drain rate).

If no queue depth is specified, the output of the show interface queue-monitor command displays statistics
for queues with a minimum depth of one kbyte, which includes all queues which have reached a depth
greater than zero.

Subtopics

Congestion Event Detection

Congestion Event Detection

Congestion event detection is supported on 8325, 8325H, 8325P and 10000 switch series. This feature
enables users to configure queue statistics thresholds which are actively checked by the switch on
interfaces where monitoring and thresholds are applied. This mechanism leverages queue monitoring or
a Flow Congestion-Monitor as the source of periodic queue statistics samples for comparison against the
configured thresholds. If a statistic has crossed a threshold, information about the occurrence is saved within
the switch and an optional action can also be taken at the time of the occurrence. Accumulated occurrences
(events) can be viewed on the switch through the CLI or requested through the REST API interface.

Terms

Class

For networking, a set of packets sharing a common characteristic. For example, all IPv4 packets.

Code point

The name of a packet header field, or the value carried within a packet header field:

•  Example 1: Priority code point (PCP) is the name of a field in the IEEE 802.1Q VLAN tag.

•  Example 2: Differentiated services code point (DSCP) is the name of a field carried within the DS field of

an IP packet header.

Public

Congestion Event Detection 24

Color

A metadata label associated with each packet within the switch. It has three values: green (0), yellow (1),
or red (2). When packets encounter congestion for a resource (queue), the switch uses packet color to
distinguish which packets must be dropped, and is mostly used for packets marked with Assured Forwarding
(AF) DSCP values.

Not supported in this release.

Class of service (CoS)

A 3-bit value used to mark packets with one of eight classes (levels of priority). It is carried within the
priority code point (PCP) field of the IEEE 802.1Q VLAN tag.

Differentiated services code point (DSCP)

A 6-bit value used to mark packets for different per-hop behavior as originally defined by IETF RFC 2474. It
is carried within the differentiated services (DS) field of the IPv4 or IPv6 header.

Local priority

A meta-data label associated with a packet within the switch which is used to classify packets for different
treatment (such as queue assignment). Eight local priorities are defined on the switch, numbered from 0 to
7. A queue profile must map all eight local priorities to whatever queues are in use on the switch, and a
schedule profile must specify the configuration for these same queues.

Metadata

Information labels associated with each packet in the switch, separate from the packet headers and data.
These labels are used by the switch in its handling of the packet. For example: arrival port, egress port, VLAN
membership, and local priority.

Priority code point (PCP)

The name of a 3-bit field in the IEEE 802.1Q VLAN tag. It carries the CoS value to mark a packet with one of
eight classes (priority levels).

Quality of service (QoS)

General term used when describing or measuring performance. For networking, it means how different
classes of packets are treated when traversing a network or device.

Traffic class (TC)

General term for a set of packets sharing a common characteristic. It used to be the name of an 8-bit field in
the IPv6 header originally defined by IETF RFC 2460. This field name was changed to differentiated services
by IETF RFC 2474.

Type of service (ToS)

General term when there are different levels of treatment (fare class). It used to be the name of an 8-bit
field in the IPv4 header originally defined by IETF RFC 791. This field name was changed to differentiated
services by IETF RFC 2474.

Public

Terms 25

QoS configuration

Learn more about QoS behaviors on the switch

Subtopics

Configuring QoS
Configuring expedited forwarding for VoIP traffic
Configuring rate limiting
Configuring egress queue shaping
Configuring egress port shaping
Configuring threshold profiles
Monitoring queue operation

Configuring QoS

Syntax

Procedure

1.  Configure how local priority values are assigned to ingress packets with the commands  qos cos-ma

p ,  qos dscp-map , and  qos trust .

2.  Optionally, add a rate limit for ingress traffic on one or more interfaces with the command  rate-lim

it .

3.

If you do not want to use the default QoS queue profile to map local priority to queue , create one or
more custom queue profiles with the command  qos queue-profile . For each queue in a custom
queue profile:

a.  Assign a local priority value with the command  map queue .

b.  Optionally, define a descriptive name with the command  name queue . All local priorities (0 to 7)
must be mapped to a queue, and the queues selected for use must be in contiguous order starting at
0.

4.

If you do not want to use the default QoS schedule profile to determine the order in which queues are
selected to transmit a packet, create one or more custom schedule profiles with the command  qos s
chedule-profile . For each queue in a custom schedule queue profile, define scheduling priority
with the commands  strict queue  and  dwrr queue .

5.  Optionally, on 8100 or 8360 Switch Series, create a threshold profile to limit throughput on one or more
queues with the command  qos threshold-profile . Assign threshold values to the queue with

Public

QoS configuration 26

the command  queue . Then, apply the profile with the command  apply qoes threshold-pr
ofile

6.  Optionally for strict queues, configure egress queue shaping to limit egress bandwidth on an interface to
a value that is less than its line rate. Use the  max-bandwidth  parameter of the  strict queue
command.

7.  Activate QoS settings with the command  apply qos . This command lets you apply a queue profile
and schedule profile globally to all interfaces, or a schedule profile override to individual interfaces.
When applying QoS settings to a port configured to support priority-based flow control, specific
configuration settings must be respected when defining a CoS map and queue profile. See the command
flow-control in the Command-Line Interface Guide for details.

8.  View QoS configuration settings with the provided  show  commands.

Examples

This example creates the following configuration:

•  Configures CoS to be used to assign local priority to ingress packets.

•  Modifies the default CoS map to assign CoS 1 to local priority 1.

•  Creates a queue profile named  Q1  and assigns local priorities as follows:

Queue

Local Priority

0

1

1

3

4

5

5

5

0

1

2

3

4

5

6

7

Public

Configuring QoS 27

•  Creates a schedule profile named  S1  and assigns WFQ to all queues in the schedule profile with the

following weights:

Queue

Weight

0

1

3

4

5

5

10

15

25

50

•  Creates a threshold profile named  T1  with the following limits:

Queue

4

5

Threshold

40 KB

50 KB

•  Applies Q1 and S1 to all interfaces that do not have a QoS override applied.

switch(config)# qos trust cos

switch(config)# qos cos-map 1 local-priority 1

switch(config)# qos queue-profile Q1

switch(config)# map queue 0 local-priority 0

switch(config)# map queue 1 local-priority 1

switch(config)# map queue 1 local-priority 2

switch(config)# map queue 3 local-priority 3

switch(config)# map queue 4 local-priority 4

switch(config)# map queue 5 local-priority 5

switch(config)# map queue 5 local-priority 6

switch(config)# map queue 5 local-priority 7

switch(config)# qos schedule-profile S1

switch(config-schedule)# wfq queue 0 weight 5

switch(config-schedule)# wfq queue 1 weight 10

switch(config-schedule)# wfq queue 3 weight 15

switch(config-schedule)# wfq queue 4 weight 25

Public

Configuring QoS 28

switch(config-schedule)# wfq queue 5 weight 50

switch(config)# qos threshold-profile T1

switch(config-threshold)# queue 4 action ecn threshold 40 kbytes

switch(config-threshold)# queue 5 action ecn threshold 50 kbytes

switch(config-threshold)# exit

switch(config)# apply qos threshold-profile T!

switch(config)# wfq queue 5 weight 50

switch(config)# apply qos queue-profile Q1 schedule-profile S1

This example creates the following configuration:

•  Configures CoS to be used to assign local priority to ingress packets.

•  Modifies the default CoS map to assign CoS 1 to local priority 1.

•  Creates a queue profile named  Q1  and assigns local priorities as follows:

Queue

Local Priority

0

1

1

2

3

4

5

5

0

1

2

3

4

5

6

7

•  Creates a schedule profile named  S1  and assigns DWRR to all queues in the schedule profile with the

following weights:

Queue

0

Weight

5

Public

Configuring QoS 29

Queue

Weight

1

2

3

4

5

10

15

20

25

50

•  Applies Q1 and S1 to all interfaces that do not have a QoS override applied.

switch(config)# qos trust cos

switch(config)# qos cos-map 1 local-priority 1

switch(config)# qos queue-profile Q1

switch(config-queue)# map queue 0 local-priority 0

switch(config-queue)# map queue 1 local-priority 1

switch(config-queue)# map queue 1 local-priority 2

switch(config-queue)# map queue 2 local-priority 3

switch(config-queue)# map queue 3 local-priority 4

switch(config-queue)# map queue 4 local-priority 5

switch(config-queue)# map queue 5 local-priority 6

switch(config-queue)# map queue 5 local-priority 7

switch(config-queue)# qos schedule-profile S1

switch(config-schedule)# dwrr queue 0 weight 5

switch(config-schedule)# dwrr queue 1 weight 10

switch(config-schedule)# dwrr queue 2 weight 15

switch(config-schedule)# dwrr queue 3 weight 20

switch(config-schedule)# dwrr queue 4 weight 25

switch(config-schedule)# dwrr queue 5 weight 50
switch(config)# apply qos queue-profile Q1 schedule-profile S1

Queue

Minimum bandwidth (pecentage)

0

1

2

3

5

5

10

10

Public

Configuring QoS 30

Queue

Minimum bandwidth (pecentage)

4

5

6

7

20

20

10

20

Configuring expedited forwarding for VoIP traffic

Voice over IP (VoIP) traffic is delay and jitter sensitive. For optimum transmission of VoIP traffic, dwell time
in network devices must be kept to a minimum and all network devices in the data path must have identical
per-hop behaviors. To configure a dedicated queue on the switch to handle VoIP traffic with priority service
before all other queues, follow these steps.

Prerequisites

This scenario assumes that VoIP packets are uniquely identified using DiffServ code point 46, Expedited
Forwarding (EF).

Procedure

1.  Map DSCP EF packets exclusively to local priority 5 . The default DSCP map has eight code points (40
through 47), that are mapped to local priority To reserve local priority 5 for VoIP traffic, the other code
points must be reassigned. In this scenario, local priority 6 is used for all reassignments, including for
code point 40, Call Signaling protocol (CS5).

switch(config)# qos dscp-map 40 local-priority 6 name CS5

switch(config)# qos dscp-map 41 local-priority 6
switch(config)# qos dscp-map 42 local-priority 6

switch(config)# qos dscp-map 43 local-priority 6

switch(config)# qos dscp-map 44 local-priority 6

switch(config)# qos dscp-map 45 local-priority 6

switch(config)# qos dscp-map 47 local-priority 6

2.  Queue 7 is the highest priority queue, so for best throughput, create a queue profile that maps local

priority to queue 7.
switch(config)# qos queue-profile ef_priority

switch(config-queue)# name queue 7 Voice_Priority_Queue

switch(config-queue)# map queue 7 local-priority 5

Public

Configuring expedited forwarding for VoIP traffic 31

switch(config-queue)# map queue 6 local-priority 7

switch(config-queue)# map queue 5 local-priority 6

switch(config-queue)# map queue 4 local-priority 4

switch(config-queue)# map queue 3 local-priority 3

switch(config-queue)# map queue 2 local-priority 2

switch(config-queue)# map queue 1 local-priority 1

switch(config-queue)# map queue 0 local-priority 0

3.  Create a schedule profile that services queue 7 using strict priority (SP), and the remaining queues with

DWRR. This scenario gives all DWRR queues equal weight.
switch(config)# qos schedule-profile voip

switch(config-schedule)# strict queue 7

switch(config-schedule)# dwrr queue 6 weight 1

switch(config-schedule)# dwrr queue 5 weight 1

switch(config-schedule)# dwrr queue 4 weight 1

switch(config-schedule)# dwrr queue 3 weight 1

switch(config-schedule)# dwrr queue 2 weight 1

switch(config-schedule)# dwrr queue 1 weight 1

switch(config-schedule)# dwrr queue 0 weight 1

switch(config-schedule)# exit

switch(config)#

4.  Apply the profiles to all interfaces.

switch(config)# apply qos queue-profile ef_priority schedule-profile voip

5.  Configure DSCP trust mode on all ports

switch(config)# qos trust dscp

Configuring rate limiting

This scenario illustrates how to use rate limiting to manage the traffic from various devices connected to a
switch. The physical topology of the network looks like this:

Public

Configuring rate limiting 32

A certain amount of broadcast traffic is necessary to maintain healthy network operation, particularly from
routers and across service boundaries. In this scenario, both the service cloud and the router connections
limit this traffic to 1 Gbps. The server has a smaller limit, as it does not require as much network protocol
traffic as the service cloud and router.

A multicast server needs to be able to stream multicast traffic to clients, so a multicast rate limit may
not be helpful. A computer, however, should not be generating large amounts of multicast traffic (it may
be receiving streams, but typically not sending them). In this example, the computer is configured with a
multicast rate limit to prevent malicious traffic from taking up network bandwidth.

Finally, while the service cloud and router may need to send traffic for unknown unicast addresses to resolve
address forwarding, the server and computer should send very little of this type of traffic. Rate limiting
unknown unicast traffic on those two devices enforces that.

Procedure

1.  Configure broadcast and multicast rate limiting for the service cloud connection.

switch# config

switch(config)# interface 1/1/1

switch(config-if)# rate-limit broadcast 500 pps

switch(config-if)# rate-limit multicast 500 pps

switch(config-if)# exit

2.  Configure broadcast rate limiting for the router connection.

switch(config-if)# interface 1/1/2
switch(config-if)# rate-limit broadcast 500 pps

switch(config-if)# exit

Public

Configuring rate limiting 33

3.  Configure broadcast rate limiting for the server connection.

switch(config-if)# interface 1/1/5

switch(config-if)# rate-limit broadcast 100 pps

switch(config-if)# exit

4.  Configure broadcast, and multicast rate limiting for the computer connection.

switch(config-if)# interface 1/1/10

switch(config-if)# rate-limit broadcast 50 pps

switch(config-if)# rate-limit multicast 50 pps

Configuring egress queue shaping

This example shows how to apply egress queue shaping to an interface. First, a schedule profile is created
that has per-queue bandwidth limits set on all queues with  strict  as the scheduling algorithm. Next, this
profile is applied to an interface or LAG.

The following example creates a schedule profile named EQSExample, which services all queues using strict
priority. This profile configures queues 1, 4, and 7 with a bandwidth limit of 10 Gbps, 20 Gbps, and 30
Gbps respectively. Queues 1 and 7 are also configured with a burst of 30 KB (burst configuration is only
supported on the 8320, 8325, 9300, and 10000). The apply qos schedule-profile command is then used
to apply the EQSExample profile to interface 1/1/1. The actual burst and bandwidth configured on an
interface can be found by using the show interface <IF-NAME> qos command.

         switch(config)# qos schedule-profile EQSExample

switch(config-schedule)# strict queue 0

switch(config-schedule)# strict queue 1 max-bandwidth 10000000 kbps

switch(config-schedule)# strict queue 2

switch(config-schedule)# strict queue 3

switch(config-schedule)# strict queue 4 max-bandwidth 20000000 kbps

switch(config-schedule)# strict queue 5

switch(config-schedule)# strict queue 6

switch(config-schedule)# strict queue 7 max-bandwidth 30000000 kbps

switch(config-schedule)# exit

switch(config)# interface 1/1/1

Public

Configuring egress queue shaping 34

switch(config-if)# apply qos schedule-profile EQSExample

The following example creates a schedule profile named EQSExample which services all queues using
strict priority. This profile configures queues 1, 4 and 7 with a bandwidth limit of 10%, 20%, and 30% of
link bandwidth respectively. Queues 1 and 7 are also configured with a burst of 30 KB. The apply qos
schedule-profile command is then used to apply the EQSExample profile to the port. The actual burst
and bandwidth configured on an interface can be found by using the show interface < IF-NAME > qos
command.

         (config)# qos schedule-profile EQSExample

(config-schedule)# strict queue 0

(config-schedule)# strict queue 1 max-bandwidth 10 percent

(config-schedule)# strict queue 2

(config-schedule)# strict queue 3

(config-schedule)# strict queue 4 max-bandwidth 20 percent

(config-schedule)# strict queue 5

(config-schedule)# strict queue 6

(config-schedule)# strict queue 7 max-bandwidth 30 percent

Configuring egress port shaping

This example shows how to apply egress port shaping to an interface to limit the rate of egress traffic.
Egress port shaping is configured by specifying the desired bandwidth rate in kilobits per second (kbps)
or as a percentage of link bandwidth with an optional burst size in kilobytes (KB). In order to be effective,
the configured rate must be less than the link rate of the port. If the configured egress port-shaping
rate exceeds the port's link rate, then egress port shaping is effectively disabled. Egress port shapes are
enforced separately on each individual member of a LAG, not on the LAG as a whole. Because shapes are
in kilobits-per-second (kbps), larger shapes may be needed on high speed ports in order to allow normal
network function. A shape of 100 kbps might be reasonable on a 1-Gigabit port, but too restrictive on a port
that is 10-Gigabits or faster.

The configured egress rate and burst on a specific interface can be found by using the show interface and
show interface qos commands.

The following example configures an egress rate of 100 Mbps and a burst of 30 KB:

switch(config)# interface 1/1/1

switch(config-if)# qos shape 100000 kbps

Public

Configuring egress port shaping 35

burst 30

In the next example, both egress port shaping and egress queue shaping are configured on the same
interface.

The example creates a schedule profile named  EQSExample  with strict priority for all seven queues.
Queue 7 is configured with a bandwidth limit of 300 Mbps and a burst of 30 KB. The profile is then applied
to interface  1/1/1  with egress port shaping of 400 Mbps and a burst size of 30 KB. As egress queue
shaping and egress port shaping are both configured on port  1/1/1 , egress queue shaping is subject to
the lower port or queue shape rate. The effective bandwidth for the traffic egressing on queue 7 will be 300
Mbps and the effective burst will be 30 KB.

switch(config)# qos schedule-profile EQSExample

switch(config-schedule)# strict queue 0

switch(config-schedule)# strict queue 1

switch(config-schedule)# strict queue 2

switch(config-schedule)# strict queue 3

switch(config-schedule)# strict queue 4

switch(config-schedule)# strict queue 5

switch(config-schedule)# strict queue 6

switch(config-schedule)# strict queue 7 max-bandwidth 300000 kbps

             burst 30

switch(config-schedule)# exit

switch(config)# interface 1/1/1

switch(config-if)# apply qos schedule-profile EQSExample

switch(config-if)# qos shape 400000 kbps

            burst 30

Configuring an egress port shape of 10 percent and a burst of 30 KB on port 1/1/1. The configured egress
rate and burst on a specific interface can be found by using the show interface and show interface qos
commands.

switch(config)# interface 1/1/1

switch(config-if)# qos shape 10 percent

         burst 30

Public

Configuring egress port shaping 36

Configuring threshold profiles

The threshold profile is an optional configuration that specifies a per-packet action to be taken for each port
queue when the queue utilization reaches or exceeds the configured threshold. The per-queue configuration
within the threshold profile is optional, which means any number of queues may be configured. An
unconfigured queue means that no threshold action behavior will occur. Also, an empty threshold profile is
valid and can be applied.

Use the  apply qos threshold-profile <THRESHOLD-NAME>   command in the global
context to configure all ports to use the profile, or in the interface context to configure the interface to use
the profile. No threshold profiles are created or configured by default.

Each entry in a threshold profile can configure a WRED action for a particular queue and color combination.
Each entry in a threshold profile can configure an ECN action or a WRED action, either of which can take
effect depending on the contents of the packet being added to the queue. For WRED action, it is possible to
configure separate thresholds for responsive protocol packets (for example, TCP) as well as non-responsive
protocol packets (for example, UDP).

In an environment where congestion management features are required in order to reduce latency and
responsive transport protocols are in use, ECN can be configured on queues carrying delay-sensitive
traffic. The desired result is that a network device's port-queue utilization is actively managed, resulting in
ECN-capable transport (ECT) packets being Congestion Encountered (CE) marked when queue utilization
reaches or exceeds a configured threshold. Threshold profiles can be either strict or probabilistic. With a
strict threshold, the action will always occur when the threshold is exceeded. For a probabilistic profile,
minimum and maximum thresholds are set and the action starts probabilistically occurring when the
minimum threshold is crossed. The action probability increases until the maximum threshold is crossed, after
which it occurs on every packet.

Procedure

To configure one or more port queues with ECN or WRED, complete the following steps:

1.  Create a threshold profile defining one or more queue threshold configurations with an ECN or WRED

action.
(Option 1) Create a threshold profile with an ECN action on queue 7:

switch(config)# qos threshold-profile threshprofile
switch(config-threshold)# queue 7 action ecn all threshold 40 kbytes

(Option 2) Create a probabilistic threshold profile with an ECN and WRED action on queue 6:

switch(config)# qos threshold-profile threshprofile

switch(config-threshold)# queue 6 action ecn all min-threshold 40 kbytes

max-threshold 60 kbytes

switch(config-threshold)# queue 6 action wred-resp yellow min-threshold
80 kbytes max-threshold 500 kbytes max-prob 40 percent
switch(config-threshold)# queue 6 action wred-non-resp yellow min-

threshold 100 kbytes max-threshold 550 kbytes max-prob 50 percent

Public

Configuring threshold profiles 37

2.  Apply the threshold profile globally (all ports), OR apply the Threshold Profile as a port override to any

ports that require ECN or WRED behavior.
(Option 1) Apply the threshold profile as a global default (all ports):

switch(config)# apply qos threshold-profile threshprofile

(Option 2) Apply the threshold profile to specific Ethernet or LAG interfaces as a port override:

switch(config)# int 1/1/1

switch(config-if)# apply qos threshold-profile threshprofile

switch(config)# int 1/1/2

switch(config-if)# apply qos threshold-profile threshprofile

switch(config)# int lag 10

switch(config-if)# apply qos threshold-profile threshprofile

To configure one or more port queues with WRED, complete the following steps:

1.  Create a threshold profile defining one or more queue threshold configurations with a WRED action.

switch(config)# qos threshold-profile threshprofile

switch(config-threshold)# queue 6 action wred-resp yellow min-threshold

80 kbytes max-threshold 500 kbytes max-prob 40 percent

switch(config-threshold)# queue 6 action wred-non-resp yellow min-

threshold 100 kbytes max-threshold 550 kbytes max-prob 50 percent

2.  Apply the threshold profile globally (all ports), or apply the threshold profile as a port override to any

ports that require WRED behavior.
(Option 1) Apply the threshold profile as a global default (all ports):

switch(config)# apply qos threshold-profile threshprofile

(Option 2) Apply the threshold profile to specific ethernet or LAG interfaces as a port override:

switch(config)# int 1/1/1

switch(config-if)# apply qos threshold-profile threshprofile

switch(config)# int 1/1/2

switch(config-if)# apply qos threshold-profile threshprofile

switch(config)# int lag 10

switch(config-if)# apply qos threshold-profile threshprofile

Monitoring queue operation

Public

Monitoring queue operation 38

Use the show interface queues command to display the traffic transmitted per queue, and the number of
packets dropped due to the queue being full. For example:

switch# show interface 1/1/1 queues

Interface 1/1/1 is  (Administratively down)

 Admin state is down

 State information: admin_down

         Tx Packets             Tx Bytes          Tx Drops

 Q0             100                 8000                 0

 Q1         1234567          12345678908                 5

 Q2              0                     0                 0

 Q3              0                     0                 0

 Q4              0                     0                 0

 Q5              0                     0                 0

 Q6              0                     0                 0

 Q7              0                     0                 0

•  Tx Bytes: Total bytes transmitted. The byte count may include packet headers and internal metadata

that are removed before the packet is transmitted. Packet headers added when the packet is transmitted
may not be included.

•  Tx Packets: Total packets transmitted.

•  Tx Drops: The number of packets dropped by a queue before it was sent. When traffic cannot be

transmitted out of an egress interface, it may be buffered in memory if space is available. The more
servicing assigned to a queue by a schedule profile, the less likely traffic destined for that queue will
back up and potentially dropped.

switch# show interface 1/1/1 queues

Interface 1/1/1 is  (Administratively down)

 Admin state is down

 State information: admin_down

         Tx Packets             Tx Bytes          Tx Drops

 Q0             100                 8000                 0
 Q1         1234567          12345678908                 5

 Q2              0                     0                 0

 Q3              0                     0                 0

 Q4              0                     0                 0

 Q5              0                     0                 0

 Q6              0                     0                 0

 Q7              0                     0                 0

Public

Data center bridging for storage and lossless Ethe... 39

D
a
t
a

c
e
n
t
e
r

b
r
i
d
g
i
n
g

f
o
r

s
t
o
r
a
g
e

a
n
d

l
o
s
s
l
e
s
s

E
t
h
e
.
.
.

Data center bridging for storage and lossless Ethernet

NOTE

Supported on the 8325, 9300, and 10000 Switch Series.

The term lossless Ethernet is intertwined with the Data Center Bridging protocol suite (DCB) to eliminate
traffic loss within an Ethernet fabric. In a lossy fabric, traffic loss can occur due to queue buffer overflow. DCB
standards define methods for avoiding packet drops, head of line blocking, and excessive latency, which can
be applied to different priorities of traffic flowing on an interface. When these settings are applied uniformly
across an Ethernet fabric, lossless Ethernet can be achieved.

DCB achieves this by managing bandwidth, priority, and flow control of selected traffic priorities when
sharing the same Ethernet network link.

Subtopics

Data center bridging components
Host network interface cards
DCB layer 3 configuration task list
DCBx configuration
Priority-based flow control
QoS queue profile
QoS schedule profile - enhanced transmission selection
IP explicit congestion notification
Lossless QoS pool
QoS trust
Troubleshooting data center bridging

Data center bridging components

Data center bridging is comprised of the following key components:

Public

Data center bridging components 40

NOTE

IP ECN is an extension to IP supporting TCP and is covered by RFC 3168. It is a
requirement to support lossless traffic flows over L3 networks.

Subtopics

PFC - Priority-based flow control
ETS - Enhanced transmission selection
QCN - Quantized congestion notification
DCBx - Data center bridging exchange protocol
IP ECN

PFC - Priority-based flow control

Priority-based Flow Control (PFC) is a link-level flow control mechanism similar to Ethernet PAUSE and
standardized in IEEE 802.1Qbb.

The standard Ethernet PAUSE stops all traffic on an Ethernet link impacting all traffic flows. PFC PAUSE
stops only the priorities specified by the data within the pause frame, allowing other traffic priorities to
continue unaffected.

ETS - Enhanced transmission selection

Enhanced Transmission Selection (ETS) allows management of the link bandwidth by specifying bandwidth
availability to each priority group. Priorities can be grouped according to bandwidth or bandwidth allocated
to each individual priority.

Public

PFC - Priority-based flow control 41

QCN - Quantized congestion notification

Quantized Congestion Notification (QCN) provides congestion control at Layer 2. It was developed in
parallel to the related effort on PFC.

QCN is designed to provide congestion awareness to an upstream link partner, allowing the link partner to
reduce the traffic rate in order to avoid congestion on the downstream device.

NOTE

This standard is not required if the PFC feature is available and is not supported
on the CX switch platform.

DCBx - Data center bridging exchange protocol

Data Center Bridging Exchange protocol (DCBx) is a discovery and capability exchange protocol for
communicating Data Center Bridging configuration information between link peers. DCBx is specified as
part of IEEE 802.1Qaz-2011. DCBx uses LLDP as the underlying protocol for exchange of parameters with
the peer.

The DCBx parameters are exchanged as LLDP TLVs. AOS-CX switches support both pre-standard CEE and
IEEE standard DCBx.

DCBx supports VSX synchronization. For more information about enabling VSX synchronization, see the
Virtual Switching Extension (VSX) Guide for your switch and software version.

DCBx is an extension of LLDP used by DCB devices to exchange configuration information with directly
connected peers. Its applications include:

•  Discovery of peer capabilities

•  Detection of misconfigurations and identifying configuration mismatches

•  Advising a DCB peer of which DCB configurations it should adopt

Subtopics

DCBx guidelines

DCBx guidelines

•  DCBx is disabled by default.

Public

QCN - Quantized congestion notification 42

•  LLDP must be enabled on the interfaces supporting DCBx.

•  DCBx should be configured on all L2 interfaces.

•  L3 hops which leverage PFC and ECN do not require DCBx, however it is recommended to enable it.

•  DCBx is only supported on physical interfaces and not on management or logical interfaces, similar to

how LLDP behaves.

•  DCBx is not essential between host and switch but is highly desirable as to avoid manual PFC

configurations of host devices.

•  Supported protocols include:

◦  DCBx Converged Enhanced Ethernet (CEE)

◦  DCBx IEEE 802.1Qaz

•  AOS-CX advertises DCBx with the willing bit set to 0 in all TLVs. This tells the peer that the switch is not

willing to change its configuration to match the peer's configuration.

•  When a peer device does not support the configured DCBx version (IEEE or CEE), a misconfiguration

error will be displayed in the  show dcbx interface  output.

IP ECN

IP Explicit Congestion Notification (ECN) is not part of the DCB protocol standard and is covered separately
by RFC 3168, however ECN plays a critical role in enhancing lossless Ethernet over a layer 3 IP fabric. IP ECN
is a congestion notification protocol which throttles back traffic rather than pausing or dropping packets in
the event of congestion. It is a slow acting mechanism and assists in avoiding pause frames generated by
PFC by throttling back traffic before queue congestion occurs.

When devices in an IP ECN fabric experience congestion, the device marks congestion via ECN bits in the
IP DiffServ field and forwards the IP packets on to either the next IP hop or to the end host destination.
The receiving host is IP ECN aware and the congestion notification is handled by the upper layer protocols
such as TCP. The IP ECN congestion bits are then echoed back to the transmitting host device which in turn
reduces its transmission rate.

In order for IP ECN to work, the sender and receiver's upper layer protocol must be congestion-aware such
as TCP or SCTP (Stream Control Transmission Protocol). In addition, all switch hops in the path between the
sender and receiver are required to be ECN-aware and configured appropriately.

Host network interface cards

Network interface cards (NICs) on hosts that require lossless Ethernet can support the following protocols:

Public

IP ECN 43

•  PFC

•  ETS

•  DCBx*

•

IP ECN

NOTE

*Support for DCBx is not mandatory but highly desirable.

PFC support is a prerequisite for storage and lossless Ethernet networking. AOS-CX provides the following
DCB features which are supported across specific listed CX platforms:

Feature

DCB Protocols

AOS-CX 10.10 or later

Priority‐based Flow Control (PF
C)

Yes (10000/9300/8400/8100/83
60/8325)

Enhanced Transmission Selection (
ETS)

Yes (10000/9300/8400/8100/83
60/8325)

Data Center Bridging Exchange (
DCBx)

Yes (10000/9300/8400/8100/83
60/8325)

Quantized Congestion Notification
(QCN)

No

L3 Notification Protocol

IP Explicit Congestion Notification
(ECN)

Yes (10000/9300/8400/8100/83
60/8325)

Lossless PFC priorities per port

7 (10000/9300/8325)

2 (8100/8360)

1 (8400)

Public

Host network interface cards 44

Feature

Lossless pools

NOTE

AOS-CX 10.10 or later

3 (10000/9300/8325)

DCB protocols are only supported on the network underlay and are not
supported across VXLAN overlay.

NOTE

The HPE Aruba Networking 10000, 9300, and 8325 Switch Series support
Asymmetric PFC.

DCB layer 3 configuration task list

Procedure

1.  Enable DCBx

2.  Configure QoS pool(s)

3.  Configure and apply QoS queue and schedule profiles

4.  Optionally make any required configuration changes to the CoS and DSCP maps.

5.  Configure global trust and override trust settings on individual interface settings

6.  Enable PFC on the required priorities for each interface where it is necessary

7.  Configure DCBx application TLVs

8.  Configure ECN

Results

Public

DCB layer 3 configuration task list 45

DCBx configuration

DCBx is dependent on LLDP and uses LLDP TLVs to exchange configuration details. A DCBx-enabled device
can advertise various parameters including ETS, PFC, and 802.1p CoS value.

A DCBx-enabled switch can request its peer to map certain application traffic to a priority using the DCBx
TLV subtype (0x0c). Whether the host accepts the QoS parameters or rejects them is dependent on the
host’s local DCBx NIC willing "W" bit state:

•

If set to 1 - Indicates that the adapter is willing to accept QoS parameters from the remote peer

•

If set to 0 – Operational QoS parameters are always resolved from the local Host nic QoS parameters

An example of DCBx TLV advertisement where the switch advertises to the host to use TCP port 3260 for
iSCSI and places it in queue 4 (802.1p CoS value 4):

Subtopics

DCBx configuration considerations
Enabling DCBx

DCBx configuration considerations

DCBx is expected to operate over a point-to-point link. If multiple LLDP neighbors are detected, then DCBx
behaves if its peer DCBx TLVs are not present and behaves this way until the multiple LLDP neighbor
condition is no longer present.

•  DCBx can be enabled globally or within a specific interface and is disabled by default

•  The IEEE DCBx IEEE 802.1Qaz is the default version when DCBx is enabled

•  LLDP must be enabled prior to configuring DCBx

Public

DCBx configuration 46

•  DCBx is not essential between host and switch but is highly desirable as to avoid manual PFC

configurations of host devices.

•  DCBx should be configured on every switch hop interface.

Enabling DCBx

LLDP must enabled globally prior to any DCBx configuration and can be enabled with the  lldp enabl
e  command. DCBx can be enabled either globally or at the interface level and can specify either the IEEE or
CEE version by using the  lldp dcbx  command..

NOTE

The DCBx application TLV is part of the DCBx configuration but must be
configured after the PFC configuration.

Enabling DCBx globally:

switch(config)# lldp dcbx

Enabling the IEEE version of DCBx globally:

switch(config)# lldp dcbx version ieee

Enabling the CEE version of DCBx globally:

switch(config)# lldp dcbx version cee

Enabling DCBx for an interface:

switch(config-if)# lldp dcbx

Enabling the IEEE version of DCBx for an interface:

switch(config-if)# lldp dcbx version ieee

Enabling the CEE version of DCBx for an interface:

switch(config-if)# lldp dcbx version cee

The  no  form of any of these commands will remove the configuration from the switch. In order to do
this you must first enter the appropriate configuration context as indicated by the  switch(config)
#  prompt for global configuration or  switch(config-if)#  for interface configuration. For example,
removing the IEEE version of DCBx from a specific interface:

Public

Enabling DCBx 47

switch(config)# interface 1/1/1

switch(config-if)# no lldp dcbx version ieee

Priority-based flow control

Priority-based Flow Control (PFC) provides an enhancement to the Ethernet flow control pause command.
PFC operates at layer 2 , supporting layer 2 and layer 3 network connectivity. The standard Ethernet pause
frame will pause all traffic on an Ethernet link when an ingress interface buffer is full, impacting all traffic
flows.

The 802.1Qbb standard for PFC allows up to 8 different traffic classes to separately paused by a device.
AOSCX switch devices support a varying number of PFC-enabled priorities on each port, depending on the
model. However, a priority configured with PFC should be assigned to its own queue. Never combine more
than one PFC priority in a queue because either priority being paused will result in both getting paused by
the switch. The PFC receiving side sends a pause frame (XOFF) to the transmitting station when the buffer
becomes full for a specific PFC-configured traffic class. This pause frame requests the transmitting station
stop sending packets of that traffic class but allows all other traffic to continue.

It is recommended to configure PFC or link-level flow control RXTX mode and pools once on a running
system. Changing the pool or flow control configuration on a running system will cause brief traffic
disruption and packets will be lost in the data flow while the reconfiguration occurs. This may affect one,
multiple, or all ports, depending on the existing configuration, and changes made to it.

Switch series

Priority‐based flow control priorities

8325/8325H/9300/10000

Up to 7 PFC priorities per interface.

8360

8400

Up to 2 PFC priorities per interface.

One PFC priority configured per interface.

PFC has the following characteristics:

•

IEEE 802.1Qbb is based on Ethernet flow control

•  Pause frames stop transmitters when downstream buffer is full

•  Required to support lossless Ethernet (avoid dropping storage traffic)

•  Provides mechanism with PAUSE per 802.1p priority

Public

Priority-based flow control 48

•  Provides PAUSE of one or more traffic classes

NOTE

Jumbo frame MTU size is required on network infrastructure to support storage
networking traffic.

Subtopics

PFC and the QoS pool
Asymmetric PFC
Configurable flow control buffer thresholds
Configurable port QoS counters
Considerations and prerequisites

PFC and the QoS pool

About this task

The QoS pool option on the HPE Aruba Networking 8325, 9300, and 10000 Switch Series enables the
creation of a packet buffer pool which is dedicated specially for lossless traffic. The  qos pool  command
configures lossless pool size, headroom buffer associated with the pool, and the priorities that are mapped to
that pool.

The lossless pool size is a percentage of the total available buffer memory on the device. The headroom pool
memory is allocated from the lossless pool and is used for storing packets that arrive on a port after a PFC
pause has been asserted.

The headroom pool is necessary because the upstream device may have transmitted frames which are
in-flight on the wire when it receives the pause frame from the downstream switch. The downstream switch
must have reserved buffer space for these in-flight frames in order to guarantee lossless delivery.

Public

PFC and the QoS pool 49

An example would be:

Procedure

1.  Packets are received on a switch interface from an upstream transmitting device where the receiving

switch cannot transmit them as fast as they are arriving. These packets must be buffered by the switch
in the shared lossless pool until they can be transmitted. If this condition continues long enough, the
switch interface allocation from the shared lossless pool becomes exhausted.

2.  A PFC pause frame is sent from the switch interface to the upstream device.

3.  Packets received by the switch after sending a pause to the upstream device are buffered in the

headroom pool.

Asymmetric PFC

Symmetric PFC is when an interface has the same configuration in both directions. This is the same
functionality as symmetric Ethernet flow control pause.

Asymmetric PFC allows the configuration of the pause function on an interface independently in each
direction relative to the specific PFC priority. The interface can have different configurations for both the
receive and transmit buffers.

•  Symmetric PFC - Interface has same configuration in both directions

•  Asymmetric PFC - Interface has different configuration in both directions

◦  Provides the ability to separately enable taking action (stop transmit) upon receipt of a pause frame

and transmitting a pause frame when the buffer limit is reached due to arriving packets.

◦  Can be enabled in both directions, disabled in both directions, or enabled in one direction and

disabled in the other direction

Receive (Rx) buffer

Transmit (Tx) buffer

Configured flow control state

On

Off

Off

On

Interface doesn't request that the
connected peer stop sending traffi
c. It will respond to PFC pause fra
mes received from the connected
peer but will not send pause fram
es upstream.

Interface generates and sends pau
se frames but will not respond to
received pause frames and will con

Public

Asymmetric PFC 50

Receive (Rx) buffer

Transmit (Tx) buffer

Configured flow control state

On

On

tinue to transmit in the event that
it receives one.

Interface both sends and respond
s to received pause frames applied
to the specific configured PFC prio
rity.

Configurable flow control buffer thresholds

The switch supports configuration of XOFF limit, XON delta and headroom limit buffer thresholds on flow
control enabled interfaces. The purpose for each of these values is:

•  XOFF limit is defined as the amount of shared buffer space flow-controlled packets are allowed to

consume before pause is asserted to the link partner.

•  XON delta is defined as the offset below XOFF limit when pause is de-asserted to the link partner.

•  Headroom limit is defined as the amount of buffer space reserved to absorb any in-flight packets from
the time that the XOFF message is transmitted by the local device until the time that the last packet is
sent by the link partner and received by the local device.

By default when LLFC RXTX or PFC is enabled, the switch uses a dynamic buffer threshold for the XOFF
limit, a delta value for XON and a headroom buffer limit based on 350m cable length. For many scenarios
these defaults are sufficient to provide good performance without problems. However, in some situations
it may be useful to tune the XOFF limit, XON delta and headroom parameters based on the unique
requirements of a particular deployment. In those situations, the buffer tuning capabilities described in
this section can be useful to help optimize memory usage. Refer to the QoS Commands section for syntax
of the CLI. QoS buffer configuration using flow-control buffer commands are only applicable to ports or
priorities configured for flow-control. If specified for a port or priority not configured for flow-control, the
configuration has no effect. QoS buffer configuration for PFC priorities are not applicable to LLFC RXTX
ports and vice versa.

Subtopics

XOFF thresholds
XON delta
Headroom size

XOFF thresholds

Public

Configurable flow control buffer thresholds 51

The lossless buffer limits for traffic arriving on flow-control enabled ports or priorities can be optionally
configured using one of two modes, dynamic or static. If no user-configured limit is specified, the default
limit of dynamic alpha 2 is configured.

Subtopics

Dynamic XOFF thresholds
Static XOFF thresholds

Dynamic XOFF thresholds

The limit scales as a function of available buffer resources and is configured by specifying an alpha value in
the range between -7 and 3. The dynamic limit is based on the currently-available free space, multiplied by
2 raised to the power of the specified alpha value. A value less than zero means that the limit is a fraction of
the pool free space, e.g. -1 corresponds to half. A value greater than zero means that the limit is a multiple of
the free-space size, e.g. 1 corresponds to double.

Static XOFF thresholds

A static limit sets a fixed size for the XOFF threshold.

XON delta

The value is relative to the XOFF limit and applies to both dynamic and static XOFF limit configurations.
When the buffer in-use amount from a source port (LLFC RXTX) or source port + priority (PFC) reaches
the XOFF limit, pause is asserted to the link peer. At this point, pause will remain asserted until the shared
buffer in-use amount by this port/priority decreases by the XON Delta amount. Once enough packets are
transmitted to reduce In-Use by this amount, pause is de-asserted. It is important to note that the XON
Delta value will impact the amount of flow-control pause frames sent to the link peer and can have a
negative impact on performance. A value that is too small can result in many more pause frames sent to
the link peer as the buffer in-use amount reaches the XOFF limit, drops slightly and meets the XON delta,
then immediately jumps back to the XOFF limit. Conversely, a value that is too large can result in poor link
bandwidth utilization due to insufficient buffered packets as the buffer drains too far before more packets
arrive to utilize the link. The default XON Delta value is 12288 bytes.

Headroom size

Public

Dynamic XOFF thresholds 52

This value can be explicitly configured by setting the buffer size or implicitly configured by setting the cable
length. If both are specified, the buffer size value is used and the cable length is ignored.

Subtopics

Headroom limit
Cable length value
Cable length auto
Cable length default

Headroom limit

Headroom Limit for a LLFC RXTX port or PFC priority, sets a fixed size of headroom pool buffer space for
in-flight packets that arrive after XOFF is asserted.

Cable length value

Indirectly adjusts the headroom buffer size on the physical interface. Cable length is one of the delay
components that effects traffic round trip time (RTT). Based on IEEE std 802.1Qbb, RTT depends on several
delay components such as PFC transmission delay, Interface Delay, Cable Delay and Higher layer delay. Cable
length configuration changes the cable delay component of RTT and is used to compute the headroom
buffer size for in-flight packets that arrive after XOFF is asserted. If both headroom buffer limit and cable
length are configured, the headroom buffer limit is used and cable length is ignored.

Cable length auto

Auto mode will compute the headroom size using the length of the attached cable when known. If the cable
length cannot be determined, headroom is computed using the configured cable length or the default length
of 350 meters.

Cable length default

If none of the commands that adjust the headroom limit are configured, a default cable-length of 350 meters
is used to compute the headroom pool limit.

Public

Headroom limit 53

Configurable port QoS counters

Counters not natively supported by the network processor can be enabled by creating matching TCAM
entries in the Ingress Field Processor (IFP) and Egress Field Processor (EFP).

NOTE

The switch may fail to obtain the necessary TCAM resources due to consumption
by other features. Use the show resources command to assess TCAM resource
usage. The show running-config interface < IFNAME > command will display a
warning message if counters are not enabled.

The following counters are supported using TCAM:

•  RoCEv2 Protocol Counters

•  ECN Counters

Subtopics

RoCEv2 protocol counters
ECN Counters

RoCEv2 protocol counters

RoCEv2 is carried in IP-UDP packets. The TCAM can inspect and match on RoCEv2 protocol header fields
for the purpose of counting specific protocol packet types. These counters provide a scalable method for
debugging end-user RoCEv2 sessions on switches, as opposed to individually checking each session for
packet drops and congestion on end stations. The following section outlines the fields that are matched on
the network devices for each relevant counter.

Congestion notification (CNP)

A congestion notification is sent to alert the source about a congestion event.

CNP Packet format:

+--------------------+

|    MAC Header      |

+--------------------+

|  IPv4/v6 Header    |

| - IP protocol:17   |
|  (0x11)            |
+--------------------+

|    UDP Header      |

| - L4 Destination-  |

Public

Configurable port QoS counters 54

|   port:4791(0x12b7)|

+--------------------+

|    BTH  Header     |

|   -opcode:0x81     |

|   -flags:0x40      |

+--------------------+

|    ICRC            |

+--------------------+

|    FCS             |

+--------------------+
An entry is created in the ingress TCAM to match the highlighted fields above in order to count the packets.

Negative acknowledgement (NAK)

When a receiver detects a Packet Sequence Number (PSN) value in a received packet that does not match
the expected PSN or fall within the valid duplicate packet range, it generates a NAK packet to signal an
event to the source.

NAK Packet format:

+--------------------+

|    MAC Header      |

+--------------------+

|  IPv4/v6 Header    |

| - IP protocol:17   |

|  (0x11)            |

+--------------------+

|    UDP Header      |

| - L4 Destination-  |

|   port:4791(0x12b7)|

+--------------------+

|    BTH  Header     |

|    -opcode:0x11    |

+--------------------+

|    AETH Header     |

|   -syndrome:0x60   |

+--------------------+

|    ICRC            |

+--------------------+

|    FCS             |

+--------------------+
An entry is created in the ingress TCAM to match the highlighted fields and count the packets.

Positive acknowledgement (ACK)

A positive ACK packet is generated to signal an event to a source when a receiver correctly receives the
packets sent.

Public

RoCEv2 protocol counters 55

ACK Packet format:

+--------------------+

|    MAC Header      |

+--------------------+

|  IPv4/v6 Header    |

| - IP protocol:17   |

|  (0x11)            |

+--------------------+

|    UDP Header      |

| - L4 Destination-  |

|   port:4791(0x12b7)|

+--------------------+

|    BTH  Header     |

|    -opcode:0x11    |

+--------------------+

|    AETH Header     |

|   -syndrome:0x00   |

+--------------------+

|    ICRC            |

+--------------------+

|    FCS             |

+--------------------+
An entry is created in the ingress TCAM to match the highlighted fields and count the packets.

Other RoCEv2 packets

All received packets on the port with UDP destintion port set to 4791 (0x12b7) that are not CNP, NAK, or
ACK packets.

Total RoCEv2 packets

All received packets on the port with UDP destintion port set to 4791 (0x12b7).

ECN Counters

ECN defines the last two bits (ECN field) in the Differentiated Services (DS) field of the IP header as follows:

ECN-capable transport (ECT) counters

The last two bits in the DS field are set to either 0x01 or 0x10 by end stations. Two entries are created in
the egress TCAM of the switch to match the last two bits of the DS field set to either 0x01 or 0x10 in order
to count the packets.

Congestion experienced (CE) counters

Public

ECN Counters 56

On the 9300 and 9300S Switch Series, packets marked with the "Congestion Experienced" (CE) bit by the
switch are not counted in the CE TX packet counters. These counters only reflect packets marked with the
CE bit by upstream devices.

On the 8325, 8325H, and 10000 Switch Series, the last two bits in the DS field are set to 0x11 by the switch
experiencing congestion. An entry is created in the egress TCAM to match these two bits of the DS field to
count the packets.

Considerations and prerequisites

PFC configuration is dependent on the successful configuration of the appropriate QoS pool with the
priorities required for the PFC interface configuration. PFC cannot be enabled on an interface if the PFC
priority is not first mapped to a lossless pool. The exception is when RX-only flow control is allowed to be
configured without any pools. This is to support semi-lossless behavior where the switch can be paused by
the downstream device (LLFC or PFC depending on the config), but the switch will eventually start dropping
packets if the queue (lossy buffer) becomes full. The number of unique priority-based flow control (PFC)
combinations across all switch interfaces cannot be more than 3 for the 8325/10000 Switch Series and
cannot be more than 7 for the 9300 Switch Series.

An example of QoS pool configuration:

switch(config)# qos pool 1 lossless size 30 percent headroom 2048 kbytes

priorities 1,2

switch(config)# qos pool 2 lossless size 30 percent headroom 2048 kbytes

priorities 3,4

switch(config)# qos pool 3 lossless size 30 percent headroom 2048 kbytes

priorities 5,6,7

NOTE

PFC is required to be configured on all interfaces between the host initiator and
the host target for both L2 and L3 connections.

QoS queue profile

The QoS queue profile maps local priorities to queues. The CoS-map defines the 802.1p priority code
mappings to the local priorities. The relationship to the QoS queue profile for lossless Ethernet is the CoS
map and the DSCP map. The factory defaults are applied for both maps at system start up.

Default CoS map

Public

Considerations and prerequisites 57

switch# show qos cos-map default

code_point local_priority color   name

---------- -------------- ------- ----

0          1              green   Best_Effort

1          0              green   Background

2          2              green   Excellent_Effort

3          3              green   Critical_Applications

4          4              green   Video

5          5              green   Voice

6          6              green   Internetwork_Control

7          7              green   Network_Control

switch# show qos dscp-map

DSCP     code_point local_priority mpls_exp color   name

-------- ---------- -------------- -------- ------- ----

000000   0          1              0        green   CS0

Codepoints 1-7 removed for brevity

001000   8          0              1        green   CS1

Codepoints 9-15 removed for brevity

010000   16         2              2        green   CS2

Codepoints 17-23 removed for brevity

011000   24         3              3        green   CS3

Codepoints 25-31 removed for brevity

100000   32         4              4        green   CS4

Codepoints 33-39 removed for brevity

101000   40         5              5        green   CS5

Codepoints 40-47 removed for brevity

110000   48         6              6        green   CS6

Codepoints 48-55 removed for brevity

111000   56         7              7        green   CS7

Codepoints 57-63 removed for brevity
Factory default QoS queue profile

A single factory-default queue profile is initially applied to every port:

switch# show qos queue-profile factory-default

queue_num local_priorities name

--------- ---------------- ----

0         0                Scavenger_and_backup_data

1         1

2         2
3         3
4         4

5         5

6         6

7         7

Public

QoS queue profile 58

The default queue-profile has each local-priority mapped to a separate queue:

Best effort traffic will use Queue 1 using the default cos-map and qos-queue profile.

•  Code point 0 (CoS value 0) is mapped to local priority 1 in the default cos-map for best effort traffic

•  Code point 1 (CoS value 1) is mapped to local priority 0 in the default cos-map for less than best effort

traffic

•  Local priority 1 is mapped to queue 1 in the qos queue-profile factory-default

•  The default CoS map and DSCP map can be leveraged noting the CoS value 0 (typically best effort

traffic) will be mapped to queue 1 when using the default maps

A QoS queue profile is always applied to the switch and is necessary to specify internal priority to queue
mapping. At all times either the factory-default queue profile or a user-specified queue profile is applied to
the switch.

Subtopics

QoS queue profile configuration

QoS queue profile configuration

About this task

The preferred QoS queue profile configuration will depend on the number PFC priorities as part of the
lossless traffic class and the overall QoS requirements for all traffic classes.

•  A local priority can only be associated with a single queue

•  Any number of local priorities can be configured to a single queue

Public

QoS queue profile configuration 59

•

It is essential that local priority 7 is given a dedicated queue with a minimum bandwidth for
infrastructure control traffic to avoid buffer starvation from other priority queues

NOTE

It is not recommended to assign multiple local priorities to the same queue if
those local priorities are used for lossless traffic.

QoS queue profile configuration involves the following steps:

Procedure

1.

Identify local priorities for mapping to the QoS queue profile

2.  Map local priorities to the appropriate queue

Results

Create a QoS queue profile called  queue-profile-1 :

switch(config)# qos queue-profile queue-profile-1

Map queues in  queue-profile-1  to local priorities:

switch(config)# qos queue-profile queue-profile-1

switch(config-queue)# map queue 0 local-priority 0

switch(config-queue)# map queue 1 local-priority 1,2,5,6

switch(config-queue)# map queue 2 local-priority 3

switch(config-queue)# map queue 3 local-priority 4

switch(config-queue)# map queue 4 local-priority 7

The  no  form of the  qos queue-profile  command will remove the QoS queue profile:

switch(config)# no qos queue-profile queue-profile-1

QoS schedule profile - enhanced transmission selection

Public

QoS schedule profile - enhanced transmission selec... 60

Q
o
S

s
c
h
e
d
u
l
e

p
r
o
fi
l
e

-

e
n
h
a
n
c
e
d

t
r
a
n
s
m
i
s
s
i
o
n

s
e
l
e
c
.
.
.

AOS-CX leverages the DWRR algorithm to provide different weights to each QoS queue which will support a
single or a number of traffic classes in a profile. The profile is called the schedule-profile and by default all
interfaces will have the default-schedule profile applied.

NOTE

The configuration examples below apply to the 8100, 8325, 8360, 9300, and
10000 Switch Series. Configuration on the 8400 Switch Series is similar with the
only difference being it uses the WFQ algorithm instead of DWRR.

The factory default schedule profile :

switch# show qos schedule-profile factory-default

queue_num algorithm     weight max-bandwidth_kbps burst_KB

--------- ------------- ------ ------------------ --------

0         dwrr          1

1         dwrr          1

2         dwrr          1

3         dwrr          1

4         dwrr          1

5         dwrr          1

6         dwrr          1

7         dwrr          1

Subtopics

DWRR Calculation
QoS schedule profile configuration
Overriding the global schedule profile on an interface

DWRR Calculation

To calculate the bandwidth relative to the DWRR weight, the queue weight is divisible by the sum of the
weights for all queues. The default schedule profile has 8 queues with each queue having a weight of 1.
To calculate the bandwidth used for each queue, the individual queue weight is divided by the sum of
weights of all queues. An example using the factory default schedule profile which represents the minimum
bandwidth for each queue:

•  Queue 0 dwrr weight 1 - 1(8) = 12.5%

•  Queue 1 dwrr weight 1 - 1(8) = 12.5%

•  Queue 2 dwrr weight 1 - 1(8) = 12.5%

•  Queue 3 dwrr weight 1 - 1(8) = 12.5%

Public

DWRR Calculation 61

•  Queue 4 dwrr weight 1 - 1(8) = 12.5%

•  Queue 5 dwrr weight 1 - 1(8) = 12.5%

•  Queue 6 dwrr weight 1 - 1(8) = 12.5%

•  Queue 7 dwrr weight 1 - 1(8) = 12.5%

NOTE

The total percentage should add up to 100% for all weights.

For lossless Ethernet traffic flows, a custom schedule profile must provide the appropriate amount of
bandwidth to the lossless queues as well as the lossy queues configured on the switch system. The
queue-profile and the schedule-profile must specify the same queues. If the custom schedule-profile uses
the same queues as the factory-default queue-profile, then no custom queue-profile is required.

QoS schedule profile configuration

About this task

The following considerations should be taken into account when configuring a QoS schedule profile:

•  Assign DWRR weights based on lossless flows, traffic flow volume, and a consideration to other traffic

classes.

•  Ensure that the highest numbered queue specified in the applied queue-profile (assigned to critical

networking traffic) has a minimum amount of bandwidth to avoid queue starvation.

•  Number of queues

◦  On the 9300 Switch Series the number of queues in the queue profile must align to the number of

queues with allocated weights in the schedule profile.

◦  On the 8325/10000 Switch Series it is possible to configure any of the 8 queues (0-7). The number
of queues as well as the queue numbers themselves must be the same between the applied queue
profile and schedule profile.

•

It is recommended to use weights totaling 100 for easy reference to bandwidth percentage reservations.

QoS schedule profile configuration involves the following steps:

Procedure

1.  Configure QoS queue profile

2.  Create the schedule profile

Public

QoS schedule profile configuration 62

3.  Apply the QoS queue profile and schedule profile

Results

Creating a QoS schedule profile:

switch (config)# qos schedule-profile schedule-profile1

The below example shows an ETS configuration within a 2-queue environment. The settings use a weight to
set the amount of available bandwidth for each queue. The settings in the example below would ensure that
50% of bandwidth will be applied to both queue 0 and queue 1:

switch(config)# qos schedule-profile schedule-profile1

switch(config-schedule)# dwrr queue 0 weight 15

switch(config-schedule)# dwrr queue 1 weight 15

Applying the schedule profile and queue profile:

switch (config)# apply qos queue-profile profile1 schedule-profile schedule-

profile1

The global configuration will be applied to all interfaces.

Overriding the global schedule profile on an interface

About this task

A different schedule profile can be applied directly to interfaces which will override the global schedule
profile. The caveat is that the schedule profile queues must align to the same queues as defined in the
applied QoS queue profile. The procedure for applying a different schedule profile to a specific interface is as
follows:

Procedure

1.  Create a schedule profile that specifies the same queues used in the globally-applied queue profile

2.  Customize the scheduling algorithm and weight (depending on algorithm) for each queue

3.  Apply the override schedule profile to the desired interface(s)

Results

Creating the interface override schedule profile called  schedule-profile2 :

switch (config)# qos schedule-profile schedule-profile2

switch (config-schedule)# dwrr queue 0 weight 5

Public

Overriding the global schedule profile on an inter... 63

O
v
e
r
r
i
d
i
n
g

t
h
e

g
l
o
b
a
l

s
c
h
e
d
u
l
e

p
r
o
fi
l
e

o
n

a
n

i
n
t
e
r
.
.
.

switch (config-schedule)# dwrr queue 1 weight 50

switch (config-schedule)# dwrr queue 2 weight 20

switch (config-schedule)# dwrr queue 3 weight 15

switch (config-schedule)# dwrr queue 4 weight 10

Applying schedule profile  schedule-profile2  mapped with queue profile  profile1  to the
global config:

 switch(config)# apply qos queue-profile profile1 schedule-profile schedule-

profile2

Verifying that that the interface override has occurred:

switch# show qos schedule-profile

profile_status profile_name

-------------- ------------

complete       factory-default

applied        schedule-profile2

complete       strict

incomplete     test1
Validating that schedule profile  schedule-profile2  is applied to an interface:

switch# show interface 1/1/1 qos

Interface 1/1/1 is up

 Admin state is up

 qos trust none (global)

 qos queue-profile profile1 (global)

 qos schedule-profile schedule-profile2 (global)

Creating the schedule profile called  profile1  that will become the global schedule profile:

switch (config)# qos schedule-profile schedule-profile1

switch (config-schedule)# dwrr queue 0 weight 5
switch (config-schedule)# dwrr queue 1 weight 25

switch (config-schedule)# dwrr queue 2 weight 35

switch (config-schedule)# dwrr queue 3 weight 25

switch (config-schedule)# dwrr queue 4 weight 10

Applying schedule profile  profile1  to queue profile  profile1 :

switch (config)# apply qos queue-profile profile1 schedule-profile schedule-
profile1

Public

Overriding the global schedule profile on an inter... 64

Validating that the schedule profile  profile1  is applied globally and has overwritten the global setting
of schedule profile  profile2 :

switch# show qos schedule-profile

profile_status profile_name

-------------- ------------

complete       factory-default

applied        schedule-profile1

complete       schedule-profile2

complete       strict
Validating the global the schedule profile  profile1  has been applied to all interfaces:

switch# show interface qos

Interface 1/1/1 is up

 Admin state is up

 qos trust none (global)

 qos queue-profile profile1 (global)

 qos schedule-profile schedule-profile1 (global)

output removed for brevity

Interface 1/1/56 is up

 Admin state is up

 qos trust none (global)

 qos queue-profile profile1 (global)

 qos schedule-profile schedule-profile1 (global)

Applying schedule profile  profile2  to a specific interface to override the global schedule profile:

switch (config)# interface 1/1/1

switch (config-if)# apply qos schedule-profile schedule-profile2

Verifying that both schedule profiles are applied:

switch# show qos schedule-profile

profile_status profile_name

-------------- ------------

complete       factory-default

applied        schedule-profile1

applied        schedule-profile2

complete       strict
Verifying that schedule profile  profile2  has overridden  profile1  on interface 1/1/1 and  profil
e1  has been applied to all other interfaces:

switch# show interface qos

Interface 1/1/1 is up

Public

Overriding the global schedule profile on an inter... 65

Admin state is up

 qos trust none (global)

 qos queue-profile profile1 (global)

 qos schedule-profile schedule-profile2 (override)

interfaces removed for brevity

Interface 1/1/56 is up

 Admin state is up

 qos trust none (global)

 qos queue-profile profile1 (global)

 qos schedule-profile schedule-profile1 (global)

Schedule profile  profile2  has been applied only to interface 1/1/1. All other interfaces retain the global
schedule profile setting of  profile1 .

IP explicit congestion notification

About this task

TCP/IP networks signal congestion by dropping packets. When packets are dropped due to congestion,
TCP/IP easily detects this but performance suffers. For lossless Ethernet fabric, dropping packets is not
allowed, so a different action is required to inform endpoints of congestion. Instead of dropping packets
when congestion is experienced, ECN marks the IP packet as congestion experienced (CE).

ECN is used in conjunction with DCBx and used to avoid hitting the PFC limits over L3 network hops. The
ECN bits of a packet are conditionally marked by a switch based on a configurable ECN threshold which
allows TCP to function normally without dropping IP packets. ECN has the following characteristics:

•  Uses the DiffServ field in the IP header to mark the congestion status along the packet transmission

path.

•  End-to-end communication protocol which requires support by each end device as well as all

intermediate switch hops.

•  Applied on a queue basis and can be applied to 1 or more queues concurrently up to the 8 queue limit.

ECN uses the two "least significant" bits in the Traffic Class (DiffServ) field of the IP header (the bits that are
farthest to the right) to signal the current state of network congestion. The possible markings are:

Bits

00

01

Congestion status

Abbreviation

Non ECN‐Capable Transport

Non‐ECT

ECN Capable Transport

ECT(1)

Public

IP explicit congestion notification 66

| Bits |     | Congestion status      | Abbreviation |     |
| ---- | --- | ---------------------- | ------------ | --- |
| 10   |     | ECN Capable Transport  | ECT(0)       |     |
| 11   |     | Congestion Encountered | CE           |     |
NOTE
ECT(1) and ECT(0) are considered to be functionally the same by the switch. If
congestion is encountered, the zero bit will be flipped to indicate congestion.
The benefit of ECN is that it reduces the likelihood of dropping packets in a lossy fabric or reduces the usage
of flow-control pause in a lossless fabric. ECN accomplishes this via the following actions:
Procedure
1.  IP packets flow normally on an IP network from an ECN-enabled device with the ECN field marked
ECT(0) or ECT(1) to indicate support for ECN
2.  If an ECN-enabled host device receives a packet marked CE; it acknowledges the marked packet with its
upper layer protocols (TCP)
3.  The host receiving the CE marked packet sends the congestion notification back to the transmitting
host
4.  The transmitting host device handles ECE marking in the received acknowledgment frame by reducing
its transmit rate
5.  The reverse congestion notification occurs in the TCP header, not the IP header, using the ECE flag of
the acknowledgment frame.
|     | Public |     | IP explicit congestion notification | 67  |
| --- | ------ | --- | ----------------------------------- | --- |

Results

Subtopics

IP ECN configuration considerations
IP ECN configuration procedure

Public

IP explicit congestion notification 68

IP ECN configuration considerations

NOTE

Only supported by the HPE Aruba Networking 8325, 9300, and 10000 Switch
Series.

The HPE Aruba Networking 8325, 9300, and 10000 Switch Series have a dual threshold profile with
a minimum and maximum threshold in bytes. Between the minimum and maximum thresholds there is
a probability curve. As the buffer utilization increases past the minimum threshold, there is a higher
probability of packets being marked by ECN due to congestion. When buffer utilization reaches the
maximum threshold all packets are marked for ECN congestion.

An ECN threshold profile can be applied either globally or at the interface level to override the global
threshold setting. Only one ECN threshold profile can be applied to a port.

The following factors should always be taken into account when configuring IP ECN:

•  ECN is configured on queues carrying delay-sensitive traffic.

•  Any number of queues maybe configured in a profile.

•  An unconfigured queue means no threshold action behavior will occur.

•  ECN can be applied globally or on individual interfaces.

•  No threshold policies are applied by default.

•  All switches in the transmission path between two ECN-enabled endpoints must have ECN enabled and

configured for the appropriate queue.

•  General guidance is to allocate 512 kilobytes per flow (.5MB) to derive the minimum threshold and add
between 512 kilobytes and 1024 kilobytes (1MB) to the total for the maximum threshold. An example
when configuring 4 ingress flows:

◦  Minimum threshold = 2048 kilobytes (2MB)

◦  Maximum threshold = 2560 kilobytes (2.5MB)

•  Testing is recommended to ensure ECN thresholds are correctly applied.

IP ECN configuration procedure

The procedure for configuring IP ECN is as follows:

•  Create a threshold profile using the qos threshold-profile command and apply threshold values

Public

IP ECN configuration considerations 69

•  Optionally apply a QoS threshold profile globally

•  Optionally apply a QoS threshold profile to the desired interface(s) to override the global threshold

profile setting

Creating a QoS threshold profile called ECN applied globally to all interfaces:

switch(config)# qos threshold-profile ECN

switch(config-threshold)# queue 1 action ecn all min-threshold 512 kbytes

max-threshold 1520 kbytes

switch(config)# apply qos threshold-profile ECN

Creating a QoS threshold profile called ECN2 :

switch(config)# qos threshold-profile ECN2

switch(config-threshold)# queue 1 action ecn all min-threshold 3072 kbytes

max-threshold 4096 kbytes

Applying QoS threshold profile ECN2 to a specific interface:

switch(config)# interface 1/1/1

switch(config-if)# apply qos threshold-profile ECN2

Lossless QoS pool

The QoS pool is a packet buffer pool. The HPE Aruba Networking 8325, 9300, and 10000 Switch Series
have a configurable QoS pool with an associated headroom buffer space, while the 8360 has a single fixed
QoS pool which is not exposed to the CLI for configuration. The 8400 Switch Series assigns reserved buffer
space per-interface per-PFC-priority, there is no fixed lossless pool.

Switch series

8325/9300/10000

8360/8400

Lossless QoS pools

Three configurable lossless pools

Single fixed lossless pool

The QoS pool is a packet buffer pool resident in memory in the switch. Only the QoS pools on the HPE Aruba
Networking 8325, 9300, and 10000 Switch Series are configurable and have the following attributes:

•  The QoS pool option enables the creation of a packet buffer pool which is dedicated to lossless traffic

Public

Lossless QoS pool 70

•  The QoS pool command allows the creation of a lossless pool size, headroom buffer associated with the

pool, and the priorities that are mapped to that pool.

•  The lossless pool size is a percentage of the total available buffer memory on the device.

•  The headroom pool memory is allocated from the lossless pool and is used for storing packets that

arrive on a port after a pause has been asserted.

Subtopics

Considerations and prerequisites
QoS pool configuration

Considerations and prerequisites

There are no prerequisite configuration activities required to configure QoS pools. However, a PFC priority
or any related PFC commands cannot be enabled on an interface until the creation of the QoS pool and the
appropriate PFC priority mapping to that pool. The following considerations should be taken into account
when configuring QoS pools:

•  Maximum buffer size in memory

◦  8325/10000: 32Mb

◦  9300: 66 MB

•  Maximum configurable headroom memory size: 10240 kbytes (10Mb)

•  Factory-default headroom size: 3072 kbytes (3Mb)

•  The sum of pool sizes cannot be larger than 90% of the available Kbyte memory

•  The headroom size cannot be greater than half of the lossless pool buffer size.

NOTE
Best practice for QoS pools on all platforms is to not assign the best effort traffic
class (default local priority 1) and the critical control traffic (local priority 7) to a
lossless pool.

QoS pool configuration

Public

Considerations and prerequisites 71

QoS pools are enabled using the QoS pool command in the global configuration context.

NOTE
For additional information on QoS pool configuration please refer to the  qos p
ool   command.

NOTE

The following examples are applicable to the 8325, 9300, and 10000 Switch
Series.

Configuration options for QoS pool size:

switch(config)# qos pool (1-3) lossless size ?

  <10-90>            The percentage of packet buffer memory to be allocated

to

                     this pool in integer format

  <10.00-90.00>      The percentage of packet buffer memory to be allocated

to

                     this pool in decimal format

  factory-default    Configure the pool size to the default value
Configuration options for headroom size:

switch(config)# qos pool 2 lossless size factory-default percent headroom ?

  <0-10240>        The headroom buffer size in kilobytes

  factory-default  Configure the default headroom buffer size in kilobytes
Configuring a QoS pool size of 60% of the total available buffer memory and a headroom size of 2048 kB
with priorities 1, 2, and 3 mapped to the QoS pool:

switch(config)# qos pool 2 lossless size 60 percent headroom 2048 kbytes

priorities 1,2,3

The  no  form of the  QoS pool  command will remove the configuration from the switch. For example,
removing QoS pool 2:

switch (config)# no qos pool 2

PFC flow-control priorities must be removed on all interfaces prior to removing the QoS pool otherwise
a warning message will be displayed and the QoS pool will not be removed from the configuration. The
warning message reads as follows:

'flow-control priority' must be unconfigured for all interfaces before
deleting pool 2.
Use the  no flow-control priority  command within the appropriate interface context:

switch(config-if)# no flow-control priority

  <0-7>    The packet priority to flow control

Public

QoS pool configuration 72

rx       Honor received PAUSE requests for this priority

  rxtx     Send and receive PAUSE requests for this priority

  tx       Send PAUSE requests for this priority
Reapply the  no qos pool  command:

switch (config)# no qos pool 2

QoS trust

QoS trust can be applied either globally or at the interface level which will override the global setting. The
following considerations should be taken into account when configuring QoS trust:

•  L2 communications between the switch and the host must leverage the 802.1Q tag meaning the

interface between the switch and host must be a trunk link.

•  L2 switch fabric 802.1Q tags must be configured between target and initiator across the layer 2 fabric.

•  L3 switch fabric must sync the appropriate CoS map to local preferences with the DCSP map local

preferences. This is to ensure appropriate mapping for CoS and DSCP markings across the network.

Set a global trust setting or leave global QoS trust the default setting. Override the global trust setting on
specific interfaces as desired.

NOTE
QoS trust is set to none by default.

Subtopics

Layer 3 CoS-DSCP markings
Verifying trust settings

Public

QoS trust 73

Layer 3 CoS-DSCP markings

About this task

A remark policy may be advantageous in order to ensure that the local priority derived from the "trusted"
CoS value is remarked to the desired DSCP code point for transmission across the IP fabric. The diagram
illustrates an example of layer 3 switch configuration with remark policy:

Configuration steps:

Procedure

1.  Switch A

a.  A classifier is applied to match traffic with a priority code point (PCP) of 4

b.  A policy is applied to remark the classified traffic to the desired DSCP code point (CS4)

c.  The policy is applied to the switch egress interface

2.  Switch C

a.  A classifier is applied to match traffic with a DSCP code point of CS4

b.  A policy is applied to remark the classified traffic to the local-priority of 4 (CoS 4)

c.  The policy is applied to the ingress interface (facing the initiator host)

3.  Switch C

A classifier is applied to match traffic with a PCP of 4

A policy is applied to remark the classified traffic to the desired DSCP code point (CS4 in this example)

Public

Layer 3 CoS-DSCP markings 74

The policy is applied to the switch egress interface

4.  Switch A

A classifier is applied to match traffic with a DSCP code point of CS4

A policy is applied to remark the classified traffic to the local-priority of 4 (CoS 4)

The policy is applied to the routed ingress interface (facing the target host)

NOTE

The policies applied ensure that the DSCP value is consistent across the L3
network. At the final hop, the DSCP values is mapped to the correct CoS value
for transmission to the target host. The policy is applied to the reverse flow.

Verifying trust settings

Global trust verification

switch# show qos trust

qos trust cos
Interface trust verification

switch# show interface 1/1/1 qos

Interface 1/1/1 is up

 Admin state is up

 qos trust cos (override)

 qos queue-profile factory-default (global)

 qos schedule-profile factory-default (global)

Troubleshooting data center bridging

About this task

It is assumed that prior to engaging in troubleshooting that host targets and initiators have network
connectivity, are using DCBx, and that hosts are supporting appropriate DCB protocols like PFC. Checks
should be applied to every switch hop. The following flow chart represents the HPE Aruba Networking-
recommended data center bridging troubleshooting flow supporting common DCB implementation:

Public

Verifying trust settings 75

Procedure

1.  Verify that host target/initiator configurations are using 801.Q tagged frames to support the 802.1p

field.

Check that both host and initiator are using 802.1Q tagged frames between host and switch. This
requires the switch interface to be configured as a trunk interface supporting the appropriate VLANs.
Check that the appropriate qos trust setting is applied to the interface. This can either globally or via
the interface context with the qos trust and show interface 1/1/1 qos commands. The qos trust setting
should be set to qos trust cos if the host is supporting PFC as well as DCBx and is configured to use the
appropriate CoS setting for a specific lossless traffic flow.

2.  Validate DCBx application and QoS Pools

NOTE

Only applicable to the HPE Aruba Networking 8325, 9300, and 10000 Switch
Series

Validate that DCBx is configured on the correct interfaces, that the adjacent neighbor is using the
correct DCBx version, and using the same PFC priority. If DCBx is configured and the PFC priority
matches at either end for the link, the following output is displayed:

switch# show dcbx interface 1/1/1

DCBx admin state           : enabled

DCBx operational state     : active

DCBx version               : local = ieee, remote = ieee

PFC operational state      : active
Mismatch  Advertisement              Local    Peer

--------- -------------------------- -------- ----

Priority Flow Control (PFC)

          Willing:                   No       No

Public

Troubleshooting data center bridging 76

MACsec Bypass Capability:  No       No

          Max PFC Traffic Classes:   2        2

          Priority 0:                False    False

          Priority 1:                False    False

          Priority 2:                False    False

          Priority 3:                False    False

          Priority 4:                True     True

          Priority 5:                False    False

          Priority 6:                False    False

          Priority 7:                False    False

Output omiitted for brevity

switch(config)# show qos pool config

Global Packet-Buffer Configuration and Status (in

Kbytes)

                                        Sum of         Applied

Configured                                           Port

Priority        Priority

  Packet Buffer Pools Size              Limits         Mapping

Mapping

-------------------------------------------------------------------------

---

  Lossy Pool          9546                  --     0,1,2,5,6,7

0,1,2,5,6,7

  Lossless Pool 1     7546 (30.00%)         --

4               4

  Headroom Pool 1     2000                   0

--              --

  Lossless Pool 2     9728 (40.00%)         --

3               3

  Headroom Pool 2     3000                   0

--              --
  Reserved Memory     948                   --

--              --

-------------------------------------------------------------------------

---

  TOTAL:                   32768

3.  Verify qos-queue profile and qos schedule-profile

Verify that the qos-queue profile and the global qos schedule-profile have been applied. A single
qos queue-profile is applied to the system. A schedule is always applied to all interfaces (either
the globally configured schedule profile, an interface-override schedule profile, or the factory-default

Public

Troubleshooting data center bridging 77

schedule-profile if the configuration cannot be applied). Each port can have its own schedule profile.
Verify that the correct QoS queue profile is applied. An example of the QoS queue profile 4qp applied to
the system:

switch# show qos queue-profile

profile_status profile_name

-------------- ------------

complete       3qp

applied        4qp

complete       SMB

complete       factory-default
Verify that the correct QoS schedule profile is applied to an interface. An example of the QoS schedule
profile 4sp applied to the system:

switch# show interface 1/1/1 qos

Interface 1/1/1 is up

 Admin state is up

 qos trust cos (override)

 qos queue-profile 4qp (global)

 qos schedule-profile 4sp (global)

4.  Check DCBx TLV and PFC Configurations

Verify that the correct DCBx application TLV is configured and has the correct priority using the show
dcbx interface command.

Verify that appropriate interfaces have PFC configured:

switch# show interface 1/1/2

interface 1/1/2

    no shutdown

    flow-control priority rxtx 4

    no routing

    vlan trunk native 1
    vlan trunk allowed 1,110

    qos trust cos

Output omitted for brevity

QoS commands

Select a command from the list in the left navigation menu..

Subtopics

Public

QoS commands 78

apply qos threshold-profile
clear queue-monitor interface
dcbx application
dwrr queue
flow-control buffer cable-length
forwarding-mode
lldp dcbx disable
lldp dcbx (per interface)
lldp dcbx (global)
map queue
name queue
qos cos-map
qos dscp-map
qos dscp
qos egress-rewrite
qos egress-rewrite-map
qos pool
qos queue-profile
qos schedule-profile
qos shape
qos threshold-profile
qos trust
queue action
queue-monitor
queue-monitor polling-interval seconds
rate-limit
show dcbx interface
show forwarding-mode
show interface qos
show interface qos buffers
show interface queues
show interface queue-monitor
show interface queue-monitor status
show qos cos-map
show qos dscp-map
show qos egress-rewrite-map
show qos pool
show qos queue-profile
show qos schedule-profile
show qos threshold-profile
show qos trust
show queue-monitor status
strict queue

Public

QoS commands 79

apply qos threshold-profile

Syntax

NOTE

Only supported on the 8325, 9300, and 10000 Switch Series.

apply qos threshold-profile <THRESHOLD-NAME>

no apply qos threshold-profile

Description

Applies a threshold profile globally to all Ethernet and LAG interfaces on the switch, or to a specific interface.
When applied globally, the specified threshold profile is configured only on Ethernet interfaces and LAGs
that do not already have their own schedule profile.

The same profile can be applied both globally and locally to an interface. This guarantees that an interface
always uses the specified threshold profile, even if the global profile is changed.

The no form of this command removes the specified threshold profile from an interface, and causes it to use
the global threshold profile. This is the only way to remove a threshold profile override from an interface. A
profile can only be deleted once it is no longer applied to any interface.

Parameter

Description

<THRESHOLD‐NAME>

Specifies the name of the threshold profile to apply. Range: 1 to
64 alphanumeric characters, including period (.), underscore (_),
and hyphen (‐).

Example Applying the threshold profile mythreshold to all interfaces that do not have an applied profile:
switch(config)# apply qos threshold-profile mythreshold

Command History

Release

Modification

10.07 or earlier

‐‐

Public

apply qos threshold-profile 80

Command Information

Platforms

Command context

Authority

config
config‐if
config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

8325

8325H

8325P

9300

9300S

10000

10040

clear queue-monitor interface

Syntax

clear queue-monitor interface [<IFNAME>|<IFRANGE>]

Description

Clear the data collected on an interface since enabling queue monitoring. If no interfaces are specified,
perform a clear of data collected on all interfaces with queue monitoring enabled.

Parameter

<IFNAME>

Description

Name of the interface.

Format: <MEMBER>/<SLOT>/<PORT>

<IFRANGE>

Range of interfaces.

Format: <MEMBER>/<SLOT>/<PORT>‐<MEMBER>/<SLOT>
/<PORT>

Examples

Clearing queue monitor data collected on interface 1/1/1:

Public

clear queue-monitor interface 81

config)# clear queue-monitor interface 1/1/1

Warning: clearing collected queue monitor statistics will be reflected

in all CLI sessions, any agents running in the analytics engine, and any

external systems monitoring switch statistics.

Continue (y/n)? y
Clearing queue monitor data collected on interfaces 1/1/1 and 1/1/2:

config)# clear queue-monitor interface 1/1/1-1/1/2

Warning: clearing collected queue monitor statistics will be reflected

in all CLI sessions, any agents running in the analytics engine, and any

external systems monitoring switch statistics.

Continue (y/n)? y
Clearing all queue monitor data collected on all interfaces:

config)# clear queue-monitor interface

Warning: clearing collected queue monitor statistics will be reflected

in all CLI sessions, any agents running in the analytics engine, and any

external systems monitoring switch statistics.

Continue (y/n)? y

Related Commands

Command

Description

queue‐monitor

Command History

Release

10.15

This command enables the queue monitoring feature, allowing the switch to coll
ect queue statistics at 10‐second time intervals. These aggregate statistics ca
n be used to monitor network health, troubleshoot network issues, and identify
normal network behavior patterns and performance anomalies. This feature is di
sabled by default, but can be enabled on a maximum of 52 interfaces per switch
.

Modification

Command introduced on 8100, 8325, 8325H, 8325P, 8360, 9300, 9300S and 1
0000 Switch series

Public

clear queue-monitor interface 82

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

8325

8325H

8325P

9300

9300S

10000

dcbx application

Syntax

dcbx application {iscsi | tcp-sctp <PORT-NUM> | tcp-sctp-udp <PORT-NUM> |

tcp-udp <PORT-NUM>

  | udp <PORT-NUM> | ether <ETHERTYPE>} priority <PRIORITY>

no dcbx application

Description

Configures application to priority map that gets advertised in DCBx application priority messages. This tells
the DCBx peer to send the application traffic with the configured priority so that the traffic is treated as
lossless. Multiple applications can be configured in this manner. PFC lossless priority configured on the
switch should be the same as this priority.

The no form of this command removes the existing configuration.

Parameter

iscsi

Description

Specifies a physical port on the switch. TCP ports 860 and 326
0.

tcp‐sctp <PORT‐NUM>

Specifies the traffic for a specified TCP or SCTP port. Range: 1
to 65535.

tcp‐sctp‐udp <PORT‐NUM>

Specifies the traffic for a specified TCP or SCTP or UDP port. Ra
nge: 1 to 65535.

Public

dcbx application 83

Parameter

Description

Specifies the traffic for a specified TCP or UDP port. Range: 1 to
65535.

Specifies the traffic for a specified UDP port. Range: 1 to 65535
.

Specifies the traffic for a specific Ethernet type. Range: 1536 to
65535.

Specifies the application priority. Range: 0 to 7.

tcp‐udp <PORT‐NUM>

udp <PORT‐NUM>

<ETHERTYPE>

<PRIORITY>

Usage

•

In CEE DCBx version, the following traffic type configurations are sent using application TLVs:

◦  Ethertype

◦

iSCSI

◦  TCP-UDP

•

In IEEE DCBx version, the following traffic type configurations are sent using application TLVs:

◦  Ethertype

◦

iSCSI

◦  TCP-SCTP

◦  TCP-SCTP-UDP

◦  UDP

Examples

Mapping iSCSI traffic to priority 5.

switch(config)# dcbx application iscsi priority 5

Mapping TCP or SCTP traffic with port 860 to priority 3.

switch(config)# dcbx application tcp-sctp 860 priority 3

Public

dcbx application 84

Command History

Release

10.08

Modification

Added a parameter option tcp‐udp.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

8320

8325

8325H

8325P

9300

9300S

10000

10040

dwrr queue

Syntax

dwrr queue <QUEUE-NUMBER> weight <WEIGHT> [max-bandwidth <RATE> {kbps|

percent} [burst <SIZE>]]

no dwrr queue <QUEUE-NUMBER> [weight <WEIGHT> [max-bandwidth <RATE> {kbps|

percent} [burst <SIZE>]]

Description

Assigns the deficit weighted round robin (DWRR) algorithm and its weight to a queue in a schedule profile.
DWRR allocates available bandwidth among all non-empty queues in relation to the queue weights.

Egress queue shaping can be configured using the max-bandwidth option to limit the amount of traffic
transmitted per output queue at all times, even when there is leftover bandwidth available on the port. The
buffer associated with each egress queue stores the excess traffic to smooth the output rate. Sustained rates

Public

dwrr queue 85

of traffic above the maximum bandwidth will eventually fill the output queue, causing tail drops. Use show
interface < IF-NAME > queues to determine if any tail-drop errors have occurred.

Use show qos schedule-profile <NAME> to view the settings of a specific schedule profile.

To remove only egress queue shaping, re-enter the dwrr queue command without the max-bandwidth
parameter.

The no form of this command removes the DWRR algorithm from a queue in a schedule profile.

Parameter

<QUEUE‐NUMBER>

Description

Specifies the queue number. Range: 0 to 7.

Specifies the scheduling weight. Range: 1 to 127.

 weight <WEIGHT>

max‐bandwidth <RATE>

Specifies the maximum bandwidth rate allowed on the queue in
kbps. Range: 64 to 100000000. Alternatively, the maximum ba
ndwidth rate can be configured on the queue as a percentage o
f the port shape or link bandwidth if a port shape is not configu
red. The allowed range is 1‐100.

burst <SIZE>

Specifies the maximum burst size allowed on the queue in kby
tes. Range: 1 to 1073.* Default: 32.

Examples

Assigning DWRR with a weight of 17 to queue 2 in the schedule profile MySchedule:

switch(config)# qos schedule-profile MySchedule

switch(config-schedule)# dwrr queue 2 weight 17

Deleting DWRR for queue 2 from the schedule profile MySchedule:

switch(config)# qos schedule-profile MySchedule

switch(config-schedule)# no dwrr queue 2

Command History

Release

10.13

Modification

Added max‐bandwidth and burst parameters.

10.07 or earlier

‐‐

Public

dwrr queue 86

Command Information

Platforms

Command context

Authority

config‐
schedule‐<NAME>

Administrators or local user group members with execution righ
ts for this command.

8320

8325

8325H

8325P

9300

9300S

10000

10040

flow-control buffer cable-length

Syntax

flow-control buffer cable-length {auto|<VALUE>}

no flow-control buffer cable-length {auto|<VALUE>}

Description

Configures the cable length value in meters used to calculate the headroom buffer size if an explicit
headroom buffer limit is not configured and flow-control is enabled. If auto is used then the L1 reported
cable length is used to calculate the headroom buffer size.

If no headroom limit or cable length configuration is specified (or cable-length auto is specified but hardware
is not reporting a cable length) then a default cable length of 350 meters is used to compute the headroom
limit.

The no form of this command removes the existing cable length configuration.

Parameter

auto

<VALUE>

Description

Specifies the interface‐detected cable length.

Specifies cable length value in meters.

Public

flow-control buffer cable-length 87

Examples

Configuring a cable length of 400 meters on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# flow-control buffer cable-length 400

Removing the configured cable length value of 400 meters on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# no flow-control buffer cable-length 400

Configuring interface-detected cable length on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# flow-control buffer cable-length auto

Removing the configuration for interface-detected cable length on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# no flow-control buffer cable-length auto

Command History

Release

10.13

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config‐if

Administrators or local user group members with execution righ
ts for this command.

8325

8325H

8325P

9300

9300S

10000

10040

Public

flow-control buffer cable-length 88

forwarding-mode

Syntax

forwarding-mode {cut-through | store-and-forward}

[no] forwarding-mode cut-through

Description

Configures cut-through or store-and-forward forwarding mode for all ports. Cut-through forwarding mode
enables fast processing of traffic to allow for lower latency and higher performance. Packets begin
transmission while still being received if conditions allow it. Store-and-forward forwarding mode allows
packets to be queued before getting transmitted.

The no version of this command can be used to disable cut-through mode and return the switch to the
default store-and-forward forwarding mode.

NOTE

Cut-through forwarding mode is not supported on ports with linked speeds less
than 10G or ports with Link Level Flow Control (LLFC) Rx enabled.

Parameter

cut‐through

store‐and‐forward

Description

Enables cut‐through forwarding mode. This forwarding mode
is recommended for improved performance.

Default. Enables store‐and‐forward forwarding mode. All por
ts on the switch are always configured with store‐and‐forwa
rd mode by default. If no forwarding mode is configured for the
switch, all ports will be configured with store‐and‐forward m
ode.

Examples

Setting the forwarding mode for all ports to cut-through mode:

switch(config)# forwarding-mode cut-through

Setting the forwarding mode for all ports to store-and-forward mode:

switch(config)# forwarding-mode store-and-forward

Public

forwarding-mode 89

Command History

Release

Modification

10.15.1000

Command introduced on 8325H Switch series.

Command Information

Platforms

Command context

Authority

8325H

config‐if

Administrators or local user group members with execution righ
ts for this command.

lldp dcbx disable

Syntax

lldp dcbx disable

no lldp dcbx disable

Description

Disables DCBx on an interface.

The no form of this command removes the DCBx configuration from the interface, which will then default to
the global configuration.

Usage

If the interface command specifies a different version than the global configuration, it overrides the globally
configured DCBx version. If the command is executed without specifying a version, the IEEE version is
configured.

Examples

Disabling DCBx on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# lldp dcbx disable

Reverting interface 1/1/1 to the global DCBx configuration:

Public

lldp dcbx disable 90

switch(config)# interface 1/1/1

switch(config-if)# no lldp dcbx

Command History

Release

10.08

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config‐if

Administrators or local user group members with execution righ
ts for this command.

8320

8325

8325H

8325P

10000

lldp dcbx (per interface)

Syntax

lldp dcbx [version {cee|ieee}]

no lldp dcbx [version {cee|ieee}]

Description

Enables DCBx on an interface. By default, an interface follows the global DCBx configuration. DCBx must be
enabled globally for the interface configuration to take effect.

The no form of this command removes the port-override DCBx configuration and reverts the port behavior
to the global DCBx configuration.

Parameter

Description

version { cee | ieee }

Configures the DCBx version in either CEE (Converged Enhance
d Ethernet) or IEEE (IEEE 802.1Qaz). Default version: IEEE

Public

lldp dcbx (per interface) 91

Usage

If the interface command specifies a different version than the global configuration, it overrides the globally
configured DCBx version. If the command is executed without specifying a version, the IEEE version is
configured.

Examples

Enabling DCBx on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# lldp dcbx

Disabling DCBx on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# no lldp dcbx

Enabling DCBx on interface 1/1/1 with the CEE version:

switch(config)# interface 1/1/1

switch(config-if)# lldp dcbx version cee

Enabling DCBx and configuring PFC for priority 4 on interface 1/1/1.

NOTE

Priority Flow Control (PFC) commands are only supported on the 8100, 8325,
9300, and 8360 Switch Series.

switch(config)# interface 1/1/1

switch(config-if)# lldp dcbx

switch(config-if)# flow-control priority 4

Command History

Release

10.08

Modification

Added a parameter 'version'

10.07 or earlier

‐‐

Public

lldp dcbx (per interface) 92

Command Information

Platforms

Command context

Authority

config‐if

Administrators or local user group members with execution righ
ts for this command.

8320

8325

8325H

8325P

9300

10000

lldp dcbx (global)

Syntax

lldp dcbx [version {cee|ieee}]

no lldp dcbx [version {cee|ieee}]

Description

Enables advertisement of the DCBx TLVs in LLDP packets either globally or per interface. By default, DCBx
is disabled in the switch.

The no form of this command disables DCBx advertisement.

Parameter

Description

version { cee | ieee }

Configures the DCBx version in either CEE (Converged Enhance
d Ethernet) or IEEE (IEEE 802.1Qaz). Default version: IEEE

Examples

Enabling DCBx globally with default version:

switch(config)# lldp dcbx

Disabling DCBx globally:

switch(config)# no lldp dcbx

Enabling DCBx globally with the CEE version:

Public

lldp dcbx (global) 93

switch(config)# lldp dcbx version cee

Enabling DCBx on an interface with default version:

switch(config-if)# lldp dcbx

Disabling DCBx on an interface:

switch(config-if)# no lldp dcbx

Enabling DCBx on an interface with the CEE version:

switch(config-if)# lldp dcbx version cee

Command History

Release

10.08

Modification

Added optional CEE and IEEE parameters.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config
config‐if

Administrators or local user group members with execution righ
ts for this command.

8320

8325

8325H

8325P

9300

9300S

10000

10040

map queue

Public

map queue 94

Syntax

map queue <QUEUE-NUMBER> local-priority <PRIORITY-NUMBER>

no map queue <QUEUE-NUMBER> [local-priority <PRIORITY-NUMBER>]

Description

Assigns a local priority to a queue in a queue profile. By default, the larger the queue number the higher its
priority. A queue without a local priority value assigned to it is not used to store packets. The same queue
can be assigned multiple local priorities.

The no form of this command removes the specified local priority from a specific queue. If no local priority
number is specified, then all local priorities are removed from the queue.

Parameter

Description

Specifies the queue number. Range: 0 to 7.

<QUEUE‐NUMBER>

<PRIORITY‐NUMBER>

Usage

Specifies the local priority. Range: 0 to 7, where 0 is the lowest
priority and 7 is the highest.

For a queue profile to be complete and ready to be applied, all eight local priorities must be mapped to a
queue. Any local priority used by interface Priority-based Flow Control (PFC) must be the only local priority
mapped to its queue. In order for PFC pausing to work as intended, no other local priorities should be
mapped to that same queue. This queue mapping should be configured during initial switch provisioning
and only changed during maintenance periods where all ports are disabled.

NOTE

PFC is only supported on the 8325, 9300, and 10000 Series Switch

The following commands illustrate a valid configuration, where every local priority value is assigned to a
queue:

            map queue 0 local-priority 0
            map queue 1 local-priority 1
            map queue 1 local-priority 2

            map queue 3 local-priority 3

            map queue 4 local-priority 4

Public

map queue 95

map queue 5 local-priority 5

            map queue 5 local-priority 6

            map queue 5 local-priority 7

The following commands illustrate an invalid configuration, because local priority 2 is not assigned to a
queue:

            map queue 0 local-priority 0

            map queue 1 local-priority 1

            map queue 2 local-priority 3

            map queue 3 local-priority 4

            map queue 4 local-priority 5

            map queue 5 local-priority 6

            map queue 5 local-priority 7

Examples

Assigning priority 7 to queue 7 in profile myprofile:

switch(config)# qos queue-profile myprofile

switch(config-queue)# map queue 7 local-priority 7

Removing priority 7 from queue 7 in profile myprofile:

switch(config)# qos queue-profile myprofile

switch(config-queue)# no map queue 7 local-priority 7

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

config‐queue

Administrators or local user group members with execution righ
ts for this command.

Public

map queue 96

name queue

Syntax

name queue  <QUEUE-NUMBER>

            <DESCRIPTION>

no name queue  <QUEUE-NUMBER>

Description

Assigns a description to a queue in a queue profile. This is for identification purposes and has no effect on
configuration.

The no form of this command removes the description associated with a queue.

Parameter

Description

Specifies the queue number. Range: 0 to 7.

<QUEUE‐NUMBER>

<DESCRIPTION>

Specifies a queue description for identification purposes. Range
: 1 to 64 alphanumeric characters, including period (.), undersco
re (_), and hyphen (‐).

Examples Assigning the description priority-traffic to queue 7:
switch(config)# qos queue-profile myprofile

switch(config-queue)# name queue 7 priority-traffic

Removing the description from queue 7:
switch(config)# qos queue-profile myprofile

switch(config-queue)# no name queue 7

Command History

Release

Modification

10.07 or earlier

‐‐

Public

name queue 97

Command Information

Platforms

Command context

Authority

All platforms

config‐queue

Administrators or local user group members with execution righ
ts for this command.

qos cos-map

Syntax

qos cos-map <CODE-POINT> local-priority <PRIORITY-NUMBER> [color <COLOR>]

[name <DESCRIPTION>]

no qos cos-map <CODE-POINT>

Description

Defines the local priority assigned to incoming packets for a specific 802.1 VLAN priority code point (CoS)
value. The CoS map values are used to mark incoming packets when QoS trust mode is set to cos. In trust
none mode, CoS map entry 0 is used to set the port default local priority and color.

To see the default CoS map settings, use the following command:

switch# show qos cos-map default

code_point local_priority color   name

---------- -------------- ------- ----

0          1              green   Best_Effort

1          0              green   Background

2          2              green   Excellent_Effort

3          3              green   Critical_Applications
4          4              green   Video

5          5              green   Voice

6          6              green   Internetwork_Control

7          7              green   Network_Control
The no form of this command restores the assignments for a CoS map value to the default setting.

Parameter

Description

Specifies an 802.1 VLAN priority CoS value. Range: 0 to 7. Defa
ult 0.

Public

qos cos-map 98

Parameter

<CODE‐POINT>

Description

local‐priority <PRIORITY‐
NUMBER>

Specifies a local priority value to associate with the  CODE‐PO
INT  value. Range: 0 to 7. Default: 0.

color <COLOR>

Reserved for future use.

name <DESCRIPTION>

Specifies a description for the CoS setting. The name is for iden
tification only, and has no effect on queue configuration. Range
: 1 to 64 alphanumeric characters, including period (.), undersco
re (_), and hyphen (‐).

Usage

Any code point configured for use by interface Priority-based Flow Control (PFC) must be assigned a unique
local priority in the CoS map. No other code point can be assigned that same local priority. This should be
configured during initial switch provisioning and only changed during maintenance periods where all ports
are disabled.

NOTE

PFC is only supported on the 8325, 9300, and 10000 Series Switch

Examples

Mapping CoS value 1 to a local priority of 2:

switch(config)# qos cos-map 1 local-priority 2

Mapping CoS value 1 to the default local priority value:

switch(config)# no qos cos-map 1

Command History

Release

Modification

10.07 or earlier

‐‐

Public

qos cos-map 99

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

8320

8325

8325H

8325P

9300

9300S

10000

10040

qos dscp-map

Syntax

qos dscp-map <CODE-POINT> local-priority <PRIORITY-NUMBER> [color <COLOR>]

[name <DESCRIPTION>]

no qos dscp-map <CODE-POINT>

Description

Defines the local priority color assigned to incoming packets for a specific IP differentiated services code
point (DSCP) value. The DSCP map values are used to prioritize incoming packets when QoS trust mode is
set to dscp.

The no form of this command restores the assignments for a code point to the default setting.

NOTE

Use show qos dscp-map to view the current settings. To see the default DSCP map settings, use the
following command:

switch# show qos dscp-map default
DSCP     code_point cos color   name

-------- ---------- --- ------- ----

000000   0          0   green   CS0

000001   1          0   green

Public

qos dscp-map 100

000010   2          0   green

000011   3          0   green

000100   4          0   green

000101   5          0   green

...

101101   45         5   green

101110   46         5   green   EF

101111   47         5   green

110000   48         6   green   CS6

...

111101   61         7   green

111110   62         7   green

111111   63         7   green

switch# show qos dscp-map default

DSCP     code_point cos  name

-------- ---------- ---  ----

000000   0          0    CS0

000001   1          0

000010   2          0

000011   3          0

000100   4          0

000101   5          0

...

101101   45         5

101110   46         5    EF

101111   47         5

110000   48         6    CS6

...

111100   60         7

111101   61         7

111110   62         7

111111   63         7
switch# show qos dscp-map default

code_point local_priority cos color   name

---------- -------------- --- ------- ----

0          1                  green   CS0

1          1                  green

2          1                  green

3          1                  green

4          1                  green

5          1                  green

...

45         5                  green

Public

qos dscp-map 101

46         5                  green   EF

47         5                  green

48         6                  green   CS6

...

61         7                  green

62         7                  green

63         7                  green

switch# show qos dscp-map default

code_point local_priority color   name

---------- -------------- ------- ----

0          1              green   CS0

1          1              green

2          1              green

3          1              green

4          1              green

5          1              green

...

45         5              green

46         5              green   EF

47         5              green

48         6              green   CS6

...

61         7              green

62         7              green

63         7              green

Parameter

Description

<CODE‐POINT>

Specifies an IP differentiated services code point. Range: 0 to 6
3. Default: 0.

local‐priority <PRIORITY‐
NUMBER>

Specifies a local priority value to associate with the CODE‐PO
INT value. Range: 0 to 7. Default: 0.

color <COLOR>

cos <PCP‐VALUE>

Configures the QoS CoS map color. The supported colors are g
reen, red, and yellow. The default color is green.

Specifies an optional 802.1p VLAN Priority Code Point remark
value. Range: 0 to 7. Default: No remark.

name <DESCRIPTION>

Specifies a description for the DSCP setting. The name is used
for identification only, and has no effect on queue configuration.

Public

qos dscp-map 102

Parameter

Description

Range: 1 to 64 alphanumeric characters, including period (.), un
derscore (_), and hyphen (‐).

Examples Setting code point 1 to a local priority of 2 and a CoS of 0:
switch(config)# qos dscp-map 1 local-priority 2 cos 0

Setting code point 1 to the default value:
switch(config)# no qos dscp-map 1

Setting code point 46 to a Cos of 7 and CoS map color as yellow: Setting code point 41 to a CoS of 6:
Setting code point 41 to the default value: Setting code point 1, 3-5 to a local priority 2 , and CoS color as
green with the description EntryName:
switch(config)# qos dscp-map 1,3-5 local-priority 2 color green name

EntryName

Command History

Release

10.13

Modification

Added <COLOR> parameters.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

8320

8325

8325H

8325P

9300

9300S

10000

10040

Public

qos dscp-map 103

qos dscp

Syntax

qos dscp <CODE-POINT>

no qos dscp

Description

Configures a differentiated services code point (DSCP) remark for an Ethernet or LAG interface. IPV4 and
IPV6 packets that ingress on the interface are remarked at egress using the configured DSCP value.

The remark only occurs when QoS trust mode on the interface is set to none. If a DSCP remark is configured
and then trust mode is subsequently set to cos or dscp, then the DSCP remark is ignored.

The following commands will show the remark status as not applied (incompatible QoS global or port trust
configuration):

•  show running-configuration

•  show interface <INTERFACE-NAME>

•  show interface <INTERFACE-NAME> qos

The no form of this command removes a CoS remark on an interface.

Parameter

Description

Specifies an IP differentiated services code point value. Range:
0 to 63.

<CODE‐POINT>

Usage

Order of operation for arriving IPv4 or IPv6 packets:

1.  Trust none is applied with initial local-priority and color metadata assigned from the CoS Map entry

index 0.

2.  The local-priority value and the queue profile are then used to determine the queue for the packet.

3.  The remark of the packet's DSCP metadata field is performed. When the packet is transmitted, its IPv4

or IPv6 DS header is remarked with the DSCP metadata.

For arriving non-IP packets:

Trust none is applied with initial local-priority and color metadata assigned from the CoS Map entry index 0.
This selects the queue for packet scheduling. The PCP of any tagged non-IP packets is unchanged.

Public

qos dscp 104

Examples

Configuring a DSCP remark of 43 on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# qos trust none

switch(config-if)# qos dscp 43

Deleting a DSCP remark of 43 on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# no dscp 43

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐if
config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

8320

8325

8325H

8325P

9300

9300S

10000

10040

qos egress-rewrite

Syntax

qos egress-rewrite [cos|dscp]

no qos egress-rewrite [cos|dscp]

Public

qos egress-rewrite 105

Description

Enables a rewrite of the 802.1Q VLAN priority code point (PCP) or DSCP values for all traffic egressing
on the configured interface. The PCP or DHCP value is determined by a globally configured egress priority
rewrite map based on the traffic's local priority. Use this command to configure a system-wide mapping from
internal local priorities to 802.1Q VLAN priority code point (PCP) or DSCP values.

The no form of this command disables egress priority rewrite on the interface.

Use show qos egress-rewrite-map to view the current global egress priority rewrite map. Use show qos
egress-rewrite-map default to view the factory default egress priority rewrite map.

NOTE

The mapping from local priority to egress priority is determined by the Egress
Rewrite Map, which can be configured using the qos egress-rewrite-map
command in the global configuration context.

Parameter

cos

dscp

Examples

Description

Enables egress rewrite of the 802.1Q VLAN Priority Code Point
(PCP) value for all traffic egressing on the interface.

Enables an egress rewrite of the DSCP value for all traffic egres
sing on the interface.

Configuring egress rewrite for both PCP and DSCP values on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# qos egress-rewrite cos

switch(config-if)# qos egress-rewrite dscp

Disabling egress priority rewrite:

switch(config-if)# no qos egress-rewrite cos

switch(config-if)# no qos egress-rewrite dscp

Command History

Release

10.18

10.17

Modification

Command updated to support DHCP rewrite on egress.

Command introduced.

Public

qos egress-rewrite 106

Command Information

Platforms

Command context

Authority

8325

8325H

8325P

config‐if
config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

qos egress-rewrite-map

Syntax

qos egress-rewrite-map local-priority <PRIORITY-RANGE> {cos <PCP-VALUE>}|

{ dscp <DSCP-VALUE>}

no qos egress-rewrite-map local-priority <PRIORITY-RANGE> {cos <PCP-VALUE>}|

{ dscp <DSCP-VALUE>}

Description

Configures a system-wide mapping from internal local priority to an 802.1Q VLAN priority code point (PCP)
or DSCP value. The qos egress-rewrite cos command allows the PCP value to be rewritten on egress, and
the qos egress-rewrite dscp command allows the DSCP value to be rewritten on egress. The local priority
associated with a packet affects only its behavior within the switch. By default, it does not influence the
priority value written to the packet upon transmission.

This command, along with its no form, accepts a single local priority, a range of local priorities, or a
comma-separated list of local priorities and ranges. This provides a convenient method for configuring
multiple entries in the map. Note that the specified range is not saved as-is; commands such as show
running-config will display one code point per line, even if a single command configured multiple code
points.

The no form of this command restores the rewrite assignments for one or more local priorities to the
default rewrite assignment. If you specify any parameters in addition to the local priorities, the default
rewrite assignments will only be restored for those local priorities whose current configuration override

Public

qos egress-rewrite-map 107

exactly matches the provided parameters. The current configuration override is the one shown by show
running-config.

NOTE

By default, the Egress Rewrite Map is set to the inverse of the default CoS map.
Therefore, if the CoS map is modified, the Egress Rewrite Map should also be
updated to reflect the changes and maintain consistency.

If you configure a DSCP map, the default Egress Rewrite Map is configured such
that the local priorities correspond to CS<X> values in the default DSCP map.
If the default DSCP map undergoes any change, the Egress Rewrite Map should
also be changed to match the new DSCP map.

Parameter

Description

local‐priority <PRIORITY‐
RANGE>

Specifies a range of priority values or a single priority value. Su
pported values: 0-7.

cos <PCP‐VALUE>

Specifies an 802.1Q VLAN Priority Code Point rewrite value to
associate with the PRIORITY‐RANGE value(s). Supported valu
es: 0-7.

dscp <DSCP‐VALUE>

Specifies a DSCP rewrite value to associate with the PRIORIT
Y-RANGE value(s). Supported values: 0-63.

Examples

Configuring an egress rewrite map for PCP and DSCP values

switch(config)# qos egress-rewrite-map local-priority 6,7 cos 3

switch(config)# qos egress-rewrite-map local-priority 6,7 dscp 5

If you issue the  no qos egress-rewrite-map  command, any  cos  or  dscp  value included with
this command must match the existing map configuration, or the output of this command will display the
following error

switch(config)# qos egress-rewrite-map local-priority 6,7 cos 3

switch(config)# no qos egress-rewrite-map local-priority 6,7 cos 6

local-priority 6: The cos value entered does not match the currently

configured cos value.

local-priority 7: The cos value entered does not match the currently
configured cos value.

Public

qos egress-rewrite-map 108

Command History

Release

10.18

10.17

Modification

The egress rewrite map now supports DSCP values.

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

8325

8325H

8325P

qos pool

Syntax

qos pool <INDEX> lossless size {factory-default|<PERCENT>} percent headroom

{factory-default|<HSIZE>} kbytes [priorities <PRIORITY>]

no qos pool <INDEX> lossless size {factory-default|<PERCENT>} percent

headroom

{factory-default|<HSIZE>} kbytes [priorities <PRIORITY>]

NOTE

This command is not supported on the 8320 Switch Series.

WARNING
It is not recommended to configure PFC on priority 7. This priority is used by
protocol and control traffic, and device operation can be negatively impacted by
pausing of traffic.

Description

Creates or modifies a packet buffer pool for lossless traffic by configuring lossless pool size, headroom buffer
associated with the pool, and the priorities that are mapped to the pool.

Public

qos pool 109

The lossless pool size is a percentage of the total available buffer memory on the device. The headroom pool
memory is allocated from the lossless pool and is used for storing packets that arrive on a port after pause
has been asserted.

The no form of this command removes the QoS pool and returns the memory back to the default lossy pool.

Parameter

<INDEX>

Description

Specifies the index of the lossless pool.

factory‐default

Specifies the default lossless pool or headroom buffer sizes.

Specifies the lossless pool size in percent. Default: 40.6. Range:
10 to 90.

Specifies the headroom buffer size in kilobytes. Factory‐defaul
t size: 3072 kilobytes. Range: 0 to 10240 kilobytes or half the si
ze of the lossless pool, whichever is lower.

Specifies the PFC priorities to be mapped to the pool. Range: 0
to 7.

To map multiple priorities, use a comma‐separated list. Ex: 1,3
,6.

<PERCENT>

<HSIZE>

<PRIORITY>

Usage

•

•

If the switch is configured with PFC and upgraded to 10.08 or a later version, the default lossless pool is
created for existing priorities.

It is recommended to configure PFC or link-level flow control RXTX mode and pools only once on a
running system. Changing the pool or flow control configuration on a running system will cause a brief
disruption in traffic. The reconfiguration also results in packet loss in the data flow. This may affect one,
multiple, or all ports depending on the existing configuration and changes made to it.

Examples

Configuring the QoS pool using lossless pool size and headroom buffer size with one or two PFC assigned to
it:

switch(config)# qos pool 1 lossless size 60 percent headroom 2048 kbytes
priorities 4

switch(config)# qos pool 1 lossless size 60 percent headroom 2048 kbytes

priorities 3,4

Public

qos pool 110

switch(config)# qos pool 1 lossless size factory-default percent headroom

factory-default kbytes priorities 3,4

Removing the QoS pool configuration:

switch(config)# no qos pool 1 lossless size 60 percent headroom 2048 kbytes

priorities 4

Removing a priority from the existing QoS pool configuration:

switch(config)# qos pool 2 lossless size 70 percent headroom 3072 kbytes

priorities 5,6

switch(config)# qos pool 2 lossless size 70 percent headroom 3072 kbytes

priorities 5

Command History

Release

Modification

10.10.1000

Support for 9300 series switches added.

10.10

10.09

10.08

Support for 3 lossless pools added.

Support for 10000 series switches added.

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

8325

8325H

8325P

9300

9300S

10000

10040

Public

qos pool 111

qos queue-profile

Syntax

qos queue-profile <NAME>

no qos queue-profile <NAME>

Description

Creates a new QoS queue profile and switches to the config-queue context for the profile. Or, if the specified
QoS queue profile exists, this command switches to the config-queue context for the profile. A queue profile
maps queues to local-priority values. Each profile has one to eight queues numbered 0 to 7. The larger the
queue number, the higher its priority during transmission scheduling.

The no form of this command removes the specified QoS queue profile. Only profiles that are not currently
applied can be removed.

Parameter

Description

Specifies the name of the QoS queue profile to create or config
ure. Range: 1 to 64 alphanumeric characters, including period (.
), underscore (_), and hyphen (‐).

<NAME>

Examples

Creating the profile myprofile:

switch(config)# qos queue-profile myprofile

switch(config-queue)#
Deleting the profile myprofile:

switch(config)# no qos queue-profile myprofile

Command History

Release

Modification

10.07 or earlier

‐‐

Public

qos queue-profile 112

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

qos schedule-profile

Syntax

qos schedule-profile <NAME>

no qos schedule-profile <NAME>

Description

Creates a QoS schedule profile and switches to the config-schedule context for the profile. If the specified
schedule profile exists, this command switches to the config-schedule context for the profile. The schedule
profile determines the order in which queues are selected to transmit a packet, and the amount of service
defined for each queue.

Parameter

Description

Specifies the name of the QoS queue profile to create or config
ure. Range: 1 to 64 alphanumeric characters, including period (.
), underscore (_), and hyphen (‐).

<NAME>

Usage

Queues in a schedule profile are numbered consecutively starting from zero. Queue zero is the lowest
priority queue. The larger the queue number, the higher priority the queue has in scheduling algorithms.

A profile named factory-default is defined by default and applied to all interfaces. It cannot be edited or
deleted. To see its settings, use the command:

switch# show qos schedule-profile factory-default

queue_num algorithm weight
--------- --------- ------

0         dwrr      1

1         dwrr      1

2         dwrr      1

Public

qos schedule-profile 113

3         dwrr      1

4         dwrr      1

5         dwrr      1

6         dwrr      1

7         dwrr      1
A profile named strict is predefined and cannot be edited or deleted. The strict profile services all queues of
the queue profile to which it is applied, using the strict priority algorithm.

A schedule profile must be defined on all interfaces at all times.

There are two permitted configurations for a schedule profile:

1.  All queues use the same scheduling algorithm (for example, WFQ).

2.  The highest queue number uses strict priority, and all remaining (lower) queues use the same algorithm

(for example, WFQ). This supports priority scheduling behavior necessary for the IETF RFC 3246
Expedited Forwarding specification (https://tools.ietf.org/html/rfc3246).

3.  All queues use the same scheduling algorithm (for example, DWRR).

4.  The highest queue number uses strict priority, and all remaining (lower) queues use the same algorithm
(for example, DWRR). This supports priority scheduling behavior necessary for the IETF RFC 3246
Expedited Forwarding specification (https://tools.ietf.org/html/rfc3246).

5.  All queues use the same scheduling algorithm (for example, GMB).

6.  The highest queue number uses strict priority, and all remaining (lower) queues use the same algorithm

(for example, GMB). This supports priority scheduling behavior necessary for the IEFT RFC 3246
Expedited Forwarding specification (https://tools.ietf.org/html/rfc3246).

Only limited changes can be made to an applied schedule profile:

•  The weight of a wfq queue.

•  The bandwidth of a strict queue or a min-bandwidth queue.

•  The algorithm of the strict or WFQ queue can be swapped between WFQ and strict, and vice versa.

•  The weight of a dwrr queue.

•  The bandwidth of a strict queue or a min-bandwidth queue.

•  The algorithm of the highest numbered queue can be swapped between dwrr and strict, and vice versa.

•  The percentage of a GMB queue.

•  The bandwidth of a strict queue or a min-bandwidth queue.

•  The algorithm of the highest numbered queue can be swapped between GMB and strict, and vice versa.

Applicable to REST: Any other changes will result in an unusable schedule profile, and the switch will revert
to the factory-default profile until the profile is corrected.

Public

qos schedule-profile 114

The no form of this command removes the specified QoS schedule profile when it is not applied. Only
profiles that are not currently applied to an interface can be removed.

Examples

Creating the schedule profile MySchedule:

switch(config)# qos schedule-profile MySchedule

switch(config-schedule)#
Deleting the schedule profile MySchedule:

switch(config)# no qos schedule-profile MySchedule

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

qos shape

Syntax

qos shape <RATE> [kbps|percent] [burst <SIZE>]

no qos shape

Description

Limits the egress bandwidth on an interface to a value that is lower than its line rate. An optional burst value
may also be specified.

Errors will be generated in the following events:

•  A user configures a port-shaping value that is greater than 100 percent

Public

qos shape 115

•  A user configures a kbps port-shaping value that is less than the supported minimum kbps value. The

supported minimum kbps shaping value can be retrieved using the show capacities command.

The no form of this command removes shaping from an interface.

Parameter

Description

Specifies the maximum traffic rate in kbps. Range: 1 to 100000
000. 1 to 400000000 for the HPE Aruba Networking 9300/93
00S Switch Series. Alternatively, the bandwidth can also be conf
igured as a percentage of link bandwidth. The supported range
is 1‐100. Default units are kilobits per second.

Specifies the maximum burst size in kilobytes. Range: 1 to 128.
Default: 32.

<RATE>

<SIZE>

Usage

When the traffic rate destined for the port exceeds the configured egress bandwidth, the switch will buffer
the excess up to the limit of the queues. Rates larger than the interface's link rate will have no effect. When
set on a LAG, each member Ethernet port independently shapes its egress bandwidth to the specified rate.

Examples

Configuring an egress port shaping rate of 400 Mbps on interface 1/1/1 :

switch(config)# interface 1/1/1

switch(config-if)# qos shape 400000 kbps

Configuring an egress port-shaping rate of 40% on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# qos shape 40 percent

Deleting egress port shaping on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# no qos shape

Command History

Release

Modification

10.07 or earlier

‐‐

Public

qos shape 116

Command Information

Platforms

Command context

Authority

config‐if

Administrators or local user group members with execution righ
ts for this command.

8320

8325

8325H

8325P

9300

9300S

10000

10040

qos threshold-profile

Syntax

qos threshold-profile <NAME>

no qos threshold-profile <NAME>

Description

Creates a QoS threshold profile and switches to the config-threshold context for the profile. If the specified
threshold profile exists, this command switches to the config-threshold context for the existing profile. The
threshold profile determines the action to take when a threshold is exceeded for each queue.

A threshold profile is composed of up to 8 queues, numbered from 0 to 7. Each queue defines the action to
take when buffer utilization exceeds a specific threshold.

Configure queues with the command queue.

The no form of this command removes the specified QoS threshold profile. Only profiles that are not
currently applied to an interface can be removed.

Parameter

Description

Specifies the name of the QoS threshold profile to create or co
nfigure. Range: 1 to 64 alphanumeric characters, including peri
od (.), underscore (_), and hyphen (‐).

Public

qos threshold-profile 117

Description

Parameter

<NAME>

Usage

Queues in a threshold profile can be any valid queue number, although it is also valid to create a threshold
profile with no queues specified. Queue zero is the minimum allowed queue number. The maximum allowed
queue number may vary by product. For products supporting eight queues, the largest queue number is
seven. If an applied threshold profile specifies configuration of a queue number that is not in use based on
the configured queue profile, the threshold configuration of that unused queue is ignored.

Examples

Creating the threshold profile mythreshold:

switch(config)# qos threshold-profile mythreshold

switch(config-threshold)#
Deleting the threshold profile MySchedule:

switch(config)# no qos threshold-profile mythreshold

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

8325

8325H

8325P

9300

9300S

10000

10040

Public

qos threshold-profile 118

qos trust

Syntax

Description

In the config context:

•  This command sets the trust mode that is globally applied to all interfaces that do not have a trust mode

configured.

•  The no form of this command restores all interfaces that do not currently have a trust mode configured

to the default setting.

In the config-if context:

•  This command sets the trust mode override for a specific interface.

•  The no form of this command clears a trust mode override. The interface then uses the global setting.

This is the only way to remove a trust mode override.

•  When configuring  qos trust none , a local-priority and color may be optionally specified. In such

case, all traffic entering the device on this interface will be assigned the specified value.

Parameter

Description

none

Ignores all packet headers. Ingress packets are assigned the l
ocal priority and color values configured for CoS map entry 0.
Default.

local‐priority <PRIORITY‐
NUMBER>

Specifies a local priority for ingress packets on the interface. Ra
nge: 0‐7.

Public

qos trust 119

Parameter

color <COLOR>

NOTE

Description

Specifies a color for ingress packets on the interface. Options: g
reen (default), yellow and red.

On 8325, 8325H and 8325P Switch Series, this optional configuration enables
you to override the default local-priority or color assigned to packets arriving
on an interface. By default, when the feature is not enabled, the local-priority and
color are derived from CoS map entry 0. However, enabling the feature allows
you to specify a local-priority and/or color, bypassing the default settings in CoS
map entry 0. The specified local-priority determines the queue used by packets,
as mapped by the queue profile, while the specified color provides preferential
handling of packets within a queue during times of congestion. The preferential
treatment is subject to the threshold profile applied to the egress queue.

Example

Setting the global trust mode to dscp, which is applied to all interfaces that do not already have an
individual trust mode configured. An override is then applied to interface 2/2/2, and LAG 100, setting trust
mode to cos:

            switch(config)# qos trust dscp

switch(config)# interface 2/2/2

switch(config-if)# qos trust cos

switch(config-if)# interface lag 100

switch(config-if)# qos trust cos
In the example below, 1 is the local-priority value. This overrides the global  qos trust dscp ,
causing all arriving packets at interface 1/1/1 to be assigned the specified priority, and thereby ignoring the
configuration in CoS map entry 0. Optionally, the color can be set as well:

            switch(config)# interface 1/1/1

switch(config-if)# qos trust none local-priority 1 color yellow

switch(config)# interface 1/1/1

switch(config-if)# no qos trust
Display ethernet port 6 with port-specific configuration to specify the default local-priority. The color
configuration is displayed as well:

            switch# show interface 1/1/6
Interface 1/1/6 is up

 Admin state is up

 Link state: up for 16 seconds (since Tue Sep 12 00:11:36 UTC 2023)

 Link transitions: 1

Public

qos trust 120

Description:

 Persona:

 Hardware: Ethernet, MAC Address: 3c:2c:99:ff:ea:97

 MTU 1500

 Type 10G-LR / 10G SFP+ LR

 Full-duplex

 qos trust none local-priority 1 color yellow (override)

 rate-limit broadcast 1 percent (99968 kbps actual)

 Speed 10000 Mb/s

 Auto-negotiation is off

 Flow-control: off
Display QoS on ethernet port 5:

            switch# show interface 1/1/5 qos

Interface 1/1/5 is down

 Admin state is up

 qos trust none local-priority 1 color green (override)

 qos queue-profile factory-default (global)

 qos schedule-profile EQSExample (override)

 qos dscp 47

 rate-limit unknown-unicast 64 pps (64 pps actual)

 rate-limit broadcast 500 pps (500 pps actual)

 qos shape 200000 kbps (200064 kbps actual) burst 70 (70 actual)

               Maximum  Bandwidth      Burst

Queue        Bandwidth  Units           (KB)

--------------------------------------------

Q1            10082461  kbps             120

Q4            20164923  kbps              32

Q7            30247384  kbps             120

Override of DSCP value in the interface context:

            switch(config)# interface 1/1/1

switch(config-if)# qos trust none

switch(config-if)# qos dscp 1
Override of CoS value in the interface context:

            switch(config)# interface 1/1/1

Public

qos trust 121

switch(config-if)# qos trust none

switch(config-if)# qos cos 1

NOTE

The warning message QoS port remark configurations are not applied when the
QoS trust mode is cos or dscp, is seen if a port trust command other than trust
none is attempted when there is already a remark configuration on the port. To
restore the old remark configuration, configure the port trust mode to none.

NOTE

The warning message QoS port remark configurations are not applied when the
global QoS trust mode is cos or dscp, is seen if a port no qos trust command
is attempted when there is already a remark configuration on the port and the
global trust mode is not none. To re-apply the remark configuration, set the port
trust mode to none.

Command History

Release

10.17

Modification

Added  local‐priority  and  color  parameters for trust mode none o
n 8325, 8325H and 8325P Switch Series.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config
config‐if
config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

queue action

Syntax

WRED

HPE Aruba Networking 8320, 8325, 8325P, 8325H, 9300/9300S, 9300S, 10000 Switch Series

Public

queue action 122

queue <0-7> action wred-resp { green | yellow | red } min-threshold <WRED-

MIN-LIMIT> kbytes max-threshold <WRED-MAX-LIMIT> kbytes max-prob <WRED-MAX-

PROB> percent

queue <0-7> action wred-non-resp { green | yellow | red } min-threshold

<WRED-MIN-LIMIT> kbytes max-threshold <WRED-MAX-LIMIT> kbytes max-prob

<WRED-MAX-PROB> percent

ECN

HPE Aruba Networking 8325, 8325H, 8325P, 9300/9300S, 10000 Switch Series

queue <0-7> action ecn all threshold <LIMIT> kbytes

queue <0-7> action ecn all min-threshold <MIN-LIMIT> kbytes max-threshold

<MAX-LIMIT> kbytes

no queue <0-7>

Description

Defines the threshold settings and action for a specified queue in a threshold-profile. For ECN, when
queue utilization exceeds the threshold value, ECT (ECN-Capable Transport) packets will be CE (Congestion
Encountered) marked when transmitted.

For WRED, when queue utilization exceeds the threshold value, WRED action will randomly early-drop
packets to signal congestion. More than one WRED action can be configured on a single queue for different
packet colors.

When supported, dual threshold configures an ECN action based on the following queue thresholds:

•  When the queue exceeds the minimum threshold limit, the ECN action marks ECT packets CE with

increasing probability.

•  When the queue exceeds the maximum threshold limit, the ECN action marks all ECT packets CE.

The no form of this command removes the settings for a queue.

Parameter

Description

Specifies the queue number. Range: 0 to 7.

<0‐7>

<LIMIT>, <MIN‐LIMIT>, <MAX‐
LIMIT>

Specifies the threshold value in kilobytes. Range: 0 to 6000 kilo
bytes.

Public

queue action 123

Parameter

Description

<WRED‐MIN‐LIMIT>

<WRED‐MAX‐LIMIT>

<WRED‐MAX‐PROB>

Specifies the queue minimum utilization threshold value for WR
ED to probabilistically start dropping packets.

Specifies the queue maximum utilization threshold value for W
RED, after which every packet is dropped.

Specifies the maximum WRED probability of dropping a packet
for the specified queue.

NOTE

Applicable only on the HPE Aruba Networking
6400v2, 8100, 8360v2, 8320, 8325, 8400, 930
0/9300S, and 10000 Switch Series.

Examples

Assigning a threshold to queue 7 in profile mythreshold:

switch(config)# qos threshold-profile mythreshold

switch(config-threshold)# queue 7 action ecn all threshold 4000 kbytes

Assigning a minimum and maximum threshold in kilobytes to queue 5 in profile mythreshold:

switch(config)# qos threshold-profile mythreshold

switch(config-threshold)# queue 5 action ecn min-threshold 2000 kbytes max-

threshold 4000 kbytes

Configuring a responsive WRED action on queue 2 for red-, yellow-, and green-colored packets:

switch(config)# qos threshold-profile threshprofile

switch(config-threshold)# queue 2 action wred-resp green min-threshold 100

kbytes max-threshold 2000 kbytes max-prob 70 percent
switch(config-threshold)# queue 2 action wred-resp yellow min-threshold 80

kbytes max-threshold 1000 kbytes max-prob 85 percent

switch(config-threshold)# queue 2 action wred-resp red min-threshold 50

kbytes max-threshold 900 kbytes max-prob 90 percent

Configuring a non-responsive WRED action on queue 4 for red-, yellow-, and green-colored packets:

switch(config)# qos threshold-profile threshprofile
switch(config-threshold)# queue 4 action wred-non-resp green min-threshold
500 kbytes max-threshold 2100 kbytes max-prob 71 percent

switch(config-threshold)# queue 4 action wred-non-resp yellow min-threshold

250 kbytes max-threshold 1000 kbytes max-prob 82 percent

Public

queue action 124

switch(config-threshold)# queue 4 action wred-non-resp red min-threshold 50

kbytes max-threshold 900 kbytes max-prob 95 percent

Removing a threshold from queue 7 in profile mythreshold:

switch(config)# qos threshold-profile mythreshold

switch(config-threshold)# no queue 7

Command History

Release

10.11

Modification

WRED syntax support introduced in 6200, 6300, 6400, 8320, 8325, 8360, 840
0, 9300, and 10000 Switch Series.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐
threshold

Administrators or local user group members with execution righ
ts for this command.

8320

8325

8325H

8325P

9300

9300S

10000

10040

queue-monitor

Syntax

queue-monitor

no queue-monitor

Public

queue-monitor 125

Description

This command enables the queue monitoring feature, allowing the switch to collect queue statistics.
then display this information as a queue statistics history. These aggregate statistics can be used to
monitor network health, troubleshoot network issues, and identify normal network behavior patterns and
performance anomalies. This feature is disabled by default, but can be enabled on a maximum of 52
interfaces per switch.

Examples

Enabling the queue monitoring feature on interface 1/1/1:

(config)# interface 1/1/1

(config-if)# queue-monitor

Disabling the queue monitoring feature on interface 1/1/1:

(config)# interface 1/1/1

(config-if)# no queue-monitor

Related Commands

Command

Description

show queue‐monitor
status

This command is used to view the global state of the queue monitor feature. Ou
tput includes the memory consumed by the feature, the statistics being monito
red for collection, and the interfaces currently enabled for monitoring.

Command History

Release

Modification

10.14.1000

Command introduced on 9300 Switch series

10.14

Command introduced on 8325 and 10000 Switch series

Command Information

Platforms

Command context

Authority

config‐if

Administrators or local user group members with execution righ
ts for this command.

8325

8325H

8325P

Public

queue-monitor 126

Platforms

Command context

Authority

9300

9300S

10000

queue-monitor polling-interval seconds

Syntax

queue-monitor polling-interval seconds <SEC>

no queue-monitor polling-interval seconds <SEC>

Description

Configures the polling interval used to sample interface queue data. The specified interval is applied to all
interfaces where queue monitoring is enabled. Changing the polling interval clears all previously collected
queue statistics and restarts data collection from the time the new interval is applied.

The no form of the command resets the polling interval to the default value of 10 seconds.

Parameter

Description

polling‐interval seconds
<SEC>

Specifies the polling interval in seconds. Valid polling intervals a
re 1, 5, 10, 30, or 60 seconds.

Examples

Setting the polling interval to 1 second:

switch(config)# queue-monitor polling-interval seconds 1

Changing the polling interval while queue monitoring is enabled on one or more interfaces:

switch(config)# queue-monitor polling-interval seconds 20

Warning: changing the polling interval will clear collected queue monitor

statistics and will be reflected in all CLI sessions, any agents running in

the

analytics engine, and any external systems monitoring switch statistics.
Continue (y/n)? y
Resetting the polling interval to the default of 10 seconds when no interfaces have queue monitoring
enabled:

Public

queue-monitor polling-interval seconds 127

switch(config)# no queue-monitor polling-interval

Resetting the polling interval to the default of 10 seconds when one or more interfaces have queue
monitoring enabled:

switch(config)# no queue-monitor polling-interval

Warning: changing the polling interval will clear collected queue monitor

statistics and will be reflected in all CLI sessions, any agents running in

the

analytics engine, and any external systems monitoring switch statistics.

Continue (y/n)? y

Command History

Release

10.17

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

8325

8325H

8325P

9300

9300S

10000

rate-limit

Syntax

rate-limit {broadcast|multicast|unknown-unicast} <RATE> {percent|pps}
no rate-limit {broadcast|multicast|unknown-unicast}

Public

rate-limit 128

Description

Sets the amount of traffic of a specific type that can ingress on an Ethernet port, or on each port of a LAG
interface. Rate limits are enforced separately on each individual member of a LAG, not on the LAG as a
whole.

The HPE Aruba Networking 832x, 9300, and 10000 Switch Series do not allow mixing percentage-based
and pps-based rate limits on the same interface at the same time. While the CLI prevents this, REST users
who notice unapplied rate limits should check message logs to determine whether the failure is due to invalid
configuration.

If an interface's overall rate-limiting configuration becomes invalid, any prior rate-limit settings remain in
hardware until explicitly removed. This is to prevent unexpected excess traffic, in the event of accidental
misconfiguration. Apart from deletions, other rate-limiting configuration changes on that interface are
ignored until conflicts between the hardware unit-types are resolved (i.e., until all of the interface's rate-limit
settings use only one of the two unit-types).

The no form of this command removes the traffic limit for the specified traffic type.

Parameter

Description

{broadcast|multicast|
unknown‐unicast}

<RATE> {percent|pps}

Specifies the type of ingress traffic to which the rate limit appli
es: broadcast, multicast, or unknown‐unicast. The multicast
rate limit affects multicast and broadcast traffic. The broadcast
rate limit only affects broadcast traffic. When both types are ap
plied to the same interface, broadcast packets are limited to the
lower of the two rate values. Layer 2 BPDU packets, like spanni
ng tree, are also included in the multicast rate limit.

Specifies the rate limit in packets per second or as a percentag
e of link bandwidth. Range: 64 to 209090910 pps, or 1‐100
percent. For percent mode, the actual rate limit will be approxim
ately equivalent to the minimum of the two 64‐kbps step val
ues that are closest to the kbps‐converted percentage rate. T
he actual applied rate limit can be verified using the show inte
rface <IF‐NAME> qos command.

For percentage mode, rate‐limits may be shown as "not applie
d" until after link‐up has occurred on the configured port or L
AG.

NOTE
The HPE Aruba Networking 9300/9300S Switch Series has a range of 64 to
836363640 pps, or 1-100 percent.

Examples Limiting multicast traffic to 4000 pps on interface 1/1/3:

Public

rate-limit 129

switch(config)# interface 1/1/3

switch(config-if)# rate-limit multicast 4000 pps

Viewing the results of the configuration setting:
switch# show interface 1/1/3 qos

Interface 1/3/3 is down (Administratively down)

 Admin state is down

 Hardware: Ethernet, MAC Address: 1c:98:ec:e3:6a:00

 MTU 1500

 Full-duplex

 rate-limit multicast 4000 pps (4000 actual)

 Speed 0 Mb/s

 Auto-Negotiation is turned on

 Input flow-control is off, output flow-control is off

 RX

            0 input packets              0 bytes

            0 input error                0 dropped

            0 CRC/FCS

       L3:

            ucast: 0 packets, 0 bytes

            mcast: 0 packets, 0 bytes

 TX

            0 output packets             0 bytes

            0 input error                0 dropped

            0 collision

       L3:

            ucast: 0 packets, 0 bytes

            mcast: 0 packets, 0 bytes
Limiting broadcast traffic to 50 pps on LAG 100:
switch# config

switch(config)# interface 1/1/3

switch(config-if)# interface lag 100
switch(config-if)# rate-limit broadcast 50 pps

Configuring an unknown-unicast rate-limit in packets per second:
switch(config)# interface 1/1/3

switch(config-if)# rate-limit unknown-unicast 100 pps

Configuring a multicast rate-limit as a percentage of link bandwidth:
switch(config)# interface 1/1/4
switch(config-if)# rate-limit multicast 1 percent

Public

rate-limit 130

Command History

Release

10.13

Modification

Added the percent parameter.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐if

Administrators or local user group members with execution righ
ts for this command.

8320

8325

8325H

8325P

9300

9300S

10000

10040

show dcbx interface

Syntax

show dcbx interface <IFNAME> [peer | vsx-peer]

Description

Shows the current DCBx status and the configuration of PFC, ETS, and application priority applied on the
interface and the status of the TLVs received from the peer.

Parameter

Description

interface <IFNAME>

Specifies the interface name.

peer

Shows peer DCBx information.

Public

show dcbx interface 131

Parameter

vsx‐peer

Examples

Description

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Showing DCBx on interface 1/1/1 with default DCBx version:

switch# show dcbx interface 1/1/1

 DCBx admin state           : enabled

 DCBx operational state     : active

 DCBx version               : local = IEEE, remote = IEEE

 PFC operational state      : active

 Mismatch  Advertisement                Local           Peer

 --------- ---------------------------- --------------- ----

 Priority Flow Control (PFC)

       ->  Willing:                     No              Yes

           MACsec Bypass Capability:    Yes             Yes

           Max PFC Traffic Classes:     1               1

           Priority 0:                  False           False

           Priority 1:                  False           False

           Priority 2:                  False           False

           Priority 3:                  False           False

           Priority 4:                  True            True

           Priority 5:                  False           False

           Priority 6:                  False           False

           Priority 7:                  False           False

 Enhanced Transmission Selection (ETS)

       ->  Willing:                     No              Yes

           Credit-Based Shaper:         No              No
           Max Traffic Classes:         8               8

           Priority 0:                  Class 1         Class 1

           Priority 1:                  Class 0         Class 0

           Priority 2:                  Class 2         Class 2

           Priority 3:                  Class 3         Class 3

           Priority 4:                  Class 4         Class 4

           Priority 5:                  Class 5         Class 5

           Priority 6:                  Class 6         Class 6

           Priority 7:                  Class 7         Class 7

           Class 0:                     ETS 5           ETS 5

           Class 1:                     ETS 30          ETS 30

           Class 2:                     ETS 10          ETS 10

Public

show dcbx interface 132

->  Class 3:                     ETS 10          ETS 25

       ->  Class 4:                     ETS 25          ETS 10

           Class 5:                     ETS 10          ETS 10

           Class 6:                     ETS 10          ETS 10

           Class 7:                     Strict          Strict

 Application Priority Map:

 Mismatch  Protocol     Protocol ID     Local     Peer

                                        Priority  Priority

 --------- ------------ --------------- --------- ---------

       ->  iscsi                                  5

           tcp-sctp     1001 (0x03E9)   1         1

       ->  tcp-sctp     1002 (0x03EA)   2         7

           EtherType    2000 (0x07D0)   6         6
Showing DCBx on interface 1/1/1 with CEE version:

switch# show dcbx interface 1/1/1

 DCBx admin state           : enabled

 DCBx operational state     : active

 DCBx version               : local = CEE, remote = CEE

 PFC operational state      : active

 Mismatch  Advertisement                Local           Peer

 --------- ---------------------------- --------------- ----

 Control

           Operating Version:           0               0

           Max Version:                 0               0

           Sequence Number:             1               1

       ->  Acknowledgement Number:      1               0

 Priority Flow Control (PFC)

           Operating Version:           0               0

           Max Version:                 0               0

           Enabled:                     Yes             Yes

       ->  Willing:                     No              Yes

           Error:                       No              No

           Max PFC Traffic Classes:     8               8

           Priority 0:                  False           False

           Priority 1:                  False           False

           Priority 2:                  False           False

           Priority 3:                  False           False

           Priority 4:                  True            True

           Priority 5:                  False           False

           Priority 6:                  False           False

           Priority 7:                  False           False

 Priority Group

           Operating Version:           0               0

Public

show dcbx interface 133

Max Version:                 0               0

       ->  Enabled:                     Yes             No

       ->  Willing:                     No              Yes

           Error:                       No              No

           Max Traffic Classes:         8               8

           Priority 0:                  PGID 1          PGID 1

           Priority 1:                  PGID 0          PGID 0

           Priority 2:                  PGID 2          PGID 2

           Priority 3:                  PGID 3          PGID 3

           Priority 4:                  PGID 4          PGID 4

           Priority 5:                  PGID 5          PGID 5

           Priority 6:                  PGID 6          PGID 6

           Priority 7:                  PGID 7          PGID 7

       ->  PG0 Percentage:              5               10

       ->  PG1 Percentage:              10              25

           PG2 Percentage:              30              30

           PG3 Percentage:              30              30

           PG4 Percentage:              30              30

           PG5 Percentage:              30              30

           PG6 Percentage:              30              30

           PG7 Percentage:              30              30

 Application Protocol

           Operating Version:           0               0

           Max Version:                 0               0

           Enabled:                     Yes             Yes

       ->  Willing:                     No              Yes

           Error:                       No              No

 Application Priority Map:

 Mismatch  Protocol     Protocol ID     Local     Peer

                                        Priority  Priority

 --------- ------------ --------------- --------- ---------

       ->  iscsi                                  5
           tcp/udp      1001 (0x03E9)   1         1

       ->  tcp/udp      1002 (0x03EA)   2         7

           EtherType    2000 (0x07D0)   6         6
Showing DCBx on interface 1/1/1 with mismatched version:

switch# show dcbx interface 1/1/1

 DCBx admin state           : enabled

 DCBx operational state     : version_mismatch
 DCBx version               : local = IEEE, remote = CEE

 PFC operational state      : active
Showing DCBx peer connected to interface 1/1/1 using CEE version:

Public

show dcbx interface 134

switch# show dcbx interface 1/1/1 peer

 DCBx version: CEE

 Control

       Operating Version      : 0

       Max Version            : 0

       Sequence Number        : 1

       Acknowledgement Number : 1

 Priority Flow Control (PFC)

       Operating Version      : 0

       Max Version            : 0

       Enabled                : Yes

       Willing                : No

       Error                  : No

       Max PFC Traffic Classes: 8

       Priority 0             : False

       Priority 1             : False

       Priority 2             : False

       Priority 3             : False

       Priority 4             : True

       Priority 5             : False

       Priority 6             : False

       Priority 7             : False

 Priority Group

       Operating Version      : 0

       Max Version            : 0

       Enabled                : No

       Willing                : Yes

       Error                  : No

       Max Traffic Classes    : 8

       Priority 0             : PGID 1

       Priority 1             : PGID 0

       Priority 2             : PGID 2
       Priority 3             : PGID 3

       Priority 4             : PGID 4

       Priority 5             : PGID 5

       Priority 6             : PGID 6

       Priority 7             : PGID 7

       PG0 Percentage         : 25

       PG1 Percentage         : 25

       PG2 Percentage         : 10

       PG3 Percentage         : 10

       PG4 Percentage         : 5

       PG5 Percentage         : 5

Public

show dcbx interface 135

PG6 Percentage         : 10

       PG7 Percentage         : 10

 Application Protocol

       Operating Version      : 0

       Max Version            : 255

       Enabled                : Yes

       Willing                : No

       Error                  : No

 Application Priority Map:

       Protocol       Protocol ID     Priority

       -------------- --------------- --------

       iscsi                          5

       tcp/udp        1001 (0x03E9)   1

       tcp/udp        1002 (0x03EA)   7

       EtherType      2000 (0x07D0)   6

Command History

Release

10.08

Modification

Updated the output to show the DCBx version enhancement.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

8320

8325

8325H

8325P

9300

9300S

10000

10040

Public

show dcbx interface 136

show forwarding-mode

Syntax

show forwarding-mode [vsx-peer]

Description

Display information about the forwarding mode setting configured and applied to the switch interfaces. If
cut-through forwarding mode has been configured but is not yet applied to the hardware, the output of the
show forwarding-mode command will indicate the current state of hardware.

NOTE

Cut-through forwarding mode is not supported on ports with linked speeds less
than 10G or ports with Link Level Flow Control (LLFC) Rx enabled.

Parameter

vsx‐peer

Usage

Description

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is onl
y available on switches that support VSX.

Certain conditions will result in packets being automatically processed as store-and-forward forwarding
mode by the switch instead of cut-through forwarding mode. Examples of these conditions include queueing
or congestion on egress ports, unsupported ports (CPU, management, or loopback ports), or unsupported
speed combinations.

Examples

The following example displays the current forwarding mode when cut-through mode is enabled.

switch# show forwarding-mode

----------------------------------------------------------------------

           Forwarding Mode      Forwarding Mode

Port       Configured           Applied              Status

----------------------------------------------------------------------

1/1/1      cut-through          cut-through          ok

1/1/2      cut-through          cut-through          ok
1/1/3      cut-through          --                   Link not up

1/1/4      cut-through          store-and-forward    Incompatible speed
A status of ok indicates that the configured forwarding mode has been successfully applied to the interface.
The following status type scan indicate that the configured forwarding mode is not successfully applied.

Public

show forwarding-mode 137

•  hardware error: Errors or issues within the physical interface are preventing the configured forwarding

mode from being applied.

•  Link not up: The forwarding mode is not applied because the link is not yet active.

•

•

Incompatible with flow control: The port has Link Level Flow Control (LLFC) Rx enabled and therefore
cannot accept a cut-through forwarding mode configuration. The port will retain the default store-and-
forward forwarding mode setting.

Incompatible speed: Link speed for the port is less than 10G, so the port cannot accept a cut-through
forwarding mode configuration. The port will retain the default store-and-forward forwarding mode
setting.

Command History

Release

Modification

10.15.1000

Command introduced on 8325H Switch series.

Command Information

Platforms

Command context

Authority

8325H

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show interface qos

Syntax

show interface <INTERFACE-NAME> qos

Description

Shows various QoS settings for a specific interface.

Parameter

Description

Specifies the name of an interface on the switch. Format: mem
ber/slot/port or lag number.

Public

show interface qos 138

Parameter

<INTERFACE‐NAME>

Description

Examples

switch# show interface 1/1/5 qos

Interface 1/1/5 is up

 Admin state is up

 qos trust cos (global)

 qos queue-profile factory-default (global)

 qos schedule-profile factory-default (global)

 qos threshold-profile test (override)

 qos cos 5

 qos dscp 47

 rate-limit unknown-unicast 1 percent (10000 actual)

 rate-limit broadcast 40000 kbps (40000 actual)

 rate-limit icmp ip-all 10000 kbps (10000 actual)
switch# show interface lag1 qos

Aggregate-name lag1

 Admin state is up

 qos trust cos (global)

 qos queue-profile factory-default (global)

 qos schedule-profile test (override)

 qos threshold-profile test (override)

 qos cos 5

 qos dscp 47

 rate-limit unknown-unicast 1 percent (10000 actual)

 rate-limit broadcast 40000 kbps (40000 actual)

 rate-limit icmp ip-all 10000 kbps (10000 actual)

Per Interface Status

                Maximum  Bandwidh

 Queue        Bandwidth  Units

 --------------------------------

 Q1               20000  kbps

 Q4               30000  kbps

 Q7               40000  kbps

switch# show interface 1/1/5 qos

Interface 1/1/5 is up
 Admin state is up
 qos trust cos (global)

 qos queue-profile factory-default (global)

 qos schedule-profile factory-default (global)

Public

show interface qos 139

qos cos 5

 qos dscp 47

 rate-limit unknown-unicast 1 percent (10000 actual)

 rate-limit broadcast 40000 kbps (40000 actual)

 rate-limit icmp ip-all 10000 kbps (10000 actual)

switch# show interface 1/1/5 qos

Interface 1/1/5 is up

 Admin state is up

 qos trust none (global)

 qos queue-profile factory-default (global)

 qos schedule-profile factory-default (global)

 qos cos 5

 qos dscp 47

 rate-limit broadcast 4 percent (40000 actual)

 rate-limit icmp ip-all 10000 kbps (10000 actual)

                          Forwarded Pkts         Dropped Pkts

Forwarded Bytes        Dropped Bytes

   Broadcast:                     944468                 1044

1044658890             85662408

   ICMP:                           82210                    0

2689008                    0

 qos shape 200000 kbps (199999 kbps actual)

switch# show interface lag1 qos

Aggregate-name lag1

 Admin state is up

 qos trust cos (global)

 qos queue-profile factory-default (global)

 qos schedule-profile test (override)

 qos cos 5

 qos dscp 47

 rate-limit broadcast 4 percent (40000 actual)

 rate-limit icmp ip-all 10000 kbps (10000 actual)
                          Forwarded Pkts         Dropped Pkts

Forwarded Bytes        Dropped Bytes

   Broadcast:                     944468                 1044

1044658890             85662408

   ICMP:                           82210                    0

2689008                    0

 qos shape 200000 kbps (199999 kbps actual per interface, 399998 kbps total

for LAG)

Per Interface Status

                Maximum  Bandwidh

 Queue        Bandwidth  Units

Public

show interface qos 140

--------------------------------

 Q1               20000  kbps

 Q4               30000  kbps

 Q7               40000  kbps
Showing QoS settings for interface 1/1/5:

switch# show interface 1/1/5 qos

Interface 1/1/5 is down

 Admin state is up

 qos trust none (global)

 qos queue-profile factory-default (global)

 qos schedule-profile EQSExample (override)

 qos dscp 47

 rate-limit unknown-unicast 64 pps (64 actual)

 rate-limit broadcast 500 pps (500 actual)

 qos shape 200000 kbps (200064 kbps actual) burst 70 (70 actual)

                Maximum  Bandwidth      Burst

 Queue        Bandwidth  Units           (KB)

 --------------------------------------------

 Q1            10082461  kbps             120

 Q4            20164923  kbps              32

 Q7            30247384  kbps             120
Showing QoS settings for interface 1/1/6:

NOTE

The following example applies only to the HPE Aruba Networking 8320, 8325,
and 1000 Switch Series.

switch# show interface 1/1/6 qos

Interface 1/1/6 is down

 Admin state is up

 qos trust none (global)
 qos queue-profile factory-default (global)

 qos schedule-profile EQSExample (override)

 rate-limit multicast 1 percent (100000 actual)

 qos shape 200000 kbps (200064 kbps actual) burst 70 (70 actual)

                Maximum  Bandwidth      Burst

 Queue        Bandwidth  Units           (KB)

 --------------------------------------------

 Q1            10082461  kbps             120

 Q4            20164923  kbps              32

 Q7            30247384  kbps             120

Public

show interface qos 141

Showing QoS settings for interface 1/1/6:

NOTE

The following example applies only to the HPE Aruba Networking 9300 Switch
Series.

switch# show interface 1/1/6 qos

Interface 1/1/6 is down

 Admin state is up

 qos trust none (global)

 qos queue-profile factory-default (global)

 qos schedule-profile EQSExample (override)

 rate-limit multicast 1 percent (400000 actual)

 qos shape 200000 kbps (200064 kbps actual) burst 70 (70 actual)

                Maximum  Bandwidth      Burst

 Queue        Bandwidth  Units           (KB)

 --------------------------------------------

 Q1            10082461  kbps             120

 Q4            20164923  kbps              32

 Q7            30247384  kbps             120
switch# show interface 1/1/5 qos

Interface 1/1/5 is down

 Admin state is up

 qos trust none (global)

 qos queue-profile factory-default (global)

 qos schedule-profile EQSExample (override)

 qos threshold-profile threshprofile (global)

 rate-limit unknown-unicast 50 pps (41 actual)

 rate-limit broadcast 500 kbps (505 actual)

 rate-limit multicast 1 percent (10000 actual)

 qos shape 200000 kbps (199999 kbps actual) burst 20 (20 actual)

                Maximum  Bandwidth      Burst

 Queue        Bandwidth  Units           (KB)

 --------------------------------------------

 Q1            10082461  kbps              20

 Q4            20164923  kbps              31

 Q7            30247384  kbps              15

switch# show interface lag1 qos

Aggregate-name lag1
 Admin state is up

 qos trust none (global)

 qos queue-profile factory-default (global)

 qos schedule-profile EQSExample (override)

Public

show interface qos 142

qos threshold-profile threshprofile (global)

 rate-limit unknown-unicast 50 pps (41 actual)

 rate-limit broadcast 500 kbps (505 actual)

 rate-limit multicast 1 percent (10000 actual)

 qos shape 200000 kbps (199999 kbps actual per interface, 399998 kbps total

for LAG) burst 20 (20 actual per interface)

                Maximum  Bandwidth      Burst

 Queue        Bandwidth  Units           (KB)

 --------------------------------------------

 Q1            10082461  kbps              20

 Q4            20164923  kbps              31

 Q7            30247384  kbps              15

switch# show interface 1/1/49 qos

Interface 1/1/49 is up

 Admin state is up

 qos trust none (global)

 qos queue-profile factory-default (global)

 qos schedule-profile factory-default (global)

 qos shape 10000000 kbps (10000000 kbps actual)

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

show interface qos buffers

Syntax

show interface <INTERFACE-NAME> qos buffers

Public

show interface qos buffers 143

Description

Shows interface-level buffer usage statistics.

Parameter

Description

Specifies the name of an Ethernet port on the switch.

<INTERFACE‐NAME>

Usage

Usage statistics include:

•

In-Use: Current buffer memory consumption in kilobytes for each priority.

•  Recent-Peak: Maximum amount of buffer memory consumed by each priority since the last time the

statistics were queried.

•  Max-Use: Maximum amount of buffer memory consumed by each priority since the statistics were last

cleared.

•  Limit: Specifies the hardware-programmed usage limit for the row. Priorities configured for lossless

behavior display two rows:

◦  First row displays lossless pool usage and configured XOFF limit.

◦  Second row displays headroom pool usage and the configured limit.

The hardware-programmed headroom pool limit is based on configuration of either the flow-control buffer
headroom or flow-control buffer cable-length commands on the interface. If both configurations are
specified on the same interface, the headroom buffer limit configuration takes precedence over the cable
length. If auto is configured, then the hardware interface detected cable-length is used. If no headroom limit
or cable length configuration is specified (or cable-length auto is specified but hardware is not reporting a
cable length) then a default cable length of 350 meters is used to compute the headroom limit.

Examples

Showing buffer statistics for interface 1/1/1:

switch# show interface 1/1/1 qos buffers

Buffer usage for 1/1/1 in kbytes:

Cable Length: 350 meters (default)

Recent Peak Interval: 50 seconds
Dynamic thresholds limit = 2^<Alpha>*FreeSpace

Ingress:

  Pri  Pool type     Pool Id   In Use   Recent Peak  Max Use     Limit

  ---  ---------     -------   ------   -----------  -------     -----

Public

show interface qos buffers 144

0    Lossy               0     1486          2357     4852

  1    Lossless            1      542          1468     5123     Dyn:1

  1    Headroom            1        0             0        6        65

  2    Lossless            2     4825          7658    12240     Dyn:1

  2    Headroom            2        0             0        0        65

  3    Lossy               0        0             0        0

  4    Lossy               0        0             0        0

  5    Lossy               0        0             0        0

  6    Lossy               0        0             0        0

  7    Lossy               0        0             0        0
Showing buffer statistics for interface 1/1/2:

switch# show interface 1/1/2 qos buffers

Buffer usage for 1/1/2 in kbytes:

Cable Length: 400 meters (user configured)

Recent Peak Interval: 50 seconds

Dynamic thresholds limit = 2^<Alpha>*FreeSpace

Ingress:

  Pri  Pool type     Pool Id   In Use   Recent Peak  Max Use     Limit

  ---  ---------     -------   ------   -----------  -------     -----

  0    Lossy               0     1486          2357     4852

  1    Lossless            1      542          1468     5123     Dyn:1

  1    Headroom            1        0             0        6        66

  2    Lossless            2     4825          7658    12240     Dyn:1

  2    Headroom            2        0             0        0        66

  3    Lossy               0        0             0        0

  4    Lossy               0        0             0        0

  5    Lossy               0        0             0        0

  6    Lossy               0        0             0        0

  7    Lossy               0        0             0        0
Showing buffer statistics for interface 1/1/3:

switch# show interface 1/1/3 qos buffers
Buffer usage for 1/1/3 in kbytes:

Cable Length: 50 meters (hardware detected)

Recent Peak Interval: 50 seconds

Dynamic thresholds limit = 2^<Alpha>*FreeSpace

Ingress:

  Pri  Pool type     Pool Id   In Use   Recent Peak  Max Use     Limit

  ---  ---------     -------   ------   -----------  -------     -----

  0    Lossy               0     1486          2357     4852

  1    Lossless            1      542          1468     5123     Dyn:1

  1    Headroom            1        0             0        6        55

  2    Lossless            2     4825          7658    12240     Dyn:1

  2    Headroom            2        0             0        0        55

Public

show interface qos buffers 145

3    Lossy               0        0             0        0

  4    Lossy               0        0             0        0

  5    Lossy               0        0             0        0

  6    Lossy               0        0             0        0

  7    Lossy               0        0             0        0

Command History

Release

10.11

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

8325

8325H

8325P

9300

9300S

10000

10040

show interface queues

Syntax

show interface <INTERFACE-NAME> queues

Description

Displays interface-level queue statistics.

Parameter

Description

Specifies the name of an Ethernet port or LAG on the switch. Fo
rmat: member/slot/port or lag number.

Public

show interface queues 146

Parameter

<INTERFACE‐NAME>

Description

Usage

Statistics include:

•  Tx Bytes: Total bytes transmitted. The byte count may include packet headers and internal metadata

that are removed before the packet is transmitted. Packet headers added when the packet is transmitted
may not be included.

•  Tx Packets: Total packets transmitted.

•  Tx Drops: Total packets dropped by an egress queue due to insufficient capacity.

Examples

Showing queue statistics for interface 1/1/5:

switch# show interface 1/1/5 queues

Interface 1/1/5 is down

Admin state is up

Tx Bytes      Tx Packets        Tx Drops

Q0                     0               0               3

Q1                 15356              73               0

Q2                     0               0               0

Q3                     0               0               0

Q4                     0               0               0

Q5                     0               0               0

Q6                     0               0               0

Q7                     0               0               0
Showing queue statistics for interface lag 1:

switch# show interface lag 1 queues

Aggregate-name lag1

Aggregated-interfaces :

1/1/6  1/1/7

Speed 20000 Mb/s

Tx Bytes      Tx Packets        Tx Drops

Q0                     0               0               0

Q1                     0               0               0

Q2                     0               0               0

Q3                     0               0               0

Q4                     0               0               0

Q5                     0               0               0

Public

show interface queues 147

Q6                     0               0               0

Q7                  3450              25               0

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

show interface queue-monitor

Syntax

show interface {<IFNAME>} queue-monitor

histogram [filter  [since <1-10000> days|hours|minutes|seconds][type {queue-

depth}|queue-tx-rate

            |queue-drops}]

list [filter [since <1-10000> days|hours|minutes|seconds][threshold {kbps

<1-4294967295>}|{kbytes <1-4294967295>}|{packets <1-4294967295>}] [type

{queue-depth [
            queue-tx-rate

            |queue-drops]] [slot <slot-id>]

table [filter [threshold {kbps <1-4294967295>}|{kbytes <1-4294967295>}|

{packets <1-4294967295>}] [type {queue-depth}|queue-tx-rate

            |queue-drops]]

Description

Display queue statistics history in the CLI as either a list or a histogram, or as a table, showing the previous
five minutes of queue statistics history.

Public

show interface queue-monitor 148

Parameter

Description

interface [<IFNAME>]

Specifies the name of an Ethernet port or LAG on the switch. If
the optional <IFNAME> parameter is omitted, the output of this
command displays all queue statistic data for all interfaces.

Format: <MEMBER>/<SLOT>/<PORT> or lag <ID>

histogram|list|table

Specifies the output format for queue monitor output.

•  histogram ‐ Queue statistics history is presented in histog

•

ram format for the last 8 hours.
list ‐ Queue statistics history is presented in the list form
at for the last 8 hours

•  table ‐ Queue statistics history is presented in tabular for

mat for the last 5 minutes.

The list format is able to display all of the collected queue stati
stics history data when no filters are applied. To limit the inform
ation displayed in the output of this command, use the filter pa
rameters to filter the output to the format and data you require.

   filter

since <1‐10000>
days|hours|minutes|seconds

Show events no older than a specified age, measured in second
s, days, hours or minutes.

type {queue‐depth}
|queue‐tx‐rate

|queue‐drops

   threshold
{kbps|kbytes|packets <1‐
4294967295>}

Examples

Filter queue monitoring data by the specified filter type. If you
do not specify a filter type, the type defaults to queue‐depth
. To see filtered output for other statistics types, you must speci
fy the type.

•  queue‐depth: Show queue depth data.
•  queue‐tx‐rate: Show average queue transmission (tx)

rate data.

•  queue‐drops: Show queue drops data.

Show data that exceeds a specified threshold in kilobytes, num
ber of packets, or kilobits per second.

Displaying the queue statistics history data for all monitored interfaces in list format:

switch# show interface queue-monitor list
Time Range: 8 hours (2023-08-07 09:11:30 to 2023-08-08 17:11:30 (UTC+00:00))

Time                 Interface  Queue  Statistic              Value

----------------------------------------------------------------------------

----

Public

show interface queue-monitor 149

2023-08-08 17:11:10  1/1/9      4      Average Queue Tx Rate  54321 kbps

2023-08-08 17:11:20  1/1/8      4      Average Queue Tx Rate  1234 kbps

2023-08-08 17:11:20  1/1/9      4      Average Queue Tx Rate  54321 kbps

2023-08-08 17:11:30  1/1/8      4      Average Queue Tx Rate  1234 kbps

2023-08-08 17:11:30  1/1/9      4      Average Queue Tx Rate  54321 kbps

The following example displays a portion of output of the show interface 1/1/8 queue-monitor command,
showing queue statistics history data in tabular format for interface 1/1/8 with a min-depth of 2 kbytes.

switch# show interface 1/1/8 queue-monitor table min-depth kbytes 2

1/1/8 Statistics History

Collection Interval: 10 seconds

Time Range: 2023-08-08 17:07:00 to 2023-08-08 17:12:00 (UTC)

Min-Depth Filter: 2 KB

                          Queue Depth - bytes

Time (s)       Q0       Q1       Q2       Q3       Q4       Q5

Q6       Q7

----------------------------------------------------------------------------

----

-300            -        -        -        -        -        -

-        -

-295            -        -        -        -        -        -

-        -

-290            -        -        -        -        -        -

-        -

-285            -        -        -        -        -        -

-        -

-280            -        -        -        -        -        -

-        -

-275            -        -        -        -        -        -

-        -

-270            -        -        -        -        -        -

-        -

-265            -        -        -        -        -        -

-        -

-260            -        -        -        -        -        -

-        -

-255            -        -        -        -        -        -

Public

show interface queue-monitor 150

-        -

-250            -     2078        -        -        -        -

-        -

-245            -     9914        -        -        -        -

-        -

-240            -   171102        -        -        -        -

-        -

-235            -   996262        -        -        -        -

-        -

-230            -     5444        -        -        -        -

-        -

-225            -        -        -        -        -        -

-        -

-220            -        -        -        -        -        -

-        -

-215            -        -        -        -        -        -

-        -

-210            -        -        -        -        -        -

-        -

-205            -        -        -        -        -        -

-        -

-200            -        -        -        -        -        -

-        -

...
Displaying the queue statistics history data for interface 1/1/8 in histogram format.

switch(config)# show interface 1/1/8 queue-monitor histogram

1/1/8 Statistics History

Time Range: 2023-08-08 09:12:15 to 2023-08-08 17:12:15 (UTC)

Samples per Queue: 13

                         Count at Depth

Depth (KB)        Q0      Q1      Q2      Q3      Q4      Q5      Q6      Q7

----------------------------------------------------------------------------

0                 13      13      13      13       7      13      13      10

1-64               0       0       0       0       6       0       0       3

65-128             0       0       0       0       0       0       0       0

129-256            0       0       0       0       0       0       0       0

257-512            0       0       0       0       0       0       0       0

513-1024           0       0       0       0       0       0       0       0

1025-2048          0       0       0       0       0       0       0       0

2049-4096          0       0       0       0       0       0       0       0

4097-8192          0       0       0       0       0       0       0       0

8193-16384         0       0       0       0       0       0       0       0

Public

show interface queue-monitor 151

16385-32768        0       0       0       0       0       0       0       0

32769-65536        0       0       0       0       0       0       0       0
Output of the global show command when queue monitoring is not enabled on any interfaces.

switch(config)# show interface queue-monitor list

Queue monitoring is not enabled on any interfaces.
Output of the show command when the interface requested does not have queue monitoring enabled.

switch(config)# show interface 1/1/8 queue-monitor table

Interface 1/1/8 does not have queue monitoring enabled.
Output of the global show command with the list presentation speficied when there is no relevant data to
show. Note: the table and histogram presentation formats output all enabled interface data.

switch(config)# show interface queue-monitor list

Enabled interfaces have not collected any data.
Output of the show command for an interface with the list presentation specified but there is no relevant
data to show.

switch(config)# show interface 1/1/8 queue-monitor list

Interface 1/1/8 has not collected any data.

Related Commands

Command

Description

This command enables the queue monitoring feature, allowing the switch to coll
ect queue statistics at 10‐second time intervals. These aggregate statistics ca
n be used to monitor network health, troubleshoot network issues, and identify
normal network behavior patterns and performance anomalies. This feature is di
sabled by default, but can be enabled on a maximum of 52 interfaces per switch
.

queue‐monitor

Command History

Release

10.18

Modification

Command introduced on 10040 Switch series

10.14.1000

Command introduced on 9300 and 9300S Switch series

10.14

Command introduced on 8325 and 10000 Switch series

Public

show interface queue-monitor 152

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

8325

8325H

8325P

9300

9300S

10000

10040

show interface queue-monitor status

Syntax

show interface {<IFNAME> | <IFRANGE>} queue-monitor status [vsx-peer]

Description

Displays the queue monitoring status for a specific interface or range of interfaces. If no interface is
specified, the command will display the queue monitoring status for all interfaces configured.

Parameter

Description

{<IFNAME> | <IFRANGE>}

vsx‐peer

Use the queue‐monitor status parameters to show whether t
he feature is enabled or disabled, and information about memor
y consumption and monitored interfaces. Include the optional <I
FNAME> parameter to filter the output of this command to sho
w data for just the specified interface, or include both the <IFN
AME > parameter and the additional <IFRANGE> parameter als
o to view data for a range of interfaces. If no interface is specifi
ed, the command will display the queue monitor status for all in
terfaces that have queue monitoring configured.

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Public

show interface queue-monitor status 153

Examples

Showing queue monitoring status for interface 1/1/1 when queue monitoring is not configured on that
interface.

switch# show interface 1/1/1 queue-monitor status

Interface 1/1/1 does not have queue monitoring enabled.
Showing the queue monitoring status for interface 1/1/1 when queue monitoring is enabled on that
interface.

switch# show interface 1/1/1 queue-monitor status

Interface 1/1/1

Status               : Enabled

Monitored Statistics :

            , queue-tx-rate

            , queue-drops

Showing the queue monitoring status for a range of interfaces when queue monitoring is enabled on those
interfaces.

switch# show interface 1/1/1-1/1/2 queue-monitor status

Interface 1/1/1

Status               : Enabled

Monitored Statistics :

            , queue-tx-rate

            , queue-drops

Interface 1/1/2

Status               : Enabled

Monitored Statistics :

            , queue-tx-rate

            , queue-drops

Showing the queue monitoring status for all interfaces that have queue monitoring enabled, but the
interface does not support any statistics.

switch# show interface queue-monitor status

Interface 1/1/1

Status               : Blocked (No queue statistics supported for

monitoring)

Interface 1/1/2

Status               : Blocked (No queue statistics supported for

monitoring)

Interface 1/1/3 does not have queue monitoring enabled.
Showing the queue monitoring status for all interfaces where queue monitoring is enabled on interface
1/1/1.

switch# show interface queue-monitor status

Interface 1/1/1

Public

show interface queue-monitor status 154

Status               : Enabled

Monitored Statistics :

            , queue-tx-rate

            , queue-drops

Interface 1/1/2 does not have queue monitoring enabled.

Interface 1/1/3 does not have queue monitoring enabled.
Showing the queue monitoring status for all interfaces when the feature pack is invalid and queue
monitoring is configured only on interface 1/1/1.

switch# show interface queue-monitor status

Interface 1/1/1

Status               : Blocked (Invalid feature pack)

Interface 1/1/2 does not have queue monitoring enabled.

Interface 1/1/3 does not have queue monitoring enabled.
Showing the queue monitoring status for interface 1/1/1 when the feature pack is invalid and queue
monitoring is configured on that interface.

switch# show interface 1/1/1 queue-monitor status

Interface 1/1/1

Status               : Blocked (Invalid feature pack)

Command History

Release

10.18

10.17

Modification

Command introduced on 10040 Switch series

Command introduced

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

8325

8325H

8325P

9300

9300S

10000

10040

Public

show interface queue-monitor status 155

show qos cos-map

Syntax

show qos cos-map [default] [vsx-peer]

Description

Shows the global QoS CoS code point settings, or the factory default settings.

Parameter

default

vsx‐peer

Description

Shows the factory default CoS code point settings.

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Examples

Showing the current CoS map:

switch# show qos cos-map

code_point local_priority color   name

---------- -------------- ------- ----

0          2              green   Best_Effort

1          0              green   Background

2          1              green   Spare

3          3              green   Excellent_Effort
4          4              green   Controlled_Load

5          5              green   Video

6          6              green   Voice

7          7              green   Network_Control
Showing the default CoS map:

switch# show qos cos-map default

code_point local_priority color   name
---------- -------------- ------- ----
0          1              green   Best_Effort

1          0              green   Background

2          2              green   Excellent_Effort

3          3              green   Critical_Applications

Public

show qos cos-map 156

4          4              green   Video

5          5              green   Voice

6          6              green   Internetwork_Control

7          7              green   Network_Control
(Color is reserved for future use.)

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

8320

8325

8325H

8325P

9300

9300S

10000

10040

show qos dscp-map

Syntax

show qos dscp-map [default] [vsx-peer]

Description

Displays the current or default global QoS dscp-map.

Public

show qos dscp-map 157

Parameter

default

vsx‐peer

Description

Shows the factory default DSCP code point settings.

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Examples

Showing the current QoS DSCP map:

switch# show qos dscp-map

code_point local_priority color   name

---------- -------------- ------- ----

0          1              green   CS0

1          1              green

2          1              green

3          1              green

4          1              green

5          1              green

6          1              green

7          1              green

8          0              green   CS1

...

45         5              green

46         7              green   EF

47         5              green

48         6              green   CS6

...

61         7              green
62         7              green

63         7              green
Showing the default QoS DSCP map:

switch# show qos dscp-map default

code_point local_priority color   name

---------- -------------- ------- ----

0          1              green   CS0
1          1              green
2          1              green

3          1              green

4          1              green

Public

show qos dscp-map 158

5          1              green

...

45         5              green

46         5              green   EF

47         5              green

48         6              green   CS6

...

61         7              green

62         7              green

63         7              green

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

show qos egress-rewrite-map

Syntax

show qos egress-rewrite-map [default] [vsx-peer]

Description

The output of this command displays a mapping table that shows the PCP and DSCP value that corresponds
to a local-priority value for packets egressing on ports configured with the qos egress-rewrite feature.

Public

show qos egress-rewrite-map 159

Parameters

Parameter

default

vsx-peer

Usage

Description

Optional. Display the default egress rewrite map values.

Optional. Display values for the VSX peer switch

The show qos egress-rewrite-map command displays the currently configured rewrite map values. Include
the default parameter to display the original default values.

Example

switch# show qos egress-rewrite-map

 Local     PCP (CoS)  DSCP

 Priority  Rewrite    Rewrite

 --------- ---------- --------

 0         1           8

 1         0           0

 2         2           17

 3         3           28

 4         3           32

 5         7           40

 6         5           48

 7         6           60

           CoS Rewrite  DSCP Rewrite

 Port      Status       Status

 --------- ------------ -------------
 1/1/1     applied      applied

 1/1/2     applied      applied

 1/1/8     applied      --

 ```

 switch# show qos egress-rewrite-map default

 Local     PCP (CoS)  DSCP

 Priority  Rewrite    Rewrite

 --------- ---------- --------
 0         1          8

 1         0          0

 2         2          16

 3         3          24

Public

show qos egress-rewrite-map 160

4         4          32

 5         5          40

 6         6          48

 7         7          56

Modification

The output of this command updated to include DHCP rewrite information

Command introduced

Release

10.18

10.17

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

8325

8325H

8325P

show qos pool

Syntax

show qos pool [config [vsx-peer] | statistics]

Description

Shows the QoS pool buffer configuration and analysis information.

Parameter

config

statistics

vsx‐peer

Description

Shows the current pool configuration.

Shows the pool statistics.

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f

Public

show qos pool 161

Parameter

Description

rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Examples

Showing the QoS global pool configuration and analysis:

switch# show qos pool

  Global Packet-Buffer Overview (in Kbytes)

                                                           Port        Max

  Packet Buffer Pools                   Size             Limits      Usage

  ------------------------------------------------------------------------

  Lossy Pool                            4105                 --       3242

  Lossless Pool 1                      13080 (50.00%)        --       9235

    Headroom Pool 1                     2058                 --          0

      Sum of port headroom limits         --                198         --

  Lossless Pool 2                       8973 (37.10%)        --       8467

    Headroom Pool 2                     2058                 --        974

      Sum of port headroom limits         --                265         --

  ------------------------------------------------------------------------

  TOTAL:                               32768

  Analysis:

    Lossy Pool      was 79% utilized

    Lossless pool 1 was 71% utilized

    Headroom pool 1  is 90% over-provisioned

    Lossless pool 2 was 94% utilized

    Headroom pool 2  is 87% over-provisioned

```
Showing the QoS current pool configuration:

switch# show qos pool config

  Global Packet-Buffer Configuration (in Kbytes)

                                                           Port

  Packet Buffer Pools                   Size             Limits

  -------------------------------------------------------------

  Lossy Pool                            4105                 --

  Lossless Pool 1                      13080 (50.00%)        --

    Headroom Pool 1                     2058                 --

      Sum of port headroom limits         --                198

  Lossless Pool 2                       8973 (37.10%)        --

    Headroom Pool 2                     2058                 --

      Sum of port headroom limits                           265

  -------------------------------------------------------------

Public

show qos pool 162

TOTAL:                               32768

  Lossless Pool 1                    XOFF  Headroom

  -------------------------------------------------

  1/1/1 priority 3              Dynamic 2        49

  1/1/4 priority 3              Dynamic 2        49

  1/1/50:1-1/1/50:2 priority 3  Dynamic 2        50

  -------------------------------------------------

  TOTAL:                               --       198

  Lossless Pool 2                    XOFF  Headroom

  -------------------------------------------------

  1/1/4 priority 5              Dynamic 2        49

  1/1/16 priority 5             Dynamic 2        24

  1/1/32-1/1/33 priority 5      Dynamic 2        96

  -------------------------------------------------

  TOTAL:                               --       265

```
Showing the QoS pool statistics:

switch# show qos pool statistics

  Packet-Buffer Pool Statistics

  Recent-Peak Interval: 37 seconds

  Packet Buffer Pools   Total Size     Peak Use   Recent Peak   Current Use

  -------------------   ----------   ----------   -----------   -----------

  Lossy Pool                  6144         4852          2357          1486

  Lossless Pool 1            10240         5123          1468           542

    Headroom 1                2048            6             0             0

  Lossless Pool 2            12280        12240          7658          4825

    Headroom 2                2048            0             0             0

  All buffer sizes are in Kbytes.

```

Command History

Release

Modification

10.10.1000

Support for 9300 series switches added.

10.09

10.08

Support for 10000 series switches added.

Command introduced.

Public

show qos pool 163

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

8325

8325H

8325P

9300

9300S

10000

10040

show qos queue-profile

Syntax

show qos queue-profile [<NAME> | factory-default] [vsx-peer]

Description

Shows the status of all queue profiles, or a specific queue profile.

Parameter

Description

<NAME>

Specifies the name of a queue profile. Range 1 to 64 alphanum
eric characters, including period (.), underscore (_), and hyphen
(‐).

[factory‐default]

Specifies the factory default queue profile.

vsx‐peer

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Usage

The status of a queue profile can be:

Public

show qos queue-profile 164

•  Applied - The profile is actively being used by the switch.

•  Complete - The profile meets the criteria to be applied.

•

Incomplete - The profile does not meet the criteria to be applied.

For a queue profile to be complete and ready to be applied:

•  All eight cos values must be mapped to some queue.

•  There can be only 2, 4, or 8 queues.

•  The queues must be consecutively numbered starting at zero.

•  All eight local priorities must be mapped to some queue.

•  There can be 1 to 8 queues.

•  The queues must be consecutively numbered starting at zero.

•  All eight local priorities must be mapped to some queue.

•  There can be 1 to 8 queues.

•  All eight local priorities must be mapped to some queue.

•  There must be 8 queues.

Examples

Showing the settings of the factory default queue profile:

switch# show qos queue-profile factory-default

queue_num cos name

--------- --- ----

0         1

1         0

2         2
3         3

4         4

5         5

6         6

7         7

switch# show qos queue-profile factory-default

queue_num local_priorities name

--------- ---------------- ----

0         0

1         1

2         2

3         3

Public

show qos queue-profile 165

4         4

5         5

6         6

7         7

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

show qos schedule-profile

Syntax

show qos schedule-profile [<NAME> | factory-default | strict] [vsx-peer]

Description

Shows the status of all schedule profiles, or a specific schedule profile.

Parameter

Description

<NAME>

Specifies the name of a queue or schedule profile. Range: 1 to 6
4 alphanumeric characters, including period (.), underscore (_),
and hyphen (‐).

[factory‐default]

Specifies the factory default queue profile.

vsx‐peer

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f

Public

show qos schedule-profile 166

Parameter

Description

rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Usage

The status of a schedule profile can be:

•  Applied - The profile is actively being used by one or more ports.

•  Complete - The profile meets the criteria to be applied.

•

Incomplete - The profile does not meet the criteria to be applied.

For a schedule profile to be complete and ready to be applied it must have:

•  An algorithm for each queue defined by the applied queue profile.

•  All queues must use the same algorithm except for the highest numbered queue, which may be strict.

Example

Showing the status of all schedule profiles:

switch# show qos schedule-profile

profile_status profile_name

-------------- ------------

applied        MySchedule

complete       factory-default

complete       Test
Showing the configuration of factory default schedule profile:

switch# show qos schedule-profile factory-default

Queue                              Maximum   Bandwidth

Number  Algorithm      Percent   Bandwidth   Units

------- -------------- -------- ----------   ----------
0       min-bandwidth  2

1       min-bandwidth  3

2       min-bandwidth  30

3       min-bandwidth  10

4       min-bandwidth  10

5       min-bandwidth  10

6       min-bandwidth  15

7       min-bandwidth  20

switch# show qos schedule-profile factory-default

Queue

Number  Algorithm      Weight

Public

show qos schedule-profile 167

------- -------------- --------

0       dwrr           1

1       dwrr           1

2       dwrr           1

3       dwrr           1

4       dwrr           1

5       dwrr           1

6       dwrr           1

7       dwrr           1

switch# show qos schedule-profile factory-default

Queue

Number  Algorithm      Weight

------- -------------- --------

0       wfq            1

1       wfq            1

2       wfq            1

3       wfq            1

4       wfq            1

5       wfq            1

6       wfq            1

7       wfq            1

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

show qos threshold-profile

Public

show qos threshold-profile 168

Syntax

show qos threshold-profile [<NAME>]  [vsx-peer]

Description

Shows the status of all threshold profiles, or a specific threshold profile.

Parameter

Description

Specifies the name of a threshold profile. Range: 1 to 64 alphan
umeric characters, including period (.), underscore (_), and hyph
en (‐).

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

<NAME>

vsx‐peer

Usage

Status fields are:

•  applied: The threshold profile is applied to all configured ports.

•  partially applied: The threshold profile is applied to some configured ports but failed on other configured

ports.

•  not applied: The threshold profile could not be applied to any configured ports.

•  blank field: The threshold profile is not applied in the configuration (globally or as a port override).

Examples

switch# show qos threshold-profile

profile_status           profile_name

----------------------   ------------

CustomThresh

applied                  mythreshold
Showing the status of threshold profile mythreshold:

On the 8325, 9300, and 10000 switches:

switch# show qos threshold-profile mythreshold

Queue Action         Color   Minimum  Maximum  Max Probability

----- -------------- ------- -------- -------- ----------------

2     wred-resp      green   1000     1200     30

Public

show qos threshold-profile 169

2     wred-non-resp  red     1100     1150     40

3     ecn            all     1200     1300

Port      Status

--------- -------

1/1/1     applied

1/1/8     applied

1/2/2     applied
On the 8100 and 8360 switches:

switch# show qos threshold-profile mythreshold

queue_num action  Threshold

--------- ------- ---------

5         ecn       40

7         ecn       50

Ports       Status

---------   --------------------

1/1/1       applied

1/1/8       applied

1/2/2       applied

switch# show qos threshold-profile mythreshold

queue_num action  Threshold

--------- ------- ---------

5         ecn       2000

7         ecn       5000

Ports       Status

---------   --------------------

1/1/1       applied

1/1/8       applied

1/2/2       applied

switch# show qos threshold-profile mythreshold

queue_num action  Threshold

--------- ------- ---------

3         ecn       3000

4         ecn       4000

Ports       Status

---------   --------------------

1/2/2       Error: Insufficient TCAM Resources

Command History

Release

10.08

Modification

Updated the example.

Public

show qos threshold-profile 170

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

8325

8325H

8325P

9300

9300S

10000

10040

show qos trust

Syntax

show qos trust [default] [vsx-peer]

Description

Shows the global QoS trust settings, or the factory default settings.

Parameter

default

vsx‐peer

Description

Shows the factory default QoS trust settings.

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Examples

Showing the current QoS trust settings:

Public

show qos trust 171

switch# show qos trust

qos trust cos
Showing the default QoS trust settings:

switch# show qos trust default

qos trust none

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

show queue-monitor status

Syntax

show queue-monitor status

Description

Displays the global state of the queue monitoring feature. The output includes the global enable/disable
status, the memory consumed by the feature, the statistics being collected, and the interfaces currently
enabled for monitoring.

Examples

Showing queue monitoring status when queue monitoring is not enabled on any interfaces.

switch# show queue-monitor status
Feature Status           : Running
Memory Consumption       : 0 kbytes

Monitored Interfaces/Max : 0/52
Showing the queue monitoring status when queue monitoring is enabled on interface 1/1/1.

Public

show queue-monitor status 172

switch# show queue-monitor status

Feature Status           : Running

Memory Consumption       : 184 kbytes

Polling Interval         : 10 seconds

Data Retention Duration  : 8 hours

Monitored Interfaces/Max : 1/52

Monitored Interfaces     : 1/1/1

Related Commands

Command

Description

This command enables the queue monitoring feature, allowing the switch to coll
ect queue statistics at 10‐second time intervals. These aggregate statistics ca
n be used to monitor network health, troubleshoot network issues, and identify
normal network behavior patterns and performance anomalies. This feature is di
sabled by default, but can be enabled on a maximum of 52 interfaces per switch
.

queue‐monitor

Command History

Release

10.18

Modification

Command introduced on 10040 Switch series

10.14.1000

Command introduced on 9300 and 9300S Switch series

10.14

Command introduced on 8325 and 10000 Switch series

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

8325

8325H

8325P

9300

9300S

10000

10040

Public

show queue-monitor status 173

strict queue

Syntax

            strict queue <0-7> [max-bandwidth <RATE> [kbps|percent]][burst

<SIZE>]]

no strict queue <0-7> [max-bandwidth <RATE> [kbps|percent]][burst <SIZE>]]

Description

Assigns the strict priority algorithm to a queue. Strict priority services all packets waiting in a queue, before
servicing the packets in lower priority queues.

Egress queue shaping can be configured using the max-bandwidth and burst options to limit the amount of
traffic transmitted per output queue. The buffer associated with each egress queue stores the excess traffic
to absorb bursts and smooth the output rate. Sustained rates of traffic above the maximum bandwidth will
eventually fill the output queue, causing tail drops. Use show interface <IF-NAME> queues to determine if
any tail-drop errors have occurred.

The no form of this command removes the the queue configuration from the schedule profile. To remove
only egress queue shaping, re-enter the strict queue command without the max-bandwidth and burst
parameters.

Parameter

Description

Specifies the number of the queue. Range: 0 to 7.

<QUEUE‐NUMBER>

max‐bandwidth <BANDWIDTH>

Specifies the maximum bandwidth allowed on the queue in Kbp
s. Range: 8 to 100000000. Alternatively, the maximum bandwid
th rate can also be configured on the queue as a percentage of
the port shape or link bandwidth if a port shape is not configur
ed. The allowed range is 1‐100.

burst <SIZE>

Specifies the maximum burst allowed on the queue.

HPE Aruba Networking 8320, 8325 and 10000 Switch Series:
Range: 1 to 1073. Default: 32.

HPE Aruba Networking 9300 Switch Series: Range: 1 to 1024.
Default: 32.

Public

strict queue 174

Parameter

Description

HPE Aruba Networking 8400 Switch Series: Range: 1 to 32. De
fault: 32.

Usage

Either all the queues of the schedule profile can be strict or just the highest numbered queue. When applied
to a LAG, each member Ethernet port independently schedules its egress transmissions using the strict
settings. Only limited changes can be made to a strict queue that is part of an applied schedule profile:

•  The max-bandwidth settings.

•  The highest numbered queue can be swapped between strict and dwrr

Any other changes or removing a queue (no strict queue) will result in an unusable schedule profile. If that
schedule profile is applied in the interface context, the switch will revert to the schedule profile applied in the
global context until the profile is corrected. If that schedule profile is applied in the global context, the switch
will revert to using the factory-default profile until the profile is corrected.

It is possible for the following errors to occur:

•  The max-bandwidth cannot be greater than 100 percent.

This error occurs when a max-bandwidth value greater than 100 percent is configured on a queue.

•  The max-bandwidth cannot be less than < NUM > kbps.

This error occurs when a kbps max-bandwidth value less than the supported minimum kbps shape value
is configured on a queue. The supported minimum kbps shape value can be retrieved using the show
capacities command.

Examples

Assigning strict priority to queue 7 in the schedule profile MySchedule:

switch(config)# qos schedule-profile MySchedule

switch(config-schedule)# strict queue 7

Deleting strict priority from queue 7 in the schedule profile MySchedule:

switch(config)# qos schedule-profile MySchedule

switch(config-schedule)# no strict queue 7

Assigning strict priority to queue 7 in the schedule profile MySchedule with a maximum bandwidth of
10000 Kbps and a burst of 62 Kbytes:

switch(config)# qos schedule-profile myschedule

switch(config-schedule)# strict queue 7 max-bandwith 10000 kbps

Public

strict queue 175

Assigning strict priority to queue 7 in the schedule profile MySchedule with a maximum bandwidth of 40
percent and a burst of 62 Kbytes:

switch(config)# qos schedule-profile MySchedule

switch(config-schedule)# strict queue 7 max-bandwidth 40 percent

Command History

Release

10.13

Modification

Added the kbps and percent parameters.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config‐
schedule‐<NAME>

Administrators or local user group members with execution righ
ts for this command.

Feature and Proactive Troubleshooting

AOS-CX switches include an intelligent, intuitive and distributed troubleshooting framework that makes
network troubleshooting simpler, inexpensive and efficient. Use the CLI commands in this section to
troubleshoot individual features of AOS-CX software, or issue the troubleshoot proactive command to
set up proactive system troubleshooting to automatically troubleshoot issues based on any of the following.

1.  Events

2.  Log messages

3.  CoPP or other database changes

4.  CPU levels exceeding a threshold

Public

Feature and Proactive Troubleshooting 176

5.  Memory exceeding a threshold

6.  Daemon crashes

NOTE

Feature-specific troubleshooting information can also be viewed via the
Deepshoot >Troubleshoot page of the Switch WebUI. For more details, refer
to the latest WebUI Reference Guide for your switch model.

Subtopics

troubleshoot qos

troubleshoot qos

Syntax

troubleshoot qos

   cos-map

   health [verbose]

   queue-profile

   rate-limit

   schedule-profile

Description

Troubleshoot QoS features.

Parameter

cos‐map

health [verbose]

Description

Troubleshoot issues with Class of Service (CoS) maps,

Display health information for QoS feature errors on the netwo
rk, including the error message, message ID, severity level, and
when the message was last reported. By default, the troublesh
oot qos health command displays basic troubleshooting inform
ation for all QoS features. Include the health parameter after a
QoS feature name to display troubleshooting information for th
at feature only.

Include the optional verbose keyword after the health param
eter to display detailed diagnostic progress and confirm whethe
r additional errors were suppressed.

Public

troubleshoot qos 177

Parameter

queue‐profile

rate‐limit

Description

Troubleshoot queue profile configuration issues.

Troubleshoot rate limiting and policing issues.

schedule‐profile

Troubleshoot schedule profile configuration issues.

Examples

The following example indicates that there are no current issues with QoS features:

6300(config)# troubleshoot qos

--------------------------------------------------

Basic-health troubleshoot

--------------------------------------------------

No basic-health issues found

====================================================

Troubleshoot qos executed successfully

====================================================

Command History

Release

10.18

Modification

Command introduced

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

Support and Other Resources

Access HPE Aruba Networking support and updates, and view warranty and regulatory information

Subtopics

Public

Support and Other Resources 178

Accessing HPE Aruba Networking Support
Accessing Updates
Warranty Information
Regulatory Information
Documentation Feedback

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

Public

Accessing HPE Aruba Networking Support 179

HPE Aruba Networking Developer Hub

https://developer.arubanetworks.com/hpe‐aruba
‐networking‐aoscx/docs/about

Airheads social forums and Knowledge Base

https://community.arubanetworks.com/

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

Public

Accessing Updates 180

Regulatory Information

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

Regulatory Information 181