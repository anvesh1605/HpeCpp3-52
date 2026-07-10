AOS-CX 10.18.xxxx Monitoring Guide (4100i, 6000, 6100 Switch
Series)

Published: May 2026

AOS-CX 10.18.xxxx Monitoring Guide (4100i, 6000, 6100 Switch
Series)

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

AOS-CX 10.18.xxxx Monitoring Guide (4100i, 6000, 6...

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

M
o
n
i
t
o
r
i
n
g

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

6
0
0
0
,

6
.
.
.

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX 10.18.xxxx Monitoring Guide (4100i, 6000, 6...

Table of contents

About this document..................................................................................................................................................................................7

Applicable products........................................................................................................................................................................7

Latest version available online.................................................................................................................................................7

Command syntax notation conventions.............................................................................................................................7

About the examples....................................................................................................................................................................... 9

Identifying switch ports and interfaces...............................................................................................................................9

Monitoring hardware through visual observation..................................................................................................................10

Confirming normal operation of the switch by reading LEDs.............................................................................10

Detecting if the switch is not ready for a failover event........................................................................................ 12

Finding faulted components using the switch LEDs................................................................................................13

IP Flow Information Export..................................................................................................................................................................14

Flow monitors..................................................................................................................................................................................16

Flow Records................................................................................................................................................................................... 17

Flow Exporters................................................................................................................................................................................17

Destinations..................................................................................................................................................................................... 18

Configuring IP Flow Information Export on 4100i, 6000, and 6100 Switches........................................ 18

Alarms.............................................................................................................................................................................................................. 21

Alarm commands.......................................................................................................................................................................... 22

alarm .......................................................................................................................................................................................22

alarm input ..........................................................................................................................................................................25

alarm snooze ..................................................................................................................................................................... 27

show alarm ..........................................................................................................................................................................28

Boot commands..........................................................................................................................................................................................31

Boot commands.............................................................................................................................................................................31

boot set-default ...............................................................................................................................................................31

boot system ........................................................................................................................................................................32

show boot-history .......................................................................................................................................................... 34

L1-100Mbps downshift......................................................................................................................................................................... 39

Limitations with speed downshift....................................................................................................................................... 40

L1-100Mbps downshift commands...................................................................................................................................40

downshift enable .............................................................................................................................................................40

show interface .................................................................................................................................................................. 41

show interface downshift-enable .......................................................................................................................... 53

show running-config interface ................................................................................................................................55

Public

Table of contents 4

Mirroring......................................................................................................................................................................................................... 57

Mirror statistics.............................................................................................................................................................................. 59

Classifier policies and mirroring sessions....................................................................................................................... 59

Mirroring commands...................................................................................................................................................................60

clear mirror ......................................................................................................................................................................... 60

comment .............................................................................................................................................................................. 61

destination interface .....................................................................................................................................................62

destination tunnel .......................................................................................................................................................... 64

diagnostic ............................................................................................................................................................................66

disable ................................................................................................................................................................................... 68

enable .................................................................................................................................................................................... 68

mirror endpoint ................................................................................................................................................................70

mirror session ....................................................................................................................................................................72

show mirror ........................................................................................................................................................................ 73

show mirror endpoint ...................................................................................................................................................76

source interface ............................................................................................................................................................... 78

Monitoring a device using SNMP..................................................................................................................................................... 80

Packet Capture............................................................................................................................................................................................80

Power-over-Ethernet...............................................................................................................................................................................81

PoE commands...............................................................................................................................................................................82

lldp dot3 poe ..................................................................................................................................................................... 83

lldp med poe ......................................................................................................................................................................84

power-over-ethernet .................................................................................................................................................... 85

power-over-ethernet allocate-by .......................................................................................................................... 86

power-over-ethernet always-on ............................................................................................................................ 88

power-over-ethernet assigned-class .................................................................................................................. 89

power-over-ethernet pre-std-detect .................................................................................................................. 90

power-over-ethernet priority .................................................................................................................................. 91

power-over-ethernet quick-poe .............................................................................................................................92

power-over-ethernet threshold ..............................................................................................................................94

power-over-ethernet trap ..........................................................................................................................................95

show lldp local .................................................................................................................................................................. 96

show lldp neighbor ........................................................................................................................................................ 97

show power-over-ethernet ....................................................................................................................................... 98

Aruba AirWave......................................................................................................................................................................................... 101

SNMP support and AirWave................................................................................................................................................101

Supported features with AirWave and the AOS-CX switch...............................................................................102

Configuring the AOS-CX switch to be monitored by AirWave........................................................................ 103

Public

Table of contents 5

AirWave commands..................................................................................................................................................................104

logging ............................................................................................................................................................................... 104

snmp-server community ..........................................................................................................................................107

snmp-server host .........................................................................................................................................................110

snmp-server vrf ............................................................................................................................................................ 116

snmpv3 context ............................................................................................................................................................117

snmpv3 user ................................................................................................................................................................... 118

snmpv3 user view ...........................................................................................................................................122

Support and Other Resources.........................................................................................................................................................123

Accessing HPE Aruba Networking Support...............................................................................................................124

Accessing Updates....................................................................................................................................................................125

Warranty Information.............................................................................................................................................................. 125

Regulatory Information.......................................................................................................................................................... 126

Documentation Feedback.....................................................................................................................................................126

Public

Table of contents 6

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

About this document 7

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

Command syntax notation conventions 8

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

About the examples 9

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6000 and 6100 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

Monitoring hardware through visual observation

Subtopics

Confirming normal operation of the switch by reading LEDs
Detecting if the switch is not ready for a failover event
Finding faulted components using the switch LEDs

Confirming normal operation of the switch by reading LEDs

This task describes using the switch LEDs to confirm that the switch is operating normally.

NOTE

For complete information on LED behaviors for your AOS-CX switch, refer to
the Installation and Getting Started Guide for that switch series, available for
download from the section of the .

Procedure

1.  Quick check: Verify that the chassis has power and there are no fault conditions.

On the front of the switch, verify that the states of the following LEDs are On Green:

2.

•  Power

•  Health

Verify that the Health LEDs of all installed line modules are On Green.

Public

Monitoring hardware through visual observation 10

C
o
n
fi
r
m
i
n
g

n
o
r
m
a
l

o
p
e
r
a
t
i
o
n

o
f

t
h
e

s
w
i
t
c
h

b
y

r
e
a
d
i
.
.
.

3.  Verify that the Health LEDs of all installed management modules are On Green.

4.  Verify that the network ports are operating normally.

a.  On the active management module, check the Status Front section. Verify that each LED that

indicates a line module is in one of the following states:

•  On Green (normal operation)

•  Off (no line module installed)

b.  On each line module, verify that each port LED is in one of the following states:

•  On Green, Half-Bright Green, or Flickering Green (normal operation)

•  Off (no cable connected or port off by default in config)

5.  Verify that the power supplies are operating normally.

a.  On the active management module, check the Status Front section. Verify that each LED that

indicates a power supply is in one of the following states:

•  On Green (normal operation)

•  Off (no power supply installed)

b.  On each power supply, verify that LEDs are in the following states:

•  Power LED: On Green

•  Fault LED: Off

6.  Verify that the rear components are operating normally by checking the Status Rear section of the

active management module:

a.  Verify that the LEDs for the fabric modules are in one of the following states:

•  On Green (normal operation)

•  Off (component not installed)

b.  Verify that the LEDs for the fan trays and fans are On Green.

7.  Verify that the standby management module is ready to take over as the active management module.

On the standby management module, verify the states of the following LEDs:

•  Health LED is On Green.

•  Management state standby (Stby) LED is On Green.

Public

Detecting if the switch is not ready for a failove... 11

D
e
t
e
c
t
i
n
g

i
f

t
h
e

s
w
i
t
c
h

i
s

n
o
t

r
e
a
d
y

f
o
r

a

f
a
i
l
o
v
e
.
.
.

Detecting if the switch is not ready for a failover event

This task describes using the switch LEDs to detect if the switch is not ready for the loss of a fabric module
or for a failover from the active management module to the standby management module.

NOTE

Although you can detect power supply failures by viewing the LEDs, you
must use software commands to determine if the power supply redundancy is
sufficient to power the chassis if a power supply fails. For complete information
on LED behaviors for your AOS-CX switch, refer to the Installation and Getting
Started Guide for that switch series, available for download from the section of
the .

Procedure

1.  Detect if the standby management module is shut down.

If the standby management module is shut down, the LED states are as follows:

•  The standby management module health LED is Off.

•  The standby management state active (Actv) LED is Off.

•  The standby management state standby (Stby) LED is Off.

•  On the active management module in the Status Front Management Modules section, the LED
for the standby management module is Off. For example, if the active management module is
Management Module LED 5, Management Modules LED 6 is Off.

2.  Detect if the standby management module is in a transient state. If the standby management module is

booting, updating, or in another transient state, the LED states are as follows:

•  The standby management module health LED is Slow Flash Green when the service operating

system is running or during an operating system update.

•  The standby management module Booting LED is Slow Flash Green when the AOS-CX operating

system is booting.

•  The standby management state active (Actv) LED is Off.

•  The standby management state standby (Stby) LED is Off.

•  On the active management module in the Status Front Management Modules section, the LED for

the standby management module is Slow Flash Green.

3.  Detect if a fabric module is shut down or not present. If a fabric module is shut down or not present, the

LED states are as follows:

•  On the active management module, in the Status Rear section, the LED for the fabric module is Off.

Public

Detecting if the switch is not ready for a failove... 12

•  On the rear display module, the LED for the fabric module is Off.

•  On the fabric module, the health LED is Off. However, the fabric module is behind fan 1 and is not

directly visible.

Finding faulted components using the switch LEDs

This task describes using the switch LEDs to find components that are in a fault condition.

NOTE

All green LEDs—except for chassis power LEDs and the Usr1 LED—are off when
the LED mode is set to Light Faults (The Usr1 LED of the LED Mode section
of the active management module is On Green and the default behavior for the
Usr1 LED is being used.). For complete information on LED behaviors for your
AOS-CX switch, refer to the Installation and Getting Started Guide for that
switch series, available for download from the section of the .

Procedure

1.  Find the switch that has the fault condition, which is indicated by a chassis health LED in the state of

Slow Flash Orange.
The chassis health LED is located on the front of the switch and on the rear panel of the switch.

2.

If you are at the back of the switch, on the rear panel, look for LEDs that are in the Slow Flash Orange
state:
The Status Rear area has LEDs for power supplies, fabric modules, fan trays, and fans. The number on
the LED represents the unit number of the component.

If the only LED in a state of Slow Flash Orange is the Chassis health LED, go to the front of the switch.

3.  At the front of the switch, on the active management module, look for LEDs that are in the Slow Flash

Orange state:

•  The Status Front area has LEDs for power supplies, line and fabric modules, and management

modules. The number on the LED indicates the slot number of the component.

•  The Status Rear area has LEDs for fabric modules and fan trays, with a single LED for all the fans in

the fan tray. The number on the LED represents the slot or bay number of the component.

4.  Use the number indicated by the LED that is flashing to locate the slot that contains the faulted

component.
The fabric modules are located behind the fan trays, and the fabric module number corresponds to the
fan tray number.

Public

Finding faulted components using the switch LEDs 13

5.  At the front of the switch, on line modules, look for LEDs that are in the Slow Flash Orange state:

Module LEDs and Port LEDs indicate faults if their states are Slow Flash Orange.

IP Flow Information Export

IP Flow Information Export (IPFIX) is an embedded network flow analysis tool that compiles characteristic
and measured properties of flows and sends flow reports to internal or external flow collectors. IPFIX is
configurable via the command-line or REST interfaces. With IPFIX, customers configure flow records with
match (key) fields and collection (non-key) fields. Match fields are the set of fields that define a flow, such
as IP address or UDP port. Collection fields are the set of fields that identify information to collect for a flow,
such as packet and byte counters.

A flow exporter defines where and how to export flow reports. Flow exporters are created as standalone
entities in the config context to provide flow monitors the ability to export flow reports.

Compatibility with Traffic Insight

The AOS-CX traffic insight feature allows monitoring of large amount of data that it collects from various
flow exporters like IPFIX, and provides the ability to filter, aggregate, and sort the data based on user
flow monitor requests. Traffic insight tracks different monitor requests simultaneously and provides monitor
reports per request. For more information on configuring the Traffic Insight features, refer to the AOS-CX
Security Guide.

Information Elements

The IPFIX Information Elements (IE) are entities that are defined and maintained by the Internet Assigned
Numbers Authority (IANA). They are characterized by a unique piece of information they can provided
about a flow. Information Elements may be either private or public. Private Information Elements are
exported with a Private Enterprise Number (PEN).

AOS-CX can act as an intermediate collecting process for flow reports from hardware to append certain
additional IPFIX information elements to the flow reports. When configured, the software will act as an
intermediate exporting process to export the augmented flow reports to any configured flow exporters.

AOS-CX supports the standard and private information elements shown in the tables below.

NOTE

Not all switches support all information elements. View a list of information
elements supported by your switch using the command show flow monitor
<monitor-name> information-elements. All Standard Information Element
registration information can be found on the IANA website, at https://
www.iana.org/assignments/ipfix/.

Public

IP Flow Information Export 14

Standard Information Elements

octetDeltaCount

packetDeltaCount

protocolIdentifier

sourceTransportPort

sourceIPv4Address

ingressInterface

destinationTransportPort

destinationIPv4Address

vlanId

ipVersion

flowStartMicroseconds

flowEndMicroseconds

paddingOctets

ingressPhysicalInterface

About individual Information Elements

The following IEs are used for both IPv4 and IPv6 flows:

•  cngSourceIP

•  cngDestinationIP

They are always 16 bytes wide. The IP version of the flow is indicated in the ipVersion IE. For IPv4
addresses, the first 12 octets are zero and the IPv4 address is encoded in the last 4 octets. For IPv6
addresses, the full 16 bytes encode the address.

The following IEs reflect the hardware interface ID used by the associated flow:

•

ingressPhysicalInterface

Public

IP Flow Information Export 15

•  egressPhysicalInterface

The hardware interface ID does not match the front-panel port number of the interface. The hardware
interface ID can be mapped to the front-panel port number by using the REST API to query for hw_intf_info
for all interfaces and saving the switch_intf_id value together with the associated front-panel name to form
a mapping table.

Example using curl and jq:

bash

$ curl -X GET

    "{SWITCH}/rest/{VERSION}/system/interfaces?

attributes=hw_intf,info,name&depth=2"

    -H "x-csrf-token: {CSRFTOKEN}"

    -b {AUTH COOKIE FILE}

    | jq 'to_entries

          | map({port: .key, switch_intf_id:

(.value.hw_intf_info.switch_intf_id | tonumber)})

          | sort_by(.switch_intf_id)

          | map({(.port): .switch_intf_id})

          | add'

{

  "1/1/6": 1,

  "1/1/2": 2,

  "1/1/1": 3,

  ...

}

Subtopics

Flow monitors
Flow Records
Flow Exporters
Destinations
Configuring IP Flow Information Export on 4100i, 6000, and 6100 Switches

Flow monitors

A flow monitor is applied to an interface to perform network traffic monitoring. A flow monitor consists of
a flow record, a flow cache, and optional flow exporters. A flow record must be created and assigned to the
flow monitor for the monitoring process to function. Flow data is compiled from the network traffic on the
interface and stored in the flow cache based on the match (key) and collect (non-key) fields in the flow
record. Data from the flow cache is exported by the flow exporters assigned to the flow monitor. 4100i,
6000, and 6100 switch series support a maximum of sixteen flow exporters that can be applied to a single
flow monitor.

Public

Flow monitors 16

Flow Records

A flow record defines match (key) fields and collection (non-key) fields. Match fields are the set of fields that
define a flow, such as IP address or UDP port. Collection fields are the set of fields that identify information
to collect for a flow, such as packet and byte counters. On the 4100i, 6000, and 6100 switch series a
maximum of sixteen flow records can be created.

There are six mandatory match fields, of which the IP match fields must be of the same type (IPv4 or IPv6).

NOTE

A flow record is invalid if it does not contain one of the supported sets of match
fields.

The supported sets of match fields are:

•

IPv4 version

•

IPV4 source address

•

IPv4 destination address

•

IPv4 protocol

•  Transport destination port

•  Transport source port

•

IPv6 version

•

IPv6 source address

•

IPv6 destination address

•

IPv6 protocol

•  Transport destination port

•  Transport source port

Flow Exporters

A flow exporter defines where and how to export flow reports. Flow exporters are created as standalone
entities in the config context to provide flow monitors the ability to export flow reports. 4100i, 6000,

Public

Flow Records 17

and 6100 Switch series support a maximum of sixteen flow exporters that can be applied to a single flow
monitor.

Destinations

About this task

The destination specifies where flow reports are sent. There are two possible destination types for a flow
exporter, but only one can be used at a time within the 4100i, 6000, and 6100 switch series:

Procedure

Hostname or IP address of a device .

Results

A flow exporter can only send flow reports to one destination. The destination type specifies which
destination to use. If no destination type is specified, the default destination type is the hostname or IP
address of a device supported on 4100i, 6000, and 6100 Switch series. A destination of each type can
be configured, but only the one corresponding to the destination type is used. If there is no destination
corresponding to the destination type, then the flow exporter configuration is incomplete. If a new
destination of a particular type is configured, it will replace the destination of that type that was previously
configured.

•  Traffic Insight instance

Configuring IP Flow Information Export on 4100i, 6000, and 6100
Switches

The following list describes the steps required to configure a IP flow information export (IPFIX) solution:

•  Step one: Create flow records

•  Step two: Configure flow exporter(s)

•  Step three: Configure monitor(s)

•  Step four: Apply a flow monitors to interface(s)

NOTE
IPv6 related commands are only applicable to switches that support IPv6
protocol.

Public

Destinations 18

C
o
n
fi
g
u
r
i
n
g

I
P

F
l
o
w

I
n
f
o
r
m
a
t
i
o
n

E
x
p
o
r
t

o
n

4
1
0
0
i
,

6
.
.
.

Step one: Create Flow Records

Flow Records are used to define the data that will be added to the IPFIX template. This example configures
one record for IPv4 and one for IPv6.

switch(config)# flow record flowRecordv4

switch(config-flow-record)# match ip protocol

switch(config-flow-record)# match ip source address

switch(config-flow-record)# match ip destination address

switch(config-flow-record)# match ip version

switch(config-flow-record)# match transport destination port

switch(config-flow-record)# match transport source port

switch(config-flow-record)# collect counter bytes

switch(config-flow-record)# collect counter packets

switch(config-flow-record)# collect application name

switch(config-flow-record)# collect timestamp absolute first

switch(config-flow-record)# collect timestamp absolute last

switch(config-flow-record)# collect application https url

switch(config)# flow record flowRecordv6

switch(config-flow-record)# match ipv6 protocol

switch(config-flow-record)# match ipv6 source address

switch(config-flow-record)# match ipv6 destination address

switch(config-flow-record)# match ipv6 version

switch(config-flow-record)# match transport destination port

switch(config-flow-record)# match transport source port

switch(config-flow-record)# collect counter bytes

switch(config-flow-record)# collect counter packets
switch(config-flow-record)# collect timestamp absolute first
Next, use the show flow record command to verify the configuration.

Step two: Configure flow exporter(s)

In this step, you can define an exporter to send to an external destination by hostname or IP address, or
to an internal destination such as Traffic Insight. The example below configures IPFIX to export data to an
external address/hostname:

switch(config)# flow exporter flowExternal

switch(config-flow-exporter)# destination type hostname-or-ip-addr

switch(config-flow-exporter)# destination 11.1.1.1

switch(config-flow-exporter)# show flow exporter

----------------------------------------------------------------------------

----
Flow exporter 'flowExternal
----------------------------------------------------------------------------

----

Status                  : Accepted

Public

Configuring IP Flow Information Export on 4100i, 6... 19

Export Protocol         : ipfix

Destination Type        : Hostname or IP address

Destination             : 11.1.1.1

Transport Configuration

Protocol            : udp

Port                : 4739
To configure IPFIX to export to Traffic Insight, first configure Traffic Insight.

switch(config)# traffic-insight TI

switch(config-ti-TI)# source ipfix

switch(config-ti-TI)# monitor topN type topN-flows

switch(config-ti-TI)# monitor appFlow type application-flows

switch(config-ti-TI)# enable
Next, configure the flow exporter for Traffic Insight

switch(config)# flow exporter flowExpTI

switch(config-flow-exporter)# export-protocol ipfix

switch(config-flow-exporter)# destination type traffic-insight

switch(config-flow-exporter)# destination traffic-insight TI
You can use the show flow exporter command to verify the flow exporter configuration for Traffic Insight

switch(config)# show flow exporter flowExpTI

----------------------------------------------------------------------------

----

Flow exporter 'flowExpTI'

----------------------------------------------------------------------------

----

Status                  : Accepted

Export Protocol         : ipfix

Destination Type        : Traffic Insight

Destination             : TI

Transport Configuration

Protocol            : udp

Port                : 4739
Finally, use the show run traffic-insight command to verify the Traffic Insight configuration:

switch(config)# show running-config traffic-insight

traffic-insight TI

enable

source ipfix

!

monitor topN type topN-flows entries 5
monitor appFlow type application-flows

Step three: Configure the monitor(s)

First, configure an IPv4 flow monitor.

Public

Configuring IP Flow Information Export on 4100i, 6... 20

switch(config)# flow monitor flowMonv4

switch(config-flow-monitor)# record flowRecordv4

Switch (config-flow-monitor)# exporter flowExternal

switch(config-flow-monitor)# exit
Next, configure an IPv6 flow monitor.

switch(config)# flow monitor flowMonv6

switch(config-flow-monitor)# record flowRecordv6

switch(config-flow-monitor)# exporter flowExternal

switch(config-flow-monitor)# exit
Once both flow monitors are created, use the show flow monitor command to verify the flow monitor
configurations.

switch(config-flow-monitor)# show flow monitor

----------------------------------------------------------------------------

----

Flow monitor 'flowMonv4'

----------------------------------------------------------------------------

----

Status                   : Accepted

Flow Record              : flowRecordv4

Flow Exporter(s)         : flowExternal

Cache Configuration

Inactive Timeout     : 120

Active Timeout       : 1800

----------------------------------------------------------------------------

----

Flow monitor 'flowMonv6'

----------------------------------------------------------------------------

----

Status                   : Accepted

Flow Record              : flowRecordv6

Flow Exporter(s)         : flowExternal
Cache Configuration

Inactive Timeout         : 120

Active Timeout  : 1800

Alarms

Public

Alarms 21

Alarms allow you to configure physical alarms for alarm input ports and specific systems events.

CAUTION

Alarms are only available on the 4100i switch.

Subtopics

Alarm commands

Alarm commands

Subtopics

alarm
alarm input
alarm snooze
show alarm

alarm

Syntax

alarm

   power-supply|temperature

action <LOG-AND-TRAP>|<RELAY>

   input IN1|IN2

action  <LOG-AND-TRAP>|<RELAY>

name <STRING>
trigger <CLOSED>| <OPEN>

   no...

   snooze

<time in minutes>

repeat

Description

Configures input alarm and actions, or global events to be forwarded to the output alarm port, or temporarily
disables (snoozes) active event forwarding to the alarm relay for a specified time interval.

Public

Alarm commands 22

Parameter

temperature

power‐supply

   action

<LOG‐AND‐TRAP>

<RELAY>

Description

Selects the alarm for ambient temperatures reaching the thresh
old limit of 70°C.

Selects the alarm events from the power supply.

Specifies the action to be taken when the monitored event occu
rs.

Generates an event log and SNMP trap.

Relays an event to alarm output port.

input IN1|IN2

Specifies the input alarm port.

   action

Specifies the action to be taken when the monitored event occu
rs.

Generates an event log and SNMP trap.

Relays an event to alarm output port.

<LOG‐AND‐TRAP>

<RELAY>

   name <STRING>

Specifies the external device connected.

   trigger

Triggers an alarm based on a normally open or closed circuit.

Generates an alarm event when the circuit is closed.

<CLOSED>

Generates an alarm event when the circuit is open.

Public

alarm 23

Parameter

<OPEN>

no ...

snooze

Description

Negates any configured parameter or removes the specified co
nfiguration.

Snooze the relay action for specified time interval.

   <time in minutes>

Specifies the snooze time in minutes. The range is 0‐1440 mi
nutes..

   repeat

Repeats the previous snooze time.

Examples

Disabling a temperature event to remove the configuration for all actions associated with the event:

switch(config)# no alarm temperature

Configuring an alarm for a temperature event for the log-and-trap action:

switch(config)# alarm temperature action log-and-trap

Removing the configuration for the temperature event for a log-and-trap action:

switch(config)# no alarm temperature action log-and-trap

Configuring an alarm for a power-supply event for the relay action:

switch(config)# alarm power-supply action relay

Removing the configuration for the power-supply event for the relay action:

switch(config)# no alarm power-supply action relay

Configuring an alarm on input port 1 named Door-Sensor:

switch(config)# alarm input IN1 name Door-Sensor

Removing the configuring for an alarm on input port 1:

switch(config)# no alarm input IN1

Configuring an alarm on input port 1 with log-and-trap action:

switch(config)# alarm input IN1 action log-and-trap

Removing the configuration for an alarm on input port 1 with log-and-trap action:

Public

alarm 24

switch(config)# no alarm input IN1 action log-and-trap

Configuring an alarm on input port 1 to trigger an alarm when the door sensor circuit is closed:

switch(config)# alarm input IN1 trigger closed

Configuring an alarm relay action for 10 minutes:

switch(config)# alarm snooze 10

Configuring an alarm relay action to be repeated with previously configured snooze time:

switch(config)# alarm snooze repeat

Command History

Release

10.08

Modification

Feature introduced.

Command Information

Platforms

Command context

Authority

4100i

config

Administrators or local user group members with execution righ
ts for this command.

alarm input

Syntax

alarm input {IN1 | IN2} [name <STRING>] [action <LOG-AND-TRAP> | <RELAY>]

[trigger <CLOSED | OPEN>]

no alarm input {IN1| IN2} [name <STRING>] [action <LOG-AND-TRAP> | <RELAY>]

[trigger <CLOSED | OPEN>]

Description

Configures input alarm and actions. The no form of this command removes the specified configuration.

Public

alarm input 25

Description

Specifies the input alarm port..

Specifies the external device connected.

Descriptive string.

Specifies the action to be taken when the monitored event occu
rs.

Generates an event log and SNMP trap.

Relays an event to alarm output port.

Triggers an alarm based on a normally open or closed circuit.

Generates an alarm event when the circuit is closed.

Generates an alarm event when the circuit is open.

Parameter

{IN1 | IN2}

name

<STRING>

action

<LOG‐AND‐TRAP>

<RELAY>

trigger

<CLOSED>

<OPEN>

Examples

Configuring an alarm on input port 1 named Door-Sensor:

switch(config)# alarm input IN1 name Door-Sensor

Removing the configuring for an alarm on input port 1:

switch(config)# no alarm input IN1

Configuring an alarm on input port 1 with log-and-trap action:

Public

alarm input 26

switch(config)# alarm input IN1 action log-and-trap

Removing the configuration for an alarm on input port 1 with log-and-trap action:

switch(config)# no alarm input IN1 action log-and-trap

Configuring an alarm on input port 1 to trigger an alarm when the door sensor circuit is closed:

switch(config)# alarm input IN1 trigger closed

Command History

Release

10.08

Modification

Feature introduced.

Command Information

Platforms

Command context

Authority

4100i

config

Administrators or local user group members with execution righ
ts for this command.

alarm snooze

Syntax

alarm snooze [time in minutes] [repeat]

Description

Configures any active event forwarded to alarm relay to be snoozed.

Parameter

Description

time in minutes

Specifies the value for time in minutes. The range is 0‐1440
minutes..

repeat

Repeats the previous snooze time.

Public

alarm snooze 27

Examples

Configuring an alarm relay action for 10 minutes:

switch(config)# alarm snooze 10
Configuring an alarm relay action to be repeated with previously configured snooze time:

switch(config)# alarm snooze repeat

Command History

Release

10.08

Modification

Feature introduced.

Command Information

Platforms

Command context

Authority

4100i

config

Administrators or local user group members with execution righ
ts for this command.

show alarm

Syntax

show alarm

   input [IN1 | IN2]

   power supply

   temperature
   timer

Description

Shows all of the details of global status monitoring alarm events.

Parameter

{IN1 | IN2}

power supply

Description

Specifies the input alarm port..

Selects the alarm events from the power supply.

Public

show alarm 28

Parameter

timer

temperature

Examples

Description

Shows the status of an alarm snooze timer's status and duration
.

Selects the alarm for ambient temperatures reaching threshold l
imits.

Showing details for all global alarm events on the switch:

switch# show alarm

Alarm Snooze Timer Status: active

Duration remaining: 1 min 32 sec

-----------------------------------------------------------------------

Global Alarm: Temperature

-----------------------------------------------------------------------

Alarm Event            Status        log-and-trap       Relay

-----------------------------------------------------------------------

Temperature            inactive      true               false

-----------------------------------------------------------------------

Global Alarm: power-supply

-----------------------------------------------------------------------

Alarm Event              Status        log-and-trap    Relay

-----------------------------------------------------------------------

power-supply             active        false           true
Showing details for the temperature alarm:

switch# show alarm temperature

Alarm Snooze Timer Status: Active

Duration remaining: 5 min 36 sec

-----------------------------------------------------------------------

Global Alarm: Temperature
-----------------------------------------------------------------------

Alarm Event            Status        log-and-trap       Relay

-----------------------------------------------------------------------

Temperature            inactive      true               false
Showing the status of an alarm snooze timer when it is inactive :

switch# show alarm timer

Alarm Snooze Timer Status: inactive
Showing the status of an active 3-minute alarm snooze timer:

switch# show alarm timer

Alarm Snooze Timer Status: active

Duration remaining: 2 min 55 sec

Public

show alarm 29

Showing details for all alarm input ports on the switch:

switch# show alarm input

Alarm Snooze Timer Status: inactive

-----------------------------------------------------------------------

Input Alarm IN1, Name: Door-Sensor

-----------------------------------------------------------------------

Alarm Port          Status        log-and-trap    Relay      Trigger

-----------------------------------------------------------------------

IN1                 inactive      true            false      closed

-----------------------------------------------------------------------

Input Alarm IN2, Name: N/A

-----------------------------------------------------------------------

Alarm Port           Status        log-and-trap    Relay      Trigger

-----------------------------------------------------------------------

IN2                  active        false           true       open
Showing details for alarm input ports IN1:

switch# show alarm input IN1

Alarm Snooze Timer Status: inactive

-----------------------------------------------------------------------

Input Alarm IN1, Name: Door-Sensor

-----------------------------------------------------------------------

Alarm Port          Status        log-and-trap    Relay       Trigger

-----------------------------------------------------------------------

IN1                 inactive      true            false       closed

Command History

Release

10.08

Modification

Feature introduced.

Command Information

Platforms

Command context

Authority

4100i

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

Public

show alarm 30

Boot commands

Subtopics

Boot commands

Boot commands

Subtopics

boot set-default
boot system
show boot-history

boot set-default

Syntax

boot set-default {primary | secondary}

Description

Sets the default operating system image to use when the system is booted.

Parameter

primary

secondary

Example

Description

Selects the primary network operating system image.

Selects the secondary network operating system image.

Selecting the primary image as the default boot image:

switch# boot set-default primary

Default boot image set to primary.

NOTE
For more information on features that use this command, refer to the
Fundamentals Guide or the Monitoring Guide for your switch model.

Public

Boot commands 31

Command History

Release

10.07 or earlier

Command Information

Platforms

All platforms

Modification

‐‐

Command context

Authority

Manager ( # )

Administrators or local user group
members with execution rights for
this command.

boot system

Syntax

boot system [primary | secondary | serviceos]

Description

Reboots all modules on the switch. By default, the configured default operating system image is used.
Optional parameters enable you to specify which system image to use for the reboot operation and for
future reboot operations.

Parameter

primary

secondary

serviceos

Description

Selects the primary operating system image for this reboot and
sets the configured default operating system image to primary
for future reboots.

Selects the secondary operating system image for this reboot a
nd sets the configured default operating system image to secon
dary for future reboots.

Selects the service operating system for this reboot. Does not c
hange the configured default operating system image. The ser
vice operating system acts as a standalone bootloader and rec
overy OS for switches running the AOS-CX operating system an
d is used in rare cases when troubleshooting a switch.

Public

boot system 32

Usage

This command reboots the entire system. If you do not select one of the optional parameters, the system
reboots from the configured default boot image.

You can use the show images command to show information about the primary and secondary system
images.

Choosing one of the optional parameters affects the setting for the default boot image:

•

If you select the primary or secondary optional parameter, that image becomes the configured default
boot image for future system reboots. The command fails if the switch is not able to set the operating
system image to the image you selected.
You can use the boot set-default command to change the configured default operating system image.

•

If you select serviceos as the optional parameter, the configured default boot image remains the same,
and the system reboots all management modules with the service operating system.

If the configuration of the switch has changed since the last reboot, when you execute the boot system
command you are prompted to save the configuration and you are prompted to confirm the reboot
operation.

Saving the configuration is not required. However, if you attempt to save the configuration and there is an
error during the save operation, the boot system command is aborted.

Examples

Rebooting the system from the configured default operating system image:

switch# boot system

Do you want to save the current configuration (y/n)? y

The running configuration was saved to the startup configuration.

This will reboot the entire switch and render it unavailable

until the process is complete.

Continue (y/n)? y

The system is going down for reboot.

The system is going down for reboot.
Rebooting the system from the secondary operating system image, setting the secondary operating system
image as the configured default boot image:

switch# boot system secondary

Default boot image set to secondary.

Do you want to save the current configuration (y/n)? n

This will reboot the entire switch and render it unavailable

until the process is complete.
Continue (y/n)? y
The system is going down for reboot.
Canceling a system reboot:

Public

boot system 33

switch# boot system

Do you want to save the current configuration (y/n)? n

This will reboot the entire switch and render it unavailable

until the process is complete.

Continue (y/n)? n

Reboot aborted.

switch#

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

show boot-history

Syntax

show boot-history [all|{vsf member <1-10>}]

Description

Shows boot history information. When no parameters are specified, shows the most recent information about
the current boot operation, and the three previous boot operations for the switch. When the all parameter is
specified, the output of this command shows the boot information for the active management module.

.

NOTE

To view boot-history on a standby, the command must be sent on the conductor
console.

Public

show boot-history 34

Parameter

all

Description

Optional. Shows boot information for the active management m
odule.

vsf member <1‐10>

Optional. Display boot history for the specified VSF member

Usage

This command displays the boot-index, boot-ID, and up time in seconds for the current boot. If there is a
previous boot, it displays boot-index, boot-ID, reboot time (based on the time zone configured in the system)
and reboot reasons. Previous boot information is displayed in reverse chronological order.

The output of this command includes the following information:

Parameter

Index

Boot ID

Description

The position of the boot in the history file. Range: 0 to 3.

A unique ID for the boot . A system‐generated 128‐bit strin
g.

Current Boot, up for

<time>

For the current boot, the show boot‐history command shows
the number of seconds the module has been running on the cur
rent software.

<Timestamp>: boot reason

For previous boot operations, the show boot‐history comma
nd shows the time at which the operation occurred and the rea
son for the boot. The reason for the boot is one of the following
values:

•  <DAEMON‐NAME> crash: The daemon identified by <DA

EMON‐NAME> caused the module to boot.

•  Kernel crash: The operating system software associated wit

h the module caused the module to boot.

•  Uncontrolled reboot: The reason for the reboot is not kno

wn.

•  Reboot requested through database: The reboot occurre
d because of a request made through the CLI or other API.

Public

show boot-history 35

Table 1. Description of reboots handled through the database
Boot History String

Description

Reboot requested by user

Reset button pressed

A user requested a switch reboot through the CLI or
web UI.

The switch detected a short‐press of the reset but
ton

Backplane fault

A backplane fault occurred.

Configuration change

A configuration change resulted in a reboot.

Configuration version migration

A configuration version migration occurred which re
quired a reboot.

Console error

Fabric fault

The console failed to start.

A fabric fault occurred.

All line modules faulted

A zero line card condition occurred.

Redundancy switchover requested

A user requested a redundancy switchover.

Redundant Management communication timeout

The standby management module has taken over fro
m an unresponsive active management module.

Redundant Management election timeout

Critical service fault (error)

A failure to elect a standby management module in t
he allotted time.

A daemon critical to switch operation has stopped fu
nctioning. An extra error string may be present to d
escribe the error in detail.

VSF autojoin renumber

Reset triggered by VSF autojoin.

VSF member renumbered

A user requested a renumber of a VSF member.

VSF switchover requested

A user requested a VSF switchover.

VSX software update

Reset triggered by a VSX software update.

Chassis critical temperature

Chassis operating temperature exceeded.

Chassis low critical temperature

Chassis temperature below the minimum operating t
hreshold.

Chassis insufficient fans

Insufficient fans to cool the chassis.

Public

show boot-history 36

Boot History String

Description

Chassis unsupported PSUs/fans

Unsupported or misconfigured PSUs or system fans.

Management module critical temperature

ISSU SMM update

ISSU switchover

ISSU aborted

Management module operating temperature exceed
ed.

Standby management module reboot triggered by a
n In‐Service Software Upgrade (ISSU).

Redundancy switchover triggered by an In‐Service
Software Upgrade.

Standby management module reset triggered by fail
ure during an In‐Service Software Upgrade.

Rollback timer expired

Reset triggered by the ISSU rollback timer expiring.

Examples

Showing the boot history of the active management module:

switch# show boot-history

Management module

=================

Index : 2

Boot ID : c34a2c2499004a02bbeeff4992e1fdbd

Current Boot, up for 1 days 13 hrs 13 mins 27 secs

Index : 1

Boot ID : bfba9bc486304e57904ac717a0ccbdcd

02 Sep 23 02:55:33 : CPU request reset with 0x20201, Version:

FL.10.14.0000-1619-ga9ec1805bd442~dirty

02 Sep 23 02:55:33 : Switch boot count is 2

Index : 0

Boot ID : a88a71b7ca9a4574af7e3b811ddfdc7e

02 Sep 23 02:49:26 : Reboot requested by user, Version: FL.10.14.0000-1619-

ga9ec1805bd442~dirty

02 Sep 23 02:50:02 : Switch boot count is 1

Index : 3

Boot ID : f00ba10c8c44457f83fee303d014a89a

25 Aug 23 10:27:42 :  Power on reset with 0x1, Version: FL.10.14.0000-1465-

g9df95249d06b0~dirty

25 Aug 23 10:28:18 :  Switch boot count is 3

25 Aug 23 10:29:02 :  Primary overtemperature fault detected with 0x2 in

PSU 1/1

Public

show boot-history 37

switch#

Management module

=================

Index : 3

Boot ID : f1bf071bdd04492bbf8439c6e479d612

Current Boot, up for 22 hrs 12 mins 22 secs

Index : 2

Boot ID : edfa2d6598d24e989668306c4a56a06d

07 Aug 18 16:28:01 : Reboot requested through database

Index : 1

Boot ID : 0bda8d0361df4a7e8e3acdc1dba5caad

07 Aug 18 14:08:46 : Reboot requested through database

Index : 0

Boot ID : 23da2b0e26d048d7b3f4b6721b69c110

07 Aug 18 13:00:46 : Reboot requested through database

Line module 1/1

=================

Index : 3

10 Aug 17 12:45:46 : dune_agent crashed

...

Management module

=================

Index : 3

Boot ID : f1bf071bdd04492bbf8439c6e479d612

Current Boot, up for 22 hrs 12 mins 22 secs

Index : 2

Boot ID : edfa2d6598d24e989668306c4a56a06d

07 Aug 18 16:28:01 : Reboot requested through database

Index : 1

Boot ID : 0bda8d0361df4a7e8e3acdc1dba5caad

07 Aug 18 14:08:46 : Reboot requested through database

Index : 0
Boot ID : 23da2b0e26d048d7b3f4b6721b69c110

07 Aug 18 13:00:46 : Reboot requested through database

Line module 1/1

=================

Index : 3

10 Aug 17 12:45:46 : dune_agent crashed

...
switch# show boot-history
Management module

=================

Index : 2

Public

show boot-history 38

Boot ID : a61ad00d10864c748bc7893a5d4af2e4

15 Dec 23 19:02:02 : Power on reset with 0x1, Version: FL.10.13.1000AF

15 Dec 23 19:02:02 : Switch boot count is 0

15 Dec 23 19:02:17 : PSU 1/1: Fault detected

Index : 1

Boot ID : 30d831bbfdfa425baf50a629ee01b185

15 Dec 23 19:01:58 : Power on reset with 0x1, Version: FL.10.13.1000AF

15 Dec 23 19:01:58 : Switch boot count is 0

switch# show boot-history vsf member 2

Member-2

=========

Index : 0

Boot ID : df99026c194a44f1944a3e7685fb4d90

Current Boot, up for 3 hrs 31 mins 39 secs

Index : 3

Boot ID : 7bf4104903fe4ad1ba4bce40e8099c76

10 Aug 17 10:02:24 : Reboot requested through database

10 Aug 17 10:02:13 : Switch boot count is 2

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

L1-100Mbps downshift

The speed downshift feature allows the user to link-up at sub-optimal speeds when failing to link-up at
the highest advertised speed. There are fixed number of link attempts made to establish link at highest
advertised speed and when all of them fail and attempt is made to link-up at a lower possible speed.

Public

L1-100Mbps downshift 39

This feature requires underlying PHY to have support for the same and hence capability is only added to
select set of ports. If a link cannot be established at the highest common denominator within a set number of
link attempts, the PHY advertises the next highest speed using auto-negotiation.

Subtopics

Limitations with speed downshift
L1-100Mbps downshift commands

Limitations with speed downshift

•  Link up may be delayed as certain number of retries are done to establish the link at highest advertise

speeds by both link partners before downshifting.

•  Link may be established at sub-optimal speed.

L1-100Mbps downshift commands

Subtopics

downshift enable
show interface
show interface downshift-enable
show running-config interface

downshift enable

Syntax

downshift-enable

no downshift-enable

Description

Enables/disables automatic speed downshift on an interface that supports downshift, generally 1GBASE-T
ports. When enabled, downshift allows an interface to link at a lower advertised speed when unable to
establish a stable link at the maximum speed. Downshifting only applies to physical interfaces that are
not members of a LAG and is only available when auto-negotiation is enabled. When only one speed is
advertised, downshift will not be triggered.

Public

Limitations with speed downshift 40

Examples

switch(config-if)# interface 1/1/1

switch(config-if)# downshift-enable

Warning: this is a non-standard mode for use only when standards-based

auto-negotiation is not able to establish a stable link. Enabling this

may cause the port to link at a lower than expected speed and should

not be used on ports that are members of a LAG. Support calls may require

this feature to be disabled

Continue (y/n)?

switch(config-if)#

When automatic downshift is enabled:

switch(config-if)# show running-config interface

interface 1/1/1

    downshift-enable

Disabling automatic speed downshift:

switch(config-if)# interface 1/1/1

switch(config-if)# no downshift-enable

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

show interface

Public

show interface 41

Syntax

show interface [<IFNNAME>|<IFRANGE>] [brief | physical]

show interface [<IFNNAME>|<IFRANGE>] [extended [non-zero] | [human-

readable]]

show interface [<IFNNAME>] monitor [human-readable]

show interface [lag | vlan ] [<ID>] [brief]

show interface lag [<LAG-ID>] [extended [non-zero] | [human-readable]]

show interface lag [<LAG-ID>] monitor [human-readable]

Description

Shows active configurations and operational status information for interfaces.

Parameter

Description

Specifies a interface name.

<IFNAME>

<IFRANGE>

brief

physical

extended

human‐readable

non‐zero

LAG

Specifies the port identifier range.

Shows brief info in tabular format.

Shows the physical connection info in tabular format.

Shows additional statistics, including the tx filtered and rx filte
red counters.

•  Rx filter packets are protocol packets received when the p

rotocol is disabled on the switch and there is only one port i
n the VLAN. Protocols include OSPF, PIM, RIP, LACP, and LL
DP.

•  An example of a Tx filtered packet would be a multicast pac

ket being filtered from going out of the ingress port.

Shows statistics rounded to the nearest power of 1000, for exa
mple, 1K, 345M, 2G. This is available only in the CLI interface o
utput.

Shows only non zero statistics.

Shows LAG interface information.

Public

show interface 42

Description

Continuously monitor interface statistics.

Shows VLAN interface information.

Specifies the LAG number. Range: 1‐256

Specifies the VLAN ID. Range: 1‐4094

Parameter

monitor

VLAN

<LAG‐ID>

<VLAN‐ID>

Examples

switch# show interface 1/1/1

Interface 1/1/1 is up

Admin state is up

Link state: up for 2 days (since Sun Jun 21 05:30:22 UTC 2020)

Link transitions: 1

Description: backup data center link

Hardware: Ethernet, MAC Address: 70:72:cf:fd:e7:b4

MTU 1500

Type 1GbT

Full-duplex

qos trust none

Speed 1000 Mb/s

Auto-negotiation is on

Flow-control: off

Error-control: off

                Energy-Efficient Ethernet is enabled

                MDI mode: MDIX

L3 Counters: Rx Enabled, Tx Enabled

Rate collection interval: 300 seconds

Rates                           RX                   TX        Total (RX+TX)

------------- -------------------- -------------------- --------------------

Mbits / sec                   0.00                 0.00                 0.00

KPkts / sec                   0.00                 0.00                 0.00

Unicast                       0.00                 0.00                 0.00

Multicast                     0.00                 0.00                 0.00

Broadcast                     0.00                 0.00                 0.00

Utilization %                 0.00                 0.00                 0.00

Public

show interface 43

Statistics                      RX                   TX                Total

------------- -------------------- -------------------- --------------------

Packets                          0                    0                    0

Unicast                          0                    0                    0

Multicast                        0                    0                    0

Broadcast                        0                    0                    0

Bytes                            0                    0                    0

Jumbos                           0                    0                    0

Dropped                          0                    0                    0

Filtered                         0                    0                    0

Pause Frames                     0                    0                    0

L3 Packets                       0                    0                    0

L3 Bytes                         0                    0                    0

Errors                           0                    0                    0

CRC/FCS                          0                  n/a                    0

Collision                      n/a                    0                    0

Runts                            0                  n/a                    0

Giants                           0                  n/a                    0

Other                            0                    0                    0
Showing information when interface 1/1/1 is configured:

MDI mode: MDIX

VLAN Mode: native-untagged

Native VLAN: 1

Allowed VLAN List: all

Rate collection interval: 300 seconds

Rates                           RX                   TX        Total (RX+TX)

------------- -------------------- -------------------- --------------------

Mbits / sec                   0.00                 0.00                 0.00

KPkts / sec                   0.00                 0.00                 0.00

Unicast                       0.00                 0.00                 0.00

Multicast                     0.00                 0.00                 0.00

Broadcast                     0.00                 0.00                 0.00

Utilization %                 0.00                 0.00                 0.00

Statistics                      RX                   TX                Total

------------- -------------------- -------------------- --------------------

Packets                          0                    0                    0

Unicast                          0                    0                    0

Multicast                        0                    0                    0

Broadcast                        0                    0                    0

Bytes                            0                    0                    0

Jumbos                           0                    0                    0

Dropped                          0                    0                    0

Filtered                         0                    0                    0

Public

show interface 44

Pause Frames                     0                    0                    0

Errors                           0                    0                    0

CRC/FCS                          0                  n/a                    0

Collision                      n/a                    0                    0

Runts                            0                  n/a                    0

Giants                           0                  n/a                    0
Showing information when the interface is currently linked at a downshifted speed:

switch(config-if)# show interface 1/1/1

Interface 1/1/1 is up

...

Auto-negotiation is on with downshift active
Showing information when the interface is currently linked with energy-efficient-ethernet negotiated:

switch(config-if)# show interface 1/1/1

Interface 1/1/1 is up

...

Energy-Efficient Ethernet is enabled and active

switch(config-if)# show interface 1/1/1

Interface 1/1/1 is down

Admin state is up

State information: Disabled by VSX

Link state: down for 3 days (since Tue Mar 16 05:20:47 UTC 2021)

Link transitions: 0

Description:

Hardware: Ethernet, MAC Address: 04:09:73:62:90:e7

MTU 1500

Type SFP+DAC3

Full-duplex

qos trust none

Speed 0 Mb/s

Auto-negotiation is off

Flow-control: off
Error-control: off

VLAN Mode: native-untagged

Native VLAN: 1

Allowed VLAN List: 1502-1505

Rate collection interval: 300 seconds

Rate                               RX                   TX        Total

(RX+TX)

---------------- -------------------- --------------------

--------------------

Mbits / sec                      0.00                 0.00

0.00

KPkts / sec                      0.00                 0.00

Public

show interface 45

0.00

Unicast                          0.00                 0.00

0.00

Multicast                        0.00                 0.00

0.00

Broadcast                        0.00                 0.00

0.00

Utilization                      0.00                 0.00

0.00

Statistic                          RX                   TX

Total

---------------- -------------------- --------------------

--------------------

Packets                             0

0                    0

Unicast                             0

0                    0

Multicast                           0

0                    0

Broadcast                           0

0                    0

Bytes                               0

0                    0

Jumbos                              0

0                    0

Dropped                             0

0                    0

Pause Frames                        0

0                    0

Errors                              0

0                    0

CRC/FCS                             0
n/a                    0

Collision                         n/a

0                    0

Runts                               0

n/a                    0

Giants                              0

n/a                    0
Showing information when the interface is configured with EEE and the EEE has auto-negotiated:

switch(config-if)# show interface 1/1/1 physical

----------------------------------------------------------------------------

----------------------------------------------------------------

Public

show interface 46

Link    Admin         Speed           Flow-

Control          EEE       PoE Power                      Port

Port        Type           Status   Config   Status | Config    Status |

Config   Status | Config  (Watts)    State Information  Description

----------------------------------------------------------------------------

----------------------------------------------------------------

1/1/1       1GbT           up       up       1G       auto      off

off      on       on       --        10M/100M/1G        --
Showing the monitor information:

NOTE

In monitor mode, the CLI refreshes data automatically until it is exited by
entering q. Pressing ? opens the help menu to display which options are available
in this context.

Interface 1/1/1 is up

Rate                               RX                   TX        Total

(RX+TX)

---------------- -------------------- --------------------

--------------------

MBits / sec                  30196.43             30196.43

60392.85

MPkts / sec                  58977.39             58977.40

117954.79

Unicast                          0.00                 0.00

0.00

Multicast                    58977.39             58977.40

117954.79

Broadcast                        0.00                 0.00

0.00

Utilization %                   75.49                75.49

150.98

Statistic                          RX                   TX        Total

(RX+TX)

---------------- -------------------- --------------------

--------------------

Packets                    4756527649           4756527865

9513055514

Unicast                             0

0                    0

Multicast                  4756527649           4756527865

9513055514

Broadcast                           2

Public

show interface 47

0                    2

Bytes                    304417778668         304417795428

608835574096

Jumbos                              0

0                    0

Dropped                             0          19028847730

19028847730

Pause Frames                        0

0                    0

Errors                              0

0                    0

CRC/FCS                             0

n/a                    0

help: ?, quit: q

Help for Interface Monitor

h  Toggle human-readable mode

c  Clear interface statistics

Does not apply to rates

Arrows, PgUp, PgDn, Home, End

Navigate interface statistics

Delay: 2

help: ?, quit: q
Showing the output for interface 1/1/1 in human-readable format:

NOTE
In human-readable format, the < 1 symbol for Utilization indicates that the
amount of packets is between zero and one. This is true in cases where the
number of bytes increases but the number of packets and the Utilization value is
not displayed even in the normal output, where the human-readable parameter is
not included in the command.

switch(config-if)# show interface 1/1/1 human-readable
Interface 1/1/1 is up

Rate                               RX                   TX        Total

(RX+TX)

---------------- -------------------- --------------------

--------------------

Bits / sec                         3M

3M                   6M

Pkts / sec                        316                  316

633

Unicast                           319                  319

638

Multicast                           0

Public

show interface 48

0                    0

Broadcast                           0

0                    0

Utilization %                     < 1                  < 1

< 1

Statistic                          RX                   TX

Total

---------------- -------------------- --------------------

--------------------

Packets                          577K

577K                   1M

Unicast                          577K

577K                   1M

Multicast                           0

51                   51

Broadcast                           0

15                   15

Bytes                            744M

745M                   1G

Jumbos                              0

0                    0

Dropped                             0

0                    0

Filtered                            0

0                    0

Pause Frames                        0

0                    0

Errors                              0

0                    0

CRC/FCS                             0

n/a                    0

Collision                         n/a
0                    0

Runts                               0

n/a                    0

Giants                              0

n/a                    0
Showing information about extended counters:

NOTE
The output of the  show interface extended  command varies
depending on the switch model and configuration.

Public

show interface 49

switch(config-if)# show interface 1/1/17 extended

-------------------------------------------------------------------

Interface 1/1/17

-------------------------------------------------------------------

Statistics                                     Value

-------------------------------------------------------------------

Dot1d Tp Port In Frames                        547

Dot1d Tp Port Out Frames                       608

Dot3 In Pause Frames                           0

Dot3 Out Pause Frames                          0

Ethernet Stats Broadcast Packets               19

Ethernet Stats Bytes                           40162

Ethernet Stats Packets                         342

...

-------------------------------------------------------------------

Error-Statistics                               Value

-------------------------------------------------------------------

Dot1d Base Port MTU Exceeded Discards          0

Dot3 Control In Unknown Opcodes                0

Dot3 Stats Alignment Errors                    0

Dot3 Stats FCS Errors                          0

Dot3 Stats Frame Too Longs                     0

Dot3 Stats Internal Mac Transmit Errors        0

Ethernet RX Oversize Packets                   0

...
Showing interface link-status:

switch# show interface link-status

-------------------------------------------------------------

Port           Type           Physical    Link         Last

                              Link State  Transitions  Change

-------------------------------------------------------------

1/1/1          1G-BT          down        0            --

1/1/2          1G-BT          up          1            1 minute ago (Fri

Mar 09 12:36:56 UTC 2018)

1/1/3          1G-BT          up          1            1 minute ago (Fri

Mar 09 12:36:56 UTC 2018)

1/1/4          --             down        0            --

1/1/5          --             down        0            --
Showing interface loopback 1 link-status:

-------------------------------------------------------------

                              Physical    Link         Last

Port           Type           Link State  Transitions  Change

Public

show interface 50

-------------------------------------------------------------

loopback1      --             up          --           --
Showing interface 1/1/2-1/1/3 link-status:

-------------------------------------------------------------

                              Physical    Link         Last

Port           Type           Link State  Transitions  Change

-------------------------------------------------------------

1/1/2          1G-BT          up          1            1 minute ago (Fri

Mar 09 12:36:56 UTC 2018)

1/1/3          1G-BT          up          1            1 minute ago (Fri

Mar 09 12:36:56 UTC 2018)
Showing interface link-status:

switch# show interface link-status

-------------------------------------------------------------------------

Port           Type            Physical    Link        Link Flaps  Last

                               Link State  Transitions Ignored     Change

-------------------------------------------------------------------------

1/1/1          1G-BT           down        0           0           --

1/1/2          1G-BT           up          1           0           1 minute

ago (Fri Mar 09 12:36:56 UTC 2018)

1/1/3          1G-BT           up          1           0           1 minute

ago (Fri Mar 09 12:36:56 UTC 2018)

1/1/4          --              down        0           0           --

1/1/5          --              down        0           0           --
Showing state information when interface is blocked:

8360(config-if)# show interface 1/1/1

Interface 1/1/1 is up (Blocked)

Admin state is up

State information: Blocked by UDLD

Link state: up for 1 minute (since Mon Jun 10 09:25:27 UTC 2024)

Link transitions: 1

Description:

Persona:

Hardware: Ethernet, MAC Address: 00:fd:45:67:85:91

MTU 1500

Type 10G-LR / 10G SFP+ LR

Full-duplex

qos trust none

Speed 10000 Mb/s

Auto-negotiation is off

Flow-control: off

Error-control: off

Public

show interface 51

VLAN Mode: access

Access VLAN: 1

Rate collection interval: 300 seconds

Rate                               RX                   TX        Total

(RX+TX)

---------------- -------------------- --------------------

--------------------

Mbits / sec                      0.00                 0.00

0.00

KPkts / sec                      0.00                 0.00

0.00

Unicast                          0.00                 0.00

0.00

Multicast                        0.00                 0.00

0.00

Broadcast                        0.00                 0.00

0.00

Utilization %                    0.00                 0.00

0.00

Statistic                          RX                   TX

Total

---------------- -------------------- --------------------

--------------------

Packets                            15

15                   30

Unicast                            12

12                   24

Multicast                           3

3                    6

Broadcast                           0

0                    0

Bytes                            1350                 1350
2700

Jumbos                              0

0                    0

Dropped                             0

0                    0

Pause Frames                        0

0                    0

Errors                              0

0                    0

CRC/FCS                             0

n/a                    0

Public

show interface 52

Collision                         n/a
0                    0
Runts                               0
n/a                    0
Giants                              0
n/a                    0
Command History
| Release |     | Modification |     |     |     |     |
| ------- | --- | ------------ | --- | --- | --- | --- |
10.15 Added state information when port goes into down state.
| 10.11 |     | Added  monitor |  parameter. |             |     |     |
| ----- | --- | -------------- | ----------- | ----------- | --- | --- |
| 10.10 |     | Added          |             |  parameter. |     |     |
human‐readable
| 10.07 or earlier |     | ‐‐  |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- |
Command Information
| Platforms | Command context |     | Authority |     |     |     |
| --------- | --------------- | --- | --------- | --- | --- | --- |
All platforms Operator (> ) or Manage Operators or Administrators or local user group members with
r (#) execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show interface downshift-enable
Syntax
show interface [<IFNNAME>|<IFRANGE>] downshift-enable
Description
Displays speed downshift information, including the interface speed status and configuration.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
Specifies a interface name.

|     | Public |     |     |     | show interface downshift-enable | 53  |
| --- | ------ | --- | --- | --- | ------------------------------- | --- |

Description

Specifies the port identifier range.

Parameter

<IFNAME>

<IFRANGE>

Examples

Showing automatic downshift information:

switch(config-if)# show interface downshift-enable

-------------------------------------------------

              Downshift              Speed

Port      Enabled | Active    Status   | Config

-------------------------------------------------

1/1/1     yes       yes       100M-FDx   auto

1/1/2     yes       no        1G         auto

1/1/3     yes       no        100M-FDx   100M-FDx

1/1/4     no        no        --         auto
Showing automatic downshift information on per interface:

switch(config-if)# show interface 1/1/2 downshift-enable

-------------------------------------------------

              Downshift              Speed

Port      Enabled | Active    Status   | Config

-------------------------------------------------

1/1/2     yes       no        1G         auto

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show interface downshift-enable 54

Command Information
| Platforms | Command context | Authority |     |     |
| --------- | --------------- | --------- | --- | --- |
4100i config Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
6000
ommand from the operator context (>) only.
6100

show running-config interface
Syntax
show running-config interface [<IFNNAME>|<IFRANGE>]
show running-config interface [lag | loopback | tunnel | vlan ] [<ID>]
Description
Displays active configurations of various switch interfaces.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
Specifies a interface name.

<IFNAME>

Specifies the port identifier range.

<IFRANGE>

| LAG      |     | Specifies LAG interface information       |     |     |
| -------- | --- | ----------------------------------------- | --- | --- |
| LOOPBACK |     | Specifies loopback interface information. |     |     |
| TUNNEL   |     | Specifies tunnel interface information.   |     |     |
| VLAN     |     | Specifies VLAN interface information.     |     |     |
Specifies the LAG number. Range: 1‐256.

|     | Public |     | show running-config interface | 55  |
| --- | ------ | --- | ----------------------------- | --- |

Parameter

<LAG‐ID>

Description

Specifies the LOOPBACK number. Range: 0‐255.

Specifies the tunnel ID. Range: 1‐255.

Specifies the VLAN ID. Range: 1‐4094.

Specifies the VXLAN interface information.

Specifies the VXLAN interface identifier. Default: 1.

<LOOPBACK‐ID>

<TUNNEL‐ID>

<VLAN‐ID>

VXLAN

<VXLAN‐ID>

Examples

Showing 1/1/2 interface configuration:

switch(config-if)# show running-config interface 1/1/2

interface 1/1/2

   no shutdown

   description DC-23

   exit
Showing loopback interfaces configured:

switch(config-if)# show running-config interface loopback

interface loopback 1

    description lb interface 1

    exit

interface loopback 2

    description lb interface 2
    exit
Showing loopback interfaces not configured:

switch(config-if)# show running-config interface loopback

No loopback interfaces configured.

Public

show running-config interface 56

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

4100i

6000

6100

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

Mirroring

Mirroring allows you to replicate all traffic arriving and/or leaving the selected system interfaces. This data
can be used for collection or analysis.

The traffic replicated using mirroring can be sent to a separate interface on the same switch as the traffic
source for analysis or inspection. Such a collection of interfaces and settings is called a mirror session.

A mirror session can be configured with many traffic sources but only a single output, or destination. In the
initial configuration, the mirror session is disabled. You have enable the feature to start the replication.

CAUTION

Care must be taken in choosing the number and rates of sources to avoid
over-saturating a session destination. A mirror session with multiple 10G sources
can overwhelm a single 10G destination and important data may be lost.

This version of AOS-CX support the following mirror capabilities:

•  Support for a VLAN as source for a mirror session

•  6100, 6000 and 4100i Switch series support of 2 simultaneously enabled Mirroring Sessions with LAG

sources, regardless of direction

•  Ability for a given Mirror source in one session to act as source in another Mirror Session

•  Support for a Layer 2/bridged Link Aggregation Group (LAG) as Session destination

Public

Mirroring 57

•  Support for a Layer 3/Route-only Link Aggregation Group (LAG) as Session destination

NOTE

The following interface types are not supported as mirror source or destination:

•  Management

•  Persona

•  Loopback

•  VxLAN

•  Subinterfaces

Hit Count Behavior for Policy Mirroring Actions

When using classifier policies with mirroring actions, it is important to note that packets mirrored via these
policy actions will have their hit counts recorded within the Policy hit counts. These packets will not be
recorded as output packets in the Mirror Session statistics, except in the case of Mirror-to-CPU sessions.
This distinction means that traffic metrics for packets mirrored via Policy Actions should be obtained from
Policy hit counts, as these packets will not appear in the Mirror Session output statistics.

Mirroring and CoPP

When configuring a Mirror Session with the destination set to the CPU, it is important to understand how
mirrored traffic interacts with Control Plane Policing (CoPP).

Control plane packets that are already destined for the switch (for example, routing protocol packets and
management traffic) will be processed by their respective CoPP classes. These packets will still be mirrored
to the CPU as part of the Mirror-to-CPU session, but they will not be counted under the Mirror-to-CPU CoPP
class. The Mirror-to-CPU CoPP class is specifically designed to manage dataplane traffic that is mirrored to
the CPU. Any control plane traffic mirrored to the CPU will bypass this class and be handled by the CoPP
class corresponding to its original purpose (e.g., OSPF, BGP, or ARP). Administrators should account for this
distinction when analyzing traffic mirrored to the CPU.

For example, if a mirror session is configured to mirror all traffic from a source interface to the CPU, and
that interface receives OSPF packets, the OSPF packets will be mirrored to the CPU. these packets will be
processed by the OSPF CoPP class, not the Mirror-to-CPU CoPP class.

Subtopics

Mirror statistics
Classifier policies and mirroring sessions
Mirroring commands

Public

Mirroring 58

Mirror statistics

Mirror statistics are reset for a Mirror-to-CPU session when an interface is added or removed from a LAG
that is a source interface in the Mirror session and during a failover.

Classifier policies and mirroring sessions

About this task

Network traffic can be mirrored to a destination interface in two ways:

•  Using a mirroring session alone.

•  Using Classifier Policies with mirror actions in conjunction with a mirroring session.

Basic mirroring sessions provide coarse control over the type of traffic mirrored from a source: all received,
all transmitted, or both. However, a traffic class within a Classifier Policy applied to a source can provide
much finer grained control of mirrored traffic. For example, a policy can match on many different aspects
of the Ethernet or IPv4 or IPv6 header information in each frame or packet received or transmitted on an
interface.

The steps to configure a policy and class with a mirror action are the following:

Procedure

1.  Configuring a mirroring session with a destination interface.

2.  Enabling the mirroring session.

3.  Configuring the Classifier Policy, specifying the mirroring session ID in the mirror action.

Results

If the packets being mirrored are received from a VLAN that is not allowed on the mirror destination, the
mirrored packets would be dropped at the mirror destination interface. When the mirrored packets are
dropped at the destination, the mirror output packet and byte count will increment, however the packets will
not be received at the mirror destination.

The mirror destination port among the active mirror sessions must be unique. That is, if an interface is
configured as a source or destination in an active mirror session, the same port cannot be used as a
destination in another active mirror session.

Scenario 1

Scenario 2

Public

Mirror statistics 59

Mirroring commands

Subtopics

clear mirror
comment
destination interface
destination tunnel
diagnostic
disable
enable
mirror endpoint
mirror session
show mirror
show mirror endpoint
source interface

clear mirror

Syntax

clear mirror [all | <SESSION-ID>]

Description

Clears the mirror statistics for all configured mirror sessions or a specified session

Description

Specifies all configured sessions.

Specifies a numeric identifier for the session. Range: 1 to 4

Parameter

all

<SESSION‐ID>

Examples

Clearing mirror statistics for all configured mirror sessions:

switch# clear mirror all

Clearing mirror statistics for mirror session 1:

Public

Mirroring commands 60

switch# clear mirror 1

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

comment

Syntax

comment <COMMENT>

no comment

Description

Specifies a comment for the mirroring session.

When used in mirror endpoint command context, specifies a comment for the mirror endpoint.

The no form of this command removes the comment.

Parameter

Description

A comment string of up to 64 characters composed of letters, n
umbers, underscores, dashes, spaces, and periods.

<COMMENT>

Usage

Comments are optional and can be added or removed at any time without affecting the state of the
mirroring session.

Public

comment 61

Adding a comment to a session that already has a comment replaces the existing comment.

Examples

Adding a comment to a mirror session:

switch(config-mirror-3)# comment This Mirror will be removed during next

maintenance window

Removing the comment from mirror session 3:

switch(config-mirror-3)# no comment

Adding a comment to a mirror endpoint:

switch(config-mirror-endpoint-test)# comment Monitor endpoint traffic

Replacing the existing comment for mirror endpoint:

switch(config-mirror-endpoint-test)# comment Monitor statistics on each

endpoint interfaces

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

config‐mirror‐
<SESSION‐ID>

Administrators or local user group members with execution righ
ts for this command.

destination interface

Public

destination interface 62

Syntax

destination interface {<INTERFACE-ID>|<LAG-NAME>}

no destination interface {<INTERFACE-ID>|<LAG-NAME>}

Description

Configures the specified interface as the destination of the mirrored traffic.

The no form of this command immediately disables the mirroring session and removes the specified
destination interface from the configuration.

Parameter

Description

Specifies a interface. Format:  member/slot/port .

<INTERFACE‐ID>

<LAG‐NAME>

Usage

Specifies a LAG (link aggregation group) identifier.

Configuring a different destination interface in an enabled mirroring session causes all mirrored traffic to
use the new destination interface. This action might cause a temporary suspension of mirrored source traffic
during the reconfiguration. Mirroring traffic to a LAG destination with a device running LACP attached to the
destination will cause the LAG link to flap if LACP packets are part of the mirrored traffic source.

Examples

Configuring a mirroring session and adding an interface as a destination:

switch(config)# mirror session 1
switch(config-mirror-1)# destination interface 1/1/1

Replacing the existing destination with different interface:

switch(config-mirror-1)# destination interface 1/1/12

Removing a destination:

switch(config-mirror-1)# no destination interface 1/1/12

Public

destination interface 63

Switch Destination interface limit per mirror session (4 possible sess
ions)
| 4100i |     | 1   |     |     |
| ----- | --- | --- | --- | --- |
| 6000  |     | 1   |     |     |
| 6100  |     | 1   |     |     |
| 10040 |     | 1   |     |     |
Command History
Release Modification
10.07 or earlier ‐‐
Command Information
| Platforms | Command context | Authority |     |     |
| --------- | --------------- | --------- | --- | --- |
All platforms config‐mirror‐ Administrators or local user group members with execution righ
|     | <SESSION‐ID> | ts for this command. |     |     |
| --- | ------------ | -------------------- | --- | --- |

destination tunnel
Syntax
destination tunnel <TUNNEL-IPV4-ADDR> source <SOURCE-IPv4-ADDR>
   dscp <DSCP-VALUE> vrf <VRF-NAME> id <SPAN-ID>
no destination tunnel
Description
Specifies the tunnel where all mirrored traffic for the session is transmitted. Only one tunnel destination is
allowed per session.
You may configure multiple mirror sessions with the same source/destination IP address pair, however, only
one of those sessions sharing the same source/destination IP address pair can be enabled at a given time.
|     | Public |     | destination tunnel | 64  |
| --- | ------ | --- | ------------------ | --- |

ERSPAN is not supported leaving the switch by the OOB port. If VRF management is configured for an
ERSPAN session, the session will be in "mirror_err_tunnel_oob_port_not_supported" operation status.

ERSPAN is not supported leaving the switch encapsulated within another tunnel (e.g. GRE IPv4).
When the path to the destination IP address will leave via a tunnel, the session will be in
"tunnel_route_resolution_not_populated" operation status.

NOTE

The interface/LAG used to transmit ERSPAN packets should not be a source in
the same mirror session.

The no form of this command will cease the use of the tunnel and disable the session.

Parameter

Description

Specifies the tunnel address in IPv4 format (x.x.x.x), where x is
a decimal number from 0 to 255.

Specifies the source address in IPv4 format (x.x.x.x), where x is
a decimal number from 0 to 255.

Specifies the DSCP value to be carried within the DS field of E
RSPAN packet header. Range: 0 to 63. Default: 0.

Specifies a VRF name. Default: default.

<TUNNEL‐IPV4‐ADDR>

<SOURCE‐IPv4‐ADDR>

<DSCP‐VALUE>

<VRF‐NAME>

Examples

Creating a Mirror Session and adding tunnel destination, source, dscp, and VRF:

switch# config

switch(config)# mirror session 1

switch(config-mirror-1)# destination tunnel 1.1.1.1 source 2.2.2.2 dscp 10
vrf default

Replacing the existing tunnel destination:

Public

destination tunnel 65

switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp

10 vrf default

Replacing the existing destination with a different DSCP value:

switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp

2 vrf default

Removing the destination:

switch(config-mirror-1)# no destination tunnel

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

config‐mirror‐
<SESSION‐ID>

Administrators or local user group members with execution righ
ts for this command.

diagnostic

Syntax

diagnostic

diag utilities tshark [file]

diag utilities tshark [delete-file]

Public

diagnostic 66

Description

Captures packets from a mirror-to-cpu session, and save the most recent 32MB to pcap file which can then
be copied and analyzed. When capturing a mirror-to-cpu session to a file, packets will not be dumped to the
console.

NOTE
The  diagnostic  command must be entered prior to the  diag utiliti
es tshark  command.

Use the delete-file form of this command to delete the most recent capture file.

Since file and delete-file are optional, the behavior of the base command diag utilities tshark does not
save anything to a file, and instead dumps the tshark session to the console until CTRL + c is entered.

Parameter

file

Description

Saves captured packets to a temporary file.

delete‐file

Deletes the most recent captured file.

Example

Performing diagnostic:

switch# diagnostic

switch# diagnostic utilities tshark file

Inspecting traffic mirrored to the CPU until Ctrl-C is entered

^CEnding traffic inspection.

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

Public

diagnostic 67

disable

Syntax

disable

Description

Disables the mirroring session specified by the current command context.

Usage

By default, mirroring sessions are disabled.

When a mirroring session is disabled, the show mirror command for that session ID shows an Admin Status
of disable and an Operation Status of disabled.

Example

Disabling a mirroring session:

switch(config)# mirror session 3

switch(config-mirror-3)# disable

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

config‐mirror‐
<SESSION‐ID>

Administrators or local user group members with execution righ
ts for this command.

enable

Public

disable 68

Syntax

enable

Description

Enables the mirroring session for the current command context.

Usage

By default, mirroring sessions are disabled.

When a mirroring session is enabled, the show mirror command for that session ID shows an Admin Status
of enable and an Operation Status of enabled.

If sFlow is enabled on an interface and a mirroring session specifies the same interface as the source of
received traffic (the source is configured with a direction of

rx
or

both
):

•  The attempt to enable the mirroring session fails and an error is returned.

NOTE

When adding, removing, or changing the configuration of a source interface in
an enabled mirroring session, packets from other mirror sources using the same
destination interface might be interrupted.

Example

Configuring and enabling a mirroring session:

switch(config)# mirror session 3

switch(config-mirror-3)# source interface 1/1/2 rx

switch(config-mirror-3)# destination interface 1/1/3
switch(config-mirror-3)# comment Monitor router port ingress-only traffic

switch(config-mirror-3)# enable

Command History

Release

Modification

10.07 or earlier

‐‐

Public

enable 69

Command Information

Platforms

Command context

Authority

All platforms

config‐mirror‐
<SESSION‐ID>

Administrators or local user group members with execution righ
ts for this command.

mirror endpoint

Syntax

mirror endpoint <NAME>

no mirror endpoint <NAME>

Description

Creates the specified mirror endpoint or enters its context if it already exists. The specifics of a mirror
endpoint are created or altered while in the mirror endpoint context and the mirror endpoint is enabled or
disabled from this context. It may be possible to support different encapsulations by different ASICs. For
example, UDP for PVOS compatibility. Termination of GRE encapsulation is also supported.

The no form of this command removes an existing mirror endpoint. An enabled mirror endpoint is
automatically disabled first before removal.

Parameter

Description

Specifies mirror endpoint name.

<NAME>

Examples

Creating a mirror endpoint named test :

switch(config)# mirror endpoint test

Deleting mirror endpoint named test:

switch(config)# no mirror endpoint test

Public

mirror endpoint 70

Configuring a mirror endpoint named test :

6100(config)# mirror endpoint test

6100(config-mirror-endpoint-test)#

6100(config-mirror-endpoint-test)# destination

  interface  Specify interfaces to send traffic

6100(config-mirror-endpoint-test)# destination interface

  IFNAMELIST  An interface, a range or a comma seperated list of interfaces

6100(config-mirror-endpoint-test)# destination interface 1/1/3

  <cr>

6100(config-mirror-endpoint-test)# destination interface 1/1/3

6100(config-mirror-endpoint-test)#

6100(config-mirror-endpoint-test)# source 1.1.1.1 destination 1.1.1.2 id 1

vrf default

6100(config-mirror-endpoint-test)#

NOTE

Only physical ports can be configured as interface for mirror-endpoint
destination. LAG port is not supported as interface for mirror-endpoint
destination.

NOTE

The maximum allowed number of destination interfaces for both mirror-session
and mirror-endpoint is 1.

Command History

Release

Modification

10.13.1000

Added support for 4100i, 6000, and 6100 switches.

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

Public

mirror endpoint 71

mirror session

Syntax

mirror session <SESSION-ID>

no mirror session <SESSION-ID>

Description

Creates a mirroring session configuration context or enters an existing mirroring session configuration
context.

From this context, you can enter commands to configure and enable or disable the mirroring session.

The no form of this command removes an existing mirroring session from the configuration.

Parameter

Description

Specifies the session identifier. Range: 1 to 4

<SESSION‐ID>

Examples

switch(config)# mirror session 1

switch(config-mirror-1)#

switch(config)# mirror session 3

switch(config-mirror-3)#

switch(config)# no mirror session 1

switch(config)#

NOTE

When configuring mirroring via the command-line interfacde, not all
configuration errors will result in an immediate error message. After making
configuration changes, always check the operation status of your mirror sessions
using the show mirror command.

Public

mirror session 72

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

show mirror

Syntax

show mirror [<SESSION-ID>]

Description

Shows information about mirroring sessions. If  <SESSION-ID>  is not specified, then the command
shows a summary of all configured mirroring sessions. If  <SESSION-ID>  is specified, then the command
shows detailed information about the specified mirroring session.

Parameter

Description

Specifies the session identifier. Range: 1 to 4

<SESSION‐ID>

Usage

Information in the Admin Status column of the command output indicates the configured status. The admin
status is one of the following values:

•  enable: The mirroring session is enabled.

•  disable: The mirroring session has been configured but not yet enabled, or has been disabled.

Public

show mirror 73

Information in the Operation Status colum indicates the status of the mirroring session. Operation status is
one of the following values:

•  dest_doesnt_exist:The configured destination interface is not found in the system. The mirroring

session cannot be enabled.

•  destination_shutdown: The mirroring session is enabled, but the destination interface is shut down.

No traffic can be monitored.

•  disabled: The mirroring session is disabled and is not in an error condition.

•  enabled: The mirroring session is enabled.

•  external/driver_error: An internal ASIC hardware error occurred.

•  hit_active_sessions_capacity: The mirroring session could not be enabled because the maximum

number of supported mirroring sessions are already enabled.

•

internal_error: An invalid parameter was passed to the ASIC software layer.

•  no_dest_configured: The mirroring session does not have a destination interface configured.

•  no_name_configured: A software error occurred. The mirroring session does not have a session ID in its

configuration.

•  null_mirror: A software error occurred. The session object reference is invalid.

•  out_of_memory: The system is out of memory, reboot recommended.

•  tunnel_route_resolution_not_populated: If the destination tunnel IP address is not reachable.

•  unknown_error: An unexpected error occurred.

Examples

Showing summary information about all configured mirroring sessions:

switch# show mirror
ID  Admin Status  Operation Status

--- ------------- ----------------------------------------------------

1   enable        enabled

2   disable       disabled

3   disable       disabled

4   enable        internal_error
Showing detailed information about a single mirroring session:

switch# show mirror 3

 Mirror Session: 3

 Admin Status: disable

 Operation Status: disabled

Public

show mirror 74

Comment: Monitor router port ingress-only traffic

 Source: interface 1/1/2 rx

 Destination: interface 1/1/3

switch#
Show the details of mirror session 1 with an empty LAG as destination:

switch: show mirror 1

Admin Status: enable

Operation Status: dest_doesnt_exist

Source: interface 1/1/1 rx

Source: interface tx none

Destination: interface lag1

Output Packets: 0

Output Bytes: 0
Show the details of mirror session 1 with a LAG and a LAG member of same LAG as sources. In this scenario,
traffic received on all LAG member interfaces is mirrored, is it is not necessary to define 1/1/1 as a source
since it is already part of LAG1; this does not impact the mirror output packet or byte counters.

switch: show mirror 1

Admin Status: enable

Operation Status: enabled

Source: interface 1/1/1 rx

Source: interface lag1 rx

Destination: interface 1/1/2

Output Packets: 0

Output Bytes: 0
Showing the details of mirror session 1 for a mirror configuration enabled with invalid interface which is not
part of a lag:

switch# show mirror 1

Mirror Session: 1

Admin Status: enable

Operation Status: disabled

Source: interface 1/1/1 (unknown lag) both
Destination: cpu

Output Packets: 0

Output Bytes: 0
Certain configurations can cause this condition while the mirror source configuration remains unchanged:

1.  Removing of a port from a LAG (Link Aggregation Group).

2.  Port split or unsplit operations that result in LAG membership removal.

To recover from this issue, unconfigure the affected interface (previously part of a LAG), or restore the LAG
membership configuration.

Public

show mirror 75

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

show mirror endpoint

Syntax

show mirror endpoint [<NAME>]

Description

Shows a list of all configured mirror endpoints, their Admin Status and their Operation Status.

The optional parameter will display the details of the specified mirror endpoint if it exists.

Parameter

Description

Specifies name of the mirror endpoint instance to be displayed.

<NAME>

Examples

Showing a summary of all configured mirror endpoints on the switch:

switch# show mirror endpoint
Name    Admin Status   Operation Status

-----  -------------- ----------------------------------------------------

test    enable         enabled

monitor disable        disabled

Public

show mirror endpoint 76

Showing the details of enabled mirror endpoint test:

switch# show mirror endpoint test

Mirror Endpoint: audit

Admin Status: enable

Operation Status: enabled

Comment: Mirror Endpoint Audit

Type: gre

Tunnel: source 1.1.1.1 destination 1.1.1.2 id 1 vrf default

Interface: 1/1/3

Output Packets: 123456789

Output Bytes: 0

NOTE

"Output Packets" in "show mirror endpoint [name]" is only supported for
statistics.
"Output Bytes" in "show mirror endpoint [name]" is not supported due to ASIC
limitation.

Command History

Release

Modification

10.13.1000

Added support for 4100i, 6000, and 6100 switches.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

4100i

6000

6100

Public

show mirror endpoint 77

source interface

Syntax

source interface {<PORT-NUM> | <LAG-NAME>} [<DIRECTION>]

no source interface {<PORT-NUM> | <LAG-NAME>} [<DIRECTION>]

Description

Configures the specified interface (either an Ethernet port or a LAG) as a source of traffic to be mirrored.

The no form of this command ceases mirroring traffic from the specified source interface and removes the
source interface from the mirroring session configuration.

Parameter

Description

<PORT‐NUM>

<LAG‐NAME>

<DIRECTION>

Specifies a physical port on the switch. Use the format membe
r/slot/port (for example, 1/3/1).

Specifies the identifier for the LAG (link aggregation group).

Selects the direction of traffic to be mirrored from this source in
terface. There is no default for this parameter. Valid values are t
he following:

•  both: Mirror both transmitted and received packets.
•  rx: Mirror only received packets.
•  tx: Mirror only transmitted packets.

Usage

There is a limit of source interfaces in each direction of a given mirror session:

Switch

4100i

6000

6100

Source interface limit per mirror session (4 possibl
e sessions)

28

52

52

Public

source interface 78

Switch

10040

Source interface limit per mirror session (4 possibl
e sessions)

128

However, there is a practical limit to the amount of traffic that a mirror destination can transmit. For example,
mirroring session with multiple 10G sources can overwhelm a single 10G destination.

NOTE

When adding, removing, or changing the configuration of a source port in an
enabled mirroring session, packets from other mirror sources using the same
destination port might be interrupted.

Examples

Configuring a mirrored traffic source interface:

switch(config-mirror-1)# source interface

  LAG-NAME      Enter a LAG name. For example, lag10

  PORT-NUM      Enter a port number
Creating a mirroring session and configuring a source interface to mirror both transmitted and received
packets:

switch(config)# mirror session 1

switch(config-mirror-1)# source interface 1/1/1 both

Creating a second mirroring session and configuring two source interfaces. One port mirroring only
transmitted packets and the other mirroring both transmitted and received packets:

switch(config)# mirror session 2

switch(config-mirror-2)# source interface 1/1/3 tx

switch(config-mirror-2)# source interface 1/2/1 both

Removing the first source interface:

switch(config-mirror-2)# no source interface 1/2/3

Configuring a source interface to mirror received packets only:

switch(config-mirror-3)# source interface 1/1/2 rx

Configuring a source interface to mirror both transmitted and received packets:

switch(config-mirror-1)# source interface 1/1/1 both

Configuring a LAG as source interface to mirror both transmitted and received packets:

Public

source interface 79

switch(config-mirror-4)# source interface lag1 both

Stopping the mirroring of received packets from a configured source interface:

switch(config-mirror-4)# no source interface lag1 rx

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

config‐mirror‐
<SESSION‐ID>

Administrators or local user group members with execution righ
ts for this command.

Monitoring a device using SNMP

Configuring SNMP: Refer to the SNMP/MIB Guide for information on how to add SNMP so a device can be
monitored from a network management system (NMS).

Configuring an SNMP trap receiver: Refer to the SNMP/MIB Guide and specific information about the  sho
w snmp trap  command to enable SNMP traps.

Packet Capture

The Packet Capture is a solution which enables the Central administrator to capture or view packets
from clients connected to Halon switches. The solution serves as a tool which an admin can leverage to
debug clients connected to managed devices across branches in an enterprise. The switch requires packet
exchanges to be copied to the CPU (both ingress and egress packets) per client session, so that they can be
streamed to Central where the admin can view the packet exchanges for further analysis.

This feature is supported on the following platforms:

Public

Monitoring a device using SNMP 80

•  Rosewood (6200, 6300, 6400, 8360)

•  Matrix (4100i, 6000, 6100)

Power-over-Ethernet

•  The Power-over-Ethernet (PoE) subsystem manages power supplied to devices using standard Ethernet
data cables. A Power Sourcing Equipment (PSE) supplies DC power as well as Ethernet connectivity
to a Powered Device (PD) using a standard Ethernet cable. The maximum current depends on the PD
Requested Class.

•  A PoE subsystem contains two parts : a PSE and PD. A Power Sourcing Equipment (PSE) is a device that
provides power through a standard Ethernet cable. A PoE capable switch functions as PSE. All Aruba
PoE switches are considered as PSEs. A PD is a device powered by a PSE. Examples of PD are VoIP
phones, Wireless APs, and IP cameras.

•  When a PD or any network cable is connected to a PSE port, the PSE applies a detection voltage and
measures the resistance value of the PD. If resistance is within IEEE 802.3 standard values (23 - 26k
ohm), the connected device is treated as PD and classification begins. For legacy devices to be detected,
you must enable prestandard detection on the switch.

•  PDs are divided into different types and classes based on PD power requirements. The power supplied
by the PSE is higher than the power PD draws to accommodate for the line losses that can result with
the use of the standard maximum length cable(100m).

◦  Type 1: PSE can supply maximum of 15.4W, and PD can draw a maximum of 13W.

◦  Type 2: PSE can supply maximum of 30W, and PD can draw a maximum of 25.5W.

◦  Type 3: PSE can supply maximum of 60W, and PD can draw a maximum of 51W.

◦  Type 4: PSE can supply maximum of 90W, and PD can draw a maximum of 71W.

•  Classes of PD:

◦  Class 0: Type1 PD, it can draw a maximum of 13W.

◦  Class 1: Type1 PD, it can draw a maximum of 3.84W.

◦  Class 2: Type1 PD, it can draw a maximum of 6.49W.

◦  Class 3: Type1 PD, it can draw a maximum of 13W.

◦  Class 4: Type2 PD, it can draw a maximum of 25.5W.

◦  Class 5: Type3 PD, it can draw a maximum of 40W.

Public

Power-over-Ethernet 81

◦  Class 6: Type3 PD, it can draw a maximum of 51W.

◦  Class 7: Type4 PD, it can draw a maximum of 62W.

◦  Class 8: Type4 PD, it can draw a maximum of 71.3W.

•

IEEE 802.3bt introduced 4-Pair PoE as a means of supplying higher power to PDs that need more than
the current 25.5W supplied by IEEE 802.3at. To increase the available power without damaging the
Ethernet cable, the standard introduced the ability to use all four pairs within the Ethernet cable instead
of the two pairs used by previous standards (802.3at, 802.3af).

•  Supported protocols:

◦  Compatibility with IEEE 802.3af, 802.3at, 802.3bt and prestandard.

◦  Long first class event supported on Type 3-4 PSE.

◦  Support for Single Signature (SS) Type 0-6 and Dual Signature (DS) Type 0-4 PDs.

◦  Multi-Event classification permits mutual ID of SS Class 0-6 and DS Class 0-4.

◦  Support LLDP Data Link Layer (DLL) Type 1-2 extension 12-octet TLV and Type 3-4 extension

29-octet TLV.

◦  Default PSE assigned class delivers the maximum PSE capable power at initial power up based on

PD requested class.

•  Always-on PoE is a feature that provides the ability for a switch to continue to provide power across user
initiated reboots through software. Always-on PoE is enabled by default and no additional configuration
is needed.

NOTE

PDs only remain powered, no data transfer or PoE power negotiation can occur
until the switch has completely booted up and in normal operation. PD faults
occurring prior to full switch boot up will result in PoE power removal and restart
the detection process only after switch returns to normal operation.

Subtopics

PoE commands

PoE commands

All PoE configuration commands except quick-poe, threshold configuration and always-on poe
configuration are entered at the config-if context. The PoE threshold command is used at the system

Public

PoE commands 82

level whereas the always-on poe and power-over-ethernet quick-poe commands are set at the slot level.
These commands can only be configured in the global configuration context.

Subtopics

lldp dot3 poe
lldp med poe
power-over-ethernet
power-over-ethernet allocate-by
power-over-ethernet always-on
power-over-ethernet assigned-class
power-over-ethernet pre-std-detect
power-over-ethernet priority
power-over-ethernet quick-poe
power-over-ethernet threshold
power-over-ethernet trap
show lldp local
show lldp neighbor
show power-over-ethernet

lldp dot3 poe

Syntax

lldp dot3 poe

no lldp dot3 poe

Description

Enables 802.3 TLV list in LLDP to advertise for Power over Ethernet Data Link Layer Classification. LLDP
dot3 TLV is by default enabled for PoE.

The no form of this command disables 802.3 TLV list in LLDP.

Examples

Enabling 802.3 TLV list in LLDP:

switch(config)# interface 1/1/1

switch(config-if)# lldp dot3 poe

Disabling 802.3 TLV list in LLDP:

switch(config-if)# no lldp dot3 poe

Public

lldp dot3 poe 83

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

lldp med poe

Syntax

lldp med poe [priority-override]

no lldp med poe [priority-override]

Description

Enables MED TLV list in LLDP to advertise for Power over Ethernet Data Link Layer Classification. Also
enables the lldp-MED TLV priority to override user configured port priority for Power over Ethernet. When
both dot3 and MED are enabled, dot 3 will take precedence. MED TLV is by default enabled for PoE. Priority
over-ride is by default disabled.

The no form of this command disables MED TLV list in LLDP.

Parameter

Description

[priority‐override]

System defined name of the interface.

Examples

Enabling and disabling LLDP MED PoE:

switch(config)# interface 1/1/1

switch(config-if)# lldp med poe

Public

lldp med poe 84

switch(config-if)# no lldp med poe

Enabling and disabling LLDP MED PoE priority override:

switch(config-if)# lldp med poe priority-override

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

power-over-ethernet

Syntax

power-over-ethernet

no power-over-ethernet

Description

Enables per-interface power distribution. Per-port power is enabled by default with priority low. PoE cannot
be disabled for individual ports when Quick PoE is enabled for the entire switch or line module.

The no form of this command disables per-interface power distribution.

Examples

Enabling per-interface power distribution:

switch(config)# interface 1/1/1

switch(config-if)# power-over-ethernet

Public

power-over-ethernet 85

Disabling per-interface power distribution:

switch(config-if)# no power-over-ethernet

Showing Quick PoE enabled:

switch(config)# power-over-ethernet quick-poe 1/1

switch(config)# no power-over-ethernet

Interface PoE cannot be disabled when Quick PoE is enabled.

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

power-over-ethernet allocate-by

Syntax

power-over-ethernet allocate-by {usage | class}

no power-over-ethernet allocate-by {usage | class}

Description

Configures the power allocation method. Power allocation method is initially based on usage. PSE Allocated
power value will change to LLDP negotiated power if and when LLDP exchange takes place between PSE
and PD. When there is no LLDP negotiation, PSE Allocated Power Value will be the actual instantaneous
power draw and reserve power based on actual consumption. In allocate-by class, power allocation is based
on PD requested class and PSE allocated power value will be the LLDP negotiated power when LLDP
exchange takes place between PSE and PD. When there is no LLDP negotiation, PSE Allocate Power will be
based on PD class. Reserve power is based on PD Class. By default, power allocation is by usage.

Public

power-over-ethernet allocate-by 86

The power allocation method can be changed on an interface through port-access (User roles or RADIUS).
An allocation method when configured through port-access will replace the user configured method.

The no form of this command resets the action to default.

Parameter

usage

class

Usage

Description

Configures the usage‐based allocation method.

Configures the class‐based allocation method.

If you enable pd-class-override for an interface, the allocate-by configuration of that interface will be
automatically changed to class. However, if you change the allocation method to usage when pd-class-
override is still enabled, you will receive an error message stating that "The power allocation method cannot
be changed when pd-class-override is enabled."

To remove pd-class-override, you can use the no power-over-ethernet pd-class-override command . It is
important to note that pd-class-override requires the allocation method to be set to class and is enforced
when configured through CLI. However, if you override the allocation method to usage via port-access,
pd-class-override will not be in effect. Therefore, it is recommended that you do not override the allocation
method to usage through port-access on interfaces configured with pd-class-override.

Examples

Configuring the power allocation method:

switch(config)# interface 1/1/1

switch(config-if)# power-over-ethernet allocate-by usage

switch(config-if)# power-over-ethernet allocate-by class

Resetting power allocation method:

switch(config-if)# no power-over-ethernet allocate-by class

Command History

Release

Modification

10.07 or earlier

‐‐

Public

power-over-ethernet allocate-by 87

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

power-over-ethernet always-on

Syntax

power-over-ethernet always-on <MODULE-ID>

no power-over-ethernet always-on <MODULE-ID>

Description

Always-on PoE is a feature that provides the ability to the switch to continue to provide power across a soft
reboot. It is applicable only to the interfaces which were connected and delivering before the soft reboot.
Also, power will not be delivered if power to the switch is interrupted. This command enables or disables the
always-on PoE feature at the switch or the slot level. By default, always-on PoE is enabled at the switch or
the slot level.

The no form of this command disables power distribution on soft reboot.

Parameter

Description

Module number to apply always‐on PoE configuration.

<MODULE‐ID>

Examples

Enabling per-interface power distribution:

switch(config)# power-over-ethernet always-on 1/1

Disabling per-interface power distribution:

switch(config)# no power-over-ethernet always-on 1/1

Public

power-over-ethernet always-on 88

Command History

Release

10.08

Modification

Command introduced

Command Information

Platforms

Command context

Authority

4100i

config

Administrators or local user group members with execution righ
ts for this command.

power-over-ethernet assigned-class

Syntax

power-over-ethernet assigned-class {3 | 4 | 6}

no power-over-ethernet assigned-class

Description

Limit PoE power based on the assigned class. When an user assigns a maximum class to an interface, the
PSE will limit the maximum power delivered to the PD up to a total power draw not exceeding the PSE
assigned-class power. Power demotion occurs when a PD requested class is higher than the PSE assigned
class, permitting the PD to receive power and operate in a reduced power mode. PoE ports cannot set an
assigned class when Quick PoE is enabled on the sybsystem. The default assigned class is 4 for 2-pair
capable PSE and 6 for 4-pair capable PSE.

The no form of this command resets the action to default.

Examples

Setting PoE assigned class:

switch(config)# interface 1/1/1

switch(config-if)# power-over-ethernet assigned-class 4

Resetting PoE assigned class to default:

switch(config-if)# no power-over-ethernet assigned-class 4

Showing Quick PoE enabled:

Public

power-over-ethernet assigned-class 89

switch(config)# power-over-ethernet quick-poe 1/1

switch(config)# interface 1/1/1

switch(config)# power-over-ethernet assigned-class 4

Interface assigned class cannot be configured when Quick PoE is enabled.

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

power-over-ethernet pre-std-detect

Syntax

power-over-ethernet pre-std-detect

no power-over-ethernet pre-std-detect

Description

Before IEEE 802.3 released the first Power over Ethernet standard (802.3af), vendors had shipped PoE
capable switches and PD's. HPE Aruba Networking switches are backward compatible and will support
both IEEE standard and pre-standard 802.3af Power over Ethernet PD's concurrently. This CLI allows the
user to enable or disable pre-802.3af-standard device detection and powering on the specific port. When
pre-std-detect is enabled, power will be delivered on PairA only. Default is disabled.

The no form of this command resets the action to default.

Examples

Enabling pre-standard device detection:

Public

power-over-ethernet pre-std-detect 90

switch(config)# interface 1/1/1

switch(config-if)# power-over-ethernet pre-std-detect

Disabling pre-standard device detection:

switch(config-if)# no power-over-ethernet pre-std-detect

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

power-over-ethernet priority

Syntax

power-over-ethernet priority {critical | high | low}

no power-over-ethernet priority {critical | high | low}

Description

Sets PoE priority for an interface Specifying critical, high, or low indicates the priority of the interface in
the event of power over-subscription. Within the same priority level, higher power-priority line-module ports
have higher precedence. With same PoE priority and same line-module priority, lower numbered line-module
ports have higher precedence. Per-interface PoE priority is low by default.

The no form of this command resets the priority to default PoE priority "low".

Examples

Configuring PoE priority:

Public

power-over-ethernet priority 91

switch(config)# interface 1/1/1

switch(config-if)# power-over-ethernet priority critical

switch(config-if)# power-over-ethernet priority high

Resetting the PoE priority to default:

switch(config-if)# no power-over-ethernet priority high

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

power-over-ethernet quick-poe

Syntax

power-over-ethernet quick-poe <MODULE-ID>
no power-over-ethernet quick-poe <MODULE-ID

NOTE
This command is not available on the 6000 or 6100 Switch Series.

NOTE
This command is available only on the 4100i Switch Series.

Public

power-over-ethernet quick-poe 92

Description

Quick PoE is a feature that provides the ability for the switch to provide power to the connected powered
device as soon as switch goes through cold reboot. When quick PoE is enabled on the subsystem PoE port
disablement and PD demotion is not allowed. also quick PoE enablement is not allowed if any of the port is
disabled on the subsystem. User should not over-subscribe the PoE power when quick PoE is enabled. Quick
PoE saved configuration will work irrespective of the configuration change at reboot.

Enables quick PoE feature on the switch or the subsystem level. By default, quick-PoE is disabled for the
subsystem.

The no form of this command disables quick PoE.

Parameter

Description

Specifies module number for quick PoE configuration .

<MODULE‐ID>

Examples

Enabling and disabling quick PoE:

switch(config)# power-over-ethernet quick-poe 1/2

switch(config)# no power-over-ethernet quick-poe 1/2

switch(config-if)# power-over-ethernet quick-poe 1/1

PoE must be enabled on all interfaces before enabling Quick PoE

switch(config-if)# power-over-ethernet quick-poe 1/3

All interfaces must use the default assigned class before enabling Quick PoE

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

config‐if

Administrators or local user group members with execution righ
ts for this command.

Public

power-over-ethernet quick-poe 93

power-over-ethernet threshold

Syntax

power-over-ethernet threshold <PERCENTAGE>

no power-over-ethernet threshold <PERCENTAGE>

Description

Sets the threshold at which the system will send an excess power consumption notification trap. Default
value is 80 percentage.

The no form of this command resets the action to default.

Parameter

Description

Excess power consumption trap threshold. Range 1‐99.

<PERCENTAGE>

Examples

Setting the power-over-ethernet threshold:

switch(config)# power-over-ethernet threshold 75

Resetting the power-over-ethernet threshold to default:

switch(config-if)# no power-over-ethernet threshold 75

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

config

Public

Administrators or local user group members with execution righ
ts for this command.

power-over-ethernet threshold 94

Platforms

Command context

Authority

6100

power-over-ethernet trap

Syntax

power-over-ethernet trap

no power-over-ethernet trap

Description

This command enables/disables the SNMP trap generation for PoE related events at system level. PoE trap
generation is enabled by default.

The no form of this command resets the priority to default PoE priority "low".

Examples

Enabling SNMP trap generation for PoE:

switch(config)# power-over-ethernet trap

Disabling SNMP trap generation for PoE:

switch(config-if)# no power-over-ethernet trap

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

Public

power-over-ethernet trap 95

show lldp local

Syntax

show lldp local-device [<INTERFACE-ID>]

Description

Displays information advertised by the switch if the LLDP feature is enabled by user.

Parameter

Description

Specifies an interface. Format: member/slot/port

<INTERFACE‐ID>

Examples

Showing LLDP local device:

switch# show lldp local-device 1/1/10

Local Port Data

===============

Port-ID           : 1/1/10

Port-Desc         : "1/1/10"

Port VLAN ID      : 0

PoE Plus Information

PoE Device Type    : Type 2 PSE

Power Source       : Primary

Power Priority     : low
PSE Allocated Power: 25.0 W

PD Requested Power : 25.0 W

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show lldp local 96

Command Information

Platforms

Command context

Authority

4100i

6000

6100

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show lldp neighbor

Syntax

show lldp neighbor [<INTERFACE-ID>]

Description

Displays detailed information about a particular neighbor connected to a particular interface.

Parameter

Description

Specifies an interface. Format: member/slot/port

<INTERFACE‐ID>

Examples

Showing LLDP neighbor information when there is only one neighbor:

switch# show lldp neighbor-info 1/1/10

Port                           : 1/1/10

Neighbor Entries               : 1

Neighbor Entries Deleted       : 0

Neighbor Entries Dropped       : 0

Neighbor Entries Aged-Out      : 0

Neighbor Chassis-Name          : 84:d4:7e:ce:5d:68

Neighbor Chassis-Description   : ArubaOS (MODEL: 325), Version HPE_ANW IAP

Neighbor Chassis-ID            : 84:d4:7e:ce:5d:68

Neighbor Management-Address    : 169.254.41.250

Chassis Capabilities Available : Bridge, WLAN

Chassis Capabilities Enabled   :

Public

show lldp neighbor 97

Neighbor Port-ID               : 84:d4:7e:ce:5d:68

Neighbor Port-Desc             : eth0

TTL                            : 120

Neighbor Port VLAN ID          :

Neighbor PoEplus information   : DOT3

Neighbor Device Type           : TYPE2 PD

Neighbor Power Priority        : Unkown

Neighbor Power Source          : Primary

Neighbor Power Requested       : 25.0 W

Neighbor Power Allocated       : 0.0 W

Neighbor Power Supported       : No

Neighbor Power Enabled         : No

Neighbor Power Class           : 5

Neighbor Power Paircontrol     : No

Neighbor Power Pairs           : SIGNAL

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

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show power-over-ethernet

Syntax

show power-over-ethernet [member <MEMBER-ID>] [brief]

Description

Displays the status information of the full system.

Public

show power-over-ethernet 98

Parameter

Description

Displays the detailed status of given member.

<MEMBER‐ID>

brief

Examples

Display the brief status of all ports or the given port.

Showing sample output for show power-over-ethernet :

switch# show power-over-ethernet

System Power Status

  PoE  Power Status            : No redundancy

  Operational Power Status     : No redundancy

  Total Available Power        : 360 W

  Total Configured Power       :   0 W

  Total Failover Pwr Avl       :   0 W

  Total Redundancy Power       :   0 W

  Total Power Drawn            :   0 W

  Total Power Reserved         :   0 W

  Total Remaining Power        : 360 W

  Trap Threshold               : 80 %

  Trap Enabled                 : Yes

  Always-on PoE Enabled        : 1/1

  Quick PoE Enabled            : None

Internal Power

        Total Power

  PS    (Watts)        Status

  ----- -------------  ---------------------
  1/1   0              Ok

  1/2   0              Absent
Showing sample output for power-over-ethernet brief per-port:

switch# show power-over-ethernet 1/1/1 brief

Status and Configuration Information for port 1/1/1

  Member 1Power Status

    Available: 370 W  Reserved: 55.60 W  Remaining: 314.40 W
    Always-on PoE Enabled: 1/1
PoE      Pwr Power    Pre-std Alloc PSE Pwr PD Pwr PoE Port     PD     Cls

Type

Port     En  Priority Detect  Act   Rsrvd   Draw   Status       Sign

Public

show power-over-ethernet 99

-------  --- ------   ------- ----- ------  ------ ---------    -----  ---

----

1/1/1    Yes Low      Off     Class  0.0 W   0.0 W Denied       None   4   2
Showing sample output for power-over-ethernet brief for interface range:

switch# show power-over-ethernet 1/1/1-1/1/2 brief

Status and Configuration Information for port 1/1/1-1/1/2

    Power Status

    Available: 360 W  Reserved: 0.00 W  Remaining: 360.00 W

    Always-on PoE Enabled: 1/1

    Quick PoE Enabled: None

PoE      Pwr Power    Pre-std Alloc PSE Pwr PD Pwr PoE Port     PD     Cls

Type

Port     En  Priority Detect  Act   Rsrvd   Draw   Status       Sign

-------  --- ------   ------- ----- ------  ------ ---------    -----  ---

----

1/1/1    Yes Low      Off     Usage  0.0 W   0.0 W Searching    N/A    N/A

N/A

1/1/2    Yes Low      Off     Usage  0.6 W   0.0 W Searching    N/A    N/A

N/A
Showing sample output for power-over-ethernet for a missing line card:

switch# show power-over-ethernet 1/3 brief

Module 1/3 is not physically present.
Showing sample output for power-over-ethernet port when physical interface is not present:

switch# show power-over-ethernet 2/1/1

Interface 2/1/1 is not present.

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

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

Public

show power-over-ethernet 100

Aruba AirWave

You can manage and monitor the AOS-CX switch through Aruba AirWave. The following benefits and
functions include:

•  Configuration (partial configuration)

•  Device topology

•

Immediate and historical trend reports

•  Monitoring of the device and user connected to the network.

•  Network discovery

•  Syslogs and trap receiver

For information about which versions of Aruba AirWave support AOS-CX, see the AOS-CX Release Notes.

Subtopics

SNMP support and AirWave
Supported features with AirWave and the AOS-CX switch
Configuring the AOS-CX switch to be monitored by AirWave
AirWave commands

SNMP support and AirWave

For AirWave to discover and monitor the switch, you must:

•  Enable the SNMP services on the switch.

•  Configure the SNMP agent to use the SNMP version supported by the management station.

SNMP on the switch

The switch provides SNMP services through the management channel and the data interfaces. Functionality,
such as device discovery from NMS, syslog and trap forwarding, can be any channel configured by you.

Although the SNMP server can be enabled on both VRFs ( mgmt  and  default ), only one instance of
SNMP can be running. The highest priority is on the  default  VRF.

For example, assume that SNMP is first enabled on the  mgmt  VRF ( snmp-server vrf mgmt ).
Then, SNMP is enabled on the  default  VRF ( snmp-server vrf default ) without disabling
SNMP on the  mgmt  (using an equivalent  no  form of the command). The  show running-config

Public

Aruba AirWave 101

command displays both  snmp-server vrf  commands; however, the SNMP instance is running only on
the  default  VRF (highest priority).

switch# config

switch(config)# snmp-server vrf mgmt

switch(config)# snmp-server vrf default

switch(config)# show running-config

Current configuration:

!

!Version AOS-CX Virtual.10.01.

led locator on

!

!

!

snmp-server vrf default

snmp-server vrf mgmt

!

...

Supported features with AirWave and the AOS-CX switch

AirWave supports the following features with the AOS-CX switch:

Device management

Device discovery using SNMPv2C and SNMPv3

Device dashboards

Monitoring management

Device health attributes (device status/reachability)

Interface and VLAN management

Initiates an SSH connection from Aruba AirWave to
AOS-CX so that the device outputs from the AOS-CX
CLI can be displayed in the Aruba AirWave user inter
face.

Firmware versions

Displays neighbor devices connected to AOS-CX swi
tches

Device topology

Public

Supported features with AirWave and the AOS-CX swi... 102

S
u
p
p
o
r
t
e
d

f
e
a
t
u
r
e
s

w
i
t
h

A
i
r
W
a
v
e

a
n
d

t
h
e

A
O
S
-
C
X

s
w
i
.
.
.

Configuration management

Partial configuration

Alarm management

Alarm triggers (device and interface up/down, new d
evice discoveries, custom event triggers)

Report management

Syslogs and traps

Device inventory, interface utilization, and device rea
chability reports

Summary report of device model, firmware, and boot
loader version

Configuring the AOS-CX switch to be monitored by AirWave

Prerequisites

Aruba AirWave is active on the network.

Procedure

1.  Enable SNMP on the switch by entering the  snmp-server vrf  command.

switch(config)# snmp-server vrf mgmt

switch(config)# snmp-server vrf default

2.  Configure the SNMPv2C community to public by entering the  snmp-server community publ

ic  command. In this instance,  public  is a read-only community string.
switch(config)# snmp-server community public

3.  The community-string is used by SNMPv1 and SNMPv2C for unencrypted authentication. SNMPv3 lets
you encrypt the authentication mechanism. To enable SNMPv3, enter the  snmpv3 user  and  snmp
v3 context  commands.
switch(config)# snmpv3 user Admin auth sha auth-pass ciphertext

AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=

priv des priv-pass ciphertext

AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=

switch(config)# snmpv3 context Admin

For discovering devices in AirWave through the SNMPv3 community, the SNMPv3 context name is not
mandatory. Devices can still be discovered in Aruba AirWave without the SNMPv3 context name.

Public

Configuring the AOS-CX switch to be monitored by A... 103

C
o
n
fi
g
u
r
i
n
g

t
h
e

A
O
S
-
C
X

s
w
i
t
c
h

t
o

b
e

m
o
n
i
t
o
r
e
d

b
y

A
.
.
.

4.  Enter the  logging  command for enabling syslog forwarding to a remote syslog server, such as

AirWave:
switch(config)# logging 10.0.10.2 severity debug

5.  SNMP traps enable an agent to notify the management station of significant events by way of an

unsolicited SNMP message. Enable SNMP traps by entering the  snmp-server host  command:
switch(config)# snmp-server host 10.10.10.10 trap version v2c vrf default

SNMP traps cannot be forwarded from AOS-CX 10.00 switches that have the VRF configured as mgmt.
Later versions of AOS-CX support SNMP trap forwarding even when the VRF is configured as default or
mgmt.

6.  For information on how to add a device for monitoring in the Aruba AirWave user interface, see the

documentation for Aruba AirWave.

AirWave commands

Subtopics

logging
snmp-server community
snmp-server host
snmp-server vrf
snmpv3 context
snmpv3 user

logging

Syntax

logging {<IPV4-ADDR> | <IPV6-ADDR> | <FQDN | HOSTNAME>} {udp [<PORT-NUM>]}|

{tcp [<PORT-NUM>]}|{|tls [<PORT-NUM>]}

   auth-mode {certificate|subject-name}

   disable

   filter <FILTER-NAME>
   include-auditable-events
   legacy-tls-renegotiation]

   rate-limit-burst <BURST>

   rate-limit-interval <INTERVAL>] ]

Public

AirWave commands 104

severity <LEVEL>]

   vrf <VRF-NAME>]

no logging {<IPV4-ADDR> | <IPV6-ADDR> | <FQDN | HOSTNAME> }

Description

Enables syslog forwarding to a remote syslog server.

The no form of this command disables syslog forwarding to a remote syslog server.

Starting with AOS-CX 10.11, payload information is present in accounting logs.

The maximum REST payload that can be sent to RADIUS/TACACS server is 1024 characters, and the
maximum of REST payload that can be sent to syslog server is 3500 characters. If this limit is is reached, the
log will display three dots (...) to indicate that the log an exceeded the character limit and is incomplete.

Parameter

Description

{<IPV4‐ADDR> | <IPV6‐ADDR>
| <HOSTNAME>}

Selects the IPv4 address, IPv6 address, or host name of the rem
ote syslog server. Required.

[udp [<PORT‐NUM>] | tcp
[<PORT‐NUM> |
  tls [<PORT‐NUM>]]

Specifies the UDP port, TCP port, or TLS port of the remote sysl
og server to receive the forwarded syslog messages.

   udp [<PORT‐NUM>]

Range: 1 to 65535. Default: 514

   tcp [<PORT‐NUM>]

Range: 1 to 65535. Default: 1470

   tls [<PORT‐NUM>]

Range: 1 to 65535. Default: 6514

auth‐mode

disable

Specifies the TLS authentication mode used to validate the cert
ificate.

•  certificate: Validates the peer using trust anchor certificate

based authentication. Default.

•  subject‐name: Validates the peer using trust anchor certif

icates as well as subject‐name based authentication.

Disable remote syslog confguration. This does not delete the co
nfiguration, just disables/pauses the forwarding of syslog mess
agesto the remote server. The config/forwarding can be reenabl
ed (un‐paused) again using the no logging <hostname> disa
ble command.

filter <FILTER‐NAME>

Specifies the name of the filter to be applied on the syslog mes
sages.

include‐auditable‐events

Specifies that auditable messages are also logged to the remote
syslog server.

Public

logging 105

Parameter

Description

legacy‐tls‐renegotiation

Enables the TLS connection with a remote syslog server suppor
ting legacy renegotiation.

rate‐limit‐burst <BURST>

Specifies the rate limit for the messages sent to the remote sysl
og server.

rate‐limit‐interval
<INTERVAL>

Specifies the rate limit interval in seconds. Default: 30 Seconds

severity <LEVEL>

Specifies the severity of the syslog messages:

•  alert: Forwards syslog messages with the severity of alert

(6) and emergency (7).

•  crit: Forwards syslog messages with the severity of critical

(5) and above.

•  debug: Forwards syslog messages with the severity of deb

ug (0) and above.

•  emerg: Forwards syslog messages with the severity of eme

rgency (7) only.

•  err: Forwards syslog messages with the severity of err (4) a

•

nd above
info: Forwards syslog messages with the severity of info (1
) and above. Default.

•  notice: Forwards syslog messages with the severity of notic

e (2) and above.

•  warning: Forwards syslog messages with the severity of wa

rning (3) and above.

Specifies the VRF used to connect to the syslog server. Optional
. Default:  default

vrf <VRF‐NAME>

Examples

Enabling the syslog forwarding to remote syslog server 10.0.10.2:

switch(config)# logging 10.0.10.2

Enabling the syslog forwarding of messages with a severity of err (4) and above to TCP port 4242 on
remote syslog server 10.0.10.9 with VRF lab_vrf:

switch(config)# logging 10.0.10.9 tcp 4242 severity err vrf lab_vrf

Disabling syslog forwarding to a remote syslog server:

Public

logging 106

switch(config)# no logging

Enabling syslog forwarding over TLS to a remote syslog server using subject-name authentication mode:

switch(config)#logging example.com tls auth-mode subject-name

Applying log filtering for syslog server forwarding:

switch(config)# logging 10.0.10.6 severity info filter filter_lldp_logs vrf

mgmt

Applying log filtering and enabling the rate limit for syslog server forwarding over TCP port:

switch(config)# logging 10.0.10.2 tcp 3440 severity err vrf mgmt include-

auditable-events filter filter_lldp_logs rate-limit-burst 3 rate-limit-

interval 35

Command History

Release

Modification

10.12.1000

The disable parameter is introduced

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

snmp-server community

Syntax

snmp-server community <STRING>
no snmp-server community <STRING>

Public

snmp-server community 107

Description

Adds an SNMPv1/SNMPv2c community string. A community string is like a password that controls read/
write access to the SNMP agent. A network management program must supply this name when attempting
to get SNMP information from the switch. A maximum of 10 community strings are supported. Once you
create your own community string, the default community string ( public ) is deleted.

The no form of this command removes the specified SNMPv1/SNMPv2c community string. When no
community string exists, a default community string with the value public is automatically defined.

Parameter

Description

Specifies the SNMPv1/SNMPv2c community string. Range: 1 to
32 printable ASCII characters, excluding space and question ma
rk.

<STRING>

Subcommands

access-level {ro | rw}

no access-level {ro | rw}
This subcommand changes the access level of the SNMP community. The default access level is read-only
(ro).

The no form of this subcommand changes the access level of the community to default.

Parameter

Description

ro

rw

Specifies Read‐Only access with the SNMP community.

Specifies Read‐Write access with the SNMP community.

access-list {ip | ipv6} <ACL-NAME>

no access-list {ip | ipv6} <ACL-NAME>

This subcommand associates an ACL with the SNMP community. If an ACL is not associated with the SNMP
community, the default access is allowed for all the hosts.

The no form of this subcommand removes association of the ACL with the SNMP community.

Parameter

ip

ipv6

Description

Specifies the IPv4 ACL type.

Specifies the IPv6 ACL type.

Public

snmp-server community 108

Parameter

Description

Specifies the ACL name. It supports a maximum of 64 characte
rs.

<ACL‐NAME>

Examples

Setting the SNMPv1/SNMPv2c community string to private:

switch(config)# snmp-server community private

Removing SNMPv1/SNMPv2c community string private:

switch(config)# no snmp-server community private

Configuring the access level for the SMNP community to read-only:

switch(config-community)# access-level ro

Changing the access level of the SNMP community to default:

switch(config-community)# no access-level rw

Associating an IPv4 ACL named my_acl with the SMNP community:

switch(config-community)# access-list ip my_acl

Removing the associated IPv4 ACL named my_acl from the SNMP community:

switch(config-community)# no access-list ip my_acl

Configuration supported for SNMP ACL:

access-list ip ipv4_acl
    10 permit any 4.4.4.4 4.4.4.1

    20 permit any 3.3.3.3 3.3.3.1

access-list ipv6 ipv6_acl

    10 permit any 2001::2 2001::1

    20 permit any 3001::2 3001::1

snmp-server vrf default

snmp-server community my_comm_1

    access-list ip ipv4_acl

    access-list ipv6 ipv6_acl
Configuration not supported for SNMP ACL:

access-list ip ipv4_acl

    10 deny any 6.6.6.6 6.6.6.1

Public

snmp-server community 109

access-list ipv6 ipv6_acl

    10 deny any 6001::6 6000::1

snmp-server vrf default

snmp-server community my_comm_1

    access-list ip ipv4_acl

    access-list ipv6 ipv6_acl

NOTE
hitcounts for SNMP ACL will not be incremented.
Example:show access-list hitcounts ip all will not show the hit count of SNMP
ACL.

Command History

Release

10.14

Modification

Replaced the ipv4 parameter with the ip parameter. The ipv4 parameter is dep
recated.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config
config‐
community

Administrators or local user group members with execution righ
ts for this command.

snmp-server host

Syntax

snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community

<STRING>]
[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]
no snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION>

[community <STRING>]

[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]

snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community

Public

snmp-server host 110

<STRING>]

[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]

no snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community

<STRING>]

[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]

snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform

version v3] user <NAME> [port <UDP-PORT>] [<VRF-NAME>] [notification-type

<NOTIFICATION-TYPE>]

no snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform

version v3] user <NAME> [port <UDP-PORT>] [<VRF-NAME>] [notification-type

<NOTIFICATION-TYPE>]

Description

Configures a trap/informs receiver to which the SNMP agent can send SNMP v1/v2c/v3 traps or v2c informs.
A maximum of 30 SNMP traps/informs receivers can be configured.

The no form of this command removes the specified trap/inform receiver.

NOTE

Avoid configuring the same receiver for both SNMP traps and informs on the
same UDP port for v1, v2, and v3.

Parameter

Description

<IPv4‐ADDR>

<IPv6‐ADDR>

Specifies the IP address of a trap receiver in IPv4 format (x.x.x.
x), where x is a decimal number from 0 to 255. You can remove
leading zeros. For example, the address 192.169.005.100 beco
mes 192.168.5.100.

Specifies the IP address of a trap receiver in IPv6 format (x:x::x:
x).

trap version <VERSION>

Specifies the trap notification type for SNMPv1, v2c or v3. Avail
able options are: v1, v2c or v3.

inform version v2c

Specifies the inform notification type for SNMPv2c.

trap version v3

Specifies the trap notification type for SNMPv3.

user <NAME>

Specifies the SNMPv3 user name to be used in the SNMP trap n
otifications.

Public

snmp-server host 111

Parameter

Description

community <STRING>

<UDP‐PORT>

<VRF‐NAME>

Specifies the name of the community string to use when sendin
g trap notifications. Range: 1 ‐ 32 printable ASCII characters,
excluding space and question mark. Default: public.

Specifies the UDP port on which notifications are sent. Range: 1
‐ 65535. Default: 162.

Specifies the VRF on which the SNMP agent listens for incomin
g requests.

<notification‐type>

The supported notification types are:

Specifies the type of notification to be sent to the trap receiver.
If no type is specified, all notifications are sent.

interface
lldp
loop‐protect

•  aaa‐server
•  alarm
•  bgp
•  card
•  config
•  entity
•  fan
•
•
•
•  mac‐notify
•  mstp
•  mvrp
•  ospf
•  ospfv3
•  port‐security
•  power
•  power‐ethernet
•  rmon
•  rpvst
•  stp
•  temperature
•  vrrp
•  vsf

Public

snmp-server host 112

Parameter

Examples

Description

•  vsx

switch(config)# snmp-server host 10.10.10.10 trap version v1

switch(config)# no snmp-server host 10.10.10.10 trap version v1

switch(config)# snmp-server host a:b::c:d trap version v1

switch(config)# no snmp-server host a:b::c:d trap version v1

switch(config)# snmp-server host 10.10.10.10 trap version v2c community

public

switch(config)# no snmp-server host 10.10.10.10 trap version v2c community

public

switch(config)# snmp-server host a:b::c:d trap version v2c community public

switch(config)# no snmp-server host a:b::c:d trap version v2c community

public

switch(config)# snmp-server host 10.10.10.10 trap version v2c community

public port 5000

switch(config)# no snmp-server host 10.10.10.10 trap version v2c community

public port 5000

switch(config)# snmp-server host 10.10.10.10 trap version v2c community

public port 5000 vrf default

switch(config)# no snmp-server host 10.10.10.10 trap version v2c community

public port 5000 vrf default

switch(config)# snmp-server host a:b::c:d trap version v2c community public

port 5000

switch(config)# no snmp-server host a:b::c:d trap version v2c community

public port 5000

switch(config)# snmp-server host 10.10.10.10 inform version v2c community

public

switch(config)# no snmp-server host 10.10.10.10 inform version v2c

community public

switch(config)# snmp-server host a:b::c:d inform version v2c community

public

Public

snmp-server host 113

switch(config)# no snmp-server host a:b::c:d inform version v2c community

public

switch(config)# snmp-server host 10.10.10.10 inform version v2c community

public port 5000

switch(config)# no snmp-server host 10.10.10.10 inform version v2c

community public port 5000

switch(config)# snmp-server host 10.10.10.10 inform version v2c community

public port 5000 vrf default

switch(config)# no snmp-server host 10.10.10.10 inform version v2c

community public port 5000 vrf default

switch(config)# snmp-server host a:b::c:d inform version v2c community

public port 5000

switch(config)# no snmp-server host a:b::c:d inform version v2c community

public port 5000

switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin

switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin

switch(config)# snmp-server host a:b::c:d trap version v3 user Admin

switch(config)# no snmp-server host a:b::c:d trap version v3 user Admin

switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin

port 2000

switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin

port 2000

switch(config)# snmp-server host a:b::c:d trap version v3 user Admin port

2000
switch(config)# no snmp-server host a:b::c:d trap version v3 user Admin

port 2000

SNMP trap notification type examples:

switch(config)# snmp-server host 10.10.10.10 trap version v2c community
public notification-type bgp fan interface power entity

switch(config)# no snmp-server host 10.10.10.10 trap version v2c community

public notification-type bgp

switch(config)# snmp-server host a:b::c:d inform version v3 user Admin

Public

snmp-server host 114

notification-type bgp fan interface power-ethernet

switch(config)# no snmp-server host a:b::c:d inform version v3 user Admin

notification-type bgp interface

switch(config)# snmp-server host a:b::c:d inform version v3 user Admin

notification-type ?

  aaa-server      Sends AAA notifications.

  alarm           Sends Alarm notifications.

  bgp             Sends Border Gateway Protocol (BGP) state change

notifications.

  card            Sends Card notifications.

  config          Sends Configuration change notifications.

  entity          Sends Entity notifications.

  fan             Sends Fan notifications.

  interface       Sends Interface notifications.

  lldp            Sends Link Layer Discovery Protocol (LLDP) notifications.

  loop-protect    Sends Loop Protect notifications.

  mac-notify      Sends MAC Notify notifications.

  mstp            Sends Multiple Spanning Tree Protocol (MSTP)

notifications.

  mvrp            Sends Multiple VLAN Registration Protocol (MVRP)

notifications.

  ospf            Sends Open Shortest Path First (OSPFv2) notifications.

  ospfv3          Sends Open Shortest Path First version 3 (OSPFv3)

notifications.

  port-security   Sends Port Security notifications.

  power           Sends Power notifications.

  power-ethernet  Sends Power over Ethernet (PoE) notifications.

  rmon            Sends Remote Network Monitoring (RMON) notifications.

  rpvst           Sends Rapid Per VLAN Spanning Tree (RPVST) notifications.

  snmp            Sends Sends Simple Network Management Protocol (SNMP)

notifications.

  stp             Sends Spanning Tree Protocol (STP) notifications.
  temperature     Sends Temperature notifications.

  vrrp            Sends Virtual Router Redundancy Protocol (VRRP)

notifications.

  vsf             Sends Virtual Switching Framework (VSF) notifications.

  vsx             Sends Virtual System Extension (VSX) notifications.

Command History

Release

Modification

10.07 or earlier

‐‐

Public

snmp-server host 115

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

snmp-server vrf

Syntax

snmp-server vrf <VRF-NAME>

no snmp-server vrf <VRF-NAME>

Description

Configures a VRF on which the SNMP agent listens for incoming requests. By default, the SNMP agent does
not listen on any VRF. 4100i, 6000, and 6100 only support default VRF. The SNMP agent can listen on
multiple VRFs.

The no form of this command stops the SNMP agent from listening for incoming requests on the specified
VRF.

Parameter

Description

Specifies the name of a VRF.

<VRF‐NAME>

Examples

Configuring the SNMP agent to listen on VRF default.

switch(config)# snmp-server vrf default

Configuring the SNMP agent to listen on VRF mgmt.

Stopping the SNMP agent from listening on VRF default.

switch(config)# no snmp-server vrf default

Public

snmp-server vrf 116

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

snmpv3 context

Syntax

snmpv3 context <NAME> vrf <VRF-NAME> [community <STRING>]

no snmpv3 context <NAME> [vrf <VRF-NAME>] [community <STRING>]

Description

Creates an SNMPv3 context on the specified VRF.

The no form of this command removes the specified SNMP context.

Parameter

Description

<NAME>

Specifies the name of the context. Range: 1 to 32 printable ASC
II characters, excluding space and question mark (?).

vrf <VRF‐NAME>

Specifies the VRF associated with the context. Default: default.

community <STRING>

Specifies the SNMP community string associated with the con
text. Range: 1 to 32 printable ASCII characters, excluding space
and question mark. Default: public.

Public

snmpv3 context 117

Examples

Creating an SNMPv3 context named newContext:

switch(config)# snmpv3 context newContext

Creating an SNMPv3 context named newContext on VRF myVrf and with community string private.

switch(config)# snmpv3 context newContext vrf myVrf community private

Removing the SNMPv3 context named newContext on VRF myVrf:

switch(config)# no snmpv3 context newContext vrf myVrf

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

snmpv3 user

Syntax

snmpv3 user <NAME>

      [auth <AUTH-PROTO> auth-pass [{plaintext | ciphertext} <AUTH-PASS>]]

      [priv <PRIV-PROTO> priv-pass [{plaintext | ciphertext} <PRIV-PASS>]]

      [access-level ro|rw]

no snmpv3 user <NAME>

        [auth <AUTH-PROTO> auth-pass [{plaintext | ciphertext} <AUTH-PASS>]]
        [priv <PRIV-PROTO> priv-pass [{plaintext | ciphertext} <PRIV-PASS>]]

[access-level ro|rw]

Public

snmpv3 user 118

Description

Creates an SNMPv3 user and adds it to an SNMPv3 context. The SNMPv3 security level (set with command
snmpv3 security-level) determines which users are allowed to authenticate.

The no form of this command removes the specified SNMPv3 user.

NOTE

When updating the authentication protocols and privacy protocols for the
existing SNMPv3 users, you must also update the access level. Otherwise, the
access level will be set to read-only.

Parameter

Description

<NAME>

access‐level

auth <AUTH‐PROTO>

auth‐pass [{plaintext |
ciphertext} <AUTH‐PASS>]

Specifies the SNMPv3 username. Range 1 to 32 printable ASCII
characters, excluding space and question mark (?).

Configures the access level for the SNMPv3 user:

•  ro: Allow read‐only access for the SNMPv3 user
•  rw: Allow read‐write access for the SNMPv3 user

Sets the authentication protocol used to validate user logins. Su
pported protocols are md5, sha, sha224, sha256, sha384, and
sha512.

Specifies the SNMPv3 user authentication password. Range for
plaintext is 8 to 32 printable ASCII characters, excluding space
and question mark (?). Range for ciphertext is 1 to 256 printab
le ASCII characters. Ciphertext is used when copying user confi
guration settings between switches.

NOTE

Authentication passwords that include special c
haracters must be enclosed in single quotation
marks ('). For example, 'auth‐pwd20246!@#'.

priv <PRIV‐PROTO>

Sets the SNMPv3 privacy protocol (encryption method). Suppor
ted privacy protocols are aes, aes192, aes256, and des.

priv‐pass [{plaintext |
ciphertext} <PRIV‐PASS>]

Specifies the SNMPv3 user privacy encryption password. Range
for plaintext is 8 to 32 printable ASCII characters, excluding sp
ace and question mark (?). Range for ciphertext is 1 to 256 pri

Public

snmpv3 user 119

Parameter

Description

ntable ASCII characters. Ciphertext is used when copying user c
onfiguration settings between switches.

NOTE

Authentication passwords that include special c
haracters must be enclosed in single quotation
marks ('). For example, 'priv‐pwd20246!@#'.

NOTE

When the authentication password is not provided on the command line,
plaintext authentication password prompting occurs upon pressing Enter,
followed by privacy encryption protocol prompting, and finally plaintext
encryption password prompting. The entered password characters are masked
with asterisks.

NOTE

When the authentication type and password plus the privacy protocol
(encryption method) are provided on the command line but the encryption
password is not provided, plaintext encryption password prompting occurs upon
pressing Enter. The entered password characters are masked with asterisks.

Examples

Defining SNMPv3 user Admin1 using sha authentication and des privacy encryption with provided plaintext
passwords:

switch(config)# snmpv3 user Admin1 auth sha auth-pass plaintext F82#450h

                priv des priv-pass plaintext F82#4eva

Defining SNMPv3 user Admin2 using MD5 authentication and AES privacy encryption with provided
authentication password and privacy encryption type but prompted encryption password:

switch(config)# snmpv3 user Admin2 auth md5 auth-pass plaintext F82#450h

                            priv aes priv-pass

Enter the privacy encryption key: ********

Re-Enter the privacy encryption key: ********

Defining SNMPv3 user Admin2 using MD5 authentication and AES privacy encryption with plaintext
password prompting and privacy encryption selection:

Public

snmpv3 user 120

switch(config)# snmpv3 user Admin2 auth md5 auth-pass

Enter the authentication password: ********

Re-Enter the authentication password: ********

Configure the privacy protocol (y/n)? y

Enter the privacy protocol (aes/des)? aes

Enter the privacy encryption key: ********

Re-Enter the privacy encryption key: ********

Removing SNMPv3 user Admin1:

switch(config)# no snmpv3 user Admin1

Creating an SNMP user on switch 1 and then creating the same user on switch 2 by copying from the switch
1 configuration:

On switch 1, configure a user named Admin3, and then use the show running-config command to display
switch configuration. Save a copy of the full snmpv3 user command (shown by show running-config). This
saved command is used on switch 2.

switch1(config)# snmpv3 user Admin3 auth sha auth-pass plaintext F82#450h

                 priv des priv-pass plaintext F82#4eva

switch1(config)# exit

switch1# show running-config

Current configuration:

!

!Version AOS-CX xx.xx.xx.xxxxxx

!

snmpv3 user Admin3 auth sha auth-pass ciphertext AQBaf2d...FJVcZ3o=

priv des priv-pass ciphertext AQBaH2p...2jfTFwQ=

ssh server vrf mgmt

!

interface mgmt

no shutdown

ip dhcp
vlan 1
On switch 2, execute the snmpv3 user command that you saved from switch 1 (as shown by show
running-config). This creates the user on switch 2 with the same configuration.

switch2(config)# snmpv3 user Admin3 auth sha auth-pass ciphertext

AQBaf2d...FJVcZ3o=

                 priv des priv-pass ciphertext AQBaH2p...2jfTFwQ=

The following command sets a read-write access level for an SNMPv3 user with the user name user1.

switch(config)# snmpv3 user user1 auth md5 auth-pass plaintext abc1234

access-level rw

Public

snmpv3 user 121

Command History

Release

10.13

Modification

Following authentication protocols are supported: sha224, sha256, sha384, an
d sha512.

Following privacy protocols are supported: aes192 and aes256.

10.09

The access‐level parameter was introduced.

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

Subtopics

snmpv3 user view

snmpv3 user view

Syntax

snmpv3 user <USER-NAME> view <VIEW-NAME>

no snmpv3 user <USER-NAME> view <VIEW-NAME>

Description

Associates a user with an existing SNMP MIB view.

The no form of this command removes the associated user from the specified SNMP MIB view.

Parameter

Description

Specifies the user name for the SNMP MIB view. Accepts a maxi
mum of 32 characters.

Public

snmpv3 user view 122

Description

Specifies the view name for the SNMP MIB view. Accepts a maxi
mum of 32 characters.

Parameter

<USER‐NAME>

<VIEWNAME>

Examples

Adding a user in the existing SNMP MIB view:

switch(config)# snmpv3 user nw-admin view my-nw-view

Removing the user from the SNMP MIB view:

switch(config)# no snmpv3 user nw-admin view my-nw-view

Attaching unconfigured or unknown SNMP view to an SNMPv3 user:

switch(config)# snmpv3 user nw-admin view myView

View myView is not configured.

Command History

Release

10.10

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

Subtopics

Accessing HPE Aruba Networking Support

Public

Support and Other Resources 123

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

Accessing HPE Aruba Networking Support 124

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

Accessing Updates 125

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

Regulatory Information 126