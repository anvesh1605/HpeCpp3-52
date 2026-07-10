AOS-CX 10.15.xxxx
Monitoring Guide

8400 Switch Series

Published: February 2025

Version: 1

Copyright Information

© Copyright 2025 Hewlett Packard Enterprise Development LP.

This product includes code licensed under certain open source licenses which require source
compliance. The corresponding source for these components is available upon request. This offer is
valid to anyone in receipt of this information and shall expire three years following the date of the final
distribution of this product version by Hewlett Packard Enterprise Company. To obtain such source
code, please check if the code is available in the HPE Software Center at
https://myenterpriselicense.hpe.com/cwp-ui/software but, if not, send a written request for specific
software version and product for which you want the open source code. Along with the request, please
send a check or money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company
Attn: General Counsel
WW Corporate Headquarters
1701 E Mossy Oaks Rd Spring, TX 77389
United States of America.

| 2

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

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

3

Contents
| About                                             | this document                      |         |                    |               | 8   |
| ------------------------------------------------- | ---------------------------------- | ------- | ------------------ | ------------- | --- |
| Applicableproducts                                |                                    |         |                    |               | 8   |
| Latestversionavailableonline                      |                                    |         |                    |               | 8   |
| Commandsyntaxnotationconventions                  |                                    |         |                    |               | 8   |
| Abouttheexamples                                  |                                    |         |                    |               | 9   |
| Identifyingswitchportsandinterfaces               |                                    |         |                    |               | 9   |
| Identifyingmodularswitchcomponents                |                                    |         |                    |               | 10  |
| Aruba                                             | 8400 switch series                 | member, | slot, and          | port notation | 11  |
| LineModulesandManagementModules                   |                                    |         |                    |               | 11  |
| Monitoring                                        | hardware                           | through | visual observation |               | 13  |
| ConfirmingnormaloperationoftheswitchbyreadingLEDs |                                    |         |                    |               | 13  |
| Detectingiftheswitchisnotreadyforafailoverevent   |                                    |         |                    |               | 14  |
| FindingfaultedcomponentsusingtheswitchLEDs        |                                    |         |                    |               | 14  |
| Boot commands                                     |                                    |         |                    |               | 16  |
| bootfabric-module                                 |                                    |         |                    |               | 16  |
| bootline-module                                   |                                    |         |                    |               | 17  |
| bootmanagement-module                             |                                    |         |                    |               | 18  |
| bootmanagement-module(recoveryconsole)            |                                    |         |                    |               | 19  |
| bootset-default                                   |                                    |         |                    |               | 21  |
| bootsystem                                        |                                    |         |                    |               | 21  |
| showboot-history                                  |                                    |         |                    |               | 23  |
| External                                          | storage                            |         |                    |               | 27  |
| Externalstoragecommands                           |                                    |         |                    |               | 27  |
|                                                   | address(externalstorage)           |         |                    |               | 27  |
|                                                   | directory                          |         |                    |               | 28  |
|                                                   | disableexternal-storagelogfiles    |         |                    |               | 29  |
|                                                   | enable(external-storagelogfiles)   |         |                    |               | 30  |
|                                                   | external-storage                   |         |                    |               | 30  |
|                                                   | password(external-storage)         |         |                    |               | 31  |
|                                                   | showexternal-storage               |         |                    |               | 32  |
|                                                   | showrunning-configexternal-storage |         |                    |               | 33  |
|                                                   | type(externalstorage)              |         |                    |               | 34  |
|                                                   | username(externalstorage)          |         |                    |               | 35  |
|                                                   | vrf(externalstorage)               |         |                    |               | 35  |
| IP-SLA                                            |                                    |         |                    |               | 37  |
| IP-SLAguidelines                                  |                                    |         |                    |               | 37  |
| LimitationswithVoIPSLAs                           |                                    |         |                    |               | 38  |
| IP-SLAcommands                                    |                                    |         |                    |               | 38  |
|                                                   | http                               |         |                    |               | 38  |
|                                                   | https                              |         |                    |               | 39  |
|                                                   | icmp-echo                          |         |                    |               | 41  |
|                                                   | ip-sla                             |         |                    |               | 42  |
|                                                   | ip-slaresponder                    |         |                    |               | 42  |
5
AOS-CX10.15.xxxxMonitoringGuide| (8400SwitchSeries)

|                                                  | showip-slaresponder        |            | 44  |
| ------------------------------------------------ | -------------------------- | ---------- | --- |
|                                                  | showip-slaresponderresults |            | 45  |
|                                                  | showip-sla                 |            | 46  |
|                                                  | start-test                 |            | 50  |
|                                                  | stop-test                  |            | 50  |
|                                                  | tcp-connect                |            | 51  |
|                                                  | udp-echo                   |            | 52  |
|                                                  | udp-jitter-voip            |            | 53  |
|                                                  | vrf(ipsla)                 |            | 54  |
|                                                  | showinterface              |            | 55  |
|                                                  | showinterfacestatistics    |            | 62  |
| Mirroring                                        |                            |            | 66  |
| MirroringandsFlow                                |                            |            | 66  |
| Mirrorstatistics                                 |                            |            | 67  |
| Classifierpoliciesandmirroringsessions           |                            |            | 67  |
| Mirroringcommands                                |                            |            | 68  |
|                                                  | clearmirror                |            | 68  |
|                                                  | comment                    |            | 69  |
|                                                  | copytcpdump-pcap           |            | 70  |
|                                                  | copytshark-pcap            |            | 71  |
|                                                  | destinationcpu             |            | 72  |
|                                                  | destinationinterface       |            | 72  |
|                                                  | destinationtunnel          |            | 74  |
|                                                  | diagnostic                 |            | 75  |
|                                                  | diagutilitiestcpdump       |            | 76  |
|                                                  | disable(mirrorsession)     |            | 79  |
|                                                  | enable(mirrorsession)      |            | 79  |
|                                                  | mirrorsession              |            | 80  |
|                                                  | showmirror                 |            | 81  |
|                                                  | sourceinterface            |            | 83  |
|                                                  | sourcevlan                 |            | 85  |
| Monitoring                                       | a device                   | using SNMP | 88  |
| Breakout                                         | cable support              |            | 89  |
| Limitationswithbreakoutcablesupport              |                            |            | 89  |
| Breakoutcablesupportcommands                     |                            |            | 89  |
|                                                  | split                      |            | 89  |
| Aruba                                            | AirWave                    |            | 92  |
| SNMPsupportandAirWave                            |                            |            | 92  |
|                                                  | SNMPontheswitch            |            | 92  |
| SupportedfeatureswithAirWaveandtheAOS-CXswitch   |                            |            | 93  |
| ConfiguringtheAOS-CXswitchtobemonitoredbyAirWave |                            |            | 93  |
| AirWavecommands                                  |                            |            | 94  |
|                                                  | logging                    |            | 94  |
|                                                  | snmp-servercommunity       |            | 96  |
|                                                  | snmp-serverhost            |            | 97  |
|                                                  | snmp-servervrf             |            | 99  |
|                                                  | snmpv3context              |            | 99  |
|                                                  | snmpv3user                 |            | 100 |
| Support                                          | and Other                  | Resources  | 103 |
| AccessingArubaSupport                            |                            |            | 103 |
| AccessingUpdates                                 |                            |            | 104 |
|6

Warranty Information
Regulatory Information
Documentation Feedback

104
104
104

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

7

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n Aruba 8400 Switch Series (JL366A, JL363A, JL687A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

example-text

Usage

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

{ }

[ ]

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

Braces. Indicates that at least one of the enclosed items is required.

Brackets. Indicates that the enclosed item or items are optional.

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

8

Convention

… or

...

Usage

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
format: member/slot/port.

On the Aruba 8400 Switch Series

About this document | 9

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/5 and 1/6.

o Line modules are on the front of the switch in slots 1/1 through 1/4, and 1/7 through 1/10.

n port: Physical number of a port on a line module

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

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

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

10

Aruba 8400 switch series member, slot,

Chapter 2

Aruba 8400 switch series member, slot, and port notation

The software notation for describing member, slot, and port information depends on the switch
hardware.

The physical interfaces on the Aruba 8400 Switch Series use the format:
member/slot/port
member

Specifies the chassis number. In this release of the software, the value of member is always 1.

slot

Specifies physical location in the switch chassis.

port

Specifies the physical port on the module.

The slot numbers are unique to each type of component—in contrast to being unique within a chassis.

Line Modules and Management Modules

Line modules are on the front of the switch in slots 1/1 through 1/4 and 1/7 through 1/10.

The number of ports depend on the line module. Line module ports are labeled in software as port or
interface, depending on the context.

For example, interface 1/1/1 is the logical interface associated with the physical interface member 1,
slot 1, port 1.

Management modules are on the front of the switch in slots 1/5 and 1/6.

Figure 1 Aruba 8400 Switch Series line module and management module slots

Power supplies

Power supplies are on the front of the switch behind the bezel above the line modules and management
modules. Power supplies are labeled in software as Member/PSU: 1/1 through 1/4.

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

11

Fan trays

Fan trays are on the rear of the switch and are labeled in software as Member/Tray: 1/1 through 1/3.

Fans

Fans are on the rear of the switch in fan trays and are labeled in software as Member/Tray/Fan:

n 1/1/1 through 1/1/6

n 1/2/1 through 1/2/6

n 1/3/1 through 1/3/6

Fabric modules

Fabric modules are on the rear of the switch, behind the fan trays, in slots 1/1 through 1/3.

Rear display module

The rear display module is on the rear of the switch and is not labeled with a member or slot number.

Aruba 8400 switch series member, slot, and port notation | 12

Monitoring hardware through visual

Chapter 3

Monitoring hardware through visual observation

Confirming normal operation of the switch by reading LEDs

This task describes using the switch LEDs to confirm that the switch is operating normally.

For complete information on LED behaviors for your AOS-CX switch, refer to the Installation and Getting

Started Guide for that switch series, available for download from the Aruba Switch Documentation section of the

Aruba Hardware Documentation and Translations Portal.

Procedure

1. Quick check: Verify that the chassis has power and there are no fault conditions.

On the front of the switch, verify that the states of the following LEDs are On Green:

n Power

n Health
Verify that the Health LEDs of all installed line modules are On Green.

2.

3. Verify that the Health LEDs of all installed management modules are On Green.

4. Verify that the network ports are operating normally.

a. On the active management module, check the Status Front section. Verify that each LED that

indicates a line module is in one of the following states:
n On Green (normal operation)

n Off (no line module installed)

b. On each line module, verify that each port LED is in one of the following states:

n On Green, Half-Bright Green, or Flickering Green (normal operation)

n Off (no cable connected or port off by default in config)

5. Verify that the power supplies are operating normally.

a. On the active management module, check the Status Front section. Verify that each LED that

indicates a power supply is in one of the following states:
n On Green (normal operation)

n Off (no power supply installed)

b. On each power supply, verify that LEDs are in the following states:

n Power LED: On Green

n Fault LED: Off

6. Verify that the rear components are operating normally by checking the Status Rear section of the

active management module:
a. Verify that the LEDs for the fabric modules are in one of the following states:

n On Green (normal operation)

n Off (component not installed)

b. Verify that the LEDs for the fan trays and fans are On Green.

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

13

7. Verifythatthestandbymanagementmoduleisreadytotakeoverastheactivemanagement
module.Onthestandbymanagementmodule,verifythestatesofthefollowingLEDs:
| n HealthLEDisOnGreen.                       |        |        |              |                |       |
| ------------------------------------------- | ------ | ------ | ------------ | -------------- | ----- |
| n Managementstatestandby(Stby)LEDisOnGreen. |        |        |              |                |       |
| Detecting                                   | if the | switch | is not ready | for a failover | event |
ThistaskdescribesusingtheswitchLEDstodetectiftheswitchisnotreadyforthelossofafabric
moduleorforafailoverfromtheactivemanagementmoduletothestandbymanagementmodule.
AlthoughyoucandetectpowersupplyfailuresbyviewingtheLEDs,youmustusesoftwarecommandsto
determineifthepowersupplyredundancyissufficienttopowerthechassisifapowersupplyfails.Forcomplete
informationonLEDbehaviorsforyourAOS-CXswitch,refertotheInstallationandGettingStartedGuidefor
thatswitchseries,availablefordownloadfromtheArubaSwitchDocumentationsectionoftheArubaHardware
DocumentationandTranslationsPortal.
Procedure
1. Detectifthestandbymanagementmoduleisshutdown.
Ifthestandbymanagementmoduleisshutdown,theLEDstatesareasfollows:
| n ThestandbymanagementmodulehealthLEDisOff.       |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- |
| n Thestandbymanagementstateactive(Actv)LEDisOff.  |     |     |     |     |     |
| n Thestandbymanagementstatestandby(Stby)LEDisOff. |     |     |     |     |     |
n OntheactivemanagementmoduleintheStatusFrontManagementModulessection,theLED
forthestandbymanagementmoduleisOff.Forexample,iftheactivemanagementmoduleis
ManagementModuleLED5,ManagementModulesLED6isOff.
2. Detectifthestandbymanagementmoduleisinatransientstate.Ifthestandbymanagement
moduleisbooting,updating,orinanothertransientstate,theLEDstatesareasfollows:
n ThestandbymanagementmodulehealthLEDisSlowFlashGreenwhentheserviceoperating
systemisrunningorduringanoperatingsystemupdate.
n ThestandbymanagementmoduleBootingLEDisSlowFlashGreenwhentheAOS-CX
operatingsystemisbooting.
| n Thestandbymanagementstateactive(Actv)LEDisOff.  |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- |
| n Thestandbymanagementstatestandby(Stby)LEDisOff. |     |     |     |     |     |
n OntheactivemanagementmoduleintheStatusFrontManagementModulessection,theLED
forthestandbymanagementmoduleisSlowFlashGreen.
3. Detectifafabricmoduleisshutdownornotpresent.Ifafabricmoduleisshutdownornot
present,theLEDstatesareasfollows:
n Ontheactivemanagementmodule,intheStatusRearsection,theLEDforthefabricmoduleis
Off.
Onthereardisplaymodule,theLEDforthefabricmoduleisOff.
n
n Onthefabricmodule,thehealthLEDisOff.However,thefabricmoduleisbehindfan1andis
notdirectlyvisible.
| Finding | faulted | components | using | the switch | LEDs |
| ------- | ------- | ---------- | ----- | ---------- | ---- |
ThistaskdescribesusingtheswitchLEDstofindcomponentsthatareinafaultcondition.
Monitoringhardwarethroughvisualobservation|14

All green LEDs—except for chassis power LEDs and the Usr1 LED—are off when the LED mode is set to Light

Faults (The Usr1 LED of the LED Mode section of the active management module is On Green and the default

behavior for the Usr1 LED is being used.). For complete information on LED behaviors for your AOS-CX switch,

refer to the Installation and Getting Started Guide for that switch series, available for download from the

Aruba Switch Documentation section of the Aruba Hardware Documentation and Translations Portal.

Procedure

1. Find the switch that has the fault condition, which is indicated by a chassis health LED in the state

of Slow Flash Orange.

The chassis health LED is located on the front of the switch and on the rear panel of the switch.

2.

If you are at the back of the switch, on the rear panel, look for LEDs that are in the Slow Flash
Orange state:

The Status Rear area has LEDs for power supplies, fabric modules, fan trays, and fans. The
number on the LED represents the unit number of the component.

If the only LED in a state of Slow Flash Orange is the Chassis health LED, go to the front of the
switch.

3. At the front of the switch, on the active management module, look for LEDs that are in the Slow

Flash Orange state:
n The Status Front area has LEDs for power supplies, line and fabric modules, and management

modules. The number on the LED indicates the slot number of the component.

n The Status Rear area has LEDs for fabric modules and fan trays, with a single LED for all the

fans in the fan tray. The number on the LED represents the slot or bay number of the
component.

4. Use the number indicated by the LED that is flashing to locate the slot that contains the faulted

component.

The fabric modules are located behind the fan trays, and the fabric module number corresponds
to the fan tray number.

5. At the front of the switch, on line modules, look for LEDs that are in the Slow Flash Orange state:

Module LEDs and Port LEDs indicate faults if their states are Slow Flash Orange.

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

15

Chapter 4
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
16
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries)

Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideortheMonitoring
Guideforyourswitchmodel.
| Command History     |         |     |         |              |
| ------------------- | ------- | --- | ------- | ------------ |
| Release             |         |     |         | Modification |
| 10.07orearlier      |         |     |         | --           |
| Command Information |         |     |         |              |
| Platforms           | Command |     | context | Authority    |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
| switch# boot | line-module |     | 1/1 |     |
| ------------ | ----------- | --- | --- | --- |
This command will reboot the specified line module and interfaces on this
module will not send or receive packets while the module is down. Any
traffic passing through the line module will be interrupted. Management
sessions connected through the line module will be affected. It might take
up to 2 minutes to complete rebooting the module. During that time, you can
| monitor progress |     | by viewing | the    | event log. |
| ---------------- | --- | ---------- | ------ | ---------- |
| Do you want      | to  | continue   | (y/n)? | y          |
switch#
Bootcommands|17

Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideortheMonitoring
Guideforyourswitchmodel.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
boot management-module
| boot management-module |     | {active | | standby | | <SLOT-ID>} |
| ---------------------- | --- | ------- | --------- | ------------ |
Description
Rebootsthespecifiedmanagementmodule.Choosethemanagementmoduletorebootbyrole(active
orstandby)orbyslotnumber.
| Parameter |     |     | Description                        |     |
| --------- | --- | --- | ---------------------------------- | --- |
| active    |     |     | Selectstheactivemanagementmodule.  |     |
| standby   |     |     | Selectsthestandbymanagementmodule. |     |
<SLOT-ID> Specifiesthememberandslotofthemanagementmoduleinthe
formatmember/slot.Forexample,tospecifythemodulein
member1slot5,enter1/5.
Usage
Thiscommandrebootsasinglemanagementmoduleinachassis.Choosethemanagementmoduleto
rebootbyrole(activeorstandby)orbyslotnumber.
Youcanusetheshow imagescommandtoshowinformationabouttheprimaryandsecondarysystem
images.
Ifyoureboottheactivemanagementmoduleandthestandbymanagementmoduleisavailable,the
activemanagementmodulerebootsandthestandbymanagementmodulebecomestheactive
managementmodule.
Ifyoureboottheactivemanagementmoduleandthestandbymanagementmoduleisnotavailable,
youarewarned,youarepromptedtosavetheconfiguration,andyouarepromptedtoconfirmthe
operation.
Ifyourebootthestandbymanagementmodule,thestandbymanagementmodulerebootsandremains
thestandbymanagementmodule.
Ifyouattempttorebootamanagementmodulethatisnotavailable,thebootcommandisaborted.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 18

Savingtheconfigurationisnotrequired.However,ifyouattempttosavetheconfigurationandthereis
anerrorduringthesaveoperation,thebootcommandisaborted.
HewlettPackardEnterpriserecommendsthatyouusethebootmanagement-modulecommandinsteadof
pressingthemoduleresetbuttontorebootamanagementmodulebecauseifyouarerebootingtheonly
availablemanagementmodule,thebootmanagement-modulecommandenablesyoutosavethe
configuration,cancelthereboot,orboth.
Examples
Rebootingtheactivemanagementmodulewhenthestandbymanagementmoduleisavailable:
| switch# | boot | management-module |     | active |     |     |     |     |
| ------- | ---- | ----------------- | --- | ------ | --- | --- | --- | --- |
The management-module in slot 1/5 is going down for reboot now.
Rebootingtheactivemanagementmodulewhenthestandbymanagementmoduleisnotavailable:
| switch#        | boot       | management-module |              | 1/5     |               |        |             |     |
| -------------- | ---------- | ----------------- | ------------ | ------- | ------------- | ------ | ----------- | --- |
| The management |            | module            | in slot      | 1/5     | is currently  | active | and         | no  |
| standby        | management |                   | module was   | found.  |               |        |             |     |
| This will      | reboot     | the               | entire       | switch. |               |        |             |     |
| Do you         | want       | to save           | the current  |         | configuration | (y/n)? | n           |     |
| This will      | reboot     | the               | entire       | switch  | and render    | it     | unavailable |     |
| until the      | process    |                   | is complete. |         |               |        |             |     |
| Continue       | (y/n)?     | y                 |              |         |               |        |             |     |
| The system     | is         | going             | down for     | reboot. |               |        |             |     |
command,refertotheFundamentalsGuideortheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |         |     |                                                    |     |     |     |
| -------------- | ----------- | ------- | ------- | --- | -------------------------------------------------- | --- | --- | --- |
| Release        |             |         |         |     | Modification                                       |     |     |     |
| 10.07orearlier |             |         |         |     | --                                                 |     |     |     |
| Command        | Information |         |         |     |                                                    |     |     |     |
| Platforms      |             | Command | context |     | Authority                                          |     |     |     |
| 8400           |             |         |         |     | Administratorsorlocalusergroupmemberswithexecution |     |     |     |
Manager(#)
rightsforthiscommand.
| boot management-module |     |     |                |     | (recovery |     | console) |     |
| ---------------------- | --- | --- | -------------- | --- | --------- | --- | -------- | --- |
| boot management-module |     |     | {local|remote} |     |           |     |          |     |
Description
Rebootsthespecifiedmanagementmodulebyspecifiedlocation(localorremote).
Bootcommands|19

| Parameter |     | Description                      |
| --------- | --- | -------------------------------- |
| <local>   |     | Rebootsthelocalmanagementmodule. |
<remote>
Rebootstheremotemanagementmodule.
Usage
Thiscommandrebootsasinglemanagementmoduleinachassis.Choosethemanagementmoduleto
rebootbyrole(activeorstandby)orbyslotnumber.
Youcanusetheshow imagescommandtoshowinformationabouttheprimaryandsecondarysystem
images.
Ifyoureboottheactivemanagementmoduleandthestandbymanagementmoduleisavailable,the
activemanagementmodulerebootsandthestandbymanagementmodulebecomestheactive
managementmodule.
Ifyoureboottheactivemanagementmoduleandthestandbymanagementmoduleisnotavailable,
youarewarned,youarepromptedtosavetheconfiguration,andyouarepromptedtoconfirmthe
operation.
Ifyourebootthestandbymanagementmodule,thestandbymanagementmodulerebootsandremains
thestandbymanagementmodule.
Ifyouattempttorebootamanagementmodulethatisnotavailable,thebootcommandisaborted.
Savingtheconfigurationisnotrequired.However,ifyouattempttosavetheconfigurationandthereis
anerrorduringthesaveoperation,thebootcommandisaborted.
HewlettPackardEnterpriserecommendsthatyouusethebootmanagement-modulecommandinsteadof
pressingthemoduleresetbuttontorebootamanagementmodulebecauseifyouarerebootingtheonly
availablemanagementmodule,thebootmanagement-modulecommandenablesyoutosavethe
configuration,cancelthereboot,orboth.
Examples
Bootingaremotemanagementmodule:
| switch# boot | management-module   | remote            |
| ------------ | ------------------- | ----------------- |
| There is     | no other management | module installed. |
Aborting.
switch#
command,refertotheFundamentalsGuideortheMonitoringGuideforyourswitchmodel.
| Command History     |     |                    |
| ------------------- | --- | ------------------ |
| Release             |     | Modification       |
| 10.12               |     | Commandintroduced. |
| Command Information |     |                    |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 20

Platforms

Command context

Authority

8400

Manager (#)

Administrators or local user group members with execution
rights for this command.

boot set-default
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

For more information on features that use this command, refer to the Fundamentals Guide or the Monitoring
Guide for your switch model.

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution rights
for this command.

boot system
boot system [primary | secondary | serviceos]

Description

Boot commands | 21

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

Selects the secondary operating system image for this reboot and
sets the configured default operating system image to secondary
for future reboots.

Selects the service operating system for this reboot. Does not
change the configured default operating system image. The
service operating system acts as a standalone bootloader and
recovery OS for switches running the AOS-CX operating system
and is used in rare cases when troubleshooting a switch.

This command reboots the entire system. If you do not select one of the optional parameters, the
system reboots from the configured default boot image.

You can use the show images command to show information about the primary and secondary system
images.

Choosing one of the optional parameters affects the setting for the default boot image:

n If you select the primary or secondary optional parameter, that image becomes the configured

default boot image for future system reboots. The command fails if the switch is not able to set the
operating system image to the image you selected.

You can use the boot set-default command to change the configured default operating system image.

n If you select serviceos as the optional parameter, the configured default boot image remains the

same, and the system reboots all management modules with the service operating system.

If the configuration of the switch has changed since the last reboot, when you execute the boot system
command you are prompted to save the configuration and you are prompted to confirm the reboot
operation.

Saving the configuration is not required. However, if you attempt to save the configuration and there is
an error during the save operation, the boot system command is aborted.

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

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

22

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
| Reboot    | aborted.     |               |               |                |
switch#
Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideortheMonitoring
Guideforyourswitchmodel.
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| show boot-history |           |        |          |     |
| ----------------- | --------- | ------ | -------- | --- |
| show boot-history | [all|{vsf | member | <1-10>}] |     |
Description
Showsboothistoryinformation.Whennoparametersarespecified,showsthemostrecentinformation
aboutthecurrentbootoperation,andthethreepreviousbootoperationsfortheswitch.Whentheall
parameterisspecified,theoutputofthiscommandshowsthebootinformationfortheactive
managementmodule.
Forswitchesthatsupportlinemodules(suchas8400switchseries)includingtheallparameterdisplays
informationfortheactivemanagementmoduleandallavailablelinemodules.
Bootcommands|23

To view boot-history on a standby, the command must be sent on the conductor console.

Parameter

all

Description

Optional. Shows boot information for the active management
module. For switches that support line modules, including this
parameter displays information for and all available line modules.

vsf member <1-10>

Optional. Display boot history for the specified VSF member

Usage

This command displays the boot-index, boot-ID, and up time in seconds for the current boot. If there is
a previous boot, it displays boot-index, boot-ID, reboot time (based on the time zone configured in the
system) and reboot reasons. Previous boot information is displayed in reverse chronological order.

The output of this command includes the following information:

Parameter

Index

Boot ID

Current Boot, up for <time>

<Timestamp>: boot reason

Description

The position of the boot in the history file. Range: 0
to 3.

A unique ID for the boot . A system-generated 128-
bit string.

For the current boot, the show boot-history
command shows the number of seconds the
module has been running on the current software.

For previous boot operations, the show boot-
history command shows the time at which the
operation occurred and the reason for the boot.
The reason for the boot is one of the following
values:

n <DAEMON-NAME> crash: The daemon identified

by <DAEMON-NAME> caused the module to boot.

n Kernel crash: The operating system software

associated with the module caused the module

to boot.

n Uncontrolled reboot: The reason for the reboot

is not known.

n Reboot requested through database: The

reboot occurred because of a request made

through the CLI or other API.

Examples

Showing the boot history of the active management module:

switch# show boot-history
Management module
=================

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

24

| Index : | 2                                  |        |     |     |                 |
| ------- | ---------------------------------- | ------ | --- | --- | --------------- |
| Boot ID | : c34a2c2499004a02bbeeff4992e1fdbd |        |     |     |                 |
| Current | Boot, up for                       | 1 days | 13  | hrs | 13 mins 27 secs |
| Index : | 1                                  |        |     |     |                 |
| Boot ID | : bfba9bc486304e57904ac717a0ccbdcd |        |     |     |                 |
02 Sep 23 02:55:33 : CPU request reset with 0x20201, Version: FL.10.14.0000-1619-
ga9ec1805bd442~dirty
| 02 Sep  | 23 02:55:33                        | : Switch | boot | count | is 2 |
| ------- | ---------------------------------- | -------- | ---- | ----- | ---- |
| Index : | 0                                  |          |      |       |      |
| Boot ID | : a88a71b7ca9a4574af7e3b811ddfdc7e |          |      |       |      |
02 Sep 23 02:49:26 : Reboot requested by user, Version: FL.10.14.0000-1619-
ga9ec1805bd442~dirty
| 02 Sep  | 23 02:50:02                        | : Switch | boot | count | is 1 |
| ------- | ---------------------------------- | -------- | ---- | ----- | ---- |
| Index : | 3                                  |          |      |       |      |
| Boot ID | : f00ba10c8c44457f83fee303d014a89a |          |      |       |      |
25 Aug 23 10:27:42 : Power on reset with 0x1, Version: FL.10.14.0000-1465-
g9df95249d06b0~dirty
| 25 Aug | 23 10:28:18 | : Switch | boot | count | is 3 |
| ------ | ----------- | -------- | ---- | ----- | ---- |
25 Aug 23 10:29:02 : Primary overtemperature fault detected with 0x2 in PSU 1/1
Showingtheboothistoryoftheactivemanagementmoduleandalllinemodules:
switch#
| Management | module |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- |
=================
| Index :     | 3                                  |          |           |      |                  |
| ----------- | ---------------------------------- | -------- | --------- | ---- | ---------------- |
| Boot ID     | : f1bf071bdd04492bbf8439c6e479d612 |          |           |      |                  |
| Current     | Boot, up for                       | 22 hrs   | 12        | mins | 22 secs          |
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
| Management | module |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- |
=================
| Index : | 3                                  |          |           |      |                  |
| ------- | ---------------------------------- | -------- | --------- | ---- | ---------------- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |          |           |      |                  |
| Current | Boot, up for                       | 22 hrs   | 12        | mins | 22 secs          |
| Index : | 2                                  |          |           |      |                  |
| Boot ID | : edfa2d6598d24e989668306c4a56a06d |          |           |      |                  |
| 07 Aug  | 18 16:28:01                        | : Reboot | requested |      | through database |
Bootcommands|25

| Index :     | 1                                  |                    |                  |
| ----------- | ---------------------------------- | ------------------ | ---------------- |
| Boot ID     | : 0bda8d0361df4a7e8e3acdc1dba5caad |                    |                  |
| 07 Aug      | 18 14:08:46                        | : Reboot requested | through database |
| Index :     | 0                                  |                    |                  |
| Boot ID     | : 23da2b0e26d048d7b3f4b6721b69c110 |                    |                  |
| 07 Aug      | 18 13:00:46                        | : Reboot requested | through database |
| Line module | 1/1                                |                    |                  |
=================
| Index : | 3           |              |         |
| ------- | ----------- | ------------ | ------- |
| 10 Aug  | 17 12:45:46 | : dune_agent | crashed |
...
Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideortheMonitoring
Guideforyourswitchmodel.
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 26

Chapter 5
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
| Parameter   |     |     | Description                                |     |
| ----------- | --- | --- | ------------------------------------------ | --- |
| <IPV4-ADDR> |     |     | SpecifiestheNASserverIPv4address,Global.   |     |
| <IPV6-ADDR> |     |     | SpecifiestheIPv6addressoftheNASserver.     |     |
| <HOSTNAME>  |     |     | SpecifiesthehostnameoftheNASserver.String. |     |
Examples
CreatingthelogfilesstoragevolumewithIPaddress10.1.1.1:
27
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries)

| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)#
address 10.1.1.1
Deletinganexternalstoragevolumenamedlogfiles:
| switch(config)#                           | external-storage |     | logfiles   |          |
| ----------------------------------------- | ---------------- | --- | ---------- | -------- |
| switch(config-external-storage-logfiles)# |                  |     | no address | 10.1.1.1 |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8400 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
memberswithexecutionrightsforthis
command.
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
| switch(config)#                           | external-storage |     | logfiles     |       |
| ----------------------------------------- | ---------------- | --- | ------------ | ----- |
| switch(config-external-storage-logfiles)# |                  |     | no directory | /home |
Externalstorage|28

Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |              |           |
| -------------- | ----------- | ------- | ------------ | --------- |
| Release        |             |         | Modification |           |
| 10.07orearlier |             |         | --           |           |
| Command        | Information |         |              |           |
| Platforms      | Command     | context |              | Authority |
8400 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
usergroupmemberswithexecution
rightsforthiscommand.Operatorscan
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
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |              |           |
| -------------- | ----------- | ------- | ------------ | --------- |
| Release        |             |         | Modification |           |
| 10.07orearlier |             |         | --           |           |
| Command        | Information |         |              |           |
| Platforms      | Command     | context |              | Authority |
config-external-storage-<VOLUME-NAME>
| 8400 |     |     |     | OperatorsorAdministratorsorlocal |
| ---- | --- | --- | --- | -------------------------------- |
usergroupmemberswithexecution
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 29

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
rightsforthiscommand.Operatorscan
executethiscommandfromthe
operatorcontext(>)only.
| enable | (external-storage |     | logfiles) |     |
| ------ | ----------------- | --- | --------- | --- |
enable
no enable
Description
Enablestheexternalstoragevolume.
Thenoformofthiscommanddisablestheexternalstoragevolume.Thisisidenticaltothedisable
command.
Examples
Creatingandthenenablingavolumenamedlogfiles:
| switch(config)# |     | external-storage | logfiles |     |
| --------------- | --- | ---------------- | -------- | --- |
switch(config-external-storage-logfiles)# enable
Disablestheexternalstoragevolume:
| switch(config)# |     | external-storage | logfiles |     |
| --------------- | --- | ---------------- | -------- | --- |
switch(config-external-storage-logfiles)# disable
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |              |           |
| -------------- | ----------- | ------- | ------------ | --------- |
| Release        |             |         | Modification |           |
| 10.07orearlier |             |         | --           |           |
| Command        | Information |         |              |           |
| Platforms      | Command     | context |              | Authority |
8400 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
usergroupmemberswithexecution
rightsforthiscommand.Operatorscan
executethiscommandfromthe
operatorcontext(>)only.
external-storage
| external-storage    |     | <VOLUME-NAME> |     |     |
| ------------------- | --- | ------------- | --- | --- |
| no external-storage |     | <VOLUME-NAME> |     |     |
Description
Externalstorage|30

Createsorupdatesanexternalstoragevolume.
Thenoformofthiscommanddeletesanexternalstoragevolume.
Examples
Creatingthelogfilesstoragevolume:
| switch(config)# |     | external-storage |     | logfiles |
| --------------- | --- | ---------------- | --- | -------- |
switch(config-external-storage-logfiles)#
Deletingthelogfilesstoragevolume:
| switch(config)# |     | no  | external-storage | logfiles |
| --------------- | --- | --- | ---------------- | -------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |     |         |              |
| -------------- | ----------- | --- | ------- | ------------ |
| Release        |             |     |         | Modification |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| password    | (external-storage) |     |               |             |
| ----------- | ------------------ | --- | ------------- | ----------- |
| password    | [{plaintext        | |   | ciphertext}   | <PASSWORD>] |
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
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 31

| switch(config)# | external-storage |     | logfiles |     |     |     |
| --------------- | ---------------- | --- | -------- | --- | --- | --- |
switch(config-external-storage-logfiles)#
|     |     |     |     | password | plaintext | Xj#9 |
| --- | --- | --- | --- | -------- | --------- | ---- |
Creatingavolumenamedbak1withapromptedplaintextpassword:
| switch(config)#                       | external-storage |           | bak1       |     |     |     |
| ------------------------------------- | ---------------- | --------- | ---------- | --- | --- | --- |
| switch(config-external-storage-bak1)# |                  |           | password   |     |     |     |
| Enter the                             | NAS server       | password: | ********** |     |     |     |
| Re-Enter                              | the NAS server   | password: | ********** |     |     |     |
Clearingthepasswordforvolumelogfiles:
| switch(config)# | external-storage |     | logfiles |     |     |     |
| --------------- | ---------------- | --- | -------- | --- | --- | --- |
switch(config-external-storage-logfiles)#
|     |     |     |     | no password | plaintext | Xj#9 |
| --- | --- | --- | --- | ----------- | --------- | ---- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |              |     |           |     |
| -------------- | ----------- | ------- | ------------ | --- | --------- | --- |
| Release        |             |         | Modification |     |           |     |
| 10.07orearlier |             |         | --           |     |           |     |
| Command        | Information |         |              |     |           |     |
| Platforms      | Command     | context |              |     | Authority |     |
8400 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
memberswithexecutionrightsforthis
command.
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
Externalstorage|32

|     |     | Address | VRF | Username | Type | Directory | State |
| --- | --- | ------- | --- | -------- | ---- | --------- | ----- |
----------------------------------------------------------------------------------
--
| nfsvol |     | 10.1.1.1 | nas | --- | NFSv3 | /home |     |
| ------ | --- | -------- | --- | --- | ----- | ----- | --- |
operational
| nfsfiles |     | 20.1.1.1  | nas | netstorage | NFSv4 | /netstor | disabled |
| -------- | --- | --------- | --- | ---------- | ----- | -------- | -------- |
| scpdev   |     | nasserver | nas | scpstor    | SCP   | /scp     |          |
unaccessible
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |         |              |     |     |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- | --- | --- |
| Release        |             |         |         | Modification |     |     |     |
| 10.07orearlier |             |         |         | --           |     |     |     |
| Command        | Information |         |         |              |     |     |     |
| Platforms      |             | Command | context | Authority    |     |     |     |
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
(#)
| show                | running-config |                  | external-storage |     |     |     |     |
| ------------------- | -------------- | ---------------- | ---------------- | --- | --- | --- | --- |
| show running-config |                | external-storage |                  |     |     |     |     |
Description
Showstherunningconfigurationoftheexternalstorage.
Examples
| switch#          | show      | running-config |     | external-storage |     |     |     |
| ---------------- | --------- | -------------- | --- | ---------------- | --- | --- | --- |
| external-storage |           | nfsvol         |     |                  |     |     |     |
|                  | address   | 10.1.1.1       |     |                  |     |     |     |
|                  | vrf       | nas            |     |                  |     |     |     |
|                  | type      | nfsv4          |     |                  |     |     |     |
|                  | directoty | /home          |     |                  |     |     |     |
enable
| external-storage |           | scpdev     |     |     |     |     |     |
| ---------------- | --------- | ---------- | --- | --- | --- | --- | --- |
|                  | address   | 30.1.1.1   |     |     |     |     |     |
|                  | vrf       | nas        |     |     |     |     |     |
|                  | username  | switchuser |     |     |     |     |     |
|                  | password  | ciphertext |     | xxx |     |     |     |
|                  | type      | scp        |     |     |     |     |     |
|                  | directoty | /home      |     |     |     |     |     |
enable
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 33

| Command        | History     |     |         |              |
| -------------- | ----------- | --- | ------- | ------------ |
| Release        |             |     |         | Modification |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
|                | (#)     |          |        | rightsforthiscommand. |
| -------------- | ------- | -------- | ------ | --------------------- |
| type (external |         | storage) |        |                       |
| type {nfsv3    | | nfsv4 | |        | scp}   |                       |
| no type {nfsv3 | |       | nfsv4    | | scp} |                       |
Description
Setsthenetworkattachedstorageaccesstypeforreachingtheexternalstoragevolume.
Thenoformofthiscommanddeletesanexternalstoragevolume.
| Parameter |     |     |     | Description                             |
| --------- | --- | --- | --- | --------------------------------------- |
| nfsv3     |     |     |     | SpecifiestheNFSv3networkaccessprotocol. |
nfsv4
SpecifiestheNFSv4networkaccessprotocol.
| scp |     |     |     | SpecifiestheSCPnetworkaccessprotocol. |
| --- | --- | --- | --- | ------------------------------------- |
Examples
CreatingthelogfilesvolumeusingNFSV4:
| switch(config)# |     | external-storage |     | logfiles |
| --------------- | --- | ---------------- | --- | -------- |
switch(config-external-storage-logfiles)# type nfsv4
Clearingtheexternalstorageaccesstype:
| switch(config)# |     | external-storage |     | logfiles |
| --------------- | --- | ---------------- | --- | -------- |
switch(config-external-storage-logfiles)#
no type nfsv4
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History |     |     |              |
| -------------- | ------- | --- | --- | ------------ |
| Release        |         |     |     | Modification |
| 10.07orearlier |         |     |     | --           |
Externalstorage|34

| Command   | Information |         |     |           |
| --------- | ----------- | ------- | --- | --------- |
| Platforms | Command     | context |     | Authority |
config-external-storage-<VOLUME-NAME>
| 8400 |     |     |     | Administratorsorlocalusergroup |
| ---- | --- | --- | --- | ------------------------------ |
memberswithexecutionrightsforthis
command.
| username             | (external   | storage) |     |     |
| -------------------- | ----------- | -------- | --- | --- |
| username <USER-NAME> |             |          |     |     |
| no username          | <USER-NAME> |          |     |     |
Description
Setstheusernameforloggingintoanetworkattachedstorageserver.
Thenoformofthiscommandclearsausername.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<USER-NAME>
Specifiestheusername.
Examples
Creatingavolumenamedlogfileswiththeusernamenassuser:
| switch(config)#                           | external-storage |     | logfiles |         |
| ----------------------------------------- | ---------------- | --- | -------- | ------- |
| switch(config-external-storage-logfiles)# |                  |     | username | nasuser |
Clearingtheusernamenasuserfromaccessingthelogfilesvolume:
| switch(config)#                           | external-storage |     | logfiles    |         |
| ----------------------------------------- | ---------------- | --- | ----------- | ------- |
| switch(config-external-storage-logfiles)# |                  |     | no username | nasuser |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |              |           |
| -------------- | ----------- | ------- | ------------ | --------- |
| Release        |             |         | Modification |           |
| 10.07orearlier |             |         | --           |           |
| Command        | Information |         |              |           |
| Platforms      | Command     | context |              | Authority |
8400 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
memberswithexecutionrightsforthis
command.
| vrf (external | storage) |     |     |     |
| ------------- | -------- | --- | --- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 35

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
| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)# vrf nas
ClearingaccessofaVRFnamednastothenetworkattachedstorage:
| switch(config)#                           | external-storage |     | logfiles   |     |
| ----------------------------------------- | ---------------- | --- | ---------- | --- |
| switch(config-external-storage-logfiles)# |                  |     | no vrf nas |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8400 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
memberswithexecutionrightsforthis
command.
Externalstorage|36

Chapter 6

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

n Maximum sessions: IP-SLA source 500, IP-SLA responder 500.

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

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

37

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

Selects HTTP request type as get or raw where the
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

IP-SLA | 38

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
604800.
version <VERSION-NUMBER> SpecifiesthesourceinterfacetouseforsendingIP-SLA
probes.
| http-raw-request | <RAW-PAYLOAD> |     | HTTPrawrequest.String. |
| ---------------- | ------------- | --- | ---------------------- |
Examples
switch(config-ipsla-1)# http get http://device.arubanetworks.com/root/home.html
switch(config-ipsla-1)# http raw http://device.arubanetworks.com/root/home.html
| switch(config-ipsla-1)# |     | http 2.2.2.2 | source 1/1/1 |
| ----------------------- | --- | ------------ | ------------ |
switch(config-ipsla-1)# http http://device.arubanetworks.com source 2.2.2.1
switch(config-ipsla-1)# http http://device.arubanetworks.com/root/home.html
| source-interface | 1/1/1 |     |     |
| ---------------- | ----- | --- | --- |
switch(config-ipsla-1)# http http://device.arubanetworks.com name-server
10.10.10.2
switch(config-ipsla-1)# http raw raw-request "GET /en/US/hmpgs/index.html
HTTP/1.0\r\n\r\n"
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
https
https {get | raw} URL [source {<SOURCE-IPV4-ADDR> | <IFNAME>} source-port <PORT-NUM>]
[proxy proxy-url] [cache disable] [name-server <IPV4-ADDR-DNS-SERVER>]
[probe-interval <<PROBE-INTERVAL>>] [version <VERSION-NUMBER>] [https-raw-request
<RAW-PAYLOAD>]
no https {get | raw} URL [source {<SOURCE-IPV4-ADDR> | <IFNAME>} source-port <PORT-NUM>]
[proxy proxy-url] [cache disable] [name-server <IPV4-ADDR-DNS-SERVER>]
[probe-interval <<PROBE-INTERVAL>>] [version <VERSION-NUMBER>] [https-raw-request
<RAW-PAYLOAD>]
Description
ConfiguresHTTPSastheIP-SLAtestmechanism.RequiresdestinationURLandtypeofHTTPSrequest
(get/raw).
Thenoformofthiscommandremovestheconfiguration.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 39

ForHTTPSIP-SLAsessions,itisnotrequiredtoinstallacertificateontheswitch.
| Parameter   |     | Description                               |     |
| ----------- | --- | ----------------------------------------- | --- |
| {get | raw} |     | SelectsHTTPSrequesttypeasgetorrawwherethe |     |
systemwillgenerateorprovideHTTPSpayload.
URL
SpecifiesHTTPSURLaddressofsyntax.https://<HOST
NAME/IP-ADDRESS>:<PORT>/<PATH>.
source {<SOURCE-IPV4-ADDR> | <IFNAME>} SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
source-port <PORT-NUM> SpecifiesthevalueofthesourceportfortheIP-SLA
probes.
cache disable SelectscacheoptionfortheHTTPSserver.Bydefaultthe
optionisenabled.
name-server <IPV4-ADDR-DNS-SERVER> SpecifiestheIPv4addressofDNSserver.
| probe-interval | <PROBE-INTERVAL> |     |     |
| -------------- | ---------------- | --- | --- |
Specifiestheprobeintervalinseconds.Range:30to
604800.
version <VERSION-NUMBER> SpecifiesthesourceinterfacetouseforsendingIP-SLA
probes.
| https-raw-request | <RAW-PAYLOAD> | HTTPSrawrequest.String. |     |
| ----------------- | ------------- | ----------------------- | --- |
Examples
switch(config-ipsla-1)# https get https://device.arubanetworks.com/root/home.html
| switch(config-ipsla-1)# | https get | https://2.2.2.2 | source 1/1/1 |
| ----------------------- | --------- | --------------- | ------------ |
switch(config-ipsla-1)# https get https://device.arubanetworks.com source 2.2.2.1
switch(config-ipsla-1)# https get https://device.arubanetworks.com/root/home.html
| source-interface | 1/1/1 |     |     |
| ---------------- | ----- | --- | --- |
switch(config-ipsla-1)# https get https://device.arubanetworks.com name-server
10.10.10.2
switch(config-ipsla-1)# https raw https://device.arubanetworks.com/root/home.html
| raw-request “GET | /en/US/hmpgs/index.html” |     |     |
| ---------------- | ------------------------ | --- | --- |
switch(config-ipsla-1)# no https get https://2.2.2.2 source 1/1/1
| switch(config-ipsla-1)# | no https | raw |     |
| ----------------------- | -------- | --- | --- |
https://device.arubanetworks.com/root/home.html raw-request “GET
/en/US/hmpgs/index.html”
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
Command History
| Release    |     | Modification       |     |
| ---------- | --- | ------------------ | --- |
| 10.12.1000 |     | Commandintroduced. |     |
Command Information
IP-SLA|40

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
icmp-echo
icmp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} [source {<SOURCE-IPV4-ADDR> | <IFNAME>}]
[name-server <IPV4-ADDR-DNS-SERVER>] [payload-size <PAYLOAD-SIZE>]
| [tos <TYPE-OF-SERVICE>] |     | [probe-interval | <PROBE-INTERVAL>] |     |
| ----------------------- | --- | --------------- | ----------------- | --- |
Description
ConfiguresICMPechoastheIP-SLAtestmechanism.RequiresdestinationaddressfortheIP-SLAtest.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
{<DEST-IPV4-ADDR> | <HOSTNAME>} SelectsthedestinationIPv4addressfortheIP-SLAor
thehostnameofthedestination.
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
| name-server | <IPV4-ADDR-DNS-SERVER> |     |     |     |
| ----------- | ---------------------- | --- | --- | --- |
SpecifiestheDNSserverfordestinationhostname
resolution.
payload-size <PAYLOAD-SIZE> SpecifiesthepayloadsizeofanSLAprobe.Range:0to
1440.
tos <TYPE-OF-SERVICE> Specifiesthetypeofservetobeusedintheprobe
packets.Range:0to255.
probe-interval <PROBE-INTERVAL> Specifiestheprobeintervalinseconds.Range:5to
604800.
Examples
| switch(config)#             | ip-sla | test      |         |                |
| --------------------------- | ------ | --------- | ------- | -------------- |
| switch(config-ip-sla-test)# |        | icmp-echo | 2.2.2.2 |                |
| switch(config-ip-sla-test)# |        | icmp-echo | 2.2.2.2 | source 3.3.3.3 |
switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
| name-server | 4.4.4.4 |     |     |     |
| ----------- | ------- | --- | --- | --- |
switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
| name-server | 4.4.4.4 | probe-interval | 80  |     |
| ----------- | ------- | -------------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |     |     |              |     |
| ------------------- | --- | --- | ------------ | --- |
| Release             |     |     | Modification |     |
| 10.07orearlier      |     |     | --           |     |
| Command Information |     |     |              |     |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 41

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
ip-sla
ip-sla <IP-SLA-NAME>
| no ip-sla <IP-SLA-NAME> |     |     |     |     |
| ----------------------- | --- | --- | --- | --- |
Description
CreatesanIPServiceLevelAgreement(SLA)profileandswitchestotheconfig-ip-slacontext.
ThenoformofthiscommanddeletesanIP-SLAprofile.Bydefault,allprofileusethedefaultVRF
(default).
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IP-SLA-NAME> SpecifiesanIP-SLAprofilename.Length:1to64characters.
Examples
CreatinganIP-SLA:
| switch(config)# | ip-sla | 1   |     |     |
| --------------- | ------ | --- | --- | --- |
switch(config-ip-sla-1)#
DeletinganIP-SLA:
| switch(config)# | no  | ip-sla 1 |     |     |
| --------------- | --- | -------- | --- | --- |
switch(config)#
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip-sla responder
ip-sla responder <SLA-NAME> (udp-echo | tcp-connect | udp-jitter-voip) <PORT-NUM>
{source {< {A.B.C.D | A:B::C:D> | <IFNAME>}|[vrf <VRF-NAME>]{ipv6}
IP-SLA|42

no ip-sla responder <SLA-NAME> (udp-echo | tcp-connect | udp-jitter-voip) <PORT-NUM>

{source {< {A.B.C.D | A:B::C:D> | <IFNAME>}|[vrf <VRF-NAME>]{ipv6}

Description

Selects the IP-SLA responder. The responder can be configured for udp-echo, tcp-connect, udp-jitter-
voip type. It requires the SLA name, SLA type, and port number as arguments.

The no form of this command removes the IP-SLA responder.

Parameter

<SLA-NAME>

udp-echo

tcp-connect

vrf <VRF-NAME>

udp-jitter-voip

<PORT-NUM>

[source {<SOURCE-IPV4-ADDR> | <IFNAME>}]

[source {<SOURCE-IPV6-ADDR> | <IFNAME>}]

Description

Specifies the SLA name. Length: 1 to 64 characters.

Enables responder for udp-echo probes.

Selects TCP connect as the IP-SLA test mechanism.

Specifies the name of the VRF to use.

Selects VOIP jitter as the IP-SLA test mechanism.

Specifies the port number to listen for IP-SLA probes.
Range: 1 to 65535.

Selects the source IPv4 address for SLA probes or the
source interface to use for sending IP-SLA probes.

Selects the source IPv6 address for SLA probes or the
source interface to use for sending IP-SLA probes.

Usage

The IPv6 keyword is required if an IPv6 address is being used by the source interface or VRF. Otherwise,
by default, it will be considered as an IPv4 address.

Examples

switch(config)# ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
switch(config)# ip-sla responder SLA1 udp-echo 8000 source 1/1/1

switch(config)# no ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2

switch(config)#ip-sla responder <SLA-NAME> udp-jitter-voip 1025 vrf <VRF>
switch(config)#ip-sla responder <SLA-NAME> udp-echo 8000 source 1002::1
switch(config)#ip-sla responder <SLA-NAME> udp-echo 8000 source 1/1/1 ipv6
switch(config)#ip-sla responder <SLA-NAME> udp-jitter-voip 1025 vrf <VRF> ipv6

For more information on features that use this command, refer to the Monitoring Guide for your switch model.

Command History

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

43

Release

10.15

Modification

Added ipv6 parameter.

10.07 or earlier

--

Command Information

Platforms

Command context

Authority

8400

config

Administrators or local user group members with execution
rights for this command.

show ip-sla responder
show ip-sla responder <SLA-NAME>

Description

Shows the given IP-SLA responder configuration and operation status.

Parameter

<SLA-NAME>

Examples

Description

Specifies the SLA name.

switch(config)# show ip-sla responder SLA3

SLA Name
IP-SLA Type
VRF
Responder Port
Responder IP
Responder Interface : 1/1/1
Responder Status

: SLA3
: Udp-echo
: Default
: 8000
: 2.2.2.3

: Running

switch(config)# show ip-sla responder 1

: 1 (non-persistent)
SLA Name
: udp-echo
SLA Type
: default
VRF Name
: 10
Responder Port
Responder IP
:
Responder Interface :
Responder Status

: Running

For more information on features that use this command, refer to the Monitoring Guide for your switch model.

Command History

Release

10.07 or earlier

Modification

--

IP-SLA | 44

| Command   | Information |         |         |           |     |
| --------- | ----------- | ------- | ------- | --------- | --- |
| Platforms |             | Command | context | Authority |     |
config
| 8400 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
| show | ip-sla | responder | results |     |     |
| ---- | ------ | --------- | ------- | --- | --- |
show ip-sla responder <SLA-NAME> <SOURCE-IPV4-ADDR> <PORT-NUM> results
Description
Showsthegivenip-slaresponderstatisticsforagivensourceIPandport.Thiscommandisonly
applicableforthesourceswheresourceIPandportareconfigured.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<SLA-NAME>
SpecifiestheSLAname.
| <SOURCE-IPV4-ADDR> |     |     |     | SpecifiesthesourceIPV4address. |     |
| ------------------ | --- | --- | --- | ------------------------------ | --- |
<PORT-NUM>
Specifiestheportnumber.Range:1to65535.
Examples
| switch# |           | show ip-sla | responder  | SLA1 2.2.2.1 | 8000 results |
| ------- | --------- | ----------- | ---------- | ------------ | ------------ |
|         | IP-SLA    | Type        | : Udp-echo |              |              |
|         | VRF       | Name        | : Default  |              |              |
|         | Source    | IP          | : 2.2.2.1  |              |              |
|         | Source    | Port        | : 8000     |              |              |
|         | Responder | Port        | : 8888     |              |              |
|         | Responder | IP          | : 2.2.2.3  |              |              |
|         | Responder | Interface   | :          |              |              |
|         | Responder | Status      | : Running  |              |              |
|         | Packets   | Received    | : 2        |              |              |
|         | Packets   | Sent        | : 2        |              |              |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |         |              |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- |
| Release        |             |         |         | Modification |     |
| 10.07orearlier |             |         |         | --           |     |
| Command        | Information |         |         |              |     |
| Platforms      |             | Command | context | Authority    |     |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 45

| show | ip-sla             |     |     |           |        |     |     |
| ---- | ------------------ | --- | --- | --------- | ------ | --- | --- |
| show | ip-sla {<SLA-NAME> |     |     | [results] | | all} |     |     |
Description
ShowsthegivenIP-SLAsourceconfigurationandstatus.
| Parameter  |     |     |     |     | Description          |     |     |
| ---------- | --- | --- | --- | --- | -------------------- | --- | --- |
| <SLA-NAME> |     |     |     |     | SpecifiestheSLAname. |     |     |
results
ShowsthestatisticscalculatedforanSLAtype.
| all |     |     |     |     | Showsallip-slasourceconfigurationsandstatus. |     |     |
| --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- |
Examples
| switch# | show         | ip-sla     | xyz            | results  |             |               |             |
| ------- | ------------ | ---------- | -------------- | -------- | ----------- | ------------- | ----------- |
|         | IP-SLA       | session    | status         |          |             |               |             |
|         | IP-SLA       | Name       |                |          |             | : xyz         |             |
|         | IP-SLA       | Type       |                |          |             | : tcp-connect |             |
|         | Destination  |            | Host           | Name/IP  | Address:    | 2.2.2.1       |             |
|         | Destination  |            | Port           |          |             | : 8888        |             |
|         | Source       | IP         | Address/IFName |          |             | : 2.2.2.2     |             |
|         | Source       | Port       |                |          |             | : 5555        |             |
|         | Status       |            |                |          |             | : running     |             |
|         | IP-SLA       | session    | cumulative     |          | counters    |               |             |
|         | Total        | Probes     | Transmitted    |          |             | : 1           |             |
|         | Probes       | Timed-out  |                |          |             | : 0           |             |
|         | Bind         | Error      |                |          |             | : 0           |             |
|         | Destination  |            | Address        |          | Unreachable | : 0           |             |
|         | DNS          | Resolution |                | Failures |             | : 0           |             |
|         | Reception    |            | Error          |          |             | : 0           |             |
|         | Transmission |            | Error          |          |             | : 0           |             |
|         | IP-SLA       | Latest     | Probe          | Results  |             |               |             |
|         | Last         | Probe      | Time           |          |             | : 2018 Jul    | 13 02:00:35 |
|         | Packets      |            | Sent           |          |             | : 1           |             |
|         | Packets      |            | Received       |          |             | : 1           |             |
|         | Packet       | Loss       | in             | Test     |             | : 0.0000%     |             |
|         | Minimum      | RTT(ms)    |                |          |             | : 12          |             |
|         | Maximum      | RTT(ms)    |                |          |             | : 12          |             |
|         | Average      | RTT(ms)    |                |          |             | : 12          |             |
|         | DNS RTT(ms)  |            |                |          |             | : 0           |             |
|         | TCP RTT(ms)  |            |                |          |             | : 12          |             |
switch(config)#
|     |        |                   | show   | ip-sla | xyz           |     |     |
| --- | ------ | ----------------- | ------ | ------ | ------------- | --- | --- |
|     | IP-SLA | Name              |        |        | : xyz         |     |     |
|     | Status |                   |        |        | : scheduled   |     |     |
|     | IP-SLA | Type              |        |        | : tcp-connect |     |     |
|     | VRF    |                   |        |        | : ipslasrc    |     |     |
|     | Source | Port              |        |        | : 5555        |     |     |
|     | Source | IP                |        |        | : 2.2.2.2     |     |     |
|     | Source | Interface         |        |        | :             |     |     |
|     | Domain | Name              | Server |        | :             |     |     |
|     | Probe  | interval(seconds) |        |        | : 90          |     |     |
IP-SLA|46

switch(config)#
|                 |                         |            | show ip-sla    | jitter-sla        | results           |              |            |     |
| --------------- | ----------------------- | ---------- | -------------- | ----------------- | ----------------- | ------------ | ---------- | --- |
|                 | IP-SLA                  | session    | status         |                   |                   |              |            |     |
|                 | IP-SLA                  | Name       |                |                   | : jitter-sla      |              |            |     |
|                 | IP-SLA                  | Type       |                |                   | : udp-jitter-voip |              |            |     |
|                 | Destination             |            | Host Name/IP   | Address:          | 2.2.2.1           |              |            |     |
|                 | Destination             |            | Port           |                   | : 8888            |              |            |     |
|                 | Source                  | IP         | Address/IFName |                   | :                 |              |            |     |
|                 | Source                  | Port       |                |                   | : 5555            |              |            |     |
|                 | Status                  |            |                |                   | : running         |              |            |     |
|                 | IP-SLA                  | Session    | Cumulative     | Counters          |                   |              |            |     |
|                 | Total                   | Probes     | Transmitted    |                   | : 1               |              |            |     |
|                 | Probes                  | Timed-out  |                |                   | : 0               |              |            |     |
|                 | Bind                    | Error      |                |                   | : 0               |              |            |     |
|                 | Destination             |            | Address        | Unreachable       | : 0               |              |            |     |
|                 | DNS                     | Resolution | Failures       |                   | : 0               |              |            |     |
|                 | Reception               |            | Error          |                   | : 0               |              |            |     |
|                 | Transmission            |            | Error          |                   | : 0               |              |            |     |
|                 | IP-SLA                  | Latest     | Probe Results  |                   |                   |              |            |     |
|                 | Last                    | Probe      | Time           |                   | : 2018 Jul        | 13           | 02:02:48   |     |
|                 | Packets                 | Sent       |                |                   | : 1               |              |            |     |
|                 | Packets                 | Received   |                |                   | : 1               |              |            |     |
|                 | Packet                  | Loss       | in Test        |                   | : 0.0000%         |              |            |     |
|                 | Minimum                 | RTT(ms)    |                |                   | : 1               |              |            |     |
|                 | Maximum                 | RTT(ms)    |                |                   | : 1               |              |            |     |
|                 | Average                 | RTT(ms)    |                |                   | : 1               |              |            |     |
|                 | DNS                     | RTT(ms)    |                |                   | : 0               |              |            |     |
|                 | Min                     | Positive   | SD             |                   | : 1               | Min Positive | DS         | : 2 |
|                 | Max                     | Positive   | SD             |                   | : 1               | Max Positive | DS         | : 2 |
|                 | Positive                |            | SD Number      |                   | : 2               | Positive     | DS Number  | : 2 |
|                 | Positive                |            | SD Sum         |                   | : 2               | Positive     | DS Sum     | : 4 |
|                 | Positive                |            | SD Average     |                   | : 5               | Positive     | DS Average | : 5 |
|                 | Min                     | Negative   | SD             |                   | : 1               | Min Negative | DS         | : 1 |
|                 | Max                     | Negative   | SD             |                   | : 1               | Max Negative | DS         | : 1 |
|                 | Negative                |            | SD Number      |                   | : 2               | Negative     | DS Number  | : 4 |
|                 | Negative                |            | SD Sum         |                   | : 2               | Negative     | DS Sum     | : 4 |
|                 | Negative                |            | SD Average     |                   | : 5               | Negative     | DS Average | : 5 |
|                 | Max                     | SD Delay   |                |                   | : 0               | Max DS       | Delay      | : 0 |
|                 | Min                     | SD Delay   |                |                   | : 0               | Min DS       | Delay      | : 0 |
|                 | Average                 | SD         | Delay          |                   | : 0               | Average      | DS Delay   | : 0 |
|                 | Voice Scores:           |            |                |                   |                   |              |            |     |
|                 | MOS                     | Score      |                |                   | : 4.38            | ICPIF        |            | : 0 |
| switch(config)# |                         |            | show ip-sla    | m3op              |                   |              |            |     |
|                 | IP-SLA                  | Name       |                | : jitter-sla      |                   |              |            |     |
|                 | Status                  |            |                | : running         |                   |              |            |     |
|                 | IP-SLA                  | Type       |                | : udp-jitter-voip |                   |              |            |     |
|                 | VRF                     |            |                | : ipslasrc        |                   |              |            |     |
|                 | Source                  | IP         |                | : 2.2.2.2         |                   |              |            |     |
|                 | Source                  | Interface  |                | :                 |                   |              |            |     |
|                 | Domain                  | Name       | Server         | :                 |                   |              |            |     |
|                 | TOS                     |            |                | : 10              |                   |              |            |     |
|                 | Probe Interval(seconds) |            |                | : 90              |                   |              |            |     |
|                 | Advantage               | Factor     |                | : 0               |                   |              |            |     |
|                 | Codec Type              |            |                | : g711a           |                   |              |            |     |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 47

| switch(config)# |                   | show ip-sla         | https-sla         |                        |             |
| --------------- | ----------------- | ------------------- | ----------------- | ---------------------- | ----------- |
| SLA             | Name              |                     | : https-sla       |                        |             |
| Status          |                   |                     | : running         |                        |             |
| SLA             | Type              |                     | : https           |                        |             |
| VRF             |                   |                     | : default         |                        |             |
| Source          | Port              |                     | : 1027            |                        |             |
| Source          | IP                |                     | : 1.1.1.1         |                        |             |
| Source          | Interface         |                     | :                 |                        |             |
| Domain          | Name              | Server              | :                 |                        |             |
| Probe           | Interval(seconds) |                     | : 60              |                        |             |
| HTTPS           | Request           | Type                | : raw             |                        |             |
| HTTPS           | URL               |                     | : https://1.1.1.2 |                        |             |
| Cache           |                   |                     | : Enabled         |                        |             |
| HTTPS           | Proxy             | URL                 | :                 |                        |             |
| HTTP            | Version           | Number              | :                 |                        |             |
| switch(config)# |                   | show ip-sla         | all               |                        |             |
| IP-SLA          | session           | status              |                   |                        |             |
| IP-SLA          | Name              |                     |                   | : 707 (non-persistent) |             |
| IP-SLA          | Type              |                     |                   | : https                |             |
| Destination     |                   | Host Name/IP        | Address           | : NA                   |             |
| Destination     |                   | Port                |                   | : NA                   |             |
| Source          | IP Address/IFName |                     |                   | :                      |             |
| Source          | Port              |                     |                   | :                      |             |
| Status          |                   |                     |                   | : running              |             |
| IP-SLA          | Session           | Cumulative          | Counters          |                        |             |
| Total Probes    |                   | Transmitted         |                   | : 1                    |             |
| Probes          | Timed-out         |                     |                   | : 0                    |             |
| Bind Error      |                   |                     |                   | : 0                    |             |
| Destination     |                   | Address Unreachable |                   | : 0                    |             |
| DNS Resolution  |                   | Failures            |                   | : 0                    |             |
| Reception       | Error             |                     |                   | : 0                    |             |
| Transmission    |                   | Error               |                   | : 0                    |             |
| IP-SLA          | Latest            | Probe Results       |                   |                        |             |
| Last Probe      | Time              |                     |                   | : 2023 Jun             | 05 13:10:19 |
| Packets         | Sent              |                     |                   | : 1                    |             |
| Packets         | Received          |                     |                   | : 1                    |             |
| Packet          | Loss              | in Test             |                   | : 0.0000%              |             |
| Minimum         | RTT(ms)           |                     |                   | : 20                   |             |
| Maximum         | RTT(ms)           |                     |                   | : 20                   |             |
| Average         | RTT(ms)           |                     |                   | : 20                   |             |
| DNS RTT(ms)     |                   |                     |                   | : 0                    |             |
| TCP RTT(ms)     |                   |                     |                   | : 12                   |             |
| TLS RTT(ms)     |                   |                     |                   | : 8                    |             |
| switch(config)# |                   | show ip-sla         | http-sla          |                        |             |
| IP-SLA          | Name              |                     | : http-sla        |                        |             |
| Status          |                   |                     | : running         |                        |             |
| IP-SLA          | Type              |                     | : http            |                        |             |
| VRF             |                   |                     | : ipslasrc        |                        |             |
IP-SLA|48

| Source     | IP                |        | : 2.2.2.2          |     |     |     |     |     |     |     |
| ---------- | ----------------- | ------ | ------------------ | --- | --- | --- | --- | --- | --- | --- |
| Source     | Interface         |        | :                  |     |     |     |     |     |     |     |
| Domain     | Name              | Server | : 10.10.10.2       |     |     |     |     |     |     |     |
| Probe      | Interval(seconds) |        | : 90               |     |     |     |     |     |     |     |
| HTTP       | Request           | Type   | : get              |     |     |     |     |     |     |     |
| HTTP/HTTPS |                   | URL    | : abcd.com/ws/home |     |     |     |     |     |     |     |
| Cache      |                   |        | : Enabled          |     |     |     |     |     |     |     |
| HTTP       | Proxy             | URL    | :                  |     |     |     |     |     |     |     |
| HTTP       | Version           | Number | : 1.1              |     |     |     |     |     |     |     |
```
| ##### IP-SLA |     | status description |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
```
| | Status |     |     | |   | Description |     |     |     |     |     | |   |
| -------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
|-------------------------|------------------------------------------------|
| | running |     |     | |   | SLA is | fully operational |     |     |     |     | |   |
| --------- | --- | --- | --- | ------ | ----------------- | --- | --- | --- | --- | --- |
| Bind Error | Another service is using the same source port |
| | Interface |     | Down | |   | Interface | status | is not | up  |     |     |     |
| ----------- | --- | ---- | --- | --------- | ------ | ------ | --- | --- | --- | --- |
| Dns Resolution Error | Failed to resolve destination hostname |
| | No       | Route |       | |   | No available | route    | to the   | responder |         |     | |   |
| ---------- | ----- | ----- | --- | ------------ | -------- | -------- | --------- | ------- | --- | --- |
| | Internal |       | Error | |   | Unexpected   | error    | prevents | SLA       | session |     | |   |
| | Disabled |       |       | |   | SLA is       | disabled |          |           |         |     | |   |
|Configuration Incomplete | Configuration is not complete to enable the SLA|
```
| ##### IP | SLA | session cumulative |     | counters | description |     |     |     |     |     |
| -------- | --- | ------------------ | --- | -------- | ----------- | --- | --- | --- | --- | --- |
```
| | Status |     |     |     | |   | Description |     |     |     |     |     |
| -------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
|
|--------------------------------|--------------------------------------------
------------------------------|
|Probes Timed-out | Total numbers of probes failed to receive
| response. |       |                 | |   |     |               |     |        |              |     |        |
| --------- | ----- | --------------- | --- | --- | ------------- | --- | ------ | ------------ | --- | ------ |
| |Bind     | Error |                 |     | |   | Total numbers | of  | probes | transmission |     | failed |
| as source | port  | not available.| |     |     |               |     |        |              |     |        |
|Destination Address Unreachable | Total numbers of probes transmission failed
| due to route |     | unavailable. | |   |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|DNS Resolution Failures | Total numbers of probes failed due to DNS
| resolution    | failure. |                  | |   |     |               |     |        |            |     |     |
| ------------- | -------- | ---------------- | --- | --- | ------------- | --- | ------ | ---------- | --- | --- |
| |Reception    |          | Error            |     | |   | Total numbers | of  | probes | failed due | to  |     |
| internal      | error    | in reception.    |     | |   |               |     |        |            |     |     |
| |Transmission |          | Error            |     | |   | Total numbers | of  | probes | failed due | to  |     |
| internal      | errr     | in transmission. |     | |   |               |     |        |            |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |     |     |                                       |     |     |     |     |     |     |
| -------------- | ----------- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
| Release        |             |     |     | Modification                          |     |     |     |     |     |     |
| 10.12.1000     |             |     |     | UpdatedtodisplayhttpsasanIP-SLA type. |     |     |     |     |     |     |
| 10.07orearlier |             |     |     | --                                    |     |     |     |     |     |     |
| Command        | Information |     |     |                                       |     |     |     |     |     |     |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 49

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
|     | (#) |     | rightsforthiscommand. |     |
| --- | --- | --- | --------------------- | --- |
start-test
start-test
Description
StartstheIP-SLAprobes.
Examples
| switch(config)#             | ip-sla | test       |     |     |
| --------------------------- | ------ | ---------- | --- | --- |
| switch(config-ip-sla-test)# |        | start-test |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
stop-test
stop-test
Description
StopstheIP-SLAprobes.
Examples
| switch(config)#             | ip-sla | test      |     |     |
| --------------------------- | ------ | --------- | --- | --- |
| switch(config-ip-sla-test)# |        | stop-test |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History |     |     |     |     |
| --------------- | --- | --- | --- | --- |
IP-SLA|50

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
tcp-connect
tcp-connect {<DEST-IPV4-ADDR> | <HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>]
| [probe-interval | <PROBE-INTERVAL>] |     |     |
| --------------- | ----------------- | --- | --- |
Description
ConfiguresTCPconnectastheIP-SLAtestmechanism.Requiresdestinationaddress/hostnameand
destinationportfortheIP-SLAoftcp-connectIP-SLAtype.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
{<DEST-IPV4-ADDR> | <HOSTNAME>} SelectsthedestinationIPv4addressfortheIP-SLAor
thehostnameofthedestination.
<PORT-NUM>
DestinationportfortheIP-SLA.Range:1to65535.
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
| [source-port | <PORT-NUM>] |     | SpecifiestheportfortheIP-SLAtest. |
| ------------ | ----------- | --- | --------------------------------- |
[name-server <IPV4-ADDR-DNS-SERVER>] SpecifiestheDNSserverfordestinationhostname
resolution.
[probe-interval <PROBE-INTERVAL>] Probeintervalinseconds.Range:30to604800.
Examples
| switch(config-ipsla-1)# |     | tcp-connect | 2.2.2.2 8080 |
| ----------------------- | --- | ----------- | ------------ |
switch(config-ipsla-1)# tcp-connect 2.2.2.2 8080 source 2.2.2.1 source-port 6000
switch(config-ipsla-1)# tcp-connect 2.2.2.2 8080 source 1/1/1 source-port 6000
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080 source
| 2.2.2.1 | source-port | 6000 |     |
| ------- | ----------- | ---- | --- |
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080 source
| 1/1/1 source-port | 6000 |     |     |
| ----------------- | ---- | --- | --- |
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080 name-
| server 10.10.10.2 |     |     |     |
| ----------------- | --- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command | History |     |     |
| ------- | ------- | --- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 51

| Release             |         | Modification |           |     |
| ------------------- | ------- | ------------ | --------- | --- |
| 10.07orearlier      |         | --           |           |     |
| Command Information |         |              |           |     |
| Platforms           | Command | context      | Authority |     |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
udp-echo
udp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>] [payload-
size
<PAYLOAD-SIZE>] [tos <TYPE-OF-SERVICE>] [probe-interval <PROBE-INTERVAL>]
Description
ConfiguresUDPechoastheIP-SLAtestmechanism.Requiresdestinationaddress/hostnameand
destinationportnumberfortheIP-SLAofudp-echoSLAtype.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
{<DEST-IPV4-ADDR> | <HOSTNAME>} SelectsthedestinationIPv4addressfortheIP-SLAor
thehostnameofthedestination.
| <PORT-NUM> |     |     | SpecifiesthedestinationportfortheIP-SLA.Range:1 |     |
| ---------- | --- | --- | ----------------------------------------------- | --- |
to65535.
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
[source-port <PORT-NUM>] SpecifiessourceportfortheIP-SLAtest.Range:1to
65535.
| [name-server | <IPV4-ADDR-DNS-SERVER>] |     |     |     |
| ------------ | ----------------------- | --- | --- | --- |
SpecifiestheDNSserverfordestinationhostname
resolution.
[payload-size <PAYLOAD-SIZE>] SpecifiesthepayloadsizeofanSLAprobe.Range:28
to1440.
| [<TYPE-OF-SERVICE>] |     |     | Typeofservice.Range:0to255. |     |
| ------------------- | --- | --- | --------------------------- | --- |
probe-interval <PROBE-INTERVAL> Probeintervalinseconds.Range:5to604800.
Examples
| switch(config-ipsla-1)# |     | udp-echo 2.2.2.2 | 8080 |     |
| ----------------------- | --- | ---------------- | ---- | --- |
switch(config-ipsla-1)#
|     |     | udp-echo 2.2.2.2 | 8080 source | 2.2.2.1 |
| --- | --- | ---------------- | ----------- | ------- |
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080
| switch(config-ipsla-1)# |     | udp-echo 2.2.2.2 | 8080 source | 1/1/1 |
| ----------------------- | --- | ---------------- | ----------- | ----- |
switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 2.2.2.1 payload-size 50
switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 1/1/1 payload-size 50
| switch(config-ipsla-1)# |     | udp-echo 2.2.2.2 | 8080 payload-size | 50  |
| ----------------------- | --- | ---------------- | ----------------- | --- |
IP-SLA|52

switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080 source
2.2.2.1
| payload-size | 50  |     |     |
| ------------ | --- | --- | --- |
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080 source
1/1/1
| payload-size | 50  |     |     |
| ------------ | --- | --- | --- |
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080
| name-server | 10.10.10.2 |     |     |
| ----------- | ---------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Release Modification
10.07orearlier --
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
udp-jitter-voip
udp-jitter-voip {<DEST-IPV4-ADDR> | <HOSTNAME>} <PORT-NUM> [codec-type <CODEC-TYPE>]
[advantage-factor <VALUE>] [source {<SOURCE-IPV4-ADDR> | <IFNAME>} [source-port
<PORT-NUM>]]
[name-server <IPV4-ADDR-DNS-SERVER>][probe-interval <PROBE-INTERVAL>] [tos <TYPE-OF-
SERVICE>]
Description
ConfigureUDPjittervoipastheIP-SLAtestmechanism.Requiresdestinationaddress/hostnameand
sourceaddress/interfacefortheIP-SLAofudp-jitter-voipIP-SLAtype.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
{<DEST-IPV4-ADDR>|<HOSTNAME>} SelectsthedestinationIPv4addressfortheIP-SLAor
thehostnameofthedestination.
| <PORT-NUM> |     |     | SelectstheportnumberfortheIP-SLA.Range:1to |
| ---------- | --- | --- | ------------------------------------------ |
65535.
[codec-type <CODEC-TYPE>] Selectsthecodec-typefortheVoipIP-SLAtest.
[advantage-factor <ADVANTAGE-FACTOR>] Selectsthevaluefortheadvantagefactor.Default
valueis0.
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
| [source-port | <PORT-NUM>] |     |     |
| ------------ | ----------- | --- | --- |
SpecifiesthevalueofsourceportfortheIP-SLA
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 53

| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
probes.
[name-server <IPV4-ADDR-DNS-SERVER>] SpecifiestheDNSserverfordestinationhostname
resolution.
tos <TYPE-OF-SERVICE> Specifiesthetypeofservice.Range:0to255.
| probe-interval |     | <PROBE-INTERVAL> |     |     |     |
| -------------- | --- | ---------------- | --- | --- | --- |
Specifiestheprobeintervalinseconds.Range:120to
604800.
Examples
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10 codec-
type g711a
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10
| codec-type | g711a | source | 2.2.2.1 |     |     |
| ---------- | ----- | ------ | ------- | --- | --- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
| advantage-factor |     | 10  | codec-type | g711a |     |
| ---------------- | --- | --- | ---------- | ----- | --- |
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10
| codec-type | g711a | source | 1/1/1 |     |     |
| ---------- | ----- | ------ | ----- | --- | --- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
| advantage-factor |     | 10  | codec-type | g711a source | 2.2.2.1 |
| ---------------- | --- | --- | ---------- | ------------ | ------- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
| advantage-factor |     | 10  | codec-type | g711a source | 1/1/1 |
| ---------------- | --- | --- | ---------- | ------------ | ----- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
advantage-factor 10 codec-type g711a name-server 10.10.10.2 probe-interval 120
| source 10.1.1.1 |     | source-port |     | 8888 tos 10 |     |
| --------------- | --- | ----------- | --- | ----------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |     |         |              |           |
| -------------- | ----------- | --- | ------- | ------------ | --------- |
| Release        |             |     |         | Modification |           |
| 10.07orearlier |             |     |         | --           |           |
| Command        | Information |     |         |              |           |
| Platforms      | Command     |     | context |              | Authority |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
vrf (ip sla)
vrf <VRF-NAME>
no vrf [<VRF-NAME>]
Description
ConfigurestheVRFonwhichtheSLAwillsendorreceivepackets.Bydefault,thedefaultVRFisused.
ThenoformofthecommandremovesVRFfromSLA.
IP-SLA|54

| Parameter  |     |     | Description                               |     |
| ---------- | --- | --- | ----------------------------------------- | --- |
| <VRF-NAME> |     |     | SpecifiesaVRFname.Length:Default:default. |     |
Examples
| switch(config-ip-sla-test)# |     | vrf | ipslasrc |     |
| --------------------------- | --- | --- | -------- | --- |
| switch(config-ip-sla-test)# |     | no  | vrf      |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| show interface |                       |     |        |             |
| -------------- | --------------------- | --- | ------ | ----------- |
| show interface | [<IFNNAME>|<IFRANGE>] |     | [brief | | physical] |
show interface [<IFNNAME>|<IFRANGE>] [extended [non-zero] | [human-readable]]
| show interface | [<IFNNAME>] | monitor | [human-readable] |     |
| -------------- | ----------- | ------- | ---------------- | --- |
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief]
show interface lag [<LAG-ID>] [extended [non-zero] | [human-readable]]
| show interface | lag [<LAG-ID>] | monitor | [human-readable] |     |
| -------------- | -------------- | ------- | ---------------- | --- |
Description
Showsactiveconfigurationsandoperationalstatusinformationforinterfaces.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IFNAME>
Specifiesainterfacename.
| <IFRANGE> |     |     | Specifiestheportidentifierrange. |     |
| --------- | --- | --- | -------------------------------- | --- |
brief
Showsbriefinfointabularformat.
| physical |     |     | Showsthephysicalconnectioninfointabularformat. |     |
| -------- | --- | --- | ---------------------------------------------- | --- |
extended
Showsadditionalstatistics,includingthetxfilteredandrx
filteredcounters.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 55

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
n Rxfilterpacketsareprotocolpacketsreceivedwhenthe
protocolisdisabledontheswitchandthereisonlyoneportin
theVLAN.ProtocolsincludeOSPF,PIM,RIP,LACP,andLLDP.
n AnexampleofaTxfilteredpacketwouldbeamulticastpacket
beingfilteredfromgoingoutoftheingressport.
human-readable
Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
| non-zero      |     |     |     | Showsonlynonzerostatistics.                    |     |
| ------------- | --- | --- | --- | ---------------------------------------------- | --- |
| LAG           |     |     |     | ShowsLAGinterfaceinformation.                  |     |
| monitor       |     |     |     | Continuouslymonitorinterfacestatistics.        |     |
| LOOPBACK      |     |     |     | Showsloopbackinterfaceinformation.             |     |
| TUNNEL        |     |     |     | Showstunnelinterfaceinformation.               |     |
| VLAN          |     |     |     | ShowsVLANinterfaceinformation.                 |     |
| <LAG-ID>      |     |     |     | SpecifiestheLAGnumber.Range:1-256              |     |
| <LOOPBACK-ID> |     |     |     | SpecifiestheLOOPBACKnumber.Range:0-255         |     |
| <TUNNEL-ID>   |     |     |     | SpecifiesthetunnelID.Range:1-255               |     |
| <VLAN-ID>     |     |     |     | SpecifiestheVLANID.Range:1-4094                |     |
| VXLAN         |     |     |     | ShowstheVXLANinterfaceinformation.             |     |
| <VXLAN-ID>    |     |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |
Examples
Showinginterfaceinformationwhenitisconfiguredasaroute-onlyport:
| switch#           | show      | interface | 1/1/1        |                     |           |
| ----------------- | --------- | --------- | ------------ | ------------------- | --------- |
| Interface         | 1/1/1     | is up     |              |                     |           |
| Admin state       | is        | up        |              |                     |           |
| Link state:       | up        | for 2     | days (since  | Sun Jun 21 05:30:22 | UTC 2020) |
| Link transitions: |           | 1         |              |                     |           |
| Description:      |           | backup    | data center  | link                |           |
| Hardware:         | Ethernet, |           | MAC Address: | 70:72:cf:fd:e7:b4   |           |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | none |             |            |         |     |
| ---------------- | ---- | ----------- | ---------- | ------- | --- |
| Speed 1000       | Mb/s |             |            |         |     |
| Auto-negotiation |      | is          | on         |         |     |
| Flow-control:    |      | off         |            |         |     |
| Error-control:   |      | off         |            |         |     |
| L3 Counters:     |      | Rx Enabled, | Tx Enabled |         |     |
| Rate collection  |      | interval:   | 300        | seconds |     |
IP-SLA|56

| Rates |     |     |     | RX  |     | TX  | Total | (RX+TX) |
| ----- | --- | --- | --- | --- | --- | --- | ----- | ------- |
------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     | 0.00 |     | 0.00 |     | 0.00  |
| ----------- | --- | --- | --- | ---- | --- | ---- | --- | ----- |
| KPkts /     | sec |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Unicast     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Multicast   |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Broadcast   |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Utilization | %   |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Statistics  |     |     |     | RX   |     | TX   |     | Total |
------------- -------------------- -------------------- --------------------
| Packets      |     |     |     | 0   |     | 0   |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast      |     |     |     | 0   |     | 0   |     | 0   |
| Multicast    |     |     |     | 0   |     | 0   |     | 0   |
| Broadcast    |     |     |     | 0   |     | 0   |     | 0   |
| Bytes        |     |     |     | 0   |     | 0   |     | 0   |
| Jumbos       |     |     |     | 0   |     | 0   |     | 0   |
| Dropped      |     |     |     | 0   |     | 0   |     | 0   |
| Filtered     |     |     |     | 0   |     | 0   |     | 0   |
| Pause Frames |     |     |     | 0   |     | 0   |     | 0   |
| L3 Packets   |     |     |     | 0   |     | 0   |     | 0   |
| L3 Bytes     |     |     |     | 0   |     | 0   |     | 0   |
| Errors       |     |     |     | 0   |     | 0   |     | 0   |
| CRC/FCS      |     |     |     | 0   |     | n/a |     | 0   |
| Collision    |     |     |     | n/a |     | 0   |     | 0   |
| Runts        |     |     |     | 0   |     | n/a |     | 0   |
| Giants       |     |     |     | 0   |     | n/a |     | 0   |
| Other        |     |     |     | 0   |     | 0   |     | 0   |
Showinginformationwhentheinterfaceiscurrentlylinkedatadownshiftedspeed:
| switch(config-if)# |       | show  | interface | 1/1/1 |     |     |     |     |
| ------------------ | ----- | ----- | --------- | ----- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is up |           |       |     |     |     |     |
...
| Auto-negotiation |     | is on | with | downshift | active |     |     |     |
| ---------------- | --- | ----- | ---- | --------- | ------ | --- | --- | --- |
ShowinginformationwhentheinterfaceisshutdownduringaVSX split:
| switch(config-if)# |       | show     | interface | 1/1/1  |     |     |     |     |
| ------------------ | ----- | -------- | --------- | ------ | --- | --- | --- | --- |
| Interface          | 1/1/1 | is down  |           |        |     |     |     |     |
| Admin state        | is    | up       |           |        |     |     |     |     |
| State information: |       | Disabled |           | by VSX |     |     |     |     |
Link state: down for 3 days (since Tue Mar 16 05:20:47 UTC 2021)
| Link transitions: |     | 0   |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:
| Hardware: | Ethernet, | MAC | Address: | 04:09:73:62:90:e7 |     |     |     |     |
| --------- | --------- | --- | -------- | ----------------- | --- | --- | --- | --- |
MTU 1500
Type SFP+DAC3
Full-duplex
| qos trust        | none            |                 |     |         |     |     |     |     |
| ---------------- | --------------- | --------------- | --- | ------- | --- | --- | --- | --- |
| Speed 0          | Mb/s            |                 |     |         |     |     |     |     |
| Auto-negotiation |                 | is off          |     |         |     |     |     |     |
| Flow-control:    |                 | off             |     |         |     |     |     |     |
| Error-control:   |                 | off             |     |         |     |     |     |     |
| VLAN Mode:       | native-untagged |                 |     |         |     |     |     |     |
| Native           | VLAN:           | 1               |     |         |     |     |     |     |
| Allowed          | VLAN            | List: 1502-1505 |     |         |     |     |     |     |
| Rate collection  |                 | interval:       | 300 | seconds |     |     |     |     |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 57

| Rate |     |     | RX  |     | TX  | Total | (RX+TX) |     |
| ---- | --- | --- | --- | --- | --- | ----- | ------- | --- |
---------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     | 0.00 |     | 0.00 |     |       | 0.00 |
| ----------- | --- | --- | ---- | --- | ---- | --- | ----- | ---- |
| KPkts /     | sec |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Unicast     |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Multicast   |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Broadcast   |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Utilization |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Statistic   |     |     | RX   |     | TX   |     | Total |      |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     | 0   |     | 0   |     |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast      |     |     | 0   |     | 0   |     |     | 0   |
| Multicast    |     |     | 0   |     | 0   |     |     | 0   |
| Broadcast    |     |     | 0   |     | 0   |     |     | 0   |
| Bytes        |     |     | 0   |     | 0   |     |     | 0   |
| Jumbos       |     |     | 0   |     | 0   |     |     | 0   |
| Dropped      |     |     | 0   |     | 0   |     |     | 0   |
| Pause Frames |     |     | 0   |     | 0   |     |     | 0   |
| Errors       |     |     | 0   |     | 0   |     |     | 0   |
| CRC/FCS      |     |     | 0   |     | n/a |     |     | 0   |
| Collision    |     |     | n/a |     | 0   |     |     | 0   |
| Runts        |     |     | 0   |     | n/a |     |     | 0   |
| Giants       |     |     | 0   |     | n/a |     |     | 0   |
Showingthemonitorinformation:
Inmonitormode,theCLI refreshesdataautomaticallyuntilitisexitedbyenteringq.Pressing?opensthehelp
menutodisplaywhichoptionsareavailableinthiscontext.
| Interface | 1/1/1 is up |     |     |     |     |       |         |     |
| --------- | ----------- | --- | --- | --- | --- | ----- | ------- | --- |
| Rate      |             |     | RX  |     | TX  | Total | (RX+TX) |     |
---------------- -------------------- -------------------- --------------------
| MBits /     | sec |     | 30196.43 |     | 30196.43 |       | 60392.85  |      |
| ----------- | --- | --- | -------- | --- | -------- | ----- | --------- | ---- |
| MPkts /     | sec |     | 58977.39 |     | 58977.40 |       | 117954.79 |      |
| Unicast     |     |     | 0.00     |     | 0.00     |       |           | 0.00 |
| Multicast   |     |     | 58977.39 |     | 58977.40 |       | 117954.79 |      |
| Broadcast   |     |     | 0.00     |     | 0.00     |       |           | 0.00 |
| Utilization | %   |     | 75.49    |     | 75.49    |       | 150.98    |      |
| Statistic   |     |     | RX       |     | TX       | Total | (RX+TX)   |      |
---------------- -------------------- -------------------- --------------------
| Packets      |                      | 4756527649   |     | 4756527865   |     |              | 9513055514  |     |
| ------------ | -------------------- | ------------ | --- | ------------ | --- | ------------ | ----------- | --- |
| Unicast      |                      |              | 0   |              | 0   |              |             | 0   |
| Multicast    |                      | 4756527649   |     | 4756527865   |     |              | 9513055514  |     |
| Broadcast    |                      |              | 2   |              | 0   |              |             | 2   |
| Bytes        |                      | 304417778668 |     | 304417795428 |     | 608835574096 |             |     |
| Jumbos       |                      |              | 0   |              | 0   |              |             | 0   |
| Dropped      |                      |              | 0   | 19028847730  |     |              | 19028847730 |     |
| Pause Frames |                      |              | 0   |              | 0   |              |             | 0   |
| Errors       |                      |              | 0   |              | 0   |              |             | 0   |
| CRC/FCS      |                      |              | 0   |              | n/a |              |             | 0   |
| help: ?,     | quit: q              |              |     |              |     |              |             |     |
| Help for     | Interface Monitor    |              |     |              |     |              |             |     |
| h Toggle     | human-readable       | mode         |     |              |     |              |             |     |
| c Clear      | interface statistics |              |     |              |     |              |             |     |
| Does not     | apply to rates       |              |     |              |     |              |             |     |
| Arrows,      | PgUp, PgDn, Home,    | End          |     |              |     |              |             |     |
IP-SLA|58

| Navigate | interface | statistics |     |     |     |     |     |
| -------- | --------- | ---------- | --- | --- | --- | --- | --- |
Delay: 2
| help: ?, | quit: q |     |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- | --- |
Showingtheoutputforinterface1/1/1inhuman-readableformat:
Inhuman-readableformat,the<1symbolforUtilizationindicatesthattheamountofpacketsisbetweenzero
andone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsandthe
Utilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
| switch(config-if)# |       | show interface | 1/1/1 human-readable |     |     |       |         |
| ------------------ | ----- | -------------- | -------------------- | --- | --- | ----- | ------- |
| Interface          | 1/1/1 | is up          |                      |     |     |       |         |
| Rate               |       |                | RX                   |     | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Bits / sec  |     |     | 3M  |     | 3M  |     | 6M    |
| ----------- | --- | --- | --- | --- | --- | --- | ----- |
| Pkts / sec  |     |     | 316 |     | 316 |     | 633   |
| Unicast     |     |     | 319 |     | 319 |     | 638   |
| Multicast   |     |     | 0   |     | 0   |     | 0     |
| Broadcast   |     |     | 0   |     | 0   |     | 0     |
| Utilization | %   |     | < 1 |     | < 1 |     | < 1   |
| Statistic   |     |     | RX  |     | TX  |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     | 577K |     | 577K |     | 1M  |
| ------------ | --- | --- | ---- | --- | ---- | --- | --- |
| Unicast      |     |     | 577K |     | 577K |     | 1M  |
| Multicast    |     |     | 0    |     | 51   |     | 51  |
| Broadcast    |     |     | 0    |     | 15   |     | 15  |
| Bytes        |     |     | 744M |     | 745M |     | 1G  |
| Jumbos       |     |     | 0    |     | 0    |     | 0   |
| Dropped      |     |     | 0    |     | 0    |     | 0   |
| Filtered     |     |     | 0    |     | 0    |     | 0   |
| Pause Frames |     |     | 0    |     | 0    |     | 0   |
| Errors       |     |     | 0    |     | 0    |     | 0   |
| CRC/FCS      |     |     | 0    |     | n/a  |     | 0   |
| Collision    |     |     | n/a  |     | 0    |     | 0   |
| Runts        |     |     | 0    |     | n/a  |     | 0   |
| Giants       |     |     | 0    |     | n/a  |     | 0   |
Showinginformationaboutextendedcounters:
Theoutputoftheshow interface extendedcommandvariesdependingontheswitchmodeland
configuration.
| switch(config-if)# |     | show interface | 1/1/17 extended |     |     |     |     |
| ------------------ | --- | -------------- | --------------- | --- | --- | --- | --- |
-------------------------------------------------------------------
| Interface | 1/1/17 |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------
| Statistics |     |     |     | Value |     |     |     |
| ---------- | --- | --- | --- | ----- | --- | --- | --- |
-------------------------------------------------------------------
| Dot1d Tp      | Port In         | Frames  |     | 547   |     |     |     |
| ------------- | --------------- | ------- | --- | ----- | --- | --- | --- |
| Dot1d Tp      | Port Out        | Frames  |     | 608   |     |     |     |
| Dot3 In Pause | Frames          |         |     | 0     |     |     |     |
| Dot3 Out      | Pause Frames    |         |     | 0     |     |     |     |
| Ethernet      | Stats Broadcast | Packets |     | 19    |     |     |     |
| Ethernet      | Stats Bytes     |         |     | 40162 |     |     |     |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 59

| Ethernet | Stats Packets |     |     | 342 |     |     |
| -------- | ------------- | --- | --- | --- | --- | --- |
...
-------------------------------------------------------------------
| Error-Statistics |     |     |     | Value |     |     |
| ---------------- | --- | --- | --- | ----- | --- | --- |
-------------------------------------------------------------------
| Dot1d Base   | Port MTU    | Exceeded     | Discards | 0   |     |     |
| ------------ | ----------- | ------------ | -------- | --- | --- | --- |
| Dot3 Control | In Unknown  | Opcodes      |          | 0   |     |     |
| Dot3 Stats   | Alignment   | Errors       |          | 0   |     |     |
| Dot3 Stats   | FCS Errors  |              |          | 0   |     |     |
| Dot3 Stats   | Frame Too   | Longs        |          | 0   |     |     |
| Dot3 Stats   | Internal    | Mac Transmit | Errors   | 0   |     |     |
| Ethernet     | RX Oversize | Packets      |          | 0   |     |     |
...
Showinginterfacelink-status:
| switch# | show interface | link-status |     |     |     |     |
| ------- | -------------- | ----------- | --- | --- | --- | --- |
-------------------------------------------------------------
| Port | Type |     | Physical   | Link        | Last   |     |
| ---- | ---- | --- | ---------- | ----------- | ------ | --- |
|      |      |     | Link State | Transitions | Change |     |
-------------------------------------------------------------
| 1/1/1    | 1G-BT     |     | down | 0   | --       |                 |
| -------- | --------- | --- | ---- | --- | -------- | --------------- |
| 1/1/2    | 1G-BT     |     | up   | 1   | 1 minute | ago (Fri Mar 09 |
| 12:36:56 | UTC 2018) |     |      |     |          |                 |
| 1/1/3    | 1G-BT     |     | up   | 1   | 1 minute | ago (Fri Mar 09 |
| 12:36:56 | UTC 2018) |     |      |     |          |                 |
| 1/1/4    | --        |     | down | 0   | --       |                 |
| 1/1/5    | --        |     | down | 0   | --       |                 |
Showinginterfaceloopback1link-status:
-------------------------------------------------------------
|      |      |     | Physical   | Link        | Last   |     |
| ---- | ---- | --- | ---------- | ----------- | ------ | --- |
| Port | Type |     | Link State | Transitions | Change |     |
-------------------------------------------------------------
| loopback1 | --  |     | up  | --  | --  |     |
| --------- | --- | --- | --- | --- | --- | --- |
Showinginterface1/1/2-1/1/3link-status:
-------------------------------------------------------------
|      |      |     | Physical   | Link        | Last   |     |
| ---- | ---- | --- | ---------- | ----------- | ------ | --- |
| Port | Type |     | Link State | Transitions | Change |     |
-------------------------------------------------------------
| 1/1/2    | 1G-BT     |     | up  | 1   | 1 minute | ago (Fri Mar 09 |
| -------- | --------- | --- | --- | --- | -------- | --------------- |
| 12:36:56 | UTC 2018) |     |     |     |          |                 |
| 1/1/3    | 1G-BT     |     | up  | 1   | 1 minute | ago (Fri Mar 09 |
| 12:36:56 | UTC 2018) |     |     |     |          |                 |
Showinginterfacelink-status:
| switch# | show interface | link-status |     |     |     |     |
| ------- | -------------- | ----------- | --- | --- | --- | --- |
-------------------------------------------------------------------------
| Port | Type |     | Physical   | Link        | Link Flaps | Last   |
| ---- | ---- | --- | ---------- | ----------- | ---------- | ------ |
|      |      |     | Link State | Transitions | Ignored    | Change |
IP-SLA|60

-------------------------------------------------------------------------
| 1/1/1    |     | 1G-BT    |     |       | down |     | 0   | 0   | --       |     |
| -------- | --- | -------- | --- | ----- | ---- | --- | --- | --- | -------- | --- |
| 1/1/2    |     | 1G-BT    |     |       | up   |     | 1   | 0   | 1 minute | ago |
| (Fri Mar | 09  | 12:36:56 | UTC | 2018) |      |     |     |     |          |     |
| 1/1/3    |     | 1G-BT    |     |       | up   |     | 1   | 0   | 1 minute | ago |
| (Fri Mar | 09  | 12:36:56 | UTC | 2018) |      |     |     |     |          |     |
| 1/1/4    |     | --       |     |       | down |     | 0   | 0   | --       |     |
| 1/1/5    |     | --       |     |       | down |     | 0   | 0   | --       |     |
Showingstateinformationwheninterfaceisblocked:
| 8360(config-if)#   |       |       | show    | interface |         | 1/1/1 |     |     |     |     |
| ------------------ | ----- | ----- | ------- | --------- | ------- | ----- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is    | up      | (Blocked) |         |       |     |     |     |     |
| Admin state        |       | is up |         |           |         |       |     |     |     |     |
| State information: |       |       | Blocked |           | by UDLD |       |     |     |     |     |
Link state: up for 1 minute (since Mon Jun 10 09:25:27 UTC 2024)
| Link transitions: |     |     | 1   |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:
Persona:
| Hardware: | Ethernet, |     | MAC | Address: |     | 00:fd:45:67:85:91 |     |     |     |     |
| --------- | --------- | --- | --- | -------- | --- | ----------------- | --- | --- | --- | --- |
MTU 1500
| Type 10G-LR |     | / 10G | SFP+ | LR  |     |     |     |     |     |     |
| ----------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
Full-duplex
| qos trust        | none   |           |        |     |         |     |     |     |       |         |
| ---------------- | ------ | --------- | ------ | --- | ------- | --- | --- | --- | ----- | ------- |
| Speed 10000      |        | Mb/s      |        |     |         |     |     |     |       |         |
| Auto-negotiation |        |           | is off |     |         |     |     |     |       |         |
| Flow-control:    |        | off       |        |     |         |     |     |     |       |         |
| Error-control:   |        | off       |        |     |         |     |     |     |       |         |
| VLAN Mode:       | access |           |        |     |         |     |     |     |       |         |
| Access           | VLAN:  | 1         |        |     |         |     |     |     |       |         |
| Rate collection  |        | interval: |        | 300 | seconds |     |     |     |       |         |
| Rate             |        |           |        |     |         | RX  |     | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| ----------- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | ----- |
| KPkts /     | sec |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Unicast     |     |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Multicast   |     |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Broadcast   |     |     |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Utilization |     | %   |     |     |     | 0.00 |     | 0.00 |     | 0.00  |
| Statistic   |     |     |     |     |     | RX   |     | TX   |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     |     |     |     | 15   |     | 15   |     | 30   |
| ------------ | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | ---- |
| Unicast      |     |     |     |     |     | 12   |     | 12   |     | 24   |
| Multicast    |     |     |     |     |     | 3    |     | 3    |     | 6    |
| Broadcast    |     |     |     |     |     | 0    |     | 0    |     | 0    |
| Bytes        |     |     |     |     |     | 1350 |     | 1350 |     | 2700 |
| Jumbos       |     |     |     |     |     | 0    |     | 0    |     | 0    |
| Dropped      |     |     |     |     |     | 0    |     | 0    |     | 0    |
| Pause Frames |     |     |     |     |     | 0    |     | 0    |     | 0    |
| Errors       |     |     |     |     |     | 0    |     | 0    |     | 0    |
| CRC/FCS      |     |     |     |     |     | 0    |     | n/a  |     | 0    |
| Collision    |     |     |     |     |     | n/a  |     | 0    |     | 0    |
| Runts        |     |     |     |     |     | 0    |     | n/a  |     | 0    |
| Giants       |     |     |     |     |     | 0    |     | n/a  |     | 0    |
Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideortheMonitoring
Guideforyourswitchmodel.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 61

| Command History |     |     |                                                 |
| --------------- | --- | --- | ----------------------------------------------- |
| Release         |     |     | Modification                                    |
| 10.15           |     |     | Addedstateinformationwhenportgoesintodownstate. |
10.11
Addedmonitorparameter.
| 10.10               |         |         | Addedhuman-readableparameter. |
| ------------------- | ------- | ------- | ----------------------------- |
| 10.07orearlier      |         |         | --                            |
| Command Information |         |         |                               |
| Platforms           | Command | context | Authority                     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show interface | statistics |     |     |
| -------------- | ---------- | --- | --- |
show interface [<IFNAME>|<IFRANGE>] statistics [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] statistics monitor [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] error-statistics [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] error-statistics monitor [non-zero] [human-readable]
show interface lag [<LAG-ID>] statistics [non-zero] [human-readable]
show interface lag [<LAG-ID>] statistics monitor [non-zero] [human-readable]
show interface lag [<LAG-ID>] error-statistics [non-zero] [human-readable]
show interface lag [<LAG-ID>] error-statistics monitor [non-zero] [human-readable]
show interface vxlan <VXLAN-ID> statistics [non-zero] [human-readable]
Description
Showsstatisticsforswitchinterfacessuchaspacketstransmittedandreceived,bytestransmittedand
received,broadcastandmulticastpackets.
| Parameter |     |     | Description              |
| --------- | --- | --- | ------------------------ |
| <IFNAME>  |     |     | Specifiesainterfacename. |
<IFRANGE>
Specifiestheportidentifierrange.
| LAG |     |     | ShowsLAGinterfaceinformation. |
| --- | --- | --- | ----------------------------- |
<LAG-ID>
SpecifiestheLAGnumber.Range:1-256
| VXLAN |     |     | ShowstheVXLANinterfaceinformation. |
| ----- | --- | --- | ---------------------------------- |
<VXLAN-ID>
SpecifiestheVXLANinterfaceidentifier.Default:1
| monitor |     |     | Continuouslymonitorinterfacestatistics. |
| ------- | --- | --- | --------------------------------------- |
human-readable
Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.
| non-zero |     |     | Showsonlynonzerostatistics. |
| -------- | --- | --- | --------------------------- |
IP-SLA|62

Examples

Showing statistics of all interfaces:

Showing statistics of all interfaces with only non-zero statistics:

Showing statistics of all interfaces in the human-readable format:

Showing statistics of a single interfaces:

Showing statistics of all members of a LAG interface:

Showing error statistics of all interfaces:

Showing monitor statistics:

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

63

The rows and columns of show interface monitor statistics depends on the length of width of the client terminal.

The CLI can be navigated using the arrow keys as well as the PageUp, PageDown, Home, and End keys.

Showing monitor error statistics in human-readable format:

IP-SLA | 64

Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideortheMonitoring
Guideforyourswitchmodel.
| Command History     |         |         |                               |
| ------------------- | ------- | ------- | ----------------------------- |
| Release             |         |         | Modification                  |
| 10.11               |         |         | Addedmoitorparameter.         |
| 10.10               |         |         | Addedhuman-readableparameter. |
| 10.07orearlier      |         |         | --                            |
| Command Information |         |         |                               |
| Platforms           | Command | context | Authority                     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 65

Chapter 7

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

Mirroring and sFlow

The mirroring feature (when mirroring received traffic) and the sFlow sampling feature both require the
receive (rx) capability of a given port. If both features are configured and enabled to use the receive
capability on the same port, only one of the features can perform its task.

This interaction does not affect transmit (tx) mirroring because sFlow does not use the transmit (tx)
capability of a port.

Behavior if sFlow is enabled and mirror enable is attempted

If sFlow is enabled on a port and a mirroring session specifies the same port as a source of received
traffic (the source is configured with a direction of rx or both):

n The attempt to enable the mirroring session fails and an error is returned.

n To enable the mirroring session, first you must disable sFlow on that port.

Behavior if mirroring is enabled and sFlow enable is attempted

If a mirroring session specifies a port as a source of received traffic (the source is configured with a
direction of rx or both), and you attempt to enable sFlow on the same port:

n Mirroring on that port continues.

n No error or warning message is returned when sFlow is enabled, but sFlow sampling on that port

does not occur.

When sFlow is enabled on a port but sampling is not occurring, the show sflow <INTERFACE-NAME>
command shows that sFlow is enabled but shows a value of 0 (zero) for the number of samples.

To activate sFlow sampling on that port, you must do the following:

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

66

1. Disable the mirroring session on the port.

2. Disable sFlow on the port.

3. Enable sFlow on the port.

Behavior when the startup configuration has both sFlow and rx mirroring enabled on
the same port

If the startup configuration has the same port configured with both sFlow enabled and as a source of
received traffic in an enabled mirroring session:

n During a boot or management module failover operation, it is not possible to predict whether the
receive capability of the port will be assigned to the sFlow feature or to the mirroring feature.

n To ensure that the feature that you want is used on a specific port, after the boot operation or

management module failover operation completes, disable both features on that port and then
enable the feature you want to use.

Mirror statistics

Mirror statistics are reset for a Mirror-to-CPU session when an interface is added or removed from a
LAG that is a source interface in the Mirror session and during a failover.

Mirror statistics are reset for a Mirror-to-CPU session on a failover.

Classifier policies and mirroring sessions

Network traffic can be mirrored to a destination interface in two ways:

n Using a mirroring session alone.

n Using Classifier Policies with mirror actions in conjunction with a mirroring session.

Basic mirroring sessions provide coarse control over the type of traffic mirrored from a source: all
received, all transmitted, or both. However, a traffic class within a Classifier Policy applied to a source
can provide much finer grained control of mirrored traffic. For example, a policy can match on many
different aspects of the Ethernet or IPv4 or IPv6 header information in each frame or packet received or
transmitted on an interface.

The steps to configure a policy and class with a mirror action are the following:

1. Configuring a mirroring session with a destination interface.

2. Enabling the mirroring session.

3. Configuring the Classifier Policy, specifying the mirroring session ID in the mirror action.

Any subsequent configuration changes to either the enabled mirroring session or the classifier policy
can affect the behavior of the network monitoring that occurs. For examples, see Scenario 1 and
Scenario 2.

Scenario 1

1. Mirroring session 1 is configured with destination interface 1/1/10 and source interface 1/1/5 in

the both direction, then the session is enabled.

2. Mirroring session 2 is configured with destination interface 1/1/20, then the session is enabled.

3. Policy Policy_2 is configured with a class matching OSPF traffic from any source IPv4 address to

Mirroring | 67

any destination IPv4 address and an action of mirror, specifying mirroring session 2.

4. Policy_2 is applied to interface 1/1/5 in the inbound direction.

This sequence of actions creates a situation where the interface 1/1/5 is effectively configured as a
source for two separate enabled mirroring sessions. This configuration is not permitted if you attempt
to configure and enable the two mirroring sessions through the CLI. However, mirroring may occur for
both sessions because policies with mirror actions have priority over basic mirroring sessions.

In this example:

n Because of Policy_2, all OSPF traffic ingressing interface 1/1/5 is mirrored to 1/1/20, which is the

destination interface of mirroring session 2.

n After Policy_2 is applied, and because of the mirroring session 1 is enabled, all non-OSPF traffic
ingressing interface 1/1/5 is mirrored to 1/1/10, which is the destination interface of mirroring
session 1.

n Because Policy_2 does not match egressing traffic, and because mirroring session 1 is enabled, all
traffic egressing interface 1/1/5 is mirrored to 1/1/10, which is the destination interface of mirroring
session 1.

Scenario 2

1. Mirroring session 2 is configured with destination interface 1/1/20 and source interface 1/1/3,

then the session is enabled.

2. Policy Policy_2 is configured with a class matching OSPF traffic from any source IPv4 address to

any destination IPv4 address and an action of mirror specifying mirroring session 2.

3. Policy_2 is applied to interface 1/1/5 in the inbound direction.

In this scenario, a single mirroring session is configured with a source interface and is configured as the
target of the mirror action of a policy applied to a different source interface. In this example, the
destination interface 1/1/20 receives traffic from interface 1/1/3 and from interface 1/1/5.

Mirroring commands

clear mirror
clear mirror [all | <SESSION-ID>]

Description

Clears the mirror statistics for all configured mirror sessions or a specified session

Parameter

all

<SESSION-ID>

Examples

Description

Specifies all configured sessions.

Specifies a numeric identifier for the session. Range: 1 to 4

Clearing mirror statistics for all configured mirror sessions:

switch# clear mirror all

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

68

Clearingmirrorstatisticsformirrorsession1:
| switch# clear | mirror | 1   |     |     |     |
| ------------- | ------ | --- | --- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
comment
comment <COMMENT>
no comment
Description
Specifiesacommentforthemirroringsession.
Thenoformofthiscommandremovesthecomment.
| Parameter |     |     | Description                                        |     |     |
| --------- | --- | --- | -------------------------------------------------- | --- | --- |
| <COMMENT> |     |     | Acommentstringofupto64characterscomposedofletters, |     |     |
numbers,underscores,dashes,spaces,andperiods.
Usage
Commentsareoptionalandcanbeaddedorremovedatanytimewithoutaffectingthestateofthe
mirroringsession.
Addingacommenttoasessionthatalreadyhasacommentreplacestheexistingcomment.
Examples
Addingacommenttoamirrorsession:
switch(config-mirror-3)#
|             |        | comment | This Mirror will | be removed | during next |
| ----------- | ------ | ------- | ---------------- | ---------- | ----------- |
| maintenance | window |         |                  |            |             |
Removingthecommentfrommirrorsession3:
| switch(config-mirror-3)# |     | no comment |     |     |     |
| ------------------------ | --- | ---------- | --- | --- | --- |
Mirroring|69

Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |              |           |     |     |
| -------------- | ----------- | ------- | ------------ | --------- | --- | --- |
| Release        |             |         | Modification |           |     |     |
| 10.07orearlier |             |         | --           |           |     |     |
| Command        | Information |         |              |           |     |     |
| Platforms      | Command     | context |              | Authority |     |     |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
copy tcpdump-pcap
| copy tcpdump-pcap | <FILE-NAME> | <REMOTE-URL> |     |     |     |     |
| ----------------- | ----------- | ------------ | --- | --- | --- | --- |
Description
Savespacketcapturefilestoexternalstorage.
| Parameter   |     |     | Description                          |     |     |     |
| ----------- | --- | --- | ------------------------------------ | --- | --- | --- |
| <FILE-NAME> |     |     | Specifiesthepacketcapturefiletosave. |     |     |     |
<REMOTE-URL>
Specifiestheexternalstoragetowhichthepacketcapturefilewill
besaved.
Usage
Onlyfourfilescanbesavedatanypointontheswitch.Packetcapturefilesarenotsavedafterafailover
| orreboot.Viewalistofsavedfilesusingdiag |     |     | utilities | list-files. |     |     |
| --------------------------------------- | --- | --- | --------- | ----------- | --- | --- |
Examples
Savingmy_capture_file.pcaptosftp://root@10.0.0.2/file.pcap:
switch# copy tcpdump-pcap my_capture_file.pcap sftp://root@10.0.0.2/file.pcap
| root@10.0.0.2's      | passowrd:            |     |                    |          |           |       |
| -------------------- | -------------------- | --- | ------------------ | -------- | --------- | ----- |
| Connected            | to 10.0.0.2.         |     |                    |          |           |       |
| sftp > put           | my_capture_file.pcap |     | file.pcap          |          |           |       |
| Uploading            | my_capture_file.pcap |     | to /root/file.pcap |          |           |       |
| my_capture_file.pcap |                      |     |                    | 100% 156 | 219.8KB/s | 00:00 |
| Copied               | successfuly.         |     |                    |          |           |       |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command | History |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 70

| Release   |             |         | Modification      |     |     |     |
| --------- | ----------- | ------- | ----------------- | --- | --- | --- |
| 10.08     |             |         | Commandintroduced |     |     |     |
| Command   | Information |         |                   |     |     |     |
| Platforms | Command     | context | Authority         |     |     |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
copy tshark-pcap
| copy tshark-pcap | <REMOTE-URL> | [vrf | <VRF-NAME>] |     |     |     |
| ---------------- | ------------ | ---- | ----------- | --- | --- | --- |
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
| switch#         | copy tshark-pcap | sftp://root@10.0.0.2/file.pcap |     |          |           |       |
| --------------- | ---------------- | ------------------------------ | --- | -------- | --------- | ----- |
| root@10.0.0.2's | password:        |                                |     |          |           |       |
| Connected       | to 10.0.0.2.     |                                |     |          |           |       |
| sftp> put       | packets.pcap     | file.pcap                      |     |          |           |       |
| Uploading       | packets.pcap     | to /root/file.pcap             |     |          |           |       |
| packets.pcap    |                  |                                |     | 100% 156 | 219.8KB/s | 00:00 |
| Copied          | successfully.    |                                |     |          |           |       |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |     |              |     |     |     |
| -------------- | ----------- | --- | ------------ | --- | --- | --- |
| Release        |             |     | Modification |     |     |     |
| 10.07orearlier |             |     | --           |     |     |     |
| Command        | Information |     |              |     |     |     |
Mirroring|71

| Platforms | Command |     | context |     | Authority |     |
| --------- | ------- | --- | ------- | --- | --------- | --- |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
| theSupportability |     | Guide. |     |     |     |     |
| ----------------- | --- | ------ | --- | --- | --- | --- |
ThenoformofthiscommandwillimmediatelystopsmirroringtraffictotheCPU,butwillnotremove
anysourcesfromthemirrorconfiguration.
Examples
ConfiguringamirrorsessionwithCPUasthedestination.
| switch#                  | config |        |             |     |     |     |
| ------------------------ | ------ | ------ | ----------- | --- | --- | --- |
| switch(config)#          |        | mirror | session     | 1   |     |     |
| switch(config-mirror-1)# |        |        | destination |     | cpu |     |
Removingthedestinationentirely.
| switch(config-mirror-1)# |     |     | no  | destination |     | cpu |
| ------------------------ | --- | --- | --- | ----------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |     |         |     |              |           |
| -------------- | ----------- | --- | ------- | --- | ------------ | --------- |
| Release        |             |     |         |     | Modification |           |
| 10.07orearlier |             |     |         |     | --           |           |
| Command        | Information |     |         |     |              |           |
| Platforms      | Command     |     | context |     |              | Authority |
8400 config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| destination    | interface |     |                             |     |     |     |
| -------------- | --------- | --- | --------------------------- | --- | --- | --- |
| destination    | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |     |     |
| no destination | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |     |     |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 72

Description
Configuresthespecifiedinterfaceasthedestinationofthemirroredtraffic.
Thenoformofthiscommandimmediatelydisablesthemirroringsessionandremovesthespecified
destinationinterfacefromtheconfiguration.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE-ID>
Specifiesainterface.Format:member/slot/port.
| <LAG-NAME> |     |     | SpecifiesaLAG(linkaggregationgroup)identifier. |     |
| ---------- | --- | --- | ---------------------------------------------- | --- |
Usage
Supportedmirrordestinations:Layer2orLayer3Ethernetports,LAGs,tunnel,orCPUasaMirror
Destination.AportthatisalreadyamemberofaLAGisnotavalidmirrordestination.
Configuringadifferentdestinationinterfaceinanenabledmirroringsessioncausesallmirroredtraffic
tousethenewdestinationinterface.Thisactionmightcauseatemporarysuspensionofmirrored
sourcetrafficduringthereconfiguration.
Examples
Configuringamirroringsessionandaddinganinterfaceasadestination:
| switch(config)#          | mirror | session 1   |           |       |
| ------------------------ | ------ | ----------- | --------- | ----- |
| switch(config-mirror-1)# |        | destination | interface | 1/1/1 |
Replacingtheexistingdestinationwithdifferentinterface:
switch(config-mirror-1)#
|     |     | destination | interface | 1/1/12 |
| --- | --- | ----------- | --------- | ------ |
Removingadestination:
| switch(config-mirror-1)# |     | no destination | interface | 1/1/12 |
| ------------------------ | --- | -------------- | --------- | ------ |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
Switch Destination interface limit per mirror session (4 possible sessions)
| 8400 1 |     |     |     |     |
| ------ | --- | --- | --- | --- |
Command History
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
Command Information
Mirroring|73

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| destination | tunnel |     |     |     |
| ----------- | ------ | --- | --- | --- |
destination tunnel <TUNNEL-IPV4-ADDR> source <SOURCE-IPv4-ADDR>
| dscp <DSCP-VALUE> | vrf    | <VRF-NAME> | id <SPAN-ID> |     |
| ----------------- | ------ | ---------- | ------------ | --- |
| no destination    | tunnel |            |              |     |
Description
Specifiesthetunnelwhereallmirroredtrafficforthesessionistransmitted.Onlyonetunneldestination
isallowedpersession.
Youmayconfiguremultiplemirrorsessionswiththesamesource/destinationIPaddresspair,however,
onlyoneofthosesessionssharingthesamesource/destinationIPaddresspaircanbeenabledata
giventime.
MultipleMirrorSessionscanbeenabledwiththesamesource/destinationIPaddresspairifthespan
IDsaredifferentforsessions.Bydefaultitisassigned0ifnotspecified.
ERSPANisnotsupportedleavingtheswitchbytheOOBport.IfVRFmanagementisconfiguredforan
ERSPANsession,thesessionwillbein"mirror_err_tunnel_oob_port_not_supported"operationstatus.
ERSPANisnotsupportedleavingtheswitchencapsulatedwithinanothertunnel(e.g.GREIPv4).When
thepathtothedestinationIPaddresswillleaveviaatunnel,thesessionwillbein"tunnel_route_
resolution_not_populated"operationstatus.
Theinterface/LAGusedtotransmitERSPANpacketsshouldnotbeasourceinthesamemirrorsession.
Thenoformofthiscommandwillceasetheuseofthetunnelanddisablethesession.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<TUNNEL-IPV4-ADDR> SpecifiesthetunneladdressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.
<SOURCE-IPv4-ADDR> SpecifiesthesourceaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.
<DSCP-VALUE>
SpecifiestheDSCPvaluetobecarriedwithintheDSfieldof
ERSPANpacketheader.Range:0to63.Default:0.
| <VRF-NAME> |     |     | SpecifiesaVRFname.Default:default. |     |
| ---------- | --- | --- | ---------------------------------- | --- |
<SPAN-ID>
SpecifiesthespanIDfortheERSPANsessionandduringafailover.
Range:0to10.
Examples
CreatingaMirrorSessionandaddingtunneldestination,source,dscp,andVRF:
| switch# config  |        |         |     |     |
| --------------- | ------ | ------- | --- | --- |
| switch(config)# | mirror | session | 1   |     |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 74

switch(config-mirror-1)# destination tunnel 1.1.1.1 source 2.2.2.2 dscp 10 vrf
default
Replacingtheexistingtunneldestination:
switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 10 vrf
default
ReplacingtheexistingdestinationwithadifferentDSCPvalue:
switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 2 vrf
default
Removingthedestination:
| switch(config-mirror-1)# |     | no destination | tunnel |
| ------------------------ | --- | -------------- | ------ |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |              |           |
| ------------------- | ------- | ------------ | --------- |
| Release             |         | Modification |           |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
8400 config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
diagnostic
diagnostic
| diag utilities | tshark | [file]        |     |
| -------------- | ------ | ------------- | --- |
| diag utilities | tshark | [delete-file] |     |
Description
Capturespacketsfromamirror-to-cpusession,andsavethemostrecent32MBtopcapfilewhichcan
thenbecopiedandanalyzed.Whencapturingamirror-to-cpusessiontoafile,packetswillnotbe
dumpedtotheconsole.
Thediagnosticcommandmustbeenteredpriortothediag utilities tsharkcommand.
Usethedelete-fileformofthiscommandtodeletethemostrecentcapturefile.
Mirroring|75

Sincefileanddelete-fileareoptional,thebehaviorofthebasecommanddiag utilities tsharkdoes
notsaveanythingtoafile,andinsteaddumpsthetsharksessiontotheconsoleuntilCTRL + cis
entered.
| Parameter   |     |     | Description                           |     |     |
| ----------- | --- | --- | ------------------------------------- | --- | --- |
| file        |     |     | Savescapturedpacketstoatemporaryfile. |     |     |
| delete-file |     |     | Deletesthemostrecentcapturedfile.     |     |     |
Example
Performingdiagnostic:
| switch#    | diagnostic |             |            |              |            |
| ---------- | ---------- | ----------- | ---------- | ------------ | ---------- |
| switch#    | diagnostic | utilities   | tshark     | file         |            |
| Inspecting | traffic    | mirrored    | to the CPU | until Ctrl-C | is entered |
| ^CEnding   | traffic    | inspection. |            |              |            |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| diag utilities | tcpdump |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- |
diag utilities tcpdump [command <TEXT> | delete file <FILE-NAME> | list-files |
vrf <VRF-NAME> | count <COUNT-NUM> | proto <PROTO-NUM> | host-ip <IP-ADDR> | source-ip
<IP-ADDR> | destination-ip <IP-ADDR> | host-port <PORT> | source-port <PORT> |
destination-port <PORT> | verbosity <LEVEL> | print <DATA> | ethernet-type <ETH-NUM>]
Description
Capturestrafficreceivedortransmittedoveranetwork.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
command <TEXT> Capturespacketsbasedonaspecifiedtcpdumpcommandstring.
| delete file | <FILE-NAME> |     | Deletesspecifiedtcpdumplistfiles. |     |     |
| ----------- | ----------- | --- | --------------------------------- | --- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 76

Parameter

list-files

vrf <VRF-NAME>

count <COUNT-NUM>

proto <PROTO-NUM>

host-ip <IP-ADDR>

Description

Lists all the tcpdump capture files saved on the device.

Captures packets on the specified VRF. If no VRF is named, the
default is used.

Runs the tcpdump command until the specified number of
packets are captured. Range: 1-2147483647.

Captures packets of a particular type based on IP protocol
number. Range: 0-255.

Captures packets matching with the source or destination IP
address.

source-ip <IP-ADDR>

Captures packets from the specified IP address.

destination-ip <IP-ADDR>

Captures packets sent to the specified IP address.

host-port <PORT>

Captures packets matching with the source or destination port.

source-port <PORT>

Captures packets from the specified IP port.

destination-port <PORT>

Captures packets sent to the specified IP port.

verbosity <LEVEL>

Captures packets of the specified verbosity. Range: level1-level4. If
no verbosity is specified, the default is level1.

print <DATA>

Captures the data of each packet. The maximum is 262144 bytes

ethernet-type <ETH-NUM>

Captures packets based on the particular ethernet type. Range: 0-
65535.

Usage

n When using the command option, the only traffic captured will be packets that have been mirrored

to the CPU.

n When using the command option, command line sanitization is performed to prevent options that

may cause harm or security issues. The following options are blocked:

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

Mirroring | 77

Examples
InspectingtrafficmirroredtotheCPUviatcpdumpandsavingtheoutputtomy_capture_file.pcap:
switch#
|     | diag utilities | tcpdump | command | -c 2 -x | -w my_capture_file.pcap |     |
| --- | -------------- | ------- | ------- | ------- | ----------------------- | --- |
Inspecting traffic mirrored to the CPU via tcpdump until Ctrl-C is entered.
| 2 packets | captured         |           |     |     |     |     |
| --------- | ---------------- | --------- | --- | --- | --- | --- |
| 2 packets | received         | by filter |     |     |     |     |
| 0 packets | dropped          | by kernel |     |     |     |     |
| Ending    | traffic capture. |           |     |     |     |     |
Listingsavedcapturefiles:
| switch# | diag utilities | tcpdump | list-files |     |     |     |
| ------- | -------------- | ------- | ---------- | --- | --- | --- |
my_capture_file.pcap
Readingmy_capture_file.pcap:
| switch# | diag utilities | tcpdump | command | -r my_capture_file.pcap |     |     |
| ------- | -------------- | ------- | ------- | ----------------------- | --- | --- |
reading from file /tmp/tcpdump/my_capture_file1.pcap, link-type EN10MB (Ethernet)
1 11:59:34.047867 IP6 localhost.40318 > localhost.ntp: NTPv2, Reserved, length
12
0x0000: 0000 0304 0006 0000 0000 0000 0000 86dd ................
0x0010: 600a 7e47 0014 1140 0000 0000 0000 0000 `.~G...@........
0x0020: 0000 0000 0000 0001 0000 0000 0000 0000 ................
0x0030: 0000 0000 0000 0001 9d7e 007b 0014 0027 .........~.{...'
|     | 0x0040: 1601 | 0001 0000 | 0000 0000 | 0000 |     | ............ |
| --- | ------------ | --------- | --------- | ---- | --- | ------------ |
2 11:59:34.047915 IP6 localhost.ntp > localhost.40318: NTPv2, Reserved, length
12
0x0000: 0000 0304 0006 0000 0000 0000 0000 86dd ................
0x0010: 6b8d 23c5 0014 1140 0000 0000 0000 0000 k.#....@........
0x0020: 0000 0000 0000 0001 0000 0000 0000 0000 ................
0x0030: 0000 0000 0000 0001 007b 9d7e 0014 0027 .........{.~...'
|     | 0x0040: d681 | 0001 c016 | 0000 0000 | 0000 |     |     |
| --- | ------------ | --------- | --------- | ---- | --- | --- |
Removingmy_capture_file.pcap:
switch#
|              | diag utilities | tcpdump | delete-file | my_capture_file.pcap |     |     |
| ------------ | -------------- | ------- | ----------- | -------------------- | --- | --- |
| Successfully | removed        | file    |             |                      |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command | History     |     |                   |     |     |     |
| ------- | ----------- | --- | ----------------- | --- | --- | --- |
| Release |             |     | Modification      |     |     |     |
| 10.08   |             |     | Commandintroduced |     |     |     |
| Command | Information |     |                   |     |     |     |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 78

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
| switch(config)# |     | mirror session | 3   |     |
| --------------- | --- | -------------- | --- | --- |
switch(config-mirror-3)#
disable
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |              |           |
| -------------- | ----------- | ------- | ------------ | --------- |
| Release        |             |         | Modification |           |
| 10.07orearlier |             |         | --           |           |
| Command        | Information |         |              |           |
| Platforms      | Command     | context |              | Authority |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| enable | (mirror | session) |     |     |
| ------ | ------- | -------- | --- | --- |
enable
Description
Enablesthemirroringsessionforthecurrentcommandcontext.
Usage
Bydefault,mirroringsessionsaredisabled.
Whenamirroringsessionisenabled,theshow mirrorcommandforthatsessionIDshowsanAdmin
| StatusofenableandanOperation |     |     | Statusofenabled. |     |
| ---------------------------- | --- | --- | ---------------- | --- |
Mirroring|79

IfsFlowisenabledonaninterfaceandamirroringsessionspecifiesthesameinterfaceasthesourceof
receivedtraffic(thesourceisconfiguredwithadirectionofrxorboth):
n Theattempttoenablethemirroringsessionfailsandanerrorisreturned.
n Toenablethemirroringsession,firstyoumustdisablesFlowontheport.
Whenadding,removing,orchangingtheconfigurationofasourceinterfaceinanenabledmirroringsession,
packetsfromothermirrorsourcesusingthesamedestinationinterfacemightbeinterrupted.
Example
Configuringandenablingamirroringsession:
| switch(config)#          | mirror | session     | 3         |       |       |     |
| ------------------------ | ------ | ----------- | --------- | ----- | ----- | --- |
| switch(config-mirror-3)# |        | source      | interface | 1/1/2 | rx    |     |
| switch(config-mirror-3)# |        | destination | interface |       | 1/1/3 |     |
switch(config-mirror-3)#
|                          |     | comment | Monitor | router | port ingress-only | traffic |
| ------------------------ | --- | ------- | ------- | ------ | ----------------- | ------- |
| switch(config-mirror-3)# |     | enable  |         |        |                   |         |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |           |     |     |
| ------------------- | ------- | ------- | ------------ | --------- | --- | --- |
| Release             |         |         | Modification |           |     |     |
| 10.07orearlier      |         |         | --           |           |     |     |
| Command Information |         |         |              |           |     |     |
| Platforms           | Command | context |              | Authority |     |     |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| mirror session    |              |     |     |     |     |     |
| ----------------- | ------------ | --- | --- | --- | --- | --- |
| mirror session    | <SESSION-ID> |     |     |     |     |     |
| no mirror session | <SESSION-ID> |     |     |     |     |     |
Description
Createsamirroringsessionconfigurationcontextorentersanexistingmirroringsessionconfiguration
context.
Fromthiscontext,youcanentercommandstoconfigureandenableordisablethemirroringsession.
Thenoformofthiscommandremovesanexistingmirroringsessionfromtheconfiguration.
| Parameter    |     |     | Description                              |     |     |     |
| ------------ | --- | --- | ---------------------------------------- | --- | --- | --- |
| <SESSION-ID> |     |     | Specifiesthesessionidentifier.Range:1to4 |     |     |     |
Examples
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 80

| switch(config)# |     | mirror | session | 1   |
| --------------- | --- | ------ | ------- | --- |
switch(config-mirror-1)#
| switch(config)# |     | mirror | session | 3   |
| --------------- | --- | ------ | ------- | --- |
switch(config-mirror-3)#
| switch(config)# |     | no  | mirror session | 1   |
| --------------- | --- | --- | -------------- | --- |
switch(config)#
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |     |         |              |
| -------------- | ----------- | --- | ------- | ------------ |
| Release        |             |     |         | Modification |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
InformationintheAdmin Statuscolumnofthecommandoutputindicatestheconfiguredstatus.The
adminstatusisoneofthefollowingvalues:
n enable:Themirroringsessionisenabled.
n disable:Themirroringsessionhasbeenconfiguredbutnotyetenabled,orhasbeendisabled.
InformationintheOperation Statuscolumindicatesthestatusofthemirroringsession.Operation
statusisoneofthefollowingvalues:
Mirroring|81

n dest_doesnt_exist:Theconfigureddestinationinterfaceisnotfoundinthesystem.Themirroring
sessioncannotbeenabled.
n destination_shutdown: The mirroring session is enabled, but the destination interface is shut
| down. No | trafficcanbemonitored. |     |     |     |
| -------- | ---------------------- | --- | --- | --- |
n disabled:Themirroringsessionisdisabledandisnotinanerrorcondition.
n enabled:Themirroringsessionisenabled.
n external/driver_error:AninternalASIChardwareerroroccurred.
n hit_active_sessions_capacity:Themirroringsessioncouldnotbeenabledbecausethemaximum
numberofsupportedmirroringsessionsarealreadyenabled.
n internal_error:AninvalidparameterwaspassedtotheASICsoftwarelayer.
n no_dest_configured:Themirroringsessiondoesnothaveadestinationinterfaceconfigured.
no_name_configured:Asoftwareerroroccurred.ThemirroringsessiondoesnothaveasessionID
n
initsconfiguration.
n null_mirror:Asoftwareerroroccurred.Thesessionobjectreferenceisinvalid.
out_of_memory:Thesystemisoutofmemory,rebootrecommended.
n
n tunnel_route_resolution_not_populated:IfthedestinationtunnelIPaddressisnotreachable.
n unknown_error:Anunexpectederroroccurred.
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
switch#
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |     |              |     |
| -------------- | ----------- | --- | ------------ | --- |
| Release        |             |     | Modification |     |
| 10.07orearlier |             |     | --           |     |
| Command        | Information |     |              |     |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 82

| Platforms |     | Command | context |     | Authority |     |     |     |
| --------- | --- | ------- | ------- | --- | --------- | --- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| source    | interface |             |     |               |             |               |               |     |
| --------- | --------- | ----------- | --- | ------------- | ----------- | ------------- | ------------- | --- |
| source    | interface | {<PORT-NUM> |     | | <LAG-NAME>} |             | [<DIRECTION>] |               |     |
| no source | interface | {<PORT-NUM> |     | |             | <LAG-NAME>} |               | [<DIRECTION>] |     |
Description
Configuresthespecifiedinterface(eitheranEthernetportoraLAG)asasourceoftraffictobemirrored.
Thenoformofthiscommandceasesmirroringtrafficfromthespecifiedsourceinterfaceandremoves
thesourceinterfacefromthemirroringsessionconfiguration.
| Parameter  |     |     |     |     | Description                                    |     |     |     |
| ---------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| <PORT-NUM> |     |     |     |     | Specifiesaphysicalportontheswitch.Usetheformat |     |     |     |
member/slot/port(forexample,1/3/1).
<LAG-NAME> SpecifiestheidentifierfortheLAG(linkaggregationgroup).
<DIRECTION>
Selectsthedirectionoftraffictobemirroredfromthissource
interface.Thereisnodefaultforthisparameter.Validvaluesare
thefollowing:
| both |     |     |     |     | Mirrorbothtransmittedandreceivedpackets. |     |     |     |
| ---- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
| rx   |     |     |     |     | Mirroronlyreceivedpackets.               |     |     |     |
| tx   |     |     |     |     | Mirroronlytransmittedpackets.            |     |     |     |
Usage
Thereisalimitofsourceinterfacesineachdirectionofagivenmirrorsession:
|     |     |     |     | Source |     | interface | limit per mirror | session (4 |
| --- | --- | --- | --- | ------ | --- | --------- | ---------------- | ---------- |
Switch
|      |     |     |     | possible |     | sessions) |     |     |
| ---- | --- | --- | --- | -------- | --- | --------- | --- | --- |
| 8400 |     |     |     | 256      |     |           |     |     |
| 9300 |     |     |     | 128      |     |           |     |     |
However,thereisapracticallimittotheamountoftrafficthatamirrordestinationcantransmit.For
example,mirroringsessionwithmultiple10Gsourcescanoverwhelmasingle10Gdestination.
Youcanconfigurethesamesourceinterfaceinmultiplemirroringsessions,butonlyoneofthose
mirroringsessionscanbeenabledatatime.
Classifierpolicieswithmirroractionscanalsobeusedtomatchandmirrornetworktraffic.Although
mirroractionsofclassifierpoliciesmustspecifyanenabledmirroringsession,thetrafficmatchingand
mirroringactionsareseparatefromandtakepriorityoverbasicmirroringsessions.Forexample,
mirroringsession1mightmonitorasourceinterface,butaclassifierpolicymightmatchsometraffic
fromthatsamesourceinterfaceanddirectittothedestinationinterfaceofadifferentmirroring
Mirroring|83

session.Inthissituation,onlythetrafficthatisnotmatchedbythepolicyisconsideredformatchingby
mirroringsession1.
IfaninterfaceisinactiveusebythesFlowfeature,thenthatinterfacecannotbeusedassourceof
receivedtraffic(configuredasasourcedestinationwithadirectionofrxorboth)inanenabled
mirroringsession.Ifyouwanttousethisinterfaceasasourceofreceivedtrafficinamirroringsession,
youmustdisablesFlowontheinterfacebeforeyouenablethemirroringsessiononthesameinterface.
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
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 84

| switch(config-mirror-4)# |     |     | no source | interface | lag1 rx |
| ------------------------ | --- | --- | --------- | --------- | ------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |     |         |              |           |
| -------------- | ----------- | --- | ------- | ------------ | --------- |
| Release        |             |     |         | Modification |           |
| 10.07orearlier |             |     |         | --           |           |
| Command        | Information |     |         |              |           |
| Platforms      | Command     |     | context |              | Authority |
config-mirror-<SESSION-ID>
| Allplatforms |     |     |     |     | Administratorsorlocalusergroupmemberswith |
| ------------ | --- | --- | --- | --- | ----------------------------------------- |
executionrightsforthiscommand.
| source    | vlan            |     |          |         |     |
| --------- | --------------- | --- | -------- | ------- | --- |
| source    | vlan <VLAN-NUM> | {rx | | tx |   | both}   |     |
| no source | vlan <VLAN-NUM> |     | {rx | tx | | both} |     |
Description
MirroringwithVLANasasourceissupportedinthefollowingtrafficdirections:
n both-trafficreceivedandtransmitted
n rx-onlyreceivedtraffic
n tx-onlytransmittedtraffic
MorethanonesourceVLANcanbeconfiguredinamirrorsession.EachsuchVLANmayspecifyitsown
direction.
Thereisalimitof6sourceVLANsforagivenmirrorsession.Thereisalsoalimitof6sourceVLANs
acrossallmirrorsessions.
SameVLANmaynotbeconfiguredasamirrorsourceformultiplesessions.
WhenchangingasourceVLAN inanenabledmirrorsession(i.e.adding,changingdirection,orremoving)
mirroredpacketsbeingtransmittedoutofthemirrordestinationportfromothermirrorsourcesmaybebriefly
interruptedduringthereconfiguration.
DirectionofanexistingsourceVLANcanbeupdatedinoneoftwoways.
n Reenterthesource vlan <VLAN-NUM> <direction>commandwiththenewpreferreddirection.
n Usetheno source vlan <VLAN-NUM> <direction>formofthecommandwithadirection(rxortx)
toselectivelyremovethespecifieddirection.
SpecifyingthelastremainingdirectionforthatVLANwillremovetheVLANfromtheconfiguration
entirely.
MirroringallowsconfigurationofVLANasasource.WhenVLANsourceisconfiguredintherxdirection,
allpacketsaremirroredastheyarereceivedintheswitch.WhenVLANsourceisconfiguredintx
direction,allpacketsaremirroredastheyaretransmittedoutoftheswitch.
Mirroring|85

Forpacketsbridgedthroughtheswitch:
n Ifthemirrorisconfiguredin'both'direction,twocopiesofpacketsaremirrored,otherwiseonecopy
ofthepacketwillbemirrored.
Forroutedpackets:
n Ifthemirrorisconfiguredinrxdirection,packetsaremirroredinthepre-routedformwiththe
DestinationMACaddressastheswitchaddress.
Also,bridgedpacketsaretheonlypacketsmirroredintherxdirection.
n Ifthemirrorisconfiguredintxdirection,packetsaremirroredinpost-routedformwiththesource
MACastheswitchaddress.DestinationMACisthenexthopgatewayorstation.
n Ifthemirrorisconfiguredinbothdirection,onecopyofthepacketwillbemirrored.
TomirrorroutedpacketsreceivedonaVLANandtransmittedoutadifferentVLAN,enabletx
n
mirroringonthedestinationVLAN.
Controlplanepacketsgeneratedbytheswitch'sCPUareprocessedbothintheingressandtheegress
packetprocessingpipeline.ThefollowingarethebehaviorformirroringwithVLANassource:
n Ifthemirrorisconfiguredintherxortxdirection,thepacketsaremirroredtothemirror
destination.
n Ifthemirrorisconfiguredinthebothdirection,twocopiesofthepacketsaremirroredtothemirror
destination.
ThenoformcommandwillceasemirroringtrafficfromthespecifiedsourceVLANandremovethe
sourcefromthemirrorconfiguration.
| Parameter |     | Description |
| --------- | --- | ----------- |
VLAN-NUM
SelectstheVLANnumber.
direction Specifiesthedirectionofmirroring.tx(transmit),rx(receive),or
both.
Examples
CreatingamirrorsessionandaddingaVLANasasourceoftrafficinbothdirectionsonthatport:
| switch# configure        | terminal       |              |
| ------------------------ | -------------- | ------------ |
| switch(config)#          | mirror session | 1            |
| switch(config-mirror-1)# | source         | vlan 10 both |
CreatingamirrorsessionandaddingtwoVLANsassourcesoftraffic:
directions:
| switch# configure        | terminal       |              |
| ------------------------ | -------------- | ------------ |
| switch(config)#          | mirror session | 2            |
| switch(config-mirror-2)# | source         | vlan 10 tx   |
| switch(config-mirror-2)# | source         | vlan 20 both |
Configuringthesourceinsession2toreceivebyspecifyingthesourceinterfaceconfiguration:
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 86

| switch(config-mirror-2)# |     | source | vlan 10 rx |
| ------------------------ | --- | ------ | ---------- |
Removingthefirstsourceinterfaceinsession2entirely,andremovingthetransmitdirectionfromthe
othersothatmirroringonlyoccursinthereceivedirection:
| switch(config-mirror-2)# |     | source | vlan 10 rx |
| ------------------------ | --- | ------ | ---------- |
switch(config-mirror-2)#
|     |     | source | vlan 20 tx |
| --- | --- | ------ | ---------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Mirroring|87

Chapter 8
|            |          |            | Monitoring | a device | using SNMP |
| ---------- | -------- | ---------- | ---------- | -------- | ---------- |
| Monitoring | a device | using SNMP |            |          |            |
Configuring SNMP:RefertotheSNMP/MIBGuideforinformationonhowtoaddSNMPsoadevicecan
bemonitoredfromanetworkmanagementsystem(NMS).
Configuring an SNMP trap receiver:RefertotheSNMP/MIBGuideandspecificinformationaboutthe
| show snmp | trapcommandtoenableSNMPtraps. |     |     |     |     |
| --------- | ----------------------------- | --- | --- | --- | --- |
88
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries)

Chapter 9

Breakout cable support

Breakout cable support

Ports default to an unsplit state. When a port is 'split', the split interfaces become active and can be
configured independently. For example, when a 40G QSFP+ port is split four ways, each split interface
behaves like a separate 10G SFP+ port. The split interfaces have the same name as the base port with an
added suffix to represent their lane of the breakout cable or optical channel on SR4 optics. Splitting an
interface removes most of the port's configuration settings and makes it inactive. The port will no longer
appear in many show interface commands and most configuration commands are not allowed; the split
interface name must be used.

The same thing happens in reverse when an interface is unsplit. However, note that the 'split' and 'no
split' commands are always performed in the unsplit port's context.

Limitations with breakout cable support

n The 8400 switch does not support DAC breakout cables, only optical breakout cables.

n The JL365A Aruba 8400X 8p 40G QSFP+ Adv module does not support Priority-Based Flow Control

(PFC) on split ports.

n The JL366A Aruba 8400X 6p 40G/100G QSFP28 Adv module does not support 100G breakout cables; it

only supports split ports at the 40G speed (into 4x10G links).

Breakout cable support commands

split
split [<COUNT>][<SPEED>][confirm]
no split [confirm]

Description

Splits a port into multiple interfaces. Only ports capable of supporting breakout cables or
SR4/eSR4/eDR4 optics can be split.

Parameter

Description

<COUNT>

<SPEED>

confirm

Usage

Specifies the number of child interfaces to activate upon splitting
the port. Default: 4.

Specifies the speed for the child interfaces.

Specifies the confirmation of port splitting.

n Some switch interfaces support different split counts depending on the installed transceiver. For

these interfaces, the number of child interfaces to activate can be specified. If omitted, the default is

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

89

4.Fortransceiverscapableofsupportingmultiplesplitmodes,theclosestmodewithenoughlanesis
used.
n Sometransceiversalsosupportmultiplesplitmodeswithdifferentspeeds.Forexample,2x200Gor
2x100G.Whenaspeedisnotspecified,thehighestavailablespeedforthesplitcountisused.To
selectadifferentsplitmodewithalowerspeed,thedesiredspeedmustbespecified.
Thesplittableportsforallmodelsareshowninthetablebelow:
| Model |     |     | Description |     |     | Port info |     |
| ----- | --- | --- | ----------- | --- | --- | --------- | --- |
8400Xmodules
| n JL365A |     |     | 8400X8p40GQSFP+AdvModule |     |     | 1-8(40G) |     |
| -------- | --- | --- | ------------------------ | --- | --- | -------- | --- |
n JL366A
|     |     |     | 8400X6p40G/100GQSFP28Adv |     |     | 1-6Onlycapableof40Gsplitinto |     |
| --- | --- | --- | ------------------------ | --- | --- | ---------------------------- | --- |
|     |     |     | Module                   |     |     | 4x10G                        |     |
JL366Amodulesdonothave25G
MACstosupportsplit100G
8400Xmodules
n JL365A
|     |     |     | 8400X8p40GQSFP+AdvMod |     |     | 1-8(40G) |     |
| --- | --- | --- | --------------------- | --- | --- | -------- | --- |
n JL366A
|     |     |     | 8400X6p40G/100GQSFP28Adv |     |     | 1-6Onlycapableof40Gsplitinto |     |
| --- | --- | --- | ------------------------ | --- | --- | ---------------------------- | --- |
|     |     |     | Mod                      |     |     | 4x10G                        |     |
JL366Amodulesdonothave25G
MACstosupportsplit100G
Examples
Splittinganinterface:
| switch(config-if)# |     | interface | 1/1/1 |     |     |     |     |
| ------------------ | --- | --------- | ----- | --- | --- | --- | --- |
| switch(config-if)# |     | split     |       |     |     |     |     |
This command will disable the specified port, clear its configuration,
and split it into multiple interfaces. The split interfaces will not
| be available       | until | the  | next system | or line module | reboot. |     |     |
| ------------------ | ----- | ---- | ----------- | -------------- | ------- | --- | --- |
| Continue (y/n)?    |       | y    |             |                |         |     |     |
| switch(config-if)# |       | show | interface   | brief          |         |     |     |
----------------------------------------------------------------------------------
--
| Port Native | Mode | Type |     | Enabled Status | Reason |     | Speed |
| ----------- | ---- | ---- | --- | -------------- | ------ | --- | ----- |
| Desc        | VLAN |      |     |                |        |     |       |
----------------------------------------------------------------------------------
--
1/1/1:1 -- routed QSFP+DA3x4 yes down Split reboot pending -- --
1/1/1:2 -- routed QSFP+DA3x4 yes down Split reboot pending -- --
1/1/1:3 -- routed QSFP+DA3x4 yes down Split reboot pending -- --
1/1/1:4 -- routed QSFP+DA3x4 yes down Split reboot pending -- --
Unsplittingaportonaswitchthatrequiresareboot:
| switch(config)#    |     | interface | 1/1/1 |     |     |     |     |
| ------------------ | --- | --------- | ----- | --- | --- | --- | --- |
| switch(config-if)# |     | no split  |       |     |     |     |     |
Breakoutcablesupport|90

This command will disable the split interfaces for this port and clear
their configuration. The port will not be available until the next
| system   | or line module | reboot. |     |
| -------- | -------------- | ------- | --- |
| Continue | (y/n)? y       |         |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
8400 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 91

Chapter 10
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
isenabledonthedefaultVRF(snmp-server default)withoutdisablingSNMPonthemgmt(using
vrf
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
92
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries)

| snmp-server |     | vrf mgmt |     |     |     |     |
| ----------- | --- | -------- | --- | --- | --- | --- |
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
|     | switch(config)# | snmp-server | vrf mgmt |     |     |     |
| --- | --------------- | ----------- | -------- | --- | --- | --- |
switch(config)#
|     |     | snmp-server | vrf default |     |     |     |
| --- | --- | ----------- | ----------- | --- | --- | --- |
2. ConfiguretheSNMPv2Ccommunitytopublicbyenteringthesnmp-server community public
command.Inthisinstance,publicisaread-onlycommunitystring.
ArubaAirWave|93

|     | switch(config)# | snmp-server | community | public |
| --- | --------------- | ----------- | --------- | ------ |
3. Thecommunity-stringisusedbySNMPv1andSNMPv2Cforunencryptedauthentication.SNMPv3
letsyouencrypttheauthenticationmechanism.ToenableSNMPv3,enterthesnmpv3 userand
| snmpv3 | contextcommands. |     |     |     |
| ------ | ---------------- | --- | --- | --- |
switch(config)# snmpv3 user Admin auth sha auth-pass ciphertext
AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=
|     | priv des priv-pass | ciphertext |     |     |
| --- | ------------------ | ---------- | --- | --- |
AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=
switch(config)#
|     |     | snmpv3 context | Admin |     |
| --- | --- | -------------- | ----- | --- |
FordiscoveringdevicesinAirWavethroughtheSNMPv3community,theSNMPv3contextnameis
notmandatory.DevicescanstillbediscoveredinArubaAirWavewithouttheSNMPv3context
name.
4. Enterthelogging commandforenablingsyslogforwardingtoaremotesyslogserver,suchas
AirWave:
|     | switch(config)# | logging 10.0.10.2 | severity | debug |
| --- | --------------- | ----------------- | -------- | ----- |
5. SNMPtrapsenableanagenttonotifythemanagementstationofsignificanteventsbywayofan
unsolicitedSNMPmessage.EnableSNMPtrapsbyenteringthesnmp-server hostcommand:
switch(config)# snmp-server host 10.10.10.10 trap version v2c vrf default
SNMPtrapscannotbeforwardedfromAOS-CX10.00switchesthathavetheVRFconfiguredas
mgmt.LaterversionsofAOS-CXsupportSNMPtrapforwardingevenwhentheVRFisconfiguredas
defaultormgmt.
6. ForinformationonhowtoaddadeviceformonitoringintheArubaAirWaveuserinterface,see
thedocumentationforArubaAirWave.
| AirWave | commands |     |     |     |
| ------- | -------- | --- | --- | --- |
logging
logging {<IPV4-ADDR> | <IPV6-ADDR> | <FQDN | HOSTNAME>} [ {udp [<PORT-NUM>] }|{tcp
[<PORT-NUM>} | {tls [<PORT-NUM> [auth-mode {certificate|subject-name}] [legacy-tls-
renegotiation]}] [severity <LEVEL>] [vrf <VRF-NAME>] [include-auditable-events]
[filter <FILTER-NAME>] [ rate-limit-burst <BURST> [rate-limit-interval <INTERVAL>] ]
| no logging | {<IPV4-ADDR> | | <IPV6-ADDR> | | <HOSTNAME> |     |
| ---------- | ------------ | ------------- | ------------ | --- |
Description
Enablessyslogforwardingtoaremotesyslogserver.
Thenoformofthiscommanddisablessyslogforwardingtoaremotesyslogserver.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 94

Parameter

Description

{<IPV4-ADDR> | <IPV6-ADDR> | <HOSTNAME>}

Selects the IPv4 address, IPv6 address, or host name
of the remote syslog server. Required.

[udp [<PORT-NUM>] | tcp [<PORT-NUM>]]

Specifies the UDP port or TCP port of the remote
syslog server to receive the forwarded syslog
messages.

udp [<PORT-NUM>]

tcp [<PORT-NUM>]

tls [<PORT-NUM>]

include-auditable-events

severity <LEVEL>

auth-mode

legacy-tls-renegotiation

vrf <VRF-NAME>

Examples

Range: 1 to 65535. Default: 514

Range: 1 to 65535. Default: 1470

Range: 1 to 65535. Default: 6514

Specifies that auditable messages are also logged to
the remote syslog server.

Specifies the severity of the syslog messages:
n alert: Forwards syslog messages with the

severity of alert (6) and emergency (7).
n crit: Forwards syslog messages with the severity

of critical (5) and above.

n debug: Forwards syslog messages with the

severity of debug (0) and above.

n emerg: Forwards syslog messages with the

severity of emergency (7) only.

n err: Forwards syslog messages with the severity

of err (4) and above

n info: Forwards syslog messages with the severity

of info (1) and above. Default.

n notice: Forwards syslog messages with the

severity of notice (2) and above.

n warning: Forwards syslog messages with the

severity of warning (3) and above.

Specifies the TLS authentication mode used to
validate the certificate.

n certificate: Validates the peer using trust anchor

certificate based authentication. Default.
n subject-name: Validates the peer using trust

anchor certificates as well as subject-name based

authentication.

Enables the TLS connection with a remote syslog
server supporting legacy renegotiation.

Specifies the VRF used to connect to the syslog
server. Optional. Default: default

Enabling the syslog forwarding to remote syslog server 10.0.10.2:

switch(config)# logging 10.0.10.2

Aruba AirWave | 95

Enablingthesyslogforwardingofmessageswithaseverityoferr (4)andabovetoTCPport4242on
remotesyslogserver10.0.10.9withVRFlab_vrf:
switch(config)# logging 10.0.10.9 tcp 4242 severity err vrf lab_vrf
Disablingsyslogforwardingtoaremotesyslogserver:
| switch(config)# |     | no logging |     |     |     |
| --------------- | --- | ---------- | --- | --- | --- |
EnablingsyslogforwardingoverTLStoaremotesyslogserverusingsubject-nameauthenticationmode:
| switch(config)# |             | logging example.com |     | tls auth-mode | subject name |
| --------------- | ----------- | ------------------- | --- | ------------- | ------------ |
| Command         | History     |                     |     |               |              |
| Release         |             |                     |     | Modification  |              |
| 10.07orearlier  |             |                     |     | --            |              |
| Command         | Information |                     |     |               |              |
| Platforms       | Command     | context             |     | Authority     |              |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    |           | community |     |     |     |
| -------------- | --------- | --------- | --- | --- | --- |
| snmp-server    | community | <STRING>  |     |     |     |
| no snmp-server | community | <STRING>  |     |     |     |
Description
AddsanSNMPv1/SNMPv2ccommunitystring.Acommunitystringisapasswordthatcontrolsread
accesstotheSNMPagent.Anetworkmanagementprogrammustsupplythisnamewhenattemptingto
getSNMPinformationfromtheswitch.Amaximumof10communitystringsaresupported.Onceyou
createyourowncommunitystring,thedefaultcommunitystring(public)isdeleted.
ThenoformofthiscommandremovesthespecifiedSNMPv1/SNMPv2ccommunitystring.Whenno
communitystringexists,adefaultcommunitystringwiththevaluepublicisautomaticallydefined.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<STRING> SpecifiestheSNMPv1/SNMPv2ccommunitystring.Range:1to32
printableASCIIcharacters,excludingspaceandquestionmark.
Examples
SettingtheSNMPv1/SNMPv2ccommunitystringtoprivate:
| switch(config)# |     | snmp-server | community | private |     |
| --------------- | --- | ----------- | --------- | ------- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 96

RemovingSNMPv1/SNMPv2ccommunitystringprivate:
| switch(config)# | no          | snmp-server | community    | private |
| --------------- | ----------- | ----------- | ------------ | ------- |
| Command         | History     |             |              |         |
| Release         |             |             | Modification |         |
| 10.07orearlier  |             |             | --           |         |
| Command         | Information |             |              |         |
| Platforms       | Command     | context     | Authority    |         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server | host |     |     |     |
| ----------- | ---- | --- | --- | --- |
snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>]
| [port <UDP-PORT>] | [vrf | <VRF-NAME>] |     |     |
| ----------------- | ---- | ----------- | --- | --- |
no snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>]
| [port <UDP-PORT>] | [vrf | <VRF-NAME>] |     |     |
| ----------------- | ---- | ----------- | --- | --- |
snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]
| [port <UDP-PORT>] | [vrf | <VRF-NAME>] |     |     |
| ----------------- | ---- | ----------- | --- | --- |
no snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]
| [port <UDP-PORT>] | [vrf | <VRF-NAME>] |     |     |
| ----------------- | ---- | ----------- | --- | --- |
snmp-server host <IPv4-ADDR> [trap version v3 | inform version v3] user <NAME>
| [port <UDP-PORT>] | [vrf | <VRF-NAME>] |     |     |
| ----------------- | ---- | ----------- | --- | --- |
no snmp-server host <IPv4-ADDR> [trap version v3 | inform version v3] user <NAME>
| [port <UDP-PORT>] | [vrf | <VRF-NAME>] |     |     |
| ----------------- | ---- | ----------- | --- | --- |
Description
Configuresatrap/informsreceivertowhichtheSNMPagentcansendSNMPv1/v2c/v3trapsorv2c
informs.Amaximumof30SNMPtraps/informsreceiverscanbeconfigured.
Thenoformofthiscommandremovesthespecifiedtrap/informreceiver.
| Configuringsnmpv3 | informsisnotsupported. |     |                                                  |     |
| ----------------- | ---------------------- | --- | ------------------------------------------------ | --- |
| Parameter         |                        |     | Description                                      |     |
| <IPv4-ADDR>       |                        |     | SpecifiestheIPaddressofatrapreceiverinIPv4format |     |
(x.x.x.x),wherexisadecimalnumberfrom0to255.Youcan
removeleadingzeros.Forexample,theaddress
192.169.005.100becomes192.168.5.100.
trap version <VERSION> SpecifiesthetrapnotificationtypeforSNMPv1orv2c.Available
optionsare:v1orv2c.
inform version v2c SpecifiestheinformnotificationtypeforSNMPv2c.
| trap version | v3  |     | SpecifiesthetrapnotificationtypeforSNMPv3. |     |
| ------------ | --- | --- | ------------------------------------------ | --- |
ArubaAirWave|97

| Parameter   |     |     | Description                                     |     |     |
| ----------- | --- | --- | ----------------------------------------------- | --- | --- |
| user <NAME> |     |     | SpecifiestheSNMPv3usernametobeusedintheSNMPtrap |     |     |
notifications.
| community <STRING> |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- |
Specifiesthenameofthecommunitystringtousewhensending
trapnotifications.Range:1-32printableASCIIcharacters,
excludingspaceandquestionmark.Default:public.
<UDP-PORT>
SpecifiestheUDPportonwhichnotificationsaresent.Range:1-
65535.Default:162.
vrf <VRF-NAME> SpecifiesthenameoftheVRFonwhichtosendthenotifications.
Examples
| switch(config)# | snmp-server | host | 10.10.10.10 | trap version | v1  |
| --------------- | ----------- | ---- | ----------- | ------------ | --- |
switch(config)# no snmp-server host 10.10.10.10 trap version v1
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public
port 5000
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
port 5000
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public
| port 5000 | vrf default |     |     |     |     |
| --------- | ----------- | --- | --- | --- | --- |
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
| port 5000 | vrf default |     |     |     |     |
| --------- | ----------- | --- | --- | --- | --- |
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community
public
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
port 5000
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community
| public port | 5000 |     |     |     |     |
| ----------- | ---- | --- | --- | --- | --- |
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
| port 5000 | vrf default |     |     |     |     |
| --------- | ----------- | --- | --- | --- | --- |
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community
| public port | 5000 vrf | default |     |     |     |
| ----------- | -------- | ------- | --- | --- | --- |
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin port 2000
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin port
2000
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 98

| snmp-server    |     | vrf        |     |     |     |     |
| -------------- | --- | ---------- | --- | --- | --- | --- |
| snmp-server    | vrf | <VRF-NAME> |     |     |     |     |
| no snmp-server | vrf | <VRF-NAME> |     |     |     |     |
Description
ConfigurestheVRFonwhichtheSNMPagentlistensforincomingrequests.Bydefault,theSNMPagent
doesnotlistenonanyVRF.
ThenoformofthiscommandstopstheSNMPagentfromlisteningforincomingrequestsonthe
specifiedVRF.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<VRF-NAME> SpecifiestheVRFonwhichtheSNMPagentlistensforincoming
requests.TheSNMPagentcanlistenoneitherthemgmtor
defaultVRF.Ifconfiguredforboth,theSNMPagentlistenson
default,whichhasahigherpriority.
Example
| switch(config)# |             | snmp-server |             | vrf | default      |     |
| --------------- | ----------- | ----------- | ----------- | --- | ------------ | --- |
| switch(config)# |             | no          | snmp-server |     | vrf default  |     |
| Command         | History     |             |             |     |              |     |
| Release         |             |             |             |     | Modification |     |
| 10.07orearlier  |             |             |             |     | --           |     |
| Command         | Information |             |             |     |              |     |
| Platforms       | Command     |             | context     |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmpv3    | context        |        |                |             |            |           |
| --------- | -------------- | ------ | -------------- | ----------- | ---------- | --------- |
| snmpv3    | context <NAME> |        | vrf <VRF-NAME> |             | [community | <STRING>] |
| no snmpv3 | context        | <NAME> | [vrf           | <VRF-NAME>] |            |           |
Description
CreatesanSNMPv3contextonthespecifiedVRF.
ThenoformofthiscommandremovesthespecifiedSNMPcontext.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<NAME>
Specifiesthenameofthecontext.Range:1to32printableASCII
ArubaAirWave|99

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
characters,excludingspaceandquestionmark(?).
vrf <VRF-NAME> SpecifiestheVRFassociatedwiththecontext.Default:default.
community <STRING> SpecifiestheSNMPcommunitystringassociatedwiththecontext.
Range:1to32printableASCIIcharacters,excludingspaceand
questionmark.Default:public.
Examples
CreatinganSNMPv3contextnamednewContext:
| switch(config)# |     |     | snmpv3 | context | newContext |     |     |
| --------------- | --- | --- | ------ | ------- | ---------- | --- | --- |
CreatinganSNMPv3contextnamednewContextonVRFmyVrfandwithcommunitystringprivate.
switch(config)# snmpv3 context newContext vrf myVrf community private
RemovingtheSNMPv3contextnamednewContextonVRFmyVrf:
| switch(config)# |             |         | no snmpv3 | context | newContext   | vrf myVrf |     |
| --------------- | ----------- | ------- | --------- | ------- | ------------ | --------- | --- |
| Command         | History     |         |           |         |              |           |     |
| Release         |             |         |           |         | Modification |           |     |
| 10.07orearlier  |             |         |           |         | --           |           |     |
| Command         | Information |         |           |         |              |           |     |
| Platforms       |             | Command | context   |         | Authority    |           |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmpv3 | user |     |     |     |     |     |     |
| ------ | ---- | --- | --- | --- | --- | --- | --- |
snmpv3 user <NAME> [auth <AUTH-PROTOCOL> auth-pass {plaintext | ciphertext}
<AUTH-PWORD> [priv <PRIV-PROTOCOL> priv-pass {plaintext | ciphertext} <PRIV-PWORD>] ]
| no snmpv3    | user | <NAME> | [auth           | <AUTH-PROTOCOL> |           | auth-pass     |     |
| ------------ | ---- | ------ | --------------- | --------------- | --------- | ------------- | --- |
| <AUTH-PWORD> |      | [priv  | <PRIV-PROTOCOL> |                 | priv-pass | <PRIV-PWORD>] | ]   |
Description
CreatesanSNMPv3userandaddsittoanSNMPv3context.
ThenoformofthiscommandremovesthespecifiedSNMPv3user.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 100

Parameter

<NAME>

auth <AUTH-PROTOCOL>

auth-pass {plaintext | ciphertext} <AUTH-PWORD>

priv <PRIV-PROTOCOL>

priv-pass {plaintext | ciphertext} <PRIV-PWORD>

Description

Specifies the SNMPv3 username. Range 1 - 32
printable ASCII characters, excluding space
and question mark.

Specifies the authentication protocol used to
validate user logins. Available options are:
md5 or sha.

Specifies the SNMPv3 user password. Range
for plaintext is 8 - 32 printable ASCII
characters, excluding space and question
mark.
Range for ciphertext is 1 - 120 printable
ASCII characters. This option is only used
when copying user configuration settings
between switches. It enables you to duplicate
a user's configuration on another switch
without having to know their password.

Specifies the SNMPv3 security protocol
(encryption method). Available options are:
aes or des.

Specifies the SNMPv3 user privacy
passphrase. Range for plaintext is 8 - 32
printable ASCII characters, excluding space
and question mark.
Range for ciphertext is 1 - 120 printable
ASCII characters. This option is only used
when copying user configuration settings
between switches. It enables you to duplicate
a user's configuration on another switch
without having to know their password.

Examples

Defining an SNMPv3 user named Admin using sha authentication with the plaintext password
mypassword and using des security with the plaintext password myprivpass:

switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des
priv-pass plaintext myprivpass

Removing an SNMPv3 user named Admin:

switch(config)# no snmpv3 user Admin

Defining an SNMPv3 user named Admin using sha authentication with the plaintext password
mypassword and using des security with the plaintext password myprivpass:

switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des
priv-pass plaintext myprivpass

Copying an SNMP user from switch 1 to switch 2.

Aruba AirWave | 101

Onswitch1,configureausercalledAdmin,thenissuetheshow running-configcommandtodisplay
switchconfigurationsettings.Thesnmpv3usercommandusestheciphertextoptiontoprotectthe
users'spasswords.
switch1(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword
| priv des | priv-pass | plaintext |     | myprivpass |     |
| -------- | --------- | --------- | --- | ---------- | --- |
switch1(config)#
exit
| switch1#               | show | running-config |     |     |     |
| ---------------------- | ---- | -------------- | --- | --- | --- |
| Current configuration: |      |                |     |     |     |
!
| !Version | AOS-CX | TL.10.00.0003-8017-gdeb0606~dirty |     |     |     |
| -------- | ------ | --------------------------------- | --- | --- | --- |
!
!
!
| snmpv3 user | Admin | auth | sha | auth-pass | ciphertext |
| ----------- | ----- | ---- | --- | --------- | ---------- |
AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=
| priv des | priv-pass | ciphertext |     |     |     |
| -------- | --------- | ---------- | --- | --- | --- |
AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=
| ssh server | vrf | mgmt |     |     |     |
| ---------- | --- | ---- | --- | --- | --- |
!
!
!
!
| interface   | mgmt |     |     |     |     |
| ----------- | ---- | --- | --- | --- | --- |
| no shutdown |      |     |     |     |     |
| ip dhcp     |      |     |     |     |     |
vlan 1
Onswitch2,executethesnmpv3usercommandthatwasdisplayedbyshow running-configonswitch
1.Thiscreatestheuseronswitch2withthesameconfigurationsettings.
switch1(config)#
|     |     | snmpv3 | user | Admin | auth sha auth-pass |
| --- | --- | ------ | ---- | ----- | ------------------ |
ciphertextAQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=priv
| des priv-pass |     | ciphertext |     |     |     |
| ------------- | --- | ---------- | --- | --- | --- |
AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=
| Command History     |         |     |         |     |              |
| ------------------- | ------- | --- | ------- | --- | ------------ |
| Release             |         |     |         |     | Modification |
| 10.07orearlier      |         |     |         |     | --           |
| Command Information |         |     |         |     |              |
| Platforms           | Command |     | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxMonitoringGuide|(8400SwitchSeries) 102

Chapter 11

Support and Other Resources

Support and Other Resources

Accessing Aruba Support

Aruba Support Services

https://www.hpe.com/us/en/networking/hpe-aruba-networking-
support-services.html

AOS-CX Switch Software Documentation
Portal

https://arubanetworking.hpe.com/techdocs/AOS-CX/help_
portal/Content/home.htm

Aruba Support Portal

https://networkingsupport.hpe.com/home

North America telephone

1-800-943-4526 (US & Canada Toll-Free Number)

+1-650-750-0350 (Backup—Toll Number)

International telephone

https://www.hpe.com/psnow/doc/a50011948enw

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

https://developer.arubanetworks.com/hpe-aruba-networking-aoscx/docs/about

https://community.arubanetworks.com/

Videos on new features introduced in this release:

https://www.youtube.com/playlist?list=PLsYGHuNuBZcbWPEjjHuVMqP-Q_UL3CskS

HPE Aruba
Networking
Developer Hub

Airheads social
forums and
Knowledge Base

AOS-CX

Software

Technical

Update channel

on YouTube.

AOS-CX 10.15.xxxx Monitoring Guide | (8400 Switch Series)

103

ArubaHardware https://arubanetworking.hpe.com/techdocs/hardware/DocumentationPortal/Content/home.
| Documentation | htmm |     |
| ------------- | ---- | --- |
andTranslations
Portal
| Arubasoftware | https://networkingsupport.hpe.com/downloads |     |
| ------------- | ------------------------------------------- | --- |
| Software      | https://licensemanagement.hpe.com/          |     |
licensingand
FeaturePacks
| End-of-Life | https://networkingsupport.hpe.com/end-of-life |     |
| ----------- | --------------------------------------------- | --- |
information
| Accessing | Updates |     |
| --------- | ------- | --- |
YoucanaccessupdatesfromtheArubaSupportPortalathttps://networkingsupport.hpe.com.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://networkingsupport.hpe./notifications/subscriptions(requiresanactiveArubaSupportPortal
accounttomanagesubscriptions).SecuritynoticesareviewablewithoutanArubaSupportPortal
account.
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
productrecycling,energyefficiency),andsafetyinformationandcompliancedata,(RoHSandWEEE).For
moreinformation,seehttps://www.arubanetworks.com/company/about-us/environmental-citizenship/.
| Documentation |     | Feedback |
| ------------- | --- | -------- |
Arubaiscommittedtoprovidingdocumentationthatmeetsyourneeds.Tohelpusimprovethe
documentation,sendanyerrors,suggestions,orcommentstoDocumentationFeedback
(docsfeedback-switching@hpe.com).Whensubmittingyourfeedback,includethedocumenttitle,part
number,edition,andpublicationdatelocatedonthefrontcoverofthedocument.Foronlinehelp
content,includetheproductname,productversion,helpedition,andpublicationdatelocatedonthe
legalnoticespage.
SupportandOtherResources|104