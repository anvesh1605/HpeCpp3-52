AOS-CX 10.13 Monitoring
Guide

6200 Switch Series

Published: January 2024

Version: 2

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

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

3

Contents
| About                                             | this document                      |              |                    | 8   |
| ------------------------------------------------- | ---------------------------------- | ------------ | ------------------ | --- |
| Applicableproducts                                |                                    |              |                    | 8   |
| Latestversionavailableonline                      |                                    |              |                    | 8   |
| Commandsyntaxnotationconventions                  |                                    |              |                    | 8   |
| Abouttheexamples                                  |                                    |              |                    | 9   |
| Identifyingswitchportsandinterfaces               |                                    |              |                    | 9   |
| Monitoring                                        | hardware                           | through      | visual observation | 11  |
| ConfirmingnormaloperationoftheswitchbyreadingLEDs |                                    |              |                    | 11  |
| Detectingiftheswitchisnotreadyforafailoverevent   |                                    |              |                    | 12  |
| FindingfaultedcomponentsusingtheswitchLEDs        |                                    |              |                    | 12  |
| Boot                                              | commands                           |              |                    | 14  |
| bootset-default                                   |                                    |              |                    | 14  |
| bootsystem                                        |                                    |              |                    | 14  |
| showboot-history                                  |                                    |              |                    | 16  |
| Switch                                            | system                             | and hardware | commands           | 20  |
| External                                          | storage                            |              |                    | 21  |
| Externalstoragecommands                           |                                    |              |                    | 21  |
|                                                   | address                            |              |                    | 21  |
|                                                   | directory                          |              |                    | 22  |
|                                                   | disable                            |              |                    | 23  |
|                                                   | enable                             |              |                    | 23  |
|                                                   | external-storage                   |              |                    | 24  |
|                                                   | password(external-storage)         |              |                    | 25  |
|                                                   | showexternal-storage               |              |                    | 26  |
|                                                   | showrunning-configexternal-storage |              |                    | 26  |
|                                                   | type                               |              |                    | 27  |
|                                                   | username                           |              |                    | 28  |
|                                                   | vrf                                |              |                    | 29  |
| IP-SLA                                            |                                    |              |                    | 30  |
| IP-SLAguidelines                                  |                                    |              |                    | 30  |
| LimitationswithVoIPSLAs                           |                                    |              |                    | 31  |
| IP-SLAcommands                                    |                                    |              |                    | 31  |
|                                                   | https                              |              |                    | 31  |
|                                                   | ip-slaresponder                    |              |                    | 32  |
|                                                   | showip-slaresponder                |              |                    | 33  |
|                                                   | showip-slaresponderresults         |              |                    | 34  |
|                                                   | showip-sla                         |              |                    | 35  |
| L1-100Mbps                                        |                                    | downshift    |                    | 40  |
| Limitationswithspeeddownshift                     |                                    |              |                    | 40  |
| L1-100Mbpsdownshiftcommands                       |                                    |              |                    | 40  |
|                                                   | downshiftenable                    |              |                    | 40  |
|                                                   | showinterface                      |              |                    | 41  |
5
AOS-CX10.13MonitoringGuide| (6200SwitchSeries)

| showinterfacestatistics                          |          |            | 45  |
| ------------------------------------------------ | -------- | ---------- | --- |
| showinterfacedownshift-enable                    |          |            | 49  |
| showrunning-configinterface                      |          |            | 50  |
| Mirroring                                        |          |            | 52  |
| Mirrorstatistics                                 |          |            | 52  |
| Classifierpoliciesandmirroringsessions           |          |            | 52  |
| VLANasasource                                    |          |            | 53  |
| Mirroringcommands                                |          |            | 53  |
| clearmirror                                      |          |            | 53  |
| clearmirrorendpoint                              |          |            | 54  |
| comment                                          |          |            | 55  |
| copytcpdump-pcap                                 |          |            | 56  |
| copytshark-pcap                                  |          |            | 57  |
| destinationcpu                                   |          |            | 58  |
| destinationinterface                             |          |            | 58  |
| destinationtunnel                                |          |            | 59  |
| diagnostic                                       |          |            | 61  |
| diagutilitiestcpdump                             |          |            | 62  |
| disable                                          |          |            | 64  |
| enable                                           |          |            | 65  |
| mirrorsession                                    |          |            | 65  |
| mirrorendpoint                                   |          |            | 66  |
| showmirror                                       |          |            | 67  |
| showmirrorendpoint                               |          |            | 69  |
| shutdown                                         |          |            | 70  |
| source                                           |          |            | 71  |
| sourceinterface                                  |          |            | 72  |
| sourcevlan                                       |          |            | 74  |
| Monitoring                                       | a device | using SNMP | 77  |
| Power-over-Ethernet                              |          |            | 78  |
| PoEcommands                                      |          |            | 79  |
| lldpdot3poe                                      |          |            | 79  |
| lldpmedpoe                                       |          |            | 80  |
| power-over-ethernet                              |          |            | 80  |
| power-over-ethernetallocate-by                   |          |            | 81  |
| power-over-ethernetalways-on                     |          |            | 82  |
| power-over-ethernetassigned-class                |          |            | 83  |
| power-over-ethernetpre-std-detect                |          |            | 84  |
| power-over-ethernetpriority                      |          |            | 85  |
| power-over-ethernetquick-poe                     |          |            | 86  |
| power-over-ethernetthreshold                     |          |            | 86  |
| power-over-ethernettrap                          |          |            | 87  |
| showlldplocal                                    |          |            | 88  |
| showlldpneighbor                                 |          |            | 89  |
| showpower-over-ethernet                          |          |            | 90  |
| Aruba AirWave                                    |          |            | 94  |
| SNMPsupportandAirWave                            |          |            | 94  |
| SNMPontheswitch                                  |          |            | 94  |
| SupportedfeatureswithAirWaveandtheAOS-CXswitch   |          |            | 95  |
| ConfiguringtheAOS-CXswitchtobemonitoredbyAirWave |          |            | 95  |
| AirWavecommands                                  |          |            | 96  |
| logging                                          |          |            | 96  |
|6

|                                    | snmp-servercommunity |           | 98  |
| ---------------------------------- | -------------------- | --------- | --- |
|                                    | snmp-serverhost      |           | 99  |
|                                    | snmp-servervrf       |           | 101 |
|                                    | snmpv3context        |           | 101 |
|                                    | snmpv3user           |           | 102 |
| Support                            | and Other            | Resources | 105 |
| AccessingHPEArubaNetworkingSupport |                      |           | 105 |
| AccessingUpdates                   |                      |           | 106 |
|                                    | ArubaSupportPortal   |           | 106 |
|                                    | MyNetworking         |           | 106 |
| WarrantyInformation                |                      |           | 106 |
| RegulatoryInformation              |                      |           | 107 |
| DocumentationFeedback              |                      |           | 107 |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 7

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A, R8Q68A, R8Q69A, R8Q70A,
R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A, JL724B, JL725B, JL726B, JL727B, JL728B,
S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,  S0M87A,  S0M88A,  S0M89A,  S0M90A,
S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

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

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

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
| On the 6200 Switch | Series |     |     |
| ------------------ | ------ | --- | --- |
Aboutthisdocument|9

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

10

Monitoring hardware through visual observation

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

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

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

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

13

Chapter 3

Boot commands

Boot commands

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

Reboots all modules on the switch. By default, the configured default operating system image is used.
Optional parameters enable you to specify which system image to use for the reboot operation and for
future reboot operations.

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

14

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

Rebooting the system from the secondary operating system image, setting the secondary operating
system image as the configured default boot image:

Boot commands | 15

| switch#    | boot system  | secondary         |               |                |
| ---------- | ------------ | ----------------- | ------------- | -------------- |
| Default    | boot image   | set to secondary. |               |                |
| Do you     | want to save | the current       | configuration | (y/n)? n       |
| This will  | reboot the   | entire switch     | and render    | it unavailable |
| until the  | process      | is complete.      |               |                |
| Continue   | (y/n)? y     |                   |               |                |
| The system | is going     | down for reboot.  |               |                |
Cancelingasystemreboot:
switch#
boot system
| Do you    | want to save | the current   | configuration | (y/n)? n       |
| --------- | ------------ | ------------- | ------------- | -------------- |
| This will | reboot the   | entire switch | and render    | it unavailable |
| until the | process      | is complete.  |               |                |
| Continue  | (y/n)? n     |               |               |                |
| Reboot    | aborted.     |               |               |                |
switch#
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show boot-history |           |        |          |     |
| ----------------- | --------- | ------ | -------- | --- |
| show boot-history | [all|{vsf | member | <1-10>}] |     |
Description
Showsboothistoryinformation.Whennoparametersarespecified,showsthemostrecentinformation
aboutthecurrentbootoperation,andthethreepreviousbootoperationsfortheswitch.Whentheall
parameterisspecified,theoutputofthiscommandshowsthebootinformationfortheactive
managementmodule.
.
Toviewboot-historyonastandby,thecommandmustbesentontheconductorconsole.
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 16

| Parameter |     | Description                                         |     |
| --------- | --- | --------------------------------------------------- | --- |
| all       |     | Optional.Showsbootinformationfortheactivemanagement |     |
module.
| vsf member <1-10> |     |     |     |
| ----------------- | --- | --- | --- |
Optional.DisplayboothistoryforthespecifiedVSFmember
Usage
Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereis
apreviousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
system)andrebootreasons.Previousbootinformationisdisplayedinreversechronologicalorder.
Theoutputofthiscommandincludesthefollowinginformation:
| Parameter |     |     | Description                                  |
| --------- | --- | --- | -------------------------------------------- |
| Index     |     |     | Thepositionofthebootinthehistoryfile.Range:0 |
to3.
Boot ID
AuniqueIDfortheboot.Asystem-generated128-
bitstring.
Current Boot, up for <time> Forthecurrentboot,theshowboot-history
commandshowsthenumberofsecondsthe
modulehasbeenrunningonthecurrentsoftware.
<Timestamp>: boot reason Forpreviousbootoperations,theshowboot-
historycommandshowsthetimeatwhichthe
operationoccurredandthereasonfortheboot.
Thereasonforthebootisoneofthefollowing
values:
n <DAEMON-NAME>crash:Thedaemonidentified
by<DAEMON-NAME>causedthemoduletoboot.
n Kernelcrash:Theoperatingsystemsoftware
associatedwiththemodulecausedthemodule
toboot.
n Uncontrolledreboot:Thereasonforthereboot
isnotknown.
n Rebootrequestedthroughdatabase:The
rebootoccurredbecauseofarequestmade
throughtheCLIorotherAPI.
Examples
Showingtheboothistoryoftheactivemanagementmodule:
| switch# show | boot-history |     |     |
| ------------ | ------------ | --- | --- |
| Management   | module       |     |     |
=================
| Index : 2                                  |               |        |                 |
| ------------------------------------------ | ------------- | ------ | --------------- |
| Boot ID : c34a2c2499004a02bbeeff4992e1fdbd |               |        |                 |
| Current Boot,                              | up for 1 days | 13 hrs | 13 mins 27 secs |
| Index : 1                                  |               |        |                 |
Bootcommands|17

| Boot ID | : bfba9bc486304e57904ac717a0ccbdcd |     |     |
| ------- | ---------------------------------- | --- | --- |
02 Sep 23 02:55:33 : CPU request reset with 0x20201, Version: FL.10.14.0000-1619-
ga9ec1805bd442~dirty
| 02 Sep  | 23 02:55:33                        | : Switch boot | count is 2 |
| ------- | ---------------------------------- | ------------- | ---------- |
| Index : | 0                                  |               |            |
| Boot ID | : a88a71b7ca9a4574af7e3b811ddfdc7e |               |            |
02 Sep 23 02:49:26 : Reboot requested by user, Version: FL.10.14.0000-1619-
ga9ec1805bd442~dirty
| 02 Sep  | 23 02:50:02                        | : Switch boot | count is 1 |
| ------- | ---------------------------------- | ------------- | ---------- |
| Index : | 3                                  |               |            |
| Boot ID | : f00ba10c8c44457f83fee303d014a89a |               |            |
25 Aug 23 10:27:42 : Power on reset with 0x1, Version: FL.10.14.0000-1465-
g9df95249d06b0~dirty
| 25 Aug | 23 10:28:18 | : Switch | boot count is 3 |
| ------ | ----------- | -------- | --------------- |
25 Aug 23 10:29:02 : Primary overtemperature fault detected with 0x2 in PSU 1/1
Showingtheboothistoryoftheactivemanagementmoduleandalllinemodules:
switch#
| Management | module |     |     |
| ---------- | ------ | --- | --- |
=================
| Index :     | 3                                  |                    |                  |
| ----------- | ---------------------------------- | ------------------ | ---------------- |
| Boot ID     | : f1bf071bdd04492bbf8439c6e479d612 |                    |                  |
| Current     | Boot, up for                       | 22 hrs 12          | mins 22 secs     |
| Index :     | 2                                  |                    |                  |
| Boot ID     | : edfa2d6598d24e989668306c4a56a06d |                    |                  |
| 07 Aug      | 18 16:28:01                        | : Reboot requested | through database |
| Index :     | 1                                  |                    |                  |
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
| Management | module |     |     |
| ---------- | ------ | --- | --- |
=================
| Index : | 3                                  |                    |                  |
| ------- | ---------------------------------- | ------------------ | ---------------- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |                    |                  |
| Current | Boot, up for                       | 22 hrs 12          | mins 22 secs     |
| Index : | 2                                  |                    |                  |
| Boot ID | : edfa2d6598d24e989668306c4a56a06d |                    |                  |
| 07 Aug  | 18 16:28:01                        | : Reboot requested | through database |
| Index : | 1                                  |                    |                  |
| Boot ID | : 0bda8d0361df4a7e8e3acdc1dba5caad |                    |                  |
| 07 Aug  | 18 14:08:46                        | : Reboot requested | through database |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 18

| Index :     | 0                                  |          |           |     |                  |
| ----------- | ---------------------------------- | -------- | --------- | --- | ---------------- |
| Boot ID     | : 23da2b0e26d048d7b3f4b6721b69c110 |          |           |     |                  |
| 07 Aug      | 18 13:00:46                        | : Reboot | requested |     | through database |
| Line module | 1/1                                |          |           |     |                  |
=================
| Index : | 3           |              |     |         |     |
| ------- | ----------- | ------------ | --- | ------- | --- |
| 10 Aug  | 17 12:45:46 | : dune_agent |     | crashed |     |
...
ThefollowingexampledisplaystheboothistoryfortheVSFmember2.
| switch# | show boot-history |     | vsf | member | 2   |
| ------- | ----------------- | --- | --- | ------ | --- |
Member-2
=========
| Index :        | 0                                  |          |           |       |                  |
| -------------- | ---------------------------------- | -------- | --------- | ----- | ---------------- |
| Boot ID        | : df99026c194a44f1944a3e7685fb4d90 |          |           |       |                  |
| Current        | Boot, up for                       | 3        | hrs 31    | mins  | 39 secs          |
| Index :        | 3                                  |          |           |       |                  |
| Boot ID        | : 7bf4104903fe4ad1ba4bce40e8099c76 |          |           |       |                  |
| 10 Aug         | 17 10:02:24                        | : Reboot | requested |       | through database |
| 10 Aug         | 17 10:02:13                        | : Switch | boot      | count | is 2             |
| Command        | History                            |          |           |       |                  |
| Release        |                                    |          |           |       | Modification     |
| 10.07orearlier |                                    |          |           |       | --               |
| Command        | Information                        |          |           |       |                  |
| Platforms      | Command                            | context  |           |       | Authority        |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Bootcommands|19

Chapter 4
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
Switchsystemandhardwarecommandsaregeneralcommandsusedtoconfigurefundamentalsettings
ontheswitch.
RefertotheFundamentalsGuidetoviewtheswitchsystemandhardwarecommands.
20
AOS-CX10.13MonitoringGuide|(6200SwitchSeries)

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
21
AOS-CX10.13MonitoringGuide|(6200SwitchSeries)

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
6200 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
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
Externalstorage|22

| Release             |         |         | Modification |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
6200 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
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
6200 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
usergroupmemberswithexecution
rightsforthiscommand.Operatorscan
executethiscommandfromthe
operatorcontext(>)only.
enable
enable
no enable
Description
Enablestheexternalstoragevolume.
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 23

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
6200 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
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
Externalstorage|24

| Release        |             |     |         | Modification |
| -------------- | ----------- | --- | ------- | ------------ |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecution
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
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 25

| Release        |             |         | Modification |           |     |     |
| -------------- | ----------- | ------- | ------------ | --------- | --- | --- |
| 10.07orearlier |             |         | --           |           |     |     |
| Command        | Information |         |              |           |     |     |
| Platforms      | Command     | context |              | Authority |     |     |
6200 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
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
6200 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
(#)
| show running-config |     | external-storage |     |     |     |     |
| ------------------- | --- | ---------------- | --- | --- | --- | --- |
Externalstorage|26

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
6200 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
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
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 27

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
6200 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
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
Externalstorage|28

| Release             |         |         | Modification |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
6200 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
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
6200 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
memberswithexecutionrightsforthis
command.
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 29

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

n Maximum sessions: IP-SLA source 50, IP-SLA responder 80.

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

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

30

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

Configures HTTPS as the IP-SLA test mechanism. Requires destination URL and type of HTTPS request
(get/raw).

The no form of this command removes the configuration.

For HTTPS IP-SLA sessions, it is not required to install a certificate on the switch.

Parameter

{get | raw}

URL

Description

Selects HTTPS request type as get or raw where the
system will generate or provide HTTPS payload.

Specifies HTTPS URL address of syntax. https://<HOST
NAME/IP-ADDRESS>:<PORT>/<PATH>.

source {<SOURCE-IPV4-ADDR> | <IFNAME>}

Selects the source IPv4 address for SLA probes or the
source interface to use for sending IP-SLA probes.

IP-SLA | 31

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
source-port <PORT-NUM> SpecifiesthevalueofthesourceportfortheIP-SLA
probes.
cache disable
SelectscacheoptionfortheHTTPSserver.Bydefaultthe
optionisenabled.
name-server <IPV4-ADDR-DNS-SERVER> SpecifiestheIPv4addressofDNSserver.
| probe-interval | <PROBE-INTERVAL> |     |     |     |
| -------------- | ---------------- | --- | --- | --- |
Specifiestheprobeintervalinseconds.Range:30to
604800.
version <VERSION-NUMBER> SpecifiesthesourceinterfacetouseforsendingIP-SLA
probes.
| https-raw-request | <RAW-PAYLOAD> |     | HTTPSrawrequest.String. |     |
| ----------------- | ------------- | --- | ----------------------- | --- |
Examples
switch(config-ipsla-1)# https get https://device.arubanetworks.com/root/home.html
| switch(config-ipsla-1)# |     | https get | https://2.2.2.2 | source 1/1/1 |
| ----------------------- | --- | --------- | --------------- | ------------ |
switch(config-ipsla-1)# https get https://device.arubanetworks.com source 2.2.2.1
switch(config-ipsla-1)# https get https://device.arubanetworks.com/root/home.html
| source-interface | 1/1/1 |     |     |     |
| ---------------- | ----- | --- | --- | --- |
switch(config-ipsla-1)# https get https://device.arubanetworks.com name-server
10.10.10.2
switch(config-ipsla-1)# https raw https://device.arubanetworks.com/root/home.html
| raw-request | “GET /en/US/hmpgs/index.html” |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- |
switch(config-ipsla-1)# no https get https://2.2.2.2 source 1/1/1
| switch(config-ipsla-1)# |     | no https | raw |     |
| ----------------------- | --- | -------- | --- | --- |
https://device.arubanetworks.com/root/home.html raw-request “GET
/en/US/hmpgs/index.html”
| Command History     |         |         |                    |           |
| ------------------- | ------- | ------- | ------------------ | --------- |
| Release             |         |         | Modification       |           |
| 10.12.1000          |         |         | Commandintroduced. |           |
| Command Information |         |         |                    |           |
| Platforms           | Command | context |                    | Authority |
6200 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
ip-sla responder
ip-sla responder <SLA-NAME> {udp-echo | tcp-connect | udp-jitter-voip} <PORT-NUM>
| [source {<SOURCE-IPV4-ADDR> |     | |   | <IFNAME>}][vrf | <VRF-NAME>] |
| --------------------------- | --- | --- | -------------- | ----------- |
no ip-sla responder <SLA-NAME> {udp-echo | tcp-connect | udp-jitter-voip} <PORT-NUM>
| [source {<SOURCE-IPV4-ADDR> |     | |   | <IFNAME>}][vrf | <VRF-NAME>] |
| --------------------------- | --- | --- | -------------- | ----------- |
Description
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 32

SelectstheIP-SLAresponder.Therespondercanbeconfiguredforudp-echo,tcp-connect,udp-jitter-
voiptype.ItrequirestheSLAname,SLAtype,andportnumberasarguments.SourceIP/interfaceIDisa
mustfortypeudp-jitter-voipandoptionalforothertypes.
ThenoformofthiscommandremovestheIP-SLAresponder.
Parameter Description
<SLA-NAME>
SpecifiestheSLAname.Length:1to64characters.
udp-echo Enablesresponderforudp-echoprobes.
tcp-connect
SelectsTCPconnectastheIP-SLAtestmechanism.
vrf <VRF-NAME> SpecifiesthenameoftheVRFtouse.
udp-jitter-voip
SelectsVOIPjitterastheIP-SLAtestmechanism.
<PORT-NUM> SpecifiestheportnumbertolistenforIP-SLAprobes.
Range:1to65535.
| [source | {<SOURCE-IPV4-ADDR> | | <IFNAME>}] |     |
| ------- | ------------------- | ------------ | --- |
SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
Examples
switch(config)# ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
switch(config)# ip-sla responder SLA1 udp-echo 8000 source 1/1/1
switch(config)# no ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ip-sla | responder |            |     |
| ----------- | --------- | ---------- | --- |
| show ip-sla | responder | <SLA-NAME> |     |
Description
ShowsthegivenIP-SLAresponderconfigurationandoperationstatus.
IP-SLA|33

| Parameter  |     |     |     |     | Description          |
| ---------- | --- | --- | --- | --- | -------------------- |
| <SLA-NAME> |     |     |     |     | SpecifiestheSLAname. |
Examples
|                | switch(config)# | show      | ip-sla     | responder        | SLA3         |
| -------------- | --------------- | --------- | ---------- | ---------------- | ------------ |
|                | SLA             | Name      | :          | SLA3             |              |
|                | IP-SLA          | Type      | :          | Udp-echo         |              |
|                | VRF             |           | :          | Default          |              |
|                | Responder       | Port      | :          | 8000             |              |
|                | Responder       | IP        | :          | 2.2.2.3          |              |
|                | Responder       | Interface | :          | 1/1/1            |              |
|                | Responder       | Status    | :          | Running          |              |
|                | switch(config)# | show      | ip-sla     | responder        | 1            |
|                | SLA Name        |           | : 1        | (non-persistent) |              |
|                | SLA Type        |           | : udp-echo |                  |              |
|                | VRF Name        |           | : default  |                  |              |
|                | Responder       | Port      | : 10       |                  |              |
|                | Responder       | IP        | :          |                  |              |
|                | Responder       | Interface | :          |                  |              |
|                | Responder       | Status    | : Running  |                  |              |
| Command        | History         |           |            |                  |              |
| Release        |                 |           |            |                  | Modification |
| 10.07orearlier |                 |           |            |                  | --           |
| Command        | Information     |           |            |                  |              |
| Platforms      |                 | Command   | context    |                  | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show | ip-sla | responder |     | results |     |
| ---- | ------ | --------- | --- | ------- | --- |
show ip-sla responder <SLA-NAME> <SOURCE-IPV4-ADDR> <PORT-NUM> results
Description
Showsthegivenip-slaresponderstatisticsforagivensourceIPandport.Thiscommandisonly
applicableforthesourceswheresourceIPandportareconfigured.
| Parameter          |     |     |     |     | Description                            |
| ------------------ | --- | --- | --- | --- | -------------------------------------- |
| <SLA-NAME>         |     |     |     |     | SpecifiestheSLAname.                   |
| <SOURCE-IPV4-ADDR> |     |     |     |     | SpecifiesthesourceIPV4address.         |
| <PORT-NUM>         |     |     |     |     | Specifiestheportnumber.Range:1to65535. |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 34

Examples
| switch#        | show        |          | ip-sla    | responder  | SLA1         | 2.2.2.1 | 8000 results |
| -------------- | ----------- | -------- | --------- | ---------- | ------------ | ------- | ------------ |
|                | IP-SLA      | Type     |           | : Udp-echo |              |         |              |
|                | VRF Name    |          |           | : Default  |              |         |              |
|                | Source      | IP       |           | : 2.2.2.1  |              |         |              |
|                | Source      | Port     |           | : 8000     |              |         |              |
|                | Responder   |          | Port      | : 8888     |              |         |              |
|                | Responder   |          | IP        | : 2.2.2.3  |              |         |              |
|                | Responder   |          | Interface | :          |              |         |              |
|                | Responder   |          | Status    | : Running  |              |         |              |
|                | Packets     | Received |           | : 2        |              |         |              |
|                | Packets     | Sent     |           | : 2        |              |         |              |
| Command        | History     |          |           |            |              |         |              |
| Release        |             |          |           |            | Modification |         |              |
| 10.07orearlier |             |          |           |            | --           |         |              |
| Command        | Information |          |           |            |              |         |              |
| Platforms      |             | Command  |           | context    | Authority    |         |              |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show | ip-sla |             |     |           |        |     |     |
| ---- | ------ | ----------- | --- | --------- | ------ | --- | --- |
| show | ip-sla | {<SLA-NAME> |     | [results] | | all} |     |     |
Description
ShowsthegivenIP-SLAsourceconfigurationandstatus.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<SLA-NAME>
SpecifiestheSLAname.
| results |     |     |     |     | ShowsthestatisticscalculatedforanSLAtype. |     |     |
| ------- | --- | --- | --- | --- | ----------------------------------------- | --- | --- |
all
Showsallip-slasourceconfigurationsandstatus.
Examples
| switch# | show        | ip-sla  |                   | xyz results  |          |     |             |
| ------- | ----------- | ------- | ----------------- | ------------ | -------- | --- | ----------- |
|         | IP-SLA      | session |                   | status       |          |     |             |
|         | IP-SLA      |         | Name              |              |          | :   | xyz         |
|         | IP-SLA      |         | Type              |              |          | :   | tcp-connect |
|         | Destination |         |                   | Host Name/IP | Address: |     | 2.2.2.1     |
|         | Destination |         |                   | Port         |          | :   | 8888        |
|         | Source      |         | IP Address/IFName |              |          | :   | 2.2.2.2     |
|         | Source      |         | Port              |              |          | :   | 5555        |
IP-SLA|35

|                 | Status                  |                   |              |               | : running         |             |
| --------------- | ----------------------- | ----------------- | ------------ | ------------- | ----------------- | ----------- |
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
|                 | Minimum RTT(ms)         |                   |              |               | : 12              |             |
|                 | Maximum RTT(ms)         |                   |              |               | : 12              |             |
|                 | Average RTT(ms)         |                   |              |               | : 12              |             |
|                 | DNS RTT(ms)             |                   |              |               | : 0               |             |
|                 | TCP RTT(ms)             |                   |              |               | : 12              |             |
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
|                 | Source                  | Port              |              |               | : 5555            |             |
|                 | Status                  |                   |              |               | : running         |             |
|                 | IP-SLA Session          |                   | Cumulative   | Counters      |                   |             |
|                 | Total                   | Probes            | Transmitted  |               | : 1               |             |
|                 | Probes                  | Timed-out         |              |               | : 0               |             |
|                 | Bind Error              |                   |              |               | : 0               |             |
|                 | Destination             |                   | Address      | Unreachable   | : 0               |             |
|                 | DNS Resolution          |                   | Failures     |               | : 0               |             |
|                 | Reception               | Error             |              |               | : 0               |             |
|                 | Transmission            |                   | Error        |               | : 0               |             |
|                 | IP-SLA Latest           | Probe             | Results      |               |                   |             |
|                 | Last Probe              | Time              |              |               | : 2018 Jul        | 13 02:02:48 |
|                 | Packets                 | Sent              |              |               | : 1               |             |
|                 | Packets                 | Received          |              |               | : 1               |             |
|                 | Packet                  | Loss              | in Test      |               | : 0.0000%         |             |
|                 | Minimum                 | RTT(ms)           |              |               | : 1               |             |
|                 | Maximum                 | RTT(ms)           |              |               | : 1               |             |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 36

|                 | Average   |                   | RTT(ms)     |                   | : 1                    |          |            |     |
| --------------- | --------- | ----------------- | ----------- | ----------------- | ---------------------- | -------- | ---------- | --- |
|                 | DNS       | RTT(ms)           |             |                   | : 0                    |          |            |     |
|                 | Min       | Positive          | SD          |                   | : 1 Min                | Positive | DS         | : 2 |
|                 | Max       | Positive          | SD          |                   | : 1 Max                | Positive | DS         | : 2 |
|                 | Positive  |                   | SD Number   |                   | : 2 Positive           |          | DS Number  | : 2 |
|                 | Positive  |                   | SD Sum      |                   | : 2 Positive           |          | DS Sum     | : 4 |
|                 | Positive  |                   | SD Average  |                   | : 5 Positive           |          | DS Average | : 5 |
|                 | Min       | Negative          | SD          |                   | : 1 Min                | Negative | DS         | : 1 |
|                 | Max       | Negative          | SD          |                   | : 1 Max                | Negative | DS         | : 1 |
|                 | Negative  |                   | SD Number   |                   | : 2 Negative           |          | DS Number  | : 4 |
|                 | Negative  |                   | SD Sum      |                   | : 2 Negative           |          | DS Sum     | : 4 |
|                 | Negative  |                   | SD Average  |                   | : 5 Negative           |          | DS Average | : 5 |
|                 | Max       | SD                | Delay       |                   | : 0 Max                | DS       | Delay      | : 0 |
|                 | Min       | SD                | Delay       |                   | : 0 Min                | DS       | Delay      | : 0 |
|                 | Average   |                   | SD Delay    |                   | : 0 Average            |          | DS Delay   | : 0 |
|                 | Voice     | Scores:           |             |                   |                        |          |            |     |
|                 | MOS       | Score             |             |                   | : 4.38 ICPIF           |          |            | : 0 |
| switch(config)# |           |                   | show ip-sla | m3op              |                        |          |            |     |
|                 | IP-SLA    | Name              |             | : jitter-sla      |                        |          |            |     |
|                 | Status    |                   |             | : running         |                        |          |            |     |
|                 | IP-SLA    | Type              |             | : udp-jitter-voip |                        |          |            |     |
|                 | VRF       |                   |             | : ipslasrc        |                        |          |            |     |
|                 | Source    | IP                |             | : 2.2.2.2         |                        |          |            |     |
|                 | Source    | Interface         |             | :                 |                        |          |            |     |
|                 | Domain    | Name              | Server      | :                 |                        |          |            |     |
|                 | TOS       |                   |             | : 10              |                        |          |            |     |
|                 | Probe     | Interval(seconds) |             | : 90              |                        |          |            |     |
|                 | Advantage |                   | Factor      | : 0               |                        |          |            |     |
|                 | Codec     | Type              |             | : g711a           |                        |          |            |     |
| switch(config)# |           |                   | show ip-sla | https-sla         |                        |          |            |     |
|                 | SLA Name  |                   |             | : https-sla       |                        |          |            |     |
|                 | Status    |                   |             | : running         |                        |          |            |     |
|                 | SLA Type  |                   |             | : https           |                        |          |            |     |
|                 | VRF       |                   |             | : default         |                        |          |            |     |
|                 | Source    | Port              |             | : 1027            |                        |          |            |     |
|                 | Source    | IP                |             | : 1.1.1.1         |                        |          |            |     |
|                 | Source    | Interface         |             | :                 |                        |          |            |     |
|                 | Domain    | Name              | Server      | :                 |                        |          |            |     |
|                 | Probe     | Interval(seconds) |             | : 60              |                        |          |            |     |
|                 | HTTPS     | Request           | Type        | : raw             |                        |          |            |     |
|                 | HTTPS     | URL               |             | : https://1.1.1.2 |                        |          |            |     |
|                 | Cache     |                   |             | : Enabled         |                        |          |            |     |
|                 | HTTPS     | Proxy             | URL         | :                 |                        |          |            |     |
|                 | HTTP      | Version           | Number      | :                 |                        |          |            |     |
| switch(config)# |           |                   | show ip-sla | all               |                        |          |            |     |
| IP-SLA          | session   |                   | status      |                   |                        |          |            |     |
| IP-SLA          | Name      |                   |             |                   | : 707 (non-persistent) |          |            |     |
| IP-SLA          | Type      |                   |             |                   | : https                |          |            |     |
| Destination     |           | Host              | Name/IP     | Address           | : NA                   |          |            |     |
| Destination     |           | Port              |             |                   | : NA                   |          |            |     |
| Source          | IP        | Address/IFName    |             |                   | :                      |          |            |     |
| Source          | Port      |                   |             |                   | :                      |          |            |     |
| Status          |           |                   |             |                   | : running              |          |            |     |
IP-SLA|37

| IP-SLA          | Session           | Cumulative          | Counters |                  |          |             |     |     |
| --------------- | ----------------- | ------------------- | -------- | ---------------- | -------- | ----------- | --- | --- |
| Total Probes    |                   | Transmitted         |          | :                | 1        |             |     |     |
| Probes          | Timed-out         |                     |          | :                | 0        |             |     |     |
| Bind Error      |                   |                     |          | :                | 0        |             |     |     |
| Destination     |                   | Address Unreachable |          | :                | 0        |             |     |     |
| DNS Resolution  |                   | Failures            |          | :                | 0        |             |     |     |
| Reception       | Error             |                     |          | :                | 0        |             |     |     |
| Transmission    |                   | Error               |          | :                | 0        |             |     |     |
| IP-SLA          | Latest            | Probe Results       |          |                  |          |             |     |     |
| Last Probe      | Time              |                     |          | :                | 2023 Jun | 05 13:10:19 |     |     |
| Packets         | Sent              |                     |          | :                | 1        |             |     |     |
| Packets         | Received          |                     |          | :                | 1        |             |     |     |
| Packet          | Loss              | in Test             |          | :                | 0.0000%  |             |     |     |
| Minimum         | RTT(ms)           |                     |          | :                | 20       |             |     |     |
| Maximum         | RTT(ms)           |                     |          | :                | 20       |             |     |     |
| Average         | RTT(ms)           |                     |          | :                | 20       |             |     |     |
| DNS RTT(ms)     |                   |                     |          | :                | 0        |             |     |     |
| TCP RTT(ms)     |                   |                     |          | :                | 12       |             |     |     |
| TLS RTT(ms)     |                   |                     |          | :                | 8        |             |     |     |
| switch(config)# |                   | show ip-sla         | http-sla |                  |          |             |     |     |
| IP-SLA          | Name              |                     | :        | http-sla         |          |             |     |     |
| Status          |                   |                     | :        | running          |          |             |     |     |
| IP-SLA          | Type              |                     | :        | http             |          |             |     |     |
| VRF             |                   |                     | :        | ipslasrc         |          |             |     |     |
| Source          | IP                |                     | :        | 2.2.2.2          |          |             |     |     |
| Source          | Interface         |                     | :        |                  |          |             |     |     |
| Domain          | Name              | Server              | :        | 10.10.10.2       |          |             |     |     |
| Probe           | Interval(seconds) |                     | :        | 90               |          |             |     |     |
| HTTP            | Request           | Type                | :        | get              |          |             |     |     |
| HTTP/HTTPS      |                   | URL                 | :        | abcd.com/ws/home |          |             |     |     |
| Cache           |                   |                     | :        | Enabled          |          |             |     |     |
| HTTP            | Proxy             | URL                 | :        |                  |          |             |     |     |
| HTTP            | Version           | Number              | :        | 1.1              |          |             |     |     |
```
| ##### IP-SLA |     | status description |     |     |     |     |     |     |
| ------------ | --- | ------------------ | --- | --- | --- | --- | --- | --- |
```
| | Status |     |     |     | | Description |     |     |     | |   |
| -------- | --- | --- | --- | ------------- | --- | --- | --- | --- |
|-------------------------|------------------------------------------------|
| | running |     |     |     | | SLA is | fully | operational |     | |   |
| --------- | --- | --- | --- | -------- | ----- | ----------- | --- | --- |
| Bind Error | Another service is using the same source port |
| | Interface |     | Down |     | | Interface | status | is not | up  |     |
| ----------- | --- | ---- | --- | ----------- | ------ | ------ | --- | --- |
| Dns Resolution Error | Failed to resolve destination hostname |
| | No       | Route |       |     | | No available |          | route to the | responder   | |   |
| ---------- | ----- | ----- | --- | -------------- | -------- | ------------ | ----------- | --- |
| | Internal |       | Error |     | | Unexpected   | error    | prevents     | SLA session | |   |
| | Disabled |       |       |     | | SLA is       | disabled |              |             | |   |
|Configuration Incomplete | Configuration is not complete to enable the SLA|
```
| ##### IP | SLA | session cumulative |     | counters | description |     |     |     |
| -------- | --- | ------------------ | --- | -------- | ----------- | --- | --- | --- |
```
| | Status |     |     |     | |   | Description |     |     |     |
| -------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
|
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 38

|--------------------------------|--------------------------------------------
------------------------------|
|Probes Timed-out | Total numbers of probes failed to receive
| response. |        |       |                 |     | |               |           |              |        |
| --------- | ------ | ----- | --------------- | --- | --------------- | --------- | ------------ | ------ |
|           | |Bind  | Error |                 |     | | Total numbers | of probes | transmission | failed |
| as        | source | port  | not available.| |     |                 |           |              |        |
|Destination Address Unreachable | Total numbers of probes transmission failed
| due | to route | unavailable. |     | |   |     |     |     |     |
| --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
|DNS Resolution Failures | Total numbers of probes failed due to DNS
| resolution     |               | failure.    |               |     | |                                     |           |            |     |
| -------------- | ------------- | ----------- | ------------- | --- | ------------------------------------- | --------- | ---------- | --- |
|                | |Reception    |             | Error         |     | | Total numbers                       | of probes | failed due | to  |
| internal       |               | error       | in reception. |     | |                                     |           |            |     |
|                | |Transmission |             | Error         |     | | Total numbers                       | of probes | failed due | to  |
| internal       |               | errr in     | transmission. |     | |                                     |           |            |     |
| Command        |               | History     |               |     |                                       |           |            |     |
| Release        |               |             |               |     | Modification                          |           |            |     |
| 10.12.1000     |               |             |               |     | UpdatedtodisplayhttpsasanIP-SLA type. |           |            |     |
| 10.07orearlier |               |             |               |     | --                                    |           |            |     |
| Command        |               | Information |               |     |                                       |           |            |     |
| Platforms      |               | Command     | context       |     | Authority                             |           |            |     |
6200 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
|     |     | (#) |     |     | rightsforthiscommand. |     |     |     |
| --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
IP-SLA|39

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
40
AOS-CX10.13MonitoringGuide|(6200SwitchSeries)

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
| 6200 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
| show interface |                       |     |     |        |             |
| -------------- | --------------------- | --- | --- | ------ | ----------- |
| show interface | [<IFNNAME>|<IFRANGE>] |     |     | [brief | | physical] |
show interface [<IFNNAME>|<IFRANGE>] [extended [non-zero] | [human-readable]]
| show interface | [<IFNNAME>] |     | monitor | [human-readable] |     |
| -------------- | ----------- | --- | ------- | ---------------- | --- |
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief]
show interface lag [<LAG-ID>] [extended [non-zero] | [human-readable]]
| show interface | lag | [<LAG-ID>] | monitor | [human-readable] |     |
| -------------- | --- | ---------- | ------- | ---------------- | --- |
Description
Showsactiveconfigurationsandoperationalstatusinformationforinterfaces.
| Parameter |     |     |     | Description              |     |
| --------- | --- | --- | --- | ------------------------ | --- |
| <IFNAME>  |     |     |     | Specifiesainterfacename. |     |
<IFRANGE>
Specifiestheportidentifierrange.
| brief |     |     |     | Showsbriefinfointabularformat. |     |
| ----- | --- | --- | --- | ------------------------------ | --- |
physical
Showsthephysicalconnectioninfointabularformat.
extended Showsadditionalstatistics,includingthetxfilteredandrx
filteredcounters.
n Rxfilterpacketsareprotocolpacketsreceivedwhenthe
protocolisdisabledontheswitchandthereisonlyoneportin
theVLAN.ProtocolsincludeOSPF,PIM,RIP,LACP,andLLDP.
n AnexampleofaTxfilteredpacketwouldbeamulticastpacket
beingfilteredfromgoingoutoftheingressport.
L1-100Mbpsdownshift|41

Parameter Description
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
non-zero
Showsonlynonzerostatistics.
LAG ShowsLAGinterfaceinformation.
monitor
Continuouslymonitorinterfacestatistics.
LOOPBACK Showsloopbackinterfaceinformation.
TUNNEL
Showstunnelinterfaceinformation.
VLAN ShowsVLANinterfaceinformation.
<LAG-ID>
SpecifiestheLAGnumber.Range:1-256
<LOOPBACK-ID> SpecifiestheLOOPBACKnumber.Range:0-255
<TUNNEL-ID>
SpecifiesthetunnelID.Range:1-255
<VLAN-ID> SpecifiestheVLANID.Range:1-4094
VXLAN
ShowstheVXLANinterfaceinformation.
<VXLAN-ID> SpecifiestheVXLANinterfaceidentifier.Default:1
Examples
Showinginformationwheninterface1/1/1isconfigured:
| MDI mode:       | MDIX            |             |     |       |         |
| --------------- | --------------- | ----------- | --- | ----- | ------- |
| VLAN Mode:      | native-untagged |             |     |       |         |
| Native VLAN:    | 1               |             |     |       |         |
| Allowed VLAN    | List: all       |             |     |       |         |
| Rate collection | interval:       | 300 seconds |     |       |         |
| Rates           |                 | RX          | TX  | Total | (RX+TX) |
------------- -------------------- -------------------- --------------------
| Mbits / sec |     | 0.00 | 0.00 |     | 0.00  |
| ----------- | --- | ---- | ---- | --- | ----- |
| KPkts / sec |     | 0.00 | 0.00 |     | 0.00  |
| Unicast     |     | 0.00 | 0.00 |     | 0.00  |
| Multicast   |     | 0.00 | 0.00 |     | 0.00  |
| Broadcast   |     | 0.00 | 0.00 |     | 0.00  |
| Utilization | %   | 0.00 | 0.00 |     | 0.00  |
| Statistics  |     | RX   | TX   |     | Total |
------------- -------------------- -------------------- --------------------
| Packets   |     | 0   | 0   |     | 0   |
| --------- | --- | --- | --- | --- | --- |
| Unicast   |     | 0   | 0   |     | 0   |
| Multicast |     | 0   | 0   |     | 0   |
| Broadcast |     | 0   | 0   |     | 0   |
| Bytes     |     | 0   | 0   |     | 0   |
| Jumbos    |     | 0   | 0   |     | 0   |
| Dropped   |     | 0   | 0   |     | 0   |
| Filtered  |     | 0   | 0   |     | 0   |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 42

| Pause     | Frames |     |     |     | 0   |     |     |     | 0   |     |     | 0   |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Errors    |        |     |     |     | 0   |     |     |     | 0   |     |     | 0   |
| CRC/FCS   |        |     |     |     | 0   |     |     | n/a |     |     |     | 0   |
| Collision |        |     |     |     | n/a |     |     |     | 0   |     |     | 0   |
| Runts     |        |     |     |     | 0   |     |     | n/a |     |     |     | 0   |
| Giants    |        |     |     |     | 0   |     |     | n/a |     |     |     | 0   |
Showinginformationwhentheinterfaceiscurrentlylinkedatadownshiftedspeed:
| switch(config-if)# |     |       | show  | interface | 1/1/1 |     |     |     |     |     |     |     |
| ------------------ | --- | ----- | ----- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Interface          |     | 1/1/1 | is up |           |       |     |     |     |     |     |     |     |
...
| Auto-negotiation |     |     | is on with | downshift |     | active |     |     |     |     |     |     |
| ---------------- | --- | --- | ---------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- |
Showinginformationwhentheinterfaceiscurrentlylinkedwithenergy-efficient-ethernetnegotiated:
| switch(config-if)# |     |       | show  | interface | 1/1/1 |     |     |     |     |     |     |     |
| ------------------ | --- | ----- | ----- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Interface          |     | 1/1/1 | is up |           |       |     |     |     |     |     |     |     |
...
| Energy-Efficient |     |     | Ethernet | is  | enabled | and active |     |     |     |     |     |     |
| ---------------- | --- | --- | -------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
ShowinginformationwhentheinterfaceisconfiguredwithEEEandtheEEEhasauto-negotiated:
| switch(config-if)# |     |     | show | interface | 1/1/1 | physical |     |     |     |     |     |     |
| ------------------ | --- | --- | ---- | --------- | ----- | -------- | --- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
----------------------------------------------------------
|        |     |        |           | Link   |             | Admin  |        | Speed       |        |        | Flow-Control |        |
| ------ | --- | ------ | --------- | ------ | ----------- | ------ | ------ | ----------- | ------ | ------ | ------------ | ------ |
|        | EEE |        | PoE Power |        |             |        | Port   |             |        |        |              |        |
| Port   |     | Type   |           | Status |             | Config | Status | |           | Config | Status | |            | Config |
| Status | |   | Config | (Watts)   | State  | Information |        |        | Description |        |        |              |        |
----------------------------------------------------------------------------------
----------------------------------------------------------
| 1/1/1 |     | 1GbT |     | up          |     | up  | 1G  |     | auto | off |     | off |
| ----- | --- | ---- | --- | ----------- | --- | --- | --- | --- | ---- | --- | --- | --- |
| on    |     | on   | --  | 10M/100M/1G |     |     |     | --  |      |     |     |     |
Showingthemonitorinformation:
Inmonitormode,theCLI refreshesdataautomaticallyuntilitisexitedbyenteringq.Pressing?opensthehelp
menutodisplaywhichoptionsareavailableinthiscontext.
| Interface |     | 1/1/1 | is up |     |     |     |     |     |     |     |       |         |
| --------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- |
| Rate      |     |       |       |     |     | RX  |     |     | TX  |     | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| MBits       | / sec |     |     |     | 30196.43 |     |     | 30196.43 |       |     | 60392.85  |         |
| ----------- | ----- | --- | --- | --- | -------- | --- | --- | -------- | ----- | --- | --------- | ------- |
| MPkts       | / sec |     |     |     | 58977.39 |     |     | 58977.40 |       |     | 117954.79 |         |
| Unicast     |       |     |     |     | 0.00     |     |     |          | 0.00  |     |           | 0.00    |
| Multicast   |       |     |     |     | 58977.39 |     |     | 58977.40 |       |     | 117954.79 |         |
| Broadcast   |       |     |     |     | 0.00     |     |     |          | 0.00  |     |           | 0.00    |
| Utilization |       | %   |     |     | 75.49    |     |     |          | 75.49 |     |           | 150.98  |
| Statistic   |       |     |     |     |          | RX  |     |          | TX    |     | Total     | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Packets |     |     |     | 4756527649 |     |     |     | 4756527865 |     |     | 9513055514 |     |
| ------- | --- | --- | --- | ---------- | --- | --- | --- | ---------- | --- | --- | ---------- | --- |
| Unicast |     |     |     |            |     | 0   |     |            | 0   |     |            | 0   |
L1-100Mbpsdownshift|43

| Multicast    |                |            | 4756527649   |     | 4756527865   |     | 9513055514   |     |
| ------------ | -------------- | ---------- | ------------ | --- | ------------ | --- | ------------ | --- |
| Broadcast    |                |            |              | 2   |              | 0   |              | 2   |
| Bytes        |                |            | 304417778668 |     | 304417795428 |     | 608835574096 |     |
| Jumbos       |                |            |              | 0   |              | 0   |              | 0   |
| Dropped      |                |            |              | 0   | 19028847730  |     | 19028847730  |     |
| Pause Frames |                |            |              | 0   |              | 0   |              | 0   |
| Errors       |                |            |              | 0   |              | 0   |              | 0   |
| CRC/FCS      |                |            |              | 0   |              | n/a |              | 0   |
| help: ?,     | quit: q        |            |              |     |              |     |              |     |
| Help for     | Interface      | Monitor    |              |     |              |     |              |     |
| h Toggle     | human-readable |            | mode         |     |              |     |              |     |
| c Clear      | interface      | statistics |              |     |              |     |              |     |
| Does not     | apply to       | rates      |              |     |              |     |              |     |
| Arrows,      | PgUp, PgDn,    | Home,      | End          |     |              |     |              |     |
| Navigate     | interface      | statistics |              |     |              |     |              |     |
Delay: 2
| help: ?, | quit: q |     |     |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Showingtheoutputforinterface1/1/1inhuman-readableformat:
Inhuman-readableformat,the<1symbolforUtilizationindicatesthattheamountofpacketsisbetweenzero
andone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsandthe
Utilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
| switch(config-if)# |       | show  | interface | 1/1/1 human-readable |     |     |       |         |
| ------------------ | ----- | ----- | --------- | -------------------- | --- | --- | ----- | ------- |
| Interface          | 1/1/1 | is up |           |                      |     |     |       |         |
| Rate               |       |       |           | RX                   |     | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Bits /      | sec |     |     | 3M  |     | 3M  |     | 6M    |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ----- |
| Pkts /      | sec |     |     | 316 |     | 316 |     | 633   |
| Unicast     |     |     |     | 319 |     | 319 |     | 638   |
| Multicast   |     |     |     | 0   |     | 0   |     | 0     |
| Broadcast   |     |     |     | 0   |     | 0   |     | 0     |
| Utilization | %   |     |     | < 1 |     | < 1 |     | < 1   |
| Statistic   |     |     |     | RX  |     | TX  |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     |     | 577K |     | 577K |     | 1M  |
| ------------ | --- | --- | --- | ---- | --- | ---- | --- | --- |
| Unicast      |     |     |     | 577K |     | 577K |     | 1M  |
| Multicast    |     |     |     | 0    |     | 51   |     | 51  |
| Broadcast    |     |     |     | 0    |     | 15   |     | 15  |
| Bytes        |     |     |     | 744M |     | 745M |     | 1G  |
| Jumbos       |     |     |     | 0    |     | 0    |     | 0   |
| Dropped      |     |     |     | 0    |     | 0    |     | 0   |
| Filtered     |     |     |     | 0    |     | 0    |     | 0   |
| Pause Frames |     |     |     | 0    |     | 0    |     | 0   |
| Errors       |     |     |     | 0    |     | 0    |     | 0   |
| CRC/FCS      |     |     |     | 0    |     | n/a  |     | 0   |
| Collision    |     |     |     | n/a  |     | 0    |     | 0   |
| Runts        |     |     |     | 0    |     | n/a  |     | 0   |
| Giants       |     |     |     | 0    |     | n/a  |     | 0   |
Showinginformationaboutextendedcounters:
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 44

Theoutputoftheshow interface extendedcommandvariesdependingontheswitchmodeland
configuration.
| switch(config-if)# |     | show | interface |     | 1/1/17 extended |     |
| ------------------ | --- | ---- | --------- | --- | --------------- | --- |
-------------------------------------------------------------------
| Interface | 1/1/17 |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- |
-------------------------------------------------------------------
| Statistics |     |     |     |     |     | Value |
| ---------- | --- | --- | --- | --- | --- | ----- |
-------------------------------------------------------------------
| Dot1d Tp | Port In         | Frames |         |     |     | 547   |
| -------- | --------------- | ------ | ------- | --- | --- | ----- |
| Dot1d Tp | Port Out        | Frames |         |     |     | 608   |
| Dot3 In  | Pause Frames    |        |         |     |     | 0     |
| Dot3 Out | Pause Frames    |        |         |     |     | 0     |
| Ethernet | Stats Broadcast |        | Packets |     |     | 19    |
| Ethernet | Stats Bytes     |        |         |     |     | 40162 |
| Ethernet | Stats Packets   |        |         |     |     | 342   |
...
-------------------------------------------------------------------
| Error-Statistics |     |     |     |     |     | Value |
| ---------------- | --- | --- | --- | --- | --- | ----- |
-------------------------------------------------------------------
| Dot1d Base   | Port        | MTU Exceeded |          | Discards |        | 0   |
| ------------ | ----------- | ------------ | -------- | -------- | ------ | --- |
| Dot3 Control | In          | Unknown      | Opcodes  |          |        | 0   |
| Dot3 Stats   | Alignment   |              | Errors   |          |        | 0   |
| Dot3 Stats   | FCS Errors  |              |          |          |        | 0   |
| Dot3 Stats   | Frame       | Too          | Longs    |          |        | 0   |
| Dot3 Stats   | Internal    | Mac          | Transmit |          | Errors | 0   |
| Ethernet     | RX Oversize |              | Packets  |          |        | 0   |
...
| Command | History |     |     |     |              |     |
| ------- | ------- | --- | --- | --- | ------------ | --- |
| Release |         |     |     |     | Modification |     |
10.11
Addedmonitorparameter.
| 10.10          |             |     |         |     | Addedhuman-readableparameter. |     |
| -------------- | ----------- | --- | ------- | --- | ----------------------------- | --- |
| 10.07orearlier |             |     |         |     | --                            |     |
| Command        | Information |     |         |     |                               |     |
| Platforms      | Command     |     | context |     | Authority                     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show interface |     | statistics |     |     |     |     |
| -------------- | --- | ---------- | --- | --- | --- | --- |
show interface [<IFNAME>|<IFRANGE>] statistics [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] statistics monitor [non-zero] [human-readable]
L1-100Mbpsdownshift|45

show interface [<IFNAME>|<IFRANGE>] error-statistics [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] error-statistics monitor [non-zero] [human-readable]
show interface lag [<LAG-ID>] statistics [non-zero] [human-readable]
show interface lag [<LAG-ID>] statistics monitor [non-zero] [human-readable]
show interface lag [<LAG-ID>] error-statistics [non-zero] [human-readable]
show interface lag [<LAG-ID>] error-statistics monitor [non-zero] [human-readable]
show interface vxlan <VXLAN-ID> statistics [non-zero] [human-readable]

Description

Shows statistics for switch interfaces such as packets transmitted and received, bytes transmitted and
received, broadcast and multicast packets.

Parameter

<IFNAME>

<IFRANGE>

LAG

<LAG-ID>

VXLAN

<VXLAN-ID>

monitor

human-readable

non-zero

Examples

Showing statistics of all interfaces:

Description

Specifies a interface name.

Specifies the port identifier range.

Shows LAG interface information.

Specifies the LAG number. Range: 1-256

Shows the VXLAN interface information.

Specifies the VXLAN interface identifier. Default: 1

Continuously monitor interface statistics.

Shows statistics rounded to the nearest power of 1000, for
example, 1K, 345M, 2G.

Shows only non zero statistics.

Showing statistics of all interfaces with only non-zero statistics:

Showing statistics of all interfaces in the human-readable format:

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

46

Showing statistics of a single interfaces:

Showing statistics of all members of a LAG interface:

Showing error statistics of all interfaces:

Showing monitor statistics:

The rows and columns of show interface monitor statistics depends on the length of width of the client terminal.

The CLI can be navigated using the arrow keys as well as the PageUp, PageDown, Home, and End keys.

L1-100Mbps downshift | 47

Showing monitor error statistics in human-readable format:

Command History

Release

10.11

10.10

Modification

Added moitor parameter.

Added human-readable parameter.

10.07 or earlier

--

Command Information

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

48

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
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
L1-100Mbpsdownshift|49

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6200 config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show running-config |           | interface             |     |     |
| ------------------- | --------- | --------------------- | --- | --- |
| show running-config | interface | [<IFNNAME>|<IFRANGE>] |     |     |
show running-config interface [lag | loopback | tunnel | vlan ] [<ID>]
Description
Displaysactiveconfigurationsofvariousswitchinterfaces.
| Parameter     |     |     | Description                                     |     |
| ------------- | --- | --- | ----------------------------------------------- | --- |
| <IFNAME>      |     |     | Specifiesainterfacename.                        |     |
| <IFRANGE>     |     |     | Specifiestheportidentifierrange.                |     |
| LAG           |     |     | SpecifiesLAGinterfaceinformation                |     |
| LOOPBACK      |     |     | Specifiesloopbackinterfaceinformation.          |     |
| TUNNEL        |     |     | Specifiestunnelinterfaceinformation.            |     |
| VLAN          |     |     | SpecifiesVLANinterfaceinformation.              |     |
| <LAG-ID>      |     |     | SpecifiestheLAGnumber.Range:1-256.              |     |
| <LOOPBACK-ID> |     |     | SpecifiestheLOOPBACKnumber.Range:0-255.         |     |
| <TUNNEL-ID>   |     |     | SpecifiesthetunnelID.Range:1-255.               |     |
| <VLAN-ID>     |     |     | SpecifiestheVLANID.Range:1-4094.                |     |
| VXLAN         |     |     | SpecifiestheVXLANinterfaceinformation.          |     |
| <VXLAN-ID>    |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1. |     |
Examples
Showing1/1/2interfaceconfiguration:
| switch(config-if)# |       | show running-config | interface | 1/1/2 |
| ------------------ | ----- | ------------------- | --------- | ----- |
| interface          | 1/1/2 |                     |           |       |
| no shutdown        |       |                     |           |       |
| description        | DC-23 |                     |           |       |
exit
Showingloopbackinterfacesconfigured:
| switch(config-if)# |     | show running-config | interface | loopback |
| ------------------ | --- | ------------------- | --------- | -------- |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 50

| interface |             | loopback | 1            |     |     |     |
| --------- | ----------- | -------- | ------------ | --- | --- | --- |
|           | description |          | lb interface | 1   |     |     |
exit
| interface |             | loopback | 2            |     |     |     |
| --------- | ----------- | -------- | ------------ | --- | --- | --- |
|           | description |          | lb interface | 2   |     |     |
exit
Showingloopbackinterfacesnotconfigured:
| switch(config-if)# |             |            | show running-config |              | interface | loopback |
| ------------------ | ----------- | ---------- | ------------------- | ------------ | --------- | -------- |
| No                 | loopback    | interfaces | configured.         |              |           |          |
| Command            | History     |            |                     |              |           |          |
| Release            |             |            |                     | Modification |           |          |
| 10.07orearlier     |             |            |                     | --           |           |          |
| Command            | Information |            |                     |              |           |          |
| Platforms          |             | Command    | context             | Authority    |           |          |
6200 config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
L1-100Mbpsdownshift|51

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

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

52

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

Mirroring | 53

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
| clear mirror | endpoint |          |     |
| ------------ | -------- | -------- | --- |
| clear mirror | endpoint | [<NAME>] |     |
Description
Clearsmirrorendpointstatisticsforallconfiguredmirrorendpoints.Theoptionalparametercanbe
addedtoclearaspecificmirrorendpoint.
| Parameter |     |     | Description                                          |
| --------- | --- | --- | ---------------------------------------------------- |
| <NAME>    |     |     | Specifiesnameofthemirrorendpointinstancetobecleared. |
Examples
Clearingstatisticsforallconfiguredmirrorendpoints:
| switch# clear | mirror | endpoint |     |
| ------------- | ------ | -------- | --- |
Clearingmirrorstatisticsformirrorendpointtest:
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 54

| switch# clear       | mirror  | endpoint test |                                                    |
| ------------------- | ------- | ------------- | -------------------------------------------------- |
| Command History     |         |               |                                                    |
| Release             |         |               | Modification                                       |
| 10.07orearlier      |         |               | --                                                 |
| Command Information |         |               |                                                    |
| Platforms           | Command | context       | Authority                                          |
| 6200                |         |               | Administratorsorlocalusergroupmemberswithexecution |
Operator(>)orManager
|     | (#) |     | rightsforthiscommand. |
| --- | --- | --- | --------------------- |
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
Examples
Addingacommenttoamirrorsession:
switch(config-mirror-3)# comment This Mirror will be removed during next
| maintenance | window |     |     |
| ----------- | ------ | --- | --- |
Removingthecommentfrommirrorsession3:
| switch(config-mirror-3)# |     | no comment |     |
| ------------------------ | --- | ---------- | --- |
Addingacommenttoamirrorendpoint:
Mirroring|55

switch(config-mirror-endpoint-test)# comment Monitor endpoint traffic
Replacingtheexistingcommentformirrorendpoint:
switch(config-mirror-endpoint-test)# comment Monitor statistics on each endpoint
interfaces
| Command        | History     |         |              |           |     |     |
| -------------- | ----------- | ------- | ------------ | --------- | --- | --- |
| Release        |             |         | Modification |           |     |     |
| 10.07orearlier |             |         | --           |           |     |     |
| Command        | Information |         |              |           |     |     |
| Platforms      | Command     | context |              | Authority |     |     |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
|     | config-mirror-endpoint |     |     | executionrightsforthiscommand. |     |     |
| --- | ---------------------- | --- | --- | ------------------------------ | --- | --- |
copy tcpdump-pcap
| copy tcpdump-pcap | <FILE-NAME> | <REMOTE-URL> |     |     |     |     |
| ----------------- | ----------- | ------------ | --- | --- | --- | --- |
Description
Savespacketcapturefilestoexternalstorage.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<FILE-NAME>
Specifiesthepacketcapturefiletosave.
<REMOTE-URL> Specifiestheexternalstoragetowhichthepacketcapturefilewill
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
| Command              | History              |     |                    |          |           |       |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 56

| Release   |             |         | Modification      |     |     |     |
| --------- | ----------- | ------- | ----------------- | --- | --- | --- |
| 10.08     |             |         | Commandintroduced |     |     |     |
| Command   | Information |         |                   |     |     |     |
| Platforms | Command     | context | Authority         |     |     |     |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecution
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
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Mirroring|57

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
| switch(config-mirror-1)# |             |     | no      | destination |              | cpu       |
| ------------------------ | ----------- | --- | ------- | ----------- | ------------ | --------- |
| Command                  | History     |     |         |             |              |           |
| Release                  |             |     |         |             | Modification |           |
| 10.07orearlier           |             |     |         |             | --           |           |
| Command                  | Information |     |         |             |              |           |
| Platforms                | Command     |     | context |             |              | Authority |
6200 config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| destination    | interface |     |                             |     |     |     |
| -------------- | --------- | --- | --------------------------- | --- | --- | --- |
| destination    | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |     |     |
| no destination | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |     |     |
Description
Configuresthespecifiedinterfaceasthedestinationofthemirroredtraffic.
Thenoformofthiscommandimmediatelydisablesthemirroringsessionandremovesthespecified
destinationinterfacefromtheconfiguration.
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 58

| Parameter      |     |     |     |     | Description                                    |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesainterface.Format:member/slot/port.   |     |     |
| <LAG-NAME>     |     |     |     |     | SpecifiesaLAG(linkaggregationgroup)identifier. |     |     |
Usage
Configuringadifferentdestinationinterfaceinanenabledmirroringsessioncausesallmirroredtraffic
tousethenewdestinationinterface.Thisactionmightcauseatemporarysuspensionofmirrored
sourcetrafficduringthereconfiguration.
Examples
Configuringamirroringsessionandaddinganinterfaceasadestination:
| switch(config)#          |     | mirror | session     | 1   |           |     |       |
| ------------------------ | --- | ------ | ----------- | --- | --------- | --- | ----- |
| switch(config-mirror-1)# |     |        | destination |     | interface |     | 1/1/1 |
Replacingtheexistingdestinationwithdifferentinterface:
| switch(config-mirror-1)# |     |     | destination |     | interface |     | 1/1/12 |
| ------------------------ | --- | --- | ----------- | --- | --------- | --- | ------ |
Removingadestination:
| switch(config-mirror-1)# |     |     | no  | destination |     | interface | 1/1/12 |
| ------------------------ | --- | --- | --- | ----------- | --- | --------- | ------ |
Switch Destination interface limit per mirror session (4 possible sessions)
| 6200           | 64          |     |         |     |              |           |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --------- | --- |
| Command        | History     |     |         |     |              |           |     |
| Release        |             |     |         |     | Modification |           |     |
| 10.07orearlier |             |     |         |     | --           |           |     |
| Command        | Information |     |         |     |              |           |     |
| Platforms      | Command     |     | context |     |              | Authority |     |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| destination       | tunnel |               |            |        |                    |     |     |
| ----------------- | ------ | ------------- | ---------- | ------ | ------------------ | --- | --- |
| destination       | tunnel | <TUNNEL-IPV4> |            | source | <SOURCE-IPv4-ADDR> |     |     |
| dscp <DSCP-VALUE> |        | vrf           | <VRF-NAME> |        |                    |     |     |
| no destination    | tunnel |               |            |        |                    |     |     |
Description
Mirroring|59

Specifies the tunnel where all mirrored traffic for the session is transmitted. Only one tunnel destination
is allowed per session.

You may configure multiple mirror sessions with the same source/destination IP address pair, however,
only one of those sessions sharing the same source/destination IP address pair can be enabled at a
given time.

ERSPAN is not supported leaving the switch by the OOB port. If VRF management is configured for an
ERSPAN session, the session will be in "mirror_err_tunnel_oob_port_not_supported" operation status.

ERSPAN is not supported leaving the switch encapsulated within another tunnel (e.g. GRE IPv4). When
the path to the destination IP address will leave via a tunnel, the session will be in "tunnel_route_
resolution_not_populated" operation status.

The interface/LAG used to transmit ERSPAN packets should not be a source in the same mirror session.

The no form of this command will cease the use of the tunnel and disable the session.

Parameter

Description

<TUNNEL-IPV4-ADDR>

<SOURCE-IPv4-ADDR>

<DSCP-VALUE>

Specifies the tunnel address in IPv4 format (x.x.x.x), where x is a
decimal number from 0 to 255.

Specifies the source address in IPv4 format (x.x.x.x), where x is a
decimal number from 0 to 255.

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

Removing the destination:

switch(config-mirror-1)# no destination tunnel

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

60

| Command        | History     |              |           |     |
| -------------- | ----------- | ------------ | --------- | --- |
| Release        |             | Modification |           |     |
| 10.07orearlier |             | --           |           |     |
| Command        | Information |              |           |     |
| Platforms      | Command     | context      | Authority |     |
6200 config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
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
Sincefileanddelete-fileareoptional,thebehaviorofthebasecommanddiag utilities tsharkdoes
notsaveanythingtoafile,andinsteaddumpsthetsharksessiontotheconsoleuntilCTRL + cis
entered.
| Parameter |     | Description                           |     |     |
| --------- | --- | ------------------------------------- | --- | --- |
| file      |     | Savescapturedpacketstoatemporaryfile. |     |     |
delete-file
Deletesthemostrecentcapturedfile.
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
Mirroring|61

| Command   | Information |         |           |
| --------- | ----------- | ------- | --------- |
| Platforms | Command     | context | Authority |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 62

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

0000 0304 0006 0000 0000 0000 0000 86dd
6b8d 23c5 0014 1140 0000 0000 0000 0000
0000 0000 0000 0001 0000 0000 0000 0000
0000 0000 0000 0001 007b 9d7e 0014 0027

................
k.#....@........
................
.........{.~...'

Mirroring | 63

|     | 0x0040: d681 | 0001 c016 | 0000 0000 | 0000 |
| --- | ------------ | --------- | --------- | ---- |
Removingmy_capture_file.pcap:
switch# diag utilities tcpdump delete-file my_capture_file.pcap
| Successfully | removed     | file    |                   |     |
| ------------ | ----------- | ------- | ----------------- | --- |
| Command      | History     |         |                   |     |
| Release      |             |         | Modification      |     |
| 10.08        |             |         | Commandintroduced |     |
| Command      | Information |         |                   |     |
| Platforms    | Command     | context | Authority         |     |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecution
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
| switch(config)#          | mirror      | session | 3            |     |
| ------------------------ | ----------- | ------- | ------------ | --- |
| switch(config-mirror-3)# |             | disable |              |     |
| Command                  | History     |         |              |     |
| Release                  |             |         | Modification |     |
| 10.07orearlier           |             |         | --           |     |
| Command                  | Information |         |              |     |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 64

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
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
Configuringandenablingamirroringsession:
| switch(config)#          | mirror | session | 3         |          |
| ------------------------ | ------ | ------- | --------- | -------- |
| switch(config-mirror-3)# |        | source  | interface | 1/1/2 rx |
switch(config-mirror-3)#
|     |     | destination | interface | 1/1/3 |
| --- | --- | ----------- | --------- | ----- |
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
Mirroring|65

Description
Createsamirroringsessionconfigurationcontextorentersanexistingmirroringsessionconfiguration
context.
Fromthiscontext,youcanentercommandstoconfigureandenableordisablethemirroringsession.
Thenoformofthiscommandremovesanexistingmirroringsessionfromtheconfiguration.
| Parameter    |     |     | Description                              |
| ------------ | --- | --- | ---------------------------------------- |
| <SESSION-ID> |     |     | Specifiesthesessionidentifier.Range:1to4 |
Examples
| switch(config)# | mirror | session | 1   |
| --------------- | ------ | ------- | --- |
switch(config-mirror-1)#
switch(config)#
|     | mirror | session | 3   |
| --- | ------ | ------- | --- |
switch(config-mirror-3)#
| switch(config)# | no  | mirror session | 1   |
| --------------- | --- | -------------- | --- |
switch(config)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| mirror endpoint    |        |     |     |
| ------------------ | ------ | --- | --- |
| mirror endpoint    | <NAME> |     |     |
| no mirror endpoint | <NAME> |     |     |
Description
Createsthespecifiedmirrorendpointorentersitscontextifitalreadyexists.Thespecificsofamirror
endpointarecreatedoralteredwhileinthemirrorendpointcontextandthemirrorendpointisenabled
ordisabledfromthiscontext.ItmaybepossibletosupportdifferentencapsulationsbydifferentASICs.
Forexample,UDPforPVOScompatibility.TerminationofGREencapsulationisalsosupported.
Thenoformofthiscommandremovesanexistingmirrorendpoint.Anenabledmirrorendpointis
automaticallydisabledfirstbeforeremoval.
| Parameter |     |     | Description                  |
| --------- | --- | --- | ---------------------------- |
| <NAME>    |     |     | Specifiesmirrorendpointname. |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 66

Examples
Creatingamirrorendpointnamedtest:
switch(config)#
|     | mirror | endpoint |     | test |     |     |
| --- | ------ | -------- | --- | ---- | --- | --- |
Deletingmirrorendpointnamedtest:
| switch(config)# | no  | mirror endpoint |     | test |     |     |
| --------------- | --- | --------------- | --- | ---- | --- | --- |
Configuringamirrorendpointnamedtest:
| 6100(config)# | mirror | endpoint | test |     |     |     |
| ------------- | ------ | -------- | ---- | --- | --- | --- |
6100(config-mirror-endpoint-test)#
| 6100(config-mirror-endpoint-test)# |         |            |     | destination     |           |     |
| ---------------------------------- | ------- | ---------- | --- | --------------- | --------- | --- |
| interface                          | Specify | interfaces |     | to send traffic |           |     |
| 6100(config-mirror-endpoint-test)# |         |            |     | destination     | interface |     |
IFNAMELIST An interface, a range or a comma seperated list of interfaces
| 6100(config-mirror-endpoint-test)# |     |     |     | destination | interface | 1/1/3 |
| ---------------------------------- | --- | --- | --- | ----------- | --------- | ----- |
<cr>
| 6100(config-mirror-endpoint-test)# |     |     |     | destination | interface | 1/1/3 |
| ---------------------------------- | --- | --- | --- | ----------- | --------- | ----- |
6100(config-mirror-endpoint-test)#
6100(config-mirror-endpoint-test)# source 1.1.1.1 destination 1.1.1.2 id 1 vrf
default
6100(config-mirror-endpoint-test)#
Onlyphysicalportscanbeconfiguredasinterfaceformirror-endpointdestination.LAGportisnotsupportedas
interfaceformirror-endpointdestination.
Themaximumallowednumberofdestinationinterfacesforbothmirror-sessionandmirror-endpointis1.
| Command History     |         |         |     |                                            |     |     |
| ------------------- | ------- | ------- | --- | ------------------------------------------ | --- | --- |
| Release             |         |         |     | Modification                               |     |     |
| 10.13.1000          |         |         |     | Addedsupportfor4100i,6000,and6100switches. |     |     |
| 10.07orearlier      |         |         |     | --                                         |     |     |
| Command Information |         |         |     |                                            |     |     |
| Platforms           | Command | context |     | Authority                                  |     |     |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show mirror
| show mirror | [<SESSION-ID>] |     |     |     |     |     |
| ----------- | -------------- | --- | --- | --- | --- | --- |
Description
Mirroring|67

Shows information about mirroring sessions. If <SESSION-ID> is not specified, then the command shows
a summary of all configured mirroring sessions. If <SESSION-ID> is specified, then the command shows
detailed information about the specified mirroring session.

Parameter

<SESSION-ID>

Usage

Description

Specifies the session identifier. Range: 1 to 4

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

Showing summary information about all configured mirroring sessions:

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

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

68

| switch# show    | mirror    | 3        |       |              |     |         |
| --------------- | --------- | -------- | ----- | ------------ | --- | ------- |
| Mirror Session: |           | 3        |       |              |     |         |
| Admin Status:   |           | disable  |       |              |     |         |
| Operation       | Status:   | disabled |       |              |     |         |
| Comment:        | Monitor   | router   | port  | ingress-only |     | traffic |
| Source:         | interface | 1/1/2    | rx    |              |     |         |
| Destination:    | interface |          | 1/1/3 |              |     |         |
| Output Packets: |           | 0        |       |              |     |         |
| Output Bytes:   |           | 0        |       |              |     |         |
switch#
| Command History     |         |     |         |     |              |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- |
| Release             |         |     |         |     | Modification |     |
| 10.07orearlier      |         |     |         |     | --           |     |
| Command Information |         |     |         |     |              |     |
| Platforms           | Command |     | context |     | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show mirror | endpoint |          |     |     |     |     |
| ----------- | -------- | -------- | --- | --- | --- | --- |
| show mirror | endpoint | [<NAME>] |     |     |     |     |
Description
Showsalistofallconfiguredmirrorendpoints,theirAdminStatusandtheirOperationStatus.
Theoptionalparameterwilldisplaythedetailsofthespecifiedmirrorendpointifitexists.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<NAME>
Specifiesnameofthemirrorendpointinstancetobedisplayed.
Examples
Showingasummaryofallconfiguredmirrorendpointsontheswitch:
| switch# show | mirror | endpoint |           |     |        |     |
| ------------ | ------ | -------- | --------- | --- | ------ | --- |
| Name Admin   | Status |          | Operation |     | Status |     |
----- -------------- ----------------------------------------------------
| test enable     |     |     | enabled  |     |     |     |
| --------------- | --- | --- | -------- | --- | --- | --- |
| monitor disable |     |     | disabled |     |     |     |
Showingthedetailsofenabledmirrorendpointtest:
| switch# show     | mirror | endpoint |     | test |     |     |
| ---------------- | ------ | -------- | --- | ---- | --- | --- |
| Mirror Endpoint: |        | audit    |     |      |     |     |
| Admin Status:    | enable |          |     |      |     |     |
Mirroring|69

| Operation       | Status: enabled |             |         |                  |
| --------------- | --------------- | ----------- | ------- | ---------------- |
| Comment:        | Mirror Endpoint | Audit       |         |                  |
| Type: gre       |                 |             |         |                  |
| Tunnel: source  | 1.1.1.1         | destination | 1.1.1.2 | id 1 vrf default |
| Interface:      | 1/1/3           |             |         |                  |
| Output Packets: | 123456789       |             |         |                  |
| Output Bytes:   | 0               |             |         |                  |
"OutputPackets"in"showmirrorendpoint[name]"isonlysupportedforstatistics.
"OutputBytes"in"showmirrorendpoint[name]"isnotsupportedduetoASIClimitation.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
4100i Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| 6000 | (#) |     |     |     |
| ---- | --- | --- | --- | --- |
6100
6200
shutdown
shutdown
no shutdown
Description
Enablesmirrorendpointfromitsdefaultdisabledstate.Toverifythemirrorendpointwassuccessfully
activated,runtheshow mirror endpoint NAMEcommandandverifythattheAdmin Statusand
Operational Statushaschangedfromdisabledtoenabled.Ifthestatusvalueremainsdisabled,
consultthesystemlogstodeterminethereasonforactivationfailure.Todisablethemirrorendpoint,
firstdisabletheremotemirrorsessionontheswitchthat'soriginatingthedata.Next,usetheshutdown
commandtodisablethemirrorendpoint.
Examples
Enablingamirrorendpoint:
| switch(config)#                      | mirror | endpoint | test        |     |
| ------------------------------------ | ------ | -------- | ----------- | --- |
| switch(config-mirror-endpoint-test)# |        |          | no shutdown |     |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 70

Disablingamirrorendpoint:
| switch(config)#                      | mirror  | endpoint | test         |
| ------------------------------------ | ------- | -------- | ------------ |
| switch(config-mirror-endpoint-test)# |         |          | shutdown     |
| Command History                      |         |          |              |
| Release                              |         |          | Modification |
| 10.07orearlier                       |         |          | --           |
| Command Information                  |         |          |              |
| Platforms                            | Command | context  | Authority    |
config
| 6200 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
source
source <SOURCE-IP> destination <DESTINATION-IP> id <1-4294967295> [vrf <VRF_NAME>] [type
{gre}]
no source
Description
Configurestunnelparametersofthemirrorendpoint.Configuringatunnelparametertoamirror
endpointwillreplacetheexistingconfiguration.BydefaulttheVRFisdefault,userscanalsoexplicitly
provideacustomVRF.ThedefaulttunneltypeisconsideredtobeGREandusersalsohavetheoptionto
explicitlygivetypeasGRE.
Thenoformremovesthetunnelparametersofthemirrorendpoint.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<SOURCE-IP>
SpecifiesL3encapsulatedIPv4sourceintheformA.B.C.D.
<DESTINATION-IP> SpecifiesL3encapsulatedIPv4destinationintheformA.B.C.D.
id
Specifiestunnelidentifierfromtheencapsulatedpacket.
| <VRF_NAME> |     |     | SpecifiesthenameofVRF forwhichthetunnelbelongsto. |
| ---------- | --- | --- | ------------------------------------------------- |
Examples
Configuringatunnelparametertoamirrorendpoint:
switch(config-mirror-endpoint-test)# source 1.1.1.1 destination 7.7.7.7 id 1 vrf
| default type    | gre |     |     |
| --------------- | --- | --- | --- |
| Command History |     |     |     |
Mirroring|71

| Release        |             |         |         |     | Modification |     |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |             |         |         |     | --           |     |     |     |
| Command        | Information |         |         |     |              |     |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |     |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
| 6200 |     |     |     | 64       |     |           |     |     |
However,thereisapracticallimittotheamountoftrafficthatamirrordestinationcantransmit.For
example,mirroringsessionwithmultiple10Gsourcescanoverwhelmasingle10Gdestination.
Whenadding,removing,orchangingtheconfigurationofasourceportinanenabledmirroringsession,packets
fromothermirrorsourcesusingthesamedestinationportmightbeinterrupted.
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 72

Examples
Configuringamirroredtrafficsourceinterface:
switch(config-mirror-1)#
source interface
| LAG-NAME | Enter | a LAG  | name. For | example, | lag10 |
| -------- | ----- | ------ | --------- | -------- | ----- |
| PORT-NUM | Enter | a port | number    |          |       |
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
switch(config-mirror-4)#
|     |     | no  | source | interface | lag1 rx |
| --- | --- | --- | ------ | --------- | ------- |
Command History
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
Command Information
Mirroring|73

Platforms

Command context

Authority

All platforms

config-mirror-<SESSION-ID>

Administrators or local user group members with
execution rights for this command.

source vlan
source vlan <VLAN-NUM> {rx | tx | both}
no source vlan <VLAN-NUM> {rx | tx | both}

Description

Mirroring with VLAN as a source is supported in the following traffic directions:

n both - traffic received and transmitted

n rx - only received traffic

n tx - only transmitted traffic

More than one source VLAN can be configured in a mirror session. Each such VLAN may specify its own
direction.

There is a limit of 1024 source VLANs for a given mirror session. There is also a limit of 4096 source
VLANs across all mirror sessions.

When changing a source VLAN in an enabled mirror session (i.e. adding, changing direction, or removing)

mirrored packets being transmitted out of the mirror destination port from other mirror sources may be briefly

interrupted during the reconfiguration.

Direction of an existing source VLAN can be updated in one of two ways.

n Reenter the source vlan <VLAN-NUM> <direction> command with the new preferred direction.

n Use the no source vlan <VLAN-NUM> <direction> form of the command with a direction (rx or tx)

to selectively remove the specified direction.

Specifying the last remaining direction for that VLAN will remove the VLAN from the configuration
entirely.

Mirroring allows configuration of VLAN as a source. When VLAN source is configured in the rx direction,
all packets are mirrored as they are received in the switch. When VLAN source is configured in tx
direction, all packets are mirrored as they are transmitted out of the switch.

For packets bridged through the switch:

n If the mirror is configured in 'both' direction, two copies of packets are mirrored, otherwise one copy

of the packet will be mirrored.

For routed packets:

n If the mirror is configured in rx direction, packets are mirrored in the pre-routed form with the

Destination MAC address as the switch address.

n If the mirror is configured in tx direction, packets are mirrored in post-routed form with the source

MAC as the switch address. Destination MAC is the nexthop gateway or station.

n If the mirror is configured in both direction, one copy of the packet will be mirrored.

Control plane packets generated by the switch's CPU are processed both in theingress and the egress
packet processing pipeline. The following are the behavior for mirroring with VLAN as source:

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

74

n Ifthemirrorisconfiguredintherxortxdirection,thepacketsaremirroredtothemirror
destination.
n Ifthemirrorisconfiguredinthebothdirection,twocopiesofthepacketsaremirroredtothemirror
destination.
ThenoformcommandwillceasemirroringtrafficfromthespecifiedsourceVLANandremovethe
sourcefromthemirrorconfiguration.
| Parameter |     | Description           |
| --------- | --- | --------------------- |
| VLAN-NUM  |     | SelectstheVLANnumber. |
direction Specifiesthedirectionofmirroring.tx(transmit),rx(receive),or
both.
Examples
CreatingamirrorsessionandaddingaVLANasasourceoftrafficinbothdirectionsonthatport:
| switch# configure | terminal |     |
| ----------------- | -------- | --- |
switch(config)#
|                          | mirror session | 1            |
| ------------------------ | -------------- | ------------ |
| switch(config-mirror-1)# | source         | vlan 10 both |
CreatingamirrorsessionandaddingtwoVLANsassourcesoftraffic:
directions:
| switch# configure        | terminal       |            |
| ------------------------ | -------------- | ---------- |
| switch(config)#          | mirror session | 2          |
| switch(config-mirror-2)# | source         | vlan 10 tx |
switch(config-mirror-2)#
source vlan 20 both
Configuringthesourceinsession2toreceivebyspecifyingthesourceinterfaceconfiguration:
| switch(config-mirror-2)# | source | vlan 10 rx |
| ------------------------ | ------ | ---------- |
Removingthefirstsourceinterfaceinsession2entirely,andremovingthetransmitdirectionfromthe
othersothatmirroringonlyoccursinthereceivedirection:
| switch(config-mirror-2)# | source | vlan 10 rx |
| ------------------------ | ------ | ---------- |
| switch(config-mirror-2)# | source | vlan 20 tx |
Command History
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
Command Information
Mirroring|75

Platforms

Command context

Authority

6200

config

Administrators or local user group members with execution
rights for this command.

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

76

Chapter 9
|            |          |            | Monitoring | a device | using SNMP |
| ---------- | -------- | ---------- | ---------- | -------- | ---------- |
| Monitoring | a device | using SNMP |            |          |            |
Configuring SNMP:RefertotheSNMP/MIBGuideforinformationonhowtoaddSNMPsoadevicecan
bemonitoredfromanetworkmanagementsystem(NMS).
Configuring an SNMP trap receiver:RefertotheSNMP/MIBGuideandspecificinformationaboutthe
| show snmp | trapcommandtoenableSNMPtraps. |     |     |     |     |
| --------- | ----------------------------- | --- | --- | --- | --- |
77
AOS-CX10.13MonitoringGuide|(6200SwitchSeries)

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

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

78

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

Power-over-Ethernet | 79

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| lldp med     | poe                     |     |     |     |
| ------------ | ----------------------- | --- | --- | --- |
| lldp med poe | [priority-override]     |     |     |     |
| no lldp med  | poe [priority-override] |     |     |     |
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
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
power-over-ethernet
power-over-ethernet
no power-over-ethernet
Description
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 80

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
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
Power-over-Ethernet|81

Thepowerallocationmethodcanbechangedonaninterfacethroughport-access(Userrolesor
RADIUS).Anallocationmethodwhenconfiguredthroughport-accesswillreplacetheuserconfigured
method.
Thenoformofthiscommandresetstheactiontodefault.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
usage
Configurestheusage-basedallocationmethod.
| class |     |     |     | Configurestheclass-basedallocationmethod. |     |     |
| ----- | --- | --- | --- | ----------------------------------------- | --- | --- |
Usage
Ifyouenablepd-class-overrideforaninterface,theallocate-byconfigurationofthatinterfacewillbe
automaticallychangedtoclass.However,ifyouchangetheallocationmethodtousagewhenpd-class-
overrideisstillenabled,youwillreceiveanerrormessagestatingthat"Thepowerallocationmethod
cannotbechangedwhenpd-class-overrideisenabled."
Toremovepd-class-override,youcanusetheno power-over-ethernet pd-class-overridecommand.
Itisimportanttonotethatpd-class-overriderequirestheallocationmethodtobesettoclassandis
enforcedwhenconfiguredthroughCLI.However,ifyouoverridetheallocationmethodtousagevia
port-access,pd-class-overridewillnotbeineffect.Therefore,itisrecommendedthatyoudonot
overridetheallocationmethodtousagethroughport-accessoninterfacesconfiguredwithpd-class-
override.
Examples
Configuringthepowerallocationmethod:
| switch(config)# |     | interface | 1/1/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|                    |     | power-over-ethernet |     |     | allocate-by | usage |
| ------------------ | --- | ------------------- | --- | --- | ----------- | ----- |
| switch(config-if)# |     | power-over-ethernet |     |     | allocate-by | class |
Resettingpowerallocationmethod:
| switch(config-if)#  |         | no power-over-ethernet |     |              | allocate-by | class |
| ------------------- | ------- | ---------------------- | --- | ------------ | ----------- | ----- |
| Command History     |         |                        |     |              |             |       |
| Release             |         |                        |     | Modification |             |       |
| 10.07orearlier      |         |                        |     | --           |             |       |
| Command Information |         |                        |     |              |             |       |
| Platforms           | Command | context                |     | Authority    |             |       |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| power-over-ethernet |     |           | always-on   |     |     |     |
| ------------------- | --- | --------- | ----------- | --- | --- | --- |
| power-over-ethernet |     | always-on | <MODULE-ID> |     |     |     |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 82

| no power-over-ethernet |     |     | always-on | <MODULE-ID> |     |     |
| ---------------------- | --- | --- | --------- | ----------- | --- | --- |
Description
Always-onPoEisafeaturethatprovidestheabilitytotheswitchtocontinuetoprovidepoweracrossa
softreboot.Itisapplicableonlytotheinterfaceswhichwereconnectedanddeliveringbeforethesoft
reboot.Also,powerwillnotbedeliveredifpowertotheswitchisinterrupted.Thiscommandenablesor
disablesthealways-onPoEfeatureattheswitchortheslotlevel.Bydefault,always-onPoEisenabledat
theswitchortheslotlevel.
Thenoformofthiscommanddisablespowerdistributiononsoftreboot.
| Parameter   |     |     |     |     | Description                                   |     |
| ----------- | --- | --- | --- | --- | --------------------------------------------- | --- |
| <MODULE-ID> |     |     |     |     | Modulenumbertoapplyalways-onPoEconfiguration. |     |
Examples
Enablingper-interfacepowerdistribution:
| switch(config)# |     | power-over-ethernet |     |     | always-on | 1/1 |
| --------------- | --- | ------------------- | --- | --- | --------- | --- |
Disablingper-interfacepowerdistribution:
| switch(config)#     |         | no  | power-over-ethernet |     | always-on    | 1/1 |
| ------------------- | ------- | --- | ------------------- | --- | ------------ | --- |
| Command History     |         |     |                     |     |              |     |
| Release             |         |     |                     |     | Modification |     |
| 10.07orearlier      |         |     |                     |     | --           |     |
| Command Information |         |     |                     |     |              |     |
| Platforms           | Command |     | context             |     | Authority    |     |
config
| 6200 |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
| power-over-ethernet    |     |                | assigned-class |     |          |     |
| ---------------------- | --- | -------------- | -------------- | --- | -------- | --- |
| power-over-ethernet    |     | assigned-class |                | {3  | | 4 | 6} |     |
| no power-over-ethernet |     |                | assigned-class |     |          |     |
Description
LimitPoEpowerbasedontheassignedclass.Whenanuserassignsamaximumclasstoaninterface,
thePSEwilllimitthemaximumpowerdeliveredtothePDuptoatotalpowerdrawnotexceedingthe
PSEassigned-classpower.PowerdemotionoccurswhenaPDrequestedclassishigherthanthePSE
assignedclass,permittingthePDtoreceivepowerandoperateinareducedpowermode.PoEports
cannotsetanassignedclasswhenQuickPoEisenabledonthesybsystem.Thedefaultassignedclassis
4for2-paircapablePSEand6for4-paircapablePSE.
Thenoformofthiscommandresetstheactiontodefault.
Power-over-Ethernet|83

Examples
SettingPoEassignedclass:
switch(config)#
|                    |     | interface           | 1/1/1 |     |                |     |     |     |
| ------------------ | --- | ------------------- | ----- | --- | -------------- | --- | --- | --- |
| switch(config-if)# |     | power-over-ethernet |       |     | assigned-class |     |     | 4   |
ResettingPoEassignedclasstodefault:
| switch(config-if)# |     | no power-over-ethernet |     |     | assigned-class |     |     | 4   |
| ------------------ | --- | ---------------------- | --- | --- | -------------- | --- | --- | --- |
ShowingQuickPoEenabled:
| switch(config)# |     | power-over-ethernet |       |     | quick-poe      | 1/1 |     |     |
| --------------- | --- | ------------------- | ----- | --- | -------------- | --- | --- | --- |
| switch(config)# |     | interface           | 1/1/1 |     |                |     |     |     |
| switch(config)# |     | power-over-ethernet |       |     | assigned-class |     | 4   |     |
Interface assigned class cannot be configured when Quick PoE is enabled.
| Command History     |         |         |     |              |     |     |     |     |
| ------------------- | ------- | ------- | --- | ------------ | --- | --- | --- | --- |
| Release             |         |         |     | Modification |     |     |     |     |
| 10.07orearlier      |         |         |     | --           |     |     |     |     |
| Command Information |         |         |     |              |     |     |     |     |
| Platforms           | Command | context |     | Authority    |     |     |     |     |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| power-over-ethernet    |     |                | pre-std-detect |     |     |     |     |     |
| ---------------------- | --- | -------------- | -------------- | --- | --- | --- | --- | --- |
| power-over-ethernet    |     | pre-std-detect |                |     |     |     |     |     |
| no power-over-ethernet |     | pre-std-detect |                |     |     |     |     |     |
Description
BeforeIEEE802.3releasedthefirstPoweroverEthernetstandard(802.3af),vendorshadshippedPoE
capableswitchesandPD's.AswearebackwardcompatibleArubawillsupportbothIEEEstandardand
pre-standard802.3afPoweroverEthernetPD'sconcurrently.ThisCLIallowstheusertoenableor
disablepre-802.3af-standarddevicedetectionandpoweringonthespecificport.Whenpre-std-detectis
enabled,powerwillbedeliveredonPairAonly.Defaultisdisabled.
Thenoformofthiscommandresetstheactiontodefault.
Examples
Enablingstandarddevicedetection:
| switch(config)#    |     | interface           | 1/1/1 |     |                |     |     |     |
| ------------------ | --- | ------------------- | ----- | --- | -------------- | --- | --- | --- |
| switch(config-if)# |     | power-over-ethernet |       |     | pre-std-detect |     |     |     |
Disablingstandarddevicedetection:
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 84

| switch(config-if)#  |         |     | no power-over-ethernet |              | pre-std-detect |
| ------------------- | ------- | --- | ---------------------- | ------------ | -------------- |
| Command History     |         |     |                        |              |                |
| Release             |         |     |                        | Modification |                |
| 10.07orearlier      |         |     |                        | --           |                |
| Command Information |         |     |                        |              |                |
| Platforms           | Command |     | context                | Authority    |                |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| power-over-ethernet    |     |          | priority           |     |               |
| ---------------------- | --- | -------- | ------------------ | --- | ------------- |
| power-over-ethernet    |     | priority | {critical          |     | | high | low} |
| no power-over-ethernet |     |          | priority {critical |     | | high | low} |
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
| 6200 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
Power-over-Ethernet|85

| power-over-ethernet |     |           | quick-poe |             |     |     |
| ------------------- | --- | --------- | --------- | ----------- | --- | --- |
| power-over-ethernet |     | quick-poe |           | <MODULE-ID> |     |     |
no power-over-ethernet
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
config-if
| 6200 |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
| power-over-ethernet    |     |           | threshold |              |     |     |
| ---------------------- | --- | --------- | --------- | ------------ | --- | --- |
| power-over-ethernet    |     | threshold |           | <PERCENTAGE> |     |     |
| no power-over-ethernet |     |           | threshold | <PERCENTAGE> |     |     |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 86

Description
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
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
Power-over-Ethernet|87

| switch(config-if)# |             |         | no power-over-ethernet |     |              | trap |
| ------------------ | ----------- | ------- | ---------------------- | --- | ------------ | ---- |
| Command            | History     |         |                        |     |              |      |
| Release            |             |         |                        |     | Modification |      |
| 10.07orearlier     |             |         |                        |     | --           |      |
| Command            | Information |         |                        |     |              |      |
| Platforms          |             | Command | context                |     | Authority    |      |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show      | lldp         | local |                  |     |     |     |
| --------- | ------------ | ----- | ---------------- | --- | --- | --- |
| show lldp | local-device |       | [<INTERFACE-ID>] |     |     |     |
Description
DisplaysinformationadvertisedbytheswitchiftheLLDPfeatureisenabledbyuser.
| Parameter      |     |     |     |     | Description                                  |     |
| -------------- | --- | --- | --- | --- | -------------------------------------------- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port |     |
Examples
ShowingLLDPlocaldevice:
| switch# | show | lldp | local-device |     | 1/1/10 |     |
| ------- | ---- | ---- | ------------ | --- | ------ | --- |
| Local   | Port | Data |              |     |        |     |
===============
| Port-ID        |             |             | : 1/1/10   |     |              |     |
| -------------- | ----------- | ----------- | ---------- | --- | ------------ | --- |
| Port-Desc      |             |             | : "1/1/10" |     |              |     |
| Port           | VLAN        | ID          | : 0        |     |              |     |
| PoE            | Plus        | Information |            |     |              |     |
| PoE            | Device      | Type        | : Type     | 2   | PSE          |     |
| Power          | Source      |             | : Primary  |     |              |     |
| Power          | Priority    |             | : low      |     |              |     |
| PSE            | Allocated   | Power:      | 25.0       | W   |              |     |
| PD             | Requested   | Power       | : 25.0     | W   |              |     |
| Command        | History     |             |            |     |              |     |
| Release        |             |             |            |     | Modification |     |
| 10.07orearlier |             |             |            |     | --           |     |
| Command        | Information |             |            |     |              |     |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 88

| Platforms | Command |     | context | Authority |     |
| --------- | ------- | --- | ------- | --------- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
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
| Command Information  |                    |             |           |                     |      |
Power-over-Ethernet|89

| Platforms |     | Command |     | context | Authority |     |
| --------- | --- | ------- | --- | ------- | --------- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show | power-over-ethernet |     |     |         |              |         |
| ---- | ------------------- | --- | --- | ------- | ------------ | ------- |
| show | power-over-ethernet |     |     | [member | <MEMBER-ID>] | [brief] |
Description
Displaysthestatusinformationofthefullsystem.
| Parameter   |     |     |     |     | Description                                    |     |
| ----------- | --- | --- | --- | --- | ---------------------------------------------- | --- |
| <MEMBER-ID> |     |     |     |     | Displaysthedetailedstatusofgivenmember.        |     |
| <IFNAME>    |     |     |     |     | Displaythedetailedstatusofgivenport.           |     |
| brief       |     |     |     |     | Displaythebriefstatusofallportsorthegivenport. |     |
Examples
Showingsampleoutputforshowpower-over-ethernetonstandaloneboxwithVSFcapabiity:
|     | switch# show        | power-over-ethernet |          |                       |                 |        |
| --- | ------------------- | ------------------- | -------- | --------------------- | --------------- | ------ |
|     | System Power        | Status              |          | for member            | 1               |        |
|     | Configured          |                     | Power    | Status                | : No redundancy |        |
|     | Operational         |                     | Power    | Status                | : No redundancy |        |
|     | Total Available     |                     | Power    |                       | : 740 W         |        |
|     | Total Failover      |                     | Pwr      | Avl                   | : 0 W           |        |
|     | Total Redundancy    |                     |          | Power                 | : 0 W           |        |
|     | Total Power         |                     | Drawn    |                       | : 0 W           | +/- 6W |
|     | Total Power         |                     | Reserved |                       | : 0 W           |        |
|     | Total Remaining     |                     | Power    |                       | : 740 W         |        |
|     | Trap Threshold      |                     |          |                       | : 80 %          |        |
|     | Trap Enabled        |                     |          |                       | : Yes           |        |
|     | Always-on           | PoE                 | Enabled  |                       | : 1/1           |        |
|     | Quick PoE           | Enabled             |          |                       | : None          |        |
|     | Internal            | Power               |          |                       |                 |        |
|     | Total               |                     | Power    |                       |                 |        |
|     | PS (Watts)          |                     |          | Status                |                 |        |
|     | ----- ------------- |                     |          | --------------------- |                 |        |
|     | 1 0                 |                     |          | Absent                |                 |        |
|     | 2 740               |                     |          | Ok                    |                 |        |
|     | System Power        | Status              |          | for member            | 2               |        |
|     | Configured          |                     | Power    | Status                | : No redundancy |        |
|     | Operational         |                     | Power    | Status                | : No redundancy |        |
|     | Total Available     |                     | Power    |                       | : 600 W         |        |
|     | Total Failover      |                     | Pwr      | Avl                   | : 0 W           |        |
|     | Total Redundancy    |                     |          | Power                 | : 0 W           |        |
|     | Total Power         |                     | Drawn    |                       | : 0 W           | +/- 6W |
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 90

| Total          | Power       | Reserved |     | :      | 0 W |     |     |     |     |
| -------------- | ----------- | -------- | --- | ------ | --- | --- | --- | --- | --- |
| Total          | Remaining   | Power    |     | : 600  | W   |     |     |     |     |
| Trap Threshold |             |          |     | : 80   | %   |     |     |     |     |
| Trap Enabled   |             |          |     | : Yes  |     |     |     |     |     |
| Always-on      | PoE         | Enabled  |     | : None |     |     |     |     |     |
| Quick          | PoE Enabled |          |     | : None |     |     |     |     |     |
| Internal       | Power       |          |     |        |     |     |     |     |     |
Total Power
| PS    | (Watts)       |     | Status                |     |     |     |     |     |     |
| ----- | ------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
| ----- | ------------- |     | --------------------- |     |     |     |     |     |     |
| 1     | 0             |     | Absent                |     |     |     |     |     |     |
| 2     | 600           |     | Ok                    |     |     |     |     |     |     |
Showingsampleoutputforpower-over-ethernetmember:
| switch#        | show power-over-ethernet |              |        | member |            | 1   |     |     |     |
| -------------- | ------------------------ | ------------ | ------ | ------ | ---------- | --- | --- | --- | --- |
| System Power   | Status                   | for          | member | 1      |            |     |     |     |     |
| Configured     |                          | Power Status |        | : No   | redundancy |     |     |     |     |
| Operational    |                          | Power Status |        | : No   | redundancy |     |     |     |     |
| Total          | Available                | Power        |        | : 740  | W          |     |     |     |     |
| Total          | Failover                 | Pwr          | Avl    | :      | 0 W        |     |     |     |     |
| Total          | Redundancy               | Power        |        | :      | 0 W        |     |     |     |     |
| Total          | Power                    | Drawn        |        | :      | 0 W +/-    | 6W  |     |     |     |
| Total          | Power                    | Reserved     |        | :      | 0 W        |     |     |     |     |
| Total          | Remaining                | Power        |        | : 740  | W          |     |     |     |     |
| Trap Threshold |                          |              |        | : 80   | %          |     |     |     |     |
| Trap Enabled   |                          |              |        | : No   |            |     |     |     |     |
| Always-on      | PoE                      | Enabled      |        | : 1/1  |            |     |     |     |     |
| Quick          | PoE Enabled              |              |        | : 1/1  |            |     |     |     |     |
| Internal       | Power                    |              |        |        |            |     |     |     |     |
Total Power
| PS    | (Watts)       |     | Status                |     |     |     |     |     |     |
| ----- | ------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
| ----- | ------------- |     | --------------------- |     |     |     |     |     |     |
| 1     | 0             |     | Absent                |     |     |     |     |     |     |
| 2     | 740           |     | Ok                    |     |     |     |     |     |     |
Showingsampleoutputforpower-over-ethernetbriefinaVSFstack:
switch#
|            | show power-over-ethernet |              |             | brief |     |            |          |     |     |
| ---------- | ------------------------ | ------------ | ----------- | ----- | --- | ---------- | -------- | --- | --- |
| Status and | Configuration            |              | Information |       | for | PoE        |          |     |     |
| Member     | 1 Power                  | Status       |             |       |     |            |          |     |     |
| Available: |                          | 370 W        | Reserved:   | 55.60 | W   | Remaining: | 314.40 W |     |     |
| Always-on  |                          | PoE Enabled: |             | 1/1   |     |            |          |     |     |
| Quick      | PoE                      | Enabled:     | None        |       |     |            |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En Priority |     | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | --- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes Low |     | Off | Class | 0.0 | W 0.0 | W Denied | None 4 | 2   |
| ----- | ------- | --- | --- | ----- | --- | ----- | -------- | ------ | --- |
1/1/2 Yes Critical Off Usage 1.6 W 1.5 W Delivering* Single 0 1
1/1/3 Yes High Off Class 54.0 W 25.5 W Delivering*^ Dual 1/3 3
| 1/1/4 | No Low |     | On  | Usage | 0.0 | W 0.0 | W Disabled | None N/A | N/A |
| ----- | ------ | --- | --- | ----- | --- | ----- | ---------- | -------- | --- |
Power-over-Ethernet|91

| Member     | 2 Power Status |           |      |     |            |       |     |     |
| ---------- | -------------- | --------- | ---- | --- | ---------- | ----- | --- | --- |
| Available: | 600 W          | Reserved: | 0.00 | W   | Remaining: | 600 W |     |     |
| Always-on  | PoE Enabled:   |           | None |     |            |       |     |     |
| Quick      | PoE Enabled:   | None      |      |     |            |       |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 2/1/1 | Yes Low | Off | Class | 0.0 | W 0.0 | W Searching | None N/A | N/A |
| ----- | ------- | --- | ----- | --- | ----- | ----------- | -------- | --- |
2/1/2 Yes Critical Off Usage 0.0 W 0.0 W Searching None N/A N/A
| 2/1/3      | Yes High    | Off | Class     | 0.0 | W 0.0          | W Searching | None N/A | N/A |
| ---------- | ----------- | --- | --------- | --- | -------------- | ----------- | -------- | --- |
| 2/1/4      | No Low      | On  | Usage     | 0.0 | W 0.0          | W Disabled  | None N/A | N/A |
| *This port | may go down | in  | the event | of  | a PSU failure. |             |          |     |
^This port is power demoted due to user config or power availabilty.
Showingsampleoutputforpower-over-ethernetbriefper-port:
| switch#    | show power-over-ethernet |             |       | 1/1/1 | brief        |          |     |     |
| ---------- | ------------------------ | ----------- | ----- | ----- | ------------ | -------- | --- | --- |
| Status and | Configuration            | Information |       | for   | port 1/1/1   |          |     |     |
| Member     | 1Power Status            |             |       |       |              |          |     |     |
| Available: | 370 W                    | Reserved:   | 55.60 |       | W Remaining: | 314.40 W |     |     |
| Always-on  | PoE Enabled:             |             | 1/1   |       |              |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes Low | Off | Class | 0.0 | W 0.0 | W Denied | None 4 | 2   |
| ----- | ------- | --- | ----- | --- | ----- | -------- | ------ | --- |
Showingsampleoutputforpower-over-ethernetbriefforinterfacerange:
For6300Switchseries:
| switch#    | show power-over-ethernet |             |       | 1/1/1-1/1/2 | brief            |          |     |     |
| ---------- | ------------------------ | ----------- | ----- | ----------- | ---------------- | -------- | --- | --- |
| Status and | Configuration            | Information |       | for         | port 1/1/1-1/1/2 |          |     |     |
| Member     | 1Power Status            |             |       |             |                  |          |     |     |
| Available: | 370 W                    | Reserved:   | 55.60 |             | W Remaining:     | 314.40 W |     |     |
| Always-on  | PoE Enabled:             |             | 1/1   |             |                  |          |     |     |
| Quick      | PoE Enabled:             | None        |       |             |                  |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes Low | Off | Class | 0.0 | W 0.0 | W Denied | None 4 | 2   |
| ----- | ------- | --- | ----- | --- | ----- | -------- | ------ | --- |
1/1/2 Yes Critical Off Usage 1.6 W 1.5 W Delivering* Single 0 1
Showingsampleoutputforpower-over-ethernetforamissinglinecard:
| switch#    | show power-over-ethernet |     |          | 1/3 brief |     |     |     |     |
| ---------- | ------------------------ | --- | -------- | --------- | --- | --- | --- | --- |
| Module 1/3 | is not physically        |     | present. |           |     |     |     |     |
Showingsampleoutputforpower-over-ethernetbriefforamissingmember:
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 92

| switch# | show power-over-ethernet |          | member 3 brief |
| ------- | ------------------------ | -------- | -------------- |
| Member  | 3 is not physically      | present. |                |
Showingsampleoutputforpower-over-ethernetportwhenphysicalinterfaceisnotpresent:
| switch#        | show power-over-ethernet |              | 2/1/1        |
| -------------- | ------------------------ | ------------ | ------------ |
| Interface      | 2/1/1 is                 | not present. |              |
| Command        | History                  |              |              |
| Release        |                          |              | Modification |
| 10.07orearlier |                          |              | --           |
| Command        | Information              |              |              |
| Platforms      | Command                  | context      | Authority    |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
Power-over-Ethernet|93

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
94
AOS-CX10.13MonitoringGuide|(6200SwitchSeries)

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
ArubaAirWave|95

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
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 96

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

Aruba AirWave | 97

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
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 98

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
ArubaAirWave|99

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
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 100

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
ArubaAirWave|101

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
characters,excludingspaceandquestionmark(?).
vrf <VRF-NAME> SpecifiestheVRFassociatedwiththecontext.Default:default.
community <STRING> SpecifiestheSNMPcommunitystringassociatedwiththecontext.
Range:1to32printableASCIIcharacters,excludingspaceand
questionmark.Default:public.
Examples
CreatinganSNMPv3contextnamednewContext:
| switch(config)# |             | snmpv3 context | newContext   |     |     |
| --------------- | ----------- | -------------- | ------------ | --- | --- |
| Command         | History     |                |              |     |     |
| Release         |             |                | Modification |     |     |
| 10.07orearlier  |             |                | --           |     |     |
| Command         | Information |                |              |     |     |
| Platforms       | Command     | context        | Authority    |     |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmpv3 | user |     |     |     |     |
| ------ | ---- | --- | --- | --- | --- |
snmpv3 user <NAME> [auth <AUTH-PROTOCOL> auth-pass {plaintext | ciphertext}
<AUTH-PWORD> [priv <PRIV-PROTOCOL> priv-pass {plaintext | ciphertext} <PRIV-PWORD>] ]
| no snmpv3    | user <NAME> | [auth <AUTH-PROTOCOL> |           | auth-pass     |     |
| ------------ | ----------- | --------------------- | --------- | ------------- | --- |
| <AUTH-PWORD> | [priv       | <PRIV-PROTOCOL>       | priv-pass | <PRIV-PWORD>] | ]   |
Description
CreatesanSNMPv3userandaddsittoanSNMPv3context.
ThenoformofthiscommandremovesthespecifiedSNMPv3user.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<NAME>
SpecifiestheSNMPv3username.Range1-32
printableASCIIcharacters,excludingspace
andquestionmark.
auth <AUTH-PROTOCOL> Specifiestheauthenticationprotocolusedto
validateuserlogins.Availableoptionsare:
md5orsha.
auth-pass {plaintext | ciphertext} <AUTH-PWORD> SpecifiestheSNMPv3userpassword.Range
forplaintextis8-32printableASCII
characters,excludingspaceandquestion
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 102

Parameter

Description

priv <PRIV-PROTOCOL>

priv-pass {plaintext | ciphertext} <PRIV-PWORD>

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

On switch 1, configure a user called Admin, then issue the show running-config command to display
switch configuration settings. The snmpv3 user command uses the ciphertext option to protect the
users's passwords.

switch1(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword
priv des priv-pass plaintext myprivpass
switch1(config)# exit
switch1# show running-config
Current configuration:

Aruba AirWave | 103

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
| switch1(config)# |     | snmpv3 | user | Admin | auth sha auth-pass |
| ---------------- | --- | ------ | ---- | ----- | ------------------ |
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
AOS-CX10.13MonitoringGuide|(6200SwitchSeries) 104

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

AOS-CX Software
Technical Update
channel on

https://developer.arubanetworks.com/hpe-aruba-networking-aoscx/docs/about

https://community.arubanetworks.com/

Videos on new features introduced in this release:

https://www.youtube.com/playlist?list=PLsYGHuNuBZcbWPEjjHuVMqP-Q_UL3CskS

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

105

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

https://networkingsupport.hpe.com/downloads

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

https://networkingsupport.hpe.com/notifications/subscriptions (requires an active HPE Aruba
Networking support account to manage subscriptions). Security notices are viewable without a
networking support account.

Warranty Information

To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Support and Other Resources | 106

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

AOS-CX 10.13 Monitoring Guide | (6200 Switch Series)

107