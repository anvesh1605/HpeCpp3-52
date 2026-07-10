AOS-CX 10.17.xxxx Monitoring Guide For 4100i, 6000, 6100 Switch
Series

Published: February 2026

AOS-CX 10.17.xxxx Monitoring Guide For 4100i, 6000, 6100 Switch
Series

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

AOS-CX 10.17.xxxx Monitoring Guide For 4100i, 6000...

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

F
o
r

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
.
.
.

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX 10.17.xxxx Monitoring Guide For 4100i, 6000...

Table of contents

About this document..................................................................................................................................................................................8

Applicable products........................................................................................................................................................................8

Latest version available online.................................................................................................................................................8

Command syntax notation conventions.............................................................................................................................8

About the examples.................................................................................................................................................................... 10

Identifying switch ports and interfaces........................................................................................................................... 10

Monitoring hardware through visual observation..................................................................................................................11

Confirming normal operation of the switch by reading LEDs.............................................................................11

Detecting if the switch is not ready for a failover event........................................................................................ 13

Finding faulted components using the switch LEDs................................................................................................14

IP Flow Information Export..................................................................................................................................................................15

Flow monitors..................................................................................................................................................................................17

Flow Records................................................................................................................................................................................... 18

Flow Exporters................................................................................................................................................................................18

Destinations..................................................................................................................................................................................... 19

Configuring IP Flow Information Export on 4100i, 6000, and 6100 Switches........................................ 19

Flow monitoring commands................................................................................................................................................... 23

exporter ................................................................................................................................................................................23

flow exporter ..................................................................................................................................................................... 24

flow monitor .......................................................................................................................................................................27

flow record ..........................................................................................................................................................................29

ip|ipv6 flow monitor (interface) ..............................................................................................................................32

show flow exporter ........................................................................................................................................................ 33

show flow monitor ..........................................................................................................................................................36

show flow record ............................................................................................................................................................. 39

show ipfix flow-table-utilization..............................................................................................................................42

Alarms.............................................................................................................................................................................................................. 43

Alarm commands.......................................................................................................................................................................... 43

alarm .......................................................................................................................................................................................44

alarm input ..........................................................................................................................................................................47

alarm snooze ..................................................................................................................................................................... 49

show alarm ..........................................................................................................................................................................50

Boot commands..........................................................................................................................................................................................52

Boot commands.............................................................................................................................................................................52

Public

Table of contents 4

boot set-default ...............................................................................................................................................................53

boot system ........................................................................................................................................................................54

show boot-history .......................................................................................................................................................... 56

L1-100Mbps downshift......................................................................................................................................................................... 61

Limitations with speed downshift....................................................................................................................................... 61

L1-100Mbps downshift commands...................................................................................................................................61

downshift enable .............................................................................................................................................................62

show interface .................................................................................................................................................................. 63

show interface downshift-enable .......................................................................................................................... 75

show running-config interface ................................................................................................................................76

Mirroring......................................................................................................................................................................................................... 78

Mirror statistics.............................................................................................................................................................................. 80

Classifier policies and mirroring sessions....................................................................................................................... 80

Mirroring commands...................................................................................................................................................................81

clear mirror ......................................................................................................................................................................... 81

comment .............................................................................................................................................................................. 83

destination interface .....................................................................................................................................................84

destination tunnel .......................................................................................................................................................... 86

diagnostic ............................................................................................................................................................................88

disable ................................................................................................................................................................................... 89

enable .................................................................................................................................................................................... 90

mirror endpoint ................................................................................................................................................................91

mirror session ....................................................................................................................................................................93

show mirror ........................................................................................................................................................................ 95

show mirror endpoint ...................................................................................................................................................98

source interface ............................................................................................................................................................... 99

Monitoring a device using SNMP.................................................................................................................................................. 102

Packet Capture.........................................................................................................................................................................................102

Power-over-Ethernet............................................................................................................................................................................103

PoE commands............................................................................................................................................................................104

lldp dot3 poe .................................................................................................................................................................. 105

lldp med poe ...................................................................................................................................................................106

power-over-ethernet ................................................................................................................................................. 107

power-over-ethernet allocate-by .......................................................................................................................108

power-over-ethernet always-on ......................................................................................................................... 110

power-over-ethernet assigned-class ............................................................................................................... 111

power-over-ethernet pre-std-detect ............................................................................................................... 112

power-over-ethernet priority ............................................................................................................................... 113

Public

Table of contents 5

power-over-ethernet quick-poe ..........................................................................................................................114

power-over-ethernet threshold ...........................................................................................................................116

power-over-ethernet trap .......................................................................................................................................117

show lldp local ............................................................................................................................................................... 118

show lldp neighbor ..................................................................................................................................................... 119

show power-over-ethernet .................................................................................................................................... 120

Aruba AirWave......................................................................................................................................................................................... 123

SNMP support and AirWave................................................................................................................................................123

Supported features with AirWave and the AOS-CX switch...............................................................................124

Configuring the AOS-CX switch to be monitored by AirWave........................................................................ 125

AirWave commands..................................................................................................................................................................126

Remote syslog commands.......................................................................................................................................126

clear accounting-logs ................................................................................................................................... 126

diag persistent-storage ...............................................................................................................................128

logging .................................................................................................................................................................. 130

logging accounting-format-native ........................................................................................................133

logging filter .......................................................................................................................................................134

logging facility .................................................................................................................................................. 138

logging persistent-storage ........................................................................................................................139

SNMP commands..........................................................................................................................................................141

event-trap-enable ...........................................................................................................................................142

lldp trap enable ................................................................................................................................................ 143

mac-notify traps .............................................................................................................................................. 146

rmon alarm {enable | disable} {index | all} ....................................................................................... 149

rmon alarm ..........................................................................................................................................................150

show configuration-changes trap ......................................................................................................... 152

show mac-notify port ................................................................................................................................... 153

show mac-notify .............................................................................................................................................. 154

show rmon alarm .............................................................................................................................................155

show snmp agent-port ................................................................................................................................ 157

show snmp community ................................................................................................................................158

show snmpv3 context .................................................................................................................................. 159

show snmpv3 engine-id ..............................................................................................................................160

show snmpv3 security-level ..................................................................................................................... 161

show snmp system .........................................................................................................................................162

show snmp trap ............................................................................................................................................... 163

show snmpv3 users .......................................................................................................................................164

show snmp views ............................................................................................................................................ 165

Public

Table of contents 6

show snmp vrf .................................................................................................................................................. 166

snmpv3 context ...............................................................................................................................................167

snmpv3 engine-id ...........................................................................................................................................168

snmpv3 security-level ..................................................................................................................................170

snmp-server agent-port ............................................................................................................................. 171

snmp-server community view ................................................................................................................. 172

snmp-server community .............................................................................................................................173

snmp-server historical-counters-monitor ........................................................................................ 176

snmp-server host ............................................................................................................................................177

snmp-server system-contact ................................................................................................................... 183

snmp-server system-description ...........................................................................................................184

snmp-server system-location .................................................................................................................. 185

snmp-server trap-source interface vrf ............................................................................................... 186

snmp-server vrf ............................................................................................................................................... 188

snmpv3 user view ...........................................................................................................................................189

snmpv3 user ...................................................................................................................................................... 190

snmp-server response-source .................................................................................................................194

snmp-server snmpv3-only ........................................................................................................................ 196

snmp-server trap ............................................................................................................................................ 197

snmp-server trap aaa-server-reachability-status ........................................................................199

snmp-server trap configuration-changes .........................................................................................200

snmp-server trap mac-notify ...................................................................................................................201

snmp-server trap port-security ..............................................................................................................202

snmp-server trap snmp ...............................................................................................................................203

snmp-server trap vsx ....................................................................................................................................204

snmp-server view ........................................................................................................................................... 206

Support and Other Resources.........................................................................................................................................................207

Accessing HPE Aruba Networking Support...............................................................................................................208

Accessing Updates....................................................................................................................................................................209

Warranty Information.............................................................................................................................................................. 209

Regulatory Information.......................................................................................................................................................... 210

Documentation Feedback.....................................................................................................................................................210

See Also........................................................................................................................................................................................................210

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

About this document 8

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

Command syntax notation conventions 9

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

About the examples 10

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

Monitoring hardware through visual observation 11

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

Detecting if the switch is not ready for a failove... 12

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

Detecting if the switch is not ready for a failove... 13

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

Finding faulted components using the switch LEDs 14

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

IP Flow Information Export 15

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

IP Flow Information Export 16

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
Flow monitoring commands

Flow monitors

A flow monitor is applied to an interface to perform network traffic monitoring. A flow monitor consists of
a flow record, a flow cache, and optional flow exporters. A flow record must be created and assigned to the
flow monitor for the monitoring process to function. Flow data is compiled from the network traffic on the
interface and stored in the flow cache based on the match (key) and collect (non-key) fields in the flow
record. Data from the flow cache is exported by the flow exporters assigned to the flow monitor. 4100i,

Public

Flow monitors 17

6000, and 6100 switch series support a maximum of sixteen flow exporters that can be applied to a single
flow monitor.

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

Public

Flow Records 18

A flow exporter defines where and how to export flow reports. Flow exporters are created as standalone
entities in the config context to provide flow monitors the ability to export flow reports. 4100i, 6000,
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

Public

Destinations 19

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

•  Step four: Apply a flow monitors to interface(s)

NOTE

IPv6 related commands are only applicable to switches that support IPv6
protocol.

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

Public

Configuring IP Flow Information Export on 4100i, 6... 20

----------------------------------------------------------------------------

----

Flow exporter 'flowExternal

----------------------------------------------------------------------------

----

Status                  : Accepted

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

Public

Configuring IP Flow Information Export on 4100i, 6... 21

!

monitor topN type topN-flows entries 5

monitor appFlow type application-flows

Step three: Configure the monitor(s)

First, configure an IPv4 flow monitor.

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

Public

Configuring IP Flow Information Export on 4100i, 6... 22

Flow monitoring commands

Subtopics

exporter
flow exporter
flow monitor
flow record
ip|ipv6 flow monitor (interface)
show flow exporter
show flow monitor
show flow record
show ipfix flow-table-utilization

exporter

Syntax

exporter <EXPORTER-NAME>

no exporter <EXPORTER-NAME>

Description

Assigns a flow exporter to flow monitor in the config-flow-monitor context.

The no form of this command removes the flow exporter from the selected monitor.

Parameter

Description

<EXPORTER‐NAME>

Specifies the name of the flow exporter assigned to the monitor.

NOTE
A maximum of sixteen flow exporters can be applied to each flow monitor.

Examples

Assigning flow exporter, flow-exporter-1, to flow monitor, flow-monitor-1:

switch(config)# flow monitor flow-monitor-1

switch(config-flow-monitor)# exporter flow-exporter-1

Removing a flow exporter assigned to flow monitor, flow-monitor-1:

Public

Flow monitoring commands 23

switch(config)# flow monitor flow-monitor-1

switch(config-flow-monitor)# no exporter flow-exporter-1

Attempting to assign non-existent flow exporter, flow-exporter-5, to flow monitor, flow-monitor-1:

switch(config)# flow monitor flow-monitor-1

switch(config-flow-monitor)# exporter flow-exporter-5

Flow exporter 'flow-exporter-5' does not exist.

switch(config-flow-monitor)#
Attempting to assign flow exporter, flow-exporter-6, to monitor, flow-monitor-3, when two exporters are
assigned:

switch(config)# flow monitor flow-monitor-3

switch(config-flow-monitor)# exporter flow-exporter 4

switch(config-flow-monitor)# exporter flow-exporter 5

switch(config-flow-monitor)# exporter flow-exporter 6

switch(config-flow-monitor)#

Command History

Release

Modification

10.17.1000

Command introduced

10.16

Command introduced

Command Information

Platforms

Command context

Authority

4100i

6000

6100

config‐flow‐
monitor

Administrators or local user group members with execution righ
ts for this command.

flow exporter

Syntax

flow exporter <name>

Public

flow exporter 24

description <description>

   destination

traffic-insight}

traffic-insight <instance-name>

   no ...

   transport udp <port>

Description

A flow exporter is the part of the IP Flow Information Export (IPFIX) feature that defines how a flow monitor
exports flow reports. You can assign the same flow exporter configuration to more than one flow monitor.
Each flow exporter includes a destination setting that identifies the device to which the flow reports are sent

Parameter

<name>

Description

Name of the flow exporter, up to 64 characters.

export‐protocol ipfix

Define an export protocol for the flow exporter. The default ipfi
x protocol is the only protocol currently available.

description <description>

A description of the flow exporter, up to 256 characters and spa
ces.

destination

   <hostname>

   <ip6addr>

vrf <vrfname>

Configure the export destination

The exporter sends flow records to the specified hostname dest
ination. The hostname can be a string of up to 64 characters.

The exporter sends flow records to this IPv6 address destinatio
n.

You can optionally include the name of the destination VRF in t
he destination definition on 5420, 6200, 6300, 6400, 8100, 83
60, 9300S Switch series.

type

Configure the type of the destination.

   hostname‐or‐ip‐addr

Define the destination type as a hostname or IP address.

   traffic‐insight <name>

Define the destination type as a traffic insight instance.

no ...

Negate any configured parameter.

traffic‐insight <INSTANCE‐
NAME>

Specify the a Traffic Insight instance to be used as the destinati
on.

template data timeout

<timeout>

A flow exporter template describes the format of exported flow
reports. Therefore, flow reports cannot be decoded properly wi
thout the corresponding templates. This setting defines how o

Public

flow exporter 25

Parameter

Description

ften the flow exporter will resend templates to the flow monitor.
The supported range is 1‐86400 seconds, and the default is 6
00 seconds.

transport udp <port>

Transport protocol and port for sending flow record reports. Th
e default port is port 4739.

Usage

The following table shows the maximum supported of flow monitors and flow exporters for each switch
model.

Examples

The following example creates a flow exporter configuration named exporter-1:

switch(config)# flow exporter exporter-1

switch(config-flow-exporter)# destination type traffic-insight

switch(config-flow-exporter)# destination traffic-insight-instance-1

The following example attempts to create more than the maximum number of allowed flow exporters:

switch(config)# flow exporter exporter-1

switch(config)# flow exporter exporter-2

<--OUTPUT OMITTED FOR BREVITY-->

switch(config)# flow exporter exporter-16

switch(config)# flow exporter exporter-17

Unable to add another flow exporter; the limit is 16.
The following example configures the destination type:

switch(config)# destination type {hostname-or-ip-addr | traffic-insight}

switch(config)# destination {<HOSTNAME> | <IPV4-ADDR> | <IPV6-ADDR>}
switch(config)# destination traffic-insight <INSTANCE-NAME>

Command History

Release

Modification

10.17.1000

Command introduced on 4100i, 6000, and 6100 Switch series.

Public

flow exporter 26

Command Information

Platforms

Command context

Authority

4100i

6000

6100

config
config‐flow‐
exporter

Administrators or local user group members with execution righ
ts for this command.

flow monitor

Syntax

flow monitor <name>

    exporter <name>
cache timeout {inactive <timeout}|{active <timeout}

    description <description>

    record <name>

Description

On HPE Aruba Networking 4100i, 6000, and 6100 Switch series, a flow monitor is the part of the IP
Flow Information Export (IPFIX) feature that performs network monitoring for the selected interface. A flow
monitor configuration consists of a flow record, a flow cache, and one or more associated flow exporters.
A flow monitor compiles data from the network traffic on the interface and stores it in the flow cache in a
format defined by the flow record. The flow exporters associated with the monitor then export data from the
flow cache to the flow exporter destination.

NOTE

HPE Aruba Networking 4100i, 6000, and 6100 Switch series support a maximum
of sixteen flow exporters that can be applied to a single flow monitor. If no
software augmentation of flows is required, there is no need to configure a flow
collector or flow monitor.

Parameter

<name>

Description

Name of the flow monitor, up to 64 characters.

 cache timeout active

 <timeout>

Use the cache timeout parameter to define an active or inactive
timeout for the flow monitor. A flow monitor closes a flow sessio
n that is active for longer than the active timeout or inactive for
longer than the inactive timeout.

Public

flow monitor 27

Parameter

 cache timeout

inactive <timeout>

Description
The active timeout range is 120‐604800. The default active t
ime out value is 1800 and inactive timeout value is 120.

Use the cache timeout parameter to define an inactive timeout
for the flow monitor. A flow monitor closes a flow session that is
active for longer than the active timeout or inactive for longer t
han the inactive timeout.

For 4100i, 6000, and 6100 Switch Series, the minimum suppor
ted inactive timeout range is 120 seconds. The maximum inacti
ve timeout range is 604800 seconds, and the default inactive ti
meout is 120 seconds.

description

A description up to 256 characters long, including spaces.

exporter <name>

Assign a flow exporter to a flow monitor.

record <name>

Examples

(For HPE Aruba Networking 5420, 6200, 6300, 6400, 8100, 8
325, 8325P, 8325H, 8360, 9300, 9300S, 10040 Switch series)
Assigns a flow record to a flow monitor.

The following example creates a flow monitor configuration named monitor-1.

switch(config)# flow monitor monitor-1

switch(config-flow-monitor)# description Monitor for analyzing basic ipv4

traffic

switch(config-flow-monitor)# exporter flow-exporter-1

switch(config-flow-monitor)# record flow-record-1

switch(config-flow-monitor)# cache timeout inactive 120

switch(config-flow-monitor)# cache timeout active 1500
The following example assigns collector-1 as the collector associated with this monitor.

switch(config)# flow monitor monitor-1

switch(config-flow-monitor)# collector collector-1
The following workflow changes the flow record assigned to a flow monitor.

switch(config)# flow monitor flow-monitor-1

switch(config-flow-monitor)# record flow-record-2
Create more than the maximum number of allowed flow monitors

switch(config)# flow monitor monitor-1
switch(config)# flow monitor monitor-2

<--OUTPUT OMITTED FOR BREVITY-->

switch(config)# flow monitor monitor-16

Public

flow monitor 28

switch(config)# flow monitor monitor-17

No more than 16 flow monitors can be configured. Another flow monitor

must be removed first.
Add or modify the description of flow exporter flow-exporter-1

switch(config)# flow exporter flow-exporter-1

switch(config-flow-exporter)# description Exports flows to 10.2.3.45:2055

switch(config-flow-exporter)# description Exports flows to Traffic Insight

Command History

Release

Modification

10.17.1000

Command introduced on the 4100i, 6000, and 6100 switch series.

Command Information

Platforms

Command context

Authority

4100i

6000

6100

config
config‐flow‐
monitor

Administrators or local user group members with execution righ
ts for this command.

flow record

Syntax

flow record <record-name>
   match
ip {source|destination} address

ip protocol|version

ipv6 {source|destination} address

ipv6 protocol|version

transport {source | destination} port

   collect
counter {packets|bytes}
timestamp absolute last

   descriptioN <description>

Public

flow record 29

Description

Creates or modifies a flow record and switches to the config-flow-record context for the flow record. Define
data to be included in a flow record by configuring flow record match and collect fields.

A flow record defines match (key) fields and collection (non-key) fields. Customers configure flow records
with match (key) fields and collect (non-key) fields. Match fields are the set of fields that define a flow, such
as IP address or UDP port. Collect fields are the set of fields that identify information to collect for a flow,
such as packet and byte counters.

Traffic with matching attributes (for example, traffic coming from the same interface, sent to the same
destination with the same protocol) are classified as a single flow. Information for some or all of the matched
settings can be collected and exported to a destination defined by the flow exporter assigned to the flow
monitor.

NOTE

Traffic must match a match rule definition before it can be collected and sent. You
cannot collect and send data that is not matched.

NOTE

For 4100i, 6000, and 6100 Switch series, a maximum of sixteen flow records can
be created.

Parameter

<record‐name>

match

description

Description

Name of the flow monitor, up to 64 characters.

match traffic according to one or more of the following key attri
butes:

ip source: Match traffic from the same IPv4 source.
•
ip destination: Match traffic to the same IPv4 destination.
•
ip protocol: Match traffic using the same IP version
•
ip version: Match traffic using the same IP protocol
•
ipv6 source: Match traffic from an IPv6 source.
•
•
ipv6 destination: Match traffic to an IPv6 destination.
ipv6 protocol: Match traffic using the same IPv6 version
•
ipv6 version: Match traffic using the same IPv6 protocol
•
•  transport {source | destination} port: Match traffic by sou

rce or destination transport port

A description for the flow record up to 256 characters long, incl
uding spaces.

collect

Configures data fields to be included a flow record.

Public

flow record 30

Parameter

Description

•  counter bytes: Collect counter data for bytes in the flow.
•  counter packets: Collect counter data for packets in the flo

w.

•  timestamp absolute first: Collect absolute timestamp of th

e first packet observed.

•  timestamp absolute last: Collect absolute timestamp of th

e last packet observed.

Examples

Adding counter and timestamp collect fields to flow-record-1:

switch(config)# flow record flow-record-1

Creating more than the maximum number of allowed flow records:

switch(config)# flow record record-1

switch(config)# flow record record-1

switch(config)# flow record record-2

<--OUTPUT OMITTED FOR BREVITY-->

switch(config)# flow record record-16

switch(config)# flow record record-17

Unable to add another flow record; the limit is 16.
Adding IPv4 match fields to flow record flow-record-1 using the ip keyword:

switch(config)# flow record flow-record-1

switch(config-flow-record)# match ip source address

switch(config-flow-record)# match ip destination address

switch(config-flow-record)# match ip protocol
Adding IPv6 match fields to flow record flow-record-2:

switch(config)# flow record flow-record-2

switch(config-flow-record)# match ipv6 source address

switch(config-flow-record)# match ipv6 destination address

switch(config-flow-record)# match ipv6 protocol

switch(config-flow-record)# match ipv6 version
Removing the IPv4 destination address match field from flow record flow-record-1 using the ip keyword:

switch(config)# flow record flow-record-1

switch(config-flow-record)# no match ip destination address
Removing the IPv4 destination address match field from flow record flow-record-1 using the ipv4 keyword:

switch(config)# flow record flow-record-1

switch(config-flow-record)# no match ipv4 destination address
Removing the transport destination port match field from flow record flow-record-1:

Public

flow record 31

switch(config)# flow record flow-record-1

switch(config-flow-record)# no match transport destination port

Command History

Release

Modification

10.17.1000

Command introduced on 4100i, 6000, and 6100 Switch series.

10.13

Added application https url and dns response‐code parameters.

Command Information

Platforms

Command context

Authority

4100i

6000

6100

config
config‐flow‐
record

Administrators or local user group members with execution righ
ts for this command.

ip|ipv6 flow monitor (interface)

Syntax

[no] ip|ipv6 flow monitor (interface)

Description

Enable flow monitoring on inbound and outbound interfaces by assigning a flow monitor to that interface.
Only physical interfaces and LAG interfaces can be monitored. A flow monitor cannot be applied to an
interface that is part of a LAG. If an unsupported application is attempted, an error message will be
displayed. If the flow monitor is associated with a flow record that contains application fields as collect fields,
then Application Recognition should be enabled on the same interface.

The [no] form of command disables the flow monitoring.

NOTE
The 4100i, 6000, and 6100 Switch Series support ingress-only interfaces;
therefore, flow monitoring on these platforms is limited to inbound traffic.

Public

ip|ipv6 flow monitor (interface) 32

Examples

Associate a flow monitor configuration named flow-monitor-3 for IPv6 traffic on a physical interface.

switch(config)# interface 1/1/1

switch(config-if)# ip flow monitor flow-monitor-3 in
Enable an IPv6 flow monitor on a physical interface

switch(config)# interface lag 1

switch(config-if)# ipv6 flow monitor flow-monitor-1 in

Command History

Release

Modification

10.17.1000

Command introduced on 4100i, 6000, and 6100 Switch series.

Command Information

Platforms

Command context

Authority

4100i

6000

6100

config
config‐flow‐
monitor

Administrators or local user group members with execution righ
ts for this command.

show flow exporter

Syntax

show flow exporter [<name>]

[statistics]

Description

Displays flow exporter statistics, configuration and status. When no exporter name is specified, the output of
this command displays information for all flow exporters.

The output of this command can indicate the following status types:

•  Rejected (Destination type is hostname or IP address, but no destination is specified)

Public

show flow exporter 33

•  Rejected (Destination type is hostname or IP address, but the specified hostname or IP address is

invalid)

•  Rejected (Destination type is Traffic Insight, but no destination is specified)

•  Rejected (Destination type is Traffic Insight, but the specified Traffic Insight instance does not exist)

•  Rejected (Destination type is Traffic Insight, but the specified Traffic Insight instance is not enabled)

•  Rejected (Destination type is Traffic Insight, but the specified Traffic Insight instance source is not IPFIX)

•  Rejected (Internal error: destination type is Traffic Insight, but the specified Traffic Insight instance is

invalid)

Parameter

<name>

statistics

Examples

Description

Name of the flow exporter.

Adds statistical information about the flow exporter to the outp
ut.

Display the configuration of a flow exporter named exporter-1.

switch# show flow exporter exporter-1

----------------------------------------------------------------------------

----

Flow exporter 'exporter-1'

----------------------------------------------------------------------------

----

Description             : Exports to the first collector

Status                  : Accepted

Export Protocol         : ipfix
Destination Type        : Hostname or IP address

Destination             : 192.168.0.1

Transport Configuration

    Protocol            : UDP

    Port                : 9995
Display statistics information for all flow exporters

switch# show flow exporter statistics
----------------------------------------------------------------------------
----

Flow exporter 'exporter-1'

----------------------------------------------------------------------------

Public

show flow exporter 34

----

Reports sent            : 14961

----------------------------------------------------------------------------

----

Flow exporter 'exporter-2'

----------------------------------------------------------------------------

----

Reports sent            : 5
Display information with no flow exporters configured

switch# show flow exporter

No flow exporters configured.
Display a flow exporter information with TI as a destination

switch# show flow exporter exporter-5

----------------------------------------------------------------------------

----

Exporter Name           : exporter-5

----------------------------------------------------------------------------

----

Description             : Exporter configured with TI as the destination

Status                  : Rejected (Destination type is Traffic Insight,

but the specified Traffic Insight instance does not exist)

Export Protocol         : ipfix

Destination Type        : Traffic Insight

Destination             : instance-1

Transport Configuration

Protocol            : UDP

Port                : 2055
Display information for a flow exporter that has multiple destinations of different types configured and
hostname-or-ip-addr is specified as the destination type to use.

switch# show flow exporter exporter-6

----------------------------------------------------------------------------

----

Flow exporter 'exporter-6'

----------------------------------------------------------------------------

----

Description             : TI and hostname configured, but type is hostname-

or-ip-addr

Status                  : Accepted

Export Protocol         : ipfix

Destination Type        : Hostname or IP address

Destination             : collector-1

Destination VRF         : mgmt

Public

show flow exporter 35

Transport Configuration

Protocol            : UDP

Port                : 4821

Command History

Release

Modification

10.17.1000

Command introduced on 4100i, 6000, and 6100 Switch series

Command Information

Platforms

Command context

Authority

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

4100I

6000

6100

show flow monitor

Syntax

show flow monitor

[statistics | information-elements]

show flow monitor <MONITOR-NAME>

[statistics]

Description

Displays flow monitor configuration and status. When no monitor name is specified, the output of this
command displays information for all flow monitors.

Parameter

<name>

Description

Name of the flow monitor.

Public

show flow monitor 36

Parameter

statistics

Description

Includes the statistics parameter to display additional flow and
cache statistics.

information-elements

Displays the configured information elements for the flow moni
tor.

Usage

The output of this command can indicate the following status types:

•  Possible status types for all switches

◦  Accepted

◦  Rejected (Internal error: monitor does not exist)

◦  Rejected (The state of one or more of the assigned flow exporters is rejected)

The possible statistics for a flow monitor are:

Examples

Display information for flow monitor monitor-1 on 4100i, 6000, and 6100 Switch series:

switch# show flow monitor 'monitor-1

----------------------------------------------------------------------------

----

Flow monitor 'monitor-1'

----------------------------------------------------------------------------

----

Description             : Used for IPv4 traffic analysis

Status                  : Accepted
Flow Record             : record-1

Flow Exporter(s)        : exporter-1, exporter-2

Cache Configuration

Inactive Timeout    : 1800

Active Timeout      : 300

----------------------------------------------------------------------------

----
Display information for flow monitor monitor-2 on 4100i, 6000, and 6100 Switch series:

switch# show flow monitor 'monitor-2

----------------------------------------------------------------------------

----

Flow monitor 'monitor-2'

Public

show flow monitor 37

----------------------------------------------------------------------------

----

Description             : Used for IPv6 traffic analysis

Status                  : Rejected (The state of one or more of the

specified flow exporters is rejected)

Flow Record             : record-2

Flow Exporter(s)        : exporter-1

Cache Configuration

Inactive Timeout    : 1800

Active Timeout      : 2400

----------------------------------------------------------------------------

----
Display information and statistics for a flow monitor on 4100i, 6000, and 6100 Switch series:

show flow monitor statistics

----------------------------------------------------------------------------

----

Flow monitor 'monitor-1'

----------------------------------------------------------------------------

----

Current Entries          : 2

Flows Added              : 6

Total Flows Terminated   : 4

  Flows Aged             : 2

    Active Timeout       : 1

    Inactive Timeout     : 1

  End of Flow Detected   : 2

  Forced End             : 0

  Flows Aged             : 4

Command History

Release

Modification

10.17.1000

Command introduced on 4100i, 6000, and 6100 Switch series.

Command Information

Platforms

Command context

Authority

4100i

6000

config
config‐flow‐
monitor

Administrators or local user group members with execution righ
ts for this command.

Public

show flow monitor 38

Platforms

Command context

Authority

6100

show flow record

Syntax

show flow record [<name>]

Description

Display flow record configuration and status. When no record name is specified, the output of this command
displays information for all flow records.

The output of this command can indicate the following status types:

•  Accepted

•  Rejected (Internal error: failed to process record)

•  Rejected (Mix of IPv4 and IPv6 match fields is not allowed. Specify match fields of the same IP version

(IPv4 or IPv6))

•  Rejected (Incomplete match fields. The mandatory match fields are: version, source address, destination

address protocol, transport destination port, and transport source port)

Parameter

<name>

Examples

Description

Name of the flow record.

NOTE
IPv6 related commands are only applicable to switches that support IPv6
protocol.

Display the configuration of a flow record named flow-record-1.

switch# show flow record record-1

----------------------------------------------------------------------------

----

Flow record  'record-1'

Public

show flow record 39

----------------------------------------------------------------------------

----

Description             : Used for IPv4 traffic analysis

Status                  : Accepted

Match Fields

    ipv4 destination address

    ipv4 protocol

    ipv4 source address

    transport destination port

    transport source port

Collect Fields

counter bytes

    counter packets

Display the information of a specific flow record.

switch# show flow record record-1

----------------------------------------------------------------------------

----

Flow record  'record-1'

----------------------------------------------------------------------------

----

Description             : Used for IPv4 traffic analysis

Status                  : Accepted

Match Fields

    ipv4 destination address

    ipv4 protocol

    ipv4 source address

    transport destination port

    transport source port

Collect Fields

    counter bytes

    counter packets
Display information for all flow records

switch# show flow record

----------------------------------------------------------------------------
----
Flow record  'record-1'

----------------------------------------------------------------------------

----

Description             : Used for IPv4 traffic analysis

Public

show flow record 40

Status                  : Accepted

Match Fields

ipv4 destination address

ipv4 protocol

ipv4 source address

transport destination port

transport source port

Collect Fields

counter bytes

counter packets

----------------------------------------------------------------------------

----

Flow record  'record-2'

----------------------------------------------------------------------------

----

Description             : Used for IPv6 traffic analysis

Status                  : Accepted

Match Fields

ipv6 destination address

ipv6 protocol

ipv6 source address

ipv6 version

transport destination port

transport source port

Collect Fields

application name

counter bytes

counter packets

```
Display information for a specific flow record

switch# show flow record record-3

----------------------------------------------------------------------------

----

Flow record  'record-3'

----------------------------------------------------------------------------

----

Description             : Used for IPv4 traffic analysis

destination address, protocol, transport destination port, and transport

source port.)
Match Fields

ipv4 destination address

ipv4 protocol

ipv4 source address

Public

show flow record 41

Collect Fields

counter bytes

counter packets
Display information with no flow records configured

switch# show flow record

No flow records configured

Command History

Release

Modification

10.17.1000

Command introduced on the 4100i, 6000, and 6100 Switch series.

Command Information

Platforms

Command context

Authority

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

4100i

6000

6100

show ipfix flow-table-utilization

Syntax

show ipfix flow-table-utilization

Description

Displays the current IPFIX flow table utilization per VSF member, including both the maximum capacity and
the current number of current flows.

Examples

Displaying current IPFIX flow table utilization:

switch# show ipfix flow-table-utilization
=================

Slot name | flow resources capacity | flow resources in use

----------|-------------------------|----------------------

Public

show ipfix flow-table-utilization 42

1/1       | 3072                    | 1245

1/3       | 3072                    | 980

Command History

Release

Modification

10.17.1000

Command introduced on 4100i, 6000, and 6100 Switch series.

Command Information

Platforms

Command context

Authority

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

4100i

6000

6100

Alarms

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

Public

Alarms 43

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

Public

alarm 44

Parameter

   action

<LOG‐AND‐TRAP>

<RELAY>

Description

Specifies the action to be taken when the monitored event occu
rs.

Generates an event log and SNMP trap.

Relays an event to alarm output port.

   name <STRING>

Specifies the external device connected.

   trigger

Triggers an alarm based on a normally open or closed circuit.

Generates an alarm event when the circuit is closed.

<CLOSED>

<OPEN>

no ...

snooze

Generates an alarm event when the circuit is open.

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

Public

alarm 45

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

Public

alarm 46

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

Parameter

{IN1 | IN2}

name

<STRING>

action

<LOG‐AND‐TRAP>

<RELAY>

Description

Specifies the input alarm port..

Specifies the external device connected.

Descriptive string.

Specifies the action to be taken when the monitored event occu
rs.

Generates an event log and SNMP trap.

Relays an event to alarm output port.

Public

alarm input 47

Description

Triggers an alarm based on a normally open or closed circuit.

Generates an alarm event when the circuit is closed.

Generates an alarm event when the circuit is open.

Parameter

trigger

<CLOSED>

<OPEN>

Examples

Configuring an alarm on input port 1 named Door-Sensor:

switch(config)# alarm input IN1 name Door-Sensor

Removing the configuring for an alarm on input port 1:

switch(config)# no alarm input IN1

Configuring an alarm on input port 1 with log-and-trap action:

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

Public

alarm input 48

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

Examples

Repeats the previous snooze time.

Configuring an alarm relay action for 10 minutes:

switch(config)# alarm snooze 10
Configuring an alarm relay action to be repeated with previously configured snooze time:

switch(config)# alarm snooze repeat

Command History

Release

10.08

Modification

Feature introduced.

Public

alarm snooze 49

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

timer

temperature

Examples

Description

Specifies the input alarm port..

Selects the alarm events from the power supply.

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

Public

show alarm 50

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

Public

show alarm 51

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

Boot commands

Subtopics

Boot commands

Boot commands

Subtopics

boot set-default
boot system
show boot-history

Public

Boot commands 52

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

Public

boot set-default 53

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

Usage

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

Public

boot system 54

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

Public

boot system 55

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

Public

show boot-history 56

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

Public

show boot-history 57

Boot History String

All line modules faulted

Description

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

Public

show boot-history 58

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

Public

show boot-history 59

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

Public

show boot-history 60

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

Public

L1-100Mbps downshift 61

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

Public

downshift enable 62

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

Specifies the port identifier range.

Public

show interface 63

Description

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

Continuously monitor interface statistics.

Shows VLAN interface information.

Specifies the LAG number. Range: 1‐256

Specifies the VLAN ID. Range: 1‐4094

Parameter

<IFRANGE>

brief

physical

extended

human‐readable

non‐zero

LAG

monitor

VLAN

<LAG‐ID>

<VLAN‐ID>

Examples

switch# show interface 1/1/1
Interface 1/1/1 is up
Admin state is up

Link state: up for 2 days (since Sun Jun 21 05:30:22 UTC 2020)

Public

show interface 64

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

Public

show interface 65

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

Public

show interface 66

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

Public

show interface 67

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

Public

show interface 68

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

Public

show interface 69

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

Public

show interface 70

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

Public

show interface 71

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

Public

show interface 72

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

Public

show interface 73

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

Collision                         n/a

0                    0

Runts                               0

n/a                    0

Giants                              0

n/a                    0

Command History

Release

10.15

10.11

10.10

Modification

Added state information when port goes into down state.

Added  monitor  parameter.

Added  human‐readable  parameter.

10.07 or earlier

‐‐

Public

show interface 74

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

show interface downshift-enable

Syntax

show interface [<IFNNAME>|<IFRANGE>] downshift-enable

Description

Displays speed downshift information, including the interface speed status and configuration.

Parameter

Description

Specifies a interface name.

<IFNAME>

<IFRANGE>

Examples

Specifies the port identifier range.

Showing automatic downshift information:

switch(config-if)# show interface downshift-enable

-------------------------------------------------

              Downshift              Speed

Port      Enabled | Active    Status   | Config
-------------------------------------------------
1/1/1     yes       yes       100M-FDx   auto

1/1/2     yes       no        1G         auto

Public

show interface downshift-enable 75

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

show running-config interface

Syntax

show running-config interface [<IFNNAME>|<IFRANGE>]

show running-config interface [lag | loopback | tunnel | vlan ] [<ID>]

Description

Displays active configurations of various switch interfaces.

Public

show running-config interface 76

Parameter

Description

Specifies a interface name.

<IFNAME>

<IFRANGE>

LAG

LOOPBACK

TUNNEL

VLAN

<LAG‐ID>

<LOOPBACK‐ID>

<TUNNEL‐ID>

<VLAN‐ID>

VXLAN

<VXLAN‐ID>

Specifies the port identifier range.

Specifies LAG interface information

Specifies loopback interface information.

Specifies tunnel interface information.

Specifies VLAN interface information.

Specifies the LAG number. Range: 1‐256.

Specifies the LOOPBACK number. Range: 0‐255.

Specifies the tunnel ID. Range: 1‐255.

Specifies the VLAN ID. Range: 1‐4094.

Specifies the VXLAN interface information.

Specifies the VXLAN interface identifier. Default: 1.

Public

show running-config interface 77

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

Public

Mirroring 78

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

Public

Mirroring 79

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

Public

Mirror statistics 80

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

Public

Mirroring commands 81

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

Public

clear mirror 82

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

Public

comment 83

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

Specifies a LAG (link aggregation group) identifier.

Public

destination interface 84

Usage

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

Destination interface limit per mirror session (4 possible sess
ions)

1

1

1

1

Switch

4100i

6000

6100

10040

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

Public

destination interface 85

Platforms

Command context

Authority

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

<TUNNEL‐IPV4‐ADDR>

Specifies the tunnel address in IPv4 format (x.x.x.x), where x is
a decimal number from 0 to 255.

Specifies the source address in IPv4 format (x.x.x.x), where x is
a decimal number from 0 to 255.

Public

destination tunnel 86

Parameter

Description

<SOURCE‐IPv4‐ADDR>

Specifies the DSCP value to be carried within the DS field of E
RSPAN packet header. Range: 0 to 63. Default: 0.

Specifies a VRF name. Default: default.

<DSCP‐VALUE>

<VRF‐NAME>

Examples

Creating a Mirror Session and adding tunnel destination, source, dscp, and VRF:

switch# config

switch(config)# mirror session 1

switch(config-mirror-1)# destination tunnel 1.1.1.1 source 2.2.2.2 dscp 10

vrf default

Replacing the existing tunnel destination:

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

Public

destination tunnel 87

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

Public

diagnostic 88

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

Public

disable 89

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

Public

enable 90

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

Public

mirror endpoint 91

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

Public

mirror endpoint 92

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

mirror session

Syntax

mirror session <SESSION-ID>

no mirror session <SESSION-ID>

Public

mirror session 93

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

mirror session 94

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

Public

show mirror 95

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

Public

show mirror 96

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

Public

show mirror 97

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
Showing the details of enabled mirror endpoint test:

switch# show mirror endpoint test

Mirror Endpoint: audit
Admin Status: enable

Operation Status: enabled

Comment: Mirror Endpoint Audit

Type: gre

Tunnel: source 1.1.1.1 destination 1.1.1.2 id 1 vrf default

Interface: 1/1/3

Public

show mirror endpoint 98

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

source interface

Syntax

source interface {<PORT-NUM> | <LAG-NAME>} [<DIRECTION>]
no source interface {<PORT-NUM> | <LAG-NAME>} [<DIRECTION>]

Public

source interface 99

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

10040

Source interface limit per mirror session (4 possibl
e sessions)

28

52

52

128

Public

source interface 100

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

switch(config-mirror-4)# source interface lag1 both

Stopping the mirroring of received packets from a configured source interface:

switch(config-mirror-4)# no source interface lag1 rx

Public

source interface 101

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

•  Rosewood (6200, 6300, 6400, 8360)

•  Matrix (4100i, 6000, 6100)

Public

Monitoring a device using SNMP 102

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

◦  Class 6: Type3 PD, it can draw a maximum of 51W.

◦  Class 7: Type4 PD, it can draw a maximum of 62W.

◦  Class 8: Type4 PD, it can draw a maximum of 71.3W.

Public

Power-over-Ethernet 103

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
level whereas the always-on poe and power-over-ethernet quick-poe commands are set at the slot level.
These commands can only be configured in the global configuration context.

Subtopics

lldp dot3 poe

Public

PoE commands 104

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

lldp dot3 poe 105

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

lldp med poe 106

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

power-over-ethernet 107

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

power-over-ethernet allocate-by 108

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

power-over-ethernet allocate-by 109

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

power-over-ethernet always-on 110

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

power-over-ethernet assigned-class 111

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

power-over-ethernet pre-std-detect 112

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

power-over-ethernet priority 113

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

power-over-ethernet quick-poe 114

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

power-over-ethernet quick-poe 115

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

power-over-ethernet threshold 116

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

power-over-ethernet trap 117

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

show lldp local 118

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

show lldp neighbor 119

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

show power-over-ethernet 120

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

show power-over-ethernet 121

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

show power-over-ethernet 122

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

Aruba AirWave 123

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

Supported features with AirWave and the AOS-CX swi... 124

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

Configuring the AOS-CX switch to be monitored by A... 125

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

Remote syslog commands
SNMP commands

Remote syslog commands

Subtopics

clear accounting-logs
diag persistent-storage
logging
logging accounting-format-native
logging filter
logging facility
logging persistent-storage

clear accounting-logs

Public

AirWave commands 126

Syntax

clear accounting-logs

Description

Use this command to clear accounting logs. Once issued, only logs generated after this command is run will
be displayed in the output of the show accounting log commands.

NOTE

This command will not clear logs when the logging accounting-format-native
feature is configured. To clear accounting logs on switches with this feature
enabled, users should first revert the native accounting format back to the
default AOS-CX format by executing the no logging accounting-format-native
command.

Example

switch(config)# clear accounting-logs

The following example shows that accounting logs cannot be cleared using the clear accounting-logs
command if the logging accounting-native-format command has been enabled, and that disabling this
option with the no logging accounting-format-native command again allows the accounting logs to be
cleared.

switch# logging audit-format-native

switch# clear accounting-logs

Warning: Clear accounting-logs is not supported for 'audit-format-native'.

switch# no logging audit-format-native

switch# clear accounting-logs

switch# show accounting log last 5

---------------------------------------------------

Command logs from current boot

---------------------------------------------------

No command logs has been logged in the system

Command History

Release

10.11

Modification

Command introduced.

Public

clear accounting-logs 127

Command Information

Platforms

Command context

Authority

All platforms

Operator (>) or Manager
(#)

Administrators or local user group members with execution righ
ts for this command.

diag persistent-storage

Syntax

diag persistent-storage enable [{severity <LEVEL> | timeout <TIMEOUT> |

filter <FILTER_NAME> | storage-writes <STORAGE_WRITES> | usb <STORAGE_URL>}]

diag persistent-storage disable

Description

Enables or disables storage of logs in storage. Only logs of the specified severity and above will be preserved
in the storage.

NOTE

To switch the persistent storage setting from one option (e.g., USB) to another
(e.g., storage-writes), you must first disable persistent storage by running the
command diag persistent-storage disable. that the storage-writes option applies
only to local storage and does not work with USB.

Parameter

enable

disable

Description

Enable persistent logging.

Disable persistent logging.

severity <LEVEL>

Specifies the severity of the syslog messages:

•  alert: Preserves syslog messages with the severity of alert

(6) and emergency (7)

•  crit: Preserves syslog messages with the severity of critical

(5) and above. Default.

•  debug: Preserves syslog messages with the severity of deb

ug (0) and above.

Public

diag persistent-storage 128

Parameter

Description

•  emer: Preserves syslog messages with the severity of eme

rgency (7) only.

•  err: Preserves syslog messages with the severity of err (4)

•

and above.
info: Preserves syslog messages with the severity of info (1
) and above.

•  notice: Preserves syslog messages with the severity of noti

ce (2) and above.

•  warn: Preserves syslog messages with the severity of warn

ing (3) and above.

filter <FILTER_NAME>

Preserve logs for specified filter name.

timeout <TIMEOUT>

Preserve logs for specified duration. Range: 1 to 60 minutes. De
fault: 20 minutes.

storage‐writes
<STORAGE_WRITES>

Limit the amount of storage writes.

usb <STORAGE_URL>

Preserve logs in the USB storage.

Examples

Enabling storage of logs in storage with severity err and timeout 30 minutes:

switch(config)#diag persistent-storage enable severity err timeout 30

Logs will be written to storage. Prolonged usage of persistent logging can

affect lifetime of storage. Hence enable persistent logging only for short

duration and also for the right severity.

Do you want to continue (y/n)? y
Enabling storage of logs in storage with severity err and timeout 30 minutes and 512 storage-writes:

switch(config)#diag persistent-storage enable severity err timeout 30

storage-writes 512

Logs will be written to storage. Prolonged usage of persistent logging can

affect lifetime of storage. Hence enable persistent logging only for short

duration and also for the right severity.

Do you want to continue (y/n)? y
Disabling log storage:

switch(config)# diag persistent-storage disable

Public

diag persistent-storage 129

Command History

Release

10.17

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

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

Public

logging 130

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

Public

logging 131

Parameter

Description

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

switch(config)# no logging

Enabling syslog forwarding over TLS to a remote syslog server using subject-name authentication mode:

switch(config)#logging example.com tls auth-mode subject-name

Applying log filtering for syslog server forwarding:

switch(config)# logging 10.0.10.6 severity info filter filter_lldp_logs vrf
mgmt

Applying log filtering and enabling the rate limit for syslog server forwarding over TCP port:

Public

logging 132

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

logging accounting-format-native

Syntax

logging accounting-format-native

[no] logging accounting-format-native

Description

Change the accounting log message format to native Linux format. (Default: AOS-CX format)

The 'no' form of this command will change the accounting log message format to AOS-CX format.

Usage

This option enables the switch to show all types of accounting records to the user. When configured, the
same format will be used while sending messages to syslog servers. When upgrading to this version of
AOS-CX from AOS-CX 10.10 or earlier versions, if native accounting logs are preferred, then best practices is
to issue this command as a part of the upgrade. If the switch upgrades from AOS-CX 10.10 or earlier without
configuring this setting, by default, the accounting log message format will be AOS-CX Format.

Public

logging accounting-format-native 133

Example

This example changes the accounting log message format to native Linux format.

switch(config)# logging accounting-format-native

The following example returns the accounting log message format to the default AOS-CX format.

switch(config)# no logging accounting-format-native

Command History

Release

10.11

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

logging filter

Syntax

logging filter <FILTER-NAME>

   [{enable | disable}]
   [<SEQUENCE-ID>] {permit | deny} [event-id <EVENT-ID-RANGE>] [includes

<REGEX>] [severity <COMPARISON-OPERATOR>

            <LEVEL>]

   no <SEQUENCE-ID>

   resequence <OLD-SEQUENCE-ID>

            <NEW-SEQUENCE-ID>

no logging filter <FILTER-NAME>

Description

Creates a filter to restrict what event or debug logs are logged. A filter can be used to either permit or deny:

Public

logging filter 134

•  The event logs from being generated on the switch, or

•  The event or debug logs generated on the switch from being forwarded to a syslog server.

A filter is identified by a filter name and can have up to 20 rules or entries, each with a different sequence
number, matching criteria, and corresponding action (deny or permit). When a filter is applied on a log, the
log is matched against the criteria mentioned in the rules or entries in ascending numerical order of their
sequence numbers until a matching entry is found. Once a matching entry is found, its corresponding action
is applied on the log. If no matching rule is found, the default action (permit) is applied.

The no form of this command removes the filter.

Parameter

Description

Specifies the unique name to identify the filter.

<FILTER‐NAME>

enable

Filter event logs generated on the switch.

<SEQUENCE‐ID>

deny

permit

<event‐id>

Specifies the filter criteria sequence number. Default: Incremen
ts by 10 from the largest sequence‐id currently used in this fil
ter.

Prevents the matching log from being logged.

Allows the matching log.

Matches logs by event ID. Specify an event ID or a range of eve
nt IDs. It supports a maximum of 100 event IDs.

includes <REGEX>

Matches the log message against a regular expression string.

severity

Matches the logs by severity level.

The following options are used to compare the severity:

•  eq: Match events of severity equal to the specified.
•  ge: Match events of severity greater than or equal to the sp

ecified.

•  gt: Match events of severity greater than the specified.
•

le: Match events of severity lesser than or equal to the spec
ified.
lt: Match events of severity lesser than the specified.

•

Public

logging filter 135

Parameter

Description

The following are the severity levels:

•  alert: Logs with the severity alert (6).
•  crit: Logs with the severity critical (5).
•  debug: Logs with the severity debug (0).
•  emerg: Logs with the severity emergency (7).
•  err: Logs with the severity err (4).
info: Logs with the severity info (1).
•
•  notice: Logs with the severity notice (2).
•  warning: Logs with the severity warning (3).

Usage

Filtering event logs on the switch: To permit or deny event logs from being generated on the switch.
In this case, the matching event logs are filtered at generation. The denied event logs are neither logged
to the switch events nor forwarded to any remote syslog servers. Multiple filters can be configured, but
only one filter can be applied to filter the events on the switch. Such a filter can be chosen by adding the
enable command under its configuration. Configuring the enable command under a new filter automatically
removes it from the filter where it was previously used.

For example:

logging filter low_severity_logs

enable

10 deny severity lt info
This configuration denies the event logs which have a severity less than info.

NOTE
If a filter contains enable command, it is not recommended to configure this
filter in the logging command used for remote syslog server configuration. This
is because, any event logs denied by the filter are already not available for
forwarding to a remote server.

A filter with enable command will not affect debug logs. Consider the configuration in the following example
of a filter with enable command and two rules applied 10 permit severity ge info and 20 deny. This implies
permit only those event logs which have severity greater than or equal to info.

Example:

            logging filter low_severity_logs
enable
10 permit severity ge info

20 deny

Public

logging filter 136

Filtering event or debug logs when forwarding to a remote syslog server: The filter name must be
configured in the logging command that is used to configure remote syslog server. The logs will be
generated on the switch and the filter only decides whether to deny or permit the syslog forwarding for the
matching log. For example: logging 10.0.10.6 filter filter_lldp_logs

NOTE
The filter affects debug logs only when the command debug destination syslog
is configured on the switch.

NOTE

The severity mentioned in the remote syslog server configuration using logging
command under configuration context has more precedence than the severity
mentioned in a filter entry. If a log with warning severity is permitted by a filter,
but the remote syslog configuration has severity err mentioned in it, the log will
not be forwarded to the remote syslog server (since warning(3) is lesser than
err(4)). On the other hand, if a log with err severity is permitted by a filter and
the remote syslog configuration has severity warning mentioned in it, the log will
be forwarded to the remote syslog server.

Examples

Configuring a new logging filter:

switch(config)# logging filter example_filter

To deny logs having event ID 1301 and a range of event IDs from 1305 to 1309:

switch(config-logging-filter)# 20 deny event-id 1301,1305-1309

To permit logs having event ID 1300:

switch(config-logging-filter)# 30 permit event-id 1300

To permit logs with severity greater than or equal to  err :

switch(config-logging-filter)# 30 permit severity ge err

To deny logs with severity greater than info:

switch(config-logging-filter)# 30 deny severity gt info

To deny logs with event ID 1024 and a message matching the regular expression LLDP:

Public

logging filter 137

switch(config-logging-filter)# 40 deny event-id 1024 includes LLDP

Denying all logs:

switch(config-logging-filter)# 40 deny

Changing the sequence ID of an existing rule:

switch(config-logging-filter)# resequence 20 70

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

config  and  config
‐logging‐filter

Administrators or local user group members with execution righ
ts for this command.

logging facility

Syntax

logging facility {local0 | local1 | local2 | local3 | local4 | local5 |

local6 | local7}

no logging facility

Description

Sets the logging facility to be used for remote syslog messages. Default:  local7

The no form of this command disables the logging facility to be used for remote syslog messages.

Public

logging facility 138

Parameter

Description

{local0 | local1 | local2 |

  local3 | local4 | local5

Selects the logging facility to be used for remote syslog messag
es. Required.

|

  local6 | local7}

Specifies the severity of the syslog messages:

•
•
•
•
•
•
•
•

local0
local1
local2
local3
local4
local5
local6
local7

Examples

Sets the local5 logging facility to be used for remote syslog messages:

switch(config)# logging facility local5

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

logging persistent-storage

Public

logging persistent-storage 139

Syntax

logging persistent-storage [severity {alert|crit|debug|emerg|err|info|

notice|warning}]

no logging persistent-storage

Description

Enables or disables storage of logs in storage. Only logs of the specified severity and above will be preserved
in the storage.

The no form of this command disables storage of logs in storage.

NOTE

This command is deprecated. Please use "diag persistent-storage" command to
preserve logs in storage.

Parameter

Description

severity <LEVEL>

Specifies the severity of the syslog messages:

•  alert: Preserves syslog messages with the severity of alert

(6) and emergency (7)

•  crit: Preserves syslog messages with the severity of critical

(5) and above. Default.

•  debug: Preserves syslog messages with the severity of deb

ug (0) and above.

•  emerg: Preserves syslog messages with the severity of em

ergency (7) only.

•  err: Preserves syslog messages with the severity of err (4)

•

and above.
info: Preserves syslog messages with the severity of info (1
) and above.

•  notice: Preserves syslog messages with the severity of noti

ce (2) and above.

•  warning: Preserves syslog messages with the severity of

warning (3) and above.

Usage

These logs can be copied out by using the copy support-files all or copy support-files previous-boot.

Examples

Enabling storage of logs in storage with severity info:

Public

logging persistent-storage 140

switch(config)#logging persistent-storage severity info

Logs will be written to storage and made available across reboot.

Do you want to continue (y/n)?
Disabling storage of logs in storage:

switch(config)# no logging persistent-storage

Command History

Release

10.17

Modification

Command deprecated.

10.07 or earlier

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

SNMP commands

Subtopics

event-trap-enable
lldp trap enable
mac-notify traps
rmon alarm {enable | disable} {index | all}
rmon alarm
show configuration-changes trap
show mac-notify port
show mac-notify
show rmon alarm
show snmp agent-port
show snmp community
show snmpv3 context
show snmpv3 engine-id
show snmpv3 security-level

Public

SNMP commands 141

show snmp system
show snmp trap
show snmpv3 users
show snmp views
show snmp vrf
snmpv3 context
snmpv3 engine-id
snmpv3 security-level
snmp-server agent-port
snmp-server community view
snmp-server community
snmp-server historical-counters-monitor
snmp-server host
snmp-server system-contact
snmp-server system-description
snmp-server system-location
snmp-server trap-source interface vrf
snmp-server vrf
snmpv3 user view
snmpv3 user
snmp-server response-source
snmp-server snmpv3-only
snmp-server trap
snmp-server trap aaa-server-reachability-status
snmp-server trap configuration-changes
snmp-server trap mac-notify
snmp-server trap port-security
snmp-server trap snmp
snmp-server trap vsx
snmp-server view

event-trap-enable

Syntax

event-trap-enable

no event-trap-enable

Description

Enables the notification of events to be sent as traps to the SNMP management stations. It is enabled by
default.

The no form of this command disables the event traps.

Public

event-trap-enable 142

Examples

Enabling the event traps:

switch(config)# event-trap-enable

Disabling the event traps:

switch(config)# no event-trap-enable

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

lldp trap enable

Syntax

lldp trap enable

no lldp trap enable

Description

Enables sending SNMP traps for LLDP related events from a particular interface. LLDP trap generation is
enabled by default on all the interfaces and has to be disabled for interfaces on which traps are not required
to be generated.

The no form of this command disables the LLDP trap generation.

NOTE
LLDP trap generation is disabled by default at the global level and must be
enabled before any LLDP traps are sent.

Public

lldp trap enable 143

Examples

Enabling LLDP trap generation on global level:

switch(config)# lldp trap enable

Enabling LLDP trap generation on interface level:

switch(config-if)# lldp trap enable

Disabling LLDP trap generation on global level:

switch(config)# no lldp trap enable

Disabling LLDP trap generation on interface level:

switch(config-if)# no lldp trap enable

Displaying LLDP global configuration:

switch# show lldp configuration

LLDP Global Configuration

=========================

LLDP Enabled                 : No

LLDP Transmit Interval       : 30

LLDP Hold Time Multiplier    : 4

LLDP Transmit Delay Interval : 2

LLDP Reinit Timer Interval   : 2

LLDP Trap Enabled            : No

TLVs Advertised

===============

Management Address

Port Description

Port VLAN-ID

System Description
System Name

LLDP Port Configuration

=======================

PORT           TX-ENABLED          RX-ENABLED          INTF-TRAP-ENABLED

--------------------------------------------------------------------------

1/1/1          Yes                 Yes                 Yes

1/1/2          Yes                 Yes                 Yes

1/1/3          Yes                 Yes                 Yes

1/1/4          Yes                 Yes                 Yes

1/1/5          Yes                 Yes                 Yes

1/1/6          Yes                 Yes                 Yes

...........

Public

lldp trap enable 144

...........

mgmt           Yes                 Yes                 Yes
Displaying LLDP Configuration for the interface:

switch# show lldp configuration 1/1/1

LLDP Global Configuration

=========================

LLDP Enabled                 : Yes

LLDP Transmit Interval       : 30

LLDP Hold Time Multiplier    : 4

LLDP Transmit Delay Interval : 2

LLDP Reinit Timer Interval   : 2

LLDP Trap Enabled            : No

LLDP Port Configuration

=======================

PORT           TX-ENABLED          RX-ENABLED          INTF-TRAP-ENABLED

--------------------------------------------------------------------------

1/1/1          Yes                 Yes                 Yes
Displaying LLDP Configuration for the management interface:

switch# show lldp configuration mgmt

LLDP Global Configuration

=========================

LLDP Enabled                 : Yes

LLDP Transmit Interval       : 30

LLDP Hold Time Multiplier    : 4

LLDP Transmit Delay Interval : 2

LLDP Reinit Timer Interval   : 2

LLDP Trap Enabled            : Yes

LLDP Port Configuration

=======================

PORT           TX-ENABLED          RX-ENABLED          INTF-TRAP-ENABLED

--------------------------------------------------------------------------
mgmt           Yes                 Yes                 Yes

Command History

Release

Modification

10.07 or earlier

‐‐

Public

lldp trap enable 145

Command Information

Platforms

Command context

Authority

All platforms

config  and  config
‐if

Administrators or local user group members with execution righ
ts for this command.

mac-notify traps

Syntax

mac-notify traps {aged | learned | moved | removed}

no mac-notify traps {aged | learned | moved | removed}

Description

Configures a Layer 2 or VXLAN interface to generate SNMP trap notifications for up to four different types
of MAC address related events on the trunk or access in physical or lag interfaces.

MAC notification trap addition to or removal from an interface can be in any combination, quantity, or order.
The addition of existing configured traps or removal of non-configured traps will be accepted and ignored.

NOTE
The mac-notify feature must be enabled globally for any interface configurations
to generate SNMP traps. Enabling mac-notify traps may impact the system
performance on networks with a large number of mac-notify events.

The no form of this command removes the traps from the interface.

Parameter

aged

learned

moved

Description

Notifies when a MAC address aged out on the interface.

Notifies when a MAC address is learned on the interface.

Notifies when a MAC address moved from the interface.

Public

mac-notify traps 146

Parameter

removed

NOTE

Description

Notifies when a MAC address is removed from the interface.

MAC notification cannot be configured on a Layer 3 (routing) interface. A Layer
2 interface that is changed to a Layer 3 interface through the  routing
command will discard any existing MAC notification configurations.
When MACs are learned on VXLAN tunnels or port-access port-security
enabled ports, the move scenario is handled by the EVPN/port-access feature
respectively. It performs the move by deleting the MAC from the old port and
installing it on the new port. In this scenario, MAC trap notifications, if enabled,
will reflect that by producing removed and learned notifications.

Usage

•  MAC notify trap will not generate for static MACs.

•  vsx-sync is not supported. You must enable the MAC notify traps explicitly on secondary to ensure the

traps are generated.

•  For EVPN MAC move between the following interfaces, the respective event types are produced (not

always removed or learned)

◦  Port to port: moved

◦  Port to tunnel: removed/learned

◦  Tunnel to port: removed/learned

◦  Tunnel to Tunnel: moved

Examples

NOTE
MAC notification types and the associated events only apply to Layer 2 and
VXLAN interfaces, hence routing might need to be disabled on the relevant
interfaces.

Enable MAC notification traps within the SNMP module at a global level:

switch(config)# snmp-server trap
 aaa-server-reachability-status  Enable SNMP trap for AAA server

reachability  status

 configuration-changes           Enable configuration changes traps

Public

mac-notify traps 147

cpu-utilization                 Enable high CPU utilization traps

 link-status                     Enable link status traps for all physical

interfaces

 mac-notify                      Enable MAC table change notification traps

 memory-utilization              Enable high memory utilization traps

 module                          Enable module event traps

 port-security                   Enable port-security violation traps.

                                  (Default: enable)

 rmon-events                     Enable RMON event traps

 snmp                            Enable snmp traps
For more information, see snmp-server trap mac-notify.

Enabling the traps on an L2 interface:

switch(config)# interface 1/1/1

switch(config-if)# mac-notify traps learned

1/1/1 is not an L2 interface or tunnel

switch(config-if)# no routing

switch(config-if)# mac-notify traps learned removed

switch(config-if)# mac-notify traps moved

switch(config-if)# mac-notify traps aged

switch(config)# interface vxlan 1

switch(config-vxlan-if)# mac-notify traps learned removed

switch(config)# interface lag101

switch(config-if)# mac-notify traps removed

Disabling the  learned  and  removed  traps from the interface 1/1/1:

switch(config)# interface 1/1/1

switch(config-if)# no mac-notify traps learned removed

switch(config)# interface vxlan 1

switch(config-vxlan-if)# no mac-notify traps learned removed

Enable sending SNMP notifications for MAC table changes:

switch(config-vxlan-if)# mac-notify traps

  aged            Notify when a MAC address aged out on the interface

  learned         Notify when a MAC address was learned on the interface

  moved           Notify when a MAC address moved from the interface

  removed         Notify when a MAC address was removed from the interface

switch(config-vxlan-if)# mac-notify traps learned aged removed moved

Public

mac-notify traps 148

Command History

Release

Modification

10.13.1000

Support for SNMP MAC notify traps on VXLAN tunnels.

10.10

10.08

Support for port access features with mac‐notify added.

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

Auditors or Administrators or local user group members with
execution rights for this command. Auditors can execute this co
mmand from the auditor context (auditor>) only.

rmon alarm {enable | disable} {index | all}

Syntax

rmon alarm {enable | disable} {index <INDEX> | all}
no rmon alarm [enable | disable] [index <INDEX> | all]

Description

Enables and disables the RMON alarm and its index. RMON alarm is enabled by default.

Parameter

enable

disable

Description

Enables the RMON alarm index

Disables the RMON alarm index.

Public

rmon alarm {enable | disable} {index | all} 149

Parameter

index <INDEX>

Description

Specifies the RMON alarm index. Range: 1 to 20.

all

Examples

Specifies all the RMON alarms.

Enabling or disabling all the RMON alarm:

switch(config)# rmon alarm enable all

switch(config)# rmon alarm disable all

Enabling or disabling RMON alarm by index:

switch(config)# rmon alarm enable index 1

switch(config)# rmon alarm disable index 1

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

rmon alarm

Syntax

rmon alarm index <INDEX> snmp-oid <SNMP-OID> rising-threshold <RISING-
THRESHOLD>

     falling-threshold <FALLING-THRESHOLD> [sample-interval <SAMPLE-

INTERVAL>] [sample-type <ABSOLUTE|DELTA>]

no rmon alarm [index <INDEX>]

Public

rmon alarm 150

Description

Stores configuration entries in an alarm table that defines the sample interval, sample-type, and threshold
parameters for an SNMP MIB object. Only the SNMP MIB objects that resolve to an ASN.1 primitive type of
INTEGER (INTEGER, Integer32, Counter32, Counter64, Gauge32, or TimeTicks) will be monitored.

The no form of this command removes all RMON alarms and allows you to specify an index to remove a
particular RMON alarm.

Parameter

index <INDEX>

Description

Specifies the RMON alarm index. Range: 1 to 20.

snmp‐oid <SNMP‐OID>

Specifies the SNMP MIB object to be monitored by RMON.

rising‐threshold <RISING‐
THRESHOLD>

Specifies the upper threshold value for the RMON alarm.

falling‐threshold <FALLING‐
THRESHOLD>

Specifies the falling threshold value for the RMON alarm. The fa
lling threshold must be less than the rising threshold.

sample‐interval  <SAMPLE‐
INTERVAL>

Sample interval in seconds. Default: 30.

sample‐type <ABSOLUTE|
DELTA>

Specifies the method of sampling of the SNMP MIB object. Defa
ult: Absolute.

Examples

Configuring RMON for the MIB object ifOutErrors.15 with an index 1, rising threshold of 2147483647 and
falling threshold of -2134 using absolute sampling for a sample interval of 100 seconds:

switch(config)# rmon alarm index 1 snmp-oid ifOutErrors.15 rising-threshold

2147483647

     falling-threshold -2134 sample-type absolute sample-interval 100

Removing RMON alarm with the index 5:

switch(config)# no rmon alarm index 5

Public

rmon alarm 151

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

show configuration-changes trap

Syntax

show configuration-changes trap

Description

Shows the SNMP configuration changes trap settings.

Example

Showing the SNMP configuration changes trap:

switch# show configuration-changes trap

SNMP Configuration changes trap : Enabled

```

Command History

Release

10.10

Modification

Command introduced

Public

show configuration-changes trap 152

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

show mac-notify port

Syntax

show mac-notify [port <PORTS>]

Description

Displays the MAC notification configuration on a range of ports.

Parameter

Description

[port <PORTS>]

Specifies a port, range of ports, or list of ports.

Examples

Showing the MAC notification configuration on a range of ports:

switch(config)# show mac-notify port 1/1/1,1/1/3,1/1/5,lag101-lag104

MAC notification global Setting: Enabled

Port         Enabled Traps

---------------------------------------
1/1/1        aged learned moved

1/1/3        --

1/1/5        moved

lag101       removed

lag102       --

lag103       --

lag104       aged learned moved removed

Public

show mac-notify port 153

Command History

Release

10.08

Modification

Command introduced

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

show mac-notify

Syntax

show mac-notify

Description

Displays whether the MAC notification feature in the SNMP module is enabled or not. It also displays the trap
notification types configured on the Layer 2 ports in the system.

Examples

Showing the MAC notification configuration on all configured ports in the system:

switch# show mac-notify
MAC notification global setting : Enabled

Port         Enabled Traps

---------------------------------------

1/1/1        aged learned moved

1/1/5        moved

lag101       removed

lag104       aged learned moved removed

...

...

Public

show mac-notify 154

Command History

Release

10.08

Modification

Command introduced

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

show rmon alarm

Syntax

show rmon alarm [index <INDEX>]

Description

Displays the RMON alarm configurations.

Parameter

index <INDEX>

Description

Specifies the RMON alarm index. Range: 1 to 20.

Examples

Showing all RMON alarm configurations:

switch# show rmon alarm

Index              : 1

Enabled            : true

Status             : valid
MIB object         : ifOutErrors.15

Sample type        : delta

Sampling interval  : 6535 seconds

Rising threshold   : 100

Public

show rmon alarm 155

Falling threshold  : 10

Last sampled value : 0

Last sample time   : 2020-09-21 05:58:11

Index              : 3

Enabled            : true

Status             : invalid

MIB object         : IF-MIB::ifDescr.19

Sample type        : absolute

Sampling interval  : 10000 seconds

Rising threshold   : 4000

Falling threshold  : 10

Last sampled value : 0
Showing RMON alarm with alarm index 1:

switch# show rmon alarm index 1

Index              : 1

Enabled            : true

Status             : valid

MIB object         : ifOutErrors.15

Sample type        : delta

Sampling interval  : 6535 seconds

Rising threshold   : 100

Falling threshold  : 10

Last sampled value : 0

Last sample time   : 2020-06-21 05:58:11
Showing disabled RMON alarm information:

switch# show  rmon   alarm

Index              : 1

Enabled            : false

Status             : valid

MIB object         : ifOutErrors.15

Sample type        : delta
Sampling interval  : 6535 seconds

Rising threshold   : 100

Falling threshold  : 10

Last sampled value : 0

Last sample time   : 2020-09-21 05:58:11

Index              : 3

Enabled            : false

Status             : invalid

MIB object         : IF-MIB::ifDescr.19

Sample type        : absolute

Sampling interval  : 10000 seconds

Rising threshold   : 4000

Public

show rmon alarm 156

Falling threshold  : 10

Last sampled value : 0

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

show snmp agent-port

Syntax

show snmp agent-port

Description

Displays SNMP agent UDP port number.

Example

Displaying SNMP agent UDP port number:

switch# show snmp agent-port

SNMP agent port : 161

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show snmp agent-port 157

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

show snmp community

Syntax

show snmp community

Description

Displays a list of all configured SNMPv1/v2c communities.

Usage

When a user creates a custom community before enabling an SNMP agent, AOS-CX automatically removes
the default public community from the system.

Example

Displaying a list of all configured SNMPv1/v2c communities:

switch#show snmp community

SNMP-COMMUNITIES

-------------------------------------------------------------------

Community          Access-level  ACL Name   ACL Type   View

-------------------------------------------------------------------
private            ro            my_acl     ipv4       view1

private            ro            my_acl     ipv6       none

private2           rw            new_Acl    ipv6       view2

private3           rw            none       none       none
When the switch is configured to use SNMPv3 only, the output of the show snmp community command
displays the message SNMP v1/v2c is disabled while snmpv3-only mode is configured:

switch# show snmp community
----------------------------------------------------------------------------

--------------

Community                        Access-level ACL Name                  ACL

Type   View

Public

show snmp community 158

----------------------------------------------------------------------------

--------------

SNMP v1/v2c is disabled while snmpv3-only mode is configured

Command History

Release

10.14

10.10

10.08

Modification

The output of this command now displays an error message when the switch is i
n SNMPv3‐only mode.

Output has been updated with SNMP view details. A View column is added to th
e command output.

Added ACL Type column to the command output.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

show snmpv3 context

Syntax

show snmpv3 context

Description

Displays all configured SNMP contexts.

Examples

Displaying all configured SNMP contexts:

switch# show snmpv3 context

--------------------------------------------------------------------------

name                            vrf                             community

--------------------------------------------------------------------------

Public

show snmpv3 context 159

contextA                        default                         private

switch# show snmpv3 context

--------------------------------------------------------------------------

Name           vrf             Community          ype[Instance_id]

------------------------------------------------------------------

A              default         public             vrf

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

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show snmpv3 engine-id

Syntax

show snmpv3 engine-id

Description

Displays the configured SNMPv3 snmp engine-id.

If the SNMPv3 engine-id is not configured, by default a unique engine-id is created by the switch using a
combination of the enterprise OID value and the switch's mac address.

Example

Displaying the configured SNMPv3 engine-id:

switch# show snmpv3 engine-id

SNMP engine-id : 80:00:B8:5C:08:00:09:1d:de:a5

Public

show snmpv3 engine-id 160

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

show snmpv3 security-level

Syntax

show snmpv3 security-level

Description

Displays the configured SNMPv3 security level.

Examples

Displaying the configured SNMPv3 security level:

switch# show snmpv3 security-level

SNMPv3 security-level : auth

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show snmpv3 security-level 161

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

show snmp system

Syntax

show snmp system

Description

Displays SNMP description, location, and contact information.

Example

Displaying SNMP description, location, and contact information:

switch# show snmp system

SNMP system information

----------------------------

System description : Aggregation router

System location : Main lab

System contact : John Smith, Lab Admin

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show snmp system 162

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

show snmp trap

Syntax

show snmp trap

Description

Displays all configured SNMP traps/informs receivers.

Example

Displaying all configured SNMP trap and informs receivers:

switch# show snmp trap

HOST           PORT  TYPE   VER COMMUNITY/USER NAME VRF        NOTIFICATION

TYPES

----------------------------------------------------------------------------

-------

10.10.10.10    162   trap   v1  public              default    bgp

10.10.10.10    162   inform v2c public              default    bgp, ospf,

fan, mstp

10.10.10.10    162   inform v3  name                default

Command History

Release

10.14

Modification

Updated the example output.

10.07 or earlier

‐‐

Public

show snmp trap 163

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

show snmpv3 users

Syntax

show snmpv3 users

Description

Displays all configured SNMPv3 users.

For more details on the user enabled status, see snmpv3 security-level.

Example

Displaying all configured SNMPv3 users:

switch# show snmpv3 users

------------------------------------------------------------------------

User        AuthMode  PrivMode  Status   Context    Access-level  View

------------------------------------------------------------------------

name        md5       none      Enabled  context2   ro            view1

                                         context1

                                         context3

name2       none      none      Disabled none       ro            view2

name3       none      none      Disabled none       ro            none

Command History

Release

10.10

Modification

Output has been updated with SNMP view details. A View column is added to th
e command output.

10.07 or earlier

‐‐

Public

show snmpv3 users 164

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

show snmp views

Syntax

show snmp views

Description

Displays the list of all the configured SNMP views.

Usage

The following table contains the status and its description of the configured SNMP views:

Status

Description

pending_validation

Default value that indicates SNMP view is yet to be validated.

operational

OID and mask validated.

Invalid OID/mask.

Validation failed for reasons other than OID/mask.

invalid

failed

Examples

Displaying the list of all the configured SNMP views:

switch# show snmp views

------------------------------------------------------

SNMP MIB Views
------------------------------------------------------

View    : new

OID Tree: sysUpTime.0

Mask    : ff

Public

show snmp views 165

Type    : included

Status  : pending_validation

View    : admin

OID Tree: ifIndex.1

Mask    : ff:a0

Type    : included

Status  : operational

View    : user

OID Tree: sysb

Mask    : none

Type    : excluded

Status  : invalid

View    : admin

OID Tree: .1.3.6.1.2.1.1

Mask    : none

Type    : excluded

Status  : operational

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

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show snmp vrf

Syntax

show snmp vrf

Description

Displays the VRF on which the SNMP agent service is running.

Public

show snmp vrf 166

Example

Displaying SNMP services enabled on VRF:

switch#show snmp vrf

SNMP enabled VRF

----------------------------

mgmt

default

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

snmpv3 context

Syntax

snmpv3 context <NAME> vrf <VRF-NAME> [community <STRING>]
no snmpv3 context <NAME> [vrf <VRF-NAME>] [community <STRING>]

Description

Creates an SNMPv3 context on the specified VRF.

The no form of this command removes the specified SNMP context.

Parameter

Description

Specifies the name of the context. Range: 1 to 32 printable ASC
II characters, excluding space and question mark (?).

Public

snmpv3 context 167

Parameter

<NAME>

Description

vrf <VRF‐NAME>

Specifies the VRF associated with the context. Default: default.

community <STRING>

Specifies the SNMP community string associated with the con
text. Range: 1 to 32 printable ASCII characters, excluding space
and question mark. Default: public.

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

snmpv3 engine-id

Public

snmpv3 engine-id 168

Syntax

snmpv3 engine-id <ENGINE-ID>

no snmpv3 engine-id <ENGINE-ID>

Description

Configures the SNMPv3 SNMP engine-id allowing an administrator to configure a unique SNMP engine-id
for the switch. This engine-id is used by the NMS management tool to identify and distinguish multiple
switches on the same network.

The no form of this command restores the default engine-id, created by the switch using a combination of
the enterprise OID value and the switch's mac address.

Parameter

Description

SNMPv3 SNMP engine‐id in colon separated hexadecimal n
otation.

<ENGINE‐ID>

Examples

Configuring the SNMPv3 engine-id:

switch(config)#

switch(config)# snmpv3 engine-id

  WORD  SNMPv3 snmp engine-id in colon seperated hexadecimal notation

switch(config)# snmpv3 engine-id 01:23:45:67:89:ab:cd:ef:01:23:45:67
Restoring the default SNMPv3 engine-id:

switch(config)# no snmpv3 engine-id

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

snmpv3 engine-id 169

snmpv3 security-level

Syntax

snmpv3 security-level {auth | auth-privacy}

no snmpv3 security-level {auth | auth-privacy}

Description

Configures the SNMPv3 security level. The security level determines which SMNPv3 users defined by the
command  snmpv3 user  are able to connect.

The no form of this command changes the security level as follows:

•  no snmpv3 security-level auth: Sets the security level to auth-privacy.

•  no snmpv3 security-level auth-privacy: Sets the security level to no authentication or privacy, allowing

any SNMP user to connect.

Parameter

auth

auth‐privacy

Examples

Description

SNMPv3 users that support authentication, or authentication a
nd privacy are allowed.

Only SNMPv3 users with both authentication and privacy are al
lowed. This is the highest level of SNMPv3 security. Default.

Setting the SNMPv3 security level to authentication and privacy:

switch(config)# snmpv3 security-level auth-privacy

Setting the SNMPv3 security level to authentication only:

switch(config)# snmpv3 security-level auth

Setting the SNMPv3 security level to no authentication and no privacy:

switch(config)# no snmpv3 security-level auth-privacy

Restoring the default SNMPv3 security level to authentication and privacy:

switch(config)# no snmpv3 security-level auth

Public

snmpv3 security-level 170

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

snmp-server agent-port

Syntax

snmp-server agent-port <PORT>

no snmp-server agent-port [<PORT>]

Description

Sets the UDP port number that the SNMP master agent uses to communicate. UDP port 161 is the default
port.

The no form of this command sets the SNMP master agent port to the default value.

Parameter

Description

Specifies the UDP port number that the SNMP master agent wil
l use. Range: 1 to 65535. Default: 161.

<PORT>

Examples

Setting the SNMP master agent port to 2000:

switch(config)# snmp-server agent-port 2000

Resetting the SNMP master agent port to the default value:

Public

snmp-server agent-port 171

switch(config-schedule)# no snmp-server agent-port 2000

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

snmp-server community view

Syntax

snmp-server community <STRING> [view <VIEW-NAME>]

no snmp-server community <STRING> [view <VIEW-NAME>]

Description

Associates an SNMP MIB view with the SNMP community.

The no form of this command removes the associated SNMP MIB view from the SNMP community.

Parameter

Description

<STRING>

<VIEW‐NAME>

Specifies the SNMPv1/SNMPv2c community string. Range: 1 to
32 printable ASCII characters, excluding space and question ma
rk.

Specifies the view name for the SNMP MIB view. Accepts a maxi
mum of 32 characters.

Public

snmp-server community view 172

Examples

Configuring the SNMPv1/SNMPv2c community:

switch(config)# snmp-server community my_community

switch(config-community)#
Adding SNMP MIB view to the SNMP community:

switch(config-community)# view name1

Removing SNMP MIB view from the SNMP community:

switch(config-community)# no view name1

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
config‐
community

Administrators or local user group members with execution righ
ts for this command.

snmp-server community

Syntax

snmp-server community <STRING>

no snmp-server community <STRING>

Description

Adds an SNMPv1/SNMPv2c community string. A community string is like a password that controls read/
write access to the SNMP agent. A network management program must supply this name when attempting

Public

snmp-server community 173

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

Specifies the ACL name. It supports a maximum of 64 characte
rs.

Public

snmp-server community 174

Description

Parameter

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

access-list ipv6 ipv6_acl

    10 deny any 6001::6 6000::1

Public

snmp-server community 175

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

snmp-server historical-counters-monitor

Syntax

snmp-server historical-counters-monitor

no snmp-server historical-counters-monitor

Description

Enables the Remote Network Monitoring agent (rmond) to start collecting historical interface statistics. The
no form of this command stops the historical interface statistics collection.

Public

snmp-server historical-counters-monitor 176

Example

Enabling the  rmond  agent to start historical interface statistics collection:

switch(config)# snmp-server historical-counters-monitor

Disabling the  rmond  agent to stop historical interface statistics collection:

switch(config)# no snmp-server historical-counters-monitor

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

snmp-server host

Syntax

snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community
<STRING>]

[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]

no snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION>

[community <STRING>]

[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]

snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community

<STRING>]

[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]

no snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community

<STRING>]

[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]

Public

snmp-server host 177

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

community <STRING>

Specifies the SNMPv3 user name to be used in the SNMP trap n
otifications.

Specifies the name of the community string to use when sendin
g trap notifications. Range: 1 ‐ 32 printable ASCII characters,
excluding space and question mark. Default: public.

Specifies the UDP port on which notifications are sent. Range: 1
‐ 65535. Default: 162.

Public

snmp-server host 178

Parameter

<UDP‐PORT>

<VRF‐NAME>

Description

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
•  vsx

Examples

switch(config)# snmp-server host 10.10.10.10 trap version v1

switch(config)# no snmp-server host 10.10.10.10 trap version v1

Public

snmp-server host 179

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

switch(config)# no snmp-server host a:b::c:d inform version v2c community

public

switch(config)# snmp-server host 10.10.10.10 inform version v2c community

public port 5000

switch(config)# no snmp-server host 10.10.10.10 inform version v2c

community public port 5000

Public

snmp-server host 180

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

notification-type bgp fan interface power-ethernet

switch(config)# no snmp-server host a:b::c:d inform version v3 user Admin

notification-type bgp interface

switch(config)# snmp-server host a:b::c:d inform version v3 user Admin

notification-type ?

  aaa-server      Sends AAA notifications.

  alarm           Sends Alarm notifications.

  bgp             Sends Border Gateway Protocol (BGP) state change

Public

snmp-server host 181

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

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

Public

snmp-server host 182

snmp-server system-contact

Syntax

snmp-server system-contact <INFO>

no snmp-server system-contact [<INFO>]

Description

Sets SNMP contact information.

The no form of this command removes the SNMP contact information.

Parameter

Description

Specifies SNMP contact information. Range: 1 to 128 printable
ASCII characters, except for question mark (?).

<INFO>

Examples

Defines SNMP contact information to be John Smith, Lab Admin:

switch(config)# snmp-server system-contact John Smith, Lab Admin

Removes SNMP contact information:

switch(config)# no snmp-server system-contact

Command History

Release

Modification

10.07 or earlier

‐‐

Public

snmp-server system-contact 183

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

snmp-server system-description

Syntax

snmp-server system-description <DESCRIPTION>

no snmp-server system-description

Description

Sets the SNMP system description.

The no form of this command removes the SNMP system description.

Parameter

Description

<DESCRIPTION>

Specifies the SNMP system description. Typical content to inclu
de would be the full name and version of the following:

•  Hardware type of the system
•  Software operating system
•  Networking software

Range: 1 to 64 printable ASCII characters, except for the questi
on mark (?).

Examples

Defines the SNMP system description to be mainSwitch:

switch(config)# snmp-server system-description mainSwitch

Removes the SNMP system description:

switch(config)# no snmp-server system-description mainSwitch

Public

snmp-server system-description 184

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

snmp-server system-location

Syntax

snmp-server system-location <INFO>

no snmp-server system-location

Description

Sets the SNMP location information.

The no form of this command removes the SNMP location information.

Parameter

Description

Specifies the SNMP location information. Range: 1 to 128 prin
table ASCII characters, except for the question mark (?).

<INFO>

Examples

Defines the SNMP location information to be Main Lab:

switch(config)# snmp-server system-location Main Lab

Removes the SNMP location information:

Public

snmp-server system-location 185

switch(config)# no snmp-server system-location

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

snmp-server trap-source interface vrf

Syntax

snmp-server trap-source {interface <IF-NAME> | <IPv4-Address> | <IPv6-

Address>} [vrf <VRF-NAME>]

no snmp-server trap-source {interface <IF-NAME> | <IPv4-Address> | <IPv6-

Address>} [vrf <VRF-NAME>]

Description

Configures SNMP trap source interface or IP address for a VRF.

The no form of this command removes the SNMP trap-source configuration for a VRF.

Parameter

Description

<IF‐NAME>

Specifies the source interface name. Interface name can be phys
ical interface, loopback interface, LAG interface, or VLAN interfa
ce.

Specifies the IPv4 address of source interface for the SNMP tra
p.

Public

snmp-server trap-source interface vrf 186

Parameter

<IPv4‐Address>

Description

Specifies the IPv6 address of source interface for the SNMP tra
p.

Specifies the name of a VRF associated to the source interface
for the SNMP trap.

<IPv6‐Address>

<VRF‐NAME>

Examples

Configuring SNMP trap source interface for a VRF.

switch(config)# snmp-server trap-source interface 1/1/12 vrf sample

switch(config)# snmp-server trap-source interface loopback10 vrf sample

switch(config)# snmp-server trap-source interface vlan23 vrf sample

Configuring SNMP trap source IP address for a VRF.

switch(config)# snmp-server trap-source 10.0.0.1 vrf red

switch(config)# snmp-server trap-source 1001::1 vrf red

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

snmp-server trap-source interface vrf 187

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

Command History

Release

Modification

10.07 or earlier

‐‐

Public

snmp-server vrf 188

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

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

Specifies the view name for the SNMP MIB view. Accepts a maxi
mum of 32 characters.

<USER‐NAME>

<VIEWNAME>

Examples

Adding a user in the existing SNMP MIB view:

switch(config)# snmpv3 user nw-admin view my-nw-view

Removing the user from the SNMP MIB view:

switch(config)# no snmpv3 user nw-admin view my-nw-view

Attaching unconfigured or unknown SNMP view to an SNMPv3 user:

Public

snmpv3 user view 189

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

Description

Creates an SNMPv3 user and adds it to an SNMPv3 context. The SNMPv3 security level (set with command
snmpv3 security-level) determines which users are allowed to authenticate.

The no form of this command removes the specified SNMPv3 user.

NOTE
When updating the authentication protocols and privacy protocols for the
existing SNMPv3 users, you must also update the access level. Otherwise, the
access level will be set to read-only.

Public

snmpv3 user 190

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
ntable ASCII characters. Ciphertext is used when copying user c
onfiguration settings between switches.

NOTE

Public

snmpv3 user 191

Parameter

Description

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

switch(config)# snmpv3 user Admin2 auth md5 auth-pass
Enter the authentication password: ********
Re-Enter the authentication password: ********

Configure the privacy protocol (y/n)? y

Enter the privacy protocol (aes/des)? aes

Public

snmpv3 user 192

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

snmpv3 user 193

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

snmp-server response-source

Syntax

snmp-server response-source {interface <IF-NAME> | <IPv4-ADDRESS> | <IPv6-

ADDRESS>} [vrf <VRF-NAME>]

no snmp-server response-source {interface <IF-NAME | <IPv4-ADDRESS> | <IPv6-

ADDRESS>} [vrf <VRF-NAME>]

Description

Configures the source interface or IP address for sending SNMP responses. Each SNMP can independently
have its own unique response source IP address.

Public

snmp-server response-source 194

The no form of this command removes the source interface name or IP address for sending SNMP
responses.

NOTE

•

It is recommended to use the loopback interface or ip address of the
loopback interface as the response source. If a device does not support a
loopback interface, then configure SVI interface or SVI IP address as the
response source.

•  The active gateway IP address cannot be configured as the response source.

•

It is recommended to limit the maximum number of response source to five.

•  The interface used for the response source should be in the up state. If the

interface is down, the default source IP will be used.

•  The use of udp6 is mandatory for IPv6 SNMP operations. For example,

you can use the following syntax: snmpwalk -v2c -c public -m ALL udp6:
[2100::2] .1.3.6.1.2.1.1.

Parameter

Description

interface <IF‐NAME>

Specifies the source interface name. The interface can be a p
hysical interface, loopback interface, or VLAN interface.

<IPv4‐ADDRESS>

<IPv6‐ADDRESS>

vrf <VRF‐NAME>

Specifies the IPv4 address of the source interface for the SNMP
response.

Specifies the IPv6 address of the source interface for the SNMP
response.

Specifies the VRF name associated to the source interface for t
he SNMP response.

Examples

Configuring a response source for the interface 1/1/12:

switch(config)# snmp-server response-source interface 1/1/12 vrf red

Public

snmp-server response-source 195

Configuring a response source for interface loopback10:

switch(config)# snmp-server response-source interface loopback10 vrf red

Configuring a response source for the IPv4 address 10.0.0.1:

switch(config)# snmp-server response-source 10.0.0.1 vrf sample

Configuring a response source for the IPv6 address 2001::1:

switch(config)# snmp-server response-source 2001::1 vrf default

Command History

Release

10.13

10.10

Modification

Added support for IPv6 address.

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

snmp-server snmpv3-only

Syntax

snmp-server snmpv3-only

no snmp-server snmpv3-only

Description

Accepts SNMPv3 messages only, SNMPv1 and SNMPv2c will be disabled. By default SNMPv1, SNMPv2c and
SNMPv3 will all be enabled.

The no form of this command restores the default setting and reenables SNMPv1 and SNMPv2c .

Public

snmp-server snmpv3-only 196

Examples
Configuring SNMPv3 messages only, and disabling SNMPv1 and SNMPv2c:
switch(config)# snmp-server snmpv3-only

Command History
Release Modification
10.10 Command introduced
Command Information
| Platforms | Command context | Authority |     |     |
| --------- | --------------- | --------- | --- | --- |
All platforms config Administrators or local user group members with execution righ
ts for this command.

snmp-server trap
Syntax
snmp-server trap {cpu-utilization | memory-utilization | rmon-events}
no snmp-server trap {cpu-utilization | memory-utilization | rmon-events}
Description
Enables the SNMP traps. The SNMP traps are enabled by default.
The no form of this command disables the SNMP traps.
| Parameter       |     | Description                        |     |     |
| --------------- | --- | ---------------------------------- | --- | --- |
| cpu‐utilization |     | Enables the CPU utilization traps. |     |     |
Enables the memory utilization traps.
memory‐utilization
| rmon‐events |        | Enables the RMON event traps. |                  |     |
| ----------- | ------ | ----------------------------- | ---------------- | --- |
|             | Public |                               | snmp-server trap | 197 |

Examples

Enabling the SNMP traps:

switch(config)# snmp-server trap cpu-utilization

switch(config)# snmp-server trap memory-utilization

switch(config)# snmp-server trap rmon-events

Disabling the SNMP traps:

switch(config)# no snmp-server trap cpu-utilization

switch(config)# no snmp-server trap memory-utilization

switch(config)# no snmp-server trap rmon-events

Displaying the SNMP trap configuration:

switch(config)# show running-config all | inc snmp

snmp-server trap rmon-events

snmp-server trap cpu-utilization

snmp-server trap memory-utilization
Displaying CPU and Memory usage:

switch(config)# show system

Hostname           : XXXX

System Description : XX.10.07.0001CI

System Contact     :

System Location    :

Vendor             : Aruba

Product Name       : JLXXXX XXXX Base Chassis/3xFT/18xFans/Cbl Mgr/X462

Bundle

Chassis Serial Nbr : SG6ZOO9068

Base MAC Address   : f40343-806400

AOS-CX Version : XX.10.07.0001CI

Time Zone          : UTC

Up Time            : 8 minutes
CPU Util (%)       : 1

Memory Usage (%)   : 10

Command History

Release

Modification

10.07 or earlier

‐‐

Public

snmp-server trap 198

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

snmp-server trap aaa-server-reachability-stat
us

Syntax

snmp-server trap aaa-server-reachability-status

no snmp-server trap aaa-server-reachability-status

Description

Enables the SNMP trap for AAA server status. When enabled, traps are sent whenever AAA server (RADIUS,
TACACS) status changes from reachable to unreachable and vice versa.

The no form of this command disables sending SNMP trap for AAA server status.

Examples

Enabling the SNMP trap for AAA server status:

switch(config)# snmp-server trap aaa-server-reachability-status

Disabling the SNMP trap for AAA server status:

switch(config)# no snmp-server trap aaa-server-reachability-status

Command History

Release

10.10

Modification

Command introduced on 4100i, 6000, 6100, 8100, 8320, 8325, 8360, 8400, 9
300, and 10000 switches.

Public

snmp-server trap aaa-server-reachability-status 199

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

snmp-server trap configuration-changes

Syntax

snmp-server trap configuration-changes

no snmp-server trap configuration-changes

Description

Enables sending SNMP traps whenever the configuration changes. Configuration trap generation is disabled
by default.

The no form of this command disables sending SNMP traps for configuration changes.

Parameter

Description

configuration‐changes

Specifies SNMP traps for configuration changes.

Examples

Enabling the SNMP traps for configuration changes:

switch(config)# snmp-server trap configuration-changes

Disabling the SNMP traps for configuration changes:

switch(config)# no snmp-server trap configuration-changes

Command History

Release

10.10

Modification

Command introduced

Public

snmp-server trap configuration-changes 200

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

snmp-server trap mac-notify

Syntax

snmp-server trap mac-notify

no snmp-server trap mac-notify

Description

Enables the MAC notification traps within the SNMP module at a global level. When enabled, traps are sent
for interfaces that are configured for MAC notification events.

The no form of this command disables sending MAC notification traps at a global level. When disabled,
existing mac-notify interface configuration is preserved but MAC notification events on configured
interfaces will not cause SNMP traps to be transmitted.

Examples

Enabling the SNMP MAC notification feature in the system globally:

switch(config)# snmp-server trap mac-notify

Disabling the SNMP MAC notification feature in the system globally:

switch(config)# no snmp-server trap mac-notify

Command History

Release

10.08

Modification

Command introduced

Public

snmp-server trap mac-notify 201

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

snmp-server trap port-security

Syntax

snmp-server trap port-security

no snmp-server trap port-security

Description

Enables SNMP port-security violation traps on the system. Port-security violation traps are enabled by
default.

The no form of this command disables the SNMP port-security violation traps on the system.

Parameter

port‐security

Examples

Description

Specifies SNMP traps for port‐security.

Enabling the SNMP port-security violation traps on the system:

switch(config)# snmp-server trap port-security

Disabling the SNMP port-security violation traps on the system:

switch(config)# no snmp-server trap port-security

Command History

Release

10.10

Modification

Command introduced

Public

snmp-server trap port-security 202

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

snmp-server trap snmp

Syntax

snmp-server trap snmp {authentication | coldstart | warmstart} [vrf

<VRF_NAME>]

no snmp-server trap snmp {authentication | coldstart | warmstart} [vrf

<VRF_NAME>]

Description

Enables SNMPv2 MIB traps. The SNMPv2 traps are disabled by default.

The no form of this command disables the SNMPv2 MIB traps.

SNMPv2 MIB supports the following traps:

•  authentication:  Authentication trap is sent when the SNMP server receives a protocol message

that is not properly authenticated.

•  coldstart:  A coldstart trap is sent when the switch reboots.

•  warmstart:  A warmstart trap is sent when there is a user intervention to enable or disable the

SNMP service on the switch.

NOTE

SNMPv2 Authentication traps do not support source IP configuration.

Parameter

Description

authentication

Enables the authentication traps.

coldstart

Enables the coldstart traps.

Public

snmp-server trap snmp 203

Parameter

warmstart

<VRF_NAME>

Description

Enables the warmstart traps.

Specifies the VRF name. Enables the SNMPv2 traps for a VRF.

Examples

Enabling all SNMPv2 traps:

switch(config)# snmp-server trap snmp

Enabling only SNMPv2 authentication traps:

switch(config)# snmp-server trap snmp authentication

Disabling all SNMP traps:

switch(config)# no snmp-server trap snmp

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

snmp-server trap vsx

Public

snmp-server trap vsx 204

Syntax

snmp-server trap vsx

no snmp-server trap vsx

Description

Enables sending the SNMP traps for VSX related events. VSX trap generation is disabled by default.

The no form of this command disables sending the SNMP traps for VSX related events.

The trap support is available for the following VSX events:

•

ISL up and down

•  KA up and down

•  MCLAG up and down

Parameter

vsx

Description

Specifies SNMP traps for VSX events.

Examples

Enabling the VSX traps:

switch(config)# snmp-server trap vsx

switch(config)# show vsx configuration trap

SNMP traps : Enabled
Disabling the VSX traps:

switch(config)# no snmp-server trap vsx

switch(config)# show vsx configuration trap

SNMP traps : Disabled

Command History

Release

Modification

10.07 or earlier

‐‐

Public

snmp-server trap vsx 205

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

snmp-server view

Syntax

snmp-server view <VIEWNAME>

            <OID_TREE> [<MASK>] <included/excluded>

no snmp-server view <VIEWNAME>

            <OID_TREE> [<MASK>] <included/excluded>

Description

Configures an SNMP MIB view.

The no form of this command removes the specified SNMP MIB view.

Parameter

Description

<VIEWNAME>

<OID_TREE>

<MASK>

Specifies the name of the SNMP MIB view. Supports up to a ma
ximum of 32 characters.

Specifies the OID tree to be included or excluded in SNMP MIB
view.

Specifies the OID mask value. The values must be in hexadecim
al character separated with : (colon).

Specifies the OID tree that is included in or excluded from the S
NMP MIB view.

Public

snmp-server view 206

Parameter

Description

<included/excluded>

Usage

You can configure a maximum of 50 SNMP MIB views. The following VTY message is displayed when the
configuration exceeds the maximum SNMP MIB views:

switch(config)# snmp-server view name51 1.3.6.1.2.1.1 fe:00 included

Configuration failed: Maximum allowed views are configured.

Examples

Configuring the SNMP MIB views:

switch(config)# snmp-server view name1 .1.3.6.1.2.1.2.2.1.1.1 FF:A0 included

switch(config)# snmp-server view name2 IF-MIB::ifindex included

switch(config)# snmp-server view name4 1.3.6.1.2.1.1 fe:00 included

Removing an SNMP MIB view:

switch(config)# no snmp-server view name4 1.3.6.1.2.1.1 fe:00 included

Command History

Release

10.10

Modification

Command introduced.

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

Public

Support and Other Resources 207

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

Accessing HPE Aruba Networking Support 208

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

Accessing Updates 209

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

See Also

Public

Regulatory Information 210