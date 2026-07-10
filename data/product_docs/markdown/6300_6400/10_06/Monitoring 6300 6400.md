AOS-CX 10.06 Monitoring Guide
6300, 6400 Switch Series

Part Number: 5200-7711
Published: November 2020
Edition: 1

© Copyright 2020 Hewlett Packard Enterprise

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
Identifying switch ports and interfaces .......................................................................................................9
Identifying switch components ....................................................................................................................9

Chapter 2 Monitoring hardware through visual observation................ 10
Confirming normal operation of the switch by reading LEDs.................................................................10
Detecting if the switch is not ready for a failover event.......................................................................... 11
Finding faulted components using the switch LEDs................................................................................ 12

Chapter 3 Aruba 6300/6400 Switch Series LEDs......................................... 13
Switch and port LEDs for 6300 switch series............................................................................................ 13
Switch and port LEDs for 6400 switch series............................................................................................ 15
Front panel LEDs for 6400 switch series........................................................................................ 16

Chapter 4 Boot commands............................................................................. 20
boot fabric-module............................................................................................................................... 20
boot line-module.................................................................................................................................... 21
boot management-module...................................................................................................................... 21
boot set-default.................................................................................................................................... 23
boot system............................................................................................................................................... 23
show boot-history..................................................................................................................................25

Chapter 5 Switch system and hardware commands................................ 28
bluetooth disable..................................................................................................................................28
bluetooth enable.................................................................................................................................... 28
clear events............................................................................................................................................. 29
clear ip errors...................................................................................................................................... 30
domain-name............................................................................................................................................... 30
hostname...................................................................................................................................................... 31
led locator............................................................................................................................................... 32
module admin-state............................................................................................................................... 32
module product-number.........................................................................................................................33
mtrace...........................................................................................................................................................35
show bluetooth........................................................................................................................................ 36
show boot-history..................................................................................................................................37
show capacities...................................................................................................................................... 39
show capacities-status...................................................................................................................... 40
show core-dump........................................................................................................................................ 41
show domain-name.................................................................................................................................... 43
show environment fan........................................................................................................................... 44
show environment led........................................................................................................................... 46

Contents

3

show environment power-consumption........................................................................................... 47
show environment power-supply.......................................................................................................48
show environment rear-display-module....................................................................................... 49
show environment temperature......................................................................................................... 50
show events............................................................................................................................................... 52
show fabric............................................................................................................................................... 55
show hostname...........................................................................................................................................56
show images............................................................................................................................................... 57
show ip errors........................................................................................................................................ 58
show module............................................................................................................................................... 59
show running-config............................................................................................................................. 61
show running-config current-context......................................................................................... 65
show startup-config............................................................................................................................. 66
show system............................................................................................................................................... 67
show system error-counter-monitor..............................................................................................68
show system resource-utilization................................................................................................ 70
show tech....................................................................................................................................................71
show usb...................................................................................................................................................... 72
show usb file-system........................................................................................................................... 73
show version............................................................................................................................................. 74
system resource-utilization poll-interval............................................................................75
top cpu........................................................................................................................................................ 75
top memory..................................................................................................................................................76
usb................................................................................................................................................................. 77
usb mount | unmount ............................................................................................................................ 77

Chapter 6 External storage.............................................................................79
External storage commands....................................................................................................................... 79
address............................................................................................................................................. 79
directory........................................................................................................................................ 80
disable............................................................................................................................................. 81
enable............................................................................................................................................... 81
external-storage.........................................................................................................................82
password...........................................................................................................................................82
show external-storage............................................................................................................. 83
show running-config external-storage............................................................................84
type....................................................................................................................................................84
username...........................................................................................................................................85
vrf...................................................................................................................................................... 86

Chapter 7 IP-SLA................................................................................................ 87
IP-SLA guidelines.......................................................................................................................................... 87
Limitations with VoIP SLAs.......................................................................................................................... 88
IP-SLA commands.........................................................................................................................................88
http....................................................................................................................................................88
icmp-echo........................................................................................................................................ 89
ip-sla............................................................................................................................................... 90
ip-sla responder.........................................................................................................................91
show ip-sla responder............................................................................................................. 92
show ip-sla responder results........................................................................................... 92
show ip-sla <SLA-NAME>........................................................................................................... 93
start-test...................................................................................................................................... 95

4

AOS-CX 10.06 Monitoring Guide

stop-test........................................................................................................................................ 95
tcp-connect.................................................................................................................................... 96
udp-echo...........................................................................................................................................97
udp-jitter-voip........................................................................................................................... 98
vrf...................................................................................................................................................... 99

Chapter 8 L1-100Mbps downshift............................................................... 100
Limitations with speed downshift............................................................................................................ 100
L1-100Mbps downshift commands......................................................................................................... 100
downshift enable.......................................................................................................................100
show interface........................................................................................................................... 101
show interface downshift-enable.....................................................................................103
show running-config interface......................................................................................... 104

Chapter 9 Mirroring........................................................................................107
Mirror statistics...........................................................................................................................................107
Classifier policies and mirroring sessions............................................................................................... 107
VLAN as a source........................................................................................................................................ 108
Mirroring commands................................................................................................................................. 108
clear mirror................................................................................................................................108
comment........................................................................................................................................... 109
copy tshark-pcap.......................................................................................................................110
destination cpu.........................................................................................................................110
destination interface........................................................................................................... 111
destination tunnel.................................................................................................................. 112
diagnostic.................................................................................................................................... 113
disable........................................................................................................................................... 114
enable............................................................................................................................................. 115
mirror session........................................................................................................................... 115
show mirror.................................................................................................................................. 116
source interface.......................................................................................................................118
source vlan.................................................................................................................................. 119

Chapter 10 Monitoring a device by using SNMP......................................121

Chapter 11 Power-over-Ethernet (PoE)...................................................... 122
PoE commands...........................................................................................................................................123
lldp dot3 poe............................................................................................................................. 123
lldp med poe................................................................................................................................124
power-over-ethernet................................................................................................................124
power-over-ethernet allocate-by.....................................................................................125
power-over-ethernet always-on......................................................................................... 126
power-over-ethernet assigned-class ............................................................................126
power-over-ethernet pre-std-detect.............................................................................. 127
power-over-ethernet priority........................................................................................... 128
power-over-ethernet quick-poe ....................................................................................... 128
power-over-ethernet threshold......................................................................................... 129
power-over-ethernet priority........................................................................................... 130
show lldp local.........................................................................................................................130
show lldp neighbor.................................................................................................................. 131
show power-over-ethernet.....................................................................................................132

Contents

5

Chapter 12 Aruba AirWave........................................................................... 137
SNMP support and AirWave......................................................................................................................137
Supported features with AirWave and the AOS-CX switch....................................................................138
Configuring the AOS-CX switch to be monitored by AirWave............................................................... 138
logging........................................................................................................................................... 139
snmp-server community........................................................................................................... 140
snmp-server host.......................................................................................................................141
snmp-server vrf.........................................................................................................................143
snmpv3 context........................................................................................................................... 143
snmpv3 user.................................................................................................................................. 144

Chapter 13 Support and other resources..................................................147
Accessing Aruba Support.......................................................................................................................... 147
Accessing updates......................................................................................................................................147
Warranty information................................................................................................................................ 148
Regulatory information............................................................................................................................. 148
Documentation feedback..........................................................................................................................148

6

AOS-CX 10.06 Monitoring Guide

Chapter 1
About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

• Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A, JL667A,

JL668A, JL762A)

• Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

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

Table Continued

Chapter 1 About this document

7

Convention

Usage

{ }

[ ]

… or

...

Braces. Indicates that at least one of the enclosed items is required.

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

8

AOS-CX 10.06 Monitoring Guide

Identifying switch ports and interfaces
Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:

member/slot/port

On the 6300 Switch Series

• member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•

slot: Line module number. Always 1.

• port: Physical number of a port on a line module.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the 6400 Switch Series

• member: Always 1. VSF is not supported on this switch.

•

slot: Specifies physical location of a module in the switch chassis.

◦ Management modules are on the front of the switch in slots 1/1 and 1/2.

◦

Line modules are on the front of the switch starting in slot 1/3.

• port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

Identifying switch components

• Power supplies are on the front of the switch behind the bezel above the management modules. Power

supplies are labeled in software in the format: member/power supply:

◦ member: 1.

◦ power supply: 1 to 4.

•

Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

◦ member: 1.

◦

◦

tray: 1 to 4.

fan: 1 to 4.

•

Fabric modules are not labeled on the switch but are labeled in software in the format: member/module:

◦ member: 1.

◦ member: 1 or 2.

• The display module on the rear of the switch is not labeled with a member or slot number.

Chapter 1 About this document

9

Chapter 2
Monitoring hardware through visual observation

Confirming normal operation of the switch by reading
LEDs
This task describes using the switch LEDs to confirm that the switch is operating normally.

Procedure

1. Quick check: Verify that the chassis has power and there are no fault conditions.

On the front of the switch, verify that the states of the following LEDs are On Green:

• Power

• Health

2. Verify that the Health LEDs of all installed line modules are On Green.

3. Verify that the Health LEDs of all installed management modules are On Green.

4. Verify that the network ports are operating normally.

a. On the active management module, check the Status Front section. Verify that each LED that indicates

a line module is in one of the following states:

• On Green (normal operation)

• Off (no line module installed)

b. On each line module, verify that each port LED is in one of the following states:

• On Green, Half-Bright Green, or Flickering Green (normal operation)

• Off (no cable connected or port off by default in config)

5. Verify that the power supplies are operating normally.

a. On the active management module, check the Status Front section. Verify that each LED that indicates

a power supply is in one of the following states:

• On Green (normal operation)

• Off (no power supply installed)

b. On each power supply, verify that LEDs are in the following states:

• Power LED: On Green

•

Fault LED: Off

10

AOS-CX 10.06 Monitoring Guide

6. Verify that the rear components are operating normally by checking the Status Rear section of the active

management module:

a. Verify that the LEDs for the fabric modules are in one of the following states:

• On Green (normal operation)

• Off (component not installed)

b. Verify that the LEDs for the fan trays and fans are On Green.

7. Verify that the standby management module is ready to take over as the active management module.

On the standby management module, verify the states of the following LEDs:

• Health LED is On Green.

• Management state standby (Stby) LED is On Green.

Detecting if the switch is not ready for a failover event
This task describes using the switch LEDs to detect if the switch is not ready for the loss of a fabric module
or for a failover from the active management module to the standby management module.

NOTE: Although you can detect power supply failures by viewing the LEDs, you must use
software commands to determine if the power supply redundancy is sufficient to power the
chassis if a power supply fails.

Procedure

1. Detect if the standby management module is shut down.

If the standby management module is shut down, the LED states are as follows:

• The standby management module health LED is Off.

• The standby management state active (Actv) LED is Off.

• The standby management state standby (Stby) LED is Off.

• On the active management module in the Status Front Management Modules section, the LED for the
standby management module is Off. For example, if the active management module is Management
Module LED 5, Management Modules LED 6 is Off.

2. Detect if the standby management module is in a transient state.

If the standby management module is booting, updating, or in another transient state, the LED states are
as follows:

• The standby management module health LED is Slow Flash Green when the service operating system

is running or during an operating system update.

• The standby management module Booting LED is Slow Flash Green when the ArubaOS-CX operating

system is booting.

Chapter 2 Monitoring hardware through visual observation

11

• The standby management state active (Actv) LED is Off.

• The standby management state standby (Stby) LED is Off.

• On the active management module in the Status Front Management Modules section, the LED for the

standby management module is Slow Flash Green.

3. Detect if a fabric module is shut down or not present.

If a fabric module is shut down or not present, the LED states are as follows:

• On the active management module, in the Status Rear section, the LED for the fabric module is Off.

• On the rear display module, the LED for the fabric module is Off.

• On the fabric module, the health LED is Off. However, the fabric module is behind fan 1 and is not

directly visible.

Finding faulted components using the switch LEDs
This task describes using the switch LEDs to find components that are in a fault condition.

NOTE: All green LEDs—except for chassis power LEDs and the Usr1 LED—are off when the LED
mode is set to Light Faults (The Usr1 LED of the LED Mode section of the active management
module is On Green and the default behavior for the Usr1 LED is being used.).

Procedure

1. Find the switch that has the fault condition, which is indicated by a chassis health LED in the state of Slow

Flash Orange.

The chassis health LED is located on the front of the switch and on the rear panel of the switch.

2. If you are at the back of the switch, on the rear panel, look for LEDs that are in the Slow Flash Orange

state:

The Status Rear area has LEDs for power supplies, fabric modules, fan trays, and fans. The number on
the LED represents the unit number of the component.

If the only LED in a state of Slow Flash Orange is the Chassis health LED, go to the front of the switch.

3. At the front of the switch, on the active management module, look for LEDs that are in the Slow Flash

Orange state:

• The Status Front area has LEDs for power supplies, line and fabric modules, and management

modules. The number on the LED indicates the slot number of the component.

• The Status Rear area has LEDs for fabric modules and fan trays, with a single LED for all the fans in the

fan tray. The number on the LED represents the slot or bay number of the component.

4. Use the number indicated by the LED that is flashing to locate the slot that contains the faulted

component.

The fabric modules are located behind the fan trays, and the fabric module number corresponds to the
fan tray number.

5. At the front of the switch, on line modules, look for LEDs that are in the Slow Flash Orange state:

Module LEDs and Port LEDs indicate faults if their states are Slow Flash Orange.

12

AOS-CX 10.06 Monitoring Guide

Chapter 3
Aruba 6300/6400 Switch Series LEDs

Switch and port LEDs for 6300 switch series
Figure 1: Switch and port LEDs

Table 1: Switch and port LEDs: Labels and description

Label

Description

1

2

3

4

5

6

7

8

9

Switch port LEDs

Back Module status LED

Speed mode selected LED

PoE mode selected

Reset button Usr mode selected LED

UID (Unit Identification)

Global Status LED

LED Mode status LED

Management Console LED

Table 2: Front panel LED behavior

Switch LEDs

Function

State

Meaning

Back LED

PoE LED

Status of modular
components installed
in the back of the
chassis (not applicable
for 6300F switches

Indicates Port LEDs are
showing PoE

On - Green

Normal

Slow Flash - Amber

Fault in one of the modules
in the back of the chassis

Off

PoE mode not selected

On - Green

PoE mode selected

Chapter 3 Aruba 6300/6400 Switch Series LEDs

Table Continued

13

| Switch LEDs | Function               | State              | Meaning                    |
| ----------- | ---------------------- | ------------------ | -------------------------- |
|             | information (not       | Slow Flash - Amber | Hardware failure PoE       |
|             | applicable for non PoE |                    | enabled port, PoE mode not |
|             | switches)              |                    | selected                   |
|             |                        | On - Amber         | Hardware failure PoE       |
enabled port, PoE mode
selected
| Spd LED | Indicates Port LEDs are | Off | Speed mode not selected |
| ------- | ----------------------- | --- | ----------------------- |
showing speed
|     |     | On - Green | Speed mode selected |
| --- | --- | ---------- | ------------------- |
information
|     |     | Not Implemented | No fault defined |
| --- | --- | --------------- | ---------------- |
Stk LED Indicates Port LEDs are Off Stacking mode not selected
showing stacking mode
|     |     | On - Green | Stacking mode selected |
| --- | --- | ---------- | ---------------------- |
information
|     |     | On - Amber | A port has a stacking failure. |
| --- | --- | ---------- | ------------------------------ |
Stacking mode selected
|     |     | Slow flash Amber | A port has a stacking failure. |
| --- | --- | ---------------- | ------------------------------ |
Stacking mode not selected
| UID LED | User-configurable LED | Off | User defined the located |
| ------- | --------------------- | --- | ------------------------ |
LED : OFF
|     |     | On/Flash Blue (for 30 | User defined the locator |
| --- | --- | --------------------- | ------------------------ |
|     |     | min)                  | LED: On/Flash            |
Global Status Indicator Overall status of the Flash - Green Self-test in progress during
| LED | product |     | UBOOT, SVOS and ArubaOS- |
| --- | ------- | --- | ------------------------ |
CV
|     |     | On - Green | Successfully initialized |
| --- | --- | ---------- | ------------------------ |
ArubaOS-CX
|     |     | Flash - Amber | Recoverable faults (e.g. fans, |
| --- | --- | ------------- | ------------------------------ |
PSU fault)
|     |     | On - Amber | Critical faults (e.g. exceed |
| --- | --- | ---------- | ---------------------------- |
temperature limit)
OOBM Status Indicator Status of OOBM Link Off OOBM port is not
| LED | connectivity |     | connected, no link |
| --- | ------------ | --- | ------------------ |
established
|     |     | Half Bright - Green | OOBM port is enabled and |
| --- | --- | ------------------- | ------------------------ |
established link with partner
|     |     | On - Green | Experiencing high |
| --- | --- | ---------- | ----------------- |
bandwidth utilization
|     |     | Activity Flicker - Green | % of the time that the LED |
| --- | --- | ------------------------ | -------------------------- |
light up is roughly
proportional to the % of full
bandwidth utilization of the
port
* Press the Mode Select button to switch between User(default), PoE, Spd, or Stk Mode.
| 14  |     |     | AOS-CX 10.06 Monitoring Guide |
| --- | --- | --- | ----------------------------- |

Table 3: Rear Panel LED behavior
| Switch LEDs    | Function              | State/Mode         | Meaning                 |
| -------------- | --------------------- | ------------------ | ----------------------- |
| Fan health LED | Status of fan         | On - Green         | Normal                  |
|                |                       | Slow flash - Amber | Fan fault               |
| UID LED        | User-configurable LED | Off                | User define the locator |
LED : OFF
|     |     | On/Flash (30 min) - blue | User define the locator |
| --- | --- | ------------------------ | ----------------------- |
LED: On/Flash
PSU Status Indicator LED Status of power supply On Green Normal
|     |     | Off | No power, PSU has |
| --- | --- | --- | ----------------- |
invalid AC input of invalid
DC outputs
|     |     | Slow Flash - Green | Power supply has faulted |
| --- | --- | ------------------ | ------------------------ |
or warning
Switch and port LEDs for 6400 switch series
Figure 2: Rear panel LEDs for 6400 switch series
1
Power supply status (1) (2) (3) (4)
2
Chassis power LED
3
Chassis health LED
4
Unit identification (UID) LED
5
Fan tray status (1, 2)
Chapter 3 Aruba 6300/6400 Switch Series LEDs 15

Front panel LEDs for 6400 switch series

The Aruba 6400 switches have two management module (MM) slots. Management modules support control
plane activities and in-memory running of the Time Series Database.

Figure 3: Management module slots with management modules installed

When two management modules are installed, one operates in active mode and the other operates in
standby mode. The active slot is determined by election. Installing two management modules provides
control plane high availability.

Figure 4: Management module features

1

Mgmt state (Actv) LED

Indicates the status of the management module after
booting. If the MM is the active MM, then the LED glows
steady green.

System power LED

When the system is receiving power, glows steady green.=.

2

3

Management module health LED
(green)

4

Line module status LEDs

Indicates status of the switch. LED glows steady green when
switch is ready after booting from the Network Operating
System (NOS).

Indicates if a line module is installed in a line module slot (1
through 5 for 6405 switches; 1 through 10 on 6410
switches). If a line module is installed in a given slot, then
the numbered LED for that slot glows steady green.

Table Continued

16

AOS-CX 10.06 Monitoring Guide

5

6

7

Front Power supply status (1 2 3 4)
LEDs

Indicates if a power supply is installed in the slot. If an active
power supply is installed, then the LEDs glow steady green.

Fan tray status LEDs (1 - 4)

Indicate if the fan tray is installed in the slot. If a fan tray is
installed in the slot, then the LED glows steady green.

LED mode: Usr1, Usr2 Spd, and PoE
LEDs

The display of these LEDs is based on the LED mode button
selection.

• Usr1 LED: Indicates if the line module is working

8

Auxillary port

correctly.

• Usr2 LED: Reserved

• Spd LED: Indicates the traffic rate of the line module.

Without a USB device installed, the auxiliary port LED is off
after power-on and self-test.

With a USB device installed, this LED displays the following
after power-on and self-test:

• Steady green: USB installed, initialized, and mounted, but

no data transfer.

•

Flicker green: Data transfer in progress

9

Mgmt port (OOBM Port) with
Activity/Link LED

Without an active network connection, this LED is off after
power-on and self-test completes.

With an active network connection, this LED operates as
follows:

• Half-bright green: Port enabled and receiving Link

indication from connected device.

•

Flickering half-bright to full-bright green: Varying port
activity level.

• Steady green: Port at high utilization.

Changes the behavior of the line module port LEDs. This
button changes the LED behavior from the default Link/
Activity behavior to cycle through the PoE, speed (Spd), and
user (Usr) options.

Serial console port (RJ-45)

USB Micro-B console port

LED Mode button

UID (Unit Identification) LED

PoE

Power-over-Ethernet

Chassis temperature status (Temp)
LED

Indicates the status of the chassis temperature. If the
temperature is at or below the specified rating, then the LED
glows steady green,

Table Continued

10

11

12

13

14

15

Chapter 3 Aruba 6300/6400 Switch Series LEDs

17

16 Mgmt reset button

17 Mgmt state (Stby) LED

A recessed button that is used to reset the selected
management module.

Indicates the status of the management module after
booting. If the MM is the standby MM, then the LED glows
steady green.

Power Supply LEDs

Figure 5: Aruba X382 54DC 2700W AC Power Supply (JL372A)

The Aruba 6400 has four power supply unit slots that support the Aruba X382 54DC 2700W AC power supply
unit (PSU).

Figure 6: Aruba X382 54DC 2700W AC Power Supply (JL372A)

1

2

3

4

Power LED (green)

Power fail LED (amber)

Power supply handle

Latch release tab

• A single PSU is sufficient for fans and management cards to come up and provide user access and

diagnostics.

• At 220 V AC, only two PSUs are required for full operation and a single PSU is sufficient for the fans and

management cards to come up and provide user access/diagnostics.

• At 220 V AC: Installing three PSUs offers 2+1 redundancy and installing all four PSUs offers 2+2

redundancy.

• At 110 V AC: The switch offers N + 1 redundancy.

• The PSUs are hot-swappable. The chassis can be connected to an AC power source for a given PSU slot

while the PSU for that slot is being removed or installed.

1

2

3

4

Power LED (green)

Power fail LED (amber)

Power supply handle

Latch release tab

18

AOS-CX 10.06 Monitoring Guide

• A single PSU is sufficient for fans and management cards to come up and provide user access and

diagnostics.

• At 220 V AC, only two PSUs are required for full operation and a single PSU is sufficient for the fans and

management cards to come up and provide user access/diagnostics.

• At 220 V AC: Installing three PSUs offers 2+1 redundancy and installing all four PSUs offers 2+2

redundancy.

• At 110 V AC: The switch offers N + 1 redundancy.

• The PSUs are hot-swappable. The chassis can be connected to an AC power source for a given PSU slot

while the PSU for that slot is being removed or installed.

Line module LEDs

1*

2 *

3*

*4

5*

Line module 4-channel port LEDs

Line module port LED for upper port

Line module port LED for lower port

Line module port LED for upper uplink port

Line module port LED for lower uplink port

Chapter 3 Aruba 6300/6400 Switch Series LEDs

19

Chapter 4
Boot commands

boot fabric-module

Syntax

boot fabric-module <SLOT-ID>

Description

Reboots the specified fabric module.

Command context

Manager (#)

Parameters
<SLOT-ID>

Specifies the member and slot of the module in the format member/slot. For example, to specify the
module in member 1 slot 3, enter 1/3.

Authority

Administrators or local user group members with execution rights for this command.

Usage

The boot fabric-module command reboots the specified fabric module. Traffic performance is affected
while the module is down.

If the specified module is the only fabric module in an up state, rebooting that module stops traffic switching
between line modules and the line modules power down. The line modules power up when one fabric
module returns to an up state.

This command is valid for fabric modules only.

Examples

Rebooting the fabric module in slot 1/3 when auto-confirm is not enabled:

switch# boot fabric-module 1/3
This command will reboot the specified fabric module.  Traffic performance may
be affected while the module is down.  Rebooting the last fabric module will
stop traffic switching between line modules.
Do you want to continue (y/n)? y

switch#

Rebooting the fabric module in slot 1/1 when auto-confirm is enabled:

switch# boot fabric-module 1/3
This command will reboot the specified fabric module.  Traffic performance may
be affected while the module is down.  Rebooting the last fabric module will
stop traffic switching between line modules.

20

AOS-CX 10.06 Monitoring Guide

Do you want to continue (y/n) y (auto-confirm)

switch#

boot line-module

Syntax

boot line-module <SLOT-ID>

Description

Reboots the specified line module.

Command context

Manager (#)

Parameters
<SLOT-ID>

Specifies the member and slot of the module in the format member/slot. For example, to specify the
module in member 1 slot 3, enter 1/3.

Authority

Administrators or local user group members with execution rights for this command.

Usage

This command is supported on switches that have multiple line modules.

Reboots the specified line module. Any traffic for the switch passing through the affected module (SSH,
TELNET, and SNMP) is interrupted. It can take up to 2 minutes to reboot the module. During that time, you
can monitor progress by viewing the event log.

This command is valid for line modules only.

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

boot management-module

Syntax

boot management-module {active | standby | <SLOT-ID>}

Chapter 4 Boot commands

21

Description

Reboots the specified management module. Choose the management module to reboot by role (active or
standby) or by slot number.

Command context

Manager (#)

Parameters
active

Selects the active management module.

standby

Selects the standby management module.

<SLOT-ID>

Specifies the member and slot of the management module in the format member/slot. For example, to
specify the module in member 1 slot 5, enter 1/5.

Authority

Administrators or local user group members with execution rights for this command.

Usage

This command is supported on switches that have multiple management modules.

This command reboots a single management module in a chassis. Choose the management module to
reboot by role (active or standby) or by slot number.

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

NOTE: Hewlett Packard Enterprise recommends that you use the boot management-module
command instead of pressing the module reset button to reboot a management module
because if you are rebooting the only available management module, the boot management-
module command enables you to save the configuration, cancel the reboot, or both.

Examples

Rebooting the active management module when the standby management module is available:

switch# boot management-module active
The management-module in slot 1/5 is going down for reboot now.

22

AOS-CX 10.06 Monitoring Guide

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

boot set-default

Syntax

boot set-default {primary | secondary}

Description

Sets the default operating system image to use when the system is booted.

Command context

Manager (#)

Parameters
primary

Selects the primary network operating system image.

secondary

Selects the secondary network operating system image.

Authority

Administrators or local user group members with execution rights for this command.

Example

Selecting the primary image as the default boot image:

switch# boot set-default primary
Default boot image set to primary.

boot system

Syntax

boot system [primary | secondary | serviceos]

Description

Reboots all modules on the switch. By default, the configured default operating system image is used.
Optional parameters enable you to specify which system image to use for the reboot operation and for
future reboot operations.

Chapter 4 Boot commands

23

Command context

Manager (#)

Parameters
primary

Selects the primary operating system image for this reboot and sets the configured default operating
system image to primary for future reboots.

secondary

Selects the secondary operating system image for this reboot and sets the configured default operating
system image to secondary for future reboots.

serviceos

Selects the service operating system for this reboot. Does not change the configured default operating
system image. The service operating system acts as a standalone bootloader and recovery OS for
switches running the ArubaOS-CX operating system and is used in rare cases when troubleshooting a
switch.

Authority

Administrators or local user group members with execution rights for this command.

Usage

This command reboots the entire system. If you do not select one of the optional parameters, the system
reboots from the configured default boot image.

You can use the show images command to show information about the primary and secondary system
images.

Choosing one of the optional parameters affects the setting for the default boot image:

•

•

If you select the primary or secondary optional parameter, that image becomes the configured default
boot image for future system reboots. The command fails if the switch is not able to set the operating
system image to the image you selected.

You can use the boot set-default command to change the configured default operating system
image.

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

24

AOS-CX 10.06 Monitoring Guide

Continue (y/n)? y
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

show boot-history

Syntax

show boot-history [all]

Description

Shows boot information. When no parameters are specified, shows the most recent information about the
boot operation, and the three previous boot operations for the active management module. When the all
parameter is specified, shows the boot information for the active management module and all available line
modules. To view boot-history on the standby, the command must be sent on the standby console.

Command context

Manager (#)

Parameters
all

Shows boot information for the active management module and all available line modules.

Authority

Administrators or local user group members with execution rights for this command.

Usage

This command displays the boot-index, boot-ID, and up time in seconds for the current boot. If there is a
previous boot, it displays boot-index, boot-ID, reboot time (based on the time zone configured in the system)
and reboot reasons. Previous boot information is displayed in reverse chronological order.

Chapter 4 Boot commands

25

Index

The position of the boot in the history file. Range: 0 to3.

Boot ID

A unique ID for the boot . A system-generated 128-bit string.

Current Boot, up for <SECONDS> seconds

For the current boot, the show boot-history command shows the number of seconds the module
has been running on the current software.

Timestamp boot reason

For previous boot operations, the show boot-history command shows the time at which the
operation occurred and the reason for the boot. The reason for the boot is one of the following values:

<DAEMON-NAME> crash

The daemon identified by <DAEMON-NAME> caused the module to boot.

Kernel crash

The operating system software associated with the module caused the module to boot.

Reboot requested through database

The reboot occurred because of a request made through the CLI or other API.

Uncontrolled reboot

The reason for the reboot is not known.

Examples

Showing the boot history of the active management module:

switch# show boot-history
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
switch#

Showing the boot history of the active management module and all line modules:

switch# show boot-history all
Management module
=================

Index : 3
Boot ID : f1bf071bdd04492bbf8439c6e479d612
Current Boot, up for 22 hrs 12 mins 22 secs

26

AOS-CX 10.06 Monitoring Guide

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

Chapter 4 Boot commands

27

Chapter 5
Switch system and hardware commands

bluetooth disable

Syntax

bluetooth disable

no bluetooth disable

Description

Disables the Bluetooth feature on the switch. The Bluetooth feature includes both Bluetooth Classic and
Bluetooth Low Energy (BLE). Bluetooth is enabled by default.

The no form of this command enables the Bluetooth feature on the switch.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Example

Disabling Bluetooth on the switch. <XXXX> is the switch platform and <NNNNNNNNNN> is the device
identifier.

switch(config)# bluetooth disable
switch# show bluetooth
Enabled             : No
Device name         : <XXXX>-<NNNNNNNNNN>

switch(config)# show running-config
...
bluetooth disabled
...

bluetooth enable

Syntax

bluetooth enable

no bluetooth enable

Description

This command enables the Bluetooth feature on the switch. The Bluetooth feature includes both Bluetooth
Classic and Bluetooth Low Energy (BLE).

Default: Bluetooth is enabled by default.

28

AOS-CX 10.06 Monitoring Guide

The no form of this command disables the Bluetooth feature on the switch.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Usage

The default configuration of the Bluetooth feature is enabled. The output of the show running-config
command includes Bluetooth information only if the Bluetooth feature is disabled.

The Bluetooth feature includes both Bluetooth Classic and Bluetooth Low Energy (BLE).

The Bluetooth feature requires the USB feature to be enabled. If the USB feature has been disabled, you
must enable the USB feature before you can enable the Bluetooth feature.

Examples

switch(config)# bluetooth enable

clear events

Syntax

clear events

Description

Clears up event logs. Using the show events command will only display the logs generated after the clear
events command.

Command context

Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Examples

Clearing all generated event logs:

switch# show events
---------------------------------------------------
show event logs
---------------------------------------------------
2018-10-14:06:57:53.534384|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource utilization poll interval is changed to 27
2018-10-14:06:58:30.805504|lldpd|103|LOG_INFO|MSTR|1|Configured LLDP tx-timer to 36
2018-10-14:07:01:01.577564|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource utilization poll interval is changed to 49

switch# clear events

switch# show events
---------------------------------------------------
show event logs
---------------------------------------------------
2018-10-14:07:03:05.637544|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource utilization poll interval is changed to 34

Chapter 5 Switch system and hardware commands

29

clear ip errors

Syntax

clear ip errors

Description

Clears all IP error statistics.

Command context

Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Example

Clearing and showing ip errors:

switch# clear ip errors
switch# show ip errors
----------------------------------
Drop reason                Packets
----------------------------------
Malformed packets                0
IP address errors                0
...

domain-name

Syntax

domain-name <NAME>

no domain-name [<NAME>]

Description

Specifies the domain name of the switch.

The no form of this command sets the domain name to the default, which is no domain name.

Command context

config

Parameters
<NAME>

Specifies the domain name to be assigned to the switch. The first character of the name must be a letter
or a number. Length: 1 to 32 characters.

Authority

Administrators or local user group members with execution rights for this command.

30

AOS-CX 10.06 Monitoring Guide

Examples

Setting and showing the domain name:

switch# show domain-name

switch# config
switch(config)# domain-name example.com
switch(config)# show domain-name
example.com
switch(config)#

Setting the domain name to the default value:

switch(config)# no domain-name
switch(config)# show domain-name

switch(config)#

hostname

Syntax

hostname <HOSTNAME>

no hostname [<HOSTNAME>]

Description

Sets the host name of the switch.

The no form of this command sets the host name to the default value, which is switch.

Command context

config

Parameters
<HOSTNAME>

Specifies the host name. The first character of the host name must be a letter or a number. Length: 1 to
32 characters. Default: switch

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting and showing the host name:

switch# show hostname
switch
switch# config
switch(config)# hostname myswitch
myswitch(config)# show hostname
myswitch

Setting the host name to the default value:

Chapter 5 Switch system and hardware commands

31

myswitch(config)# no hostname
switch(config)#

led locator

Syntax

led locator {on | off | flashing}

Description

Sets the state of the locator LED to on, off (default), or flashing.

Command context

Manager (#)

Parameters
on

Turns on the LED.

off

Turns off the LED, which is the default value.

flashing

Sets the LED to blink on and off repeatedly.

Authority

Administrators or local user group members with execution rights for this command.

Example

Setting the state of the locator LED:

switch# led locator flashing

module admin-state

Syntax

module <SLOT-ID> admin-state {diagnostic | down | up}

Not supported on the 6300 Switch Series.

Description

Sets the administrative state of the specified line module.

Command context

config

32

AOS-CX 10.06 Monitoring Guide

Parameters
<SLOT-ID>

Specifies the member and slot of the module. For example, to specify the module in member 1, slot 3,
enter the following:

1/3

admin-state {diagnostic | down | up}

Selects the administrative state in which to put the specified module:
diagnostic

Selects the diagnostic administrative state. Network traffic does not pass through the module.

down

Selects the down administrative state. Network traffic does not pass through the module.

up

Selects the up administrative state. The line module is fully operational. The up state is the default
administrative state.

Authority

Administrators or local user group members with execution rights for this command.

Example

Setting the administrative state of the module in slot 1/3 to down:

switch(config)# module 1/3 admin-state down

module product-number

Syntax

module <SLOT-ID> product-number [<PRODUCT-NUM>]

no module <SLOT-ID>

Not supported on the 6300 Switch Series.

Description

Changes the configuration of the switch to indicate that the specified member and slot number contains, or
will contain, a line module.

The no form of this command removes the line module and its interfaces from the configuration. If there is
a line module installed in the slot, the line module is powered off and then powered on.

Command context

config

Parameters
<SLOT-ID>

Specifies the member and slot in the form m/s, where m is the member number, and s is the slot
number.

Chapter 5 Switch system and hardware commands

33

<PRODUCT-NUM>

Specifies the product number of the line module. For example: JL363A

If there is a line module installed in the slot when you execute this command, <PRODUCT-NUM> is
optional. The switch reads the product number information from the module that is installed in the slot.

If there is no line module installed in the slot when you execute this command, <PRODUCT-NUM> is
required.

Authority

Administrators or local user group members with execution rights for this command.

Usage

The default configuration associated with a line module slot is:

• There is no module product number or interface configuration information associated with the slot. The

slot is available for the installation with any supported line module.

• The Admin State is Up (which is the default value for Admin State).

To add a line module to the configuration, you must use the module command either before or after you
install the physical module.

If you execute the module command after you install a line module in an empty slot, you can omit the
<PRODUCT-NUM> variable. The switch reads the product information from the installed module.

If the module is not installed in the slot when you execute the module command, you must specify a value
for the <PRODUCT-NUM> variable:

• The switch validates the product number of the module against the slot number you specify to ensure

that the right type of module is configured for the specified slot.

For example, the switch returns an error if you specify the product number of a line module for a slot
reserved for management modules.

• You can configure the line module interfaces before the line module is installed.

When you install the physical line module in a preconfigured slot, the following actions occur:

•

•

If a product number was specified in the command and it matches the product number of the installed
module, the switch initializes the module.

If a product number was specified in the command and the product number of the module does not
match what was specified, the module device initialization fails.

The no form of the command removes the line module and its interfaces from the configuration and
restores the line module slot to the default configuration.

If there is a line module installed in the slot when you execute the no form of the command, the command
also powers off and then powers on the module. Traffic passing through the line module is stopped.
Management sessions connected through the line module are also affected.

If the slot associated with the line module is in the default configuration, you can remove the module from
the chassis without disrupting the operation of the switch.

Examples

Configuring slot 1/1 for future installation of a line module:

34

AOS-CX 10.06 Monitoring Guide

switch(config)# module 1/1 product-number jl363a

Configuring a line module that is already installed in slot 1/1:

switch(config)# module 1/1 product-number

Attempting to configure slot 1/1 for the future installation of a line module without specifying the product
number (returned error shown):

switch(config)# module 1/1 product-number
Line module '1/4' is not physically available.  Please provide the product
number to preconfigure the line module.

Removing a module from the configuration:

switch(config)# no module 1/1
This command will power cycle the specified line module and restore its default
configuration. Any traffic passing through the line module will be interrupted.
Management sessions connected through the line module will be affected. It
might take a few minutes to complete this operation.

Do you want to continue (y/n)? y
switch(config)#

mtrace

Syntax

mtrace <IPV4-SRC-ADDR> <IPV4-GROUP-ADDR> [lhr <IPV4-LHR-ADDR>] [ttl <HOPS>]
   [vrf <VRF-NAME>]

Description

Traces the specified IPv4 source and group addresses.

Command context

Manager (#)

Parameters
IPV4-SRC-ADDR

Specifies the source IPv4 address to trace.

IPV4-GROUP-ADDR

Specifies the group IPv4 address to trace.

lhr <IPV4-LHR-ADDR>

Specifies the last hop router address from which to start the trace.

ttl <HOPS>

Specifies the Time-To-Live duration in hops. Range: 1 to 255 hops. Default: 8 hops.

vrf <VRF-NAME>

Specifies the name of the VRF. If a name is not specified the default VRF will be used.

Authority

Administrators or local user group members with execution rights for this command.

Chapter 5 Switch system and hardware commands

35

Examples

Tracing with source, group, and LHR addresses and TTL:

(switch)# mtrace 20.0.0.1 239.1.1.1 lhr 10.1.1.1 ttl 10

Type escape sequence to abort.
Mtrace from 10.0.0.1 for Source 20.0.0.1 via Group 239.1.1.1
From destination(?) to source (?)...
Querying ful reverse path...
0  10.0.0.1
-1  30.0.0.1 PIM  0 ms
-2  40.0.0.1 PIM  2 ms
-3  50.0.0.1 PIM  100 ms
-4  60.0.0.1 PIM  156 ms
-5  20.0.0.1 PIM  123 ms

Tracing with source and group addresses:

(switch)# mtrace 200.0.0.1 239.1.1.1

Type escape sequence to abort.
Mtrace from self for Source 200.0.0.1 via Group 239.1.1.1
From destination(?) to source (?)...
Querying ful reverse path...
0  10.0.0.1
-1  30.0.0.1 PIM  0 ms
-2  40.0.0.1 PIM  2 ms
-3  50.0.0.1 PIM  100 ms
-4  60.0.0.1 PIM  156 ms
-5  200.0.0.1 PIM  123 ms

show bluetooth

Syntax

show bluetooth

Description

Shows general status information about the Bluetooth wireless management feature on the switch.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

This command shows status information about the following:

• The USB Bluetooth adapter

• Clients connected using Bluetooth

• The switch Bluetooth feature.

36

AOS-CX 10.06 Monitoring Guide

The output of the show running-config command includes Bluetooth information only if the Bluetooth
feature is disabled.

The device name given to the switch includes the switch serial number to uniquely identify the switch while
pairing with a mobile device.

The management IP address is a private network address created for managing the switch through a
Bluetooth connection.

Examples

Example output when Bluetooth is enabled but no Bluetooth adapter is connected. <XXXX> is the switch
platform and <NNNNNNNNNN> is the device identifier.

switch# show bluetooth
Enabled             : Yes
Device name         : <XXXX>-<NNNNNNNNNN>
Adapter State       : Absent

Example output when Bluetooth is enabled and there is a Bluetooth adapter connected:

switch# show bluetooth
Enabled             : Yes
Device name         : <XXXX>-<NNNNNNNNNN>
Adapter State       : Ready
Adapter IP address  : 192.168.99.1
Adapter MAC address : 480fcf-af153a

Connected Clients
-----------------
Name            MAC Address     IP Address    Connected Since
--------------  --------------  ------------  ------------------------
Mark's iPhone   089734-b12000   192.168.99.10  2018-07-09 08:47:22 PDT

Example output when Bluetooth is disabled:

switch# show bluetooth
Enabled             : No
Device name         : <XXXX>-<NNNNNNNNNN>

show boot-history

Syntax

show boot-history [all]

Description

Shows boot information. When no parameters are specified, shows the most recent information about the
boot operation, and the three previous boot operations for the active management module. When the all
parameter is specified, shows the boot information for the active management module and all available line
modules. To view boot-history on the standby, the command must be sent on the standby console.

Command context

Manager (#)

Parameters
all

Shows boot information for the active management module and all available line modules.

Chapter 5 Switch system and hardware commands

37

Authority

Administrators or local user group members with execution rights for this command.

Usage

This command displays the boot-index, boot-ID, and up time in seconds for the current boot. If there is a
previous boot, it displays boot-index, boot-ID, reboot time (based on the time zone configured in the system)
and reboot reasons. Previous boot information is displayed in reverse chronological order.

Index

The position of the boot in the history file. Range: 0 to3.

Boot ID

A unique ID for the boot . A system-generated 128-bit string.

Current Boot, up for <SECONDS> seconds

For the current boot, the show boot-history command shows the number of seconds the module
has been running on the current software.

Timestamp boot reason

For previous boot operations, the show boot-history command shows the time at which the
operation occurred and the reason for the boot. The reason for the boot is one of the following values:

<DAEMON-NAME> crash

The daemon identified by <DAEMON-NAME> caused the module to boot.

Kernel crash

The operating system software associated with the module caused the module to boot.

Reboot requested through database

The reboot occurred because of a request made through the CLI or other API.

Uncontrolled reboot

The reason for the reboot is not known.

Examples

Showing the boot history of the active management module:

switch# show boot-history
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
switch#

38

AOS-CX 10.06 Monitoring Guide

Showing the boot history of the active management module and all line modules:

switch# show boot-history all
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

show capacities

Syntax

show capacities <FEATURE> [vsx-peer]

Description

Shows system capacities and their values for all features or a specific feature.

Command context

Manager (#)

Parameters
<FEATURE>

Specifies a feature. For example, aaa or vrrp.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Capacities are expressed in user-understandable terms. Thus they may not map to a specific hardware or
software resource or component. They are not intended to define a feature exhaustively.

Chapter 5 Switch system and hardware commands

39

Examples

Showing all available capacities for BGP:

switch# show capacities bgp

System Capacities: Filter BGP
Capacities Name                                                             Value
-----------------------------------------------------------------------------------
Maximum number of AS numbers in as-path attribute                                32
...

Showing all available capacities for mirroring:

switch# show capacities mirroring

System Capacities: Filter Mirroring
Capacities Name                                                             Value
-----------------------------------------------------------------------------------
Maximum number of Mirror Sessions configurable in a system                        4
Maximum number of enabled Mirror Sessions in a system                             4

Showing all available capacities for MSTP:

switch# show capacities mstp

System Capacities: Filter MSTP
Capacities Name                                                             Value
-----------------------------------------------------------------------------------
Maximum number of mstp instances configurable in a system                        64

Showing all available capacities for VLAN count:

switch# show capacities vlan-count

System Capacities: Filter VLAN Count
Capacities Name                                                             Value
-----------------------------------------------------------------------------------
Maximum number of VLANs supported in the system                                4094

show capacities-status

Syntax

show capacities-status <FEATURE>
     [vsx-peer]

Description

Shows system capacities status and their values for all features or a specific feature.

Command context

Manager (#)

Parameters
<FEATURE>

Specifies the feature, for example aaa or vrrp for which to display capacities, values, and status.
Required.

40

AOS-CX 10.06 Monitoring Guide

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing the system capacities status for all features:

switch# show capacities-status

System Capacities Status
Capacities Status Name                                                      Value Maximum
-----------------------------------------------------------------------------------------
Number of active gateway mac addresses in a system                              0      16
Number of aspath-lists configured                                               0      64
Number of community-lists configured                                            0      64
...

Showing the system capacities status for BGP:

switch# show capacities-status bgp

System Capacities Status: Filter BGP
Capacities Status Name                                                      Value Maximum
-----------------------------------------------------------------------------------------
Number of aspath-lists configured                                               0      64
Number of community-lists configured                                            0      64
Number of neighbors configured across all VRFs                                  0      50
Number of peer groups configured across all VRFs                                0      25
Number of prefix-lists configured                                               0      64
Number of route-maps configured                                                 0      64
Number of routes in BGP RIB                                                     0  256000
Number of route reflector clients configured across all VRFs                    0      16

show core-dump

Syntax

show core-dump [all | <SLOT-ID>]

Description

Shows core dump information about the specified module. When no parameters are specified, shows only
the core dumps generated in the current boot of the management module. When the all parameter is
specified, shows all available core dumps.

Command context

Manager (#)

Parameters
all

Shows all available core dumps.

Chapter 5 Switch system and hardware commands

41

<SLOT-ID>

Shows the core dumps for the management module or line module in <SLOT-ID>. <SLOT-ID> specifies
a physical location on the switch. Use the format member/slot/port (for example, 1/3/1) for line
modules. Use the format member/slot for management modules.

You must specify the slot ID for either the active management module, or the line module.

Authority

Administrators or local user group members with execution rights for this command.

Usage

When no parameters are specified, the show core-dump command shows only the core dumps generated
in the current boot of the management module. You can use this command to determine when any crashes
are occurring in the current boot.

If no core dumps have occurred, the following message is displayed: No core dumps are present

To show core dump information for the standby management module, you must use the standby
command to switch to the standby management module and then execute the show core-dump
command.

In the output, the meaning of the information is the following:

Daemon Name

Identifies name of the daemon for which there is dump information.

Instance ID

Identifies the specific instance of the daemon shown in the Daemon Name column.

Present

Indicates the status of the core dump:

Yes

The core dump has completed and available for copying.

In Progress

Core dump generation is in progress. Do not attempt to copy this core dump.

Timestamp

Indicates the time the daemon crash occurred. The time is the local time using the time zone configured
on the switch.

Build ID

Identifies additional information about the software image associated with the daemon.

Examples

Showing core dump information for the current boot of the active management module only:

switch# show core-dump
==================================================================================
Daemon Name     | Instance ID | Present    | Timestamp             | Build ID
==================================================================================
hpe-fand          1399          Yes         2017-08-04 19:05:34      1246d2a
hpe-sysmond       957           Yes         2017-08-04 19:05:29      1246d2a
==================================================================================
Total number of core dumps : 2
==================================================================================

42

AOS-CX 10.06 Monitoring Guide

Showing all core dumps:

switch# show core-dump all
=============================================================================
Management Module core-dumps
=============================================================================
Daemon Name     | Instance ID | Present    | Timestamp           | Build ID
=============================================================================
hpe-sysmond       513           Yes         2017-07-31 13:58:05    e70f101
hpe-tempd         1048          Yes         2017-08-13 13:31:53    e70f101
hpe-tempd         1052          Yes         2017-08-13 13:41:44    e70f101

Line Module core-dumps
=============================================================================
Line Module : 1/1
=============================================================================
dune_agent_0      18958         Yes         2017-08-12 11:50:17    e70f101
dune_agent_0      18842         Yes         2017-08-12 11:50:09    e70f101
=============================================================================
Total number of core dumps : 5
=============================================================================

show domain-name

Syntax

show domain-name

Description

Shows the current domain name.

Command context

Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Usage

If there is no domain name configured, the CLI displays a blank line.

Example

Setting and showing the domain name:

switch# show domain-name

switch# config
switch(config)# domain-name example.com
switch(config)# show domain-name
example.com
switch(config)#

Chapter 5 Switch system and hardware commands

43

show environment fan

Syntax

show environment fan [vsf | vsx-peer]

Description

Shows the status information for all fans and fan trays (if present) in the system.

Command context

Manager (#)

Parameters
vsf

Shows output from the VSF member-id on switches that support VSF.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

For fan trays, Status is one of the following values:

ready

The fan tray is operating normally.

fault

The fan tray is in a fault event. The status of the fan tray does not indicate the status of fans.

empty

The fan tray is not installed in the system.

For fans:

Speed

Indicates the relative speed of the fan based on the nominal speed range of the fan. Values are:

Slow

The fan is running at less than 25% of its maximum speed.

Normal

The fan is running at 25-49% of its maximum speed.

Medium

The fan is running at 50-74% of its maximum speed.

Fast

The fan is running at 75-99% of its maximum speed.

44

AOS-CX 10.06 Monitoring Guide

Max

The fan is running at 100% of its maximum speed.

N/A

The fan is not installed.

Direction

The direction of airflow through the fan. Values are:

front-to-back

Air flows from the front of the system to the back of the system.

N/A

The fan is not installed.

Status

Fan status. Values are:

uninitialized

The fan has not completed initialization.

ok

The fan is operating normally.

fault

The fan is in a fault state.

empty

The fan is not installed.

Examples

Showing output for systems with fan trays for 6400 switch series:

switch# show environment fan
Fan tray information
------------------------------------------------------------------------------
Mbr/Tray  Description                             Status  Serial Number  Fans
------------------------------------------------------------------------------
1/1       R0X32A Aruba 6400 Fan Tray              ready   SG9ZKJL7JW     4
1/2       R0X32A Aruba 6400 Fan Tray              ready   SG9ZKJL7GL     4
1/3       R0X32A Aruba 6400 Fan Tray              ready   SG9ZKJL78L     4
1/4       R0X32A Aruba 6400 Fan Tray              ready   SG9ZKJL7GJ     4
Fan information
---------------------------------------------------------------------------
Mbr/Tray/Fan  Product  Serial Number  Speed   Direction      Status  RPM
              Name
---------------------------------------------------------------------------
1/1/1         N/A      N/A            slow    front-to-back  ok      5371
1/1/2         N/A      N/A            slow    front-to-back  ok      5320
1/1/3         N/A      N/A            slow    front-to-back  ok      5328
1/1/4         N/A      N/A            slow    front-to-back  ok      5256
1/2/1         N/A      N/A            slow    front-to-back  ok      5371
1/2/2         N/A      N/A            slow    front-to-back  ok      5349
1/2/3         N/A      N/A            slow    front-to-back  ok      5292
1/2/4         N/A      N/A            slow    front-to-back  ok      5349
1/3/1         N/A      N/A            slow    front-to-back  ok      5313
1/3/2         N/A      N/A            slow    front-to-back  ok      5371
1/3/3         N/A      N/A            slow    front-to-back  ok      5379

Chapter 5 Switch system and hardware commands

45

1/3/4         N/A      N/A            slow    front-to-back  ok      5379
1/4/1         N/A      N/A            slow    front-to-back  ok      5313
1/4/2         N/A      N/A            slow    front-to-back  ok      5299
1/4/3         N/A      N/A            slow    front-to-back  ok      5285
1/4/4         N/A      N/A            slow    front-to-back  ok      5371

Showing output for a system without a fan tray:

switch# show environment fan

Fan information
---------------------------------------------------------------
Fan   Serial Number  Speed   Direction      Status        RPM
---------------------------------------------------------------
1     SGXXXXXXXXXX   slow    front-to-back  ok            6000
2     SGXXXXXXXXXX   normal  front-to-back  ok            8000
3     SGXXXXXXXXXX   medium  front-to-back  ok            11000
4     SGXXXXXXXXXX   fast    front-to-back  ok            14000
5     SGXXXXXXXXXX   max     front-to-back  fault         16500
6     N/A            N/A     N/A            empty
...

show environment led

Syntax

show environment led [vsf <MEMBER-ID>| vsx-peer]

Description

Shows state and status information for all the configurable LEDs in the system.

Command context

Operator (>) or Manager (#)

Parameters
vsf <MEMBER-ID>

Shows output from the specified VSF member-id on switches that support VSF.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Showing state and status for LED for 6300 or 6400 switch series:

switch# show environment led
Mbr/Name       State     Status
-------------------------------
1/locator      off       ok

46

AOS-CX 10.06 Monitoring Guide

show environment power-consumption

Syntax

show environment power-consumption [vsx-peer]

Not supported on the 6300 Switch Series.

Description

Shows the power being consumed by each management module, line card, and fabric card subsystem, and
shows power consumption for the entire chassis.

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

Usage

This command is only applicable to systems that support power consumption readings.

The power consumption values are updated once every minute.

The output of this command includes the following information:

Name

Shows the member number and slot number of the management module, line module, or fabric card
module.

Type

Shows the type of module installed at the location specified by Name.

Description

Shows the product name and brief description of the module.

Usage

Shows the instantaneous power consumption of the module. Power consumption is shown in Watts.

Module Total Power Usage

Shows the total power consumption of all the modules listed. Power consumption is shown in Watts.

Chassis Total Power Usage

Shows the total instantaneous power consumed by the entire chassis, including modules and
components that do not support individual power reporting. Power consumption is shown in Watts.

Chassis Total Power Available

Shows the total amount of power, in Watts, that can be supplied to the chassis.

Chapter 5 Switch system and hardware commands

47

Chassis Total Power Allocated

Shows total power, in Watts, that is allocated to powering the chassis and its installed modules.

Chassis Total Power Unallocated

Shows the total amount of power, in Watts, that has not been allocated to powering the chassis or its
installed modules. This power can be used for additional hardware you install in the chassis.

Example

Showing the power consumption for an Aruba 6400 switch:

switch> show environment power-consumption
                                                                       Power
Name    Type                Description                                Usage
------------------------------------------------------------------------------
1/1     management-module   R0X31A 6400 Management Module              18 W
1/2     management-module                                              0 W
1/3     line-card-module                                               0 W
1/4     line-card-module    R0X39A 6400 48p 1GbE CL4 PoE 4SFP56 Mod    54 W
1/5     line-card-module                                               0 W
1/6     line-card-module    R0X39A 6400 48p 1GbE CL4 PoE 4SFP56 Mod    56 W
1/7     line-card-module    R0X39A 6400 48p 1GbE CL4 PoE 4SFP56 Mod    51 W
1/1     fabric-card-module  R0X24A 6405 Chassis                        71 W

Module Total Power Usage                                               250 W
Chassis Total Power Usage                                              294 W

Chassis Total Power Available                                          1800 W

show environment power-supply

Syntax

show environment power-supply [vsf | vsx-peer]

Description

Shows status information about all power supplies in the switch.

Command context

Operator (>) or Manager (#)

Parameters
vsf

Shows output from the VSF member-id on switches that support VSF.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

48

AOS-CX 10.06 Monitoring Guide

Usage

The following information is provided for each power supply:

Mbr/PSU

Shows the member and slot number of the power supply.

Product Number

Shows the product number of the power supply.

Serial Number

Shows the serial number of the power supply, which uniquely identifies the power supply.

PSU Status

The status of the power supply. Values are:

OK

Power supply is operating normally.

OK*

Power supply is operating normally, but it is the only power supply in the chassis. One power supply
is not sufficient to supply full power to the switch. When this value is shown, the output of the
command also shows a message at the end of the displayed data.

Absent

No power supply is installed in the specified slot.

Input fault

The power supply has a fault condition on its input.

Output fault

The power supply has a fault condition on its output.

Warning

The power supply is not operating normally.

Wattage Maximum

Shows the maximum amount of wattage that the power supply can provide.

Example

Showing the output when only one power supply is installed in an Aruba 6400 switch chassis:

switch# show environment power-supply
         Product  Serial                PSU           Wattage
Mbr/PSU  Number   Number                Status        Maximum
--------------------------------------------------------------
1/1      R0X36A   CN91KMM2H3            OK            3000
1/2      N/A      N/A                   Absent        0
1/3      N/A      N/A                   Absent        0
1/4      N/A      N/A                   Absent        0

show environment rear-display-module

Syntax

show environment rear-display-module [vsx-peer]

Chapter 5 Switch system and hardware commands

49

Description

Shows information about the display module on the back of the switch (Aruba 8400 switches only).

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

Example

Showing the rear display module information on the back of the switch:

switch> show environment rear-display-module

Rear display module is ready
Description: 8400 Rear Display Mod
Full Description: 8400 Rear Display Module
Serial number: SG00000000
Part number: 5300_0272

show environment temperature

Syntax

show environment temperature [detail] [vsf | vsx-peer]

Description

Shows the temperature information from sensors in the switch that affect fan control.

Command context

Operator (>) or Manager (#)

Parameters
detail

Shows detailed information from each temperature sensor.

vsf

Shows output from the VSF member-id on switches that support VSF.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

50

AOS-CX 10.06 Monitoring Guide

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

Temperatures are shown in Celsius.

Valid values for status are the following:

normal

Sensor is within nominal temperature range.

min

Lowest temperature from this sensor.

max

Highest temperature from this sensor.

low_critical

Lowest threshold temperature for this sensor.

critical

Highest threshold temperature for this sensor.

fault

Fault event for this sensor.

emergency

Over temperature event for this sensor.

Examples

Showing current temperature information for a 6300 switch:

switch# show environment temperature
Temperature information
------------------------------------------------------------------------------
                                                     Current
Mbr/Slot-Sensor                 Module Type        temperature  Status
------------------------------------------------------------------------------
1/1-PHY-01-04                   line-card-module     45.00 C    normal
1/1-PHY-05-08                   line-card-module     45.00 C    normal
1/1-PHY-09-12                   line-card-module     46.00 C    normal
1/1-PHY-13-16                   line-card-module     47.00 C    normal
1/1-PHY-17-20                   line-card-module     47.00 C    normal
1/1-PHY-21-24                   line-card-module     50.00 C    normal
1/1-PHY-25-28                   line-card-module     45.00 C    normal
1/1-PHY-29-32                   line-card-module     47.00 C    normal
1/1-PHY-33-36                   line-card-module     48.00 C    normal
1/1-PHY-37-40                   line-card-module     47.00 C    normal
1/1-PHY-41-44                   line-card-module     48.00 C    normal
1/1-PHY-45-48                   line-card-module     49.00 C    normal
1/1-Switch-ASIC-Internal        line-card-module     56.25 C    normal

1/1-CPU-Zone-0                  management-module    50.00 C    normal
1/1-CPU-Zone-1                  management-module    50.00 C    normal
1/1-CPU-Zone-2                  management-module    50.00 C    normal
1/1-CPU-Zone-3                  management-module    51.00 C    normal
1/1-CPU-Zone-4                  management-module    51.00 C    normal
1/1-CPU-diode                   management-module    53.12 C    normal

Chapter 5 Switch system and hardware commands

51

1/1-DDR                         management-module    45.25 C    normal
1/1-Inlet-Air                   management-module    24.88 C    normal
1/1-MB-IBC                      management-module    45.62 C    normal
1/1-Switch-ASIC-diode           management-module    58.06 C    normal

Showing detailed temperature information for a 6300 switch:

switch# show environment temperature detail
Detailed temperature information
----------------------------------------------------------------
Mbr/Slot-Sensor      : 1/1-PHY-01-04
Module Type          : line-card-module
Module Description   : JL659A 6300M 48SR5 CL6 PoE 4SFP56 Swch
Status               : normal
Fan-state            : normal
Current temperature  : 45.00 C
Minimum temperature  : 41.00 C
Maximum temperature  : 50.00 C

Mbr/Slot-Sensor      : 1/1-PHY-05-08
Module Type          : line-card-module
Module Description   : JL659A 6300M 48SR5 CL6 PoE 4SFP56 Swch
Status               : normal
Fan-state            : normal
Current temperature  : 45.00 C
Minimum temperature  : 41.00 C
Maximum temperature  : 50.00 C

...

show events

Syntax

show events [ -e <EVENT-ID> |
     -s {alert | crit | debug | emer | err | info | notice | warn} |
     -r | -a | -i  <MEMBER/SLOT> | -n <count> |
     -m {active | standby} |
     -c {lldp | ospf | ... | } |
     -d {lldpd | hpe-fand | ... |}]

For 6300 switches:

show events [ -e <EVENT-ID> |
     -s {alert | crit | debug | emer | err | info | notice | warn} |
     -r | -a | -i  <MEMBER-SLOT> | -n <count> |
     -m {master | standby} |
     -c {lldp | ospf | ... | } |
     -d {lldpd | hpe-fand | ... |}]

Description

Shows event logs generated by the switch modules since the last reboot.

Command context

Manager (#)

52

AOS-CX 10.06 Monitoring Guide

Parameters
-e <EVENT-ID>

Shows the event logs for the specified event ID. Event ID range: 101 through 99999.

-s {alert | crit | debug | emer | err | info | notice | warn}

Shows the event logs for the specified severity. Select the severity from the following list:

• alert: Displays event logs with severity alert and above.

• crit: Displays event logs with severity critical and above.

• debug: Displays event logs with all severities.

• emer: Displays event logs with severity emergency only.

• err: Displays event logs with severity error and above.

• info: Displays event logs with severity info and above.

• notice: Displays event logs with severity notice and above.

• warn: Displays event logs with severity warning and above.

-r

-a

Shows the most recent event logs first.

Shows all event logs, including those events from previous boots.

-i <MEMBER-SLOT>

Shows the event logs for the specified slot ID on a 6400 switch.

-i <MEMBER-ID>

Shows the event logs for the specified VSF member ID on a 6300 switch.

-n <count>

Displays the specified number of event logs.

-m {active | standby}

Shows the event logs for the specified management card role on an 8400 or 6400 switch. Selecting active
displays the event log for the AMM management card role and standby displays event logs for the SMM
management card role.

-m {master | standby}

Shows the event logs for the specified role on a 6200 or 6300 switch. Selecting master displays the event
log for the VSF master role and standby displays event logs for the VSF standby role.

-c {lldp | ospf | ... | }

Shows the event logs for the specified event category. Enter show event -c for a full listing of
supported categories with descriptions.

-d {lldpd | hpe-fand | ... |}

Shows the event logs for the specified process. Enter show event -d for a full listing of supported
daemons with descriptions.

Chapter 5 Switch system and hardware commands

53

Authority

Auditors or Administrators or local user group members with execution rights for this command. Auditors
can execute this command from the auditor context (auditor>) only.

Examples

Showing event logs:

switch# show events
---------------------------------------------------
show event logs
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to 70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to up for bridge_normal interface
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1 in Hardware

Showing the most recent event logs first:

switch# show events -r
---------------------------------------------------
show event logs
---------------------------------------------------
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1 in Hardware
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to up for bridge_normal interface
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to 70:72:cf:51:50:7c

Showing all event logs:

switch# show events -a
---------------------------------------------------
show event logs
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to 70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to up for bridge_normal interface
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1 in Hardware

Showing event logs related to the DHCP relay agent:

switch# show events -c dhcp-relay
2016-05-31:06:26:27.363923|hpe-relay|110001|LOG_INFO|DHCP Relay Enabled
2016-05-31:07:08:51.351755|hpe-relay|110002|LOG_INFO|DHCP Relay Disabled

Showing event logs related to the DHCPv6 relay agent:

switch# show events -c dhcpv6-relay
2016-05-31:06:26:27.363923|hpe-relay|109001|LOG_INFO|DHCPv6 Relay Enabled
2016-05-31:07:08:51.351755|hpe-relay|109002|LOG_INFO|DHCPv6 Relay Disabled

Showing event logs related to IRDP:

switch# switch# show events -c irdp
2016-05-31:06:26:27.363923|hpe-rdiscd|111001|LOG_INFO|IRDP enabled on interface %s
2016-05-31:07:08:51.351755|hpe-rdiscd|111002|LOG_INFO|IRDP disabled on interface %s

Showing event logs related to LACP:

switch# show events -c lacp
---------------------------------------------------
show event logs
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to 70:72:cf:51:50:7c

Showing event logs as per the specified management card role for a switch:

switch# show events -m master
---------------------------------------------------
show event logs
---------------------------------------------------
2020-04-22T05:36:13.348594+00:00 6300 lldpd[3055]: Event|109|LOG_INFO|MSTR|1|Configured LLDP tx-delay to 2
2020-04-22T05:36:14.430166+00:00 6300 vrfmgrd[3053]: Event|5401|LOG_INFO|MSTR|1|Created a vrf entity b1721d27-41c2-485d-9bae-2cfcbc9bd13d
2020-04-22T05:36:14.942597+00:00 6300 vrfmgrd[3053]: Event|5401|LOG_INFO|MSTR|1|Created a vrf entity 5eb532c9-5b4d-4d83-b34a-db24ae542d4e

54

AOS-CX 10.06 Monitoring Guide

Showing event logs as per the specified slot ID:

switch# show events -i 1
---------------------------------------------------
Event logs from current boot
---------------------------------------------------
2020-04-22T05:36:14.430166+00:00 6300 vrfmgrd[3053]: Event|5401|LOG_INFO|MSTR|1|Created a vrf entity b1721d27-41c2-485d-9bae-2cfcbc9bd13d
2020-04-22T05:36:14.942597+00:00 6300 vrfmgrd[3053]: Event|5401|LOG_INFO|MSTR|1|Created a vrf entity 5eb532c9-5b4d-4d83-b34a-db24ae542d4e
2020-04-22T05:36:15.886252+00:00 6300 vsfd[710]: Event|9903|LOG_INFO|MSTR|1|Master 1 boot complete

Showing event logs as per the specified process:

switch# show events -d lacpd
---------------------------------------------------
show event logs
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to 70:72:cf:51:50:7c

Displaying the specified number of event logs:

switch# show events -n 5
---------------------------------------------------
show event logs
---------------------------------------------------
2018-03-21:06:12:15.500603|arpmgrd|6101|LOG_INFO|AMM|-|ARPMGRD daemon has started
2018-03-21:06:12:17.734405|lldpd|109|LOG_INFO|AMM|-|Configured LLDP tx-delay to 2
2018-03-21:06:12:17.740517|lacpd|1307|LOG_INFO|AMM|-|LACP system ID set to 70:72:cf:d4:34:42
2018-03-21:06:12:17.743491|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity 42cc3df7-1113-412f-b5cb-e8227b8c22f2
2018-03-21:06:12:17.904008|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity 4409133e-2071-4ab8-adfe-f9662c06b889

show fabric

Syntax

show fabric [<SLOT-ID>] [vsx-peer]

Not supported on the 6300 Switch Series.

Description

Shows information about the installed fabrics.

Command context

Operator (>) or Manager (#)

Parameters
<SLOT-ID>

Specifies the member and slot of the fabric to show. For example, to show the module in member 1, slot
2, enter the following:

1/2

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing all fabrics on Aruba 6400 switches that have two fabrics:

Chapter 5 Switch system and hardware commands

55

switch# show fabric

Fabric Modules
==============

     Product                                    Serial
Name Number  Description                        Number     Status
---- ------- --------------------------------   ---------- ----------------
1/1  R0X25A  6410 Chassis                       SG9ZKM9999 Ready
1/2  R0X25A  6410 Chassis                       SG9ZKM9999 Ready

Showing all fabrics on Aruba 6400 switches that have one fabric:

switch# show fabric

Fabric Modules
==============

     Product                                        Serial
Name Number  Description                            Number     Status
---- ------- -------------------------------------- ---------- ----------------
1/1  R0X24A  6405 Chassis                           SG9ZKM9076 Ready

Showing a single fabric module on Aruba 6400 switches:

switch# show fabric 1/1

Fabric module 1/1 is ready
Admin state: Up
Description: 6405 Chassis
Full Description: 6405 Chassis
Serial number: SG00000000
Product number: R0X24A

show hostname

Syntax

show hostname [vsx-peer]

Description

Shows the current host name.

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

Setting and showing the host name:

56

AOS-CX 10.06 Monitoring Guide

switch# show hostname
switch
switch# config
switch(config)# hostname myswitch
myswitch(config)# show hostname
myswitch

show images

Syntax

show images [vsx-peer]

Description

Shows information about the software in the primary and secondary images.

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

Example

Showing the primary and secondary images on a 6300 switch:

switch(config)# show images
---------------------------------------------------------------------------
ArubaOS-CX Primary Image
---------------------------------------------------------------------------
Version : FL.xx.xx.xxxx
Size    : 722 MB
Date    : 2019-10-22 17:00:46 PDT
SHA-256 : 4c84e49c0961fc56b5c7eab064750a333f1050212b7ce2fab587d13469d24cfa

---------------------------------------------------------------------------
ArubaOS-CX Secondary Image
---------------------------------------------------------------------------
Version : FL.xx.xx.xxxx
Size    : 722 MB
Date    : 2019-10-22 17:00:46 PDT
SHA-256 : 4c84e49c0961fc56b5c7eab064750a333f1050212b7ce2fab587d13469d24cfa

Default Image : secondary

------------------------------------------------------
Management Module 1/1 (Active)
------------------------------------------------------
Active Image       : secondary

Chapter 5 Switch system and hardware commands

57

Service OS Version : FL.01.05.0001-internal
BIOS Version       : FL.01.0001

Showing the primary and secondary images on a 6400 switch:

switch(config)# show images
---------------------------------------------------------------------------
ArubaOS-CX Primary Image
---------------------------------------------------------------------------
Version : FL.xx.xx.xxxxQ-2710-gd4ac39f30c9
Size    : 766 MB
Date    : 2019-10-30 17:22:01 PDT
SHA-256 : e560ca9141f425d19024d122573c5ff730df2a9a726488212263b45ea00382cf

---------------------------------------------------------------------------
ArubaOS-CX Secondary Image
---------------------------------------------------------------------------
Version : FL.xx.xx.xxxx
Size    : 722 MB
Date    : 2019-10-21 19:36:26 PDT
SHA-256 : 657e28adc1b512217ce780e3523c37c94db3d3420231deac1ab9aaa8324dc6b9

Default Image : secondary

------------------------------------------------------
Management Module 1/1 (Active)
------------------------------------------------------
Active Image       : secondary
Service OS Version : FL.01.05.0001-internal
BIOS Version       : FL.01.0001

show ip errors

Syntax

show ip errors [vsx-peer]

Description

Shows IP error statistics for packets received by the switch since the switch was last booted.

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

Usage

IP error info about received packets is collected from each active line card on the switch and is preserved
during failover events. Error counts are cleared when the switch is rebooted.

58

AOS-CX 10.06 Monitoring Guide

Drop reasons are the following:

Malformed packet

The packet does not conform to TCP/IP protocol standards such as packet length or internet header
length.

A large number of malformed packets can indicate that there are hardware malfunctions such as loose
cables, network card malfunctions, or that a DOS (denial of service) attack is occurring.

IP address error

The packet has an error in the destination or source IP address. Examples of IP address errors include
the following:

• The source IP address and destination IP address are the same.

• There is no destination IP address.

• The source IP address is a multicast IP address.

• The forwarding header of an IPv6 address is empty.

• There is no source IP address for an IPv6 packet.

Invalid TTLs

The TTL (time to live) value of the packet reached zero. The packet was discarded because it traversed
the maximum number of hops permitted by the TTL value.

TTLs are used to prevent packets from being circulated on the network endlessly.

Example

Showing ip error statistics for packets received by the switch:

switch# show ip errors
----------------------------------
Drop reason                Packets
----------------------------------
Malformed packets                1
IP address errors               10
...

show module

Syntax

show module [<SLOT-ID>] [vsx-peer]

Description

Shows information about installed line modules and management modules.

Command context

Operator (>) or Manager (#)

Chapter 5 Switch system and hardware commands

59

Parameters
<SLOT-ID>

Specifies the member and slot numbers in format member/slot. For example, to show the module in
member 1, slot 3, enter 1/3.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

Identifies and shows status information about the line modules and management modules that are installed
in the switch.

If you use the <SLOT-ID> parameter to specify a slot that does not have a line module installed, a message
similar to the following example is displayed:

Module 1/4 is not physically present.

To show the configuration information—if any—associated with that line module slot, use the show
running-configuration command.

Status is one of the following values:

Active

This module is the active management module.

Standby

This module is the standby management module.

Deinitializing

The module is being deinitialized.

Diagnostic

The module is in a state used for troubleshooting.

Down

The module is physically present but is powered down.

Empty

The module hardware is not installed in the chassis.

Failed

The module has experienced an error and failed.

Failover

This module is a fabric module or a line module, and it is in the process of connecting to the new active
management module during a management module failover event.

Initializing

The module is being initialized.

60

AOS-CX 10.06 Monitoring Guide

Present

The module hardware is installed in the chassis.

Ready

The module is available for use.

Updating

A firmware update is being applied to the module.

Examples

Showing all installed modules (Aruba 6300 switch):

switch(config)# show module

Management Modules
==================

     Product                                        Serial
Name Number  Description                            Number     Status
---- ------- -------------------------------------- ---------- ----------------
1/1  JL659A  6300M 48SR5 CL6 PoE 4SFP56 Swch        ID9ZKHN090 Active (local)

Line Modules
============

     Product                                        Serial
Name Number  Description                            Number     Status
---- ------- -------------------------------------- ---------- ----------------
1/1  JL659A  6300M 48SR5 CL6 PoE 4SFP56 Swch        ID9ZKHN090 Ready

Showing a line module (Aruba 6400 switch):

switch# show module 1/3

Line module 1/3 is ready
 Admin state: Up
 Description: 6400 24p 10GT 4SFP56 Mod
 Full Description: 6400 24-port 10GBASE-T and 4-port SFP56 Module
 Serial number: SG9ZKMS045
 Product number: R0X42A
 Power priority: 128

Showing a slot that does not contain a line module:

switch(config)# show module 1/3
Module 1/3 is not physically present

show running-config

Syntax

show running-config [<FEATURE>] [all] [vsx-peer]

Description

Shows the current nondefault configuration running on the switch. No user information is displayed.

Chapter 5 Switch system and hardware commands

61

Command context

Manager (#)

Parameters
<FEATURE>

Specifies the name of a feature. For a list of feature names, enter the show running-config
command, followed by a space, followed by a question mark (?). When the json parameter is used, the
vsx-peer parameter is not applicable.

all

Shows all default values for the current running configuration.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing the current running configuration:

switch> show running-config
Current configuration:
!
!Version ArubaOS-CX 10.0X.XXXX
!
lldp enable
linecard-module LC1 part-number JL363A
vrf green
!
!
!
!
!
!
aaa authentication login default local
aaa authorization commands default none
!
!
!
!
router ospf 1 vrf green
    area 0.0.0.0
router pim vrf green
    enable
    rp-address 30.0.0.4
vlan 1
    no shutdown
vlan 20
    no shutdown
vlan 30
    no shutdown
interface 1/1/1
    no shutdown
    no routing
    vlan access 30

62

AOS-CX 10.06 Monitoring Guide

interface 1/1/32
    no shutdown
    no routing
    vlan access 20
interface bridge_normal-1
    no shutdown
interface bridge_normal-2
    no shutdown
interface vlan20
    no shutdown
    vrf attach green
    ip address 20.0.0.44/24
    ip ospf 1 area 0.0.0.0
    ip pim-sparse enable

interface vlan30
    no shutdown
    vrf attach green
    ip address 30.0.0.44/24
    ip ospf 1 area 0.0.0.0
    ip pim-sparse enable

    ip pim-sparse hello-interval 100

Showing the current running configuration in json format:

switch> show running-config json
Running-configuration in JSON:
{
    "Monitoring_Policy_Script": {
        "system_resource_monitor_mm1.1.0": {
            "Monitoring_Policy_Instance": {
                "system_resource_monitor_mm1.1.0/system_resource_monitor_mm1.1.0.default": {
                    "name": "system_resource_monitor_mm1.1.0.default",
                    "origin": "system",
                    "parameters_values": {
                        "long_term_high_threshold": "70",
                        "long_term_normal_threshold": "60",
                        "long_term_time_period": "480",
                        "medium_term_high_threshold": "80",
                        "medium_term_normal_threshold": "60",
                        "medium_term_time_period": "120",
                        "short_term_high_threshold": "90",
                        "short_term_normal_threshold": "80",
                        "short_term_time_period": "5"
                    }
                }
            },
...
...
...
...

Show the current running configuration without default values:

switch(config)# show running-config
Current configuration:
!
!Version ArubaOS-CX Virtual.10.04.0000-6523-gbb15c03~dirty
led locator on
!
!
!
!
!
!

Chapter 5 Switch system and hardware commands

63

!
!
!
vlan 1
switch(config)# show running-config all
Current configuration:
!
!Version ArubaOS-CX Virtual.10.04.0000-6523-gbb15c03~dirty
led locator on
!
!
!
!
!
!
!
!
!
vlan 1
switch(config)#

Show the current running configuration with default values:

switch(config)# snmp-server vrf mgmt
switch(config)# show running-config
Current configuration:
!
!Version ArubaOS-CX Virtual.10.04.0000-6523-gbb15c03~dirty
led locator on
!
!
!
!
snmp-server vrf mgmt
!
!
!
!
!
vlan 1
switch(config)#
switch(config)#
switch(config)# show running-config all
Current configuration:
!
!Version ArubaOS-CX Virtual.10.04.0000-6523-gbb15c03~dirty
led locator on
!
!
!
!
snmp-server vrf mgmt
snmp-server agent-port 161
snmp-server community public
!
!
!
!
!
vlan 1
switch(config)#

64

AOS-CX 10.06 Monitoring Guide

show running-config current-context

Syntax

show running-config current-context

Description

Shows the current non-default configuration running on the switch in the current command context.

Command context

config or a child of config. See Usage.

Authority

Administrators or local user group members with execution rights for this command.

Usage

You can enter this command from the following configuration contexts:

• Any child of the global configuration (config) context. If the child context has instances—such as

interfaces—you can enter the command in the context of a specific instance.

Support for this command is provided for one level below the config context. For example, entering this
command for a child of a child of the config context not supported.

If you enter the command on a child of the config context, the current configuration of that context and
the children of that context are displayed.

• The global configuration (config) context.

If you enter this command in the global configuration (config) context, it shows the running
configuration of the entire switch. Use the show running-configuration command instead.

Examples

On the 6400 Switch Series, interface identification differs.

Showing the running configuration for the current interface:

switch(config-if)# show running-config current-context
interface 1/1/1
    vsx-sync qos vlans
    no shutdown
    description Example interface
vlan access 1
    exit

Showing the current running configuration for the management interface:

switch(config-if-mgmt)# show running-config current-context
interface mgmt
    no shutdown
    ip static 10.0.0.1/24
    default-gateway 10.0.0.8
    nameserver 10.0.0.1

Showing the running configuration for the external storage share named nasfiles:

Chapter 5 Switch system and hardware commands

65

switch(config-external-storage-nasfiles)# show running-config current-context
external-storage nasfiles
   address 192.168.0.1
   vrf default
   username nasuser
   password ciphertext AQBapalKj+XMsZumHEwIc9OR6YcOw5Z6Bh9rV+9ZtKDKzvbaBAAAAB1CTrM=
   type scp
   directory /home/nas
   enable
switch(config-external-storage-nasfiles)#

Showing the running configuration for a context that does not have instances:

switch(config-vsx)# show run current-context
vsx
    inter-switch-link 1/1/1
    role secondary
    vsx-sync sflow time

show startup-config

Syntax

show startup-config [json]

Description

Shows the contents of the startup configuration.

NOTE: Switches in the factory-default configuration do not have a startup configuration to
display.

Command context

Manager (#)

Parameters
json

Display output in JSON format.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing the startup-configuration in non-JSON format for a 6300 switch:

switch(config)# show startup-config
Startup configuration:
!
!Version ArubaOS-CX FL.xx.xx.xxxx
!export-password: default
hostname BLDG01-F1
user admin group administrators password ciphertext
AQBapWl8I2ZunZ43NE/8KlbQ7zYC4gTT6uSFYi6n6wyY9PdBYgAAACONCR/3+AcNvzRBch0DoG7W9z84LpJA+6C9SKfNwCqi5/
nUPk/ZOvN91/EQXvPNkHtBtQWyYZqfkebbEH78VWRHfWZjApv4II9qmQfxpA79wEvzshdzZmuAKrm
user ateam group administrators password ciphertext
AQBapcPqMXoF+H10NKrqAedXLvlSRwf4wUEL22hXGD6ZBhicYgAAAGsbh70DKg1u+Ze1wxgmDXjkGO3bseYiR3LKQg66vrfrqR/
M3oLlliPdZDnq9XMMvCL+7jBbYhYes8+uDxuSTh8kdkd/qj3lo5FUuC5fENgCjU0YI1l7qtU+YEnsj
!
!

66

AOS-CX 10.06 Monitoring Guide

!
!
radius-server host 10.10.10.15
!
radius dyn-authorization enable
ssh server vrf default
ssh server vrf mgmt
!
!
!
!
!
router ospf 1
    router-id 1.63.63.1
    area 0.0.0.0
vlan 1
vlan 66
    name vlan66
vlan 67
    name vlan67
vlan 999
    name vlan999
vlan 4000
spanning-tree
interface mgmt
    no shutdown
    ip static 10.6.9.15/24
    default-gateway 10.6.9.1

Showing the startup-configuration in JSON format:

switch# show startup-config json
Startup configuration:
{
    "AAA_Server_Group": {
        "local": {
            "group_name": "local"
        },
        "none": {
            "group_name": "none"
        }
    },
...

show system

Syntax

show system [vsx-peer]

Description

Shows general status information about the system.

Command context

Operator (>) or Manager (#)

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Chapter 5 Switch system and hardware commands

67

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

CPU utilization represents the average utilization across all the CPU cores.

System Contact, System Location, and System Description can be set with the snmp-server command.

Examples

Showing system information on a 6300 switch:

switch(config)# show system
Hostname           : switch
System Description : FL.10.xx.xxxxx
System Contact     :
System Location    :

Vendor             : Aruba
Product Name       : JL659A 6300M 48SR5 CL6 PoE 4SFP56 Swch
Chassis Serial Nbr : ID9ZKHN090
Base MAC Address   : 9020c2-245080
ArubaOS-CX Version : FL.10.xx.xxxx

Time Zone          : UTC

Up Time            : 5 days, 15 hours, 33 minutes
CPU Util (%)       : 21
Memory Usage (%)   : 19

Showing system information om a 6400 switch:

switch(config)# show system
Hostname           : switch
System Description : FL.10.xx.xxxxx
System Contact     :
System Location    :

Vendor             : Aruba
Product Name       : R0X24A 6405 Chassis
Chassis Serial Nbr : SG9ZKM7206
Base MAC Address   : 9020c2-dc4700
ArubaOS-CX Version : FL.10.xx.xxxxx

Time Zone          : UTC

Up Time            : 32 minutes
CPU Util (%)       : 3
Memory Usage (%)   : 10
BLDG02-F3(config)#

show system error-counter-monitor

Syntax

show system error-counter-monitor {basic <PORT-NUM> | extended} [vsx-peer]

68

AOS-CX 10.06 Monitoring Guide

Description

Shows error counter statistics.

Command context

Manager (#)

Parameters
basic <PORT-NUM>

Specifies a physical port on the switch. Use the format member/slot/port (for example, 1/3/1).

extended

Shows statistics for all interfaces.

Command context

Manager (#)

Examples

Showing error counter statistics for interface 1/1/1:

switch# show system error-counter-monitor basic 1/1/1

Interface error counter statistics for 1/1/1

Error Counter                      Value
-----------------------------------------
EtherStatsOversizePkts             983
EtherStatsUndersizePkts            1024
EtherStatsJabbers                  10
Dot3StatsAlignmentErrors           462
Dot3StatsFCSErrors                 321
Dot3StatsLateCollisions            2024
EtherStatsFragments                121
Dot3StatsExcessiveCollisions       1025
IfInBroadcastPkts                  2001

Showing error counter statistics for all interfaces:

switch# show system error-counter-monitor extended

Interface error counter statistics for 1/1/1

Error Counter                      Value
-----------------------------------------
EtherStatsOversizePkts             983
EtherStatsUndersizePkts            1024
EtherStatsJabbers                  10
Dot3StatsAlignmentErrors           462
Dot3StatsFCSErrors                 321
Dot3StatsLateCollisions            2024
EtherStatsFragments                121
Dot3StatsExcessiveCollisions       1025
IfInBroadcastPkts                  2001
...
...
Interface error counter statistics for 1/8/32

Error Counter                     Value
-----------------------------------------

Chapter 5 Switch system and hardware commands

69

EtherStatsOversizePkts             0
...

show system resource-utilization

Syntax

show system resource-utilization [daemon <DAEMON-NAME> | module <SLOT-ID>] [vsx-peer]

Description

Shows information about the usage of system resources such as CPU, memory, and open file descriptors.

Command context

Manager (#)

Parameters
daemon <DAEMON-NAME>

Shows the filtered resource utilization data for the process specified by <DAEMON-NAME> only.

NOTE: For a list of daemons that log events, enter show events -d ? from a switch
prompt in the manager (#) context.

module <SLOT-ID>

Shows the filtered resource utilization data for the line module specified by <SLOT-ID> only.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing all system resource utilization data:

switch# show system resource-utilization
System Resources:
Processes: 70
CPU usage(%): 20
Memory usage(%): 25
Open FD's: 1024

Process             CPU Usage(%)         Memory Usage(%)    Open FD's
-----------------------------------------------------------------------
pmd                    2                      1                14
hpe-sysmond            1                      2                11
hpe-mgmdd              0                      1                5
...

Showing the resource utilization data for the pmd process:

switch# show system resource-utilization daemon pmd
Process             CPU Usage         Memory Usage    Open FD's

70

AOS-CX 10.06 Monitoring Guide

-----------------------------------------------------------------------
pmd                     2                1             14

Showing resource utilization data when system resource utilization polling is disabled:

switch# show system resource-utilization
System resource utilization data poll is currently disabled

Showing resource utilization data for a line module:

switch# show system resource-utilization module 1/1
System Resource utilization for line card module: 1/1
CPU usage(%): 0
Memory usage(%): 35
Open FD's: 512

show tech

Syntax

show tech [basic | <FEATURE>] [local-file]

Description

Shows detailed information about switch features by automatically running the show commands associated
with the feature. If no parameters are specified, the show tech command shows information about all
switch features. Technical support personnel use the output from this command for troubleshooting.

Command context

Manager (#)

Parameters
basic

Specifies showing a basic set of information.

<FEATURE>

Specifies the name of a feature. For a list of feature names, enter the show tech command, followed by
a space, followed by a question mark (?).

local-file

Shows the output of the show tech command to a local text file.

Authority

Administrators or local user group members with execution rights for this command.

Usage

To terminate the output of the show tech command, enter Ctrl+C.

If the command was not terminated with Ctrl+C, at the end of the output, the show tech command shows
the following:

• The time consumed to execute the command.

• The list of failed show commands, if any.

Chapter 5 Switch system and hardware commands

71

To get a copy of the local text file content created with the show tech command that is used with the local-
file parameter, use the copy show-tech local-file command.

Example

Showing the basic set of system information:

switch# show tech basic
=============================================================
Show Tech executed on Wed Sep  6 16:50:37 2017
=============================================================
=============================================================
[Begin] Feature basic
=============================================================

*******************************
Command : show core-dump all
*******************************
no core dumps are present

...
=============================================================
[End] Feature basic
=============================================================

=============================================================
1 show tech command failed
=============================================================
Failed command:
  1. show boot-history
=============================================================
Show tech took 3.000000 seconds for execution

Directing the output of the show tech basic command to the local text file:

switch# show tech basic local-file
Show Tech output stored in local-file. Please use 'copy show-tech local-file'
to copy-out this file.

show usb

Syntax
show usb

Description

Shows the USB port configuration and mount settings.

Command context

Operator (>) or Manager (#)

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

72

AOS-CX 10.06 Monitoring Guide

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

If USB has not been enabled:

switch> show usb
Enabled: No
Mounted: No

If USB has been enabled, but no device has been mounted:

switch> show usb
Enabled: Yes
Mounted: No

If USB has been enabled and a device mounted:

switch> show usb
Enabled: Yes
Mounted: Yes

show usb file-system

Syntax
show usb file-system [<PATH>]

Description

Shows directory listings for a mounted USB device. When entered without the <PATH> parameter the top
level directory tree is shown.

Command context

Operator (>) or Manager (#)

Parameters

<PATH>

Specifies the file path to show. A leading "/" in the path is optional.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

Adding a leading "/" as the first character of the <PATH> parameter is optional.

Attempting to enter '..' as any part of the <PATH> will generate an invalid path argument error. Only fully-
qualified path names are supported.

Examples

Showing the top level directory tree:

Chapter 5 Switch system and hardware commands

73

switch# show usb file-system
/mnt/usb:
'System Volume Information'  dir1'

/mnt/usb/System Volume Information':
IndexerVolumeGuid  WPSettings.dat

/mnt/usb/dir1:
dir2  test1

/mnt/usb/dir1/dir2:
test2

Showing available path options from the top level:

switch# show usb file-system /
total 64
drwxrwxrwx 2 32768 Jan 22 16:27 'System Volume Information'
drwxrwxrwx 3 32768 Mar  5 15:26 dir1

Showing the contents of a specific folder:

switch# show usb file-system /dir1
total 32
drwxrwxrwx 2 32768 Mar  5 15:26 dir2
-rwxrwxrwx 1     0 Feb  5 18:08 test1

switch# show usb file-system dir1/dir2
total 0
-rwxrwxrwx 1 0 Feb  6 05:35 test2

Attempting to enter an invalid character in the path:

switch# show usb file-system dir1/../..
Invalid path argument

show version

Syntax

show version [vsx-peer]

Description

Shows version information about the network operating system software, service operating system
software, and BIOS.

Command context

Operator (>) or Manager (#)

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

74

AOS-CX 10.06 Monitoring Guide

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Showing version information for a 6300 switch:

switch(config)# show version
-----------------------------------------------------------------------------
ArubaOS-CX
(c) Copyright 2017-2020 Hewlett Packard Enterprise Development LP
-----------------------------------------------------------------------------
Version      : FL.xx.xx.xxxx
Build Date   : 2020-10-22 17:00:46 PDT
Build ID     : ArubaOS-CX:FL.xx.xx.xxxx:85c3c2f3d59e:201910222335
Build SHA    : 85c3c2f3d59ec8318ba97178fad387aecb671b33
Active Image : secondary

Service OS Version : FL.01.05.0001-internal
BIOS Version       : FL.01.0001

system resource-utilization poll-interval

Syntax

system resource-utilization poll-interval <SECONDS>

Description

Configures the polling interval for system resource information collection and recording such as CPU and
memory usage.

Command context

config

Parameters
<SECONDS>

Specifies the poll interval in seconds. Range: 10-3600. Default: 10.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configuring the system resource utilization poll interval:

switch(config)# system resource-utilization poll-interval 20

top cpu

Syntax

top cpu

Chapter 5 Switch system and hardware commands

75

Description

Shows CPU utilization information.

Command context

Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Showing top CPU information:

switch# top cpu
top - 09:42:55 up 3 min, 3 users, load average: 3.44, 3.78, 1.70
Tasks:  76 total, 2 running, 74 sleeping,  0 stopped,  0 zombie
%Cpu(s): 31.4 us, 32.7 sy, 0.5 ni, 34.4 id, 04. wa, 0.0 hi, 0.6 si, 0.0 st
KiB Mem : 4046496 total,  2487508 free,  897040 used,   661948 buff/cache
KiB Swap:       0 total,        0 free,       0 used,  2859196 avail Mem

  PID USER     PRI  NI   VIRT    RES   SHR S  %CPU %MEM      TIME+ COMMAND
...

top memory

Syntax

top memory

Description

Shows memory utilization information.

Command context

Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Showing top memory:

switch> top memory
top - 09:42:55 up 3 min, 3 users, load average: 3.44, 3.78, 1.70
Tasks:  76 total, 2 running, 74 sleeping,  0 stopped,  0 zombie
%Cpu(s): 31.4 us, 32.7 sy, 0.5 ni, 34.4 id, 04. wa, 0.0 hi, 0.6 si, 0.0 st
KiB Mem : 4046496 total,  2487508 free,  897040 used,   661948 buff/cache
KiB Swap:       0 total,        0 free,       0 used,  2859196 avail Mem

  PID USER     PRI  NI   VIRT    RES   SHR S  %CPU %MEM      TIME+ COMMAND
...

76

AOS-CX 10.06 Monitoring Guide

usb

Syntax

usb

no usb

Description

Enables the USB ports on the switch. This setting is persistent across switch reboots and management
module failovers. Both active and standby management modules are affected by this setting.

The no form of this command disables the USB ports.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Example

Enabling USB ports:

switch(config)# usb

Disabling USB ports when a USB drive is mounted:

switch(config)# no usb

usb mount | unmount

Syntax

usb {mount | unmount}

Description

Enables or disables the inserted USB drive.

Command context

Manager (#)

Parameters
mount

Enables the inserted USB drive.

unmount

Disables the inserted USB drive in preparation for removal.

Authority

Administrators or local user group members with execution rights for this command.

Chapter 5 Switch system and hardware commands

77

Usage

If USB has been enabled in the configuration, the USB port on the active management module is available
for mounting a USB drive. The USB port on the standby management module is not available.

An inserted USB drive must be mounted each time the switch boots or fails over to a different management
module.

A USB drive must be unmounted before removal.

The supported USB file systems are FAT16 and FAT32.

Examples

Mounting a USB drive in the USB port:

switch# usb mount

Unmounting a USB drive:

switch# usb unmount

78

AOS-CX 10.06 Monitoring Guide

Chapter 6
External storage

The switch has limited capacity to store data, collected by switch features and protocols. You can provide
virtually unlimited storage capacity by adding user-supplied external storage volumes. Supported volume
types and storage protocols include: NFSv3, NFSv4, and SCP (sshfs).

One application of external storage is the saving and restoring of DHCP lease files over SCP or NFS network
attached storage systems. SCP file system protocol uses a user mode process to emulate a network file
system. The key advantage is packet level encryption and simple configuration. The key disadvantage is slow
performance.

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

External storage commands

address

Syntax

address {<IPV4-ADDR> | <IPV6-ADDR> | hostname <HOSTNAME>}

no address {<IPV4-ADDR> | <IPV6-ADDR> | hostname <HOSTNAME>}

Description

Specifies the NAS IP address or hostname.

The no form of this command deletes an IP address or hostname.

Command context

config-external-storage-<VOLUME-NAME>

Parameters
<IPV4-ADDR>

Specifies the NAS server IPv4 address, Global.

<IPV6-ADDR>

Specifies the IPv6 address of the NAS server.

Chapter 6 External storage

79

<HOSTNAME>

Specifies the hostname of the NAS server. String.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating the logfiles storage volume with IP address 10.1.1.1:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# address 10.1.1.1

Deleting an external storage volume named logfiles:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# no address 10.1.1.1

directory

Syntax

directory <DIRECTORY-NAME>

no directory <DIRECTORY-NAME>

Description

Selects an existing directory on the external storage volume.

The no form of this command clears a directory of an external storage volume.

Command context

config-external-storage-<VOLUME-NAME>

Parameters
<DIRECTORY-NAME>

Specifies the external storage directory for mapping the volume.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Creating a volume named logfiles that is mapped under /home on the server:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# directory /home

Clearing the directory /home:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# no directory /home

80

AOS-CX 10.06 Monitoring Guide

disable

Syntax

disable

no disable

Description

Disables the external storage volume.

The no form of this command enables the external storage volume. This is identical to the enable
command.

Command context

config-external-storage-<VOLUME-NAME>

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Disabling a volume named logfiles:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# disable

enable

Syntax

enable

no enable

Description

Enables the external storage volume.

The no form of this command disables the external storage volume. This is identical to the disable
command.

Command context

config-external-storage-<VOLUME-NAME>

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Creating and then enabling a volume named logfiles:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# enable

Chapter 6 External storage

81

Disables the external storage volume:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# disable

external-storage

Syntax

external-storage <VOLUME-NAME>

no external-storage <VOLUME-NAME>

Description

Creates or updates an external storage volume.

The no form of this command deletes an external storage volume.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating the logfiles storage volume:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)#

Deleting the logfiles storage volume:

switch(config)# no external-storage logfiles

password

Syntax

password {plaintext | ciphertext} <PASSWORD>

no password {plaintext | ciphertext} <PASSWORD>

Description

Sets the password for logging in to a network attached storage server.

The no form of this command clears the password for logging in to a network attached storage server.

Command context

config-external-storage-<VOLUME-NAME>

Parameters
plaintext

Specifies the password be in plain text format.

82

AOS-CX 10.06 Monitoring Guide

ciphertext

Specifies the password be in ciphertext format.

<PASSWORD>

Specifies the password.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating a volume named logfiles with the password xxxx:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# password plaintext xxxx

Clearing the plaintext password xxxx:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# no password plaintext xxxx

show external-storage

Syntax

show external-storage [<VOLUME-NAME>]

Description

Shows external storage configuration and state for all volumes or for a specified volume.

Command context

Operator (>) or Manager (#)

Parameters
<VOLUME-NAME>

Specifies the external storage volume name that the show command will use.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch# show external-storage

------------------------------------------------------------------------------------
           Address      VRF      Username      Type       Directory     State
------------------------------------------------------------------------------------
nfsvol     10.1.1.1     nas      ---           NFSv3      /home         operational
nfsfiles   20.1.1.1     nas      netstorage    NFSv4      /netstor      disabled
scpdev     nasserver    nas      scpstor       SCP        /scp          unaccessible

Chapter 6 External storage

83

show running-config external-storage

Syntax

show running-config external-storage

Description

Shows the running configuration of the external storage.

Command context

Operator (>) or Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

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

type

Syntax

type {nfsv3 | nfsv4 | scp}

no type {nfsv3 | nfsv4 | scp}

Description

Sets the network attached storage access type for reaching the external storage volume.

The no form of this command deletes an external storage volume.

Command context

config-external-storage-<VOLUME-NAME>

Parameters
nfsv3

Specifies the NFSv3 network access protocol.

84

AOS-CX 10.06 Monitoring Guide

nfsv4

Specifies the NFSv4 network access protocol.

scp

Specifies the SCP network access protocol.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating the logfiles volume using NFSV4:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# type nfsv4

Clearing the external storage access type:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# no type nfsv4

username

Syntax

username <USER-NAME>

no username <USER-NAME>

Description

Sets the username for logging in to a network attached storage server.

The no form of this command clears a username.

Command context

config-external-storage-<VOLUME-NAME>

Parameters
<USER-NAME>

Specifies the username.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating a volume named logfiles with the user name nassuser:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# username nasuser

Clearing the user name nasuser from accessing the logfiles volume:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# no username nasuser

Chapter 6 External storage

85

vrf

Syntax

vrf <VRF-NAME>

no vrf <VRF-NAME>

Description

Setting a VRF to reach network attached storage.

The no form of this command clears access of a VRF to network attached storage.

Command context

config-external-storage-<VOLUME-NAME>

Parameters
<VRF-NAME>

Specifies the VRF name.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating the logfiles volume and setting a VRF named nas to access the network attached storage:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# vrf nas

Clearing access of a VRF named nas to the network attached storage:

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# no vrf nas

86

AOS-CX 10.06 Monitoring Guide

Chapter 7
IP-SLA

The IP Service Level Agreement (IP-SLA) is a feature that enables the measuring of network performance
between two nodes in a network for different service level agreement parameters such as round-trip time
(RTT), one-way delay, jitter, reachability, packet loss, and voice quality scores. These two nodes can span
across area in access, distribution or core inside a LAN as well as across WAN between core to core or core
to Data Centre switches. This feature helps you measure the SLA for different protocols or applications such
as UDP echo, UDP jitter (for voice and video), TCP connect, HTTP, and ICMP echo. This guide provides details
for managing and monitoring different types of IP-SLAs.

IP-SLA guidelines

• ArubaOS-CX supports only SLA configuration through CLI and thresholds can be configured using NAE

agents using WebUI/REST.

• ArubaOS-CX supports only forever tests. On-demand tests are not supported.

• Maximum sessions: IP-SLA source 500, IP-SLA responder 100.

• NAE can effectively monitor a maximum of 300 parameters, reducing the maximum supported session

by 300.

• NAE supports only syslog.

• NAE agents must be triggered for each IP-SLA test on every switch.

•

If multiple IP addresses are received for a DNS query, DNS works with the first resolved IP.

• When the DNS server IP is not configured, the first DNS server in resolve.conf is used.

• The source interface/IP option is not applicable for SLAs configured on 'mgmt' VRF, as it has only one

interface.

• A system time change because of NTP or a manual change causes an incorrect calculation.

• There is no interoperability of UDP echo SLA between ArubaOS-CX and FlexFabric switches.

• Source IP and source port combination must be unique across SLA sessions in a same switch.

• Do not use the same source port across the source and responder sessions in a switch.

• NTP synchronization is a must for SLA types involving one-way delay such as UDP jitter VoIP.

•

It is mandatory to set default CoPP to the max value when UDP jitter SLA is enabled otherwise 100%
packet loss can be seen and UDP-Jitter sla probe will result in failure as seen in the following
example.

copp-policy default
     class hypertext priority 6 rate 50000 burst 64
     default-class priority 6 rate 99999 burst 9999

• Deviations with respect to PVOS results: The packet losses due to internal switch-related issues like

interface shutdown or interface flaps will not be considered as 'Probes Timed-out error', as the IP-SLA

Chapter 7 IP-SLA

87

solution is to measure network performance and anomalies. Rather, this kind of packet loss will be
counted in internal counters like 'Destination address unreachable'.

Limitations with VoIP SLAs

• A maximum of 80 concurrent VoIP SLAs can be scheduled in a 20 second slot.

• A single VoIP probe takes 20 seconds to complete.

• The default and minimum probe interval for VoIP SLA is 120 seconds.

• SLAs scheduled in the same slot, periodically sends 1000 probe packets for 120 seconds in 20 second

intervals.

• Default 120 second probe interval is divided in to 6 slots of 20 seconds to avoid synchronization of all

configured VoIP SLAs sending probes at the same time.

• SLAs started at the same time exceeding the concurrent limit of 80 must wait for the next 20 second VoIP

slot to open before moving to ‘running’ state.

• The maximum number of VoIP SLAs supported is 80 X 6 slots = 480 SLAs.

• SLAs exceeding 480 will continue to remain in the 'waiting for VoIP slot' until any slot is freed by stopping

the running SLA.

• To avoid high RTT, a single switch with more than 20 SLAs should not have single responder SLA.

• When IP is received dynamically (e.g. using DHCP) for interfaces other than management interface, IPSLA

source or responder has to be configured only using interface name.

IP-SLA commands

http

Syntax

http {get | raw} URL [source {<SOURCE-IPV4-ADDR> | <IFNAME>} source-port <PORT-NUM>]
     [proxy proxy-url] [cache disable] [name-server <IPV4-ADDR-DNS-SERVER>]
     [probe-interval <30-604800>] [version<VERSION-NUMBER>] [http-raw-request <RAW-PAYLOAD>]

Description

Configures HTTP as the IP-SLA test mechanism. Requires destination URL and type of HTTP request (raw/
get).

Command context

config-ip-sla-<IP-SLA-NAME>

Parameters
{get | raw}

Selects HTTP request type as GET or RAW where the system will generate or provide HTTP payload.

URL

Specifies HTTP URL address of syntax. http://<HOST NAME/IP-ADDRESS>:<PORT>/<PATH>.

88

AOS-CX 10.06 Monitoring Guide

source {<SOURCE-IPV4-ADDR> | <IFNAME>}

Selects the source IPv4 address for SLA probes or the source interface to use for sending IP-SLA probes.

source-port <PORT-NUM>

Specifies the value of the source port for the IP-SLA probes.

cache disable

Selects cache option for the HTTP server. By default the option is enabled.

name-server <IPV4-ADDR-DNS-SERVER>

Specifies the IPv4 address of DNS server.

probe-interval <PROBE-INTERVAL>

Specifies the probe interval in seconds. Range: 30 to 604800.

version <VERSION-NUMBER>

Specifies the source interface to use for sending IP-SLA probes.

http-raw-request <RAW-PAYLOAD>

HTTP raw request. String.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config-ipsla-1)# http get http://device.arubanetworks.com/root/home.html
    switch(config-ipsla-1)# http raw http://device.arubanetworks.com/root/home.html
    switch(config-ipsla-1)# http 2.2.2.2 source 1/1/1
    switch(config-ipsla-1)# http http://device.arubanetworks.com  source 2.2.2.1
    switch(config-ipsla-1)# http http://device.arubanetworks.com/root/home.html source-interface 1/1/1
    switch(config-ipsla-1)# http http://device.arubanetworks.com  name-server 10.10.10.2
    switch(config-ipsla-1)# http raw raw-request "GET /en/US/hmpgs/index.html HTTP/1.0\r\n\r\n"

icmp-echo

Syntax

icmp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} [source {<SOURCE-IPV4-ADDR> | <IFNAME>}]
     [name-server <IPV4-ADDR-DNS-SERVER>] [payload-size <PAYLOAD-SIZE>]
     [tos <TYPE-OF-SERVICE>] [probe-interval <PROBE-INTERVAL>]

Description

Configures ICMP echo as the IP-SLA test mechanism. Requires destination address for the IP-SLA test.

Command context

config-ip-sla-<IP-SLA-NAME>

Parameters
{<DEST-IPV4-ADDR> | <HOSTNAME>}

Selects the destination IPv4 address for the IP-SLA or the hostname of the destination.

[source {<SOURCE-IPV4-ADDR> | <IFNAME>}]

Selects the source IPv4 address for SLA probes or the source interface to use for sending IP-SLA probes.

Chapter 7 IP-SLA

89

name-server <IPV4-ADDR-DNS-SERVER>

Specifies the DNS server for destination hostname resolution.

payload-size <PAYLOAD-SIZE>

Specifies the payload size of an SLA probe. Range: 0 to 1440.

tos <TYPE-OF-SERVICE>

Specifies the type of serve to be used in the probe packets. Range: 0 to 255.

probe-interval <PROBE-INTERVAL>

Specifies the probe interval in seconds. Range: 5 to 604800.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# ip-sla test
    switch(config-ip-sla-test)# icmp-echo 2.2.2.2
    switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3
    switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
    switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400 name-server 4.4.4.4
    switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400 name-server 4.4.4.4  probe-interval 80

ip-sla

Syntax

ip-sla <IP-SLA-NAME>

no ip-sla <IP-SLA-NAME>

Description

Creates an IP Service Level Agreement (SLA) profile and switches to the config-ip-sla context.

The no form of this command deletes an IP-SLA profile. By default, all profile use the default VRF (default).

Command context

config

Parameters
<IP-SLA-NAME>

Specifies an IP-SLA profile name. Length: 1 to 63 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating an IP-SLA:

switch(config)# ip-sla 1
switch(config-ip-sla-1)#

Deleting an IP-SLA:

90

AOS-CX 10.06 Monitoring Guide

switch(config)# no ip-sla 1
switch(config)#

ip-sla responder

Syntax

ip-sla responder <SLA-NAME> {udp-echo | tcp-connect | udp-jitter-voip} <PORT-NUM>
     [source {<SOURCE-IPV4-ADDR> | <IFNAME>}][vrf <VRF-NAME>]

no ip-sla responder <SLA-NAME>

Description

Selects the IP-SLA responder. The responder can be configured for udp-echo, tcp-connect, udp-jitter-voip
type. It requires the SLA name, SLA type, and port number as arguments. Source IP/interface ID is a must for
type udp-jitter-voip and optional for other types.

The no form of this command removes the IP-SLA responder.

Command context

config

Parameters
<SLA-NAME>

Specifies the SLA name.

udp-echo

Enables responder for udp-echo probes.

tcp-connect

Selects TCP connect as the IP-SLA test mechanism.

vrf <VRF-NAME>

Specifies the name of the VRF to use.

udp-jitter-voip

Selects VOIP jitter as the IP-SLA test mechanism.

<PORT-NUM>

Specifies the port number to listen for IP-SLA probes. Range: 1 to 65535.

[source {<SOURCE-IPV4-ADDR> | <IFNAME>}]

Selects the source IPv4 address for SLA probes or the source interface to use for sending IP-SLA probes.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
switch(config)# ip-sla responder SLA1 udp-echo 8000 source 1/1/1

switch(config)# no ip-sla responder <SLA-NAME>

Chapter 7 IP-SLA

91

show ip-sla responder

Syntax

show ip-sla responder <SLA-NAME>

Description

Shows the given IP-SLA responder configuration and operation status.

Command context

config

Parameters
<SLA-NAME>

Specifies the SLA name.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# show ip-sla responder SLA3

    SLA Name            : SLA3
    IP-SLA Type         : Udp-echo
    VRF                 : Default
    Responder Port      : 8000
    Responder IP        : 2.2.2.3
    Responder Interface : 1/1/1
    Responder Status    : Running

show ip-sla responder results

Syntax

show ip-sla responder <SLA-NAME> <SOURCE-IPV4-ADDR> <PORT-NUM> results

Description

Shows the given ip-sla responder statistics for a given source IP and port. This command is only applicable
for the sources where source IP and port are configured.

Command context

config

Parameters
<SLA-NAME>

Specifies the SLA name.

<SOURCE-IPV4-ADDR>

Specifies the source IPV4 address.

<PORT-NUM>

Specifies the port number. Range: 1 to 65535.

92

AOS-CX 10.06 Monitoring Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch# show  ip-sla responder SLA1 2.2.2.1 8000 results

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

show ip-sla <SLA-NAME>

Syntax

show ip-sla <SLA-NAME> results

Description

Shows the given IP-SLA source configuration and status.

Command context

Operator (>) or Manager (#)

Parameters
<SLA-NAME>

Specifies the SLA name.

results

Shows the statistics calculated for an SLA type.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch# show ip-sla xyz results

    IP-SLA session status
       IP-SLA Name                     : xyz
       IP-SLA Type                     : tcp-connect
       Destination Host Name/IP Address: 2.2.2.1
       Destination Port                : 8888
       Source IP Address/IFName        : 2.2.2.2
       Source Port                     : 5555
       Status                          : Running

    IP-SLA session cumulative counters
       Total Probes Transmitted        : 1
       Probes Timed-out                : 0
       Bind Error                      : 0
       Destination Address Unreachable : 0
       DNS Resolution Failures         : 0
       Reception Error                 : 0
       Transmission Error              : 0

    IP-SLA Latest Probe Results

Chapter 7 IP-SLA

93

Last Probe Time                 : 2018 Jul 13 02:00:35
       Packets Sent                    : 1
       Packets Received                : 1
       Packet Loss in Test             : 0.0000%

    Minimum RTT(ms)                    : 0.7900
    Maximum RTT(ms)                    : 0.7900
    Average RTT(ms)                    : 0.7900
    DNS RTT(ms)                        : 0.0000
    TCP RTT(ms)                        : 0.9710

switch(config)# show ip-sla xyz
    IP-SLA Name             : xyz
    Status                  : scheduled
    IP-SLA Type             : tcp-connect
    VRF                     : ipslasrc
    Source Port             : 5555
    Source IP               : 2.2.2.2
    Source Interface        :
    Domain Name Server      :
    Probe interval(seconds) : 90

switch(config)# show ip-sla jitter-sla results
    IP-SLA session status
       IP-SLA Name                     : jitter-sla
       IP-SLA Type                     : udp-jitter-voip
       Destination Host Name/IP Address: 2.2.2.1
       Destination Port                : 8888
       Source IP Address/IFName        :
       Source Port                     : 5555
       Status                          : Running

    IP-SLA Session Cumulative Counters
       Total Probes Transmitted        : 1
       Probes Timed-out                : 0
       Bind Error                      : 0
       Destination Address Unreachable : 0
       DNS Resolution Failures         : 0
       Reception Error                 : 0
       Transmission Error              : 0

    IP-SLA Latest Probe Results
       Last Probe Time                 : 2018 Jul 13 02:02:48
       Packets Sent                    : 1
       Packets Received                : 1
       Packet Loss in Test             : 0.0000%

       Minimum RTT(ms)                 : 0.7900
       Maximum RTT(ms)                 : 0.7900
       Average RTT(ms)                 : 0.7900
       DNS RTT(ms)                     : 0.0000

       Min Positive SD                 : 1      Min Positive DS        : 2
       Max Positive SD                 : 1      Max Positive DS        : 2
       Positive SD Number              : 2      Positive DS Number     : 2
       Positive SD Sum                 : 2      Positive DS Sum        : 4
       Positive SD Average             : 5      Positive DS Average    : 5
       Min Negative SD                 : 1      Min Negative DS        : 1
       Max Negative SD                 : 1      Max Negative DS        : 1
       Negative SD Number              : 2      Negative DS Number     : 4
       Negative SD Sum                 : 2      Negative DS Sum        : 4
       Negative SD Average             : 5      Negative DS Average    : 5

       Max SD Delay                    : 0      Max DS Delay           : 0
       Min SD Delay                    : 0      Min DS Delay           : 0
       Average SD Delay                : 0      Average DS Delay       : 0

    Voice Scores:
       MOS  Score                      : 4.38   ICPIF                  : 0

switch(config)# show ip-sla m3op
    IP-SLA Name             : jitter-sla
    Status                  : Running
    IP-SLA Type             : udp-jitter-voip
    VRF                     : ipslasrc
    Source IP               : 2.2.2.2
    Source Interface        :
    Domain Name Server      :
    TOS                     : 10
    Probe Interval(seconds) : 90
    Advantage Factor        : 0
    Codec Type              : g711a

94

AOS-CX 10.06 Monitoring Guide

switch(config)# show ip-sla http-sla
    IP-SLA Name             : http-sla
    Status                  : Running
    IP-SLA Type             : http
    VRF                     : ipslasrc
    Source IP               : 2.2.2.2
    Source Interface        :
    Domain Name Server      : 10.10.10.2
    Probe Interval(seconds) : 90
    HTTP Request Type       : GET
    HTTP/HTTPS URL          : abcd.com/ws/home
    Cache                   : Enabled
    HTTP Proxy URL          :
    HTTP Version Number     : 1.1
    ```

##### IP-SLA status description
    ```
    | Status                  | Description                                    |
    |-------------------------|------------------------------------------------|
    | Running                 | SLA is fully operational                       |
    | Bind Error              | Another service is using the same source port  |
    | Interface Down          | Interface status is not up
    | Dns Resolution Error    | Failed to resolve destination hostname         |
    | No Route                | No available route to the responder            |
    | Internal Error          | Unexpected error prevents SLA session          |
    | Disabled                | SLA is disabled                                |
    |Configuration Incomplete | Configuration is not complete to enable the SLA|
    ```
##### IP SLA session cumulative counters description
    ```
    | Status                         | Description                                                              |
    |--------------------------------|--------------------------------------------------------------------------|
    |Probes Timed-out                | Total numbers of probes failed to receive response.                      |
    |Bind Error                      | Total numbers of probes transmission failed as source port not available.|
    |Destination Address Unreachable | Total numbers of probes transmission failed due to route unavailable.    |
    |DNS Resolution Failures         | Total numbers of probes failed due to DNS resolution failure.            |
    |Reception Error                 | Total numbers of probes failed due to internal error in reception.       |
    |Transmission Error              | Total numbers of probes failed due to internal errr in transmission.     |

start-test

Syntax

start-test

Description

Starts the IP-SLA probes.

Command context

config-ip-sla-<IP-SLA-NAME>

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# ip-sla test
switch(config-ip-sla-test)# start-test

stop-test

Syntax

stop-test

Description

Stops the IP-SLA probes.

Chapter 7 IP-SLA

95

Command context

config-ip-sla-<IP-SLA-NAME>

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# ip-sla test
switch(config-ip-sla-test)# stop-test

tcp-connect

Syntax

tcp-connect {<DEST-IPV4-ADDR> | <HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
     <IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>]
     [probe-interval <PROBE-INTERVAL>]

Description

Configures TCP connect as the IP-SLA test mechanism. Requires destination address/hostname and
destination port for the IP-SLA of tcp-connect IP-SLA type.

Command context

config-ip-sla-<IP-SLA-NAME>

Parameters
{<DEST-IPV4-ADDR> | <HOSTNAME>}

Selects the destination IPv4 address for the IP-SLA or the hostname of the destination.

<PORT-NUM>

Destination port for the IP-SLA. Range: 1 to 65535.

[source {<SOURCE-IPV4-ADDR> | <IFNAME>}]

Selects the source IPv4 address for SLA probes or the source interface to use for sending IP-SLA probes.

[source-port <PORT-NUM>]

Specifies the port for the IP-SLA test.

[name-server <IPV4-ADDR-DNS-SERVER>]

Specifies the DNS server for destination hostname resolution.

[probe-interval <PROBE-INTERVAL>]

Probe interval in seconds. Range: 30 to 604800.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config-ipsla-1)# tcp-connect 2.2.2.2 8080
       switch(config-ipsla-1)# tcp-connect 2.2.2.2 8080 source 2.2.2.1 source-port 6000
       switch(config-ipsla-1)# tcp-connect 2.2.2.2 8080 source 1/1/1 source-port 6000

       switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
       switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080 source 2.2.2.1 source-port 6000

96

AOS-CX 10.06 Monitoring Guide

switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080 source 1/1/1 source-port 6000
       switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080 name-server 10.10.10.2

udp-echo

Syntax

udp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
     <IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>] [payload-size
     <PAYLOAD-SIZE>] [tos <TYPE-OF-SERVICE>] [probe-interval <PROBE-INTERVAL>]

Description

Configures UDP echo as the IP-SLA test mechanism. Requires destination address/hostname and
destination port number for the IP-SLA of udp-echo SLA type.

Command context

config-ip-sla-<IP-SLA-NAME>

Parameters
{<DEST-IPV4-ADDR> | <HOSTNAME>}

Selects the destination IPv4 address for the IP-SLA or the hostname of the destination.

<PORT-NUM>

Specifies the destination port for the IP-SLA. Range: 1 to 65535.

[source {<SOURCE-IPV4-ADDR> | <IFNAME>}]

Selects the source IPv4 address for SLA probes or the source interface to use for sending IP-SLA probes.

[source-port <PORT-NUM>]

Specifies source port for the IP-SLA test. Range: 1 to 65535.

[name-server <IPV4-ADDR-DNS-SERVER>]

Specifies the DNS server for destination hostname resolution.

[payload-size <PAYLOAD-SIZE>]

Specifies the payload size of an SLA probe. Range: 28 to 1440.

[<TYPE-OF-SERVICE>]

Type of service. Range: 0 to 255.

probe-interval <PROBE-INTERVAL>

Probe interval in seconds. Range: 5 to 604800.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config-ipsla-1)# udp-echo 2.2.2.2 8080
    switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 2.2.2.1
    switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080
    switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 1/1/1
    switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 2.2.2.1 payload-size 50
    switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 1/1/1 payload-size 50
    switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 payload-size 50
    switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080 source 2.2.2.1

Chapter 7 IP-SLA

97

payload-size 50
    switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080 source 1/1/1
     payload-size 50
    switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080
     name-server 10.10.10.2

udp-jitter-voip

Syntax

udp-jitter-voip {<DEST-IPV4-ADDR> | <HOSTNAME>} <PORT-NUM> [codec-type <CODEC-TYPE>]
     [advantage-factor <VALUE>] [source {<SOURCE-IPV4-ADDR> | <IFNAME>} [source-port <PORT-NUM>]]
     [name-server <IPV4-ADDR-DNS-SERVER>][probe-interval <PROBE-INTERVAL>] [tos <TYPE-OF-SERVICE>]

Description

Configure UDP jitter voip as the IP-SLA test mechanism. Requires destination address/hostname and source
address/interface for the IP-SLA of udp-jitter-voip IP-SLA type.

Command context

config-ip-sla-<IP-SLA-NAME>

Parameters
{<DEST-IPV4-ADDR>|<HOSTNAME>}

Selects the destination IPv4 address for the IP-SLA or the hostname of the destination.

<PORT-NUM>

Selects the port number for the IP-SLA. Range: 1 to 65535.

[codec-type <CODEC-TYPE>]

Selects the codec-type for the Voip IP-SLA test.

[advantage-factor <ADVANTAGE-FACTOR>]

Selects the value for the advantage factor. Default value is 0.

[source {<SOURCE-IPV4-ADDR> | <IFNAME>}]

Selects the source IPv4 address for SLA probes or the source interface to use for sending IP-SLA probes.

[source-port <PORT-NUM>]

Specifies the value of source port for the IP-SLA probes.

[name-server <IPV4-ADDR-DNS-SERVER>]

Specifies the DNS server for destination hostname resolution.

tos<TYPE-OF-SERVICE>

Specifies the type of service. Range: 0 to 255.

probe-interval <PROBE-INTERVAL>

Specifies the probe interval in seconds. Range: 120 to 604800.

Authority

Administrators or local user group members with execution rights for this command.

98

AOS-CX 10.06 Monitoring Guide

Examples

switch(config-ipsla-1)# udp-jitter-voip  2.2.2.2 8080 advantage-factor 10 codec-
type g711a
    switch(config-ipsla-1)# udp-jitter-voip  2.2.2.2 8080 advantage-factor 10
codec-type g711a source 2.2.2.1
    switch(config-ipsla-1)# udp-jitter-voip  https://device.arubanetworks.com 8080
advantage-factor 10 codec-type g711a
    switch(config-ipsla-1)# udp-jitter-voip  2.2.2.2 8080 advantage-factor 10
codec-type g711a source 1/1/1
    switch(config-ipsla-1)# udp-jitter-voip  https://device.arubanetworks.com 8080
advantage-factor 10 codec-type g711a source 2.2.2.1
    switch(config-ipsla-1)# udp-jitter-voip  https://device.arubanetworks.com 8080
advantage-factor 10 codec-type g711a source 1/1/1
    switch(config-ipsla-1)# udp-jitter-voip  https://device.arubanetworks.com 8080
advantage-factor 10 codec-type g711a name-server 10.10.10.2 probe-interval 120
source 10.1.1.1 source-port 8888 tos 10

vrf

Syntax

vrf <VRF-NAME>

no vrf [<VRF-NAME>]

Description

Configures the VRF on which the SLA will send or receive packets. By default, the default VRF is used.

The no form of the command removes VRF from SLA.

Command context

config-ip-sla-<IP-SLA-NAME>

Parameters
<VRF-NAME>

Specifies a VRF name. Length: Default: default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config-ip-sla-test)# vrf ipslasrc

switch(config-ip-sla-test)# no vrf

Chapter 7 IP-SLA

99

Chapter 8
L1-100Mbps downshift

The speed downshift feature allows the user to link-up at sub-optimal speeds when failing to link-up at the
highest advertised speed. There are fixed number of link attempts made to establish link at highest
advertised speed and when all of them fail and attempt is made to link-up at a lower possible speed.

This feature requires underlying PHY to have support for the same and hence capability is only added to
select set of ports. If a link cannot be established at the highest common denominator within a set number
of link attempts, the PHY advertises the next highest speed using auto-negotiation.

Limitations with speed downshift

•

•

Link up may be delayed as certain number of retries are done to establish the link at highest advertise
speeds by both link partners before downshifting.

Link may be established at sub-optimal speed.

L1-100Mbps downshift commands

downshift enable

Syntax

downshift-enable

no downshift-enable

Description

Enables/disables automatic speed downshift on an interface that supports downshift, generally 1GBASE-T
ports. When enabled, downshift allows an interface to link at a lower advertised speed when unable to
establish a stable link at the maximum speed. Downshifting only applies to physical interfaces that are not
members of a LAG and is only available when auto-negotiation is enabled. When only one speed is
advertised, downshift will not be triggered.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config-if)# interface 1/1/1
switch(config-if)# downshift-enable

Warning: this is a non-standard mode for use only when standards-based
auto-negotiation is not able to establish a stable link. Enabling this
may cause the port to link at a lower than expected speed and should

100

AOS-CX 10.06 Monitoring Guide

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

show interface

Syntax

show interface [<IFNNAME>|<IFRANGE>] [brief | physical | extended [non-zero]]

show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief | physical]

show interface [lag | loopback | tunnel | vlan ] [<ID>] [extended | non-zero]

Description

Displays active configurations and operational status information for interfaces.

Command context

config

Parameters
<IFNAME>

Specifies a interface name.

<IFRANGE>

Specifies the port identifier range.

brief

Displays brief info in tabular format.

extended

Displays the physical connection info in tabular format.

non-zero

Displays only non zero statistics.

LAG

Displays LAG interface information

Chapter 8 L1-100Mbps downshift

101

LOOPBACK

Displays loopback interface information.

TUNNEL

Displays tunnel interface information.

VLAN

Displays VLAN interface information.

<LAG-ID>

Specifies the LAG number. Range: 1-256

<LOOPBACK-ID>

Specifies the LOOPBACK number. Range: 0-255

<TUNNEL-ID>

Specifies the tunnel ID. Range: 1-255

<VLAN-ID>

Specifies the VLAN ID. Range: 1-4094

VXLAN

Displays the VXLAN interface information.

<VXLAN-ID>

Specifies the VXLAN interface identifier. Default: 1

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing interfaces configured for L2 forwarding:

switch(config-if)# show interface
Interface 1/1/1 is down (Administratively down)
 Admin state is down
 State information: Administratively down
 Link transitions: 2
 Description: Backup data center link
 Hardware: Ethernet, MAC Address: 70:72:cf:fd:e7:b4
 MTU 9198
 Type SFP-SX
 Full-duplex
 qos trust none
 Speed 0 Mb/s
 Auto-negotiation is on
 Flow-control: off
 Error-control: off
 VLAN Mode: access
 Access VLAN: 1
 Rx
      1386055 total packets            586397526 total bytes
      1374287   unicast packets
        11764   multicast packets
            4   broadcast packets
            0 errors                           0 dropped
            0 CRC/FCS

102

AOS-CX 10.06 Monitoring Guide

Tx
      2475612 total packets           1003506711 total bytes
      2311806   unicast packets
       100369   multicast packets
        63437   broadcast packets
            0 errors                     2462773 dropped
            0 collision

Interface 1/2/1 is down (Administratively down)
 Admin state is down
 State information: Administratively down
 Link transitions: 0
 Description:
 Hardware: Ethernet, MAC Address: 70:72:cf:fd:e7:b4
 MTU 9198
 Type QSFP+SR4
 Full-duplex
 qos trust none
 Speed 0 Mb/s
 Auto-negotiation is off
 Flow-control: off
 Error-control: off
 VLAN Mode: access
 Access VLAN: 1
 Rx
            0 total packets                    0 total bytes
            0   unicast packets
            0   multicast packets
            0   broadcast packets
            0 errors                           0 dropped
            0 CRC/FCS
 Tx
            0 total packets                    0 total bytes
            0   unicast packets
            0   multicast packets
            0   broadcast packets
            0 errors                           0 dropped
            0 collision

When the interface is currently linked at a downshifted speed:

switch(config-if)# show interface 1/1/1

Interface 1/1/1 is up
 ...
 Auto-negotiation is on with downshift active

show interface downshift-enable

Syntax

show interface [<IFNNAME>|<IFRANGE>] downshift-enable

Description

Displays speed downshift information, including the interface speed status and configuration.

Command context

config

Chapter 8 L1-100Mbps downshift

103

Parameters
<IFNAME>

Specifies a interface name.

<IFRANGE>

Specifies the port identifier range.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

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

show running-config interface

Syntax

show running-config interface [<IFNNAME>|<IFRANGE>]

show running-config interface [lag | loopback | tunnel | vlan ] [<ID>]

Description

Displays active configurations of various switch interfaces.

Command context

config

Parameters
<IFNAME>

Specifies a interface name.

<IFRANGE>

Specifies the port identifier range.

104

AOS-CX 10.06 Monitoring Guide

LAG

Specifies LAG interface information

LOOPBACK

Specifies loopback interface information.

TUNNEL

Specifies tunnel interface information.

VLAN

Specifies VLAN interface information.

<LAG-ID>

Specifies the LAG number. Range: 1-256.

<LOOPBACK-ID>

Specifies the LOOPBACK number. Range: 0-255.

<TUNNEL-ID>

Specifies the tunnel ID. Range: 1-255.

<VLAN-ID>

Specifies the VLAN ID. Range: 1-4094.

VXLAN

Specifies the VXLAN interface information.

<VXLAN-ID>

Specifies the VXLAN interface identifier. Default: 1.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

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

Chapter 8 L1-100Mbps downshift

105

switch(config-if)# show running-config interface loopback

No loopback interfaces configured.

106

AOS-CX 10.06 Monitoring Guide

Chapter 9
Mirroring

Mirroring allows you to replicate all traffic arriving and/or leaving the selected system interfaces. This data
can be used for collection or analysis.

The traffic replicated using mirroring can be sent to a separate interface on the same switch as the traffic
source for analysis or inspection. Such a collection of interfaces and settings is called a mirror session.

A mirror session can be configured with many traffic sources but only a single output, or destination. In the
initial configuration, the mirror session is disabled. You have enable the feature to start the replication.

CAUTION: Care must be taken in choosing the number and rates of sources to avoid over-
saturating a session destination. A mirror session with multiple 10G sources can overwhelm a
single 10G destination and important data may be lost.

Mirror statistics
Mirror statistics are reset for a Mirror-to-CPU session when an interface is added or removed from a LAG
that is a source interface in the Mirror session and during a failover.

Classifier policies and mirroring sessions
Network traffic can be mirrored to a destination interface in two ways:

• Using a mirroring session alone.

• Using Classifier Policies with mirror actions in conjunction with a mirroring session.

Basic mirroring sessions provide coarse control over the type of traffic mirrored from a source: all received,
all transmitted, or both. However, a traffic class within a Classifier Policy applied to a source can provide
much finer grained control of mirrored traffic. For example, a policy can match on many different aspects of
the Ethernet or IPv4 or IPv6 header information in each frame or packet received or transmitted on an
interface.

The steps to configure a policy and class with a mirror action are the following:

1. Configuring a mirroring session with a destination interface.

2. Enabling the mirroring session.

3. Configuring the Classifier Policy, specifying the mirroring session ID in the mirror action.

If the packets being mirrored are received from a VLAN that is not allowed on the mirror destination, the
mirrored packets would be dropped at the mirror destination interface. When the mirrored packets are
dropped at the destination, the mirror output packet and byte count will increment, however the packets
will not be received at the mirror destination.

The mirror destination port among the active mirror sessions must be unique. That is, if an interface is
configured as a source or destination in an active mirror session, the same port cannot be used as a
destination in another active mirror session.

Chapter 9 Mirroring

107

VLAN as a source
ArubaOS-CX allows configuration of VLAN as a mirroring source. When a VLAN source is configured in the
'rx' direction, all packets are mirrored as they are received in the switch. When a VLAN source is configured
in 'tx' direction, all packets are mirrored as they are transmitted out of the switch.

More than one source VLAN can be configured in a mirror session. Each such VLAN may specify its own
direction.

There is a limit of 1024 source VLANs in each direction of a given mirror session.

Same VLANs can be configured as a mirror source for multiple sessions.

Note: When changing a source VLAN in an enabled mirror session (that is, adding, changing direction, or
removing), mirrored packets being transmitted out the mirror destination port from other mirror sources
may be briefly interrupted during the reconfiguration.

Direction of an existing source VLAN can be updated in one of two ways:

1. Reenter the source vlan command with the new preferred direction.

2. Use the no form of the command with a direction (rx or tx) to selectively remove the specified direction.

Specifying the last remaining direction for that VLAN will remove the VLAN from the configuration
entirely.

For packets bridged through the switch:

If the mirror is configured in 'both' direction, two copies of packets are mirrored, otherwise one copy of the
packet will be mirrored.

For routed packets:

•

•

•

If the mirror is configured in the 'rx' direction, packets are mirrored in the pre-routed form with the
destination MAC address as the switch address.

If the mirror is configured in the 'tx' direction, packets are mirrored in the post-routed form with the
source MAC as the switch address. Destination MAC is the nexthop gateway or station.

If the mirror is configured in the 'both' direction, one copy of the packet will be mirrored.

Control plane packets generated by the switch's CPU are processed both in the ingress and the egress
packet processing pipeline. The following are the behaviors for mirroring with VLAN as source:

•

•

If the mirror is configured in the 'rx' or 'tx' direction, the packets are mirrored to the mirror destination.

If the mirror is configured in the 'both' direction, two copies of the packets are mirrored to the mirror
destination.

Mirroring commands

clear mirror

Syntax

clear mirror [all | <SESSION-ID>]

108

AOS-CX 10.06 Monitoring Guide

Description

Clears the mirror statistics for all configured mirror sessions or a specified session

Command context

Manager (#)

Parameters
all

Specifies all configured sessions.

<SESSION-ID>

Specifies a numeric identifier for the session. Range: 1 to 4

Authority

Administrators or local user group members with execution rights for this command.

Examples

Clearing mirror statistics for all configured mirror sessions:

switch# clear mirror all

Clearing mirror statistics for mirror session 1:

switch# clear mirror 1

comment

Syntax

comment <COMMENT>

no comment

Description

Specifies a descriptive comment for the mirroring session.

The no form of this command removes the comment.

Command context

config-mirror-<SESSION-ID>

Parameters
<COMMENT>

A comment string of up to 64 characters composed of letters, numbers, underscores, dashes, spaces,
and periods.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Comments are optional and can be added or removed at any time without affecting the state of the
mirroring session.

Chapter 9 Mirroring

109

Adding a comment to a session that already has a comment replaces the existing comment.

Examples

Adding a comment:

switch(config-mirror-3)# comment This Mirror will be removed during next maintenance window

Removing the comment for mirroring session 3:

switch(config-mirror-3)# no comment

copy tshark-pcap

Syntax

copy tshark-pcap <REMOTE-URL> [vrf <VRF-NAME>]

Description

Copies the tshark capture data to a file on a TFTP or SFTP server.

Command context

Manager (#)

Parameters
<REMOTE-URL>

Specifies the capture file on a remote TFTP or SFTP server. The URL syntax is:

{tftp:// | sftp://<USER>@} {<IP>|<HOST>} [:<PORT>] [;blocksize=<SIZE>]/<FILE>

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

Authority

Administrators or local user group members with execution rights for this command.

Example

Copying the capture data to a file on SFTP server 10.0.0.2:

switch# copy tshark-pcap sftp://root@10.0.0.2/file.pcap

root@10.0.0.2's password:
Connected to 10.0.0.2.
sftp> put packets.pcap file.pcap
Uploading packets.pcap to /root/file.pcap
packets.pcap                                  100%  156   219.8KB/s   00:00
Copied successfully.

destination cpu

Syntax

destination cpu

no destination cpu

110

AOS-CX 10.06 Monitoring Guide

Description

The command causes the mirror session to transmit mirrored packets to the switch CPU. This destination
may be configured for multiple sessions, however only one such configured session may be active at a given
time.

The diagnostic utility Tshark may be used to view and capture packets transmitted to the CPU through this
route. Ctrl+C must be entered to terminate a Tshark capture session. More details can be found in the
Supportability Guide.

The no form of this command will immediately stops mirroring traffic to the CPU, but will not remove any
sources from the mirror configuration.

Command context

config-mirror-<SESSION-ID>

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring a mirror session with CPU as the destination.

switch# config
switch(config)# mirror session 1
switch(config-mirror-1)# destination cpu

Removing the destination entirely.

switch(config-mirror-1)# no destination cpu

destination interface

Syntax

destination interface {<INTERFACE-ID>|<LAG-NAME>}

no destination interface

Description

Configures the specified interface as the destination of the mirrored traffic.

The no form of this command immediately disables the mirroring session and removes the specified
destination interface from the configuration.

Command context

config-mirror-<SESSION-ID>

Parameters
<INTERFACE-ID>

Specifies a interface. Format: member/slot/port.

<LAG-NAME>

Specifies a LAG (link aggregation group) identifier.

Chapter 9 Mirroring

111

Authority

Administrators or local user group members with execution rights for this command.

Usage

Only one destination is allowed per session.

Configuring a different destination interface in an enabled mirroring session causes all mirrored traffic to
use the new destination interface. This action might cause a temporary suspension of mirrored source
traffic during the reconfiguration.

Examples

On the 6400 Switch Series, interface identification differs.

Configuring a mirroring session and adding an interface as a destination:

switch(config)# mirror session 1
switch(config-mirror-1)# destination interface 1/1/1

Replacing the existing destination with different interface:

switch(config-mirror-1)# destination interface 1/1/12

Removing a destination:

switch(config-mirror-1)# no destination interface

destination tunnel

Syntax

Description

Specifies the tunnel where all mirrored traffic for the session is transmitted. Only one tunnel destination is
allowed per session.

You may configure multiple mirror sessions with the same source/destination IP address pair, however, only
one of those sessions sharing the same source/destination IP address pair can be enabled at a given time.

ERSPAN is not supported leaving the switch by the OOB port. If VRF management is configured for an
ERSPAN session, the session will be in "mirror_err_tunnel_oob_port_not_supported" operation status.

ERSPAN is not supported leaving the switch encapsulated within another tunnel (e.g. GRE IPv4). When the
path to the destination IP address will leave via a tunnel, the session will be in
"tunnel_route_resolution_not_populated" operation status.

NOTE: The interface/LAG used to transmit ERSPAN packets should not be a source in the same
mirror session.

The no form of this command will cease the use of the tunnel and disable the session.

Command context

config-mirror-<SESSION-ID>

Authority

Administrators or local user group members with execution rights for this command.

112

AOS-CX 10.06 Monitoring Guide

Parameters
<TUNNEL-IPV4-ADDR>

Specifies the tunnel address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255.

<SOURCE-IPv4-ADDR>

Specifies the source address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255.

<DSCP-VALUE>

Specifies the DSCP value to be carried within the DS field of ERSPAN packet header. Range: 0 to 63.
Default: 0.

<VRF-NAME>

Specifies a VRF name. Default: default.

Examples

Creating a Mirror Session and adding tunnel destination, source, dscp, and VRF:

switch# config
switch(config)# mirror session 1
switch(config-mirror-1)# destination tunnel 1.1.1.1 source 2.2.2.2 dscp 10 vrf default

Replacing the existing tunnel destination:

switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 10 vrf default

Replacing the existing destination with a different DSCP value:

switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 2 vrf default

Replacing the existing destination with a different VRF:

switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 2 vrf newvrf

Removing the destination:

switch(config-mirror-1)# no destination tunnel

diagnostic

Syntax

diagnostic

diag utilities tshark [file]
diag utilities tshark [delete-file]

Description

Captures packets from a mirror-to-cpu session, and save the most recent 32MB to pcap file which can then
be copied and analyzed. When capturing a mirror-to-cpu session to a file, packets will not be dumped to the
console.

NOTE: The diagnostic command must be entered prior to the diag utilities tshark
command.

Use the delete-file form of this command to delete the most recent capture file.

Chapter 9 Mirroring

113

Since file and delete-file are optional, the behavior of the base command diag utilities tshark
does not save anything to a file, and instead dumps the tshark session to the console until CTRL + c is
entered.

Command context

Manager (#)

Parameters
file

Saves captured packets to a temporary file.

delete-file

Deletes the most recent captured file.

Authority

Administrators or local user group members with execution rights for this command.

Example

Performing diagnostic:

switch# diagnostic

switch# diagnostic utilities tshark file
Inspecting traffic mirrored to the CPU until Ctrl-C is entered
^CEnding traffic inspection.

disable

Syntax

disable

Description

Disables the mirroring session specified by the current command context.

Command context

config-mirror-<SESSION-ID>

Authority

Administrators or local user group members with execution rights for this command.

Usage

By default, mirroring sessions are disabled.

When a mirroring session is disabled, the show mirror command for that session ID shows an Admin
Status of disable and an Operation Status of disabled.

Example

Disabling a mirroring session:

switch(config)# mirror session 3
switch(config-mirror-3)# disable

114

AOS-CX 10.06 Monitoring Guide

enable

Syntax

enable

Description

Enables the mirroring session for the current command context.

Command context

config-mirror-<SESSION-ID>

Authority

Administrators or local user group members with execution rights for this command.

Usage

By default, mirroring sessions are disabled.

When a mirroring session is enabled, the show mirror command for that session ID shows an Admin
Status of enable and an Operation Status of enabled.

If sFlow is enabled on an interface and a mirroring session specifies the same interface as the source of
received traffic (the source is configured with a direction of rx or both):

The attempt to enable the mirroring session fails and an error is returned.

NOTE: When adding, removing, or changing the configuration of a source interface in an
enabled mirroring session, packets from other mirror sources using the same destination
interface might be interrupted.

Example

On the 6400 Switch Series, interface identification differs.

Configuring and enabling a mirroring session:

switch(config)# mirror session 3
switch(config-mirror-3)# source interface 1/1/2 rx
switch(config-mirror-3)# destination interface 1/1/3
switch(config-mirror-3)# comment Monitor router port ingress-only traffic
switch(config-mirror-3)# enable

mirror session

Syntax

mirror session <SESSION-ID>

no mirror session <SESSION-ID>

Description

Creates a mirroring session configuration context or enters an existing mirroring session configuration
context.

From this context, you can enter commands to configure and enable or disable the mirroring session.

Chapter 9 Mirroring

115

The no form of this command removes an existing mirroring session from the configuration.

Command context

config

Parameters
<SESSION-ID>

Specifies the session identifier. Range: 1 to 4

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# mirror session 1
switch(config-mirror-1)#

switch(config)# mirror session 3
switch(config-mirror-3)#

switch(config)# no mirror session 1
switch(config)#

show mirror

Syntax

show mirror [<SESSION-ID>] [vsx-peer]

Description

Shows information about mirroring sessions. If <SESSION-ID> is not specified, then the command shows a
summary of all configured mirroring sessions. If <SESSION-ID> is specified, then the command shows
detailed information about the specified mirroring session.

Command context

Operator (>) or Manager (#)

Parameters
<SESSION-ID>

Specifies the session identifier. Range: 1 to 4

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

Admin Status indicates the configured status. Admin Status is one of the following values:

116

AOS-CX 10.06 Monitoring Guide

enable

The mirroring session is enabled.

disable

The mirroring session has been configured but not yet enabled, or has been disabled.

Operation Status indicates the status of the mirroring session. Operation Status is one of the following
values:

dest_doesnt_exist

The configured destination interface is not found in the system. The mirroring session cannot be
enabled.

destination_shutdown

The mirroring session is enabled, but the destination interface is shut down. No traffic can be
monitored.

disabled

The mirroring session is disabled and is not in an error condition.

enabled

The mirroring session is enabled.

external/driver_error

An internal ASIC hardware error occurred.

hit_active_sessions_capacity

The mirroring session could not be enabled because the maximum number of supported mirroring
sessions are already enabled.

internal_error

An invalid parameter was passed to the ASIC software layer.

no_dest_configured

The mirroring session does not have a destination interface configured.

no_name_configured

A software error occurred. The mirroring session does not have a session ID in its configuration.

null_mirror

A software error occurred. The session object reference is invalid.

out_of_memory

The system is out of memory, reboot recommended.

tunnel_route_resolution_not_populated

If the destination tunnel IP address is not reachable.

unknown_error

An unexpected error occurred.

Examples

On the 6400 Switch Series, interface identification differs.

Showing summary information about all configured mirroring sessions:

Chapter 9 Mirroring

117

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
 Output Packets: 0
 Output Bytes: 0
switch#

source interface

Syntax

source interface {<PORT-NUM> | <LAG-NAME>} [<DIRECTION>]

no source interface {<PORT-NUM> | <LAG-NAME>} [<DIRECTION>]

Description

Configures the specified interface (either an Ethernet port or a LAG) as a source of traffic to be mirrored.

The no form of this command ceases mirroring traffic from the specified source interface and removes the
source interface from the mirroring session configuration.

Command context

config-mirror-<SESSION-ID>

Parameters
<PORT-NUM>

Specifies a physical port on the switch. Use the format member/slot/port (for example, 1/3/1).

<LAG-NAME>

Specifies the identifier for the LAG (link aggregation group).

<DIRECTION>

Selects the direction of traffic to be mirrored from this source interface. There is no default for this
parameter. Valid values are the following:

both

Mirror both transmitted and received packets.

rx

tx

Mirror only received packets.

Mirror only transmitted packets.

118

AOS-CX 10.06 Monitoring Guide

Authority

Administrators or local user group members with execution rights for this command.

Usage

There is a limit of four source interfaces in each direction of a given mirror session. However, there is a
practical limit to the amount of traffic that a mirror destination can transmit. For example, mirroring session
with multiple 10G sources can overwhelm a single 10G destination.

NOTE: When adding, removing, or changing the configuration of a source port in an enabled
mirroring session, packets from other mirror sources using the same destination port might be
interrupted.

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

source vlan

Syntax

source vlan <VLAN-NUM> {rx | tx | both}
no source vlan <VLAN-NUM> [rx | tx | both]

Chapter 9 Mirroring

119

Description

Adds or removes VLAN as a source of traffic to be mirrored. More than one source VLAN can be configured
in a mirror session. Each VLAN may specify its own direction.

The no version of the command ceases mirroring traffic from the specified source VLAN and removes the
source from the mirror configuration.

There is a limit of 1024 source VLANs in each direction of a given mirror session. The same VLAN can be
configured as a mirror source for multiple sessions.

Command context

config

Parameters
<VLAN-NUM>

Configured VLAN number.

Mirror only received traffic.

rx

tx

Mirror only transmitted traffic.

both

Mirror both received and transmitted traffic.

Authority

Administrators or local user group members with execution rights for this command.

Example

Create a mirror session and add VLAN 10 as a source of traffic in both directions on that port.

switch(config)# mirror session 1
switch(config-mirror-1)# source vlan 10 both

Create a second mirror session and add VLAN 10 as a transmit sources of traffic and VLAN 20 in both receive
and transmit directions.

switch(config)# mirror session 2
switch(config-mirror-2)# source vlan 10 tx
switch(config-mirror-2)# source vlan 20 both

Reconfigure the source in session 2 to be receive only by respecifying the source interface configuration.

switch(config-mirror-2)# source vlan 10 rx

From the second session, remove the first source interface entirely and remove the transmit direction from
the other so that mirroring only occurs in the receive direction.

switch(config-mirror-2)# no source vlan 10
switch(config-mirror-2)# no source vlan 20 tx

Message received when trying to add more than 1024 mirror source VLANs

switch(config-mirror-2)# source vlan 2000 rx
The maximum number of source VLANs per mirror session is 1024 in each direction

120

AOS-CX 10.06 Monitoring Guide

Chapter 10
Monitoring a device by using SNMP

Configuring SNMP: Refer to the ArubaOS-CX SNMP/MIB Guide for information on how to add SNMP so a
device can be monitored from a network management system (NMS).

Configuring an SNMP trap receiver: Refer to the ArubaOS-CX SNMP/MIB Guide and specific information
about the show snmp trap command to enable SNMP traps.

Chapter 10 Monitoring a device by using SNMP

121

Chapter 11
Power-over-Ethernet (PoE)

• The Power-over-Ethernet (PoE) subsystem manages power supplied to devices using standard Ethernet
data cables. A Power Sourcing Equipment (PSE) supplies DC power as well as Ethernet connectivity to a
Powered Device (PD) using a standard Ethernet cable. The maximum current depends on the PD
Requested Class.

• A PoE subsystem contains two parts : a PSE and PD. A Power Sourcing Equipment (PSE) is a device that

provides power through a standard Ethernet cable. A PoE capable switch functions as PSE. All Aruba PoE
switches are considered as PSEs. A PD is a device powered by a PSE. Examples of PD are VoIP phones,
Wireless APs, and IP cameras.

• When a PD or any network cable is connected to a PSE port, the PSE applies a detection voltage and

measures the resistance value of the PD. If resistance is within IEEE 802.3 standard values (23 - 26k ohm),
the connected device is treated as PD and classification begins. For legacy devices to be detected, you
must enable prestandard detection on the switch.

• PDs are divided into different types and classes based on PD power requirements. The power supplied by
the PSE is higher than the power PD draws to accommodate for the line losses that can result with the
use of the standard maximum length cable(100m).

◦ Type 1: PSE can supply minimum of 15.4W, and PD can draw a maximum of 13W.

◦ Type 2: PSE can supply minimum of 30W, and PD can draw a maximum of 25.5W.

◦ Type 3: PSE can supply minimum of 60W, and PD can draw a maximum of 51W.

◦ Type 4: PSE can supply minimum of 90W, and PD can draw a maximum of 71W.

• Classes of PD:

◦ Class 0: Type1 PD, it can draw a maximum of 13W.

◦ Class 1: Type1 PD, it can draw a maximum of 3.84W.

◦ Class 2: Type1 PD, it can draw a maximum of 6.49W.

◦ Class 3: Type1 PD, it can draw a maximum of 13W.

◦ Class 4: Type2 PD, it can draw a maximum of 25.5W.

◦ Class 5: Type3 PD, it can draw a maximum of 40W.

◦ Class 6: Type3 PD, it can draw a maximum of 51W.

◦ Class 7: Type4 PD, it can draw a maximum of 62W.

◦ Class 8: Type4 PD, it can draw a maximum of 71.3W.

•

IEEE 802.3bt introduced 4-Pair PoE as a means of supplying higher power to PDs that need more than the
current 25.5W supplied by IEEE 802.3at. To increase the available power without damaging the Ethernet
cable, the standard introduced the ability to use all four pairs within the Ethernet cable instead of the two
pairs used by previous standards (802.3at, 802.3af).

• Supported protocols:

◦ Compatibility with IEEE 802.3af, 802.3at, 802.3bt and prestandard.

◦

Long first class event supported on Type 3-4 PSE.

122

AOS-CX 10.06 Monitoring Guide

◦ Support for Single Signature (SS) Type 0-6 and Dual Signature (DS) Type 0-4 PDs.

◦ Multi-Event classification permits mutual ID of SS Class 0-6 and DS Class 0-4.

◦ Support LLDP Data Link Layer (DLL) Type 1-2 extension 12-octet TLV and Type 3-4 extension 29-octet

TLV.

◦ Default PSE assigned class delivers the maximum PSE capable power at initial power up based on PD

requested class.

• Always-on PoE is a feature that provides the ability for a switch to continue to provide power across user
initiated reboots through software. Always-on PoE is enabled by default and no additional configuration
is needed.

NOTE: PDs only remain powered, no data transfer or PoE power negotiation can occur until the
switch has completely booted up and in normal operation. PD faults occurring prior to full
switch boot up will result in PoE power removal and restart the detection process only after
switch returns to normal operation.

PoE commands
All PoE configuration commands except threshold configuration and always-on poe
configuration are entered at the config-if context. The PoE threshold command is used at the system
level whereas the always-on poe command is set at the slot level. These commands can only be
configured in the global configuration context.

lldp dot3 poe

Syntax

lldp dot3 poe

no lldp dot3 poe

Description

Enables 802.3 TLV list in LLDP to advertise for Power over Ethernet Data Link Layer Classification. LLDP dot3
TLV is by default enabled for PoE.

The no form of this command disables 802.3 TLV list in LLDP.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Enabling 802.3 TLV list in LLDP:

switch(config)# interface 1/1/1
switch(config-if)# lldp dot3 poe

Disabling 802.3 TLV list in LLDP:

Chapter 11 Power-over-Ethernet (PoE)

123

switch(config-if)# no lldp dot3 poe

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

Command context

config-if

Parameters
[priority-override]

System defined name of the interface.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Enabling and disabling LLDP MED PoE:

switch(config)# interface 1/1/1
switch(config-if)# lldp med poe
switch(config-if)# no lldp med poe

Enabling and disabling LLDP MED PoE priority override:

switch(config-if)# lldp med poe priority-override

power-over-ethernet

Syntax

power-over-ethernet

no power-over-ethernet

Description

Enables per-interface power distribution. Per-port power is enabled by default with priority low. PoE cannot
be disabled for individual ports when Quick PoE is enabled for the entire switch or line module.

The no form of this command disables per-interface power distribution.

124

AOS-CX 10.06 Monitoring Guide

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Enabling per-interface power distribution:

switch(config)# interface 1/1/1
switch(config-if)# power-over-ethernet

Disabling per-interface power distribution:

switch(config-if)# no power-over-ethernet

Showing Quick PoE enabled:

switch(config-if)# power-over-ethernet quick-poe 1/1
switch(config-if)# interface 1/1/1
switch(config-if)# no power-over-ethernet
Interface PoE cannot be disabled when Quick PoE is enabled.

power-over-ethernet allocate-by

Syntax

power-over-ethernet allocate-by {usage | class}

no power-over-ethernet allocate-by {usage | class}

Description

Configures the power allocation method. Power allocation method is initially based on usage. PSE Allocated
power value will change to LLDP negotiated power if and when LLDP exchange takes place between PSE and
PD. When there is no LLDP negotiation, PSE Allocated Power Value will be the actual instantaneous power
draw and reserve power based on actual consumption. In allocate-by class, power allocation is based on PD
requested class and PSE allocated power value will be the LLDP negotiated power when LLDP exchange
takes place between PSE and PD. . When there is no LLDP negotiation, PSE Allocate Power will be based on
PD class. Reserve power is based on PD Class. By default, power allocation is by usage.

The no form of this command resets the action to default.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Configuring the power allocation method:

Chapter 11 Power-over-Ethernet (PoE)

125

switch(config)# interface 1/1/1
switch(config-if)# power-over-ethernet allocate-by usage
switch(config-if)# power-over-ethernet allocate-by class

Resetting power allocation method:

switch(config-if)# no power-over-ethernet allocate-by class

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

Command context

config

Parameters
<MODULE-ID>

Module number to apply always-on PoE configuration.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling per-interface power distribution:

switch(config)# power-over-ethernet always-on 1/1

Disabling per-interface power distribution:

switch(config)# no power-over-ethernet always-on 1/1

power-over-ethernet assigned-class

Syntax

power-over-ethernet assigned-class {3 | 4 | 6}

no power-over-ethernet assigned-class

Description

Limit PoE power based on the assigned class. When an user assigns a maximum class to an interface, the
PSE will limit the maximum power delivered to the PD up to a total power draw not exceeding the PSE

126

AOS-CX 10.06 Monitoring Guide

assigned-class power. Power demotion occurs when a PD requested class is higher than the PSE assigned
class, permitting the PD to receive power and operate in a reduced power mode. PoE ports cannot set an
assigned class when Quick PoE is enabled on the sybsystem. The default assigned class is 4 for 2-pair
capable PSE and 6 for 4-pair capable PSE.

The no form of this command resets the action to default.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Setting PoE assigned class:

switch(config)# interface 1/1/1
switch(config-if)# power-over-ethernet assigned-class 4

Resetting PoE assigned class to default:

switch(config-if)# no power-over-ethernet assigned-class 4

Showing Quick PoE enabled:

switch(config)# power-over-ethernet quick-poe 1/1
switch(config)# interface 1/1/1
switch(config)# power-over-ethernet assigned-class 4
Interface assigned class cannot be configured when Quick PoE is enabled.

power-over-ethernet pre-std-detect

Syntax

power-over-ethernet pre-std-detect

no power-over-ethernet pre-std-detect

Description

Before IEEE 802.3 released the first Power over Ethernet standard (802.3af), vendors had shipped PoE
capable switches and PD's. As we are backward compatible Aruba will support both IEEE standard and pre-
standard 802.3af Power over Ethernet PD's concurrently. This CLI allows the user to enable or disable
pre-802.3af-standard device detection and powering on the specific port. When pre-std-detect is enabled,
power will be delivered on PairA only. Default is disabled.

The no form of this command resets the action to default.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Chapter 11 Power-over-Ethernet (PoE)

127

Examples

On the 6400 Switch Series, interface identification differs.

Enabling standard device detection:

switch(config)# interface 1/1/1
switch(config-if)# power-over-ethernet pre-std-detect

Disabling standard device detection:

switch(config-if)# no power-over-ethernet pre-std-detect

power-over-ethernet priority

Syntax

power-over-ethernet priority {critical | high | low}

no power-over-ethernet priority {critical | high | low}

Description

Sets PoE priority for an interface Specifying critical, high, or low indicates the priority of the interface in the
event of power over-subscription. Within the same priority level, higher power-priority line-module ports
have higher precedence. With same PoE priority and same line-module priority, lower numbered line-
module ports have higher precedence. Per-interface PoE priority is low by default.

The no form of this command resets the priority to default PoE priority "low".

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring PoE priority:

switch(config)# interface 1/1/1
switch(config-if)# power-over-ethernet priority critical
switch(config-if)# power-over-ethernet priority high

Resetting the PoE priority to default:

switch(config-if)# no power-over-ethernet priority high

power-over-ethernet quick-poe

Syntax

power-over-ethernet quick-poe <MODULE-ID>

no power-over-ethernet

Description

Quick PoE is a feature that provides the ability for the switch to provide power to the connected powered
device as soon as switch goes through cold reboot. When quick PoE is enabled on the subsystem PoE port

128

AOS-CX 10.06 Monitoring Guide

disablement and PD demotion is not allowed. also quick PoE enablement is not allowed if any of the port is
disabled on the subsystem. User should not over-subscribe the PoE power when quick PoE is enabled. Quick
PoE saved configuration will work irrespective of the configuration change at reboot.

Enables quick PoE feature on the switch or the subsystem level. By default, quick-PoE is disabled for the
subsystem.

The no form of this command disables quick PoE.

Command context

config-if

Parameters
<MODULE-ID>

Specifies module number for quick PoE configuration .

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Enabling and disabling quick PoE:

switch(config)# power-over-ethernet quick-poe 1/2
switch(config)# no power-over-ethernet quick-poe 1/1

switch(config-if)# power-over-ethernet quick-poe 1/1
PoE must be enabled on all interfaces before enabling Quick PoE

switch(config-if)# power-over-ethernet quick-poe 1/3
All interfaces must use the default assigned class before enabling Quick PoE

power-over-ethernet threshold

Syntax

power-over-ethernet threshold <PERCENTAGE>

no power-over-ethernet threshold <PERCENTAGE>

Description

Sets the threshold at which the system will send an excess power consumption notification trap. Default
value is 80 percentage.

The no form of this command resets the action to default.

Command context

config

Parameters
<PERCENTAGE>

Excess power consumption trap threshold. Range 1-99.

Chapter 11 Power-over-Ethernet (PoE)

129

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the power-over-ethernet threshold:

switch(config)# power-over-ethernet threshold 75

Resetting the power-over-ethernet threshold to default:

switch(config-if)# no power-over-ethernet threshold 75

power-over-ethernet priority

Syntax

power-over-ethernet trap

no power-over-ethernet trap

Description

This command enables/disables the SNMP trap generation for PoE related events at system level. PoE trap
generation is enabled by default.

The no form of this command resets the priority to default PoE priority "low".

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling SNMP trap generation for PoE:

switch(config)# power-over-ethernet trap

Disabling SNMP trap generation for PoE:

switch(config-if)# no power-over-ethernet trap

show lldp local

Syntax

show lldp local-device [<INTERFACE-ID>]

Description

Displays information advertised by the switch if the LLDP feature is enabled by user.

Command context

Operator (>) or Manager (#)

130

AOS-CX 10.06 Monitoring Guide

Parameters
<INTERFACE-ID>

Specifies an interface. Format: member/slot/port

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

On the 6400 Switch Series, interface identification differs.

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

show lldp neighbor

Syntax

show lldp neighbor [<INTERFACE-ID>]

Description

Displays detailed information about a particular neighbor connected to a particular interface.

Command context

Operator (>) or Manager (#)

Parameters
<INTERFACE-ID>

Specifies an interface. Format: member/slot/port

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

On the 6400 Switch Series, interface identification differs.

Showing LLDP neighbor information when there is only one neighbor:

Chapter 11 Power-over-Ethernet (PoE)

131

switch# show lldp neighbor-info 1/1/10

Port                           : 1/1/10
Neighbor Entries               : 1
Neighbor Entries Deleted       : 0
Neighbor Entries Dropped       : 0
Neighbor Entries Aged-Out      : 0
Neighbor Chassis-Name          : 84:d4:7e:ce:5d:68
Neighbor Chassis-Description   : ArubaOS (MODEL: 325), Version Aruba IAP
Neighbor Chassis-ID            : 84:d4:7e:ce:5d:68
Neighbor Management-Address    : 169.254.41.250
Chassis Capabilities Available : Bridge, WLAN
Chassis Capabilities Enabled   :
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

show power-over-ethernet

Syntax

6300 Switch Series:

show power-over-ethernet [member <MEMBER-ID>] [brief]

6400 Switch Series:

show power-over-ethernet [<MODULE-ID>] [brief]

6300, 6400 Switch Series:

show power-over-ethernet [<IFRANGE> [brief]

Description

Displays the status information of the full system. Displays the brief status of all port or given port if
parameter brief is used. Displays the detailed status of given port.

Command context

Operator (>) or Manager (#)

Parameters
<MEMBER-ID>

Displays the detailed status of given member.

<MODULE-ID>

Displays detailed status for the given module.

132

AOS-CX 10.06 Monitoring Guide

<IFRANGE>

Port identifier range.

<IFNAME>

Display the detailed status of given port.

brief

Display the brief status of all ports or the given port.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing sample output for show power-over-ethernet on standalone box with VSF capabiity:

switch# show power-over-ethernet

System Power Status for member 1

  Configured  Power Status     : No redundancy
  Operational Power Status     : No redundancy
  Total Available Power        : 740 W
  Total Failover Pwr Avl       :   0 W
  Total Redundancy Power       :   0 W
  Total Power Drawn            :   0 W +/- 6W
  Total Power Reserved         :   0 W
  Total Remaining Power        : 740 W
  Trap Threshold               : 80 %
  Trap Enabled                 : Yes
  Always-on PoE Enabled        : 1/1
  Quick PoE Enabled            : None

Internal Power
        Total Power
  PS    (Watts)        Status
  ----- -------------  ---------------------
  1     0              Absent
  2     740            Ok

System Power Status for member 2

  Configured  Power Status     : No redundancy
  Operational Power Status     : No redundancy
  Total Available Power        : 600 W
  Total Failover Pwr Avl       :   0 W
  Total Redundancy Power       :   0 W
  Total Power Drawn            :   0 W +/- 6W
  Total Power Reserved         :   0 W
  Total Remaining Power        : 600 W
  Trap Threshold               : 80 %
  Trap Enabled                 : Yes
  Always-on PoE Enabled        : None
  Quick PoE Enabled            : None

Internal Power
        Total Power
  PS    (Watts)        Status

Chapter 11 Power-over-Ethernet (PoE)

133

----- -------------  ---------------------
  1     0              Absent
  2     600            Ok

Showing sample output for power-over-ethernet member:

switch# show power-over-ethernet member 1

System Power Status for member 1

  Configured  Power Status     : No redundancy
  Operational Power Status     : No redundancy
  Total Available Power        : 740 W
  Total Failover Pwr Avl       :   0 W
  Total Redundancy Power       :   0 W
  Total Power Drawn            :   0 W +/- 6W
  Total Power Reserved         :   0 W
  Total Remaining Power        : 740 W
  Trap Threshold               : 80 %
  Trap Enabled                 : No
  Always-on PoE Enabled        : 1/1
  Quick PoE Enabled            : 1/1

Internal Power
        Total Power
  PS    (Watts)        Status
  ----- -------------  ---------------------
  1     0              Absent
  2     740            Ok

Showing sample output for power-over-ethernet brief in a VSF stack:

switch# show power-over-ethernet brief

Status and Configuration Information for PoE

  Member 1 Power Status
    Available: 370 W  Reserved: 55.60 W  Remaining: 314.40 W
    Always-on PoE Enabled: 1/1
    Quick PoE Enabled: None

PoE      Pwr Power    Pre-std Alloc PSE Pwr PD Pwr PoE Port     PD     Cls Type
Port     En  Priority Detect  Act   Rsrvd   Draw   Status       Sign
-------  --- ------   ------- ----- ------  ------ ---------    -----  --- ----
1/1/1    Yes Low      Off     Class  0.0 W   0.0 W Denied       None   4   2
1/1/2    Yes Critical Off     Usage  1.6 W   1.5 W Delivering*  Single 0   1
1/1/3    Yes High     Off     Class 54.0 W  25.5 W Delivering*^ Dual   1/3 3
1/1/4    No  Low      On      Usage  0.0 W   0.0 W Disabled     None   N/A N/A

  Member 2 Power Status
    Available: 600 W  Reserved: 0.00 W  Remaining: 600 W
    Always-on PoE Enabled: None
    Quick PoE Enabled: None

PoE      Pwr Power    Pre-std Alloc PSE Pwr PD Pwr PoE Port     PD     Cls Type
Port     En  Priority Detect  Act   Rsrvd   Draw   Status       Sign
-------  --- ------   ------- ----- ------  ------ ---------    -----  --- ----
2/1/1    Yes Low      Off     Class  0.0 W   0.0 W Searching    None   N/A  N/A
2/1/2    Yes Critical Off     Usage  0.0 W   0.0 W Searching    None   N/A  N/A
2/1/3    Yes High     Off     Class  0.0 W   0.0 W Searching    None   N/A  N/A
2/1/4    No  Low      On      Usage  0.0 W   0.0 W Disabled     None   N/A  N/A

*This port may go down in the event of a PSU failure.
^This port is power demoted due to user config or power availabilty.

134

AOS-CX 10.06 Monitoring Guide

Showing sample output for power-over-ethernet brief for a Chassis system:

switch# show power-over-ethernet brief

Status and Configuration Information for PoE

  Power Status
    Available: 370 W  Reserved: 55.60 W  Remaining: 314.40 W
    Always-on PoE Enabled: 1/1,1/3,1/4,1/7
    Quick PoE Enabled: None

PoE      Pwr Power    Pre-std Alloc PSE Pwr PD Pwr PoE Port     PD     Cls Type
Port     En  Priority Detect  Act   Rsrvd   Draw   Status       Sign
-------  --- ------   ------- ----- ------  ------ ---------    -----  --- ----
1/1/1    Yes Low      Off     Class  0.0 W   0.0 W Denied       None   4   2
1/1/2    Yes Critical Off     Usage  1.6 W   1.5 W Delivering*  Single 0   1
1/1/3    Yes High     Off     Class 54.0 W  25.5 W Delivering^  Dual   1/3 3
1/1/4    No  Low      On      Usage  0.0 W   0.0 W Disabled     None   N/A N/A

*This port may go down in the event of a PSU failure.
^This port is power demoted due to user config or power availabilty.

Showing sample output for power-over-ethernet brief per-port:

switch# show power-over-ethernet 1/1/1 brief

Status and Configuration Information for port 1/1/1

  Member 1Power Status
    Available: 370 W  Reserved: 55.60 W  Remaining: 314.40 W
    Always-on PoE Enabled: 1/1
PoE      Pwr Power    Pre-std Alloc PSE Pwr PD Pwr PoE Port     PD     Cls Type
Port     En  Priority Detect  Act   Rsrvd   Draw   Status       Sign
-------  --- ------   ------- ----- ------  ------ ---------    -----  --- ----
1/1/1    Yes Low      Off     Class  0.0 W   0.0 W Denied       None   4   2

Showing sample output for power-over-ethernet brief for interface range:

switch# show power-over-ethernet 1/1/1-1/1/2 brief

Status and Configuration Information for port 1/1/1-1/1/2

  Member 1Power Status
    Available: 370 W  Reserved: 55.60 W  Remaining: 314.40 W
    Always-on PoE Enabled: 1/1
PoE      Pwr Power    Pre-std Alloc PSE Pwr PD Pwr PoE Port     PD     Cls Type
Port     En  Priority Detect  Act   Rsrvd   Draw   Status       Sign
-------  --- ------   ------- ----- ------  ------ ---------    -----  --- ----
1/1/1    Yes Low      Off     Class  0.0 W   0.0 W Denied       None   4   2
1/1/2    Yes Critical Off     Usage  1.6 W   1.5 W Delivering*  Single 0   1

Showing sample output for power-over-ethernet for a missing line card:

switch# show power-over-ethernet 1/3 brief

Module 1/3 is not physically present.

Showing sample output for power-over-ethernet brief for a missing member:

switch# show power-over-ethernet member 3 brief

Member 3 is not physically present.

Chapter 11 Power-over-Ethernet (PoE)

135

Showing sample output for power-over-ethernet port when physical interface is not present:

switch# show power-over-ethernet 2/1/1

Interface 2/1/1 is not present.

136

AOS-CX 10.06 Monitoring Guide

Chapter 12
Aruba AirWave

You can manage and monitor the AOS-CX switch through Aruba AirWave. The following benefits and
functions include:

• Configuration (partial configuration)

• Device topology

•

Immediate and historical trend reports

• Monitoring of the device and user connected to the network.

• Network discovery

• Syslogs and trap receiver

For information about which versions of Aruba AirWave support AOS-CX, see the ArubaOS-CX Release Notes.

SNMP support and AirWave
For AirWave to discover and monitor the switch, you must:

• Enable the SNMP services on the switch.

• Configure the SNMP agent to use the SNMP version supported by the management station.

SNMP on the switch

The switch provides SNMP services through the management channel and the data interfaces. Functionality,
such as device discovery from NMS, syslog and trap forwarding, can be any channel configured by you.

Although the SNMP server can be enabled on both VRFs (mgmt and default), only one instance of SNMP
can be running. The highest priority is on the default VRF.

For example, assume that SNMP is first enabled on the mgmt VRF (snmp-server vrf mgmt). Then, SNMP is
enabled on the default VRF (snmp-server vrf default) without disabling SNMP on the mgmt (using an
equivalent no form of the command). The show running-config command displays both snmp-server
vrf commands; however, the SNMP instance is running only on the default VRF (highest priority).

switch# config
switch(config)# snmp-server vrf mgmt
switch(config)# snmp-server vrf default
switch(config)# show running-config
Current configuration:
!
!Version ArubaOS-CX Virtual.10.01.
led locator on
!
!
!
snmp-server vrf default
snmp-server vrf mgmt
!
...

Chapter 12 Aruba AirWave

137

Supported features with AirWave and the AOS-CX
switch
AirWave supports the following features with the AOS-CX switch:

Device management

Device discovery using SNMPv2C and SNMPv3

Monitoring management

Device health attributes (device status/reachability)

Device dashboards

Interface and VLAN management

Initiates an SSH connection from Aruba AirWave to AOS-CX so that the
device outputs from the AOS-CX CLI can be displayed in the Aruba
AirWave user interface.

Firmware versions

Displays neighbor devices connected to AOS-CX switches

Configuration management

Partial configuration

Device topology

Alarm management

Alarm triggers (device and interface up/down, new device discoveries,
custom event triggers)

Syslogs and traps

Report management

Device inventory, interface utilization, and device reachability reports

Summary report of device model, firmware, and boot loader version

Configuring the AOS-CX switch to be monitored by
AirWave

Prerequisites

Aruba AirWave is active on the network.

Procedure

1. Enable SNMP on the ArubaOS-CX switch by entering the snmp-server vrf command.

switch(config)# snmp-server vrf mgmt
switch(config)# snmp-server vrf default

2. Configure the SNMPv2C community to public by entering the snmp-server community public

command. In this instance, public is a read-only community string.

138

AOS-CX 10.06 Monitoring Guide

switch(config)# snmp-server community public

3. The community-string is used by SNMPv1 and SNMPv2C for unencrypted authentication. SNMPv3 lets
you encrypt the authentication mechanism. To enable SNMPv3, enter the snmpv3 user and snmpv3
context commands.

switch(config)# snmpv3 user Admin auth sha auth-pass ciphertext
AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=
priv des priv-pass ciphertext AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=

switch(config)# snmpv3 context Admin

For discovering devices in AirWave through the SNMPv3 community, the SNMPv3 context name is not
mandatory. Devices can still be discovered in Aruba AirWave without the SNMPv3 context name.

4. Enter the logging command for enabling syslog forwarding to a remote syslog server, such as AirWave:

switch(config)# logging 10.0.10.2 severity debug

5. SNMP traps enable an agent to notify the management station of significant events by way of an
unsolicited SNMP message. Enable SNMP traps by entering the snmp-server host command:

switch(config)# snmp-server host 10.10.10.10 trap version v2c vrf default

SNMP traps cannot be forwarded from AOS-CX 10.00 switches that have the VRF configured as mgmt.
Later versions of AOS-CX support SNMP trap forwarding even when the VRF is configured as default or
mgmt.

6. For information on how to add a device for monitoring in the Aruba AirWave user interface, see the

documentation for Aruba AirWave.

logging

Syntax

logging {<IPV4-ADDR> | <IPV6-ADDR> | <HOSTNAME>}
     [udp [<PORT-NUM>] | tcp [<PORT-NUM>]] [include-auditable-events]
     [severity <LEVEL>] [vrf <VRF-NAME>]

no logging {<IPV4-ADDR> | <IPV6-ADDR> | <HOSTNAME>}
     [udp [<PORT-NUM>] | tcp [<PORT-NUM>]] [severity <LEVEL>]
     [vrf <VRF-NAME>]

no logging

Description

Enables syslog forwarding to a remote syslog server.

The no form of this command disables syslog forwarding to a remote syslog server.

Command context

config

Parameters
{<IPV4-ADDR> | <IPV6-ADDR> | <HOSTNAME>}

Selects the IPv4 address, IPv6 address, or host name of the remote syslog server. Required.

[udp [<PORT-NUM>] | tcp [<PORT-NUM>]]

Specifies the UDP port or TCP port of the remote syslog server to receive the forwarded syslog
messages.

Chapter 12 Aruba AirWave

139

udp [<PORT-NUM>]

Range: 1 to 65535. Default: 514

tcp [<PORT-NUM>]

Range: 1 to 65535. Default: 1470

include-auditable-events

Specifies that auditable messages are also logged to the remote syslog server.

severity <LEVEL>

Specifies the severity of the syslog messages:

• alert: Forwards syslog messages with the severity of alert (6) and emergency (7).

• crit: Forwards syslog messages with the severity of critical (5) and above.

• debug: Forwards syslog messages with the severity of debug (0) and above.

• emerg: Forwards syslog messages with the severity of emergency (7) only.

• err: Forwards syslog messages with the severity of err (4) and above

• info: Forwards syslog messages with the severity of info (1) and above. Default.

• notice: Forwards syslog messages with the severity of notice (2) and above.

• warning: Forwards syslog messages with the severity of warning (3) and above.

vrf <VRF-NAME>

Specifies the VRF used to connect to the syslog server. Optional. Default: default

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling the syslog forwarding to remote syslog server 10.0.10.2:

switch(config)# logging 10.0.10.2

Enabling the syslog forwarding of messages with a severity of err (4) and above to TCP port 4242 on
remote syslog server 10.0.10.9 with VRF lab_vrf:

switch(config)# logging 10.0.10.9 tcp 4242 severity err vrf lab_vrf

Disabling syslog forwarding to a remote syslog server:

switch(config)# no logging

snmp-server community

Syntax

snmp-server community <STRING>

no snmp-server community <STRING>

140

AOS-CX 10.06 Monitoring Guide

Description

Adds an SNMPv1/SNMPv2c community string. A community string is a password that controls read access to
the SNMP agent. A network management program must supply this name when attempting to get SNMP
information from the switch. A maximum of 10 community strings are supported. Once you create your own
community string, the default community string (public) is deleted.

The no form of this command removes the specified SNMPv1/SNMPv2c community string. When no
community string exists, a default community string with the value public is automatically defined.

Command context

config

Parameters
<STRING>

Specifies the SNMPv1/SNMPv2c community string. Range: 1 to 32 printable ASCII characters, excluding
space and question mark.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the SNMPv1/SNMPv2c community string to private:

switch(config)# snmp-server community private

Removing SNMPv1/SNMPv2c community string private:

switch(config)# no snmp-server community private

snmp-server host

Syntax

snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>]
[port <UDP-PORT>] [vrf <VRF-NAME>]

no snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>]
[port <UDP-PORT>] [vrf <VRF-NAME>]

snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]
[port <UDP-PORT>] [vrf <VRF-NAME>]

no snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]
[port <UDP-PORT>] [vrf <VRF-NAME>]

snmp-server host <IPv4-ADDR> [trap version v3 | inform version v3] user <NAME>
[port <UDP-PORT>] [vrf <VRF-NAME>]

no snmp-server host <IPv4-ADDR> [trap version v3 | inform version v3] user <NAME>
[port <UDP-PORT>] [vrf <VRF-NAME>]

Description

Configures a trap/informs receiver to which the SNMP agent can send SNMP v1/v2c/v3 traps or v2c informs.
A maximum of 30 SNMP traps/informs receivers can be configured.

Chapter 12 Aruba AirWave

141

The no form of this command removes the specified trap/inform receiver.

NOTE: Configuring snmpv3 informs is not supported.

Command context

config

Parameters
<IPv4-ADDR>

Specifies the IP address of a trap receiver in IPv4 format (x.x.x.x), where x is a decimal number from 0
to 255. You can remove leading zeros. For example, the address 192.169.005.100 becomes
192.168.5.100.

trap version <VERSION>

Specifies the trap notification type for SNMPv1 or v2c. Available options are: v1 or v2c.

inform version v2c

Specifies the inform notification type for SNMPv2c.

trap version v3

Specifies the trap notification type for SNMPv3.

user <NAME>

Specifies the SNMPv3 user name to be used in the SNMP trap notifications.

community <STRING>

Specifies the name of the community string to use when sending trap notifications. Range: 1 - 32
printable ASCII characters, excluding space and question mark. Default: public.

<UDP-PORT>

Specifies the UDP port on which notifications are sent. Range: 1 - 65535. Default: 162.

vrf <VRF-NAME>

Specifies the name of the VRF on which to send the notifications.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# snmp-server host 10.10.10.10 trap version v1
switch(config)# no snmp-server host 10.10.10.10 trap version v1

switch(config)# snmp-server host 10.10.10.10 trap version v2c community public
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public

switch(config)# snmp-server host 10.10.10.10 trap version v2c community public port 5000
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public port 5000

switch(config)# snmp-server host 10.10.10.10 trap version v2c community public port 5000 vrf default
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public port 5000 vrf default

switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public

switch(config)# snmp-server host 10.10.10.10 inform version v2c community public port 5000
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public port 5000

switch(config)# snmp-server host 10.10.10.10 inform version v2c community public port 5000 vrf default

142

AOS-CX 10.06 Monitoring Guide

switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public port 5000 vrf default

switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin

switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin port 2000
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin port 2000

snmp-server vrf

Syntax

snmp-server vrf <VRF-NAME>

no snmp-server vrf <VRF-NAME>

Description

Configures the VRF on which the SNMP agent listens for incoming requests. By default, the SNMP agent
does not listen on any VRF.

The no form of this command stops the SNMP agent from listening for incoming requests on the specified
VRF.

Command context

config

Parameters
<VRF-NAME>

Specifies the VRF on which the SNMP agent listens for incoming requests. The SNMP agent can listen on
either the mgmt or default VRF. If configured for both, the SNMP agent listens on default, which has a
higher priority.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# snmp-server vrf default

switch(config)# no snmp-server vrf default

snmpv3 context

Syntax

snmpv3 context <NAME> vrf <VRF-NAME> [community <STRING>]

no snmpv3 context <NAME> [vrf <VRF-NAME>]

Description

Creates an SNMPv3 context on the specified VRF.

The no form of this command removes the specified SNMP context.

Command context

config

Chapter 12 Aruba AirWave

143

Parameters
<NAME>

Specifies the name of the context. Range: 1 to 32 printable ASCII characters, excluding space and
question mark (?).

vrf <VRF-NAME>

Specifies the VRF associated with the context. Default: default.

community <STRING>

Specifies the SNMP community string associated with the context. Range: 1 to 32 printable ASCII
characters, excluding space and question mark. Default: public.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating an SNMPv3 context named newContext:

switch(config)# snmpv3 context newContext

Creating an SNMPv3 context named newContext on VRF myVrf and with community string private.

switch(config)# snmpv3 context newContext vrf myVrf community private

Removing the SNMPv3 context named newContext on VRF myVrf:

switch(config)# no snmpv3 context newContext vrf myVrf

snmpv3 user

Syntax

snmpv3 user <NAME> [auth <AUTH-PROTOCOL> auth-pass {plaintext | ciphertext}
<AUTH-PWORD> [priv <PRIV-PROTOCOL> priv-pass {plaintext | ciphertext} <PRIV-PWORD>] ]

no snmpv3 user <NAME> [auth <AUTH-PROTOCOL> auth-pass
<AUTH-PWORD> [priv <PRIV-PROTOCOL> priv-pass <PRIV-PWORD>] ]

Description

Creates an SNMPv3 user and adds it to an SNMPv3 context.

The no form of this command removes the specified SNMPv3 user.

Command context

config

Parameters
<NAME>

Specifies the SNMPv3 username. Range 1 - 32 printable ASCII characters, excluding space and question
mark.

auth <AUTH-PROTOCOL>

Specifies the authentication protocol used to validate user logins. Available options are: md5 or sha.

144

AOS-CX 10.06 Monitoring Guide

auth-pass {plaintext | ciphertext} <AUTH-PWORD>

Specifies the SNMPv3 user password. Range for plaintext is 8 - 32 printable ASCII characters,
excluding space and question mark.

Range for ciphertext is 1 - 120 printable ASCII characters. This option is only used when copying user
configuration settings between switches. It enables you to duplicate a user's configuration on another
switch without having to know their password.

priv <PRIV-PROTOCOL>

Specifies the SNMPv3 security protocol (encryption method). Available options are: aes or des.

priv-pass {plaintext | ciphertext} <PRIV-PWORD>

Specifies the SNMPv3 user privacy passphrase. Range for plaintext is 8 - 32 printable ASCII characters,
excluding space and question mark.

Range for ciphertext is 1 - 120 printable ASCII characters. This option is only used when copying user
configuration settings between switches. It enables you to duplicate a user's configuration on another
switch without having to know their password.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defining an SNMPv3 user named Admin using sha authentication with the plaintext password mypassword
and using des security with the plaintext password myprivpass:

switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des priv-pass plaintext myprivpass

Removing an SNMPv3 user named Admin:

switch(config)# no snmpv3 user Admin

Defining an SNMPv3 user named Admin using sha authentication with the plaintext password mypassword
and using des security with the plaintext password myprivpass:

switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des priv-pass plaintext myprivpass

Copying an SNMP user from switch 1 to switch 2.

On switch 1, configure a user called Admin, then issue the show running-config command to display
switch configuration settings. The snmpv3 user command uses the ciphertext option to protect the
users's passwords.

switch1(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword
priv des priv-pass plaintext myprivpass
switch1(config)# exit
switch1# show running-config
Current configuration:
!
!Version ArubaOS-CX TL.10.00.0003-8017-gdeb0606~dirty
!
!
!
snmpv3 user Admin auth sha auth-pass ciphertext
AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=
priv des priv-pass ciphertext AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=
ssh server vrf mgmt
!
!
!
!
interface mgmt
    no shutdown

Chapter 12 Aruba AirWave

145

ip dhcp
vlan 1

On switch 2, execute the snmpv3 user command that was displayed by show running-config on switch 1.
This creates the user on switch 2 with the same configuration settings.

switch1(config)# snmpv3 user Admin auth sha auth-pass ciphertext
AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=
priv des priv-pass ciphertext AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=

146

AOS-CX 10.06 Monitoring Guide

Chapter 13
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

Chapter 13 Support and other resources

147

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

148

AOS-CX 10.06 Monitoring Guide