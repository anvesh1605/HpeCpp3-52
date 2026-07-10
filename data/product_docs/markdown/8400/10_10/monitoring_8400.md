AOS-CX 10.10 Monitoring
Guide

8400 Switch Series

Published: November 2023

Version: 3

Copyright Information

© Copyright 2024 Hewlett Packard Enterprise Development LP.

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

3

Contents
| About                                             | this document                      |              |          |             |               | 7   |
| ------------------------------------------------- | ---------------------------------- | ------------ | -------- | ----------- | ------------- | --- |
| Applicableproducts                                |                                    |              |          |             |               | 7   |
| Latestversionavailableonline                      |                                    |              |          |             |               | 7   |
| Commandsyntaxnotationconventions                  |                                    |              |          |             |               | 7   |
| Abouttheexamples                                  |                                    |              |          |             |               | 8   |
| Identifyingswitchportsandinterfaces               |                                    |              |          |             |               | 8   |
| Identifyingmodularswitchcomponents                |                                    |              |          |             |               | 9   |
| Aruba                                             | 8400 switch                        | series       | member,  | slot, and   | port notation | 10  |
| LineModulesandManagementModules                   |                                    |              |          |             |               | 10  |
| Monitoring                                        | hardware                           | through      | visual   | observation |               | 12  |
| ConfirmingnormaloperationoftheswitchbyreadingLEDs |                                    |              |          |             |               | 12  |
| Detectingiftheswitchisnotreadyforafailoverevent   |                                    |              |          |             |               | 13  |
| FindingfaultedcomponentsusingtheswitchLEDs        |                                    |              |          |             |               | 13  |
| Boot                                              | commands                           |              |          |             |               | 15  |
| bootfabric-module                                 |                                    |              |          |             |               | 15  |
| bootline-module                                   |                                    |              |          |             |               | 16  |
| bootmanagement-module                             |                                    |              |          |             |               | 17  |
| bootset-default                                   |                                    |              |          |             |               | 18  |
| bootsystem                                        |                                    |              |          |             |               | 19  |
| showboot-history                                  |                                    |              |          |             |               | 21  |
| Switch                                            | system                             | and hardware | commands |             |               | 23  |
| External                                          | storage                            |              |          |             |               | 24  |
| Externalstoragecommands                           |                                    |              |          |             |               | 24  |
|                                                   | address                            |              |          |             |               | 24  |
|                                                   | directory                          |              |          |             |               | 25  |
|                                                   | disable                            |              |          |             |               | 26  |
|                                                   | enable                             |              |          |             |               | 26  |
|                                                   | external-storage                   |              |          |             |               | 27  |
|                                                   | password(external-storage)         |              |          |             |               | 28  |
|                                                   | showexternal-storage               |              |          |             |               | 29  |
|                                                   | showrunning-configexternal-storage |              |          |             |               | 29  |
|                                                   | type                               |              |          |             |               | 30  |
|                                                   | username                           |              |          |             |               | 31  |
|                                                   | vrf                                |              |          |             |               | 32  |
| IP-SLA                                            |                                    |              |          |             |               | 33  |
| IP-SLAguidelines                                  |                                    |              |          |             |               | 33  |
| LimitationswithVoIPSLAs                           |                                    |              |          |             |               | 34  |
| IP-SLAcommands                                    |                                    |              |          |             |               | 34  |
|                                                   | http                               |              |          |             |               | 34  |
|                                                   | icmp-echo                          |              |          |             |               | 35  |
|                                                   | ip-sla                             |              |          |             |               | 36  |
|                                                   | ip-slaresponder                    |              |          |             |               | 37  |
5
AOS-CX10.10MonitoringGuide| (8400SwitchSeries)

|                                                  | showip-slaresponder        |            | 38  |
| ------------------------------------------------ | -------------------------- | ---------- | --- |
|                                                  | showip-slaresponderresults |            | 39  |
|                                                  | showip-sla<SLA-NAME>       |            | 39  |
|                                                  | start-test                 |            | 42  |
|                                                  | stop-test                  |            | 43  |
|                                                  | tcp-connect                |            | 43  |
|                                                  | udp-echo                   |            | 44  |
|                                                  | udp-jitter-voip            |            | 46  |
|                                                  | vrf                        |            | 47  |
|                                                  | showinterface              |            | 48  |
| Mirroring                                        |                            |            | 52  |
| MirroringandsFlow                                |                            |            | 52  |
| Mirrorstatistics                                 |                            |            | 53  |
| Classifierpoliciesandmirroringsessions           |                            |            | 53  |
| Mirroringcommands                                |                            |            | 54  |
|                                                  | clearmirror                |            | 54  |
|                                                  | comment                    |            | 55  |
|                                                  | copytcpdump-pcap           |            | 56  |
|                                                  | copytshark-pcap            |            | 57  |
|                                                  | destinationcpu             |            | 57  |
|                                                  | destinationinterface       |            | 58  |
|                                                  | destinationtunnel          |            | 59  |
|                                                  | diagnostic                 |            | 61  |
|                                                  | diagutilitiestcpdump       |            | 62  |
|                                                  | disable                    |            | 64  |
|                                                  | enable                     |            | 64  |
|                                                  | mirrorsession              |            | 65  |
|                                                  | showmirror                 |            | 66  |
|                                                  | sourceinterface            |            | 68  |
| Monitoring                                       | a device                   | using SNMP | 71  |
| Breakout                                         | cable support              |            | 72  |
| Limitationswithbreakoutcablesupport              |                            |            | 72  |
| Breakoutcablesupportcommands                     |                            |            | 72  |
|                                                  | split                      |            | 72  |
| Aruba                                            | AirWave                    |            | 75  |
| SNMPsupportandAirWave                            |                            |            | 75  |
|                                                  | SNMPontheswitch            |            | 75  |
| SupportedfeatureswithAirWaveandtheAOS-CXswitch   |                            |            | 76  |
| ConfiguringtheAOS-CXswitchtobemonitoredbyAirWave |                            |            | 76  |
| Support                                          | and Other                  | Resources  | 78  |
| AccessingHPEArubaNetworkingSupport               |                            |            | 78  |
| AccessingUpdates                                 |                            |            | 79  |
|                                                  | ArubaSupportPortal         |            | 79  |
|                                                  | MyNetworking               |            | 79  |
| WarrantyInformation                              |                            |            | 79  |
| RegulatoryInformation                            |                            |            | 80  |
| DocumentationFeedback                            |                            |            | 80  |
|6

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n Aruba 8400 Switch Series (JL375A, JL376A)

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

7

| Convention |     | Usage                                                    |     |
| ---------- | --- | -------------------------------------------------------- | --- |
| [ ]        |     | Brackets.Indicatesthattheencloseditemoritemsareoptional. |     |
| …or        |     | Ellipsis:                                                |     |
... n Incodeandscreenexamples,averticalorhorizontalellipsisindicatesan
omissionofinformation.
n Insyntaxusingbracketsandbraces,anellipsisindicatesitemsthatcanbe
repeated.Whenanitemfollowedbyellipsesisenclosedinbrackets,zero
ormoreitemscanbespecified.
| About the | examples |     |     |
| --------- | -------- | --- | --- |
Examplesinthisdocumentarerepresentativeandmightnotmatchyourparticularswitchor
environment.
Theslotandportnumbersinthisdocumentareforillustrationonlyandmightbeunavailableonyour
switch.
| Understanding | the CLI prompts |     |     |
| ------------- | --------------- | --- | --- |
Whenillustratingthepromptsinthecommandlineinterface(CLI),thisdocumentusesthegenericterm
switch,insteadofthehostnameoftheswitch.Forexample:
switch>
TheCLIpromptindicatesthecurrentcommandcontext.Forexample:
switch>
Indicatestheoperatorcommandcontext.
switch#
Indicatesthemanagercommandcontext.
switch(CONTEXT-NAME)#
Indicatestheconfigurationcontextforafeature.Forexample:
switch(config-if)#
Identifiestheinterfacecontext.
| Variable information | in  | CLI prompts |     |
| -------------------- | --- | ----------- | --- |
Incertainconfigurationcontexts,thepromptmayincludevariableinformation.Forexample,whenin
theVLANconfigurationcontext,aVLANnumberappearsintheprompt:
switch(config-vlan-100)#
Whenreferringtothiscontext,thisdocumentusesthesyntax:
switch(config-vlan-<VLAN-ID>)#
Where<VLAN-ID>isavariablerepresentingtheVLANnumber.
| Identifying | switch | ports and | interfaces |
| ----------- | ------ | --------- | ---------- |
Physicalportsontheswitchandtheircorrespondinglogicalsoftwareinterfacesareidentifiedusingthe
format:
member/slot/port
| On the 8400 Switch | Series |     |     |
| ------------------ | ------ | --- | --- |
Aboutthisdocument|8

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

9

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

10

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

Aruba 8400 switch series member, slot, and port notation | 11

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

12

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
Monitoringhardwarethroughvisualobservation|13

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

14

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
| Command History |     |     |     |
| --------------- | --- | --- | --- |
15
AOS-CX10.10MonitoringGuide|(8400SwitchSeries)

| Release             |         |     |         | Modification |
| ------------------- | ------- | --- | ------- | ------------ |
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
| Command History     |     |     |     |              |
| ------------------- | --- | --- | --- | ------------ |
| Release             |     |     |     | Modification |
| 10.07orearlier      |     |     |     | --           |
| Command Information |     |     |     |              |
Bootcommands|16

Platforms

Command context

Authority

8400

Manager (#)

Administrators or local user group members with execution
rights for this command.

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

17

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
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| boot set-default |     |          |              |     |     |     |     |
| ---------------- | --- | -------- | ------------ | --- | --- | --- | --- |
| boot set-default |     | {primary | | secondary} |     |     |     |     |
Description
Setsthedefaultoperatingsystemimagetousewhenthesystemisbooted.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
primary
Selectstheprimarynetworkoperatingsystemimage.
| secondary |     |     |     |     | Selectsthesecondarynetworkoperatingsystemimage. |     |     |
| --------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- |
Example
Selectingtheprimaryimageasthedefaultbootimage:
| switch# | boot    | set-default | primary         |     |     |     |     |
| ------- | ------- | ----------- | --------------- | --- | --- | --- | --- |
| Default | boot    | image       | set to primary. |     |     |     |     |
| Command | History |             |                 |     |     |     |     |
Bootcommands|18

Release

10.07 or earlier

Modification

--

Command Information

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

19

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
Bootcommands|20

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show boot-history |       |     |     |
| ----------------- | ----- | --- | --- |
| show boot-history | [all] |     |     |
Description
Showsbootinformation.Whennoparametersarespecified,showsthemostrecentinformationabout
thebootoperation,andthethreepreviousbootoperationsfortheactivemanagementmodule.When
theallparameterisspecified,showsthebootinformationfortheactivemanagementmoduleandall
availablelinemodules.Toviewboot-historyonthestandby,thecommandmustbesentonthestandby
console.
| Parameter |     |     | Description                                         |
| --------- | --- | --- | --------------------------------------------------- |
| all       |     |     | Showsbootinformationfortheactivemanagementmoduleand |
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
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 21

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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Bootcommands|22

Chapter 5
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
Switchsystemandhardwarecommandsaregeneralcommandsusedtoconfigurefundamentalsettings
ontheswitch.
RefertotheFundamentalsGuidetoviewtheswitchsystemandhardwarecommands.
23
AOS-CX10.10MonitoringGuide|(8400SwitchSeries)

Chapter 6
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
| External | storage | commands |     |     |
| -------- | ------- | -------- | --- | --- |
address
| address    | {<IPV4-ADDR> | | <IPV6-ADDR> | | hostname | <HOSTNAME>} |
| ---------- | ------------ | ------------- | ---------- | ----------- |
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
24
AOS-CX10.10MonitoringGuide|(8400SwitchSeries)

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
| Command History                           |                  |     |              |       |
Externalstorage|25

| Release             |         |         | Modification |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8400 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
usergroupmemberswithexecution
rightsforthiscommand.Operatorscan
executethiscommandfromthe
operatorcontext(>)only.
disable
disable
no disable
Description
Disablestheexternalstoragevolume.
Thenoformofthiscommandenablestheexternalstoragevolume.Thisisidenticaltotheenable
command.
Examples
Disablingavolumenamedlogfiles:
| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)# disable
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8400 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
usergroupmemberswithexecution
rightsforthiscommand.Operatorscan
executethiscommandfromthe
operatorcontext(>)only.
enable
enable
no enable
Description
Enablestheexternalstoragevolume.
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 26

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
8400 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
usergroupmemberswithexecution
rightsforthiscommand.Operatorscan
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
| switch(config)# | no  | external-storage | logfiles |     |
| --------------- | --- | ---------------- | -------- | --- |
| Command History |     |                  |          |     |
Externalstorage|27

| Release        |             |     |         | Modification |
| -------------- | ----------- | --- | ------- | ------------ |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
| Re-Enter                              | the     | NAS server       | password: | ********** |
Clearingthepasswordforvolumelogfiles:
| switch(config)# |     | external-storage |     | logfiles |
| --------------- | --- | ---------------- | --- | -------- |
switch(config-external-storage-logfiles)# no password plaintext Xj#9
| Command | History |     |     |     |
| ------- | ------- | --- | --- | --- |
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 28

| Release        |             |         | Modification |           |     |     |
| -------------- | ----------- | ------- | ------------ | --------- | --- | --- |
| 10.07orearlier |             |         | --           |           |     |     |
| Command        | Information |         |              |           |     |     |
| Platforms      | Command     | context |              | Authority |     |     |
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
switch#
show external-storage
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
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
(#)
| show running-config |     | external-storage |     |     |     |     |
| ------------------- | --- | ---------------- | --- | --- | --- | --- |
Externalstorage|29

| show running-config |     |     | external-storage |     |     |
| ------------------- | --- | --- | ---------------- | --- | --- |
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
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
|     |     | (#) |     |     | rightsforthiscommand. |
| --- | --- | --- | --- | --- | --------------------- |
type
| type {nfsv3 |        | | nfsv4 | | scp} |     |     |
| ----------- | ------ | ------- | ------ | --- | --- |
| no type     | {nfsv3 | | nfsv4 | | scp} |     |     |
Description
Setsthenetworkattachedstorageaccesstypeforreachingtheexternalstoragevolume.
Thenoformofthiscommanddeletesanexternalstoragevolume.
| Parameter |     |     |     |     | Description                             |
| --------- | --- | --- | --- | --- | --------------------------------------- |
| nfsv3     |     |     |     |     | SpecifiestheNFSv3networkaccessprotocol. |
nfsv4
SpecifiestheNFSv4networkaccessprotocol.
| scp |     |     |     |     | SpecifiestheSCPnetworkaccessprotocol. |
| --- | --- | --- | --- | --- | ------------------------------------- |
Examples
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 30

CreatingthelogfilesvolumeusingNFSV4:
| switch(config)#                           | external-storage |     | logfiles   |     |
| ----------------------------------------- | ---------------- | --- | ---------- | --- |
| switch(config-external-storage-logfiles)# |                  |     | type nfsv4 |     |
Clearingtheexternalstorageaccesstype:
| switch(config)#                           | external-storage |         | logfiles     |           |
| ----------------------------------------- | ---------------- | ------- | ------------ | --------- |
| switch(config-external-storage-logfiles)# |                  |         | no type      | nfsv4     |
| Command History                           |                  |         |              |           |
| Release                                   |                  |         | Modification |           |
| 10.07orearlier                            |                  |         | --           |           |
| Command Information                       |                  |         |              |           |
| Platforms                                 | Command          | context |              | Authority |
8400 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
memberswithexecutionrightsforthis
command.
username
username <USER-NAME>
| no username | <USER-NAME> |     |     |     |
| ----------- | ----------- | --- | --- | --- |
Description
Setstheusernameforloggingintoanetworkattachedstorageserver.
Thenoformofthiscommandclearsausername.
| Parameter   |     |     | Description           |     |
| ----------- | --- | --- | --------------------- | --- |
| <USER-NAME> |     |     | Specifiestheusername. |     |
Examples
Creatingavolumenamedlogfileswiththeusernamenassuser:
| switch(config)#                           | external-storage |     | logfiles |         |
| ----------------------------------------- | ---------------- | --- | -------- | ------- |
| switch(config-external-storage-logfiles)# |                  |     | username | nasuser |
Clearingtheusernamenasuserfromaccessingthelogfilesvolume:
| switch(config)#                           | external-storage |     | logfiles    |         |
| ----------------------------------------- | ---------------- | --- | ----------- | ------- |
| switch(config-external-storage-logfiles)# |                  |     | no username | nasuser |
| Command History                           |                  |     |             |         |
Externalstorage|31

| Release             |         |         | Modification |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8400 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
memberswithexecutionrightsforthis
command.
vrf
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
| switch(config)#                           | external-storage |         | logfiles     |           |
| ----------------------------------------- | ---------------- | ------- | ------------ | --------- |
| switch(config-external-storage-logfiles)# |                  |         | no vrf nas   |           |
| Command History                           |                  |         |              |           |
| Release                                   |                  |         | Modification |           |
| 10.07orearlier                            |                  |         | --           |           |
| Command Information                       |                  |         |              |           |
| Platforms                                 | Command          | context |              | Authority |
8400 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
memberswithexecutionrightsforthis
command.
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 32

Chapter 7

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

33

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

IP-SLA | 34

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
604800.
version <VERSION-NUMBER> SpecifiesthesourceinterfacetouseforsendingIP-SLA
probes.
| http-raw-request | <RAW-PAYLOAD> |     | HTTPrawrequest.String. |
| ---------------- | ------------- | --- | ---------------------- |
Examples
switch(config-ipsla-1)# http get http://device.arubanetworks.com/root/home.html
| switch(config-ipsla-1)# |     | http raw |     |
| ----------------------- | --- | -------- | --- |
http://device.arubanetworks.com/root/home.html
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
| Command History     |         |              |           |
| ------------------- | ------- | ------------ | --------- |
| Release             |         | Modification |           |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
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
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
name-server <IPV4-ADDR-DNS-SERVER> SpecifiestheDNSserverfordestinationhostname
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 35

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
resolution.
payload-size <PAYLOAD-SIZE> SpecifiesthepayloadsizeofanSLAprobe.Range:0to
1440.
tos <TYPE-OF-SERVICE> Specifiesthetypeofservetobeusedintheprobe
packets.Range:0to255.
| probe-interval | <PROBE-INTERVAL> |     |     |     |     |
| -------------- | ---------------- | --- | --- | --- | --- |
Specifiestheprobeintervalinseconds.Range:5to
604800.
Examples
| switch(config)#             | ip-sla | test |           |                |         |
| --------------------------- | ------ | ---- | --------- | -------------- | ------- |
| switch(config-ip-sla-test)# |        |      | icmp-echo | 2.2.2.2        |         |
| switch(config-ip-sla-test)# |        |      | icmp-echo | 2.2.2.2 source | 3.3.3.3 |
switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
| name-server | 4.4.4.4 |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- |
switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
| name-server         | 4.4.4.4 | probe-interval | 80           |           |     |
| ------------------- | ------- | -------------- | ------------ | --------- | --- |
| Command History     |         |                |              |           |     |
| Release             |         |                | Modification |           |     |
| 10.07orearlier      |         |                | --           |           |     |
| Command Information |         |                |              |           |     |
| Platforms           | Command | context        |              | Authority |     |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
ip-sla
ip-sla <IP-SLA-NAME>
| no ip-sla <IP-SLA-NAME> |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- |
Description
CreatesanIPServiceLevelAgreement(SLA)profileandswitchestotheconfig-ip-slacontext.
ThenoformofthiscommanddeletesanIP-SLAprofile.Bydefault,allprofileusethedefaultVRF
(default).
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<IP-SLA-NAME>
SpecifiesanIP-SLAprofilename.Length:1to63characters.
Examples
CreatinganIP-SLA:
IP-SLA|36

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
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
Examples
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 37

switch(config)# ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
switch(config)#
|     |     |     | ip-sla | responder | SLA1 | udp-echo | 8000 source | 1/1/1 |
| --- | --- | --- | ------ | --------- | ---- | -------- | ----------- | ----- |
switch(config)# no ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
| Command        | History     |         |     |         |              |     |     |     |
| -------------- | ----------- | ------- | --- | ------- | ------------ | --- | --- | --- |
| Release        |             |         |     |         | Modification |     |     |     |
| 10.07orearlier |             |         |     |         | --           |     |     |     |
| Command        | Information |         |     |         |              |     |     |     |
| Platforms      |             | Command |     | context | Authority    |     |     |     |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show | ip-sla | responder |            |     |     |     |     |     |
| ---- | ------ | --------- | ---------- | --- | --- | --- | --- | --- |
| show | ip-sla | responder | <SLA-NAME> |     |     |     |     |     |
Description
ShowsthegivenIP-SLAresponderconfigurationandoperationstatus.
| Parameter  |     |     |     |     | Description          |     |     |     |
| ---------- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
| <SLA-NAME> |     |     |     |     | SpecifiestheSLAname. |     |     |     |
Examples
| switch(config)# |             |           | show | ip-sla responder |              | SLA3 |     |     |
| --------------- | ----------- | --------- | ---- | ---------------- | ------------ | ---- | --- | --- |
|                 | SLA Name    |           |      | : SLA3           |              |      |     |     |
|                 | IP-SLA      | Type      |      | : Udp-echo       |              |      |     |     |
|                 | VRF         |           |      | : Default        |              |      |     |     |
|                 | Responder   | Port      |      | : 8000           |              |      |     |     |
|                 | Responder   | IP        |      | : 2.2.2.3        |              |      |     |     |
|                 | Responder   | Interface |      | : 1/1/1          |              |      |     |     |
|                 | Responder   | Status    |      | : Running        |              |      |     |     |
| Command         | History     |           |      |                  |              |      |     |     |
| Release         |             |           |      |                  | Modification |      |     |     |
| 10.07orearlier  |             |           |      |                  | --           |      |     |     |
| Command         | Information |           |      |                  |              |      |     |     |
IP-SLA|38

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show | ip-sla | responder |     | results |     |     |
| ---- | ------ | --------- | --- | ------- | --- | --- |
show ip-sla responder <SLA-NAME> <SOURCE-IPV4-ADDR> <PORT-NUM> results
Description
Showsthegivenip-slaresponderstatisticsforagivensourceIPandport.Thiscommandisonly
applicableforthesourceswheresourceIPandportareconfigured.
| Parameter          |     |     |     |     | Description                            |     |
| ------------------ | --- | --- | --- | --- | -------------------------------------- | --- |
| <SLA-NAME>         |     |     |     |     | SpecifiestheSLAname.                   |     |
| <SOURCE-IPV4-ADDR> |     |     |     |     | SpecifiesthesourceIPV4address.         |     |
| <PORT-NUM>         |     |     |     |     | Specifiestheportnumber.Range:1to65535. |     |
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
config
| 8400 |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
| show | ip-sla | <SLA-NAME> |         |     |     |     |
| ---- | ------ | ---------- | ------- | --- | --- | --- |
| show | ip-sla | <SLA-NAME> | results |     |     |     |
Description
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 39

ShowsthegivenIP-SLAsourceconfigurationandstatus.
| Parameter  |     |     |     | Description                               |     |     |
| ---------- | --- | --- | --- | ----------------------------------------- | --- | --- |
| <SLA-NAME> |     |     |     | SpecifiestheSLAname.                      |     |     |
| results    |     |     |     | ShowsthestatisticscalculatedforanSLAtype. |     |     |
Examples
switch#
|                 | show                    | ip-sla            | xyz results  |               |                   |             |
| --------------- | ----------------------- | ----------------- | ------------ | ------------- | ----------------- | ----------- |
|                 | IP-SLA session          |                   | status       |               |                   |             |
|                 | IP-SLA                  | Name              |              |               | : xyz             |             |
|                 | IP-SLA                  | Type              |              |               | : tcp-connect     |             |
|                 | Destination             |                   | Host Name/IP | Address:      | 2.2.2.1           |             |
|                 | Destination             |                   | Port         |               | : 8888            |             |
|                 | Source                  | IP Address/IFName |              |               | : 2.2.2.2         |             |
|                 | Source                  | Port              |              |               | : 5555            |             |
|                 | Status                  |                   |              |               | : Running         |             |
|                 | IP-SLA session          |                   | cumulative   | counters      |                   |             |
|                 | Total                   | Probes            | Transmitted  |               | : 1               |             |
|                 | Probes                  | Timed-out         |              |               | : 0               |             |
|                 | Bind Error              |                   |              |               | : 0               |             |
|                 | Destination             |                   | Address      | Unreachable   | : 0               |             |
|                 | DNS Resolution          |                   | Failures     |               | : 0               |             |
|                 | Reception               | Error             |              |               | : 0               |             |
|                 | Transmission            |                   | Error        |               | : 0               |             |
|                 | IP-SLA Latest           | Probe             | Results      |               |                   |             |
|                 | Last Probe              | Time              |              |               | : 2018 Jul        | 13 02:00:35 |
|                 | Packets                 | Sent              |              |               | : 1               |             |
|                 | Packets                 | Received          |              |               | : 1               |             |
|                 | Packet                  | Loss              | in Test      |               | : 0.0000%         |             |
|                 | Minimum RTT(ms)         |                   |              |               | : 0.7900          |             |
|                 | Maximum RTT(ms)         |                   |              |               | : 0.7900          |             |
|                 | Average RTT(ms)         |                   |              |               | : 0.7900          |             |
|                 | DNS RTT(ms)             |                   |              |               | : 0.0000          |             |
|                 | TCP RTT(ms)             |                   |              |               | : 0.9710          |             |
| switch(config)# |                         | show              | ip-sla       | xyz           |                   |             |
|                 | IP-SLA Name             |                   |              | : xyz         |                   |             |
|                 | Status                  |                   |              | : scheduled   |                   |             |
|                 | IP-SLA Type             |                   |              | : tcp-connect |                   |             |
|                 | VRF                     |                   |              | : ipslasrc    |                   |             |
|                 | Source Port             |                   |              | : 5555        |                   |             |
|                 | Source IP               |                   |              | : 2.2.2.2     |                   |             |
|                 | Source Interface        |                   |              | :             |                   |             |
|                 | Domain Name             | Server            |              | :             |                   |             |
|                 | Probe interval(seconds) |                   |              | : 90          |                   |             |
| switch(config)# |                         | show              | ip-sla       | jitter-sla    | results           |             |
|                 | IP-SLA session          |                   | status       |               |                   |             |
|                 | IP-SLA                  | Name              |              |               | : jitter-sla      |             |
|                 | IP-SLA                  | Type              |              |               | : udp-jitter-voip |             |
|                 | Destination             |                   | Host Name/IP | Address:      | 2.2.2.1           |             |
|                 | Destination             |                   | Port         |               | : 8888            |             |
|                 | Source                  | IP Address/IFName |              |               | :                 |             |
IP-SLA|40

|                 | Source                  | Port       |               |                   | : 5555     |              |            |     |
| --------------- | ----------------------- | ---------- | ------------- | ----------------- | ---------- | ------------ | ---------- | --- |
|                 | Status                  |            |               |                   | : Running  |              |            |     |
|                 | IP-SLA                  | Session    | Cumulative    | Counters          |            |              |            |     |
|                 | Total                   | Probes     | Transmitted   |                   | : 1        |              |            |     |
|                 | Probes                  | Timed-out  |               |                   | : 0        |              |            |     |
|                 | Bind                    | Error      |               |                   | : 0        |              |            |     |
|                 | Destination             |            | Address       | Unreachable       | : 0        |              |            |     |
|                 | DNS                     | Resolution | Failures      |                   | : 0        |              |            |     |
|                 | Reception               |            | Error         |                   | : 0        |              |            |     |
|                 | Transmission            |            | Error         |                   | : 0        |              |            |     |
|                 | IP-SLA                  | Latest     | Probe Results |                   |            |              |            |     |
|                 | Last                    | Probe      | Time          |                   | : 2018 Jul | 13           | 02:02:48   |     |
|                 | Packets                 | Sent       |               |                   | : 1        |              |            |     |
|                 | Packets                 | Received   |               |                   | : 1        |              |            |     |
|                 | Packet                  | Loss       | in Test       |                   | : 0.0000%  |              |            |     |
|                 | Minimum                 | RTT(ms)    |               |                   | : 0.7900   |              |            |     |
|                 | Maximum                 | RTT(ms)    |               |                   | : 0.7900   |              |            |     |
|                 | Average                 | RTT(ms)    |               |                   | : 0.7900   |              |            |     |
|                 | DNS                     | RTT(ms)    |               |                   | : 0.0000   |              |            |     |
|                 | Min                     | Positive   | SD            |                   | : 1        | Min Positive | DS         | : 2 |
|                 | Max                     | Positive   | SD            |                   | : 1        | Max Positive | DS         | : 2 |
|                 | Positive                |            | SD Number     |                   | : 2        | Positive     | DS Number  | : 2 |
|                 | Positive                |            | SD Sum        |                   | : 2        | Positive     | DS Sum     | : 4 |
|                 | Positive                |            | SD Average    |                   | : 5        | Positive     | DS Average | : 5 |
|                 | Min                     | Negative   | SD            |                   | : 1        | Min Negative | DS         | : 1 |
|                 | Max                     | Negative   | SD            |                   | : 1        | Max Negative | DS         | : 1 |
|                 | Negative                |            | SD Number     |                   | : 2        | Negative     | DS Number  | : 4 |
|                 | Negative                |            | SD Sum        |                   | : 2        | Negative     | DS Sum     | : 4 |
|                 | Negative                |            | SD Average    |                   | : 5        | Negative     | DS Average | : 5 |
|                 | Max                     | SD Delay   |               |                   | : 0        | Max DS       | Delay      | : 0 |
|                 | Min                     | SD Delay   |               |                   | : 0        | Min DS       | Delay      | : 0 |
|                 | Average                 | SD         | Delay         |                   | : 0        | Average      | DS Delay   | : 0 |
|                 | Voice Scores:           |            |               |                   |            |              |            |     |
|                 | MOS                     | Score      |               |                   | : 4.38     | ICPIF        |            | : 0 |
| switch(config)# |                         |            | show ip-sla   | m3op              |            |              |            |     |
|                 | IP-SLA                  | Name       |               | : jitter-sla      |            |              |            |     |
|                 | Status                  |            |               | : Running         |            |              |            |     |
|                 | IP-SLA                  | Type       |               | : udp-jitter-voip |            |              |            |     |
|                 | VRF                     |            |               | : ipslasrc        |            |              |            |     |
|                 | Source                  | IP         |               | : 2.2.2.2         |            |              |            |     |
|                 | Source                  | Interface  |               | :                 |            |              |            |     |
|                 | Domain                  | Name       | Server        | :                 |            |              |            |     |
|                 | TOS                     |            |               | : 10              |            |              |            |     |
|                 | Probe Interval(seconds) |            |               | : 90              |            |              |            |     |
|                 | Advantage               | Factor     |               | : 0               |            |              |            |     |
|                 | Codec Type              |            |               | : g711a           |            |              |            |     |
| switch(config)# |                         |            | show ip-sla   | http-sla          |            |              |            |     |
|                 | IP-SLA                  | Name       |               | : http-sla        |            |              |            |     |
|                 | Status                  |            |               | : Running         |            |              |            |     |
|                 | IP-SLA                  | Type       |               | : http            |            |              |            |     |
|                 | VRF                     |            |               | : ipslasrc        |            |              |            |     |
|                 | Source                  | IP         |               | : 2.2.2.2         |            |              |            |     |
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 41

|     | Source     | Interface         |        |     | :                  |     |     |     |     |     |     |     |
| --- | ---------- | ----------------- | ------ | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
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
| resolution     |               | failure.    |                  |         |     | |            |               |     |        |            |     |     |
| -------------- | ------------- | ----------- | ---------------- | ------- | --- | ------------ | ------------- | --- | ------ | ---------- | --- | --- |
|                | |Reception    |             | Error            |         |     | |            | Total numbers | of  | probes | failed due | to  |     |
| internal       |               | error       | in reception.    |         |     | |            |               |     |        |            |     |     |
|                | |Transmission |             | Error            |         |     | |            | Total numbers | of  | probes | failed due | to  |     |
| internal       |               | errr        | in transmission. |         |     | |            |               |     |        |            |     |     |
| Command        |               | History     |                  |         |     |              |               |     |        |            |     |     |
| Release        |               |             |                  |         |     | Modification |               |     |        |            |     |     |
| 10.07orearlier |               |             |                  |         |     | --           |               |     |        |            |     |     |
| Command        |               | Information |                  |         |     |              |               |     |        |            |     |     |
| Platforms      |               | Command     |                  | context |     | Authority    |               |     |        |            |     |     |
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
(#)
start-test
start-test
IP-SLA|42

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
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
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
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
tcp-connect
tcp-connect {<DEST-IPV4-ADDR> | <HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>]
| [probe-interval | <PROBE-INTERVAL>] |     |     |
| --------------- | ----------------- | --- | --- |
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 43

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
| [source-port | <PORT-NUM>] |     |     | SpecifiestheportfortheIP-SLAtest. |
| ------------ | ----------- | --- | --- | --------------------------------- |
[name-server <IPV4-ADDR-DNS-SERVER>] SpecifiestheDNSserverfordestinationhostname
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
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
udp-echo
udp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>] [payload-
size
<PAYLOAD-SIZE>] [tos <TYPE-OF-SERVICE>] [probe-interval <PROBE-INTERVAL>]
IP-SLA|44

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
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
[source-port <PORT-NUM>] SpecifiessourceportfortheIP-SLAtest.Range:1to
65535.
[name-server <IPV4-ADDR-DNS-SERVER>]
SpecifiestheDNSserverfordestinationhostname
resolution.
[payload-size <PAYLOAD-SIZE>] SpecifiesthepayloadsizeofanSLAprobe.Range:28
to1440.
| [<TYPE-OF-SERVICE>] |     | Typeofservice.Range:0to255. |     |
| ------------------- | --- | --------------------------- | --- |
probe-interval <PROBE-INTERVAL> Probeintervalinseconds.Range:5to604800.
Examples
| switch(config-ipsla-1)# | udp-echo 2.2.2.2 | 8080 |     |
| ----------------------- | ---------------- | ---- | --- |
switch(config-ipsla-1)#
|     | udp-echo 2.2.2.2 | 8080 source | 2.2.2.1 |
| --- | ---------------- | ----------- | ------- |
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
Command Information
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 45

Platforms

Command context

Authority

8400

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

codec-type g711a source 1/1/1

switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080

advantage-factor 10 codec-type g711a source 2.2.2.1

switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080

IP-SLA | 46

| advantage-factor | 10  | codec-type g711a source | 1/1/1 |     |
| ---------------- | --- | ----------------------- | ----- | --- |
switch(config-ipsla-1)#
|     |     | udp-jitter-voip | https://device.arubanetworks.com | 8080 |
| --- | --- | --------------- | -------------------------------- | ---- |
advantage-factor 10 codec-type g711a name-server 10.10.10.2 probe-interval 120
| source 10.1.1.1 | source-port | 8888 tos 10 |     |     |
| --------------- | ----------- | ----------- | --- | --- |
| Command History |             |             |     |     |
Release Modification
10.07orearlier --
| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
vrf
vrf <VRF-NAME>
no vrf [<VRF-NAME>]
Description
ConfigurestheVRFonwhichtheSLAwillsendorreceivepackets.Bydefault,thedefaultVRFisused.
ThenoformofthecommandremovesVRFfromSLA.
Parameter Description
<VRF-NAME> SpecifiesaVRFname.Length:Default:default.
Examples
| switch(config-ip-sla-test)# |     | vrf ipslasrc |     |     |
| --------------------------- | --- | ------------ | --- | --- |
| switch(config-ip-sla-test)# |     | no vrf       |     |     |
| Command History             |     |              |     |     |
Release Modification
10.07orearlier --
| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
config-ip-sla-<IP-SLA-NAME>
| 8400 |     |     | Administratorsorlocalusergroupmemberswith |     |
| ---- | --- | --- | ----------------------------------------- | --- |
executionrightsforthiscommand.
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 47

| show interface |     |     |     |     |
| -------------- | --- | --- | --- | --- |
show interface [<IFNNAME>|<IFRANGE>] [brief | physical | extended [non-zero] [human-
| readable] | | [human-readable]] |     |     |     |
| ----------- | ----------------- | --- | --- | --- |
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief | physical]
| show interface | lag [<LAG-ID>] | [extended | [non-zero]] |     |
| -------------- | -------------- | --------- | ----------- | --- |
Description
Showsactiveconfigurationsandoperationalstatusinformationforinterfaces.
| Parameter |     |     | Description                                    |     |
| --------- | --- | --- | ---------------------------------------------- | --- |
| <IFNAME>  |     |     | Specifiesainterfacename.                       |     |
| <IFRANGE> |     |     | Specifiestheportidentifierrange.               |     |
| brief     |     |     | Showsbriefinfointabularformat.                 |     |
| physical  |     |     | Showsthephysicalconnectioninfointabularformat. |     |
| extended  |     |     | Showsadditionalstatistics.                     |     |
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
| non-zero      |     |     | Showsonlynonzerostatistics.                    |     |
| ------------- | --- | --- | ---------------------------------------------- | --- |
| LAG           |     |     | ShowsLAGinterfaceinformation.                  |     |
| LOOPBACK      |     |     | Showsloopbackinterfaceinformation.             |     |
| TUNNEL        |     |     | Showstunnelinterfaceinformation.               |     |
| VLAN          |     |     | ShowsVLANinterfaceinformation.                 |     |
| <LAG-ID>      |     |     | SpecifiestheLAGnumber.Range:1-256              |     |
| <LOOPBACK-ID> |     |     | SpecifiestheLOOPBACKnumber.Range:0-255         |     |
| <TUNNEL-ID>   |     |     | SpecifiesthetunnelID.Range:1-255               |     |
| <VLAN-ID>     |     |     | SpecifiestheVLANID.Range:1-4094                |     |
| VXLAN         |     |     | ShowstheVXLANinterfaceinformation.             |     |
| <VXLAN-ID>    |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |
Examples
Showinginterfaceinformationwhenitisconfiguredasaroute-onlyport:
| switch#           | show interface | 1/1/1         |                     |           |
| ----------------- | -------------- | ------------- | ------------------- | --------- |
| Interface         | 1/1/1 is up    |               |                     |           |
| Admin state       | is up          |               |                     |           |
| Link state:       | up for         | 2 days (since | Sun Jun 21 05:30:22 | UTC 2020) |
| Link transitions: | 1              |               |                     |           |
IP-SLA|48

| Description: |           | backup data | center   | link              |     |     |     |     |
| ------------ | --------- | ----------- | -------- | ----------------- | --- | --- | --- | --- |
| Hardware:    | Ethernet, | MAC         | Address: | 70:72:cf:fd:e7:b4 |     |     |     |     |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | none |             |     |         |     |     |       |         |
| ---------------- | ---- | ----------- | --- | ------- | --- | --- | ----- | ------- |
| Speed 1000       | Mb/s |             |     |         |     |     |       |         |
| Auto-negotiation |      | is on       |     |         |     |     |       |         |
| Flow-control:    |      | off         |     |         |     |     |       |         |
| Error-control:   |      | off         |     |         |     |     |       |         |
| L3 Counters:     |      | Rx Enabled, | Tx  | Enabled |     |     |       |         |
| Rate collection  |      | interval:   | 300 | seconds |     |     |       |         |
| Rates            |      |             |     | RX      |     | TX  | Total | (RX+TX) |
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
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 49

Link state: down for 3 days (since Tue Mar 16 05:20:47 UTC 2021)
| Link transitions: |     | 0   |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- |
Description:
| Hardware: | Ethernet, | MAC | Address: | 04:09:73:62:90:e7 |     |     |     |
| --------- | --------- | --- | -------- | ----------------- | --- | --- | --- |
MTU 1500
Type SFP+DAC3
Full-duplex
| qos trust        | none            |           |     |         |     |       |         |
| ---------------- | --------------- | --------- | --- | ------- | --- | ----- | ------- |
| Speed 0          | Mb/s            |           |     |         |     |       |         |
| Auto-negotiation |                 | is off    |     |         |     |       |         |
| Flow-control:    | off             |           |     |         |     |       |         |
| Error-control:   |                 | off       |     |         |     |       |         |
| VLAN Mode:       | native-untagged |           |     |         |     |       |         |
| Native           | VLAN: 1         |           |     |         |     |       |         |
| Allowed          | VLAN List:      | 1502-1505 |     |         |     |       |         |
| Rate collection  |                 | interval: | 300 | seconds |     |       |         |
| Rate             |                 |           |     | RX      | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     | 0.00 | 0.00 |     | 0.00  |
| ----------- | --- | --- | --- | ---- | ---- | --- | ----- |
| KPkts /     | sec |     |     | 0.00 | 0.00 |     | 0.00  |
| Unicast     |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Multicast   |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Broadcast   |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Utilization |     |     |     | 0.00 | 0.00 |     | 0.00  |
| Statistic   |     |     |     | RX   | TX   |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     |     | 0   | 0   |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- |
| Unicast      |     |     |     | 0   | 0   |     | 0   |
| Multicast    |     |     |     | 0   | 0   |     | 0   |
| Broadcast    |     |     |     | 0   | 0   |     | 0   |
| Bytes        |     |     |     | 0   | 0   |     | 0   |
| Jumbos       |     |     |     | 0   | 0   |     | 0   |
| Dropped      |     |     |     | 0   | 0   |     | 0   |
| Pause Frames |     |     |     | 0   | 0   |     | 0   |
| Errors       |     |     |     | 0   | 0   |     | 0   |
| CRC/FCS      |     |     |     | 0   | n/a |     | 0   |
| Collision    |     |     |     | n/a | 0   |     | 0   |
| Runts        |     |     |     | 0   | n/a |     | 0   |
| Giants       |     |     |     | 0   | n/a |     | 0   |
Showingtheoutputinhuman-readableformat:
Inthehuman-readableformat,the< 1symbolforUtilizationindicatesthattheamountofpacketsis
betweenzeroandone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsand
theUtilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
| switch(config-if)# |       | show  | interface | 1/1/1 human-readable |     |     |     |
| ------------------ | ----- | ----- | --------- | -------------------- | --- | --- | --- |
| Interface          | 1/1/1 | is up |           |                      |     |     |     |
...
| Rate |     |     |     | RX  | TX  | Total | (RX+TX) |
| ---- | --- | --- | --- | --- | --- | ----- | ------- |
---------------- -------------------- -------------------- --------------------
| Bits / | sec |     |     | 3M  | 3M  |     | 6M  |
| ------ | --- | --- | --- | --- | --- | --- | --- |
IP-SLA|50

|     | Pkts / sec  |     |     | 316 | 316 | 633   |
| --- | ----------- | --- | --- | --- | --- | ----- |
|     | Unicast     |     |     | 319 | 319 | 638   |
|     | Multicast   |     |     | 0   | 0   | 0     |
|     | Broadcast   |     |     | 0   | 0   | 0     |
|     | Utilization | %   |     | < 1 | < 1 | < 1   |
|     | Statistic   |     |     | RX  | TX  | Total |
---------------- -------------------- -------------------- --------------------
|     | Packets      |     |     | 577K | 577K | 1M  |
| --- | ------------ | --- | --- | ---- | ---- | --- |
|     | Unicast      |     |     | 577K | 577K | 1M  |
|     | Multicast    |     |     | 0    | 51   | 51  |
|     | Broadcast    |     |     | 0    | 15   | 15  |
|     | Bytes        |     |     | 744M | 745M | 1G  |
|     | Jumbos       |     |     | 0    | 0    | 0   |
|     | Dropped      |     |     | 0    | 0    | 0   |
|     | Filtered     |     |     | 0    | 0    | 0   |
|     | Pause Frames |     |     | 0    | 0    | 0   |
|     | Errors       |     |     | 0    | 0    | 0   |
|     | CRC/FCS      |     |     | 0    | n/a  | 0   |
|     | Collision    |     |     | n/a  | 0    | 0   |
|     | Runts        |     |     | 0    | n/a  | 0   |
|     | Giants       |     |     | 0    | n/a  | 0   |
...
| Command | History |     |     |              |     |     |
| ------- | ------- | --- | --- | ------------ | --- | --- |
| Release |         |     |     | Modification |     |     |
10.10
Addedhuman-readableparameter.
| 10.07orearlier |             |         |         | --        |     |     |
| -------------- | ----------- | ------- | ------- | --------- | --- | --- |
| Command        | Information |         |         |           |     |     |
| Platforms      |             | Command | context | Authority |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 51

Chapter 8

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

52

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

Mirroring | 53

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

54

Clearingmirrorstatisticsformirrorsession1:
| switch# clear       | mirror  | 1       |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
comment
comment <COMMENT>
no comment
Description
Specifiesacommentforthemirroringsession.
Thenoformofthiscommandremovesthecomment.
| Parameter |     |     | Description                                        |
| --------- | --- | --- | -------------------------------------------------- |
| <COMMENT> |     |     | Acommentstringofupto64characterscomposedofletters, |
numbers,underscores,dashes,spaces,andperiods.
Usage
Commentsareoptionalandcanbeaddedorremovedatanytimewithoutaffectingthestateofthe
mirroringsession.
Addingacommenttoasessionthatalreadyhasacommentreplacestheexistingcomment.
Examples
Addingacommenttoamirrorsession:
switch(config-mirror-3)# comment This Mirror will be removed during next
| maintenance | window |     |     |
| ----------- | ------ | --- | --- |
Removingthecommentfrommirrorsession3:
| switch(config-mirror-3)# |     | no comment |     |
| ------------------------ | --- | ---------- | --- |
| Command History          |     |            |     |
Mirroring|55

| Release        |             |         | Modification |           |     |     |     |
| -------------- | ----------- | ------- | ------------ | --------- | --- | --- | --- |
| 10.07orearlier |             |         | --           |           |     |     |     |
| Command        | Information |         |              |           |     |     |     |
| Platforms      | Command     | context |              | Authority |     |     |     |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
copy tcpdump-pcap
| copy tcpdump-pcap | <FILE-NAME> | <REMOTE-URL> |     |     |     |     |     |
| ----------------- | ----------- | ------------ | --- | --- | --- | --- | --- |
Description
Savespacketcapturefilestoexternalstorage.
| Parameter   |     |     | Description                          |     |     |     |     |
| ----------- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
| <FILE-NAME> |     |     | Specifiesthepacketcapturefiletosave. |     |     |     |     |
<REMOTE-URL>
Specifiestheexternalstoragetowhichthepacketcapturefilewill
besaved.
Usage
Onlyfourfilescanbesavedatanypointontheswitch.Packetcapturefilesarenotsavedafterafailover
| orreboot.Viewalistofsavedfilesusingdiag |     |     | utilities | list-files. |     |     |     |
| --------------------------------------- | --- | --- | --------- | ----------- | --- | --- | --- |
Examples
Savingmy_capture_file.pcaptosftp://root@10.0.0.2/file.pcap:
switch# copy tcpdump-pcap my_capture_file.pcap sftp://root@10.0.0.2/file.pcap
| root@10.0.0.2's      | passowrd:            |         |                    |     |          |           |       |
| -------------------- | -------------------- | ------- | ------------------ | --- | -------- | --------- | ----- |
| Connected            | to 10.0.0.2.         |         |                    |     |          |           |       |
| sftp > put           | my_capture_file.pcap |         | file.pcap          |     |          |           |       |
| Uploading            | my_capture_file.pcap |         | to /root/file.pcap |     |          |           |       |
| my_capture_file.pcap |                      |         |                    |     | 100% 156 | 219.8KB/s | 00:00 |
| Copied               | successfuly.         |         |                    |     |          |           |       |
| Command              | History              |         |                    |     |          |           |       |
| Release              |                      |         | Modification       |     |          |           |       |
| 10.08                |                      |         | Commandintroduced  |     |          |           |       |
| Command              | Information          |         |                    |     |          |           |       |
| Platforms            | Command              | context | Authority          |     |          |           |       |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 56

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
theSupportabilityGuide.
Mirroring|57

ThenoformofthiscommandwillimmediatelystopsmirroringtraffictotheCPU,butwillnotremove
anysourcesfromthemirrorconfiguration.
Examples
ConfiguringamirrorsessionwithCPUasthedestination.
| switch#                  | config |        |             |     |     |     |
| ------------------------ | ------ | ------ | ----------- | --- | --- | --- |
| switch(config)#          |        | mirror | session     | 1   |     |     |
| switch(config-mirror-1)# |        |        | destination |     | cpu |     |
Removingthedestinationentirely.
| switch(config-mirror-1)# |             |     | no      | destination |              | cpu       |
| ------------------------ | ----------- | --- | ------- | ----------- | ------------ | --------- |
| Command                  | History     |     |         |             |              |           |
| Release                  |             |     |         |             | Modification |           |
| 10.07orearlier           |             |     |         |             | --           |           |
| Command                  | Information |     |         |             |              |           |
| Platforms                | Command     |     | context |             |              | Authority |
8400 config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| destination    | interface |     |                             |     |     |     |
| -------------- | --------- | --- | --------------------------- | --- | --- | --- |
| destination    | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |     |     |
| no destination | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |     |     |
Description
Configuresthespecifiedinterfaceasthedestinationofthemirroredtraffic.
Thenoformofthiscommandimmediatelydisablesthemirroringsessionandremovesthespecified
destinationinterfacefromtheconfiguration.
| Parameter      |     |     |     |     | Description                                  |     |
| -------------- | --- | --- | --- | --- | -------------------------------------------- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesainterface.Format:member/slot/port. |     |
<LAG-NAME>
SpecifiesaLAG(linkaggregationgroup)identifier.
Usage
Supportedmirrordestinations:Layer2orLayer3Ethernetports,LAGs,tunnel,orCPUasaMirror
Destination.AportthatisalreadyamemberofaLAGisnotavalidmirrordestination.
Configuringadifferentdestinationinterfaceinanenabledmirroringsessioncausesallmirroredtraffic
tousethenewdestinationinterface.Thisactionmightcauseatemporarysuspensionofmirrored
sourcetrafficduringthereconfiguration.
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 58

Examples
Configuringamirroringsessionandaddinganinterfaceasadestination:
switch(config)#
|                          |     | mirror | session     | 1   |           |       |
| ------------------------ | --- | ------ | ----------- | --- | --------- | ----- |
| switch(config-mirror-1)# |     |        | destination |     | interface | 1/1/1 |
Replacingtheexistingdestinationwithdifferentinterface:
| switch(config-mirror-1)# |     |     | destination |     | interface | 1/1/12 |
| ------------------------ | --- | --- | ----------- | --- | --------- | ------ |
Removingadestination:
| switch(config-mirror-1)# |         |     | no destination |              | interface | 1/1/12 |
| ------------------------ | ------- | --- | -------------- | ------------ | --------- | ------ |
| Command History          |         |     |                |              |           |        |
| Release                  |         |     |                | Modification |           |        |
| 10.07orearlier           |         |     |                | --           |           |        |
| Command Information      |         |     |                |              |           |        |
| Platforms                | Command |     | context        |              | Authority |        |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| destination | tunnel |     |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- | --- |
destination tunnel <TUNNEL-IPV4-ADDR> source <SOURCE-IPv4-ADDR>
| dscp <DSCP-VALUE> |        | vrf | <VRF-NAME> | id <SPAN-ID> |     |     |
| ----------------- | ------ | --- | ---------- | ------------ | --- | --- |
| no destination    | tunnel |     |            |              |     |     |
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
Mirroring|59

The no form of this command will cease the use of the tunnel and disable the session.

Parameter

Description

<TUNNEL-IPV4-ADDR>

<SOURCE-IPv4-ADDR>

<DSCP-VALUE>

<VRF-NAME>

<SPAN-ID>

Examples

Specifies the tunnel address in IPv4 format (x.x.x.x), where x is
a decimal number from 0 to 255.

Specifies the source address in IPv4 format (x.x.x.x), where x is
a decimal number from 0 to 255.

Specifies the DSCP value to be carried within the DS field of
ERSPAN packet header. Range: 0 to 63. Default: 0.

Specifies a VRF name. Default: default.

Specifies the span ID for the ERSPAN session and during a failover.
Range: 0 to 10.

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

Modification

--

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

60

| Command   | Information |         |           |     |
| --------- | ----------- | ------- | --------- | --- |
| Platforms | Command     | context | Authority |     |
config-mirror-<SESSION-ID>
| 8400 |     |     | Administratorsorlocalusergroupmemberswith |     |
| ---- | --- | --- | ----------------------------------------- | --- |
executionrightsforthiscommand.
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
| Parameter |     | Description                           |     |     |
| --------- | --- | ------------------------------------- | --- | --- |
| file      |     | Savescapturedpacketstoatemporaryfile. |     |     |
delete-file
Deletesthemostrecentcapturedfile.
Example
Performingdiagnostic:
switch#
diagnostic
| switch#        | diagnostic          | utilities tshark    | file         |            |
| -------------- | ------------------- | ------------------- | ------------ | ---------- |
| Inspecting     | traffic             | mirrored to the CPU | until Ctrl-C | is entered |
| ^CEnding       | traffic inspection. |                     |              |            |
| Command        | History             |                     |              |            |
| Release        |                     | Modification        |              |            |
| 10.07orearlier |                     | --                  |              |            |
| Command        | Information         |                     |              |            |
Mirroring|61

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution
rights for this command.

diag utilities tcpdump
diag utilities tcpdump [command <TEXT> | delete file <FILE-NAME> | list-files |

vrf <VRF-NAME> | count <COUNT-NUM> | proto <PROTO-NUM> | host-ip <IP-ADDR> | source-ip
<IP-ADDR> | destination-ip <IP-ADDR> | host-port <PORT> | source-port <PORT> |
destination-port <PORT> | verbosity <LEVEL> | print <DATA> | ethernet-type <ETH-NUM>]

Description

Captures traffic received or transmitted over a network.

Parameter

command <TEXT>

Description

Captures packets based on a specified tcpdump command string.

delete file <FILE-NAME>

Deletes specified tcpdump list files.

list-files

vrf <VRF-NAME>

count <COUNT-NUM>

proto <PROTO-NUM>

host-ip <IP-ADDR>

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

n When using the command option, the only traffic captured will be packets that have been mirrored to

the CPU.

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

62

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

Mirroring | 63

switch# diag utilities tcpdump delete-file my_capture_file.pcap
| Successfully        | removed | file    |                   |     |
| ------------------- | ------- | ------- | ----------------- | --- |
| Command History     |         |         |                   |     |
| Release             |         |         | Modification      |     |
| 10.08               |         |         | Commandintroduced |     |
| Command Information |         |         |                   |     |
| Platforms           | Command | context | Authority         |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
disable
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
| switch(config)#          | mirror  | session | 3            |           |
| ------------------------ | ------- | ------- | ------------ | --------- |
| switch(config-mirror-3)# |         | disable |              |           |
| Command History          |         |         |              |           |
| Release                  |         |         | Modification |           |
| 10.07orearlier           |         |         | --           |           |
| Command Information      |         |         |              |           |
| Platforms                | Command | context |              | Authority |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
enable
enable
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 64

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
n Toenablethemirroringsession,firstyoumustdisablesFlowontheport.
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
config-mirror-<SESSION-ID>
| Allplatforms |     |     |     | Administratorsorlocalusergroupmemberswith |
| ------------ | --- | --- | --- | ----------------------------------------- |
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
Mirroring|65

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
| switch(config)# |     | no  | mirror session | 1   |
| --------------- | --- | --- | -------------- | --- |
switch(config)#
| Command        | History     |     |         |              |
| -------------- | ----------- | --- | ------- | ------------ |
| Release        |             |     |         | Modification |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show mirror |                |     |            |     |
| ----------- | -------------- | --- | ---------- | --- |
| show mirror | [<SESSION-ID>] |     | [vsx-peer] |     |
Description
Showsinformationaboutmirroringsessions.If<SESSION-ID>isnotspecified,thenthecommandshows
asummaryofallconfiguredmirroringsessions.If<SESSION-ID>isspecified,thenthecommandshows
detailedinformationaboutthespecifiedmirroringsession.
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
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 66

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
Mirroring|67

| Release        |             |         |         |     | Modification |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| source    | interface |             |     |               |             |               |
| --------- | --------- | ----------- | --- | ------------- | ----------- | ------------- |
| source    | interface | {<PORT-NUM> |     | | <LAG-NAME>} |             | [<DIRECTION>] |
| no source | interface | {<PORT-NUM> |     | |             | <LAG-NAME>} | [<DIRECTION>] |
Description
Configuresthespecifiedinterface(eitheranEthernetportoraLAG)asasourceoftraffictobemirrored.
Thenoformofthiscommandceasesmirroringtrafficfromthespecifiedsourceinterfaceandremoves
thesourceinterfacefromthemirroringsessionconfiguration.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<PORT-NUM>
Specifiesaphysicalportontheswitch.Usetheformat
member/slot/port(forexample,1/3/1).
<LAG-NAME> SpecifiestheidentifierfortheLAG(linkaggregationgroup).
<DIRECTION> Selectsthedirectionoftraffictobemirroredfromthissource
interface.Thereisnodefaultforthisparameter.Validvaluesare
thefollowing:
both
Mirrorbothtransmittedandreceivedpackets.
| rx  |     |     |     |     | Mirroronlyreceivedpackets. |     |
| --- | --- | --- | --- | --- | -------------------------- | --- |
tx
Mirroronlytransmittedpackets.
Usage
Thereisalimitofsourceinterfacesineachdirectionofagivenmirrorsession:
| Switch |     | Source | interface |     | limit |     |
| ------ | --- | ------ | --------- | --- | ----- | --- |
| 8400   |     | 256    |           |     |       |     |
However,thereisapracticallimittotheamountoftrafficthatamirrordestinationcantransmit.For
example,mirroringsessionwithmultiple10Gsourcescanoverwhelmasingle10Gdestination.
Youcanconfigurethesamesourceinterfaceinmultiplemirroringsessions,butonlyoneofthose
mirroringsessionscanbeenabledatatime.
Classifierpolicieswithmirroractionscanalsobeusedtomatchandmirrornetworktraffic.Although
mirroractionsofclassifierpoliciesmustspecifyanenabledmirroringsession,thetrafficmatchingand
mirroringactionsareseparatefromandtakepriorityoverbasicmirroringsessions.Forexample,
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 68

mirroringsession1mightmonitorasourceinterface,butaclassifierpolicymightmatchsometraffic
fromthatsamesourceinterfaceanddirectittothedestinationinterfaceofadifferentmirroring
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
Mirroring|69

Stoppingthemirroringofreceivedpacketsfromaconfiguredsourceinterface:
| switch(config-mirror-4)# |         | no source | interface    | lag1 rx   |
| ------------------------ | ------- | --------- | ------------ | --------- |
| Command History          |         |           |              |           |
| Release                  |         |           | Modification |           |
| 10.07orearlier           |         |           | --           |           |
| Command Information      |         |           |              |           |
| Platforms                | Command | context   |              | Authority |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 70

Chapter 9
|            |          |            | Monitoring | a device | using SNMP |
| ---------- | -------- | ---------- | ---------- | -------- | ---------- |
| Monitoring | a device | using SNMP |            |          |            |
Configuring SNMP:RefertotheSNMP/MIBGuideforinformationonhowtoaddSNMPsoadevicecan
bemonitoredfromanetworkmanagementsystem(NMS).
Configuring an SNMP trap receiver:RefertotheSNMP/MIBGuideandspecificinformationaboutthe
| show snmp | trapcommandtoenableSNMPtraps. |     |     |     |     |
| --------- | ----------------------------- | --- | --- | --- | --- |
71
AOS-CX10.10MonitoringGuide|(8400SwitchSeries)

Chapter 10

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

Splits a port into multiple interfaces. Only ports capable of supporting breakout cables or SR4/eSR4
optics can be split.

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

72

4.Fortransceiverscapableofsupportingmultiplesplitmodes,theclosestmodewithenoughlanesis
used.
n Sometransceiversalsosupportmultiplesplitmodeswithdifferentspeeds.Forexample,2x200Gor
2x100G.Whenaspeedisnotspecified,thehighestavailablespeedforthesplitcountisused.To
selectadifferentsplitmodewithalowerspeed,thedesiredspeedmustbespecified.
Thesplittableportsforallmodelsareshowninthetablebelow:
| Model |     |     |     | Description |     |     | Port info |     |
| ----- | --- | --- | --- | ----------- | --- | --- | --------- | --- |
Aruba8400Xmodules
| n JL365A |     |     |     | Aruba8400X8p40GQSFP+AdvMod |     |     | 1-8(40G) |     |
| -------- | --- | --- | --- | -------------------------- | --- | --- | -------- | --- |
n JL366A
|     |     |     |     | Aruba8400X6p40G/100GQSFP28 |     |     | 1-6Onlycapableof40Gsplitinto |     |
| --- | --- | --- | --- | -------------------------- | --- | --- | ---------------------------- | --- |
|     |     |     |     | AdvMod                     |     |     | 4x10G                        |     |
JL366Amodulesdonothave25G
MACstosupportsplit100G
Examples
Splittinganinterface:
| switch(config-if)# |     |     | interface | 1/1/1 |     |     |     |     |
| ------------------ | --- | --- | --------- | ----- | --- | --- | --- | --- |
| switch(config-if)# |     |     | split     |       |     |     |     |     |
This command will disable the specified port, clear its configuration,
and split it into multiple interfaces. The split interfaces will not
| be available       |        | until | the next       | system | or line module | reboot. |     |     |
| ------------------ | ------ | ----- | -------------- | ------ | -------------- | ------- | --- | --- |
| Continue           | (y/n)? | y     |                |        |                |         |     |     |
| switch(config-if)# |        |       | show interface |        | brief          |         |     |     |
----------------------------------------------------------------------------------
----
| Port | Native | Mode | Type |     | Enabled Status | Reason |     | Speed |
| ---- | ------ | ---- | ---- | --- | -------------- | ------ | --- | ----- |
| Desc |        | VLAN |      |     |                |        |     |       |
----------------------------------------------------------------------------------
----
1/1/1:1 -- routed QSFP+DA3x4 yes down Split reboot pending -- -
-
1/1/1:2 -- routed QSFP+DA3x4 yes down Split reboot pending -- -
-
1/1/1:3 -- routed QSFP+DA3x4 yes down Split reboot pending -- -
-
1/1/1:4 -- routed QSFP+DA3x4 yes down Split reboot pending -- -
-
Unsplittingaportonaswitchthatrequiresareboot:
| switch(config)#    |     | interface |          | 1/1/1 |     |     |     |     |
| ------------------ | --- | --------- | -------- | ----- | --- | --- | --- | --- |
| switch(config-if)# |     |           | no split |       |     |     |     |     |
This command will disable the split interfaces for this port and clear
their configuration. The port will not be available until the next
| system   | or line | module | reboot. |     |     |     |     |     |
| -------- | ------- | ------ | ------- | --- | --- | --- | --- | --- |
| Continue | (y/n)?  | y      |         |     |     |     |     |     |
Breakoutcablesupport|73

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8400 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10MonitoringGuide|(8400SwitchSeries) 74

Chapter 11
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
75
AOS-CX10.10MonitoringGuide|(8400SwitchSeries)

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
ArubaAirWave|76

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

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

77

Chapter 12

Support and Other Resources

Support and Other Resources

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

https://www.arubanetworks.com/support-services/

AOS-CX Switch Software Documentation
Portal

https://www.arubanetworks.com/techdocs/AOS-CX/help_
portal/Content/home.htm

HPE Aruba Networking Support Portal

https://networkingsupport.hpe.com/home

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

HPE Aruba
Networking
Developer Hub

Airheads social
forums and
Knowledge Base

https://developer.arubanetworks.com/hpe-aruba-networking-aoscx/docs/about

https://community.arubanetworks.com/

AOS-CX Software

Videos on new features introduced in this release:

Technical Update

https://www.youtube.com/playlist?list=PLsYGHuNuBZcbWPEjjHuVMqP-Q_UL3CskS

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

78

channel on

YouTube.

HPE Aruba
Networking
Hardware
Documentation
and Translations
Portal

HPE Aruba
Networking
software

Software
licensing and
Feature Packs

End-of-Life
information

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

https://networkingsupport.hpe.com/downloads

https://licensemanagement.hpe.com/

https://www.arubanetworks.com/support-services/end-of-life/

Accessing Updates

You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

https://asp.arubanetworks.com/downloads

If you are unable to find your product in the Aruba Support Portal, you may need to search My
Networking, where older networking products can be found:

My Networking

https://www.hpe.com/networking/support

To view and update your entitlements, and to link your contracts and warranties with your profile, go to
the Hewlett Packard Enterprise Support Center More Information on Access to Support Materials
page:

https://support.hpe.com/portal/site/hpsc/aae/home/

Access to some updates might require product entitlement when accessed through the Hewlett Packard
Enterprise Support Center. You must have an HP Passport set up with relevant entitlements.

Some software products provide a mechanism for accessing software updates through the product
interface. Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://asp.arubanetworks.com/notifications/subscriptions (requires an active Aruba Support Portal
(ASP) account to manage subscriptions). Security notices are viewable without an ASP account.

Warranty Information

To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Support and Other Resources | 79

Regulatory Information

To view the regulatory information for your product, view the Safety and Compliance Information for
Server, Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs,
product recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For
more information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation Feedback

Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

AOS-CX 10.10 Monitoring Guide | (8400 Switch Series)

80