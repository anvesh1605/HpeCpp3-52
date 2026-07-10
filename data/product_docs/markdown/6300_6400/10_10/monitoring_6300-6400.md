AOS-CX 10.10 Monitoring
Guide

6300, 6400 Switch Series

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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

3

Contents
| About                                             | this document                      |              |                    | 8   |
| ------------------------------------------------- | ---------------------------------- | ------------ | ------------------ | --- |
| Applicableproducts                                |                                    |              |                    | 8   |
| Latestversionavailableonline                      |                                    |              |                    | 8   |
| Commandsyntaxnotationconventions                  |                                    |              |                    | 8   |
| Abouttheexamples                                  |                                    |              |                    | 9   |
| Identifyingswitchportsandinterfaces               |                                    |              |                    | 9   |
| Identifyingmodularswitchcomponents                |                                    |              |                    | 10  |
| Monitoring                                        | hardware                           | through      | visual observation | 11  |
| ConfirmingnormaloperationoftheswitchbyreadingLEDs |                                    |              |                    | 11  |
| Detectingiftheswitchisnotreadyforafailoverevent   |                                    |              |                    | 12  |
| FindingfaultedcomponentsusingtheswitchLEDs        |                                    |              |                    | 12  |
| Boot                                              | commands                           |              |                    | 14  |
| bootfabric-module                                 |                                    |              |                    | 14  |
| bootline-module                                   |                                    |              |                    | 15  |
| bootmanagement-module                             |                                    |              |                    | 16  |
| bootset-default                                   |                                    |              |                    | 17  |
| bootsystem                                        |                                    |              |                    | 18  |
| showboot-history                                  |                                    |              |                    | 20  |
| Switch                                            | system                             | and hardware | commands           | 22  |
| External                                          | storage                            |              |                    | 23  |
| Externalstoragecommands                           |                                    |              |                    | 23  |
|                                                   | address                            |              |                    | 23  |
|                                                   | directory                          |              |                    | 24  |
|                                                   | disable                            |              |                    | 25  |
|                                                   | enable                             |              |                    | 25  |
|                                                   | external-storage                   |              |                    | 26  |
|                                                   | password(external-storage)         |              |                    | 27  |
|                                                   | showexternal-storage               |              |                    | 28  |
|                                                   | showrunning-configexternal-storage |              |                    | 28  |
|                                                   | type                               |              |                    | 29  |
|                                                   | username                           |              |                    | 30  |
|                                                   | vrf                                |              |                    | 31  |
| IP-SLA                                            |                                    |              |                    | 32  |
| IP-SLAguidelines                                  |                                    |              |                    | 32  |
| LimitationswithVoIPSLAs                           |                                    |              |                    | 33  |
| IP-SLAcommands                                    |                                    |              |                    | 33  |
|                                                   | http                               |              |                    | 33  |
|                                                   | icmp-echo                          |              |                    | 34  |
|                                                   | ip-sla                             |              |                    | 35  |
|                                                   | ip-slaresponder                    |              |                    | 36  |
|                                                   | showip-slaresponder                |              |                    | 37  |
|                                                   | showip-slaresponderresults         |              |                    | 38  |
|                                                   | showip-sla<SLA-NAME>               |              |                    | 38  |
5
AOS-CX10.10MonitoringGuide| (6300,6400SwitchSeries)

| start-test                             |           |            | 41  |
| -------------------------------------- | --------- | ---------- | --- |
| stop-test                              |           |            | 42  |
| tcp-connect                            |           |            | 42  |
| udp-echo                               |           |            | 43  |
| udp-jitter-voip                        |           |            | 45  |
| vrf                                    |           |            | 46  |
| L1-100Mbps                             | downshift |            | 47  |
| Limitationswithspeeddownshift          |           |            | 47  |
| L1-100Mbpsdownshiftcommands            |           |            | 47  |
| downshiftenable                        |           |            | 47  |
| showinterface                          |           |            | 48  |
| showinterfacedownshift-enable          |           |            | 52  |
| showrunning-configinterface            |           |            | 53  |
| Mirroring                              |           |            | 56  |
| Mirrorstatistics                       |           |            | 56  |
| Classifierpoliciesandmirroringsessions |           |            | 56  |
| VLANasasource                          |           |            | 57  |
| Mirroringcommands                      |           |            | 57  |
| clearmirror                            |           |            | 57  |
| comment                                |           |            | 58  |
| copytcpdump-pcap                       |           |            | 59  |
| copytshark-pcap                        |           |            | 60  |
| destinationcpu                         |           |            | 61  |
| destinationinterface                   |           |            | 62  |
| destinationtunnel                      |           |            | 63  |
| diagnostic                             |           |            | 64  |
| diagutilitiestcpdump                   |           |            | 65  |
| disable                                |           |            | 67  |
| enable                                 |           |            | 68  |
| mirrorsession                          |           |            | 69  |
| showmirror                             |           |            | 69  |
| sourceinterface                        |           |            | 71  |
| Monitoring                             | a device  | using SNMP | 74  |
| Power-over-Ethernet                    |           |            | 75  |
| PoEcommands                            |           |            | 76  |
| lldpdot3poe                            |           |            | 76  |
| lldpmedpoe                             |           |            | 77  |
| power-over-ethernet                    |           |            | 77  |
| power-over-ethernetallocate-by         |           |            | 78  |
| power-over-ethernetalways-on           |           |            | 79  |
| power-over-ethernetassigned-class      |           |            | 80  |
| power-over-ethernetpower-pairs         |           |            | 81  |
| power-over-ethernetpre-std-detect      |           |            | 82  |
| power-over-ethernetpriority            |           |            | 83  |
| power-over-ethernetquick-poe           |           |            | 83  |
| power-over-ethernetthreshold           |           |            | 84  |
| power-over-ethernettrap                |           |            | 85  |
| showlldplocal                          |           |            | 86  |
| showlldpneighbor                       |           |            | 87  |
| showpower-over-ethernet                |           |            | 88  |
| Aruba AirWave                          |           |            | 95  |
|6

| SNMPsupportandAirWave                            |                    |           | 95  |
| ------------------------------------------------ | ------------------ | --------- | --- |
|                                                  | SNMPontheswitch    |           | 95  |
| SupportedfeatureswithAirWaveandtheAOS-CXswitch   |                    |           | 96  |
| ConfiguringtheAOS-CXswitchtobemonitoredbyAirWave |                    |           | 96  |
| Support                                          | and Other          | Resources | 98  |
| AccessingHPEArubaNetworkingSupport               |                    |           | 98  |
| AccessingUpdates                                 |                    |           | 99  |
|                                                  | ArubaSupportPortal |           | 99  |
|                                                  | MyNetworking       |           | 99  |
| WarrantyInformation                              |                    |           | 99  |
| RegulatoryInformation                            |                    |           | 100 |
| DocumentationFeedback                            |                    |           | 100 |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 7

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A)

n Aruba 6400 Switch Series (JL762A, R0X31A, R0X38B, R0X39B, R0X40B, R0X41A, R0X42A, R0X43A,

R0X44A, R0X45A, R0X26A, R0X27A, JL741A)

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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

8

| Convention |     | Usage |     |
| ---------- | --- | ----- | --- |
{ } Braces.Indicatesthatatleastoneoftheencloseditemsisrequired.
| [ ] |     | Brackets.Indicatesthattheencloseditemoritemsareoptional. |     |
| --- | --- | -------------------------------------------------------- | --- |
| …or |     | Ellipsis:                                                |     |
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
| On the 6300 Switch | Series |     |     |
| ------------------ | ------ | --- | --- |
Aboutthisdocument|9

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.
The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

10

Monitoring hardware through visual

Chapter 2

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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

11

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
Monitoringhardwarethroughvisualobservation|12

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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

13

Chapter 3
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
14
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries)

| Release             |         |     |         | Modification |
| ------------------- | ------- | --- | ------- | ------------ |
| 10.07orearlier      |         |     |         | --           |
| Command Information |         |     |         |              |
| Platforms           | Command |     | context | Authority    |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --------------------- |
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
Thiscommandissupportedonswitchesthathavemultiplelinemodules.
Rebootsthespecifiedlinemodule.Anytrafficfortheswitchpassingthroughtheaffectedmodule(SSH,
TELNET,andSNMP)isinterrupted.Itcantakeupto2minutestorebootthemodule.Duringthattime,
youcanmonitorprogressbyviewingtheeventlog.
Thiscommandisvalidforlinemodulesonly.
Examples
Reloadingthemoduleinslot1/1:
switch#
| boot | line-module |     | 1/1 |     |
| ---- | ----------- | --- | --- | --- |
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
Bootcommands|15

Platforms

Command context

Authority

6300
6400

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

This command is supported on switches that have multiple management modules.

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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

16

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
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6400
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
Bootcommands|17

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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

18

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
Bootcommands|19

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
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 20

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
Bootcommands|21

Chapter 4
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
Switchsystemandhardwarecommandsaregeneralcommandsusedtoconfigurefundamentalsettings
ontheswitch.
RefertotheFundamentalsGuidetoviewtheswitchsystemandhardwarecommands.
22
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries)

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
23
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries)

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
6300 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 6400 |     |     |     | memberswithexecutionrightsforthis |
| ---- | --- | --- | --- | --------------------------------- |
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
Externalstorage|24

| Release             |         |         | Modification |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
6300 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
| 6400 |     |     |     | usergroupmemberswithexecution |
| ---- | --- | --- | --- | ----------------------------- |
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
6300 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
| 6400 |     |     |     | usergroupmemberswithexecution |
| ---- | --- | --- | --- | ----------------------------- |
rightsforthiscommand.Operatorscan
executethiscommandfromthe
operatorcontext(>)only.
enable
enable
no enable
Description
Enablestheexternalstoragevolume.
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 25

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
6300 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
| 6400 |     |     |     | usergroupmemberswithexecution |
| ---- | --- | --- | --- | ----------------------------- |
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
Externalstorage|26

| Release        |             |     |         | Modification |
| -------------- | ----------- | --- | ------- | ------------ |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400        |                    |     |               | rightsforthiscommand. |
| ----------- | ------------------ | --- | ------------- | --------------------- |
| password    | (external-storage) |     |               |                       |
| password    | [{plaintext        |     | | ciphertext} | <PASSWORD>]           |
| no password | {plaintext         |     | | ciphertext} | <PASSWORD>            |
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
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 27

| Release        |             |         | Modification |           |     |     |
| -------------- | ----------- | ------- | ------------ | --------- | --- | --- |
| 10.07orearlier |             |         | --           |           |     |     |
| Command        | Information |         |              |           |     |     |
| Platforms      | Command     | context |              | Authority |     |     |
6300 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 6400 |     |     |     | memberswithexecutionrightsforthis |     |     |
| ---- | --- | --- | --- | --------------------------------- | --- | --- |
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
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |     |     |     |
| ---- | --- | --- | --------------------- | --- | --- | --- |
(#)
| show running-config |     | external-storage |     |     |     |     |
| ------------------- | --- | ---------------- | --- | --- | --- | --- |
Externalstorage|28

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
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
| 6400 |     | (#) |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --- | --------------------- |
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
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 29

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
6300 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 6400 |     |     |     | memberswithexecutionrightsforthis |
| ---- | --- | --- | --- | --------------------------------- |
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
Externalstorage|30

| Release             |         |         | Modification |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
6300 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 6400 |     |     |     | memberswithexecutionrightsforthis |
| ---- | --- | --- | --- | --------------------------------- |
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
6300 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 6400 |     |     |     | memberswithexecutionrightsforthis |
| ---- | --- | --- | --- | --------------------------------- |
command.
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 31

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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

32

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

IP-SLA | 33

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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | ------------------------------ |
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
| name-server | <IPV4-ADDR-DNS-SERVER> |     |     |
| ----------- | ---------------------- | --- | --- |
SpecifiestheDNSserverfordestinationhostname
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 34

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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | --- | ------------------------------ | --- |
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
<IP-SLA-NAME> SpecifiesanIP-SLAprofilename.Length:1to63characters.
Examples
CreatinganIP-SLA:
IP-SLA|35

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
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
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
| Parameter  |     |     | Description          |     |
| ---------- | --- | --- | -------------------- | --- |
| <SLA-NAME> |     |     | SpecifiestheSLAname. |     |
udp-echo
Enablesresponderforudp-echoprobes.
| tcp-connect |     |     | SelectsTCPconnectastheIP-SLAtestmechanism. |     |
| ----------- | --- | --- | ------------------------------------------ | --- |
vrf <VRF-NAME>
SpecifiesthenameoftheVRFtouse.
| udp-jitter-voip |     |     | SelectsVOIPjitterastheIP-SLAtestmechanism. |     |
| --------------- | --- | --- | ------------------------------------------ | --- |
<PORT-NUM>
SpecifiestheportnumbertolistenforIP-SLAprobes.
Range:1to65535.
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
Examples
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 36

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
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400 |        |           |            |     | rightsforthiscommand. |     |     |     |
| ---- | ------ | --------- | ---------- | --- | --------------------- | --- | --- | --- |
| show | ip-sla | responder |            |     |                       |     |     |     |
| show | ip-sla | responder | <SLA-NAME> |     |                       |     |     |     |
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
IP-SLA|37

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400 |        |           |     |         | rightsforthiscommand. |     |
| ---- | ------ | --------- | --- | ------- | --------------------- | --- |
| show | ip-sla | responder |     | results |                       |     |
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
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400 |        |            |         |     | rightsforthiscommand. |     |
| ---- | ------ | ---------- | ------- | --- | --------------------- | --- |
| show | ip-sla | <SLA-NAME> |         |     |                       |     |
| show | ip-sla | <SLA-NAME> | results |     |                       |     |
Description
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 38

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
IP-SLA|39

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
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 40

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
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     |     |     |     | rightsforthiscommand. |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
(#)
start-test
start-test
IP-SLA|41

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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | ------------------------------ |
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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | ------------------------------ |
tcp-connect
tcp-connect {<DEST-IPV4-ADDR> | <HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>]
| [probe-interval | <PROBE-INTERVAL>] |     |     |
| --------------- | ----------------- | --- | --- |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 42

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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
udp-echo
udp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>] [payload-
size
<PAYLOAD-SIZE>] [tos <TYPE-OF-SERVICE>] [probe-interval <PROBE-INTERVAL>]
IP-SLA|43

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
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 44

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
udp-jitter-voip
udp-jitter-voip {<DEST-IPV4-ADDR> | <HOSTNAME>} <PORT-NUM> [codec-type <CODEC-TYPE>]
[advantage-factor <VALUE>] [source {<SOURCE-IPV4-ADDR> | <IFNAME>} [source-port
<PORT-NUM>]]
[name-server <IPV4-ADDR-DNS-SERVER>][probe-interval <PROBE-INTERVAL>] [tos <TYPE-OF-
SERVICE>]
Description
ConfigureUDPjittervoipastheIP-SLAtestmechanism.Requiresdestinationaddress/hostnameand
sourceaddress/interfacefortheIP-SLAofudp-jitter-voipIP-SLAtype.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
{<DEST-IPV4-ADDR>|<HOSTNAME>} SelectsthedestinationIPv4addressfortheIP-SLAor
thehostnameofthedestination.
| <PORT-NUM> |     |     |     | SelectstheportnumberfortheIP-SLA.Range:1to |
| ---------- | --- | --- | --- | ------------------------------------------ |
65535.
| [codec-type | <CODEC-TYPE>] |     |     |     |
| ----------- | ------------- | --- | --- | --- |
Selectsthecodec-typefortheVoipIP-SLAtest.
[advantage-factor <ADVANTAGE-FACTOR>] Selectsthevaluefortheadvantagefactor.Default
valueis0.
| [source {<SOURCE-IPV4-ADDR> |     | |   | <IFNAME>}] |     |
| --------------------------- | --- | --- | ---------- | --- |
SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
[source-port <PORT-NUM>] SpecifiesthevalueofsourceportfortheIP-SLA
probes.
[name-server <IPV4-ADDR-DNS-SERVER>] SpecifiestheDNSserverfordestinationhostname
resolution.
tos <TYPE-OF-SERVICE> Specifiesthetypeofservice.Range:0to255.
probe-interval <PROBE-INTERVAL> Specifiestheprobeintervalinseconds.Range:120to
604800.
Examples
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10 codec-
type g711a
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10
| codec-type | g711a source | 2.2.2.1 |     |     |
| ---------- | ------------ | ------- | --- | --- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
| advantage-factor | 10  | codec-type | g711a |     |
| ---------------- | --- | ---------- | ----- | --- |
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10
| codec-type | g711a source | 1/1/1 |     |     |
| ---------- | ------------ | ----- | --- | --- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
| advantage-factor | 10  | codec-type | g711a source | 2.2.2.1 |
| ---------------- | --- | ---------- | ------------ | ------- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
IP-SLA|45

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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
6400
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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | ------------------------------ | --- |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 46

Chapter 7
L1-100Mbps downshift
| L1-100Mbps downshift |     |     |
| -------------------- | --- | --- |
Thespeeddownshiftfeatureallowstheusertolink-upatsub-optimalspeedswhenfailingtolink-upat
thehighestadvertisedspeed.Therearefixednumberoflinkattemptsmadetoestablishlinkathighest
advertisedspeedandwhenallofthemfailandattemptismadetolink-upatalowerpossiblespeed.
ThisfeaturerequiresunderlyingPHYtohavesupportforthesameandhencecapabilityisonlyaddedto
selectsetofports.Ifalinkcannotbeestablishedatthehighestcommondenominatorwithinaset
numberoflinkattempts,thePHYadvertisesthenexthighestspeedusingauto-negotiation.
| Limitations | with speed | downshift |
| ----------- | ---------- | --------- |
n Linkupmaybedelayedascertainnumberofretriesaredonetoestablishthelinkathighest
advertisespeedsbybothlinkpartnersbeforedownshifting.
Linkmaybeestablishedatsub-optimalspeed.
n
| L1-100Mbps       | downshift | commands |
| ---------------- | --------- | -------- |
| downshift enable |           |          |
downshift-enable
no downshift-enable
Description
Enables/disablesautomaticspeeddownshiftonaninterfacethatsupportsdownshift,generally1GBASE-
Tports.Whenenabled,downshiftallowsaninterfacetolinkataloweradvertisedspeedwhenunableto
establishastablelinkatthemaximumspeed.Downshiftingonlyappliestophysicalinterfacesthatare
notmembersofaLAGandisonlyavailablewhenauto-negotiationisenabled.Whenonlyonespeedis
advertised,downshiftwillnotbetriggered.
Examples
| switch(config-if)# | interface        | 1/1/1 |
| ------------------ | ---------------- | ----- |
| switch(config-if)# | downshift-enable |       |
Warning: this is a non-standard mode for use only when standards-based
auto-negotiation is not able to establish a stable link. Enabling this
may cause the port to link at a lower than expected speed and should
not be used on ports that are members of a LAG. Support calls may require
| this feature    | to be disabled |     |
| --------------- | -------------- | --- |
| Continue (y/n)? |                |     |
switch(config-if)#
Whenautomaticdownshiftisenabled:
47
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries)

| switch(config-if)# |       | show | running-config |     | interface |
| ------------------ | ----- | ---- | -------------- | --- | --------- |
| interface          | 1/1/1 |      |                |     |           |
downshift-enable
Disablingautomaticspeeddownshift:
| switch(config-if)#  |         | interface           | 1/1/1 |              |     |
| ------------------- | ------- | ------------------- | ----- | ------------ | --- |
| switch(config-if)#  |         | no downshift-enable |       |              |     |
| Command History     |         |                     |       |              |     |
| Release             |         |                     |       | Modification |     |
| 10.07orearlier      |         |                     |       | --           |     |
| Command Information |         |                     |       |              |     |
| Platforms           | Command | context             |       | Authority    |     |
config-if
| 6300           |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| -------------- | --- | --- | --- | -------------------------------------------------- | --- |
| 6400           |     |     |     | rightsforthiscommand.                              |     |
| show interface |     |     |     |                                                    |     |
show interface [<IFNNAME>|<IFRANGE>] [brief | physical | extended [non-zero] [human-
| readable] | | [human-readable]] |     |     |     |     |
| ----------- | ----------------- | --- | --- | --- | --- |
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief | physical]
| show interface | lag | [<LAG-ID>] | [extended |     | [non-zero]] |
| -------------- | --- | ---------- | --------- | --- | ----------- |
Description
Showsactiveconfigurationsandoperationalstatusinformationforinterfaces.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<IFNAME>
Specifiesainterfacename.
| <IFRANGE> |     |     |     | Specifiestheportidentifierrange. |     |
| --------- | --- | --- | --- | -------------------------------- | --- |
brief
Showsbriefinfointabularformat.
| physical |     |     |     | Showsthephysicalconnectioninfointabularformat. |     |
| -------- | --- | --- | --- | ---------------------------------------------- | --- |
extended
Showsadditionalstatistics.
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
| non-zero |     |     |     | Showsonlynonzerostatistics.   |     |
| -------- | --- | --- | --- | ----------------------------- | --- |
| LAG      |     |     |     | ShowsLAGinterfaceinformation. |     |
L1-100Mbpsdownshift|48

| Parameter     |     |     |     | Description                                    |     |     |     |     |
| ------------- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- |
| LOOPBACK      |     |     |     | Showsloopbackinterfaceinformation.             |     |     |     |     |
| TUNNEL        |     |     |     | Showstunnelinterfaceinformation.               |     |     |     |     |
| VLAN          |     |     |     | ShowsVLANinterfaceinformation.                 |     |     |     |     |
| <LAG-ID>      |     |     |     | SpecifiestheLAGnumber.Range:1-256              |     |     |     |     |
| <LOOPBACK-ID> |     |     |     | SpecifiestheLOOPBACKnumber.Range:0-255         |     |     |     |     |
| <TUNNEL-ID>   |     |     |     | SpecifiesthetunnelID.Range:1-255               |     |     |     |     |
| <VLAN-ID>     |     |     |     | SpecifiestheVLANID.Range:1-4094                |     |     |     |     |
| VXLAN         |     |     |     | ShowstheVXLANinterfaceinformation.             |     |     |     |     |
| <VXLAN-ID>    |     |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |     |     |     |
Examples
Showinginterfaceinformationwhenitisconfiguredasaroute-onlyport:
| switch#           | show interface |        | 1/1/1        |                   |                 |           |     |     |
| ----------------- | -------------- | ------ | ------------ | ----------------- | --------------- | --------- | --- | --- |
| Interface         | 1/1/1          | is up  |              |                   |                 |           |     |     |
| Admin state       | is             | up     |              |                   |                 |           |     |     |
| Link state:       | up             | for    | 2 days       | (since Sun        | Jun 21 05:30:22 | UTC 2020) |     |     |
| Link transitions: |                | 1      |              |                   |                 |           |     |     |
| Description:      |                | backup | data center  | link              |                 |           |     |     |
| Hardware:         | Ethernet,      |        | MAC Address: | 70:72:cf:fd:e7:b4 |                 |           |     |     |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | none |             |     |               |            |     |       |         |
| ---------------- | ---- | ----------- | --- | ------------- | ---------- | --- | ----- | ------- |
| Speed 1000       | Mb/s |             |     |               |            |     |       |         |
| Auto-negotiation |      | is          | on  |               |            |     |       |         |
| Flow-control:    |      | off         |     |               |            |     |       |         |
| Error-control:   |      | off         |     |               |            |     |       |         |
| Energy-Efficient |      | Ethernet    |     | is enabledMDI | mode: MDIX |     |       |         |
| L3 Counters:     |      | Rx Enabled, | Tx  | Enabled       |            |     |       |         |
| Rate collection  |      | interval:   |     | 300 seconds   |            |     |       |         |
| Rates            |      |             |     | RX            |            | TX  | Total | (RX+TX) |
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
| Packets   |     |     |     | 0   |     | 0   |     | 0   |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast   |     |     |     | 0   |     | 0   |     | 0   |
| Multicast |     |     |     | 0   |     | 0   |     | 0   |
| Broadcast |     |     |     | 0   |     | 0   |     | 0   |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 49

| Bytes        |     |     |     | 0   |     | 0   |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
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
Showinginformationwhentheinterfaceiscurrentlylinkedwithenergy-efficient-ethernetnegotiated:
| switch(config-if)# |       | show  | interface | 1/1/1 |     |     |     |     |
| ------------------ | ----- | ----- | --------- | ----- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is up |           |       |     |     |     |     |
...
| Energy-Efficient |     | Ethernet | is  | enabled | and active |     |     |     |
| ---------------- | --- | -------- | --- | ------- | ---------- | --- | --- | --- |
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
| qos trust        | none            |                 |     |         |     |     |       |         |
| ---------------- | --------------- | --------------- | --- | ------- | --- | --- | ----- | ------- |
| Speed 0          | Mb/s            |                 |     |         |     |     |       |         |
| Auto-negotiation |                 | is off          |     |         |     |     |       |         |
| Flow-control:    |                 | off             |     |         |     |     |       |         |
| Error-control:   |                 | off             |     |         |     |     |       |         |
| VLAN Mode:       | native-untagged |                 |     |         |     |     |       |         |
| Native           | VLAN:           | 1               |     |         |     |     |       |         |
| Allowed          | VLAN            | List: 1502-1505 |     |         |     |     |       |         |
| Rate collection  |                 | interval:       | 300 | seconds |     |     |       |         |
| Rate             |                 |                 |     |         | RX  | TX  | Total | (RX+TX) |
L1-100Mbpsdownshift|50

---------------- -------------------- -------------------- --------------------
| Mbits       | /         | sec |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| ----------- | --------- | --- | --- | --- | ---- | --- | --- | ---- | --- | ----- |
| KPkts       | /         | sec |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
|             | Unicast   |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
|             | Multicast |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
|             | Broadcast |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Utilization |           |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Statistic   |           |     |     |     | RX   |     |     | TX   |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets |           |     |     |     | 0   |     |     | 0   |     | 0   |
| ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|         | Unicast   |     |     |     | 0   |     |     | 0   |     | 0   |
|         | Multicast |     |     |     | 0   |     |     | 0   |     | 0   |
|         | Broadcast |     |     |     | 0   |     |     | 0   |     | 0   |
| Bytes   |           |     |     |     | 0   |     |     | 0   |     | 0   |
| Jumbos  |           |     |     |     | 0   |     |     | 0   |     | 0   |
| Dropped |           |     |     |     | 0   |     |     | 0   |     | 0   |
| Pause   | Frames    |     |     |     | 0   |     |     | 0   |     | 0   |
| Errors  |           |     |     |     | 0   |     |     | 0   |     | 0   |
|         | CRC/FCS   |     |     |     | 0   |     |     | n/a |     | 0   |
|         | Collision |     |     |     | n/a |     |     | 0   |     | 0   |
|         | Runts     |     |     |     | 0   |     |     | n/a |     | 0   |
|         | Giants    |     |     |     | 0   |     |     | n/a |     | 0   |
ShowinginformationwhentheinterfaceisconfiguredwithEEEandtheEEEhasauto-negotiated:
| switch(config-if)# |     |     | show | interface | 1/1/1 physical |     |     |     |     |     |
| ------------------ | --- | --- | ---- | --------- | -------------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
----------------------------------------------------------
|        |     |        |           | Link   | Admin       |        | Speed       |          | Flow-Control |        |
| ------ | --- | ------ | --------- | ------ | ----------- | ------ | ----------- | -------- | ------------ | ------ |
|        | EEE |        | PoE Power |        |             | Port   |             |          |              |        |
| Port   |     | Type   |           | Status | Config      | Status |             | | Config | Status |     | Config |
| Status | |   | Config | (Watts)   | State  | Information |        | Description |          |              |        |
----------------------------------------------------------------------------------
----------------------------------------------------------
| 1/1/1 |     | 1GbT |     | up          | up  | 1G  |     | auto | off | off |
| ----- | --- | ---- | --- | ----------- | --- | --- | --- | ---- | --- | --- |
| on    |     | on   | --  | 10M/100M/1G |     |     | --  |      |     |     |
Showingtheoutputinhuman-readableformat:
Inthehuman-readableformat,the< 1symbolforUtilizationindicatesthattheamountofpacketsis
betweenzeroandone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsand
theUtilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
switch(config-if)#
|           |     |       | show  | interface | 1/1/1 human-readable |     |     |     |     |     |
| --------- | --- | ----- | ----- | --------- | -------------------- | --- | --- | --- | --- | --- |
| Interface |     | 1/1/1 | is up |           |                      |     |     |     |     |     |
...
| Rate |     |     |     |     | RX  |     |     | TX  | Total | (RX+TX) |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- |
---------------- -------------------- -------------------- --------------------
| Bits | / sec     |     |     |     | 3M  |     |     | 3M  |     | 6M  |
| ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pkts | / sec     |     |     |     | 316 |     |     | 316 |     | 633 |
|      | Unicast   |     |     |     | 319 |     |     | 319 |     | 638 |
|      | Multicast |     |     |     | 0   |     |     | 0   |     | 0   |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 51

|     | Broadcast   |     |     | 0   | 0   | 0     |
| --- | ----------- | --- | --- | --- | --- | ----- |
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
| Command        | History     |         |         |                               |     |     |
| -------------- | ----------- | ------- | ------- | ----------------------------- | --- | --- |
| Release        |             |         |         | Modification                  |     |     |
| 10.10          |             |         |         | Addedhuman-readableparameter. |     |     |
| 10.07orearlier |             |         |         | --                            |     |     |
| Command        | Information |         |         |                               |     |     |
| Platforms      |             | Command | context | Authority                     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show | interface | downshift-enable      |     |                  |     |     |
| ---- | --------- | --------------------- | --- | ---------------- | --- | --- |
| show | interface | [<IFNNAME>|<IFRANGE>] |     | downshift-enable |     |     |
Description
Displaysspeeddownshiftinformation,includingtheinterfacespeedstatusandconfiguration.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<IFNAME>
Specifiesainterfacename.
| <IFRANGE> |     |     |     | Specifiestheportidentifierrange. |     |     |
| --------- | --- | --- | --- | -------------------------------- | --- | --- |
Examples
Showingautomaticdownshiftinformation:
L1-100Mbpsdownshift|52

| switch(config-if)# |     |     | show interface | downshift-enable |     |
| ------------------ | --- | --- | -------------- | ---------------- | --- |
-------------------------------------------------
|      |         | Downshift |        | Speed  |          |
| ---- | ------- | --------- | ------ | ------ | -------- |
| Port | Enabled | |         | Active | Status | | Config |
-------------------------------------------------
| 1/1/1 | yes |     | yes | 100M-FDx | auto     |
| ----- | --- | --- | --- | -------- | -------- |
| 1/1/2 | yes |     | no  | 1G       | auto     |
| 1/1/3 | yes |     | no  | 100M-FDx | 100M-FDx |
| 1/1/4 | no  |     | no  | --       | auto     |
Showingautomaticdownshiftinformationonperinterface:
switch(config-if)#
|     |     |     | show interface | 1/1/2 | downshift-enable |
| --- | --- | --- | -------------- | ----- | ---------------- |
-------------------------------------------------
|      |         | Downshift |        | Speed  |          |
| ---- | ------- | --------- | ------ | ------ | -------- |
| Port | Enabled | |         | Active | Status | | Config |
-------------------------------------------------
| 1/1/2          | yes         |     | no      | 1G           | auto |
| -------------- | ----------- | --- | ------- | ------------ | ---- |
| Command        | History     |     |         |              |      |
| Release        |             |     |         | Modification |      |
| 10.07orearlier |             |     |         | --           |      |
| Command        | Information |     |         |              |      |
| Platforms      | Command     |     | context | Authority    |      |
config
| 6300 |     |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith  |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- |
| 6400 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
commandfromtheoperatorcontext(>)only.
| show running-config |     |           | interface |                       |     |
| ------------------- | --- | --------- | --------- | --------------------- | --- |
| show running-config |     | interface |           | [<IFNNAME>|<IFRANGE>] |     |
show running-config interface [lag | loopback | tunnel | vlan ] [<ID>]
Description
Displaysactiveconfigurationsofvariousswitchinterfaces.
| Parameter |     |     |     | Description                            |     |
| --------- | --- | --- | --- | -------------------------------------- | --- |
| <IFNAME>  |     |     |     | Specifiesainterfacename.               |     |
| <IFRANGE> |     |     |     | Specifiestheportidentifierrange.       |     |
| LAG       |     |     |     | SpecifiesLAGinterfaceinformation       |     |
| LOOPBACK  |     |     |     | Specifiesloopbackinterfaceinformation. |     |
| TUNNEL    |     |     |     | Specifiestunnelinterfaceinformation.   |     |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 53

| Parameter     |     | Description                                     |     |     |
| ------------- | --- | ----------------------------------------------- | --- | --- |
| VLAN          |     | SpecifiesVLANinterfaceinformation.              |     |     |
| <LAG-ID>      |     | SpecifiestheLAGnumber.Range:1-256.              |     |     |
| <LOOPBACK-ID> |     | SpecifiestheLOOPBACKnumber.Range:0-255.         |     |     |
| <TUNNEL-ID>   |     | SpecifiesthetunnelID.Range:1-255.               |     |     |
| <VLAN-ID>     |     | SpecifiestheVLANID.Range:1-4094.                |     |     |
| VXLAN         |     | SpecifiestheVXLANinterfaceinformation.          |     |     |
| <VXLAN-ID>    |     | SpecifiestheVXLANinterfaceidentifier.Default:1. |     |     |
Examples
Showing1/1/2interfaceconfiguration:
| switch(config-if)# | show  | running-config | interface | 1/1/2 |
| ------------------ | ----- | -------------- | --------- | ----- |
| interface          | 1/1/2 |                |           |       |
no shutdown
| description | DC-23 |     |     |     |
| ----------- | ----- | --- | --- | --- |
exit
Showingloopbackinterfacesconfigured:
| switch(config-if)# | show         | running-config | interface | loopback |
| ------------------ | ------------ | -------------- | --------- | -------- |
| interface          | loopback 1   |                |           |          |
| description        | lb interface | 1              |           |          |
exit
| interface   | loopback 2   |     |     |     |
| ----------- | ------------ | --- | --- | --- |
| description | lb interface | 2   |     |     |
exit
Showingloopbackinterfacesnotconfigured:
| switch(config-if)#  | show       | running-config | interface | loopback |
| ------------------- | ---------- | -------------- | --------- | -------- |
| No loopback         | interfaces | configured.    |           |          |
| Command History     |            |                |           |          |
| Release             |            | Modification   |           |          |
| 10.07orearlier      |            | --             |           |          |
| Command Information |            |                |           |          |
L1-100Mbpsdownshift|54

Platforms

Command context

Authority

6300
6400

config

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

55

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

Mirror statistics

Mirror statistics are reset for a Mirror-to-CPU session when an interface is added or removed from a
LAG that is a source interface in the Mirror session and during a failover.

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

If the packets being mirrored are received from a VLAN that is not allowed on the mirror destination, the
mirrored packets would be dropped at the mirror destination interface. When the mirrored packets are
dropped at the destination, the mirror output packet and byte count will increment, however the
packets will not be received at the mirror destination.

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

56

The mirror destination port among the active mirror sessions must be unique. That is, if an interface is
configured as a source or destination in an active mirror session, the same port cannot be used as a
destination in another active mirror session.

VLAN as a source

AOS-CX allows configuration of VLAN as a mirroring source. When a VLAN source is configured in the 'rx'
direction, all packets are mirrored as they are received in the switch. When a VLAN source is configured
in 'tx' direction, all packets are mirrored as they are transmitted out of the switch.

More than one source VLAN can be configured in a mirror session. Each such VLAN may specify its own
direction.

There is a limit of 1024 source VLANs in each direction of a given mirror session.

Same VLANs can be configured as a mirror source for multiple sessions.

Note: When changing a source VLAN in an enabled mirror session (that is, adding, changing direction, or
removing), mirrored packets being transmitted out the mirror destination port from other mirror
sources may be briefly interrupted during the reconfiguration.

Direction of an existing source VLAN can be updated in one of two ways:

1. Reenter the source vlan command with the new preferred direction.

2. Use the no form of the command with a direction (rx or tx) to selectively remove the specified
direction. Specifying the last remaining direction for that VLAN will remove the VLAN from the
configuration entirely.

For packets bridged through the switch:

If the mirror is configured in 'both' direction, two copies of packets are mirrored, otherwise one copy of
the packet will be mirrored.

For routed packets:

n If the mirror is configured in the 'rx' direction, packets are mirrored in the pre-routed form with the

destination MAC address as the switch address.

n If the mirror is configured in the 'tx' direction, packets are mirrored in the post-routed form with the

source MAC as the switch address. Destination MAC is the nexthop gateway or station.

n If the mirror is configured in the 'both' direction, one copy of the packet will be mirrored.

Control plane packets generated by the switch's CPU are processed both in the ingress and the egress
packet processing pipeline. The following are the behaviors for mirroring with VLAN as source:

n If the mirror is configured in the 'rx' or 'tx' direction, the packets are mirrored to the mirror

destination.

n If the mirror is configured in the 'both' direction, two copies of the packets are mirrored to the mirror

destination.

Mirroring commands

clear mirror
clear mirror [all | <SESSION-ID>]

Description

Mirroring | 57

Clearsthemirrorstatisticsforallconfiguredmirrorsessionsoraspecifiedsession
| Parameter |     |     | Description                     |
| --------- | --- | --- | ------------------------------- |
| all       |     |     | Specifiesallconfiguredsessions. |
<SESSION-ID> Specifiesanumericidentifierforthesession.Range:1to4
Examples
Clearingmirrorstatisticsforallconfiguredmirrorsessions:
| switch# clear | mirror | all |     |
| ------------- | ------ | --- | --- |
Clearingmirrorstatisticsformirrorsession1:
| switch# clear       | mirror  | 1       |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
comment
comment <COMMENT>
no comment
Description
Specifiesacommentforthemirroringsession.
Whenusedinmirrorendpointcommandcontext,specifiesacommentforthemirrorendpoint.
Thenoformofthiscommandremovesthecomment.
| Parameter |     |     | Description                                        |
| --------- | --- | --- | -------------------------------------------------- |
| <COMMENT> |     |     | Acommentstringofupto64characterscomposedofletters, |
numbers,underscores,dashes,spaces,andperiods.
Usage
Commentsareoptionalandcanbeaddedorremovedatanytimewithoutaffectingthestateofthe
mirroringsession.
Addingacommenttoasessionthatalreadyhasacommentreplacestheexistingcomment.
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 58

Examples
Addingacommenttoamirrorsession:
switch(config-mirror-3)#
|             |        | comment | This Mirror | will be removed | during next |
| ----------- | ------ | ------- | ----------- | --------------- | ----------- |
| maintenance | window |         |             |                 |             |
Removingthecommentfrommirrorsession3:
| switch(config-mirror-3)# |     | no comment |     |     |     |
| ------------------------ | --- | ---------- | --- | --- | --- |
Addingacommenttoamirrorendpoint:
switch(config-mirror-endpoint-test)# comment Monitor endpoint traffic
Replacingtheexistingcommentformirrorendpoint:
switch(config-mirror-endpoint-test)# comment Monitor statistics on each endpoint
interfaces
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
|     | config-mirror-endpoint |     |     | executionrightsforthiscommand. |     |
| --- | ---------------------- | --- | --- | ------------------------------ | --- |
copy tcpdump-pcap
| copy tcpdump-pcap | <FILE-NAME> | <REMOTE-URL> |     |     |     |
| ----------------- | ----------- | ------------ | --- | --- | --- |
Description
Savespacketcapturefilestoexternalstorage.
| Parameter   |     |     | Description                          |     |     |
| ----------- | --- | --- | ------------------------------------ | --- | --- |
| <FILE-NAME> |     |     | Specifiesthepacketcapturefiletosave. |     |     |
<REMOTE-URL> Specifiestheexternalstoragetowhichthepacketcapturefilewill
besaved.
Usage
Onlyfourfilescanbesavedatanypointontheswitch.Packetcapturefilesarenotsavedafterafailover
| orreboot.Viewalistofsavedfilesusingdiag |     |     | utilities | list-files. |     |
| --------------------------------------- | --- | --- | --------- | ----------- | --- |
Mirroring|59

Examples
Savingmy_capture_file.pcaptosftp://root@10.0.0.2/file.pcap:
switch#
copy tcpdump-pcap my_capture_file.pcap sftp://root@10.0.0.2/file.pcap
| root@10.0.0.2's      | passowrd:            |         |                    |      |               |       |
| -------------------- | -------------------- | ------- | ------------------ | ---- | ------------- | ----- |
| Connected            | to 10.0.0.2.         |         |                    |      |               |       |
| sftp > put           | my_capture_file.pcap |         | file.pcap          |      |               |       |
| Uploading            | my_capture_file.pcap |         | to /root/file.pcap |      |               |       |
| my_capture_file.pcap |                      |         |                    | 100% | 156 219.8KB/s | 00:00 |
| Copied               | successfuly.         |         |                    |      |               |       |
| Command              | History              |         |                    |      |               |       |
| Release              |                      |         | Modification       |      |               |       |
| 10.08                |                      |         | Commandintroduced  |      |               |       |
| Command              | Information          |         |                    |      |               |       |
| Platforms            | Command              | context | Authority          |      |               |       |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |     |     |     |
| ---- | --- | --- | --------------------- | --- | --- | --- |
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
| Command         | History          |                                |     |          |           |       |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 60

| Release             |         |         |     | Modification |
| ------------------- | ------- | ------- | --- | ------------ |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400           |     |     |     | rightsforthiscommand. |
| -------------- | --- | --- | --- | --------------------- |
| destination    | cpu |     |     |                       |
| destination    | cpu |     |     |                       |
| no destination | cpu |     |     |                       |
Description
ThecommandcausesthemirrorsessiontotransmitmirroredpacketstotheswitchCPU.This
destinationmaybeconfiguredformultiplesessions,howeveronlyonesuchconfiguredsessionmaybe
activeatagiventime.
ThediagnosticutilityTsharkmaybeusedtoviewandcapturepacketstransmittedtotheCPUthrough
thisroute.Ctrl+CmustbeenteredtoterminateaTsharkcapturesession.Moredetailscanbefoundin
theSupportabilityGuide.
ThenoformofthiscommandwillimmediatelystopsmirroringtraffictotheCPU,butwillnotremove
anysourcesfromthemirrorconfiguration.
Examples
ConfiguringamirrorsessionwithCPUasthedestination.
| switch# config           |        |             |     |     |
| ------------------------ | ------ | ----------- | --- | --- |
| switch(config)#          | mirror | session     | 1   |     |
| switch(config-mirror-1)# |        | destination |     | cpu |
Removingthedestinationentirely.
| switch(config-mirror-1)# |         | no      | destination | cpu          |
| ------------------------ | ------- | ------- | ----------- | ------------ |
| Command History          |         |         |             |              |
| Release                  |         |         |             | Modification |
| 10.07orearlier           |         |         |             | --           |
| Command Information      |         |         |             |              |
| Platforms                | Command | context |             | Authority    |
6300 config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
6400
Mirroring|61

| destination    | interface |     |                             |     |     |     |     |
| -------------- | --------- | --- | --------------------------- | --- | --- | --- | --- |
| destination    | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |     |     |     |
| no destination | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |     |     |     |
Description
Configuresthespecifiedinterfaceasthedestinationofthemirroredtraffic.
Thenoformofthiscommandimmediatelydisablesthemirroringsessionandremovesthespecified
destinationinterfacefromtheconfiguration.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID>
Specifiesainterface.Format:member/slot/port.
| <LAG-NAME> |     |     |     |     | SpecifiesaLAG(linkaggregationgroup)identifier. |     |     |
| ---------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- |
Usage
Configuringadifferentdestinationinterfaceinanenabledmirroringsessioncausesallmirroredtraffic
tousethenewdestinationinterface.Thisactionmightcauseatemporarysuspensionofmirrored
sourcetrafficduringthereconfiguration.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringamirroringsessionandaddinganinterfaceasadestination:
| switch(config)#          |     | mirror | session     | 1   |           |     |       |
| ------------------------ | --- | ------ | ----------- | --- | --------- | --- | ----- |
| switch(config-mirror-1)# |     |        | destination |     | interface |     | 1/1/1 |
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
config-mirror-<SESSION-ID>
| Allplatforms |     |     |     |     |     | Administratorsorlocalusergroupmemberswith |     |
| ------------ | --- | --- | --- | --- | --- | ----------------------------------------- | --- |
executionrightsforthiscommand.
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 62

| destination       | tunnel               |                           |
| ----------------- | -------------------- | ------------------------- |
| destination       | tunnel <TUNNEL-IPV4> | source <SOURCE-IPv4-ADDR> |
| dscp <DSCP-VALUE> | vrf <VRF-NAME>       |                           |
| no destination    | tunnel               |                           |
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
| Parameter |     | Description |
| --------- | --- | ----------- |
<TUNNEL-IPV4-ADDR> SpecifiesthetunneladdressinIPv4format(x.x.x.x),wherexis
adecimalnumberfrom0to255.
<SOURCE-IPv4-ADDR> SpecifiesthesourceaddressinIPv4format(x.x.x.x),wherexis
adecimalnumberfrom0to255.
<DSCP-VALUE> SpecifiestheDSCPvaluetobecarriedwithintheDSfieldof
ERSPANpacketheader.Range:0to63.Default:0.
| <VRF-NAME> |     | SpecifiesaVRFname.Default:default. |
| ---------- | --- | ---------------------------------- |
Examples
CreatingaMirrorSessionandaddingtunneldestination,source,dscp,andVRF:
| switch#         | config         |     |
| --------------- | -------------- | --- |
| switch(config)# | mirror session | 1   |
switch(config-mirror-1)# destination tunnel 1.1.1.1 source 2.2.2.2 dscp 10 vrf
default
Replacingtheexistingtunneldestination:
switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 10 vrf
default
ReplacingtheexistingdestinationwithadifferentDSCPvalue:
Mirroring|63

switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 2 vrf
default
ReplacingtheexistingdestinationwithadifferentVRF:
switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 2 vrf
newvrf
Removingthedestination:
| switch(config-mirror-1)# |         | no destination | tunnel    |
| ------------------------ | ------- | -------------- | --------- |
| Command History          |         |                |           |
| Release                  |         | Modification   |           |
| 10.07orearlier           |         | --             |           |
| Command Information      |         |                |           |
| Platforms                | Command | context        | Authority |
6300 config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
| 6400 |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | ------------------------------ |
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
Sincefileanddelete-fileareoptional,thebehaviorofthebasecommanddiag utilities tshark
doesnotsaveanythingtoafile,andinsteaddumpsthetsharksessiontotheconsoleuntilCTRL + cis
entered.
| Parameter   |     | Description                           |     |
| ----------- | --- | ------------------------------------- | --- |
| file        |     | Savescapturedpacketstoatemporaryfile. |     |
| delete-file |     | Deletesthemostrecentcapturedfile.     |     |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 64

Example
Performingdiagnostic:
switch#
diagnostic
| switch#        | diagnostic  | utilities   | tshark       | file         |            |
| -------------- | ----------- | ----------- | ------------ | ------------ | ---------- |
| Inspecting     | traffic     | mirrored    | to the CPU   | until Ctrl-C | is entered |
| ^CEnding       | traffic     | inspection. |              |              |            |
| Command        | History     |             |              |              |            |
| Release        |             |             | Modification |              |            |
| 10.07orearlier |             |             | --           |              |            |
| Command        | Information |             |              |              |            |
| Platforms      | Command     | context     | Authority    |              |            |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
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
| delete file | <FILE-NAME> |     |     |     |     |
| ----------- | ----------- | --- | --- | --- | --- |
Deletesspecifiedtcpdumplistfiles.
| list-files |     |     | Listsallthetcpdumpcapturefilessavedonthedevice. |     |     |
| ---------- | --- | --- | ----------------------------------------------- | --- | --- |
vrf <VRF-NAME>
CapturespacketsonthespecifiedVRF.IfnoVRF isnamed,the
defaultisused.
count <COUNT-NUM> Runsthetcpdumpcommanduntilthespecifiednumberof
packetsarecaptured.Range: 1-2147483647.
proto <PROTO-NUM> CapturespacketsofaparticulartypebasedonIPprotocol
number.Range: 0-255.
host-ip <IP-ADDR> CapturespacketsmatchingwiththesourceordestinationIP
address.
source-ip <IP-ADDR> CapturespacketsfromthespecifiedIPaddress.
Mirroring|65

Parameter

Description

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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

66

| switch# | diag utilities | tcpdump | list-files |     |     |
| ------- | -------------- | ------- | ---------- | --- | --- |
my_capture_file.pcap
Readingmy_capture_file.pcap:
| switch# | diag utilities | tcpdump | command | -r my_capture_file.pcap |     |
| ------- | -------------- | ------- | ------- | ----------------------- | --- |
reading from file /tmp/tcpdump/my_capture_file1.pcap, link-type EN10MB (Ethernet)
1 11:59:34.047867 IP6 localhost.40318 > localhost.ntp: NTPv2, Reserved, length
12
0x0000: 0000 0304 0006 0000 0000 0000 0000 86dd ................
0x0010: 600a 7e47 0014 1140 0000 0000 0000 0000 `.~G...@........
0x0020: 0000 0000 0000 0001 0000 0000 0000 0000 ................
0x0030: 0000 0000 0000 0001 9d7e 007b 0014 0027 .........~.{...'
|     | 0x0040: 1601 | 0001 0000 | 0000 0000 | 0000 | ............ |
| --- | ------------ | --------- | --------- | ---- | ------------ |
2 11:59:34.047915 IP6 localhost.ntp > localhost.40318: NTPv2, Reserved, length
12
0x0000: 0000 0304 0006 0000 0000 0000 0000 86dd ................
0x0010: 6b8d 23c5 0014 1140 0000 0000 0000 0000 k.#....@........
0x0020: 0000 0000 0000 0001 0000 0000 0000 0000 ................
0x0030: 0000 0000 0000 0001 007b 9d7e 0014 0027 .........{.~...'
|     | 0x0040: d681 | 0001 c016 | 0000 0000 | 0000 |     |
| --- | ------------ | --------- | --------- | ---- | --- |
Removingmy_capture_file.pcap:
switch# diag utilities tcpdump delete-file my_capture_file.pcap
| Successfully | removed     | file    |                   |     |     |
| ------------ | ----------- | ------- | ----------------- | --- | --- |
| Command      | History     |         |                   |     |     |
| Release      |             |         | Modification      |     |     |
| 10.08        |             |         | Commandintroduced |     |     |
| Command      | Information |         |                   |     |     |
| Platforms    | Command     | context | Authority         |     |     |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6400
disable
disable
Description
Disablesthemirroringsessionspecifiedbythecurrentcommandcontext.
Usage
Bydefault,mirroringsessionsaredisabled.
Whenamirroringsessionisdisabled,theshow mirrorcommandforthatsessionIDshowsanAdmin
| StatusofdisableandanOperation |     |     | Statusofdisabled. |     |     |
| ----------------------------- | --- | --- | ----------------- | --- | --- |
Example
Mirroring|67

Disablingamirroringsession:
| switch(config)#          | mirror  | session | 3            |           |
| ------------------------ | ------- | ------- | ------------ | --------- |
| switch(config-mirror-3)# |         | disable |              |           |
| Command History          |         |         |              |           |
| Release                  |         |         | Modification |           |
| 10.07orearlier           |         |         | --           |           |
| Command Information      |         |         |              |           |
| Platforms                | Command | context |              | Authority |
config-mirror-<SESSION-ID>
| Allplatforms |     |     |     | Administratorsorlocalusergroupmemberswith |
| ------------ | --- | --- | --- | ----------------------------------------- |
executionrightsforthiscommand.
enable
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
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringandenablingamirroringsession:
| switch(config)#          | mirror | session | 3         |          |
| ------------------------ | ------ | ------- | --------- | -------- |
| switch(config-mirror-3)# |        | source  | interface | 1/1/2 rx |
switch(config-mirror-3)#
|     |     | destination | interface | 1/1/3 |
| --- | --- | ----------- | --------- | ----- |
switch(config-mirror-3)# comment Monitor router port ingress-only traffic
| switch(config-mirror-3)# |     | enable |     |     |
| ------------------------ | --- | ------ | --- | --- |
| Command History          |     |        |     |     |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 68

| Release             |         |         | Modification |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
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
| Parameter    |     |     | Description                              |     |
| ------------ | --- | --- | ---------------------------------------- | --- |
| <SESSION-ID> |     |     | Specifiesthesessionidentifier.Range:1to4 |     |
Examples
| switch(config)# | mirror | session | 1   |     |
| --------------- | ------ | ------- | --- | --- |
switch(config-mirror-1)#
| switch(config)# | mirror | session | 3   |     |
| --------------- | ------ | ------- | --- | --- |
switch(config-mirror-3)#
| switch(config)# | no  | mirror session | 1   |     |
| --------------- | --- | -------------- | --- | --- |
switch(config)#
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show mirror
Mirroring|69

show mirror [<SESSION-ID>] [vsx-peer]

Description

Shows information about mirroring sessions. If <SESSION-ID> is not specified, then the command shows
a summary of all configured mirroring sessions. If <SESSION-ID> is specified, then the command shows
detailed information about the specified mirroring session.

Parameter

<SESSION-ID>

vsx-peer

Usage

Description

Specifies the session identifier. Range: 1 to 4

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

Admin Status indicates the configured status. Admin Status is one of the following values:
enable
The mirroring session is enabled.
disable
The mirroring session has been configured but not yet enabled, or has been disabled.

Operation Status indicates the status of the mirroring session. Operation Status is one of the following
values:
dest_doesnt_exist
The configured destination interface is not found in the system. The mirroring session cannot be enabled.
destination_shutdown
The mirroring session is enabled, but the destination interface is shut down. No traffic can be monitored.
disabled
The mirroring session is disabled and is not in an error condition.
enabled
The mirroring session is enabled.
external/driver_error
An internal ASIC hardware error occurred.
hit_active_sessions_capacity
The mirroring session could not be enabled because the maximum number of supported mirroring sessions are
already enabled.
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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

70

Operation Status

switch# show mirror
ID Admin Status
--- ------------- ----------------------------------------------------
1
2
3
4

enabled
disabled
disabled
internal_error

enable
disable
disable
enable

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

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

source interface
source interface {<PORT-NUM> | <LAG-NAME>} [<DIRECTION>]
no source interface {<PORT-NUM> | <LAG-NAME>} [<DIRECTION>]

Description

Configures the specified interface (either an Ethernet port or a LAG) as a source of traffic to be mirrored.

The no form of this command ceases mirroring traffic from the specified source interface and removes
the source interface from the mirroring session configuration.

Parameter

<PORT-NUM>

<LAG-NAME>

<DIRECTION>

Description

Specifies a physical port on the switch. Use the format
member/slot/port (for example, 1/3/1).

Specifies the identifier for the LAG (link aggregation group).

Selects the direction of traffic to be mirrored from this source

Mirroring | 71

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
interface.Thereisnodefaultforthisparameter.Validvaluesare
thefollowing:
both
Mirrorbothtransmittedandreceivedpackets.
| rx  |     |     | Mirroronlyreceivedpackets. |     |     |
| --- | --- | --- | -------------------------- | --- | --- |
tx
Mirroronlytransmittedpackets.
Usage
Thereisalimitofsourceinterfacesineachdirectionofagivenmirrorsession:
| Switch | Source | interface | limit |     |     |
| ------ | ------ | --------- | ----- | --- | --- |
| 6300   | 64     |           |       |     |     |
| 6400   | 64     |           |       |     |     |
However,thereisapracticallimittotheamountoftrafficthatamirrordestinationcantransmit.For
example,mirroringsessionwithmultiple10Gsourcescanoverwhelmasingle10Gdestination.
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
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 72

Configuringasourceinterfacetomirrorreceivedpacketsonly:
| switch(config-mirror-3)# |     | source | interface | 1/1/2 rx |
| ------------------------ | --- | ------ | --------- | -------- |
Configuringasourceinterfacetomirrorbothtransmittedandreceivedpackets:
| switch(config-mirror-1)# |     | source | interface | 1/1/1 both |
| ------------------------ | --- | ------ | --------- | ---------- |
ConfiguringaLAGassourceinterfacetomirrorbothtransmittedandreceivedpackets:
switch(config-mirror-4)#
|     |     | source | interface | lag1 both |
| --- | --- | ------ | --------- | --------- |
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
Mirroring|73

Chapter 9
|            |          |            | Monitoring | a device | using SNMP |
| ---------- | -------- | ---------- | ---------- | -------- | ---------- |
| Monitoring | a device | using SNMP |            |          |            |
Configuring SNMP:RefertotheSNMP/MIBGuideforinformationonhowtoaddSNMPsoadevicecan
bemonitoredfromanetworkmanagementsystem(NMS).
Configuring an SNMP trap receiver:RefertotheSNMP/MIBGuideandspecificinformationaboutthe
| show snmp | trapcommandtoenableSNMPtraps. |     |     |     |     |
| --------- | ----------------------------- | --- | --- | --- | --- |
74
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries)

Chapter 10

Power-over-Ethernet

Power-over-Ethernet

n The Power-over-Ethernet (PoE) subsystem manages power supplied to devices using standard
Ethernet data cables. A Power Sourcing Equipment (PSE) supplies DC power as well as Ethernet
connectivity to a Powered Device (PD) using a standard Ethernet cable. The maximum current
depends on the PD Requested Class.

n A PoE subsystem contains two parts : a PSE and PD. A Power Sourcing Equipment (PSE) is a device
that provides power through a standard Ethernet cable. A PoE capable switch functions as PSE. All
Aruba PoE switches are considered as PSEs. A PD is a device powered by a PSE. Examples of PD are
VoIP phones, Wireless APs, and IP cameras.

n When a PD or any network cable is connected to a PSE port, the PSE applies a detection voltage and
measures the resistance value of the PD. If resistance is within IEEE 802.3 standard values (23 - 26k
ohm), the connected device is treated as PD and classification begins. For legacy devices to be
detected, you must enable prestandard detection on the switch.

n PDs are divided into different types and classes based on PD power requirements. The power

supplied by the PSE is higher than the power PD draws to accommodate for the line losses that can
result with the use of the standard maximum length cable(100m).

o Type 1: PSE can supply maximum of 15.4W, and PD can draw a maximum of 13W.

o Type 2: PSE can supply maximum of 30W, and PD can draw a maximum of 25.5W.

o Type 3: PSE can supply maximum of 60W, and PD can draw a maximum of 51W.

o Type 4: PSE can supply maximum of 90W, and PD can draw a maximum of 71W.

n Classes of PD:

o Class 0: Type1 PD, it can draw a maximum of 13W.

o Class 1: Type1 PD, it can draw a maximum of 3.84W.

o Class 2: Type1 PD, it can draw a maximum of 6.49W.

o Class 3: Type1 PD, it can draw a maximum of 13W.

o Class 4: Type2 PD, it can draw a maximum of 25.5W.

o Class 5: Type3 PD, it can draw a maximum of 40W.

o Class 6: Type3 PD, it can draw a maximum of 51W.

o Class 7: Type4 PD, it can draw a maximum of 62W.

o Class 8: Type4 PD, it can draw a maximum of 71.3W.

n IEEE 802.3bt introduced 4-Pair PoE as a means of supplying higher power to PDs that need more than
the current 25.5W supplied by IEEE 802.3at. To increase the available power without damaging the
Ethernet cable, the standard introduced the ability to use all four pairs within the Ethernet cable
instead of the two pairs used by previous standards (802.3at, 802.3af).

n Supported protocols:

o Compatibility with IEEE 802.3af, 802.3at, 802.3bt and prestandard.

o Long first class event supported on Type 3-4 PSE.

o Support for Single Signature (SS) Type 0-6 and Dual Signature (DS) Type 0-4 PDs.

o Multi-Event classification permits mutual ID of SS Class 0-6 and DS Class 0-4.

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

75

o Support LLDP Data Link Layer (DLL) Type 1-2 extension 12-octet TLV and Type 3-4 extension 29-

octet TLV.

o Default PSE assigned class delivers the maximum PSE capable power at initial power up based on

PD requested class.

n Always-on PoE is a feature that provides the ability for a switch to continue to provide power across
user initiated reboots through software. Always-on PoE is enabled by default and no additional
configuration is needed.

PDs only remain powered, no data transfer or PoE power negotiation can occur until the switch has completely

booted up and in normal operation. PD faults occurring prior to full switch boot up will result in PoE power

removal and restart the detection process only after switch returns to normal operation.

PoE commands

All PoE configuration commands except threshold configuration and always-on poe configuration
are entered at the config-if context. The PoE threshold command is used at the system level whereas
the always-on poeand power-over-ethernet quick-poe commands are set at the slot level. These
commands can only be configured in the global configuration context.

lldp dot3 poe
lldp dot3 poe
no lldp dot3 poe

Description

Enables 802.3 TLV list in LLDP to advertise for Power over Ethernet Data Link Layer Classification. LLDP
dot3 TLV is by default enabled for PoE.

The no form of this command disables 802.3 TLV list in LLDP.

Examples

On the 6400 Switch Series, interface identification differs.

Enabling 802.3 TLV list in LLDP:

switch(config)# interface 1/1/1
switch(config-if)# lldp dot3 poe

Disabling 802.3 TLV list in LLDP:

switch(config-if)# no lldp dot3 poe

Command History

Release

10.07 or earlier

Command Information

Modification

--

Power-over-Ethernet | 76

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400         |                         |     |     | rightsforthiscommand. |
| ------------ | ----------------------- | --- | --- | --------------------- |
| lldp med     | poe                     |     |     |                       |
| lldp med poe | [priority-override]     |     |     |                       |
| no lldp med  | poe [priority-override] |     |     |                       |
Description
EnablesMEDTLVlistinLLDPtoadvertiseforPoweroverEthernetDataLinkLayerClassification.Also
enablesthelldp-MEDTLVprioritytooverrideuserconfiguredportpriorityforPoweroverEthernet.
Whenbothdot3andMEDareenabled,dot3willtakeprecedence.MEDTLVisbydefaultenabledfor
PoE.Priorityover-rideisbydefaultdisabled.
ThenoformofthiscommanddisablesMEDTLVlistinLLDP.
| Parameter           |     |     |     | Description                      |
| ------------------- | --- | --- | --- | -------------------------------- |
| [priority-override] |     |     |     | Systemdefinednameoftheinterface. |
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablinganddisablingLLDPMEDPoE:
| switch(config)#    |     | interface | 1/1/1 |     |
| ------------------ | --- | --------- | ----- | --- |
| switch(config-if)# |     | lldp      | med   | poe |
| switch(config-if)# |     | no lldp   | med   | poe |
EnablinganddisablingLLDPMEDPoEpriorityoverride:
| switch(config-if)#  |         | lldp    | med | poe priority-override |
| ------------------- | ------- | ------- | --- | --------------------- |
| Command History     |         |         |     |                       |
| Release             |         |         |     | Modification          |
| 10.07orearlier      |         |         |     | --                    |
| Command Information |         |         |     |                       |
| Platforms           | Command | context |     | Authority             |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --------------------- |
power-over-ethernet
power-over-ethernet
no power-over-ethernet
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 77

Description
Enablesper-interfacepowerdistribution.Per-portpowerisenabledbydefaultwithprioritylow.PoE
cannotbedisabledforindividualportswhenQuickPoEisenabledfortheentireswitchorlinemodule.
Thenoformofthiscommanddisablesper-interfacepowerdistribution.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
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
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400                   |     |             |             |             | rightsforthiscommand. |          |        |     |
| ---------------------- | --- | ----------- | ----------- | ----------- | --------------------- | -------- | ------ | --- |
| power-over-ethernet    |     |             |             | allocate-by |                       |          |        |     |
| power-over-ethernet    |     | allocate-by |             |             | {usage                | | class} |        |     |
| no power-over-ethernet |     |             | allocate-by |             | {usage                | |        | class} |     |
Description
Configuresthepowerallocationmethod.Powerallocationmethodisinitiallybasedonusage.PSE
AllocatedpowervaluewillchangetoLLDPnegotiatedpowerifandwhenLLDPexchangetakesplace
betweenPSEandPD.WhenthereisnoLLDPnegotiation,PSEAllocatedPowerValuewillbetheactual
instantaneouspowerdrawandreservepowerbasedonactualconsumption.Inallocate-byclass,power
allocationisbasedonPDrequestedclassandPSEallocatedpowervaluewillbetheLLDPnegotiated
powerwhenLLDPexchangetakesplacebetweenPSEandPD.WhenthereisnoLLDPnegotiation,PSE
AllocatePowerwillbebasedonPDclass.ReservepowerisbasedonPDClass.Bydefault,power
allocationisbyusage.
Power-over-Ethernet|78

Thenoformofthiscommandresetstheactiontodefault.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringthepowerallocationmethod:
| switch(config)#    |     | interface |                     | 1/1/1 |     |             |       |
| ------------------ | --- | --------- | ------------------- | ----- | --- | ----------- | ----- |
| switch(config-if)# |     |           | power-over-ethernet |       |     | allocate-by | usage |
| switch(config-if)# |     |           | power-over-ethernet |       |     | allocate-by | class |
Resettingpowerallocationmethod:
| switch(config-if)#  |         |     | no power-over-ethernet |     |              | allocate-by | class |
| ------------------- | ------- | --- | ---------------------- | --- | ------------ | ----------- | ----- |
| Command History     |         |     |                        |     |              |             |       |
| Release             |         |     |                        |     | Modification |             |       |
| 10.07orearlier      |         |     |                        |     | --           |             |       |
| Command Information |         |     |                        |     |              |             |       |
| Platforms           | Command |     | context                |     | Authority    |             |       |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400                   |     |           |           |             | rightsforthiscommand. |     |     |
| ---------------------- | --- | --------- | --------- | ----------- | --------------------- | --- | --- |
| power-over-ethernet    |     |           | always-on |             |                       |     |     |
| power-over-ethernet    |     | always-on |           | <MODULE-ID> |                       |     |     |
| no power-over-ethernet |     |           | always-on | <MODULE-ID> |                       |     |     |
Description
Always-onPoEisafeaturethatprovidestheabilitytotheswitchtocontinuetoprovidepoweracrossa
softreboot.Itisapplicableonlytotheinterfaceswhichwereconnectedanddeliveringbeforethesoft
reboot.Also,powerwillnotbedeliveredifpowertotheswitchisinterrupted.Thiscommandenablesor
disablesthealways-onPoEfeatureattheswitchortheslotlevel.Bydefault,always-onPoEisenabledat
theswitchortheslotlevel.
Thenoformofthiscommanddisablespowerdistributiononsoftreboot.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<MODULE-ID>
Modulenumbertoapplyalways-onPoEconfiguration.
Examples
Enablingper-interfacepowerdistribution:
| switch(config)# |     | power-over-ethernet |     |     | always-on | 1/1 |     |
| --------------- | --- | ------------------- | --- | --- | --------- | --- | --- |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 79

Disablingper-interfacepowerdistribution:
| switch(config)#     |         | no  | power-over-ethernet |              | always-on |     | 1/1 |     |
| ------------------- | ------- | --- | ------------------- | ------------ | --------- | --- | --- | --- |
| Command History     |         |     |                     |              |           |     |     |     |
| Release             |         |     |                     | Modification |           |     |     |     |
| 10.07orearlier      |         |     |                     | --           |           |     |     |     |
| Command Information |         |     |                     |              |           |     |     |     |
| Platforms           | Command |     | context             | Authority    |           |     |     |     |
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400                   |     |                |                | rightsforthiscommand. |        |     |     |     |
| ---------------------- | --- | -------------- | -------------- | --------------------- | ------ | --- | --- | --- |
| power-over-ethernet    |     |                | assigned-class |                       |        |     |     |     |
| power-over-ethernet    |     | assigned-class |                | {3 |                  | 4 | 6} |     |     |     |
| no power-over-ethernet |     |                | assigned-class |                       |        |     |     |     |
Description
LimitPoEpowerbasedontheassignedclass.Whenanuserassignsamaximumclasstoaninterface,
thePSEwilllimitthemaximumpowerdeliveredtothePDuptoatotalpowerdrawnotexceedingthe
PSEassigned-classpower.PowerdemotionoccurswhenaPDrequestedclassishigherthanthePSE
assignedclass,permittingthePDtoreceivepowerandoperateinareducedpowermode.PoEports
cannotsetanassignedclasswhenQuickPoEisenabledonthesybsystem.Thedefaultassignedclassis
4for2-paircapablePSEand6for4-paircapablePSE.
Thenoformofthiscommandresetstheactiontodefault.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
SettingPoEassignedclass:
| switch(config)#    |     | interface | 1/1/1               |     |                |     |     |     |
| ------------------ | --- | --------- | ------------------- | --- | -------------- | --- | --- | --- |
| switch(config-if)# |     |           | power-over-ethernet |     | assigned-class |     |     | 4   |
ResettingPoEassignedclasstodefault:
| switch(config-if)# |     |     | no power-over-ethernet |     | assigned-class |     |     | 4   |
| ------------------ | --- | --- | ---------------------- | --- | -------------- | --- | --- | --- |
ShowingQuickPoEenabled:
switch(config)#
|                 |     | power-over-ethernet |       |     | quick-poe      | 1/1 |     |     |
| --------------- | --- | ------------------- | ----- | --- | -------------- | --- | --- | --- |
| switch(config)# |     | interface           | 1/1/1 |     |                |     |     |     |
| switch(config)# |     | power-over-ethernet |       |     | assigned-class |     | 4   |     |
Interface assigned class cannot be configured when Quick PoE is enabled.
| Command History |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Power-over-Ethernet|80

| Release             |         |     |         |     | Modification |     |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- | --- |
| 10.07orearlier      |         |     |         |     | --           |     |     |
| Command Information |         |     |         |     |              |     |     |
| Platforms           | Command |     | context |     | Authority    |     |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400                   |     |             |             |        | rightsforthiscommand. |                    |     |
| ---------------------- | --- | ----------- | ----------- | ------ | --------------------- | ------------------ | --- |
| power-over-ethernet    |     |             | power-pairs |        |                       |                    |     |
| power-over-ethernet    |     | power-pairs |             | {alt-a |                       | | alt-a-and-alt-b} |     |
| no power-over-ethernet |     |             | power-pairs |        | {alt-a                | | alt-a-and-alt-b} |     |
Description
Configuresthefour-paircapableswitchtooperateinamode,thatrestrictsthepowerdeliveryforclass
0toclass4singlesignaturedevicestooperateonlyonALT-Apowerpair.
Whenconfigured,awarningmessageisdisplayed.UsermustacceptthewarningbyenteringYtoenablethe
mode.
ThenoformofthiscommandresetsthepowerpairstodefaultPoEpairs.
| Parameter |     |     |     |     | Description                      |     |     |
| --------- | --- | --- | --- | --- | -------------------------------- | --- | --- |
| alt-a     |     |     |     |     | DeliverspoweronlyontheALT-Apair. |     |     |
alt-a-and-alt-b
DeliverspowerontheALT-AandALT-Bpairs.Thisisthedefault
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
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 81

| switch(config-if)# |     | no power-over-ethernet | power-pairs | alt-a |
| ------------------ | --- | ---------------------- | ----------- | ----- |
This setting configures the interface to deliver power on the ALT-A
and ALT-B cable pairs. This is the default and most devices work
properly with this setting, however some older Class 0-4 devices may
| not operate         | correctly. |         |                   |     |
| ------------------- | ---------- | ------- | ----------------- | --- |
| Continue            | (y/n)? y   |         |                   |     |
| Command History     |            |         |                   |     |
| Release             |            |         | Modification      |     |
| 10.09               |            |         | CommandIntroduced |     |
| Command Information |            |         |                   |     |
| Platforms           | Command    | context | Authority         |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400                   |                |                | rightsforthiscommand. |     |
| ---------------------- | -------------- | -------------- | --------------------- | --- |
| power-over-ethernet    |                | pre-std-detect |                       |     |
| power-over-ethernet    | pre-std-detect |                |                       |     |
| no power-over-ethernet |                | pre-std-detect |                       |     |
Description
BeforeIEEE802.3releasedthefirstPoweroverEthernetstandard(802.3af),vendorshadshippedPoE
capableswitchesandPD's.AswearebackwardcompatibleArubawillsupportbothIEEEstandardand
pre-standard802.3afPoweroverEthernetPD'sconcurrently.ThisCLIallowstheusertoenableor
disablepre-802.3af-standarddevicedetectionandpoweringonthespecificport.Whenpre-std-detectis
enabled,powerwillbedeliveredonPairAonly.Defaultisdisabled.
Thenoformofthiscommandresetstheactiontodefault.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Enablingstandarddevicedetection:
| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)#
|     |     | power-over-ethernet | pre-std-detect |     |
| --- | --- | ------------------- | -------------- | --- |
Disablingstandarddevicedetection:
| switch(config-if)# |     | no power-over-ethernet | pre-std-detect |     |
| ------------------ | --- | ---------------------- | -------------- | --- |
| Command History    |     |                        |                |     |
Power-over-Ethernet|82

| Release             |         |     |         | Modification |     |
| ------------------- | ------- | --- | ------- | ------------ | --- |
| 10.07orearlier      |         |     |         | --           |     |
| Command Information |         |     |         |              |     |
| Platforms           | Command |     | context | Authority    |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400                   |     |          |                    | rightsforthiscommand. |               |
| ---------------------- | --- | -------- | ------------------ | --------------------- | ------------- |
| power-over-ethernet    |     |          | priority           |                       |               |
| power-over-ethernet    |     | priority | {critical          |                       | | high | low} |
| no power-over-ethernet |     |          | priority {critical |                       | | high | low} |
Description
SetsPoEpriorityforaninterfaceSpecifyingcritical,high,orlowindicatesthepriorityoftheinterfacein
theeventofpowerover-subscription.Withinthesameprioritylevel,higherpower-priorityline-module
portshavehigherprecedence.WithsamePoEpriorityandsameline-modulepriority,lowernumbered
line-moduleportshavehigherprecedence.Per-interfacePoEpriorityislowbydefault.
ThenoformofthiscommandresetstheprioritytodefaultPoEpriority"low".
Examples
ConfiguringPoEpriority:
| switch(config)#    |     | interface | 1/1/1               |     |                   |
| ------------------ | --- | --------- | ------------------- | --- | ----------------- |
| switch(config-if)# |     |           | power-over-ethernet |     | priority critical |
| switch(config-if)# |     |           | power-over-ethernet |     | priority high     |
ResettingthePoEprioritytodefault:
| switch(config-if)#  |         |     | no power-over-ethernet |              | priority high |
| ------------------- | ------- | --- | ---------------------- | ------------ | ------------- |
| Command History     |         |     |                        |              |               |
| Release             |         |     |                        | Modification |               |
| 10.07orearlier      |         |     |                        | --           |               |
| Command Information |         |     |                        |              |               |
| Platforms           | Command |     | context                | Authority    |               |
config-if
| 6300                |     |           |             | Administratorsorlocalusergroupmemberswithexecution |     |
| ------------------- | --- | --------- | ----------- | -------------------------------------------------- | --- |
| 6400                |     |           |             | rightsforthiscommand.                              |     |
| power-over-ethernet |     |           | quick-poe   |                                                    |     |
| power-over-ethernet |     | quick-poe | <MODULE-ID> |                                                    |     |
no power-over-ethernet
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 83

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
| Parameter   |     |     |     |     | Description                                    |     |
| ----------- | --- | --- | --- | --- | ---------------------------------------------- | --- |
| <MODULE-ID> |     |     |     |     | SpecifiesmodulenumberforquickPoEconfiguration. |     |
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablinganddisablingquickPoE:
| switch(config)#    |     | power-over-ethernet |                     |     | quick-poe | 1/2 |
| ------------------ | --- | ------------------- | ------------------- | --- | --------- | --- |
| switch(config)#    |     | no                  | power-over-ethernet |     | quick-poe | 1/2 |
| switch(config-if)# |     |                     | power-over-ethernet |     | quick-poe | 1/1 |
PoE must be enabled on all interfaces before enabling Quick PoE
| switch(config-if)# |     |     | power-over-ethernet |     | quick-poe | 1/3 |
| ------------------ | --- | --- | ------------------- | --- | --------- | --- |
All interfaces must use the default assigned class before enabling Quick PoE
| Command History     |         |     |         |     |              |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- |
| Release             |         |     |         |     | Modification |     |
| 10.07orearlier      |         |     |         |     | --           |     |
| Command Information |         |     |         |     |              |     |
| Platforms           | Command |     | context |     | Authority    |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400                   |     |           |           |              | rightsforthiscommand. |     |
| ---------------------- | --- | --------- | --------- | ------------ | --------------------- | --- |
| power-over-ethernet    |     |           | threshold |              |                       |     |
| power-over-ethernet    |     | threshold |           | <PERCENTAGE> |                       |     |
| no power-over-ethernet |     |           | threshold | <PERCENTAGE> |                       |     |
Description
Power-over-Ethernet|84

Setsthethresholdatwhichthesystemwillsendanexcesspowerconsumptionnotificationtrap.Default
valueis80percentage.
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
config
| 6300                   |     |      | Administratorsorlocalusergroupmemberswithexecution |     |     |
| ---------------------- | --- | ---- | -------------------------------------------------- | --- | --- |
| 6400                   |     |      | rightsforthiscommand.                              |     |     |
| power-over-ethernet    |     | trap |                                                    |     |     |
| power-over-ethernet    |     | trap |                                                    |     |     |
| no power-over-ethernet |     | trap |                                                    |     |     |
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
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 85

| Command        | History     |         |         |     |              |
| -------------- | ----------- | ------- | ------- | --- | ------------ |
| Release        |             |         |         |     | Modification |
| 10.07orearlier |             |         |         |     | --           |
| Command        | Information |         |         |     |              |
| Platforms      |             | Command | context |     | Authority    |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400      |              |       |                  |     | rightsforthiscommand. |
| --------- | ------------ | ----- | ---------------- | --- | --------------------- |
| show      | lldp         | local |                  |     |                       |
| show lldp | local-device |       | [<INTERFACE-ID>] |     |                       |
Description
DisplaysinformationadvertisedbytheswitchiftheLLDPfeatureisenabledbyuser.
| Parameter      |     |     |     |     | Description                                  |
| -------------- | --- | --- | --- | --- | -------------------------------------------- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port |
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingLLDPlocaldevice:
| switch# | show | lldp | local-device |     | 1/1/10 |
| ------- | ---- | ---- | ------------ | --- | ------ |
| Local   | Port | Data |              |     |        |
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
Power-over-Ethernet|86

| Platforms | Command |     | context | Authority |     |
| --------- | ------- | --- | ------- | --------- | --- |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp          | neighbor |                  |     |     |     |
| ------------------ | -------- | ---------------- | --- | --- | --- |
| show lldp neighbor |          | [<INTERFACE-ID>] |     |     |     |
Description
Displaysdetailedinformationaboutaparticularneighborconnectedtoaparticularinterface.
| Parameter      |     |     |     | Description                                  |     |
| -------------- | --- | --- | --- | -------------------------------------------- | --- |
| <INTERFACE-ID> |     |     |     | Specifiesaninterface.Format:member/slot/port |     |
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingLLDPneighborinformationwhenthereisonlyoneneighbor:
| switch# show | lldp         | neighbor-info |     | 1/1/10              |     |
| ------------ | ------------ | ------------- | --- | ------------------- | --- |
| Port         |              |               |     | : 1/1/10            |     |
| Neighbor     | Entries      |               |     | : 1                 |     |
| Neighbor     | Entries      | Deleted       |     | : 0                 |     |
| Neighbor     | Entries      | Dropped       |     | : 0                 |     |
| Neighbor     | Entries      | Aged-Out      |     | : 0                 |     |
| Neighbor     | Chassis-Name |               |     | : 84:d4:7e:ce:5d:68 |     |
Neighbor Chassis-Description : ArubaOS (MODEL: 325), Version Aruba IAP
| Neighbor             | Chassis-ID         |             |           | : 84:d4:7e:ce:5d:68 |      |
| -------------------- | ------------------ | ----------- | --------- | ------------------- | ---- |
| Neighbor             | Management-Address |             |           | : 169.254.41.250    |      |
| Chassis Capabilities |                    |             | Available | : Bridge,           | WLAN |
| Chassis Capabilities |                    |             | Enabled   | :                   |      |
| Neighbor             | Port-ID            |             |           | : 84:d4:7e:ce:5d:68 |      |
| Neighbor             | Port-Desc          |             |           | : eth0              |      |
| TTL                  |                    |             |           | : 120               |      |
| Neighbor             | Port               | VLAN        | ID        | :                   |      |
| Neighbor             | PoEplus            | information |           | : DOT3              |      |
| Neighbor             | Device             | Type        |           | : TYPE2             | PD   |
| Neighbor             | Power              | Priority    |           | : Unkown            |      |
| Neighbor             | Power              | Source      |           | : Primary           |      |
| Neighbor             | Power              | Requested   |           | : 25.0              | W    |
| Neighbor             | Power              | Allocated   |           | : 0.0 W             |      |
| Neighbor             | Power              | Supported   |           | : No                |      |
| Neighbor             | Power              | Enabled     |           | : No                |      |
| Neighbor             | Power              | Class       |           | : 5                 |      |
| Neighbor             | Power              | Paircontrol |           | : No                |      |
| Neighbor             | Power              | Pairs       |           | : SIGNAL            |      |
| Command History      |                    |             |           |                     |      |
| Release              |                    |             |           | Modification        |      |
| 10.07orearlier       |                    |             |           | --                  |      |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 87

| Command   | Information |         |     |         |           |     |
| --------- | ----------- | ------- | --- | ------- | --------- | --- |
| Platforms |             | Command |     | context | Authority |     |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show | power-over-ethernet |     |     |     |     |     |
| ---- | ------------------- | --- | --- | --- | --- | --- |
6300SwitchSeries:
| show | power-over-ethernet |     |     | [member | <MEMBER-ID>] | [brief] |
| ---- | ------------------- | --- | --- | ------- | ------------ | ------- |
6400SwitchSeries:
| show | power-over-ethernet |     |     | [<MODULE-ID>] | [brief] |     |
| ---- | ------------------- | --- | --- | ------------- | ------- | --- |
6300,6400SwitchSeries:
| show | power-over-ethernet |     |     | [<IFRANGE>] | [brief] |     |
| ---- | ------------------- | --- | --- | ----------- | ------- | --- |
Description
Displaysthestatusinformationofthefullsystem.Displaysthebriefstatusofallportorgivenportif
parameterbriefisused.Displaysthedetailedstatusofgivenport.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<MODULE-ID>
Displaysdetailedstatusforthegivenmodule.
| <IFRANGE> |     |     |     |     | Portidentifierrange. |     |
| --------- | --- | --- | --- | --- | -------------------- | --- |
<IFNAME>
Displaythedetailedstatusofgivenport.
| brief |     |     |     |     | Displaythebriefstatusofallportsorthegivenport. |     |
| ----- | --- | --- | --- | --- | ---------------------------------------------- | --- |
Examples
Showingsampleoutputforshowpower-over-ethernetonstandaloneboxwithVSFcapabiity:
|     | switch# show     | power-over-ethernet |          |            |                 |        |
| --- | ---------------- | ------------------- | -------- | ---------- | --------------- | ------ |
|     | System Power     | Status              |          | for member | 1               |        |
|     | Configured       |                     | Power    | Status     | : No redundancy |        |
|     | Operational      |                     | Power    | Status     | : No redundancy |        |
|     | Total Available  |                     | Power    |            | : 740 W         |        |
|     | Total Failover   |                     | Pwr      | Avl        | : 0 W           |        |
|     | Total Redundancy |                     |          | Power      | : 0 W           |        |
|     | Total Power      |                     | Drawn    |            | : 0 W           | +/- 6W |
|     | Total Power      |                     | Reserved |            | : 0 W           |        |
|     | Total Remaining  |                     | Power    |            | : 740 W         |        |
|     | Trap Threshold   |                     |          |            | : 80 %          |        |
|     | Trap Enabled     |                     |          |            | : Yes           |        |
|     | Always-on        | PoE                 | Enabled  |            | : 1/1           |        |
|     | Quick PoE        | Enabled             |          |            | : None          |        |
|     | Internal         | Power               |          |            |                 |        |
|     | Total            |                     | Power    |            |                 |        |
|     | PS (Watts)       |                     |          | Status     |                 |        |
Power-over-Ethernet|88

| -----          | ------------- |              | --------------------- |        |            |     |
| -------------- | ------------- | ------------ | --------------------- | ------ | ---------- | --- |
| 1              | 0             |              | Absent                |        |            |     |
| 2              | 740           |              | Ok                    |        |            |     |
| System Power   | Status        | for          | member                | 2      |            |     |
| Configured     |               | Power Status |                       | : No   | redundancy |     |
| Operational    |               | Power Status |                       | : No   | redundancy |     |
| Total          | Available     | Power        |                       | : 600  | W          |     |
| Total          | Failover      | Pwr          | Avl                   | :      | 0 W        |     |
| Total          | Redundancy    | Power        |                       | :      | 0 W        |     |
| Total          | Power         | Drawn        |                       | :      | 0 W +/-    | 6W  |
| Total          | Power         | Reserved     |                       | :      | 0 W        |     |
| Total          | Remaining     | Power        |                       | : 600  | W          |     |
| Trap Threshold |               |              |                       | : 80   | %          |     |
| Trap Enabled   |               |              |                       | : Yes  |            |     |
| Always-on      | PoE           | Enabled      |                       | : None |            |     |
| Quick          | PoE Enabled   |              |                       | : None |            |     |
| Internal       | Power         |              |                       |        |            |     |
Total Power
| PS    | (Watts)       |     | Status                |     |     |     |
| ----- | ------------- | --- | --------------------- | --- | --- | --- |
| ----- | ------------- |     | --------------------- |     |     |     |
| 1     | 0             |     | Absent                |     |     |     |
| 2     | 600           |     | Ok                    |     |     |     |
Showingsampleoutputforpower-over-ethernetmember:
| switch#        | show power-over-ethernet |              |        | member |            | 1   |
| -------------- | ------------------------ | ------------ | ------ | ------ | ---------- | --- |
| System Power   | Status                   | for          | member | 1      |            |     |
| Configured     |                          | Power Status |        | : No   | redundancy |     |
| Operational    |                          | Power Status |        | : No   | redundancy |     |
| Total          | Available                | Power        |        | : 740  | W          |     |
| Total          | Failover                 | Pwr          | Avl    | :      | 0 W        |     |
| Total          | Redundancy               | Power        |        | :      | 0 W        |     |
| Total          | Power                    | Drawn        |        | :      | 0 W +/-    | 6W  |
| Total          | Power                    | Reserved     |        | :      | 0 W        |     |
| Total          | Remaining                | Power        |        | : 740  | W          |     |
| Trap Threshold |                          |              |        | : 80   | %          |     |
| Trap Enabled   |                          |              |        | : No   |            |     |
| Always-on      | PoE                      | Enabled      |        | : 1/1  |            |     |
| Quick          | PoE Enabled              |              |        | : 1/1  |            |     |
| Internal       | Power                    |              |        |        |            |     |
Total Power
| PS    | (Watts)       |     | Status                |     |     |     |
| ----- | ------------- | --- | --------------------- | --- | --- | --- |
| ----- | ------------- |     | --------------------- |     |     |     |
| 1     | 0             |     | Absent                |     |     |     |
| 2     | 740           |     | Ok                    |     |     |     |
Showingsampleoutputforpower-over-ethernetbriefinaVSFstack:
| switch#    | show power-over-ethernet |     |             | brief |     |     |
| ---------- | ------------------------ | --- | ----------- | ----- | --- | --- |
| Status and | Configuration            |     | Information |       | for | PoE |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 89

| Member     | 1 Power Status |           |       |     |              |          |     |     |
| ---------- | -------------- | --------- | ----- | --- | ------------ | -------- | --- | --- |
| Available: | 370 W          | Reserved: | 55.60 |     | W Remaining: | 314.40 W |     |     |
| Always-on  | PoE Enabled:   |           | 1/1   |     |              |          |     |     |
| Quick      | PoE Enabled:   | None      |       |     |              |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes Low | Off | Class | 0.0 | W 0.0 | W Denied | None 4 | 2   |
| ----- | ------- | --- | ----- | --- | ----- | -------- | ------ | --- |
1/1/2 Yes Critical Off Usage 1.6 W 1.5 W Delivering* Single 0 1
1/1/3 Yes High Off Class 54.0 W 25.5 W Delivering*^ Dual 1/3 3
| 1/1/4      | No Low         | On        | Usage | 0.0 | W 0.0      | W Disabled | None N/A | N/A |
| ---------- | -------------- | --------- | ----- | --- | ---------- | ---------- | -------- | --- |
| Member     | 2 Power Status |           |       |     |            |            |          |     |
| Available: | 600 W          | Reserved: | 0.00  | W   | Remaining: | 600 W      |          |     |
| Always-on  | PoE Enabled:   |           | None  |     |            |            |          |     |
| Quick      | PoE Enabled:   | None      |       |     |            |            |          |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 2/1/1 | Yes Low | Off | Class | 0.0 | W 0.0 | W Searching | None N/A | N/A |
| ----- | ------- | --- | ----- | --- | ----- | ----------- | -------- | --- |
2/1/2 Yes Critical Off Usage 0.0 W 0.0 W Searching None N/A N/A
| 2/1/3      | Yes High    | Off    | Class | 0.0 | W 0.0          | W Searching | None N/A | N/A |
| ---------- | ----------- | ------ | ----- | --- | -------------- | ----------- | -------- | --- |
| 2/1/4      | No Low      | On     | Usage | 0.0 | W 0.0          | W Disabled  | None N/A | N/A |
| *This port | may go down | in the | event | of  | a PSU failure. |             |          |     |
^This port is power demoted due to user config or power availabilty.
Showingsampleoutputforpower-over-ethernetbriefforaChassissystem:
| switch#    | show power-over-ethernet |             |                 | brief |              |          |     |     |
| ---------- | ------------------------ | ----------- | --------------- | ----- | ------------ | -------- | --- | --- |
| Status and | Configuration            | Information |                 | for   | PoE          |          |     |     |
| Power      | Status                   |             |                 |       |              |          |     |     |
| Available: | 370 W                    | Reserved:   | 55.60           |       | W Remaining: | 314.40 W |     |     |
| Always-on  | PoE Enabled:             |             | 1/1,1/3,1/4,1/7 |       |              |          |     |     |
| Quick      | PoE Enabled:             | None        |                 |       |              |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes Low | Off | Class | 0.0 | W 0.0 | W Denied | None 4 | 2   |
| ----- | ------- | --- | ----- | --- | ----- | -------- | ------ | --- |
1/1/2 Yes Critical Off Usage 1.6 W 1.5 W Delivering* Single 0 1
1/1/3 Yes High Off Class 54.0 W 25.5 W Delivering^ Dual 1/3 3
| 1/1/4      | No Low      | On     | Usage | 0.0 | W 0.0          | W Disabled | None N/A | N/A |
| ---------- | ----------- | ------ | ----- | --- | -------------- | ---------- | -------- | --- |
| *This port | may go down | in the | event | of  | a PSU failure. |            |          |     |
^This port is power demoted due to user config or power availabilty.
Showingsampleoutputforpower-over-ethernetbriefper-port:
switch#
|            | show power-over-ethernet |             |       | 1/1/1 | brief        |          |     |     |
| ---------- | ------------------------ | ----------- | ----- | ----- | ------------ | -------- | --- | --- |
| Status and | Configuration            | Information |       | for   | port 1/1/1   |          |     |     |
| Member     | 1Power Status            |             |       |       |              |          |     |     |
| Available: | 370 W                    | Reserved:   | 55.60 |       | W Remaining: | 314.40 W |     |     |
Power-over-Ethernet|90

| Always-on | PoE Enabled: |     | 1/1 |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes Low | Off | Class | 0.0 | W 0.0 | W Denied | None 4 | 2   |
| ----- | ------- | --- | ----- | --- | ----- | -------- | ------ | --- |
Showingsampleoutputforpower-over-ethernetbriefforinterfacerange:
For6300Switchseries:
| switch#    | show power-over-ethernet |             | 1/1/1-1/1/2 |     | brief            |          |     |     |
| ---------- | ------------------------ | ----------- | ----------- | --- | ---------------- | -------- | --- | --- |
| Status and | Configuration            | Information |             | for | port 1/1/1-1/1/2 |          |     |     |
| Member     | 1Power Status            |             |             |     |                  |          |     |     |
| Available: | 370 W                    | Reserved:   | 55.60       | W   | Remaining:       | 314.40 W |     |     |
| Always-on  | PoE Enabled:             |             | 1/1         |     |                  |          |     |     |
| Quick      | PoE Enabled:             | None        |             |     |                  |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes Low | Off | Class | 0.0 | W 0.0 | W Denied | None 4 | 2   |
| ----- | ------- | --- | ----- | --- | ----- | -------- | ------ | --- |
1/1/2 Yes Critical Off Usage 1.6 W 1.5 W Delivering* Single 0 1
For6400Switchseries:
| switch#    | show power-over-ethernet |             | 1/1/1-1/1/2 |              | brief            |          |     |     |
| ---------- | ------------------------ | ----------- | ----------- | ------------ | ---------------- | -------- | --- | --- |
| Status and | Configuration            | Information |             | for          | port 1/1/1-1/1/2 |          |     |     |
| Power      | Status                   |             |             |              |                  |          |     |     |
| Available: | 360 W                    | Reserved:   | 0.00        | W Remaining: |                  | 360.00 W |     |     |
| Always-on  | PoE Enabled:             |             | 1/1         |              |                  |          |     |     |
| Quick      | PoE Enabled:             | None        |             |              |                  |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes Low | Off | Usage | 0.0 | W 0.0 | W Searching | N/A N/A | N/A |
| ----- | ------- | --- | ----- | --- | ----- | ----------- | ------- | --- |
| 1/1/2 | Yes Low | Off | Usage | 0.6 | W 0.0 | W Searching | N/A N/A | N/A |
Showingsampleoutputforpower-over-ethernetforamissinglinecard:
| switch#    | show power-over-ethernet |     | 1/3      | brief |     |     |     |     |
| ---------- | ------------------------ | --- | -------- | ----- | --- | --- | --- | --- |
| Module 1/3 | is not physically        |     | present. |       |     |     |     |     |
Showingsampleoutputforpower-over-ethernetbriefforamissingmember:
| switch#  | show power-over-ethernet |     | member   | 3   | brief |     |     |     |
| -------- | ------------------------ | --- | -------- | --- | ----- | --- | --- | --- |
| Member 3 | is not physically        |     | present. |     |       |     |     |     |
Showingsampleoutputforpower-over-ethernetportwhenphysicalinterfaceisnotpresent:
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 91

| switch#   | show  | power-over-ethernet |          | 2/1/1 |     |     |     |     |     |
| --------- | ----- | ------------------- | -------- | ----- | --- | --- | --- | --- | --- |
| Interface | 2/1/1 | is not              | present. |       |     |     |     |     |     |
Showingpower-over-ethernetportwithdualsignaturePDconnected:
| switch#   | show       | power-over-ethernet |             | 1/1/1      |     |               |          |       |              |
| --------- | ---------- | ------------------- | ----------- | ---------- | --- | ------------- | -------- | ----- | ------------ |
| Status    | and        | Configuration       | Information |            | for | port 1/1/1*   |          |       |              |
| Power     | Enable     |                     | :           | Yes        |     | PD signature  |          |       | : Dual       |
| PoE PairA |            | Status              | :           | Delivering |     | PoE PairB     | Status   |       | : Delivering |
| Alloc-by  | Configured |                     | :           | Class      |     | Alloc-by      | Actual   |       | : Class      |
| User      | Profile    | Priority            | :           | High       |     | Port Config   | Priority |       | : Low        |
| Port      | Priority   |                     | :           | High       |     | Pre-std       | Detect   |       | : Disabled   |
| PD Type   |            |                     | :           | Type3      |     | User Assigned |          | Class | : Class6     |
PairA Requested Class : Class1 PairB Requested Class : Class4
| PairA    | Assigned | Class | :   | Class1   |     | PairB Assigned |            | Class | : Class4     |
| -------- | -------- | ----- | --- | -------- | --- | -------------- | ---------- | ----- | ------------ |
| Fault    | Status   | PairA | :   | None     |     | Fault Status   |            | PairB | : None       |
| PD Class | Override |       | :   | Disabled |     | Power Pairs    | Configured |       | : alt-a      |
|          |          |       |     |          |     | Power Pairs    | Applied    |       | : alt-a-and- |
alt-b
| PoE Counter |         | Information |     |     |     |            |       |       |     |
| ----------- | ------- | ----------- | --- | --- | --- | ---------- | ----- | ----- | --- |
| Over        | Current | Cnt PairA   | :   | 0   |     | MPS Absent | Cnt   | PairA | : 0 |
| Power       | Denied  | Cnt PairA   | :   | 0   |     | Short Cnt  | PairA |       | : 0 |
| Over        | Current | Cnt PairB   | :   | 0   |     | MPS Absent | Cnt   | PairB | : 0 |
| Power       | Denied  | Cnt PairB   | :   | 0   |     | Short Cnt  | PairB |       | : 0 |
Power Information
| PSE Voltage |     |            | :   | 56.3 V |     | PSE Reserved |       | power | : 34.0 W |
| ----------- | --- | ---------- | --- | ------ | --- | ------------ | ----- | ----- | -------- |
| PD Current  |     | Draw       | :   | 4.1 A  |     | PD Power     | Draw  |       | : 24.6 W |
| PD Average  |     | Power Draw | :   | 24.0 W |     | PD Peak      | Power | Draw  | : 25.1 W |
LLDP Information
| MED Override |            |       |       |      | :   | Enabled       |     |     |     |
| ------------ | ---------- | ----- | ----- | ---- | --- | ------------- | --- | --- | --- |
| MED Priority |            |       |       |      | :   | High          |     |     |     |
| PSE TLV      | Configured |       |       |      | :   | dot3, med     |     |     |     |
| PSE TLV      | Sent       | Type  |       |      | :   | dot3-ext      |     |     |     |
| PD TLV       | Sent       | Type  |       |      | :   | med, dot3-ext |     |     |     |
| DS PSE       | Allocated  | Power | Value | Alt  | A : | 2.5 W         |     |     |     |
| DS PD        | Requested  | Power | Value | Mode | A : | 2.5 W         |     |     |     |
| DS PSE       | Allocated  | Power | Value | Alt  | B : | 25.0 W        |     |     |     |
| DS PD        | Requested  | Power | Value | Mode | B : | 25.0 W        |     |     |     |
Showingpower-over-ethernetportwithsinglesignaturePDconnected:
| switch#  | show       | power-over-ethernet |             | 1/1/1      |     |              |          |     |         |
| -------- | ---------- | ------------------- | ----------- | ---------- | --- | ------------ | -------- | --- | ------- |
| Status   | and        | Configuration       | Information |            | for | port 1/1/9*  |          |     |         |
| Power    | Enable     |                     | :           | Yes        |     | PD signature |          |     | : None  |
| PoE Port |            | Status              | :           | Delivering |     | PD Type      |          |     | : Type3 |
| Alloc-by | Configured |                     | :           | Usage      |     | Alloc-by     | Actual   |     | : Usage |
| User     | Profile    | Priority            | :           | High       |     | Port Config  | Priority |     | : Low   |
Power-over-Ethernet|92

| Port Priority |       | : High   |     | Pre-std      | Detect   |       | : Disabled |
| ------------- | ----- | -------- | --- | ------------ | -------- | ----- | ---------- |
| PD Requested  | Class | : Class1 |     | PSE Assigned | Class    |       | : Class1   |
| Fault Status  |       | : None   |     | User set     | Assigned | Class | : Class6   |
PD Class Override : Disabled Power Pairs Configured : alt-a-and-alt-
b
|     |     |     |     | Power Pairs | Applied |     | : alt-a-and-alt- |
| --- | --- | --- | --- | ----------- | ------- | --- | ---------------- |
b
| PoE Counter  | Information |     |     |            |     |     |     |
| ------------ | ----------- | --- | --- | ---------- | --- | --- | --- |
| Over Current | Cnt         | : 0 |     | MPS Absent | Cnt |     | : 0 |
| Power Denied | Cnt         | : 0 |     | Short Cnt  |     |     | : 0 |
Power Information
| PSE Voltage |            | : 56.3 | V   | PSE Reserved | power      |     | : 8.6 W |
| ----------- | ---------- | ------ | --- | ------------ | ---------- | --- | ------- |
| PD Current  | Draw       | : 1.1  | A   | PD Power     | Draw       |     | : 8.6 W |
| PD Average  | Power Draw | : 8.0  | W   | PD Peak      | Power Draw |     | : 9.1 W |
LLDP Information
| LLDP Detect   |             | :       | Disabled |     |     |     |     |
| ------------- | ----------- | ------- | -------- | --- | --- | --- | --- |
| PSE TLV       | Configured  | :       | N/A      |     |     |     |     |
| PSE TLV       | Sent Type   | :       | N/A      |     |     |     |     |
| PD TLV        | Sent Type   | :       | N/A      |     |     |     |     |
| PSE Allocated | Power       | Value : | 0.0 W    |     |     |     |     |
| PD Requested  | Power Value | :       | 0.0 W    |     |     |     |     |
Showingpower-over-ethernetforaportrange:
| switch# show  | power-over-ethernet |              | 1/1/3-1/1/4 |              |          |       |            |
| ------------- | ------------------- | ------------ | ----------- | ------------ | -------- | ----- | ---------- |
| Status and    | Configuration       | Information  | for         | port 1/1/3   |          |       |            |
| Power Enable  |                     | : Yes        |             | PD signature |          |       | : None     |
| PoE Port      | Status              | : Delivering |             | PD Type      |          |       | : Type3    |
| Alloc-by      | Config              | : Usage      |             | Alloc-by     | Actual   |       | : Usage    |
| User Profile  | Priority            | : High       |             | Port Config  | Priority |       | : Low      |
| Port Priority |                     | : High       |             | Pre-std      | Detect   |       | : Disabled |
| PD Requested  | Class               | : Class1     |             | PSE Assigned | Class    |       | : Class1   |
| Fault Status  |                     | : None       |             | User set     | Assigned | Class | : Class6   |
PD Class Override : Disabled Power Pairs Configured : alt-a-and-alt-
b
|     |     |     |     | Power Pairs | Applied |     | : alt-a-and-alt- |
| --- | --- | --- | --- | ----------- | ------- | --- | ---------------- |
b
| PoE Counter  | Information |     |     |            |     |     |     |
| ------------ | ----------- | --- | --- | ---------- | --- | --- | --- |
| Over Current | Cnt         | : 0 |     | MPS Absent | Cnt |     | : 0 |
| Power Denied | Cnt         | : 0 |     | Short Cnt  |     |     | : 0 |
Power Information
| PSE Voltage |            | : 56.3 | V   | PSE Reserved | power      |     | : 8.6 W |
| ----------- | ---------- | ------ | --- | ------------ | ---------- | --- | ------- |
| PD Current  | Draw       | : 1.1  | A   | PD Power     | Draw       |     | : 8.6 W |
| PD Average  | Power Draw | : 8.0  | W   | PD Peak      | Power Draw |     | : 9.1 W |
LLDP Information
| LLDP Detect |     | :   | Disabled |     |     |     |     |
| ----------- | --- | --- | -------- | --- | --- | --- | --- |
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries) 93

| PSE TLV             | Configured    |         | :            | N/A                                    |                  |            |       |             |
| ------------------- | ------------- | ------- | ------------ | -------------------------------------- | ---------------- | ---------- | ----- | ----------- |
| PSE TLV             | Sent Type     |         | :            | N/A                                    |                  |            |       |             |
| PD TLV              | Sent Type     |         | :            | N/A                                    |                  |            |       |             |
| PSE Allocated       | Power         | Value   | :            | 0.0 W                                  |                  |            |       |             |
| PD Requested        | Power         | Value   | :            | 0.0 W                                  |                  |            |       |             |
| Status and          | Configuration |         | Information  | for                                    | port 1/1/4*      |            |       |             |
| Power Enable        |               |         | : Yes        |                                        | PD signature     |            |       | : None      |
| PoE Port            | Status        |         | : Delivering |                                        | PD Type          |            |       | : Type3     |
| Alloc-by            | Config        |         | : Usage      |                                        | Alloc-by         | Actual     |       | : Usage     |
| User Profile        | Priority      |         | : High       |                                        | Port Config      | Priority   |       | : Low       |
| Port Priority       |               |         | : High       |                                        | Pre-std          | Detect     |       | : Disabled  |
| PD Requested        | Class         |         | : Class1     |                                        | PSE Assigned     | Class      |       | : Class1    |
| Fault Status        |               |         | : None       |                                        | User set         | Assigned   | Class | : Class6    |
| PD Class            | Override      |         | : Disabled   |                                        | Power Pairs      | Configured |       | : alt-a     |
|                     |               |         |              |                                        | Power Pairs      | Applied    |       | : alt-a     |
| PoE Counter         | Information   |         |              |                                        |                  |            |       |             |
| Over Current        | Cnt           |         | : 0          |                                        | MPS Absent       | Cnt        |       | : 0         |
| Power Denied        | Cnt           |         | : 0          |                                        | Short Cnt        |            |       | : 0         |
| Power Information   |               |         |              |                                        |                  |            |       |             |
| PSE Voltage         |               |         | : 56.3       | V                                      | PSE Reserved     | power      |       | : 4.3 W     |
| PD Current          | Draw          |         | : 1.1        | A                                      | PD Power         | Draw       |       | : 4.3 W     |
| PD Average          | Power         | Draw    | : 4.0        | W                                      | PD Peak          | Power Draw |       | : 4.3 W     |
| LLDP Information    |               |         |              |                                        |                  |            |       |             |
| LLDP Detect         |               |         | :            | Disabled                               |                  |            |       |             |
| PSE TLV             | Configured    |         | :            | N/A                                    |                  |            |       |             |
| PSE TLV             | Sent Type     |         | :            | N/A                                    |                  |            |       |             |
| PD TLV              | Sent Type     |         | :            | N/A                                    |                  |            |       |             |
| PSE Allocated       | Power         | Value   | :            | 0.0 W                                  |                  |            |       |             |
| PD Requested        | Power         | Value   | :            | 0.0 W                                  |                  |            |       |             |
| Command History     |               |         |              |                                        |                  |            |       |             |
| Release             |               |         |              | Modification                           |                  |            |       |             |
| 10.09               |               |         |              | Addedpower-pairsconfigurationintheshow |                  |            |       | power-over- |
|                     |               |         |              | ethernet                               | <IFRANGE>output. |            |       |             |
| 10.07orearlier      |               |         |              | --                                     |                  |            |       |             |
| Command Information |               |         |              |                                        |                  |            |       |             |
| Platforms           | Command       | context |              | Authority                              |                  |            |       |             |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Power-over-Ethernet|94

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
95
AOS-CX10.10MonitoringGuide|(6300,6400SwitchSeries)

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
ArubaAirWave|96

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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

97

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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

98

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

Support and Other Resources | 99

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

AOS-CX 10.10 Monitoring Guide | (6300, 6400 Switch Series)

100