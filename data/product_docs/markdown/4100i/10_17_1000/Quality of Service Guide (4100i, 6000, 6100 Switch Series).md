AOS-CX 10.17.xxxx Quality of Service Guide (4100i, 6000, 6100
Switch Series)

Published: February 2026

AOS-CX 10.17.xxxx Quality of Service Guide (4100i, 6000, 6100
Switch Series)

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

AOS-CX 10.17.xxxx Quality of Service Guide (4100i,...

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
4
1
0
0
i
,
.
.
.

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX 10.17.xxxx Quality of Service Guide (4100i,...

Table of contents

About this document..................................................................................................................................................................................6

Applicable products........................................................................................................................................................................6

Latest version available online.................................................................................................................................................6

Command syntax notation conventions.............................................................................................................................6

About the examples....................................................................................................................................................................... 8

Identifying switch ports and interfaces...............................................................................................................................8

QoS overview.................................................................................................................................................................................................. 9

End-to-end QoS behavior...........................................................................................................................................................9

Best effort service............................................................................................................................................................10

Class of Service................................................................................................................................................................. 10

Differentiated services..................................................................................................................................................11

QoS on the switch.........................................................................................................................................................................12

QoS trust...............................................................................................................................................................................14

Dynamic QoS trust mode................................................................................................................................15

Port rate limiting...............................................................................................................................................................16

Queue profiles....................................................................................................................................................................16

Schedule profiles.............................................................................................................................................................. 17

Egress queue shaping................................................................................................................................................... 19

Terms...................................................................................................................................................................................... 19

QoS configuration......................................................................................................................................................................................20

Configuring QoS ...........................................................................................................................................................................20

Configuring expedited forwarding for VoIP traffic....................................................................................................26

Configuring rate limiting...........................................................................................................................................................28

Configuring egress queue shaping.....................................................................................................................................29

Configuring threshold profiles.............................................................................................................................................. 30

Supporting Ethernet 802.1D Class of Service.............................................................................................................31

Monitoring queue operation...................................................................................................................................................32

QoS commands........................................................................................................................................................................................... 33

apply qos threshold-profile ................................................................................................................................................... 34

map queue .......................................................................................................................................................................................35

min-bandwidth ..............................................................................................................................................................................37

name queue .................................................................................................................................................................................... 38

qos cos ............................................................................................................................................................................................... 39

qos dscp-map ................................................................................................................................................................................ 41

Public

Table of contents 4

qos dscp ............................................................................................................................................................................................44

qos queue-profile ........................................................................................................................................................................ 46

qos schedule-profile ...................................................................................................................................................................47

qos threshold-profile ................................................................................................................................................................. 50

qos trust ............................................................................................................................................................................................52

queue action ...................................................................................................................................................................................55

rate-limit ........................................................................................................................................................................................... 57

show interface qos ......................................................................................................................................................................60

show interface queues ..............................................................................................................................................................65

show qos dscp-map ................................................................................................................................................................... 67

show qos queue-profile ............................................................................................................................................................69

show qos schedule-profile ......................................................................................................................................................71

show qos threshold-profile .................................................................................................................................................... 73

show qos trust ...............................................................................................................................................................................75

strict queue ..................................................................................................................................................................................... 76

Support and Other Resources............................................................................................................................................................79

Accessing HPE Aruba Networking Support..................................................................................................................79

Accessing Updates.......................................................................................................................................................................80

Warranty Information................................................................................................................................................................. 81

Regulatory Information............................................................................................................................................................. 81

Documentation Feedback........................................................................................................................................................81

Public

Table of contents 5

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

•  HPE Aruba Networking 4100i Switch Series (JL817A, JL818A)

•  HPE Aruba Networking 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A,

S4R20A, S4R21A, S4R22A, S4R23A, S4R24A, S4R25A, S4R26A, S4R27A, S4R28, S4R29A)

•  HPE Aruba Networking 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

example‐text

Usage

Identifies commands and their options and operands
, code examples, filenames, pathnames, and output d
isplayed in a command window. Items that appear li

Public

About this document 6

Convention

Usage

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
m followed by ellipses is enclosed in brackets, ze
ro or more items can be specified.

Public

Command syntax notation conventions 7

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

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format: member/slot/port.

On the HPE Aruba Networking 4100i Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

Public

About the examples 8

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6000 and 6100 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

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

For a network as a whole, it is best to select one service type to use as the primary end-to-end behavior, and
then use the other two service types as needed.

Subtopics

Best effort service
Class of Service
Differentiated services

Public

QoS overview 9

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
The 3-bit Priority Code Point (PCP) field within the 16-bit Ethernet VLAN tag is used to mark the CoS.

 +--------+--------+--------+----------+-----------+--------
 | mac-da | mac-sa | 0x8100 | VLAN tag | ethertype | data...
 +--------+--------+--------+----------+-----------+--------
                           /            \
                          /              \
|     | Public |     |     | Best effort service | 10  |
| --- | ------ | --- | --- | ------------------- | --- |

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
| 08         | CS1              | Low‐Priority Data       | 3662 |     |
DSCP CS1 (08) CoS 1 is deliberately set as the lowest priority. This enables a traffic service level below the
standard (best effort or default forwarding) level to be specified.
The DSCP value is carried within the IPv4 DSCP field or the upper 6-bits of the 8-bit IPv6 Traffic Class (TC)
field.
IPv4
+----+-----+----+----+---+-------+----+------+-------+------+------+-------
|     | Public |     | Differentiated services | 11  |
| --- | ------ | --- | ----------------------- | --- |

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
destination determination, egress queuing, and transmission.

NOTE

Switches with at least 52 ports will experience negative performance if a flood
occurs where at least 42 ports are members of the same VLAN and all 52 ports
have QoS rules applied to them.

Public

QoS on the switch 12

Public

QoS on the switch 13

The following diagram shows how different packets might traverse a switch. It also shows how QoS
configuration settings apply at each stage.

Subtopics

QoS trust
Port rate limiting
Queue profiles
Schedule profiles
Egress queue shaping
Terms

QoS trust

Traffic priorities for networks can be carried in VLAN tags using the CoS Priority Code Point (PCP), or
in IP packet headers using the Differentiated Services Code Point (DSCP). Whether these priorities affect
how traffic is serviced depends on how the QoS trust mode is configured on the switch. The QoS trust
mode specifies how the switch assigns values to ingress packets and can be set globally for all interfaces
or individually for each interface. By default the trust mode is set to  cos , meaning the existing QoS

Public

QoS trust 14

information in the packet will be trusted. The priority values of DSCP packets are mapped to corresponding
CoS values. If the trust mode is set to  none  the CoS value in the incoming packet will be marked as zero.

For example:

Subtopics

Dynamic QoS trust mode

Dynamic QoS trust mode

The device profile feature can dynamically set the QoS trust mode on an interface based on the LLDP
information exchanged with a link partner. The device profile's trust mode temporarily overrides the static
trust mode configured for an interface. The override remains in place as long as that link partner is
connected and its link state is up. Use command  show interface IFNAME qos  to view the
current QoS trust mode for an interface.

Public

Dynamic QoS trust mode 15

Port rate limiting

Port rate limiting helps control undesirable traffic. Its purpose is to allow enough unicast, broadcast,
multicast, and ICMP traffic for the network to function properly, while preventing flooding and traffic storms.

Some amount of each traffic type is required for normal network operation. For example, broadcast packets
may include ARP and DHCP traffic. Video streams and certain types of network protocol packets are
multicast traffic. Unknown-unicast packets may be intended for devices whose addresses have temporarily
aged out of network forwarding caches. Configuring rate limits can help provide balance between necessary
and flooded traffic.

The amount of permitted traffic (the rate limit) can be specified in kilobits-per-second (kbps) or as a
percentage of link bandwidth (percent).

Please note that rate limits are enforced separately on each individual member of a LAG, not on the LAG as
a whole. When limits are in kilobits-per-second (kbps), larger limits may be needed on high speed ports in
order to allow normal network functionality. Conversely, limits configured as a percentage of link bandwidth
may result in too much undesired traffic on high- speed ports.

Queue profiles

A queue profile defines the queues that are associated with an interface to control the transmission of
packets. Each profile supports up to eight queues, numbered 0 to 7. The larger the queue number, the
higher its priority during transmission scheduling. Packets are assigned to a queue based on their local
priority value (0 to 7). A queue profile must map all eight local priority values to whatever queues are being
used on the switch, and a schedule profile must specify the configuration for those same queues. A queue
without a local priority value assigned to it is not used to store packets. Packets are assigned to the queue
based on CoS value. The queue profile defines queue number to CoS mapping. The factory-default map
cross maps the 0 and 1 values.

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

switch# show qos queue-profile factory-default

queue_num cos         name

Public

Port rate limiting 16

--------- ----------- ----

0         1           Scavenger_and_backup_data

1         0

2         2

3         3

4         4

5         5

6         6

7         7

Local Priority

0

1

2

3

4

5

6

7

Queue

0

1

2

3

4

5

5

5

The commonly used commands for working with QoS queues are as follows:

•  qos queue-profile: Creates an empty queue-profile and enters the profile configuration context.

•  name queue: Assigns a descriptive name to a queue.

•  map queue: Maps queue to CoS.

•  apply qos queue-profile: Applies a queue-profile globally to all interfaces.

Schedule profiles

A schedule profile determines the order in which queues are selected for transmission, and the amount of
service available for each queue. A schedule profile must be configured on every interface at all times. A
schedule profile can be applied globally to all interfaces, or only to specific interfaces. The switch described
in this guide supports Guaranteed Minimum Bandwidth (GMB), Strict, and Strict EQS scheduling.

Public

Schedule profiles 17

•  All queues use weighted fair queuing (WFQ)

•  All queues use strict priority

•  The highest priority queue uses strict priority, and all other queues use WFQ

•  All queues use deficit weighted round robin queuing (DWRR)

•  All queues use strict priority

•  The highest priority queue uses strict priority, and all other queues use DWRR

•  All queues use guaranteed minimum bandwidth

•  The highest priority queue uses strict priority and all other queues use guaranteed minimum bandwidth

The switch described in this guide supports 8 queues.

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

Schedule profiles 18

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

Egress queue shaping limits the amount of traffic transmitted per strict output and guaranteed minimum
bandwidth queues. The buffer associated with each egress queue stores excess traffic to absorb bursts and
smooths the output rate. For example, an administrator might limit strict-priority or min-bandwidth queue
traffic to prevent low-priority queue starvation in the event that a device inappropriately sends too many
higher-priority packets.

Egress queue shaping can be configured on an Ethernet port or on a link aggregation group (LAG). To
configure egress queue shaping, define a schedule profile with the strict priority algorithm assigned to each
queue.

Terms

Class

For networking, a set of packets sharing a common characteristic. For example, all IPv4 packets.

Code point

The name of a packet header field, or the value carried within a packet header field:

•  Example 1: Priority code point (PCP) is the name of a field in the IEEE 802.1Q VLAN tag.

•  Example 2: Differentiated services code point (DSCP) is the name of a field carried within the DS field of

an IP packet header.

Class of service (CoS)

A 3-bit value used to mark packets with one of eight classes (levels of priority). It is carried within the
priority code point (PCP) field of the IEEE 802.1Q VLAN tag.

Differentiated services code point (DSCP)

A 6-bit value used to mark packets for different per-hop behavior as originally defined by IETF RFC 2474. It
is carried within the differentiated services (DS) field of the IPv4 or IPv6 header.

Public

Egress queue shaping 19

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

QoS configuration

Learn more about QoS behaviors on the switch

Subtopics

Configuring QoS
Configuring expedited forwarding for VoIP traffic
Configuring rate limiting
Configuring egress queue shaping
Configuring threshold profiles
Supporting Ethernet 802.1D Class of Service
Monitoring queue operation

Configuring QoS

Public

QoS configuration 20

Syntax
Procedure
1.  Configure how values are assigned to ingress packets with the commands qos dscp-map , and qo
| s trust | .   |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- |
2.  Optionally, add a rate limit for ingress traffic on one or more interfaces with the command rate-lim
it.
3.  If you do not want to use the default QoS queue profile for queue mapping, create one or more custom
queue profiles with the command qos queue-profile . For each queue in a custom queue
profile:
| a.  Assign a CoS value mapping with the command  |     |     | map queue | .   |     |     |
| ------------------------------------------------ | --- | --- | --------- | --- | --- | --- |
b.  Optionally, define a descriptive name with the command name queue . All queues must be
mapped to a CoS value, and the queues selected for use must be in contiguous order starting at 0.
4.  If you do not want to use the default QoS schedule profile to determine the order in which queues are
selected to transmit a packet, create one or more custom schedule profiles with the command  qos s
. For each queue in a custom schedule queue profile, define scheduling priority
chedule-profile
| with the commands  | strict queue |  and min-bandwidth |     | .   |     |     |
| ------------------ | ------------ | ------------------ | --- | --- | --- | --- |
5.  Optionally for strict queues, configure egress queue shaping to limit egress bandwidth on an interface to
a value that is less than its line rate. Use the  max-bandwidth  parameter of the  strict queue
command.
6.  Activate QoS settings with the command apply qos . This command lets you apply a queue profile
and schedule profile globally to all interfaces, or a schedule profile override to individual interfaces.
7.  View QoS configuration settings with the provided show commands.
Examples
•  Configures CoS to be used to assign local priority to ingress packets.
•  Modifies the default CoS map to assign CoS 1 to local priority 1.
•  Creates a queue profile named   and assigns local priorities as follows:
Q1
| Queue |        |     | Local Priority |     |                 |     |
| ----- | ------ | --- | -------------- | --- | --------------- | --- |
| 0     |        |     | 0              |     |                 |     |
| 1     |        |     | 1              |     |                 |     |
|       | Public |     |                |     | Configuring QoS | 21  |

Queue

Local Priority

1

3

4

5

5

5

2

3

4

5

6

7

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

Public

Configuring QoS 22

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

0

1

2

3

4

Public

Configuring QoS 23

Queue

4

5

5

Local Priority

5

6

7

•  Creates a schedule profile named  S1  and assigns DWRR to all queues in the schedule profile with the

following weights:

Queue

Weight

0

1

2

3

4

5

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

Public

Configuring QoS 24

switch(config-schedule)# dwrr queue 3 weight 20

switch(config-schedule)# dwrr queue 4 weight 25

switch(config-schedule)# dwrr queue 5 weight 50

switch(config)# apply qos queue-profile Q1 schedule-profile S1

The following example creates a queue profile named Q1 and assigns queue to CoS value mapping:

Queue

CoS Value

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

6

7

Creates a schedule profile named S1 and assigns minimum bandwidth for each queue with a corresponding
percentage value:

Queue

Minimum bandwidth (pecentage)

0

1

2

3

4

5

6

7

5

5

10

10

20

20

10

20

Public

Configuring QoS 25

Applies Q1 and S1 to all interfaces that do not have a QoS override applied.

switch(config)# qos trust cos

switch(config)# qos queue-profile Q1

switch(config-queue)# map queue 0 cos 0

switch(config-queue)# map queue 1 cos 1

switch(config-queue)# map queue 2 cos 2

switch(config-queue)# map queue 3 cos 3

switch(config-queue)# map queue 4 cos 4

switch(config-queue)# map queue 5 cos 5

switch(config-queue)# map queue 6 cos 6

switch(config-queue)# map queue 7 cos 7

switch(config)# qos schedule-profile S1

switch(config-schedule)# min-bandwidth queue 0 percent 5

switch(config-schedule)# min-bandwidth queue 1 percent 5

switch(config-schedule)# min-bandwidth queue 2 percent 10

switch(config-schedule)# min-bandwidth queue 3 percent 10

switch(config-schedule)# min-bandwidth queue 4 percent 20

switch(config-schedule)# min-bandwidth queue 5 percent 20

switch(config-schedule)# min-bandwidth queue 6 percent 10

switch(config-schedule)# min-bandwidth queue 7 percent 20

switch(config-schedule)# apply qos queue-profile Q1 schedule-profile S1

Configuring expedited forwarding for VoIP traffic

Voice over IP (VoIP) traffic is delay and jitter sensitive. For optimum transmission of VoIP traffic, dwell time
in network devices must be kept to a minimum and all network devices in the data path must have identical
per-hop behaviors. To configure a dedicated queue on the switch to handle VoIP traffic with priority service
before all other queues, follow these steps.

Prerequisites

This scenario assumes that VoIP packets are uniquely identified using DiffServ code point 46, Expedited
Forwarding (EF).

Procedure

1.  Map DSCP EF packets exclusively to CoS value 6. The default DSCP map has eight code points (40

through 47), that are mapped to CoS valueTo reserve CoS value 6 for VoIP traffic, the other code points
must be reassigned. In this scenario, CoS value 6 is used for all reassignments, including for code point
40, Call Signaling protocol (CS5).

Public

Configuring expedited forwarding for VoIP traffic 26

switch(config)# qos dscp-map 40 cos 6 name CS5

switch(config)# qos dscp-map 41 cos 6

switch(config)# qos dscp-map 42 cos 6

switch(config)# qos dscp-map 43 cos 6

switch(config)# qos dscp-map 44 cos 6

switch(config)# qos dscp-map 45 cos 6

2.  Queue 7 is the highest priority queue, so for best throughput, create a queue profile that maps CoS to

queue 7.
switch(config)# qos queue-profile ef_priority

switch(config-queue)# name queue 7 Voice_Priority_Queue

switch(config-queue)# map queue 7 cos 5

switch(config-queue)# map queue 6 cos 7

switch(config-queue)# map queue 5 cos 6

switch(config-queue)# map queue 4 cos 4

switch(config-queue)# map queue 3 cos 3

switch(config-queue)# map queue 2 cos 2

switch(config-queue)# map queue 1 cos 1

switch(config-queue)# map queue 0 cos 0

3.  Create a schedule profile that services queue 7 using strict priority (SP), and the remaining queues with
minimum bandwidth. This scenario defines queue 7 as strict and gives queues 0-6 an equal minimum
bandwidth.
switch(config)# qos schedule-profile voip

switch(config-schedule)# strict queue 7

switch(config-schedule)# min-bandwidth queue 6 percent 10

switch(config-schedule)# min-bandwidth queue 5 percent 10

switch(config-schedule)# min-bandwidth queue 4 percent 10

switch(config-schedule)# min-bandwidth queue 3 percent 10

switch(config-schedule)# min-bandwidth queue 2 percent 10

switch(config-schedule)# min-bandwidth queue 1 percent 10

switch(config-schedule)# min-bandwidth queue 0 percent 10

4.  Apply the profiles to all interfaces.

switch(config)# apply qos queue-profile ef_priority schedule-profile voip

5.  Configure DSCP trust mode on all ports

switch(config)# qos trust dscp

Public

Configuring expedited forwarding for VoIP traffic 27

Configuring rate limiting

This scenario illustrates how to use rate limiting to manage the traffic from various devices connected to a
switch. The physical topology of the network looks like this:

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
switch(config-if)# rate-limit broadcast 1000000 kbps

switch(config-if)# rate-limit multicast 2000000 kbps

Public

Configuring rate limiting 28

switch(config-if)# exit

2.  Configure broadcast rate limiting for the router connection.

switch(config-if)# interface 1/1/2

switch(config-if)# rate-limit broadcast 1000000 kbps

switch(config-if)# exit

3.  Configure broadcast rate limiting for the server connection.

switch(config-if)# interface 1/1/5

switch(config-if)# rate-limit broadcast 200000 kbps

switch(config-if)# exit

4.  Configure broadcast, and multicast rate limiting for the computer connection.

switch(config-if)# interface 1/1/10

switch(config-if)# rate-limit broadcast 1000 kbps

switch(config-if)# rate-limit multicast 500 kbps

Configuring egress queue shaping

This example shows how to apply egress queue shaping to an interface. First, a schedule profile is created
that has per-queue bandwidth limits set on all queues with  strict  as the scheduling algorithm. Next, this
profile is applied to an interface or LAG.

The following example creates a schedule profile named EQSExample, which services all queues using strict
priority. This profile configures queues 1, 4, and 7 with a bandwidth limit of 10 Gbps, 20 Gbps, and 30 Gbps
respectively. The apply qos schedule-profile command is then used to apply the EQSExample profile to
interface 1/1/1. The actual bandwidth configured on an interface can be found by using the show interface
<IF-NAME> qos command.

switch(config)# qos schedule-profile EQSExample

switch(config-schedule)# strict queue 0

switch(config-schedule)# strict queue 1 max-bandwidth 10000000 kbps

switch(config-schedule)# strict queue 2

Public

Configuring egress queue shaping 29

switch(config-schedule)# strict queue 3

switch(config-schedule)# strict queue 4 max-bandwidth 20000000 kbps

switch(config-schedule)# strict queue 5

switch(config-schedule)# strict queue 6

switch(config-schedule)# strict queue 7 max-bandwidth 30000000 kbps

switch(config-schedule)# exit

switch(config)# interface 1/1/1

switch(config-if)# apply qos schedule-profile EQSExample

The following example creates a schedule profile named EQSExample which services all queues using strict
priority. This profile configures queues 1, 4 and 7 with a bandwidth limit of 10%, 20%, and 30% of link
bandwidth respectively. The apply qos schedule-profile command is then used to apply the EQSExample
profile to the port. The actual burst and bandwidth configured on an interface can be found by using the
show interface < IF-NAME > qos command.

(config)# qos schedule-profile EQSExample

(config-schedule)# strict queue 0

(config-schedule)# strict queue 1 max-bandwidth 10 percent

(config-schedule)# strict queue 2

(config-schedule)# strict queue 3

(config-schedule)# strict queue 4 max-bandwidth 20 percent

(config-schedule)# strict queue 5

(config-schedule)# strict queue 6

(config-schedule)# strict queue 7 max-bandwidth 30 percent

Configuring threshold profiles

The threshold profile is an optional configuration that specifies a per-packet action to be taken for each port
queue when the queue utilization reaches or exceeds the configured threshold. The per-queue configuration
within the threshold profile is optional, which means any number of queues may be configured. An
unconfigured queue means that no threshold action behavior will occur. Also, an empty threshold profile is
valid and can be applied.

Use the  apply qos threshold-profile <THRESHOLD-NAME>   command in the global
context to configure all ports to use the profile, or in the interface context to configure the interface to use
the profile. No threshold profiles are created or configured by default.

Public

Configuring threshold profiles 30

In an environment where congestion management features are required in order to reduce latency and
responsive transport protocols are in use, ECN can be configured on queues carrying delay-sensitive
traffic. The desired result is that a network device's port-queue utilization is actively managed, resulting in
ECN-capable transport (ECT) packets being Congestion Encountered (CE) marked when queue utilization
reaches or exceeds a configured threshold.

Procedure

Supporting Ethernet 802.1D Class of Service

About this task

IEEE 802.1Q is the most current Ethernet standard for Class of Service (CoS). It superseded an earlier
standard, 802.1D, in 2005. IEEE 802.1Q slightly changed the ordering of the classes of service from its
predecessor IEEE 802.1D for CoS 2 and CoS 0:

CoS 802.1Q

7 Network Control

CoS 802.1D

7 Network Control

6 Internetwork Control

6 Voice (<10ms latency)

5 Voice (<10ms latency)

5 Video (<100ms latency)

4 Video (<100ms latency)

3 Critical Applications

2 Excellent Effort

0 Best Effort

1 Background

4 Controlled Load

3 Excellent Effort

0 Best Effort

2 Spare

1 Background

In 802.1D, both CoS 2 and CoS 1 are below CoS 0 (Best Effort).

When a switch is installed in a network of devices following 802.1D Class of Service, the QoS to queue
mapping must be reconfigured to follow the 802.1D standard by swapping the assignments of CoS 0 and 2:

Procedure

1.  Create a new queue profile with the desired queue to CoS mapping changes.

2.  Apply the created queue profile, using the  apply qos  command.

Public

Supporting Ethernet 802.1D Class of Service 31

Results

switch# config

switch(config)# queue-profile newProfile

switch(config-queue)# map queue 0 cos 1

switch(config-queue)# map queue 2 cos 0

switch(config-queue)# map queue 1 cos 2

switch(config-queue)# map queue 3 cos 3

switch(config-queue)# map queue 4 cos 4

switch(config-queue)# map queue 5 cos 5

switch(config-queue)# map queue 6 cos 6

switch(config-queue)# map queue 7 cos 7

switch# show qos queue-profile newProfile

queue_num    cos      name

--------- ----------- ----

0         1

1         2

2         0

3         3

4         4

5         5

6         6

7         7

Monitoring queue operation

Use the show interface queues command to display the traffic transmitted per queue, and the number of
packets dropped due to the queue being full. ( Tx Bytes  is available on the 6000 and 6100 Switch
Series.) For example:

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

Public

Monitoring queue operation 32

Q6              0                     0                 0

 Q7              0                     0                 0
Tx Bytes: Total bytes transmitted. The byte count may include packet headers and internal metadata that
are removed before the packet is transmitted. Packet headers added when the packet is transmitted may not
be included.

Tx Packets: Total packets transmitted.

Tx Drops: The number of packets dropped by a queue before it was sent. When traffic cannot be forwarded
out an egress interface, it backs up at ingress. The more servicing assigned to a queue by a schedule profile,
the less likely traffic destined for that queue will back up and be dropped. Tx Drops shows the sum of
packets that were dropped across all line modules (due to insufficient capacity) by the ingress Virtual Output
Queues (VOQs) destined for the egress port.

QoS commands

Select a command from the list in the left navigation menu..

Subtopics

apply qos threshold-profile
map queue
min-bandwidth
name queue
qos cos
qos dscp-map
qos dscp
qos queue-profile
qos schedule-profile
qos threshold-profile
qos trust
queue action
rate-limit
show interface qos
show interface queues
show qos dscp-map
show qos queue-profile
show qos schedule-profile
show qos threshold-profile
show qos trust
strict queue

Public

QoS commands 33

apply qos threshold-profile

Syntax

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

NOTE

For the 4100i Switch Series, you cannot apply threshold profile at the global
level. Also, the threshold profile cannot be applied on 10G ports.

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

10.13

Modification

Command enabled on 4100i Switch Series.

10.07 or earlier

‐‐

Public

apply qos threshold-profile 34

Command Information

Platforms

Command context

Authority

4100i

config
config‐if
config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

map queue

Syntax

map queue <QUEUE-NUMBER> cos <PRIORITY-NUMBER>

no map queue <QUEUE-NUMBER> [cos <PRIORITY-NUMBER>]

Description

Assigns a CoS value to a queue in a queue profile. By default, the larger the queue number the higher its
priority. A queue without a CoS value assigned to it is not used to store packets. The same queue can be
assigned multiple CoS values.

The no form of this command removes the specified cos value from a specific queue. If no CoS value is
specified, then all CoS values are removed from the queue.

Parameter

Description

Specifies the queue number. Range: 0 to 7.

<QUEUE‐NUMBER>

<PRIORITY‐NUMBER>

Usage

Specifies the CoS value. Range: 0 to 7, where 0 is the lowest pri
ority and 7 is the highest.

The following commands illustrate a valid configuration, where every local priority value is assigned to a
queue:

            map queue 0 local-priority 0

Public

map queue 35

map queue 1 local-priority 1

            map queue 1 local-priority 2

            map queue 3 local-priority 3

            map queue 4 local-priority 4

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

Public

map queue 36

Command Information

Platforms

Command context

Authority

All platforms

config‐queue

Administrators or local user group members with execution righ
ts for this command.

min-bandwidth

Syntax

min-bandwidth queue <QUEUE-NUMBER> percent <PERCENTAGE>

no min-bandwidth queue <QUEUE-NUMBER>

Description

Assigns the Guaranteed Minimum Bandwidth (GMB) algorithm and a percentage of bandwidth to a queue.
GMB allocates available bandwidth among all non-empty queues in relation to their configured minimum
bandwidth. Non-empty queues are serviced first in strict order up to their minimum bandwidth. If there is
any remaining bandwidth, the scheduler will strictly service any remaining non-empty queues.

The no form of this command only clears the algorithm for a queue if GMB has been assigned.

Occasionally, the following errors may occur:

•  *The schedule profile total sum of GMB percentages must not exceed 100.*

This error occurs when attempting to apply a schedule profile with sum of GMB percentages of queues
exceed 100 percentage. The solution is to configure GMB perecntage for queues, so that the sum of
percentage must not exceed 100.

Parameter

Description

Specifies the queue number. Range: 0 to 7.

<QUEUE‐NUMBER>

<PERCENTAGE>

Specifies bandwidth percentage used for GMB scheduling. Ran
ge: 0 to 100.

Public

min-bandwidth 37

Examples Assigning queue 0 of schedule profile S1 the GMB scheduling algorithm with minimum bandwidth
of 5 percent:
switch(config)# qos schedule-profile S1

switch(config-schedule)# min-bandwidth queue 0 percent 5

Removing GMB from queue 0:
switch(config)# qos schedule-profile s1

switch(config-schedule)# no min-bandwidth queue 0

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

4100i

6000

6100

config‐
schedule‐<NAME>

Administrators or local user group members with execution righ
ts for this command.

name queue

Syntax

name queue  <QUEUE-NUMBER>

            <DESCRIPTION>

no name queue  <QUEUE-NUMBER>

Description

Assigns a description to a queue in a queue profile. This is for identification purposes and has no effect on
configuration.

The no form of this command removes the description associated with a queue.

Public

name queue 38

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

Command Information

Platforms

Command context

Authority

All platforms

config‐queue

Administrators or local user group members with execution righ
ts for this command.

qos cos

Public

qos cos 39

Syntax

qos cos <CODE-POINT>

no qos cos

Description

Configures a CoS PCP remark for an Ethernet or LAG interface. Packets that ingress on the interface are
remarked at egress using the configured CoS PCP value.

The remark only occurs when QoS trust mode on the interface is set to none.

If QoS trust mode is not set to none, then the remark is ignored, and the following commands will
show the CoS remark status as ignored (incompatible Port Access Trust configuration) or not applied'
(incompatible QoS global/port Trust configuration):

•  show running-configuration

•  show interface <PORT-NUM>

•  show interface <PORT-NUM> qos

The no form of this command removes a CoS remark on an interface.

Parameter

Description

Specifies an 802.1 VLAN priority CoS value. Range: 0 to 7.

<CODE‐POINT>

Examples

Configuring a CoS remark of 3 on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# qos trust none

switch(config-if)# qos cos 3

Deleting a CoS remark of 3 on interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# no qos cos

Public

qos cos 40

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

Administrators or local user group members with execution righ
ts for this command.

4100i

6000

6100

qos dscp-map

Syntax

qos dscp-map <CODE-POINT>  [color <COLOR>] [cos <COS-VALUE>] [name

<DESCRIPTION>]

no qos dscp-map <CODE-POINT>

Description

Defines the CoS value color assigned to incoming packets for a specific IP differentiated services code point
(DSCP) value. The DSCP map values are used to prioritize incoming packets when QoS trust mode is set to
dscp.

The no form of this command restores the assignments for a code point to the default setting.

NOTE
The color <COLOR> parameter is supported only in 4100i Switch Series.

Use show qos dscp-map to view the current settings. To see the default DSCP map settings, use the
following command:

switch# show qos dscp-map default

DSCP     code_point cos color   name

-------- ---------- --- ------- ----

Public

qos dscp-map 41

000000   0          0   green   CS0

000001   1          0   green

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

Public

qos dscp-map 42

...

45         5                  green

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

color <COLOR>

cos <COS‐VALUE>

cos <PCP‐VALUE>

Specifies an IP differentiated services code point. Range: 0 to 6
3. Default: 0.

Configures the QoS CoS map color. The supported colors are g
reen, red, and yellow. The default color is green.

Specifies an 802.1p VLAN priority CoS remark value. Range: 0
to 7. Default 0.

Specifies an optional 802.1p VLAN Priority Code Point remark
value. Range: 0 to 7. Default: No remark.

Public

qos dscp-map 43

Parameter

Description

name <DESCRIPTION>

Specifies a description for the DSCP setting. The name is used
for identification only, and has no effect on queue configuration.
Range: 1 to 64 alphanumeric characters, including period (.), un
derscore (_), and hyphen (‐).

Examples Setting code point 1 to a local priority of 2 and a CoS of 0: Setting code point 1 to the default
value: Setting code point 46 to a Cos of 7 and CoS map color as yellow:
switch(config)# qos dscp-map 46 cos 7 name new color yellow

Setting code point 41 to a CoS of 6:
switch(config)# qos dscp-map 41 cos 6

Setting code point 41 to the default value:
switch(config)# no qos dscp-map 41

Setting code point 1, 3-5 to a local priority 2 , and CoS color as green with the description EntryName:

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

4100i

6000

6100

qos dscp

Public

qos dscp 44

Syntax

qos dscp <CODE-POINT>

no qos dscp

Description

Configures a differentiated services code point (DSCP) remark for an Ethernet or LAG interface. IPV4 and
IPV6 packets that ingress on the interface are remarked at egress using the configured DSCP value.

The remark only occurs when QoS trust mode on the interface is set to none. If a DSCP remark is configured
and then trust mode is subsequently set to cos or dscp, then the DSCP remark is ignored.

The following commands will show the remark status as ignored (incompatible Port Access Trust
configuration) or not applied (incompatible QoS global or port trust configuration):

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

1.  The CoS metadata is assigned from the DSCP map entry indexed by the DSCP remark value.

2.

If a CoS remark is also configured along with the DSCP remark, the CoS remark value will be assigned to
the packet's CoS metadata.

3.  The CoS metadata and queue profile are then used to determine the queue for the packet. If the packet

is transmitted with an 802.1Q VLAN tag, the PCP will be remarked to match the CoS metadata.

For arriving non-IP packets:

The CoS metadata is assigned from the DSCP map entry indexed by the DSCP remark value. This CoS value
and the queue profile are used to select the queue for packet scheduling. The PCP of tagged non-IP packets
will be remarked to this CoS value.

Public

qos dscp 45

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

4100i

6000

6100

config‐if
config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

qos queue-profile

Syntax

qos queue-profile <NAME>

no qos queue-profile <NAME>

Description

Creates a new QoS queue profile and switches to the config-queue context for the profile. Or, if the specified
QoS queue profile exists, this command switches to the config-queue context for the profile. . A queue
profile maps queues to CoS values. Each profile has two, four, or eight queues numbered 0 to 7. The larger
the queue number, the higher its priority during transmission scheduling.

Public

qos queue-profile 46

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

Public

qos schedule-profile 47

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

queue_num algorithm     percent max-bandwidth_kbps

--------- ------------- ------- ------------------

0         min-bandwidth 2

1         min-bandwidth 3

2         min-bandwidth 30

3         min-bandwidth 10

4         min-bandwidth 10

5         min-bandwidth 10

6         min-bandwidth 15

7         min-bandwidth 20
A profile named strict is predefined and cannot be edited or deleted. The strict profile services all queues of
the queue profile to which it is applied, using the strict priority algorithm.

A schedule profile must be defined on all interfaces at all times.

There are two permitted configurations for a schedule profile:

1.  All queues use the same scheduling algorithm (for example, WFQ).

2.  The highest queue number uses strict priority, and all remaining (lower) queues use the same algorithm

(for example, WFQ). This supports priority scheduling behavior necessary for the IETF RFC 3246
Expedited Forwarding specification (https://tools.ietf.org/html/rfc3246).

3.  All queues use the same scheduling algorithm (for example, DWRR).

Public

qos schedule-profile 48

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

The no form of this command removes the specified QoS schedule profile when it is not applied. Only
profiles that are not currently applied to an interface can be removed.

Examples

Creating the schedule profile MySchedule:

switch(config)# qos schedule-profile MySchedule

switch(config-schedule)#
Deleting the schedule profile MySchedule:

switch(config)# no qos schedule-profile MySchedule

Public

qos schedule-profile 49

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

qos threshold-profile

Syntax

qos threshold-profile <NAME>

no qos threshold-profile <NAME>

Description

Creates a QoS threshold profile and switches to the config-threshold context for the profile. If the specified
threshold profile exists, this command switches to the config-threshold context for the existing profile. The
threshold profile determines the action to take when a threshold is exceeded for each queue.

A threshold profile is composed of up to . Each queue defines the action to take when buffer utilization
exceeds a specific threshold.

Configure queues with the command queue.

The no form of this command removes the specified QoS threshold profile. Only profiles that are not
currently applied to an interface can be removed.

NOTE

In 4100i Switch Series, only one profile can be created.

Public

qos threshold-profile 50

Parameter

Description

Specifies the name of the QoS threshold profile to create or co
nfigure. Range: 1 to 64 alphanumeric characters, including peri
od (.), underscore (_), and hyphen (‐).

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

10.13

Modification

Command enabled on 4100i Switch Series.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

4100i

config

Administrators or local user group members with execution righ
ts for this command.

Public

qos threshold-profile 51

qos trust

Syntax

Description

Configures one of three modes that are applied globally on all Ethernet interfaces and LAGs that have not
applied their own trust mode. Trust mode determines whether VLAN or IP headers are used to assign CoS
values to ingress packets.

In the config context:

•  This command sets the trust mode that is globally applied to all interfaces that do not have a trust mode

configured.

•  The no form of this command restores all interfaces that do not currently have a trust mode configured

to the default setting.

In the config-if context:

•  This command sets the trust mode override for a specific interface.

•  The no form of this command clears a trust mode override. The interface then uses the global setting.

This is the only way to remove a trust mode override.

Parameter

Description

none

cos

dscp

Example

Ignores all packet headers. Ingress packets are assigned CoS val
ue zero.

For 802.1 VLAN‐tagged packets, use the priority code point f
ield from the outermost VLAN header to assign the CoS value.
For untagged packets, the CoS value is assigned to zero. Defaul
t.

For IP packets, use the DSCP as the index into the DSCP Map ta
ble to obtain the CoS value for the packet. For non‐IP packets,
the CoS value is assigned to zero.

Setting the global trust mode to dscp, which is applied to all interfaces that do not already have an
individual trust mode configured. An override is then applied to interface 2/2/2, and LAG 100, setting trust
mode to cos:

            switch(config)# qos trust dscp

switch(config)# interface 2/2/2

Public

qos trust 52

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

Public

qos trust 53

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

Modification

10.07 or earlier

‐‐

Public

qos trust 54

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

HPE Aruba Networking 4100i Switch Series

queue <0-7> action wred { green | yellow | red } min-threshold <WRED-MIN-

LIMIT> percent max-threshold <WRED-MAX-LIMIT> percent

Description

Defines the threshold settings and action for a specified queue in a threshold-profile. For ECN, when
queue utilization exceeds the threshold value, ECT (ECN-Capable Transport) packets will be CE (Congestion
Encountered) marked when transmitted.

For WRED, when queue utilization exceeds the threshold value, WRED action will randomly early-drop
packets to signal congestion. More than one WRED action can be configured on a single queue for different
packet colors.

The no form of this command removes the settings for a queue.

NOTE

•  Threshold-profile actions are only supported for traffic arriving on interfaces

configured in the trust dscp mode.

•  ECN is not supported in 4100i Switch Series.

Parameter

Description

Specifies the queue number. Range: 0 to 7.

Public

queue action 55

Parameter

<0‐7>

<WRED‐MIN‐LIMIT>

<WRED‐MAX‐LIMIT>

Examples

Description

Specifies the queue minimum utilization threshold value for WR
ED to probabilistically start dropping packets.

Specifies the queue maximum utilization threshold value for W
RED, after which every packet is dropped.

Appplicable only on the HPE Aruba Networking 4100i Switch Series

Configuring a WRED action on queue 2 for red, yellow, and green colored packets:

switch(config)# qos threshold-profile threshprofile

switch(config-threshold)# queue 4 action wred green min-threshold 50

percent max-threshold 100 percent

switch(config-threshold)# queue 4 action wred yellow min-threshold 30

percent max-threshold 50 percent

switch(config-threshold)# queue 4 action wred red min-threshold 20 percent

max-threshold 30 percent

Removing a threshold from queue 7 in profile mythreshold:

switch(config)# qos threshold-profile mythreshold

switch(config-threshold)# no queue 7

Command History

Release

10.13

Modification

Command enabled on 4100i Switch Series.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

4100i

config‐
threshold

Administrators or local user group members with execution righ
ts for this command.

Public

queue action 56

rate-limit

Syntax

rate-limit {all|broadcast|multicast|unknown-unicast|icmp {ip-all|ip|ipv4|

ipv6}} <RATE> {kbps|percent} {in|out}

no rate-limit {all|broadcast|multicast|unknown-unicast|icmp} <RATE> {kbps|

percent} {in|out}

Description

Sets the amount of traffic of a specific type that can ingress on an Ethernet interface, or on each port of a
LAG interface. Rate limits are enforced separately on each individual member of a LAG, not on the LAG as a
whole.

The no form of this command removes the traffic limit for the specified traffic type.

Parameter

all

broadcast

multicast

unknown‐unicast

icmp

Description

The all rate limit can be configured to rate‐limit all types of tr
affic.

The broadcast rate limit only affects ingress broadcast traffic. W
hen both broadcast and multicast rate limits are applied to the s
ame interface, broadcast packets are limited to the lower of the
two rate values. Layer 2 BPDU packets, like spanning tree, are al
so included in the multicast rate limit.

The multicast rate limit affects ingress multicast and broadcast
traffic. When both broadcast and multicast rate limits are applie
d to the same interface, broadcast packets are limited to the low
er of the two rate values. Layer 2 BPDU packets, like spanning t
ree, are also included in the multicast rate limit.

Unknown‐unicast packets may be intended for devices whose
addresses have temporarily aged out of network forwarding cac
hes. Configuring rate limits can help provide balance between n
ecessary and flooded traffic.

The ICMP rate limit can be configured to apply to IPv4, IPv6, or
all IP traffic. Only one ICMP rate‐limit can be configured at a ti
me. Applying a new ICMP rate‐limit replaces any previous ICM
P rate‐limit.

Public

rate-limit 57

Parameter

Description

Specifies the rate limit in kilobits‐per‐second or as a percen
tage of link bandwidth. Range: 64 to 10000000 kbps (in steps
of 64 kbps), or 1‐100 percent. The actual rate limit will be app
roximately equivalent to the minimum of the two 64‐kbps ste
p values that are closest to the configured (or kbps‐converted
) rate. The actual applied rate limit can be verified using the sh
ow interface <IF‐NAME> qos command.

For percentage mode, rate‐limits may be shown as "not applie
d" until after link‐up has occurred on the configured port or L
AG.

Specifies the rate‐limit direction of traffic as ingress or egress
. Rate limits can be applied with different rate values for ingress
and egress directions on each port. Rate‐limit direction can be
applied only on the "all" rate‐limit type.

<RATE> {kbps|percent}

{in|out}

Examples

Limiting broadcast traffic to 1024kbps on interface 1/1/3:

switch(config)# interface 1/1/3

switch(config-if)# rate-limit broadcast 1024 kbps

Limiting all ICMP IPv4 traffic to 10000kbps on interface 1/1/3:

switch(config)# interface 1/1/3

switch(config-if)# rate-limit icmp ip 1024 kbps

Configuring a multicast rate-limit as a percentage of link bandwidth:

switch(config)# interface 1/1/3

switch(config-if)# rate-limit multicast 1 percent

Viewing the results of the previous configuration settings:

switch# show interface 1/1/3 qos

Interface 1/1/3 is up

 Admin state is up

 qos trust cos (global)

 qos queue-profile factory-default (global)

 qos schedule-profile factory-default (global)
 rate-limit unknown-unicast 1024 kbps (1024 actual)
 rate-limit broadcast 1024 kbps (1100 actual)

 rate-limit multicast 1 percent (10000 actual)

 rate-limit icmp ip-all 1024 kbps (1024 actual)

Public

rate-limit 58

switch# show interface 1/1/3

Interface 1/1/3 is up

 Admin state is up

 Link state: up for 3 minutes (since Thu Nov 26 17:56:14 UTC 2020)

 Link transitions: 1

 Description:

 Hardware: Ethernet, MAC Address: f8:60:f0:c9:21:bc

 MTU 1500

 Type 1GbT

 Full-duplex

 qos trust cos

 rate-limit unknown-unicast 1024 kbps (1024 actual)

 rate-limit broadcast 1024 kbps (1100 actual)

 rate-limit multicast 1 percent (10000 actual)

 rate-limit icmp ip-all 1024 kbps (1024 actual)

 Speed 1000 Mb/s

 Auto-negotiation is on

 Energy-Efficient Ethernet is disabled

 Flow-control: off

 Error-control: off

 MDI mode: MDIX

 VLAN Mode: access

 Access VLAN: 1

 Rx

            0 total packets                    0 total bytes

            0   unicast packets

            0   multicast packets

            0   broadcast packets

            0 errors                           0 dropped

            0 CRC/FCS                          0 pause

 Tx

      1057962 total packets            366066962 total bytes
            0   unicast packets

            0   multicast packets

      1058039   broadcast packets

            0 errors                           0 dropped

            0 collision                        0 pause
Configuring all rate-limit in kilobits per second for ingress traffic and all rate-limit as a percentage of link
bandwidth for egress traffic:

switch(config)# interface 1/1/5

switch(config-if)# rate-limit all 15000 kbps in

switch(config-if)# rate-limit all 24 percent out

Public

rate-limit 59

Command History

Release

10.15

10.14

Modification

Added all and in|out parameters.

Replaced the ipv4 parameter with the ip parameter. The ipv4 parameter is dep
recated.

10.13

Added percent parameter.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐if

Administrators or local user group members with execution righ
ts for this command.

4100i

6000

6100

show interface qos

Syntax

show interface <INTERFACE-NAME> qos

Description

Shows various QoS settings for a specific interface.

Parameter

Description

<INTERFACE‐NAME>

Specifies the name of an interface on the switch. Format: mem
ber/slot/port or lag number.

Public

show interface qos 60

Examples

Showing QoS settings for interface 1/1/5:

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
Showing QoS settings for a two-member lag:

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
Showing QoS settings for interface 1/1/5:

switch# show interface 1/1/5 qos

Interface 1/1/5 is up

 Admin state is up
 qos trust cos (global)

 qos queue-profile factory-default (global)

 qos schedule-profile factory-default (global)

 qos cos 5

Public

show interface qos 61

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

 --------------------------------

Public

show interface qos 62

Q1               20000  kbps

 Q4               30000  kbps

 Q7               40000  kbps

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

Public

show interface qos 63

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

Public

show interface qos 64

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

show interface queues

Syntax

show interface <INTERFACE-NAME> queues

Description

Displays interface-level queue statistics.

Parameter

Description

Specifies the name of an Ethernet port or LAG on the switch. Fo
rmat: member/slot/port or lag number.

<INTERFACE‐NAME>

Usage

Statistics include:

Public

show interface queues 65

•  Tx Bytes: Total bytes transmitted. The byte count may include packet headers and internal metadata

that are removed before the packet is transmitted. Packet headers added when the packet is transmitted
may not be included. The byte count includes any packets subsequently dropped by an egress ACL .

•  Tx Packets: Total packets transmitted. The count includes packets subsequently dropped by an egress

ACL .

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

Q6                     0               0               0

Q7                  3450              25               0

Public

show interface queues 66

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

show qos dscp-map

Syntax

show qos dscp-map [default]

Description

Displays the current or default global QoS dscp-map.

Description

Shows the factory default DSCP code point settings.

Parameter

default

Examples

Showing the current QoS DSCP map:

switch# show qos dscp-map

DSCP     code_point cos  name

-------- ---------- ---  ----

000000   0          0    CS0
000001   1          0

000010   2          0

000011   3          0

000100   4          0

Public

show qos dscp-map 67

000101   5          0

...

101101   45         5

101110   46         6    new

101111   47         5

110000   48         6    CS6

...

111101   61         7

111110   62         7

111111   63         7
Showing the default QoS DSCP map:

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

101110   46         5

101111   47         5

110000   48         6    CS6

...

111100   60         7

111101   61         7

111110   62         7

111111   63         7

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show qos dscp-map 68

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

show qos queue-profile

Syntax

show qos queue-profile [<NAME> | factory-default]

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

Usage

The status of a queue profile can be:

•  Applied - The profile is actively being used by the switch.

•  Complete - The profile meets the criteria to be applied.

•

Incomplete - The profile does not meet the criteria to be applied.

For a queue profile to be complete and ready to be applied:

•  All eight cos values must be mapped to some queue.

•  There can be only 2, 4, or 8 queues.

•  The queues must be consecutively numbered starting at zero.

Public

show qos queue-profile 69

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

4         4

5         5

6         6

7         7

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show qos queue-profile 70

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

show qos schedule-profile [<NAME> | factory-default | strict]

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

Usage

The status of a schedule profile can be:

•  Applied - The profile is actively being used by one or more ports.

•  Complete - The profile meets the criteria to be applied.

•

Incomplete - The profile does not meet the criteria to be applied.

For a schedule profile to be complete and ready to be applied it must have:

•  An algorithm for each queue defined by the applied queue profile.

•  All queues must use the same algorithm except for the highest numbered queue, which may be strict.

Public

show qos schedule-profile 71

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

Public

show qos schedule-profile 72

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

Syntax

show qos threshold-profile [<NAME>]

Description

Shows the status of all threshold profiles, or a specific threshold profile.

Parameter

Description

Specifies the name of a threshold profile. Range: 1 to 64 alphan
umeric characters, including period (.), underscore (_), and hyph
en (‐).

<NAME>

Usage

Status fields are:

•  applied: The threshold profile is applied to all configured ports.

Public

show qos threshold-profile 73

•  partially applied: The threshold profile is applied to some configured ports but failed on other configured

ports.

•  not applied: The threshold profile could not be applied to any configured ports.

•  blank field: The threshold profile is not applied in the configuration (globally or as a port override).

NOTE

For the 4100i Switch Series, you cannot apply threshold profile at the global
level. Also, the threshold profile cannot be applied on 10G ports.

Examples

switch# show qos threshold-profile

profile_status           profile_name

----------------------   ------------

CustomThresh

applied                  mythreshold
Showing the status of the threshold profile:

switch# show qos threshold-profile

profile_status           profile_name

----------------------   ------------

applied                  threshprofile

switch# show qos threshold-profile mythreshold

Queue Action         Color   Minimum  Maximum  Max Probability

----- -------------- ------- -------- -------- ----------------

2     wred-resp      green   1000     1200     30

2     wred-non-resp  red     1100     1150     40

3     ecn            all     1200     1300

Port      Status

--------- -------

1/1/1     applied
1/1/8     applied

1/2/2     applied

switch# show qos threshold-profile mythreshold

queue_num action  Threshold

--------- ------- ---------

5         ecn       40

7         ecn       50
Ports       Status
---------   --------------------

1/1/1       applied

1/1/8       applied

Public

show qos threshold-profile 74

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

10.13

Modification

Command enabled on 4100i Switch Series.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

4100i

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show qos trust

Public

show qos trust 75

Syntax

show qos trust [default]

Description

Shows the global QoS trust settings, or the factory default settings.

Description

Shows the factory default QoS trust settings.

Parameter

default

Examples

Showing the current QoS trust settings:

switch# show qos trust

qos trust cos
Showing the default QoS trust settings:

switch# show qos trust default

qos trust cos

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

strict queue

Public

strict queue 76

Syntax

strict queue <0-7> [max-bandwidth <RATE> [kbps|percent]

no strict queue <0-7> [max-bandwidth <RATE> [kbps|percent]

Description

Assigns the strict priority algorithm to a queue. Strict priority services all packets waiting in a queue, before
servicing the packets in lower priority queues.

Egress queue shaping can be configured using the max-bandwidth option to limit the amount of traffic
transmitted per output queue. The buffer associated with each egress queue stores the excess traffic to
smooth the output rate. Sustained rates of traffic above the maximum bandwidth will eventually fill the
output queue, causing tail drops. Use show interface <IF-NAME> queues to determine if any tail-drop errors
have occurred.

The no form of this command removes the queue configuration from the schedule profile. To remove only
egress queue shaping, re-enter the strict queue command without the max-bandwidth parameter.

Parameter

Description

Specifies the number of the queue. Range: 0 to 7.

<QUEUE‐NUMBER>

max‐bandwidth <BANDWIDTH>

Specifies the maximum bandwidth allowed on the queue in Kbp
s. Range: 468 to 100000000. Alternatively, the maximum band
width rate can also be configured on the queue as a percentage
of the port shape or link bandwidth if a port shape is not config
ured. The allowed range is 1‐100.

Usage

Either all the queues of the schedule profile can be strict or just the highest numbered queue. When applied
to a LAG, each member Ethernet port independently schedules its egress transmissions using the strict
settings. Only limited changes can be made to a strict queue that is part of an applied schedule profile:

•  The max-bandwidth settings.

•  The highest numbered queue can be swapped between strict and min-bandwith

Any other changes or removing a queue (no strict queue) will result in an unusable schedule profile. If that
schedule profile is applied in the interface context, the switch will revert to the schedule profile applied in the
global context until the profile is corrected. If that schedule profile is applied in the global context, the switch
will revert to using the factory-default profile until the profile is corrected.

It is possible for the following errors to occur:

•  The max-bandwidth cannot be greater than 100 percent.

Public

strict queue 77

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
10000 Kbps:

switch(config)# qos schedule-profile MySchedule

switch(config-schedule)# strict queue 7 max-bandwidth 10000 kbps

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

Public

strict queue 78

Support and Other Resources

Access HPE Aruba Networking support and updates, and view warranty and regulatory information

Subtopics

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

Public

Support and Other Resources 79

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

Public

Accessing Updates 80

Warranty Information

To view warranty information for your product, go to https://www.arubanetworks.com/support-services/
product-warranties/.

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

Warranty Information 81