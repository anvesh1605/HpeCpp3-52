AOS-CX 10.09 Monitoring
Guide

8320, 8325, 8360 Switch Series

Published: September 2022
Edition: 4

Copyright Information

© Copyright 2023 Hewlett Packard Enterprise Development LP.

Open Source Code

This product includes code licensed under the GNU General Public License, the GNU Lesser General
Public License, and/or certain other open source licenses. A complete machine-readable copy of the
source code corresponding to such code is available upon request. This offer is valid to anyone in
receipt of this information and shall expire three years following the date of the final distribution of this
product version by Hewlett Packard Enterprise Company. To obtain such source code, send a check or
money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company
6280 America Center Drive
San Jose, CA 95002
USA

Notices

The information contained herein is subject to change without notice. The only warranties for Hewlett
Packard Enterprise products and services are set forth in the express warranty statements
accompanying such products and services. Nothing herein should be construed as constituting an
additional warranty. Hewlett Packard Enterprise shall not be liable for technical or editorial errors or
omissions contained herein.

Confidential computer software. Valid license from Hewlett Packard Enterprise required for possession,
use, or copying. Consistent with FAR 12.211 and 12.212, Commercial Computer Software, Computer
Software Documentation, and Technical Data for Commercial Items are licensed to the U.S. Government
under vendor's standard commercial license.

Links to third-party websites take you outside the Hewlett Packard Enterprise website. Hewlett Packard
Enterprise has no control over and is not responsible for information outside the Hewlett Packard
Enterprise website.

Acknowledgment

Intel®, Itanium®, Optane™, Pentium®, Xeon®, Intel Inside®, and the Intel Inside logo are trademarks of
Intel Corporation in the U.S. and other countries.

Microsoft® and Windows® are either registered trademarks or trademarks of Microsoft Corporation in
the United States and/or other countries.

Adobe® and Acrobat® are trademarks of Adobe Systems Incorporated.

Java® and Oracle® are registered trademarks of Oracle and/or its affiliates.

UNIX® is a registered trademark of The Open Group.

All third-party marks are property of their respective owners.

| 2

Contents
Contents
| Contents                            |                                  |              |                    | 3   |
| ----------------------------------- | -------------------------------- | ------------ | ------------------ | --- |
| About                               | this document                    |              |                    | 6   |
| Applicableproducts                  |                                  |              |                    | 6   |
| Latestversionavailableonline        |                                  |              |                    | 6   |
| Commandsyntaxnotationconventions    |                                  |              |                    | 6   |
| Abouttheexamples                    |                                  |              |                    | 7   |
| Identifyingswitchportsandinterfaces |                                  |              |                    | 7   |
| Identifyingmodularswitchcomponents  |                                  |              |                    | 8   |
| Monitoring                          | hardware                         | through      | visual observation | 9   |
| DiagnosingwiththeLEDs               |                                  |              |                    | 9   |
| Aruba                               | 8320 Switch                      | Series LEDs  |                    | 13  |
| ChassisLEDs                         |                                  |              |                    | 13  |
| PortLEDs                            |                                  |              |                    | 14  |
| Aruba                               | 8325 Switch                      | Series LEDs  |                    | 16  |
| ChassisLEDs                         |                                  |              |                    | 16  |
| PortLEDs                            |                                  |              |                    | 18  |
| Alarmcommands                       |                                  |              |                    | 21  |
|                                     | alarm                            |              |                    | 21  |
|                                     | alarminput                       |              |                    | 22  |
|                                     | alarmsnooze                      |              |                    | 24  |
|                                     | showalarm                        |              |                    | 24  |
|                                     | showalarminput                   |              |                    | 25  |
|                                     | showalarmtimer                   |              |                    | 26  |
| Boot                                | commands                         |              |                    | 28  |
| bootfabric-module                   |                                  |              |                    | 28  |
| bootline-module                     |                                  |              |                    | 29  |
| bootmanagement-module               |                                  |              |                    | 30  |
| bootset-default                     |                                  |              |                    | 31  |
| bootsystem                          |                                  |              |                    | 32  |
| showboot-history                    |                                  |              |                    | 34  |
| Switch                              | system                           | and hardware | commands           | 36  |
| External                            | storage                          |              |                    | 37  |
| Externalstoragecommands             |                                  |              |                    | 37  |
|                                     | address(externalstorage)         |              |                    | 37  |
|                                     | directory                        |              |                    | 38  |
|                                     | disableexternal-storagelogfiles  |              |                    | 39  |
|                                     | enable(external-storagelogfiles) |              |                    | 39  |
|                                     | external-storage                 |              |                    | 40  |
|                                     | password(external-storage)       |              |                    | 41  |
|                                     | showexternal-storage             |              |                    | 42  |
3
AOS-CX10.09MonitoringGuide| (83xxSwitchSeries)

| showrunning-configexternal-storage |          |            | 43  |
| ---------------------------------- | -------- | ---------- | --- |
| type(externalstorage)              |          |            | 43  |
| username(externalstorage)          |          |            | 44  |
| vrf(externalstorage)               |          |            | 45  |
| IP-SLA                             |          |            | 47  |
| IP-SLAguidelines                   |          |            | 47  |
| LimitationswithVoIPSLAs            |          |            | 48  |
| IP-SLAcommands                     |          |            | 48  |
| http                               |          |            | 48  |
| icmp-echo                          |          |            | 49  |
| ip-sla                             |          |            | 50  |
| ip-slaresponder                    |          |            | 51  |
| showip-slaresponder                |          |            | 52  |
| showip-slaresponderresults         |          |            | 53  |
| showip-sla<SLA-NAME>               |          |            | 53  |
| start-test                         |          |            | 57  |
| stop-test                          |          |            | 57  |
| tcp-connect                        |          |            | 58  |
| udp-echo                           |          |            | 59  |
| udp-jitter-voip                    |          |            | 60  |
| vrf(ipsla)                         |          |            | 61  |
| L1-100Mbpsdownshiftcommands        |          |            | 62  |
| downshiftenable                    |          |            | 62  |
| showinterface                      |          |            | 63  |
| showinterfacedownshift-enable      |          |            | 66  |
| showrunning-configinterface        |          |            | 67  |
| Mirroring                          |          |            | 69  |
| MirroringstatisticsandsFlow        |          |            | 69  |
| Limitations                        |          |            | 69  |
| Mirroringcommands                  |          |            | 70  |
| clearmirror                        |          |            | 70  |
| comment                            |          |            | 70  |
| copytcpdump-pcap                   |          |            | 72  |
| copytshark-pcap                    |          |            | 72  |
| destinationcpu                     |          |            | 73  |
| destinationinterface               |          |            | 74  |
| destinationtunnel                  |          |            | 75  |
| diagnostic                         |          |            | 77  |
| diagutilitiestcpdump               |          |            | 78  |
| disable(mirrorsession)             |          |            | 80  |
| enable(mirrorsession)              |          |            | 80  |
| mirrorsession                      |          |            | 81  |
| showmirror                         |          |            | 82  |
| sourceinterface                    |          |            | 84  |
| sourcevlan                         |          |            | 86  |
| Monitoring                         | a device | using SNMP | 88  |
| PoEcommands                        |          |            | 88  |
| lldpdot3poe                        |          |            | 88  |
| lldpmedpoe                         |          |            | 89  |
| power-over-ethernet                |          |            | 89  |
| power-over-ethernetallocate-by     |          |            | 90  |
| power-over-ethernetalways-on       |          |            | 91  |
| power-over-ethernetassigned-class  |          |            | 92  |
Contents|4

|                                                  | power-over-ethernetpower-pairs    |           | 93  |
| ------------------------------------------------ | --------------------------------- | --------- | --- |
|                                                  | power-over-ethernetpre-std-detect |           | 94  |
|                                                  | power-over-ethernetpriority       |           | 95  |
|                                                  | power-over-ethernetquick-poe      |           | 95  |
|                                                  | power-over-ethernetthreshold      |           | 96  |
|                                                  | power-over-ethernettrap           |           | 97  |
|                                                  | showlldplocal                     |           | 98  |
|                                                  | showlldpneighbor                  |           | 99  |
|                                                  | showpower-over-ethernet           |           | 100 |
| Breakout                                         | cable support                     |           | 102 |
| Limitationswithbreakoutcablesupport              |                                   |           | 102 |
| Breakoutcablesupportcommands                     |                                   |           | 102 |
|                                                  | split                             |           | 102 |
| Aruba                                            | AirWave                           |           | 105 |
| SNMPsupportandAirWave                            |                                   |           | 105 |
|                                                  | SNMPontheswitch                   |           | 105 |
| SupportedfeatureswithAirWaveandtheAOS-CXswitch   |                                   |           | 106 |
| ConfiguringtheAOS-CXswitchtobemonitoredbyAirWave |                                   |           | 106 |
| Support                                          | and Other                         | Resources | 108 |
| AccessingArubaSupport                            |                                   |           | 108 |
| AccessingUpdates                                 |                                   |           | 109 |
|                                                  | ArubaSupportPortal                |           | 109 |
|                                                  | MyNetworking                      |           | 109 |
| WarrantyInformation                              |                                   |           | 109 |
| RegulatoryInformation                            |                                   |           | 109 |
| DocumentationFeedback                            |                                   |           | 110 |
5
AOS-CX10.09MonitoringGuide| (83xxSwitchSeries)

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL704C, JL705C, JL706A, JL707A, JL708A,

JL709A, JL710A, JL711A, JL717C, JL718C)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

Usage

example-text

Identifies commands and their options and operands, code examples,
filenames, pathnames, and output displayed in a command window. Items
that appear like the example text in the previous column are to be entered
exactly as shown and are required unless enclosed in brackets ([ ]).

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

n For output formats where italic text cannot be displayed, variables
are enclosed in angle brackets (< >). Substitute the text—including
the enclosing angle brackets—with an actual value.

n For output formats where italic text can be displayed, variables

might or might not be enclosed in angle brackets. Substitute the
text including the enclosing angle brackets, if any, with an actual
value.

Vertical bar. A logical OR that separates multiple items from which you can
choose only one.
Any spaces that are on either side of the vertical bar are included for
readability and are not a required part of the command syntax.

AOS-CX 10.09 Monitoring Guide | (83xx Switch Series)

6

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
Examples in this document are representative and might not match your particular switch or
environment.

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

On the 83xx Switch Series

About this document | 7

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on

physical port 4 in slot 1 on member 1.

Identifying modular switch components

n Power supplies are on the front of the switch behind the bezel above the management modules.

Power supplies are labeled in software in the format: member/power supply:

o member: 1.

o power supply: 1 to 4.

n Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

o member: 1.

o tray: 1 to 4.

o fan: 1 to 4.

n Fabric modules are not labeled on the switch but are labeled in software in the format:

member/module:

o member: 1.

o member: 1 or 2.

n The display module on the rear of the switch is not labeled with a member or slot number.

AOS-CX 10.09 Monitoring Guide | (83xx Switch Series)

8

|     |     |     |            |          |         | Chapter | 2      |
| --- | --- | --- | ---------- | -------- | ------- | ------- | ------ |
|     |     |     | Monitoring | hardware | through |         | visual |
observation
| Monitoring | hardware | through | visual observation |     |     |     |     |
| ---------- | -------- | ------- | ------------------ | --- | --- | --- | --- |
| Diagnosing | with     | the     | LEDs               |     |     |     |     |
ThissectiondescribesLEDpatternsontheswitchthatindicateproblemconditionsforgeneralswitch
operationtroubleshooting.
1. CheckthetablefortheLEDpatternyouseeontheswitch.
2. Refertothecorrespondingdiagnostictip.
Table1:LEDerrorindicatorsfor8320
| Global status             |     | Port                  | LED | Diagnostic | tip |     |     |
| ------------------------- | --- | --------------------- | --- | ---------- | --- | --- | --- |
| Offwithpowercordpluggedin |     | N/A                   |     | 1          |     |     |     |
| Solidamber                |     | N/A                   |     | 2          |     |     |     |
| Slowflashamber            |     | N/A                   |     | 3          |     |     |     |
| Slowflashamber            |     | Slowflashamber*       |     | 4          |     |     |     |
| Solidgreen                |     | Offwithcableconnected |     | 5          |     |     |     |
| Solidgreen                |     | On,buttheportisnot    |     | 6          |     |     |     |
communicating
*Theflashingbehaviorisanon/offcycleapproximatelyonceevery1.6seconds.
Table2:LEDerrorindicatorsfor8325
| PS1/PS2      | LEDs Global | Status | Fan | Port LED |     | Diagnostic | Tip |
| ------------ | ----------- | ------ | --- | -------- | --- | ---------- | --- |
| Offwithpower | -           |        | -   | -        |     | 1          |     |
cordspluggedin
| Onamber** | Flashingamber |     | -       | -                     |     | 2   |     |
| --------- | ------------- | --- | ------- | --------------------- | --- | --- | --- |
| Ongreen   | Flashingamber |     | Onamber | -                     |     | 3   |     |
| Ongreen   | Flashingamber |     | -       | Flashingamber         |     | 4   |     |
| Ongreen   | Ongreen       |     | -       | Offwithcableconnected |     | 5   |     |
| Ongreen   | Ongreen       |     | -       | On,buttheportisnot    |     | 6   |     |
communicating
**EitherthePS1orPS2LEDisonamber,butnotboth.
Table3:Diagnostictips
9
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- | --- |

Tip

1

2

3

4

Problem

Solution

Both switch power supplies are

Verify the AC power source works by plugging another

not plugged into an active AC

device into the outlet.

power source.

Or try plugging the power supplies into different

outlets or try different power cords.

If the problem is still not resolved, both power

supplies may be faulty.

One of the power supplies is

Verify that the power cord is plugged into an active

not plugged into an active A

power source and to the power supply. Make sure that

power source, or the power

the connections are snug.

supply may have failed.

Try power cycling the switch by unplugging and

plugging the power cord back into the other working

power supply.

If the PS1/PS2 LED is still not on, verify the AC power

source works by plugging another device into the

outlet or try a different power cord.

If the power source and power cord are OK and this

condition persists, the switch power supply may have

failed. Call your Hewlett Packard Enterprise-authorized

network reseller, or use the electronic support

services from Hewlett Packard Enterprise to get

assistance.

One of the switch fan
assemblies may have failed.

Try disconnecting power from the switch and wait a
few moments. Then reconnect the power to the switch

and check the LEDs again If the error indication

reoccurs, one of the fan assemblies has failed. If the

ambient temperature does not exceed normal room

temperature, the switch may continue to operate

under this condition; but for best operation, replace

the fan assembly. Call your Hewlett Packard

Enterprise-authorized network reseller, or use the

electronic support services from Hewlett Packard

Enterprise to get assistance.

The network port for which the

Try power cycling the switch. If the fault indication

LED is flashing has experienced

reoccurs:

a self-test or initialization

n There may be a port configuration mismatch where

failure.

a 10G transceiver is installed in a port configured

for 25G, or the reverse.

n A 10GBase-T transceiver may be installed in an

incompatible port. Only ports 1, 2, 4, 5, 7, 8, 10, and

11 support 10GBase-T transceivers.

n The transceiver may have failed.
n The switch port may have failed.

Check the switch Event Log and show interface

Monitoring hardware through visual observation | 10

Tip

Problem

Solution

command output for indication of the fault condition.

If the port is an SFP+/SFP28 transceiver or

QSFP+/QSFP28 transceiver, verify that it is one of the

transceivers supported by the switch. Unsupported or

unrecognized transceivers will be identified with this

fault condition. For a list of supported transceivers,

see the Transceiver Guide in the Aruba Support Portal.

The transceivers are also tested when they are "hot-

swapped" - installed or changed while the switch is

powered on.

To verify that the port has failed, remove and reinstall

the transceiver without powering off the switch. If the

port fault indication reoccurs, you will have to replace

the transceiver. Check the event log to see why the

transceiver failed.

To get assistance, call your Hewlett Packard

Enterprise-authorized network reseller, or use the

electronic support services from Hewlett Packard

Enterprise.

5

The network connection is not

Try the following procedures:

working properly.

n For the indicated port, verify that both ends of the

cabling, at the switch and the connected device, are

connected properly.

n Verify that the connected device and switch are

both powered on and operating correctly.

n Verify that you have used the correct cable type for

the connection:

o For fiber-optic connections, verify that the

transmit port on the switch is connected to the

receive port on the connected device and that

the switch receive port is connected to the

transmit port on the connected device.

o The cable verification process must include all

patch cables from any end devices, including the

switch, to any patch panels in the cabling path.

n Verify that the port has not been disabled through

a switch configuration change. Use the console

interface or, if you have configured an IP address

on the switch, use the web browser interface to

determine the state of the port and re-enable the

port if necessary.

n Verify that the switch port configuration matches

the configuration of the attached device. For

example, if the switch port is configured as “Full-

AOS-CX 10.09 Monitoring Guide | (83xx Switch Series)

11

Tip

Problem

Solution

duplex”, the port on the attached device also MUST

be configured as “Full-duplex”. If the configurations

do not match, the results could be an unreliable

connection, or no link at all.

n If the other procedures do not resolve the problem,

try using a different port or a different cable.

6

The port may be improperly

Use the switch console to see if the port is part of a

configured, or the port may be

dynamic trunk (through the LACP feature), if Spanning

in a “blocking” state by the

Tree is enabled on the switch, and if the port may have

normal operation of the

Spanning Tree, LACP, or IGMP

features.

been put into a “blocking” state by those features. The
show lacp interfaces command displays the port
status for the LACP feature; the show spanning tree

command displays the port status for Spanning Tree.

Also check the Port Status screen using the show
interfaces command to see if the port has been
configured as “disabled”.

Other switch features that may affect the port

operation include VLANs, IGMP, and port group

settings. Use the switch console to see how the port is

configured for these features.

Ensure that the device at the other end of the

connection is indicating a good link to the switch. If it is

not, the problem may be with the cabling between the

devices or the connectors on the cable.

Monitoring hardware through visual observation | 12

|            |               |      |       |             | Chapter | 3    |
| ---------- | ------------- | ---- | ----- | ----------- | ------- | ---- |
|            |               |      | Aruba | 8320 Switch | Series  | LEDs |
| Aruba 8320 | Switch Series | LEDs |       |             |         |      |
| Chassis    | LEDs          |      |       |             |         |      |
Table1:ChassisLEDlabels
LED
| 1   |     | PowersupplyLEDs       |     |     |     |     |
| --- | --- | --------------------- | --- | --- | --- | --- |
| 2   |     | GlobalstatusLEDs      |     |     |     |     |
| 3   |     | FanLED                |     |     |     |     |
| 4   |     | UnitidentificationLED |     |     |     |     |
| 5   |     | Resetbutton           |     |     |     |     |
Table2:ChassisLEDbehavior
| Chassis LEDs | Function          |     | State   | Meaning                   |     |     |
| ------------ | ----------------- | --- | ------- | ------------------------- | --- | --- |
| PS1/PS2      | Powersupplystatus |     | Ongreen | Powersupplyisinstalledand |     |     |
operatingnormally.
Slowflashamber Faultdetectedforinstalled
powersupply.
Off Powersupplyisnotinstalledor
notreceivingpower.
| Fan | Fantraystatus |     | Ongreen | Systemfansareoperating |     |     |
| --- | ------------- | --- | ------- | ---------------------- | --- | --- |
normally.
Slowflashamber Oneormoresystemfanshave
afaultortheminimumnumber
offansarenotinstalled.
13
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- |

Chassis LEDs

Function

State

Meaning

Global Status

Internal power status of the

On amber

switch.

Self-test status

Switch/port fault status

Slow flash green*

Slow flash amber**

The switch has passed self-test
and is powered up normally.

The switch self-test and
initialization are in progress
after the switch has been
power cycled or reset. The
switch is not operational until
this LED stops blinking green.

A fault or initialization failure
has occurred on the switch,
one of the switch ports, OOBM
port, USB port, console port,
power supplies, or a fan. The
Status LED for the component
with the fault will flash
simultaneously.

Off

The unit is not receiving power.

UID (Unit
Identification)

Used to identify a unit in a rack
or collection of products.

On or slow flash^

Off

The LED locator on
command allows you to flash
or turn on the LED. The default
is 30 minutes.

LED will clear after the timeout
period has expired.

*The slow flash behavior is an on/off cycle approximately every 1.6 seconds.

**The slow flash behavior is an on/off cycle approximately every 1.6 seconds.

^The slow flash behavior is an on/off cycle approximately every 1.6 seconds.

Port LEDs

Table 1: Port LED labels

LED

1

QSFP+ port lane LEDs — these LEDs are not used by the product and should
remain off throughout the product's operation

Aruba 8320 Switch Series LEDs | 14

LED
2 SFP+portLEDs
3 QSFP+port51,54LEDs
4 QSFP+port49,50,52,53LEDs
5 Out-of-bandmanagementportLinkLED
6 Out-of-bandmanagementportAct(activity)LED
Table2:PortLEDbehavior
| Chassis LEDs | Function | State | Meaning |
| ------------ | -------- | ----- | ------- |
SFP+portLEDs Todisplaylinkandactivity On/flashinggreen Showsavalidlinkat1Gbpsor
|     | informationfortheport. |     | 10Gbps.Flashingindicates |
| --- | ---------------------- | --- | ------------------------ |
portactivity.
|     |     | Slowflashamber | WhentheGlobalStatusLEDis |
| --- | --- | -------------- | ------------------------ |
flashingamber,indicatesan
unsupportedtransceiverora
portfailure.
QSFP+portLEDs Todisplaylinkandactivity On/flashinggreen Showsavalidlinkat40Gbps.
|     | informationfortheport. |     | Flashingindicatesportactivity. |
| --- | ---------------------- | --- | ------------------------------ |
|     |                        | Off | WhentheGlobalStatusLEDis       |
flashingamber,indicatesan
unsupportedtransceiverora
portfailure.
Managementport Todisplaylinkinformationfor Ongreen Showsavalidlink.
| LinkLED | theport. |     |     |
| ------- | -------- | --- | --- |
Managementport Todisplayactivityinformation Flashinggreen Flashingindicatesportactivity.
| ActLED | fortheport. |     |     |
| ------ | ----------- | --- | --- |
15
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

|            |               |      |       |             | Chapter | 4    |
| ---------- | ------------- | ---- | ----- | ----------- | ------- | ---- |
|            |               |      | Aruba | 8325 Switch | Series  | LEDs |
| Aruba 8325 | Switch Series | LEDs |       |             |         |      |
| Chassis    | LEDs          |      |       |             |         |      |
Table1:ChassisLEDsfortheAruba8325-48Y8C(JL624AandJL625A)
LED
| 1   |     | Powersupply1(PS1)LEDs |     |     |     |     |
| --- | --- | --------------------- | --- | --- | --- | --- |
| 2   |     | Powersupply2(PS2)LEDs |     |     |     |     |
| 3   |     | FanLED                |     |     |     |     |
| 4   |     | GlobalstatusLED       |     |     |     |     |
| 5   |     | UnitidentificationLED |     |     |     |     |
16
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- |

Table2:ChassisLEDsfortheAruba8325-32C(JL626AandJL627A)
LED
1 UnitidentificationLED
2 GlobalstatusLED
3 Powersupply1(PS1)LEDs
4 Powersupply2(PS2)LEDs
5 FanLED
Table3:ChassisLEDbehavior
| Chassis LEDs | Function | State | Meaning |
| ------------ | -------- | ----- | ------- |
PS1/PS2 Powersupply Ongreen Powersupplyisinstalledandoperating
|     | status |         | normally.                             |
| --- | ------ | ------- | ------------------------------------- |
|     |        | Onamber | Faultdetectedforinstalledpowersupply, |
orpowersupplyisnotreceivingpower.
|     |               | Off     | Powersupplyisnotinstalled.      |
| --- | ------------- | ------- | ------------------------------- |
| Fan | Fantraystatus | Ongreen | Systemfansareoperatingnormally. |
|     |               | Onamber | Oneormoresystemfanshaveafaultor |
theminimumnumberoffansarenot
installed.
GlobalStatus Internalpower Ongreen Theswitchhaspassedself-testandis
poweredupnormally.
statusoftheswitch.
Self-teststatus
Flashingamber
|     | Switch/portfault |     | n Theswitchinitializationisinprogress |
| --- | ---------------- | --- | ------------------------------------- |
|     | status           |     | duringbootup.                         |
Aruba8325SwitchSeriesLEDs|17

| Chassis LEDs | Function | State | Meaning |     |
| ------------ | -------- | ----- | ------- | --- |
n Afaultorinitializationfailurehas
occurredontheswitch,oneofthe
switchports,powersupplies,orafan.
n TheportLEDswiththefaultwillflash
simultaneously.LEDsforpower
suppliesandfanswithafaultwillbeon
amber.
n Port-speedmismatch.Atransceiveris
installedinaportconfiguredfora
differentspeed.
|     |     | Off | Theunitisnotreceivingpower. |     |
| --- | --- | --- | --------------------------- | --- |
UID(Unit Usedtoidentifya Onblueorflashing TheLED locator oncommandallows
Identification) unitinarackor blue youturnontheLED.Thedefaultis30
collectionof
minutes.
products.
|     |     |     | TheLED locator | flashingcommand |
| --- | --- | --- | -------------- | --------------- |
willflashtheLED.
|     |     | Off | TheLED locator | offcommandturns |
| --- | --- | --- | -------------- | --------------- |
offtheLED.
Port LEDs
Table1:PortLEDsfortheAruba8325-48Y8C(JL624AandJL625A)
LED
| 1   |     | UpperSFP28portLED              |     |     |
| --- | --- | ------------------------------ | --- | --- |
| 2   |     | MiddleSFP28portLED             |     |     |
| 3   |     | LowerSFP28portLED              |     |     |
| 4   |     | QSFP28portLEDandlane1indicator |     |     |
18
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

5

6

7

8

9

LED

QSFP28 lane 2 LED

QSFP28 lane 3 LED

QSFP28 lane 4 LED

Out-of-band management port Link LED

Out-of-band management port Act (activity) LED

Table 2: Port LED behavior for the Aruba 8325-48Y8C (JL624A and JL625A)

Chassis LEDs

Function

State

Meaning

SFP28 port LEDs

To display link and activity
information for the port.

On/flashing green

Flashing amber

Off

QSFP28 port LEDs

To display link and activity
information for the port.

On/flashing green

Flashing amber

Off

Shows a valid link at 25/10
Gbps.

n Fast flashing* indicates port

activity at 25 Gbps.

n Slow flashing** indicates

port activity at 10 Gbps.

When the Global Status LED is
simultaneously flashing amber,
indicates port-speed mismatch,
an incompatible, unsupported,
faulty transceiver, or a port
failure.

Port is disabled, not connected,
or not receiving a link beat
signal.

Shows a valid link at 100/40
Gbps.

n Fast flashing^ indicates port

activity at 100 Gbps.
n Slow flashing^^ indicates

port activity at 40 Gbps.

When the Global Status LED is
simultaneously flashing amber
with the Lane 1 LED, indicates
an unsupported or faulty
transceiver, or a port failure.

Port is disabled, not connected,
or not receiving a link beat
signal.
Lanes 2-4 are always off and
are currently unused by HPE-
Aruba software.

Aruba 8325 Switch Series LEDs | 19

| Chassis LEDs | Function | State | Meaning |
| ------------ | -------- | ----- | ------- |
Managementport Todisplaylinkinformationfor Ongreen Showsavalidlink.
| LinkLED | theport. |     |                              |
| ------- | -------- | --- | ---------------------------- |
|         |          | Off | Portisdisabled,notconnected, |
ornotreceivingalinkbeat
signal.
Managementport Todisplayactivityinformation Flashingyellow Flashingindicatesportactivity.
| ActLED | fortheport. |     |     |
| ------ | ----------- | --- | --- |
*Thefastflashingbehaviorisanon/offcycleonceevery0.8seconds,approximately.
**Theslowflashingbehaviorisanon/offcycleonceevery1.6seconds,approximately.
^Thefastflashingbehaviorisanon/offcycleonceevery0.8seconds,approximately.
^^Theslowflashingbehaviorisanon/offcycleonceevery1.6seconds,approximately.
Table3:PortLEDsfortheAruba8325-32C(JL626AandJL627A)
LED
1 QSFP28portLEDandlane1indicator
2 QSFP28lane2LED(Notsupportedwithcurrentlyreleasedsoftware.)
3 QSFP28lane3LED(Notsupportedwithcurrentlyreleasedsoftware.)
4 QSFP28lane4LED(Notsupportedwithcurrentlyreleasedsoftware.)
5 Unused
6 Out-of-bandmanagementportLinkandActivityLED
Table4:PortLEDbehaviorfortheAruba8325-32C(JL626AandJL627A)
20
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

Chassis LEDs

Function

State

Meaning

QSFP28 port LEDs

To display link and activity
information for the port.

On/flashing green

Flashing amber

Off

Shows a valid link at 100/40
Gbps.

n Fast flashing* indicates port

activity at 100 Gbps.
n Slow flashing** indicates

port activity at 40 Gbps.

When the Global Status LED is
simultaneously flashing amber
with the Lane 1 LED, indicates
an unsupported or faulty
transceiver, or a port failure.

Port is disabled, not connected,
or not receiving a link beat
signal.
Lanes 2-4 are always off and
are currently unused by HPE-
Aruba software.

Management port
Link LED

To display link information for
the port.

On green

Shows a valid link.

Off

Port is disabled, not connected,
or not receiving a link beat
signal.

Management port
Act LED

To display activity information
for the port.

Flashing yellow

Flashing indicates port activity.

*The fast flashing behavior is an on/off cycle once every 0.8 seconds, approximately.

**The slow flashing behavior is an on/off cycle once every 1.6 seconds, approximately.

Alarm commands

alarm
alarm {temperature | power supply} [action <LOG-AND-TRAP> | <RELAY>]
no alarm {temperature | power supply} [action <LOG-AND-TRAP> | <RELAY>]

Description

Configures global events to be forwarded to the output alarm port. The no form of this command
disables the specified configuration.

Parameter

{temperature}

{power supply}

<LOG-AND-TRAP>

Description

Selects the alarm for ambient temperatures reaching threshold
limits. The threshold is 70°C.

Selects the alarm events from the power supply.

Generates an event log and SNMP trap.

<RELAY>

Relays an event to alarm output port.

Aruba 8325 Switch Series LEDs | 21

Examples
Disablingatemperatureeventtoremovetheconfigurationforallactionsassociatedwiththeevent:
switch(config)#
|     | no  | alarm temperature |     |
| --- | --- | ----------------- | --- |
Configuringanalarmforatemperatureeventforthelog-and-trapaction:
| switch(config)# | alarm | temperature | action log-and-trap |
| --------------- | ----- | ----------- | ------------------- |
Removingtheconfigurationforthetemperatureeventforalog-and-trapaction:
| switch(config)# | no  | alarm temperature | action log-and-trap |
| --------------- | --- | ----------------- | ------------------- |
Configuringanalarmforapower-supplyeventfortherelayaction:
| switch(config)# | alarm | power-supply | action relay |
| --------------- | ----- | ------------ | ------------ |
Removingtheconfigurationforthepower-supplyeventfortherelayaction:
| switch(config)#     | no      | alarm power-supply | action relay        |
| ------------------- | ------- | ------------------ | ------------------- |
| Command History     |         |                    |                     |
| Release             |         |                    | Modification        |
| 10.08               |         |                    | Featuredintroduced. |
| Command Information |         |                    |                     |
| Platforms           | Command | context            | Authority           |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
alarm input
alarm input {IN1 | IN2} [name <STRING>] [action <LOG-AND-TRAP> | <RELAY>] [trigger
| <CLOSED | OPEN>] |     |     |     |
| ---------------- | --- | --- | --- |
no alarm input {IN1| IN2} [name <STRING>] [action <LOG-AND-TRAP> | <RELAY>] [trigger
| <CLOSED | OPEN>] |     |     |     |
| ---------------- | --- | --- | --- |
Description
Configuresinputalarmandactions.Thenoformofthiscommandremovesthespecifiedconfiguration.
| Parameter   |     |     | Description                  |
| ----------- | --- | --- | ---------------------------- |
| {IN1 | IN2} |     |     | Specifiestheinputalarmport.. |
22
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Parameter |     | Description                          |     |
| --------- | --- | ------------------------------------ | --- |
| name      |     | Specifiestheexternaldeviceconnected. |     |
| <STRING>  |     | Descriptivestring.                   |     |
action
Specifiestheactiontobetakenwhenthemonitoredeventoccurs.
| <LOG-AND-TRAP> |     | GeneratesaneventlogandSNMPtrap.                     |     |
| -------------- | --- | --------------------------------------------------- | --- |
| <RELAY>        |     | Relaysaneventtoalarmoutputport.                     |     |
| trigger        |     | Triggersanalarmbasedonanormallyopenorclosedcircuit. |     |
| <CLOSED>       |     | Generatesanalarmeventwhenthecircuitisclosed.        |     |
| <OPEN>         |     | Generatesanalarmeventwhenthecircuitisopen.          |     |
Examples
Configuringanalarmoninputport1namedDoor-Sensor:
| switch(config)# | alarm input | IN1 name | Door-Sensor |
| --------------- | ----------- | -------- | ----------- |
Removingtheconfiguringforanalarmoninputport1:
| switch(config)# | no alarm | input IN1 |     |
| --------------- | -------- | --------- | --- |
Configuringanalarmoninputport1withlog-and-trapaction:
| switch(config)# | alarm input | IN1 action | log-and-trap |
| --------------- | ----------- | ---------- | ------------ |
Removingtheconfigurationforanalarmoninputport1withlog-and-trapaction:
| switch(config)# | no alarm | input IN1 action | log-and-trap |
| --------------- | -------- | ---------------- | ------------ |
Configuringanalarmoninputport1totriggeranalarmwhenthedoorsensorcircuitisclosed:
| switch(config)# | alarm input | IN1 trigger | closed |
| --------------- | ----------- | ----------- | ------ |
Command History
| Release |     | Modification        |     |
| ------- | --- | ------------------- | --- |
| 10.08   |     | Featuredintroduced. |     |
Command Information
Aruba8325SwitchSeriesLEDs|23

| Platforms | Command |     | context |     | Authority |
| --------- | ------- | --- | ------- | --- | --------- |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| alarm        | snooze |     |          |          |     |
| ------------ | ------ | --- | -------- | -------- | --- |
| alarm snooze | [time  | in  | minutes] | [repeat] |     |
Description
Configuresanyactiveeventforwardedtoalarmrelaytobesnoozed.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
time in minutes Specifiesthevaluefortimeinminutes.Therangeis0-1440
minutes..
repeat
Repeatstheprevioussnoozetime.
Examples
Configuringanalarmrelayactionfor10minutes:
| switch(config)# |     | alarm | snooze | 10  |     |
| --------------- | --- | ----- | ------ | --- | --- |
Configuringanalarmrelayactiontoberepeatedwithpreviouslyconfiguredsnoozetime:
| switch(config)# |             | alarm | snooze  | repeat |                     |
| --------------- | ----------- | ----- | ------- | ------ | ------------------- |
| Command         | History     |       |         |        |                     |
| Release         |             |       |         |        | Modification        |
| 10.08           |             |       |         |        | Featuredintroduced. |
| Command         | Information |       |         |        |                     |
| Platforms       | Command     |       | context |        | Authority           |
config
4100i Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show       | alarm        |     |         |         |     |
| ---------- | ------------ | --- | ------- | ------- | --- |
| show alarm | [temperature |     | | power | supply] |     |
Description
Showsallofthedetailsofglobalstatusmonitoringalarmevents.
24
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
temperature Selectsthealarmforambienttemperaturesreachingthreshold
limits.
| power supply |     |     | Selectsthealarmeventsfromthepowersupply. |     |
| ------------ | --- | --- | ---------------------------------------- | --- |
Examples
Showingdetailsforallglobalalarmeventsontheswitch:
| switch#      | show alarm   |                |     |     |
| ------------ | ------------ | -------------- | --- | --- |
| Alarm Snooze | Timer        | Status: active |     |     |
| Duration     | remaining: 1 | min 32 sec     |     |     |
-----------------------------------------------------------------------
| Global Alarm: Temperature |     |     |     |     |
| ------------------------- | --- | --- | --- | --- |
-----------------------------------------------------------------------
| Alarm Event |     | Status | log-and-trap | Relay |
| ----------- | --- | ------ | ------------ | ----- |
-----------------------------------------------------------------------
| Temperature |     | inactive | true | false |
| ----------- | --- | -------- | ---- | ----- |
-----------------------------------------------------------------------
| Global Alarm: | power-supply |     |     |     |
| ------------- | ------------ | --- | --- | --- |
-----------------------------------------------------------------------
| Alarm Event |     | Status | log-and-trap | Relay |
| ----------- | --- | ------ | ------------ | ----- |
-----------------------------------------------------------------------
| power-supply |     | active | false | true |
| ------------ | --- | ------ | ----- | ---- |
Showingdetailsforthetemperaturealarm:
| switch#      | show alarm   | temperature    |     |     |
| ------------ | ------------ | -------------- | --- | --- |
| Alarm Snooze | Timer        | Status: Active |     |     |
| Duration     | remaining: 5 | min 36 sec     |     |     |
-----------------------------------------------------------------------
| Global Alarm: Temperature |     |     |     |     |
| ------------------------- | --- | --- | --- | --- |
-----------------------------------------------------------------------
| Alarm Event |     | Status | log-and-trap | Relay |
| ----------- | --- | ------ | ------------ | ----- |
-----------------------------------------------------------------------
| Temperature         |         | inactive | true                | false |
| ------------------- | ------- | -------- | ------------------- | ----- |
| Command History     |         |          |                     |       |
| Release             |         |          | Modification        |       |
| 10.08               |         |          | Featuredintroduced. |       |
| Command Information |         |          |                     |       |
| Platforms           | Command | context  | Authority           |       |
4100i Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| show alarm | input |     |     |     |
| ---------- | ----- | --- | --- | --- |
Aruba8325SwitchSeriesLEDs|25

| show alarm | input | [IN1 | | IN2] |     |     |     |     |
| ---------- | ----- | ---- | ------ | --- | --- | --- | --- |
Description
Showsthealarmdetailsforallportsorforthespecifiedport.
| Parameter |      |     |     |     | Description                  |     |     |
| --------- | ---- | --- | --- | --- | ---------------------------- | --- | --- |
| {IN1 |    | IN2} |     |     |     | Specifiestheinputalarmport.. |     |     |
Examples
Showingdetailsforallalarminputportsontheswitch:
| switch# | show   | alarm | input   |          |     |     |     |
| ------- | ------ | ----- | ------- | -------- | --- | --- | --- |
| Alarm   | Snooze | Timer | Status: | inactive |     |     |     |
-----------------------------------------------------------------------
| Input | Alarm | IN1, | Name: Door-Sensor |     |     |     |     |
| ----- | ----- | ---- | ----------------- | --- | --- | --- | --- |
-----------------------------------------------------------------------
| Alarm | Port |     | Status |     | log-and-trap | Relay | Trigger |
| ----- | ---- | --- | ------ | --- | ------------ | ----- | ------- |
-----------------------------------------------------------------------
| IN1 |     |     | inactive |     | true | false | closed |
| --- | --- | --- | -------- | --- | ---- | ----- | ------ |
-----------------------------------------------------------------------
| Input | Alarm | IN2, | Name: | N/A |     |     |     |
| ----- | ----- | ---- | ----- | --- | --- | --- | --- |
-----------------------------------------------------------------------
| Alarm | Port |     | Status |     | log-and-trap | Relay | Trigger |
| ----- | ---- | --- | ------ | --- | ------------ | ----- | ------- |
-----------------------------------------------------------------------
| IN2 |     |     | active |     | false | true | open |
| --- | --- | --- | ------ | --- | ----- | ---- | ---- |
ShowingdetailsforalarminputportsIN1:
| switch# | show   | alarm | input   | IN1      |     |     |     |
| ------- | ------ | ----- | ------- | -------- | --- | --- | --- |
| Alarm   | Snooze | Timer | Status: | inactive |     |     |     |
-----------------------------------------------------------------------
| Input | Alarm | IN1, | Name: Door-Sensor |     |     |     |     |
| ----- | ----- | ---- | ----------------- | --- | --- | --- | --- |
-----------------------------------------------------------------------
| Alarm | Port |     | Status |     | log-and-trap | Relay | Trigger |
| ----- | ---- | --- | ------ | --- | ------------ | ----- | ------- |
-----------------------------------------------------------------------
| IN1       |             |         | inactive |         | true                | false | closed |
| --------- | ----------- | ------- | -------- | ------- | ------------------- | ----- | ------ |
| Command   | History     |         |          |         |                     |       |        |
| Release   |             |         |          |         | Modification        |       |        |
| 10.08     |             |         |          |         | Featuredintroduced. |       |        |
| Command   | Information |         |          |         |                     |       |        |
| Platforms |             | Command |          | context | Authority           |       |        |
4100i Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | alarm | timer |     |     |     |     |     |
| ---- | ----- | ----- | --- | --- | --- | --- | --- |
26
| AOS-CX10.09MonitoringGuide| |     |     | (83xxSwitchSeries) |     |     |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- | --- | --- |

| show alarm timer |     |     |     |
| ---------------- | --- | --- | --- |
Description
Showsthestatusofanalarmsnoozetimer'sstatusandduration.
Examples
Showingthestatusofanalarmsnoozetimerwhenitisinactive:
| switch#      | show alarm | timer            |     |
| ------------ | ---------- | ---------------- | --- |
| Alarm Snooze | Timer      | Status: inactive |     |
Showingthestatusofanactive3-minutealarmsnoozetimer:
| switch#             | show alarm   | timer          |                     |
| ------------------- | ------------ | -------------- | ------------------- |
| Alarm Snooze        | Timer        | Status: active |                     |
| Duration            | remaining: 2 | min 55 sec     |                     |
| Command History     |              |                |                     |
| Release             |              |                | Modification        |
| 10.08               |              |                | Featuredintroduced. |
| Command Information |              |                |                     |
| Platforms           | Command      | context        | Authority           |
4100i Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Aruba8325SwitchSeriesLEDs|27

Chapter 5
Boot commands
Boot commands
boot fabric-module
| boot fabric-module | <SLOT-ID> |     |     |
| ------------------ | --------- | --- | --- |
Description
Rebootsthespecifiedfabricmodule.
| Parameter |     |     | Description                                     |
| --------- | --- | --- | ----------------------------------------------- |
| <SLOT-ID> |     |     | Specifiesthememberandslotofthemoduleintheformat |
member/slot.Forexample,tospecifythemoduleinmember1
slot3,enter1/3.
Usage
Theboot fabric-modulecommandrebootsthespecifiedfabricmodule.Trafficperformanceisaffected
whilethemoduleisdown.
Ifthespecifiedmoduleistheonlyfabricmoduleinanupstate,rebootingthatmodulestopstraffic
switchingbetweenlinemodulesandthelinemodulespowerdown.Thelinemodulespowerupwhen
onefabricmodulereturnstoanupstate.
Thiscommandisvalidforfabricmodulesonly.
Examples
Rebootingthefabricmoduleinslot1/3whenauto-confirmisnotenabled:
| switch# boot | fabric-module | 1/3 |     |
| ------------ | ------------- | --- | --- |
This command will reboot the specified fabric module. Traffic performance may
be affected while the module is down. Rebooting the last fabric module will
| stop traffic | switching   | between line | modules. |
| ------------ | ----------- | ------------ | -------- |
| Do you want  | to continue | (y/n)? y     |          |
switch#
Rebootingthefabricmoduleinslot1/1whenauto-confirmisenabled:
| switch# boot | fabric-module | 1/3 |     |
| ------------ | ------------- | --- | --- |
This command will reboot the specified fabric module. Traffic performance may
be affected while the module is down. Rebooting the last fabric module will
| stop traffic | switching   | between line           | modules. |
| ------------ | ----------- | ---------------------- | -------- |
| Do you want  | to continue | (y/n) y (auto-confirm) |          |
switch#
| Command History |     |     |     |
| --------------- | --- | --- | --- |
28
AOS-CX10.09MonitoringGuide| (83xxSwitchSeries)

| Release             |         |     |         | Modification |
| ------------------- | ------- | --- | ------- | ------------ |
| 10.07orearlier      |         |     |         | --           |
| Command Information |         |     |         |              |
| Platforms           | Command |     | context | Authority    |
Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
boot line-module
| boot line-module |     | <SLOT-ID> |     |     |
| ---------------- | --- | --------- | --- | --- |
Description
Rebootsthespecifiedlinemodule.
| Parameter |     |     |     | Description                                     |
| --------- | --- | --- | --- | ----------------------------------------------- |
| <SLOT-ID> |     |     |     | Specifiesthememberandslotofthemoduleintheformat |
member/slot.Forexample,tospecifythemoduleinmember1
slot3,enter1/3.
Usage
Rebootsthespecifiedlinemodule.Anytrafficfortheswitchpassingthroughtheaffectedmodule(SSH,
TELNET,andSNMP)isinterrupted.Itcantakeupto2minutestorebootthemodule.Duringthattime,
youcanmonitorprogressbyviewingtheeventlog.
Thiscommandisvalidforlinemodulesonly.
Examples
Reloadingthemoduleinslot1/1:
| switch# | boot line-module |     | 1/1 |     |
| ------- | ---------------- | --- | --- | --- |
This command will reboot the specified line module and interfaces on this
module will not send or receive packets while the module is down. Any
traffic passing through the line module will be interrupted. Management
sessions connected through the line module will be affected. It might take
up to 2 minutes to complete rebooting the module. During that time, you can
| monitor     | progress | by viewing | the    | event log. |
| ----------- | -------- | ---------- | ------ | ---------- |
| Do you want | to       | continue   | (y/n)? | y          |
switch#
| Command History     |     |     |     |              |
| ------------------- | --- | --- | --- | ------------ |
| Release             |     |     |     | Modification |
| 10.07orearlier      |     |     |     | --           |
| Command Information |     |     |     |              |
Bootcommands|29

Platforms

Command context

Authority

Manager (#)

Administrators or local user group members with execution rights
for this command.

boot management-module
boot management-module {active | standby | <SLOT-ID>}

Description

Reboots the specified management module. Choose the management module to reboot by role (active
or standby) or by slot number.

Parameter

active

standby

<SLOT-ID>

Usage

Description

Selects the active management module.

Selects the standby management module.

Specifies the member and slot of the management module in the
format member/slot. For example, to specify the module in
member 1 slot 5, enter 1/5.

This command reboots a single management module in a chassis. Choose the management module to
reboot by role (active or standby) or by slot number.

You can use the show images command to show information about the primary and secondary system
images.

If you reboot the active management module and the standby management module is available, the
active management module reboots and the standby management module becomes the active
management module.

If you reboot the active management module and the standby management module is not available,
you are warned, you are prompted to save the configuration, and you are prompted to confirm the
operation.

If you reboot the standby management module, the standby management module reboots and remains
the standby management module.

If you attempt to reboot a management module that is not available, the boot command is aborted.

Saving the configuration is not required. However, if you attempt to save the configuration and there is
an error during the save operation, the boot command is aborted.

Hewlett Packarrd Enterprise recommends that you use the boot management-module command instead of
pressing the module reset button to reboot a management module because if you are rebooting the only
available management module, the boot management-module command enables you to save the
configuration, cancel the reboot, or both.

Examples

Rebooting the active management module when the standby management module is available:

AOS-CX 10.09 Monitoring Guide | (83xx Switch Series)

30

| switch# | boot | management-module |     | active |     |     |     |
| ------- | ---- | ----------------- | --- | ------ | --- | --- | --- |
The management-module in slot 1/5 is going down for reboot now.
Rebootingtheactivemanagementmodulewhenthestandbymanagementmoduleisnotavailable:
| switch#        | boot        | management-module |              | 1/5     |               |                |     |
| -------------- | ----------- | ----------------- | ------------ | ------- | ------------- | -------------- | --- |
| The management |             | module            | in slot      | 1/5     | is currently  | active and     | no  |
| standby        | management  |                   | module was   | found.  |               |                |     |
| This will      | reboot      | the               | entire       | switch. |               |                |     |
| Do you         | want        | to save           | the current  |         | configuration | (y/n)? n       |     |
| This will      | reboot      | the               | entire       | switch  | and render    | it unavailable |     |
| until the      | process     |                   | is complete. |         |               |                |     |
| Continue       | (y/n)?      | y                 |              |         |               |                |     |
| The system     | is          | going             | down for     | reboot. |               |                |     |
| Command        | History     |                   |              |         |               |                |     |
| Release        |             |                   |              |         | Modification  |                |     |
| 10.07orearlier |             |                   |              |         | --            |                |     |
| Command        | Information |                   |              |         |               |                |     |
| Platforms      |             | Command           | context      |         | Authority     |                |     |
Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| boot set-default |     |          |              |     |     |     |     |
| ---------------- | --- | -------- | ------------ | --- | --- | --- | --- |
| boot set-default |     | {primary | | secondary} |     |     |     |     |
Description
Setsthedefaultoperatingsystemimagetousewhenthesystemisbooted.
| Parameter |     |     |     |     | Description                                     |     |     |
| --------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- |
| primary   |     |     |     |     | Selectstheprimarynetworkoperatingsystemimage.   |     |     |
| secondary |     |     |     |     | Selectsthesecondarynetworkoperatingsystemimage. |     |     |
Example
Selectingtheprimaryimageasthedefaultbootimage:
| switch# | boot    | set-default | primary         |     |     |     |     |
| ------- | ------- | ----------- | --------------- | --- | --- | --- | --- |
| Default | boot    | image       | set to primary. |     |     |     |     |
| Command | History |             |                 |     |     |     |     |
Bootcommands|31

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| boot system |          |             |              |
| ----------- | -------- | ----------- | ------------ |
| boot system | [primary | | secondary | | serviceos] |
Description
Rebootsallmodulesontheswitch.Bydefault,theconfigureddefaultoperatingsystemimageisused.
Optionalparametersenableyoutospecifywhichsystemimagetousefortherebootoperationandfor
futurerebootoperations.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
primary Selectstheprimaryoperatingsystemimageforthisrebootand
setstheconfigureddefaultoperatingsystemimagetoprimary
forfuturereboots.
secondary Selectsthesecondaryoperatingsystemimageforthisrebootand
setstheconfigureddefaultoperatingsystemimagetosecondary
forfuturereboots.
serviceos Selectstheserviceoperatingsystemforthisreboot.Doesnot
changetheconfigureddefaultoperatingsystemimage.The
serviceoperatingsystemactsasastandalonebootloaderand
recoveryOSforswitchesrunningtheAOS-CXoperatingsystem
andisusedinrarecaseswhentroubleshootingaswitch.
Usage
Thiscommandrebootstheentiresystem.Ifyoudonotselectoneoftheoptionalparameters,the
systemrebootsfromtheconfigureddefaultbootimage.
Youcanusetheshow imagescommandtoshowinformationabouttheprimaryandsecondarysystem
images.
Choosingoneoftheoptionalparametersaffectsthesettingforthedefaultbootimage:
n Ifyouselecttheprimaryorsecondaryoptionalparameter,thatimagebecomestheconfigured
defaultbootimageforfuturesystemreboots.Thecommandfailsiftheswitchisnotabletosetthe
operatingsystemimagetotheimageyouselected.
Youcanusetheboot set-defaultcommandtochangetheconfigureddefaultoperatingsystemimage.
n Ifyouselectserviceosastheoptionalparameter,theconfigureddefaultbootimageremainsthe
same,andthesystemrebootsallmanagementmoduleswiththeserviceoperatingsystem.
32
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

Iftheconfigurationoftheswitchhaschangedsincethelastreboot,whenyouexecutetheboot system
commandyouarepromptedtosavetheconfigurationandyouarepromptedtoconfirmthereboot
operation.
Savingtheconfigurationisnotrequired.However,ifyouattempttosavetheconfigurationandthereis
anerrorduringthesaveoperation,theboot systemcommandisaborted.
Examples
Rebootingthesystemfromtheconfigureddefaultoperatingsystemimage:
| switch# | boot system  |             |               |          |
| ------- | ------------ | ----------- | ------------- | -------- |
| Do you  | want to save | the current | configuration | (y/n)? y |
The running configuration was saved to the startup configuration.
| This will  | reboot the | entire switch    | and render | it unavailable |
| ---------- | ---------- | ---------------- | ---------- | -------------- |
| until the  | process    | is complete.     |            |                |
| Continue   | (y/n)? y   |                  |            |                |
| The system | is going   | down for reboot. |            |                |
Rebootingthesystemfromthesecondaryoperatingsystemimage,settingthesecondaryoperating
systemimageastheconfigureddefaultbootimage:
| switch#    | boot system  | secondary         |               |                |
| ---------- | ------------ | ----------------- | ------------- | -------------- |
| Default    | boot image   | set to secondary. |               |                |
| Do you     | want to save | the current       | configuration | (y/n)? n       |
| This will  | reboot the   | entire switch     | and render    | it unavailable |
| until the  | process      | is complete.      |               |                |
| Continue   | (y/n)? y     |                   |               |                |
| The system | is going     | down for reboot.  |               |                |
Cancelingasystemreboot:
| switch#   | boot system  |               |               |                |
| --------- | ------------ | ------------- | ------------- | -------------- |
| Do you    | want to save | the current   | configuration | (y/n)? n       |
| This will | reboot the   | entire switch | and render    | it unavailable |
| until the | process      | is complete.  |               |                |
| Continue  | (y/n)? n     |               |               |                |
Reboot aborted.
switch#
| Command        | History     |     |              |     |
| -------------- | ----------- | --- | ------------ | --- |
| Release        |             |     | Modification |     |
| 10.07orearlier |             |     | --           |     |
| Command        | Information |     |              |     |
Bootcommands|33

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| show boot-history |       |     |     |
| ----------------- | ----- | --- | --- |
| show boot-history | [all] |     |     |
Description
Showsbootinformation.Whennoparametersarespecified,showsthemostrecentinformationabout
thebootoperation,andthethreepreviousbootoperationsfortheactivemanagementmodule.When
theallparameterisspecified,showsthebootinformationfortheactivemanagementmoduleandall
availablelinemodules.Toviewboot-historyonthestandby,thecommandmustbesentonthestandby
console.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
all
Showsbootinformationfortheactivemanagementmoduleand
allavailablelinemodules.
Usage
Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereis
apreviousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
system)andrebootreasons.Previousbootinformationisdisplayedinreversechronologicalorder.
Index
Thepositionofthebootinthehistoryfile.Range:0to3.
Boot ID
AuniqueIDfortheboot.Asystem-generated128-bitstring.
| Current Boot, | up for <SECONDS> | seconds |     |
| ------------- | ---------------- | ------- | --- |
Forthecurrentboot,theshow boot-historycommandshowsthenumberofsecondsthemodulehasbeen
runningonthecurrentsoftware.
| Timestamp boot | reason |     |     |
| -------------- | ------ | --- | --- |
Forpreviousbootoperations,theshow boot-historycommandshowsthetimeatwhichtheoperationoccurred
andthereasonfortheboot.Thereasonforthebootisoneofthefollowingvalues:
| <DAEMON-NAME> | crash |     |     |
| ------------- | ----- | --- | --- |
Thedaemonidentifiedby<DAEMON-NAME>causedthemoduletoboot.
Kernel crash
Theoperatingsystemsoftwareassociatedwiththemodulecausedthemoduletoboot.
| Reboot requested | through | database |     |
| ---------------- | ------- | -------- | --- |
TherebootoccurredbecauseofarequestmadethroughtheCLIorotherAPI.
| Uncontrolled | reboot |     |     |
| ------------ | ------ | --- | --- |
Thereasonfortherebootisnotknown.
Examples
Showingtheboothistoryoftheactivemanagementmodule:
| switch#    | show boot-history |     |     |
| ---------- | ----------------- | --- | --- |
| Management | module            |     |     |
=================
| Index : | 3   |     |     |
| ------- | --- | --- | --- |
34
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |          |           |      |                  |
| ------- | ---------------------------------- | -------- | --------- | ---- | ---------------- |
| Current | Boot, up for                       | 22       | hrs 12    | mins | 22 secs          |
| Index : | 2                                  |          |           |      |                  |
| Boot ID | : edfa2d6598d24e989668306c4a56a06d |          |           |      |                  |
| 07 Aug  | 18 16:28:01                        | : Reboot | requested |      | through database |
| Index : | 1                                  |          |           |      |                  |
| Boot ID | : 0bda8d0361df4a7e8e3acdc1dba5caad |          |           |      |                  |
| 07 Aug  | 18 14:08:46                        | : Reboot | requested |      | through database |
| Index : | 0                                  |          |           |      |                  |
| Boot ID | : 23da2b0e26d048d7b3f4b6721b69c110 |          |           |      |                  |
| 07 Aug  | 18 13:00:46                        | : Reboot | requested |      | through database |
switch#
Showingtheboothistoryoftheactivemanagementmoduleandalllinemodules:
| switch#    | show boot-history |     | all |     |     |
| ---------- | ----------------- | --- | --- | --- | --- |
| Management | module            |     |     |     |     |
=================
| Index :     | 3                                  |          |           |      |                  |
| ----------- | ---------------------------------- | -------- | --------- | ---- | ---------------- |
| Boot ID     | : f1bf071bdd04492bbf8439c6e479d612 |          |           |      |                  |
| Current     | Boot, up for                       | 22       | hrs 12    | mins | 22 secs          |
| Index :     | 2                                  |          |           |      |                  |
| Boot ID     | : edfa2d6598d24e989668306c4a56a06d |          |           |      |                  |
| 07 Aug      | 18 16:28:01                        | : Reboot | requested |      | through database |
| Index :     | 1                                  |          |           |      |                  |
| Boot ID     | : 0bda8d0361df4a7e8e3acdc1dba5caad |          |           |      |                  |
| 07 Aug      | 18 14:08:46                        | : Reboot | requested |      | through database |
| Index :     | 0                                  |          |           |      |                  |
| Boot ID     | : 23da2b0e26d048d7b3f4b6721b69c110 |          |           |      |                  |
| 07 Aug      | 18 13:00:46                        | : Reboot | requested |      | through database |
| Line module | 1/1                                |          |           |      |                  |
=================
| Index : | 3           |              |     |         |     |
| ------- | ----------- | ------------ | --- | ------- | --- |
| 10 Aug  | 17 12:45:46 | : dune_agent |     | crashed |     |
...
| Command        | History     |         |     |              |     |
| -------------- | ----------- | ------- | --- | ------------ | --- |
| Release        |             |         |     | Modification |     |
| 10.07orearlier |             |         |     | --           |     |
| Command        | Information |         |     |              |     |
| Platforms      | Command     | context |     | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Bootcommands|35

Chapter 6
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
Switchsystemandhardwarecommandsaregeneralcommandsusedtoconfigurefundamentalsettings
ontheswitch.
RefertotheFundamentalsGuidetoviewtheswitchsystemandhardwarecommands.
36
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

Chapter 7
External storage
| External | storage |     |     |     |
| -------- | ------- | --- | --- | --- |
Theswitchhaslimitedcapacitytostoredata,collectedbyswitchfeaturesandprotocols.Youcan
providevirtuallyunlimitedstoragecapacitybyaddinguser-suppliedexternalstoragevolumes.
Supportedvolumetypesandstorageprotocolsinclude:NFSv3,NFSv4,andSCP(sshfs).
OneapplicationofexternalstorageisthesavingandrestoringofDHCPleasefilesoverSCPorNFS
networkattachedstoragesystems.SCPfilesystemprotocolusesausermodeprocesstoemulatea
networkfilesystem.Thekeyadvantageispacketlevelencryptionandsimpleconfiguration.Thekey
disadvantageisslowperformance.
Youcansetupexternalstoragevolumecredentialsandthenenableit.Astoragemanagementprocess
actsonyourrequestsbyenablingthestoragevolumeusingtherequestedstorageprotocol.Youcan
disabletheexternalstoragevolumeorsetitupbutleaveitdisable.
Thefeaturemaintainsstoragevolumestate.Thestatesare:*disabled*(down),*connecting*
(establishingconnection),*operational*(up),and*unaccessible*(unavailable).
Ifastoragevolumeisunavailable,thesystemattemptstoreconnectperiodically.Multiplevolumescould
connectconcurrently.Ifoneconnectiontimesouttheotherscanconnectimmediately.
Thesystemsupportsserverconnectionthroughdataandmanagementports.
DataportsupportrequiresserverIPaddressonadefaultVRF.
Onceastoragevolumeisenabled,applicationscanusethevolumetostoreretrieveanddeletefilesand
directories.
| External   | storage      | commands      |            |             |
| ---------- | ------------ | ------------- | ---------- | ----------- |
| address    | (external    | storage)      |            |             |
| address    | {<IPV4-ADDR> | | <IPV6-ADDR> | | hostname | <HOSTNAME>} |
| no address | {<IPV4-ADDR> | | <IPV6-ADDR> | | hostname | <HOSTNAME>} |
Description
SpecifiestheNASIPaddressorhostname.
ThenoformofthiscommanddeletesanIPaddressorhostname.
| Parameter   |     |     | Description                              |     |
| ----------- | --- | --- | ---------------------------------------- | --- |
| <IPV4-ADDR> |     |     | SpecifiestheNASserverIPv4address,Global. |     |
<IPV6-ADDR>
SpecifiestheIPv6addressoftheNASserver.
| <HOSTNAME> |     |     | SpecifiesthehostnameoftheNASserver.String. |     |
| ---------- | --- | --- | ------------------------------------------ | --- |
Examples
CreatingthelogfilesstoragevolumewithIPaddress10.1.1.1:
37
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |
| --------------------------- | --- | ------------------ | --- | --- |

| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)#
address 10.1.1.1
Deletinganexternalstoragevolumenamedlogfiles:
| switch(config)#                           | external-storage |         | logfiles     |           |
| ----------------------------------------- | ---------------- | ------- | ------------ | --------- |
| switch(config-external-storage-logfiles)# |                  |         | no address   | 10.1.1.1  |
| Command History                           |                  |         |              |           |
| Release                                   |                  |         | Modification |           |
| 10.07orearlier                            |                  |         | --           |           |
| Command Information                       |                  |         |              |           |
| Platforms                                 | Command          | context |              | Authority |
config-external-storage-<VOLUME-NAME>
| 8320 |     |     |     | Administratorsorlocalusergroup    |
| ---- | --- | --- | --- | --------------------------------- |
| 8325 |     |     |     | memberswithexecutionrightsforthis |
| 8360 |     |     |     | command.                          |
directory
| directory <DIRECTORY-NAME> |                  |     |     |     |
| -------------------------- | ---------------- | --- | --- | --- |
| no directory               | <DIRECTORY-NAME> |     |     |     |
Description
Selectsanexistingdirectoryontheexternalstoragevolume.
Thenoformofthiscommandclearsadirectoryofanexternalstoragevolume.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<DIRECTORY-NAME> Specifiestheexternalstoragedirectoryformappingthevolume.
Examples
Creatingavolumenamedlogfilesthatismappedunder/homeontheserver:
| switch(config)#                           | external-storage |     | logfiles  |       |
| ----------------------------------------- | ---------------- | --- | --------- | ----- |
| switch(config-external-storage-logfiles)# |                  |     | directory | /home |
Clearingthedirectory/home:
| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)#
no directory /home
| Command History |     |     |     |     |
| --------------- | --- | --- | --- | --- |
Externalstorage|38

| Release        |             |         | Modification |           |
| -------------- | ----------- | ------- | ------------ | --------- |
| 10.07orearlier |             |         | --           |           |
| Command        | Information |         |              |           |
| Platforms      | Command     | context |              | Authority |
8320 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
| 8325 |     |     |     | usergroupmemberswithexecution |
| ---- | --- | --- | --- | ----------------------------- |
rightsforthiscommand.Operatorscan
8360
executethiscommandfromthe
operatorcontext(>)only.
| disable | external-storage |     | logfiles |     |
| ------- | ---------------- | --- | -------- | --- |
disable
no disable
Description
Disablestheexternalstoragevolume.
Thenoformofthiscommandenablestheexternalstoragevolume.Thisisidenticaltotheenable
command.
Examples
Disablingavolumenamedlogfiles:
| switch(config)# |     | external-storage | logfiles |     |
| --------------- | --- | ---------------- | -------- | --- |
switch(config-external-storage-logfiles)# disable
| Command        | History     |         |              |           |
| -------------- | ----------- | ------- | ------------ | --------- |
| Release        |             |         | Modification |           |
| 10.07orearlier |             |         | --           |           |
| Command        | Information |         |              |           |
| Platforms      | Command     | context |              | Authority |
8320 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
| 8325 |     |     |     | usergroupmemberswithexecution |
| ---- | --- | --- | --- | ----------------------------- |
rightsforthiscommand.Operatorscan
8360
executethiscommandfromthe
operatorcontext(>)only.
| enable | (external-storage |     | logfiles) |     |
| ------ | ----------------- | --- | --------- | --- |
enable
no enable
Description
39
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |
| --------------------------- | --- | ------------------ | --- | --- |

Enablestheexternalstoragevolume.
Thenoformofthiscommanddisablestheexternalstoragevolume.Thisisidenticaltothedisable
command.
Examples
Creatingandthenenablingavolumenamedlogfiles:
| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)# enable
Disablestheexternalstoragevolume:
| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)# disable
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8320 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
| 8325 |     |     |     | usergroupmemberswithexecution     |
| ---- | --- | --- | --- | --------------------------------- |
| 8360 |     |     |     | rightsforthiscommand.Operatorscan |
executethiscommandfromthe
operatorcontext(>)only.
external-storage
| external-storage    | <VOLUME-NAME> |     |     |     |
| ------------------- | ------------- | --- | --- | --- |
| no external-storage | <VOLUME-NAME> |     |     |     |
Description
Createsorupdatesanexternalstoragevolume.
Thenoformofthiscommanddeletesanexternalstoragevolume.
Examples
Creatingthelogfilesstoragevolume:
| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)#
Deletingthelogfilesstoragevolume:
switch(config)#
|     | no  | external-storage | logfiles |     |
| --- | --- | ---------------- | -------- | --- |
Externalstorage|40

| Command        | History     |     |         |              |
| -------------- | ----------- | --- | ------- | ------------ |
| Release        |             |     |         | Modification |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --------------- |
8360
| password    | (external-storage) |     |               |             |
| ----------- | ------------------ | --- | ------------- | ----------- |
| password    | [{plaintext        |     | | ciphertext} | <PASSWORD>] |
| no password | {plaintext         |     | | ciphertext} | <PASSWORD>  |
Description
Setsthepasswordfornetworkattachedstorageserverlogin.
Thenoformofthiscommandclearsthepasswordfornetworkattachedstorageserverlogin.
| Parameter   |              |     |     | Description               |
| ----------- | ------------ | --- | --- | ------------------------- |
| {ciphertext | | plaintext} |     |     | Selectsthepasswordformat. |
| <PASSWORD>  |              |     |     | Specifiesthepassword.     |
NOTE:Whenthepasswordisnotprovidedonthecommandline,
plaintextpasswordpromptingoccursuponpressingEnter.The
enteredpasswordcharactersaremaskedwithasterisks.
Examples
CreatingavolumenamedlogfileswithpasswordXj#9:
| switch(config)# |     | external-storage |     | logfiles |
| --------------- | --- | ---------------- | --- | -------- |
switch(config-external-storage-logfiles)# password plaintext Xj#9
Creatingavolumenamedbak1withapromptedplaintextpassword:
| switch(config)#                       |         | external-storage |           | bak1       |
| ------------------------------------- | ------- | ---------------- | --------- | ---------- |
| switch(config-external-storage-bak1)# |         |                  |           | password   |
| Enter                                 | the NAS | server           | password: | ********** |
| Re-Enter                              | the     | NAS server       | password: |            |
**********
Clearingthepasswordforvolumelogfiles:
| switch(config)# |     | external-storage |     | logfiles |
| --------------- | --- | ---------------- | --- | -------- |
switch(config-external-storage-logfiles)# no password plaintext Xj#9
41
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |
| --------------------------- | --- | ------------------ | --- | --- |

| Command        | History     |         |              |           |     |     |
| -------------- | ----------- | ------- | ------------ | --------- | --- | --- |
| Release        |             |         | Modification |           |     |     |
| 10.07orearlier |             |         | --           |           |     |     |
| Command        | Information |         |              |           |     |     |
| Platforms      | Command     | context |              | Authority |     |     |
8320 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 8325 |     |     |     | memberswithexecutionrightsforthis |     |     |
| ---- | --- | --- | --- | --------------------------------- | --- | --- |
| 8360 |     |     |     | command.                          |     |     |
show external-storage
| show external-storage |     | [<VOLUME-NAME>] |     |     |     |     |
| --------------------- | --- | --------------- | --- | --- | --- | --- |
Description
Showsexternalstorageconfigurationandstateforallvolumesorforaspecifiedvolume.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<VOLUME-NAME> Specifiestheexternalstoragevolumenamethattheshow
commandwilluse.
Examples
| switch# | show external-storage |     |     |     |     |     |
| ------- | --------------------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
--
|     | Address | VRF | Username | Type | Directory | State |
| --- | ------- | --- | -------- | ---- | --------- | ----- |
----------------------------------------------------------------------------------
--
| nfsvol | 10.1.1.1 | nas | --- | NFSv3 | /home |     |
| ------ | -------- | --- | --- | ----- | ----- | --- |
operational
| nfsfiles | 20.1.1.1  | nas | netstorage | NFSv4 | /netstor | disabled |
| -------- | --------- | --- | ---------- | ----- | -------- | -------- |
| scpdev   | nasserver | nas | scpstor    | SCP   | /scp     |          |
unaccessible
| Command        | History     |         |              |     |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- | --- |
| Release        |             |         | Modification |     |     |     |
| 10.07orearlier |             |         | --           |     |     |     |
| Command        | Information |         |              |     |     |     |
| Platforms      | Command     | context | Authority    |     |     |     |
8320 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
Externalstorage|42

| Platforms |     | Command | context |     | Authority       |
| --------- | --- | ------- | ------- | --- | --------------- |
| 8325      |     |         |         |     | forthiscommand. |
(#)
8360
| show                | running-config |     |                  | external-storage |     |
| ------------------- | -------------- | --- | ---------------- | ---------------- | --- |
| show running-config |                |     | external-storage |                  |     |
Description
Showstherunningconfigurationoftheexternalstorage.
Examples
| switch#          |           | show running-config |          | external-storage |     |
| ---------------- | --------- | ------------------- | -------- | ---------------- | --- |
| external-storage |           |                     | nfsvol   |                  |     |
|                  | address   |                     | 10.1.1.1 |                  |     |
|                  | vrf       |                     | nas      |                  |     |
|                  | type      |                     | nfsv4    |                  |     |
|                  | directoty |                     | /home    |                  |     |
enable
| external-storage |           |     | scpdev     |     |     |
| ---------------- | --------- | --- | ---------- | --- | --- |
|                  | address   |     | 30.1.1.1   |     |     |
|                  | vrf       |     | nas        |     |     |
|                  | username  |     | switchuser |     |     |
|                  | password  |     | ciphertext | xxx |     |
|                  | type      |     | scp        |     |     |
|                  | directoty |     | /home      |     |     |
enable
| Command        | History     |         |         |     |              |
| -------------- | ----------- | ------- | ------- | --- | ------------ |
| Release        |             |         |         |     | Modification |
| 10.07orearlier |             |         |         |     | --           |
| Command        | Information |         |         |     |              |
| Platforms      |             | Command | context |     | Authority    |
8320 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     | (#) |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
8360
| type        | (external |         | storage) |     |     |
| ----------- | --------- | ------- | -------- | --- | --- |
| type {nfsv3 |           | | nfsv4 | | scp}   |     |     |
| no type     | {nfsv3    | | nfsv4 | | scp}   |     |     |
Description
Setsthenetworkattachedstorageaccesstypeforreachingtheexternalstoragevolume.
Thenoformofthiscommanddeletesanexternalstoragevolume.
43
| AOS-CX10.09MonitoringGuide| |     |     | (83xxSwitchSeries) |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- |

| Parameter |     |     | Description                             |     |
| --------- | --- | --- | --------------------------------------- | --- |
| nfsv3     |     |     | SpecifiestheNFSv3networkaccessprotocol. |     |
| nfsv4     |     |     | SpecifiestheNFSv4networkaccessprotocol. |     |
| scp       |     |     | SpecifiestheSCPnetworkaccessprotocol.   |     |
Examples
CreatingthelogfilesvolumeusingNFSV4:
| switch(config)#                           | external-storage |     | logfiles   |     |
| ----------------------------------------- | ---------------- | --- | ---------- | --- |
| switch(config-external-storage-logfiles)# |                  |     | type nfsv4 |     |
Clearingtheexternalstorageaccesstype:
| switch(config)#                           | external-storage |         | logfiles     |           |
| ----------------------------------------- | ---------------- | ------- | ------------ | --------- |
| switch(config-external-storage-logfiles)# |                  |         | no type      | nfsv4     |
| Command                                   | History          |         |              |           |
| Release                                   |                  |         | Modification |           |
| 10.07orearlier                            |                  |         | --           |           |
| Command                                   | Information      |         |              |           |
| Platforms                                 | Command          | context |              | Authority |
config-external-storage-<VOLUME-NAME>
| 8320                 |             |          |     | Administratorsorlocalusergroup    |
| -------------------- | ----------- | -------- | --- | --------------------------------- |
| 8325                 |             |          |     | memberswithexecutionrightsforthis |
| 8360                 |             |          |     | command.                          |
| username             | (external   | storage) |     |                                   |
| username <USER-NAME> |             |          |     |                                   |
| no username          | <USER-NAME> |          |     |                                   |
Description
Setstheusernameforloggingintoanetworkattachedstorageserver.
Thenoformofthiscommandclearsausername.
| Parameter   |     |     | Description           |     |
| ----------- | --- | --- | --------------------- | --- |
| <USER-NAME> |     |     | Specifiestheusername. |     |
Examples
Creatingavolumenamedlogfileswiththeusernamenassuser:
Externalstorage|44

| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)#
username nasuser
Clearingtheusernamenasuserfromaccessingthelogfilesvolume:
| switch(config)#                           | external-storage |         | logfiles     |           |
| ----------------------------------------- | ---------------- | ------- | ------------ | --------- |
| switch(config-external-storage-logfiles)# |                  |         | no username  | nasuser   |
| Command History                           |                  |         |              |           |
| Release                                   |                  |         | Modification |           |
| 10.07orearlier                            |                  |         | --           |           |
| Command Information                       |                  |         |              |           |
| Platforms                                 | Command          | context |              | Authority |
config-external-storage-<VOLUME-NAME>
| 8320          |          |     |     | Administratorsorlocalusergroup    |
| ------------- | -------- | --- | --- | --------------------------------- |
| 8325          |          |     |     | memberswithexecutionrightsforthis |
| 8360          |          |     |     | command.                          |
| vrf (external | storage) |     |     |                                   |
vrf <VRF-NAME>
no vrf <VRF-NAME>
Description
SettingaVRFtoreachnetworkattachedstorage.
ThenoformofthiscommandclearsaccessofaVRFtonetworkattachedstorage.
| Parameter  |     |     | Description          |     |
| ---------- | --- | --- | -------------------- | --- |
| <VRF-NAME> |     |     | SpecifiestheVRFname. |     |
Examples
CreatingthelogfilesvolumeandsettingaVRFnamednastoaccessthenetworkattachedstorage:
| switch(config)#                           | external-storage |     | logfiles |     |
| ----------------------------------------- | ---------------- | --- | -------- | --- |
| switch(config-external-storage-logfiles)# |                  |     | vrf nas  |     |
ClearingaccessofaVRFnamednastothenetworkattachedstorage:
| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)#
no vrf nas
| Command History |     |     |     |     |
| --------------- | --- | --- | --- | --- |
45
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

Release Modification
10.07orearlier --
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8320 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 8325 |     |     | memberswithexecutionrightsforthis |
| ---- | --- | --- | --------------------------------- |
command.
8360
Externalstorage|46

Chapter 8

IP-SLA

IP-SLA

The IP Service Level Agreement (IP-SLA) is a feature that enables the measuring of network performance
between two nodes in a network for different service level agreement parameters such as round-trip
time (RTT), one-way delay, jitter, reachability, packet loss, and voice quality scores. These two nodes can
span across area in access, distribution or core inside a LAN as well as across WAN between core to core
or core to Data Centre switches. This feature helps you measure the SLA for different protocols or
applications such as UDP echo, UDP jitter (for voice and video), TCP connect, HTTP, and ICMP echo. This
guide provides details for managing and monitoring different types of IP-SLAs.

IP-SLA guidelines

n AOS-CX supports only SLA configuration through CLI and thresholds can be configured using NAE

agents using WebUI/REST.

n AOS-CX supports only forever tests. On-demand tests are not supported.

n Maximum sessions: IP-SLA source 500, IP-SLA responder 100.

n NAE can effectively monitor a maximum of 300 parameters, reducing the maximum supported

session by 300.

n NAE supports only syslog.

n NAE agents must be triggered for each IP-SLA test on every switch.

n If multiple IP addresses are received for a DNS query, DNS works with the first resolved IP.

n When the DNS server IP is not configured, the first DNS server in resolve.conf is used.

n The source interface/IP option is not applicable for SLAs configured on 'mgmt' VRF, as it has only one

interface.

n A system time change because of NTP or a manual change causes an incorrect calculation.

n There is no interoperability of UDP echo SLA between AOS-CX and FlexFabric switches.

n Source IP and source port combination must be unique across SLA sessions in a same switch.

n Do not use the same source port across the source and responder sessions in a switch.

n NTP synchronization is a must for SLA types involving one-way delay such as UDP jitter VoIP.

n It is mandatory to set default CoPP to the max value when UDP jitter SLA is enabled otherwise 100%
packet loss can be seen and UDP-Jitter sla probe will result in failure as seen in the following
example.

copp-policy default

class hypertext priority 6 rate 50000 burst 64
default-class priority 6 rate 99999 burst 9999

n Deviations with respect to PVOS results: The packet losses due to internal switch-related issues like

interface shutdown or interface flaps will not be considered as 'Probes Timed-out error', as the IP-SLA
solution is to measure network performance and anomalies. Rather, this kind of packet loss will be
counted in internal counters like 'Destination address unreachable'.

AOS-CX 10.09 Monitoring Guide | (83xx Switch Series)

47

Limitations with VoIP SLAs

n A maximum of 80 concurrent VoIP SLAs can be scheduled in a 20 second slot.

n A single VoIP probe takes 20 seconds to complete.

n The default and minimum probe interval for VoIP SLA is 120 seconds.

n SLAs scheduled in the same slot, periodically sends 1000 probe packets for 120 seconds in 20 second

intervals.

n Default 120 second probe interval is divided in to 6 slots of 20 seconds to avoid synchronization of all

configured VoIP SLAs sending probes at the same time.

n SLAs started at the same time exceeding the concurrent limit of 80 must wait for the next 20 second

VoIP slot to open before moving to ‘running’ state.

n The maximum number of VoIP SLAs supported is 80 X 6 slots = 480 SLAs.

n SLAs exceeding 480 will continue to remain in the 'waiting for VoIP slot' until any slot is freed by

stopping the running SLA.

n To avoid high RTT, a single switch with more than 20 SLAs should not have single responder SLA.

n When IP is received dynamically (e.g. using DHCP) for interfaces other than management interface,

IPSLA source or responder has to be configured only using interface name.

IP-SLA commands

http
http {get | raw} URL [source {<SOURCE-IPV4-ADDR> | <IFNAME>} source-port <PORT-NUM>]

[proxy proxy-url] [cache disable] [name-server <IPV4-ADDR-DNS-SERVER>]
[probe-interval <30-604800>] [version<VERSION-NUMBER>] [http-raw-request <RAW-

PAYLOAD>]

Description

Configures HTTP as the IP-SLA test mechanism. Requires destination URL and type of HTTP request
(raw/get).

Parameter

{get | raw}

URL

Description

Selects HTTP request type as GET or RAW where the
system will generate or provide HTTP payload.

Specifies HTTP URL address of syntax. http://<HOST
NAME/IP-ADDRESS>:<PORT>/<PATH>.

source {<SOURCE-IPV4-ADDR> | <IFNAME>}

Selects the source IPv4 address for SLA probes or the
source interface to use for sending IP-SLA probes.

source-port <PORT-NUM>

cache disable

Specifies the value of the source port for the IP-SLA
probes.

Selects cache option for the HTTP server. By default the
option is enabled.

name-server <IPV4-ADDR-DNS-SERVER>

Specifies the IPv4 address of DNS server.

probe-interval <PROBE-INTERVAL>

Specifies the probe interval in seconds. Range: 30 to
604800.

IP-SLA | 48

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
version <VERSION-NUMBER> SpecifiesthesourceinterfacetouseforsendingIP-SLA
probes.
| http-raw-request | <RAW-PAYLOAD> |     | HTTPrawrequest.String. |
| ---------------- | ------------- | --- | ---------------------- |
Examples
switch(config-ipsla-1)# http get http://device.arubanetworks.com/root/home.html
| switch(config-ipsla-1)# |     | http raw |     |
| ----------------------- | --- | -------- | --- |
http://device.arubanetworks.com/root/home.html
switch(config-ipsla-1)#
|     |     | http 2.2.2.2 | source 1/1/1 |
| --- | --- | ------------ | ------------ |
switch(config-ipsla-1)# http http://device.arubanetworks.com source 2.2.2.1
switch(config-ipsla-1)# http http://device.arubanetworks.com/root/home.html
| source-interface | 1/1/1 |     |     |
| ---------------- | ----- | --- | --- |
switch(config-ipsla-1)# http http://device.arubanetworks.com name-server
10.10.10.2
switch(config-ipsla-1)# http raw raw-request "GET /en/US/hmpgs/index.html
HTTP/1.0\r\n\r\n"
| Command History     |         |              |           |
| ------------------- | ------- | ------------ | --------- |
| Release             |         | Modification |           |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | ------------------------------ |
8360
icmp-echo
icmp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} [source {<SOURCE-IPV4-ADDR> | <IFNAME>}]
[name-server <IPV4-ADDR-DNS-SERVER>] [payload-size <PAYLOAD-SIZE>]
| [tos <TYPE-OF-SERVICE>] |     | [probe-interval | <PROBE-INTERVAL>] |
| ----------------------- | --- | --------------- | ----------------- |
Description
ConfiguresICMPechoastheIP-SLAtestmechanism.RequiresdestinationaddressfortheIP-SLAtest.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
{<DEST-IPV4-ADDR> | <HOSTNAME>} SelectsthedestinationIPv4addressfortheIP-SLAor
thehostnameofthedestination.
| [source {<SOURCE-IPV4-ADDR> |     | | <IFNAME>}] |     |
| --------------------------- | --- | ------------ | --- |
SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
name-server <IPV4-ADDR-DNS-SERVER> SpecifiestheDNSserverfordestinationhostname
resolution.
49
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
payload-size <PAYLOAD-SIZE> SpecifiesthepayloadsizeofanSLAprobe.Range:0to
1440.
tos <TYPE-OF-SERVICE> Specifiesthetypeofservetobeusedintheprobe
packets.Range:0to255.
| probe-interval | <PROBE-INTERVAL> |     |     |     |     |     |
| -------------- | ---------------- | --- | --- | --- | --- | --- |
Specifiestheprobeintervalinseconds.Range:5to
604800.
Examples
| switch(config)#             | ip-sla | test |           |                |         |     |
| --------------------------- | ------ | ---- | --------- | -------------- | ------- | --- |
| switch(config-ip-sla-test)# |        |      | icmp-echo | 2.2.2.2        |         |     |
| switch(config-ip-sla-test)# |        |      | icmp-echo | 2.2.2.2 source | 3.3.3.3 |     |
switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
| name-server | 4.4.4.4 |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- |
switch(config-ip-sla-test)#
|                     |         |                | icmp-echo    | 2.2.2.2 source | 3.3.3.3 payload-size | 400 |
| ------------------- | ------- | -------------- | ------------ | -------------- | -------------------- | --- |
| name-server         | 4.4.4.4 | probe-interval | 80           |                |                      |     |
| Command History     |         |                |              |                |                      |     |
| Release             |         |                | Modification |                |                      |     |
| 10.07orearlier      |         |                | --           |                |                      |     |
| Command Information |         |                |              |                |                      |     |
| Platforms           | Command | context        |              | Authority      |                      |     |
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
8325
8360
ip-sla
ip-sla <IP-SLA-NAME>
| no ip-sla <IP-SLA-NAME> |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- |
Description
CreatesanIPServiceLevelAgreement(SLA)profileandswitchestotheconfig-ip-slacontext.
ThenoformofthiscommanddeletesanIP-SLAprofile.Bydefault,allprofileusethedefaultVRF
(default).
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<IP-SLA-NAME>
SpecifiesanIP-SLAprofilename.Length:1to63characters.
Examples
CreatinganIP-SLA:
IP-SLA|50

| switch(config)# | ip-sla | 1   |     |     |
| --------------- | ------ | --- | --- | --- |
switch(config-ip-sla-1)#
DeletinganIP-SLA:
| switch(config)# | no  | ip-sla | 1   |     |
| --------------- | --- | ------ | --- | --- |
switch(config)#
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
config
8320 Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8360
ip-sla responder
ip-sla responder <SLA-NAME> {udp-echo | tcp-connect | udp-jitter-voip} <PORT-NUM>
| [source | {<SOURCE-IPV4-ADDR> |     | | <IFNAME>}][vrf | <VRF-NAME>] |
| ------- | ------------------- | --- | ---------------- | ----------- |
no ip-sla responder <SLA-NAME> {udp-echo | tcp-connect | udp-jitter-voip} <PORT-NUM>
| [source | {<SOURCE-IPV4-ADDR> |     | | <IFNAME>}][vrf | <VRF-NAME>] |
| ------- | ------------------- | --- | ---------------- | ----------- |
Description
SelectstheIP-SLAresponder.Therespondercanbeconfiguredforudp-echo,tcp-connect,udp-jitter-
voiptype.ItrequirestheSLAname,SLAtype,andportnumberasarguments.SourceIP/interfaceIDisa
mustfortypeudp-jitter-voipandoptionalforothertypes.
ThenoformofthiscommandremovestheIP-SLAresponder.
| Parameter       |     |     | Description                                    |     |
| --------------- | --- | --- | ---------------------------------------------- | --- |
| <SLA-NAME>      |     |     | SpecifiestheSLAname.                           |     |
| udp-echo        |     |     | Enablesresponderforudp-echoprobes.             |     |
| tcp-connect     |     |     | SelectsTCPconnectastheIP-SLAtestmechanism.     |     |
| vrf <VRF-NAME>  |     |     | SpecifiesthenameoftheVRFtouse.                 |     |
| udp-jitter-voip |     |     | SelectsVOIPjitterastheIP-SLAtestmechanism.     |     |
| <PORT-NUM>      |     |     | SpecifiestheportnumbertolistenforIP-SLAprobes. |     |
Range:1to65535.
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
51
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

Examples
switch(config)# ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
switch(config)# ip-sla responder SLA1 udp-echo 8000 source 1/1/1
switch(config)# no ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
| Command        | History     |         |     |         |              |
| -------------- | ----------- | ------- | --- | ------- | ------------ |
| Release        |             |         |     |         | Modification |
| 10.07orearlier |             |         |     |         | --           |
| Command        | Information |         |     |         |              |
| Platforms      |             | Command |     | context | Authority    |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
8360
| show | ip-sla | responder |            |     |     |
| ---- | ------ | --------- | ---------- | --- | --- |
| show | ip-sla | responder | <SLA-NAME> |     |     |
Description
ShowsthegivenIP-SLAresponderconfigurationandoperationstatus.
| Parameter  |     |     |     |     | Description          |
| ---------- | --- | --- | --- | --- | -------------------- |
| <SLA-NAME> |     |     |     |     | SpecifiestheSLAname. |
Examples
| switch(config)# |             |           | show | ip-sla responder | SLA3         |
| --------------- | ----------- | --------- | ---- | ---------------- | ------------ |
|                 | SLA         | Name      |      | : SLA3           |              |
|                 | IP-SLA      | Type      |      | : Udp-echo       |              |
|                 | VRF         |           |      | : Default        |              |
|                 | Responder   | Port      |      | : 8000           |              |
|                 | Responder   | IP        |      | : 2.2.2.3        |              |
|                 | Responder   | Interface |      | : 1/1/1          |              |
|                 | Responder   | Status    |      | : Running        |              |
| Command         | History     |           |      |                  |              |
| Release         |             |           |      |                  | Modification |
| 10.07orearlier  |             |           |      |                  | --           |
| Command         | Information |           |      |                  |              |
IP-SLA|52

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --- | --------------- | --- |
8360
| show | ip-sla | responder |     | results |     |     |
| ---- | ------ | --------- | --- | ------- | --- | --- |
show ip-sla responder <SLA-NAME> <SOURCE-IPV4-ADDR> <PORT-NUM> results
Description
Showsthegivenip-slaresponderstatisticsforagivensourceIPandport.Thiscommandisonly
applicableforthesourceswheresourceIPandportareconfigured.
| Parameter  |     |     |     |     | Description          |     |
| ---------- | --- | --- | --- | --- | -------------------- | --- |
| <SLA-NAME> |     |     |     |     | SpecifiestheSLAname. |     |
<SOURCE-IPV4-ADDR>
SpecifiesthesourceIPV4address.
| <PORT-NUM> |     |     |     |     | Specifiestheportnumber.Range:1to65535. |     |
| ---------- | --- | --- | --- | --- | -------------------------------------- | --- |
Examples
| switch#        |             | show ip-sla | responder |            | SLA1 2.2.2.1 | 8000 results |
| -------------- | ----------- | ----------- | --------- | ---------- | ------------ | ------------ |
|                | IP-SLA      | Type        |           | : Udp-echo |              |              |
|                | VRF         | Name        |           | : Default  |              |              |
|                | Source      | IP          |           | : 2.2.2.1  |              |              |
|                | Source      | Port        |           | : 8000     |              |              |
|                | Responder   | Port        |           | : 8888     |              |              |
|                | Responder   | IP          |           | : 2.2.2.3  |              |              |
|                | Responder   | Interface   |           | :          |              |              |
|                | Responder   | Status      |           | : Running  |              |              |
|                | Packets     | Received    |           | : 2        |              |              |
|                | Packets     | Sent        |           | : 2        |              |              |
| Command        | History     |             |           |            |              |              |
| Release        |             |             |           |            | Modification |              |
| 10.07orearlier |             |             |           |            | --           |              |
| Command        | Information |             |           |            |              |              |
| Platforms      |             | Command     | context   |            | Authority    |              |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --- | --------------- | --- |
8360
| show | ip-sla | <SLA-NAME> |         |     |     |     |
| ---- | ------ | ---------- | ------- | --- | --- | --- |
| show | ip-sla | <SLA-NAME> | results |     |     |     |
53
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

Description
ShowsthegivenIP-SLAsourceconfigurationandstatus.
| Parameter  |     |     |     |     | Description          |     |     |
| ---------- | --- | --- | --- | --- | -------------------- | --- | --- |
| <SLA-NAME> |     |     |     |     | SpecifiestheSLAname. |     |     |
results
ShowsthestatisticscalculatedforanSLAtype.
Examples
| switch#         | show         | ip-sla            | xyz            | results  |               |                   |             |
| --------------- | ------------ | ----------------- | -------------- | -------- | ------------- | ----------------- | ----------- |
|                 | IP-SLA       | session           | status         |          |               |                   |             |
|                 | IP-SLA       | Name              |                |          |               | : xyz             |             |
|                 | IP-SLA       | Type              |                |          |               | : tcp-connect     |             |
|                 | Destination  |                   | Host           | Name/IP  | Address:      | 2.2.2.1           |             |
|                 | Destination  |                   | Port           |          |               | : 8888            |             |
|                 | Source       | IP                | Address/IFName |          |               | : 2.2.2.2         |             |
|                 | Source       | Port              |                |          |               | : 5555            |             |
|                 | Status       |                   |                |          |               | : Running         |             |
|                 | IP-SLA       | session           | cumulative     |          | counters      |                   |             |
|                 | Total        | Probes            | Transmitted    |          |               | : 1               |             |
|                 | Probes       | Timed-out         |                |          |               | : 0               |             |
|                 | Bind         | Error             |                |          |               | : 0               |             |
|                 | Destination  |                   | Address        |          | Unreachable   | : 0               |             |
|                 | DNS          | Resolution        |                | Failures |               | : 0               |             |
|                 | Reception    |                   | Error          |          |               | : 0               |             |
|                 | Transmission |                   | Error          |          |               | : 0               |             |
|                 | IP-SLA       | Latest            | Probe          | Results  |               |                   |             |
|                 | Last         | Probe             | Time           |          |               | : 2018 Jul        | 13 02:00:35 |
|                 | Packets      |                   | Sent           |          |               | : 1               |             |
|                 | Packets      |                   | Received       |          |               | : 1               |             |
|                 | Packet       | Loss              | in             | Test     |               | : 0.0000%         |             |
|                 | Minimum      | RTT(ms)           |                |          |               | : 0.7900          |             |
|                 | Maximum      | RTT(ms)           |                |          |               | : 0.7900          |             |
|                 | Average      | RTT(ms)           |                |          |               | : 0.7900          |             |
|                 | DNS RTT(ms)  |                   |                |          |               | : 0.0000          |             |
|                 | TCP RTT(ms)  |                   |                |          |               | : 0.9710          |             |
| switch(config)# |              |                   | show           | ip-sla   | xyz           |                   |             |
|                 | IP-SLA       | Name              |                |          | : xyz         |                   |             |
|                 | Status       |                   |                |          | : scheduled   |                   |             |
|                 | IP-SLA       | Type              |                |          | : tcp-connect |                   |             |
|                 | VRF          |                   |                |          | : ipslasrc    |                   |             |
|                 | Source       | Port              |                |          | : 5555        |                   |             |
|                 | Source       | IP                |                |          | : 2.2.2.2     |                   |             |
|                 | Source       | Interface         |                |          | :             |                   |             |
|                 | Domain       | Name              | Server         |          | :             |                   |             |
|                 | Probe        | interval(seconds) |                |          | : 90          |                   |             |
| switch(config)# |              |                   | show           | ip-sla   | jitter-sla    | results           |             |
|                 | IP-SLA       | session           | status         |          |               |                   |             |
|                 | IP-SLA       | Name              |                |          |               | : jitter-sla      |             |
|                 | IP-SLA       | Type              |                |          |               | : udp-jitter-voip |             |
|                 | Destination  |                   | Host           | Name/IP  | Address:      | 2.2.2.1           |             |
IP-SLA|54

|                 | Destination             |            | Port           |                   | : 8888     |              |            |     |
| --------------- | ----------------------- | ---------- | -------------- | ----------------- | ---------- | ------------ | ---------- | --- |
|                 | Source                  | IP         | Address/IFName |                   | :          |              |            |     |
|                 | Source                  | Port       |                |                   | : 5555     |              |            |     |
|                 | Status                  |            |                |                   | : Running  |              |            |     |
|                 | IP-SLA                  | Session    | Cumulative     | Counters          |            |              |            |     |
|                 | Total                   | Probes     | Transmitted    |                   | : 1        |              |            |     |
|                 | Probes                  | Timed-out  |                |                   | : 0        |              |            |     |
|                 | Bind                    | Error      |                |                   | : 0        |              |            |     |
|                 | Destination             |            | Address        | Unreachable       | : 0        |              |            |     |
|                 | DNS                     | Resolution | Failures       |                   | : 0        |              |            |     |
|                 | Reception               |            | Error          |                   | : 0        |              |            |     |
|                 | Transmission            |            | Error          |                   | : 0        |              |            |     |
|                 | IP-SLA                  | Latest     | Probe Results  |                   |            |              |            |     |
|                 | Last                    | Probe      | Time           |                   | : 2018 Jul | 13           | 02:02:48   |     |
|                 | Packets                 | Sent       |                |                   | : 1        |              |            |     |
|                 | Packets                 | Received   |                |                   | : 1        |              |            |     |
|                 | Packet                  | Loss       | in Test        |                   | : 0.0000%  |              |            |     |
|                 | Minimum                 | RTT(ms)    |                |                   | : 0.7900   |              |            |     |
|                 | Maximum                 | RTT(ms)    |                |                   | : 0.7900   |              |            |     |
|                 | Average                 | RTT(ms)    |                |                   | : 0.7900   |              |            |     |
|                 | DNS                     | RTT(ms)    |                |                   | : 0.0000   |              |            |     |
|                 | Min                     | Positive   | SD             |                   | : 1        | Min Positive | DS         | : 2 |
|                 | Max                     | Positive   | SD             |                   | : 1        | Max Positive | DS         | : 2 |
|                 | Positive                |            | SD Number      |                   | : 2        | Positive     | DS Number  | : 2 |
|                 | Positive                |            | SD Sum         |                   | : 2        | Positive     | DS Sum     | : 4 |
|                 | Positive                |            | SD Average     |                   | : 5        | Positive     | DS Average | : 5 |
|                 | Min                     | Negative   | SD             |                   | : 1        | Min Negative | DS         | : 1 |
|                 | Max                     | Negative   | SD             |                   | : 1        | Max Negative | DS         | : 1 |
|                 | Negative                |            | SD Number      |                   | : 2        | Negative     | DS Number  | : 4 |
|                 | Negative                |            | SD Sum         |                   | : 2        | Negative     | DS Sum     | : 4 |
|                 | Negative                |            | SD Average     |                   | : 5        | Negative     | DS Average | : 5 |
|                 | Max                     | SD Delay   |                |                   | : 0        | Max DS       | Delay      | : 0 |
|                 | Min                     | SD Delay   |                |                   | : 0        | Min DS       | Delay      | : 0 |
|                 | Average                 | SD         | Delay          |                   | : 0        | Average      | DS Delay   | : 0 |
|                 | Voice Scores:           |            |                |                   |            |              |            |     |
|                 | MOS                     | Score      |                |                   | : 4.38     | ICPIF        |            | : 0 |
| switch(config)# |                         |            | show ip-sla    | m3op              |            |              |            |     |
|                 | IP-SLA                  | Name       |                | : jitter-sla      |            |              |            |     |
|                 | Status                  |            |                | : Running         |            |              |            |     |
|                 | IP-SLA                  | Type       |                | : udp-jitter-voip |            |              |            |     |
|                 | VRF                     |            |                | : ipslasrc        |            |              |            |     |
|                 | Source                  | IP         |                | : 2.2.2.2         |            |              |            |     |
|                 | Source                  | Interface  |                | :                 |            |              |            |     |
|                 | Domain                  | Name       | Server         | :                 |            |              |            |     |
|                 | TOS                     |            |                | : 10              |            |              |            |     |
|                 | Probe Interval(seconds) |            |                | : 90              |            |              |            |     |
|                 | Advantage               | Factor     |                | : 0               |            |              |            |     |
|                 | Codec Type              |            |                | : g711a           |            |              |            |     |
| switch(config)# |                         |            | show ip-sla    | http-sla          |            |              |            |     |
|                 | IP-SLA                  | Name       |                | : http-sla        |            |              |            |     |
|                 | Status                  |            |                | : Running         |            |              |            |     |
|                 | IP-SLA                  | Type       |                | : http            |            |              |            |     |
55
AOS-CX10.09MonitoringGuide| (83xxSwitchSeries)

|     | VRF        |                   |        |     | : ipslasrc         |     |     |     |     |     |     |     |
| --- | ---------- | ----------------- | ------ | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
|     | Source     | IP                |        |     | : 2.2.2.2          |     |     |     |     |     |     |     |
|     | Source     | Interface         |        |     | :                  |     |     |     |     |     |     |     |
|     | Domain     | Name              | Server |     | : 10.10.10.2       |     |     |     |     |     |     |     |
|     | Probe      | Interval(seconds) |        |     | : 90               |     |     |     |     |     |     |     |
|     | HTTP       | Request           | Type   |     | : GET              |     |     |     |     |     |     |     |
|     | HTTP/HTTPS |                   | URL    |     | : abcd.com/ws/home |     |     |     |     |     |     |     |
|     | Cache      |                   |        |     | : Enabled          |     |     |     |     |     |     |     |
|     | HTTP       | Proxy             | URL    |     | :                  |     |     |     |     |     |     |     |
|     | HTTP       | Version           | Number |     | : 1.1              |     |     |     |     |     |     |     |
```
| ##### | IP-SLA |     | status | description |     |     |     |     |     |     |     |     |
| ----- | ------ | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
```
|     | | Status |     |     |     | |   | Description |     |     |     |     |     | |   |
| --- | -------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
|-------------------------|------------------------------------------------|
|     | | Running |     |     |     | |   | SLA is | fully operational |     |     |     |     | |   |
| --- | --------- | --- | --- | --- | --- | ------ | ----------------- | --- | --- | --- | --- | --- |
| Bind Error | Another service is using the same source port |
|     | | Interface |     | Down |     | |   | Interface | status | is not | up  |     |     |     |
| --- | ----------- | --- | ---- | --- | --- | --------- | ------ | ------ | --- | --- | --- | --- |
| Dns Resolution Error | Failed to resolve destination hostname |
|     | | No       | Route |       |     | |   | No available | route    | to the   | responder |         |     | |   |
| --- | ---------- | ----- | ----- | --- | --- | ------------ | -------- | -------- | --------- | ------- | --- | --- |
|     | | Internal |       | Error |     | |   | Unexpected   | error    | prevents | SLA       | session |     | |   |
|     | | Disabled |       |       |     | |   | SLA is       | disabled |          |           |         |     | |   |
|Configuration Incomplete | Configuration is not complete to enable the SLA|
```
| ##### | IP  | SLA | session | cumulative |     | counters | description |     |     |     |     |     |
| ----- | --- | --- | ------- | ---------- | --- | -------- | ----------- | --- | --- | --- | --- | --- |
```
|     | | Status |     |     |     |     | |   | Description |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
|
|--------------------------------|--------------------------------------------
------------------------------|
|Probes Timed-out | Total numbers of probes failed to receive
| response. |        |       |     |             |     | |   |               |     |        |              |     |        |
| --------- | ------ | ----- | --- | ----------- | --- | --- | ------------- | --- | ------ | ------------ | --- | ------ |
|           | |Bind  | Error |     |             |     | |   | Total numbers | of  | probes | transmission |     | failed |
| as        | source | port  | not | available.| |     |     |               |     |        |              |     |        |
|Destination Address Unreachable | Total numbers of probes transmission failed
| due | to route |     | unavailable. |     | |   |     |     |     |     |     |     |     |
| --- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|DNS Resolution Failures | Total numbers of probes failed due to DNS
| resolution     |               | failure.    |                  |            |     | |            |               |     |        |            |     |     |
| -------------- | ------------- | ----------- | ---------------- | ---------- | --- | ------------ | ------------- | --- | ------ | ---------- | --- | --- |
|                | |Reception    |             | Error            |            |     | |            | Total numbers | of  | probes | failed due | to  |     |
| internal       |               | error       | in               | reception. |     | |            |               |     |        |            |     |     |
|                | |Transmission |             |                  | Error      |     | |            | Total numbers | of  | probes | failed due | to  |     |
| internal       |               | errr        | in transmission. |            |     | |            |               |     |        |            |     |     |
| Command        |               | History     |                  |            |     |              |               |     |        |            |     |     |
| Release        |               |             |                  |            |     | Modification |               |     |        |            |     |     |
| 10.07orearlier |               |             |                  |            |     | --           |               |     |        |            |     |     |
| Command        |               | Information |                  |            |     |              |               |     |        |            |     |     |
| Platforms      |               | Command     |                  | context    |     | Authority    |               |     |        |            |     |     |
8320 Administratorsorlocalusergroupmemberswithexecutionrights
Operator(>)orManager
| 8325 |     | (#) |     |     |     | forthiscommand. |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
8360
IP-SLA|56

start-test
start-test
Description
StartstheIP-SLAprobes.
Examples
| switch(config)#             | ip-sla | test       |     |
| --------------------------- | ------ | ---------- | --- |
| switch(config-ip-sla-test)# |        | start-test |     |
| Command History             |        |            |     |
Release Modification
10.07orearlier --
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-ip-sla-<IP-SLA-NAME>
| 8320 |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | ----------------------------------------- |
| 8325 |     |     | executionrightsforthiscommand.            |
8360
stop-test
stop-test
Description
StopstheIP-SLAprobes.
Examples
| switch(config)#             | ip-sla | test      |     |
| --------------------------- | ------ | --------- | --- |
| switch(config-ip-sla-test)# |        | stop-test |     |
| Command History             |        |           |     |
Release Modification
10.07orearlier --
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-ip-sla-<IP-SLA-NAME>
| 8320 |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | ----------------------------------------- |
| 8325 |     |     | executionrightsforthiscommand.            |
8360
57
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

tcp-connect
tcp-connect {<DEST-IPV4-ADDR> | <HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>]
| [probe-interval | <PROBE-INTERVAL>] |     |     |     |
| --------------- | ----------------- | --- | --- | --- |
Description
ConfiguresTCPconnectastheIP-SLAtestmechanism.Requiresdestinationaddress/hostnameand
destinationportfortheIP-SLAoftcp-connectIP-SLAtype.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
{<DEST-IPV4-ADDR> | <HOSTNAME>} SelectsthedestinationIPv4addressfortheIP-SLAor
thehostnameofthedestination.
| <PORT-NUM> |     |     |     | DestinationportfortheIP-SLA.Range:1to65535. |
| ---------- | --- | --- | --- | ------------------------------------------- |
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
| [source-port | <PORT-NUM>]             |     |     | SpecifiestheportfortheIP-SLAtest. |
| ------------ | ----------------------- | --- | --- | --------------------------------- |
| [name-server | <IPV4-ADDR-DNS-SERVER>] |     |     |                                   |
SpecifiestheDNSserverfordestinationhostname
resolution.
[probe-interval <PROBE-INTERVAL>] Probeintervalinseconds.Range:30to604800.
Examples
| switch(config-ipsla-1)# |     | tcp-connect | 2.2.2.2 | 8080 |
| ----------------------- | --- | ----------- | ------- | ---- |
switch(config-ipsla-1)# tcp-connect 2.2.2.2 8080 source 2.2.2.1 source-port
6000
switch(config-ipsla-1)# tcp-connect 2.2.2.2 8080 source 1/1/1 source-port
6000
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
| source 2.2.2.1 | source-port | 6000 |     |     |
| -------------- | ----------- | ---- | --- | --- |
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
| source 1/1/1 | source-port | 6000 |     |     |
| ------------ | ----------- | ---- | --- | --- |
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
| name-server    | 10.10.10.2  |         |              |           |
| -------------- | ----------- | ------- | ------------ | --------- |
| Command        | History     |         |              |           |
| Release        |             |         | Modification |           |
| 10.07orearlier |             |         | --           |           |
| Command        | Information |         |              |           |
| Platforms      | Command     | context |              | Authority |
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
8360
IP-SLA|58

udp-echo
udp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>] [payload-
size
<PAYLOAD-SIZE>] [tos <TYPE-OF-SERVICE>] [probe-interval <PROBE-INTERVAL>]
Description
ConfiguresUDPechoastheIP-SLAtestmechanism.Requiresdestinationaddress/hostnameand
destinationportnumberfortheIP-SLAofudp-echoSLAtype.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
{<DEST-IPV4-ADDR> | <HOSTNAME>} SelectsthedestinationIPv4addressfortheIP-SLAor
thehostnameofthedestination.
| <PORT-NUM> |     | SpecifiesthedestinationportfortheIP-SLA.Range:1 |     |
| ---------- | --- | ----------------------------------------------- | --- |
to65535.
| [source {<SOURCE-IPV4-ADDR> | | <IFNAME>}] |     |     |
| --------------------------- | ------------ | --- | --- |
SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
[source-port <PORT-NUM>] SpecifiessourceportfortheIP-SLAtest.Range:1to
65535.
[name-server <IPV4-ADDR-DNS-SERVER>] SpecifiestheDNSserverfordestinationhostname
resolution.
[payload-size <PAYLOAD-SIZE>] SpecifiesthepayloadsizeofanSLAprobe.Range:28
to1440.
| [<TYPE-OF-SERVICE>] |     | Typeofservice.Range:0to255. |     |
| ------------------- | --- | --------------------------- | --- |
probe-interval <PROBE-INTERVAL>
Probeintervalinseconds.Range:5to604800.
Examples
| switch(config-ipsla-1)# | udp-echo 2.2.2.2 | 8080        |         |
| ----------------------- | ---------------- | ----------- | ------- |
| switch(config-ipsla-1)# | udp-echo 2.2.2.2 | 8080 source | 2.2.2.1 |
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080
| switch(config-ipsla-1)# | udp-echo 2.2.2.2 | 8080 source | 1/1/1 |
| ----------------------- | ---------------- | ----------- | ----- |
switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 2.2.2.1 payload-size 50
switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 1/1/1 payload-size 50
| switch(config-ipsla-1)# | udp-echo 2.2.2.2 | 8080 payload-size | 50  |
| ----------------------- | ---------------- | ----------------- | --- |
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080 source
2.2.2.1
| payload-size 50 |     |     |     |
| --------------- | --- | --- | --- |
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080 source
1/1/1
| payload-size 50 |     |     |     |
| --------------- | --- | --- | --- |
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080
| name-server 10.10.10.2 |     |     |     |
| ---------------------- | --- | --- | --- |
Command History
| Release        | Modification |     |     |
| -------------- | ------------ | --- | --- |
| 10.07orearlier | --           |     |     |
59
AOS-CX10.09MonitoringGuide| (83xxSwitchSeries)

Command Information

Platforms

Command context

Authority

8320
8325
8360

config-ip-sla-<IP-SLA-NAME>

Administrators or local user group members with
execution rights for this command.

udp-jitter-voip
udp-jitter-voip {<DEST-IPV4-ADDR> | <HOSTNAME>} <PORT-NUM> [codec-type <CODEC-TYPE>]
[advantage-factor <VALUE>] [source {<SOURCE-IPV4-ADDR> | <IFNAME>} [source-port

<PORT-NUM>]]

[name-server <IPV4-ADDR-DNS-SERVER>][probe-interval <PROBE-INTERVAL>] [tos <TYPE-OF-

SERVICE>]

Description

Configure UDP jitter voip as the IP-SLA test mechanism. Requires destination address/hostname and
source address/interface for the IP-SLA of udp-jitter-voip IP-SLA type.

Parameter

Description

{<DEST-IPV4-ADDR>|<HOSTNAME>}

<PORT-NUM>

Selects the destination IPv4 address for the IP-SLA or
the hostname of the destination.

Selects the port number for the IP-SLA. Range: 1 to
65535.

[codec-type <CODEC-TYPE>]

Selects the codec-type for the Voip IP-SLA test.

[advantage-factor <ADVANTAGE-FACTOR>]

Selects the value for the advantage factor. Default
value is 0.

[source {<SOURCE-IPV4-ADDR> | <IFNAME>}]

Selects the source IPv4 address for SLA probes or the
source interface to use for sending IP-SLA probes.

[source-port <PORT-NUM>]

[name-server <IPV4-ADDR-DNS-SERVER>]

Specifies the value of source port for the IP-SLA
probes.

Specifies the DNS server for destination hostname
resolution.

tos <TYPE-OF-SERVICE>

Specifies the type of service. Range: 0 to 255.

probe-interval <PROBE-INTERVAL>

Specifies the probe interval in seconds. Range: 120 to
604800.

Examples

switch(config-ipsla-1)# udp-jitter-voip
type g711a

2.2.2.2 8080 advantage-factor 10 codec-

switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10

codec-type g711a source 2.2.2.1

switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080

advantage-factor 10 codec-type g711a

switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10

IP-SLA | 60

| codec-type | g711a | source | 1/1/1 |     |     |     |
| ---------- | ----- | ------ | ----- | --- | --- | --- |
switch(config-ipsla-1)#
|                  |     |     |            | udp-jitter-voip | https://device.arubanetworks.com | 8080 |
| ---------------- | --- | --- | ---------- | --------------- | -------------------------------- | ---- |
| advantage-factor |     | 10  | codec-type | g711a source    | 2.2.2.1                          |      |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
| advantage-factor |     | 10  | codec-type | g711a source | 1/1/1 |     |
| ---------------- | --- | --- | ---------- | ------------ | ----- | --- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
advantage-factor 10 codec-type g711a name-server 10.10.10.2 probe-interval 120
| source 10.1.1.1 |             | source-port |         | 8888 tos 10  |           |     |
| --------------- | ----------- | ----------- | ------- | ------------ | --------- | --- |
| Command         | History     |             |         |              |           |     |
| Release         |             |             |         | Modification |           |     |
| 10.07orearlier  |             |             |         | --           |           |     |
| Command         | Information |             |         |              |           |     |
| Platforms       | Command     |             | context |              | Authority |     |
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 8325 |     |     |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | --- | --- | ------------------------------ | --- |
8360
vrf (ip sla)
vrf <VRF-NAME>
no vrf [<VRF-NAME>]
Description
ConfigurestheVRFonwhichtheSLAwillsendorreceivepackets.Bydefault,thedefaultVRFisused.
ThenoformofthecommandremovesVRFfromSLA.
| Parameter  |     |     |     | Description                               |     |     |
| ---------- | --- | --- | --- | ----------------------------------------- | --- | --- |
| <VRF-NAME> |     |     |     | SpecifiesaVRFname.Length:Default:default. |     |     |
Examples
| switch(config-ip-sla-test)# |             |     |     | vrf ipslasrc |     |     |
| --------------------------- | ----------- | --- | --- | ------------ | --- | --- |
| switch(config-ip-sla-test)# |             |     |     | no vrf       |     |     |
| Command                     | History     |     |     |              |     |     |
| Release                     |             |     |     | Modification |     |     |
| 10.07orearlier              |             |     |     | --           |     |     |
| Command                     | Information |     |     |              |     |     |
61
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
8360
| L1-100Mbps | downshift |     | commands |     |
| ---------- | --------- | --- | -------- | --- |
| downshift  | enable    |     |          |     |
downshift-enable
no downshift-enable
Description
Enables/disablesautomaticspeeddownshiftonaninterfacethatsupportsdownshift,generally
1GBASE-Tports.Whenenabled,downshiftallowsaninterfacetolinkataloweradvertisedspeedwhen
unabletoestablishastablelinkatthemaximumspeed.Downshiftingonlyappliestophysicalinterfaces
thatarenotmembersofaLAGandisonlyavailablewhenauto-negotiationisenabled.Whenonlyone
speedisadvertised,downshiftwillnotbetriggered.
Examples
| switch(config-if)# |     | interface        | 1/1/1 |     |
| ------------------ | --- | ---------------- | ----- | --- |
| switch(config-if)# |     | downshift-enable |       |     |
Warning: this is a non-standard mode for use only when standards-based
auto-negotiation is not able to establish a stable link. Enabling this
may cause the port to link at a lower than expected speed and should
not be used on ports that are members of a LAG. Support calls may require
| this feature | to     | be disabled |     |     |
| ------------ | ------ | ----------- | --- | --- |
| Continue     | (y/n)? |             |     |     |
switch(config-if)#
Whenautomaticdownshiftisenabled:
| switch(config-if)# |       | show running-config |     | interface |
| ------------------ | ----- | ------------------- | --- | --------- |
| interface          | 1/1/1 |                     |     |           |
downshift-enable
Disablingautomaticspeeddownshift:
| switch(config-if)# |     | interface           | 1/1/1 |     |
| ------------------ | --- | ------------------- | ----- | --- |
| switch(config-if)# |     | no downshift-enable |       |     |
| Command History    |     |                     |       |     |
IP-SLA|62

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show interface |     |     |     |
| -------------- | --- | --- | --- |
show interface [<IFNNAME>|<IFRANGE>] [brief | physical | extended [non-zero]]
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief | physical]
show interface [lag | loopback | tunnel | vlan ] [<ID>] [extended [non-zero]]
| show interface | vxlan <ID> | [brief | | physical] |
| -------------- | ---------- | -------- | --------- |
| show interface | vxlan <ID> | [brief | | physical] |
Description
Showsactiveconfigurationsandoperationalstatusinformationforinterfaces.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IFNAME>
Specifiesainterfacename.
| <IFRANGE> |     |     | Specifiestheportidentifierrange. |
| --------- | --- | --- | -------------------------------- |
brief
Showsbriefinfointabularformat.
| physical |     |     | Showsthephysicalconnectioninfointabularformat. |
| -------- | --- | --- | ---------------------------------------------- |
extended
Showsadditionalstatistics.
| non-zero |     |     | Showsonlynonzerostatistics. |
| -------- | --- | --- | --------------------------- |
LAG
ShowsLAGinterfaceinformation.
| LOOPBACK |     |     | Showsloopbackinterfaceinformation. |
| -------- | --- | --- | ---------------------------------- |
TUNNEL
Showstunnelinterfaceinformation.
| VLAN |     |     | ShowsVLANinterfaceinformation. |
| ---- | --- | --- | ------------------------------ |
<LAG-ID>
SpecifiestheLAGnumber.Range:1-256
| <LOOPBACK-ID> |     |     | SpecifiestheLOOPBACKnumber.Range:0-255 |
| ------------- | --- | --- | -------------------------------------- |
<TUNNEL-ID>
SpecifiesthetunnelID.Range:1-255
| <VLAN-ID> |     |     | SpecifiestheVLANID.Range:1-4094 |
| --------- | --- | --- | ------------------------------- |
VXLAN
ShowstheVXLANinterfaceinformation.
| <VXLAN-ID> |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |
| ---------- | --- | --- | ---------------------------------------------- |
Examples
63
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

Thefollowingexampleshowswhentheinterfaceisconfiguredasaroute-onlyport:
| switch#           | show interface |        | 1/1/1        |        |                   |                 |           |     |     |
| ----------------- | -------------- | ------ | ------------ | ------ | ----------------- | --------------- | --------- | --- | --- |
| Interface         | 1/1/1          | is up  |              |        |                   |                 |           |     |     |
| Admin state       | is             | up     |              |        |                   |                 |           |     |     |
| Link state:       | up             | for    | 2 days       | (since | Sun               | Jun 21 05:30:22 | UTC 2020) |     |     |
| Link transitions: |                | 1      |              |        |                   |                 |           |     |     |
| Description:      |                | backup | data         | center | link              |                 |           |     |     |
| Hardware:         | Ethernet,      |        | MAC Address: |        | 70:72:cf:fd:e7:b4 |                 |           |     |     |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | none |             |     |            |         |     |     |       |         |
| ---------------- | ---- | ----------- | --- | ---------- | ------- | --- | --- | ----- | ------- |
| Speed 1000       | Mb/s |             |     |            |         |     |     |       |         |
| Auto-negotiation |      | is          | on  |            |         |     |     |       |         |
| Flow-control:    |      | off         |     |            |         |     |     |       |         |
| Error-control:   |      | off         |     |            |         |     |     |       |         |
| MDI mode:        | MDIX |             |     |            |         |     |     |       |         |
| L3 Counters:     |      | Rx Enabled, |     | Tx Enabled |         |     |     |       |         |
| Rate collection  |      | interval:   |     | 300        | seconds |     |     |       |         |
| Rates            |      |             |     |            | RX      |     | TX  | Total | (RX+TX) |
------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| ----------- | --- | --- | --- | --- | ---- | --- | ---- | --- | ----- |
| KPkts /     | sec |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Unicast     |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Multicast   |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Broadcast   |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Utilization | %   |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Statistics  |     |     |     |     | RX   |     | TX   |     | Total |
------------- -------------------- -------------------- --------------------
| Packets      |     |     |     |     | 0   |     | 0   |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast      |     |     |     |     | 0   |     | 0   |     | 0   |
| Multicast    |     |     |     |     | 0   |     | 0   |     | 0   |
| Broadcast    |     |     |     |     | 0   |     | 0   |     | 0   |
| Bytes        |     |     |     |     | 0   |     | 0   |     | 0   |
| Jumbos       |     |     |     |     | 0   |     | 0   |     | 0   |
| Dropped      |     |     |     |     | 0   |     | 0   |     | 0   |
| Filtered     |     |     |     |     | 0   |     | 0   |     | 0   |
| Pause Frames |     |     |     |     | 0   |     | 0   |     | 0   |
| L3 Packets   |     |     |     |     | 0   |     | 0   |     | 0   |
| L3 Bytes     |     |     |     |     | 0   |     | 0   |     | 0   |
| Errors       |     |     |     |     | 0   |     | 0   |     | 0   |
| CRC/FCS      |     |     |     |     | 0   |     | n/a |     | 0   |
| Collision    |     |     |     |     | n/a |     | 0   |     | 0   |
| Runts        |     |     |     |     | 0   |     | n/a |     | 0   |
| Giants       |     |     |     |     | 0   |     | n/a |     | 0   |
| Other        |     |     |     |     | 0   |     | 0   |     | 0   |
Whentheinterfaceiscurrentlylinkedatadownshiftedspeed:
| switch(config-if)# |       | show  | interface |     | 1/1/1 |     |     |     |     |
| ------------------ | ----- | ----- | --------- | --- | ----- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is up |           |     |       |     |     |     |     |
...
| Auto-negotiation |     | is  | on with | downshift |     | active |     |     |     |
| ---------------- | --- | --- | ------- | --------- | --- | ------ | --- | --- | --- |
WhentheinterfaceisshutdownduringaVSX split:
IP-SLA|64

|     | switch(config-if)# |       | show     | interface | 1/1/1 |     |     |     |
| --- | ------------------ | ----- | -------- | --------- | ----- | --- | --- | --- |
|     | Interface          | 1/1/1 | is down  |           |       |     |     |     |
|     | Admin state        | is    | up       |           |       |     |     |     |
|     | State information: |       | Disabled | by        | VSX   |     |     |     |
Link state: down for 3 days (since Tue Mar 16 05:20:47 UTC 2021)
|     | Link transitions: |     | 0   |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
Description:
|     | Hardware: | Ethernet, | MAC | Address: | 04:09:73:62:90:e7 |     |     |     |
| --- | --------- | --------- | --- | -------- | ----------------- | --- | --- | --- |
MTU 1500
|     | Type SFP+DAC3 |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Full-duplex
|     | qos trust        | none            |                 |     |         |     |       |         |
| --- | ---------------- | --------------- | --------------- | --- | ------- | --- | ----- | ------- |
|     | Speed 0          | Mb/s            |                 |     |         |     |       |         |
|     | Auto-negotiation |                 | is off          |     |         |     |       |         |
|     | Flow-control:    |                 | off             |     |         |     |       |         |
|     | Error-control:   |                 | off             |     |         |     |       |         |
|     | VLAN Mode:       | native-untagged |                 |     |         |     |       |         |
|     | Native           | VLAN:           | 1               |     |         |     |       |         |
|     | Allowed          | VLAN            | List: 1502-1505 |     |         |     |       |         |
|     | Rate collection  |                 | interval:       | 300 | seconds |     |       |         |
|     | Rate             |                 |                 |     | RX      | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
|     | Mbits /     | sec |     |     | 0.00 | 0.00 |     | 0.00  |
| --- | ----------- | --- | --- | --- | ---- | ---- | --- | ----- |
|     | KPkts /     | sec |     |     | 0.00 | 0.00 |     | 0.00  |
|     | Unicast     |     |     |     | 0.00 | 0.00 |     | 0.00  |
|     | Multicast   |     |     |     | 0.00 | 0.00 |     | 0.00  |
|     | Broadcast   |     |     |     | 0.00 | 0.00 |     | 0.00  |
|     | Utilization |     |     |     | 0.00 | 0.00 |     | 0.00  |
|     | Statistic   |     |     |     | RX   | TX   |     | Total |
---------------- -------------------- -------------------- --------------------
|                | Packets      |             |         |     | 0            | 0   |     | 0   |
| -------------- | ------------ | ----------- | ------- | --- | ------------ | --- | --- | --- |
|                | Unicast      |             |         |     | 0            | 0   |     | 0   |
|                | Multicast    |             |         |     | 0            | 0   |     | 0   |
|                | Broadcast    |             |         |     | 0            | 0   |     | 0   |
|                | Bytes        |             |         |     | 0            | 0   |     | 0   |
|                | Jumbos       |             |         |     | 0            | 0   |     | 0   |
|                | Dropped      |             |         |     | 0            | 0   |     | 0   |
|                | Pause Frames |             |         |     | 0            | 0   |     | 0   |
|                | Errors       |             |         |     | 0            | 0   |     | 0   |
|                | CRC/FCS      |             |         |     | 0            | n/a |     | 0   |
|                | Collision    |             |         |     | n/a          | 0   |     | 0   |
|                | Runts        |             |         |     | 0            | n/a |     | 0   |
|                | Giants       |             |         |     | 0            | n/a |     | 0   |
| Command        |              | History     |         |     |              |     |     |     |
| Release        |              |             |         |     | Modification |     |     |     |
| 10.07orearlier |              |             |         |     | --           |     |     |     |
| Command        |              | Information |         |     |              |     |     |     |
| Platforms      |              | Command     | context |     | Authority    |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
65
| AOS-CX10.09MonitoringGuide| |     |     | (83xxSwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- |

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show interface |                       | downshift-enable |                  |     |
| -------------- | --------------------- | ---------------- | ---------------- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |                  | downshift-enable |     |
Description
Displaysspeeddownshiftinformation,includingtheinterfacespeedstatusandconfiguration.
| Parameter |     |     | Description                      |     |
| --------- | --- | --- | -------------------------------- | --- |
| <IFNAME>  |     |     | Specifiesainterfacename.         |     |
| <IFRANGE> |     |     | Specifiestheportidentifierrange. |     |
Examples
Showingautomaticdownshiftinformation:
| switch(config-if)# |     | show interface | downshift-enable |     |
| ------------------ | --- | -------------- | ---------------- | --- |
-------------------------------------------------
|      | Downshift |          | Speed  |          |
| ---- | --------- | -------- | ------ | -------- |
| Port | Enabled   | | Active | Status | | Config |
-------------------------------------------------
| 1/1/1 | yes | yes | 100M-FDx | auto     |
| ----- | --- | --- | -------- | -------- |
| 1/1/2 | yes | no  | 1G       | auto     |
| 1/1/3 | yes | no  | 100M-FDx | 100M-FDx |
| 1/1/4 | no  | no  | --       | auto     |
Showingautomaticdownshiftinformationonperinterface:
| switch(config-if)# |     | show interface | 1/1/2 | downshift-enable |
| ------------------ | --- | -------------- | ----- | ---------------- |
-------------------------------------------------
|      | Downshift |          | Speed  |          |
| ---- | --------- | -------- | ------ | -------- |
| Port | Enabled   | | Active | Status | | Config |
-------------------------------------------------
| 1/1/2          | yes         | no  | 1G           | auto |
| -------------- | ----------- | --- | ------------ | ---- |
| Command        | History     |     |              |      |
| Release        |             |     | Modification |      |
| 10.07orearlier |             |     | --           |      |
| Command        | Information |     |              |      |
IP-SLA|66

| Platforms | Command | context | Authority                                            |     |
| --------- | ------- | ------- | ---------------------------------------------------- | --- |
|           | config  |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show running-config |           | interface             |     |     |
| ------------------- | --------- | --------------------- | --- | --- |
| show running-config | interface | [<IFNNAME>|<IFRANGE>] |     |     |
show running-config interface [lag | loopback | tunnel | vlan ] [<ID>]
| show running-config | interface | vxlan | <ID> |     |
| ------------------- | --------- | ----- | ---- | --- |
Description
Displaysactiveconfigurationsofvariousswitchinterfaces.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IFNAME>
Specifiesainterfacename.
| <IFRANGE> |     |     | Specifiestheportidentifierrange. |     |
| --------- | --- | --- | -------------------------------- | --- |
LAG
SpecifiesLAGinterfaceinformation
| LOOPBACK |     |     | Specifiesloopbackinterfaceinformation. |     |
| -------- | --- | --- | -------------------------------------- | --- |
TUNNEL
Specifiestunnelinterfaceinformation.
| VLAN |     |     | SpecifiesVLANinterfaceinformation. |     |
| ---- | --- | --- | ---------------------------------- | --- |
<LAG-ID>
SpecifiestheLAGnumber.Range:1-256.
| <LOOPBACK-ID> |     |     | SpecifiestheLOOPBACKnumber.Range:0-255. |     |
| ------------- | --- | --- | --------------------------------------- | --- |
<TUNNEL-ID>
SpecifiesthetunnelID.Range:1-255.
| <VLAN-ID> |     |     | SpecifiestheVLANID.Range:1-4094. |     |
| --------- | --- | --- | -------------------------------- | --- |
VXLAN
SpecifiestheVXLANinterfaceinformation.
| <VXLAN-ID> |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1. |     |
| ---------- | --- | --- | ----------------------------------------------- | --- |
Examples
Showing1/1/2interfaceconfiguration:
| switch(config-if)# |       | show running-config | interface | 1/1/2 |
| ------------------ | ----- | ------------------- | --------- | ----- |
| interface          | 1/1/2 |                     |           |       |
| no shutdown        |       |                     |           |       |
| description        | DC-23 |                     |           |       |
exit
Showingloopbackinterfacesconfigured:
67
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| switch(config-if)# |             |          | show running-config |     | interface | loopback |
| ------------------ | ----------- | -------- | ------------------- | --- | --------- | -------- |
| interface          |             | loopback | 1                   |     |           |          |
|                    | description |          | lb interface        | 1   |           |          |
exit
| interface |             | loopback | 2            |     |     |     |
| --------- | ----------- | -------- | ------------ | --- | --- | --- |
|           | description |          | lb interface | 2   |     |     |
exit
Showingloopbackinterfacesnotconfigured:
| switch(config-if)# |             |            | show running-config |                                                      | interface | loopback |
| ------------------ | ----------- | ---------- | ------------------- | ---------------------------------------------------- | --------- | -------- |
| No                 | loopback    | interfaces | configured.         |                                                      |           |          |
| Command            | History     |            |                     |                                                      |           |          |
| Release            |             |            |                     | Modification                                         |           |          |
| 10.07orearlier     |             |            |                     | --                                                   |           |          |
| Command            | Information |            |                     |                                                      |           |          |
| Platforms          |             | Command    | context             | Authority                                            |           |          |
|                    |             | config     |                     | OperatorsorAdministratorsorlocalusergroupmemberswith |           |          |
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
IP-SLA|68

Chapter 9

Mirroring

Mirroring

Mirroring allows you to replicate all traffic arriving and/or leaving the selected system interfaces. This
data can be used for collection or analysis.

The traffic replicated using mirroring can be sent to a separate interface on the same switch as the
traffic source for analysis or inspection. Such a collection of interfaces and settings is called a mirror
session.

A mirror session can be configured with many traffic sources but only a single output, or destination. In
the initial configuration, the mirror session is disabled. You have enable the feature to start the
replication.

Care must be taken in choosing the number and rates of sources to avoid over-saturating a session destination. A

mirror session with multiple 10G sources can overwhelm a single 10G destination and important data may be lost.

Mirroring statistics and sFlow
Mirror statistics are reset for a mirror-to-CPU session when an interface is added or removed from a
LAG that is a source interface in the mirror session.

Mirroring and sFlow configuration on the same port is supported.

Limitations
The following limitations apply when configuring multiple mirroring sessions on a switch:

n CPU generated packets egressing on a routed L3 interface will not be mirrored to the destination

port.

n Untagged egress packets that get mirrored will have the native VLAN tag in the mirrored packet.
These extra bytes can cause traffic loss at the mirror destination when running line rate traffic.

n True egress mirroring is not supported on 832x platforms. Egress mirroring takes place at the

ingress. The packets that may get dropped at the egress might also have been mirrored at ingress.
Traffic will be mirrored even before the policy actions are processed at the egress.

n Packets mirrored to CPU from a Layer-3 Route Only Port (ROP) will have a VLAN tag with the VLAN ID

set to the internal VLAN ID assigned to that port.

n 832x platforms have 4 mirror ASIC resources that can be used among the different mirror sessions.
Each direction in a mirror session will consume 1 mirror ASIC resource. Hence, a user can have up to
4 unidirectional mirror sessions or 2 bi-directional mirror sessions active at any given time. If there
are no mirror ASIC resources available when attempting to enable a mirror session, the 'Operation
Status' field of show mirror command for session ID will have the status set to 'platform_session_
limit_reached.'

AOS-CX 10.09 Monitoring Guide | (83xx Switch Series)

69

n Themirrordestinationportamongtheactivemirrorsessionsmustbeuniquei.e.ifaninterfaceis
configuredasasourceordestinationinanactivemirrorsession,thesameportcannotbeusedasa
destinationinanotheractivemirrorsession.
n Theinterface/LAGusedtotransmitERSPANpacketscannotbeasourceinanymirrorsession.
n Theinterface/LAGusedtotransmitERSPANpacketsmustbeuniqueperERSPANmirrorsession.Ifa
changeintheL3topologycausesmultipleERSPANmirrorsessionstousethesameegress
interface/LAGtotransmittheERSPANpackets,thenonlyonesessionwillwork.Theothersession(s)
willgointoanerrorstate.
| Mirroring | commands |     |     |
| --------- | -------- | --- | --- |
clear mirror
| clear mirror | [all | <SESSION-ID>] |     |     |
| ------------ | -------------------- | --- | --- |
Description
Clearsthemirrorstatisticsforallconfiguredmirrorsessionsoraspecifiedsession
| Parameter |     |     | Description                     |
| --------- | --- | --- | ------------------------------- |
| all       |     |     | Specifiesallconfiguredsessions. |
<SESSION-ID>
Specifiesanumericidentifierforthesession.Range:1to4
Examples
Clearingmirrorstatisticsforallconfiguredmirrorsessions:
| switch# | clear mirror | all |     |
| ------- | ------------ | --- | --- |
Clearingmirrorstatisticsformirrorsession1:
| switch#             | clear mirror | 1       |              |
| ------------------- | ------------ | ------- | ------------ |
| Command History     |              |         |              |
| Release             |              |         | Modification |
| 10.07orearlier      |              |         | --           |
| Command Information |              |         |              |
| Platforms           | Command      | context | Authority    |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
comment
comment <COMMENT>
Mirroring|70

no comment

Description

Specifies a comment for the mirroring session.

When used in mirror endpoint command context, specifies a comment for the mirror endpoint.

The no form of this command removes the comment.

Parameter

<COMMENT>

Usage

Description

A comment string of up to 64 characters composed of letters,
numbers, underscores, dashes, spaces, and periods.

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

switch(config-mirror-endpoint-test)# comment Monitor statistics on each endpoint
interfaces

Command History

Release

10.07 or earlier

Command Information

Modification

--

AOS-CX 10.09 Monitoring Guide | (83xx Switch Series)

71

| Platforms | Command | context |     |     | Authority |     |     |     |
| --------- | ------- | ------- | --- | --- | --------- | --- | --- | --- |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
|     | config-mirror-endpoint |     |     |     | executionrightsforthiscommand. |     |     |     |
| --- | ---------------------- | --- | --- | --- | ------------------------------ | --- | --- | --- |
copy tcpdump-pcap
| copy tcpdump-pcap | <FILE-NAME> | <REMOTE-URL> |     |     |     |     |     |     |
| ----------------- | ----------- | ------------ | --- | --- | --- | --- | --- | --- |
Description
Savespacketcapturefilestoexternalstorage.
| Parameter   |     |     |     | Description                          |     |     |     |     |
| ----------- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
| <FILE-NAME> |     |     |     | Specifiesthepacketcapturefiletosave. |     |     |     |     |
<REMOTE-URL>
Specifiestheexternalstoragetowhichthepacketcapturefilewill
besaved.
Usage
Onlyfourfilescanbesavedatanypointontheswitch.Packetcapturefilesarenotsavedafterafailover
| orreboot.Viewalistofsavedfilesusingdiag |     |     |     | utilities | list-files. |     |     |     |
| --------------------------------------- | --- | --- | --- | --------- | ----------- | --- | --- | --- |
Examples
Savingmy_capture_file.pcaptosftp://root@10.0.0.2/file.pcap:
switch# copy tcpdump-pcap my_capture_file.pcap sftp://root@10.0.0.2/file.pcap
| root@10.0.0.2's      | passowrd:            |         |           |                   |     |          |           |       |
| -------------------- | -------------------- | ------- | --------- | ----------------- | --- | -------- | --------- | ----- |
| Connected            | to 10.0.0.2.         |         |           |                   |     |          |           |       |
| sftp > put           | my_capture_file.pcap |         | file.pcap |                   |     |          |           |       |
| Uploading            | my_capture_file.pcap |         | to        | /root/file.pcap   |     |          |           |       |
| my_capture_file.pcap |                      |         |           |                   |     | 100% 156 | 219.8KB/s | 00:00 |
| Copied               | successfuly.         |         |           |                   |     |          |           |       |
| Command              | History              |         |           |                   |     |          |           |       |
| Release              |                      |         |           | Modification      |     |          |           |       |
| 10.08                |                      |         |           | Commandintroduced |     |          |           |       |
| Command              | Information          |         |           |                   |     |          |           |       |
| Platforms            | Command              | context |           | Authority         |     |          |           |       |
8320 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     | forthiscommand. |     |     |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- | --- | --- |
8360
copy tshark-pcap
| copy tshark-pcap | <REMOTE-URL> | [vrf | <VRF-NAME>] |     |     |     |     |     |
| ---------------- | ------------ | ---- | ----------- | --- | --- | --- | --- | --- |
Mirroring|72

Description
CopiesthetsharkcapturedatatoafileonaTFTPorSFTPserver.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<REMOTE-URL> SpecifiesthecapturefileonaremoteTFTPorSFTPserver.The
URLsyntaxis:
{tftp://|sftp://<USER>@}{<IP>|<HOST>}[:<PORT>]
[;blocksize=<SIZE>]/<FILE>
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |     |     |     |
| -------------- | --- | --- | --------------------------------------- | --- | --- | --- |
Example
CopyingthecapturedatatoafileonSFTPserver10.0.0.2:
| switch#         | copy tshark-pcap | sftp://root@10.0.0.2/file.pcap |              |          |           |       |
| --------------- | ---------------- | ------------------------------ | ------------ | -------- | --------- | ----- |
| root@10.0.0.2's | password:        |                                |              |          |           |       |
| Connected       | to 10.0.0.2.     |                                |              |          |           |       |
| sftp> put       | packets.pcap     | file.pcap                      |              |          |           |       |
| Uploading       | packets.pcap     | to /root/file.pcap             |              |          |           |       |
| packets.pcap    |                  |                                |              | 100% 156 | 219.8KB/s | 00:00 |
| Copied          | successfully.    |                                |              |          |           |       |
| Command         | History          |                                |              |          |           |       |
| Release         |                  |                                | Modification |          |           |       |
| 10.07orearlier  |                  |                                | --           |          |           |       |
| Command         | Information      |                                |              |          |           |       |
| Platforms       | Command          | context                        | Authority    |          |           |       |
8320 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
| destination    | cpu |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- |
| destination    | cpu |     |     |     |     |     |
| no destination | cpu |     |     |     |     |     |
Description
ThecommandcausesthemirrorsessiontotransmitmirroredpacketstotheswitchCPU.This
destinationmaybeconfiguredformultiplesessions,howeveronlyonesuchconfiguredsessionmaybe
activeatagiventime.
ThediagnosticutilityTsharkmaybeusedtoviewandcapturepacketstransmittedtotheCPUthrough
thisroute.Ctrl+CmustbeenteredtoterminateaTsharkcapturesession.Moredetailscanbefoundin
theSupportabilityGuide.
ThenoformofthiscommandwillimmediatelystopsmirroringtraffictotheCPU,butwillnotremove
anysourcesfromthemirrorconfiguration.
73
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- |

Examples
ConfiguringamirrorsessionwithCPUasthedestination.
switch#
config
| switch(config)#          |     | mirror | session     | 1   |     |     |
| ------------------------ | --- | ------ | ----------- | --- | --- | --- |
| switch(config-mirror-1)# |     |        | destination |     | cpu |     |
Removingthedestinationentirely.
| switch(config-mirror-1)# |             |     | no      | destination |              | cpu       |
| ------------------------ | ----------- | --- | ------- | ----------- | ------------ | --------- |
| Command                  | History     |     |         |             |              |           |
| Release                  |             |     |         |             | Modification |           |
| 10.07orearlier           |             |     |         |             | --           |           |
| Command                  | Information |     |         |             |              |           |
| Platforms                | Command     |     | context |             |              | Authority |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| destination    | interface |     |                             |     |     |     |
| -------------- | --------- | --- | --------------------------- | --- | --- | --- |
| destination    | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |     |     |
| no destination | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |     |     |
Description
Configuresthespecifiedinterfaceasthedestinationofthemirroredtraffic.
Thenoformofthiscommandimmediatelydisablesthemirroringsessionandremovesthespecified
destinationinterfacefromtheconfiguration.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<INTERFACE-ID>
Specifiesainterface.Format:member/slot/port.
| <LAG-NAME> |     |     |     |     | SpecifiesaLAG(linkaggregationgroup)identifier. |     |
| ---------- | --- | --- | --- | --- | ---------------------------------------------- | --- |
Usage
Supportedmirrordestinations:Layer2orLayer3Ethernetports,LAGs,orCPUasaMirrorDestination.
AportthatisalreadyamemberofaLAGisnotavalidmirrordestination.
Configuringadifferentdestinationinterfaceinanenabledmirroringsessioncausesallmirroredtraffic
tousethenewdestinationinterface.Thisactionmightcauseatemporarysuspensionofmirrored
sourcetrafficduringthereconfiguration.
Examples
Configuringamirroringsessionandaddinganinterfaceasadestination:
Mirroring|74

| switch(config)# |     | mirror | session | 1   |     |     |     |
| --------------- | --- | ------ | ------- | --- | --- | --- | --- |
switch(config-mirror-1)#
|     |     |     | destination |     | interface |     | 1/1/1 |
| --- | --- | --- | ----------- | --- | --------- | --- | ----- |
Replacingtheexistingdestinationwithdifferentinterface:
| switch(config-mirror-1)# |     |     | destination |     | interface |     | 1/1/12 |
| ------------------------ | --- | --- | ----------- | --- | --------- | --- | ------ |
Removingadestination:
| switch(config-mirror-1)# |             |     | no      | destination |              | interface | 1/1/12 |
| ------------------------ | ----------- | --- | ------- | ----------- | ------------ | --------- | ------ |
| Command                  | History     |     |         |             |              |           |        |
| Release                  |             |     |         |             | Modification |           |        |
| 10.07orearlier           |             |     |         |             | --           |           |        |
| Command                  | Information |     |         |             |              |           |        |
| Platforms                | Command     |     | context |             |              | Authority |        |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| destination       | tunnel |               |            |        |                    |     |     |
| ----------------- | ------ | ------------- | ---------- | ------ | ------------------ | --- | --- |
| destination       | tunnel | <TUNNEL-IPV4> |            | source | <SOURCE-IPv4-ADDR> |     |     |
| dscp <DSCP-VALUE> |        | vrf           | <VRF-NAME> |        |                    |     |     |
| no destination    | tunnel |               |            |        |                    |     |     |
Description
Specifiesthetunnelwhereallmirroredtrafficforthesessionistransmitted.Onlyonetunneldestination
isallowedpersession.
Youmayconfiguremultiplemirrorsessionswiththesamesource/destinationIPaddresspair,however,
onlyoneofthosesessionssharingthesamesource/destinationIPaddresspaircanbeenabledata
giventime.
ERSPANisnotsupportedleavingtheswitchbytheOOBport.IfVRFmanagementisconfiguredforan
ERSPANsession,thesessionwillbein"mirror_err_tunnel_oob_port_not_supported"operationstatus.
ERSPANisnotsupportedleavingtheswitchencapsulatedwithinanothertunnel(e.g.GREIPv4).When
thepathtothedestinationIPaddresswillleaveviaatunnel,thesessionwillbein"tunnel_route_
resolution_not_populated"operationstatus.
Theinterface/LAGusedtotransmitERSPANpacketsshouldnotbeasourceinthesamemirrorsession.
Thenoformofthiscommandwillceasetheuseofthetunnelanddisablethesession.
75
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

Parameter

Description

<TUNNEL-IPV4-ADDR>

<SOURCE-IPv4-ADDR>

<DSCP-VALUE>

Specifies the tunnel address in IPv4 format (x.x.x.x), where x is
a decimal number from 0 to 255.

Specifies the source address in IPv4 format (x.x.x.x), where x is
a decimal number from 0 to 255.

Specifies the DSCP value to be carried within the DS field of
ERSPAN packet header. Range: 0 to 63. Default: 0.

<VRF-NAME>

Specifies a VRF name. Default: default.

Examples

Creating a Mirror Session and adding tunnel destination, source, dscp, and VRF:

switch# config
switch(config)# mirror session 1
switch(config-mirror-1)# destination tunnel 1.1.1.1 source 2.2.2.2 dscp 10 vrf
default

Replacing the existing tunnel destination:

switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 10 vrf
default

Replacing the existing destination with a different DSCP value:

switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 2 vrf
default

Replacing the existing destination with a different VRF:

switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 2 vrf
newvrf

Removing the destination:

switch(config-mirror-1)# no destination tunnel

Command History

Release

10.07 or earlier

Command Information

Modification

--

Mirroring | 76

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
8320 config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | ------------------------------ | --- |
8360
diagnostic
diagnostic
| diag utilities | tshark | [file]        |     |     |
| -------------- | ------ | ------------- | --- | --- |
| diag utilities | tshark | [delete-file] |     |     |
Description
Capturespacketsfromamirror-to-cpusession,andsavethemostrecent32MBtopcapfilewhichcan
thenbecopiedandanalyzed.Whencapturingamirror-to-cpusessiontoafile,packetswillnotbe
dumpedtotheconsole.
Thediagnosticcommandmustbeenteredpriortothediag utilities tsharkcommand.
Usethedelete-fileformofthiscommandtodeletethemostrecentcapturefile.
Sincefileanddelete-fileareoptional,thebehaviorofthebasecommanddiag utilities tshark
doesnotsaveanythingtoafile,andinsteaddumpsthetsharksessiontotheconsoleuntilCTRL + cis
entered.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
file
Savescapturedpacketstoatemporaryfile.
| delete-file |     | Deletesthemostrecentcapturedfile. |     |     |
| ----------- | --- | --------------------------------- | --- | --- |
Example
Performingdiagnostic:
| switch#        | diagnostic          |                     |              |            |
| -------------- | ------------------- | ------------------- | ------------ | ---------- |
| switch#        | diagnostic          | utilities tshark    | file         |            |
| Inspecting     | traffic             | mirrored to the CPU | until Ctrl-C | is entered |
| ^CEnding       | traffic inspection. |                     |              |            |
| Command        | History             |                     |              |            |
| Release        |                     | Modification        |              |            |
| 10.07orearlier |                     | --                  |              |            |
| Command        | Information         |                     |              |            |
77
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| diag utilities | tcpdump |     |     |
| -------------- | ------- | --- | --- |
diag utilities tcpdump [command <TEXT> | delete file <FILE-NAME> | list-files |
vrf <VRF-NAME> | count <COUNT-NUM> | proto <PROTO-NUM> | host-ip <IP-ADDR> | source-ip
<IP-ADDR> | destination-ip <IP-ADDR> | host-port <PORT> | source-port <PORT> |
destination-port <PORT> | verbosity <LEVEL> | print <DATA> | ethernet-type <ETH-NUM>]
Description
Capturestrafficreceivedortransmittedoveranetwork.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
command <TEXT> Capturespacketsbasedonaspecifiedtcpdumpcommandstring.
| delete file | <FILE-NAME> |     | Deletesspecifiedtcpdumplistfiles.               |
| ----------- | ----------- | --- | ----------------------------------------------- |
| list-files  |             |     | Listsallthetcpdumpcapturefilessavedonthedevice. |
vrf <VRF-NAME> CapturespacketsonthespecifiedVRF.IfnoVRF isnamed,the
defaultisused.
count <COUNT-NUM> Runsthetcpdumpcommanduntilthespecifiednumberof
packetsarecaptured.Range: 1-2147483647.
proto <PROTO-NUM> CapturespacketsofaparticulartypebasedonIPprotocol
number.Range: 0-255.
| host-ip <IP-ADDR> |     |     |     |
| ----------------- | --- | --- | --- |
CapturespacketsmatchingwiththesourceordestinationIP
address.
source-ip <IP-ADDR> CapturespacketsfromthespecifiedIPaddress.
| destination-ip | <IP-ADDR> |     |     |
| -------------- | --------- | --- | --- |
CapturespacketssenttothespecifiedIPaddress.
host-port <PORT> Capturespacketsmatchingwiththesourceordestinationport.
| source-port | <PORT> |     |     |
| ----------- | ------ | --- | --- |
CapturespacketsfromthespecifiedIPport.
destination-port <PORT> CapturespacketssenttothespecifiedIPport.
| verbosity | <LEVEL> |     |     |
| --------- | ------- | --- | --- |
Capturespacketsofthespecifiedverbosity.Range: level1-level4.If
noverbosityisspecified,thedefaultislevel1.
print <DATA> Capturesthedataofeachpacket.Themaximumis262144bytes
ethernet-type <ETH-NUM> Capturespacketsbasedontheparticularethernettype.Range: 0-
65535.
Usage
Whenusingthecommandoption,theonlytrafficcapturedwillbepacketsthathavebeenmirroredto
n
theCPU.
Mirroring|78

n When using the command option, command line sanitization is performed to prevent options that may

cause harm or security issues. The following options are blocked:

o -i/--interface

o -Z

o -B/--buffer-size

o -C

o -W

o -Z/--relinquish privileges

n Non-word operators such as "&" or "|" are not allowed. Use boolean keywords such as "and," "or,"

and "not."

n When using command -r to read a file, do not provide any directory path characters. Use list-files

command to get the list of file names currently saved on the device, and then use those file names.

n A total of four files can be saved at any given point on the device. Packet capture files are not saved

after a failover or reboot, but can be saved to external storage using the copy tcpdump-pcap
command.

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
reading from file /tmp/tcpdump/my_capture_file1.pcap, link-type EN10MB (Ethernet)
11:59:34.047867 IP6 localhost.40318 > localhost.ntp: NTPv2, Reserved, length

1

12

0x0000:
0x0010:
0x0020:
0x0030:
0x0040:

0000 0304 0006 0000 0000 0000 0000 86dd
600a 7e47 0014 1140 0000 0000 0000 0000
0000 0000 0000 0001 0000 0000 0000 0000
0000 0000 0000 0001 9d7e 007b 0014 0027
1601 0001 0000 0000 0000 0000

................
`.~G...@........
................
.........~.{...'
............

2

11:59:34.047915 IP6 localhost.ntp > localhost.40318: NTPv2, Reserved, length

12

0x0000:
0x0010:
0x0020:
0x0030:
0x0040:

0000 0304 0006 0000 0000 0000 0000 86dd
6b8d 23c5 0014 1140 0000 0000 0000 0000
0000 0000 0000 0001 0000 0000 0000 0000
0000 0000 0000 0001 007b 9d7e 0014 0027
d681 0001 c016 0000 0000 0000

................
k.#....@........
................
.........{.~...'

Removing my_capture_file.pcap:

AOS-CX 10.09 Monitoring Guide | (83xx Switch Series)

79

switch# diag utilities tcpdump delete-file my_capture_file.pcap
| Successfully |             | removed file |                   |     |
| ------------ | ----------- | ------------ | ----------------- | --- |
| Command      | History     |              |                   |     |
| Release      |             |              | Modification      |     |
| 10.08        |             |              | Commandintroduced |     |
| Command      | Information |              |                   |     |
| Platforms    | Command     | context      | Authority         |     |
8320 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
| disable | (mirror | session) |     |     |
| ------- | ------- | -------- | --- | --- |
disable
Description
Disablesthemirroringsessionspecifiedbythecurrentcommandcontext.
Usage
Bydefault,mirroringsessionsaredisabled.
Whenamirroringsessionisdisabled,theshow mirrorcommandforthatsessionIDshowsanAdmin
| StatusofdisableandanOperation |     |     | Statusofdisabled. |     |
| ----------------------------- | --- | --- | ----------------- | --- |
Example
Disablingamirroringsession:
| switch(config)#          |             | mirror session | 3            |           |
| ------------------------ | ----------- | -------------- | ------------ | --------- |
| switch(config-mirror-3)# |             | disable        |              |           |
| Command                  | History     |                |              |           |
| Release                  |             |                | Modification |           |
| 10.07orearlier           |             |                | --           |           |
| Command                  | Information |                |              |           |
| Platforms                | Command     | context        |              | Authority |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| enable | (mirror | session) |     |     |
| ------ | ------- | -------- | --- | --- |
Mirroring|80

enable
Description
Enablesthemirroringsessionforthecurrentcommandcontext.
Usage
Bydefault,mirroringsessionsaredisabled.
Whenamirroringsessionisenabled,theshow mirrorcommandforthatsessionIDshowsanAdmin
| StatusofenableandanOperation |     |     | Statusofenabled. |     |
| ---------------------------- | --- | --- | ---------------- | --- |
IfsFlowisenabledonaninterfaceandamirroringsessionspecifiesthesameinterfaceasthesourceof
receivedtraffic(thesourceisconfiguredwithadirectionofrxorboth):
n Theattempttoenablethemirroringsessionfailsandanerrorisreturned.
Whenadding,removing,orchangingtheconfigurationofasourceinterfaceinanenabledmirroringsession,
packetsfromothermirrorsourcesusingthesamedestinationinterfacemightbeinterrupted.
Example
Configuringandenablingamirroringsession:
| switch(config)#          | mirror | session     | 3         |          |
| ------------------------ | ------ | ----------- | --------- | -------- |
| switch(config-mirror-3)# |        | source      | interface | 1/1/2 rx |
| switch(config-mirror-3)# |        | destination | interface | 1/1/3    |
switch(config-mirror-3)# comment Monitor router port ingress-only traffic
| switch(config-mirror-3)# |         | enable  |              |           |
| ------------------------ | ------- | ------- | ------------ | --------- |
| Command History          |         |         |              |           |
| Release                  |         |         | Modification |           |
| 10.07orearlier           |         |         | --           |           |
| Command Information      |         |         |              |           |
| Platforms                | Command | context |              | Authority |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| mirror session    |              |     |     |     |
| ----------------- | ------------ | --- | --- | --- |
| mirror session    | <SESSION-ID> |     |     |     |
| no mirror session | <SESSION-ID> |     |     |     |
Description
Createsamirroringsessionconfigurationcontextorentersanexistingmirroringsessionconfiguration
context.
Fromthiscontext,youcanentercommandstoconfigureandenableordisablethemirroringsession.
Thenoformofthiscommandremovesanexistingmirroringsessionfromtheconfiguration.
81
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Parameter    |     |     |     | Description                              |
| ------------ | --- | --- | --- | ---------------------------------------- |
| <SESSION-ID> |     |     |     | Specifiesthesessionidentifier.Range:1to4 |
Examples
| switch(config)# |     | mirror | session | 1   |
| --------------- | --- | ------ | ------- | --- |
switch(config-mirror-1)#
| switch(config)# |     | mirror | session | 3   |
| --------------- | --- | ------ | ------- | --- |
switch(config-mirror-3)#
switch(config)#
|     |     | no mirror | session | 1   |
| --- | --- | --------- | ------- | --- |
switch(config)#
| Command        | History     |     |         |              |
| -------------- | ----------- | --- | ------- | ------------ |
| Release        |             |     |         | Modification |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show mirror |                |     |            |     |
| ----------- | -------------- | --- | ---------- | --- |
| show mirror | [<SESSION-ID>] |     | [vsx-peer] |     |
Description
Showsinformationaboutmirroringsessions.If<SESSION-ID>isnotspecified,thenthecommand
showsasummaryofallconfiguredmirroringsessions.If<SESSION-ID>isspecified,thenthecommand
showsdetailedinformationaboutthespecifiedmirroringsession.
| Parameter    |     |     |     | Description                              |
| ------------ | --- | --- | --- | ---------------------------------------- |
| <SESSION-ID> |     |     |     | Specifiesthesessionidentifier.Range:1to4 |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
AdminStatusindicatestheconfiguredstatus.AdminStatusisoneofthefollowingvalues:
enable
Themirroringsessionisenabled.
disable
Themirroringsessionhasbeenconfiguredbutnotyetenabled,orhasbeendisabled.
Mirroring|82

OperationStatusindicatesthestatusofthemirroringsession.OperationStatusisoneofthefollowing
values:
dest_doesnt_exist
Theconfigureddestinationinterfaceisnotfoundinthesystem.Themirroringsessioncannotbeenabled.
destination_shutdown
Themirroringsessionisenabled,butthedestinationinterfaceisshutdown.Notrafficcanbemonitored.
disabled
Themirroringsessionisdisabledandisnotinanerrorcondition.
enabled
Themirroringsessionisenabled.
external/driver_error
AninternalASIChardwareerroroccurred.
hit_active_sessions_capacity
Themirroringsessioncouldnotbeenabledbecausethemaximumnumberofsupportedmirroringsessionsare
alreadyenabled.
internal_error
AninvalidparameterwaspassedtotheASICsoftwarelayer.
no_dest_configured
Themirroringsessiondoesnothaveadestinationinterfaceconfigured.
no_name_configured
Asoftwareerroroccurred.ThemirroringsessiondoesnothaveasessionIDinitsconfiguration.
null_mirror
Asoftwareerroroccurred.Thesessionobjectreferenceisinvalid.
out_of_memory
Thesystemisoutofmemory,rebootrecommended.
tunnel_route_resolution_not_populated
IfthedestinationtunnelIPaddressisnotreachable.
unknown_error
Anunexpectederroroccurred.
Examples
Showingsummaryinformationaboutallconfiguredmirroringsessions:
| switch#  | show mirror |           |        |     |
| -------- | ----------- | --------- | ------ | --- |
| ID Admin | Status      | Operation | Status |     |
--- ------------- ----------------------------------------------------
| 1 enable  |     | enabled        |     |     |
| --------- | --- | -------------- | --- | --- |
| 2 disable |     | disabled       |     |     |
| 3 disable |     | disabled       |     |     |
| 4 enable  |     | internal_error |     |     |
Showingdetailedinformationaboutasinglemirroringsession:
| switch#      | show mirror | 3        |                   |         |
| ------------ | ----------- | -------- | ----------------- | ------- |
| Mirror       | Session:    | 3        |                   |         |
| Admin        | Status:     | disable  |                   |         |
| Operation    | Status:     | disabled |                   |         |
| Comment:     | Monitor     | router   | port ingress-only | traffic |
| Source:      | interface   | 1/1/2    | rx                |         |
| Destination: | interface   | 1/1/3    |                   |         |
| Output       | Packets:    | 0        |                   |         |
| Output       | Bytes:      | 0        |                   |         |
switch#
| Command | History |     |     |     |
| ------- | ------- | --- | --- | --- |
83
AOS-CX10.09MonitoringGuide| (83xxSwitchSeries)

| Release        |             |         |         |     | Modification |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| source    | interface |             |     |               |             |               |
| --------- | --------- | ----------- | --- | ------------- | ----------- | ------------- |
| source    | interface | {<PORT-NUM> |     | | <LAG-NAME>} |             | [<DIRECTION>] |
| no source | interface | {<PORT-NUM> |     | |             | <LAG-NAME>} | [<DIRECTION>] |
Description
Configuresthespecifiedinterface(eitheranEthernetportoraLAG)asasourceoftraffictobemirrored.
Thenoformofthiscommandceasesmirroringtrafficfromthespecifiedsourceinterfaceandremoves
thesourceinterfacefromthemirroringsessionconfiguration.
| Parameter  |     |     |     |     | Description                                    |     |
| ---------- | --- | --- | --- | --- | ---------------------------------------------- | --- |
| <PORT-NUM> |     |     |     |     | Specifiesaphysicalportontheswitch.Usetheformat |     |
member/slot/port(forexample,1/3/1).
<LAG-NAME> SpecifiestheidentifierfortheLAG(linkaggregationgroup).
<DIRECTION> Selectsthedirectionoftraffictobemirroredfromthissource
interface.Thereisnodefaultforthisparameter.Validvaluesare
thefollowing:
| both |     |     |     |     | Mirrorbothtransmittedandreceivedpackets. |     |
| ---- | --- | --- | --- | --- | ---------------------------------------- | --- |
rx
Mirroronlyreceivedpackets.
| tx  |     |     |     |     | Mirroronlytransmittedpackets. |     |
| --- | --- | --- | --- | --- | ----------------------------- | --- |
Usage
Thereisalimitofsourceinterfacesineachdirectionofagivenmirrorsession:
| Switch |     | Source | interface |     | limit |     |
| ------ | --- | ------ | --------- | --- | ----- | --- |
| 8320   |     | 128    |           |     |       |     |
| 8325   |     | 128    |           |     |       |     |
| 8360   |     | 64     |           |     |       |     |
However,thereisapracticallimittotheamountoftrafficthatamirrordestinationcantransmit.For
example,mirroringsessionwithmultiple10Gsourcescanoverwhelmasingle10Gdestination.
Youcanconfigurethesamesourceinterfaceinmultiplemirroringsessions,ifrequired.
Mirroring|84

Whenadding,removing,orchangingtheconfigurationofasourceportinanenabledmirroringsession,packets
fromothermirrorsourcesusingthesamedestinationportmightbeinterrupted.
Examples
Configuringamirroredtrafficsourceinterface:
| switch(config-mirror-1)# |       | source | interface |          |       |
| ------------------------ | ----- | ------ | --------- | -------- | ----- |
| LAG-NAME                 | Enter | a LAG  | name. For | example, | lag10 |
| PORT-NUM                 | Enter | a port | number    |          |       |
Creatingamirroringsessionandconfiguringasourceinterfacetomirrorbothtransmittedandreceived
packets:
| switch(config)#          | mirror | session | 1         |     |            |
| ------------------------ | ------ | ------- | --------- | --- | ---------- |
| switch(config-mirror-1)# |        | source  | interface |     | 1/1/1 both |
Creatingasecondmirroringsessionandconfiguringtwosourceinterfaces.Oneportmirroringonly
transmittedpacketsandtheothermirroringbothtransmittedandreceivedpackets:
| switch(config)#          | mirror | session | 2         |     |            |
| ------------------------ | ------ | ------- | --------- | --- | ---------- |
| switch(config-mirror-2)# |        | source  | interface |     | 1/1/3 tx   |
| switch(config-mirror-2)# |        | source  | interface |     | 1/2/1 both |
Removingthefirstsourceinterface:
| switch(config-mirror-2)# |     | no  | source | interface | 1/2/3 |
| ------------------------ | --- | --- | ------ | --------- | ----- |
Configuringasourceinterfacetomirrorreceivedpacketsonly:
| switch(config-mirror-3)# |     | source | interface |     | 1/1/2 rx |
| ------------------------ | --- | ------ | --------- | --- | -------- |
Configuringasourceinterfacetomirrorbothtransmittedandreceivedpackets:
| switch(config-mirror-1)# |     | source | interface |     | 1/1/1 both |
| ------------------------ | --- | ------ | --------- | --- | ---------- |
ConfiguringaLAGassourceinterfacetomirrorbothtransmittedandreceivedpackets:
| switch(config-mirror-4)# |     | source | interface |     | lag1 both |
| ------------------------ | --- | ------ | --------- | --- | --------- |
Stoppingthemirroringofreceivedpacketsfromaconfiguredsourceinterface:
| switch(config-mirror-4)# |     | no  | source | interface | lag1 rx |
| ------------------------ | --- | --- | ------ | --------- | ------- |
Command History
85
AOS-CX10.09MonitoringGuide| (83xxSwitchSeries)

| Release        |             |         |         | Modification |           |
| -------------- | ----------- | ------- | ------- | ------------ | --------- |
| 10.07orearlier |             |         |         | --           |           |
| Command        | Information |         |         |              |           |
| Platforms      |             | Command | context |              | Authority |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| source | vlan |     |     |     |     |
| ------ | ---- | --- | --- | --- | --- |
Appliesonlyto8360.
Syntax
| source    | vlan | <VLAN-NUM> | {rx | tx | | both}    |     |
| --------- | ---- | ---------- | -------- | ---------- | --- |
| no source | vlan | <VLAN-NUM> | [rx |    | tx | both] |     |
Description
AddsorremovesVLANasasourceoftraffictobemirrored.MorethanonesourceVLANcanbe
configuredinamirrorsession.EachVLANmayspecifyitsowndirection.
ThenoversionofthecommandceasesmirroringtrafficfromthespecifiedsourceVLANandremoves
thesourcefromthemirrorconfiguration.
Thereisalimitof1024sourceVLANsineachdirectionofagivenmirrorsession.ThesameVLANcanbe
configuredasamirrorsourceformultiplesessions.
| Command | context |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- |
config
Parameters
<VLAN-NUM>
ConfiguredVLANnumber.
rx
Mirroronlyreceivedtraffic.
tx
Mirroronlytransmittedtraffic.
both
Mirrorbothreceivedandtransmittedtraffic.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
CreateamirrorsessionandaddVLAN10asasourceoftrafficinbothdirectionsonthatport.
| switch(config)# |     |     | mirror session | 1   |     |
| --------------- | --- | --- | -------------- | --- | --- |
switch(config-mirror-1)#
|     |     |     | source | vlan 10 | both |
| --- | --- | --- | ------ | ------- | ---- |
Mirroring|86

CreateasecondmirrorsessionandaddVLAN10asatransmitsourcesoftrafficandVLAN20inboth
receiveandtransmitdirections.
| switch(config)#          | mirror session | 2            |
| ------------------------ | -------------- | ------------ |
| switch(config-mirror-2)# | source         | vlan 10 tx   |
| switch(config-mirror-2)# | source         | vlan 20 both |
Reconfigurethesourceinsession2tobereceiveonlybyrespecifyingthesourceinterfaceconfiguration.
| switch(config-mirror-2)# | source | vlan 10 rx |
| ------------------------ | ------ | ---------- |
Fromthesecondsession,removethefirstsourceinterfaceentirelyandremovethetransmitdirection
fromtheothersothatmirroringonlyoccursinthereceivedirection.
| switch(config-mirror-2)# | no  | source vlan 10    |
| ------------------------ | --- | ----------------- |
| switch(config-mirror-2)# | no  | source vlan 20 tx |
Messagereceivedwhentryingtoaddmorethan1024mirrorsourceVLANs
switch(config-mirror-2)#
source vlan 2000 rx
The maximum number of source VLANs per mirror session is 1024 in each direction
87
AOS-CX10.09MonitoringGuide| (83xxSwitchSeries)

Chapter 10
|            |          |       |      | Monitoring | a device | using SNMP |
| ---------- | -------- | ----- | ---- | ---------- | -------- | ---------- |
| Monitoring | a device | using | SNMP |            |          |            |
Configuring SNMP:RefertotheSNMP/MIBGuideforinformationonhowtoaddSNMPsoadevicecan
bemonitoredfromanetworkmanagementsystem(NMS).
Configuring an SNMP trap receiver:RefertotheSNMP/MIBGuideandspecificinformationaboutthe
trapcommandtoenableSNMPtraps.
show snmp
PoE commands
AllPoEconfigurationcommandsexceptthreshold configurationandalways-on poe configuration
areenteredattheconfig-ifcontext.ThePoEthresholdcommandisusedatthesystemlevelwhereas
thealways-on poeandpower-over-ethernet quick-poecommandsaresetattheslotlevel.These
commandscanonlybeconfiguredintheglobalconfigurationcontext.
| lldp dot3    | poe |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- |
| lldp dot3    | poe |     |     |     |     |     |
| no lldp dot3 | poe |     |     |     |     |     |
Description
Enables802.3TLVlistinLLDPtoadvertiseforPoweroverEthernetDataLinkLayerClassification.LLDP
dot3TLVisbydefaultenabledforPoE.
Thenoformofthiscommanddisables802.3TLVlistinLLDP.
Examples
Enabling802.3TLVlistinLLDP:
| switch(config)#    |     | interface | 1/1/1 |     |     |     |
| ------------------ | --- | --------- | ----- | --- | --- | --- |
| switch(config-if)# |     | lldp dot3 | poe   |     |     |     |
Disabling802.3TLVlistinLLDP:
| switch(config-if)# |             | no lldp | dot3 poe     |     |     |     |
| ------------------ | ----------- | ------- | ------------ | --- | --- | --- |
| Command            | History     |         |              |     |     |     |
| Release            |             |         | Modification |     |     |     |
| 10.07orearlier     |             |         | --           |     |     |     |
| Command            | Information |         |              |     |     |     |
88
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| lldp med     | poe                     |     |     |
| ------------ | ----------------------- | --- | --- |
| lldp med poe | [priority-override]     |     |     |
| no lldp med  | poe [priority-override] |     |     |
Description
EnablesMEDTLVlistinLLDPtoadvertiseforPoweroverEthernetDataLinkLayerClassification.Also
enablesthelldp-MEDTLVprioritytooverrideuserconfiguredportpriorityforPoweroverEthernet.
Whenbothdot3andMEDareenabled,dot3willtakeprecedence.MEDTLVisbydefaultenabledfor
PoE.Priorityover-rideisbydefaultdisabled.
ThenoformofthiscommanddisablesMEDTLVlistinLLDP.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
[priority-override]
Systemdefinednameoftheinterface.
Examples
EnablinganddisablingLLDPMEDPoE:
switch(config)#
|                    | interface | 1/1/1       |     |
| ------------------ | --------- | ----------- | --- |
| switch(config-if)# |           | lldp med    | poe |
| switch(config-if)# |           | no lldp med | poe |
EnablinganddisablingLLDPMEDPoEpriorityoverride:
| switch(config-if)#  |         | lldp med | poe priority-override |
| ------------------- | ------- | -------- | --------------------- |
| Command History     |         |          |                       |
| Release             |         |          | Modification          |
| 10.07orearlier      |         |          | --                    |
| Command Information |         |          |                       |
| Platforms           | Command | context  | Authority             |
config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
power-over-ethernet
power-over-ethernet
no power-over-ethernet
Description
MonitoringadeviceusingSNMP|89

Enablesper-interfacepowerdistribution.Per-portpowerisenabledbydefaultwithprioritylow.PoE
cannotbedisabledforindividualportswhenQuickPoEisenabledfortheentireswitchorlinemodule.
Thenoformofthiscommanddisablesper-interfacepowerdistribution.
Examples
Enablingper-interfacepowerdistribution:
| switch(config)#    |     | interface |                     | 1/1/1 |     |     |     |     |
| ------------------ | --- | --------- | ------------------- | ----- | --- | --- | --- | --- |
| switch(config-if)# |     |           | power-over-ethernet |       |     |     |     |     |
Disablingper-interfacepowerdistribution:
| switch(config-if)# |     |     | no power-over-ethernet |     |     |     |     |     |
| ------------------ | --- | --- | ---------------------- | --- | --- | --- | --- | --- |
ShowingQuickPoEenabled:
| switch(config-if)# |             |        | power-over-ethernet    |          |              | quick-poe |     | 1/1         |
| ------------------ | ----------- | ------ | ---------------------- | -------- | ------------ | --------- | --- | ----------- |
| switch(config-if)# |             |        | interface              |          | 1/1/1        |           |     |             |
| switch(config-if)# |             |        | no power-over-ethernet |          |              |           |     |             |
| Interface          | PoE         | cannot | be                     | disabled | when         | Quick     | PoE | is enabled. |
| Command            | History     |        |                        |          |              |           |     |             |
| Release            |             |        |                        |          | Modification |           |     |             |
| 10.07orearlier     |             |        |                        |          | --           |           |     |             |
| Command            | Information |        |                        |          |              |           |     |             |
| Platforms          | Command     |        | context                |          | Authority    |           |     |             |
config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet    |     |             |             | allocate-by |        |          |        |     |
| ---------------------- | --- | ----------- | ----------- | ----------- | ------ | -------- | ------ | --- |
| power-over-ethernet    |     | allocate-by |             |             | {usage | | class} |        |     |
| no power-over-ethernet |     |             | allocate-by |             | {usage | |        | class} |     |
Description
Configuresthepowerallocationmethod.Powerallocationmethodisinitiallybasedonusage.PSE
AllocatedpowervaluewillchangetoLLDPnegotiatedpowerifandwhenLLDPexchangetakesplace
betweenPSEandPD.WhenthereisnoLLDPnegotiation,PSEAllocatedPowerValuewillbetheactual
instantaneouspowerdrawandreservepowerbasedonactualconsumption.Inallocate-byclass,power
allocationisbasedonPDrequestedclassandPSEallocatedpowervaluewillbetheLLDPnegotiated
powerwhenLLDPexchangetakesplacebetweenPSEandPD.WhenthereisnoLLDPnegotiation,PSE
AllocatePowerwillbebasedonPDclass.ReservepowerisbasedonPDClass.Bydefault,power
allocationisbyusage.
Thenoformofthiscommandresetstheactiontodefault.
90
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |

Examples
Configuringthepowerallocationmethod:
switch(config)#
|                    |     | interface |                     | 1/1/1 |     |             |     |       |
| ------------------ | --- | --------- | ------------------- | ----- | --- | ----------- | --- | ----- |
| switch(config-if)# |     |           | power-over-ethernet |       |     | allocate-by |     | usage |
| switch(config-if)# |     |           | power-over-ethernet |       |     | allocate-by |     | class |
Resettingpowerallocationmethod:
| switch(config-if)#  |         |     | no power-over-ethernet |     |              | allocate-by |     | class |
| ------------------- | ------- | --- | ---------------------- | --- | ------------ | ----------- | --- | ----- |
| Command History     |         |     |                        |     |              |             |     |       |
| Release             |         |     |                        |     | Modification |             |     |       |
| 10.07orearlier      |         |     |                        |     | --           |             |     |       |
| Command Information |         |     |                        |     |              |             |     |       |
| Platforms           | Command |     | context                |     | Authority    |             |     |       |
config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet    |     |           |           | always-on   |     |     |     |     |
| ---------------------- | --- | --------- | --------- | ----------- | --- | --- | --- | --- |
| power-over-ethernet    |     | always-on |           | <MODULE-ID> |     |     |     |     |
| no power-over-ethernet |     |           | always-on | <MODULE-ID> |     |     |     |     |
Description
Always-onPoEisafeaturethatprovidestheabilitytotheswitchtocontinuetoprovidepoweracrossa
softreboot.Itisapplicableonlytotheinterfaceswhichwereconnectedanddeliveringbeforethesoft
reboot.Also,powerwillnotbedeliveredifpowertotheswitchisinterrupted.Thiscommandenablesor
disablesthealways-onPoEfeatureattheswitchortheslotlevel.Bydefault,always-onPoEisenabledat
theswitchortheslotlevel.
Thenoformofthiscommanddisablespowerdistributiononsoftreboot.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<MODULE-ID>
Modulenumbertoapplyalways-onPoEconfiguration.
Examples
Enablingper-interfacepowerdistribution:
switch(config)#
|     |     | power-over-ethernet |     |     |     | always-on | 1/1 |     |
| --- | --- | ------------------- | --- | --- | --- | --------- | --- | --- |
Disablingper-interfacepowerdistribution:
MonitoringadeviceusingSNMP|91

| switch(config)#     |         | no  | power-over-ethernet |              | always-on |     | 1/1 |     |
| ------------------- | ------- | --- | ------------------- | ------------ | --------- | --- | --- | --- |
| Command History     |         |     |                     |              |           |     |     |     |
| Release             |         |     |                     | Modification |           |     |     |     |
| Command Information |         |     |                     |              |           |     |     |     |
| Platforms           | Command |     | context             | Authority    |           |     |     |     |
config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet    |     |                | assigned-class |      |        |     |     |     |
| ---------------------- | --- | -------------- | -------------- | ---- | ------ | --- | --- | --- |
| power-over-ethernet    |     | assigned-class |                | {3 | | 4 | 6} |     |     |     |
| no power-over-ethernet |     |                | assigned-class |      |        |     |     |     |
Description
LimitPoEpowerbasedontheassignedclass.Whenanuserassignsamaximumclasstoaninterface,
thePSEwilllimitthemaximumpowerdeliveredtothePDuptoatotalpowerdrawnotexceedingthe
PSEassigned-classpower.PowerdemotionoccurswhenaPDrequestedclassishigherthanthePSE
assignedclass,permittingthePDtoreceivepowerandoperateinareducedpowermode.PoEports
cannotsetanassignedclasswhenQuickPoEisenabledonthesybsystem.Thedefaultassignedclassis
4for2-paircapablePSEand6for4-paircapablePSE.
Thenoformofthiscommandresetstheactiontodefault.
Examples
SettingPoEassignedclass:
| switch(config)# |     | interface | 1/1/1 |     |     |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- | --- | --- |
switch(config-if)#
|     |     |     | power-over-ethernet |     | assigned-class |     |     | 4   |
| --- | --- | --- | ------------------- | --- | -------------- | --- | --- | --- |
ResettingPoEassignedclasstodefault:
| switch(config-if)# |     |     | no power-over-ethernet |     | assigned-class |     |     | 4   |
| ------------------ | --- | --- | ---------------------- | --- | -------------- | --- | --- | --- |
ShowingQuickPoEenabled:
| switch(config)# |     | power-over-ethernet |       |     | quick-poe      | 1/1 |     |     |
| --------------- | --- | ------------------- | ----- | --- | -------------- | --- | --- | --- |
| switch(config)# |     | interface           | 1/1/1 |     |                |     |     |     |
| switch(config)# |     | power-over-ethernet |       |     | assigned-class |     | 4   |     |
Interface assigned class cannot be configured when Quick PoE is enabled.
| Command History |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
92
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |

| Release             |         |     |         |     | Modification |     |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- | --- |
| 10.07orearlier      |         |     |         |     | --           |     |     |
| Command Information |         |     |         |     |              |     |     |
| Platforms           | Command |     | context |     | Authority    |     |     |
config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet    |     |             | power-pairs |        |        |                    |     |
| ---------------------- | --- | ----------- | ----------- | ------ | ------ | ------------------ | --- |
| power-over-ethernet    |     | power-pairs |             | {alt-a |        | | alt-a-and-alt-b} |     |
| no power-over-ethernet |     |             | power-pairs |        | {alt-a | | alt-a-and-alt-b} |     |
Description
Configuresthefour-paircapableswitchtooperateinamode,thatrestrictsthepowerdeliveryforclass
0toclass4singlesignaturedevicestooperateonlyonALT-Apowerpair.
Whenconfigured,awarningmessageisdisplayed.UsermustacceptthewarningbyenteringYtoenablethe
mode.
ThenoformofthiscommandresetsthepowerpairstodefaultPoEpairs.
| Parameter |     |     |     |     | Description                      |     |     |
| --------- | --- | --- | --- | --- | -------------------------------- | --- | --- |
| alt-a     |     |     |     |     | DeliverspoweronlyontheALT-Apair. |     |     |
alt-a-and-alt-b DeliverspowerontheALT-AandALT-Bpairs.Thisisthedefault
configurationonallPoEinterfaces.
Usage
IEEE802.3btdevicessuchasfour-pair(class5andhigher)anddualsignaturepowereddevicesrequire
poweronbothpairs.However,thereisnosuchrestrictiononIEEE802.3af(class0toclass3)andIEEE
802.3at(class4)powereddevicesnottodrawpoweronbothpairsiftheoverallconsumptiondoesnot
violatethepowerclasslimit.Forsuchpowereddevices,apower-pairsconfigurationisprovidedto
configurethe4-paircapableswitchtorestrictpowerononlyonepowerpair.
Examples
ConfiguringPoEpowerpairs:
| switch(config)#    |     | interface |                     | 1/1/1 |     |             |       |
| ------------------ | --- | --------- | ------------------- | ----- | --- | ----------- | ----- |
| switch(config-if)# |     |           | power-over-ethernet |       |     | power-pairs | alt-a |
This setting configures the interface to deliver power only on the ALT-A
cable pair when a Class 0-4 device is connected. Devices that require power
| on all pairs |        | may not | operate | correctly. |     |     |     |
| ------------ | ------ | ------- | ------- | ---------- | --- | --- | --- |
| Continue     | (y/n)? | y       |         |            |     |     |     |
ResettingthePoEpowerpairtodefault:
MonitoringadeviceusingSNMP|93

| switch(config-if)# |     | no power-over-ethernet |     | power-pairs | alt-a |
| ------------------ | --- | ---------------------- | --- | ----------- | ----- |
This setting configures the interface to deliver power on the ALT-A
and ALT-B cable pairs. This is the default and most devices work
properly with this setting, however some older Class 0-4 devices may
| not operate         | correctly. |         |                   |     |     |
| ------------------- | ---------- | ------- | ----------------- | --- | --- |
| Continue            | (y/n)? y   |         |                   |     |     |
| Command History     |            |         |                   |     |     |
| Release             |            |         | Modification      |     |     |
| 10.09               |            |         | CommandIntroduced |     |     |
| Command Information |            |         |                   |     |     |
| Platforms           | Command    | context | Authority         |     |     |
config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet    |                | pre-std-detect |     |     |     |
| ---------------------- | -------------- | -------------- | --- | --- | --- |
| power-over-ethernet    | pre-std-detect |                |     |     |     |
| no power-over-ethernet |                | pre-std-detect |     |     |     |
Description
BeforeIEEE802.3releasedthefirstPoweroverEthernetstandard(802.3af),vendorshadshippedPoE
capableswitchesandPD's.AswearebackwardcompatibleArubawillsupportbothIEEEstandardand
pre-standard802.3afPoweroverEthernetPD'sconcurrently.ThisCLIallowstheusertoenableor
disablepre-802.3af-standarddevicedetectionandpoweringonthespecificport.Whenpre-std-detectis
enabled,powerwillbedeliveredonPairAonly.Defaultisdisabled.
Thenoformofthiscommandresetstheactiontodefault.
Examples
Enablingstandarddevicedetection:
| switch(config)#    | interface | 1/1/1               |     |                |     |
| ------------------ | --------- | ------------------- | --- | -------------- | --- |
| switch(config-if)# |           | power-over-ethernet |     | pre-std-detect |     |
Disablingstandarddevicedetection:
| switch(config-if)# |     | no power-over-ethernet |     | pre-std-detect |     |
| ------------------ | --- | ---------------------- | --- | -------------- | --- |
| Command History    |     |                        |     |                |     |
94
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

| Release             |         |     |         |     | Modification |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- |
| 10.07orearlier      |         |     |         |     | --           |     |
| Command Information |         |     |         |     |              |     |
| Platforms           | Command |     | context |     | Authority    |     |
config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet    |     |          |          | priority  |     |               |
| ---------------------- | --- | -------- | -------- | --------- | --- | ------------- |
| power-over-ethernet    |     | priority |          | {critical |     | | high | low} |
| no power-over-ethernet |     |          | priority | {critical |     | | high | low} |
Description
SetsPoEpriorityforaninterfaceSpecifyingcritical,high,orlowindicatesthepriorityoftheinterfacein
theeventofpowerover-subscription.Withinthesameprioritylevel,higherpower-priorityline-module
portshavehigherprecedence.WithsamePoEpriorityandsameline-modulepriority,lowernumbered
line-moduleportshavehigherprecedence.Per-interfacePoEpriorityislowbydefault.
ThenoformofthiscommandresetstheprioritytodefaultPoEpriority"low".
Examples
ConfiguringPoEpriority:
| switch(config)#    |     | interface |                     | 1/1/1 |     |                   |
| ------------------ | --- | --------- | ------------------- | ----- | --- | ----------------- |
| switch(config-if)# |     |           | power-over-ethernet |       |     | priority critical |
switch(config-if)#
|     |     |     | power-over-ethernet |     |     | priority high |
| --- | --- | --- | ------------------- | --- | --- | ------------- |
ResettingthePoEprioritytodefault:
| switch(config-if)#  |         |     | no power-over-ethernet |     |              | priority high |
| ------------------- | ------- | --- | ---------------------- | --- | ------------ | ------------- |
| Command History     |         |     |                        |     |              |               |
| Release             |         |     |                        |     | Modification |               |
| 10.07orearlier      |         |     |                        |     | --           |               |
| Command Information |         |     |                        |     |              |               |
| Platforms           | Command |     | context                |     | Authority    |               |
config-if
Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet |     |           |     | quick-poe   |     |     |
| ------------------- | --- | --------- | --- | ----------- | --- | --- |
| power-over-ethernet |     | quick-poe |     | <MODULE-ID> |     |     |
no power-over-ethernet
MonitoringadeviceusingSNMP|95

Description
QuickPoEisafeaturethatprovidestheabilityfortheswitchtoprovidepowertotheconnected
powereddeviceassoonasswitchgoesthroughcoldreboot.WhenquickPoEisenabledonthe
subsystemPoEportdisablementandPDdemotionisnotallowed.alsoquickPoEenablementisnot
allowedifanyoftheportisdisabledonthesubsystem.Usershouldnotover-subscribethePoEpower
whenquickPoEisenabled.QuickPoEsavedconfigurationwillworkirrespectiveoftheconfiguration
changeatreboot.
EnablesquickPoEfeatureontheswitchorthesubsystemlevel.Bydefault,quick-PoEisdisabledforthe
subsystem.
ThenoformofthiscommanddisablesquickPoE.
| Parameter   |     |     |     |     | Description                                    |     |     |
| ----------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- |
| <MODULE-ID> |     |     |     |     | SpecifiesmodulenumberforquickPoEconfiguration. |     |     |
Examples
EnablinganddisablingquickPoE:
| switch(config)#    |     | power-over-ethernet |                     |     |     | quick-poe | 1/2 |
| ------------------ | --- | ------------------- | ------------------- | --- | --- | --------- | --- |
| switch(config)#    |     | no                  | power-over-ethernet |     |     | quick-poe | 1/2 |
| switch(config-if)# |     |                     | power-over-ethernet |     |     | quick-poe | 1/1 |
PoE must be enabled on all interfaces before enabling Quick PoE
switch(config-if)#
|     |     |     | power-over-ethernet |     |     | quick-poe | 1/3 |
| --- | --- | --- | ------------------- | --- | --- | --------- | --- |
All interfaces must use the default assigned class before enabling Quick PoE
| Command History     |         |     |         |     |              |     |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- | --- |
| Release             |         |     |         |     | Modification |     |     |
| 10.07orearlier      |         |     |         |     | --           |     |     |
| Command Information |         |     |         |     |              |     |     |
| Platforms           | Command |     | context |     | Authority    |     |     |
config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet    |     |           |           | threshold    |     |     |     |
| ---------------------- | --- | --------- | --------- | ------------ | --- | --- | --- |
| power-over-ethernet    |     | threshold |           | <PERCENTAGE> |     |     |     |
| no power-over-ethernet |     |           | threshold | <PERCENTAGE> |     |     |     |
Description
Setsthethresholdatwhichthesystemwillsendanexcesspowerconsumptionnotificationtrap.Default
valueis80percentage.
96
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

Thenoformofthiscommandresetstheactiontodefault.
| Parameter    |     |     | Description                                    |     |     |
| ------------ | --- | --- | ---------------------------------------------- | --- | --- |
| <PERCENTAGE> |     |     | Excesspowerconsumptiontrapthreshold.Range1-99. |     |     |
Examples
Settingthepower-over-ethernetthreshold:
| switch(config)# |     | power-over-ethernet | threshold | 75  |     |
| --------------- | --- | ------------------- | --------- | --- | --- |
Resettingthepower-over-ethernetthresholdtodefault:
| switch(config-if)#  |         | no power-over-ethernet |              | threshold | 75  |
| ------------------- | ------- | ---------------------- | ------------ | --------- | --- |
| Command History     |         |                        |              |           |     |
| Release             |         |                        | Modification |           |     |
| 10.07orearlier      |         |                        | --           |           |     |
| Command Information |         |                        |              |           |     |
| Platforms           | Command | context                | Authority    |           |     |
config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet    |     | trap |     |     |     |
| ---------------------- | --- | ---- | --- | --- | --- |
| power-over-ethernet    |     | trap |     |     |     |
| no power-over-ethernet |     | trap |     |     |     |
Description
Thiscommandenables/disablestheSNMPtrapgenerationforPoErelatedeventsatsystemlevel.PoE
trapgenerationisenabledbydefault.
ThenoformofthiscommandresetstheprioritytodefaultPoEpriority"low".
Examples
EnablingSNMPtrapgenerationforPoE:
| switch(config)# |     | power-over-ethernet | trap |     |     |
| --------------- | --- | ------------------- | ---- | --- | --- |
DisablingSNMPtrapgenerationforPoE:
| switch(config-if)# |     | no power-over-ethernet |     | trap |     |
| ------------------ | --- | ---------------------- | --- | ---- | --- |
| Command History    |     |                        |     |      |     |
MonitoringadeviceusingSNMP|97

| Release        |             |         |         |     | Modification |
| -------------- | ----------- | ------- | ------- | --- | ------------ |
| 10.07orearlier |             |         |         |     | --           |
| Command        | Information |         |         |     |              |
| Platforms      |             | Command | context |     | Authority    |
config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show      | lldp         | local |                  |     |     |
| --------- | ------------ | ----- | ---------------- | --- | --- |
| show lldp | local-device |       | [<INTERFACE-ID>] |     |     |
Description
DisplaysinformationadvertisedbytheswitchiftheLLDPfeatureisenabledbyuser.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port
Examples
ShowingLLDPlocaldevice:
| switch# |      | show lldp | local-device |     | 1/1/10 |
| ------- | ---- | --------- | ------------ | --- | ------ |
| Local   | Port | Data      |              |     |        |
===============
| Port-ID        |             |             | : 1/1/10   |     |              |
| -------------- | ----------- | ----------- | ---------- | --- | ------------ |
| Port-Desc      |             |             | : "1/1/10" |     |              |
| Port           | VLAN        | ID          | : 0        |     |              |
| PoE            | Plus        | Information |            |     |              |
| PoE            | Device      | Type        | : Type     | 2   | PSE          |
| Power          | Source      |             | : Primary  |     |              |
| Power          | Priority    |             | : low      |     |              |
| PSE            | Allocated   | Power:      | 25.0       | W   |              |
| PD             | Requested   | Power       | : 25.0     | W   |              |
| Command        | History     |             |            |     |              |
| Release        |             |             |            |     | Modification |
| 10.07orearlier |             |             |            |     | --           |
| Command        | Information |             |            |     |              |
98
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show lldp          | neighbor |                  |     |     |
| ------------------ | -------- | ---------------- | --- | --- |
| show lldp neighbor |          | [<INTERFACE-ID>] |     |     |
Description
Displaysdetailedinformationaboutaparticularneighborconnectedtoaparticularinterface.
| Parameter      |     |     | Description                                  |     |
| -------------- | --- | --- | -------------------------------------------- | --- |
| <INTERFACE-ID> |     |     | Specifiesaninterface.Format:member/slot/port |     |
Examples
ShowingLLDPneighborinformationwhenthereisonlyoneneighbor:
| switch#  | show lldp    | neighbor-info | 1/1/10              |     |
| -------- | ------------ | ------------- | ------------------- | --- |
| Port     |              |               | : 1/1/10            |     |
| Neighbor | Entries      |               | : 1                 |     |
| Neighbor | Entries      | Deleted       | : 0                 |     |
| Neighbor | Entries      | Dropped       | : 0                 |     |
| Neighbor | Entries      | Aged-Out      | : 0                 |     |
| Neighbor | Chassis-Name |               | : 84:d4:7e:ce:5d:68 |     |
Neighbor Chassis-Description : ArubaOS (MODEL: 325), Version Aruba IAP
| Neighbor            | Chassis-ID         |             | : 84:d4:7e:ce:5d:68 |      |
| ------------------- | ------------------ | ----------- | ------------------- | ---- |
| Neighbor            | Management-Address |             | : 169.254.41.250    |      |
| Chassis             | Capabilities       | Available   | : Bridge,           | WLAN |
| Chassis             | Capabilities       | Enabled     | :                   |      |
| Neighbor            | Port-ID            |             | : 84:d4:7e:ce:5d:68 |      |
| Neighbor            | Port-Desc          |             | : eth0              |      |
| TTL                 |                    |             | : 120               |      |
| Neighbor            | Port               | VLAN ID     | :                   |      |
| Neighbor            | PoEplus            | information | : DOT3              |      |
| Neighbor            | Device             | Type        | : TYPE2             | PD   |
| Neighbor            | Power              | Priority    | : Unkown            |      |
| Neighbor            | Power              | Source      | : Primary           |      |
| Neighbor            | Power              | Requested   | : 25.0              | W    |
| Neighbor            | Power              | Allocated   | : 0.0 W             |      |
| Neighbor            | Power              | Supported   | : No                |      |
| Neighbor            | Power              | Enabled     | : No                |      |
| Neighbor            | Power              | Class       | : 5                 |      |
| Neighbor            | Power              | Paircontrol | : No                |      |
| Neighbor            | Power              | Pairs       | : SIGNAL            |      |
| Command History     |                    |             |                     |      |
| Release             |                    |             | Modification        |      |
| 10.07orearlier      |                    |             | --                  |      |
| Command Information |                    |             |                     |      |
MonitoringadeviceusingSNMP|99

| Platforms |     |     | Command | context |     |     | Authority |     |     |     |     |
| --------- | --- | --- | ------- | ------- | --- | --- | --------- | --- | --- | --- | --- |
OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
show power-over-ethernet
Description
Displaysthestatusinformationofthefullsystem.
| Parameter |     |     |     |     |     |     | Description                                    |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- |
| brief     |     |     |     |     |     |     | Displaythebriefstatusofallportsorthegivenport. |     |     |     |     |
Examples
Showingsampleoutputforpower-over-ethernetbriefper-port:
| switch# |            | show              | power-over-ethernet |             |             | 1/1/1 | brief |            |          |     |     |
| ------- | ---------- | ----------------- | ------------------- | ----------- | ----------- | ----- | ----- | ---------- | -------- | --- | --- |
| Status  |            | and Configuration |                     |             | Information |       | for   | port 1/1/1 |          |     |     |
|         | Member     | 1Power            | Status              |             |             |       |       |            |          |     |     |
|         | Available: |                   | 370                 | W Reserved: |             | 55.60 | W     | Remaining: | 314.40 W |     |     |
|         | Always-on  |                   | PoE                 | Enabled:    | 1/1         |       |       |            |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port |     | En  | Priority | Detect |     | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | --- | --- | -------- | ------ | --- | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 |     | Yes | Low | Off |     | Class | 0.0 | W 0.0 | W Denied | None 4 | 2   |
| ----- | --- | --- | --- | --- | --- | ----- | --- | ----- | -------- | ------ | --- |
Showingsampleoutputforpower-over-ethernetforamissinglinecard:
| switch# |     | show   | power-over-ethernet |            |     | 1/3      | brief |     |     |     |     |
| ------- | --- | ------ | ------------------- | ---------- | --- | -------- | ----- | --- | --- | --- | --- |
| Module  |     | 1/3 is | not                 | physically |     | present. |       |     |     |     |     |
Showingsampleoutputforpower-over-ethernetportwhenphysicalinterfaceisnotpresent:
| switch#        |     | show        | power-over-ethernet |              |     | 2/1/1 |              |     |     |     |     |
| -------------- | --- | ----------- | ------------------- | ------------ | --- | ----- | ------------ | --- | --- | --- | --- |
| Interface      |     | 2/1/1       | is                  | not present. |     |       |              |     |     |     |     |
| Command        |     | History     |                     |              |     |       |              |     |     |     |     |
| Release        |     |             |                     |              |     |       | Modification |     |     |     |     |
| 10.07orearlier |     |             |                     |              |     |       | --           |     |     |     |     |
| Command        |     | Information |                     |              |     |       |              |     |     |     |     |
100
| AOS-CX10.09MonitoringGuide| |     |     | (83xxSwitchSeries) |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
MonitoringadeviceusingSNMP|101

Chapter 11
Breakout cable support
| Breakout | cable support |     |     |
| -------- | ------------- | --- | --- |
Portsdefaulttoanunsplitstate.Whenaportis'split',thesplitinterfacesbecomeactiveandcanbe
configuredindependently.Forexample,whena40GQSFP+portissplitfourways,eachsplitinterface
behaveslikeaseparate10GSFP+port.Thesplitinterfaceshavethesamenameasthebaseportwithan
addedsuffixtorepresenttheirlaneofthebreakoutcableoropticalchannelonSR4optics.Splittingan
interfaceremovesmostoftheport'sconfigurationsettingsandmakesitinactive.Theportwillnolonger
appearinmanyshowinterfacecommandsandmostconfigurationcommandsarenotallowed;thesplit
interfacenamemustbeused.
Thesamethinghappensinreversewhenaninterfaceisunsplit.However,notethatthe'split'and'no
split'commandsarealwaysperformedintheunsplitport'scontext.
| Limitations | with breakout | cable support |     |
| ----------- | ------------- | ------------- | --- |
n TheJL720AAruba8360-48XT4Cmodels(orderedSKU#sJL706A/JL707A)donotsupportsplitports.
| Breakout | cable support | commands |     |
| -------- | ------------- | -------- | --- |
split
split [confirm]
| no split [confirm] |     |     |     |
| ------------------ | --- | --- | --- |
Description
Splitsaportintomultipleinterfaces.OnlyportscapableofsupportingbreakoutcablesorSR4/eSR4
opticscanbesplit.
| Parameter |     | Description                              |     |
| --------- | --- | ---------------------------------------- | --- |
| confirm   |     | Specifiestheconfirmationofportsplitting. |     |
Usage
Thesplittableportsforallmodelsareshowninthetablebelow:
| Part Number | (PN) | Description | Port info |
| ----------- | ---- | ----------- | --------- |
Aruba8320Series
| n JL479A |     | Aruba83204810/640X47252Bdl | 49-54(40G) |
| -------- | --- | -------------------------- | ---------- |
n JL579A
|     |     | Aruba83203240GX47252Bdl | 5-28(40G-center24 |
| --- | --- | ----------------------- | ----------------- |
n JL581A
ports)
Aruba832048T/640X47252Bdl
49-54(40G)
102
| AOS-CX10.09MonitoringGuide| | (83xxSwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Part Number | (PN) | Description |     | Port info |
| ----------- | ---- | ----------- | --- | --------- |
Aruba832548Y8Cmodels
| JL635A(basesystem)              |     | Displayedbyshow | system |                  |
| ------------------------------- | --- | --------------- | ------ | ---------------- |
| n JL624A-Port-to-Powermodel(FB) |     |                 |        | 49-56(40Gor100G) |
Aruba8325-48Y8CFB6F2PSBdl
| n JL625A-Power-to-Portmodel(BF) |     |     |     | 49-56(40Gor100G) |
| ------------------------------- | --- | --- | --- | ---------------- |
Aruba8325-48Y8CBF6F2PS Bdl
Aruba832532Cmodels
JL636A(basesystem)
|     |     | Displayedbyshow | system |     |
| --- | --- | --------------- | ------ | --- |
n JL626A-Port-to-Powermodel(FB)
1-32(40Gor100G)
Aruba8325-32CFB6F2PSBdl
n JL627A-Power-to-Portmodel(BF)
1-32(40Gor100G)
Aruba8325-32CBF6F2PSBdl
Aruba836032Y4Cmodels
|     |     | Displayedbyshow | system |     |
| --- | --- | --------------- | ------ | --- |
JL717A(basesystem)
| n JL700APort-to-Powermodel |     |     |     | 33-36(40Gor100G) |
| -------------------------- | --- | --- | --- | ---------------- |
Aruba8360-32Y4CPrt2Pwr3F2PSBdl
n JL701APower-to-Portmodel Aruba8360-32Y4CPwr2Prt3F2PSBdl 33-36(40Gor100G)
Aruba836016Y2Cmodels
|     |     | Displayedbyshow | system |     |
| --- | --- | --------------- | ------ | --- |
JL718A(basesystem)
| n JL702APort-to-Powermodel |     |     |     | 17-18(40Gor100G) |
| -------------------------- | --- | --- | --- | ---------------- |
Aruba8360-16Y2CPrt2Pwr3F2PSBdl
n JL703APower-to-Portmodel Aruba8360-16Y2CPwr2Prt3F2PSBdl 17-18(40Gor100G)
Aruba836048XT4Cmodels
|     |     | Displayedbyshow | system |     |
| --- | --- | --------------- | ------ | --- |
JL720A(basesystem)
| n JL706APort-to-Powermodel |     |     |     | NOSUPPORTforSplit |
| -------------------------- | --- | --- | --- | ----------------- |
Aruba8360-48XT4CPrt2Pwr3F2PSBdl
n JL707APower-to-Portmodel Aruba8360-48XT4CPwr2Prt3F2PSBdl ports
Aruba8360-12Cmodels
|     |     | Displayedbyshow | system |     |
| --- | --- | --------------- | ------ | --- |
JL721A(basesystem)
| n JL708APort-to-Powermodel |     |     |     | 1-12(40Gor100G) |
| -------------------------- | --- | --- | --- | --------------- |
Aruba8360-12CPwr2Prt3F2PSBdl
n JL709APower-to-Portmodel Aruba8360-12CPrt2Pwr3F2PSBdl 1-12(40Gor100G)
Aruba836024XF2Cmodels
|     |     | Displayedbyshow | system |     |
| --- | --- | --------------- | ------ | --- |
JL722A(basesystem)
| n JL710APort-to-Powermodel |     |     |     | 25-26(40Gor100G) |
| -------------------------- | --- | --- | --- | ---------------- |
Aruba8360-24XF2CPrt2Pwr3F2PSBdl
25-26(40Gor100G)
| n JL711APower-to-Portmodel |     | Aruba8360-24XF2CPwr2Pwr3F2PSBdl |     |     |
| -------------------------- | --- | ------------------------------- | --- | --- |
Forreleases10.05and10.06,the8320,8325,and8360SwitchSeriesrequireasaveandreboottoenablethe
splitport.Fromrelease10.07onwardstheseswitchesnolongerrequireasaveandreboot.
Examples
Beforesplittinganinterface:
| 8325(config)# | show interface | 1/1/56 brief |     |     |
| ------------- | -------------- | ------------ | --- | --- |
----------------------------------------------------------------------------------
--
| Port | Native Mode Type | Enabled | Status Reason | Speed |
| ---- | ---------------- | ------- | ------------- | ----- |
| Desc | VLAN             |         |               |       |
(Mb/s)
Breakoutcablesupport|103

----------------------------------------------------------------------------------
--
1/1/56 -- routed QSFP+DA1 no down Administratively down -- --
Aftersplitting:
| 8325(config)#    |     | interface |     | 1/1/56 |     |     |     |     |     |
| ---------------- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- |
| 8325(config-if)# |     | split     |     |        |     |     |     |     |     |
This command will disable the specified port, clear its configuration,
| and split        | it     | into | multiple  | interfaces. |                          |       |     |     |     |
| ---------------- | ------ | ---- | --------- | ----------- | ------------------------ | ----- | --- | --- | --- |
| Continue         | (y/n)? | y    |           |             |                          |       |     |     |     |
| 8325(config-if)# |        | show | interface |             | 1/1/56,1/1/56:1-1/1/56:4 | brief |     |     |     |
----------------------------------------------------------------------------------
--
| Port | Native |     | Mode | Type | Enabled Status | Reason |     | Speed |     |
| ---- | ------ | --- | ---- | ---- | -------------- | ------ | --- | ----- | --- |
Desc
|     | VLAN |     |     |     |     |     |     | (Mb/s) |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | ------ | --- |
----------------------------------------------------------------------------------
--
| 1/1/56   | --  |     | routed | QSFP+DA1 | no down | Interface | split | --    | --  |
| -------- | --- | --- | ------ | -------- | ------- | --------- | ----- | ----- | --- |
| 1/1/56:1 | --  |     | routed | QSFP+DA1 | yes up  |           |       | 10000 | --  |
| 1/1/56:2 | --  |     | routed | QSFP+DA1 | yes up  |           |       | 10000 | --  |
| 1/1/56:3 | --  |     | routed | QSFP+DA1 | yes up  |           |       | 10000 | --  |
| 1/1/56:4 | --  |     | routed | QSFP+DA1 | yes up  |           |       | 10000 | --  |
Unsplittingaportonaswitchthatdoesnotrequireareboot:
| switch(config)#    |     | interface |          | 1/1/1 |     |     |     |     |     |
| ------------------ | --- | --------- | -------- | ----- | --- | --- | --- | --- | --- |
| switch(config-if)# |     |           | no split |       |     |     |     |     |     |
This command will disable the split interfaces for this port and clear
| their configuration. |             |     |         |     |              |     |     |     |     |
| -------------------- | ----------- | --- | ------- | --- | ------------ | --- | --- | --- | --- |
| Continue             | (y/n)?      | y   |         |     |              |     |     |     |     |
| Command              | History     |     |         |     |              |     |     |     |     |
| Release              |             |     |         |     | Modification |     |     |     |     |
| 10.07orearlier       |             |     |         |     | --           |     |     |     |     |
| Command              | Information |     |         |     |              |     |     |     |     |
| Platforms            | Command     |     | context |     | Authority    |     |     |     |     |
8320 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
104
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |     |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |

Chapter 12
Aruba AirWave
| Aruba | AirWave |     |     |
| ----- | ------- | --- | --- |
YoucanmanageandmonitortheAOS-CXswitchthroughArubaAirWave.Thefollowingbenefitsand
functionsinclude:
n Configuration(partialconfiguration)
n Devicetopology
n Immediateandhistoricaltrendreports
n Monitoringofthedeviceanduserconnectedtothenetwork.
n Networkdiscovery
n Syslogsandtrapreceiver
ForinformationaboutwhichversionsofArubaAirWavesupportAOS-CX,seetheAOS-CXReleaseNotes.
| SNMP | support | and | AirWave |
| ---- | ------- | --- | ------- |
ForAirWavetodiscoverandmonitortheswitch,youmust:
n EnabletheSNMPservicesontheswitch.
n ConfiguretheSNMPagenttousetheSNMPversionsupportedbythemanagementstation.
| SNMP | on the | switch |     |
| ---- | ------ | ------ | --- |
TheswitchprovidesSNMPservicesthroughthemanagementchannelandthedatainterfaces.
Functionality,suchasdevicediscoveryfromNMS,syslogandtrapforwarding,canbeanychannel
configuredbyyou.
AlthoughtheSNMPservercanbeenabledonbothVRFs(mgmtanddefault),onlyoneinstanceofSNMP
canberunning.ThehighestpriorityisonthedefaultVRF.
Forexample,assumethatSNMPisfirstenabledonthemgmtVRF(snmp-server vrf mgmt).Then,SNMP
isenabledonthedefaultVRF(snmp-server vrf default)withoutdisablingSNMPonthemgmt(using
anequivalentnoformofthecommand).Theshow running-configcommanddisplaysbothsnmp-
server vrfcommands;however,theSNMPinstanceisrunningonlyonthedefaultVRF(highest
priority).
| switch#         | config         |                     |             |
| --------------- | -------------- | ------------------- | ----------- |
| switch(config)# |                | snmp-server         | vrf mgmt    |
| switch(config)# |                | snmp-server         | vrf default |
| switch(config)# |                | show running-config |             |
| Current         | configuration: |                     |             |
!
| !Version | AOS-CX     | Virtual.10.01. |     |
| -------- | ---------- | -------------- | --- |
| led      | locator on |                |     |
!
!
!
| snmp-server | vrf | default |     |
| ----------- | --- | ------- | --- |
| snmp-server | vrf | mgmt    |     |
105
| AOS-CX10.09MonitoringGuide| |     | (83xxSwitchSeries) |     |
| --------------------------- | --- | ------------------ | --- |

!
...
| Supported |     | features | with AirWave | and the | AOS-CX | switch |
| --------- | --- | -------- | ------------ | ------- | ------ | ------ |
AirWavesupportsthefollowingfeatureswiththeAOS-CXswitch:
| Devicemanagement |     |     | DevicediscoveryusingSNMPv2CandSNMPv3 |     |     |     |
| ---------------- | --- | --- | ------------------------------------ | --- | --- | --- |
Devicedashboards
Monitoringmanagement Devicehealthattributes(devicestatus/reachability)
InterfaceandVLANmanagement
InitiatesanSSHconnectionfromArubaAirWavetoAOS-CXsothatthedevice
outputsfromtheAOS-CXCLIcanbedisplayedintheArubaAirWaveuser
interface.
Firmwareversions
DisplaysneighbordevicesconnectedtoAOS-CXswitches
Devicetopology
| Configurationmanagement |     |     | Partialconfiguration |     |     |     |
| ----------------------- | --- | --- | -------------------- | --- | --- | --- |
Alarmmanagement Alarmtriggers(deviceandinterfaceup/down,newdevicediscoveries,custom
eventtriggers)
Syslogsandtraps
Reportmanagement Deviceinventory,interfaceutilization,anddevicereachabilityreports
Summaryreportofdevicemodel,firmware,andbootloaderversion
| Configuring |     | the AOS-CX | switch | to be monitored |     | by AirWave |
| ----------- | --- | ---------- | ------ | --------------- | --- | ---------- |
Prerequisites
ArubaAirWaveisactiveonthenetwork.
Procedure
1. EnableSNMPontheswitchbyenteringthesnmp-server vrfcommand.
|     | switch(config)# | snmp-server | vrf mgmt    |     |     |     |
| --- | --------------- | ----------- | ----------- | --- | --- | --- |
|     | switch(config)# | snmp-server | vrf default |     |     |     |
2. ConfiguretheSNMPv2Ccommunitytopublicbyenteringthesnmp-server community public
command.Inthisinstance,publicisaread-onlycommunitystring.
ArubaAirWave|106

switch(config)# snmp-server community public

3. The community-string is used by SNMPv1 and SNMPv2C for unencrypted authentication. SNMPv3
lets you encrypt the authentication mechanism. To enable SNMPv3, enter the snmpv3 user and
snmpv3 context commands.

switch(config)# snmpv3 user Admin auth sha auth-pass ciphertext
AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=
priv des priv-pass ciphertext
AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=

switch(config)# snmpv3 context Admin

For discovering devices in AirWave through the SNMPv3 community, the SNMPv3 context name is
not mandatory. Devices can still be discovered in Aruba AirWave without the SNMPv3 context
name.

4. Enter the logging command for enabling syslog forwarding to a remote syslog server, such as

AirWave:

switch(config)# logging 10.0.10.2 severity debug

5. SNMP traps enable an agent to notify the management station of significant events by way of an
unsolicited SNMP message. Enable SNMP traps by entering the snmp-server host command:

switch(config)# snmp-server host 10.10.10.10 trap version v2c vrf default

SNMP traps cannot be forwarded from AOS-CX 10.00 switches that have the VRF configured as
mgmt. Later versions of AOS-CX support SNMP trap forwarding even when the VRF is configured as
default or mgmt.

6. For information on how to add a device for monitoring in the Aruba AirWave user interface, see

the documentation for Aruba AirWave.

AOS-CX 10.09 Monitoring Guide | (83xx Switch Series)

107

Support and Other Resources

Chapter 13

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

Airheads social
forums and
Knowledge Base

AOS-CX Switch
Software
Documentation
Portal

Aruba Hardware
Documentation
and Translations
Portal

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/AOS-CX/help_portal/Content/home.htm

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

AOS-CX 10.09 Monitoring Guide | (83xx Switch Series)

108

| Arubasoftware | https://asp.arubanetworks.com/downloads |     |
| ------------- | --------------------------------------- | --- |
| Software      | https://lms.arubanetworks.com/          |     |
licensing
End-of-Life https://www.arubanetworks.com/support-services/end-of-life/
information
| ArubaDeveloper | https://developer.arubanetworks.com/ |     |
| -------------- | ------------------------------------ | --- |
Hub
| Accessing | Updates |     |
| --------- | ------- | --- |
YoucanaccessupdatesfromtheArubaSupportPortalortheHPEMyNetworkingWebsite.
| Aruba | Support | Portal |
| ----- | ------- | ------ |
https://asp.arubanetworks.com/downloads
IfyouareunabletofindyourproductintheArubaSupportPortal,youmayneedtosearchMy
Networking,whereoldernetworkingproductscanbefound:
My Networking
https://www.hpe.com/networking/support
Toviewandupdateyourentitlements,andtolinkyourcontractsandwarrantieswithyourprofile,goto
theHewlettPackardEnterpriseSupportCenterMore Information on Access to Support Materials
page:
https://support.hpe.com/portal/site/hpsc/aae/home/
AccesstosomeupdatesmightrequireproductentitlementwhenaccessedthroughtheHewlettPackard
EnterpriseSupportCenter.YoumusthaveanHPPassportsetupwithrelevantentitlements.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://asp.arubanetworks.com/notifications/subscriptions(requiresanactiveArubaSupportPortal
(ASP)accounttomanagesubscriptions).SecuritynoticesareviewablewithoutanASPaccount.
| Warranty | Information |     |
| -------- | ----------- | --- |
Toviewwarrantyinformationforyourproduct,gotohttps://www.arubanetworks.com/support-
services/product-warranties/.
| Regulatory | Information |     |
| ---------- | ----------- | --- |
Toviewtheregulatoryinformationforyourproduct,viewtheSafetyandComplianceInformationfor
Server,Storage,Power,Networking,andRackProducts,availableathttps://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts
| Additional | regulatory | information |
| ---------- | ---------- | ----------- |
Arubaiscommittedtoprovidingourcustomerswithinformationaboutthechemicalsubstancesinour
productsasneededtocomplywithlegalrequirements,environmentaldata(companyprograms,
SupportandOtherResources|109

product recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For
more information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation Feedback
Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

AOS-CX 10.09 Monitoring Guide | (83xx Switch Series)

110