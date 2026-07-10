AOS-CX 10.18.xxxx Monitoring Guide (8400 Switch Series)

Published: May 2026

AOS-CX 10.18.xxxx Monitoring Guide (8400 Switch Series)

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

AOS-CX 10.18.xxxx Monitoring Guide (8400 Switch Se...

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
8
4
0
0

S
w
i
t
c
h

S
e
.
.
.

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX 10.18.xxxx Monitoring Guide (8400 Switch Se...

Table of contents

About this document..................................................................................................................................................................................7

Applicable products........................................................................................................................................................................7

Latest version available online.................................................................................................................................................7

Command syntax notation conventions.............................................................................................................................7

About the examples....................................................................................................................................................................... 8

Identifying switch ports and interfaces...............................................................................................................................9

Identifying modular switch components.........................................................................................................................10

Aruba 8400 switch series member, slot, and port notation..............................................................................................10

Monitoring hardware through visual observation..................................................................................................................12

Confirming normal operation of the switch by reading LEDs.............................................................................12

Detecting if the switch is not ready for a failover event........................................................................................ 14

Finding faulted components using the switch LEDs................................................................................................15

gRPC network management interface.......................................................................................................................................... 16

Boot commands..........................................................................................................................................................................................23

Boot commands.............................................................................................................................................................................23

boot fabric-module ........................................................................................................................................................ 24

boot line-module .............................................................................................................................................................25

boot management-module ........................................................................................................................................26

boot management-module (recovery console) .............................................................................................28

boot set-default ...............................................................................................................................................................30

boot system ........................................................................................................................................................................31

show boot-history .......................................................................................................................................................... 33

External storage......................................................................................................................................................................................... 38

External storage commands...................................................................................................................................................39

address ..................................................................................................................................................................................39

directory ...............................................................................................................................................................................41

disable ................................................................................................................................................................................... 42

enable .................................................................................................................................................................................... 43

external-storage ..............................................................................................................................................................44

password (external-storage) ....................................................................................................................................45

show external-storage ................................................................................................................................................. 46

show running-config external-storage ...............................................................................................................48

type .........................................................................................................................................................................................49

username ............................................................................................................................................................................. 50

Public

Table of contents 4

vrf .............................................................................................................................................................................................51

IP-SLA...............................................................................................................................................................................................................52

IP-SLA guidelines..........................................................................................................................................................................53

Limitations with VoIP SLAs.....................................................................................................................................................54

IP-SLA commands........................................................................................................................................................................ 54

http ..........................................................................................................................................................................................55

https ....................................................................................................................................................................................... 57

icmp-echo ............................................................................................................................................................................59

ip-sla .......................................................................................................................................................................................61

ip-sla responder ...............................................................................................................................................................62

show ip-sla all ................................................................................................................................................................... 64

show ip-sla responder ..................................................................................................................................................67

show ip-sla ..........................................................................................................................................................................69

start-test .............................................................................................................................................................................. 70

stop-test ...............................................................................................................................................................................71

tcp-connect ........................................................................................................................................................................ 72

udp-echo ..............................................................................................................................................................................74

udp-jitter-voip .................................................................................................................................................................. 76

vrf .............................................................................................................................................................................................78

Mirroring......................................................................................................................................................................................................... 79

Mirroring and sFlow.....................................................................................................................................................................81

Mirror statistics.............................................................................................................................................................................. 82

Classifier policies and mirroring sessions....................................................................................................................... 82

Mirroring commands...................................................................................................................................................................84

clear mirror ......................................................................................................................................................................... 84

comment .............................................................................................................................................................................. 85

copy tcpdump-pcap ...................................................................................................................................................... 87

copy tshark-pcap ............................................................................................................................................................ 88

destination cpu ................................................................................................................................................................ 89

destination interface .....................................................................................................................................................90

destination tunnel .......................................................................................................................................................... 92

diagnostic ............................................................................................................................................................................94

diag utilities tcpdump .................................................................................................................................................. 95

disable ................................................................................................................................................................................... 98

enable .................................................................................................................................................................................... 99

mirror session .................................................................................................................................................................101

show mirror ..................................................................................................................................................................... 102

source interface ............................................................................................................................................................ 105

Public

Table of contents 5

source vlan .......................................................................................................................................................................108

Monitoring a device using SNMP.................................................................................................................................................. 111

Breakout cable support.......................................................................................................................................................................111

Limitations with breakout cable support.....................................................................................................................111

Breakout cable support commands................................................................................................................................ 112

split ...................................................................................................................................................................................... 112

Aruba AirWave......................................................................................................................................................................................... 114

SNMP support and AirWave................................................................................................................................................115

Supported features with AirWave and the AOS-CX switch...............................................................................116

Configuring the AOS-CX switch to be monitored by AirWave........................................................................ 116

AirWave commands..................................................................................................................................................................117

logging ............................................................................................................................................................................... 118

snmp-server community ..........................................................................................................................................121

snmp-server host .........................................................................................................................................................124

snmp-server vrf ............................................................................................................................................................ 129

snmpv3 context ............................................................................................................................................................131

snmpv3 user ................................................................................................................................................................... 132

snmpv3 user view ...........................................................................................................................................136

Support and Other Resources.........................................................................................................................................................137

Accessing HPE Aruba Networking Support...............................................................................................................138

Accessing Updates....................................................................................................................................................................139

Warranty Information.............................................................................................................................................................. 139

Regulatory Information.......................................................................................................................................................... 140

Documentation Feedback.....................................................................................................................................................140

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
Identifying modular switch components

Applicable products

This document applies to the following products:

•  HPE Aruba Networking 8400 Switch Series (JL366A, JL363A, JL687A)

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
ke the example text in the previous column are to be
entered exactly as shown and are required unless en
closed in brackets ([ ]).

Public

About this document 7

Convention

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

About the examples

Examples in this document are representative and might not match your particular switch or environment.

Public

About the examples 8

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

On the HPE Aruba Networking 8400 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Specifies physical location of a module in the switch chassis.

◦  Management modules are on the front of the switch in slots 1/5 and 1/6.

◦  Line modules are on the front of the switch in slots 1/1 through 1/4, and 1/7 through 1/10.

•  port: Physical number of a port on a line module

Public

Identifying switch ports and interfaces 9

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

Identifying modular switch components

•  Power supplies are on the front of the switch behind the bezel above the management modules. Power

supplies are labeled in software in the format: member/power supply:

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

Aruba 8400 switch series member, slot, and port notation

The software notation for describing member, slot, and port information depends on the switch hardware.

The physical interfaces on the Aruba 8400 Switch Series use the format:

         member/slot/port

         member

Specifies the chassis number. In this release of the software, the value of member is always  1 .

         slot

Specifies physical location in the switch chassis.

Public

Identifying modular switch components 10

A
r
u
b
a

8
4
0
0

s
w
i
t
c
h

s
e
r
i
e
s

m
e
m
b
e
r
,

s
l
o
t
,

a
n
d

p
o
r
t

n
o
.
.
.

         port

Specifies the physical port on the module.

The slot numbers are unique to each type of component—in contrast to being unique within a chassis.

Line Modules and Management Modules

Line modules are on the front of the switch in slots 1/1 through 1/4 and 1/7 through 1/10.

The number of ports depend on the line module. Line module ports are labeled in software as port or
interface, depending on the context.

For example,  interface 1/1/1  is the logical interface associated with the physical interface member
1, slot 1, port 1.

Management modules are on the front of the switch in slots 1/5 and 1/6.

Figure 1. Aruba 8400 Switch Series line module and management module slots

Power supplies

Power supplies are on the front of the switch behind the bezel above the line modules and management
modules. Power supplies are labeled in software as Member/PSU: 1/1 through 1/4.

Public

Aruba 8400 switch series member, slot, and port no... 11

Fan trays

Fan trays are on the rear of the switch and are labeled in software as Member/Tray: 1/1 through 1/3.

Fans

Fans are on the rear of the switch in fan trays and are labeled in software as Member/Tray/Fan:

•  1/1/1 through 1/1/6

•  1/2/1 through 1/2/6

•  1/3/1 through 1/3/6

Fabric modules

Fabric modules are on the rear of the switch, behind the fan trays, in slots 1/1 through 1/3.

Rear display module

The rear display module is on the rear of the switch and is not labeled with a member or slot number.

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

Public

Monitoring hardware through visual observation 12

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
2.

•  Power

•  Health

Verify that the Health LEDs of all installed line modules are On Green.

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

Public

Confirming normal operation of the switch by readi... 13

7.  Verify that the standby management module is ready to take over as the active management module.

On the standby management module, verify the states of the following LEDs:

•  Health LED is On Green.

•  Management state standby (Stby) LED is On Green.

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

Public

Detecting if the switch is not ready for a failove... 14

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
•  The standby management state standby (Stby) LED is Off.

•  On the active management module in the Status Front Management Modules section, the LED for

the standby management module is Slow Flash Green.

3.  Detect if a fabric module is shut down or not present. If a fabric module is shut down or not present, the

LED states are as follows:

•  On the active management module, in the Status Rear section, the LED for the fabric module is Off.

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

Public

Finding faulted components using the switch LEDs 15

•  The Status Front area has LEDs for power supplies, line and fabric modules, and management

modules. The number on the LED indicates the slot number of the component.

•  The Status Rear area has LEDs for fabric modules and fan trays, with a single LED for all the fans in

the fan tray. The number on the LED represents the slot or bay number of the component.

4.  Use the number indicated by the LED that is flashing to locate the slot that contains the faulted

component.
The fabric modules are located behind the fan trays, and the fabric module number corresponds to the
fan tray number.

5.  At the front of the switch, on line modules, look for LEDs that are in the Slow Flash Orange state:

Module LEDs and Port LEDs indicate faults if their states are Slow Flash Orange.

gRPC network management interface

gRPC is a RPC framework developed by Google to create distributed systems. This protocol allows a client
running on one system to call the services defined in a remote server as a local server.

The gRPC Network Management Interface (gNMI) feature provides secure, high-performance, standards-
based network management and gRPC-based access to network device configuration and operational data.
Using industry-standard OpenConfig models, gNMI enables the building of modern network automation and
monitoring solutions.

gNMI is implemented as an HTTP/2 server supporting encrypted communication and role-based access
control. It allows network management systems to interact with the device for configuration and telemetry
using gRPC, supporting VRF-aware access and role-based control.

gNMI supports access over SVIs, loopback, and data ports.

gNMI allows for the following:

•  Streaming of real-time telemetry data from switches

•  Monitoring of interface statistics, system performance, and hardware health

•

Integration with modern network management platforms

•

Implementation of event-driven network automation

Refer to gNMI commands for information on enabling and configuring gNMI.

gNMI commands

crypto pki application gnmi certificate

Public

gRPC network management interface 16

Syntax

crypto pki application gnmi certificate <CERT-NAME>

Description

Configures a certificate for the gNMI server. local-cert is used by default. For more details, refer to the
[Public Key Infrastructure guide] (./Functionality_Guide_PKI.md)

Parameter

Description

Specifies the certificate name.

<CERT‐NAME>

Examples

Configure sign-cert for the gNMI server:

switch(config)# crypto pki application gnmi certificate sign-cert

Command History

Release

10.17

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8400

config

Administrators or local user group members with execution righ
ts for this command.

gnmi vrf

Syntax

gnmi vrf <VRF NAME>
no gnmi vrf <VRF NAME>

Public

gRPC network management interface 17

Description

Enables the gNMI server on a given VRF. gNMI can be enabled on multiple VRFs simultaneously.

NOTE

There is a maximum of 30 gNMI subscriptions per request and a maximum of
9 concurrent streams per switch. These are system-wide limits shared among all
authenticated users regardless of connection method (local or remote).

The no form of this command removes the configuration.

Disabling the gNMI server on a VRF immediately closes any active streams.

Parameter

Description

Specifies the VRF name.

<VRF NAME>

Examples

Enable the gNMI server on VRF mgmt, this allows access to the gNMI server from the OOBM port in the
"management VRF":

switch(config)# gnmi vrf mgmt

Removing the configuration of gNMI server on mgmt:

switch(config)# no gnmi vrf mgmt

Command History

Release

10.17

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8400

config

Administrators or local user group members with execution righ
ts for this command.

Public

gRPC network management interface 18

show gnmi

Syntax

show gnmi

Description

Displays the current gNMI configuration.

Examples

Display the current gNMI configuration:

switch(config)# show gmni

gNMI Configuration

----------------------------------------------------------

VRF                  : mgmt, default

Access mode          : read-only

Global stream limit  : 9

Command History

Release

10.17

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8400

config

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

diag-dump

Syntax

diag-dump gnmi basic

Description

Provides detailed service status information for gNMI and nginx-configurator daemon.

Examples

Showing feature information:

Public

gRPC network management interface 19

=========================================================================

[Start] Feature gnmi Time : Thu Jun 26 14:30:13 2025

=========================================================================

-------------------------------------------------------------------------

[Start] Daemon nginx-configurator

-------------------------------------------------------------------------

gNMI nginx VRF service status dump:

----------------------------------------------------------------------------

------

| VRF                              | LoadState    | ActiveState |

SubState        |

----------------------------------------------------------------------------

------

| VRF_2                            | loaded       | active      |

running         |

----------------------------------------------------------------------------

------

-------------------------------------------------------------------------

[End] Daemon nginx-configurator

-------------------------------------------------------------------------

=========================================================================

[End] Feature gnmi

=========================================================================

Diagnostic-dump captured for feature gnmi

Command History

Release

Modification

10.17.1000

Command introduced

Command Information

Platforms

Command context

Authority

8400

config

Administrators or local user group members with execution righ
ts for this command.

Public

gRPC network management interface 20

debug nginxconfigurator

Syntax

debug nginxconfigurator <all|gnmi> all severity <level>

Description

Enables nginx configurator and YANG resolver debug logs.

Examples

Enabling nginx configurator and YANG resolver debug logs:

switch# debug nginxconfigurator all severity debug

switch# debug yang all severity debug
Reviewing debug logs:

switch(config)# show debug buffer module nginxconfigurator

switch(config)# show debug buffer module yang-resolver

Command History

Release

Modification

10.17.1000

Command introduced

Command Information

Platforms

Command context

Authority

8400

config

Administrators or local user group members with execution righ
ts for this command.

show tech

Syntax

show tech gnmi

Description

Provides configuration, logs, and status information relevant to the gNMI HTTP/2 server.

Public

gRPC network management interface 21

Examples

Showing gNMI configuration information:

switch# show tech gnmi

====================================================

Show Tech executed on Thu Jun 26 14:30:33

2025========================================================================

================================

Begin] Feature gnmi

 ====================================================

 *********************************

Command : show gnmi

*********************************

gNMI Configuration

----------------------------

VRF                    : mgmt, default

Access mode            : read-only

Max streams globally   : 9

*********************************

Command : diag-dump gnmi basic

*********************************

=========================================================================

[Start] Feature gnmi Time : Thu Jun 26 14:30:33 2025

=========================================================================

-------------------------------------------------------------------------

[Start] Daemon nginx-configurator

-------------------------------------------------------------------------

gNMI nginx VRF service status dump:

----------------------------------------------------------------------------

------

| VRF                              | LoadState    | ActiveState |
SubState        |

----------------------------------------------------------------------------

------

| VRF_2                            | loaded       | active      |

running         |

----------------------------------------------------------------------------

------

-------------------------------------------------------------------------

[End] Daemon nginx-configurator

-------------------------------------------------------------------------

=========================================================================

Public

gRPC network management interface 22

[End] Feature gnmi

=========================================================================

Command History

Release

Modification

10.17.1000

Command introduced

Command Information

Platforms

Command context

Authority

8400

config

Administrators or local user group members with execution righ
ts for this command.

Boot commands

Subtopics

Boot commands

Boot commands

Subtopics

boot fabric-module
boot line-module
boot management-module
boot management-module (recovery console)
boot set-default
boot system
show boot-history

Public

Boot commands 23

boot fabric-module

Syntax

boot fabric-module <SLOT-ID>

Description

Reboots the specified fabric module.

Parameter

Description

Specifies the member and slot of the module in the format me
mber/slot. For example, to specify the module in member 1 slot
3, enter 1/3.

<SLOT‐ID>

Usage

The boot fabric-module command reboots the specified fabric module. Traffic performance is affected while
the module is down.

If the specified module is the only fabric module in an up state, rebooting that module stops traffic switching
between line modules and the line modules power down. The line modules power up when one fabric module
returns to an up state.

This command is valid for fabric modules only.

Examples

Rebooting the fabric module in slot 1/3 when auto-confirm is not enabled:

switch# boot fabric-module 1/3

This command will reboot the specified fabric module.  Traffic performance

may

be affected while the module is down.  Rebooting the last fabric module will

stop traffic switching between line modules.

Do you want to continue (y/n)? y

switch#
Rebooting the fabric module in slot 1/1 when auto-confirm is enabled:

switch# boot fabric-module 1/3

This command will reboot the specified fabric module.  Traffic performance
may

be affected while the module is down.  Rebooting the last fabric module will

stop traffic switching between line modules.

Public

boot fabric-module 24

Do you want to continue (y/n) y (auto-confirm)

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

8400

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

boot line-module

Syntax

boot line-module <SLOT-ID>

Description

Reboots the specified line module.

Parameter

Description

Specifies the member and slot of the module in the format me
mber/slot. For example, to specify the module in member 1 slot
3, enter 1/3.

<SLOT‐ID>

Usage

Reboots the specified line module. Any traffic for the switch passing through the affected module (SSH,
TELNET, and SNMP) is interrupted. It can take up to 2 minutes to reboot the module. During that time, you
can monitor progress by viewing the event log.

This command is valid for line modules only.

Public

boot line-module 25

Examples

Reloading the module in slot 1/1:

switch# boot line-module 1/1

This command will reboot the specified line module and interfaces on this

module will not send or receive packets while the module is down. Any

traffic passing through the line module will be interrupted. Management

sessions connected through the line module will be affected. It might take

up to 2 minutes to complete rebooting the module. During that time, you can

monitor progress by viewing the event log.

Do you want to continue (y/n)? y

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

8400

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

boot management-module

Syntax

boot management-module {active | standby | <SLOT-ID>}

Description

Reboots the specified management module. Choose the management module to reboot by role (active or
standby) or by slot number.

Parameter

Description

Selects the active management module.

Public

boot management-module 26

Parameter

active

standby

<SLOT‐ID>

Usage

Description

Selects the standby management module.

Specifies the member and slot of the management module in th
e format member/slot. For example, to specify the module in m
ember 1 slot 5, enter 1/5.

This command reboots a single management module in a chassis. Choose the management module to reboot
by role (active or standby) or by slot number.

You can use the show images command to show information about the primary and secondary system
images.

If you reboot the active management module and the standby management module is available, the active
management module reboots and the standby management module becomes the active management
module.

If you reboot the active management module and the standby management module is not available, you are
warned, you are prompted to save the configuration, and you are prompted to confirm the operation.

If you reboot the standby management module, the standby management module reboots and remains the
standby management module.

If you attempt to reboot a management module that is not available, the boot command is aborted.

Saving the configuration is not required. However, if you attempt to save the configuration and there is an
error during the save operation, the boot command is aborted.

NOTE
Hewlett Packard Enterprise recommends that you use the boot management-
module command instead of pressing the module reset button to reboot
a management module because if you are rebooting the only available
management module, the boot management-module command enables you to
save the configuration, cancel the reboot, or both.

Examples

Rebooting the active management module when the standby management module is available:

switch# boot management-module active

The management-module in slot 1/5 is going down for reboot now.

Public

boot management-module 27

Rebooting the active management module when the standby management module is not available:

switch# boot management-module 1/5

The management module in slot 1/5 is currently active and no

standby management module was found.

This will reboot the entire switch.

Do you want to save the current configuration (y/n)? n

This will reboot the entire switch and render it unavailable

until the process is complete.

Continue (y/n)? y

The system is going down for reboot.

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

boot management-module (recovery console)

Syntax

boot management-module {local|remote}

Description

Reboots the specified management module by specified location (local or remote).

Parameter

Description

Reboots the local management module.

<local>

Public

boot management-module (recovery console) 28

Parameter

Description

Reboots the remote management module.

<remote>

Usage

This command reboots a single management module in a chassis. Choose the management module to reboot
by role (active or standby) or by slot number.

You can use the show images command to show information about the primary and secondary system
images.

If you reboot the active management module and the standby management module is available, the active
management module reboots and the standby management module becomes the active management
module.

If you reboot the active management module and the standby management module is not available, you are
warned, you are prompted to save the configuration, and you are prompted to confirm the operation.

If you reboot the standby management module, the standby management module reboots and remains the
standby management module.

If you attempt to reboot a management module that is not available, the boot command is aborted.

Saving the configuration is not required. However, if you attempt to save the configuration and there is an
error during the save operation, the boot command is aborted.

NOTE
Hewlett Packard Enterprise recommends that you use the boot management-
module command instead of pressing the module reset button to reboot
a management module because if you are rebooting the only available
management module, the boot management-module command enables you to
save the configuration, cancel the reboot, or both.

Examples

Booting a remote management module:

switch# boot management-module remote

There is no other management module installed.

Aborting.

switch#

Public

boot management-module (recovery console) 29

Command History

Release

10.12

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

8400

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

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

boot set-default 30

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

boot system 31

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

boot system 32

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

For switches that support line modules (such as 8400 switch series) including the all parameter displays
information for the active management module and all available line modules.

NOTE
To view boot-history on a standby, the command must be sent on the conductor
console.

Public

show boot-history 33

Parameter

all

Description

Optional. Shows boot information for the active management m
odule. For switches that support line modules, including this pa
rameter displays information for and all available line modules.

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

show boot-history 34

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

show boot-history 35

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
Showing the boot history of the active management module and all line modules:

Public

show boot-history 36

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

show boot-history 37

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

External storage

The switch has limited capacity to store data, collected by switch features and protocols. You can provide
virtually unlimited storage capacity by adding user-supplied external storage volumes. Supported volume
types and storage protocols include: NFSv3, NFSv4, and SCP (sshfs).

One application of external storage is the saving and restoring of DHCP lease files over SCP or NFS network
attached storage systems. SCP file system protocol uses a user mode process to emulate a network file

Public

External storage 38

system. The key advantage is packet level encryption and simple configuration. The key disadvantage is
slow performance.

You can set up external storage volume credentials and then enable it. A storage management process acts
on your requests by enabling the storage volume using the requested storage protocol. You can disable the
external storage volume or set it up but leave it disable.

The feature maintains storage volume state. The states are: *disabled* (down), *connecting* (establishing
connection), *operational* (up), and *unaccessible* (unavailable).

If a storage volume is unavailable, the system attempts to reconnect periodically. Multiple volumes could
connect concurrently. If one connection times out the others can connect immediately.

The system supports server connection through data and management ports.

Data port support requires server IP address on a default VRF.

Once a storage volume is enabled, applications can use the volume to store retrieve and delete files and
directories.

Subtopics

External storage commands

External storage commands

Subtopics

address
directory
disable
enable
external-storage
password (external-storage)
show external-storage
show running-config external-storage
type
username
vrf

address

Public

External storage commands 39

Syntax

address {<IPV4-ADDR> | <IPV6-ADDR> | hostname <HOSTNAME>}

no address {<IPV4-ADDR> | <IPV6-ADDR> | hostname <HOSTNAME>}

Description

Specifies the NAS IP address or hostname.

The no form of this command deletes an IP address or hostname.

Parameter

Description

Specifies the NAS server IPv4 address, Global.

<IPV4‐ADDR>

<IPV6‐ADDR>

<HOSTNAME>

Examples

Specifies the IPv6 address of the NAS server.

Specifies the hostname of the NAS server. String.

Creating the logfiles storage volume with IP address 10.1.1.1:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# address 10.1.1.1

Deleting an external storage volume named logfiles:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# no address 10.1.1.1

Command History

Release

Modification

10.07 or earlier

‐‐

Public

address 40

Command Information

Platforms

Command context

Authority

8400

config‐
external‐
storage‐
<VOLUME‐NAME>

Administrators or local user group members with execution righ
ts for this command.

directory

Syntax

directory <DIRECTORY-NAME>

no directory <DIRECTORY-NAME>

Description

Selects an existing directory on the external storage volume.

The no form of this command clears a directory of an external storage volume.

Parameter

Description

Specifies the external storage directory for mapping the volume
.

<DIRECTORY‐NAME>

Examples

Creating a volume named logfiles that is mapped under /home on the server:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# directory /home

Clearing the directory /home:

Public

directory 41

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# no directory /home

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config‐
external‐
storage‐
<VOLUME‐NAME>

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

disable

Syntax

disable

no disable

Description

Disables the external storage volume.

The no form of this command enables the external storage volume. This is identical to the  enable
command.

Examples

Disabling a volume named logfiles:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# disable

Public

disable 42

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config‐
external‐
storage‐
<VOLUME‐NAME>

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

enable

Syntax

enable

no enable

Description

Enables the external storage volume.

The no form of this command disables the external storage volume. This is identical to the  disable
command.

Examples

Creating and then enabling a volume named logfiles:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# enable

Disables the external storage volume:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# disable

Public

enable 43

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config‐
external‐
storage‐
<VOLUME‐NAME>

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

external-storage

Syntax

external-storage <VOLUME-NAME>

no external-storage <VOLUME-NAME>

Description

Creates or updates an external storage volume.

The no form of this command deletes an external storage volume.

Examples

Creating the logfiles storage volume:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)#
Deleting the logfiles storage volume:

switch(config)# no external-storage logfiles

Public

external-storage 44

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config

Administrators or local user group members with execution righ
ts for this command.

password (external-storage)

Syntax

password [{plaintext | ciphertext} <PASSWORD>]

no password {plaintext | ciphertext} <PASSWORD>

Description

Sets the password for network attached storage server login.

The no form of this command clears the password for network attached storage server login.

Parameter

Description

{ciphertext | plaintext}

Selects the password format.

Specifies the password.

<PASSWORD>

NOTE

When the password is not provided on the com
mand line, plaintext password prompting occurs
upon pressing Enter. The entered password cha
racters are masked with asterisks.

Public

password (external-storage) 45

Examples

Creating a volume named logfiles with password Xj#9:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# password plaintext Xj#9

Creating a volume named bak1 with a prompted plaintext password:

switch(config)# external-storage bak1

switch(config-external-storage-bak1)# password

Enter the NAS server password: **********

Re-Enter the NAS server password: **********

Clearing the password for volume logfiles:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# no password plaintext Xj#9

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config‐
external‐
storage‐
<VOLUME‐NAME>

Administrators or local user group members with execution righ
ts for this command.

show external-storage

Syntax

show external-storage [<VOLUME-NAME>]

Public

show external-storage 46

Description

Shows external storage configuration and state for all volumes or for a specified volume.

Parameter

Description

Specifies the external storage volume name that the show com
mand will use.

<VOLUME‐NAME>

Examples

switch# show external-storage

----------------------------------------------------------------------------

--------

           Address      VRF      Username      Type       Directory

State

----------------------------------------------------------------------------

--------

nfsvol     10.1.1.1     nas      ---           NFSv3      /home

operational

nfsfiles   20.1.1.1     nas      netstorage    NFSv4      /netstor

disabled

scpdev     nasserver    nas      scpstor       SCP        /scp

unaccessible

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

Public

show external-storage 47

show running-config external-storage

Syntax

show running-config external-storage

Description

Shows the running configuration of the external storage.

Examples

switch# show running-config external-storage

external-storage nfsvol

      address   10.1.1.1

      vrf       nas

      type      nfsv4

      directoty /home

      enable

external-storage scpdev

      address   30.1.1.1

      vrf       nas

      username  switchuser

      password  ciphertext xxx

      type      scp

      directoty /home

      enable

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

Public

show running-config external-storage 48

type

Syntax

type {nfsv3 | nfsv4 | scp}

no type {nfsv3 | nfsv4 | scp}

Description

Sets the network attached storage access type for reaching the external storage volume.

The no form of this command deletes an external storage volume.

Parameter

Description

nfsv3

nfsv4

scp

Examples

Specifies the NFSv3 network access protocol.

Specifies the NFSv4 network access protocol.

Specifies the SCP network access protocol.

Creating the logfiles volume using NFSV4:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# type nfsv4

Clearing the external storage access type:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# no type nfsv4

Command History

Release

Modification

10.07 or earlier

‐‐

Public

type 49

Command Information

Platforms

Command context

Authority

8400

config‐
external‐
storage‐
<VOLUME‐NAME>

Administrators or local user group members with execution righ
ts for this command.

username

Syntax

username <USER-NAME>

no username <USER-NAME>

Description

Sets the username for logging in to a network attached storage server.

The no form of this command clears a username.

Parameter

Description

Specifies the username.

<USER‐NAME>

Examples

Creating a volume named logfiles with the user name nassuser:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# username nasuser

Clearing the user name nasuser from accessing the logfiles volume:

Public

username 50

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# no username nasuser

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config‐
external‐
storage‐
<VOLUME‐NAME>

Administrators or local user group members with execution righ
ts for this command.

vrf

Syntax

vrf <VRF-NAME>

no vrf <VRF-NAME>

Description

Setting a VRF to reach network attached storage.

The no form of this command clears access of a VRF to network attached storage.

Parameter

Description

Specifies the VRF name.

<VRF‐NAME>

Public

vrf 51

Examples

Creating the logfiles volume and setting a VRF named nas to access the network attached storage:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# vrf nas

Clearing access of a VRF named nas to the network attached storage:

switch(config)# external-storage logfiles

switch(config-external-storage-logfiles)# no vrf nas

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config‐
external‐
storage‐
<VOLUME‐NAME>

Administrators or local user group members with execution righ
ts for this command.

IP-SLA

The IP Service Level Agreement (IP-SLA) is a feature that enables the measuring of network performance
between two nodes in a network for different service level agreement parameters such as round-trip time
(RTT), one-way delay, jitter, reachability, packet loss, and voice quality scores. These two nodes can span
across area in access, distribution or core inside a LAN as well as across WAN between core to core or core to
Data Centre switches. This feature helps you measure the SLA for different protocols or applications such as
UDP echo, UDP jitter (for voice and video), TCP connect, HTTP, and ICMP echo. This guide provides details
for managing and monitoring different types of IP-SLAs.

Subtopics

IP-SLA guidelines

Public

IP-SLA 52

Limitations with VoIP SLAs
IP-SLA commands

IP-SLA guidelines

•  AOS-CX supports only SLA configuration through CLI and thresholds can be configured using NAE

agents using WebUI/REST.

•  AOS-CX supports only forever tests. On-demand tests are not supported.

•  Maximum sessions: IP-SLA source 500, IP-SLA responder 500.

•  NAE can effectively monitor a maximum of 300 parameters, reducing the maximum supported session

by 300.

•  NAE supports only syslog.

•  NAE agents must be triggered for each IP-SLA test on every switch.

•

If multiple IP addresses are received for a DNS query, DNS works with the first resolved IP.

•  When the DNS server IP is not explicitly configured, the system automatically uses the first DNS server

available in its default configuration.

•  The source interface/IP option is not applicable for SLAs configured on 'mgmt' VRF, as it has only one

interface.

•  A system time change because of NTP or a manual change causes an incorrect calculation.

•  There is no interoperability of UDP echo SLA between AOS-CX and FlexFabric switches.

•  Source IP and source port combination must be unique across SLA sessions in a same switch.

•  Do not use the same source port across the source and responder sessions in a switch.

•  The configuration of history results is limited to a maximum of 8 IP-SLA sessions. This means that you
can enable and store historical performance data, such as response times and availability, for up to 8
individual IP SLA sessions at any given time.

•  NTP synchronization is a must for SLA types involving one-way delay such as UDP jitter VoIP.

•

It is mandatory to set default CoPP to the maximum value when UDP jitter SLA is enabled. Otherwise,
100% packet loss can be seen and UDP jitter SLA probes will result in failure:
copp-policy default

     class hypertext priority 6 rate 50000 burst 64

Public

IP-SLA guidelines 53

     default-class priority 6 rate 99999 burst 9999

Limitations with VoIP SLAs

•  A maximum of 80 concurrent VoIP SLAs can be scheduled in a 20 second slot.

•  A single VoIP probe takes 20 seconds to complete.

•  The default and minimum probe interval for VoIP SLA is 120 seconds.

•  SLAs scheduled in the same slot, periodically sends 1000 probe packets for 120 seconds in 20 second

intervals.

•  Default 120 second probe interval is divided in to 6 slots of 20 seconds to avoid synchronization of all

configured VoIP SLAs sending probes at the same time.

•  SLAs started at the same time exceeding the concurrent limit of 80 must wait for the next 20 second

VoIP slot to open before moving to ‘running’ state.

•  The maximum number of VoIP SLAs supported is 80 X 6 slots = 480 SLAs.

•  SLAs exceeding 480 will continue to remain in the 'waiting for VoIP slot' until any slot is freed by

stopping the running SLA.

•  To avoid high RTT, a single switch with more than 20 SLAs should not have single responder SLA.

•  When IP is received dynamically (e.g. using DHCP) for interfaces other than management interface,

IPSLA source or responder has to be configured only using interface name.

IP-SLA commands

Subtopics

http
https
icmp-echo
ip-sla
ip-sla responder
show ip-sla all
show ip-sla responder
show ip-sla
start-test

Public

Limitations with VoIP SLAs 54

stop-test
tcp-connect
udp-echo
udp-jitter-voip
vrf

http

Syntax

http {get | raw} <URL> [history-interval <HISTORY-INTERVAL>] [cache

disable] [name-server {<IPV4-ADDR-DNS-SERVER>|<IPV6-ADDR-DNS-SERVER>}]

[probe-interval <PROBE-INTERVAL>] [proxy <PROXY-URL>] [source {<IPV4-ADDR>|

<IPV6-ADDR>|IFNAME>}] [source-port <SOURCE-PORT-NUM>] [version <VERSION-

NUMBER>] [http-raw-request <RAW-PAYLOAD>]

no http {get | raw} <URL> [history-interval <HISTORY-INTERVAL>] [cache

disable] [name-server {<IPV4-ADDR-DNS-SERVER>|<IPV6-ADDR-DNS-SERVER>}]

[probe-interval <PROBE-INTERVAL>] [proxy <PROXY-URL>] [source {<IPV4-ADDR>|

<IPV6-ADDR>|IFNAME>}] [source-port <SOURCE-PORT-NUM>] [version <VERSION-

NUMBER>] [http-raw-request <RAW-PAYLOAD>]

Description

Configures HTTP as the IP-SLA test mechanism. Requires destination URL and type of HTTP request
(raw/get).

The no version of this command disables HTTP as the IP-SLA test mechanism.

Parameter

{get | raw}

<URL>

Description

Selects HTTP request type as get or raw where the system will
generate or provide HTTP payload.

Specifies HTTP URL address of syntax http://<HOST NAME/IP
‐ADDRESS>:<PORT>/<PATH>.

history‐interval <HISTORY‐
INTERVAL>

Configures the history interval for the IP‐SLA. Set the history i
nterval to minimum of two times the probe‐interval for the SL
A. Range: 60 to 7200.

cache disable

Selects cache option for the HTTP server. By default the option
is enabled.

Public

http 55

Parameter

Description

name‐server {<IPV4‐ADDR‐
DNS‐SERVER>|<IPV6‐ADDR‐DNS‐
SERVER>}

probe‐interval <PROBE‐
INTERVAL>

Specifies the DNS server for destination hostname resolution.

Specifies the probe interval in seconds. Range: 30 to 604800.

proxy <PROXY‐URL>

Specifies the probe interval in seconds. Range: 30 to 604800.

source {<IPV4‐ADDR>|<IPV6‐
ADDR>|IFNAME>}

Selects the source, either an IPv4 address, an IPv6 address, or h
ostname for SLA probes.

source‐port <SOURCE‐PORT‐
NUM>

version <VERSION‐NUMBER>

Specifies the value of the source port for the IP‐SLA probes.

Specifies the source interface to use for sending IP‐SLA pro
bes.

http‐raw‐request <RAW‐
PAYLOAD>

Specifies the HTTP raw request. String.

Examples

Configuring HTTP get with parameters, including history interval:

switch(config)# ip-sla 1

switch(config-ipsla-1)# http get http://device.arubanetworks.com/root/

home.html history-interval 120 cache disable name-server 10.10.10.2 probe-

interval 30

Configuring HTTP raw with parameters:

switch(config-ipsla-1)# http raw http://2.2.2.2 http-raw-request

"GET /en/US/hmpgs/index.html HTTP/1.0\r\n\r\n"

Disabling HTTP get with parameters:

switch(config-ipsla-1)# no http get http://device.example.com/root/

home.html name-server 10.10.10.2 history-interval 120

Disabling HTTP raw with parameters:

Public

http 56

switch(config-ipsla-1)# no http raw http://device.example.com/root/

home.html http-raw-request "GET /en/US/hmpgs/index.html HTTP/1.0\r\n\r\n"

Command History

Release

10.16.1000

Modification

Added new parameter history‐interval. Also, IPv6 addresses can be used.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config‐ip‐sla‐
<IP‐SLA‐NAME>

Administrators or local user group members with execution righ
ts for this command.

https

Syntax

https {get | raw} <URL> [history-interval <HISTORY-INTERVAL>] [cache

disable] [name-server {<IPV4-ADDR-DNS-SERVER>|<IPV6-ADDR-DNS-SERVER>}]

[probe-interval <PROBE-INTERVAL>] [proxy <PROXY-URL>] [source {<IPV4-ADDR>|

<IPV6-ADDR>|IFNAME>}] [source-port <SOURCE-PORT-NUM>] [version <VERSION-

NUMBER>] [http-raw-request <RAW-PAYLOAD>]

no https {get | raw} <URL> [history-interval <HISTORY-INTERVAL>] [cache

disable] [name-server {<IPV4-ADDR-DNS-SERVER>|<IPV6-ADDR-DNS-SERVER>}]

[probe-interval <PROBE-INTERVAL>] [proxy <PROXY-URL>] [source {<IPV4-ADDR>|

<IPV6-ADDR>|IFNAME>}] [source-port <SOURCE-PORT-NUM>] [version <VERSION-

NUMBER>] [http-raw-request <RAW-PAYLOAD>]

Description

Configures HTTPS as the IP-SLA test mechanism. Requires destination URL and type of HTTPS request
(get/raw).

Public

https 57

The no form of this command removes the configuration.

NOTE

For HTTPS IP-SLA sessions, it is not required to install a certificate on the switch.

Parameter

{get | raw}

<URL>

Description

Selects HTTPS request type as get or raw where the system will
generate or provide HTTPS payload.

Specifies HTTPS URL address of syntax. https://<HOST NAME/
IP‐ADDRESS>:<PORT>/<PATH>.

history‐interval <HISTORY‐
INTERVAL>

Configures the history interval for the IP‐SLA. Set the history i
nterval to minimum of two times the probe‐interval for the SL
A. Range: 60 to 7200.

cache disable

Selects cache option for the HTTPS server. By default the optio
n is enabled.

name‐server {<IPV4‐ADDR‐
DNS‐SERVER>|<IPV6‐ADDR‐DNS‐
SERVER>}

probe‐interval <PROBE‐
INTERVAL>

Specifies the IPv4 address of DNS server.

Specifies the probe interval in seconds. Range: 30 to 604800.

proxy <PROXY‐URL>

Specifies the probe interval in seconds. Range: 30 to 604800.

source {<IPV4‐ADDR>|<IPV6‐
ADDR>|IFNAME>}

Selects the source, either an IPv4 address, an IPv6 address, or h
ostname for SLA probes.

source‐port <SOURCE‐PORT‐
NUM>

version <VERSION‐NUMBER>

Specifies the value of the source port for the IP‐SLA probes.

Specifies the source interface to use for sending IP‐SLA pro
bes.

https‐raw‐request <RAW‐
PAYLOAD>

Specifies the HTTPS raw request. String.

Examples

Configuring HTTPS get with parameters:

Public

https 58

switch(config-ipsla-1)# https get https://device.arubanetworks.com/root/

home.html

Configuring HTTPS raw with parameters:

switch(config-ipsla-1)# https raw https://device.arubanetworks.com/root/

home.html raw-request “GET /en/US/hmpgs/index.html”

Removing the HTTPS raw:

switch(config-ipsla-1)# no https raw https://device.arubanetworks.com/root/

home.html raw-request “GET /en/US/hmpgs/index.html”

Command History

Release

10.16.1000

Modification

Added new parameters history‐interval. Also, IPv6 addresses can be used.

10.12.1000

Command introduced.

Command Information

Platforms

Command context

Authority

8400

config‐ip‐sla‐
<IP‐SLA‐NAME>

Administrators or local user group members with execution righ
ts for this command.

icmp-echo

Syntax

icmp-echo {<DEST-IPV4-ADDR>|<DEST-IPV6-ADDR>|<HOSTNAME>} [history-interval

<HISTORY-INTERVAL>] [name-server {<IPV4-ADDR-DNS-SERVER>|<IPV6-ADDR-DNS-
SERVER>}[payload-size <PAYLOAD-SIZE>] [probe-interval <PROBE-INTERVAL>]

[source {<SOURCE-IPV4-ADDR>|<SOURCE-IPV6-ADDR>|<IFNAME>}] [timeout

<TIMEOUT>] [tos <TYPE-OF-SERVICE>]

no icmp-echo {<DEST-IPV4-ADDR>|<DEST-IPV6-ADDR>|<HOSTNAME>} [history-

Public

icmp-echo 59

interval <HISTORY-INTERVAL>][name-server {<IPV4-ADDR-DNS-SERVER>|<IPV6-

ADDR-DNS-SERVER>}[payload-size <PAYLOAD-SIZE>] [probe-interval <PROBE-

INTERVAL>] [source {<SOURCE-IPV4-ADDR>|<SOURCE-IPV6-ADDR>|<IFNAME>}]

[timeout <TIMEOUT>] [tos <TYPE-OF-SERVICE>]

Description

Configures ICMP echo as the IP-SLA test mechanism. Requires destination address for the IP-SLA test.

The no form of this command disables the ICMP echo as the IP-SLA test mechanism.

Parameter

Description

{<DEST‐IPV4‐ADDR>|<DEST‐
IPV6‐ADDR>|<HOSTNAME>}

Selects the destination, either an IPv4 address, an IPv6 address,
or hostname, for the IP‐SLA.

history‐interval <HISTORY‐
INTERVAL>

Specifies the history interval for the IP‐SLA. Set the history in
terval to minimum of two times the probe‐interval for the SL
A.

name‐server {<IPV4‐ADDR‐
DNS‐SERVER>|<IPV6‐ADDR‐DNS‐
SERVER>}

Range: 10 to 7200.

Specifies the DNS server for destination hostname resolution.

payload‐size <PAYLOAD‐SIZE>

Specifies the payload size of an SLA probe. Range: 0 to 1440.

probe‐interval <PROBE‐
INTERVAL>

source {<SOURCE‐IPV4‐
ADDR>|<SOURCE‐IPV6‐ADDR>|
<IFNAME>}

timeout <TIMEOUT>

Specifies the probe interval in seconds. Range: 5 to 604800.

Selects the source IPv4 or IPv6 address for SLA probes or the s
ource interface to use for sending IP‐SLA probes.

Specifies the interval before a probe is timed out. Range: 5 to 6
04800.

tos <TYPE‐OF‐SERVICE>

Specifies the type of serve value to be used in probe packets. R
ange: 0 to 255.

Examples

Configuring icmp-echo:

switch(config)# ip-sla test

switch(config-ip-sla-test)# icmp-echo 2.2.2.2 name-server 4.4.4.4 source

Public

icmp-echo 60

3.3.3.3

Configuring ICMP echo with several parameters, including history interval and timeout:

switch(config)# ip-sla test

switch(config-ip-sla-test)# icmp-echo 2.2.2.2 history-interval 160 name-

server 4.4.4.4  payload-size 400  probe-interval 80 source 3.3.3.3  timeout

20 tos 255

Command History

Release

10.16.1000

Modification

Added two new parameters history‐interval and timeout. Also, IPv6 address
es can be used.

10.07 or earlier

Command introduced.

Command Information

Platforms

Command context

Authority

8400

config‐ip‐sla‐
<IP‐SLA‐NAME>

Administrators or local user group members with execution righ
ts for this command.

ip-sla

Syntax

ip-sla <IP-SLA-NAME>

no ip-sla <IP-SLA-NAME>

Description

Creates an IP Service Level Agreement (SLA) profile and switches to the config-ip-sla context.

The no form of this command deletes an IP-SLA profile. By default, all profile use the default VRF (default).

Public

ip-sla 61

Parameter

Description

Specifies an IP‐SLA profile name. Length: 1 to 64 characters.

<IP‐SLA‐NAME>

Examples

Creating an IP-SLA:

switch(config)# ip-sla 1

switch(config-ip-sla-1)#
Deleting an IP-SLA:

switch(config)# no ip-sla 1

switch(config)#

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config

Administrators or local user group members with execution righ
ts for this command.

ip-sla responder

Syntax

ip-sla responder <SLA-NAME> (udp-echo | tcp-connect | udp-jitter-voip)
[<PORT-NUM>] [source {<SOURCE-IPV4-ADDR>|<SOURCE-IPV6-ADDR>|<IFNAME>}] [vrf
<VRF-NAME>] [ipv6]

no ip-sla responder <SLA-NAME> (udp-echo | tcp-connect | udp-jitter-voip)

Public

ip-sla responder 62

[<PORT-NUM>] [source {<SOURCE-IPV4-ADDR>|<SOURCE-IPV6-ADDR>|<IFNAME>}] [vrf

<VRF-NAME>] [ipv6]

Description

Selects the IP-SLA responder. The responder can be configured for udp-echo, tcp-connect, udp-jitter-voip
type. It requires the SLA name, SLA type, and port number as arguments.

The no form of this command removes the IP-SLA responder.

Parameter

Description

Specifies the IP‐SLA responder name. Length: 1 to 64 chara
cters.

<SLA‐NAME>

udp‐echo

tcp‐connect

Enables responder for udp‐echo probes.

Selects TCP connect as the IP‐SLA test mechanism.

udp‐jitter‐voip

Selects VOIP jitter as the IP‐SLA test mechanism.

Specifies the port number to listen for IP‐SLA probes. Range:
1 to 65535.

<PORT‐NUM>

source {<SOURCE‐IPV4‐
ADDR>|<SOURCE‐IPV6‐ADDR>|
<IFNAME>}

Selects the source IPv4 or IPv6 address for SLA probes or the s
ource interface to use for sending IP‐SLA probes.

vrf <VRF‐NAME>

Specifies the name of the VRF to use.

ipv6

Usage

Configures IPv6 responder. This keyword is required if an IPv6
address is being used by the source interface or VRF. By defaul
t, it will be considered as an IPv4 address.

The IPv6 keyword is required if an IPv6 address is being used by the source interface or VRF. Otherwise, by
default, it will be considered as an IPv4 address.

Examples

Configuring IP-SLA responder for udp-echo:

Public

ip-sla responder 63

switch(config)# ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2

Configuring IP-SLA responder with IPv6:

switch(config)#ip-sla responder SLA1 udp-echo 8000 source 1/1/1 ipv6

Configuring IP-SLA responder for udp-jitter-voip:

switch(config)#ip-sla responder SLA1 udp-jitter-voip 1025 vrf <VRF>

Disabling IP-SLA responder:

switch(config)# no ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2

Command History

Release

10.15

Modification

Added ipv6 parameter.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config

Administrators or local user group members with execution righ
ts for this command.

show ip-sla all

Syntax

show ip-sla all

Description

Shows all ip-sla source configuration and status.

Examples

Showing results for ip-sla all:

Public

show ip-sla all 64

switch# show ip-sla all

SLA Name                  : 2 (non-persistent)

Status                    : running

SLA Type                  : udp-echo

VRF                       : default

Source IP                 :

Source Interface          :

Domain Name Server        :

Payload Size              : 28

TOS                       : 0

Probe Interval(seconds)   : 60

History Interval(seconds) : 0

Timeout Interval(seconds) : 45

IP-SLA session status

IP-SLA Name                          : 2 (non-persistent)

IP-SLA Type                          : udp-echo

Destination Host Name/IP Address     : 10.1.1.2

Destination Port                     : 8888

Source IP Address/IFName             :

Source Port                          :

Status                               : running

IP-SLA Session Cumulative Counters

Total Probes Transmitted             : 10

Probes Timed-out                     : 10

Bind Error                           : 0

Destination Address Unreachable      : 0

DNS Resolution Failures              : 0

Reception Error                      : 0

Transmission Error                   : 0

Operational Status                   : down

IP-SLA Latest Probe Results

Last Probe Time                      :
Packets Sent                         : 1

Packets Received                     : 0

Packet Loss in Test                  : 100%

Minimum RTT(ms)                      :

Maximum RTT(ms)                      :

Average RTT(ms)                      :

DNS RTT(ms)                          :

----------------------------------------------------------------------------

--

SLA Name                  : echo-udp-sess2 (non-persistent)

Status                    : running

Public

show ip-sla all 65

SLA Type                  : udp-echo

VRF                       : default

Source IP                 :

Source Interface          :

Domain Name Server        :

Payload Size              : 28

TOS                       : 0

Probe Interval(seconds)   : 60

History Interval(seconds) : 0

Timeout Interval(seconds) : 45

IP-SLA session status

IP-SLA Name                          : echo-udp-sess2 (non-persistent)

IP-SLA Type                          : udp-echo

Destination Host Name/IP Address     : 100.1.1.2

Destination Port                     : 8888

Source IP Address/IFName             :

Source Port                          :

Status                               : running

IP-SLA Session Cumulative Counters

Total Probes Transmitted             : 10

Probes Timed-out                     : 0

Bind Error                           : 0

Destination Address Unreachable      : 0

DNS Resolution Failures              : 4

Reception Error                      : 0

Transmission Error                   : 0

Operational Status                   : Up

IP-SLA Latest Probe Results

Last Probe Time                      :

Packets Sent                         : 1

Packets Received                     : 1

Packet Loss in Test                  : 0.0000%
Minimum RTT(ms)                      :

Maximum RTT(ms)                      :

Average RTT(ms)                      :

DNS RTT(ms)                          :

----------------------------------------------------------------------------

--
Showing results for non-configured ip-sla all:

switch# show ip-sla all

IPSLA source is not configured

Public

show ip-sla all 66

Command History

Release

Modification

10.16.1000

Updated to display history interval.

10.12.1000

Updated to display https as an IP‐SLA type.

10.07 or earlier

Command introduced.

Command Information

Platforms

Command context

Authority

8400

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

show ip-sla responder

Syntax

show ip-sla responder <SLA-NAME> [initiator {<SOURCE-IPV4-ADDR>|<SOURCE-

IPV6-ADDR>}] [<SOURCE-PORT-NUM>] [results]

Description

Shows the given IP-SLA responder configuration and operation status.

Parameter

Description

Specifies the SLA name.

<SLA‐NAME>

initiator {<SOURCE‐IPV4‐
ADDR>|<SOURCE‐IPV6‐ADDR>}

<SOURCE‐PORT‐NUM>

Selects the source IPv4 or IPv6 address for SLA probes to use.

Configures the source port for the IP‐SLA test. Range: 1 to 65
535.

Public

show ip-sla responder 67

Parameter

results

Examples

Description

Displays the statistics for a given source IP and port.

Showing IP-SLA responder configuration:

switch# show ip-sla responder SLA3

    SLA Name            : SLA3

    IP-SLA Type         : Udp-echo

    VRF                 : Default

    Responder Port      : 8000

    Responder IP        : 2.2.2.3

    Responder Interface : 1/1/1

    Responder Status    : Running
Showing IP-SLA responder with initiator and results parameters:

switch# show ip-sla responder SLA1 initiator 2.2.2.1 8000 results

IP-SLA Type         : Udp-echo

VRF Name            : Default

Source IP           : 2.2.2.1

Source Port         : 8000

Responder Port      : 8888

Responder IP        : 2.2.2.3

Responder Interface :

Responder Status    : Running

Packets Received    : 2

Packets Sent        : 2

Command History

Release

Modification

10.16.1000

Added new parameters: initiator and results.

10.07 or earlier

Command introduced.

Command Information

Platforms

Command context

Authority

8400

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

Public

show ip-sla responder 68

show ip-sla

Syntax

show ip-sla <SLA-NAME> [{results |  history-results}]

Description

Shows the given IP-SLA source configuration and status.

Parameter

Description

Specifies the SLA name.

<SLA‐NAME>

results

Displays the statistics calculated for an SLA type.

history‐results

Displays the history statistics calculated for the SLA ID.

Examples

Showing results for ip-sla:

switch# show ip-sla xyz results

IP-SLA session status

IP-SLA Name                     : xyz

IP-SLA Type                     : tcp-connect

Destination Host Name/IP Address: 2.2.2.1

Destination Port                : 8888

Source IP Address/IFName        : 2.2.2.2

Source Port                     : 5555

Status                          : running

IP-SLA session cumulative counters

Total Probes Transmitted        : 1

Probes Timed-out                : 0

Bind Error                      : 0

Destination Address Unreachable : 0

DNS Resolution Failures         : 0

Reception Error                 : 0

Transmission Error              : 0

IP-SLA Latest Probe Results

Public

show ip-sla 69

Last Probe Time                 : 2018 Jul 13 02:00:35

Packets Sent                    : 1

Packets Received                : 1

Packet Loss in Test             : 0.0000%

Minimum RTT(ms)                 : 12

Maximum RTT(ms)                 : 12

Average RTT(ms)                 : 12

DNS RTT(ms)                     : 0

TCP RTT(ms)                     : 12
Showing history results for ip-sla:

switch# sh ip-sla abcd history-results

IP-SLA Name: abcd Session Details =============== IP-SLA Type : tcp-connect Status : running
Probe Interval(seconds) : 30 History Interval(seconds) : 600 Source Port : 3000 Destination Port :
4000 Source IP Address : 10.0.0.1 Dest Host Name/IP Address : 10.0.0.2 History Probe Results
===================== Packet Stats ------------ Probes Transmitted : 4 Packets Sent : 4 Packets
Received : 4 Loss Percentage : 0.0000% Error Stats ----------- Transmission Errors : 0 Reception Errors :
0 Bind Errors : 0 Dest. Unreachable : 0 Probes Timed-Out : 0 DNS Resolution Failures : 0 Probe RTT Stats
--------------- Min RTT(ms) : 0 Max RTT(ms) : 0 Avg RTT(ms) : 0 DNS RTT Stats ------------- Min RTT(ms) :
Max RTT(ms) : Avg RTT(ms) :

Command History

Release

10.16.1000

Modification

Added new parameter history‐results. Updated to display history interval.

10.12.1000

Updated to display https as an IP‐SLA type.

10.07 or earlier

Command introduced.

Command Information

Platforms

Command context

Authority

8400

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

start-test

Public

start-test 70

Syntax

start-test

Description

Starts the IP-SLA probes.

Examples

switch(config)# ip-sla test

switch(config-ip-sla-test)# start-test

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config‐ip‐sla‐
<IP‐SLA‐NAME>

Administrators or local user group members with execution righ
ts for this command.

stop-test

Syntax

stop-test

Description

Stops the IP-SLA probes.

Public

stop-test 71

Examples

switch(config)# ip-sla test

switch(config-ip-sla-test)# stop-test

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config‐ip‐sla‐
<IP‐SLA‐NAME>

Administrators or local user group members with execution righ
ts for this command.

tcp-connect

Syntax

tcp-connect {<DEST-IPV4-ADDR>|<DEST-IPV6-ADDR>|<HOSTNAME>} <DEST-PORT-NUM>

[history-interval <HISTORY-INTERVAL>] [name-server {<IPV4-ADDR-DNS-SERVER>|

<IPV6-ADDR-DNS-SERVER>} [probe-interval <PROBE-INTERVAL>] [source {<IPV4-

ADDR>|<IPV6-ADDR>|IFNAME>}] [source-port <PORT-NUM>]
no tcp-connect {<DEST-IPV4-ADDR>|<DEST-IPV6-ADDR>|<HOSTNAME>} <DEST-PORT-

NUM> [history-interval <HISTORY-INTERVAL>] [name-server {<IPV4-ADDR-DNS-

SERVER>|<IPV6-ADDR-DNS-SERVER>} [probe-interval <PROBE-INTERVAL>] [source

{<IPV4-ADDR>|<IPV6-ADDR>|IFNAME>}] [source-port <PORT-NUM>]

Description

Configures TCP connect as the IP-SLA test mechanism. Requires destination address/hostname and
destination port for the IP-SLA of tcp-connect IP-SLA type.

The no form of this command removes the the TCP connection.

Public

tcp-connect 72

Parameter

Description

{<DEST‐IPV4‐ADDR>|<DEST‐
IPV6‐ADDR>|<HOSTNAME>}

Selects the destination, either an IPv4 address, an IPv6 address,
or hostname, for the IP‐SLA.

Destination port for the IP‐SLA. Range: 1 to 65535.

<DEST‐PORT‐NUM>

history‐interval <HISTORY‐
INTERVAL>

Configures the history interval for the IP‐SLA. Set the history i
nterval to minimum of two times the probe‐interval for the SL
A. Range: 60 to 7200.

name‐server {<IPV4‐ADDR‐
DNS‐SERVER>|<IPV6‐ADDR‐DNS‐
SERVER>}

probe‐interval <PROBE‐
INTERVAL>

Specifies the DNS server for destination hostname resolution.

Probe interval in seconds. Range: 30 to 604800.

source {<IPV4‐ADDR>|<IPV6‐
ADDR>|IFNAME>}

Selects the source, either an IPv4 address, an IPv6 address, or h
ostname for SLA probes.

source‐port <PORT‐NUM>

Specifies the port for the IP‐SLA test.

Examples

Configuring TCP connect echo with parameters, including history interval:

switch(config)# ip-sla tcp

switch(config-ip-sla-tcp)# tcp-connect https://device.example.com 8080 name-

server 10.10.10.2 history-interval 180 source 1/1/1 source-port 6000

Disabling the TCP connect:

switch(config-ip-sla-tcp)# no tcp-connect 10:1::1:1 8080 source 1/1/1

source-port 6000

Command History

Release

10.16.1000

Modification

Added new parameters history‐interval. Also, IPv6 addresses can be used.

Public

tcp-connect 73

Release

Modification

10.07 or earlier

Command introduced.

Command Information

Platforms

Command context

Authority

8400

config‐ip‐sla‐
<IP‐SLA‐NAME>

Administrators or local user group members with execution righ
ts for this command.

udp-echo

Syntax

udp-echo {<DEST-IPV4-ADDR>|<DEST-IPV6-ADDR>|<HOSTNAME>} <DEST-PORT-NUM>

[history-interval <HISTORY-INTERVAL>] [name-server {<IPV4-ADDR-DNS-SERVER>|

<IPV6-ADDR-DNS-SERVER>} [payload-size <PAYLOAD-SIZE>] [probe-interval

<PROBE-INTERVAL>] [source {<IPV4-ADDR>|<IPV6-ADDR>|IFNAME>}] [source-port

<SOURCE-PORT-NUM>] [timeout <TIMEOUT>] [tos <TYPE-OF-SERVICE>]

no udp-echo {<DEST-IPV4-ADDR>|<DEST-IPV6-ADDR>|<HOSTNAME>} <DEST-PORT-NUM>

[history-interval <HISTORY-INTERVAL>] [name-server {<IPV4-ADDR-DNS-SERVER>|

<IPV6-ADDR-DNS-SERVER>} [payload-size <PAYLOAD-SIZE>] [probe-interval

<PROBE-INTERVAL>] [source {<IPV4-ADDR>|<IPV6-ADDR>|IFNAME>}] [source-port

<SOURCE-PORT-NUM>] [timeout <TIMEOUT>] [tos <TYPE-OF-SERVICE>]

Description

Configures UDP echo as the IP-SLA test mechanism. Requires destination address/hostname and
destination port number for the IP-SLA of udp-echo SLA type.

The no form of this command removes the UDP echo configuration.

Parameter

Description

{<DEST‐IPV4‐ADDR>|<DEST‐
IPV6‐ADDR>|<HOSTNAME>}

Selects the destination, either an IPv4 address, an IPv6 address,
or hostname, for the IP‐SLA.

Specifies the destination port for the IP‐SLA. Range: 1 to 655
35.

Public

udp-echo 74

Parameter

<DEST‐PORT‐NUM>

Description

history‐interval <HISTORY‐
INTERVAL>

Configures the history interval for the IP‐SLA. Set the history i
nterval to minimum of two times the probe‐interval for the SL
A. Range: 10 to 7200.

name‐server {<IPV4‐ADDR‐
DNS‐SERVER>|<IPV6‐ADDR‐DNS‐
SERVER>}

payload‐size <PAYLOAD‐
SIZE>

probe‐interval <PROBE‐
INTERVAL>

Specifies the DNS server for destination hostname resolution.

Specifies the payload size of an SLA probe. Range: 28 to 1440.

Specifies the probe interval in seconds. Range: 5 to 604800.

source {<IPV4‐ADDR>|<IPV6‐
ADDR>|IFNAME>}

Selects the source, either an IPv4 address, an IPv6 address, or h
ostname for SLA probes.

source‐port <SOURCE‐PORT‐
NUM>

Configures the source port for the IP‐SLA test. Range: 1 to 65
535.

timeout <TIMEOUT>

Specifies the interval before a probe is timed out. Range: 5 to 6
04800.

Specifies the type of service. Range: 0 to 255.

tos <TYPE‐OF‐
SERVICE>

Examples

Configuring UDP echo with parameters, including history interval and timeout:

switch(config-ipsla-1)# udp-echo https://device.example.com 4000 history-

interval 180 name-server 2.2.2.2 payload-size 100 probe-interval 90 source

4.4.4.4 source-port 8000 timeout 20

Removing UDP echo configuration:

switch(config-ipsla-1)# no udp-echo https://device.example.com 8080 history-
interval 160 name-server 10.10.10.2 payload-size 50 source 2.2.2.1 timeout
20

Public

udp-echo 75

Command History

Release

10.16.1000

Modification

Added two new parameters history‐interval and timeout. Also, IPv6 address
es can be used.

10.07 or earlier

Command introduced.

Command Information

Platforms

Command context

Authority

8400

config‐ip‐sla‐
<IP‐SLA‐NAME>

Administrators or local user group members with execution righ
ts for this command.

udp-jitter-voip

Syntax

udp-jitter-voip {<DEST-IPV4-ADDR>|<DEST-IPV6-ADDR>|<HOSTNAME>} <DEST-PORT-

NUM> [advantage-factor <ADVANTAGE-FACTOR>] [codec-type <CODEC-TYPE>]

[history-interval <HISTORY-INTERVAL>] [name-server {<IPV4-ADDR-DNS-SERVER>|

<IPV6-ADDR-DNS-SERVER>}] [probe-interval <PROBE-INTERVAL>] [source {<IPV4-

ADDR>|<IPV6-ADDR>|IFNAME>}] [source-port <SOURCE-PORT-NUM>] [tos <TYPE-OF-

SERVICE>]

no udp-jitter-voip {<DEST-IPV4-ADDR>|<DEST-IPV6-ADDR>|<HOSTNAME>} <DEST-

PORT-NUM> [advantage-factor <ADVANTAGE-FACTOR>] [codec-type <CODEC-TYPE>]

[history-interval <HISTORY-INTERVAL>] [name-server {<IPV4-ADDR-DNS-SERVER>|

<IPV6-ADDR-DNS-SERVER>}] [probe-interval <PROBE-INTERVAL>] [source {<IPV4-

ADDR>|<IPV6-ADDR>|IFNAME>}] [source-port <SOURCE-PORT-NUM>] [tos <TYPE-OF-

SERVICE>]

Description

Configure UDP jitter VoIP as the IP-SLA test mechanism. Requires destination address/hostname and source
address/interface for the IP-SLA of udp-jitter-voip IP-SLA type.

The no form of this command removes the UDP jitter VoIP configuration.

Public

udp-jitter-voip 76

Parameter

Description

{<DEST‐IPV4‐ADDR>|<DEST‐
IPV6‐ADDR>|<HOSTNAME>}

Selects the destination, either an IPv4 address, an IPv6 address,
or hostname, for the IP‐SLA.

Selects the port number for the IP‐SLA. Range: 1 to 65535.

<DEST‐PORT‐NUM>

advantage‐factor
<ADVANTAGE‐FACTOR>

Selects the value for the advantage factor. Default value is 0. Ra
nge: 0 to 20.

codec‐type <CODEC‐TYPE>

Selects the codec‐type for the Voip IP‐SLA test.

history‐interval <HISTORY‐
INTERVAL>

Configures the history interval for the IP‐SLA. Set the history i
nterval to minimum of two times the probe‐interval for the SL
A. Range: 240 to 7200.

name‐server {<IPV4‐ADDR‐
DNS‐SERVER>|<IPV6‐ADDR‐DNS‐
SERVER>}

probe‐interval <PROBE‐
INTERVAL>

Specifies the DNS server for destination hostname resolution.

Specifies the probe interval in seconds. Range: 120 to 604800.

source {<IPV4‐ADDR>|<IPV6‐
ADDR>|IFNAME>}

Selects the source, either an IPv4 address, an IPv6 address, or h
ostname for SLA probes.

source‐port <SOURCE‐PORT‐
NUM>

Specifies the value of source port for the IP‐SLA probes.

tos <TYPE‐OF‐SERVICE>

Specifies the type of service. Range: 0 to 255.

Examples

Configuring udp-jitter-voip with optional parameters, including history interval:

switch(config-ipsla-1)# udp-jitter-voip  https://device.arubanetworks.com
8080 advantage-factor 10 codec-type g711a history-interval 240 name-server
10.10.10.2 probe-interval 120 source 10.1.1.1 source-port 8888 tos 10

Configuring udp-jitter-voip with optional parameters:

Public

udp-jitter-voip 77

switch(config-ipsla-1)# udp-jitter-voip  2.2.2.2 8080 advantage-factor 10

codec-type g711a

Disabling udp-jitter-voip:

switch(config-ipsla-1)# no udp-jitter-voip  https://device.example.com 8080

advantage-factor 10 codec-type g711a name-server 10.10.10.2 probe-interval

120 source 10.1.1.1 source-port 8888 tos 10

Command History

Release

10.16.1000

Modification

Added new parameters history‐interval. Also, IPv6 addresses can be used.

10.07 or earlier

Command introduced.

Command Information

Platforms

Command context

Authority

8400

config‐ip‐sla‐
<IP‐SLA‐NAME>

Administrators or local user group members with execution righ
ts for this command.

vrf

Syntax

vrf <VRF-NAME>

no vrf [<VRF-NAME>]

Description

Configures the VRF on which the SLA will send or receive packets. By default, the default VRF is used.

The no form of the command removes VRF from SLA.

Public

vrf 78

Parameter

Description

Specifies a VRF name. Length: Default: default. If no VRF name i
s specified, then the default VRF name will be taken.

<VRF‐NAME>

Examples

switch(config-ip-sla-test)# vrf ipslasrc

switch(config-ip-sla-test)# no vrf

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config‐ip‐sla‐
<IP‐SLA‐NAME>

Administrators or local user group members with execution righ
ts for this command.

Mirroring

Mirroring allows you to replicate all traffic arriving and/or leaving the selected system interfaces. This data
can be used for collection or analysis.

The traffic replicated using mirroring can be sent to a separate interface on the same switch as the traffic
source for analysis or inspection. Such a collection of interfaces and settings is called a mirror session.

Public

Mirroring 79

A mirror session can be configured with many traffic sources but only a single output, or destination. In the
initial configuration, the mirror session is disabled. You have enable the feature to start the replication.

CAUTION

Care must be taken in choosing the number and rates of sources to avoid
over-saturating a session destination. A mirror session with multiple 10G sources
can overwhelm a single 10G destination and important data may be lost.

This version of AOS-CX support the following mirror capabilities:

•  Support for a VLAN as source for a mirror session

•  Ability for a given Mirror source in one session to act as source in another Mirror Session

•  Support for a Layer 2/bridged Link Aggregation Group (LAG) as Session destination (8xxx, 100xx

Switch series only)

•  Support for a Layer 3/Route-only Link Aggregation Group (LAG) as Session destination (8xxx, 100xx

Switch series only)

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

Public

Mirroring 80

to the CPU as part of the Mirror-to-CPU session, but they will not be counted under the Mirror-to-CPU CoPP
class. The Mirror-to-CPU CoPP class is specifically designed to manage dataplane traffic that is mirrored to
the CPU. Any control plane traffic mirrored to the CPU will bypass this class and be handled by the CoPP
class corresponding to its original purpose (e.g., OSPF, BGP, or ARP). Administrators should account for this
distinction when analyzing traffic mirrored to the CPU.

For example, if a mirror session is configured to mirror all traffic from a source interface to the CPU, and
that interface receives OSPF packets, the OSPF packets will be mirrored to the CPU. these packets will be
processed by the OSPF CoPP class, not the Mirror-to-CPU CoPP class.

Subtopics

Mirroring and sFlow
Mirror statistics
Classifier policies and mirroring sessions
Mirroring commands

Mirroring and sFlow

The mirroring feature (when mirroring received traffic) and the sFlow sampling feature both require the
receive (rx) capability of a given port. If both features are configured and enabled to use the receive
capability on the same port, only one of the features can perform its task.

This interaction does not affect transmit (tx) mirroring because sFlow does not use the transmit (tx)
capability of a port.

Behavior if sFlow is enabled and mirror enable is attempted

If sFlow is enabled on a port and a mirroring session specifies the same port as a source of received traffic
(the source is configured with a direction of  rx  or  both ):

•  The attempt to enable the mirroring session fails and an error is returned.

•  To enable the mirroring session, first you must disable sFlow on that port.

Behavior if mirroring is enabled and sFlow enable is attempted

If a mirroring session specifies a port as a source of received traffic (the source is configured with a direction
of  rx  or  both ), and you attempt to enable sFlow on the same port:

•  Mirroring on that port continues.

•  No error or warning message is returned when sFlow is enabled, but sFlow sampling on that port does

not occur.
When sFlow is enabled on a port but sampling is not occurring, the show sflow <INTERFACE-NAME>
command shows that sFlow is enabled but shows a value of 0 (zero) for the number of samples.

To activate sFlow sampling on that port, you must do the following:

Public

Mirroring and sFlow 81

1.  Disable the mirroring session on the port.

2.  Disable sFlow on the port.

3.  Enable sFlow on the port.

Behavior when the startup configuration has both sFlow and rx mirroring enabled on the same port

If the startup configuration has the same port configured with both sFlow enabled and as a source of
received traffic in an enabled mirroring session:

•  During a boot or management module failover operation, it is not possible to predict whether the receive

capability of the port will be assigned to the sFlow feature or to the mirroring feature.

•  To ensure that the feature that you want is used on a specific port, after the boot operation or

management module failover operation completes, disable both features on that port and then enable
the feature you want to use.

Mirror statistics

Mirror statistics are reset for a Mirror-to-CPU session when an interface is added or removed from a LAG
that is a source interface in the Mirror session and during a failover.

Mirror statistics are reset for a Mirror-to-CPU session on a failover.

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

Public

Mirror statistics 82

2.  Enabling the mirroring session.

3.  Configuring the Classifier Policy, specifying the mirroring session ID in the mirror action.

Results

Any subsequent configuration changes to either the enabled mirroring session or the classifier policy can
affect the behavior of the network monitoring that occurs. For examples, see Scenario 1 and Scenario 2.

Scenario 1

1.  Mirroring session 1 is configured with destination interface 1/1/10 and source interface 1/1/5 in the  bo

th  direction, then the session is enabled.

2.  Mirroring session 2 is configured with destination interface 1/1/20, then the session is enabled.

3.  Policy  Policy_2  is configured with a class matching OSPF traffic from any source IPv4 address to

any destination IPv4 address and an action of  mirror , specifying mirroring session 2.

4.  Policy_2  is applied to interface 1/1/5 in the inbound direction.

This sequence of actions creates a situation where the interface 1/1/5 is effectively configured as a source
for two separate enabled mirroring sessions. This configuration is not permitted if you attempt to configure
and enable the two mirroring sessions through the CLI. However, mirroring may occur for both sessions
because policies with mirror actions have priority over basic mirroring sessions.

In this example:

•  Because of  Policy_2 , all OSPF traffic ingressing interface 1/1/5 is mirrored to 1/1/20, which is the

destination interface of mirroring session 2.

•  After  Policy_2  is applied, and because of the mirroring session 1 is enabled, all non‐OSPF traffic
ingressing interface 1/1/5 is mirrored to 1/1/10, which is the destination interface of mirroring session
1.

•  Because  Policy_2  does not match egressing traffic, and because mirroring session 1 is enabled, all
traffic egressing interface 1/1/5 is mirrored to 1/1/10, which is the destination interface of mirroring
session 1.

Scenario 2

1.  Mirroring session 2 is configured with destination interface 1/1/20 and source interface 1/1/3, then the

session is enabled.

2.  Policy  Policy_2  is configured with a class matching OSPF traffic from any source IPv4 address to

any destination IPv4 address and an action of  mirror  specifying mirroring session 2.

Public

Classifier policies and mirroring sessions 83

3.  Policy_2  is applied to interface 1/1/5 in the inbound direction.

In this scenario, a single mirroring session is configured with a source interface and is configured as the
target of the mirror action of a policy applied to a different source interface. In this example, the destination
interface 1/1/20 receives traffic from interface 1/1/3 and from interface 1/1/5.

Mirroring commands

Subtopics

clear mirror
comment
copy tcpdump-pcap
copy tshark-pcap
destination cpu
destination interface
destination tunnel
diagnostic
diag utilities tcpdump
disable
enable
mirror session
show mirror
source interface
source vlan

clear mirror

Syntax

clear mirror [all | <SESSION-ID>]

Description

Clears the mirror statistics for all configured mirror sessions or a specified session

Parameter

all

Description

Specifies all configured sessions.

Public

Mirroring commands 84

Parameter

Description

Specifies a numeric identifier for the session. Range: 1 to 4

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

comment

Syntax

comment <COMMENT>

no comment

Description

Specifies a comment for the mirroring session.

The no form of this command removes the comment.

Public

comment 85

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

comment 86

copy tcpdump-pcap

Syntax

copy tcpdump-pcap <FILE-NAME> <REMOTE-URL>

Description

Saves packet capture files to external storage.

Parameter

Description

Specifies the packet capture file to save.

<FILE‐NAME>

<REMOTE‐URL>

Usage

Specifies the external storage to which the packet capture file w
ill be saved.

Only four files can be saved at any point on the switch. Packet capture files are not saved after a failover or
reboot. View a list of saved files using diag utilities list-files.

Examples

Saving my_capture_file.pcap to sftp://root@10.0.0.2/file.pcap:

switch# copy tcpdump-pcap my_capture_file.pcap sftp://root@10.0.0.2/

file.pcap

root@10.0.0.2's passowrd:
Connected to 10.0.0.2.

sftp > put my_capture_file.pcap file.pcap

Uploading my_capture_file.pcap to /root/file.pcap

my_capture_file.pcap                              100%   156   219.8KB/s

00:00

Copied successfuly.

Public

copy tcpdump-pcap 87

Command History

Release

10.08

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8400

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

copy tshark-pcap

Syntax

copy tshark-pcap <REMOTE-URL> [vrf <VRF-NAME>]

Description

Copies the tshark capture data to a file on a TFTP or SFTP server.

Parameter

Description

<REMOTE‐URL>

Specifies the capture file on a remote TFTP or SFTP server. The
URL syntax is:

{tftp:// | sftp://<USER>@} {<IP>|<HOST>} [:<PORT>] [;blocksi
ze=<SIZE>]/<FILE>

vrf <VRF‐NAME>

Specifies the name of a VRF. Default: default.

Example

Copying the capture data to a file on SFTP server 10.0.0.2:

switch# copy tshark-pcap sftp://root@10.0.0.2/file.pcap

root@10.0.0.2's password:

Connected to 10.0.0.2.

sftp> put packets.pcap file.pcap

Public

copy tshark-pcap 88

Uploading packets.pcap to /root/file.pcap

packets.pcap                                  100%  156   219.8KB/s   00:00

Copied successfully.

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

destination cpu

Syntax

destination cpu

no destination cpu

Description

The command causes the mirror session to transmit mirrored packets to the switch CPU. This destination
may be configured for multiple sessions, however only one such configured session may be active at a given
time.

The diagnostic utility Tshark may be used to view and capture packets transmitted to the CPU through
this route. Ctrl+C must be entered to terminate a Tshark capture session. More details can be found in the
Supportability Guide.

The no form of this command will immediately stops mirroring traffic to the CPU, but will not remove any
sources from the mirror configuration.

Examples

Configuring a mirror session with CPU as the destination.

switch# config

switch(config)# mirror session 1

Public

destination cpu 89

switch(config-mirror-1)# destination cpu

Removing the destination entirely.

switch(config-mirror-1)# no destination cpu

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

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

Public

destination interface 90

Parameter

Description

Specifies a LAG (link aggregation group) identifier.

<LAG‐NAME>

Usage

Supported mirror destinations: Layer 2 or Layer 3 Ethernet ports, LAGs, tunnel, or CPU as a Mirror
Destination. A port that is already a member of a LAG is not a valid mirror destination.

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

Switch

8400

10040

Destination interface limit per mirror session (4 possible sess
ions)

1

1

Command History

Release

Modification

10.07 or earlier

‐‐

Public

destination interface 91

Command Information

Platforms

Command context

Authority

All platforms

config‐mirror‐
<SESSION‐ID>

Administrators or local user group members with execution righ
ts for this command.

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

Multiple Mirror Sessions can be enabled with the same source/destination IP address pair if the span IDs are
different for sessions. By default it is assigned 0 if not specified.

ERSPAN is not supported leaving the switch by the OOB port. If VRF management is configured for an
ERSPAN session, the session will be in "mirror_err_tunnel_oob_port_not_supported" operation status.

ERSPAN is not supported leaving the switch encapsulated within another tunnel (e.g. GRE IPv4).
When the path to the destination IP address will leave via a tunnel, the session will be in
"tunnel_route_resolution_not_populated" operation status.

NOTE

The interface/LAG used to transmit ERSPAN packets should not be a source in
the same mirror session.

The no form of this command will cease the use of the tunnel and disable the session.

Public

destination tunnel 92

Parameter

Description

Specifies the tunnel address in IPv4 format (x.x.x.x), where x is
a decimal number from 0 to 255.

Specifies the source address in IPv4 format (x.x.x.x), where x is
a decimal number from 0 to 255.

Specifies the DSCP value to be carried within the DS field of E
RSPAN packet header. Range: 0 to 63. Default: 0.

Specifies a VRF name. Default: default.

Specifies the span ID for the ERSPAN session and during a fail
over. Range: 0 to 10.

<TUNNEL‐IPV4‐ADDR>

<SOURCE‐IPv4‐ADDR>

<DSCP‐VALUE>

<VRF‐NAME>

<SPAN‐ID>

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

Public

destination tunnel 93

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

8400

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

Public

diagnostic 94

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

diag utilities tcpdump

Syntax

diag utilities tcpdump [command <TEXT> | delete file <FILE-NAME> | list-

files |

  vrf <VRF-NAME> | count <COUNT-NUM> | proto <PROTO-NUM> | host-ip <IP-
ADDR> | source-ip
  <IP-ADDR> | destination-ip <IP-ADDR> | host-port <PORT> | source-port

<PORT> |

  destination-port <PORT> | verbosity <LEVEL> | print <DATA> | ethernet-

type <ETH-NUM>]

Public

diag utilities tcpdump 95

Description

Captures traffic received or transmitted over a network.

Parameter

Description

command <TEXT>

Captures packets based on a specified tcpdump command strin
g.

delete file <FILE‐NAME>

Deletes specified tcpdump list files.

list‐files

vrf <VRF‐NAME>

Lists all the tcpdump capture files saved on the device.

Captures packets on the specified VRF. If no VRF is named, the
default is used.

count <COUNT‐NUM>

Runs the tcpdump command until the specified number of pac
kets are captured. Range: 1‐2147483647.

proto <PROTO‐NUM>

Captures packets of a particular type based on IP protocol num
ber. Range: 0‐255.

host‐ip <IP‐ADDR>

Captures packets matching with the source or destination IP ad
dress.

source‐ip <IP‐ADDR>

Captures packets from the specified IP address.

destination‐ip <IP‐ADDR>

Captures packets sent to the specified IP address.

host‐port <PORT>

Captures packets matching with the source or destination port.

source‐port <PORT>

Captures packets from the specified IP port.

destination‐port <PORT>

Captures packets sent to the specified IP port.

verbosity <LEVEL>

Captures packets of the specified verbosity. Range: level1‐l
evel4. If no verbosity is specified, the default is level1.

print <DATA>

Captures the data of each packet. The maximum is 262144 by
tes

ethernet‐type <ETH‐NUM>

Captures packets based on the particular ethernet type. Range:
0‐65535.

Public

diag utilities tcpdump 96

Usage

•  When using the command option, the only traffic captured will be packets that have been mirrored to

the CPU.

•  When using the command option, command line sanitization is performed to prevent options that may

cause harm or security issues. The following options are blocked:

◦  -i/--interface

◦  -Z

◦  -B/--buffer-size

◦  -C

◦  -W

◦  -Z/--relinquish privileges

•  Non-word operators such as "&" or "|" are not allowed. Use boolean keywords such as "and," "or," and

"not."

•  When using command -r to read a file, do not provide any directory path characters. Use list-files

command to get the list of file names currently saved on the device, and then use those file names.

•  A total of four files can be saved at any given point on the device. Packet capture files are not saved

after a failover or reboot, but can be saved to external storage using the copy tcpdump-pcap command.

Examples

Inspecting traffic mirrored to the CPU via tcpdump and saving the output to my_capture_file.pcap:

switch# diag utilities tcpdump command -c 2 -x -w my_capture_file.pcap

Inspecting traffic mirrored to the CPU via tcpdump until Ctrl-C is entered.

2 packets captured

2 packets received by filter
0 packets dropped by kernel

Ending traffic capture.
Listing saved capture files:

switch# diag utilities tcpdump list-files

my_capture_file.pcap
Reading my_capture_file.pcap:

switch# diag utilities tcpdump command -r my_capture_file.pcap
reading from file /tmp/tcpdump/my_capture_file1.pcap, link-type EN10MB

(Ethernet)

  1  11:59:34.047867 IP6 localhost.40318 > localhost.ntp: NTPv2, Reserved,

length 12

Public

diag utilities tcpdump 97

        0x0000:  0000 0304 0006 0000 0000 0000 0000 86dd  ................

        0x0010:  600a 7e47 0014 1140 0000 0000 0000 0000  `.~G...@........

        0x0020:  0000 0000 0000 0001 0000 0000 0000 0000  ................

        0x0030:  0000 0000 0000 0001 9d7e 007b 0014 0027  .........~.{...'

        0x0040:  1601 0001 0000 0000 0000 0000            ............

  2  11:59:34.047915 IP6 localhost.ntp > localhost.40318: NTPv2, Reserved,

length 12

        0x0000:  0000 0304 0006 0000 0000 0000 0000 86dd  ................

        0x0010:  6b8d 23c5 0014 1140 0000 0000 0000 0000  k.#....@........

        0x0020:  0000 0000 0000 0001 0000 0000 0000 0000  ................

        0x0030:  0000 0000 0000 0001 007b 9d7e 0014 0027  .........{.~...'

        0x0040:  d681 0001 c016 0000 0000 0000
Removing my_capture_file.pcap:

switch# diag utilities tcpdump delete-file my_capture_file.pcap

Successfully removed file

Command History

Release

10.08

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8400

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

disable

Syntax

disable

Description

Disables the mirroring session specified by the current command context.

Public

disable 98

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

Syntax

enable

Description

Enables the mirroring session for the current command context.

Usage

By default, mirroring sessions are disabled.

Public

enable 99

When a mirroring session is enabled, the show mirror command for that session ID shows an Admin Status
of enable and an Operation Status of enabled.

If sFlow is enabled on an interface and a mirroring session specifies the same interface as the source of
received traffic (the source is configured with a direction of

rx
or

both
):

•  The attempt to enable the mirroring session fails and an error is returned.

•  To enable the mirroring session, first you must disable sFlow on the port.

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

Public

enable 100

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

mirror session 101

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

show mirror [<SESSION-ID>] [vsx-peer]

Description

Shows information about mirroring sessions. If  <SESSION-ID>  is not specified, then the command
shows a summary of all configured mirroring sessions. If  <SESSION-ID>  is specified, then the command
shows detailed information about the specified mirroring session.

Parameter

Description

Specifies the session identifier. Range: 1 to 4

<SESSION‐ID>

vsx‐peer

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Public

show mirror 102

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

Public

show mirror 103

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

Public

show mirror 104

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

Specifies a physical port on the switch. Use the format membe
r/slot/port (for example, 1/3/1).

<PORT‐NUM>

Public

source interface 105

Parameter

Description

Specifies the identifier for the LAG (link aggregation group).

<LAG‐NAME>

<DIRECTION>

Usage

Selects the direction of traffic to be mirrored from this source in
terface. There is no default for this parameter. Valid values are t
he following:

•  both: Mirror both transmitted and received packets.
•  rx: Mirror only received packets.
•  tx: Mirror only transmitted packets.

There is a limit of source interfaces in each direction of a given mirror session:

Switch

8400

9300/9300S

10040

Source interface limit per mirror session (4 possibl
e sessions)

256

128

128

However, there is a practical limit to the amount of traffic that a mirror destination can transmit. For example,
mirroring session with multiple 10G sources can overwhelm a single 10G destination.

You can configure the same source interface in multiple mirroring sessions, but only one of those mirroring
sessions can be enabled at a time.

Classifier policies with mirror actions can also be used to match and mirror network traffic. Although mirror
actions of classifier policies must specify an enabled mirroring session, the traffic matching and mirroring
actions are separate from and take priority over basic mirroring sessions. For example, mirroring session 1
might monitor a source interface, but a classifier policy might match some traffic from that same source
interface and direct it to the destination interface of a different mirroring session. In this situation, only the
traffic that is not matched by the policy is considered for matching by mirroring session 1.

If an interface is in active use by the sFlow feature, then that interface cannot be used as source of received
traffic (configured as a source destination with a direction of rx or both) in an enabled mirroring session. If

Public

source interface 106

you want to use this interface as a source of received traffic in a mirroring session, you must disable sFlow on
the interface before you enable the mirroring session on the same interface.

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

source interface 107

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

source vlan

Syntax

source vlan <VLAN-NUM> {rx | tx | both}

no source vlan <VLAN-NUM> {rx | tx | both}

Description

Mirroring with VLAN as a source is supported in the following traffic directions:

•  both - traffic received and transmitted

•  rx - only received traffic

•  tx - only transmitted traffic

More than one source VLAN can be configured in a mirror session. Each such VLAN may specify its own
direction.

There is a limit of 6 source VLANs for a given mirror session. There is also a limit of 6 source VLANs across
all mirror sessions.

Public

source vlan 108

Same VLAN may not be configured as a mirror source for multiple sessions.

NOTE

When changing a source VLAN in an enabled mirror session (i.e. adding, changing
direction, or removing) mirrored packets being transmitted out of the mirror
destination port from other mirror sources may be briefly interrupted during the
reconfiguration.

Direction of an existing source VLAN can be updated in one of two ways.

•  Reenter the source vlan <VLAN-NUM> <direction> command with the new preferred direction.

•  Use the no source vlan <VLAN-NUM> <direction> form of the command with a direction (rx or tx) to

selectively remove the specified direction.

Specifying the last remaining direction for that VLAN will remove the VLAN from the configuration entirely.

Mirroring allows configuration of VLAN as a source. When VLAN source is configured in the rx direction, all
packets are mirrored as they are received in the switch. When VLAN source is configured in tx direction, all
packets are mirrored as they are transmitted out of the switch.

For packets bridged through the switch:

•

If the mirror is configured in 'both' direction, two copies of packets are mirrored, otherwise one copy of
the packet will be mirrored.

For routed packets:

•

If the mirror is configured in rx direction, packets are mirrored in the pre-routed form with the
Destination MAC address as the switch address.

Also, bridged packets are the only packets mirrored in the rx direction.

•

If the mirror is configured in tx direction, packets are mirrored in post-routed form with the source MAC
as the switch address. Destination MAC is the nexthop gateway or station.

•

If the mirror is configured in both direction, one copy of the packet will be mirrored.

•  To mirror routed packets received on a VLAN and transmitted out a different VLAN, enable tx mirroring

on the destination VLAN.

Control plane packets generated by the switch's CPU are processed both in theingress and the egress packet
processing pipeline. The following are the behavior for mirroring with VLAN as source:

•

If the mirror is configured in the rx or tx direction, the packets are mirrored to the mirror destination.

•

If the mirror is configured in the both direction, two copies of the packets are mirrored to the mirror
destination.

The no form command will cease mirroring traffic from the specified source VLAN and remove the source
from the mirror configuration.

Public

source vlan 109

Parameter

VLAN‐NUM

direction

Examples

Description

Selects the VLAN number.

Specifies the direction of mirroring. tx (transmit), rx (receive), o
r both.

Creating a mirror session and adding a VLAN as a source of traffic in both directions on that port:

switch# configure terminal

switch(config)# mirror session 1

switch(config-mirror-1)# source vlan 10 both

Creating a mirror session and adding two VLANs as sources of traffic:

directions:

switch# configure terminal

switch(config)# mirror session 2

switch(config-mirror-2)# source vlan 10 tx

switch(config-mirror-2)# source vlan 20 both

Configuring the source in session 2 to receive by specifying the source interface configuration:

switch(config-mirror-2)# source vlan 10 rx

Removing the first source interface in session 2 entirely, and removing the transmit direction from the other
so that mirroring only occurs in the receive direction:

switch(config-mirror-2)# source vlan 10 rx

switch(config-mirror-2)# source vlan 20 tx

switch(config-mirror-2)# source vlan 2000 rx

The maximum number of source VLANs per mirror session is 1024 in each

direction

Command History

Release

Modification

10.07 or earlier

‐‐

Public

source vlan 110

Command Information

Platforms

Command context

Authority

8400

config

Administrators or local user group members with execution righ
ts for this command.

Monitoring a device using SNMP

Configuring SNMP: Refer to the SNMP/MIB Guide for information on how to add SNMP so a device can be
monitored from a network management system (NMS).

Configuring an SNMP trap receiver: Refer to the SNMP/MIB Guide and specific information about the  sho
w snmp trap  command to enable SNMP traps.

Breakout cable support

Ports default to an unsplit state. When a port is 'split', the split interfaces become active and can be
configured independently. For example, when a 40G QSFP+ port is split four ways, each split interface
behaves like a separate 10G SFP+ port. The split interfaces have the same name as the base port with an
added suffix to represent their lane of the breakout cable or optical channel on SR4 optics. Splitting an
interface removes most of the port's configuration settings and makes it inactive. The port will no longer
appear in many show interface commands and most configuration commands are not allowed; the split
interface name must be used.

The same thing happens in reverse when an interface is unsplit. However, note that the 'split' and 'no split'
commands are always performed in the unsplit port's context.

Subtopics

Limitations with breakout cable support
Breakout cable support commands

Limitations with breakout cable support

•  The 8400 switch does not support DAC breakout cables, only optical breakout cables.

•  The JL365A Aruba 8400X 8p 40G QSFP+ Adv module does not support Priority-Based Flow Control

(PFC) on split ports.

Public

Monitoring a device using SNMP 111

•  The JL366A Aruba 8400X 6p 40G/100G QSFP28 Adv module does not support 100G breakout cables;

it only supports split ports at the 40G speed (into 4x10G links).

Breakout cable support commands

Subtopics

split

split

Syntax

split [<COUNT>][<SPEED>][confirm]

no split [confirm]

Description

Splits a port into multiple interfaces. Only ports capable of supporting breakout cables or SR4/eSR4/eDR4
optics can be split.

Parameter

Description

Specifies the number of child interfaces to activate upon splittin
g the port. Default: 4.

<COUNT>

<SPEED>

confirm

Usage

Specifies the speed for the child interfaces.

Specifies the confirmation of port splitting.

•  Some switch interfaces support different split counts depending on the installed transceiver. For these
interfaces, the number of child interfaces to activate can be specified. If omitted, the default is 4. For
transceivers capable of supporting multiple split modes, the closest mode with enough lanes is used.

Public

Breakout cable support commands 112

•  Some transceivers also support multiple split modes with different speeds. For example, 2x200G or

2x100G. When a speed is not specified, the highest available speed for the split count is used. To select
a different split mode with a lower speed, the desired speed must be specified.

The splittable ports for all models are shown in the table below:

Model

8400X modules

•  JL365A
•  JL366A

Description

8400X 8p 40G QSFP+ Adv Modul
e

8400X 6p 40G/100G QSFP28 Ad
v Module

Port info

1‐8 (40G)

1‐6 Only capable of 40G split in
to 4 x 10G

JL366A modules do not have 25G
MACs to support split 100G

8400X modules

8400X 8p 40G QSFP+ Adv Mod

1‐8 (40G)

•  JL365A
•  JL366A

8400X 6p 40G/100G QSFP28 Ad
v Mod

1‐6 Only capable of 40G split in
to 4 x 10G

JL366A modules do not have 25G
MACs to support split 100G

Examples

Splitting an interface:

switch(config-if)# interface 1/1/1

switch(config-if)# split

This command will disable the specified port, clear its configuration,

and split it into multiple interfaces. The split interfaces will not

be available until the next system or line module reboot.

Continue (y/n)? y

switch(config-if)# show interface brief

----------------------------------------------------------------------------
--------

Port    Native Mode   Type         Enabled Status  Reason

Speed   Desc          VLAN

----------------------------------------------------------------------------

--------

1/1/1:1 --     routed QSFP+DA3x4   yes     down    Split reboot pending

--   --

1/1/1:2 --     routed QSFP+DA3x4   yes     down    Split reboot pending

--   --

1/1/1:3 --     routed QSFP+DA3x4   yes     down    Split reboot pending

--   --

Public

split 113

1/1/1:4 --     routed QSFP+DA3x4   yes     down    Split reboot pending

--   --
Unsplitting a port on a switch that requires a reboot:

switch(config)# interface 1/1/1

switch(config-if)# no split

This command will disable the split interfaces for this port and clear

their configuration. The port will not be available until the next

system or line module reboot.

Continue (y/n)? y

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

8400

config‐if

Administrators or local user group members with execution righ
ts for this command.

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

Public

Aruba AirWave 114

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

Public

SNMP support and AirWave 115

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

Public

Configuring the AOS-CX switch to be monitored by A... 116

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

Public

AirWave commands 117

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

Public

logging 118

Parameter

Description

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

•  crit: Forwards syslog messages with the severity of critical

(5) and above.

•  debug: Forwards syslog messages with the severity of deb

ug (0) and above.

•  emerg: Forwards syslog messages with the severity of eme

rgency (7) only.

Public

logging 119

Parameter

Description

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

switch(config)# logging 10.0.10.2 tcp 3440 severity err vrf mgmt include-

auditable-events filter filter_lldp_logs rate-limit-burst 3 rate-limit-

interval 35

Public

logging 120

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

Description

Adds an SNMPv1/SNMPv2c community string. A community string is like a password that controls read/
write access to the SNMP agent. A network management program must supply this name when attempting
to get SNMP information from the switch. A maximum of 10 community strings are supported. Once you
create your own community string, the default community string ( public ) is deleted.

The no form of this command removes the specified SNMPv1/SNMPv2c community string. When no
community string exists, a default community string with the value public is automatically defined.

Parameter

Description

<STRING>

Specifies the SNMPv1/SNMPv2c community string. Range: 1 to
32 printable ASCII characters, excluding space and question ma
rk.

Public

snmp-server community 121

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

Description

Specifies the IPv4 ACL type.

Specifies the IPv6 ACL type.

Specifies the ACL name. It supports a maximum of 64 characte
rs.

Parameter

ip

ipv6

<ACL‐NAME>

Examples

Setting the SNMPv1/SNMPv2c community string to private:

switch(config)# snmp-server community private

Removing SNMPv1/SNMPv2c community string private:

switch(config)# no snmp-server community private

Configuring the access level for the SMNP community to read-only:

Public

snmp-server community 122

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

snmp-server vrf default

snmp-server community my_comm_1

    access-list ip ipv4_acl

    access-list ipv6 ipv6_acl

NOTE
hitcounts for SNMP ACL will not be incremented.
Example:show access-list hitcounts ip all will not show the hit count of SNMP
ACL.

Public

snmp-server community 123

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

Public

snmp-server host 124

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

<UDP‐PORT>

<VRF‐NAME>

Specifies the SNMPv3 user name to be used in the SNMP trap n
otifications.

Specifies the name of the community string to use when sendin
g trap notifications. Range: 1 ‐ 32 printable ASCII characters,
excluding space and question mark. Default: public.

Specifies the UDP port on which notifications are sent. Range: 1
‐ 65535. Default: 162.

Specifies the VRF on which the SNMP agent listens for incomin
g requests.

Public

snmp-server host 125

Parameter

Description

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

switch(config)# snmp-server host a:b::c:d trap version v1

switch(config)# no snmp-server host a:b::c:d trap version v1

switch(config)# snmp-server host 10.10.10.10 trap version v2c community

public

switch(config)# no snmp-server host 10.10.10.10 trap version v2c community

Public

snmp-server host 126

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

switch(config)# snmp-server host 10.10.10.10 inform version v2c community

public port 5000 vrf default

switch(config)# no snmp-server host 10.10.10.10 inform version v2c

community public port 5000 vrf default

Public

snmp-server host 127

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

notifications.

  card            Sends Card notifications.

  config          Sends Configuration change notifications.

  entity          Sends Entity notifications.

  fan             Sends Fan notifications.

  interface       Sends Interface notifications.

Public

snmp-server host 128

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

snmp-server vrf

Public

snmp-server vrf 129

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

switch(config)# snmp-server vrf mgmt

Configuring the SNMP agent to listen on used-defined VRF myvrf.

switch(config)# snmp-server vrf myvrf

Stopping the SNMP agent from listening on VRF default.

switch(config)# no snmp-server vrf default

Command History

Release

Modification

10.07 or earlier

‐‐

Public

snmp-server vrf 130

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

Examples

Creating an SNMPv3 context named newContext:

switch(config)# snmpv3 context newContext

Creating an SNMPv3 context named newContext on VRF myVrf and with community string private.

switch(config)# snmpv3 context newContext vrf myVrf community private

Public

snmpv3 context 131

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

Description

Creates an SNMPv3 user and adds it to an SNMPv3 context. The SNMPv3 security level (set with command
snmpv3 security-level) determines which users are allowed to authenticate.

Public

snmpv3 user 132

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
ntable ASCII characters. Ciphertext is used when copying user c
onfiguration settings between switches.

NOTE

Public

snmpv3 user 133

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

snmpv3 user 134

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

snmpv3 user 135

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

snmpv3 user view 136

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

Support and Other Resources 137

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

Accessing HPE Aruba Networking Support 138

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

Accessing Updates 139

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

Regulatory Information 140

