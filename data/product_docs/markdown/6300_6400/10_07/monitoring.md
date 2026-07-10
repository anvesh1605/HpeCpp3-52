| AOS-CX |     | 10.07 | Monitoring |     |
| ------ | --- | ----- | ---------- | --- |
Guide
|     | 6300, | 6400 | Switch | Series |
| --- | ----- | ---- | ------ | ------ |
PartNumber:5200-7872
Published:April2021
Edition:1

Copyright Information

© Copyright 2021 Hewlett Packard Enterprise Development LP.

Open Source Code

This product includes code licensed under the GNU General Public License, the GNU Lesser General Public
License, and/or certain other open source licenses. A complete machine-readable copy of the source code
corresponding to such code is available upon request. This offer is valid to anyone in receipt of this
information and shall expire three years following the date of the final distribution of this product version
by Hewlett Packard Enterprise Company. To obtain such source code, send a check or money order in the
amount of US $10.00 to:

Hewlett Packard Enterprise Company
6280 America Center Drive
San Jose, CA 95002
USA

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
Enterprise has no control over and is not responsible for information outside the Hewlett Packard
Enterprise website.

Acknowledgment

Intel®, Itanium®, Optane™, Pentium®, Xeon®, Intel Inside®, and the Intel Inside logo are trademarks of
Intel Corporation in the U.S. and other countries.

Microsoft® and Windows® are either registered trademarks or trademarks of Microsoft Corporation in the
United States and/or other countries.

Adobe® and Acrobat® are trademarks of Adobe Systems Incorporated.

Java® and Oracle® are registered trademarks of Oracle and/or its affiliates.

UNIX® is a registered trademark of The Open Group.

All third-party marks are property of their respective owners.

| 2

Contents
Contents
| Contents                                          |                                   |          |                    | 3   |
| ------------------------------------------------- | --------------------------------- | -------- | ------------------ | --- |
| About this                                        | document                          |          |                    | 7   |
| Applicableproducts                                |                                   |          |                    | 7   |
| Latestversionavailableonline                      |                                   |          |                    | 7   |
| Commandsyntaxnotationconventions                  |                                   |          |                    | 7   |
| Abouttheexamples                                  |                                   |          |                    | 8   |
| Identifyingswitchportsandinterfaces               |                                   |          |                    | 8   |
| Identifyingmodularswitchcomponents                |                                   |          |                    | 9   |
| Monitoring                                        | hardware                          | through  | visual observation | 10  |
| ConfirmingnormaloperationoftheswitchbyreadingLEDs |                                   |          |                    | 10  |
| Detectingiftheswitchisnotreadyforafailoverevent   |                                   |          |                    | 11  |
| FindingfaultedcomponentsusingtheswitchLEDs        |                                   |          |                    | 11  |
| Aruba 6300/6400                                   | Switch                            | Series   | LEDs               | 13  |
| SwitchandportLEDsfor6300SwitchSeries              |                                   |          |                    | 13  |
| SwitchandportLEDsfor6400SwitchSeries              |                                   |          |                    | 15  |
|                                                   | FrontpanelLEDsfor6400SwitchSeries |          |                    | 16  |
|                                                   | PowerSupplyLEDs                   |          |                    | 18  |
|                                                   | LinemoduleLEDs                    |          |                    | 19  |
| Boot commands                                     |                                   |          |                    | 21  |
| bootfabric-module                                 |                                   |          |                    | 21  |
| bootline-module                                   |                                   |          |                    | 22  |
| bootmanagement-module                             |                                   |          |                    | 22  |
| bootset-default                                   |                                   |          |                    | 24  |
| bootsystem                                        |                                   |          |                    | 24  |
| showboot-history                                  |                                   |          |                    | 26  |
| Switch system                                     | and                               | hardware | commands           | 29  |
| bluetoothdisable                                  |                                   |          |                    | 29  |
| bluetoothenable                                   |                                   |          |                    | 29  |
| clearevents                                       |                                   |          |                    | 30  |
| cleariperrors                                     |                                   |          |                    | 31  |
| domain-name                                       |                                   |          |                    | 31  |
| hostname                                          |                                   |          |                    | 32  |
| ledlocator                                        |                                   |          |                    | 33  |
| moduleadmin-state                                 |                                   |          |                    | 33  |
| moduleproduct-number                              |                                   |          |                    | 34  |
| mtrace                                            |                                   |          |                    | 36  |
| showbluetooth                                     |                                   |          |                    | 37  |
| showboot-history                                  |                                   |          |                    | 38  |
| showcapacities                                    |                                   |          |                    | 40  |
| showcapacities-status                             |                                   |          |                    | 41  |
| showcore-dump                                     |                                   |          |                    | 42  |
| showdomain-name                                   |                                   |          |                    | 44  |
| showenvironmentfan                                |                                   |          |                    | 45  |
| showenvironmentled                                |                                   |          |                    | 47  |
3
AOS-CX10.07MonitoringGuide| (6300and6400SwitchSeries)

| showenvironmentpower-consumption        |                                    | 47  |
| --------------------------------------- | ---------------------------------- | --- |
| showenvironmentpower-supply             |                                    | 49  |
| showenvironmentrear-display-module      |                                    | 50  |
| showenvironmenttemperature              |                                    | 51  |
| showevents                              |                                    | 53  |
| showfabric                              |                                    | 57  |
| showhostname                            |                                    | 58  |
| showimages                              |                                    | 59  |
| showiperrors                            |                                    | 60  |
| showmodule                              |                                    | 61  |
| showrunning-config                      |                                    | 63  |
| showrunning-configcurrent-context       |                                    | 66  |
| showstartup-config                      |                                    | 68  |
| showsystem                              |                                    | 69  |
| showsystemerror-counter-monitor         |                                    | 70  |
| showsystemresource-utilization          |                                    | 71  |
| showtech                                |                                    | 73  |
| showusb                                 |                                    | 74  |
| showusbfile-system                      |                                    | 75  |
| showversion                             |                                    | 76  |
| systemresource-utilizationpoll-interval |                                    | 77  |
| topcpu                                  |                                    | 77  |
| topmemory                               |                                    | 78  |
| usb                                     |                                    | 79  |
| usbmount|unmount                        |                                    | 79  |
| External                                | storage                            | 81  |
| Externalstoragecommands                 |                                    | 81  |
|                                         | address                            | 81  |
|                                         | directory                          | 82  |
|                                         | disable                            | 82  |
|                                         | enable                             | 83  |
|                                         | external-storage                   | 84  |
|                                         | password                           | 84  |
|                                         | showexternal-storage               | 85  |
|                                         | showrunning-configexternal-storage | 86  |
|                                         | type                               | 86  |
|                                         | username                           | 87  |
|                                         | vrf                                | 88  |
| IP-SLA                                  |                                    | 89  |
| IP-SLAguidelines                        |                                    | 89  |
| LimitationswithVoIPSLAs                 |                                    | 90  |
| IP-SLAcommands                          |                                    | 90  |
|                                         | http                               | 90  |
|                                         | icmp-echo                          | 91  |
|                                         | ip-sla                             | 92  |
|                                         | ip-slaresponder                    | 92  |
|                                         | showip-slaresponder                | 93  |
|                                         | showip-slaresponderresults         | 94  |
|                                         | showip-sla<SLA-NAME>               | 95  |
|                                         | start-test                         | 97  |
|                                         | stop-test                          | 98  |
|                                         | tcp-connect                        | 98  |
|                                         | udp-echo                           | 99  |
|                                         | udp-jitter-voip                    | 100 |
Contents|4

|                                                | vrf                               |            | 101 |
| ---------------------------------------------- | --------------------------------- | ---------- | --- |
| L1-100Mbps                                     | downshift                         |            | 103 |
| Limitationswithspeeddownshift                  |                                   |            | 103 |
| L1-100Mbpsdownshiftcommands                    |                                   |            | 103 |
|                                                | downshiftenable                   |            | 103 |
|                                                | showinterface                     |            | 104 |
|                                                | showinterfacedownshift-enable     |            | 106 |
|                                                | showrunning-configinterface       |            | 107 |
| Mirroring                                      |                                   |            | 109 |
| Mirrorstatistics                               |                                   |            | 109 |
| Mirrorendpoints                                |                                   |            | 109 |
| Classifierpoliciesandmirroringsessions         |                                   |            | 110 |
| VLANasasource                                  |                                   |            | 110 |
| Mirroringcommands                              |                                   |            | 111 |
|                                                | clearmirror                       |            | 111 |
|                                                | clearmirrorendpoint               |            | 112 |
|                                                | comment                           |            | 112 |
|                                                | copytshark-pcap                   |            | 113 |
|                                                | destinationcpu                    |            | 114 |
|                                                | destinationinterface              |            | 114 |
|                                                | diagnostic                        |            | 116 |
|                                                | disable                           |            | 117 |
|                                                | enable                            |            | 118 |
|                                                | mirrorsession                     |            | 118 |
|                                                | mirrorendpoint                    |            | 119 |
|                                                | showmirror                        |            | 120 |
|                                                | showmirrorendpoint                |            | 121 |
|                                                | shutdown                          |            | 122 |
|                                                | source                            |            | 123 |
|                                                | sourceinterface                   |            | 124 |
|                                                | sourcevlan                        |            | 125 |
| Monitoring                                     | a device                          | using SNMP | 128 |
| Power-over-Ethernet                            |                                   |            | 129 |
| PoEcommands                                    |                                   |            | 130 |
|                                                | lldpdot3poe                       |            | 130 |
|                                                | lldpmedpoe                        |            | 131 |
|                                                | power-over-ethernet               |            | 131 |
|                                                | power-over-ethernetallocate-by    |            | 132 |
|                                                | power-over-ethernetalways-on      |            | 133 |
|                                                | power-over-ethernetassigned-class |            | 133 |
|                                                | power-over-ethernetpre-std-detect |            | 134 |
|                                                | power-over-ethernetpriority       |            | 135 |
|                                                | power-over-ethernetquick-poe      |            | 135 |
|                                                | power-over-ethernetthreshold      |            | 136 |
|                                                | power-over-ethernetpriority       |            | 137 |
|                                                | showlldplocal                     |            | 137 |
|                                                | showlldpneighbor                  |            | 138 |
|                                                | showpower-over-ethernet           |            | 139 |
| Aruba AirWave                                  |                                   |            | 144 |
| SNMPsupportandAirWave                          |                                   |            | 144 |
|                                                | SNMPontheswitch                   |            | 144 |
| SupportedfeatureswithAirWaveandtheAOS-CXswitch |                                   |            | 145 |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 5

| ConfiguringtheAOS-CXswitchtobemonitoredbyAirWave |                      |           | 145 |
| ------------------------------------------------ | -------------------- | --------- | --- |
|                                                  | logging              |           | 146 |
|                                                  | snmp-servercommunity |           | 148 |
|                                                  | snmp-serverhost      |           | 148 |
|                                                  | snmp-servervrf       |           | 150 |
|                                                  | snmpv3context        |           | 151 |
|                                                  | snmpv3user           |           | 151 |
| Support                                          | and other            | resources | 154 |
| AccessingArubaSupport                            |                      |           | 154 |
| Accessingupdates                                 |                      |           | 154 |
|                                                  | ArubaSupportPortal   |           | 154 |
|                                                  | MyNetworking         |           | 155 |
| Warrantyinformation                              |                      |           | 155 |
| Regulatoryinformation                            |                      |           | 155 |
| Documentationfeedback                            |                      |           | 155 |
Contents|6

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and other resources.

Command syntax notation conventions

Convention

Usage

example-text

Identifies commands and their options and operands, code examples,
filenames, pathnames, and output displayed in a command window. Items that
appear like the example text in the previous column are to be entered exactly
as shown and are required unless enclosed in brackets ([ ]).

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

n For output formats where italic text cannot be displayed, variables are
enclosed in angle brackets (< >). Substitute the text—including the
enclosing angle brackets—with an actual value.

n For output formats where italic text can be displayed, variables might

or might not be enclosed in angle brackets. Substitute the text
including the enclosing angle brackets, if any, with an actual value.

Vertical bar. A logical OR that separates multiple items from which you can
choose only one.
Any spaces that are on either side of the vertical bar are included for
readability and are not a required part of the command syntax.

Braces. Indicates that at least one of the enclosed items is required.

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

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
Examplesinthisdocumentarerepresentativeandmightnotmatchyourparticularswitchorenvironment.
Theslotandportnumbersinthisdocumentareforillustrationonlyandmightbeunavailableonyour
switch.
| Understandingthe | CLI prompts |     |     |
| ---------------- | ----------- | --- | --- |
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
Incertainconfigurationcontexts,thepromptmayincludevariableinformation.Forexample,wheninthe
VLANconfigurationcontext,aVLANnumberappearsintheprompt:
switch(config-vlan-100)#
Whenreferringtothiscontext,thisdocumentusesthesyntax:
switch(config-vlan-<VLAN-ID>)#
Where<VLAN-ID>isavariablerepresentingtheVLANnumber.
| Identifying | switch | ports and | interfaces |
| ----------- | ------ | --------- | ---------- |
Physicalportsontheswitchandtheircorrespondinglogicalsoftwareinterfacesareidentifiedusingthe
format:
member/slot/port
| On the 6300Switch | Series |     |     |
| ----------------- | ------ | --- | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to10.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis1.
Aboutthisdocument|8

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

Identifying modular switch components

n Power supplies are on the front of the switch behind the bezel above the management modules. Power

supplies are labeled in software in the format: member/power supply:

o member: 1.

o power supply: 1 to 4.

n Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

o member: 1.

o tray: 1 to 4.

o fan: 1 to 4.

n Fabric modules are not labeled on the switch but are labeled in software in the format: member/module:

o member: 1.

o member: 1 or 2.

n The display module on the rear of the switch is not labeled with a member or slot number.

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

9

Monitoring hardware through visual
observation

Chapter 2

Monitoring hardware through visual observation

Confirming normal operation of the switch by reading LEDs
This task describes using the switch LEDs to confirm that the switch is operating normally.

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

7. Verify that the standby management module is ready to take over as the active management module.

On the standby management module, verify the states of the following LEDs:

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

10

HealthLEDisOnGreen.
n
| n Managementstatestandby(Stby)LEDisOnGreen. |        |        |        |       |                |       |
| ------------------------------------------- | ------ | ------ | ------ | ----- | -------------- | ----- |
| Detecting                                   | if the | switch | is not | ready | for a failover | event |
ThistaskdescribesusingtheswitchLEDstodetectiftheswitchisnotreadyforthelossofafabricmodule
orforafailoverfromtheactivemanagementmoduletothestandbymanagementmodule.
AlthoughyoucandetectpowersupplyfailuresbyviewingtheLEDs,youmustusesoftwarecommandsto
determineifthepowersupplyredundancyissufficienttopowerthechassisifapowersupplyfails.
Procedure
1. Detectifthestandbymanagementmoduleisshutdown.
Ifthestandbymanagementmoduleisshutdown,theLEDstatesareasfollows:
| n ThestandbymanagementmodulehealthLEDisOff.       |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| n Thestandbymanagementstateactive(Actv)LEDisOff.  |     |     |     |     |     |     |
| n Thestandbymanagementstatestandby(Stby)LEDisOff. |     |     |     |     |     |     |
n OntheactivemanagementmoduleintheStatusFrontManagementModulessection,theLEDfor
thestandbymanagementmoduleisOff.Forexample,iftheactivemanagementmoduleis
ManagementModuleLED5,ManagementModulesLED6isOff.
2. Detectifthestandbymanagementmoduleisinatransientstate.Ifthestandbymanagement
moduleisbooting,updating,orinanothertransientstate,theLEDstatesareasfollows:
ThestandbymanagementmodulehealthLEDisSlowFlashGreenwhentheserviceoperating
n
systemisrunningorduringanoperatingsystemupdate.
n ThestandbymanagementmoduleBootingLEDisSlowFlashGreenwhentheArubaOS-CX
operatingsystemisbooting.
| n Thestandbymanagementstateactive(Actv)LEDisOff.  |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| n Thestandbymanagementstatestandby(Stby)LEDisOff. |     |     |     |     |     |     |
OntheactivemanagementmoduleintheStatusFrontManagementModulessection,theLEDfor
n
thestandbymanagementmoduleisSlowFlashGreen.
3. Detectifafabricmoduleisshutdownornotpresent.Ifafabricmoduleisshutdownornotpresent,
theLEDstatesareasfollows:
n Ontheactivemanagementmodule,intheStatusRearsection,theLEDforthefabricmoduleis
Off.
| n Onthereardisplaymodule,theLEDforthefabricmoduleisOff. |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
n Onthefabricmodule,thehealthLEDisOff.However,thefabricmoduleisbehindfan1andisnot
directlyvisible.
| Finding | faulted | components |     | using | the switch | LEDs |
| ------- | ------- | ---------- | --- | ----- | ---------- | ---- |
ThistaskdescribesusingtheswitchLEDstofindcomponentsthatareinafaultcondition.
AllgreenLEDs—exceptforchassispowerLEDsandtheUsr1LED—areoffwhentheLEDmodeissettoLight
Faults(TheUsr1LEDoftheLEDModesectionoftheactivemanagementmoduleisOnGreenandthedefault
behaviorfortheUsr1LEDisbeingused.).
Monitoringhardwarethroughvisualobservation|11

Procedure

1. Find the switch that has the fault condition, which is indicated by a chassis health LED in the state of

Slow Flash Orange.

The chassis health LED is located on the front of the switch and on the rear panel of the switch.

2.

If you are at the back of the switch, on the rear panel, look for LEDs that are in the Slow Flash Orange
state:

The Status Rear area has LEDs for power supplies, fabric modules, fan trays, and fans. The number on
the LED represents the unit number of the component.

If the only LED in a state of Slow Flash Orange is the Chassis health LED, go to the front of the switch.

3. At the front of the switch, on the active management module, look for LEDs that are in the Slow Flash

Orange state:
n The Status Front area has LEDs for power supplies, line and fabric modules, and management

modules. The number on the LED indicates the slot number of the component.

n The Status Rear area has LEDs for fabric modules and fan trays, with a single LED for all the fans in

the fan tray. The number on the LED represents the slot or bay number of the component.

4. Use the number indicated by the LED that is flashing to locate the slot that contains the faulted

component.

The fabric modules are located behind the fan trays, and the fabric module number corresponds to
the fan tray number.

5. At the front of the switch, on line modules, look for LEDs that are in the Slow Flash Orange state:

Module LEDs and Port LEDs indicate faults if their states are Slow Flash Orange.

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

12

|          |                                        |                               |          |           |         | Chapter | 3    |
| -------- | -------------------------------------- | ----------------------------- | -------- | --------- | ------- | ------- | ---- |
|          |                                        |                               | Aruba    | 6300/6400 | Switch  | Series  | LEDs |
| Aruba    | 6300/6400 Switch                       | Series                        | LEDs     |           |         |         |      |
| Switch   | and port                               | LEDs                          | for 6300 | Switch    | Series  |         |      |
| Figure 1 | SwitchandPortLEDs                      |                               |          |           |         |         |      |
| Table 1: | SwitchandportLEDs:Labelsanddescription |                               |          |           |         |         |      |
| Label    |                                        | Description                   |          |           |         |         |      |
| 1        |                                        | SwitchportLEDs                |          |           |         |         |      |
| 2        |                                        | BackModulestatusLED           |          |           |         |         |      |
| 3        |                                        | SpeedmodeselectedLED          |          |           |         |         |      |
| 4        |                                        | PoEmodeselected               |          |           |         |         |      |
| 5        |                                        | ResetbuttonUsrmodeselectedLED |          |           |         |         |      |
| 6        |                                        | UID(UnitIdentification)       |          |           |         |         |      |
| 7        |                                        | GlobalStatusLED               |          |           |         |         |      |
| 8        |                                        | LEDModestatusLED              |          |           |         |         |      |
| 9        |                                        | ManagementConsoleLED          |          |           |         |         |      |
| Table 2: | FrontpanelLEDbehavior                  |                               |          |           |         |         |      |
| Switch   | LEDs Function                          |                               |          | State     | Meaning |         |      |
| BackLED  | Statusofmodularcomponents              |                               |          | On-Green  | Normal  |         |      |
installedinthebackofthe
chassis(notapplicablefor
SlowFlash-Amber Faultinoneofthemodulesin
6300Fswitches) thebackofthechassis
13
| AOS-CX10.07MonitoringGuide| | (6300and6400SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ------------------------- | --- | --- | --- | --- | --- | --- |

| Switch LEDs | Function             | State | Meaning            |
| ----------- | -------------------- | ----- | ------------------ |
| PoELED      | IndicatesPortLEDsare | Off   | PoEmodenotselected |
showingPoEinformation(not
|     | applicablefornonPoE | On-Green | PoEmodeselected |
| --- | ------------------- | -------- | --------------- |
switches)
|     |     | SlowFlash-Amber | HardwarefailurePoEenabled |
| --- | --- | --------------- | ------------------------- |
port,PoEmodenotselected
|     |     | On-Amber | HardwarefailurePoEenabled |
| --- | --- | -------- | ------------------------- |
port,PoEmodeselected
| SpdLED | IndicatesPortLEDsare | Off | Speedmodenotselected |
| ------ | -------------------- | --- | -------------------- |
showingspeedinformation
|        |                      | On-Green       | Speedmodeselected       |
| ------ | -------------------- | -------------- | ----------------------- |
|        |                      | NotImplemented | Nofaultdefined          |
| StkLED | IndicatesPortLEDsare | Off            | Stackingmodenotselected |
showingstackingmode
information
|     |     | On-Green | Stackingmodeselected      |
| --- | --- | -------- | ------------------------- |
|     |     | On-Amber | Aporthasastackingfailure. |
Stackingmodeselected
|     |     | SlowflashAmber | Aporthasastackingfailure. |
| --- | --- | -------------- | ------------------------- |
Stackingmodenotselected
| UIDLED | User-configurableLED | Off | UserdefinedthelocatedLED: |
| ------ | -------------------- | --- | ------------------------- |
OFF
|     |     | On/FlashBlue(for | UserdefinedthelocatorLED: |
| --- | --- | ---------------- | ------------------------- |
|     |     | 30min)           | On/Flash                  |
GlobalStatus Overallstatusoftheproduct Flash-Green Self-testinprogressduring
| IndicatorLED |     |          | UBOOT,SVOSandArubaOS-CV |
| ------------ | --- | -------- | ----------------------- |
|              |     | On-Green | Successfullyinitialized |
ArubaOS-CX
|     |     | Flash-Amber | Recoverablefaults(e.g.fans, |
| --- | --- | ----------- | --------------------------- |
PSUfault)
|     |     | On-Amber | Criticalfaults(e.g.exceed |
| --- | --- | -------- | ------------------------- |
temperaturelimit)
Aruba6300/6400SwitchSeriesLEDs|14

| Switch       | LEDs Function    |     | State | Meaning                   |
| ------------ | ---------------- | --- | ----- | ------------------------- |
| OOBMStatus   | StatusofOOBMLink |     | Off   | OOBMportisnotconnected,no |
| IndicatorLED | connectivity     |     |       | linkestablished           |
HalfBright-Green OOBMportisenabledand
establishedlinkwithpartner
On-Green Experiencinghighbandwidth
utilization
ActivityFlicker- %ofthetimethattheLEDlight
Green upisroughlyproportionaltothe
%offullbandwidthutilizationof
theport
*PresstheModeSelectbuttontoswitchbetweenUser(default),PoE,Spd,orStkMode.
| Table 3:     | RearPanelLEDbehavior |     |            |         |
| ------------ | -------------------- | --- | ---------- | ------- |
| Switch       | LEDs Function        |     | State/Mode | Meaning |
| FanhealthLED | Statusoffan          |     | On-Green   | Normal  |
Slowflash-Amber Fanfault
| UIDLED | User-configurableLED |     | Off | UserdefinethelocatorLED: |
| ------ | -------------------- | --- | --- | ------------------------ |
OFF
On/Flash(30min)- UserdefinethelocatorLED:
blue On/Flash
| PSUStatus | Statusofpowersupply |     | OnGreen | Normal |
| --------- | ------------------- | --- | ------- | ------ |
IndicatorLED
Off Nopower,PSUhasinvalidAC
inputofinvalidDCoutputs
SlowFlash-Green Powersupplyhasfaultedor
warning
| Switch | and port | LEDs for | 6400 Switch | Series |
| ------ | -------- | -------- | ----------- | ------ |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 15

| Figure 2 RearpanelLEDsfor6400SwitchSeries |          |                               |        |
| ----------------------------------------- | -------- | ----------------------------- | ------ |
| 1                                         |          | Powersupplystatus(1)(2)(3)(4) |        |
| 2                                         |          | ChassispowerLED               |        |
| 3                                         |          | ChassishealthLED              |        |
| 4                                         |          | Unitidentification(UID)LED    |        |
| 5                                         |          | Fantraystatus(1,2)            |        |
| Front panel                               | LEDs for | 6400 Switch                   | Series |
TheAruba6400switcheshavetwomanagementmodule(MM)slots.Managementmodulessupport
controlplaneactivitiesandin-memoryrunningoftheTimeSeriesDatabase.
| Figure 3 Managementmoduleslotswithmanagementmodulesinstalled |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- |
Aruba6300/6400SwitchSeriesLEDs|16

When two management modules are installed, one operates in active mode and the other operates in
standby mode. The active slot is determined by election. Installing two management modules provides
control plane high availability.

Figure 4 Management module features

1

2

3

4

5

6

7

8

Mgmt state (Actv) LED

System power LED

Management module health LED (green)

Line module status LEDs

Front Power supply status (1 2 3 4) LEDs

Fan tray status LEDs (1 - 4)

LED mode: Usr1, Usr2 Spd, and PoE LEDs

Auxillary port

Indicates the status of the management
module after booting. If the MM is the
active MM, then the LED glows steady
green.

When the system is receiving power, glows
steady green.=.

Indicates status of the switch. LED glows
steady green when switch is ready after
booting from the Network Operating
System (NOS).

Indicates if a line module is installed in a
line module slot (1 through 5 for 6405
switches; 1 through 10 on 6410 switches). If
a line module is installed in a given slot,
then the numbered LED for that slot glows
steady green.

Indicates if a power supply is installed in
the slot. If an active power supply is
installed, then the LEDs glow steady green.

Indicate if the fan tray is installed in the
slot. If a fan tray is installed in the slot, then
the LED glows steady green.

The display of these LEDs is based on the
LED mode button selection.

n Usr1 LED: Indicates if the line module is

working correctly.
n Usr2 LED: Reserved
n Spd LED: Indicates the traffic rate of the

line module.

Without a USB device installed, the
auxiliary port LED is off after power-on and
self-test. With a USB device installed, this
LED displays the following after power-on
and self-test:

n Steady green: USB installed, initialized,

and mounted, but no data transfer.

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

17

n Flickergreen:Datatransferinprogress
9 Mgmtport(OOBMPort)withActivity/Link Withoutanactivenetworkconnection,this
|     | LED | LEDisoffafterpower-onandself-test |
| --- | --- | --------------------------------- |
completes.Withanactivenetwork
connection,thisLEDoperatesasfollows:
n Half-brightgreen:Portenabledand
receivingLinkindicationfrom
connecteddevice.
n Flickeringhalf-brighttofull-bright
green:Varyingportactivitylevel.
n Steadygreen:Portathighutilization.
| 10  | Serialconsoleport(RJ-45) |                                   |
| --- | ------------------------ | --------------------------------- |
| 11  | USBMicro-Bconsoleport    |                                   |
| 12  | LEDModebutton            | Changesthebehaviorofthelinemodule |
portLEDs.ThisbuttonchangestheLED
behaviorfromthedefaultLink/Activity
behaviortocyclethroughthePoE,speed
(Spd),anduser(Usr)options.
| 13  | UID(UnitIdentification)LED |                     |
| --- | -------------------------- | ------------------- |
| 14  | PoE                        | Power-over-Ethernet |
15 Chassistemperaturestatus(Temp)LED Indicatesthestatusofthechassis
temperature.Ifthetemperatureisator
belowthespecifiedrating,thentheLED
glowssteadygreen,
| 16  | Mgmtresetbutton | Arecessedbuttonthatisusedtoresetthe |
| --- | --------------- | ----------------------------------- |
selectedmanagementmodule.
| 17  | Mgmtstate(Stby)LED | Indicatesthestatusofthemanagement |
| --- | ------------------ | --------------------------------- |
moduleafterbooting.IftheMMisthe
standbyMM,thentheLEDglowssteady
green.
Power SupplyLEDs
TheAruba6400hasfourpowersupplyunitslotsthatsupporttheArubaX38254DC2700WACpower
supplyunit(PSU).
Figure 5 ArubaX38254DC2700WACPowerSupply(JL372A)
1 PowerLED(green)
Aruba6300/6400SwitchSeriesLEDs|18

2

3

4

Power fail LED (amber)

Power supply handle

Latch release tab

n A single PSU is sufficient for fans and management cards to come up and provide user access and

diagnostics.

n At 220 V AC, only two PSUs are required for full operation and a single PSU is sufficient for the fans and

management cards to come up and provide user access/diagnostics.

n At 220 V AC: Installing three PSUs offers 2+1 redundancy and installing all four PSUs offers 2+2

redundancy.

n At 110 V AC: The switch offers N + 1 redundancy.

n The PSUs are hot-swappable. The chassis can be connected to an AC power source for a given PSU slot

while the PSU for that slot is being removed or installed.

1

2

3

4

Power LED (green)

Power fail LED (amber)

Power supply handle

Latch release tab

n A single PSU is sufficient for fans and management cards to come up and provide user access and

diagnostics.

n At 220 V AC, only two PSUs are required for full operation and a single PSU is sufficient for the fans and

management cards to come up and provide user access/diagnostics.

n At 220 V AC: Installing three PSUs offers 2+1 redundancy and installing all four PSUs offers 2+2

redundancy.

n At 110 V AC: The switch offers N + 1 redundancy.

n The PSUs are hot-swappable. The chassis can be connected to an AC power source for a given PSU slot

while the PSU for that slot is being removed or installed.

Line module LEDs

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

19

1*

2 *

3*

4*

5*

Line module 4-channel port LEDs

Line module port LED for upper port

Line module port LED for lower port

Line module port LED for upper uplink port

Line module port LED for lower uplink port

Aruba 6300/6400 Switch Series LEDs | 20

Chapter 4

Boot commands

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
This command will reboot the specified fabric module. Traffic performance may
be affected while the module is down. Rebooting the last fabric module will
stop traffic switching between line modules.
Do you want to continue (y/n)? y

switch#

Rebooting the fabric module in slot 1/1 when auto-confirm is enabled:

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

21

switch# boot fabric-module 1/3
This command will reboot the specified fabric module. Traffic performance may
be affected while the module is down. Rebooting the last fabric module will
stop traffic switching between line modules.
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

Boot commands | 22

Syntax

boot management-module {active | standby | <SLOT-ID>}

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

If you reboot the active management module and the standby management module is not available, you
are warned, you are prompted to save the configuration, and you are prompted to confirm the operation.

If you reboot the standby management module, the standby management module reboots and remains
the standby management module.

If you attempt to reboot a management module that is not available, the boot command is aborted.

Saving the configuration is not required. However, if you attempt to save the configuration and there is an
error during the save operation, the boot command is aborted.

Hewlett Packarrd Enterprise recommends that you use the boot management-module command instead of
pressing the module reset button to reboot a management module because if you are rebooting the only
available management module, the boot management-module command enables you to save the configuration,
cancel the reboot, or both.

Examples

Rebooting the active management module when the standby management module is available:

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

23

| switch#               | boot | management-module |     |         | active |          |                 |      |
| --------------------- | ---- | ----------------- | --- | ------- | ------ | -------- | --------------- | ---- |
| The management-module |      |                   |     | in slot | 1/5    | is going | down for reboot | now. |
Rebootingtheactivemanagementmodulewhenthestandbymanagementmoduleisnotavailable:
| switch#          | boot       | management-module |        |           | 1/5        |               |                |     |
| ---------------- | ---------- | ----------------- | ------ | --------- | ---------- | ------------- | -------------- | --- |
| The management   |            | module            |        | in slot   | 1/5        | is currently  | active and     | no  |
| standby          | management |                   | module |           | was found. |               |                |     |
| This             | will       | reboot            | the    | entire    | switch.    |               |                |     |
| Do you           | want       | to save           | the    | current   |            | configuration | (y/n)? n       |     |
| This             | will       | reboot            | the    | entire    | switch     | and render    | it unavailable |     |
| until            | the        | process           | is     | complete. |            |               |                |     |
| Continue         | (y/n)?     |                   | y      |           |            |               |                |     |
| The system       |            | is going          | down   | for       | reboot.    |               |                |     |
| boot set-default |            |                   |        |           |            |               |                |     |
Syntax
| boot set-default |     | {primary |     | | secondary} |     |     |     |     |
| ---------------- | --- | -------- | --- | ------------ | --- | --- | --- | --- |
Description
Setsthedefaultoperatingsystemimagetousewhenthesystemisbooted.
Commandcontext
Manager(#)
Parameters
primary
Selectstheprimarynetworkoperatingsystemimage.
secondary
Selectsthesecondarynetworkoperatingsystemimage.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Selectingtheprimaryimageasthedefaultbootimage:
| switch#     | boot | set-default |     | primary |          |     |     |     |
| ----------- | ---- | ----------- | --- | ------- | -------- | --- | --- | --- |
| Default     | boot | image       | set | to      | primary. |     |     |     |
| boot system |      |             |     |         |          |     |     |     |
Syntax
| boot system | [primary |     | | secondary |     | |   | serviceos] |     |     |
| ----------- | -------- | --- | ----------- | --- | --- | ---------- | --- | --- |
Description
Bootcommands|24

Reboots all modules on the switch. By default, the configured default operating system image is used.
Optional parameters enable you to specify which system image to use for the reboot operation and for
future reboot operations.

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

n If you select the primary or secondary optional parameter, that image becomes the configured default
boot image for future system reboots. The command fails if the switch is not able to set the operating
system image to the image you selected.

You can use the boot set-default command to change the configured default operating system image.

n If you select serviceos as the optional parameter, the configured default boot image remains the same,

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

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

25

| This will  | reboot the | entire switch    | and render | it unavailable |
| ---------- | ---------- | ---------------- | ---------- | -------------- |
| until the  | process    | is complete.     |            |                |
| Continue   | (y/n)? y   |                  |            |                |
| The system | is going   | down for reboot. |            |                |
Rebootingthesystemfromthesecondaryoperatingsystemimage,settingthesecondaryoperatingsystem
imageastheconfigureddefaultbootimage:
| switch#   | boot system  | secondary         |               |                |
| --------- | ------------ | ----------------- | ------------- | -------------- |
| Default   | boot image   | set to secondary. |               |                |
| Do you    | want to save | the current       | configuration | (y/n)? n       |
| This will | reboot the   | entire switch     | and render    | it unavailable |
| until the | process      | is complete.      |               |                |
| Continue  | (y/n)?       |                   |               |                |
y
| The system | is going | down for reboot. |     |     |
| ---------- | -------- | ---------------- | --- | --- |
Cancelingasystemreboot:
| switch#   | boot system  |               |               |                |
| --------- | ------------ | ------------- | ------------- | -------------- |
| Do you    | want to save | the current   | configuration | (y/n)? n       |
| This will | reboot the   | entire switch | and render    | it unavailable |
| until the | process      | is complete.  |               |                |
| Continue  | (y/n)?       |               |               |                |
n
Reboot aborted.
switch#
show boot-history
Syntax
| show boot-history | [all] |     |     |     |
| ----------------- | ----- | --- | --- | --- |
Description
Showsbootinformation.Whennoparametersarespecified,showsthemostrecentinformationaboutthe
bootoperation,andthethreepreviousbootoperationsfortheactivemanagementmodule.Whentheall
parameterisspecified,showsthebootinformationfortheactivemanagementmoduleandallavailableline
modules.Toviewboot-historyonthestandby,thecommandmustbesentonthestandbyconsole.
Commandcontext
Manager(#)
Parameters
all
Showsbootinformationfortheactivemanagementmoduleandallavailablelinemodules.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Bootcommands|26

Usage
Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereisa
previousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
system)andrebootreasons.Previousbootinformationisdisplayedinreversechronologicalorder.
Index
Thepositionofthebootinthehistoryfile.Range:0to3.
Boot ID
AuniqueIDfortheboot.Asystem-generated128-bitstring.
| Current Boot, | upfor<SECONDS>seconds |     |     |
| ------------- | --------------------- | --- | --- |
Forthecurrentboot,theshow boot-historycommandshowsthenumberofsecondsthemodulehas
beenrunningonthecurrentsoftware.
| Timestampboot | reason |     |     |
| ------------- | ------ | --- | --- |
Forpreviousbootoperations,theshow boot-historycommandshowsthetimeatwhichtheoperation
occurredandthereasonfortheboot.Thereasonforthebootisoneofthefollowingvalues:
| <DAEMON-NAME> | crash |     |     |
| ------------- | ----- | --- | --- |
Thedaemonidentifiedby<DAEMON-NAME>causedthemoduletoboot.
Kernelcrash
Theoperatingsystemsoftwareassociatedwiththemodulecausedthemoduletoboot.
Rebootrequestedthroughdatabase
TherebootoccurredbecauseofarequestmadethroughtheCLIorotherAPI.
Uncontrolledreboot
Thereasonfortherebootisnotknown.
Examples
Showingtheboothistoryoftheactivemanagementmodule:
| switch#    | show boot-history |     |     |
| ---------- | ----------------- | --- | --- |
| Management | module            |     |     |
=================
| Index : | 3                                  |                    |                  |
| ------- | ---------------------------------- | ------------------ | ---------------- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |                    |                  |
| Current | Boot, up for                       | 22 hrs 12 mins     | 22 secs          |
| Index : | 2                                  |                    |                  |
| Boot ID | : edfa2d6598d24e989668306c4a56a06d |                    |                  |
| 07 Aug  | 18 16:28:01                        | : Reboot requested | through database |
| Index : | 1                                  |                    |                  |
| Boot ID | : 0bda8d0361df4a7e8e3acdc1dba5caad |                    |                  |
| 07 Aug  | 18 14:08:46                        | : Reboot requested | through database |
| Index : | 0                                  |                    |                  |
| Boot ID | : 23da2b0e26d048d7b3f4b6721b69c110 |                    |                  |
| 07 Aug  | 18 13:00:46                        | : Reboot requested | through database |
switch#
Showingtheboothistoryoftheactivemanagementmoduleandalllinemodules:
switch#
|            | show boot-history | all |     |
| ---------- | ----------------- | --- | --- |
| Management | module            |     |     |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 27

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
Bootcommands|28

Chapter 5
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
| bluetooth     | disable      |          |        |              |          |
Syntax
| bluetooth disable    |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- |
| no bluetooth disable |     |     |     |     |     |
Description
DisablestheBluetoothfeatureontheswitch.TheBluetoothfeatureincludesbothBluetoothClassicand
BluetoothLowEnergy(BLE).Bluetoothisenabledbydefault.
ThenoformofthiscommandenablestheBluetoothfeatureontheswitch.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DisablingBluetoothontheswitch.<XXXX>istheswitchplatformand<NNNNNNNNNN>isthedevice
identifier.
| switch(config)# | bluetooth             | disable |     |     |     |
| --------------- | --------------------- | ------- | --- | --- | --- |
| switch# show    | bluetooth             |         |     |     |     |
| Enabled         | : No                  |         |     |     |     |
| Device name     | : <XXXX>-<NNNNNNNNNN> |         |     |     |     |
| switch(config)# | show running-config   |         |     |     |     |
...
| bluetooth | disabled |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
...
| bluetooth | enable |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
Syntax
| bluetooth enable    |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
| no bluetooth enable |     |     |     |     |     |
Description
ThiscommandenablestheBluetoothfeatureontheswitch.TheBluetoothfeatureincludesbothBluetooth
ClassicandBluetoothLowEnergy(BLE).
Default:Bluetoothisenabledbydefault.
ThenoformofthiscommanddisablestheBluetoothfeatureontheswitch.
29
| AOS-CX10.07MonitoringGuide| | (6300and6400SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------------- | --- | --- | --- | --- |

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
2018-10-14:06:57:53.534384|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
utilization poll interval is changed to 27
2018-10-14:06:58:30.805504|lldpd|103|LOG_INFO|MSTR|1|Configured LLDP tx-timer to 36
2018-10-14:07:01:01.577564|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
utilization poll interval is changed to 49

switch# clear events

switch# show events
---------------------------------------------------

Switch system and hardware commands | 30

| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2018-10-14:07:03:05.637544|hpe-sysmond|6301|LOG_INFO|MSTR|1|System resource
| utilization | poll interval | is changed | to 34 |
| ----------- | ------------- | ---------- | ----- |
| clear ip    | errors        |            |       |
Syntax
clear ip errors
Description
ClearsallIPerrorstatistics.
Commandcontext
Manager(#)
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Clearingandshowingiperrors:
| switch# | clear ip errors |     |     |
| ------- | --------------- | --- | --- |
| switch# | show ip errors  |     |     |
----------------------------------
| Drop reason |     | Packets |     |
| ----------- | --- | ------- | --- |
----------------------------------
| Malformed  | packets | 0   |     |
| ---------- | ------- | --- | --- |
| IP address | errors  | 0   |     |
...
domain-name
Syntax
| domain-name    | <NAME>   |     |     |
| -------------- | -------- | --- | --- |
| no domain-name | [<NAME>] |     |     |
Description
Specifiesthedomainnameoftheswitch.
Thenoformofthiscommandsetsthedomainnametothedefault,whichisnodomainname.
Commandcontext
config
Parameters
<NAME>
Specifiesthedomainnametobeassignedtotheswitch.Thefirstcharacterofthenamemustbealetter
oranumber.Length:1to32characters.
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 31

Authority

Administrators or local user group members with execution rights for this command.

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

Switch system and hardware commands | 32

myswitch(config)# show hostname
myswitch

Setting the host name to the default value:

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

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

33

config

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

Specifies the member and slot in the form m/s, where m is the member number, and s is the slot number.

<PRODUCT-NUM>

Specifies the product number of the line module. For example: JL363A

If there is a line module installed in the slot when you execute this command, <PRODUCT-NUM> is optional.
The switch reads the product number information from the module that is installed in the slot.

Switch system and hardware commands | 34

If there is no line module installed in the slot when you execute this command, <PRODUCT-NUM> is
required.

Authority

Administrators or local user group members with execution rights for this command.

Usage

The default configuration associated with a line module slot is:

n There is no module product number or interface configuration information associated with the slot. The

slot is available for the installation with any supported line module.

n The Admin State is Up (which is the default value for Admin State).

To add a line module to the configuration, you must use the module command either before or after you
install the physical module.

If you execute the module command after you install a line module in an empty slot, you can omit the
<PRODUCT-NUM> variable. The switch reads the product information from the installed module.

If the module is not installed in the slot when you execute the module command, you must specify a value
for the <PRODUCT-NUM> variable:

n The switch validates the product number of the module against the slot number you specify to ensure

that the right type of module is configured for the specified slot.

For example, the switch returns an error if you specify the product number of a line module for a slot
reserved for management modules.

n You can configure the line module interfaces before the line module is installed.

When you install the physical line module in a preconfigured slot, the following actions occur:

n If a product number was specified in the command and it matches the product number of the installed

module, the switch initializes the module.

n If a product number was specified in the command and the product number of the module does not

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

switch(config)# module 1/1 product-number jl363a

Configuring a line module that is already installed in slot 1/1:

switch(config)# module 1/1 product-number

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

35

Attempting to configure slot 1/1 for the future installation of a line module without specifying the product
number (returned error shown):

switch(config)# module 1/1 product-number
Line module '1/4' is not physically available. Please provide the product
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

Examples

Tracing with source, group, and LHR addresses and TTL:

Switch system and hardware commands | 36

| (switch)#           | mtrace        | 20.0.0.1 | 239.1.1.1 |          | lhr | 10.1.1.1 | ttl 10          |
| ------------------- | ------------- | -------- | --------- | -------- | --- | -------- | --------------- |
| Type escape         | sequence      | to       | abort.    |          |     |          |                 |
| Mtrace              | from 10.0.0.1 | for      | Source    | 20.0.0.1 |     | via      | Group 239.1.1.1 |
| From destination(?) |               | to       | source    | (?)...   |     |          |                 |
| Querying            | ful reverse   | path...  |           |          |     |          |                 |
0 10.0.0.1
| -1 30.0.0.1 | PIM | 0 ms |     |     |     |     |     |
| ----------- | --- | ---- | --- | --- | --- | --- | --- |
| -2 40.0.0.1 | PIM | 2 ms |     |     |     |     |     |
| -3 50.0.0.1 | PIM | 100  | ms  |     |     |     |     |
| -4 60.0.0.1 | PIM | 156  | ms  |     |     |     |     |
| -5 20.0.0.1 | PIM | 123  | ms  |     |     |     |     |
Tracingwithsourceandgroupaddresses:
| (switch)#           | mtrace      | 200.0.0.1  |        | 239.1.1.1 |     |           |           |
| ------------------- | ----------- | ---------- | ------ | --------- | --- | --------- | --------- |
| Type escape         | sequence    | to         | abort. |           |     |           |           |
| Mtrace              | from self   | for Source |        | 200.0.0.1 |     | via Group | 239.1.1.1 |
| From destination(?) |             | to         | source | (?)...    |     |           |           |
| Querying            | ful reverse | path...    |        |           |     |           |           |
0 10.0.0.1
| -1 30.0.0.1  | PIM | 0 ms |     |     |     |     |     |
| ------------ | --- | ---- | --- | --- | --- | --- | --- |
| -2 40.0.0.1  | PIM | 2 ms |     |     |     |     |     |
| -3 50.0.0.1  | PIM | 100  | ms  |     |     |     |     |
| -4 60.0.0.1  | PIM | 156  | ms  |     |     |     |     |
| -5 200.0.0.1 | PIM | 123  | ms  |     |     |     |     |
show bluetooth
Syntax
show bluetooth
Description
ShowsgeneralstatusinformationabouttheBluetoothwirelessmanagementfeatureontheswitch.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
Thiscommandshowsstatusinformationaboutthefollowing:
n TheUSBBluetoothadapter
ClientsconnectedusingBluetooth
n
TheswitchBluetoothfeature.
n
Theoutputoftheshow running-configcommandincludesBluetoothinformationonlyiftheBluetooth
featureisdisabled.
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 37

Thedevicenamegiventotheswitchincludestheswitchserialnumbertouniquelyidentifytheswitchwhile
pairingwithamobiledevice.
ThemanagementIPaddressisaprivatenetworkaddresscreatedformanagingtheswitchthrougha
Bluetoothconnection.
Examples
ExampleoutputwhenBluetoothisenabledbutnoBluetoothadapterisconnected.<XXXX>istheswitch
platformand<NNNNNNNNNN>isthedeviceidentifier.
| switch#     | show bluetooth |                       |     |     |     |
| ----------- | -------------- | --------------------- | --- | --- | --- |
| Enabled     |                | : Yes                 |     |     |     |
| Device name |                | : <XXXX>-<NNNNNNNNNN> |     |     |     |
| Adapter     | State          | : Absent              |     |     |     |
ExampleoutputwhenBluetoothisenabledandthereisaBluetoothadapterconnected:
| switch#     | show bluetooth |                       |     |     |     |
| ----------- | -------------- | --------------------- | --- | --- | --- |
| Enabled     |                | : Yes                 |     |     |     |
| Device name |                | : <XXXX>-<NNNNNNNNNN> |     |     |     |
| Adapter     | State          | : Ready               |     |     |     |
| Adapter     | IP address     | : 192.168.99.1        |     |     |     |
| Adapter     | MAC address    | : 480fcf-af153a       |     |     |     |
| Connected   | Clients        |                       |     |     |     |
-----------------
| Name | MAC | Address | IP Address | Connected | Since |
| ---- | --- | ------- | ---------- | --------- | ----- |
-------------- -------------- ------------ ------------------------
Mark's iPhone 089734-b12000 192.168.99.10 2018-07-09 08:47:22 PDT
ExampleoutputwhenBluetoothisdisabled:
| switch#     | show bluetooth |                       |     |     |     |
| ----------- | -------------- | --------------------- | --- | --- | --- |
| Enabled     |                | : No                  |     |     |     |
| Device name |                | : <XXXX>-<NNNNNNNNNN> |     |     |     |
show boot-history
Syntax
| show boot-history | [all] |     |     |     |     |
| ----------------- | ----- | --- | --- | --- | --- |
Description
Showsbootinformation.Whennoparametersarespecified,showsthemostrecentinformationaboutthe
bootoperation,andthethreepreviousbootoperationsfortheactivemanagementmodule.Whentheall
parameterisspecified,showsthebootinformationfortheactivemanagementmoduleandallavailableline
modules.Toviewboot-historyonthestandby,thecommandmustbesentonthestandbyconsole.
Commandcontext
Manager(#)
Parameters
all
Switchsystemandhardwarecommands|38

Showsbootinformationfortheactivemanagementmoduleandallavailablelinemodules.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereisa
previousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
system)andrebootreasons.Previousbootinformationisdisplayedinreversechronologicalorder.
Index
Thepositionofthebootinthehistoryfile.Range:0to3.
Boot ID
AuniqueIDfortheboot.Asystem-generated128-bitstring.
| Current Boot, | upfor<SECONDS>seconds |     |     |
| ------------- | --------------------- | --- | --- |
Forthecurrentboot,theshow boot-historycommandshowsthenumberofsecondsthemodulehas
beenrunningonthecurrentsoftware.
| Timestampboot | reason |     |     |
| ------------- | ------ | --- | --- |
Forpreviousbootoperations,theshow boot-historycommandshowsthetimeatwhichtheoperation
occurredandthereasonfortheboot.Thereasonforthebootisoneofthefollowingvalues:
| <DAEMON-NAME> | crash |     |     |
| ------------- | ----- | --- | --- |
Thedaemonidentifiedby<DAEMON-NAME>causedthemoduletoboot.
Kernelcrash
Theoperatingsystemsoftwareassociatedwiththemodulecausedthemoduletoboot.
Rebootrequestedthroughdatabase
TherebootoccurredbecauseofarequestmadethroughtheCLIorotherAPI.
Uncontrolledreboot
Thereasonfortherebootisnotknown.
Examples
Showingtheboothistoryoftheactivemanagementmodule:
| switch#    | show boot-history |     |     |
| ---------- | ----------------- | --- | --- |
| Management | module            |     |     |
=================
| Index : | 3                                  |                    |                  |
| ------- | ---------------------------------- | ------------------ | ---------------- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |                    |                  |
| Current | Boot, up for                       | 22 hrs 12 mins     | 22 secs          |
| Index : | 2                                  |                    |                  |
| Boot ID | : edfa2d6598d24e989668306c4a56a06d |                    |                  |
| 07 Aug  | 18 16:28:01                        | : Reboot requested | through database |
| Index : | 1                                  |                    |                  |
| Boot ID | : 0bda8d0361df4a7e8e3acdc1dba5caad |                    |                  |
| 07 Aug  | 18 14:08:46                        | : Reboot requested | through database |
| Index : | 0                                  |                    |                  |
| Boot ID | : 23da2b0e26d048d7b3f4b6721b69c110 |                    |                  |
| 07 Aug  | 18 13:00:46                        | : Reboot requested | through database |
switch#
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 39

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
| show capacities |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Syntax
| show capacities | <FEATURE> |     | [vsx-peer] |     |     |
| --------------- | --------- | --- | ---------- | --- | --- |
Description
Showssystemcapacitiesandtheirvaluesforallfeaturesoraspecificfeature.
Commandcontext
Manager(#)
Parameters
<FEATURE>
Specifiesafeature.Forexample,aaaorvrrp.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Capacitiesareexpressedinuser-understandableterms.Thustheymaynotmaptoaspecifichardwareor
softwareresourceorcomponent.Theyarenotintendedtodefineafeatureexhaustively.
Switchsystemandhardwarecommands|40

Examples
ShowingallavailablecapacitiesforBGP:
switch#
|                    | show capacities |        | bgp |     |     |     |     |       |     |
| ------------------ | --------------- | ------ | --- | --- | --- | --- | --- | ----- | --- |
| System Capacities: |                 | Filter |     | BGP |     |     |     |       |     |
| Capacities         | Name            |        |     |     |     |     |     | Value |     |
-----------------------------------------------------------------------------------
| Maximum | number of | AS  | numbers | in  | as-path | attribute |     |     | 32  |
| ------- | --------- | --- | ------- | --- | ------- | --------- | --- | --- | --- |
...
Showingallavailablecapacitiesformirroring:
| switch#            | show capacities |        | mirroring |           |     |     |     |       |     |
| ------------------ | --------------- | ------ | --------- | --------- | --- | --- | --- | ----- | --- |
| System Capacities: |                 | Filter |           | Mirroring |     |     |     |       |     |
| Capacities         | Name            |        |           |           |     |     |     | Value |     |
-----------------------------------------------------------------------------------
| Maximum | number of | Mirror  | Sessions |        | configurable |     | in a system |     | 4   |
| ------- | --------- | ------- | -------- | ------ | ------------ | --- | ----------- | --- | --- |
| Maximum | number of | enabled |          | Mirror | Sessions     | in  | a system    |     | 4   |
ShowingallavailablecapacitiesforMSTP:
| switch#            | show capacities |        | mstp |      |     |     |     |       |     |
| ------------------ | --------------- | ------ | ---- | ---- | --- | --- | --- | ----- | --- |
| System Capacities: |                 | Filter |      | MSTP |     |     |     |       |     |
| Capacities         | Name            |        |      |      |     |     |     | Value |     |
-----------------------------------------------------------------------------------
| Maximum | number of | mstp | instances |     | configurable |     | in a system |     | 64  |
| ------- | --------- | ---- | --------- | --- | ------------ | --- | ----------- | --- | --- |
ShowingallavailablecapacitiesforVLANcount:
| switch#            | show capacities |        | vlan-count |      |       |     |     |       |     |
| ------------------ | --------------- | ------ | ---------- | ---- | ----- | --- | --- | ----- | --- |
| System Capacities: |                 | Filter |            | VLAN | Count |     |     |       |     |
| Capacities         | Name            |        |            |      |       |     |     | Value |     |
-----------------------------------------------------------------------------------
| Maximum                | number of | VLANs | supported |     | in  | the system |     |     | 4094 |
| ---------------------- | --------- | ----- | --------- | --- | --- | ---------- | --- | --- | ---- |
| show capacities-status |           |       |           |     |     |            |     |     |      |
Syntax
| show capacities-status |     | <FEATURE> |     | [vsx-peer] |     |     |     |     |     |
| ---------------------- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- |
Description
Showssystemcapacitiesstatusandtheirvaluesforallfeaturesoraspecificfeature.
Commandcontext
Manager(#)
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 41

Parameters
<FEATURE>
Specifiesthefeature,forexampleaaaorvrrpforwhichtodisplaycapacities,values,andstatus.
Required.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Showingthesystemcapacitiesstatusforallfeatures:
switch#
show capacities-status
| System     | Capacities | Status |     |     |     |     |               |
| ---------- | ---------- | ------ | --- | --- | --- | --- | ------------- |
| Capacities | Status     | Name   |     |     |     |     | Value Maximum |
------------------------------------------------------------------------------------
| Number | of active          | gateway | mac        | addresses | in  | a system | 0 16 |
| ------ | ------------------ | ------- | ---------- | --------- | --- | -------- | ---- |
| Number | of aspath-lists    |         | configured |           |     |          | 0 64 |
| Number | of community-lists |         | configured |           |     |          | 0 64 |
...
ShowingthesystemcapacitiesstatusforBGP:
| switch#    | show capacities-status |         |        | bgp |     |     |               |
| ---------- | ---------------------- | ------- | ------ | --- | --- | --- | ------------- |
| System     | Capacities             | Status: | Filter | BGP |     |     |               |
| Capacities | Status                 | Name    |        |     |     |     | Value Maximum |
------------------------------------------------------------------------------------
| Number | of aspath-lists    |        | configured |        |     |      | 0 64     |
| ------ | ------------------ | ------ | ---------- | ------ | --- | ---- | -------- |
| Number | of community-lists |        | configured |        |     |      | 0 64     |
| Number | of neighbors       |        | configured | across | all | VRFs | 0 50     |
| Number | of peer            | groups | configured | across | all | VRFs | 0 25     |
| Number | of prefix-lists    |        | configured |        |     |      | 0 64     |
| Number | of route-maps      |        | configured |        |     |      | 0 64     |
| Number | of routes          | in     | BGP RIB    |        |     |      | 0 256000 |
Number of route reflector clients configured across all VRFs 0 16
show core-dump
Syntax
show core-dump[all|<SLOT-ID>]
Description
Showscoredumpinformationaboutthespecifiedmodule.Whennoparametersarespecified,showsonly
thecoredumpsgeneratedinthecurrentbootofthemanagementmodule.Whentheallparameteris
specified,showsallavailablecoredumps.
Commandcontext
Manager(#)
Switchsystemandhardwarecommands|42

Parameters

all

Shows all available core dumps.

<SLOT-ID>

Shows the core dumps for the management module or line module in <SLOT-ID>. <SLOT-ID> specifies a
physical location on the switch. Use the format member/slot/port (for example, 1/3/1) for line modules.
Use the format member/slot for management modules.

You must specify the slot ID for either the active management module, or the line module.

Authority

Administrators or local user group members with execution rights for this command.

Usage

When no parameters are specified, the show core-dump command shows only the core dumps generated in
the current boot of the management module. You can use this command to determine when any crashes
are occurring in the current boot.

If no core dumps have occurred, the following message is displayed: No core dumps are present

To show core dump information for the standby management module, you must use the standby
command to switch to the standby management module and then execute the show core-dump command.

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

| Instance ID | Present

switch# show core-dump
==================================================================================
Daemon Name
==================================================================================
hpe-fand
hpe-sysmond
==================================================================================
Total number of core dumps : 2
==================================================================================

2017-08-04 19:05:34
2017-08-04 19:05:29

1246d2a
1246d2a

| Timestamp

| Build ID

1399
957

Yes
Yes

Showing all core dumps:

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

43

| switch# show | core-dump | all |     |     |     |
| ------------ | --------- | --- | --- | --- | --- |
=============================================================================
| Management | Module core-dumps |     |     |     |     |
| ---------- | ----------------- | --- | --- | --- | --- |
=============================================================================
| Daemon Name | | Instance | ID | Present | | Timestamp |     | | Build ID |
| ----------- | ---------- | ------------ | ----------- | --- | ---------- |
=============================================================================
| hpe-sysmond | 513        | Yes | 2017-07-31 | 13:58:05 | e70f101 |
| ----------- | ---------- | --- | ---------- | -------- | ------- |
| hpe-tempd   | 1048       | Yes | 2017-08-13 | 13:31:53 | e70f101 |
| hpe-tempd   | 1052       | Yes | 2017-08-13 | 13:41:44 | e70f101 |
| Line Module | core-dumps |     |            |          |         |
=============================================================================
| Line Module | : 1/1 |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
=============================================================================
| dune_agent_0 | 18958 | Yes | 2017-08-12 | 11:50:17 | e70f101 |
| ------------ | ----- | --- | ---------- | -------- | ------- |
| dune_agent_0 | 18842 | Yes | 2017-08-12 | 11:50:09 | e70f101 |
=============================================================================
| Total number | of core | dumps : 5 |     |     |     |
| ------------ | ------- | --------- | --- | --- | --- |
=============================================================================
show domain-name
Syntax
| show domain-name | [vsx-peer] |     |     |     |     |
| ---------------- | ---------- | --- | --- | --- | --- |
Description
Showsthecurrentdomainname.
Commandcontext
Manager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Ifthereisnodomainnameconfigured,theCLIdisplaysablankline.
Example
Settingandshowingthedomainname:
| switch# show    | domain-name |             |     |     |     |
| --------------- | ----------- | ----------- | --- | --- | --- |
| switch# config  |             |             |     |     |     |
| switch(config)# | domain-name | example.com |     |     |     |
| switch(config)# | show        | domain-name |     |     |     |
Switchsystemandhardwarecommands|44

example.com
switch(config)#

show environment fan

Syntax

show environment fan [vsf <MEMBER-ID> | vsx-peer]

Description

Shows the status information for all fans and fan trays (if present) in the system.

Command context

Manager (#)

Parameters

vsf <MEMBER-ID>

Shows output from the VSF member-id on switches that support VSF.

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

Max

The fan is running at 100% of its maximum speed.

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

45

N/A
Thefanisnotinstalled.
Direction
Thedirectionofairflowthroughthefan.Valuesare:
front-to-back
Airflowsfromthefrontofthesystemtothebackofthesystem.
N/A
Thefanisnotinstalled.
Status
Fanstatus.Valuesare:
uninitialized
Thefanhasnotcompletedinitialization.
ok
Thefanisoperatingnormally.
fault
Thefanisinafaultstate.
empty
Thefanisnotinstalled.
Examples
Showingoutputforsystemswithfantraysfor6400switchseries:
| switch#  | show environment | fan |     |     |     |     |
| -------- | ---------------- | --- | --- | --- | --- | --- |
| Fan tray | information      |     |     |     |     |     |
------------------------------------------------------------------------------
| Mbr/Tray | Description |     |     | Status | Serial Number | Fans |
| -------- | ----------- | --- | --- | ------ | ------------- | ---- |
------------------------------------------------------------------------------
| 1/1 | R0X32A Aruba | 6400 Fan Tray |     | ready | SG9ZKJL7JW | 4   |
| --- | ------------ | ------------- | --- | ----- | ---------- | --- |
| 1/2 | R0X32A Aruba | 6400 Fan Tray |     | ready | SG9ZKJL7GL | 4   |
| 1/3 | R0X32A Aruba | 6400 Fan Tray |     | ready | SG9ZKJL78L | 4   |
| 1/4 | R0X32A Aruba | 6400 Fan Tray |     | ready | SG9ZKJL7GJ | 4   |
Fan information
---------------------------------------------------------------------------
Mbr/Tray/Fan Product Serial Number Speed Direction Status RPM
Name
---------------------------------------------------------------------------
| 1/1/1 | N/A | N/A | slow front-to-back |     | ok 5371 |     |
| ----- | --- | --- | ------------------ | --- | ------- | --- |
| 1/1/2 | N/A | N/A | slow front-to-back |     | ok 5320 |     |
| 1/1/3 | N/A | N/A | slow front-to-back |     | ok 5328 |     |
| 1/1/4 | N/A | N/A | slow front-to-back |     | ok 5256 |     |
| 1/2/1 | N/A | N/A | slow front-to-back |     | ok 5371 |     |
| 1/2/2 | N/A | N/A | slow front-to-back |     | ok 5349 |     |
| 1/2/3 | N/A | N/A | slow front-to-back |     | ok 5292 |     |
| 1/2/4 | N/A | N/A | slow front-to-back |     | ok 5349 |     |
| 1/3/1 | N/A | N/A | slow front-to-back |     | ok 5313 |     |
| 1/3/2 | N/A | N/A | slow front-to-back |     | ok 5371 |     |
| 1/3/3 | N/A | N/A | slow front-to-back |     | ok 5379 |     |
| 1/3/4 | N/A | N/A | slow front-to-back |     | ok 5379 |     |
| 1/4/1 | N/A | N/A | slow front-to-back |     | ok 5313 |     |
| 1/4/2 | N/A | N/A | slow front-to-back |     | ok 5299 |     |
| 1/4/3 | N/A | N/A | slow front-to-back |     | ok 5285 |     |
| 1/4/4 | N/A | N/A | slow front-to-back |     | ok 5371 |     |
Showingoutputforasystemwithoutafantray:
Switchsystemandhardwarecommands|46

| switch# show | environment | fan |     |     |
| ------------ | ----------- | --- | --- | --- |
Fan information
---------------------------------------------------------------
| Fan Serial | Number Speed | Direction | Status | RPM |
| ---------- | ------------ | --------- | ------ | --- |
---------------------------------------------------------------
| 1 SGXXXXXXXXXX | slow   | front-to-back | ok    | 6000  |
| -------------- | ------ | ------------- | ----- | ----- |
| 2 SGXXXXXXXXXX | normal | front-to-back | ok    | 8000  |
| 3 SGXXXXXXXXXX | medium | front-to-back | ok    | 11000 |
| 4 SGXXXXXXXXXX | fast   | front-to-back | ok    | 14000 |
| 5 SGXXXXXXXXXX | max    | front-to-back | fault | 16500 |
| 6 N/A          | N/A    | N/A           | empty |       |
...
| show environment |     | led |     |     |
| ---------------- | --- | --- | --- | --- |
Syntax
| show environment | led [vsf | <MEMBER-ID>| | vsx-peer] |     |
| ---------------- | -------- | ------------ | --------- | --- |
Description
ShowsstateandstatusinformationforalltheconfigurableLEDsinthesystem.
Commandcontext
Operator(>)orManager(#)
Parameters
vsf <MEMBER-ID>
ShowsoutputfromthespecifiedVSFmember-idonswitchesthatsupportVSF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowstateandstatusfortheenvironmentLED:
| switch# show | environment | led    |     |     |
| ------------ | ----------- | ------ | --- | --- |
| Mbr/Name     | State       | Status |     |     |
-------------------------------
| 1/locator        | off | ok                |     |     |
| ---------------- | --- | ----------------- | --- | --- |
| show environment |     | power-consumption |     |     |
Syntax
| show environment | power-consumption | [vsx-peer] |     |     |
| ---------------- | ----------------- | ---------- | --- | --- |
Notsupportedonthe6300SwitchSeries.
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 47

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

Chassis Total Power Allocated

Shows total power, in Watts, that is allocated to powering the chassis and its installed modules.

Chassis Total Power Unallocated

Shows the total amount of power, in Watts, that has not been allocated to powering the chassis or its
installed modules. This power can be used for additional hardware you install in the chassis.

Example

Switch system and hardware commands | 48

ShowingthepowerconsumptionforanAruba6400switch:
| switch> show | environment | power-consumption |     |     |     |
| ------------ | ----------- | ----------------- | --- | --- | --- |
Power
| Name Type |     | Description |     |     | Usage |
| --------- | --- | ----------- | --- | --- | ----- |
------------------------------------------------------------------------------
| 1/1 management-module |     | R0X31A 6400 | Management | Module | 18 W |
| --------------------- | --- | ----------- | ---------- | ------ | ---- |
| 1/2 management-module |     |             |            |        | 0 W  |
| 1/3 line-card-module  |     |             |            |        | 0 W  |
1/4 line-card-module R0X39A 6400 48p 1GbE CL4 PoE 4SFP56 Mod 54 W
| 1/5 line-card-module |     |     |     |     | 0 W |
| -------------------- | --- | --- | --- | --- | --- |
1/6 line-card-module R0X39A 6400 48p 1GbE CL4 PoE 4SFP56 Mod 56 W
1/7 line-card-module R0X39A 6400 48p 1GbE CL4 PoE 4SFP56 Mod 51 W
| 1/1 fabric-card-module |                 | R0X24A 6405  | Chassis |     | 71 W   |
| ---------------------- | --------------- | ------------ | ------- | --- | ------ |
| Module Total           | Power Usage     |              |         |     | 250 W  |
| Chassis Total          | Power Usage     |              |         |     | 294 W  |
| Chassis Total          | Power Available |              |         |     | 1800 W |
| show environment       |                 | power-supply |         |     |        |
Syntax
| show environment | power-supply | [vsf <MEMBER-ID> | | vsx-peer] |     |     |
| ---------------- | ------------ | ---------------- | ----------- | --- | --- |
Description
Showsstatusinformationaboutallpowersuppliesintheswitch.
Commandcontext
Operator(>)orManager(#)
Parameters
vsf <MEMBER-ID>
ShowsoutputfromtheVSFmember-idonswitchesthatsupportVSF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
Thefollowinginformationisprovidedforeachpowersupply:
Mbr/PSU
Showsthememberandslotnumberofthepowersupply.
Product Number
Showstheproductnumberofthepowersupply.
SerialNumber
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 49

Showstheserialnumberofthepowersupply,whichuniquelyidentifiesthepowersupply.
PSUStatus
Thestatusofthepowersupply.Valuesare:
OK
Powersupplyisoperatingnormally.
OK*
Powersupplyisoperatingnormally,butitistheonlypowersupplyinthechassis.Onepowersupplyis
notsufficienttosupplyfullpowertotheswitch.Whenthisvalueisshown,theoutputofthe
commandalsoshowsamessageattheendofthedisplayeddata.
Absent
Nopowersupplyisinstalledinthespecifiedslot.
| Input fault |     |     |     |     |
| ----------- | --- | --- | --- | --- |
Thepowersupplyhasafaultconditiononitsinput.
| Output | fault |     |     |     |
| ------ | ----- | --- | --- | --- |
Thepowersupplyhasafaultconditiononitsoutput.
Warning
Thepowersupplyisnotoperatingnormally.
| Wattage Maximum |     |     |     |     |
| --------------- | --- | --- | --- | --- |
Showsthemaximumamountofwattagethatthepowersupplycanprovide.
Example
ShowingtheoutputwhenonlyonepowersupplyisinstalledinanAruba6400switchchassis:
| switch# | show environment | power-supply |        |         |
| ------- | ---------------- | ------------ | ------ | ------- |
|         | Product          | Serial       | PSU    | Wattage |
| Mbr/PSU | Number           | Number       | Status | Maximum |
--------------------------------------------------------------
| 1/1  | R0X36A      | CN91KMM2H3          | OK     | 3000 |
| ---- | ----------- | ------------------- | ------ | ---- |
| 1/2  | N/A         | N/A                 | Absent | 0    |
| 1/3  | N/A         | N/A                 | Absent | 0    |
| 1/4  | N/A         | N/A                 | Absent | 0    |
| show | environment | rear-display-module |        |      |
Syntax
| show environment | rear-display-module |     | [vsx-peer] |     |
| ---------------- | ------------------- | --- | ---------- | --- |
Description
Showsinformationaboutthedisplaymoduleonthebackoftheswitch(Aruba8400switchesonly).
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Switchsystemandhardwarecommands|50

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

show environment temperature [detail] [vsf <MEMBER-ID> | vsx-peer]

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

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

51

critical
Highestthresholdtemperatureforthissensor.
fault
Faulteventforthissensor.
emergency
Overtemperatureeventforthissensor.
Examples
Showingcurrenttemperatureinformationfora6300switch:
| switch# show | environment | temperature |     |     |     |
| ------------ | ----------- | ----------- | --- | --- | --- |
| Temperature  | information |             |     |     |     |
------------------------------------------------------------------------------
Current
| Mbr/Slot-Sensor |     |     | Module Type | temperature | Status |
| --------------- | --- | --- | ----------- | ----------- | ------ |
------------------------------------------------------------------------------
| 1/1-PHY-01-04            |     |     | line-card-module  | 45.00 | C normal |
| ------------------------ | --- | --- | ----------------- | ----- | -------- |
| 1/1-PHY-05-08            |     |     | line-card-module  | 45.00 | C normal |
| 1/1-PHY-09-12            |     |     | line-card-module  | 46.00 | C normal |
| 1/1-PHY-13-16            |     |     | line-card-module  | 47.00 | C normal |
| 1/1-PHY-17-20            |     |     | line-card-module  | 47.00 | C normal |
| 1/1-PHY-21-24            |     |     | line-card-module  | 50.00 | C normal |
| 1/1-PHY-25-28            |     |     | line-card-module  | 45.00 | C normal |
| 1/1-PHY-29-32            |     |     | line-card-module  | 47.00 | C normal |
| 1/1-PHY-33-36            |     |     | line-card-module  | 48.00 | C normal |
| 1/1-PHY-37-40            |     |     | line-card-module  | 47.00 | C normal |
| 1/1-PHY-41-44            |     |     | line-card-module  | 48.00 | C normal |
| 1/1-PHY-45-48            |     |     | line-card-module  | 49.00 | C normal |
| 1/1-Switch-ASIC-Internal |     |     | line-card-module  | 56.25 | C normal |
| 1/1-CPU-Zone-0           |     |     | management-module | 50.00 | C normal |
| 1/1-CPU-Zone-1           |     |     | management-module | 50.00 | C normal |
| 1/1-CPU-Zone-2           |     |     | management-module | 50.00 | C normal |
| 1/1-CPU-Zone-3           |     |     | management-module | 51.00 | C normal |
| 1/1-CPU-Zone-4           |     |     | management-module | 51.00 | C normal |
| 1/1-CPU-diode            |     |     | management-module | 53.12 | C normal |
| 1/1-DDR                  |     |     | management-module | 45.25 | C normal |
| 1/1-Inlet-Air            |     |     | management-module | 24.88 | C normal |
| 1/1-MB-IBC               |     |     | management-module | 45.62 | C normal |
| 1/1-Switch-ASIC-diode    |     |     | management-module | 58.06 | C normal |
Showingdetailedtemperatureinformationfora6300switch:
| switch# show         | environment | temperature | detail |     |     |
| -------------------- | ----------- | ----------- | ------ | --- | --- |
| Detailed temperature |             | information |        |     |     |
----------------------------------------------------------------
| Mbr/Slot-Sensor     |     | : 1/1-PHY-01-04    |                 |            |      |
| ------------------- | --- | ------------------ | --------------- | ---------- | ---- |
| Module Type         |     | : line-card-module |                 |            |      |
| Module Description  |     | : JL659A           | 6300M 48SR5 CL6 | PoE 4SFP56 | Swch |
| Status              |     | : normal           |                 |            |      |
| Fan-state           |     | : normal           |                 |            |      |
| Current temperature |     | : 45.00            | C               |            |      |
| Minimum temperature |     | : 41.00            | C               |            |      |
| Maximum temperature |     | : 50.00            | C               |            |      |
| Mbr/Slot-Sensor     |     | : 1/1-PHY-05-08    |                 |            |      |
| Module Type         |     | : line-card-module |                 |            |      |
| Module Description  |     | : JL659A           | 6300M 48SR5 CL6 | PoE 4SFP56 | Swch |
| Status              |     | : normal           |                 |            |      |
Switchsystemandhardwarecommands|52

| Fan-state |             |     | : normal |     |     |     |
| --------- | ----------- | --- | -------- | --- | --- | --- |
| Current   | temperature |     | : 45.00  | C   |     |     |
| Minimum   | temperature |     | : 41.00  | C   |     |     |
| Maximum   | temperature |     | : 50.00  | C   |     |     |
...
| show | events |     |     |     |     |     |
| ---- | ------ | --- | --- | --- | --- | --- |
Syntax
| show events | [ -e    | <EVENT-ID>         | |       |              |          |                  |
| ----------- | ------- | ------------------ | ------- | ------------ | -------- | ---------------- |
| -s          | {alert  | | crit             | | debug | | emer | err | | info | | notice | warn} | |
| -r          | | -a    | | -i <MEMBER/SLOT> |         | | -n <count> | |        |                  |
| -m          | {active | | standby}         | |       |              |          |                  |
| -c          | {lldp   | | ospf |           | ... | } | |            |          |                  |
| -d          | {lldpd  | | hpe-fand         | | ...   | |}]          |          |                  |
For6300switches:
| show events | [ -e    | <EVENT-ID>         | |       |              |          |                  |
| ----------- | ------- | ------------------ | ------- | ------------ | -------- | ---------------- |
| -s          | {alert  | | crit             | | debug | | emer | err | | info | | notice | warn} | |
| -r          | | -a    | | -i <MEMBER-SLOT> |         | | -n <count> | |        |                  |
| -m          | {master | | standby}         | |       |              |          |                  |
| -c          | {lldp   | | ospf |           | ... | } | |            |          |                  |
| -d          | {lldpd  | | hpe-fand         | | ...   | |}]          |          |                  |
Description
Showseventlogsgeneratedbytheswitchmodulessincethelastreboot.
Commandcontext
Manager(#)
Parameters
-e <EVENT-ID>
ShowstheeventlogsforthespecifiedeventID.EventIDrange:101through99999.
| -s {alert | | crit | | debug | | emer | | err | | info | notice | | warn} |
| --------- | ------ | ------- | ------ | ------- | ------------- | ------- |
Showstheeventlogsforthespecifiedseverity.Selecttheseverityfromthefollowinglist:
n alert:Displayseventlogswithseverityalertandabove.
n crit:Displayseventlogswithseveritycriticalandabove.
debug:Displayseventlogswithallseverities.
n
emer:Displayseventlogswithseverityemergencyonly.
n
n err:Displayseventlogswithseverityerrorandabove.
n info:Displayseventlogswithseverityinfoandabove.
n notice:Displayseventlogswithseveritynoticeandabove.
n warn:Displayseventlogswithseveritywarningandabove.
-r
Showsthemostrecenteventlogsfirst.
-a
Showsalleventlogs,includingthoseeventsfrompreviousboots.
-i <MEMBER-SLOT>
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 53

ShowstheeventlogsforthespecifiedslotIDona6400switch.
-i <MEMBER-ID>
ShowstheeventlogsforthespecifiedVSFmemberIDona6300switch.
-n <count>
Displaysthespecifiednumberofeventlogs.
| -m {active | | standby} |     |
| ---------- | ---------- | --- |
Showstheeventlogsforthespecifiedmanagementcardroleonan8400or6400switch.Selectingactive
displaystheeventlogfortheAMMmanagementcardroleandstandbydisplayseventlogsfortheSMM
managementcardrole.
| -m {master | | standby} |     |
| ---------- | ---------- | --- |
Showstheeventlogsforthespecifiedroleona6200or6300switch.Selectingmasterdisplaystheevent
logfortheVSFmasterroleandstandbydisplayseventlogsfortheVSFstandbyrole.
| -c {lldp | | ospf | | ... | } |
| -------- | -------- | ------- |
Showstheeventlogsforthespecifiedeventcategory.Entershow event -cforafulllistingofsupported
categorieswithdescriptions.
| -d {lldpd | | hpe-fand | | ... |} |
| --------- | ---------- | -------- |
Showstheeventlogsforthespecifiedprocess.Entershow event -dforafulllistingofsupported
daemonswithdescriptions.
Authority
AuditorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.Auditors
canexecutethiscommandfromtheauditorcontext(auditor>)only.
Examples
Showingeventlogs:
| switch# | show events |     |
| ------- | ----------- | --- |
---------------------------------------------------
| show | event logs |     |
| ---- | ---------- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to up for
| bridge_normal |     | interface |
| ------------- | --- | --------- |
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1 in
Hardware
Showingthemostrecenteventlogsfirst:
| switch# | show events | -r  |
| ------- | ----------- | --- |
---------------------------------------------------
| show | event logs |     |
| ---- | ---------- | --- |
---------------------------------------------------
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1 in
Hardware
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to up for
| bridge_normal |     | interface |
| ------------- | --- | --------- |
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Showingalleventlogs:
Switchsystemandhardwarecommands|54

| switch# show | events | -a  |
| ------------ | ------ | --- |
---------------------------------------------------
| show event | logs |     |
| ---------- | ---- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to up for
| bridge_normal | interface |     |
| ------------- | --------- | --- |
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1 in
Hardware
ShowingeventlogsrelatedtotheDHCPrelayagent:
| switch# show | events | -c dhcp-relay |
| ------------ | ------ | ------------- |
2016-05-31:06:26:27.363923|hpe-relay|110001|LOG_INFO|DHCP Relay Enabled
2016-05-31:07:08:51.351755|hpe-relay|110002|LOG_INFO|DHCP Relay Disabled
ShowingeventlogsrelatedtotheDHCPv6relayagent:
| switch# show | events | -c dhcpv6-relay |
| ------------ | ------ | --------------- |
2016-05-31:06:26:27.363923|hpe-relay|109001|LOG_INFO|DHCPv6 Relay Enabled
2016-05-31:07:08:51.351755|hpe-relay|109002|LOG_INFO|DHCPv6 Relay Disabled
ShowingeventlogsrelatedtoIRDP:
| switch# switch# | show | events -c irdp |
| --------------- | ---- | -------------- |
2016-05-31:06:26:27.363923|hpe-rdiscd|111001|LOG_INFO|IRDP enabled on interface %s
2016-05-31:07:08:51.351755|hpe-rdiscd|111002|LOG_INFO|IRDP disabled on interface %s
ShowingeventlogsrelatedtoLACP:
| switch# show | events | -c lacp |
| ------------ | ------ | ------- |
---------------------------------------------------
| show event | logs |     |
| ---------- | ---- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Showingeventlogsasperthespecifiedmanagementcardrolefora6400switch:
| switch# show | events | -m active |
| ------------ | ------ | --------- |
---------------------------------------------------
| show event | logs |     |
| ---------- | ---- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
2016-12-01:12:37:31.734541|intfd|4001|INFO|AMM|1|Interface port_admin set to up for
| bridge_normal | interface |     |
| ------------- | --------- | --- |
2016-12-01:12:37:32.583256|switchd|24002|ERR|AMM|1|Failed to create VLAN 1 in
Hardware
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 55

Showingeventlogsasperthespecifiedmanagementcardroleforaswitch:
| switch# | show events | -m master |     |
| ------- | ----------- | --------- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2020-04-22T05:36:13.348594+00:00 6300 lldpd[3055]: Event|109|LOG_
| INFO|MSTR|1|Configured |     | LLDP tx-delay | to 2 |
| ---------------------- | --- | ------------- | ---- |
2020-04-22T05:36:14.430166+00:00 6300 vrfmgrd[3053]: Event|5401|LOG_
INFO|MSTR|1|Created a vrf entity b1721d27-41c2-485d-9bae-2cfcbc9bd13d
2020-04-22T05:36:14.942597+00:00 6300 vrfmgrd[3053]: Event|5401|LOG_
INFO|MSTR|1|Created a vrf entity 5eb532c9-5b4d-4d83-b34a-db24ae542d4e
ShowingeventlogsasperthespecifiedslotIDfora6400switch:
| switch# | show events | -i 1/1 |     |
| ------- | ----------- | ------ | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2017-08-17:22:32:25.743991|hpe-sysmond|6301|LOG_INFO|LC|1/1|System resource
| utilization | poll interval | is changed | to 313 |
| ----------- | ------------- | ---------- | ------ |
2017-08-17:22:33:01.692860|hpe-sysmond|6301|LOG_INFO|LC|1/1|System resource
| utilization | poll interval | is changed | to 23 |
| ----------- | ------------- | ---------- | ----- |
2017-08-17:22:33:06.181436|hpe-sysmond|6301|LOG_INFO|LC|1/1|System resource
| utilization | poll interval | is changed | to 512 |
| ----------- | ------------- | ---------- | ------ |
2017-08-17:22:33:06.181436|systemd-coredump|1201|LOG_CRIT|LC|1/1|hpe-sysmond crashed
due to signal:11
ShowingeventlogsasperthespecifiedslotID:
switch#
|     | show events | -i 1 |     |
| --- | ----------- | ---- | --- |
---------------------------------------------------
| Event logs | from current | boot |     |
| ---------- | ------------ | ---- | --- |
---------------------------------------------------
2020-04-22T05:36:14.430166+00:00 6300 vrfmgrd[3053]: Event|5401|LOG_
INFO|MSTR|1|Created a vrf entity b1721d27-41c2-485d-9bae-2cfcbc9bd13d
2020-04-22T05:36:14.942597+00:00 6300 vrfmgrd[3053]: Event|5401|LOG_
INFO|MSTR|1|Created a vrf entity 5eb532c9-5b4d-4d83-b34a-db24ae542d4e
2020-04-22T05:36:15.886252+00:00 6300 vsfd[710]: Event|9903|LOG_INFO|MSTR|1|Master 1
boot complete
Showingeventlogsasperthespecifiedprocess:
| switch# | show events | -d lacpd |     |
| ------- | ----------- | -------- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
---------------------------------------------------
2016-12-01:12:37:31.733551|lacpd|15007|INFO|AMM|1|LACP system ID set to
70:72:cf:51:50:7c
Displayingthespecifiednumberofeventlogs:
switch#
|     | show events | -n 5 |     |
| --- | ----------- | ---- | --- |
---------------------------------------------------
| show event | logs |     |     |
| ---------- | ---- | --- | --- |
Switchsystemandhardwarecommands|56

---------------------------------------------------
2018-03-21:06:12:15.500603|arpmgrd|6101|LOG_INFO|AMM|-|ARPMGRD daemon has started
2018-03-21:06:12:17.734405|lldpd|109|LOG_INFO|AMM|-|Configured LLDP tx-delay to 2
2018-03-21:06:12:17.740517|lacpd|1307|LOG_INFO|AMM|-|LACP system ID set to
70:72:cf:d4:34:42
2018-03-21:06:12:17.743491|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
42cc3df7-1113-412f-b5cb-e8227b8c22f2
2018-03-21:06:12:17.904008|vrfmgrd|5401|LOG_INFO|AMM|-|Created a vrf entity
4409133e-2071-4ab8-adfe-f9662c06b889

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

switch# show fabric

Fabric Modules
==============

Product

Name Number Description
---- ------- --------------------------------
1/1 R0X25A 6410 Chassis
1/2 R0X25A 6410 Chassis

Serial
Number
Status
---------- ----------------
SG9ZKM9999 Ready
SG9ZKM9999 Ready

Showing all fabrics on Aruba 6400 switches that have one fabric:

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

57

| switch# show | fabric |     |     |
| ------------ | ------ | --- | --- |
Fabric Modules
==============
| Product     |             | Serial |        |
| ----------- | ----------- | ------ | ------ |
| Name Number | Description | Number | Status |
---- ------- -------------------------------------- ---------- ----------------
| 1/1 R0X24A | 6405 Chassis | SG9ZKM9076 | Ready |
| ---------- | ------------ | ---------- | ----- |
ShowingasinglefabricmoduleonAruba6400switches:
switch#
show fabric 1/1
| Fabric module     | 1/1 is ready |     |     |
| ----------------- | ------------ | --- | --- |
| Admin state:      | Up           |     |     |
| Description:      | 6405 Chassis |     |     |
| Full Description: | 6405 Chassis |     |     |
| Serial number:    | SG00000000   |     |     |
| Product number:   | R0X24A       |     |     |
show hostname
Syntax
| show hostname | [vsx-peer] |     |     |
| ------------- | ---------- | --- | --- |
Description
Showsthecurrenthostname.
Commandcontext
Manager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Settingandshowingthehostname:
| switch# show | hostname |     |     |
| ------------ | -------- | --- | --- |
switch
switch#
config
| switch(config)#   | hostname myswitch |     |     |
| ----------------- | ----------------- | --- | --- |
| myswitch(config)# | show hostname     |     |     |
myswitch
Switchsystemandhardwarecommands|58

show images
Syntax
| show images | [vsx-peer] |     |
| ----------- | ---------- | --- |
Description
Showsinformationaboutthesoftwareintheprimaryandsecondaryimages.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Showingtheprimaryandsecondaryimagesona6300switch:
| switch(config)# | show | images |
| --------------- | ---- | ------ |
---------------------------------------------------------------------------
| ArubaOS-CX | Primary | Image |
| ---------- | ------- | ----- |
---------------------------------------------------------------------------
| Version | : FL.xx.xx.xxxx |              |
| ------- | --------------- | ------------ |
| Size    | : 722 MB        |              |
| Date    | : 2019-10-22    | 17:00:46 PDT |
SHA-256 : 4c84e49c0961fc56b5c7eab064750a333f1050212b7ce2fab587d13469d24cfa
---------------------------------------------------------------------------
| ArubaOS-CX | Secondary | Image |
| ---------- | --------- | ----- |
---------------------------------------------------------------------------
| Version | : FL.xx.xx.xxxx |              |
| ------- | --------------- | ------------ |
| Size    | : 722 MB        |              |
| Date    | : 2019-10-22    | 17:00:46 PDT |
SHA-256 : 4c84e49c0961fc56b5c7eab064750a333f1050212b7ce2fab587d13469d24cfa
| Default | Image : secondary |     |
| ------- | ----------------- | --- |
------------------------------------------------------
| Management | Module | 1/1 (Active) |
| ---------- | ------ | ------------ |
------------------------------------------------------
| Active       | Image      | : secondary              |
| ------------ | ---------- | ------------------------ |
| Service      | OS Version | : FL.01.05.0001-internal |
| BIOS Version |            | : FL.01.0001             |
Showingtheprimaryandsecondaryimagesona6400switch:
| switch(config)# | show | images |
| --------------- | ---- | ------ |
---------------------------------------------------------------------------
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 59

| ArubaOS-CX | Primary | Image |
| ---------- | ------- | ----- |
---------------------------------------------------------------------------
| Version | : FL.xx.xx.xxxxQ-2710-gd4ac39f30c9 |              |
| ------- | ---------------------------------- | ------------ |
| Size    | : 766 MB                           |              |
| Date    | : 2019-10-30                       | 17:22:01 PDT |
SHA-256 : e560ca9141f425d19024d122573c5ff730df2a9a726488212263b45ea00382cf
---------------------------------------------------------------------------
| ArubaOS-CX | Secondary | Image |
| ---------- | --------- | ----- |
---------------------------------------------------------------------------
| Version | : FL.xx.xx.xxxx |              |
| ------- | --------------- | ------------ |
| Size    | : 722 MB        |              |
| Date    | : 2019-10-21    | 19:36:26 PDT |
SHA-256 : 657e28adc1b512217ce780e3523c37c94db3d3420231deac1ab9aaa8324dc6b9
| Default | Image : secondary |     |
| ------- | ----------------- | --- |
------------------------------------------------------
| Management | Module | 1/1 (Active) |
| ---------- | ------ | ------------ |
------------------------------------------------------
| Active       | Image      | : secondary              |
| ------------ | ---------- | ------------------------ |
| Service      | OS Version | : FL.01.05.0001-internal |
| BIOS Version |            | : FL.01.0001             |
| show ip      | errors     |                          |
Syntax
| show ip errors | [vsx-peer] |     |
| -------------- | ---------- | --- |
Description
ShowsIPerrorstatisticsforpacketsreceivedbytheswitchsincetheswitchwaslastbooted.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
IPerrorinfoaboutreceivedpacketsiscollectedfromeachactivelinecardontheswitchandispreserved
duringfailoverevents.Errorcountsareclearedwhentheswitchisrebooted.
Dropreasonsarethefollowing:
Malformedpacket
ThepacketdoesnotconformtoTCP/IPprotocolstandardssuchaspacketlengthorinternetheader
length.
Switchsystemandhardwarecommands|60

A large number of malformed packets can indicate that there are hardware malfunctions such as loose
cables, network card malfunctions, or that a DOS (denial of service) attack is occurring.

IP address error

The packet has an error in the destination or source IP address. Examples of IP address errors include the
following:

n The source IP address and destination IP address are the same.

n There is no destination IP address.

n The source IP address is a multicast IP address.

n The forwarding header of an IPv6 address is empty.

n There is no source IP address for an IPv6 packet.

Invalid TTLs

The TTL (time to live) value of the packet reached zero. The packet was discarded because it traversed the
maximum number of hops permitted by the TTL value.

TTLs are used to prevent packets from being circulated on the network endlessly.

Example

Showing ip error statistics for packets received by the switch:

switch# show ip errors
----------------------------------
Drop reason
Packets
----------------------------------
1
Malformed packets
10
IP address errors
...

show module

Syntax

show module [<SLOT-ID>] [vsx-peer]

Description

Shows information about installed line modules and management modules.

Command context

Operator (>) or Manager (#)

Parameters

<SLOT-ID>

Specifies the member and slot numbers in format member/slot. For example, to show the module in
member 1, slot 3, enter 1/3.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

61

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

Identifies and shows status information about the line modules and management modules that are
installed in the switch.

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

The module is not installed in the chassis.

Failed

The module has experienced an error and failed.

Failover

This module is a fabric module or a line module, and it is in the process of connecting to the new active
management module during a management module failover event.

Initializing

The module is being initialized.

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

Product

Name Number Description
---- ------- -------------------------------------- ---------- ----------------
1/1 JL659A 6300M 48SR5 CL6 PoE 4SFP56 Swch

ID9ZKHN090 Active (local)

Status

Serial
Number

Switch system and hardware commands | 62

| Line Modules |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- |
============
| Product     |             |     |     |     | Serial |        |
| ----------- | ----------- | --- | --- | --- | ------ | ------ |
| Name Number | Description |     |     |     | Number | Status |
---- ------- -------------------------------------- ---------- ----------------
| 1/1 JL659A | 6300M | 48SR5 | CL6 PoE 4SFP56 | Swch | ID9ZKHN090 | Ready |
| ---------- | ----- | ----- | -------------- | ---- | ---------- | ----- |
Showingalinemodule(Aruba6400switch):
switch#
|                   | show module | 1/3          |            |            |              |     |
| ----------------- | ----------- | ------------ | ---------- | ---------- | ------------ | --- |
| Line module       | 1/3         | is ready     |            |            |              |     |
| Admin state:      | Up          |              |            |            |              |     |
| Description:      | 6400        | 24p 10GT     | 4SFP56 Mod |            |              |     |
| Full Description: |             | 6400 24-port | 10GBASE-T  | and 4-port | SFP56 Module |     |
| Serial            | number:     | SG9ZKMS045   |            |            |              |     |
| Product           | number:     | R0X42A       |            |            |              |     |
| Power priority:   |             | 128          |            |            |              |     |
Showingaslotthatdoesnotcontainalinemodule:
| switch(config)#     |        | show module | 1/3     |     |     |     |
| ------------------- | ------ | ----------- | ------- | --- | --- | --- |
| Module 1/3          | is not | physically  | present |     |     |     |
| show running-config |        |             |         |     |     |     |
Syntax
| show running-config |     | [<FEATURE>] | [all] [vsx-peer] |     |     |     |
| ------------------- | --- | ----------- | ---------------- | --- | --- | --- |
Description
Showsthecurrentnondefaultconfigurationrunningontheswitch.Nouserinformationisdisplayed.
Commandcontext
Manager(#)
Parameters
<FEATURE>
Specifiesthenameofafeature.Foralistoffeaturenames,entertheshow running-configcommand,
followedbyaspace,followedbyaquestionmark(?).Whenthejsonparameterisused,thevsx-peer
parameterisnotapplicable.
all
Showsalldefaultvaluesforthecurrentrunningconfiguration.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 63

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

Switch system and hardware commands | 64

| switch> show          | running-config | json  |
| --------------------- | -------------- | ----- |
| Running-configuration | in             | JSON: |
{
| "Monitoring_Policy_Script": |     | {   |
| --------------------------- | --- | --- |
"system_resource_monitor_mm1.1.0": {
"Monitoring_Policy_Instance": {
"system_resource_monitor_mm1.1.0/system_resource_monitor_
| mm1.1.0.default": | {         |                                            |
| ----------------- | --------- | ------------------------------------------ |
|                   | "name":   | "system_resource_monitor_mm1.1.0.default", |
|                   | "origin": | "system",                                  |
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
Showthecurrentrunningconfigurationwithoutdefaultvalues:
| switch(config)#        | show running-config |     |
| ---------------------- | ------------------- | --- |
| Current configuration: |                     |     |
!
| !Version ArubaOS-CX | Virtual.10.04.0000-6523-gbb15c03~dirty |     |
| ------------------- | -------------------------------------- | --- |
| led locator         | on                                     |     |
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
| switch(config)#        | show running-config | all |
| ---------------------- | ------------------- | --- |
| Current configuration: |                     |     |
!
| !Version ArubaOS-CX | Virtual.10.04.0000-6523-gbb15c03~dirty |     |
| ------------------- | -------------------------------------- | --- |
| led locator         | on                                     |     |
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
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 65

Showthecurrentrunningconfigurationwithdefaultvalues:
| switch(config)#        | snmp-server | vrf mgmt       |     |
| ---------------------- | ----------- | -------------- | --- |
| switch(config)#        | show        | running-config |     |
| Current configuration: |             |                |     |
!
| !Version    | ArubaOS-CX | Virtual.10.04.0000-6523-gbb15c03~dirty |     |
| ----------- | ---------- | -------------------------------------- | --- |
| led locator | on         |                                        |     |
!
!
!
!
| snmp-server | vrf mgmt |     |     |
| ----------- | -------- | --- | --- |
!
!
!
!
!
vlan 1
switch(config)#
switch(config)#
| switch(config)#        | show | running-config | all |
| ---------------------- | ---- | -------------- | --- |
| Current configuration: |      |                |     |
!
| !Version    | ArubaOS-CX | Virtual.10.04.0000-6523-gbb15c03~dirty |     |
| ----------- | ---------- | -------------------------------------- | --- |
| led locator | on         |                                        |     |
!
!
!
!
| snmp-server | vrf mgmt   |        |     |
| ----------- | ---------- | ------ | --- |
| snmp-server | agent-port | 161    |     |
| snmp-server | community  | public |     |
!
!
!
!
!
vlan 1
switch(config)#
| show running-config |     | current-context |     |
| ------------------- | --- | --------------- | --- |
Syntax
| show running-config | current-context |     |     |
| ------------------- | --------------- | --- | --- |
Description
Showsthecurrentnon-defaultconfigurationrunningontheswitchinthecurrentcommandcontext.
Commandcontext
configorachildofconfig.SeeUsage.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Youcanenterthiscommandfromthefollowingconfigurationcontexts:
Switchsystemandhardwarecommands|66

Anychildoftheglobalconfiguration(config)context.Ifthechildcontexthasinstances—suchas
n
interfaces—youcanenterthecommandinthecontextofaspecificinstance.
Supportforthiscommandisprovidedforonelevelbelowtheconfigcontext.Forexample,enteringthis
commandforachildofachildoftheconfigcontextnotsupported.
Ifyouenterthecommandonachildoftheconfigcontext,thecurrentconfigurationofthatcontextand
thechildrenofthatcontextaredisplayed.
n Theglobalconfiguration(config)context.
Ifyouenterthiscommandintheglobalconfiguration(config)context,itshowstherunning
configurationoftheentireswitch.Usetheshow running-configurationcommandinstead.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingtherunningconfigurationforthecurrentinterface:
| switch(config-if)# | show running-config | current-context |
| ------------------ | ------------------- | --------------- |
interface 1/1/1
| vsx-sync qos | vlans |     |
| ------------ | ----- | --- |
no shutdown
| description   | Example interface |     |
| ------------- | ----------------- | --- |
| vlan access 1 |                   |     |
exit
Showingthecurrentrunningconfigurationforthemanagementinterface:
| switch(config-if-mgmt)# | show running-config | current-context |
| ----------------------- | ------------------- | --------------- |
interface mgmt
no shutdown
| ip static 10.0.0.1/24 |          |     |
| --------------------- | -------- | --- |
| default-gateway       | 10.0.0.8 |     |
| nameserver 10.0.0.1   |          |     |
Showingtherunningconfigurationfortheexternalstoragesharenamednasfiles:
switch(config-external-storage-nasfiles)# show running-config current-context
| external-storage | nasfiles |     |
| ---------------- | -------- | --- |
address 192.168.0.1
vrf default
| username nasuser |     |     |
| ---------------- | --- | --- |
password ciphertext AQBapalKj+XMsZumHEwIc9OR6YcOw5Z6Bh9rV+9ZtKDKzvbaBAAAAB1CTrM=
type scp
| directory /home/nas |     |     |
| ------------------- | --- | --- |
enable
switch(config-external-storage-nasfiles)#
Showingtherunningconfigurationforacontextthatdoesnothaveinstances:
| switch(config-vsx)# | show run current-context |     |
| ------------------- | ------------------------ | --- |
vsx
| inter-switch-link | 1/1/1 |     |
| ----------------- | ----- | --- |
role secondary
| vsx-sync sflow | time |     |
| -------------- | ---- | --- |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 67

show startup-config
Syntax
| show startup-config | [json] |     |
| ------------------- | ------ | --- |
Description
Showsthecontentsofthestartupconfiguration.
Switchesinthefactory-defaultconfigurationdonothaveastartupconfigurationtodisplay.
Commandcontext
Manager(#)
Parameters
json
DisplayoutputinJSONformat.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Showingthestartup-configurationinnon-JSONformatfora6300switch:
| switch(config)# | show startup-config |     |
| --------------- | ------------------- | --- |
| Startup         | configuration:      |     |
!
| !Version          | ArubaOS-CX FL.xx.xx.xxxx |                     |
| ----------------- | ------------------------ | ------------------- |
| !export-password: | default                  |                     |
| hostname          | BLDG01-F1                |                     |
| user admin        | group administrators     | password ciphertext |
AQBapWl8I2ZunZ43NE/8KlbQ7zYC4gTT6uSFYi6n6wyY9PdBYgAAACONCR/3+AcNvzRBch0DoG7W9z84LpJA
+6C9SKfNwCqi5/
nUPk/ZOvN91/EQXvPNkHtBtQWyYZqfkebbEH78VWRHfWZjApv4II9qmQfxpA79wEvzshdzZmuAKrm
| user ateam | group administrators | password ciphertext |
| ---------- | -------------------- | ------------------- |
AQBapcPqMXoF+H10NKrqAedXLvlSRwf4wUEL22hXGD6ZBhicYgAAAGsbh70DKg1u+Ze1wxgmDXjkGO3bseYi
R3LKQg66vrfrqR/
M3oLlliPdZDnq9XMMvCL+7jBbYhYes8+uDxuSTh8kdkd/qj3lo5FUuC5fENgCjU0YI1l7qtU+YEnsj
!
!
!
!
| radius-server | host 10.10.10.15 |     |
| ------------- | ---------------- | --- |
!
| radius dyn-authorization | enable      |     |
| ------------------------ | ----------- | --- |
| ssh server               | vrf default |     |
| ssh server               | vrf mgmt    |     |
!
!
!
!
!
| router ospf | 1   |     |
| ----------- | --- | --- |
Switchsystemandhardwarecommands|68

| router-id    | 1.63.63.1 |     |
| ------------ | --------- | --- |
| area 0.0.0.0 |           |     |
vlan 1
vlan 66
| name vlan66 |     |     |
| ----------- | --- | --- |
vlan 67
| name vlan67 |     |     |
| ----------- | --- | --- |
vlan 999
| name vlan999 |     |     |
| ------------ | --- | --- |
vlan 4000
spanning-tree
| interface | mgmt |     |
| --------- | ---- | --- |
no shutdown
| ip static       | 10.6.9.15/24 |     |
| --------------- | ------------ | --- |
| default-gateway | 10.6.9.1     |     |
Showingthestartup-configurationinJSONformat:
| switch# show           | startup-config | json |
| ---------------------- | -------------- | ---- |
| Startup configuration: |                |      |
{
| "AAA_Server_Group": | {   |     |
| ------------------- | --- | --- |
"local": {
|     | "group_name": | "local" |
| --- | ------------- | ------- |
},
"none": {
|     | "group_name": | "none" |
| --- | ------------- | ------ |
}
},
...
show system
Syntax
| show system [vsx-peer] |     |     |
| ---------------------- | --- | --- |
Description
Showsgeneralstatusinformationaboutthesystem.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 69

CPUutilizationrepresentstheaverageutilizationacrossalltheCPUcores.
SystemContact,SystemLocation,andSystemDescriptioncanbesetwiththesnmp-servercommand.
Examples
Showingsysteminformationona6300switch:
| switch(config)#    | show       | system           |           |            |      |
| ------------------ | ---------- | ---------------- | --------- | ---------- | ---- |
| Hostname           |            | : switch         |           |            |      |
| System Description |            | : FL.10.xx.xxxxx |           |            |      |
| System Contact     |            | :                |           |            |      |
| System Location    |            | :                |           |            |      |
| Vendor             |            | : Aruba          |           |            |      |
| Product            | Name       | : JL659A 6300M   | 48SR5 CL6 | PoE 4SFP56 | Swch |
| Chassis            | Serial Nbr | : ID9ZKHN090     |           |            |      |
| Base MAC           | Address    | : 9020c2-245080  |           |            |      |
| ArubaOS-CX         | Version    | : FL.10.xx.xxxx  |           |            |      |
| Time Zone          |            | : UTC            |           |            |      |
| Up Time            |            | : 5 days, 15     | hours, 33 | minutes    |      |
| CPU Util           | (%)        | : 21             |           |            |      |
| Memory Usage       | (%)        | : 19             |           |            |      |
Showingsysteminformationoma6400switch:
| switch(config)#    | show       | system           |         |     |     |
| ------------------ | ---------- | ---------------- | ------- | --- | --- |
| Hostname           |            | : switch         |         |     |     |
| System Description |            | : FL.10.xx.xxxxx |         |     |     |
| System Contact     |            | :                |         |     |     |
| System Location    |            | :                |         |     |     |
| Vendor             |            | : Aruba          |         |     |     |
| Product            | Name       | : R0X24A 6405    | Chassis |     |     |
| Chassis            | Serial Nbr | : SG9ZKM7206     |         |     |     |
| Base MAC           | Address    | : 9020c2-dc4700  |         |     |     |
| ArubaOS-CX         | Version    | : FL.10.xx.xxxxx |         |     |     |
| Time Zone          |            | : UTC            |         |     |     |
| Up Time            |            | : 32 minutes     |         |     |     |
| CPU Util           | (%)        | : 3              |         |     |     |
| Memory Usage       | (%)        | : 10             |         |     |     |
BLDG02-F3(config)#
| show system |     | error-counter-monitor |     |     |     |
| ----------- | --- | --------------------- | --- | --- | --- |
Syntax
show system error-counter-monitor {basic <PORT-NUM> | extended} [vsx-peer]
Description
Showserrorcounterstatistics.
Commandcontext
Manager(#)
Switchsystemandhardwarecommands|70

Parameters
basic <PORT-NUM>
Specifiesaphysicalportontheswitch.Usetheformatmember/slot/port(forexample,1/3/1).
extended
Showsstatisticsforallinterfaces.
Commandcontext
Manager(#)
Examples
Showingerrorcounterstatisticsforinterface1/1/1:
| switch#       | show system error-counter-monitor |            | basic 1/1/1 |
| ------------- | --------------------------------- | ---------- | ----------- |
| Interface     | error counter                     | statistics | for 1/1/1   |
| Error Counter |                                   |            | Value       |
-----------------------------------------
| EtherStatsOversizePkts       |     |     | 983  |
| ---------------------------- | --- | --- | ---- |
| EtherStatsUndersizePkts      |     |     | 1024 |
| EtherStatsJabbers            |     |     | 10   |
| Dot3StatsAlignmentErrors     |     |     | 462  |
| Dot3StatsFCSErrors           |     |     | 321  |
| Dot3StatsLateCollisions      |     |     | 2024 |
| EtherStatsFragments          |     |     | 121  |
| Dot3StatsExcessiveCollisions |     |     | 1025 |
| IfInBroadcastPkts            |     |     | 2001 |
Showingerrorcounterstatisticsforallinterfaces:
| switch#       | show system error-counter-monitor |            | extended  |
| ------------- | --------------------------------- | ---------- | --------- |
| Interface     | error counter                     | statistics | for 1/1/1 |
| Error Counter |                                   |            | Value     |
-----------------------------------------
| EtherStatsOversizePkts       |     |     | 983  |
| ---------------------------- | --- | --- | ---- |
| EtherStatsUndersizePkts      |     |     | 1024 |
| EtherStatsJabbers            |     |     | 10   |
| Dot3StatsAlignmentErrors     |     |     | 462  |
| Dot3StatsFCSErrors           |     |     | 321  |
| Dot3StatsLateCollisions      |     |     | 2024 |
| EtherStatsFragments          |     |     | 121  |
| Dot3StatsExcessiveCollisions |     |     | 1025 |
| IfInBroadcastPkts            |     |     | 2001 |
...
...
| Interface     | error counter | statistics | for 1/8/32 |
| ------------- | ------------- | ---------- | ---------- |
| Error Counter |               |            | Value      |
-----------------------------------------
| EtherStatsOversizePkts |     |     | 0   |
| ---------------------- | --- | --- | --- |
...
| show system | resource-utilization |     |     |
| ----------- | -------------------- | --- | --- |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 71

Syntax
show system resource-utilization [daemon <DAEMON-NAME> | module <SLOT-ID>] [vsx-peer]
Description
ShowsinformationabouttheusageofsystemresourcessuchasCPU,memory,andopenfiledescriptors.
Commandcontext
Manager(#)
Parameters
daemon <DAEMON-NAME>
Showsthefilteredresourceutilizationdatafortheprocessspecifiedby<DAEMON-NAME>only.
Foralistofdaemonsthatlogevents,entershow events -d ?fromaswitchpromptinthemanager(#)context.
module <SLOT-ID>
Showsthefilteredresourceutilizationdataforthelinemodulespecifiedby<SLOT-ID>only.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Showingallsystemresourceutilizationdata:
| switch# show | system | resource-utilization |     |     |     |     |
| ------------ | ------ | -------------------- | --- | --- | --- | --- |
System Resources:
| Processes:       | 70   |              |        |          |     |           |
| ---------------- | ---- | ------------ | ------ | -------- | --- | --------- |
| CPU usage(%):    | 20   |              |        |          |     |           |
| Memory usage(%): | 25   |              |        |          |     |           |
| Open FD's:       | 1024 |              |        |          |     |           |
| Process          |      | CPU Usage(%) | Memory | Usage(%) |     | Open FD's |
-----------------------------------------------------------------------
| pmd         |     | 2   |     | 1   |     | 14  |
| ----------- | --- | --- | --- | --- | --- | --- |
| hpe-sysmond |     | 1   |     | 2   |     | 11  |
| hpe-mgmdd   |     | 0   |     | 1   |     | 5   |
...
Showingtheresourceutilizationdataforthepmdprocess:
| switch# show | system | resource-utilization | daemon | pmd   |           |     |
| ------------ | ------ | -------------------- | ------ | ----- | --------- | --- |
| Process      |        | CPU Usage            | Memory | Usage | Open FD's |     |
-----------------------------------------------------------------------
| pmd |     | 2   | 1   |     | 14  |     |
| --- | --- | --- | --- | --- | --- | --- |
Showingresourceutilizationdatawhensystemresourceutilizationpollingisdisabled:
Switchsystemandhardwarecommands|72

| switch# | show     | system      | resource-utilization |           |              |          |
| ------- | -------- | ----------- | -------------------- | --------- | ------------ | -------- |
| System  | resource | utilization |                      | data poll | is currently | disabled |
Showingresourceutilizationdataforalinemodule:
| switch# | show      | system      | resource-utilization |          | module       | 1/1 |
| ------- | --------- | ----------- | -------------------- | -------- | ------------ | --- |
| System  | Resource  | utilization |                      | for line | card module: | 1/1 |
| CPU     | usage(%): | 0           |                      |          |              |     |
| Memory  | usage(%): | 35          |                      |          |              |     |
| Open    | FD's:     | 512         |                      |          |              |     |
| show    | tech      |             |                      |          |              |     |
Syntax
| show tech | [basic | | <FEATURE>] |     | [local-file] |     |     |
| --------- | ------ | ------------ | --- | ------------ | --- | --- |
Description
Showsdetailedinformationaboutswitchfeaturesbyautomaticallyrunningtheshowcommandsassociated
withthefeature.Ifnoparametersarespecified,theshow techcommandshowsinformationaboutall
switchfeatures.Technicalsupportpersonnelusetheoutputfromthiscommandfortroubleshooting.
Commandcontext
Manager(#)
Parameters
basic
Specifiesshowingabasicsetofinformation.
<FEATURE>
Specifiesthenameofafeature.Foralistoffeaturenames,entertheshow techcommand,followedbya
space,followedbyaquestionmark(?).
local-file
| Showstheoutputoftheshow |     |     |     | techcommandtoalocaltextfile. |     |     |
| ----------------------- | --- | --- | --- | ---------------------------- | --- | --- |
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
| Toterminatetheoutputoftheshow |     |     |     | techcommand,enterCtrl+C. |     |     |
| ----------------------------- | --- | --- | --- | ------------------------ | --- | --- |
IfthecommandwasnotterminatedwithCtrl+C,attheendoftheoutput,theshow techcommandshows
thefollowing:
Thetimeconsumedtoexecutethecommand.
n
n Thelistoffailedshowcommands,ifany.
Togetacopyofthelocaltextfilecontentcreatedwiththeshowtechcommandthatisusedwiththelocal-
| fileparameter,usethecopy |     |     | show-tech | local-filecommand. |     |     |
| ------------------------ | --- | --- | --------- | ------------------ | --- | --- |
Example
Showingthebasicsetofsysteminformation:
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 73

| switch# | show tech basic |     |     |
| ------- | --------------- | --- | --- |
=============================================================
| Show Tech | executed | on Wed Sep | 6 16:50:37 2017 |
| --------- | -------- | ---------- | --------------- |
=============================================================
=============================================================
| [Begin] | Feature basic |     |     |
| ------- | ------------- | --- | --- |
=============================================================
*******************************
| Command | : show core-dump | all |     |
| ------- | ---------------- | --- | --- |
*******************************
| no core | dumps are present |     |     |
| ------- | ----------------- | --- | --- |
...
=============================================================
| [End] Feature | basic |     |     |
| ------------- | ----- | --- | --- |
=============================================================
=============================================================
| 1 show | tech command | failed |     |
| ------ | ------------ | ------ | --- |
=============================================================
Failed command:
| 1. show | boot-history |     |     |
| ------- | ------------ | --- | --- |
=============================================================
| Show tech | took 3.000000 | seconds | for execution |
| --------- | ------------- | ------- | ------------- |
Directingtheoutputoftheshowtech basiccommandtothelocaltextfile:
| switch# | show tech basic | local-file |     |
| ------- | --------------- | ---------- | --- |
Show Tech output stored in local-file. Please use 'copy show-tech local-file'
| to copy-out | this file. |     |     |
| ----------- | ---------- | --- | --- |
show usb
Syntax
show usb [vsx-peer]
Description
ShowstheUSBportconfigurationandmountsettings.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Switchsystemandhardwarecommands|74

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

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

75

| switch# | show usb file-system |     |     |
| ------- | -------------------- | --- | --- |
/mnt/usb:
| 'System           | Volume Information' | dir1'          |     |
| ----------------- | ------------------- | -------------- | --- |
| /mnt/usb/System   | Volume              | Information':  |     |
| IndexerVolumeGuid |                     | WPSettings.dat |     |
/mnt/usb/dir1:
dir2 test1
/mnt/usb/dir1/dir2:
test2
Showingavailablepathoptionsfromthetoplevel:
| switch# | show usb file-system | /   |     |
| ------- | -------------------- | --- | --- |
total 64
| drwxrwxrwx | 2 32768 | Jan 22 16:27 'System | Volume Information' |
| ---------- | ------- | -------------------- | ------------------- |
| drwxrwxrwx | 3 32768 | Mar 5 15:26 dir1     |                     |
Showingthecontentsofaspecificfolder:
| switch# | show usb file-system | /dir1 |     |
| ------- | -------------------- | ----- | --- |
total 32
| drwxrwxrwx | 2 32768              | Mar 5 15:26 dir2  |     |
| ---------- | -------------------- | ----------------- | --- |
| -rwxrwxrwx | 1 0                  | Feb 5 18:08 test1 |     |
| switch#    | show usb file-system | dir1/dir2         |     |
total 0
| -rwxrwxrwx | 1 0 Feb | 6 05:35 test2 |     |
| ---------- | ------- | ------------- | --- |
Attemptingtoenteraninvalidcharacterinthepath:
| switch# | show usb file-system | dir1/../.. |     |
| ------- | -------------------- | ---------- | --- |
| Invalid | path argument        |            |     |
show version
Syntax
| show version | [vsx-peer] |     |     |
| ------------ | ---------- | --- | --- |
Description
Showsversioninformationaboutthenetworkoperatingsystemsoftware,serviceoperatingsystem
software,andBIOS.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
Switchsystemandhardwarecommands|76

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Showingversioninformationfora6300switch:
| switch(config)# |     | show | version |     |     |     |
| --------------- | --- | ---- | ------- | --- | --- | --- |
-----------------------------------------------------------------------------
ArubaOS-CX
(c) Copyright 2017-2020 Hewlett Packard Enterprise Development LP
-----------------------------------------------------------------------------
| Version |      | : FL.xx.xx.xxxx |          |     |     |     |
| ------- | ---- | --------------- | -------- | --- | --- | --- |
| Build   | Date | : 2020-10-22    | 17:00:46 | PDT |     |     |
Build ID : ArubaOS-CX:FL.xx.xx.xxxx:85c3c2f3d59e:201910222335
| Build   | SHA                  | : 85c3c2f3d59ec8318ba97178fad387aecb671b33 |                        |               |     |     |
| ------- | -------------------- | ------------------------------------------ | ---------------------- | ------------- | --- | --- |
| Active  | Image                | : secondary                                |                        |               |     |     |
| Service | OS Version           | :                                          | FL.01.05.0001-internal |               |     |     |
| BIOS    | Version              | :                                          | FL.01.0001             |               |     |     |
| system  | resource-utilization |                                            |                        | poll-interval |     |     |
Syntax
| system resource-utilization |     |     | poll-interval | <SECONDS> |     |     |
| --------------------------- | --- | --- | ------------- | --------- | --- | --- |
Description
ConfiguresthepollingintervalforsystemresourceinformationcollectionandrecordingsuchasCPUand
memoryusage.
Commandcontext
config
Parameters
<SECONDS>
Specifiesthepollintervalinseconds.Range:10-3600.Default:10.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Configuringthesystemresourceutilizationpollinterval:
| switch(config)# |     | system | resource-utilization |     | poll-interval | 20  |
| --------------- | --- | ------ | -------------------- | --- | ------------- | --- |
top cpu
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 77

Syntax

top cpu

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
Tasks: 76 total, 2 running, 74 sleeping, 0 stopped, 0 zombie
%Cpu(s): 31.4 us, 32.7 sy, 0.5 ni, 34.4 id, 04. wa, 0.0 hi, 0.6 si, 0.0 st
KiB Mem : 4046496 total, 2487508 free, 897040 used,
KiB Swap:

0 used, 2859196 avail Mem

661948 buff/cache

0 total,

0 free,

PID USER

PRI NI

VIRT

RES

SHR S %CPU %MEM

TIME+ COMMAND

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
Tasks: 76 total, 2 running, 74 sleeping, 0 stopped, 0 zombie
%Cpu(s): 31.4 us, 32.7 sy, 0.5 ni, 34.4 id, 04. wa, 0.0 hi, 0.6 si, 0.0 st
KiB Mem : 4046496 total, 2487508 free, 897040 used,

661948 buff/cache

Switch system and hardware commands | 78

KiB Swap:

0 total,

0 free,

0 used, 2859196 avail Mem

PID USER

PRI NI

VIRT

RES

SHR S %CPU %MEM

TIME+ COMMAND

...

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

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

79

Disables the inserted USB drive in preparation for removal.

Authority

Administrators or local user group members with execution rights for this command.

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

Switch system and hardware commands | 80

Chapter 6

External storage

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

<HOSTNAME>

Specifies the hostname of the NAS server. String.

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

81

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreatingthelogfilesstoragevolumewithIPaddress10.1.1.1:
| switch(config)#                           | external-storage | logfiles |          |
| ----------------------------------------- | ---------------- | -------- | -------- |
| switch(config-external-storage-logfiles)# |                  | address  | 10.1.1.1 |
Deletinganexternalstoragevolumenamedlogfiles:
| switch(config)#                           | external-storage | logfiles   |          |
| ----------------------------------------- | ---------------- | ---------- | -------- |
| switch(config-external-storage-logfiles)# |                  | no address | 10.1.1.1 |
directory
Syntax
directory <DIRECTORY-NAME>
| no directory <DIRECTORY-NAME> |     |     |     |
| ----------------------------- | --- | --- | --- |
Description
Selectsanexistingdirectoryontheexternalstoragevolume.
Thenoformofthiscommandclearsadirectoryofanexternalstoragevolume.
Commandcontext
config-external-storage-<VOLUME-NAME>
Parameters
<DIRECTORY-NAME>
Specifiestheexternalstoragedirectoryformappingthevolume.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Creatingavolumenamedlogfilesthatismappedunder/homeontheserver:
| switch(config)# | external-storage | logfiles |     |
| --------------- | ---------------- | -------- | --- |
switch(config-external-storage-logfiles)#
directory /home
Clearingthedirectory/home:
| switch(config)#                           | external-storage | logfiles     |       |
| ----------------------------------------- | ---------------- | ------------ | ----- |
| switch(config-external-storage-logfiles)# |                  | no directory | /home |
disable
Externalstorage|82

Syntax

disable
no disable

Description

Disables the external storage volume.

The no form of this command enables the external storage volume. This is identical to the enable command.

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

Disables the external storage volume:

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

83

| switch(config)# | external-storage | logfiles |
| --------------- | ---------------- | -------- |
switch(config-external-storage-logfiles)#
disable
external-storage
Syntax
| external-storage    | <VOLUME-NAME> |     |
| ------------------- | ------------- | --- |
| no external-storage | <VOLUME-NAME> |     |
Description
Createsorupdatesanexternalstoragevolume.
Thenoformofthiscommanddeletesanexternalstoragevolume.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Creatingthelogfilesstoragevolume:
| switch(config)# | external-storage | logfiles |
| --------------- | ---------------- | -------- |
switch(config-external-storage-logfiles)#
Deletingthelogfilesstoragevolume:
| switch(config)# | no external-storage | logfiles |
| --------------- | ------------------- | -------- |
password
Syntax
| password [{plaintext | | ciphertext} | <PASSWORD>] |
| -------------------- | ------------- | ----------- |
no password
Description
Setsthepasswordforloggingintoanetworkattachedstorageserver.
Thenoformofthiscommandclearsthepasswordforloggingintoanetworkattachedstorageserver.
Commandcontext
config-external-storage-<VOLUME-NAME>
Parameters
| {ciphertext | plaintext} |     |     |
| ------------------------ | --- | --- |
Selectsthepasswordformat.
<PASSWORD>
Specifiesthepassword.
Externalstorage|84

Whenthepasswordisnotprovidedonthecommandline,plaintextpasswordpromptingoccursuponpressing
Enter.Theenteredpasswordcharactersaremaskedwithasterisks.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreatingavolumenamedlogfileswithpasswordXj#9:
| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)# password plaintext Xj#9
Creatingavolumenamedbak1withapromptedplaintextpassword:
| switch(config)#                           | external-storage |           | bak1 |          |
| ----------------------------------------- | ---------------- | --------- | ---- | -------- |
| switch(config-external-storage-logfiles)# |                  |           |      | password |
| Enter the                                 | NAS server       | password: |      |          |
**********
| Re-Enter | Enter the | NAS server | password: | ********** |
| -------- | --------- | ---------- | --------- | ---------- |
Clearingthepasswordforvolumelogfiles:
| switch(config)#                           | external-storage |     | logfiles |             |
| ----------------------------------------- | ---------------- | --- | -------- | ----------- |
| switch(config-external-storage-logfiles)# |                  |     |          | no password |
show external-storage
Syntax
| show external-storage |     | [<VOLUME-NAME>] |     |     |
| --------------------- | --- | --------------- | --- | --- |
Description
Showsexternalstorageconfigurationandstateforallvolumesorforaspecifiedvolume.
Commandcontext
Operator(>)orManager(#)
Parameters
<VOLUME-NAME>
Specifiestheexternalstoragevolumenamethattheshowcommandwilluse.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| switch# | show external-storage |     |     |     |
| ------- | --------------------- | --- | --- | --- |
------------------------------------------------------------------------------------
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 85

|     |     | Address |     |     | VRF Username | Type | Directory | State |
| --- | --- | ------- | --- | --- | ------------ | ---- | --------- | ----- |
------------------------------------------------------------------------------------
| nfsvol   |                | 10.1.1.1  |     |     | nas ---          | NFSv3 | /home    | operational  |
| -------- | -------------- | --------- | --- | --- | ---------------- | ----- | -------- | ------------ |
| nfsfiles |                | 20.1.1.1  |     |     | nas netstorage   | NFSv4 | /netstor | disabled     |
| scpdev   |                | nasserver |     |     | nas scpstor      | SCP   | /scp     | unaccessible |
| show     | running-config |           |     |     | external-storage |       |          |              |
Syntax
| show running-config |     |     | external-storage |     |     |     |     |     |
| ------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
Description
Showstherunningconfigurationoftheexternalstorage.
Commandcontext
Operator(>)orManager(#)
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| switch#          |           | show | running-config |     | external-storage |     |     |     |
| ---------------- | --------- | ---- | -------------- | --- | ---------------- | --- | --- | --- |
| external-storage |           |      | nfsvol         |     |                  |     |     |     |
|                  | address   |      | 10.1.1.1       |     |                  |     |     |     |
|                  | vrf       |      | nas            |     |                  |     |     |     |
|                  | type      |      | nfsv4          |     |                  |     |     |     |
|                  | directoty |      | /home          |     |                  |     |     |     |
enable
| external-storage |           |     | scpdev     |     |     |     |     |     |
| ---------------- | --------- | --- | ---------- | --- | --- | --- | --- | --- |
|                  | address   |     | 30.1.1.1   |     |     |     |     |     |
|                  | vrf       |     | nas        |     |     |     |     |     |
|                  | username  |     | switchuser |     |     |     |     |     |
|                  | password  |     | ciphertext |     | xxx |     |     |     |
|                  | type      |     | scp        |     |     |     |     |     |
|                  | directoty |     | /home      |     |     |     |     |     |
enable
type
Syntax
| type {nfsv3 |        | | nfsv4 | |     | scp}   |     |     |     |     |
| ----------- | ------ | ------- | ----- | ------ | --- | --- | --- | --- |
| no type     | {nfsv3 | |       | nfsv4 | | scp} |     |     |     |     |
Description
Setsthenetworkattachedstorageaccesstypeforreachingtheexternalstoragevolume.
Thenoformofthiscommanddeletesanexternalstoragevolume.
Commandcontext
config-external-storage-<VOLUME-NAME>
Parameters
Externalstorage|86

nfsv3

Specifies the NFSv3 network access protocol.

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

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

87

switch(config)# external-storage logfiles
switch(config-external-storage-logfiles)# no username nasuser

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

External storage | 88

Chapter 7

IP-SLA

IP-SLA

The IP Service Level Agreement (IP-SLA) is a feature that enables the measuring of network performance
between two nodes in a network for different service level agreement parameters such as round-trip time
(RTT), one-way delay, jitter, reachability, packet loss, and voice quality scores. These two nodes can span
across area in access, distribution or core inside a LAN as well as across WAN between core to core or core to
Data Centre switches. This feature helps you measure the SLA for different protocols or applications such as
UDP echo, UDP jitter (for voice and video), TCP connect, HTTP, and ICMP echo. This guide provides details
for managing and monitoring different types of IP-SLAs.

IP-SLA guidelines

n ArubaOS-CX supports only SLA configuration through CLI and thresholds can be configured using NAE

agents using WebUI/REST.

n ArubaOS-CX supports only forever tests. On-demand tests are not supported.

n Maximum sessions: IP-SLA source 500, IP-SLA responder 100.

n NAE can effectively monitor a maximum of 300 parameters, reducing the maximum supported session

by 300.

n NAE supports only syslog.

n NAE agents must be triggered for each IP-SLA test on every switch.

n If multiple IP addresses are received for a DNS query, DNS works with the first resolved IP.

n When the DNS server IP is not configured, the first DNS server in resolve.conf is used.

n The source interface/IP option is not applicable for SLAs configured on 'mgmt' VRF, as it has only one

interface.

n A system time change because of NTP or a manual change causes an incorrect calculation.

n There is no interoperability of UDP echo SLA between ArubaOS-CX and FlexFabric switches.

n Source IP and source port combination must be unique across SLA sessions in a same switch.

n Do not use the same source port across the source and responder sessions in a switch.

n NTP synchronization is a must for SLA types involving one-way delay such as UDP jitter VoIP.

n It is mandatory to set default CoPP to the max value when UDP jitter SLA is enabled otherwise 100%

packet loss can be seen and UDP-Jitter sla probe will result in failure as seen in the following example.

copp-policy default

class hypertext priority 6 rate 50000 burst 64
default-class priority 6 rate 99999 burst 9999

n Deviations with respect to PVOS results: The packet losses due to internal switch-related issues like

interface shutdown or interface flaps will not be considered as 'Probes Timed-out error', as the IP-SLA
solution is to measure network performance and anomalies. Rather, this kind of packet loss will be
counted in internal counters like 'Destination address unreachable'.

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

89

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

n SLAs exceeding 480 will continue to remain in the 'waiting for VoIP slot' until any slot is freed by stopping

the running SLA.

n To avoid high RTT, a single switch with more than 20 SLAs should not have single responder SLA.

n When IP is received dynamically (e.g. using DHCP) for interfaces other than management interface, IPSLA

source or responder has to be configured only using interface name.

IP-SLA commands

http

Syntax

http {get | raw} URL [source {<SOURCE-IPV4-ADDR> | <IFNAME>} source-port <PORT-NUM>]

[proxy proxy-url] [cache disable] [name-server <IPV4-ADDR-DNS-SERVER>]
[probe-interval <30-604800>] [version<VERSION-NUMBER>] [http-raw-request <RAW-PAYLOAD>]

Description

Configures HTTP as the IP-SLA test mechanism. Requires destination URL and type of HTTP request
(raw/get).

Command context

config-ip-sla-<IP-SLA-NAME>

Parameters

{get | raw}

Selects HTTP request type as GET or RAW where the system will generate or provide HTTP payload.

URL

Specifies HTTP URL address of syntax. http://<HOST NAME/IP-ADDRESS>:<PORT>/<PATH>.

source {<SOURCE-IPV4-ADDR> | <IFNAME>}

Selects the source IPv4 address for SLA probes or the source interface to use for sending IP-SLA probes.

source-port <PORT-NUM>

Specifies the value of the source port for the IP-SLA probes.

cache disable

Selects cache option for the HTTP server. By default the option is enabled.

name-server <IPV4-ADDR-DNS-SERVER>

Specifies the IPv4 address of DNS server.

IP-SLA | 90

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
switch(config-ipsla-1)# http http://device.arubanetworks.com source 2.2.2.1
switch(config-ipsla-1)# http http://device.arubanetworks.com/root/home.html

source-interface 1/1/1

switch(config-ipsla-1)# http http://device.arubanetworks.com name-server

10.10.10.2

switch(config-ipsla-1)# http raw raw-request "GET /en/US/hmpgs/index.html

HTTP/1.0\r\n\r\n"

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

name-server <IPV4-ADDR-DNS-SERVER>

Specifies the DNS server for destination hostname resolution.

payload-size <PAYLOAD-SIZE>

Specifies the payload size of an SLA probe. Range: 0 to 1440.

tos <TYPE-OF-SERVICE>

Specifies the type of serve to be used in the probe packets. Range: 0 to 255.

probe-interval <PROBE-INTERVAL>

Specifies the probe interval in seconds. Range: 5 to 604800.

Authority

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

91

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| switch(config)# |                             | ip-sla | test |           |                |         |
| --------------- | --------------------------- | ------ | ---- | --------- | -------------- | ------- |
|                 | switch(config-ip-sla-test)# |        |      | icmp-echo | 2.2.2.2        |         |
|                 | switch(config-ip-sla-test)# |        |      | icmp-echo | 2.2.2.2 source | 3.3.3.3 |
switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
| name-server |     | 4.4.4.4 |     |     |     |     |
| ----------- | --- | ------- | --- | --- | --- | --- |
switch(config-ip-sla-test)# icmp-echo 2.2.2.2 source 3.3.3.3 payload-size 400
| name-server |     | 4.4.4.4 probe-interval |     | 80  |     |     |
| ----------- | --- | ---------------------- | --- | --- | --- | --- |
ip-sla
Syntax
ip-sla <IP-SLA-NAME>
| no ip-sla | <IP-SLA-NAME> |     |     |     |     |     |
| --------- | ------------- | --- | --- | --- | --- | --- |
Description
CreatesanIPServiceLevelAgreement(SLA)profileandswitchestotheconfig-ip-slacontext.
ThenoformofthiscommanddeletesanIP-SLAprofile.Bydefault,allprofileusethedefaultVRF(default).
Commandcontext
config
Parameters
<IP-SLA-NAME>
SpecifiesanIP-SLAprofilename.Length:1to63characters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreatinganIP-SLA:
| switch(config)# |     | ip-sla | 1   |     |     |     |
| --------------- | --- | ------ | --- | --- | --- | --- |
switch(config-ip-sla-1)#
DeletinganIP-SLA:
| switch(config)# |     | no ip-sla | 1   |     |     |     |
| --------------- | --- | --------- | --- | --- | --- | --- |
switch(config)#
| ip-sla | responder |     |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- |
Syntax
ip-sla responder <SLA-NAME> {udp-echo | tcp-connect | udp-jitter-voip} <PORT-NUM>
|           | [source   | {<SOURCE-IPV4-ADDR> |     | | <IFNAME>}][vrf | <VRF-NAME>] |     |
| --------- | --------- | ------------------- | --- | ---------------- | ----------- | --- |
| no ip-sla | responder | <SLA-NAME>          |     |                  |             |     |
IP-SLA|92

Description

Selects the IP-SLA responder. The responder can be configured for udp-echo, tcp-connect, udp-jitter-voip
type. It requires the SLA name, SLA type, and port number as arguments. Source IP/interface ID is a must
for type udp-jitter-voip and optional for other types.

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

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

93

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| switch(config)# |           | show      | ip-sla     | responder | SLA3 |
| --------------- | --------- | --------- | ---------- | --------- | ---- |
|                 | SLA Name  |           | : SLA3     |           |      |
|                 | IP-SLA    | Type      | : Udp-echo |           |      |
|                 | VRF       |           | : Default  |           |      |
|                 | Responder | Port      | : 8000     |           |      |
|                 | Responder | IP        | : 2.2.2.3  |           |      |
|                 | Responder | Interface | : 1/1/1    |           |      |
|                 | Responder | Status    | : Running  |           |      |
| show            | ip-sla    | responder | results    |           |      |
Syntax
show ip-sla responder <SLA-NAME> <SOURCE-IPV4-ADDR> <PORT-NUM> results
Description
Showsthegivenip-slaresponderstatisticsforagivensourceIPandport.Thiscommandisonlyapplicable
forthesourceswheresourceIPandportareconfigured.
Commandcontext
config
Parameters
<SLA-NAME>
SpecifiestheSLAname.
<SOURCE-IPV4-ADDR>
SpecifiesthesourceIPV4address.
<PORT-NUM>
Specifiestheportnumber.Range:1to65535.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| switch# | show      | ip-sla    | responder  | SLA1 | 2.2.2.1 8000 results |
| ------- | --------- | --------- | ---------- | ---- | -------------------- |
|         | IP-SLA    | Type      | : Udp-echo |      |                      |
|         | VRF Name  |           | : Default  |      |                      |
|         | Source    | IP        | : 2.2.2.1  |      |                      |
|         | Source    | Port      | : 8000     |      |                      |
|         | Responder | Port      | : 8888     |      |                      |
|         | Responder | IP        | : 2.2.2.3  |      |                      |
|         | Responder | Interface | :          |      |                      |
|         | Responder | Status    | : Running  |      |                      |
|         | Packets   | Received  | : 2        |      |                      |
|         | Packets   | Sent      | : 2        |      |                      |
IP-SLA|94

| show | ip-sla | <SLA-NAME> |     |     |     |     |     |
| ---- | ------ | ---------- | --- | --- | --- | --- | --- |
Syntax
| show | ip-sla <SLA-NAME> |     | results |     |     |     |     |
| ---- | ----------------- | --- | ------- | --- | --- | --- | --- |
Description
ShowsthegivenIP-SLAsourceconfigurationandstatus.
Commandcontext
Operator(>)orManager(#)
Parameters
<SLA-NAME>
SpecifiestheSLAname.
results
ShowsthestatisticscalculatedforanSLAtype.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| switch#         | show         | ip-sla     | xyz            | results  |             |               |             |
| --------------- | ------------ | ---------- | -------------- | -------- | ----------- | ------------- | ----------- |
|                 | IP-SLA       | session    | status         |          |             |               |             |
|                 | IP-SLA       | Name       |                |          |             | : xyz         |             |
|                 | IP-SLA       | Type       |                |          |             | : tcp-connect |             |
|                 | Destination  |            | Host           | Name/IP  | Address:    | 2.2.2.1       |             |
|                 | Destination  |            | Port           |          |             | : 8888        |             |
|                 | Source       | IP         | Address/IFName |          |             | : 2.2.2.2     |             |
|                 | Source       | Port       |                |          |             | : 5555        |             |
|                 | Status       |            |                |          |             | : Running     |             |
|                 | IP-SLA       | session    | cumulative     |          | counters    |               |             |
|                 | Total        | Probes     | Transmitted    |          |             | : 1           |             |
|                 | Probes       | Timed-out  |                |          |             | : 0           |             |
|                 | Bind         | Error      |                |          |             | : 0           |             |
|                 | Destination  |            | Address        |          | Unreachable | : 0           |             |
|                 | DNS          | Resolution |                | Failures |             | : 0           |             |
|                 | Reception    |            | Error          |          |             | : 0           |             |
|                 | Transmission |            | Error          |          |             | : 0           |             |
|                 | IP-SLA       | Latest     | Probe          | Results  |             |               |             |
|                 | Last         | Probe      | Time           |          |             | : 2018 Jul    | 13 02:00:35 |
|                 | Packets      |            | Sent           |          |             | : 1           |             |
|                 | Packets      |            | Received       |          |             | : 1           |             |
|                 | Packet       | Loss       | in             | Test     |             | : 0.0000%     |             |
|                 | Minimum      | RTT(ms)    |                |          |             | : 0.7900      |             |
|                 | Maximum      | RTT(ms)    |                |          |             | : 0.7900      |             |
|                 | Average      | RTT(ms)    |                |          |             | : 0.7900      |             |
|                 | DNS RTT(ms)  |            |                |          |             | : 0.0000      |             |
|                 | TCP RTT(ms)  |            |                |          |             | : 0.9710      |             |
| switch(config)# |              |            | show           | ip-sla   | xyz         |               |             |
|                 | IP-SLA       | Name       |                |          | : xyz       |               |             |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 95

|                 | Status                  |                   |              | : scheduled   |                   |              |            |     |
| --------------- | ----------------------- | ----------------- | ------------ | ------------- | ----------------- | ------------ | ---------- | --- |
|                 | IP-SLA Type             |                   |              | : tcp-connect |                   |              |            |     |
|                 | VRF                     |                   |              | : ipslasrc    |                   |              |            |     |
|                 | Source Port             |                   |              | : 5555        |                   |              |            |     |
|                 | Source IP               |                   |              | : 2.2.2.2     |                   |              |            |     |
|                 | Source Interface        |                   |              | :             |                   |              |            |     |
|                 | Domain Name             | Server            |              | :             |                   |              |            |     |
|                 | Probe interval(seconds) |                   |              | : 90          |                   |              |            |     |
| switch(config)# |                         | show              | ip-sla       | jitter-sla    | results           |              |            |     |
|                 | IP-SLA session          |                   | status       |               |                   |              |            |     |
|                 | IP-SLA                  | Name              |              |               | : jitter-sla      |              |            |     |
|                 | IP-SLA                  | Type              |              |               | : udp-jitter-voip |              |            |     |
|                 | Destination             |                   | Host Name/IP | Address:      | 2.2.2.1           |              |            |     |
|                 | Destination             |                   | Port         |               | : 8888            |              |            |     |
|                 | Source                  | IP Address/IFName |              |               | :                 |              |            |     |
|                 | Source                  | Port              |              |               | : 5555            |              |            |     |
|                 | Status                  |                   |              |               | : Running         |              |            |     |
|                 | IP-SLA Session          |                   | Cumulative   | Counters      |                   |              |            |     |
|                 | Total                   | Probes            | Transmitted  |               | : 1               |              |            |     |
|                 | Probes                  | Timed-out         |              |               | : 0               |              |            |     |
|                 | Bind Error              |                   |              |               | : 0               |              |            |     |
|                 | Destination             |                   | Address      | Unreachable   | : 0               |              |            |     |
|                 | DNS Resolution          |                   | Failures     |               | : 0               |              |            |     |
|                 | Reception               | Error             |              |               | : 0               |              |            |     |
|                 | Transmission            |                   | Error        |               | : 0               |              |            |     |
|                 | IP-SLA Latest           | Probe             | Results      |               |                   |              |            |     |
|                 | Last Probe              | Time              |              |               | : 2018 Jul        | 13           | 02:02:48   |     |
|                 | Packets                 | Sent              |              |               | : 1               |              |            |     |
|                 | Packets                 | Received          |              |               | : 1               |              |            |     |
|                 | Packet                  | Loss              | in Test      |               | : 0.0000%         |              |            |     |
|                 | Minimum                 | RTT(ms)           |              |               | : 0.7900          |              |            |     |
|                 | Maximum                 | RTT(ms)           |              |               | : 0.7900          |              |            |     |
|                 | Average                 | RTT(ms)           |              |               | : 0.7900          |              |            |     |
|                 | DNS RTT(ms)             |                   |              |               | : 0.0000          |              |            |     |
|                 | Min Positive            |                   | SD           |               | : 1               | Min Positive | DS         | : 2 |
|                 | Max Positive            |                   | SD           |               | : 1               | Max Positive | DS         | : 2 |
|                 | Positive                | SD                | Number       |               | : 2               | Positive     | DS Number  | : 2 |
|                 | Positive                | SD                | Sum          |               | : 2               | Positive     | DS Sum     | : 4 |
|                 | Positive                | SD                | Average      |               | : 5               | Positive     | DS Average | : 5 |
|                 | Min Negative            |                   | SD           |               | : 1               | Min Negative | DS         | : 1 |
|                 | Max Negative            |                   | SD           |               | : 1               | Max Negative | DS         | : 1 |
|                 | Negative                | SD                | Number       |               | : 2               | Negative     | DS Number  | : 4 |
|                 | Negative                | SD                | Sum          |               | : 2               | Negative     | DS Sum     | : 4 |
|                 | Negative                | SD                | Average      |               | : 5               | Negative     | DS Average | : 5 |
|                 | Max SD                  | Delay             |              |               | : 0               | Max DS       | Delay      | : 0 |
|                 | Min SD                  | Delay             |              |               | : 0               | Min DS       | Delay      | : 0 |
|                 | Average                 | SD Delay          |              |               | : 0               | Average      | DS Delay   | : 0 |
|                 | Voice Scores:           |                   |              |               |                   |              |            |     |
|                 | MOS Score               |                   |              |               | : 4.38            | ICPIF        |            | : 0 |
| switch(config)# |                         | show              | ip-sla       | m3op          |                   |              |            |     |
|                 | IP-SLA Name             |                   |              | : jitter-sla  |                   |              |            |     |
|                 | Status                  |                   |              | : Running     |                   |              |            |     |
IP-SLA|96

| IP-SLA    | Type              |        | : udp-jitter-voip |     |     |     |     |     |     |     |
| --------- | ----------------- | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- |
| VRF       |                   |        | : ipslasrc        |     |     |     |     |     |     |     |
| Source    | IP                |        | : 2.2.2.2         |     |     |     |     |     |     |     |
| Source    | Interface         |        | :                 |     |     |     |     |     |     |     |
| Domain    | Name              | Server | :                 |     |     |     |     |     |     |     |
| TOS       |                   |        | : 10              |     |     |     |     |     |     |     |
| Probe     | Interval(seconds) |        | : 90              |     |     |     |     |     |     |     |
| Advantage |                   | Factor | : 0               |     |     |     |     |     |     |     |
| Codec     | Type              |        | : g711a           |     |     |     |     |     |     |     |
switch(config)#
|            |                   | show ip-sla | http-sla           |     |     |     |     |     |     |     |
| ---------- | ----------------- | ----------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
| IP-SLA     | Name              |             | : http-sla         |     |     |     |     |     |     |     |
| Status     |                   |             | : Running          |     |     |     |     |     |     |     |
| IP-SLA     | Type              |             | : http             |     |     |     |     |     |     |     |
| VRF        |                   |             | : ipslasrc         |     |     |     |     |     |     |     |
| Source     | IP                |             | : 2.2.2.2          |     |     |     |     |     |     |     |
| Source     | Interface         |             | :                  |     |     |     |     |     |     |     |
| Domain     | Name              | Server      | : 10.10.10.2       |     |     |     |     |     |     |     |
| Probe      | Interval(seconds) |             | : 90               |     |     |     |     |     |     |     |
| HTTP       | Request           | Type        | : GET              |     |     |     |     |     |     |     |
| HTTP/HTTPS |                   | URL         | : abcd.com/ws/home |     |     |     |     |     |     |     |
| Cache      |                   |             | : Enabled          |     |     |     |     |     |     |     |
| HTTP       | Proxy             | URL         | :                  |     |     |     |     |     |     |     |
| HTTP       | Version           | Number      | : 1.1              |     |     |     |     |     |     |     |
```
| ##### IP-SLA |     | status description |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
```
| | Status |     |     | |   | Description |     |     |     |     |     | |   |
| -------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
|-------------------------|------------------------------------------------|
| | Running |     |     | |   | SLA is | fully operational |     |     |     |     | |   |
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
|--------------------------------|----------------------------------------------
----------------------------|
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
start-test
Syntax
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 97

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

IP-SLA | 98

SelectsthedestinationIPv4addressfortheIP-SLAorthehostnameofthedestination.
<PORT-NUM>
DestinationportfortheIP-SLA.Range:1to65535.
| [source {<SOURCE-IPV4-ADDR> |     | | <IFNAME>}] |     |     |
| --------------------------- | --- | ------------ | --- | --- |
SelectsthesourceIPv4addressforSLAprobesorthesourceinterfacetouseforsendingIP-SLAprobes.
| [source-port | <PORT-NUM>] |     |     |     |
| ------------ | ----------- | --- | --- | --- |
SpecifiestheportfortheIP-SLAtest.
| [name-server | <IPV4-ADDR-DNS-SERVER>] |     |     |     |
| ------------ | ----------------------- | --- | --- | --- |
SpecifiestheDNSserverfordestinationhostnameresolution.
| [probe-interval | <PROBE-INTERVAL>] |     |     |     |
| --------------- | ----------------- | --- | --- | --- |
Probeintervalinseconds.Range:30to604800.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| switch(config-ipsla-1)# |     | tcp-connect | 2.2.2.2 8080 |     |
| ----------------------- | --- | ----------- | ------------ | --- |
switch(config-ipsla-1)# tcp-connect 2.2.2.2 8080 source 2.2.2.1 source-port
6000
switch(config-ipsla-1)# tcp-connect 2.2.2.2 8080 source 1/1/1 source-port
6000
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
| source 2.2.2.1 | source-port | 6000 |     |     |
| -------------- | ----------- | ---- | --- | --- |
switch(config-ipsla-1)#
|              |             | tcp-connect | https://device.arubanetworks.com | 8080 |
| ------------ | ----------- | ----------- | -------------------------------- | ---- |
| source 1/1/1 | source-port | 6000        |                                  |      |
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
| name-server | 10.10.10.2 |     |     |     |
| ----------- | ---------- | --- | --- | --- |
udp-echo
Syntax
udp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>] [payload-size
<PAYLOAD-SIZE>] [tos <TYPE-OF-SERVICE>] [probe-interval <PROBE-INTERVAL>]
Description
ConfiguresUDPechoastheIP-SLAtestmechanism.Requiresdestinationaddress/hostnameand
destinationportnumberfortheIP-SLAofudp-echoSLAtype.
Commandcontext
config-ip-sla-<IP-SLA-NAME>
Parameters
| {<DEST-IPV4-ADDR> | | <HOSTNAME>} |     |     |     |
| ----------------- | ------------- | --- | --- | --- |
SelectsthedestinationIPv4addressfortheIP-SLAorthehostnameofthedestination.
<PORT-NUM>
SpecifiesthedestinationportfortheIP-SLA.Range:1to65535.
| [source {<SOURCE-IPV4-ADDR> |     | | <IFNAME>}] |     |     |
| --------------------------- | --- | ------------ | --- | --- |
SelectsthesourceIPv4addressforSLAprobesorthesourceinterfacetouseforsendingIP-SLAprobes.
| [source-port | <PORT-NUM>] |     |     |     |
| ------------ | ----------- | --- | --- | --- |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 99

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
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080 source

2.2.2.1

payload-size 50

switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080 source

1/1/1

payload-size 50

switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080

name-server 10.10.10.2

udp-jitter-voip

Syntax

udp-jitter-voip {<DEST-IPV4-ADDR> | <HOSTNAME>} <PORT-NUM> [codec-type <CODEC-TYPE>]

[advantage-factor <VALUE>] [source {<SOURCE-IPV4-ADDR> | <IFNAME>} [source-port <PORT-

NUM>]]

[name-server <IPV4-ADDR-DNS-SERVER>][probe-interval <PROBE-INTERVAL>] [tos <TYPE-OF-

SERVICE>]

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

IP-SLA | 100

Selectsthevaluefortheadvantagefactor.Defaultvalueis0.
| [source {<SOURCE-IPV4-ADDR> |     | | <IFNAME>}] |     |     |
| --------------------------- | --- | ------------ | --- | --- |
SelectsthesourceIPv4addressforSLAprobesorthesourceinterfacetouseforsendingIP-SLAprobes.
| [source-port <PORT-NUM>] |     |     |     |     |
| ------------------------ | --- | --- | --- | --- |
SpecifiesthevalueofsourceportfortheIP-SLAprobes.
| [name-server <IPV4-ADDR-DNS-SERVER>] |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- |
SpecifiestheDNSserverfordestinationhostnameresolution.
tos <TYPE-OF-SERVICE>
Specifiesthetypeofservice.Range:0to255.
| probe-interval <PROBE-INTERVAL> |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- |
Specifiestheprobeintervalinseconds.Range:120to604800.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10 codec-type
g711a
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10 codec-
| type g711a source | 2.2.2.1 |     |     |     |
| ----------------- | ------- | --- | --- | --- |
switch(config-ipsla-1)#
|                  |               | udp-jitter-voip | https://device.arubanetworks.com | 8080 |
| ---------------- | ------------- | --------------- | -------------------------------- | ---- |
| advantage-factor | 10 codec-type | g711a           |                                  |      |
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10 codec-
| type g711a source | 1/1/1 |     |     |     |
| ----------------- | ----- | --- | --- | --- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
| advantage-factor | 10 codec-type | g711a source | 2.2.2.1 |     |
| ---------------- | ------------- | ------------ | ------- | --- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
| advantage-factor | 10 codec-type | g711a source | 1/1/1 |     |
| ---------------- | ------------- | ------------ | ----- | --- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
advantage-factor 10 codec-type g711a name-server 10.10.10.2 probe-interval 120
| source 10.1.1.1 | source-port | 8888 tos 10 |     |     |
| --------------- | ----------- | ----------- | --- | --- |
vrf
Syntax
vrf <VRF-NAME>
no vrf [<VRF-NAME>]
Description
ConfigurestheVRFonwhichtheSLAwillsendorreceivepackets.Bydefault,thedefaultVRFisused.
ThenoformofthecommandremovesVRFfromSLA.
Commandcontext
config-ip-sla-<IP-SLA-NAME>
Parameters
<VRF-NAME>
SpecifiesaVRFname.Length:Default:default.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 101

Examples

switch(config-ip-sla-test)# vrf ipslasrc

switch(config-ip-sla-test)# no vrf

IP-SLA | 102

Chapter 8

L1-100Mbps downshift

L1-100Mbps downshift

The speed downshift feature allows the user to link-up at sub-optimal speeds when failing to link-up at the
highest advertised speed. There are fixed number of link attempts made to establish link at highest
advertised speed and when all of them fail and attempt is made to link-up at a lower possible speed.

This feature requires underlying PHY to have support for the same and hence capability is only added to
select set of ports. If a link cannot be established at the highest common denominator within a set number
of link attempts, the PHY advertises the next highest speed using auto-negotiation.

Limitations with speed downshift

n Link up may be delayed as certain number of retries are done to establish the link at highest advertise

speeds by both link partners before downshifting.

n Link may be established at sub-optimal speed.

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

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

103

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

Displays LAG interface information.

LOOPBACK

Displays loopback interface information.

TUNNEL

L1-100Mbps downshift | 104

Displaystunnelinterfaceinformation.
VLAN
DisplaysVLANinterfaceinformation.
<LAG-ID>
SpecifiestheLAGnumber.Range:1-256
<LOOPBACK-ID>
SpecifiestheLOOPBACKnumber.Range:0-255
<TUNNEL-ID>
SpecifiesthetunnelID.Range:1-255
<VLAN-ID>
SpecifiestheVLANID.Range:1-4094
VXLAN
DisplaystheVXLANinterfaceinformation.
<VXLAN-ID>
SpecifiestheVXLANinterfaceidentifier.Default:1
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowinginterfacesconfiguredforL2forwarding:
| switch(config-if)# |              |           | show             | interface         |                   |       |     |
| ------------------ | ------------ | --------- | ---------------- | ----------------- | ----------------- | ----- | --- |
| Interface          |              | 1/1/1 is  | down             | (Administratively |                   | down) |     |
| Admin              | state        | is down   |                  |                   |                   |       |     |
| State              | information: |           | Administratively |                   |                   | down  |     |
| Link               | transitions: |           | 2                |                   |                   |       |     |
| Description:       |              | Backup    | data             | center            | link              |       |     |
| Hardware:          |              | Ethernet, | MAC              | Address:          | 70:72:cf:fd:e7:b4 |       |     |
MTU 9198
Type SFP-SX
Full-duplex
| qos              | trust | none    |       |     |     |     |     |
| ---------------- | ----- | ------- | ----- | --- | --- | --- | --- |
| Speed            | 0     | Mb/s    |       |     |     |     |     |
| Auto-negotiation |       |         | is on |     |     |     |     |
| Flow-control:    |       | off     |       |     |     |     |     |
| Error-control:   |       | off     |       |     |     |     |     |
| VLAN             | Mode: | access  |       |     |     |     |     |
| Access           |       | VLAN: 1 |       |     |     |     |     |
Rx
|     | 1386055 | total           | packets |         |     | 586397526 | total bytes |
| --- | ------- | --------------- | ------- | ------- | --- | --------- | ----------- |
|     | 1374287 | unicast         |         | packets |     |           |             |
|     |         | 11764 multicast |         | packets |     |           |             |
|     |         | 4 broadcast     |         | packets |     |           |             |
|     |         | 0 errors        |         |         |     |           | 0 dropped   |
|     |         | 0 CRC/FCS       |         |         |     |           |             |
Tx
|     | 2475612 | total           | packets |         |     | 1003506711 | total bytes |
| --- | ------- | --------------- | ------- | ------- | --- | ---------- | ----------- |
|     | 2311806 | unicast         |         | packets |     |            |             |
|     | 100369  | multicast       |         | packets |     |            |             |
|     |         | 63437 broadcast |         | packets |     |            |             |
|     |         | 0 errors        |         |         |     | 2462773    | dropped     |
|     |         | 0 collision     |         |         |     |            |             |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 105

| Interface         | 1/2/1        | is down          | (Administratively |     |     | down) |
| ----------------- | ------------ | ---------------- | ----------------- | --- | --- | ----- |
| Admin             | state is     | down             |                   |     |     |       |
| State             | information: | Administratively |                   |     |     | down  |
| Link transitions: |              | 0                |                   |     |     |       |
Description:
| Hardware:     | Ethernet, |     | MAC Address: |     | 70:72:cf:fd:e7:b4 |     |
| ------------- | --------- | --- | ------------ | --- | ----------------- | --- |
| MTU 9198      |           |     |              |     |                   |     |
| Type QSFP+SR4 |           |     |              |     |                   |     |
Full-duplex
| qos trust        | none    |     |     |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- | --- |
| Speed            | 0 Mb/s  |     |     |     |     |     |
| Auto-negotiation |         | is  | off |     |     |     |
| Flow-control:    |         | off |     |     |     |     |
| Error-control:   |         | off |     |     |     |     |
| VLAN Mode:       | access  |     |     |     |     |     |
| Access           | VLAN: 1 |     |     |     |     |     |
Rx
|     | 0 total | packets   |         |         |     | 0 total bytes |
| --- | ------- | --------- | ------- | ------- | --- | ------------- |
|     | 0       | unicast   | packets |         |     |               |
|     | 0       | multicast |         | packets |     |               |
|     | 0       | broadcast |         | packets |     |               |
0 errors 0 dropped
0 CRC/FCS
Tx
|     | 0 total | packets   |         |         |     | 0 total bytes |
| --- | ------- | --------- | ------- | ------- | --- | ------------- |
|     | 0       | unicast   | packets |         |     |               |
|     | 0       | multicast |         | packets |     |               |
|     | 0       | broadcast |         | packets |     |               |
0 errors 0 dropped
0 collision
Whentheinterfaceiscurrentlylinkedatadownshiftedspeed:
| switch(config-if)# |       | show  | interface |     | 1/1/1 |     |
| ------------------ | ----- | ----- | --------- | --- | ----- | --- |
| Interface          | 1/1/1 | is up |           |     |       |     |
...
| Auto-negotiation |     | is               | on with | downshift |     | active |
| ---------------- | --- | ---------------- | ------- | --------- | --- | ------ |
| show interface   |     | downshift-enable |         |           |     |        |
Syntax
| show interface | [<IFNNAME>|<IFRANGE>] |     |     |     | downshift-enable |     |
| -------------- | --------------------- | --- | --- | --- | ---------------- | --- |
Description
Displaysspeeddownshiftinformation,includingtheinterfacespeedstatusandconfiguration.
Commandcontext
config
Parameters
<IFNAME>
Specifiesainterfacename.
<IFRANGE>
Specifiestheportidentifierrange.
L1-100Mbpsdownshift|106

Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showingautomaticdownshiftinformation:
| switch(config-if)# |     | show | interface | downshift-enable |     |
| ------------------ | --- | ---- | --------- | ---------------- | --- |
-------------------------------------------------
|      | Downshift |          |        | Speed |          |
| ---- | --------- | -------- | ------ | ----- | -------- |
| Port | Enabled   | | Active | Status |       | | Config |
-------------------------------------------------
| 1/1/1 | yes | yes | 100M-FDx |     | auto     |
| ----- | --- | --- | -------- | --- | -------- |
| 1/1/2 | yes | no  | 1G       |     | auto     |
| 1/1/3 | yes | no  | 100M-FDx |     | 100M-FDx |
| 1/1/4 | no  | no  | --       |     | auto     |
Showingautomaticdownshiftinformationonperinterface:
| switch(config-if)# |     | show | interface | 1/1/2 | downshift-enable |
| ------------------ | --- | ---- | --------- | ----- | ---------------- |
-------------------------------------------------
|      | Downshift |          |        | Speed |          |
| ---- | --------- | -------- | ------ | ----- | -------- |
| Port | Enabled   | | Active | Status |       | | Config |
-------------------------------------------------
| 1/1/2               | yes | no  | 1G        |     | auto |
| ------------------- | --- | --- | --------- | --- | ---- |
| show running-config |     |     | interface |     |      |
Syntax
| show running-config |     | interface | [<IFNNAME>|<IFRANGE>] |     |     |
| ------------------- | --- | --------- | --------------------- | --- | --- |
show running-config interface [lag | loopback | tunnel | vlan ] [<ID>]
Description
Displaysactiveconfigurationsofvariousswitchinterfaces.
Commandcontext
config
Parameters
<IFNAME>
Specifiesainterfacename.
<IFRANGE>
Specifiestheportidentifierrange.
LAG
SpecifiesLAGinterfaceinformation
LOOPBACK
Specifiesloopbackinterfaceinformation.
TUNNEL
Specifiestunnelinterfaceinformation.
VLAN
SpecifiesVLANinterfaceinformation.
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 107

<LAG-ID>
SpecifiestheLAGnumber.Range:1-256.
<LOOPBACK-ID>
SpecifiestheLOOPBACKnumber.Range:0-255.
<TUNNEL-ID>
SpecifiesthetunnelID.Range:1-255.
<VLAN-ID>
SpecifiestheVLANID.Range:1-4094.
VXLAN
SpecifiestheVXLANinterfaceinformation.
<VXLAN-ID>
SpecifiestheVXLANinterfaceidentifier.Default:1.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
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
| switch(config-if)# | show       | running-config | interface | loopback |
| ------------------ | ---------- | -------------- | --------- | -------- |
| No loopback        | interfaces | configured.    |           |          |
L1-100Mbpsdownshift|108

Chapter 9

Mirroring

Mirroring

Mirroring allows you to replicate all traffic arriving and/or leaving the selected system interfaces. This data
can be used for collection or analysis.

The traffic replicated using mirroring can be sent to a separate interface on the same switch as the traffic
source for analysis or inspection. Such a collection of interfaces and settings is called a mirror session.

A mirror session can be configured with many traffic sources but only a single output, or destination. In the
initial configuration, the mirror session is disabled. You have enable the feature to start the replication.

Care must be taken in choosing the number and rates of sources to avoid over-saturating a session destination. A

mirror session with multiple 10G sources can overwhelm a single 10G destination and important data may be lost.

Mirror statistics
Mirror statistics are reset for a Mirror-to-CPU session when an interface is added or removed from a LAG
that is a source interface in the Mirror session and during a failover.

Mirror endpoints
Enables switches to terminate a tunnel, decapsulate the original packet from the tunnel, and replicate the
original packet out to one or more switch interface(s). Supports termination of GRE encapsulation.

Scenario 1

A topology where there are two switches (sw1,sw2) connected by one link.

sw1 contains the mirror configuration with tunnel as destination, the mirrored packets are GRE
encapsulated.

sw2 contains the remote mirror termination, which decapsulates the packet and copies it to the configured
destinations. In the below configuration, the remote mirror decapsulates the GRE packet with
source/destination IP 9.9.9.9/2.2.2.2 with GRE Key 1 and replicate the inner payload to 1/1/2,1/1/3.

Configuration in sw1:

mirror session 1
destination tunnel 2.2.2.2 source 9.9.9.9
source interface 1/1/7 rx
enable

Configuration in sw2:

mirror endpoint test
source 9.9.9.9 destination 2.2.2.2 id 1
destination interface 1/1/2,1/1/3

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

109

no shutdown

Classifier policies and mirroring sessions
Network traffic can be mirrored to a destination interface in two ways:

n Using a mirroring session alone.

n Using Classifier Policies with mirror actions in conjunction with a mirroring session.

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

VLAN as a source
AOS-CX allows configuration of VLAN as a mirroring source. When a VLAN source is configured in the 'rx'
direction, all packets are mirrored as they are received in the switch. When a VLAN source is configured in 'tx'
direction, all packets are mirrored as they are transmitted out of the switch.

More than one source VLAN can be configured in a mirror session. Each such VLAN may specify its own
direction.

There is a limit of 1024 source VLANs in each direction of a given mirror session.

Same VLANs can be configured as a mirror source for multiple sessions.

Note: When changing a source VLAN in an enabled mirror session (that is, adding, changing direction, or
removing), mirrored packets being transmitted out the mirror destination port from other mirror sources
may be briefly interrupted during the reconfiguration.

Direction of an existing source VLAN can be updated in one of two ways:

1. Reenter the source vlan command with the new preferred direction.

2. Use the no form of the command with a direction (rx or tx) to selectively remove the specified
direction. Specifying the last remaining direction for that VLAN will remove the VLAN from the
configuration entirely.

For packets bridged through the switch:

Mirroring | 110

If the mirror is configured in 'both' direction, two copies of packets are mirrored, otherwise one copy of the
packet will be mirrored.

For routed packets:

n If the mirror is configured in the 'rx' direction, packets are mirrored in the pre-routed form with the

destination MAC address as the switch address.

n If the mirror is configured in the 'tx' direction, packets are mirrored in the post-routed form with the

source MAC as the switch address. Destination MAC is the nexthop gateway or station.

n If the mirror is configured in the 'both' direction, one copy of the packet will be mirrored.

Control plane packets generated by the switch's CPU are processed both in the ingress and the egress
packet processing pipeline. The following are the behaviors for mirroring with VLAN as source:

n If the mirror is configured in the 'rx' or 'tx' direction, the packets are mirrored to the mirror destination.

n If the mirror is configured in the 'both' direction, two copies of the packets are mirrored to the mirror

destination.

Mirroring commands

clear mirror

Syntax

clear mirror [all | <SESSION-ID>]

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

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

111

clear mirror endpoint

Syntax

clear mirror endpoint [NAME]

Description

Clears mirror endpoint statistics for all configured mirror endpoints. The optional parameter can be added
to clear a specific mirror endpoint.

Command context

Operator (>) or Manager (#)

Parameters

NAME

Specifies name of the mirror endpoint instance to be cleared.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Clearing statistics for all configured mirror endpoints:

switch# clear mirror endpoint

Clearing mirror statistics for mirror endpoint test:

switch# clear mirror endpoint test

comment

Syntax

comment <COMMENT>
no comment

Description

Specifies a comment for the mirroring session.

When used in mirror endpoint command context, specifies a comment for the mirror endpoint.

The no form of this command removes the comment.

Command context

config-mirror-<SESSION-ID>
config-mirror-endpoint

Parameters

<COMMENT>

A comment string of up to 64 characters composed of letters, numbers, underscores, dashes, spaces,
and periods.

Mirroring | 112

Authority

Administrators or local user group members with execution rights for this command.

Usage

Comments are optional and can be added or removed at any time without affecting the state of the
mirroring session.

Adding a comment to a session that already has a comment replaces the existing comment.

Examples

Adding a comment to a mirror session:

switch(config-mirror-3)# comment This Mirror will be removed during next maintenance
window

Removing the comment from mirror session 3:

switch(config-mirror-3)# no comment

Adding a comment to a mirror endpoint:

switch(config-mirror-endpoint-test)# comment Monitor endpoint traffic

Replacing the existing comment for mirror endpoint:

switch(config-mirror-endpoint-test)# comment Monitor statistics on each endpoint
interfaces

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

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

113

Example
CopyingthecapturedatatoafileonSFTPserver10.0.0.2:
switch#
|                 | copy             | tshark-pcap | sftp://root@10.0.0.2/file.pcap |     |          |           |       |
| --------------- | ---------------- | ----------- | ------------------------------ | --- | -------- | --------- | ----- |
| root@10.0.0.2's |                  | password:   |                                |     |          |           |       |
| Connected       | to               | 10.0.0.2.   |                                |     |          |           |       |
| sftp>           | put packets.pcap |             | file.pcap                      |     |          |           |       |
| Uploading       | packets.pcap     |             | to /root/file.pcap             |     |          |           |       |
| packets.pcap    |                  |             |                                |     | 100% 156 | 219.8KB/s | 00:00 |
| Copied          | successfully.    |             |                                |     |          |           |       |
| destination     |                  | cpu         |                                |     |          |           |       |
Syntax
| destination    | cpu |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- |
| no destination | cpu |     |     |     |     |     |     |
Description
ThecommandcausesthemirrorsessiontotransmitmirroredpacketstotheswitchCPU.Thisdestination
maybeconfiguredformultiplesessions,howeveronlyonesuchconfiguredsessionmaybeactiveatagiven
time.
ThediagnosticutilityTsharkmaybeusedtoviewandcapturepacketstransmittedtotheCPUthroughthis
route.Ctrl+CmustbeenteredtoterminateaTsharkcapturesession.Moredetailscanbefoundinthe
SupportabilityGuide.
ThenoformofthiscommandwillimmediatelystopsmirroringtraffictotheCPU,butwillnotremoveany
sourcesfromthemirrorconfiguration.
Commandcontext
config-mirror-<SESSION-ID>
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringamirrorsessionwithCPUasthedestination.
| switch#                  | config |        |             |     |     |     |     |
| ------------------------ | ------ | ------ | ----------- | --- | --- | --- | --- |
| switch(config)#          |        | mirror | session     | 1   |     |     |     |
| switch(config-mirror-1)# |        |        | destination |     | cpu |     |     |
Removingthedestinationentirely.
| switch(config-mirror-1)# |     |           | no  | destination | cpu |     |     |
| ------------------------ | --- | --------- | --- | ----------- | --- | --- | --- |
| destination              |     | interface |     |             |     |     |     |
Syntax
| destination    | interface | <IFNAMELIST> |              |     |     |     |     |
| -------------- | --------- | ------------ | ------------ | --- | --- | --- | --- |
| no destination | interface |              | <IFNAMELIST> |     |     |     |     |
Mirroring|114

<IFNAMELIST> can accept input as System interfaces and LAGs in the form of range, comma or both.

Description

config context:

Specifies the interface to where all mirrored traffic for the session will be transmitted.

There is a limit of 64 destination interfaces in a given mirror session.

You may configure the same destination in multiple mirror sessions however only one of those sessions
sharing the destination can be enabled at a given time.

Layer 2 or Layer 3 Ethernet ports, LAGs, tunnels and CPU as a mirror destination is supported. A port that is
already a member of a LAG is not a valid mirror destination.

Configuring a different destination interface in an enabled mirror session will cause all mirrored traffic to use
the new interface. This may cause a temporary suspension of mirrored traffic from the sources during the
reconfiguration.

The no form of this command will cease the use of the interface and disable the session. If there is at least
one interface the mirror session will continue to be enabled.

mirror endpoint context:

Specifies the interface(s) to where the original packets after decapsulation from the tunnel will be
transmitted. This includes system interfaces (e.g, 1/1/1) and LAG interfaces (e.g, lag1). A maximum of 64
interfaces can be configured as an endpoint interface for a given mirror endpoint.

The no form of this command remove the specific endpoint interface(s) from the configured list. If no
interface is specified, all the endpoint interfaces will be removed.

Command context

config-mirror-<SESSION-ID>
config-mirror-endpoint

Parameters

IFNAMELIST

Specifies list of destination interfaces.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating a mirror session and adding an interface as a destination:

switch(config)# mirror session 1
switch(config-mirror-1)# destination interface 1/1/1

Replacing the existing destination with a different port:

switch(config-mirror-1)# destination interface 1/1/5

Replacing the existing destination with a LAG interface:

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

115

| switch(config-mirror-1)# | destination | interface | lag100 |     |
| ------------------------ | ----------- | --------- | ------ | --- |
Removingtheexistingdestinationentirely:
| switch(config-mirror-1)# | no destination | interface |     |     |
| ------------------------ | -------------- | --------- | --- | --- |
Removingdestinationinterfaces:
| switch(config-mirror-1)# | no destination | interface | 1/1/1-1/1/2 |     |
| ------------------------ | -------------- | --------- | ----------- | --- |
If an interface to delete is not part of the mirror session, display warning message
and continue
| switch(config-mirror-1)# | no destination | interface | 1/1/1-1/1/2 |     |
| ------------------------ | -------------- | --------- | ----------- | --- |
Ignoring destination interface 1/1/2 as it is not currently configured in mirror
session 1
Configuring1/1/1-1/1/10,1/1/20asamirrorendpointinterface:
switch(config-mirror-endpoint-test)# destination interface 1/1/1-1/1/10,1/1/20
Removingmirroredendpointinterface1/1/1:
switch(config-mirror-endpoint-test)# no destination interface 1/1/1
Removingmirroredendpointinterfaces1/1/1-1/1/2:
switch(config-mirror-endpoint-test)#
|     |     | no destination | interface | 1/1/1-1/1/2 |
| --- | --- | -------------- | --------- | ----------- |
Attemptingtoremove1/1/11fromalistwhenitisnotconfigured:
switch(config-mirror-endpoint-test)# no destination interface 1/1/11
Ignoring interface 1/1/11 as it is not currently configured in mirror endpoint 1
diagnostic
Syntax
diagnostic
| diag utilities tshark [file]        |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- |
| diag utilities tshark [delete-file] |     |     |     |     |
Description
Capturespacketsfromamirror-to-cpusession,andsavethemostrecent32MBtopcapfilewhichcanthen
becopiedandanalyzed.Whencapturingamirror-to-cpusessiontoafile,packetswillnotbedumpedtothe
console.
Thediagnosticcommandmustbeenteredpriortothediag utilities tsharkcommand.
Mirroring|116

Use the delete-file form of this command to delete the most recent capture file.

Since file and delete-file are optional, the behavior of the base command diag utilities tshark does
not save anything to a file, and instead dumps the tshark session to the console until CTRL + c is entered.

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

When a mirroring session is disabled, the show mirror command for that session ID shows an Admin Status
of disable and an Operation Status of disabled.

Example

Disabling a mirroring session:

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

117

| switch(config)# | mirror session | 3   |     |
| --------------- | -------------- | --- | --- |
switch(config-mirror-3)#
disable
enable
Syntax
enable
Description
Enablesthemirroringsessionforthecurrentcommandcontext.
Commandcontext
config-mirror-<SESSION-ID>
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Bydefault,mirroringsessionsaredisabled.
Whenamirroringsessionisenabled,theshow mirrorcommandforthatsessionIDshowsanAdmin Status
| ofenableandanOperation | Statusofenabled. |     |     |
| ---------------------- | ---------------- | --- | --- |
IfsFlowisenabledonaninterfaceandamirroringsessionspecifiesthesameinterfaceasthesourceof
receivedtraffic(thesourceisconfiguredwithadirectionofrxorboth):
Theattempttoenablethemirroringsessionfailsandanerrorisreturned.
n
Whenadding,removing,orchangingtheconfigurationofasourceinterfaceinanenabledmirroringsession,
packetsfromothermirrorsourcesusingthesamedestinationinterfacemightbeinterrupted.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringandenablingamirroringsession:
| switch(config)#          | mirror session | 3         |          |
| ------------------------ | -------------- | --------- | -------- |
| switch(config-mirror-3)# | source         | interface | 1/1/2 rx |
| switch(config-mirror-3)# | destination    | interface | 1/1/3    |
switch(config-mirror-3)# comment Monitor router port ingress-only traffic
| switch(config-mirror-3)# | enable |     |     |
| ------------------------ | ------ | --- | --- |
mirror session
Syntax
| mirror session <SESSION-ID> |              |     |     |
| --------------------------- | ------------ | --- | --- |
| no mirror session           | <SESSION-ID> |     |     |
Description
Createsamirroringsessionconfigurationcontextorentersanexistingmirroringsessionconfiguration
context.
Mirroring|118

From this context, you can enter commands to configure and enable or disable the mirroring session.

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

mirror endpoint

Syntax

mirror endpoint NAME
no mirror endpoint NAME

Description

Creates the specified mirror endpoint or enters its context if it already exists. The specifics of a mirror
endpoint are created or altered while in the mirror endpoint context and the mirror endpoint is enabled or
disabled from this context. It may be possible to support different encapsulations by different ASICs. For
example, UDP for PVOS compatibility. Termination of GRE encapsulation is also supported.

The no form of this command removes an existing mirror endpoint. An enabled mirror endpoint is
automatically disabled first before removal.

Command context

You must be in the global configuration context: switch(config)#.

Parameters

NAME

Specifies mirror endpoint name.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating a mirror endpoint named test :

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

119

switch(config)# mirror endpoint test

Deleting mirror endpoint named test

switch(config)# no mirror endpoint test

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

The mirroring session is enabled, but the destination interface is shut down. No traffic can be monitored.

disabled

The mirroring session is disabled and is not in an error condition.

Mirroring | 120

enabled
Themirroringsessionisenabled.
external/driver_error
AninternalASIChardwareerroroccurred.
hit_active_sessions_capacity
Themirroringsessioncouldnotbeenabledbecausethemaximumnumberofsupportedmirroring
sessionsarealreadyenabled.
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
Onthe6400SwitchSeries,interfaceidentificationdiffers.
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
| show mirror | endpoint |     |     |     |
| ----------- | -------- | --- | --- | --- |
Syntax
| show mirror | endpoint | [NAME] |     |     |
| ----------- | -------- | ------ | --- | --- |
Description
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 121

Showsalistofallconfiguredmirrorendpoints,theirAdminStatusandtheirOperationStatus.
Theoptionalparameterwilldisplaythedetailsofthespecifiedmirrorendpointifitexists.
Commandcontext
Operator(>)orManager(#)
Parameters
NAME
Specifiesnameofthemirrorendpointinstancetobedisplayed.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Showingasummaryofallconfiguredmirrorendpointsontheswitch:
| switch# show | mirror endpoint  |        |     |
| ------------ | ---------------- | ------ | --- |
| Name Admin   | Status Operation | Status |     |
----- -------------- ----------------------------------------------------
| test enable     | enabled  |     |     |
| --------------- | -------- | --- | --- |
| monitor disable | disabled |     |     |
Showingthedetailsofenabledmirrorendpointaudit:
| switch# show     | mirror endpoint | audit |     |
| ---------------- | --------------- | ----- | --- |
| Mirror Endpoint: | audit           |       |     |
| Admin Status:    | enable          |       |     |
| Operation        | Status: enabled |       |     |
| Comment: Mirror  | Endpoint Audit  |       |     |
Type: gre
| Tunnel: source  | 1.1.1.1 destination | 1.1.1.2 | id 1 vrf default |
| --------------- | ------------------- | ------- | ---------------- |
| Interface:      | 1/1/1-1/1/10,lag1   |         |                  |
| Output Packets: | 123456789           |         |                  |
| Output Bytes:   | 8912345678          |         |                  |
shutdown
Syntax
no shutdown
Description
Enablesmirrorendpointfromitsdefaultdisabledstate.Toverifythemirrorendpointwassuccessfully
activated,runtheshow mirror endpoint NAMEcommandandverifythattheAdmin Statusand
Operational Statushaschangedfromdisabledtoenabled.Ifthestatusvalueremainsdisabled,consult
thesystemlogstodeterminethereasonforactivationfailure.Todisablethemirrorendpoint,firstdisable
theremotemirrorsessionontheswitchthat'soriginatingthedata.Next,usetheshutdowncommandto
disablethemirrorendpoint.
Commandcontext
Mirroring|122

You must be in the global configuration context: switch(config)#.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling a mirror endpoint:

switch(config)# mirror endpoint test
switch(config-mirror-endpoint-test)# no shutdown

Disabling a mirror endpoint:

switch(config)# mirror endpoint test
switch(config-mirror-endpoint-test)# shutdown

source

Syntax

source <source-id> destination <destination-id> id <1-4294967295> [vrf <VRF_NAME>] [type
{gre}]
no source

Description

Configures tunnel parameters of the mirror endpoint. Configuring a tunnel parameter to a mirror endpoint
will replace the existing configuration. By default the VRF is default, users can also explicitly provide a
custom VRF. The default tunnel type is considered to be GRE and users also have the option to explicitly give
type as GRE.

The no form removes the tunnel parameters of the mirror endpoint.

Command context

You must be in the global configuration context: switch(config)#.

Parameters

source-ip

Specifies L3 encapsulated IPv4 source in the form A.B.C.D.

destination-ip

Specifies L3 encapsulated IPv4 destination in the form A.B.C.D.

id

Specifies tunnel identifier from the encapsulated packet.

VRF_NAME

Specifies the name of VRF for which the tunnel belongs to.

Authority

Administrators or local user group members with execution rights for this command.

Examples

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

123

Configuring a tunnel parameter to a mirror endpoint:

switch(config-mirror-endpoint-test)# source 1.1.1.1 destination 7.7.7.7 id 1 vrf
default type gre

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

Authority

Administrators or local user group members with execution rights for this command.

Usage

There is a limit of four source interfaces in each direction of a given mirror session. However, there is a
practical limit to the amount of traffic that a mirror destination can transmit. For example, mirroring session
with multiple 10G sources can overwhelm a single 10G destination.

When adding, removing, or changing the configuration of a source port in an enabled mirroring session, packets

from other mirror sources using the same destination port might be interrupted.

Examples

Configuring a mirrored traffic source interface:

Mirroring | 124

|     | switch(config-mirror-1)# |     |       |        | source | interface    |       |
| --- | ------------------------ | --- | ----- | ------ | ------ | ------------ | ----- |
|     | LAG-NAME                 |     | Enter | a LAG  | name.  | For example, | lag10 |
|     | PORT-NUM                 |     | Enter | a port | number |              |       |
Creatingamirroringsessionandconfiguringasourceinterfacetomirrorbothtransmittedandreceived
packets:
|     | switch(config)#          |     | mirror | session |        | 1         |            |
| --- | ------------------------ | --- | ------ | ------- | ------ | --------- | ---------- |
|     | switch(config-mirror-1)# |     |        |         | source | interface | 1/1/1 both |
Creatingasecondmirroringsessionandconfiguringtwosourceinterfaces.Oneportmirroringonly
transmittedpacketsandtheothermirroringbothtransmittedandreceivedpackets:
|     | switch(config)#          |     | mirror | session |        | 2         |            |
| --- | ------------------------ | --- | ------ | ------- | ------ | --------- | ---------- |
|     | switch(config-mirror-2)# |     |        |         | source | interface | 1/1/3 tx   |
|     | switch(config-mirror-2)# |     |        |         | source | interface | 1/2/1 both |
Removingthefirstsourceinterface:
|     | switch(config-mirror-2)# |     |     |     | no source | interface | 1/2/3 |
| --- | ------------------------ | --- | --- | --- | --------- | --------- | ----- |
Configuringasourceinterfacetomirrorreceivedpacketsonly:
switch(config-mirror-3)#
|     |     |     |     |     | source | interface | 1/1/2 rx |
| --- | --- | --- | --- | --- | ------ | --------- | -------- |
Configuringasourceinterfacetomirrorbothtransmittedandreceivedpackets:
|     | switch(config-mirror-1)# |     |     |     | source | interface | 1/1/1 both |
| --- | ------------------------ | --- | --- | --- | ------ | --------- | ---------- |
ConfiguringaLAGassourceinterfacetomirrorbothtransmittedandreceivedpackets:
|     | switch(config-mirror-4)# |     |     |     | source | interface | lag1 both |
| --- | ------------------------ | --- | --- | --- | ------ | --------- | --------- |
Stoppingthemirroringofreceivedpacketsfromaconfiguredsourceinterface:
|        | switch(config-mirror-4)# |      |     |     | no source | interface | lag1 rx |
| ------ | ------------------------ | ---- | --- | --- | --------- | --------- | ------- |
| source |                          | vlan |     |     |           |           |         |
Syntax
| source | vlan   | <VLAN-NUM>      |     | {rx | | tx | | both}   |     |
| ------ | ------ | --------------- | --- | ----- | ---- | ------- | --- |
| no     | source | vlan <VLAN-NUM> |     | {rx   | | tx | | both} |     |
Description
MirroringwithVLANasasourceissupportedinthefollowingtrafficdirections:
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 125

n both - traffic received and transmitted

n rx - only received traffic

n tx - only transmitted traffic

More than one source VLAN can be configured in a mirror session. Each such VLAN may specify its own
direction.

There is a limit of 1024 source VLANs for a given mirror session. There is also a limit of 4096 source VLANs
across all mirror sessions.

Same VLAN can be configured as a mirror source for multiple sessions.

When changing a source VLAN in an enabled mirror session (i.e. adding, changing direction, or removing)

mirrored packets being transmitted out of the mirror destination port from other mirror sources may be briefly

interrupted during the reconfiguration.

Direction of an existing source VLAN can be updated in one of two ways.

n Reenter the source vlan <VLAN-NUM> <direction> command with the new preferred direction.

n Use the no source vlan <VLAN-NUM> <direction> form of the command with a direction (rx or tx) to

selectively remove the specified direction.

Specifying the last remaining direction for that VLAN will remove the VLAN from the configuration entirely.

Mirroring allows configuration of VLAN as a source. When VLAN source is configured in the rx direction, all
packets are mirrored as they are received in the switch. When VLAN source is configured in tx direction, all
packets are mirrored as they are transmitted out of the switch.

For packets bridged through the switch:

n If the mirror is configured in 'both' direction, two copies of packets are mirrored, otherwise one copy of

the packet will be mirrored.

For routed packets:

n If the mirror is configured in rx direction, packets are mirrored in the pre-routed form with the

Destination MAC address as the switch address.

n If the mirror is configured in tx direction, packets are mirrored in post-routed form with the source MAC

as the switch address. Destination MAC is the nexthop gateway or station.

n If the mirror is configured in both direction, one copy of the packet will be mirrored.

Control plane packets generated by the switch's CPU are processed both in theingress and the egress packet
processing pipeline. The following are the behavior for mirroring with VLAN as source:

n If the mirror is configured in the rx or tx direction, the packets are mirrored to the mirror destination.

n If the mirror is configured in the both direction, two copies of the packets are mirrored to the mirror

destination.

The no form command will cease mirroring traffic from the specified source VLAN and remove the source
from the mirror configuration.

Command context

You must be in the global configuration context: switch(config)#.

Mirroring | 126

Parameters
VLAN-NUM
SelectstheVLANnumber.
direction
Specifiesthedirectionofmirroring.tx(transmit),rx(receive),orboth.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
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
| switch(config-mirror-2)# | source | vlan 10 rx |
| ------------------------ | ------ | ---------- |
Removingthefirstsourceinterfaceinsession2entirely,andremovingthetransmitdirectionfromtheother
sothatmirroringonlyoccursinthereceivedirection:
| switch(config-mirror-2)# | source | vlan 10 rx |
| ------------------------ | ------ | ---------- |
| switch(config-mirror-2)# | source | vlan 20 tx |
Showingmaximumof1024mirrorsourceVLANsallowed:
| switch(config-mirror-2)# | source | vlan 2000 rx |
| ------------------------ | ------ | ------------ |
The maximum number of source VLANs per mirror session is 1024 in each direction
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 127

Chapter 10
|            |          |            | Monitoring | a device | using SNMP |
| ---------- | -------- | ---------- | ---------- | -------- | ---------- |
| Monitoring | a device | using SNMP |            |          |            |
Configuring SNMP:RefertotheArubaOS-CXSNMP/MIBGuideforinformationonhowtoaddSNMPsoa
devicecanbemonitoredfromanetworkmanagementsystem(NMS).
Configuring an SNMPtrapreceiver:RefertotheArubaOS-CXSNMP/MIBGuideandspecificinformation
| abouttheshow | trapcommandtoenableSNMPtraps. |     |     |     |     |
| ------------ | ----------------------------- | --- | --- | --- | --- |
snmp
128
| AOS-CX10.07MonitoringGuide| | (6300and6400SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------------- | --- | --- | --- | --- |

Chapter 11

Power-over-Ethernet

Power-over-Ethernet

n The Power-over-Ethernet (PoE) subsystem manages power supplied to devices using standard Ethernet
data cables. A Power Sourcing Equipment (PSE) supplies DC power as well as Ethernet connectivity to a
Powered Device (PD) using a standard Ethernet cable. The maximum current depends on the PD
Requested Class.

n A PoE subsystem contains two parts : a PSE and PD. A Power Sourcing Equipment (PSE) is a device that

provides power through a standard Ethernet cable. A PoE capable switch functions as PSE. All Aruba PoE
switches are considered as PSEs. A PD is a device powered by a PSE. Examples of PD are VoIP phones,
Wireless APs, and IP cameras.

n When a PD or any network cable is connected to a PSE port, the PSE applies a detection voltage and

measures the resistance value of the PD. If resistance is within IEEE 802.3 standard values (23 - 26k ohm),
the connected device is treated as PD and classification begins. For legacy devices to be detected, you
must enable prestandard detection on the switch.

n PDs are divided into different types and classes based on PD power requirements. The power supplied by
the PSE is higher than the power PD draws to accommodate for the line losses that can result with the
use of the standard maximum length cable(100m).

o Type 1: PSE can supply minimum of 15.4W, and PD can draw a maximum of 13W.

o Type 2: PSE can supply minimum of 30W, and PD can draw a maximum of 25.5W.

o Type 3: PSE can supply minimum of 60W, and PD can draw a maximum of 51W.

o Type 4: PSE can supply minimum of 90W, and PD can draw a maximum of 71W.

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
Ethernet cable, the standard introduced the ability to use all four pairs within the Ethernet cable instead
of the two pairs used by previous standards (802.3at, 802.3af).

n Supported protocols:

o Compatibility with IEEE 802.3af, 802.3at, 802.3bt and prestandard.

o Long first class event supported on Type 3-4 PSE.

o Support for Single Signature (SS) Type 0-6 and Dual Signature (DS) Type 0-4 PDs.

o Multi-Event classification permits mutual ID of SS Class 0-6 and DS Class 0-4.

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

129

o Support LLDP Data Link Layer (DLL) Type 1-2 extension 12-octet TLV and Type 3-4 extension 29-

octet TLV.

o Default PSE assigned class delivers the maximum PSE capable power at initial power up based on PD

requested class.

n Always-on PoE is a feature that provides the ability for a switch to continue to provide power across user
initiated reboots through software. Always-on PoE is enabled by default and no additional configuration
is needed.

PDs only remain powered, no data transfer or PoE power negotiation can occur until the switch has completely

booted up and in normal operation. PD faults occurring prior to full switch boot up will result in PoE power

removal and restart the detection process only after switch returns to normal operation.

PoE commands
All PoE configuration commands except threshold configuration and always-on poe configuration are
entered at the config-if context. The PoE threshold command is used at the system level whereas the
always-on poe command is set at the slot level. These commands can only be configured in the global
configuration context.

lldp dot3 poe

Syntax

lldp dot3 poe
no lldp dot3 poe

Description

Enables 802.3 TLV list in LLDP to advertise for Power over Ethernet Data Link Layer Classification. LLDP
dot3 TLV is by default enabled for PoE.

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

switch(config-if)# no lldp dot3 poe

Power-over-Ethernet | 130

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

Command context

config-if

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

131

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Enablingper-interfacepowerdistribution:
| switch(config)#    |     | interface           | 1/1/1 |     |     |     |
| ------------------ | --- | ------------------- | ----- | --- | --- | --- |
| switch(config-if)# |     | power-over-ethernet |       |     |     |     |
Disablingper-interfacepowerdistribution:
| switch(config-if)# |     | no power-over-ethernet |     |     |     |     |
| ------------------ | --- | ---------------------- | --- | --- | --- | --- |
ShowingQuickPoEenabled:
| switch(config-if)#  |     | power-over-ethernet    |             |       | quick-poe | 1/1         |
| ------------------- | --- | ---------------------- | ----------- | ----- | --------- | ----------- |
| switch(config-if)#  |     | interface              |             | 1/1/1 |           |             |
| switch(config-if)#  |     | no power-over-ethernet |             |       |           |             |
| Interface           | PoE | cannot be              | disabled    | when  | Quick PoE | is enabled. |
| power-over-ethernet |     |                        | allocate-by |       |           |             |
Syntax
| power-over-ethernet    |     | allocate-by |     | {usage | | class} |     |
| ---------------------- | --- | ----------- | --- | ------ | -------- | --- |
| no power-over-ethernet |     | allocate-by |     | {usage | | class} |     |
Description
Configuresthepowerallocationmethod.Powerallocationmethodisinitiallybasedonusage.PSEAllocated
powervaluewillchangetoLLDPnegotiatedpowerifandwhenLLDPexchangetakesplacebetweenPSEand
PD.WhenthereisnoLLDPnegotiation,PSEAllocatedPowerValuewillbetheactualinstantaneouspower
drawandreservepowerbasedonactualconsumption.Inallocate-byclass,powerallocationisbasedonPD
requestedclassandPSEallocatedpowervaluewillbetheLLDPnegotiatedpowerwhenLLDPexchange
takesplacebetweenPSEandPD..WhenthereisnoLLDPnegotiation,PSEAllocatePowerwillbebasedon
PDclass.ReservepowerisbasedonPDClass.Bydefault,powerallocationisbyusage.
Thenoformofthiscommandresetstheactiontodefault.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringthepowerallocationmethod:
Power-over-Ethernet|132

| switch(config)# | interface | 1/1/1 |     |     |     |     |
| --------------- | --------- | ----- | --- | --- | --- | --- |
switch(config-if)#
|                    | power-over-ethernet |     |     | allocate-by |     | usage |
| ------------------ | ------------------- | --- | --- | ----------- | --- | ----- |
| switch(config-if)# | power-over-ethernet |     |     | allocate-by |     | class |
Resettingpowerallocationmethod:
| switch(config-if)#  | no power-over-ethernet |           |     | allocate-by |     | class |
| ------------------- | ---------------------- | --------- | --- | ----------- | --- | ----- |
| power-over-ethernet |                        | always-on |     |             |     |       |
Syntax
| power-over-ethernet    | always-on | <MODULE-ID> |             |     |     |     |
| ---------------------- | --------- | ----------- | ----------- | --- | --- | --- |
| no power-over-ethernet | always-on |             | <MODULE-ID> |     |     |     |
Description
Always-onPoEisafeaturethatprovidestheabilitytotheswitchtocontinuetoprovidepoweracrossasoft
reboot.Itisapplicableonlytotheinterfaceswhichwereconnectedanddeliveringbeforethesoftreboot.
Also,powerwillnotbedeliveredifpowertotheswitchisinterrupted.Thiscommandenablesordisablesthe
always-onPoEfeatureattheswitchortheslotlevel.Bydefault,always-onPoEisenabledattheswitchor
theslotlevel.
Thenoformofthiscommanddisablespowerdistributiononsoftreboot.
Commandcontext
config
Parameters
<MODULE-ID>
Modulenumbertoapplyalways-onPoEconfiguration.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingper-interfacepowerdistribution:
| switch(config)# | power-over-ethernet |     |     | always-on | 1/1 |     |
| --------------- | ------------------- | --- | --- | --------- | --- | --- |
Disablingper-interfacepowerdistribution:
| switch(config)#     | no power-over-ethernet |                |     | always-on |     | 1/1 |
| ------------------- | ---------------------- | -------------- | --- | --------- | --- | --- |
| power-over-ethernet |                        | assigned-class |     |           |     |     |
Syntax
| power-over-ethernet    | assigned-class |     | {3 | | 4 | 6} |     |     |
| ---------------------- | -------------- | --- | ---- | ------ | --- | --- |
| no power-over-ethernet | assigned-class |     |      |        |     |     |
Description
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 133

LimitPoEpowerbasedontheassignedclass.Whenanuserassignsamaximumclasstoaninterface,the
PSEwilllimitthemaximumpowerdeliveredtothePDuptoatotalpowerdrawnotexceedingthePSE
assigned-classpower.PowerdemotionoccurswhenaPDrequestedclassishigherthanthePSEassigned
class,permittingthePDtoreceivepowerandoperateinareducedpowermode.PoEportscannotsetan
assignedclasswhenQuickPoEisenabledonthesybsystem.Thedefaultassignedclassis4for2-pair
capablePSEand6for4-paircapablePSE.
Thenoformofthiscommandresetstheactiontodefault.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
SettingPoEassignedclass:
| switch(config)#    | interface           | 1/1/1 |                |     |     |
| ------------------ | ------------------- | ----- | -------------- | --- | --- |
| switch(config-if)# | power-over-ethernet |       | assigned-class |     | 4   |
ResettingPoEassignedclasstodefault:
| switch(config-if)# | no power-over-ethernet |     | assigned-class |     | 4   |
| ------------------ | ---------------------- | --- | -------------- | --- | --- |
ShowingQuickPoEenabled:
| switch(config)# | power-over-ethernet |       | quick-poe      | 1/1 |     |
| --------------- | ------------------- | ----- | -------------- | --- | --- |
| switch(config)# | interface           | 1/1/1 |                |     |     |
| switch(config)# | power-over-ethernet |       | assigned-class |     | 4   |
Interface assigned class cannot be configured when Quick PoE is enabled.
| power-over-ethernet |     | pre-std-detect |     |     |     |
| ------------------- | --- | -------------- | --- | --- | --- |
Syntax
| power-over-ethernet    | pre-std-detect |     |     |     |     |
| ---------------------- | -------------- | --- | --- | --- | --- |
| no power-over-ethernet | pre-std-detect |     |     |     |     |
Description
BeforeIEEE802.3releasedthefirstPoweroverEthernetstandard(802.3af),vendorshadshippedPoE
capableswitchesandPD's.AswearebackwardcompatibleArubawillsupportbothIEEEstandardandpre-
standard802.3afPoweroverEthernetPD'sconcurrently.ThisCLIallowstheusertoenableordisablepre-
802.3af-standarddevicedetectionandpoweringonthespecificport.Whenpre-std-detectisenabled,
powerwillbedeliveredonPairAonly.Defaultisdisabled.
Thenoformofthiscommandresetstheactiontodefault.
Commandcontext
config-if
Power-over-Ethernet|134

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Enablingstandarddevicedetection:
| switch(config)#    | interface           | 1/1/1 |                |
| ------------------ | ------------------- | ----- | -------------- |
| switch(config-if)# | power-over-ethernet |       | pre-std-detect |
Disablingstandarddevicedetection:
| switch(config-if)#  | no power-over-ethernet |          | pre-std-detect |
| ------------------- | ---------------------- | -------- | -------------- |
| power-over-ethernet |                        | priority |                |
Syntax
| power-over-ethernet    | priority | {critical | | high | low} |
| ---------------------- | -------- | --------- | ------------- |
| no power-over-ethernet | priority | {critical | | high | low} |
Description
SetsPoEpriorityforaninterfaceSpecifyingcritical,high,orlowindicatesthepriorityoftheinterfaceinthe
eventofpowerover-subscription.Withinthesameprioritylevel,higherpower-priorityline-moduleports
havehigherprecedence.WithsamePoEpriorityandsameline-modulepriority,lowernumberedline-
moduleportshavehigherprecedence.Per-interfacePoEpriorityislowbydefault.
ThenoformofthiscommandresetstheprioritytodefaultPoEpriority"low".
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringPoEpriority:
| switch(config)#    | interface           | 1/1/1 |                   |
| ------------------ | ------------------- | ----- | ----------------- |
| switch(config-if)# | power-over-ethernet |       | priority critical |
| switch(config-if)# | power-over-ethernet |       | priority high     |
ResettingthePoEprioritytodefault:
| switch(config-if)#  | no power-over-ethernet |           | priority high |
| ------------------- | ---------------------- | --------- | ------------- |
| power-over-ethernet |                        | quick-poe |               |
Syntax
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 135

| power-over-ethernet |     | quick-poe | <MODULE-ID> |     |     |     |
| ------------------- | --- | --------- | ----------- | --- | --- | --- |
no power-over-ethernet
Description
QuickPoEisafeaturethatprovidestheabilityfortheswitchtoprovidepowertotheconnectedpowered
deviceassoonasswitchgoesthroughcoldreboot.WhenquickPoEisenabledonthesubsystemPoEport
disablementandPDdemotionisnotallowed.alsoquickPoEenablementisnotallowedifanyoftheportis
disabledonthesubsystem.Usershouldnotover-subscribethePoEpowerwhenquickPoEisenabled.
QuickPoEsavedconfigurationwillworkirrespectiveoftheconfigurationchangeatreboot.
EnablesquickPoEfeatureontheswitchorthesubsystemlevel.Bydefault,quick-PoEisdisabledforthe
subsystem.
ThenoformofthiscommanddisablesquickPoE.
Commandcontext
config-if
Parameters
<MODULE-ID>
SpecifiesmodulenumberforquickPoEconfiguration.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablinganddisablingquickPoE:
| switch(config)#    |            | power-over-ethernet    |                | quick-poe | 1/2      |           |
| ------------------ | ---------- | ---------------------- | -------------- | --------- | -------- | --------- |
| switch(config)#    |            | no power-over-ethernet |                | quick-poe | 1/1      |           |
| switch(config-if)# |            | power-over-ethernet    |                | quick-poe | 1/1      |           |
| PoE must           | be enabled | on                     | all interfaces | before    | enabling | Quick PoE |
| switch(config-if)# |            | power-over-ethernet    |                | quick-poe | 1/3      |           |
All interfaces must use the default assigned class before enabling Quick PoE
| power-over-ethernet |     |     | threshold |     |     |     |
| ------------------- | --- | --- | --------- | --- | --- | --- |
Syntax
| power-over-ethernet    |     | threshold | <PERCENTAGE> |     |     |     |
| ---------------------- | --- | --------- | ------------ | --- | --- | --- |
| no power-over-ethernet |     | threshold | <PERCENTAGE> |     |     |     |
Description
Setsthethresholdatwhichthesystemwillsendanexcesspowerconsumptionnotificationtrap.Default
valueis80percentage.
Thenoformofthiscommandresetstheactiontodefault.
Commandcontext
Power-over-Ethernet|136

config
Parameters
<PERCENTAGE>
Excesspowerconsumptiontrapthreshold.Range1-99.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingthepower-over-ethernetthreshold:
| switch(config)# | power-over-ethernet | threshold | 75  |
| --------------- | ------------------- | --------- | --- |
Resettingthepower-over-ethernetthresholdtodefault:
| switch(config-if)# | no power-over-ethernet | threshold | 75  |
| ------------------ | ---------------------- | --------- | --- |
power-over-ethernet priority
Syntax
| power-over-ethernet    | trap |     |     |
| ---------------------- | ---- | --- | --- |
| no power-over-ethernet | trap |     |     |
Description
Thiscommandenables/disablestheSNMPtrapgenerationforPoErelatedeventsatsystemlevel.PoEtrap
generationisenabledbydefault.
ThenoformofthiscommandresetstheprioritytodefaultPoEpriority"low".
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingSNMPtrapgenerationforPoE:
| switch(config)# | power-over-ethernet | trap |     |
| --------------- | ------------------- | ---- | --- |
DisablingSNMPtrapgenerationforPoE:
| switch(config-if)# | no power-over-ethernet | trap |     |
| ------------------ | ---------------------- | ---- | --- |
| show lldp local    |                        |      |     |
Syntax
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 137

| show lldp | local-device |     | [<INTERFACE-ID>] |     |
| --------- | ------------ | --- | ---------------- | --- |
Description
DisplaysinformationadvertisedbytheswitchiftheLLDPfeatureisenabledbyuser.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingLLDPlocaldevice:
| switch# | show | lldp | local-device | 1/1/10 |
| ------- | ---- | ---- | ------------ | ------ |
| Local   | Port | Data |              |        |
===============
| Port-ID   |                  |          | : 1/1/10   |       |
| --------- | ---------------- | -------- | ---------- | ----- |
| Port-Desc |                  |          | : "1/1/10" |       |
| Port      | VLAN             | ID       | : 0        |       |
| PoE       | Plus Information |          |            |       |
| PoE       | Device           | Type     | : Type     | 2 PSE |
| Power     | Source           |          | : Primary  |       |
| Power     | Priority         |          | : low      |       |
| PSE       | Allocated        | Power:   | 25.0       | W     |
| PD        | Requested        | Power    | : 25.0     | W     |
| show      | lldp             | neighbor |            |       |
Syntax
| show lldp | neighbor | [<INTERFACE-ID>] |     |     |
| --------- | -------- | ---------------- | --- | --- |
Description
Displaysdetailedinformationaboutaparticularneighborconnectedtoaparticularinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-ID>
Specifiesaninterface.Format:member/slot/port
Authority
Power-over-Ethernet|138

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingLLDPneighborinformationwhenthereisonlyoneneighbor:
| switch# show          | lldp     | neighbor-info | 1/1/10              |     |
| --------------------- | -------- | ------------- | ------------------- | --- |
| Port                  |          |               | : 1/1/10            |     |
| Neighbor Entries      |          |               | : 1                 |     |
| Neighbor Entries      | Deleted  |               | : 0                 |     |
| Neighbor Entries      | Dropped  |               | : 0                 |     |
| Neighbor Entries      | Aged-Out |               | : 0                 |     |
| Neighbor Chassis-Name |          |               | : 84:d4:7e:ce:5d:68 |     |
Neighbor Chassis-Description : ArubaOS (MODEL: 325), Version Aruba IAP
| Neighbor Chassis-ID         |             |           | : 84:d4:7e:ce:5d:68 |      |
| --------------------------- | ----------- | --------- | ------------------- | ---- |
| Neighbor Management-Address |             |           | : 169.254.41.250    |      |
| Chassis Capabilities        |             | Available | : Bridge,           | WLAN |
| Chassis Capabilities        |             | Enabled   | :                   |      |
| Neighbor Port-ID            |             |           | : 84:d4:7e:ce:5d:68 |      |
| Neighbor Port-Desc          |             |           | : eth0              |      |
| TTL                         |             |           | : 120               |      |
| Neighbor Port               | VLAN        | ID        | :                   |      |
| Neighbor PoEplus            | information |           | : DOT3              |      |
| Neighbor Device             | Type        |           | : TYPE2             | PD   |
| Neighbor Power              | Priority    |           | : Unkown            |      |
| Neighbor Power              | Source      |           | : Primary           |      |
| Neighbor Power              | Requested   |           | : 25.0              | W    |
| Neighbor Power              | Allocated   |           | : 0.0 W             |      |
| Neighbor Power              | Supported   |           | : No                |      |
| Neighbor Power              | Enabled     |           | : No                |      |
| Neighbor Power              | Class       |           | : 5                 |      |
| Neighbor Power              | Paircontrol |           | : No                |      |
| Neighbor Power              | Pairs       |           | : SIGNAL            |      |
show power-over-ethernet
Syntax
6300SwitchSeries:
| show power-over-ethernet |     | [member | <MEMBER-ID>] | [brief] |
| ------------------------ | --- | ------- | ------------ | ------- |
6400SwitchSeries:
| show power-over-ethernet |     | [<MODULE-ID>] | [brief] |     |
| ------------------------ | --- | ------------- | ------- | --- |
6300,6400SwitchSeries:
| show power-over-ethernet |     | [<IFRANGE> | [brief] |     |
| ------------------------ | --- | ---------- | ------- | --- |
Description
Displaysthestatusinformationofthefullsystem.Displaysthebriefstatusofallportorgivenportif
parameterbriefisused.Displaysthedetailedstatusofgivenport.
Commandcontext
Operator(>)orManager(#)
Parameters
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 139

<MEMBER-ID>
Displaysthedetailedstatusofgivenmember.
<MODULE-ID>
Displaysdetailedstatusforthegivenmodule.
<IFRANGE>
Portidentifierrange.
<IFNAME>
Displaythedetailedstatusofgivenport.
brief
Displaythebriefstatusofallportsorthegivenport.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showingsampleoutputforshowpower-over-ethernetonstandaloneboxwithVSFcapabiity:
| switch# show     | power-over-ethernet |                 |     |
| ---------------- | ------------------- | --------------- | --- |
| System Power     | Status for          | member 1        |     |
| Configured       | Power Status        | : No redundancy |     |
| Operational      | Power Status        | : No redundancy |     |
| Total Available  | Power               | : 740 W         |     |
| Total Failover   | Pwr                 | Avl : 0 W       |     |
| Total Redundancy | Power               | : 0 W           |     |
| Total Power      | Drawn               | : 0 W +/-       | 6W  |
| Total Power      | Reserved            | : 0 W           |     |
| Total Remaining  | Power               | : 740 W         |     |
| Trap Threshold   |                     | : 80 %          |     |
| Trap Enabled     |                     | : Yes           |     |
| Always-on        | PoE Enabled         | : 1/1           |     |
| Quick PoE        | Enabled             | : None          |     |
| Internal         | Power               |                 |     |
Total Power
| PS (Watts)          |              | Status                |     |
| ------------------- | ------------ | --------------------- | --- |
| ----- ------------- |              | --------------------- |     |
| 1 0                 |              | Absent                |     |
| 2 740               |              | Ok                    |     |
| System Power        | Status for   | member 2              |     |
| Configured          | Power Status | : No redundancy       |     |
| Operational         | Power Status | : No redundancy       |     |
| Total Available     | Power        | : 600 W               |     |
| Total Failover      | Pwr          | Avl : 0 W             |     |
| Total Redundancy    | Power        | : 0 W                 |     |
| Total Power         | Drawn        | : 0 W +/-             | 6W  |
| Total Power         | Reserved     | : 0 W                 |     |
| Total Remaining     | Power        | : 600 W               |     |
| Trap Threshold      |              | : 80 %                |     |
| Trap Enabled        |              | : Yes                 |     |
| Always-on           | PoE Enabled  | : None                |     |
| Quick PoE           | Enabled      | : None                |     |
Power-over-Ethernet|140

| Internal | Power |     |     |     |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
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
| switch#    | show power-over-ethernet |              |             | brief |     |            |          |     |     |
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
| 1/1/4      | No Low  |              | On        | Usage | 0.0 | W 0.0      | W Disabled | None N/A | N/A |
| ---------- | ------- | ------------ | --------- | ----- | --- | ---------- | ---------- | -------- | --- |
| Member     | 2 Power | Status       |           |       |     |            |            |          |     |
| Available: |         | 600 W        | Reserved: | 0.00  | W   | Remaining: | 600 W      |          |     |
| Always-on  |         | PoE Enabled: |           | None  |     |            |            |          |     |
| Quick      | PoE     | Enabled:     | None      |       |     |            |            |          |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 141

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
switch#
|            | show power-over-ethernet |             |                 | brief |              |          |     |     |
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
| switch#    | show power-over-ethernet |             |       | 1/1/1-1/1/2 | brief            |          |     |     |
| ---------- | ------------------------ | ----------- | ----- | ----------- | ---------------- | -------- | --- | --- |
| Status and | Configuration            | Information |       | for         | port 1/1/1-1/1/2 |          |     |     |
| Member     | 1Power Status            |             |       |             |                  |          |     |     |
| Available: | 370 W                    | Reserved:   | 55.60 |             | W Remaining:     | 314.40 W |     |     |
| Always-on  | PoE Enabled:             |             | 1/1   |             |                  |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
Power-over-Ethernet|142

------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes Low | Off | Class 0.0 W 0.0 | W Denied | None 4 | 2   |
| ----- | ------- | --- | --------------- | -------- | ------ | --- |
1/1/2 Yes Critical Off Usage 1.6 W 1.5 W Delivering* Single 0 1
Showingsampleoutputforpower-over-ethernetforamissinglinecard:
| switch# | show power-over-ethernet |          | 1/3 brief |     |     |     |
| ------- | ------------------------ | -------- | --------- | --- | --- | --- |
| Module  | 1/3 is not physically    | present. |           |     |     |     |
Showingsampleoutputforpower-over-ethernetbriefforamissingmember:
switch#
|        | show power-over-ethernet |          | member 3 brief |     |     |     |
| ------ | ------------------------ | -------- | -------------- | --- | --- | --- |
| Member | 3 is not physically      | present. |                |     |     |     |
Showingsampleoutputforpower-over-ethernetportwhenphysicalinterfaceisnotpresent:
| switch#   | show power-over-ethernet |          | 2/1/1 |     |     |     |
| --------- | ------------------------ | -------- | ----- | --- | --- | --- |
| Interface | 2/1/1 is not             | present. |       |     |     |     |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 143

Chapter 12
Aruba AirWave
| Aruba | AirWave |     |     |
| ----- | ------- | --- | --- |
YoucanmanageandmonitortheAOS-CXswitchthroughArubaAirWave.Thefollowingbenefitsand
functionsinclude:
n Configuration(partialconfiguration)
n Devicetopology
Immediateandhistoricaltrendreports
n
Monitoringofthedeviceanduserconnectedtothenetwork.
n
n Networkdiscovery
n Syslogsandtrapreceiver
ForinformationaboutwhichversionsofArubaAirWavesupportAOS-CX,seetheArubaOS-CXReleaseNotes.
| SNMP | support | and | AirWave |
| ---- | ------- | --- | ------- |
ForAirWavetodiscoverandmonitortheswitch,youmust:
n EnabletheSNMPservicesontheswitch.
ConfiguretheSNMPagenttousetheSNMPversionsupportedbythemanagementstation.
n
| SNMP | on the | switch |     |
| ---- | ------ | ------ | --- |
TheswitchprovidesSNMPservicesthroughthemanagementchannelandthedatainterfaces.Functionality,
suchasdevicediscoveryfromNMS,syslogandtrapforwarding,canbeanychannelconfiguredbyyou.
AlthoughtheSNMPservercanbeenabledonbothVRFs(mgmtanddefault),onlyoneinstanceofSNMPcan
berunning.ThehighestpriorityisonthedefaultVRF.
Forexample,assumethatSNMPisfirstenabledonthemgmtVRF(snmp-server vrf mgmt).Then,SNMPis
enabledonthedefaultVRF(snmp-server vrf default)withoutdisablingSNMPonthemgmt(usingan
equivalentnoformofthecommand).Theshow running-configcommanddisplaysbothsnmp-server vrf
commands;however,theSNMPinstanceisrunningonlyonthedefaultVRF(highestpriority).
| switch#         | config         |                     |             |
| --------------- | -------------- | ------------------- | ----------- |
| switch(config)# |                | snmp-server         | vrf mgmt    |
| switch(config)# |                | snmp-server         | vrf default |
| switch(config)# |                | show running-config |             |
| Current         | configuration: |                     |             |
!
| !Version | ArubaOS-CX | Virtual.10.01. |     |
| -------- | ---------- | -------------- | --- |
| led      | locator on |                |     |
!
!
!
| snmp-server | vrf | default |     |
| ----------- | --- | ------- | --- |
| snmp-server | vrf | mgmt    |     |
!
...
144
| AOS-CX10.07MonitoringGuide| |     | (6300and6400SwitchSeries) |     |
| --------------------------- | --- | ------------------------- | --- |

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
| Configuring |     | the AOS-CX | switch | to be monitored |     | by  |
| ----------- | --- | ---------- | ------ | --------------- | --- | --- |
AirWave
Prerequisites
ArubaAirWaveisactiveonthenetwork.
Procedure
1. EnableSNMPontheArubaOS-CXswitchbyenteringthesnmp-servervrfcommand.
|     | switch(config)# | snmp-server | vrf mgmt |     |     |     |
| --- | --------------- | ----------- | -------- | --- | --- | --- |
switch(config)#
|     |     | snmp-server | vrf default |     |     |     |
| --- | --- | ----------- | ----------- | --- | --- | --- |
2. ConfiguretheSNMPv2Ccommunitytopublicbyenteringthesnmp-server community public
command.Inthisinstance,publicisaread-onlycommunitystring.
|     | switch(config)# | snmp-server | community | public |     |     |
| --- | --------------- | ----------- | --------- | ------ | --- | --- |
3. Thecommunity-stringisusedbySNMPv1andSNMPv2Cforunencryptedauthentication.SNMPv3
letsyouencrypttheauthenticationmechanism.ToenableSNMPv3,enterthesnmpv3 userand
ArubaAirWave|145

|     | snmpv3 | contextcommands. |     |        |      |            |     |           |            |
| --- | ------ | ---------------- | --- | ------ | ---- | ---------- | --- | --------- | ---------- |
|     |        | switch(config)#  |     | snmpv3 | user | Admin auth | sha | auth-pass | ciphertext |
AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=
|     |     | priv des | priv-pass | ciphertext |     |     |     |     |     |
| --- | --- | -------- | --------- | ---------- | --- | --- | --- | --- | --- |
AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=
|     |     | switch(config)# |     | snmpv3 | context | Admin |     |     |     |
| --- | --- | --------------- | --- | ------ | ------- | ----- | --- | --- | --- |
FordiscoveringdevicesinAirWavethroughtheSNMPv3community,theSNMPv3contextnameis
notmandatory.DevicescanstillbediscoveredinArubaAirWavewithouttheSNMPv3contextname.
4. Enterthelogging commandforenablingsyslogforwardingtoaremotesyslogserver,suchas
AirWave:
|     |     | switch(config)# |     | logging | 10.0.10.2 | severity |     | debug |     |
| --- | --- | --------------- | --- | ------- | --------- | -------- | --- | ----- | --- |
5. SNMPtrapsenableanagenttonotifythemanagementstationofsignificanteventsbywayofan
unsolicitedSNMPmessage.EnableSNMPtrapsbyenteringthesnmp-server hostcommand:
switch(config)# snmp-server host 10.10.10.10 trap version v2c vrf default
SNMPtrapscannotbeforwardedfromAOS-CX10.00switchesthathavetheVRFconfiguredasmgmt.
LaterversionsofAOS-CXsupportSNMPtrapforwardingevenwhentheVRFisconfiguredasdefault
ormgmt.
6. ForinformationonhowtoaddadeviceformonitoringintheArubaAirWaveuserinterface,seethe
documentationforArubaAirWave.
logging
Syntax
| logging |                            | {<IPV4-ADDR>  | | <IPV6-ADDR> |                  | |            | <HOSTNAME>} |                  |             |     |
| ------- | -------------------------- | ------------- | ------------- | ---------------- | ------------ | ----------- | ---------------- | ----------- | --- |
|         | [udp                       | [<PORT-NUM>]  | |             | tcp [<PORT-NUM>] |              | | tls       | [<PORT-NUM>]]    |             |     |
|         | [include-auditable-events] |               |               |                  | [severity    | <LEVEL>]    | [vrf             | <VRF-NAME>] |     |
| logging |                            | {<IPV4-ADDR>  | | <IPV6-ADDR> |                  | |            | <HOSTNAME>} |                  |             |     |
|         | [tls                       | [<PORT-NUM>]] | [auth-mode    |                  | {certificate |             | | subject-name}] |             |     |
[legay-tls-renegotiation] [include-auditable-events] [severity <LEVEL>]
|     | [vrf    | <VRF-NAME>]  |     |             |     |              |     |     |     |
| --- | ------- | ------------ | --- | ----------- | --- | ------------ | --- | --- | --- |
| no  | logging | {<IPV4-ADDR> | |   | <IPV6-ADDR> |     | | <HOSTNAME> |     |     |     |
Description
Enablessyslogforwardingtoaremotesyslogserver.
Thenoformofthiscommanddisablessyslogforwardingtoaremotesyslogserver.
Commandcontext
config
Parameters
| {<IPV4-ADDR> |     | | <IPV6-ADDR> |     | | <HOSTNAME>} |     |     |     |     |     |
| ------------ | --- | ------------- | --- | ------------- | --- | --- | --- | --- | --- |
SelectstheIPv4address,IPv6address,orhostnameoftheremotesyslogserver.Required.
| [udp | [<PORT-NUM>] |     | | tcp [<PORT-NUM>]] |     |     |     |     |     |     |
| ---- | ------------ | --- | ------------------- | --- | --- | --- | --- | --- | --- |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 146

Specifies the UDP port or TCP port of the remote syslog server to receive the forwarded syslog
messages.
udp [<PORT-NUM>]

Range: 1 to 65535. Default: 514

tcp [<PORT-NUM>]

Range: 1 to 65535. Default: 1470

tls [<PORT-NUM>]

Range: 1 to 65535. Default: 6514

include-auditable-events

Specifies that auditable messages are also logged to the remote syslog server.

severity <LEVEL>

Specifies the severity of the syslog messages:

n alert: Forwards syslog messages with the severity of alert (6) and emergency (7).

n crit: Forwards syslog messages with the severity of critical (5) and above.

n debug: Forwards syslog messages with the severity of debug (0) and above.

n emerg: Forwards syslog messages with the severity of emergency (7) only.

n err: Forwards syslog messages with the severity of err (4) and above

n info: Forwards syslog messages with the severity of info (1) and above. Default.

n notice: Forwards syslog messages with the severity of notice (2) and above.

n warning: Forwards syslog messages with the severity of warning (3) and above.

auth-mode

Specifies the TLS authentication mode used to validate the certificate.

n certificate: Validates the peer using trust anchor certificate based authentication. Default.

n subject-name: Validates the peer using trust anchor certificates as well as subject-name based

authentication.

legacy-tls-renegotiation

Enables the TLS connection with a remote syslog server supporting legacy renegotiation.

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

Aruba AirWave | 147

| switch(config)# |     | no  | logging |     |     |     |
| --------------- | --- | --- | ------- | --- | --- | --- |
EnablingsyslogforwardingoverTLStoaremotesyslogserverusingsubject-nameauthenticationmode:
| switch(config)# |     | logging   | example.com |     | tls auth-mode | subject name |
| --------------- | --- | --------- | ----------- | --- | ------------- | ------------ |
| snmp-server     |     | community |             |     |               |              |
Syntax
| snmp-server    | community |     | <STRING> |     |     |     |
| -------------- | --------- | --- | -------- | --- | --- | --- |
| no snmp-server | community |     | <STRING> |     |     |     |
Description
AddsanSNMPv1/SNMPv2ccommunitystring.Acommunitystringisapasswordthatcontrolsreadaccess
totheSNMPagent.AnetworkmanagementprogrammustsupplythisnamewhenattemptingtogetSNMP
informationfromtheswitch.Amaximumof10communitystringsaresupported.Onceyoucreateyour
owncommunitystring,thedefaultcommunitystring(public)isdeleted.
ThenoformofthiscommandremovesthespecifiedSNMPv1/SNMPv2ccommunitystring.Whenno
communitystringexists,adefaultcommunitystringwiththevaluepublicisautomaticallydefined.
Commandcontext
config
Parameters
<STRING>
SpecifiestheSNMPv1/SNMPv2ccommunitystring.Range:1to32printableASCIIcharacters,excluding
spaceandquestionmark.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingtheSNMPv1/SNMPv2ccommunitystringtoprivate:
| switch(config)# |     | snmp-server |     | community | private |     |
| --------------- | --- | ----------- | --- | --------- | ------- | --- |
RemovingSNMPv1/SNMPv2ccommunitystringprivate:
switch(config)#
|             |     | no   | snmp-server | community | private |     |
| ----------- | --- | ---- | ----------- | --------- | ------- | --- |
| snmp-server |     | host |             |           |         |     |
Syntax
snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>]
| [port <UDP-PORT>] |     | [vrf | <VRF-NAME>] |     |     |     |
| ----------------- | --- | ---- | ----------- | --- | --- | --- |
no snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>]
| [port <UDP-PORT>] |     | [vrf | <VRF-NAME>] |     |     |     |
| ----------------- | --- | ---- | ----------- | --- | --- | --- |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 148

snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]
| [port <UDP-PORT>] | [vrf <VRF-NAME>] |     |     |     |     |
| ----------------- | ---------------- | --- | --- | --- | --- |
no snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]
| [port <UDP-PORT>] | [vrf <VRF-NAME>] |     |     |     |     |
| ----------------- | ---------------- | --- | --- | --- | --- |
snmp-server host <IPv4-ADDR> [trap version v3 | inform version v3] user <NAME>
| [port <UDP-PORT>] | [vrf <VRF-NAME>] |     |     |     |     |
| ----------------- | ---------------- | --- | --- | --- | --- |
no snmp-server host <IPv4-ADDR> [trap version v3 | inform version v3] user <NAME>
| [port <UDP-PORT>] | [vrf <VRF-NAME>] |     |     |     |     |
| ----------------- | ---------------- | --- | --- | --- | --- |
Description
Configuresatrap/informsreceivertowhichtheSNMPagentcansendSNMPv1/v2c/v3trapsorv2c
informs.Amaximumof30SNMPtraps/informsreceiverscanbeconfigured.
Thenoformofthiscommandremovesthespecifiedtrap/informreceiver.
| Configuringsnmpv3 | informsisnotsupported. |     |     |     |     |
| ----------------- | ---------------------- | --- | --- | --- | --- |
Commandcontext
config
Parameters
<IPv4-ADDR>
SpecifiestheIPaddressofatrapreceiverinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0
to255.Youcanremoveleadingzeros.Forexample,theaddress192.169.005.100becomes
192.168.5.100.
| trap version <VERSION> |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- |
SpecifiesthetrapnotificationtypeforSNMPv1orv2c.Availableoptionsare:v1orv2c.
| inform version v2c |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- |
SpecifiestheinformnotificationtypeforSNMPv2c.
| trap version v3 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
SpecifiesthetrapnotificationtypeforSNMPv3.
user <NAME>
SpecifiestheSNMPv3usernametobeusedintheSNMPtrapnotifications.
community <STRING>
Specifiesthenameofthecommunitystringtousewhensendingtrapnotifications.Range:1-32
printableASCIIcharacters,excludingspaceandquestionmark.Default:public.
<UDP-PORT>
SpecifiestheUDPportonwhichnotificationsaresent.Range:1-65535.Default:162.
vrf <VRF-NAME>
SpecifiesthenameoftheVRFonwhichtosendthenotifications.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| switch(config)# | snmp-server    | host 10.10.10.10 | trap version | v1  |     |
| --------------- | -------------- | ---------------- | ------------ | --- | --- |
| switch(config)# | no snmp-server | host 10.10.10.10 | trap version | v1  |     |
switch(config)#
|     | snmp-server | host 10.10.10.10 | trap version | v2c community | public |
| --- | ----------- | ---------------- | ------------ | ------------- | ------ |
ArubaAirWave|149

switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
switch(config)#
snmp-server host 10.10.10.10 trap version v2c community public port
5000
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
port 5000
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public port
| 5000 vrf default |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
| port 5000 vrf | default |     |     |     |     |
| ------------- | ------- | --- | --- | --- | --- |
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public
switch(config)#
|     | snmp-server | host 10.10.10.10 | inform version | v2c community | public |
| --- | ----------- | ---------------- | -------------- | ------------- | ------ |
port 5000
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public
port 5000
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
| port 5000 vrf | default |     |     |     |     |
| ------------- | ------- | --- | --- | --- | --- |
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public
| port 5000 vrf | default |     |     |     |     |
| ------------- | ------- | --- | --- | --- | --- |
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)#
|     | no snmp-server | host 10.10.10.10 | trap version | v3 user Admin |     |
| --- | -------------- | ---------------- | ------------ | ------------- | --- |
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin port 2000
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin port 2000
| snmp-server | vrf |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- |
Syntax
| snmp-server vrf    | <VRF-NAME> |     |     |     |     |
| ------------------ | ---------- | --- | --- | --- | --- |
| no snmp-server vrf | <VRF-NAME> |     |     |     |     |
Description
ConfigurestheVRFonwhichtheSNMPagentlistensforincomingrequests.Bydefault,theSNMPagent
doesnotlistenonanyVRF.
ThenoformofthiscommandstopstheSNMPagentfromlisteningforincomingrequestsonthespecified
VRF.
Commandcontext
config
Parameters
<VRF-NAME>
SpecifiestheVRFonwhichtheSNMPagentlistensforincomingrequests.TheSNMPagentcanlistenon
eitherthemgmtordefaultVRF.Ifconfiguredforboth,theSNMPagentlistensondefault,whichhasa
higherpriority.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config)# | snmp-server | vrf default |     |     |     |
| --------------- | ----------- | ----------- | --- | --- | --- |
AOS-CX10.07MonitoringGuide|(6300and6400SwitchSeries) 150

| switch(config)# |         | no  | snmp-server | vrf default |     |
| --------------- | ------- | --- | ----------- | ----------- | --- |
| snmpv3          | context |     |             |             |     |
Syntax
| snmpv3    | context <NAME> | vrf    | <VRF-NAME>       | [community | <STRING>] |
| --------- | -------------- | ------ | ---------------- | ---------- | --------- |
| no snmpv3 | context        | <NAME> | [vrf <VRF-NAME>] |            |           |
Description
CreatesanSNMPv3contextonthespecifiedVRF.
ThenoformofthiscommandremovesthespecifiedSNMPcontext.
Commandcontext
config
Parameters
<NAME>
Specifiesthenameofthecontext.Range:1to32printableASCIIcharacters,excludingspaceand
questionmark(?).
vrf <VRF-NAME>
SpecifiestheVRFassociatedwiththecontext.Default:default.
| community | <STRING> |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
SpecifiestheSNMPcommunitystringassociatedwiththecontext.Range:1to32printableASCII
characters,excludingspaceandquestionmark.Default:public.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreatinganSNMPv3contextnamednewContext:
| switch(config)# |     | snmpv3 | context | newContext |     |
| --------------- | --- | ------ | ------- | ---------- | --- |
CreatinganSNMPv3contextnamednewContextonVRFmyVrfandwithcommunitystringprivate.
switch(config)# snmpv3 context newContext vrf myVrf community private
RemovingtheSNMPv3contextnamednewContextonVRFmyVrf:
| switch(config)# |      | no  | snmpv3 context | newContext | vrf myVrf |
| --------------- | ---- | --- | -------------- | ---------- | --------- |
| snmpv3          | user |     |                |            |           |
Syntax
snmpv3 user <NAME> [auth <AUTH-PROTOCOL> auth-pass {plaintext | ciphertext}
<AUTH-PWORD> [priv <PRIV-PROTOCOL> priv-pass {plaintext | ciphertext} <PRIV-PWORD>] ]
ArubaAirWave|151

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

auth-pass {plaintext | ciphertext} <AUTH-PWORD>

Specifies the SNMPv3 user password. Range for plaintext is 8 - 32 printable ASCII characters, excluding
space and question mark.

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

Defining an SNMPv3 user named Admin using sha authentication with the plaintext password
mypassword and using des security with the plaintext password myprivpass:

switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des
priv-pass plaintext myprivpass

Removing an SNMPv3 user named Admin:

switch(config)# no snmpv3 user Admin

Defining an SNMPv3 user named Admin using sha authentication with the plaintext password
mypassword and using des security with the plaintext password myprivpass:

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

152

switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des
| priv-pass | plaintext | myprivpass |     |     |     |     |
| --------- | --------- | ---------- | --- | --- | --- | --- |
CopyinganSNMPuserfromswitch1toswitch2.
Onswitch1,configureausercalledAdmin,thenissuetheshow running-configcommandtodisplay
switchconfigurationsettings.Thesnmpv3usercommandusestheciphertextoptiontoprotectthe
users'spasswords.
switch1(config)#
|                  |                     | snmpv3 user | Admin auth | sha auth-pass | plaintext | mypassword |
| ---------------- | ------------------- | ----------- | ---------- | ------------- | --------- | ---------- |
| priv des         | priv-pass           | plaintext   | myprivpass |               |           |            |
| switch1(config)# |                     | exit        |            |               |           |            |
| switch1#         | show running-config |             |            |               |           |            |
| Current          | configuration:      |             |            |               |           |            |
!
| !Version | ArubaOS-CX | TL.10.00.0003-8017-gdeb0606~dirty |     |     |     |     |
| -------- | ---------- | --------------------------------- | --- | --- | --- | --- |
!
!
!
| snmpv3 | user Admin | auth sha | auth-pass | ciphertext |     |     |
| ------ | ---------- | -------- | --------- | ---------- | --- | --- |
AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=
| priv des | priv-pass | ciphertext |     |     |     |     |
| -------- | --------- | ---------- | --- | --- | --- | --- |
AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=
| ssh server | vrf mgmt |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- |
!
!
!
!
| interface | mgmt |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
no shutdown
ip dhcp
vlan 1
Onswitch2,executethesnmpv3usercommandthatwasdisplayedbyshow running-configonswitch1.
Thiscreatestheuseronswitch2withthesameconfigurationsettings.
| switch1(config)# |     | snmpv3 user | Admin auth | sha auth-pass |     |     |
| ---------------- | --- | ----------- | ---------- | ------------- | --- | --- |
ciphertextAQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=priv
| des priv-pass | ciphertext |     |     |     |     |     |
| ------------- | ---------- | --- | --- | --- | --- | --- |
AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=
ArubaAirWave|153

Chapter 13

Support and other resources

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

Airheads social forums and Knowledge
Base

https://community.arubanetworks.com/

Software licensing

https://lms.arubanetworks.com/

End-of-Life information

https://www.arubanetworks.com/support-services/end-of-life/

Aruba software and documentation

https://asp.arubanetworks.com/downloads

Accessing updates
You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

AOS-CX 10.07 Monitoring Guide | (6300 and 6400 Switch Series)

154

https://asp.arubanetworks.com/downloads

If you are unable to find your product in the Aruba Support Portal, you may need to search My Networking,
where older networking products can be found:

My Networking

https://www.hpe.com/networking/support

To view and update your entitlements, and to link your contracts and warranties with your profile, go to the
Hewlett Packard Enterprise Support Center More Information on Access to Support Materials page:

https://support.hpe.com/portal/site/hpsc/aae/home/

Access to some updates might require product entitlement when accessed through the Hewlett Packard
Enterprise Support Center. You must have an HP Passport set up with relevant entitlements.

Some software products provide a mechanism for accessing software updates through the product
interface. Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://asp.arubanetworks.com/notifications/subscriptions (requires an active Aruba Support Portal (ASP)
account to manage subscriptions). Security notices are viewable without an ASP account.

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

Support and other resources | 155