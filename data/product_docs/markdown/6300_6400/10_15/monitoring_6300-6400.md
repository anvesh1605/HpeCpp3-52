AOS-CX 10.15.xxxx
Monitoring Guide

6300, 6400 Switch Series

Published: March 2025

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

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

3

Contents
| About                                                   | this document |         |                    | 8   |
| ------------------------------------------------------- | ------------- | ------- | ------------------ | --- |
| Applicableproducts                                      |               |         |                    | 8   |
| Latestversionavailableonline                            |               |         |                    | 8   |
| Commandsyntaxnotationconventions                        |               |         |                    | 8   |
| Abouttheexamples                                        |               |         |                    | 9   |
| Identifyingswitchportsandinterfaces                     |               |         |                    | 9   |
| Identifyingmodularswitchcomponents                      |               |         |                    | 10  |
| Monitoring                                              | hardware      | through | visual observation | 11  |
| ConfirmingnormaloperationoftheswitchbyreadingLEDs       |               |         |                    | 11  |
| Detectingiftheswitchisnotreadyforafailoverevent         |               |         |                    | 12  |
| FindingfaultedcomponentsusingtheswitchLEDs              |               |         |                    | 12  |
| IP Flow                                                 | Information   | Export  |                    | 14  |
| CompatibilitywithTrafficInsight                         |               |         |                    | 14  |
| CompatibilitywithApplicationRecognition                 |               |         |                    | 14  |
| InformationElements                                     |               |         |                    | 14  |
| Flowmonitors                                            |               |         |                    | 15  |
| FlowRecords                                             |               |         |                    | 16  |
| FlowExporters                                           |               |         |                    | 16  |
| Destinations                                            |               |         |                    | 16  |
| ConfiguringIPFlowInformationExporton6300and6400Switches |               |         |                    | 17  |
| Stepone:CreateFlowRecords                               |               |         |                    | 17  |
| Steptwo:Configureflowexporter(s)                        |               |         |                    | 18  |
| Stepthree:Configurethemonitor(s)                        |               |         |                    | 20  |
Stepfour:(Optional)EnableApplicationRecognitionandapplyaflowmonitortointerfaces 20
| Role-basedIPFIX                        |                                         |     |     | 21  |
| -------------------------------------- | --------------------------------------- | --- | --- | --- |
| FAQsandTroubleshooting                 |                                         |     |     | 22  |
| Flowmonitoringcommands                 |                                         |     |     | 23  |
|                                        | collectapplicationtcpestablishment-time |     |     | 23  |
|                                        | diag-dumpipfixbasic                     |     |     | 23  |
|                                        | flowexporter                            |     |     | 25  |
|                                        | flowmonitor                             |     |     | 28  |
|                                        | flowrecord                              |     |     | 30  |
|                                        | flow-tracking                           |     |     | 34  |
|                                        | ip|ipv6flowmonitor(interface)           |     |     | 36  |
|                                        | ipv4|ipv6flowmonitor(role)              |     |     | 37  |
|                                        | showflowexporter                        |     |     | 38  |
|                                        | showflowmonitor                         |     |     | 40  |
|                                        | showflowrecord                          |     |     | 44  |
|                                        | showflow-tracking                       |     |     | 46  |
|                                        | showtechipfix                           |     |     | 48  |
| Boot                                   | commands                                |     |     | 50  |
| bootfabric-module                      |                                         |     |     | 50  |
| bootline-module                        |                                         |     |     | 51  |
| bootmanagement-module                  |                                         |     |     | 52  |
| bootmanagement-module(recoveryconsole) |                                         |     |     | 53  |
| bootset-default                        |                                         |     |     | 55  |
5
AOS-CX10.15.xxxxMonitoringGuide| (6300,6400SwitchSeries)

| bootsystem                             |                                    | 55  |
| -------------------------------------- | ---------------------------------- | --- |
| showboot-history                       |                                    | 57  |
| External                               | storage                            | 63  |
| Externalstoragecommands                |                                    | 63  |
|                                        | address(externalstorage)           | 63  |
|                                        | directory                          | 64  |
|                                        | disableexternal-storagelogfiles    | 65  |
|                                        | enable(external-storagelogfiles)   | 66  |
|                                        | external-storage                   | 66  |
|                                        | password(external-storage)         | 67  |
|                                        | showexternal-storage               | 68  |
|                                        | showrunning-configexternal-storage | 69  |
|                                        | type(externalstorage)              | 70  |
|                                        | username(externalstorage)          | 71  |
|                                        | vrf(externalstorage)               | 71  |
| IP-SLA                                 |                                    | 73  |
| IP-SLAguidelines                       |                                    | 73  |
| LimitationswithVoIPSLAs                |                                    | 74  |
| IP-SLAcommands                         |                                    | 74  |
|                                        | http                               | 74  |
|                                        | https                              | 75  |
|                                        | icmp-echo                          | 77  |
|                                        | ip-sla                             | 78  |
|                                        | ip-slaresponder                    | 78  |
|                                        | showip-slaresponder                | 80  |
|                                        | showip-slaresponderresults         | 81  |
|                                        | showip-sla                         | 82  |
|                                        | start-test                         | 86  |
|                                        | stop-test                          | 86  |
|                                        | tcp-connect                        | 87  |
|                                        | udp-echo                           | 88  |
|                                        | udp-jitter-voip                    | 89  |
|                                        | vrf(ipsla)                         | 90  |
| L1-100Mbps                             | downshift                          | 92  |
| Limitationswithspeeddownshift          |                                    | 92  |
| L1-100Mbpsdownshiftcommands            |                                    | 92  |
|                                        | downshiftenable                    | 92  |
|                                        | showinterface                      | 93  |
|                                        | showinterfacestatistics            | 100 |
|                                        | showinterfacedownshift-enable      | 102 |
|                                        | showrunning-configinterface        | 103 |
| Mirroring                              |                                    | 106 |
| Mirrorstatistics                       |                                    | 106 |
| Classifierpoliciesandmirroringsessions |                                    | 106 |
| VLANasasource                          |                                    | 107 |
| Mirroringcommands                      |                                    | 107 |
|                                        | clearmirror                        | 107 |
|                                        | clearmirrorendpoint                | 108 |
|                                        | comment                            | 109 |
|                                        | copytcpdump-pcap                   | 110 |
|                                        | copytshark-pcap                    | 111 |
|                                        | destinationcpu                     | 112 |
|6

|                                                  | destinationinterface              |            | 113 |
| ------------------------------------------------ | --------------------------------- | ---------- | --- |
|                                                  | destinationtunnel                 |            | 114 |
|                                                  | diagnostic                        |            | 116 |
|                                                  | diagutilitiestcpdump              |            | 116 |
|                                                  | disable(mirrorsession)            |            | 119 |
|                                                  | enable(mirrorsession)             |            | 119 |
|                                                  | mirrorsession                     |            | 120 |
|                                                  | mirrorendpoint                    |            | 121 |
|                                                  | showmirror                        |            | 122 |
|                                                  | showmirrorendpoint                |            | 124 |
|                                                  | shutdown(mirrorendpoint)          |            | 125 |
|                                                  | source                            |            | 126 |
|                                                  | sourceinterface                   |            | 127 |
|                                                  | sourcevlan                        |            | 129 |
| Monitoring                                       | a device                          | using SNMP | 132 |
| Power-over-Ethernet                              |                                   |            | 133 |
| PoEcommands                                      |                                   |            | 134 |
|                                                  | lldpdot3poe                       |            | 134 |
|                                                  | lldpmedpoe                        |            | 135 |
|                                                  | power-over-ethernet               |            | 136 |
|                                                  | power-over-ethernetallocate-by    |            | 136 |
|                                                  | power-over-ethernetalways-on      |            | 138 |
|                                                  | power-over-ethernetassigned-class |            | 139 |
|                                                  | power-over-ethernetpower-pairs    |            | 140 |
|                                                  | power-over-ethernetpre-std-detect |            | 141 |
|                                                  | power-over-ethernetpriority       |            | 142 |
|                                                  | power-over-ethernetquick-poe      |            | 143 |
|                                                  | power-over-ethernetthreshold      |            | 144 |
|                                                  | power-over-ethernettrap           |            | 144 |
|                                                  | showlldplocal                     |            | 145 |
|                                                  | showlldpneighbor                  |            | 146 |
|                                                  | showpower-over-ethernet           |            | 147 |
| Aruba                                            | AirWave                           |            | 155 |
| SNMPsupportandAirWave                            |                                   |            | 155 |
|                                                  | SNMPontheswitch                   |            | 155 |
| SupportedfeatureswithAirWaveandtheAOS-CXswitch   |                                   |            | 156 |
| ConfiguringtheAOS-CXswitchtobemonitoredbyAirWave |                                   |            | 156 |
| AirWavecommands                                  |                                   |            | 157 |
|                                                  | logging                           |            | 157 |
|                                                  | snmp-servercommunity              |            | 159 |
|                                                  | snmp-serverhost                   |            | 160 |
|                                                  | snmp-servervrf                    |            | 162 |
|                                                  | snmpv3context                     |            | 162 |
|                                                  | snmpv3user                        |            | 163 |
| Support                                          | and Other                         | Resources  | 166 |
| AccessingArubaSupport                            |                                   |            | 166 |
| AccessingUpdates                                 |                                   |            | 167 |
| WarrantyInformation                              |                                   |            | 167 |
| RegulatoryInformation                            |                                   |            | 167 |
| DocumentationFeedback                            |                                   |            | 167 |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 7

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A, S0X44A, S3L75A, S3L76A, S3L77A)

n Aruba 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B, R0X40C, R0X41A,
R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C, R0X26A, R0X27A,
JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

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

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

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
| Understanding | the CLI | prompts |     |
| ------------- | ------- | ------- | --- |
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
format:member/slot/port.
| On the Aruba | 6300 Switch | Series |     |
| ------------ | ----------- | ------ | --- |
Aboutthisdocument|9

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.
The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the Aruba 6400 and 5420 Switch Series

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

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

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

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

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

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

13

Chapter 3

IP Flow Information Export

IP Flow Information Export

IP Flow Information Export (IPFIX) is an embedded network flow analysis tool that compiles
characteristic and measured properties of flows and sends flow reports to internal or external flow
collectors. IPFIX is configurable via the command-line or REST interfaces. With IPFIX, customers configure
flow records with match (key) fields and collection (non-key) fields. Match fields are the set of fields that
define a flow, such as IP address or UDP port. Collection fields are the set of fields that identify
information to collect for a flow, such as packet and byte counters.

A flow exporter defines where and how to export flow reports. Flow exporters are created as standalone
entities in the config context to provide flow monitors the ability to export flow reports.

Compatibility with Traffic Insight

The AOS-CX traffic insight feature allows monitoring of large amount of data that it collects from various
flow exporters like IPFIX, and provides the ability to filter, aggregate, and sort the data based on user
flow monitor requests. Traffic insight tracks different monitor requests simultaneously and provides
monitor reports per request. For more information on configuring the Traffic Insight features, refer to
the AOS-CX Security Guide.

Compatibility with Application Recognition

If the application recognition feature is enabled, then the application data and the flow properties
collected by AR and IPFIX are exported to external or internal IPFIX collectors. For more information on
configuring the Application Recognition and Traffic Insight features, refer to the AOS-CX Security Guide.

Information Elements

The IPFIX Information Elements (IE) are entities that are defined and maintained by the Internet
Assigned Numbers Authority (IANA). They are characterized by a unique piece of information they can
provided about a flow. Information Elements may be either private or public. Private Information
Elements are exported with a Private Enterprise Number (PEN).

AOS-CX can act as an intermediate collecting process for flow reports from hardware to append certain
additional IPFIX information elements to the flow reports. When configured, the software will act as an
intermediate exporting process to export the augmented flow reports to any configured flow exporters.

AOS-CX supports the following standard and private information elements.

All Standard Information Element registration information can be found on the IANA website, at

https://www.iana.org/assignments/ipfix/.

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

14

Standard Information Elements

Private Information Elements

tlsClientVersion (ID 1029, 4823 Aruba)

tlsServerVersion (ID 1030, 4823 Aruba)

ja3 (ID 1031, 4823 Aruba)

ja3s (ID 1032, 4823 Aruba)

supportedNextProtocol (ID 1033, 4823 Aruba)

CertificateIssuer (ID 1034, 4823 Aruba)

CertificateIssueDate (ID 1035, 4823 Aruba)

CertificateExpiryDate (ID 1036, 4823 Aruba)

applicationType (ID 1100, 4823 Aruba)

tcp3WayHsServerRespTime (ID 1101, 4823 Aruba)

tcp3WayHsClientRespTime (ID 1102, 4823 Aruba)

octetDeltaCount

packetDeltaCount

protocolIdentifier

sourceTransportPort

sourceIPv4Address

ingressInterface

destinationTransportPort

destinationIPv4Address

sourceIPv6Address

destinationIPv6Address

classId

sourceMacAddress

vlanId

ipVersion

destinationMacAddress

applicationDescription

applicationId

applicationName

flowEndReason

flowStartMicroseconds

flowEndMicroseconds

dnsResponseCode

ingressPhysicalInterface

egressPhysicalInterface

applicationCategoryName

Flow monitors

A flow monitor is applied to an interface to perform network traffic monitoring. A flow monitor consists
of a flow record, a flow cache, and optional flow exporters. A flow record must be created and assigned

IP Flow Information Export | 15

to the flow monitor for the monitoring process to function. Flow data is compiled from the network
traffic on the interface and stored in the flow cache based on the match (key) and collect (non-key) fields
in the flow record. Data from the flow cache is exported by the flow exporters assigned to the flow
monitor. 6300 and 6400 series support a maximum of sixteen flow monitors with a limit of two flow
exporters that can be applied to a single flow monitor.

Flow Records

A flow record defines match (key) fields and collection (non-key) fields. Match fields are the set of fields
that define a flow, such as IP address or UDP port. Collection fields are the set of fields that identify
information to collect for a flow, such as packet and byte counters. On the 6200, 6300, 6400, 8100, and
8360 switch series a maximum of sixteen flow records can be created.

There are six mandatory match fields, of which the IP match fields must be of the same type (IPv4 or
IPv6).

A flow record is invalid if it does not contain one of the supported sets of match fields.

The supported sets of match fields are:

1. IPv4:

n IPv4 version

n IPV4 source address

n IPv4 destination address

n IPv4 protocol

n Transport destination port

n Transport source port

2. IPv6:

n IPv6 version

n IPv6 source address

n IPv6 destination address

n IPv6 protocol

n Transport destination port

n Transport source port

Flow Exporters

A flow exporter defines where and how to export flow reports. Flow exporters are created as
standalone entities in the config context to provide flow monitors the ability to export flow reports.
6300 and 6400 Switch series support a maximum of sixteen flow monitors with a limit of two flow
exporters that can be applied to a single flow monitor.

Destinations

The destination specifies where flow reports are sent. There are two possible types of destination for a
flow exporter:

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

16

1. (default)HostnameorIPaddressofadevicewithanoptionalVRF
2. TrafficInsightinstance
Aflowexportercanonlysendflowreportstoonedestination.Thedestinationtypespecifieswhich
destinationtouse.Ifnodestinationtypeisspecified,thedefaultdestinationtypeisthehostnameorIP
addressofadevicewithanoptionalVRF.(IfaVRFisnotspecified,thedefaultVRFwillbeused.)A
destinationofeachtypecanbeconfigured,butonlytheonecorrespondingtothedestinationtypeis
used.Ifthereisnodestinationcorrespondingtothedestinationtype,thentheflowexporter
configurationisincomplete.Ifanewdestinationofaparticulartypeisconfigured,itwillreplacethe
destinationofthattypethatwaspreviouslyconfigured.
| Configuring | IP  | Flow | Information |     | Export |     | on 6300 | and 6400 |
| ----------- | --- | ---- | ----------- | --- | ------ | --- | ------- | -------- |
Switches
ThefollowinglistdescribesthestepsrequiredtoconfigureaIP flowinformationexport(IPFIX)solution:
n Stepone:Createflowrecords
n Steptwo:Configureflowexporter(s)
Stepthree:Configuremonitor(s)
n
n Stepfour:Applyaflowmonitorstointerface(s)
IPv6relatedcommandsareonlyapplicabletoswitchesthatsupportIPv6protocol.
| Step one: | Create | Flow | Records |     |     |     |     |     |
| --------- | ------ | ---- | ------- | --- | --- | --- | --- | --- |
FlowRecordsareusedtodefinethedatathatwillbeaddedtotheIPFIXtemplate.Thisexample
configuresonerecordforIPv4andoneforIPv6.
| switch(config)#             | flow | record | flowRecordv4    |             |             |         |       |     |
| --------------------------- | ---- | ------ | --------------- | ----------- | ----------- | ------- | ----- | --- |
| switch(config-flow-record)# |      |        | match ip        | protocol    |             |         |       |     |
| switch(config-flow-record)# |      |        | match ip        | source      | address     |         |       |     |
| switch(config-flow-record)# |      |        | match ip        | destination |             | address |       |     |
| switch(config-flow-record)# |      |        | match ip        | version     |             |         |       |     |
| switch(config-flow-record)# |      |        | match transport |             | destination |         | port  |     |
| switch(config-flow-record)# |      |        | match transport |             | source      | port    |       |     |
| switch(config-flow-record)# |      |        | collect         | counter     | bytes       |         |       |     |
| switch(config-flow-record)# |      |        | collect         | counter     | packets     |         |       |     |
| switch(config-flow-record)# |      |        | collect         | application |             | name    |       |     |
| switch(config-flow-record)# |      |        | collect         | timestamp   | absolute    |         | first |     |
| switch(config-flow-record)# |      |        | collect         | timestamp   | absolute    |         | last  |     |
| switch(config-flow-record)# |      |        | collect         | application |             | https   | url   |     |
| switch(config)#             | flow | record | flowRecordv6    |             |             |         |       |     |
| switch(config-flow-record)# |      |        | match ipv6      | protocol    |             |         |       |     |
| switch(config-flow-record)# |      |        | match ipv6      | source      | address     |         |       |     |
| switch(config-flow-record)# |      |        | match ipv6      | destination |             | address |       |     |
| switch(config-flow-record)# |      |        | match ipv6      | version     |             |         |       |     |
| switch(config-flow-record)# |      |        | match transport |             | destination |         | port  |     |
| switch(config-flow-record)# |      |        | match transport |             | source      | port    |       |     |
| switch(config-flow-record)# |      |        | collect         | counter     | bytes       |         |       |     |
| switch(config-flow-record)# |      |        | collect         | counter     | packets     |         |       |     |
| switch(config-flow-record)# |      |        | collect         | application |             | name    |       |     |
IPFlowInformationExport |17

| switch(config-flow-record)# |     |     | collect timestamp   | absolute first |
| --------------------------- | --- | --- | ------------------- | -------------- |
| switch(config-flow-record)# |     |     | collect timestamp   | absolute last  |
| switch(config-flow-record)# |     |     | collect application | https url      |
switch(config-flow-record)# collect application dns response-code
| switch(config-flow-record)# |     |                                             | collect application       | tls-attributes |
| --------------------------- | --- | ------------------------------------------- | ------------------------- | -------------- |
| switch(config-flow-record)# |     |                                             | collect application       | https url"     |
| switch(config-flow-record)# |     |                                             | collect application       | type           |
| switch(config-flow-record)# |     |                                             | collect egress            | interface      |
| switch(config-flow-record)# |     |                                             | collect egress            | queue          |
| switch(config-flow-record)# |     |                                             | collect egress            | vlan           |
| switch(config-flow-record)# |     |                                             | collect forwarding-status |                |
| Next,usetheshow             |     | flow recordcommandtoverifytheconfiguration. |                           |                |
-------------------------------------------------------------
| Flow | record | 'flowRecordv4' |     |     |
| ---- | ------ | -------------- | --- | --- |
--------------------------------------------------------------------------------
| Description |                  |         | : ipv4     |     |
| ----------- | ---------------- | ------- | ---------- | --- |
| Status      |                  |         | : Accepted |     |
| Match       | Fields           |         |            |     |
|             | ipv4 destination | address |            |     |
ipv4 protocol
|     | ipv4 source | address |     |     |
| --- | ----------- | ------- | --- | --- |
ipv4 version
|         | transport   | destination | port  |     |
| ------- | ----------- | ----------- | ----- | --- |
|         | transport   | source port |       |     |
| Collect | Fields      |             |       |     |
|         | application | name        |       |     |
|         | counter     | bytes       |       |     |
|         | counter     | packets     |       |     |
|         | application | https url   |       |     |
|         | timestamp   | absolute    | first |     |
|         | timestamp   | absolute    | last  |     |
--------------------------------------------------------------------------------
| Flow | record | 'flowRecordv6' |     |     |
| ---- | ------ | -------------- | --- | --- |
--------------------------------------------------------------------------------
| Description |                  |         | : ipv6     |     |
| ----------- | ---------------- | ------- | ---------- | --- |
| Status      |                  |         | : Accepted |     |
| Match       | Fields           |         |            |     |
|             | ipv6 destination | address |            |     |
ipv6 protocol
|     | ipv6 source | address |     |     |
| --- | ----------- | ------- | --- | --- |
ipv6 version
|         | transport   | destination | port             |     |
| ------- | ----------- | ----------- | ---------------- | --- |
|         | transport   | source port |                  |     |
| Collect | Fields      |             |                  |     |
|         | application | name        |                  |     |
|         | counter     | bytes       |                  |     |
|         | counter     | packets     |                  |     |
|         | application | https url   |                  |     |
|         | timestamp   | absolute    | first            |     |
|         | timestamp   | absolute    | last             |     |
| Step    | two:        | Configure   | flow exporter(s) |     |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 18

Inthisstep,youcandefineanexportertosendtoanexternaldestinationbyhostnameorIPaddress,or
toaninternaldestinationsuchasTrafficInsight.TheexamplebelowconfiguresIPFIXtoexportdatato
anexternaladdress/hostname:
| switch(config)# | flow | exporter | flowExternal |     |     |     |     |
| --------------- | ---- | -------- | ------------ | --- | --- | --- | --- |
switch(config-flow-exporter)# destination type hostname-or-ip-addr
| switch(config-flow-exporter)# |     |     | destination |      | 11.1.1.1 |     |     |
| ----------------------------- | --- | --- | ----------- | ---- | -------- | --- | --- |
| switch(config-flow-exporter)# |     |     | show        | flow | exporter |     |     |
--------------------------------------------------------------------------------
| Flow exporter | 'flowExternal |     |     |     |     |     |     |
| ------------- | ------------- | --- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Status          |               | : Accepted |     |     |            |     |     |
| --------------- | ------------- | ---------- | --- | --- | ---------- | --- | --- |
| Export Protocol |               | : ipfix    |     |     |            |     |     |
| Destination     | Type          | : Hostname |     | or  | IP address |     |     |
| Destination     |               | : 11.1.1.1 |     |     |            |     |     |
| Transport       | Configuration |            |     |     |            |     |     |
| Protocol        |               | : udp      |     |     |            |     |     |
| Port            |               | : 4739     |     |     |            |     |     |
ToconfigureIPFIXtoexporttoTrafficInsight,firstconfigureTrafficInsight.
| switch(config)#       | traffic-insight |         |         | TI   |                   |           |     |
| --------------------- | --------------- | ------- | ------- | ---- | ----------------- | --------- | --- |
| switch(config-ti-TI)# |                 | source  | ipfix   |      |                   |           |     |
| switch(config-ti-TI)# |                 | monitor | topN    | type | topN-flows        |           |     |
| switch(config-ti-TI)# |                 | monitor | dns     | type | application-flows |           |     |
| switch(config-ti-TI)# |                 | monitor | raw-mon |      | type              | raw-flows |     |
| switch(config-ti-TI)# |                 | enable  |         |      |                   |           |     |
Next,configuretheflowexporterforTrafficInsight
| switch(config)#               | flow | exporter | flowExpTI       |     |                 |                 |     |
| ----------------------------- | ---- | -------- | --------------- | --- | --------------- | --------------- | --- |
| switch(config-flow-exporter)# |      |          | export-protocol |     |                 | ipfix           |     |
| switch(config-flow-exporter)# |      |          | destination     |     | type            | traffic-insight |     |
| switch(config-flow-exporter)# |      |          | destination     |     | traffic-insight |                 | TI  |
Youcanusetheshow flow exportercommandtoverifytheflowexporterconfigurationforTraffic
Insight
| switch(config)# | show | flow exporter |     | flowExpTI |     |     |     |
| --------------- | ---- | ------------- | --- | --------- | --- | --- | --- |
--------------------------------------------------------------------------------
| Flow exporter | 'flowExpTI' |     |     |     |     |     |     |
| ------------- | ----------- | --- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Status          |               | : Accepted |     |         |     |     |     |
| --------------- | ------------- | ---------- | --- | ------- | --- | --- | --- |
| Export Protocol |               | : ipfix    |     |         |     |     |     |
| Destination     | Type          | : Traffic  |     | Insight |     |     |     |
| Destination     |               | : TI       |     |         |     |     |     |
| Transport       | Configuration |            |     |         |     |     |     |
| Protocol        |               | : udp      |     |         |     |     |     |
| Port            |               | : 4739     |     |         |     |     |     |
Finally,usetheshow run traffic-insightcommandtoverifytheTrafficInsightconfiguration:
| switch(config)# | show | running-config |     | traffic-insight |     |     |     |
| --------------- | ---- | -------------- | --- | --------------- | --- | --- | --- |
| traffic-insight | TI   |                |     |                 |     |     |     |
IPFlowInformationExport |19

enable
| source | ipfix |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- |
!
| monitor     | topN type topN-flows           | entries | 5          |     |     |
| ----------- | ------------------------------ | ------- | ---------- | --- | --- |
| monitor     | appFlow type application-flows |         |            |     |     |
| monitor     | raw type raw-flows             |         |            |     |     |
| Step three: | Configure                      | the     | monitor(s) |     |     |
First,configureanIPv4flowmonitor.
| switch(config)#              | flow monitor           | flowMonv4 |              |     |     |
| ---------------------------- | ---------------------- | --------- | ------------ | --- | --- |
| switch(config-flow-monitor)# |                        | record    | flowRecordv4 |     |     |
| Switch                       | (config-flow-monitor)# | exporter  | flowExternal |     |     |
| switch(config-flow-monitor)# |                        | exit      |              |     |     |
Next,configureanIPv6flowmonitor.
| switch(config)#              | flow monitor | flowMonv6 |              |     |     |
| ---------------------------- | ------------ | --------- | ------------ | --- | --- |
| switch(config-flow-monitor)# |              | record    | flowRecordv6 |     |     |
| switch(config-flow-monitor)# |              | exporter  | flowExternal |     |     |
| switch(config-flow-monitor)# |              | exit      |              |     |     |
Oncebothflowmonitorsarecreated,usetheshow flow monitorcommandtoverifytheflowmonitor
configurations.
| switch(config-flow-monitor)# |     | show flow | monitor |     |     |
| ---------------------------- | --- | --------- | ------- | --- | --- |
--------------------------------------------------------------------------------
| Flow | monitor 'flowMonv4' |     |     |     |     |
| ---- | ------------------- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Status   |                | : Accepted     |     |     |     |
| -------- | -------------- | -------------- | --- | --- | --- |
| Flow     | Record         | : flowRecordv4 |     |     |     |
| Flow     | Exporter(s)    | : flowExternal |     |     |     |
| Cache    | Configuration  |                |     |     |     |
| Inactive | Timeout : 30   |                |     |     |     |
| Active   | Timeout : 1800 |                |     |     |     |
--------------------------------------------------------------------------------
| Flow | monitor 'flowMonv6' |     |     |     |     |
| ---- | ------------------- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Status     |                | : Accepted     |             |             |     |
| ---------- | -------------- | -------------- | ----------- | ----------- | --- |
| Flow       | Record         | : flowRecordv6 |             |             |     |
| Flow       | Exporter(s)    | : flowExternal |             |             |     |
| Cache      | Configuration  |                |             |             |     |
| Inactive   | Timeout : 30   |                |             |             |     |
| Active     | Timeout : 1800 |                |             |             |     |
| Step four: | (Optional)     | Enable         | Application | Recognition | and |
| apply      | a flow monitor | to interfaces  |             |             |     |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 20

EnableApplicationRecognitiononlyifyouareusingIPFIXtosendanapplicationID.Youdonotneedtoenable
ApplicationRecognitionforIPFIXtobeenabletoreportinformationtoanexternalcollectororforinternal
analyticsreports
IfyouwanttouseIPFIXtosendanapplicationIDtotheApplicationRecognitionfeature,youmustfirst
enableApplicationRecognition.
| switch(config)#                 |     | no ip source-lockdown |     | resource-extended |     |
| ------------------------------- | --- | --------------------- | --- | ----------------- | --- |
| switch(config)#                 |     | app-recognition       |     |                   |     |
| switch(config-app-recognition)# |     |                       |     | enable            |     |
| switch(config-app-recognition)# |     |                       |     | exit              |     |
Next,applyflowmonitortoIPv4andIPv6interfaces
| switch(config)#    |     | int 1/1/1-1/1/28 |              |           |     |
| ------------------ | --- | ---------------- | ------------ | --------- | --- |
| switch(config-if)# |     | app-recognition  |              | enable    |     |
| switch(config-if)# |     | ip flow          | monitor      | flowMonv4 | in  |
| switch(config-if)# |     | ipv6             | flow monitor | flowMonv6 | in  |
| switch(config-if)# |     | exit             |              |           |     |
Finally,usetheshow run interfacecommandtoverifythattheflowmonitorwasappliedtointerface.
| switch(config-if)# |       | show | run int | 1/1/1 |     |
| ------------------ | ----- | ---- | ------- | ----- | --- |
| interface          | 1/1/1 |      |         |       |     |
no shutdown
no routing
| vlan access     | 1       |           |     |     |     |
| --------------- | ------- | --------- | --- | --- | --- |
| app-recognition |         | enable    |     |     |     |
| ip flow         | monitor | flowMonv4 | in  |     |     |
| ipv6 flow       | monitor | flowMonv6 | in  |     |     |
exit
AcollectingprocessisnotconfiguredwithIPFIX.
| Role-based | IPFIX |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- |
IfIPFIXmonitoringisconfiguredonaport,anetworkadministratorwhowantstomonitortrafficfrom
clientsmustpreconfigureIPFIXmonitorbeforeonboardingtheclients.Also,ifaclientmovesfromone
porttoanother,themonitormustbereconfiguredaccordingly.Toreduceallthesecomplexities,6200,
6300and6400switchseriesallowyoutoconfigureanIPFIXmonitoronaportaccessrole.
AnIPFIXdeploymentwithmonitoringconfiguredonaportusesTCAMtogetflowstatistics.SinceTCAM
isahigh-demandresourcewhichissharedacrossmultipleprotocolsincludingthesecurityprotocols,
securitypolicyapplicationscouldfailifIPFIXconsumesmostoftheTCAMresources.Portaccessclients
canusealargeamountofofTCAMresourcesforpolicyapplications,makingitdifficultsupportport
accessclientswithTCAMbasedIPFIX.
Withrole-basedIPFIX,whenauserplugsadeviceintotoaspecificport,theiruserroleisappliedtothe
port.Whenevertheuserplugsthatdeviceintotoadifferentportagain,theroleisappliedtothat
specificport.Thisgivesmobilityandaccessibilitytotheuserandprovidespermissionsspecifictothe
user'srolewhentheuser'sdevicemovesacrossports.Role-basedIPFIXenablescolorlessportbehavior.
Therearesomemutuallyexclusivefeaturesthatwilldisablerole-basedIPFIXwhentheyareenabled.
Themutuallyexclusivefeaturesare:
IPFlowInformationExport |21

n UBT

n MAC Lockout

n Extended Router MAC

n Source Port Filter

n IP Lockdown

n L3VNI

n VSF stack

The following behaviors are observed in a deployment with role-based IPFIX:

n If a user applies the IPFIX monitor configuration on the port, it uses the existing TCAM infrastructure.

n If a port has both Role based IPFIX and Port based IPFIX, the Port based IPFIX implementation takes

the priority.

n If IPFIX monitor configuration on a port moves from role based to TCAM based or vice-versa, existing

IPFIX flows learned on that port are deleted.

n When the user role has an IPFIX configuration and fails to apply it, port access logs it, but it does not

prevent the client from getting authorized.

n If port access is in the client mode and if there is more than one client with a conflicting IPFIX monitor
configuration, traffic from all the clients will be exported through the IPFIX monitor configured for the
first client.

n Role-based IPFIX and TCAM port-based IPFIX implementations can co-exist on a switch.

n Flows from unauthorized clients are not monitored.

These are some limitations to role-based IPFIX:

n Role based IPFIX can be enabled only through port access role assignment.

n Only Ingress flow monitoring is supported on both role-based and port-based IPFIX.

FAQs and Troubleshooting

n When IPFIX is used with Application Recognition, these features do not support LAGs or MCLAGs (VSX

LAGs).

n The following messages are displayed to indicate an illegal argument:

o % The flow exporter <EXPORTER-NAME> does not exist.

o % The flow record <RECORD-NAME> does not exist.

o % The flow monitor <MONITOR-NAME> does not exist.

o Invalid destination IP address or hostname entered.

o Unable to create the flow exporter. The maximum allowed number of flow exporters (<max>) has

been reached.

o Unable to create the flow record. The maximum allowed number of flow records (<max>) has

been reached.

o Unable to create the flow monitor. The maximum allowed number of flow monitors (<max>) has

been reached.

o Flow monitor cannot be applied while interface is part of LAG <LAG-NAME>.

o Flow monitor could not be applied.

o Flow monitor could not be unapplied

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

22

| Flow         | monitoring      | commands               |     |
| ------------ | --------------- | ---------------------- | --- |
| collect      | application     | tcp establishment-time |     |
| collect      | application tcp | establishment-time     |     |
| [no] collect | application     | tcp establishment-time |     |
Description
Configurescollect(non-key)fieldsforaflowrecordwhenintheconfig-flow-recordcontext.
SupportedonIPv4andIPv6flows.
Onlyonecollectfieldcanbespecifiedperline,whileaflowrecordcanhavemultiplecollectfields.
| Parameter |     | Description                                            |     |
| --------- | --- | ------------------------------------------------------ | --- |
| tcp       |     | SpecifiesTransmissionControlProtocol(TCP)parametersasa |     |
non-keyfieldinaflowrecord.
establishment-time SpecifiesTCPconnectionestablishmenttimeasanon-keyfieldin
aflowrecord.
Usage
n ARCinspectsthefirstfewpacketsofeachflowandonlythosepacketsarecopiedtotheswitch.
n TimemeasurementforestablishedTCP flowsispossibleduringtheTCPconnectionestablishment
phase,andallthreepacketsarereceivedintheorder.
Examples
AddingaTCPconnectionestablishmenttimetoflowrecordflow-record-1asacollectfield.
switch(config-flow-record)# collect application tcp establishment-time
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command    | History     |                   |           |
| ---------- | ----------- | ----------------- | --------- |
| Release    |             | Modification      |           |
| 10.15.1000 |             | Commandintroduced |           |
| Command    | Information |                   |           |
| Platforms  | Command     | context           | Authority |
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400      | config-flow-collector |       | rightsforthiscommand. |
| --------- | --------------------- | ----- | --------------------- |
| diag-dump | ipfix                 | basic |                       |
IPFlowInformationExport |23

| diag-dump ipfix | basic |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- |
Description
DisplaysdiagnosticinformationforIPFIX.
Examples
| diag-dump ipfix | basic |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- |
=========================================================================
| [Start] Feature | ipfix Time | :   | Tue Apr 11 02:23:03 |     | 2023 |
| --------------- | ---------- | --- | ------------------- | --- | ---- |
=========================================================================
-------------------------------------------------------------------------
| [Start] Daemon | ipfixd |     |     |     |     |
| -------------- | ------ | --- | --- | --- | --- |
-------------------------------------------------------------------------
| - IPFIX Record | Cache dump | -   |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- |
| - IPFIX Record | ipfix -    |     |     |     |     |
....
| :- IPFIX Monitor | v6ti completed |       | -      |     |     |
| ---------------- | -------------- | ----- | ------ | --- | --- |
| - End of IPFIX   | Monitor        | Cache | dump - |     |     |
-------------------------------------------------------------------------
| [End] Daemon | ipfixd |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- |
-------------------------------------------------------------------------
-------------------------------------------------------------------------
| [Start] Daemon | ops-switchd |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | --- |
-------------------------------------------------------------------------
Key format: <traffic_type>_<coalescence_id>_<agent_id>_<asic_port>
| Key                              |     |     | TCAM Entry       | ID  | Count |
| -------------------------------- | --- | --- | ---------------- | --- | ----- |
| -------------------------------- |     |     | ---------------- |     | ----- |
| 1_1532781829_3_20                |     |     | 0xffff7c7e7a00   |     | 1     |
| 1_3217499901_1_12                |     |     | 0xffff91187580   |     | 1     |
| 1_3217499901_1_13                |     |     | 0xffff91183d80   |     | 1     |
| 1_3217499901_1_14                |     |     | 0xffff91186e80   |     | 1     |
....
-------------------------------------------------------------------------
| [End] Daemon | ops-switchd |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- |
-------------------------------------------------------------------------
=========================================================================
| [End] Feature | ipfix |     |     |     |     |
| ------------- | ----- | --- | --- | --- | --- |
=========================================================================
| Diagnostic-dump | captured | for | feature ipfix |     |     |
| --------------- | -------- | --- | ------------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheSecurityGuideforyourswitchmodel.
Command History
| Release |     |     | Modification                                   |     |     |
| ------- | --- | --- | ---------------------------------------------- | --- | --- |
| 10.11   |     |     | Commandintroducedon6300,6400,8100and8360Switch |     |     |
series.
Command Information
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 24

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400(v2 |     |     | rightsforthiscommand. |     |
| ------- | --- | --- | --------------------- | --- |
profileonly)
flow exporter
| flow exporter   | <name>        |     |     |     |
| --------------- | ------------- | --- | --- | --- |
| export-protocol | ipfix         |     |     |     |
| description     | <description> |     |     |     |
destination
| <hostname> | [vrf vrfname]        |     |     |     |
| ---------- | -------------------- | --- | --- | --- |
| <ipaddr>   | [vrf vrfname]        |     |     |     |
| <ip6addr>  | [vrf vrfname]        |     |     |     |
| type       | {hostname-or-ip-addr | |   |     |     |
no ..
| template  | data timeout | <timeout> |     |     |
| --------- | ------------ | --------- | --- | --- |
| transport | udp <port>   |           |     |     |
Description
AflowexporteristhepartoftheIPFlowInformationExport(IPFIX)featurethatdefineshowaflow
monitorexportsflowreports.Youcanassignthesameflowexporterconfigurationtomorethanone
flowmonitor.Eachflowexporterincludesadestinationsettingthatidentifiesthedevicetowhichthe
flowreportsaresent.Aruba6200,6300and6400 seriessupportamaximumofsixteenflowmonitors
withalimitoftwoflowexportersthatcanbeappliedtoasingleflowmonitor.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<name>
Nameoftheflowexporter,upto
64characters.
| export-protocol | ipfix |     |     | Defineanexportprotocolforthe |
| --------------- | ----- | --- | --- | ---------------------------- |
flowexporter.Thedefaultipfix
protocolistheonlyprotocol
currentlyavailable.
| description | <description> |     |     | Adescriptionoftheflowexporter, |
| ----------- | ------------- | --- | --- | ------------------------------ |
upto256charactersandspaces.
| destination | <hostname>|<IPaddr>|<ip6addr> |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- |
Theexportersendsflowrecords
tothisdestination.The
destinationcanbedefinedasa
hostname,oranIPv4orIPv6IP
address.
| [vrf vrfname] |     |     |     | Youcanoptionallyincludethe |
| ------------- | --- | --- | --- | -------------------------- |
nameofthedestinationVRFin
thedestinationdefinition.
destination type {hostname-or-ip-addr | traffic-insight} Theexportersendsflowreports
toatrafficinsightdestination.
destination traffic-insight <name> Theexportersendsflowreports
toaspecifictrafficinsight
destination.
IPFlowInformationExport |25

| Parameter |     |     |     | Description         |
| --------- | --- | --- | --- | ------------------- |
| no ..     |     |     |     | Negateanyconfigured |
parameter.
| template | data timeout <timeout> |     |     |     |
| -------- | ---------------------- | --- | --- | --- |
Aflowexportertemplate
describestheformatofexported
flowreports.Therefore,flow
reportscannotbedecoded
properlywithoutthe
correspondingtemplates.This
settingdefineshowoftentheflow
exporterwillresendtemplatesto
theflowmonitor.Thesupported
rangeis1-86400seconds,andthe
defaultis600seconds.
| transport | udp <port> |     |     | Transportprotocolandportfor |
| --------- | ---------- | --- | --- | --------------------------- |
sendingflowrecordreports.The
defaultportisport4739,
| type |     |     |     | Configurethetypeofthe |
| ---- | --- | --- | --- | --------------------- |
destination.
| IPV4-ADDR |     |     |     | TheIPv4addressofthe |
| --------- | --- | --- | --- | ------------------- |
destinationfortheflowexporter.
| INSTANCE-NAME |     |     |     | ChenameoftheTrafficInsight |
| ------------- | --- | --- | --- | -------------------------- |
instance.
Examples
Thefollowingexamplecreatesaflowexporterconfigurationnamedexporter-1.
| switch(config)#               | flow exporter | exporter-1  |              |          |
| ----------------------------- | ------------- | ----------- | ------------ | -------- |
| switch(config-flow-exporter)# |               | dscp 34     |              |          |
| switch(config-flow-exporter)# |               | destination | 192.0.2.1    | vrf VRF1 |
| switch(config-flow-exporter)# |               | template    | data timeout | 1200     |
switch(config-flow-exporter)# description Exports flows to 192.0.2.1
ThefollowingexamplesetsaTrafficInsightinstanceasthedestinationforaflowexporter
| switch(config)#               | flow exporter | exporter-3  |                      |     |
| ----------------------------- | ------------- | ----------- | -------------------- | --- |
| switch(config-flow-exporter)# |               | destination | type traffic-insight |     |
switch(config-flow-exporter)# destination traffic-insight instance-1
Followingexampleaddsadestinationofeachpossibletypeandsethostname-or-ip-addrasthetypeto
use:
| switch(config)#               | flow exporter | exporter-4  |             |     |
| ----------------------------- | ------------- | ----------- | ----------- | --- |
| switch(config-flow-exporter)# |               | destination | collector-1 |     |
switch(config-flow-exporter)# destination traffic-insight instance-1
switch(config-flow-exporter)# destination type hostname-or-ip-addr
Followingexampleremovesthedestinationoftypetraffic-insightfromaflowexporter
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 26

| switch(config)#               | flow exporter | exporter-3     |                 |     |
| ----------------------------- | ------------- | -------------- | --------------- | --- |
| switch(config-flow-exporter)# |               | no destination | traffic-insight |     |
Followingexampleremovesthedestinationoftypehostname-or-ip-addrfromaflowexporter
| switch(config)#               | flow exporter | exporter-1     |     |     |
| ----------------------------- | ------------- | -------------- | --- | --- |
| switch(config-flow-exporter)# |               | no destination |     |     |
Followingexampleremovesthedestinationtypefromaflowexporter
| switch(config)#               | flow exporter | exporter-1     |      |     |
| ----------------------------- | ------------- | -------------- | ---- | --- |
| switch(config-flow-exporter)# |               | no destination | type |     |
FollowingexamplesetsanIPv4addressasthedestinationforaflowexporter
| switch(config)# | flow exporter | exporter-1 |     |     |
| --------------- | ------------- | ---------- | --- | --- |
switch(config-flow-exporter)# destination type hostname-or-ip-addr
| switch(config-flow-exporter)# |     | destination | 192.168.0.1 |     |
| ----------------------------- | --- | ----------- | ----------- | --- |
Followingexamplesetsahostnameasthedestinationforaflowexporter
| switch(config)# | flow exporter | exporter-1 |     |     |
| --------------- | ------------- | ---------- | --- | --- |
switch(config-flow-exporter)# destination type hostname-or-ip-addr
| switch(config-flow-exporter)# |     | destination | collector1 |     |
| ----------------------------- | --- | ----------- | ---------- | --- |
FollowingexamplesetsanIPv6addressasthedestinationforaflowexporter
| switch(config)# | flow exporter | exporter-1 |     |     |
| --------------- | ------------- | ---------- | --- | --- |
switch(config-flow-exporter)# destination type hostname-or-ip-addr
switch(config-flow-exporter)# destination 2001:db87::8a2e:370a:7334
ThefollowingexamplesetsanIPv4addressasthedestinationforaflowexporterwiththeVRFtowhich
theIPv4addressbelongs
| switch(config)# | flow exporter | exporter-2 |     |     |
| --------------- | ------------- | ---------- | --- | --- |
switch(config-flow-exporter)# destination type hostname-or-ip-addr
| switch(config-flow-exporter)# |     | destination | 192.0.2.1 | vrf VRF1 |
| ----------------------------- | --- | ----------- | --------- | -------- |
ThefollowingexamplesetsaTrafficInsightinstanceasthedestinationforaflowexporter
| switch(config)#               | flow exporter | exporter-3  |                      |     |
| ----------------------------- | ------------- | ----------- | -------------------- | --- |
| switch(config-flow-exporter)# |               | destination | type traffic-insight |     |
switch(config-flow-exporter)# destination traffic-insight instance-1
Thefollowingexampleaddsadestinationofeachpossibletypeandsethostname-or-ip-addrasthe
typetouse
IPFlowInformationExport |27

| switch(config)#               | flow | exporter | exporter-4  |     |             |
| ----------------------------- | ---- | -------- | ----------- | --- | ----------- |
| switch(config-flow-exporter)# |      |          | destination |     | collector-1 |
switch(config-flow-exporter)# destination traffic-insight instance-1
switch(config-flow-exporter)# destination type hostname-or-ip-addr
Thefollowingexampleremovesthedestinationoftypetraffic-insightfromaflowexporter:
| switch(config)#               | flow | exporter | exporter-3 |             |                 |
| ----------------------------- | ---- | -------- | ---------- | ----------- | --------------- |
| switch(config-flow-exporter)# |      |          | no         | destination | traffic-insight |
Followingexampleremovesthedestinationoftypehostname-or-ip-addrfromaflowexporter
| switch(config)#               | flow | exporter | exporter-1 |             |     |
| ----------------------------- | ---- | -------- | ---------- | ----------- | --- |
| switch(config-flow-exporter)# |      |          | no         | destination |     |
Followingexampleremovesthedestinationtypefromaflowexporter
| switch(config)#               | flow | exporter | exporter-1 |             |      |
| ----------------------------- | ---- | -------- | ---------- | ----------- | ---- |
| switch(config-flow-exporter)# |      |          | no         | destination | type |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History |     |     |     |                                                |     |
| --------------- | --- | --- | --- | ---------------------------------------------- | --- |
| Release         |     |     |     | Modification                                   |     |
| 10.11           |     |     |     | Commandintroducedon6300,6400,8100and8360Switch |     |
series.
| Command Information |         |         |     |           |     |
| ------------------- | ------- | ------- | --- | --------- | --- |
| Platforms           | Command | context |     | Authority |     |
6300 config Administratorsorlocalusergroupmemberswithexecution
|     | config-flow-exporter |     |     | rightsforthiscommand. |     |
| --- | -------------------- | --- | --- | --------------------- | --- |
6400(v2
profileonly)
flow monitor
| flow monitor  | <name>        |           |     |          |           |
| ------------- | ------------- | --------- | --- | -------- | --------- |
| exporter      | <name>        |           |     |          |           |
| cache timeout | {inactive     | <timeout} |     | |{active | <timeout} |
| description   | <description> |           |     |          |           |
| record <name> |               |           |     |          |           |
Description
OnAruba6200,6300and6400Switchseries,aflowmonitoristhepartoftheIPFlowInformationExport
(IPFIX)featurethatperformsnetworkmonitoringfortheselectedinterface.Aflowmonitor
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 28

configurationconsistsofaflowrecord,aflowcache,andoneormoreassociatedflowexporters.Aflow
monitorcompilesdatafromthenetworktrafficontheinterfaceandstoresitintheflowcacheina
formatdefinedbytheflowrecord.Theflowexportersassociatedwiththemonitorthenexportdata
fromtheflowcachetotheflowexporterdestination.
Aruba6200,6300and6400Switchseriessupportamaximumofsixteenflowmonitorswithalimitoftwoflow
exportersthatcanbeappliedtoasingleflowmonitor.Ifnosoftwareaugmentationofflowsisrequired,thereis
noneedtoconfigureaflowcollectororflowmonitor.
| Parameter |     | Description                            |     |
| --------- | --- | -------------------------------------- | --- |
| <name>    |     | Nameoftheflowmonitor,upto64characters. |     |
cache timeout active <timeout> Usethecachetimeoutparametertodefineanactiveorinactive
timeoutfortheflowmonitor.Aflowmonitorclosesaflow
sessionthatisactiveforlongerthantheactivetimeoutor
inactiveforlongerthantheinactivetimeout.
Theactivetimeoutrangeis30-604800.Thedefaultactivetime
outvalueis1800andinactivetimeoutvalueis30.
| cache timeout | inactive <timeout> |     |     |
| ------------- | ------------------ | --- | --- |
Usethecachetimeoutparametertodefineaninactivetimeout
fortheflowmonitor.Aflowmonitorclosesaflowsessionthat
isactiveforlongerthantheactivetimeoutorinactiveforlonger
thantheinactivetimeout.
description Adescriptionupto256characterslong,includingspaces.
| exporter <name> |     | Assignaflowexportertoaflowmonitor. |     |
| --------------- | --- | ---------------------------------- | --- |
Eachflowmonitorsupportsamaximumoftwodifferentflow
exporters,sendingflowrecordstouptotwodestinations.
| record <name> |     | )Assignsaflowrecordtoaflowmonitor. |     |
| ------------- | --- | ---------------------------------- | --- |
Examples
Thefollowingexamplecreatesaflowmonitorconfigurationnamedmonitor-1.
| switch(config)# | flow monitor | monitor-1 |     |
| --------------- | ------------ | --------- | --- |
switch(config-flow-monitor)# description Monitor for analyzing basic ipv4 traffic
| switch(config-flow-monitor)# |     | exporter flow-exporter-1 |              |
| ---------------------------- | --- | ------------------------ | ------------ |
| switch(config-flow-monitor)# |     | exporter flow-exporter-2 |              |
| switch(config-flow-monitor)# |     | record flow-record-1     |              |
| switch(config-flow-monitor)# |     | cache timeout            | inactive 120 |
| switch(config-flow-monitor)# |     | cache timeout            | active 1500  |
Thefollowingworkflowchangestheflowrecordassignedtoaflowmonitor.
| switch(config)#              | flow monitor | flow-monitor-1       |     |
| ---------------------------- | ------------ | -------------------- | --- |
| switch(config-flow-monitor)# |              | record flow-record-2 |     |
Createmorethanthemaximumnumberofallowedflowmonitors
| switch(config)# | flow monitor | monitor-1 |     |
| --------------- | ------------ | --------- | --- |
IPFlowInformationExport |29

| switch(config)# |         | flow | monitor    |     | monitor-2  |
| --------------- | ------- | ---- | ---------- | --- | ---------- |
| <--OUTPUT       | OMITTED | FOR  | BREVITY--> |     |            |
| switch(config)# |         | flow | monitor    |     | monitor-16 |
| switch(config)# |         | flow | monitor    |     | monitor-17 |
No more than 16 flow monitors can be configured. Another flow monitor
| must be | removed | first. |     |     |     |
| ------- | ------- | ------ | --- | --- | --- |
Assignmorethanoneflowexportertoflowmonitor**flow-monitor-2*
| switch(config)#              |     | flow | monitor |     | flow-monitor-2           |
| ---------------------------- | --- | ---- | ------- | --- | ------------------------ |
| switch(config-flow-monitor)# |     |      |         |     | exporter flow-exporter-2 |
| switch(config-flow-monitor)# |     |      |         |     | exporter flow-exporter-3 |
Addormodifythedescriptionofflowrecord**flow-record-1**
| switch(config)# |     | flow | record | flow-record-1 |     |
| --------------- | --- | ---- | ------ | ------------- | --- |
switch(config-flow-record)# description Used for basic traffic analysis
Addormodifythedescriptionofflowexporter**flow-exporter-1**
| switch(config)# |     | flow | exporter |     | flow-exporter-1 |
| --------------- | --- | ---- | -------- | --- | --------------- |
switch(config-flow-exporter)# description Exports flows to 10.2.3.45:2055
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command | History |     |     |     |                                                |
| ------- | ------- | --- | --- | --- | ---------------------------------------------- |
| Release |         |     |     |     | Modification                                   |
| 10.11   |         |     |     |     | Commandintroducedon6400,6400,8200and8360Switch |
series.
| Command   | Information |     |         |     |           |
| --------- | ----------- | --- | ------- | --- | --------- |
| Platforms | Command     |     | context |     | Authority |
config
| 6300    |                     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ------- | ------------------- | --- | --- | --- | -------------------------------------------------- |
| 6400(v2 | config-flow-monitor |     |     |     | rightsforthiscommand.                              |
profileonly)
flow record
| flow record | <name> |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- |
match
| ipv6         | {protocol|version}|{source|destination |                |       |         | address} |
| ------------ | -------------------------------------- | -------------- | ----- | ------- | -------- |
| ip {source   |                                        | | destination} |       | address |          |
| ip {protocol |                                        | | version      |       |         |          |
| transport    | {source|destination}                   |                |       |         | port     |
| timestamp    | absolute                               |                | first |         |          |
| timestamp    | absolute                               |                | last  |         |          |
collect
| application |     | name |     |     |     |
| ----------- | --- | ---- | --- | --- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 30

application https url
application dns response-code
application tls-attributes
forwarding-status
egress vlan
egress interface
egress queue
counter {packets|bytes}
description <description>

Description

Define data to be included in a flow record by configuring flow record match and collect fields.

A flow record defines match (key) fields and collection (non-key) fields. Customers configure flow
records with match (key) fields and collect (non-key) fields. Match fields are the set of fields that define
a flow, such as IP address or UDP port. Collect fields are the set of fields that identify information to
collect for a flow, such as packet and byte counters.

Traffic with matching attributes (for example, traffic coming from the same interface, sent to the same
destination with the same protocol) are classified as a single flow. Information for some or all of the
matched settings can be collected and exported to a destination defined by the flow exporter assigned
to the flow monitor.

Traffic must match a match rule definition before it can be collected and sent. You cannot collect and send data

that is not matched.

Parameter

Description

<name>

match

Name of the flow monitor, up to 64 characters.

match traffic according to one or more of the following key attributes:

n ip: match traffic on an IPv4 network
n ipv6: match traffic on an IPv6 network
n protocol: Match traffic using the same IP protocol
n version: Match traffic using the same IP version
n source: Match traffic from the same source
n destination: Match traffic to the same destination
n address: Match traffic by source or destination IP address
n transport: Match traffic by source or destination transport type
n port: Match traffic by source or destination transport port

description

A description for the flow record up to 256 characters long, including spaces.

collect

Configures data fields to be included a flow record.

n application name: Specify the application name as a non-key field in a flow

record.

n application https url: Specify the HTTP/HTTPS application URL as a non-key field

in a flow record.

n application dns response-code: Specify the DNS parameters and DNS response

code as a non-key field in the flow record.

n application tls-attributes: Specifies TLS Attributes as a non-key field in a flow

record

n application tcp establishment-time: Specifies TCP connection establishment

IP Flow Information Export | 31

| Parameter | Description |     |     |     |
| --------- | ----------- | --- | --- | --- |
timeasanon-keyfieldinaflowrecord
n fowardingstatus:Specifiesforwardingstatusasanon-keyfieldinaflowrecord
egressvlan:SpecifiesanegressVLANIDasanon-keyfieldinaflowrecord.
n
n egressinterface:Specifiesanegressinterfaceasanon-keyfieldinaflowrecord.
n egressqueue:Specifiesanegressqueueasanon-keyfieldinaflowrecord.
n counterpackets:Collectcounterdataforpacketsintheflow. Packetcount
representsthenumberofincomingpacketssincethepreviousreport.
n counterbytes:Collectcounterdataforbytesintheflow. Bytecountrepresents
thenumberofincomingbytessincethepreviousreport.
n timestampabsolutefirst:Collectabsolutetimestampofthefirstpacket
observed.
n timestampabsolutelast:Collectabsolutetimestampofthelastpacketobserved.
Examples
AddingIPv4andtransportmatchfieldstoflow-record-1:
| switch(config)#             | flow record | flow-record-1        |             |      |
| --------------------------- | ----------- | -------------------- | ----------- | ---- |
| switch(config-flow-record)# |             | match ip source      | address     |      |
| switch(config-flow-record)# |             | match ip destination | address     |      |
| switch(config-flow-record)# |             | match ip protocol    |             |      |
| switch(config-flow-record)# |             | match ip version     |             |      |
| switch(config-flow-record)# |             | match transport      | source port |      |
| switch(config-flow-record)# |             | match transport      | destination | port |
switch(config-flow-record)# description Record used for basic ipv4 traffic
analysis
Thefollowingexampleaddsegresspacketmetadatacollectfieldstoflow record flow-record-1.Egress
interfacedetailswillnotbeavailableuntiltheMACentryisnotprogrammedafterARPresolution.Asa
result,theegressinterfaceinformationisexportedonlyafterthenextactive/inactivetimeoutafterthe
MACentryisprogrammed.
| switch(config)#             | flow record | flow-record-1  |           |     |
| --------------------------- | ----------- | -------------- | --------- | --- |
| switch(config-flow-record)# |             | collect egress | interface |     |
| switch(config-flow-record)# |             | collect egress | queue     |     |
Addingcounterandtimestampcollectfieldstoflow-record-1:
| switch(config)#             | flow record | flow-record-1     |          |       |
| --------------------------- | ----------- | ----------------- | -------- | ----- |
| switch(config-flow-record)# |             | collect counter   | packets  |       |
| switch(config-flow-record)# |             | collect counter   | bytes    |       |
| switch(config-flow-record)# |             | collect timestamp | absolute | first |
| switch(config-flow-record)# |             | collect timestamp | absolute | last  |
Createmorethanthemaximumnumberofallowedflowrecords:
| switch(config)# | flow record | record-1 |     |     |
| --------------- | ----------- | -------- | --- | --- |
| switch(config)# | flow record | record-2 |     |     |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 32

No more than 1 flow record can be configured. Another flow record
| must be removed | first. |     |     |     |
| --------------- | ------ | --- | --- | --- |
AddIPv4matchfieldstoflowrecord**flow-record-1**usingthe`ip`keyword
| switch(config)#             | flow record | flow-record-1 |                |         |
| --------------------------- | ----------- | ------------- | -------------- | ------- |
| switch(config-flow-record)# |             | match ip      | source address |         |
| switch(config-flow-record)# |             | match ip      | destination    | address |
| switch(config-flow-record)# |             | match ip      | protocol       |         |
| switch(config-flow-record)# |             | match ip      | version        |         |
AddIPv6matchfieldstoflowrecord**flow-record-2**
| switch(config)#             | flow record | flow-record-2 |             |         |
| --------------------------- | ----------- | ------------- | ----------- | ------- |
| switch(config-flow-record)# |             | match ipv6    | source      | address |
| switch(config-flow-record)# |             | match ipv6    | destination | address |
| switch(config-flow-record)# |             | match ipv6    | protocol    |         |
| switch(config-flow-record)# |             | match ipv6    | version     |         |
RemovetheIPv4destinationaddressmatchfieldfromflowrecord**flow-record-1**usingthe`ip`
keyword
| switch(config)#             | flow record | flow-record-1 |                |         |
| --------------------------- | ----------- | ------------- | -------------- | ------- |
| switch(config-flow-record)# |             | no match      | ip destination | address |
RemovetheIPv4destinationaddressmatchfieldfromflowrecord**flow-record-1**usingthe`ipv4`
keyword
| switch(config)#             | flow record | flow-record-1 |                  |         |
| --------------------------- | ----------- | ------------- | ---------------- | ------- |
| switch(config-flow-record)# |             | no match      | ipv4 destination | address |
Removethetransportdestinationportmatchfieldfromflowrecord**flow-record-1**
| switch(config)# | flow record | flow-record-1 |     |     |
| --------------- | ----------- | ------------- | --- | --- |
switch(config-flow-record)# no match transport destination port
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
Command History
| Release |     | Modification                                          |     |     |
| ------- | --- | ----------------------------------------------------- | --- | --- |
| 10.15   |     | Theegressvlan,egressinterfaceandegressqueueparameters |     |     |
wereadded.
| 10.14 |     | Theipv4parameterisdeprecatedandreplacedwith ip. |     |     |
| ----- | --- | ----------------------------------------------- | --- | --- |
| 10.13 |     | Addedapplicationhttpsurlanddnsresponse-code     |     |     |
IPFlowInformationExport |33

| Release |     |     | Modification |
| ------- | --- | --- | ------------ |
parameters.
| 10.11 |     |     | Commandintroducedon6300,6300,8100and8360Switch |
| ----- | --- | --- | ---------------------------------------------- |
Series.
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config
| 6300    |                    |     | Administratorsorlocalusergroupmemberswithexecution |
| ------- | ------------------ | --- | -------------------------------------------------- |
| 6400(v2 | config-flow-record |     | rightsforthiscommand.                              |
profileonly)
flow-tracking
flow-tracking
enable
icmp-ageout
interface-flow-limit
| flow statistics | enable |     |     |
| --------------- | ------ | --- | --- |
no ...
tcp-ageout
track icmp
udp-ageout
>
Description
ConfiguresflowtrackingforTCPandUDPflows,andoptionally,ICMPflows.Thenoformofthis
commanddeletestheflowtrackingconfigurationcontext.
Inordertooptimizetheflowremovalprocess,flowsthathaveaged-outareflushedinbatches.Aflow
thathasagedoutisflushedonlywhenthenextbatchprocesses.Thiscancausesomeflowstostay
inactiveforaslightlylongertimethanthevalueconfiguredhere.
| Parameter |     |     | Description          |
| --------- | --- | --- | -------------------- |
| enable    |     |     | Enablesflowtracking. |
icmp-ageout
Configuresanage-outtimeforICMPflows,inseconds.Range:10-
86400.Default:15.
interface-flow-limit Configuresglobalconcurrentflowlimitforflowtrackingenabled
interfaces.Range:64-25000.Default:none.
| flow statistics |     |     | Enableflowstatisticscollection. |
| --------------- | --- | --- | ------------------------------- |
tcp-ageout Configuresage-outtimeforestablishedTCPflowsinseconds.
Range:120-86400.Default:600.
track icmp EnabletrackingofICMPflows,inadditiontotheTCP/UDPflows
trackedbydefault.
udp-ageout
Configuresage-outtimeforestablishedUDPflowsinseconds.
Range:30-86400. Default:30.
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 34

Examples
Configuringflowtracking:
switch(config)#
flow-tracking
switch(config-flow-tracking)#
Deletingflowtracking:
switch(config)# no flow-tracking
switch(config)#
Enablingflowtracking:
switch(config)# flow-tracking
| switch(config-flow-tracking)# | enable |     |
| ----------------------------- | ------ | --- |
Disablingflowtracking:
switch(config)# flow-tracking
| switch(config-flow-tracking)# | no enable |     |
| ----------------------------- | --------- | --- |
ConfiguringanestablishedICMPflowage-outto600seconds:
switch(config)# flow-tracking
| switch(config-flow-tracking)# | icmp-ageout | 600 |
| ----------------------------- | ----------- | --- |
RemovinganestablishedICMPflowage-outof600seconds:
switch(config)#
flow-tracking
| switch(config-flow-tracking)# | no icmp-ageout | 600 |
| ----------------------------- | -------------- | --- |
ConfiguringanestablishedTCPflowage-outto1000seconds:
switch(config)# flow-tracking
| switch(config-flow-tracking)# | tcp-ageout | 1000 |
| ----------------------------- | ---------- | ---- |
RemovinganestablishedTCPflowage-outof1000seconds:
switch(config)# flow-tracking
| switch(config-flow-tracking)# | no tcp-ageout | 1000 |
| ----------------------------- | ------------- | ---- |
ConfiguringanestablishedUDPflowage-outto1000seconds:
switch(config)# flow-tracking
| switch(config-flow-tracking)# | udp-ageout | 1000 |
| ----------------------------- | ---------- | ---- |
RemovinganestablishedUDPflowage-outof1000seconds:
IPFlowInformationExport |35

| switch(config)# |     | flow-tracking |     |     |     |
| --------------- | --- | ------------- | --- | --- | --- |
switch(config-flow-tracking)#
|     |     |     |     | no udp-ageout 1000 |     |
| --- | --- | --- | --- | ------------------ | --- |
Configuringgloballevelinterfaceflowlimitto256interfaces:
| switch(config)#               |     | flow-tracking |     |                      |     |
| ----------------------------- | --- | ------------- | --- | -------------------- | --- |
| switch(config-flow-tracking)# |     |               |     | interface-flow-limit | 256 |
Removinggloballevelinterfaceflowlimitto256interfaces:
| switch(config)#               |     | flow-tracking |     |                         |     |
| ----------------------------- | --- | ------------- | --- | ----------------------- | --- |
| switch(config-flow-tracking)# |     |               |     | no interface-flow-limit | 256 |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Related | Commands |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- |
Command Description
| IP source | lockdown | resource | extended |     |     |
| --------- | -------- | -------- | -------- | --- | --- |
noipsource-lockdownresource-extendedmustbe
disabledtoenableflow-tracking
| Command   | History     |         |         |                                               |     |
| --------- | ----------- | ------- | ------- | --------------------------------------------- | --- |
| Release   |             |         |         | Modification                                  |     |
| 10.14     |             |         |         | Theflowstatisticsenableparameterisintroduced. |     |
| 10.14     |             |         |         | Thetrackicmpparameterisintroduced.            |     |
| 10.13     |             |         |         | Commandintroduced.on6300and6400SwitchSeries   |     |
| Command   | Information |         |         |                                               |     |
| Platforms |             | Command | context | Authority                                     |     |
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400(v2 |     |     |     | rightsforthiscommand. |     |
| ------- | --- | --- | --- | --------------------- | --- |
profileonly)
| ip|ipv6      | flow | monitor      | (interface) |     |     |
| ------------ | ---- | ------------ | ----------- | --- | --- |
| [no] ip|ipv6 |      | flow monitor | (interface) |     |     |
Description
Enableflowmonitoringoninboundandoutboundinterfacesbyassigningaflowmonitortothat
interface.OnlyphysicalinterfacesandLAGinterfacescanbemonitored.Aflowmonitorcannotbe
appliedtoaninterfacethatispartofaLAG.Ifanunsupportedapplicationisattempted,anerror
messagewillbedisplayed.Iftheflowmonitorisassociatedwithaflowrecordthatcontainsapplication
fieldsascollectfields,thenApplicationRecognitionshouldbeenabledonthesameinterface.
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 36

The[no]formofcommanddisablestheflowmonitoring.
Examples
Associateaflowmonitorconfigurationnamedflow-monitor-1 andflow-monitor-2 forIPv4orIPv6
trafficrespectivelyonphysicalinterface.
| switch(config)#    |     | interface |         | 1/1/1        |                |                |     |     |
| ------------------ | --- | --------- | ------- | ------------ | -------------- | -------------- | --- | --- |
| switch(config-if)# |     |           | ip flow | monitor      | flow-monitor-1 |                | in  |     |
| switch(config-if)# |     |           | ipv6    | flow monitor |                | flow-monitor-2 | in  |     |
Associateaflowmonitorconfigurationnamedflow-monitor-3andflow-monitor-4 forIPv4orIPv6
trafficrespectivelyonaLaginterface.
| switch(config)#        |     | interface |      | lag  | 1       |                |     |     |
| ---------------------- | --- | --------- | ---- | ---- | ------- | -------------- | --- | --- |
| switch(config-lag-if)# |     |           | ip   | flow | monitor | flow-monitor-3 |     | in  |
| switch(config-lag-if)# |     |           | ipv6 | flow | monitor | flow-monitor-4 |     | in  |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command   | History     |     |         |     |                                                  |           |     |     |
| --------- | ----------- | --- | ------- | --- | ------------------------------------------------ | --------- | --- | --- |
| Release   |             |     |         |     | Modification                                     |           |     |     |
| 10.11     |             |     |         |     | Commandintroduced.on6300,6400and8325SwtichSeries |           |     |     |
| Command   | Information |     |         |     |                                                  |           |     |     |
| Platforms | Command     |     | context |     |                                                  | Authority |     |     |
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400(v2 | config-flow-monitor |     |     |     |     | rightsforthiscommand. |     |     |
| ------- | ------------------- | --- | --- | --- | --- | --------------------- | --- | --- |
profileonly)
| ipv4|ipv6    | flow | monitor |        | (role) |     |     |     |     |
| ------------ | ---- | ------- | ------ | ------ | --- | --- | --- | --- |
| [no] ip|ipv6 | flow | monitor | <name> |        |     |     |     |     |
Description
Enableflowmonitoringonarole.Theauthorizationstatusofaclientdoesnotdependontheflow
monitorstatusfortheclientinhardware.Theclientwillbeauthorizedevenifthesystemisnotableto
applytheflowmonitorconfigurationintherole.
Incaseofmultipleclientsonboardtoaportwithvariedflowmonitorconfigurations,theflowmonitor
associatedwiththefirstauthenticatedclientontheportwillbeappliedforallthetrafficontheport.
The[no]formofcommandremovestheflowmonitorfromtherole.
| Parameter |     |     |     |     | Description                            |     |     |     |
| --------- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- |
| <name>    |     |     |     |     | Nameoftheflowmonitor,upto64characters. |     |     |     |
IPFlowInformationExport |37

Examples
EnableanIPv4flowmonitoronarolenamedrole01
| switch#                 | config | terminal    |         |         |                |
| ----------------------- | ------ | ----------- | ------- | ------- | -------------- |
| switch(config)#         |        | port-access | role    | role01  |                |
| switch(config-pa-role)# |        |             | ip flow | monitor | flow-monitor-1 |
EnableanIPv6flowmonitoronarolenamedrole01
| switch#                 | config      | terminal    |           |                                              |                |
| ----------------------- | ----------- | ----------- | --------- | -------------------------------------------- | -------------- |
| switch(config)#         |             | port-access | role      | role01                                       |                |
| switch(config-pa-role)# |             |             | ipv6 flow | monitor                                      | flow-monitor-2 |
| Command                 | History     |             |           |                                              |                |
| Release                 |             |             |           | Modification                                 |                |
| 10.14                   |             |             |           | Commandintroducedon6300,and6400Switchseries. |                |
| Command                 | Information |             |           |                                              |                |
| Platforms               | Command     |             | context   | Authority                                    |                |
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400(v2 | config-pa-role |     |     | rightsforthiscommand. |     |
| ------- | -------------- | --- | --- | --------------------- | --- |
profileonly)
| show      | flow exporter |          |              |     |     |
| --------- | ------------- | -------- | ------------ | --- | --- |
| show flow | exporter      | [<name>] | [statistics] |     |     |
Description
Displaysflowexporterstatistics,configurationandstatus.Whennoexporternameisspecified,the
outputofthiscommanddisplaysinformationforallflowexporters.
Theoutputofthiscommandcanindicatethefollowingstatustypes:
n Accepted
n Rejected(Internalerror:exporterdoesnotexist)
n Rejected(Internalerror:destinationtypedoesnotexist)
n Rejected(DestinationtypeishostnameorIPaddress,butnodestinationisspecified)
n Rejected(DestinationtypeishostnameorIPaddress,butthespecifiedhostnameorIPaddressis
invalid)
n Rejected(DestinationtypeisTrafficInsight,butnodestinationisspecified)
n Rejected(DestinationtypeisTrafficInsight,butthespecifiedTrafficInsightinstancedoesnotexist)
n Rejected(DestinationtypeisTrafficInsight,butthespecifiedTrafficInsightinstanceisnotenabled)
n Rejected(DestinationtypeisTrafficInsight,butthespecifiedTrafficInsightinstancesourceisnot
IPFIX)
n Rejected(Internalerror:destinationtypeisTrafficInsight,butthespecifiedTrafficInsightinstanceis
invalid)
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 38

n Rejected(Internalerror:thespecifieddestinationVRFisinvalid)
n Rejected(Internalerror:thespecifieddestinationVRFisnotready)
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<name>
Nameoftheflowexporter.
statistics Thestatisticsparameteraddsstatisticalinformationabout
theflowexportertotheoutput.
Examples
Displaytheconfigurationofaflowexporternamedexporter-1.
| switch# show | flow exporter | exporter-1 |     |     |
| ------------ | ------------- | ---------- | --- | --- |
--------------------------------------------------------------------------------
| Flow exporter | 'exporter-1' |     |     |     |
| ------------- | ------------ | --- | --- | --- |
--------------------------------------------------------------------------------
| Description     |               | : Exports     | to the first  | collector |
| --------------- | ------------- | ------------- | ------------- | --------- |
| Status          |               | : Accepted    |               |           |
| Export Protocol |               | : ipfix       |               |           |
| Destination     | Type          | : Hostname    | or IP address |           |
| Destination     |               | : 192.168.0.1 |               |           |
| Transport       | Configuration |               |               |           |
| Protocol        |               | : UDP         |               |           |
| Port            |               | : 9995        |               |           |
Displaystatisticsinformationforallflowexporters
| switch# show | flow exporter | statistics |     |     |
| ------------ | ------------- | ---------- | --- | --- |
--------------------------------------------------------------------------------
| Flow exporter | 'exporter-1' |     |     |     |
| ------------- | ------------ | --- | --- | --- |
--------------------------------------------------------------------------------
| Reports sent |     | : 14961 |     |     |
| ------------ | --- | ------- | --- | --- |
--------------------------------------------------------------------------------
| Flow exporter | 'exporter-2' |     |     |     |
| ------------- | ------------ | --- | --- | --- |
--------------------------------------------------------------------------------
| Reports sent |     | : 5 |     |     |
| ------------ | --- | --- | --- | --- |
Displayinformationwithnoflowexportersconfigured
| switch# show      | flow exporter |            |     |     |
| ----------------- | ------------- | ---------- | --- | --- |
| No flow exporters | configured.   |            |     |     |
| switch# show      | flow exporter | statistics |     |     |
| No flow exporters | configured.   |            |     |     |
Displayaflowexporter'sinformationwithTIasadestination
| switch# show | flow exporter | exporter-5 |     |     |
| ------------ | ------------- | ---------- | --- | --- |
--------------------------------------------------------------------------------
| Exporter | Name | : exporter-5 |     |     |
| -------- | ---- | ------------ | --- | --- |
IPFlowInformationExport |39

--------------------------------------------------------------------------------
| Description |     |     |     | : Exporter | configured |     | with TI | as the destination |
| ----------- | --- | --- | --- | ---------- | ---------- | --- | ------- | ------------------ |
Status : Rejected (Destination type is Traffic Insight, but the
| specified   |          | Traffic Insight |        | instance     | does    | not | exist) |     |
| ----------- | -------- | --------------- | ------ | ------------ | ------- | --- | ------ | --- |
| Export      | Protocol |                 |        | : ipfix      |         |     |        |     |
| Destination |          | Type            |        | : Traffic    | Insight |     |        |     |
| Destination |          |                 |        | : instance-1 |         |     |        |     |
| Transport   |          | Configuration   |        |              |         |     |        |     |
| Protocol    |          |                 | : UDP  |              |         |     |        |     |
| Port        |          |                 | : 2055 |              |         |     |        |     |
Displayinformationforaflowexporterthathasmultipledestinations
ofdifferenttypesconfiguredand*hostname-or-ip-addr*isspecifiedasthe
destinationtypetouse
| switch# | show | flow exporter |     | exporter-6 |     |     |     |     |
| ------- | ---- | ------------- | --- | ---------- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Flow | exporter | 'exporter-6' |     |     |     |     |     |     |
| ---- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
Description : TI and hostname configured, but type is hostname-or-ip-
addr
| Status      |          |               |        | : Accepted    |     |            |     |     |
| ----------- | -------- | ------------- | ------ | ------------- | --- | ---------- | --- | --- |
| Export      | Protocol |               |        | : ipfix       |     |            |     |     |
| Destination |          | Type          |        | : Hostname    | or  | IP address |     |     |
| Destination |          |               |        | : collector-1 |     |            |     |     |
| Destination |          | VRF           |        | : mgmt        |     |            |     |     |
| Transport   |          | Configuration |        |               |     |            |     |     |
| Protocol    |          |               | : UDP  |               |     |            |     |     |
| Port        |          |               | : 4821 |               |     |            |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command | History |     |     |     |                                                |     |     |     |
| ------- | ------- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| Release |         |     |     |     | Modification                                   |     |     |     |
| 10.11   |         |     |     |     | Commandintroducedon6300,6400,8100and8630Switch |     |     |     |
Series.
| Command   | Information |         |         |     |           |     |     |     |
| --------- | ----------- | ------- | ------- | --- | --------- | --- | --- | --- |
| Platforms |             | Command | context |     | Authority |     |     |     |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400(v2 |     |     |     |     | rightsforthiscommand. |     |     |     |
| ------- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
profileonly)
| show      | flow    | monitor        |     |              |     |     |     |     |
| --------- | ------- | -------------- | --- | ------------ | --- | --- | --- | --- |
| show flow | monitor | [statistics]   |     |              |     |     |     |     |
| show flow | monitor | <MONITOR-NAME> |     | [statistics] |     |     |     |     |
>
Description
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 40

Displays flow monitor configuration and status. When no monitor name is specified, the output of this
command displays information for all flow monitors.

The output of this command can indicate the following status types:

n Accepted

n Rejected (Internal error: monitor does not exist)

n Rejected (A record must be assigned to the monitor, but no record is assigned)

n Rejected (The state of the assigned record is rejected)

n Rejected (Internal error: failure in processing the record configuration)

n Rejected (The state of one or more of the assigned flow exporters is rejected)

Parameter

<name>

statistics

Description

Name of the flow monitor.

Display additional flow and cache statistics.

The possible statistics for a flow monitor are:

Statistics name

Meaning

Current Entries

Flows Added

Current number of flows in the flow cache for this flow monitor.

Total number of flows added to the flow cache for this flow
monitor since it was created

Total Flows Terminated

Total number of flows removed from the flow cache for this flow
monitor since it was created due to any flow end reason

Flows Aged

Active Timeout

Inactive Timeout

End of Flow Detected

Forced End

Forced End

Examples

Number of flows removed from the flow cache for this flow
monitor since it was created due to active or inactive timeout

Number of flows removed from the flow cache for this flow
monitor since it was created due to active cache timeout.

Number of flows removed from the flow cache for this flow
monitor since it was created due to inactive cache timeout.

Number of flows removed from the flow cache for this flow
monitor since it was created due to the detection of signals
indicating the end of the flow. For example, a TCP FIN/RST flag.

Number of flows removed from the flow cache for this flow

monitor since it was created due to some external event. For

example, the shutdown of a flow monitor.

Number of flows removed from the flow cache for this flow

monitor since it was created due to some external event. For

example, the shutdown of a flow monitor.

Display the configuration of a flow monitor named flow-monitor-1.

IP Flow Information Export | 41

| switch# show | flow monitor | monitor-1 |     |     |
| ------------ | ------------ | --------- | --- | --- |
--------------------------------------------------------------------------------
| Flow monitor | 'monitor-1' |     |     |     |
| ------------ | ----------- | --- | --- | --- |
--------------------------------------------------------------------------------
| Description      |     | : Used for    | IPv4 traffic | analysis |
| ---------------- | --- | ------------- | ------------ | -------- |
| Status           |     | : Accepted    |              |          |
| Flow Record      |     | : record-1    |              |          |
| Flow Exporter(s) |     | : exporter-1, | exporter-2   |          |
Cache Configuration
| Inactive | Timeout | : 1800 |     |     |
| -------- | ------- | ------ | --- | --- |
| Active   | Timeout | : 300  |     |     |
Displaythestatisticsofaflowmonitornamedflow-monitor-1.
| switch# show | flow monitor | monitor-1 | statistics |     |
| ------------ | ------------ | --------- | ---------- | --- |
--------------------------------------------------------------------------------
| Flow monitor | 'monitor-1' |     |     |     |
| ------------ | ----------- | --- | --- | --- |
--------------------------------------------------------------------------------
| Current Entries |               | : 2 |     |     |
| --------------- | ------------- | --- | --- | --- |
| Flows Added     |               | : 4 |     |     |
| Total Flows     | Terminated    | : 4 |     |     |
| Flows Aged      |               | : 2 |     |     |
| Active          | Timeout       | : 1 |     |     |
| Inactive        | Timeout       | : 1 |     |     |
| End of          | Flow Detected | : 2 |     |     |
| Forced          | End           | : 0 |     |     |
TheflowmonitorstatisticscounterswillberesettozeroafterVSFISSUswitchover.
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
Displayinformationforallflowmonitors
| switch# show | flow monitor |     |     |     |
| ------------ | ------------ | --- | --- | --- |
--------------------------------------------------------------------------------
| Flow monitor | 'monitor-1' |     |     |     |
| ------------ | ----------- | --- | --- | --- |
--------------------------------------------------------------------------------
| Description      |     | : Used for    | IPv4 traffic | analysis |
| ---------------- | --- | ------------- | ------------ | -------- |
| Status           |     | : Accepted    |              |          |
| Flow Record      |     | : record-1    |              |          |
| Flow Exporter(s) |     | : exporter-1, | exporter-2   |          |
| Flow Collector   |     | : collector-1 |              |          |
| Flow Exporter(s) |     | : exporter-1  |              |          |
Cache Configuration
| Inactive     | Timeout     | : 1800 |     |     |
| ------------ | ----------- | ------ | --- | --- |
| Active       | Timeout     | : 300  |     |     |
| Flow monitor | 'monitor-2' |        |     |     |
--------------------------------------------------------------------------------
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 42

|     | Description |     |     | : Used | for IPv6 traffic | analysis |
| --- | ----------- | --- | --- | ------ | ---------------- | -------- |
Status : Rejected (The state of one or more of the specified flow
|     | exporters           | is rejected) |     |              |     |     |
| --- | ------------------- | ------------ | --- | ------------ | --- | --- |
|     | Flow Record         |              |     | : record-2   |     |     |
|     | Flow Exporter(s)    |              |     | : exporter-1 |     |     |
|     | Cache Configuration |              |     |              |     |     |
|     | Inactive            | Timeout      |     | : 18000      |     |     |
|     | Active              | Timeout      |     | : 2400       |     |     |
```
|     | Display information |     | with | no flow | monitors configured |     |
| --- | ------------------- | --- | ---- | ------- | ------------------- | --- |
```
|     | switch# show     | flow | monitor     |            |     |     |
| --- | ---------------- | ---- | ----------- | ---------- | --- | --- |
|     | No flow monitors |      | configured. |            |     |     |
|     | switch# show     | flow | monitor     | statistics |     |     |
|     | No flow monitors |      | configured. |            |     |     |
```
| Display | statistics   | for  | all     | flow monitors |     |     |
| ------- | ------------ | ---- | ------- | ------------- | --- | --- |
|         | switch# show | flow | monitor | statistics    |     |     |
--------------------------------------------------------------------------------
|     | Flow monitor | 'monitor-1' |     |     |     |     |
| --- | ------------ | ----------- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
|     | Current Entries |               |     | : 2 |     |     |
| --- | --------------- | ------------- | --- | --- | --- | --- |
|     | Flows Added     |               |     | : 6 |     |     |
|     | Total Flows     | Terminated    |     | : 4 |     |     |
|     | Flows Aged      |               |     | : 2 |     |     |
|     | Active          | Timeout       |     | : 1 |     |     |
|     | Inactive        | Timeout       |     | : 1 |     |     |
|     | Total Flows     | Terminated    |     | : 2 |     |     |
|     | Flows Aged      |               |     | : 2 |     |     |
|     | Inactive        | Timeout       |     | : 2 |     |     |
|     | End of          | Flow Detected |     | : 2 |     |     |
|     | Forced          | End           |     | : 0 |     |     |
--------------------------------------------------------------------------------
|     | Flow monitor | 'monitor-2' |     |     |     |     |
| --- | ------------ | ----------- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
|         | Current Entries |               |     | : 6  |                                                |     |
| ------- | --------------- | ------------- | --- | ---- | ---------------------------------------------- | --- |
|         | Flows Added     |               |     | : 12 |                                                |     |
|         | Total Flows     | Terminated    |     | : 6  |                                                |     |
|         | Flows Aged      |               |     | : 4  |                                                |     |
|         | Active          | Timeout       |     | : 3  |                                                |     |
|         | Inactive        | Timeout       |     | : 1  |                                                |     |
|         | End of          | Flow Detected |     | : 2  |                                                |     |
|         | Forced          | End           |     | : 0  |                                                |     |
| Command | History         |               |     |      |                                                |     |
| Release |                 |               |     |      | Modification                                   |     |
| 10.11   |                 |               |     |      | Commandintroducedon6400,6400,8200and8360Switch |     |
series.
IPFlowInformationExport |43

| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
config
| 6300    |                     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ------- | ------------------- | --- | -------------------------------------------------- | --- |
| 6400(v2 | config-flow-monitor |     | rightsforthiscommand.                              |     |
profileonly)
| show flow        | record   |     |     |     |
| ---------------- | -------- | --- | --- | --- |
| show flow record | [<name>] |     |     |     |
Description
Displayflowrecordconfigurationandstatus.Whennorecordnameisspecified,theoutputofthis
commanddisplaysinformationforallflowrecords.
Theoutputofthiscommandcanindicatethefollowingstatustypes:
n Accepted
n Rejected(Internalerror:failedtoprocessrecord)
n Rejected(MixofIPv4andIPv6matchfieldsisnotallowed.SpecifymatchfieldsofthesameIPversion
(IPv4orIPv6))
| Parameter |     |     | Description          |     |
| --------- | --- | --- | -------------------- | --- |
| <name>    |     |     | Nameoftheflowrecord. |     |
Examples
IPv6relatedcommandsareonlyapplicabletoswitchesthatsupportIPv6protocol.
Displaytheconfigurationofaflowrecordnamedflow-record-1.
| switch# show | flow record | record-1 |     |     |
| ------------ | ----------- | -------- | --- | --- |
--------------------------------------------------------------------------------
| Flow record | 'record-1' |     |     |     |
| ----------- | ---------- | --- | --- | --- |
--------------------------------------------------------------------------------
| Description    |                | : Used for | IPv4 traffic | analysis |
| -------------- | -------------- | ---------- | ------------ | -------- |
| Status         |                | : Accepted |              |          |
| Match Fields   |                |            |              |          |
| ipv4           | destination    | address    |              |          |
| ipv4           | protocol       |            |              |          |
| ipv4           | source address |            |              |          |
| ipv4           | version        |            |              |          |
| transport      | destination    | port       |              |          |
| transport      | source         | port       |              |          |
| Collect Fields |                |            |              |          |
| application    | name           |            |              |          |
| counter        | bytes          |            |              |          |
| counter        | packets        |            |              |          |
| application    | https          | URL        |              |          |
Displaytheinformationofaspecificflowrecord.
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 44

| switch# | show | flow | record | record-1 |     |     |
| ------- | ---- | ---- | ------ | -------- | --- | --- |
--------------------------------------------------------------------------------
| Flow | record | 'record-1' |     |     |     |     |
| ---- | ------ | ---------- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Description |     |     |     | : Used     | for IPv4 traffic | analysis |
| ----------- | --- | --- | --- | ---------- | ---------------- | -------- |
| Status      |     |     |     | : Accepted |                  |          |
Match Fields
|             | ipv4 destination |             | address |      |     |     |
| ----------- | ---------------- | ----------- | ------- | ---- | --- | --- |
|             | ipv4 protocol    |             |         |      |     |     |
|             | ipv4 source      | address     |         |      |     |     |
|             | ipv4 version     |             |         |      |     |     |
|             | transport        | destination |         | port |     |     |
|             | transport        | source      | port    |      |     |     |
| Collect     | Fields           |             |         |      |     |     |
|             | application      | name        |         |      |     |     |
|             | application      | https       | url     |      |     |     |
|     counter |                  | bytes       |         |      |     |     |
|             | counter          | packets     |         |      |     |     |
Displayinformationforallflowrecords
| switch# | show | flow | record |     |     |     |
| ------- | ---- | ---- | ------ | --- | --- | --- |
--------------------------------------------------------------------------------
| Flow | record | 'record-1' |     |     |     |     |
| ---- | ------ | ---------- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Description |     |     |     | : Used     | for IPv4 traffic | analysis |
| ----------- | --- | --- | --- | ---------- | ---------------- | -------- |
| Status      |     |     |     | : Accepted |                  |          |
Match Fields
|     | ipv4 | destination |      | address |         |     |
| --- | ---- | ----------- | ---- | ------- | ------- | --- |
|     | ipv4 | protocol    | ipv4 | source  | address |     |
ipv4 version
|         | transport   | destination |        | port |     |     |
| ------- | ----------- | ----------- | ------ | ---- | --- | --- |
|         | transport   |             | source | port |     |     |
| Collect | fields      |             |        |      |     |     |
|         | application |             | name   |      |     |     |
|         | counter     | bytes       |        |      |     |     |
|         | counter     | packets     |        |      |     |     |
--------------------------------------------------------------------------------
| Flow | record | 'record-2' |     |     |     |     |
| ---- | ------ | ---------- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Description |     |     |     | : Used     | for IPv6 traffic | analysis |
| ----------- | --- | --- | --- | ---------- | ---------------- | -------- |
| Status      |     |     |     | : Accepted |                  |          |
Match Fields
|         | ipv6        | destination |         | address |     |     |
| ------- | ----------- | ----------- | ------- | ------- | --- | --- |
|         | ipv6        | protocol    |         |         |     |     |
|         | ipv6        | source      | address |         |     |     |
|         | ipv6        | version     |         |         |     |     |
|         | transport   | destination |         | port    |     |     |
|         | transport   | source      |         | port    |     |     |
| Collect | Fields      |             |         |         |     |     |
|         | application |             | name    |         |     |     |
|         | counter     | bytes       |         |         |     |     |
|         | counter     | packets     |         |         |     |     |
```
Displayinformationforaspecificflowrecord
| switch# | show | flow | record | record-3 |     |     |
| ------- | ---- | ---- | ------ | -------- | --- | --- |
--------------------------------------------------------------------------------
IPFlowInformationExport |45

| Flow record | 'record-3' |     |     |     |
| ----------- | ---------- | --- | --- | --- |
--------------------------------------------------------------------------------
| Description |     | : Used | for IPv4 traffic | analysis |
| ----------- | --- | ------ | ---------------- | -------- |
Status : Rejected (Incomplete match fields. The mandatory match
| fields are: | version, | source address, |     |     |
| ----------- | -------- | --------------- | --- | --- |
destination address, protocol, transport destination port, and transport source
port.)
| Match Fields     |         |     |     |     |
| ---------------- | ------- | --- | --- | --- |
| ipv4 destination | address |     |     |     |
ipv4 protocol
| ipv4 source | address |     |     |     |
| ----------- | ------- | --- | --- | --- |
ipv4 version
| Collect Fields  |      |     |     |     |
| --------------- | ---- | --- | --- | --- |
| application     | name |     |     |     |
| counter bytes   |      |     |     |     |
| counter packets |      |     |     |     |
Displayinformationwithnoflowrecordsconfigured
| switch# show    | flow record |     |     |     |
| --------------- | ----------- | --- | --- | --- |
| No flow records | configured  |     |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History |     |     |                                                 |     |
| --------------- | --- | --- | ----------------------------------------------- | --- |
| Release         |     |     | Modification                                    |     |
| 10.11           |     |     | Commandintroducedon6400,6400,8100,and8360Switch |     |
series.
| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400(v2 |     |     | rightsforthiscommand. |     |
| ------- | --- | --- | --------------------- | --- |
profileonly)
show flow-tracking
show flow-tracking
Description
Displaysflow-trackingandstatisticscollectionconfigurationsandstatus.
Examples
Displaytheconfigurationofrolebasedflowtrackingona6300or6400Switchseries.
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 46

| switch(config)# |            | show flow-tracking   |           |           |       |           |
| --------------- | ---------- | -------------------- | --------- | --------- | ----- | --------- |
| Flow Tracking   |            | Global Configuration |           |           |       |           |
| Configuration   |            | status               | : Enabled |           |       |           |
| Operational     | status     |                      | : Enabled |           |       |           |
| Failure         | Reason     |                      | : NA      |           |       |           |
| UDP Ageout      |            |                      | : 30      | (Seconds) |       |           |
| TCP Ageout      |            |                      | : 600     | (Seconds) |       |           |
| ICMP Ageout     |            |                      | : 15      | (Seconds) |       |           |
| Interface       | Flow       | limit                | : None    |           |       |           |
| Tracked         | Protocols  |                      | : TCP,    | UDP       |       |           |
| Statistics      | Collection |                      |           |           |       |           |
| Configuration   |            | Status               | : Enabled |           |       |           |
| Operational     |            | Status               | : Enabled |           |       |           |
| Failure         | Reason     |                      | : NA      |           |       |           |
| Flow Tracking   |            | Port Configuration   |           |           |       |           |
| Interface       |            | App Recognition      | Reflexive | ACL       | IPFIX | Operation |
Status
----------- ----------- ---------------- ---------- ---------
-
| 1/1/1  |     | Enabled  |     | Disabled | Enabled  | Enabled |
| ------ | --- | -------- | --- | -------- | -------- | ------- |
| 1/1/2  |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/3  |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/4  |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/5  |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/6  |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/7  |     | Enabled  |     | Disabled | Enabled  | Enabled |
| 1/1/8  |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/9  |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/10 |     | Disabled |     | Disabled | Disabled |         |
Disabled
| 1/1/13 |     | Enabled  |     | Disabled | Enabled  | Enabled |
| ------ | --- | -------- | --- | -------- | -------- | ------- |
| 1/1/14 |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/15 |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/16 |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/17 |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/18 |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/19 |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/20 |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/21 |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/23 |     | Enabled  |     | Disabled | Disabled | Enabled |
| 1/1/24 |     | Enabled  |     | Disabled | Enabled  | Enabled |
| 1/1/28 |     | Disabled |     | Disabled | Disabled |         |
Disabled
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
Related Commands
| Command |     |     | Description |     |     |     |
| ------- | --- | --- | ----------- | --- | --- | --- |
IPsourcelockdownresourceextended IPsourcelockdownmustbedisabledwiththenoipsource-
lockdownresource-extendedcommandbeforeenablingflow-
tracking
| Command | History |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
IPFlowInformationExport |47

| Release   |             |         | Modification                                       |
| --------- | ----------- | ------- | -------------------------------------------------- |
| 10.14     |             |         | AddedrolebasedIPFIXandICMP ageoutinformation.      |
| 10.13     |             |         | Commandintroducedon6300and6400SwitchSeries.        |
| Command   | Information |         |                                                    |
| Platforms | Command     | context | Authority                                          |
| 6300      |             |         | Administratorsorlocalusergroupmemberswithexecution |
Manager(#)
| 6400(v2 |     |     | rightsforthiscommand. |
| ------- | --- | --- | --------------------- |
profileonly)
| show tech | ipfix |     |     |
| --------- | ----- | --- | --- |
| show tech | ipfix |     |     |
Description
ShowstheIPFIXconfigurationsettings.
IfapplicablesourceIPaddressorsourceinterfaceisconfiguredfortheIPFIXprotocol,thatconfiguration
isused.
For6200,6300,6400,8360,8100and9300SSwitchSeries,Ifavalidsourceisconfigured,theexporter
sendsflowstoanexternalcollectorusingtheeffectiveconfiguredsourceIPaddressasthesourceIP
addressoftheflowpackets.Inthecontextofthisapplication,avalidsourceIPaddressisanyIPaddress
configuredintheexporter'sVRFnamespace.
Examples
TheexampleshowstheIPFIXconfigurationsettings.
| switch#show | tech | ipfix |     |
| ----------- | ---- | ----- | --- |
====================================================
| Show Tech | executed | on Tue Apr | 11 02:43:06 2023 |
| --------- | -------- | ---------- | ---------------- |
====================================================
====================================================
| [Begin] | Feature ipfix |     |     |
| ------- | ------------- | --- | --- |
====================================================
*********************************
| Command | : show flow | exporter |     |
| ------- | ----------- | -------- | --- |
*********************************
--------------------------------------------------------------------------------
| Flow exporter | 'ipfix' |     |     |
| ------------- | ------- | --- | --- |
--------------------------------------------------------------------------------
| Status      |               | : Accepted |         |
| ----------- | ------------- | ---------- | ------- |
| Export      | Protocol      | : ipfix    |         |
| Destination | Type          | : Traffic  | Insight |
| Destination |               | : t1       |         |
| Transport   | Configuration |            |         |
| Protocol    |               | : udp      |         |
| Port        |               | : 4739     |         |
--------------------------------------------------------------------------------
| Flow exporter | 'V6E1' |     |     |
| ------------- | ------ | --- | --- |
--------------------------------------------------------------------------------
....
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 48

====================================================
| [End] Feature | ipfix |     |     |
| ------------- | ----- | --- | --- |
====================================================
Formoreinformationonfeaturesthatusethiscommand,refertotheSecurityGuideforyourswitchmodel.
| Command History |     |     |                                                 |
| --------------- | --- | --- | ----------------------------------------------- |
| Release         |     |     | Modification                                    |
| 10.11           |     |     | Commandintroducedon6400,6400,8100,and8360Switch |
series.
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400(v2 |     |     | rightsforthiscommand. |
| ------- | --- | --- | --------------------- |
profileonly)
IPFlowInformationExport |49

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
50
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries)

Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideortheMonitoring
Guideforyourswitchmodel.
| Command History     |         |     |         |              |
| ------------------- | ------- | --- | ------- | ------------ |
| Release             |         |     |         | Modification |
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
Bootcommands|51

Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideortheMonitoring
Guideforyourswitchmodel.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
boot management-module
| boot management-module |     | {active | | standby | | <SLOT-ID>} |
| ---------------------- | --- | ------- | --------- | ------------ |
Description
Rebootsthespecifiedmanagementmodule.Choosethemanagementmoduletorebootbyrole(active
orstandby)orbyslotnumber.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
active
Selectstheactivemanagementmodule.
| standby |     |     | Selectsthestandbymanagementmodule. |     |
| ------- | --- | --- | ---------------------------------- | --- |
<SLOT-ID>
Specifiesthememberandslotofthemanagementmoduleinthe
formatmember/slot.Forexample,tospecifythemodulein
member1slot5,enter1/5.
Usage
Thiscommandissupportedonswitchesthathavemultiplemanagementmodules.
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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 52

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
| 6300           |             |         |         |     | Administratorsorlocalusergroupmemberswithexecution |     |     |     |
Manager(#)
| 6400                   |     |     |                |     | rightsforthiscommand. |     |          |     |
| ---------------------- | --- | --- | -------------- | --- | --------------------- | --- | -------- | --- |
| boot management-module |     |     |                |     | (recovery             |     | console) |     |
| boot management-module |     |     | {local|remote} |     |                       |     |          |     |
Description
Rebootsthespecifiedmanagementmodulebyspecifiedlocation(localorremote).
Bootcommands|53

Parameter

<local>

<remote>

Usage

Description

Reboots the local management module.

Reboots the remote management module.

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

Hewlett Packard Enterprise recommends that you use the boot management-module command instead of

pressing the module reset button to reboot a management module because if you are rebooting the only

available management module, the boot management-module command enables you to save the

configuration, cancel the reboot, or both.

Examples

Booting a remote management module:

switch# boot management-module remote
There is no other management module installed.
Aborting.
switch#

command, refer to the Fundamentals Guide or the Monitoring Guide for your switch model.

Command History

Release

10.12

Modification

Command introduced.

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

54

Command Information

Platforms

Command context

Authority

6300
6400

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

Boot commands | 55

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

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

56

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
Forswitchesthatsupportlinemodules(suchas6400switchseries)includingtheallparameterdisplays
informationfortheactivemanagementmoduleandallavailablelinemodules.
Bootcommands|57

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

through the CLI or other API. For details, see ,

show boot-history

Table 1: Description of reboots handled through the database

Boot History String

Description

Reboot requested by user

A user requested a switch reboot through the CLI or web UI.

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

58

| Boot History | String | Description |
| ------------ | ------ | ----------- |
Resetbuttonpressed Theswitchdetectedashort-pressoftheresetbutton
| Backplanefault      |     | Abackplanefaultoccurred.               |
| ------------------- | --- | -------------------------------------- |
| Configurationchange |     | Aconfigurationchangeresultedinareboot. |
Configurationversion Aconfigurationversionmigrationoccurredwhichrequireda
| migration             |     | reboot.                              |
| --------------------- | --- | ------------------------------------ |
| Consoleerror          |     | Theconsolefailedtostart.             |
| Fabricfault           |     | Afabricfaultoccurred.                |
| Alllinemodulesfaulted |     | Azerolinecardconditionoccurred.      |
| Redundancyswitchover  |     | Auserrequestedaredundancyswitchover. |
requested
RedundantManagement Thestandbymanagementmodulehastakenoverfroman
| communicationtimeout |     | unresponsiveactivemanagementmodule. |
| -------------------- | --- | ----------------------------------- |
RedundantManagement Afailuretoelectastandbymanagementmoduleintheallotted
| electiontimeout |     | time. |
| --------------- | --- | ----- |
Criticalservicefault(error) Adaemoncriticaltoswitchoperationhasstoppedfunctioning.An
extraerrorstringmaybepresenttodescribetheerrorindetail.
| VSFautojoinrenumber        |     | ResettriggeredbyVSFautojoin.         |
| -------------------------- | --- | ------------------------------------ |
| VSFmemberrenumbered        |     | AuserrequestedarenumberofaVSFmember. |
| VSFswitchoverrequested     |     | AuserrequestedaVSFswitchover.        |
| VSXsoftwareupdate          |     | ResettriggeredbyaVSXsoftwareupdate.  |
| Chassiscriticaltemperature |     | Chassisoperatingtemperatureexceeded. |
Chassislowcritical Chassistemperaturebelowtheminimumoperatingthreshold.
temperature
| Chassisinsufficientfans |     | Insufficientfanstocoolthechassis. |
| ----------------------- | --- | --------------------------------- |
Chassisunsupported UnsupportedormisconfiguredPSUsorsystemfans.
PSUs/fans
Managementmodulecritical Managementmoduleoperatingtemperatureexceeded.
temperature
ISSUSMMupdate StandbymanagementmodulereboottriggeredbyanIn-Service
SoftwareUpgrade(ISSU).
ISSUswitchover RedundancyswitchovertriggeredbyanIn-ServiceSoftware
Upgrade.
ISSUaborted Standbymanagementmoduleresettriggeredbyfailureduringan
In-ServiceSoftwareUpgrade.
Rollbacktimerexpired ResettriggeredbytheISSUrollbacktimerexpiring.
Bootcommands|59

Examples
Showingtheboothistoryoftheactivemanagementmodule:
| switch#    | show boot-history |     |     |     |     |
| ---------- | ----------------- | --- | --- | --- | --- |
| Management | module            |     |     |     |     |
=================
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
(For6400Switchseries)Showingtheboothistoryoftheactivemanagementmoduleandallline
modules:
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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 60

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
Intheeventofaresettriggeredbyapowersupplyunit(PSU),oraPSUinputfault,theoutputofthis
commandalsodisplaysinformationaboutwhythePSUinitiatedareboot.Thefollowingexample
displaystheboothistoryofaswitchwitharebootinitiatedbyaPSU.
| switch#    | show boot-history |     |     |     |     |
| ---------- | ----------------- | --- | --- | --- | --- |
| Management | module            |     |     |     |     |
=================
| Index : | 2                                  |     |     |     |     |
| ------- | ---------------------------------- | --- | --- | --- | --- |
| Boot ID | : a61ad00d10864c748bc7893a5d4af2e4 |     |     |     |     |
15 Dec 23 19:02:02 : Power on reset with 0x1, Version: FL.10.13.1000AF
| 15 Dec  | 23 19:02:02                        | : Switch | boot | count | is 0     |
| ------- | ---------------------------------- | -------- | ---- | ----- | -------- |
| 15 Dec  | 23 19:02:17                        | : PSU    | 1/1: | Fault | detected |
| Index : | 1                                  |          |      |       |          |
| Boot ID | : 30d831bbfdfa425baf50a629ee01b185 |          |      |       |          |
15 Dec 23 19:01:58 : Power on reset with 0x1, Version: FL.10.13.1000AF
| 15 Dec | 23 19:01:58 | : Switch | boot | count | is 0 |
| ------ | ----------- | -------- | ---- | ----- | ---- |
ThefollowingexampledisplaystheboothistoryfortheVSFmember2.
| switch# | show boot-history |     | vsf | member | 2   |
| ------- | ----------------- | --- | --- | ------ | --- |
Member-2
=========
| Index : | 0                                  |          |           |       |                  |
| ------- | ---------------------------------- | -------- | --------- | ----- | ---------------- |
| Boot ID | : df99026c194a44f1944a3e7685fb4d90 |          |           |       |                  |
| Current | Boot, up for                       | 3        | hrs 31    | mins  | 39 secs          |
| Index : | 3                                  |          |           |       |                  |
| Boot ID | : 7bf4104903fe4ad1ba4bce40e8099c76 |          |           |       |                  |
| 10 Aug  | 17 10:02:24                        | : Reboot | requested |       | through database |
| 10 Aug  | 17 10:02:13                        | : Switch | boot      | count | is 2             |
Bootcommands|61

Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideortheMonitoring
Guideforyourswitchmodel.
| Command History |     |     |              |
| --------------- | --- | --- | ------------ |
| Release         |     |     | Modification |
10.13.1000 Theoutputofthiscommandisenhancedtodisplayadditional
informationaboutthereasonforthereboot,ifavailable.
| 10.07orearlier      |         |         | --        |
| ------------------- | ------- | ------- | --------- |
| Command Information |         |         |           |
| Platforms           | Command | context | Authority |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 62

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
63
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries)

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
Externalstorage|64

Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |              |           |
| -------------- | ----------- | ------- | ------------ | --------- |
| Release        |             |         | Modification |           |
| 10.07orearlier |             |         | --           |           |
| Command        | Information |         |              |           |
| Platforms      | Command     | context |              | Authority |
6300 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
| 6400 |     |     |     | usergroupmemberswithexecution |
| ---- | --- | --- | --- | ----------------------------- |
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
| 6300 |     |     |     | OperatorsorAdministratorsorlocal |
| ---- | --- | --- | --- | -------------------------------- |
| 6400 |     |     |     | usergroupmemberswithexecution    |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 65

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
6300 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
| 6400 |     |     |     | usergroupmemberswithexecution |
| ---- | --- | --- | --- | ----------------------------- |
rightsforthiscommand.Operatorscan
executethiscommandfromthe
operatorcontext(>)only.
external-storage
| external-storage    |     | <VOLUME-NAME> |     |     |
| ------------------- | --- | ------------- | --- | --- |
| no external-storage |     | <VOLUME-NAME> |     |     |
Description
Externalstorage|66

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
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400        |                    |     |               | rightsforthiscommand. |
| ----------- | ------------------ | --- | ------------- | --------------------- |
| password    | (external-storage) |     |               |                       |
| password    | [{plaintext        | |   | ciphertext}   | <PASSWORD>]           |
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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 67

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
6300 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 6400 |     |     |     |     | memberswithexecutionrightsforthis |     |
| ---- | --- | --- | --- | --- | --------------------------------- | --- |
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
Externalstorage|68

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
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| 6400                |                | (#)              |                  |     |     |     |     |
| ------------------- | -------------- | ---------------- | ---------------- | --- | --- | --- | --- |
| show                | running-config |                  | external-storage |     |     |     |     |
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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 69

| Command        | History     |     |         |              |
| -------------- | ----------- | --- | ------- | ------------ |
| Release        |             |     |         | Modification |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
| 6400           | (#)     |          |        | rightsforthiscommand. |
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
Externalstorage|70

| Command   | Information |         |     |           |
| --------- | ----------- | ------- | --- | --------- |
| Platforms | Command     | context |     | Authority |
config-external-storage-<VOLUME-NAME>
| 6300 |     |     |     | Administratorsorlocalusergroup    |
| ---- | --- | --- | --- | --------------------------------- |
| 6400 |     |     |     | memberswithexecutionrightsforthis |
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
6300 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 6400 |     |     |     | memberswithexecutionrightsforthis |
| ---- | --- | --- | --- | --------------------------------- |
command.
| vrf (external | storage) |     |     |     |
| ------------- | -------- | --- | --- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 71

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
6300 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 6400 |     |     |     | memberswithexecutionrightsforthis |
| ---- | --- | --- | --- | --------------------------------- |
command.
Externalstorage|72

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

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

73

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

IP-SLA | 74

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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
6400
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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 75

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
IP-SLA|76

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 77

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
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
<IP-SLA-NAME>
SpecifiesanIP-SLAprofilename.Length:1to64characters.
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
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
ip-sla responder
ip-sla responder <SLA-NAME> (udp-echo | tcp-connect | udp-jitter-voip) <PORT-NUM>
{source {< {A.B.C.D | A:B::C:D> | <IFNAME>}|[vrf <VRF-NAME>]{ipv6}
IP-SLA|78

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

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

79

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

6300
6400

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

IP-SLA | 80

| Command   | Information |         |         |           |     |
| --------- | ----------- | ------- | ------- | --------- | --- |
| Platforms |             | Command | context | Authority |     |
config
| 6300 |        |           |         | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | ------ | --------- | ------- | -------------------------------------------------- | --- |
| 6400 |        |           |         | rightsforthiscommand.                              |     |
| show | ip-sla | responder | results |                                                    |     |
show ip-sla responder <SLA-NAME> <SOURCE-IPV4-ADDR> <PORT-NUM> results
Description
Showsthegivenip-slaresponderstatisticsforagivensourceIPandport.Thiscommandisonly
applicableforthesourceswheresourceIPandportareconfigured.
| Parameter          |     |     |     | Description                            |     |
| ------------------ | --- | --- | --- | -------------------------------------- | --- |
| <SLA-NAME>         |     |     |     | SpecifiestheSLAname.                   |     |
| <SOURCE-IPV4-ADDR> |     |     |     | SpecifiesthesourceIPV4address.         |     |
| <PORT-NUM>         |     |     |     | Specifiestheportnumber.Range:1to65535. |     |
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
6300 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6400
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 81

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
IP-SLA|82

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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 83

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
IP-SLA|84

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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 85

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
| 6400 | (#) |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
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
IP-SLA|86

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
6400 executionrightsforthiscommand.
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
| <PORT-NUM> |     |     | DestinationportfortheIP-SLA.Range:1to65535. |
| ---------- | --- | --- | ------------------------------------------- |
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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 87

| Release             |         | Modification |           |     |
| ------------------- | ------- | ------------ | --------- | --- |
| 10.07orearlier      |         | --           |           |     |
| Command Information |         |              |           |     |
| Platforms           | Command | context      | Authority |     |
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | ------------------------------ | --- |
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
| [source {<SOURCE-IPV4-ADDR> |     | | <IFNAME>}] |     |     |
| --------------------------- | --- | ------------ | --- | --- |
SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
[source-port <PORT-NUM>] SpecifiessourceportfortheIP-SLAtest.Range:1to
65535.
[name-server <IPV4-ADDR-DNS-SERVER>] SpecifiestheDNSserverfordestinationhostname
resolution.
[payload-size <PAYLOAD-SIZE>] SpecifiesthepayloadsizeofanSLAprobe.Range:28
to1440.
| [<TYPE-OF-SERVICE>] |     |     | Typeofservice.Range:0to255. |     |
| ------------------- | --- | --- | --------------------------- | --- |
probe-interval <PROBE-INTERVAL> Probeintervalinseconds.Range:5to604800.
Examples
| switch(config-ipsla-1)# |     | udp-echo 2.2.2.2 | 8080        |         |
| ----------------------- | --- | ---------------- | ----------- | ------- |
| switch(config-ipsla-1)# |     | udp-echo 2.2.2.2 | 8080 source | 2.2.2.1 |
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080
| switch(config-ipsla-1)# |     | udp-echo 2.2.2.2 | 8080 source | 1/1/1 |
| ----------------------- | --- | ---------------- | ----------- | ----- |
switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 2.2.2.1 payload-size 50
switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 1/1/1 payload-size 50
| switch(config-ipsla-1)# |     | udp-echo 2.2.2.2 | 8080 payload-size | 50  |
| ----------------------- | --- | ---------------- | ----------------- | --- |
IP-SLA|88

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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
6400
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
| [advantage-factor | <ADVANTAGE-FACTOR>] |     |     |
| ----------------- | ------------------- | --- | --- |
Selectsthevaluefortheadvantagefactor.Default
valueis0.
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
[source-port <PORT-NUM>] SpecifiesthevalueofsourceportfortheIP-SLA
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 89

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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | --- | ------------------------------ |
vrf (ip sla)
vrf <VRF-NAME>
no vrf [<VRF-NAME>]
Description
ConfigurestheVRFonwhichtheSLAwillsendorreceivepackets.Bydefault,thedefaultVRFisused.
ThenoformofthecommandremovesVRFfromSLA.
IP-SLA|90

Parameter Description
<VRF-NAME> SpecifiesaVRFname.Length:Default:default.
Examples
| switch(config-ip-sla-test)# |     | vrf ipslasrc |     |
| --------------------------- | --- | ------------ | --- |
| switch(config-ip-sla-test)# |     | no vrf       |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Release Modification
10.07orearlier --
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | ------------------------------ |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 91

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
92
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries)

| switch(config-if)# |       | show | running-config |     | interface |
| ------------------ | ----- | ---- | -------------- | --- | --------- |
| interface          | 1/1/1 |      |                |     |           |
downshift-enable
Disablingautomaticspeeddownshift:
| switch(config-if)# |     | interface           | 1/1/1 |     |     |
| ------------------ | --- | ------------------- | ----- | --- | --- |
| switch(config-if)# |     | no downshift-enable |       |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |     |              |     |
| ------------------- | ------- | ------- | --- | ------------ | --- |
| Release             |         |         |     | Modification |     |
| 10.07orearlier      |         |         |     | --           |     |
| Command Information |         |         |     |              |     |
| Platforms           | Command | context |     | Authority    |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6400
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
L1-100Mbpsdownshift|93

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
protocolisdisabledontheswitchandthereisonlyoneportin
theVLAN.ProtocolsincludeOSPF,PIM,RIP,LACP,andLLDP.
n AnexampleofaTxfilteredpacketwouldbeamulticastpacket
beingfilteredfromgoingoutoftheingressport.
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
non-zero
Showsonlynonzerostatistics.
| LAG |     |     |     |     | ShowsLAGinterfaceinformation. |     |
| --- | --- | --- | --- | --- | ----------------------------- | --- |
monitor
Continuouslymonitorinterfacestatistics.
| LOOPBACK |     |     |     |     | Showsloopbackinterfaceinformation. |     |
| -------- | --- | --- | --- | --- | ---------------------------------- | --- |
TUNNEL
Showstunnelinterfaceinformation.
| VLAN |     |     |     |     | ShowsVLANinterfaceinformation. |     |
| ---- | --- | --- | --- | --- | ------------------------------ | --- |
<LAG-ID>
SpecifiestheLAGnumber.Range:1-256
| <LOOPBACK-ID> |     |     |     |     | SpecifiestheLOOPBACKnumber.Range:0-255 |     |
| ------------- | --- | --- | --- | --- | -------------------------------------- | --- |
<TUNNEL-ID>
SpecifiesthetunnelID.Range:1-255
| <VLAN-ID> |     |     |     |     | SpecifiestheVLANID.Range:1-4094 |     |
| --------- | --- | --- | --- | --- | ------------------------------- | --- |
VXLAN
ShowstheVXLANinterfaceinformation.
| <VXLAN-ID> |     |     |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |
| ---------- | --- | --- | --- | --- | ---------------------------------------------- | --- |
Examples
Showinginterfaceinformationwhenitisconfiguredasaroute-onlyport:
| switch#           | show      | interface | 1/1/1        |                   |                 |           |
| ----------------- | --------- | --------- | ------------ | ----------------- | --------------- | --------- |
| Interface         | 1/1/1     | is up     |              |                   |                 |           |
| Admin state       | is        | up        |              |                   |                 |           |
| Link state:       | up        | for 2     | days         | (since Sun        | Jun 21 05:30:22 | UTC 2020) |
| Link transitions: |           | 1         |              |                   |                 |           |
| Description:      |           | backup    | data center  | link              |                 |           |
| Hardware:         | Ethernet, |           | MAC Address: | 70:72:cf:fd:e7:b4 |                 |           |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | none |             |     |               |            |     |
| ---------------- | ---- | ----------- | --- | ------------- | ---------- | --- |
| Speed 1000       | Mb/s |             |     |               |            |     |
| Auto-negotiation |      | is          | on  |               |            |     |
| Flow-control:    |      | off         |     |               |            |     |
| Error-control:   |      | off         |     |               |            |     |
| Energy-Efficient |      | Ethernet    |     | is enabledMDI | mode: MDIX |     |
| L3 Counters:     |      | Rx Enabled, | Tx  | Enabled       |            |     |
| Rate collection  |      | interval:   |     | 300 seconds   |            |     |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 94

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
| switch(config-if)# |       | show interface |     | 1/1/1 |     |     |     |     |
| ------------------ | ----- | -------------- | --- | ----- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is up          |     |       |     |     |     |     |
...
| Auto-negotiation |     | is on with | downshift |     | active |     |     |     |
| ---------------- | --- | ---------- | --------- | --- | ------ | --- | --- | --- |
Showinginformationwhentheinterfaceiscurrentlylinkedwithenergy-efficient-ethernetnegotiated:
| switch(config-if)# |       | show interface |     | 1/1/1 |     |     |     |     |
| ------------------ | ----- | -------------- | --- | ----- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is up          |     |       |     |     |     |     |
...
| Energy-Efficient |     | Ethernet | is enabled |     | and active |     |     |     |
| ---------------- | --- | -------- | ---------- | --- | ---------- | --- | --- | --- |
ShowinginformationwhentheinterfaceisshutdownduringaVSX split:
| switch(config-if)# |       | show interface |     | 1/1/1 |     |     |     |     |
| ------------------ | ----- | -------------- | --- | ----- | --- | --- | --- | --- |
| Interface          | 1/1/1 | is down        |     |       |     |     |     |     |
| Admin state        | is    | up             |     |       |     |     |     |     |
| State information: |       | Disabled       | by  | VSX   |     |     |     |     |
Link state: down for 3 days (since Tue Mar 16 05:20:47 UTC 2021)
| Link transitions: |     | 0   |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:
| Hardware: | Ethernet, | MAC Address: |     | 04:09:73:62:90:e7 |     |     |     |     |
| --------- | --------- | ------------ | --- | ----------------- | --- | --- | --- | --- |
MTU 1500
Type SFP+DAC3
Full-duplex
L1-100Mbpsdownshift|95

| qos              | trust      | none            |           |     |         |     |     |     |       |         |
| ---------------- | ---------- | --------------- | --------- | --- | ------- | --- | --- | --- | ----- | ------- |
| Speed            | 0 Mb/s     |                 |           |     |         |     |     |     |       |         |
| Auto-negotiation |            |                 | is off    |     |         |     |     |     |       |         |
| Flow-control:    |            |                 | off       |     |         |     |     |     |       |         |
| Error-control:   |            |                 | off       |     |         |     |     |     |       |         |
| VLAN             | Mode:      | native-untagged |           |     |         |     |     |     |       |         |
| Native           | VLAN:      | 1               |           |     |         |     |     |     |       |         |
| Allowed          | VLAN       | List:           | 1502-1505 |     |         |     |     |     |       |         |
| Rate             | collection |                 | interval: | 300 | seconds |     |     |     |       |         |
| Rate             |            |                 |           |     | RX      |     |     | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
| Mbits       | / sec |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| ----------- | ----- | --- | --- | --- | ---- | --- | --- | ---- | --- | ----- |
| KPkts       | / sec |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Unicast     |       |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Multicast   |       |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Broadcast   |       |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Utilization |       |     |     |     | 0.00 |     |     | 0.00 |     | 0.00  |
| Statistic   |       |     |     |     | RX   |     |     | TX   |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets   |        |     |     |     | 0   |     |     | 0   |     | 0   |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast   |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Multicast |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Broadcast |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Bytes     |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Jumbos    |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Dropped   |        |     |     |     | 0   |     |     | 0   |     | 0   |
| Pause     | Frames |     |     |     | 0   |     |     | 0   |     | 0   |
| Errors    |        |     |     |     | 0   |     |     | 0   |     | 0   |
| CRC/FCS   |        |     |     |     | 0   |     |     | n/a |     | 0   |
| Collision |        |     |     |     | n/a |     |     | 0   |     | 0   |
| Runts     |        |     |     |     | 0   |     |     | n/a |     | 0   |
| Giants    |        |     |     |     | 0   |     |     | n/a |     | 0   |
ShowinginformationwhentheinterfaceisconfiguredwithEEEandtheEEEhasauto-negotiated:
| switch(config-if)# |     |     | show | interface | 1/1/1 physical |     |     |     |     |     |
| ------------------ | --- | --- | ---- | --------- | -------------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
----------------------------------------------------------
|        |     |        |           | Link   | Admin       |        | Speed       |          | Flow-Control |          |
| ------ | --- | ------ | --------- | ------ | ----------- | ------ | ----------- | -------- | ------------ | -------- |
|        | EEE |        | PoE Power |        |             | Port   |             |          |              |          |
| Port   |     | Type   |           | Status | Config      | Status |             | | Config | Status       | | Config |
| Status | |   | Config | (Watts)   | State  | Information |        | Description |          |              |          |
----------------------------------------------------------------------------------
----------------------------------------------------------
| 1/1/1 |     | 1GbT |     | up          | up  | 1G  |     | auto | off | off |
| ----- | --- | ---- | --- | ----------- | --- | --- | --- | ---- | --- | --- |
| on    |     | on   | --  | 10M/100M/1G |     |     | --  |      |     |     |
Showingthemonitorinformation:
Inmonitormode,theCLI refreshesdataautomaticallyuntilitisexitedbyenteringq.Pressing?opensthehelp
menutodisplaywhichoptionsareavailableinthiscontext.
| Interface |     | 1/1/1 | is up |     |     |     |     |     |       |         |
| --------- | --- | ----- | ----- | --- | --- | --- | --- | --- | ----- | ------- |
| Rate      |     |       |       |     | RX  |     |     | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 96

| MBits /     | sec |     |     | 30196.43 |     | 30196.43 |       | 60392.85  |        |
| ----------- | --- | --- | --- | -------- | --- | -------- | ----- | --------- | ------ |
| MPkts /     | sec |     |     | 58977.39 |     | 58977.40 |       | 117954.79 |        |
| Unicast     |     |     |     | 0.00     |     | 0.00     |       |           | 0.00   |
| Multicast   |     |     |     | 58977.39 |     | 58977.40 |       | 117954.79 |        |
| Broadcast   |     |     |     | 0.00     |     | 0.00     |       |           | 0.00   |
| Utilization | %   |     |     | 75.49    |     | 75.49    |       |           | 150.98 |
| Statistic   |     |     |     | RX       |     | TX       | Total | (RX+TX)   |        |
---------------- -------------------- -------------------- --------------------
| Packets      |                |            | 4756527649   |     | 4756527865   |     |              | 9513055514  |     |
| ------------ | -------------- | ---------- | ------------ | --- | ------------ | --- | ------------ | ----------- | --- |
| Unicast      |                |            |              | 0   |              | 0   |              |             | 0   |
| Multicast    |                |            | 4756527649   |     | 4756527865   |     |              | 9513055514  |     |
| Broadcast    |                |            |              | 2   |              | 0   |              |             | 2   |
| Bytes        |                |            | 304417778668 |     | 304417795428 |     | 608835574096 |             |     |
| Jumbos       |                |            |              | 0   |              | 0   |              |             | 0   |
| Dropped      |                |            |              | 0   | 19028847730  |     |              | 19028847730 |     |
| Pause Frames |                |            |              | 0   |              | 0   |              |             | 0   |
| Errors       |                |            |              | 0   |              | 0   |              |             | 0   |
| CRC/FCS      |                |            |              | 0   |              | n/a |              |             | 0   |
| help: ?,     | quit: q        |            |              |     |              |     |              |             |     |
| Help for     | Interface      | Monitor    |              |     |              |     |              |             |     |
| h Toggle     | human-readable |            | mode         |     |              |     |              |             |     |
| c Clear      | interface      | statistics |              |     |              |     |              |             |     |
| Does not     | apply to       | rates      |              |     |              |     |              |             |     |
| Arrows,      | PgUp, PgDn,    | Home,      | End          |     |              |     |              |             |     |
| Navigate     | interface      | statistics |              |     |              |     |              |             |     |
Delay: 2
| help: ?, | quit: q |     |     |     |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Showingtheoutputforinterface1/1/1inhuman-readableformat:
Inhuman-readableformat,the<1symbolforUtilizationindicatesthattheamountofpacketsisbetweenzero
andone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsandthe
Utilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
| switch(config-if)# |       | show  | interface | 1/1/1 human-readable |     |     |       |         |     |
| ------------------ | ----- | ----- | --------- | -------------------- | --- | --- | ----- | ------- | --- |
| Interface          | 1/1/1 | is up |           |                      |     |     |       |         |     |
| Rate               |       |       |           | RX                   |     | TX  | Total | (RX+TX) |     |
---------------- -------------------- -------------------- --------------------
| Bits /      | sec |     |     | 3M  |     | 3M  |     |     | 6M    |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| Pkts /      | sec |     |     | 316 |     | 316 |     |     | 633   |
| Unicast     |     |     |     | 319 |     | 319 |     |     | 638   |
| Multicast   |     |     |     | 0   |     | 0   |     |     | 0     |
| Broadcast   |     |     |     | 0   |     | 0   |     |     | 0     |
| Utilization | %   |     |     | < 1 |     | < 1 |     |     | < 1   |
| Statistic   |     |     |     | RX  |     | TX  |     |     | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     |     | 577K |     | 577K |     |     | 1M  |
| ------------ | --- | --- | --- | ---- | --- | ---- | --- | --- | --- |
| Unicast      |     |     |     | 577K |     | 577K |     |     | 1M  |
| Multicast    |     |     |     | 0    |     | 51   |     |     | 51  |
| Broadcast    |     |     |     | 0    |     | 15   |     |     | 15  |
| Bytes        |     |     |     | 744M |     | 745M |     |     | 1G  |
| Jumbos       |     |     |     | 0    |     | 0    |     |     | 0   |
| Dropped      |     |     |     | 0    |     | 0    |     |     | 0   |
| Filtered     |     |     |     | 0    |     | 0    |     |     | 0   |
| Pause Frames |     |     |     | 0    |     | 0    |     |     | 0   |
L1-100Mbpsdownshift|97

| Errors    |     |     |     |     | 0   |     | 0   |     | 0   |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CRC/FCS   |     |     |     |     | 0   |     | n/a |     | 0   |
| Collision |     |     |     |     | n/a |     | 0   |     | 0   |
| Runts     |     |     |     |     | 0   |     | n/a |     | 0   |
| Giants    |     |     |     |     | 0   |     | n/a |     | 0   |
Showinginformationaboutextendedcounters:
Theoutputoftheshow interface extendedcommandvariesdependingontheswitchmodeland
configuration.
| switch(config-if)# |     | show | interface |     | 1/1/17 | extended |     |     |     |
| ------------------ | --- | ---- | --------- | --- | ------ | -------- | --- | --- | --- |
-------------------------------------------------------------------
| Interface | 1/1/17 |     |     |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------
| Statistics |     |     |     |     |     | Value |     |     |     |
| ---------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
-------------------------------------------------------------------
| Dot1d Tp | Port In         | Frames |         |     |     | 547   |     |     |     |
| -------- | --------------- | ------ | ------- | --- | --- | ----- | --- | --- | --- |
| Dot1d Tp | Port Out        | Frames |         |     |     | 608   |     |     |     |
| Dot3 In  | Pause Frames    |        |         |     |     | 0     |     |     |     |
| Dot3 Out | Pause Frames    |        |         |     |     | 0     |     |     |     |
| Ethernet | Stats Broadcast |        | Packets |     |     | 19    |     |     |     |
| Ethernet | Stats Bytes     |        |         |     |     | 40162 |     |     |     |
| Ethernet | Stats Packets   |        |         |     |     | 342   |     |     |     |
...
-------------------------------------------------------------------
| Error-Statistics |     |     |     |     |     | Value |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
-------------------------------------------------------------------
| Dot1d Base   | Port        | MTU Exceeded |          | Discards |        | 0   |     |     |     |
| ------------ | ----------- | ------------ | -------- | -------- | ------ | --- | --- | --- | --- |
| Dot3 Control | In          | Unknown      | Opcodes  |          |        | 0   |     |     |     |
| Dot3 Stats   | Alignment   | Errors       |          |          |        | 0   |     |     |     |
| Dot3 Stats   | FCS Errors  |              |          |          |        | 0   |     |     |     |
| Dot3 Stats   | Frame       | Too Longs    |          |          |        | 0   |     |     |     |
| Dot3 Stats   | Internal    | Mac          | Transmit |          | Errors | 0   |     |     |     |
| Ethernet     | RX Oversize | Packets      |          |          |        | 0   |     |     |     |
...
Showinginterfacelink-status:
| switch# | show interface |     | link-status |     |     |     |     |     |     |
| ------- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------
| Port | Type |     |     | Physical |       | Link        | Last   |     |     |
| ---- | ---- | --- | --- | -------- | ----- | ----------- | ------ | --- | --- |
|      |      |     |     | Link     | State | Transitions | Change |     |     |
-------------------------------------------------------------
| 1/1/1    | 1G-BT     |     |     | down |     | 0   | --           |          |     |
| -------- | --------- | --- | --- | ---- | --- | --- | ------------ | -------- | --- |
| 1/1/2    | 1G-BT     |     |     | up   |     | 1   | 1 minute ago | (Fri Mar | 09  |
| 12:36:56 | UTC 2018) |     |     |      |     |     |              |          |     |
| 1/1/3    | 1G-BT     |     |     | up   |     | 1   | 1 minute ago | (Fri Mar | 09  |
| 12:36:56 | UTC 2018) |     |     |      |     |     |              |          |     |
| 1/1/4    | --        |     |     | down |     | 0   | --           |          |     |
| 1/1/5    | --        |     |     | down |     | 0   | --           |          |     |
Showinginterfaceloopback1link-status:
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 98

-------------------------------------------------------------
|      |     |      |     |     | Physical |       | Link        | Last   |     |
| ---- | --- | ---- | --- | --- | -------- | ----- | ----------- | ------ | --- |
| Port |     | Type |     |     | Link     | State | Transitions | Change |     |
-------------------------------------------------------------
| loopback1 |     | --  |     |     | up  |     | --  | --  |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Showinginterface1/1/2-1/1/3link-status:
-------------------------------------------------------------
|      |     |      |     |     | Physical |       | Link        | Last   |     |
| ---- | --- | ---- | --- | --- | -------- | ----- | ----------- | ------ | --- |
| Port |     | Type |     |     | Link     | State | Transitions | Change |     |
-------------------------------------------------------------
| 1/1/2    |     | 1G-BT |     |     | up  |     | 1   | 1 minute | ago (Fri Mar 09 |
| -------- | --- | ----- | --- | --- | --- | --- | --- | -------- | --------------- |
| 12:36:56 | UTC | 2018) |     |     |     |     |     |          |                 |
| 1/1/3    |     | 1G-BT |     |     | up  |     | 1   | 1 minute | ago (Fri Mar 09 |
| 12:36:56 | UTC | 2018) |     |     |     |     |     |          |                 |
Showinginterfacelink-status:
| switch# | show | interface |     | link-status |     |     |     |     |     |
| ------- | ---- | --------- | --- | ----------- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------
| Port |     | Type |     |     | Physical |       | Link        | Link Flaps | Last   |
| ---- | --- | ---- | --- | --- | -------- | ----- | ----------- | ---------- | ------ |
|      |     |      |     |     | Link     | State | Transitions | Ignored    | Change |
-------------------------------------------------------------------------
| 1/1/1    |     | 1G-BT    |     |       | down |     | 0   | 0   | --           |
| -------- | --- | -------- | --- | ----- | ---- | --- | --- | --- | ------------ |
| 1/1/2    |     | 1G-BT    |     |       | up   |     | 1   | 0   | 1 minute ago |
| (Fri Mar | 09  | 12:36:56 | UTC | 2018) |      |     |     |     |              |
| 1/1/3    |     | 1G-BT    |     |       | up   |     | 1   | 0   | 1 minute ago |
| (Fri Mar | 09  | 12:36:56 | UTC | 2018) |      |     |     |     |              |
| 1/1/4    |     | --       |     |       | down |     | 0   | 0   | --           |
| 1/1/5    |     | --       |     |       | down |     | 0   | 0   | --           |
Showingstateinformationwheninterfaceisblocked:
| 8360(config-if)#   |       |       | show    | interface |         | 1/1/1 |     |     |     |
| ------------------ | ----- | ----- | ------- | --------- | ------- | ----- | --- | --- | --- |
| Interface          | 1/1/1 | is    | up      | (Blocked) |         |       |     |     |     |
| Admin state        |       | is up |         |           |         |       |     |     |     |
| State information: |       |       | Blocked |           | by UDLD |       |     |     |     |
Link state: up for 1 minute (since Mon Jun 10 09:25:27 UTC 2024)
| Link transitions: |     |     | 1   |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:
Persona:
| Hardware: | Ethernet, |     | MAC | Address: |     | 00:fd:45:67:85:91 |     |     |     |
| --------- | --------- | --- | --- | -------- | --- | ----------------- | --- | --- | --- |
MTU 1500
| Type 10G-LR |     | / 10G | SFP+ | LR  |     |     |     |     |     |
| ----------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- |
Full-duplex
| qos trust        | none   |           |        |     |         |     |     |     |               |
| ---------------- | ------ | --------- | ------ | --- | ------- | --- | --- | --- | ------------- |
| Speed 10000      |        | Mb/s      |        |     |         |     |     |     |               |
| Auto-negotiation |        |           | is off |     |         |     |     |     |               |
| Flow-control:    |        | off       |        |     |         |     |     |     |               |
| Error-control:   |        | off       |        |     |         |     |     |     |               |
| VLAN Mode:       | access |           |        |     |         |     |     |     |               |
| Access           | VLAN:  | 1         |        |     |         |     |     |     |               |
| Rate collection  |        | interval: |        | 300 | seconds |     |     |     |               |
| Rate             |        |           |        |     |         | RX  |     | TX  | Total (RX+TX) |
L1-100Mbpsdownshift|99

---------------- -------------------- -------------------- --------------------
| Mbits / sec |     |     | 0.00 | 0.00 | 0.00  |
| ----------- | --- | --- | ---- | ---- | ----- |
| KPkts / sec |     |     | 0.00 | 0.00 | 0.00  |
| Unicast     |     |     | 0.00 | 0.00 | 0.00  |
| Multicast   |     |     | 0.00 | 0.00 | 0.00  |
| Broadcast   |     |     | 0.00 | 0.00 | 0.00  |
| Utilization | %   |     | 0.00 | 0.00 | 0.00  |
| Statistic   |     |     | RX   | TX   | Total |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     | 15   | 15   | 30   |
| ------------ | --- | --- | ---- | ---- | ---- |
| Unicast      |     |     | 12   | 12   | 24   |
| Multicast    |     |     | 3    | 3    | 6    |
| Broadcast    |     |     | 0    | 0    | 0    |
| Bytes        |     |     | 1350 | 1350 | 2700 |
| Jumbos       |     |     | 0    | 0    | 0    |
| Dropped      |     |     | 0    | 0    | 0    |
| Pause Frames |     |     | 0    | 0    | 0    |
| Errors       |     |     | 0    | 0    | 0    |
| CRC/FCS      |     |     | 0    | n/a  | 0    |
| Collision    |     |     | n/a  | 0    | 0    |
| Runts        |     |     | 0    | n/a  | 0    |
| Giants       |     |     | 0    | n/a  | 0    |
Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideortheMonitoring
Guideforyourswitchmodel.
| Command History |     |     |                                                 |     |     |
| --------------- | --- | --- | ----------------------------------------------- | --- | --- |
| Release         |     |     | Modification                                    |     |     |
| 10.15           |     |     | Addedstateinformationwhenportgoesintodownstate. |     |     |
| 10.11           |     |     | Addedmonitorparameter.                          |     |     |
10.10
Addedhuman-readableparameter.
| 10.07orearlier      |         |         | --        |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- |
| Command Information |         |         |           |     |     |
| Platforms           | Command | context | Authority |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show interface | statistics |     |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- |
show interface [<IFNAME>|<IFRANGE>] statistics [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] statistics monitor [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] error-statistics [non-zero] [human-readable]
show interface [<IFNAME>|<IFRANGE>] error-statistics monitor [non-zero] [human-readable]
show interface lag [<LAG-ID>] statistics [non-zero] [human-readable]
show interface lag [<LAG-ID>] statistics monitor [non-zero] [human-readable]
show interface lag [<LAG-ID>] error-statistics [non-zero] [human-readable]
show interface lag [<LAG-ID>] error-statistics monitor [non-zero] [human-readable]
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 100

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

Showing statistics of a single interfaces:

L1-100Mbps downshift | 101

ShowingstatisticsofallmembersofaLAGinterface:
Showingerrorstatisticsofallinterfaces:
Showingmonitorstatistics:
Therowsandcolumnsofshowinterfacemonitorstatisticsdependsonthelengthofwidthoftheclientterminal.
TheCLI canbenavigatedusingthearrowkeysaswellasthePageUp,PageDown,Home,andEndkeys.
Showingmonitorerrorstatisticsinhuman-readableformat:
Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideortheMonitoring
Guideforyourswitchmodel.
| Command History |     |     |              |
| --------------- | --- | --- | ------------ |
| Release         |     |     | Modification |
10.11
Addedmoitorparameter.
| 10.10               |         |         | Addedhuman-readableparameter. |
| ------------------- | ------- | ------- | ----------------------------- |
| 10.07orearlier      |         |         | --                            |
| Command Information |         |         |                               |
| Platforms           | Command | context | Authority                     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show interface | downshift-enable |     |     |
| -------------- | ---------------- | --- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 102

| show interface | [<IFNNAME>|<IFRANGE>] |     | downshift-enable |     |
| -------------- | --------------------- | --- | ---------------- | --- |
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
| 1/1/2 | yes | no  | 1G  | auto |
| ----- | --- | --- | --- | ---- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
6300 config OperatorsorAdministratorsorlocalusergroupmemberswith
| 6400 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show running-config |     | interface |     |     |
| ------------------- | --- | --------- | --- | --- |
L1-100Mbpsdownshift|103

| show running-config | interface | [<IFNNAME>|<IFRANGE>] |     |     |
| ------------------- | --------- | --------------------- | --- | --- |
show running-config interface [lag | loopback | tunnel | vlan ] [<ID>]
Description
Displaysactiveconfigurationsofvariousswitchinterfaces.
| Parameter |     | Description              |     |     |
| --------- | --- | ------------------------ | --- | --- |
| <IFNAME>  |     | Specifiesainterfacename. |     |     |
<IFRANGE>
Specifiestheportidentifierrange.
| LAG |     | SpecifiesLAGinterfaceinformation |     |     |
| --- | --- | -------------------------------- | --- | --- |
LOOPBACK
Specifiesloopbackinterfaceinformation.
| TUNNEL |     | Specifiestunnelinterfaceinformation. |     |     |
| ------ | --- | ------------------------------------ | --- | --- |
VLAN
SpecifiesVLANinterfaceinformation.
| <LAG-ID> |     | SpecifiestheLAGnumber.Range:1-256. |     |     |
| -------- | --- | ---------------------------------- | --- | --- |
<LOOPBACK-ID>
SpecifiestheLOOPBACKnumber.Range:0-255.
| <TUNNEL-ID> |     | SpecifiesthetunnelID.Range:1-255. |     |     |
| ----------- | --- | --------------------------------- | --- | --- |
<VLAN-ID>
SpecifiestheVLANID.Range:1-4094.
| VXLAN |     | SpecifiestheVXLANinterfaceinformation. |     |     |
| ----- | --- | -------------------------------------- | --- | --- |
<VXLAN-ID>
SpecifiestheVXLANinterfaceidentifier.Default:1.
Examples
Showing1/1/2interfaceconfiguration:
| switch(config-if)# | show | running-config | interface | 1/1/2 |
| ------------------ | ---- | -------------- | --------- | ----- |
| interface 1/1/2    |      |                |           |       |
no shutdown
| description | DC-23 |     |     |     |
| ----------- | ----- | --- | --- | --- |
exit
Showingloopbackinterfacesconfigured:
| switch(config-if)# | show         | running-config | interface | loopback |
| ------------------ | ------------ | -------------- | --------- | -------- |
| interface loopback | 1            |                |           |          |
| description        | lb interface | 1              |           |          |
exit
| interface loopback | 2            |     |     |     |
| ------------------ | ------------ | --- | --- | --- |
| description        | lb interface | 2   |     |     |
exit
Showingloopbackinterfacesnotconfigured:
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 104

| switch(config-if)# |            | show running-config | interface | loopback |
| ------------------ | ---------- | ------------------- | --------- | -------- |
| No loopback        | interfaces | configured.         |           |          |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6300 config OperatorsorAdministratorsorlocalusergroupmemberswith
| 6400 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
L1-100Mbpsdownshift|105

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

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

106

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

Mirroring | 107

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
| switch# clear | mirror | 1   |     |
| ------------- | ------ | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 108

| switch# clear | mirror | endpoint |     |
| ------------- | ------ | -------- | --- |
Clearingmirrorstatisticsformirrorendpointtest:
| switch# clear | mirror | endpoint test |     |
| ------------- | ------ | ------------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| 6400 | (#) |     |     |
| ---- | --- | --- | --- |
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
Mirroring|109

switch(config-mirror-3)# comment This Mirror will be removed during next
| maintenance | window |     |     |
| ----------- | ------ | --- | --- |
Removingthecommentfrommirrorsession3:
| switch(config-mirror-3)# |     | no comment |     |
| ------------------------ | --- | ---------- | --- |
Addingacommenttoamirrorendpoint:
switch(config-mirror-endpoint-test)# comment Monitor endpoint traffic
Replacingtheexistingcommentformirrorendpoint:
switch(config-mirror-endpoint-test)# comment Monitor statistics on each endpoint
interfaces
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Release Modification
10.07orearlier --
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-mirror-<SESSION-ID>
| Allplatforms |                        |     | Administratorsorlocalusergroupmemberswith |
| ------------ | ---------------------- | --- | ----------------------------------------- |
|              | config-mirror-endpoint |     | executionrightsforthiscommand.            |
copy tcpdump-pcap
| copy tcpdump-pcap | <FILE-NAME> | <REMOTE-URL> |     |
| ----------------- | ----------- | ------------ | --- |
Description
Savespacketcapturefilestoexternalstorage.
Parameter Description
<FILE-NAME> Specifiesthepacketcapturefiletosave.
<REMOTE-URL>
Specifiestheexternalstoragetowhichthepacketcapturefilewill
besaved.
Usage
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 110

Onlyfourfilescanbesavedatanypointontheswitch.Packetcapturefilesarenotsavedafterafailover
| orreboot.Viewalistofsavedfilesusingdiag |     |     | utilities list-files. |     |     |     |
| --------------------------------------- | --- | --- | --------------------- | --- | --- | --- |
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
| Command   | History     |         |                   |     |     |     |
| --------- | ----------- | ------- | ----------------- | --- | --- | --- |
| Release   |             |         | Modification      |     |     |     |
| 10.08     |             |         | Commandintroduced |     |     |     |
| Command   | Information |         |                   |     |     |     |
| Platforms | Command     | context | Authority         |     |     |     |
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
| switch# | copy tshark-pcap | sftp://root@10.0.0.2/file.pcap |     |     |     |     |
| ------- | ---------------- | ------------------------------ | --- | --- | --- | --- |
Mirroring|111

| root@10.0.0.2's |               | password: |                    |     |          |           |       |
| --------------- | ------------- | --------- | ------------------ | --- | -------- | --------- | ----- |
| Connected       | to            | 10.0.0.2. |                    |     |          |           |       |
| sftp> put       | packets.pcap  |           | file.pcap          |     |          |           |       |
| Uploading       | packets.pcap  |           | to /root/file.pcap |     |          |           |       |
| packets.pcap    |               |           |                    |     | 100% 156 | 219.8KB/s | 00:00 |
| Copied          | successfully. |           |                    |     |          |           |       |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |     |         |              |     |     |     |
| -------------- | ----------- | --- | ------- | ------------ | --- | --- | --- |
| Release        |             |     |         | Modification |     |     |     |
| 10.07orearlier |             |     |         | --           |     |     |     |
| Command        | Information |     |         |              |     |     |     |
| Platforms      | Command     |     | context | Authority    |     |     |     |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400           |     |     |     | rightsforthiscommand. |     |     |     |
| -------------- | --- | --- | --- | --------------------- | --- | --- | --- |
| destination    | cpu |     |     |                       |     |     |     |
| destination    | cpu |     |     |                       |     |     |     |
| no destination | cpu |     |     |                       |     |     |     |
Description
ThecommandcausesthemirrorsessiontotransmitmirroredpacketstotheswitchCPU.This
destinationmaybeconfiguredformultiplesessions,howeveronlyonesuchconfiguredsessionmaybe
activeatagiventime.
ThediagnosticutilityTsharkmaybeusedtoviewandcapturepacketstransmittedtotheCPUthrough
thisroute.Ctrl+CmustbeenteredtoterminateaTsharkcapturesession.Moredetailscanbefoundin
| theSupportability |     | Guide. |     |     |     |     |     |
| ----------------- | --- | ------ | --- | --- | --- | --- | --- |
ThenoformofthiscommandwillimmediatelystopsmirroringtraffictotheCPU,butwillnotremove
anysourcesfromthemirrorconfiguration.
Examples
ConfiguringamirrorsessionwithCPUasthedestination.
switch#
config
| switch(config)#          |     | mirror | session     | 1   |     |     |     |
| ------------------------ | --- | ------ | ----------- | --- | --- | --- | --- |
| switch(config-mirror-1)# |     |        | destination |     | cpu |     |     |
Removingthedestinationentirely.
| switch(config-mirror-1)# |     |     | no  | destination | cpu |     |     |
| ------------------------ | --- | --- | --- | ----------- | --- | --- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 112

Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |     |         |     |              |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| Release        |             |     |         |     | Modification |     |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
6300 config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
| 6400           |           |     |                             |     | executionrightsforthiscommand. |     |
| -------------- | --------- | --- | --------------------------- | --- | ------------------------------ | --- |
| destination    | interface |     |                             |     |                                |     |
| destination    | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |                                |     |
| no destination | interface |     | {<INTERFACE-ID>|<LAG-NAME>} |     |                                |     |
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
Configuringadifferentdestinationinterfaceinanenabledmirroringsessioncausesallmirroredtraffic
tousethenewdestinationinterface.Thisactionmightcauseatemporarysuspensionofmirrored
sourcetrafficduringthereconfiguration.
Examples
OntheAruba6400SwitchSeries,interfaceidentificationdiffers.
Configuringamirroringsessionandaddinganinterfaceasadestination:
| switch(config)#          |     | mirror | session     | 1   |           |       |
| ------------------------ | --- | ------ | ----------- | --- | --------- | ----- |
| switch(config-mirror-1)# |     |        | destination |     | interface | 1/1/1 |
Replacingtheexistingdestinationwithdifferentinterface:
| switch(config-mirror-1)# |     |     | destination |     | interface | 1/1/12 |
| ------------------------ | --- | --- | ----------- | --- | --------- | ------ |
Removingadestination:
Mirroring|113

| switch(config-mirror-1)# |     | no destination | interface | 1/1/12 |
| ------------------------ | --- | -------------- | --------- | ------ |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
Switch Destination interface limit per mirror session (4 possible sessions)
| 6300           | 64          |              |           |     |
| -------------- | ----------- | ------------ | --------- | --- |
| 6400           | 64          |              |           |     |
| Command        | History     |              |           |     |
| Release        |             | Modification |           |     |
| 10.07orearlier |             | --           |           |     |
| Command        | Information |              |           |     |
| Platforms      | Command     | context      | Authority |     |
config-mirror-<SESSION-ID>
| Allplatforms |     |     | Administratorsorlocalusergroupmemberswith |     |
| ------------ | --- | --- | ----------------------------------------- | --- |
executionrightsforthiscommand.
| destination       | tunnel               |            |                    |     |
| ----------------- | -------------------- | ---------- | ------------------ | --- |
| destination       | tunnel <TUNNEL-IPV4> | source     | <SOURCE-IPv4-ADDR> |     |
| dscp <DSCP-VALUE> | vrf                  | <VRF-NAME> |                    |     |
| no destination    | tunnel               |            |                    |     |
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
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<TUNNEL-IPV4-ADDR> SpecifiesthetunneladdressinIPv4format(x.x.x.x),wherexisa
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 114

| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
decimalnumberfrom0to255.
<SOURCE-IPv4-ADDR> SpecifiesthesourceaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.
<DSCP-VALUE> SpecifiestheDSCPvaluetobecarriedwithintheDSfieldof
ERSPANpacketheader.Range:0to63.Default:0.
<VRF-NAME>
SpecifiesaVRFname.Default:default.
Examples
CreatingaMirrorSessionandaddingtunneldestination,source,dscp,andVRF:
switch#
config
| switch(config)# | mirror | session | 1   |     |     |     |
| --------------- | ------ | ------- | --- | --- | --- | --- |
switch(config-mirror-1)# destination tunnel 1.1.1.1 source 2.2.2.2 dscp 10 vrf
default
Replacingtheexistingtunneldestination:
switch(config-mirror-1)# destination tunnel 11.12.13.14 source 2.2.2.2 dscp 10 vrf
default
ReplacingtheexistingdestinationwithadifferentDSCPvalue:
switch(config-mirror-1)#
|     |     | destination |     | tunnel 11.12.13.14 | source 2.2.2.2 | dscp 2 vrf |
| --- | --- | ----------- | --- | ------------------ | -------------- | ---------- |
default
Removingthedestination:
| switch(config-mirror-1)# |     | no  | destination | tunnel |     |     |
| ------------------------ | --- | --- | ----------- | ------ | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |           |     |     |
| ------------------- | ------- | ------- | ------------ | --------- | --- | --- |
| Release             |         |         | Modification |           |     |     |
| 10.07orearlier      |         |         | --           |           |     |     |
| Command Information |         |         |              |           |     |     |
| Platforms           | Command | context |              | Authority |     |     |
6300 config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand. |     |     |
| ---- | --- | --- | --- | ------------------------------ | --- | --- |
Mirroring|115

diagnostic
diagnostic
| diag utilities | tshark | [file]        |     |     |     |
| -------------- | ------ | ------------- | --- | --- | --- |
| diag utilities | tshark | [delete-file] |     |     |     |
Description
Capturespacketsfromamirror-to-cpusession,andsavethemostrecent32MBtopcapfilewhichcan
thenbecopiedandanalyzed.Whencapturingamirror-to-cpusessiontoafile,packetswillnotbe
dumpedtotheconsole.
Thediagnosticcommandmustbeenteredpriortothediag utilities tsharkcommand.
Usethedelete-fileformofthiscommandtodeletethemostrecentcapturefile.
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
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| diag utilities | tcpdump |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 116

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

n When using the command option, the only traffic captured will be packets that have been mirrored

to the CPU.

n When using the command option, command line sanitization is performed to prevent options that

may cause harm or security issues. The following options are blocked:

o -i/--interface

o -Z

o -B/--buffer-size

o -C

Mirroring | 117

o -W
o -Z/--relinquishprivileges
n Non-wordoperatorssuchas"&"or"|"arenotallowed.Usebooleankeywordssuchas"and,""or,"
and"not."
Whenusingcommand -rtoreadafile,donotprovideanydirectorypathcharacters.Uselist-files
n
commandtogetthelistoffilenamescurrentlysavedonthedevice,andthenusethosefilenames.
n Atotaloffourfilescanbesavedatanygivenpointonthedevice.Packetcapturefilesarenotsaved
afterafailoverorreboot,butcanbesavedtoexternalstorageusingthecopy tcpdump-pcap
command.
Examples
InspectingtrafficmirroredtotheCPUviatcpdumpandsavingtheoutputtomy_capture_file.pcap:
switch# diag utilities tcpdump command -c 2 -x -w my_capture_file.pcap
Inspecting traffic mirrored to the CPU via tcpdump until Ctrl-C is entered.
| 2 packets | captured         |           |     |     |     |
| --------- | ---------------- | --------- | --- | --- | --- |
| 2 packets | received         | by filter |     |     |     |
| 0 packets | dropped          | by kernel |     |     |     |
| Ending    | traffic capture. |           |     |     |     |
Listingsavedcapturefiles:
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
| Successfully | removed | file |     |     |     |
| ------------ | ------- | ---- | --- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 118

| Command   | History     |         |                   |     |
| --------- | ----------- | ------- | ----------------- | --- |
| Release   |             |         | Modification      |     |
| 10.08     |             |         | Commandintroduced |     |
| Command   | Information |         |                   |     |
| Platforms | Command     | context | Authority         |     |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6400    |         |          | rightsforthiscommand. |     |
| ------- | ------- | -------- | --------------------- | --- |
| disable | (mirror | session) |                       |     |
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
Mirroring|119

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
OntheAruba6400SwitchSeries,interfaceidentificationdiffers.
Configuringandenablingamirroringsession:
| switch(config)#          | mirror | session     | 3         |          |
| ------------------------ | ------ | ----------- | --------- | -------- |
| switch(config-mirror-3)# |        | source      | interface | 1/1/2 rx |
| switch(config-mirror-3)# |        | destination | interface | 1/1/3    |
switch(config-mirror-3)# comment Monitor router port ingress-only traffic
| switch(config-mirror-3)# |     | enable |     |     |
| ------------------------ | --- | ------ | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 120

Fromthiscontext,youcanentercommandstoconfigureandenableordisablethemirroringsession.
Thenoformofthiscommandremovesanexistingmirroringsessionfromtheconfiguration.
| Parameter    |     |     | Description                              |
| ------------ | --- | --- | ---------------------------------------- |
| <SESSION-ID> |     |     | Specifiesthesessionidentifier.Range:1to4 |
Examples
| switch(config)# | mirror | session | 1   |
| --------------- | ------ | ------- | --- |
switch(config-mirror-1)#
| switch(config)# | mirror | session | 3   |
| --------------- | ------ | ------- | --- |
switch(config-mirror-3)#
| switch(config)# | no  | mirror session | 1   |
| --------------- | --- | -------------- | --- |
switch(config)#
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
Mirroring|121

Examples
Creatingamirrorendpointnamedtest:
switch(config)#
|     |     |     | mirror | endpoint |     | test |     |     |
| --- | --- | --- | ------ | -------- | --- | ---- | --- | --- |
Deletingmirrorendpointnamedtest:
|     | switch(config)# |     | no  | mirror endpoint |     | test |     |     |
| --- | --------------- | --- | --- | --------------- | --- | ---- | --- | --- |
Configuringamirrorendpointnamedtest:
|     | 6100(config)# |     | mirror | endpoint | test |     |     |     |
| --- | ------------- | --- | ------ | -------- | ---- | --- | --- | --- |
6100(config-mirror-endpoint-test)#
|     | 6100(config-mirror-endpoint-test)# |     |         |            |     | destination     |           |     |
| --- | ---------------------------------- | --- | ------- | ---------- | --- | --------------- | --------- | --- |
|     | interface                          |     | Specify | interfaces |     | to send traffic |           |     |
|     | 6100(config-mirror-endpoint-test)# |     |         |            |     | destination     | interface |     |
IFNAMELIST An interface, a range or a comma seperated list of interfaces
|     | 6100(config-mirror-endpoint-test)# |     |     |     |     | destination | interface | 1/1/3 |
| --- | ---------------------------------- | --- | --- | --- | --- | ----------- | --------- | ----- |
<cr>
|     | 6100(config-mirror-endpoint-test)# |     |     |     |     | destination | interface | 1/1/3 |
| --- | ---------------------------------- | --- | --- | --- | --- | ----------- | --------- | ----- |
6100(config-mirror-endpoint-test)#
6100(config-mirror-endpoint-test)# source 1.1.1.1 destination 1.1.1.2 id 1 vrf
default
6100(config-mirror-endpoint-test)#
Onlyphysicalportscanbeconfiguredasinterfaceformirror-endpointdestination.LAGportisnotsupportedas
interfaceformirror-endpointdestination.
Themaximumallowednumberofdestinationinterfacesforbothmirror-sessionandmirror-endpointis1.
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        |     | History     |         |         |     |                                            |     |     |
| -------------- | --- | ----------- | ------- | ------- | --- | ------------------------------------------ | --- | --- |
| Release        |     |             |         |         |     | Modification                               |     |     |
| 10.13.1000     |     |             |         |         |     | Addedsupportfor4100i,6000,and6100switches. |     |     |
| 10.07orearlier |     |             |         |         |     | --                                         |     |     |
| Command        |     | Information |         |         |     |                                            |     |     |
| Platforms      |     |             | Command | context |     | Authority                                  |     |     |
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400 |        |                |     |            |     | rightsforthiscommand. |     |     |
| ---- | ------ | -------------- | --- | ---------- | --- | --------------------- | --- | --- |
| show | mirror |                |     |            |     |                       |     |     |
| show | mirror | [<SESSION-ID>] |     | [vsx-peer] |     |                       |     |     |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 122

Description

Shows information about mirroring sessions. If <SESSION-ID> is not specified, then the command
shows a summary of all configured mirroring sessions. If <SESSION-ID> is specified, then the command
shows detailed information about the specified mirroring session.

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

Information in the Admin Status column of the command output indicates the configured status. The
admin status is one of the following values:

n enable: The mirroring session is enabled.

n disable: The mirroring session has been configured but not yet enabled, or has been disabled.

Information in the Operation Status colum indicates the status of the mirroring session. Operation
status is one of the following values:

n dest_doesnt_exist:The configured destination interface is not found in the system. The mirroring

session cannot be enabled.

n destination_shutdown: The mirroring session is enabled, but the destination interface is shut

down. No traffic can be monitored.

n disabled: The mirroring session is disabled and is not in an error condition.

n enabled: The mirroring session is enabled.

n external/driver_error: An internal ASIC hardware error occurred.

n hit_active_sessions_capacity: The mirroring session could not be enabled because the maximum

number of supported mirroring sessions are already enabled.

n internal_error: An invalid parameter was passed to the ASIC software layer.

n no_dest_configured: The mirroring session does not have a destination interface configured.

n no_name_configured: A software error occurred. The mirroring session does not have a session ID

in its configuration.

n null_mirror: A software error occurred. The session object reference is invalid.

n out_of_memory: The system is out of memory, reboot recommended.

n tunnel_route_resolution_not_populated: If the destination tunnel IP address is not reachable.

n unknown_error: An unexpected error occurred.

Examples

On the Aruba 6400 Switch Series, interface identification differs.

Showing summary information about all configured mirroring sessions:

switch# show mirror
ID Admin Status

Operation Status

Mirroring | 123

--- ------------- ----------------------------------------------------
| 1 enable  |     | enabled        |     |     |
| --------- | --- | -------------- | --- | --- |
| 2 disable |     | disabled       |     |     |
| 3 disable |     | disabled       |     |     |
| 4 enable  |     | internal_error |     |     |
Showingdetailedinformationaboutasinglemirroringsession:
| switch# show    | mirror    | 3           |              |         |
| --------------- | --------- | ----------- | ------------ | ------- |
| Mirror Session: |           | 3           |              |         |
| Admin Status:   |           | disable     |              |         |
| Operation       | Status:   | disabled    |              |         |
| Comment:        | Monitor   | router port | ingress-only | traffic |
| Source:         | interface | 1/1/2 rx    |              |         |
| Destination:    | interface | 1/1/3       |              |         |
switch#
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show mirror | endpoint |          |     |     |
| ----------- | -------- | -------- | --- | --- |
| show mirror | endpoint | [<NAME>] |     |     |
Description
Showsalistofallconfiguredmirrorendpoints,theirAdminStatusandtheirOperationStatus.
Theoptionalparameterwilldisplaythedetailsofthespecifiedmirrorendpointifitexists.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<NAME> Specifiesnameofthemirrorendpointinstancetobedisplayed.
Examples
Showingasummaryofallconfiguredmirrorendpointsontheswitch:
| switch# show | mirror | endpoint |     |     |
| ------------ | ------ | -------- | --- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 124

| Name | Admin Status | Operation |     | Status |     |
| ---- | ------------ | --------- | --- | ------ | --- |
----- -------------- ----------------------------------------------------
| test    | enable  | enabled  |     |     |     |
| ------- | ------- | -------- | --- | --- | --- |
| monitor | disable | disabled |     |     |     |
Showingthedetailsofenabledmirrorendpointtest:
| switch#       | show mirror        | endpoint    | test |         |                  |
| ------------- | ------------------ | ----------- | ---- | ------- | ---------------- |
| Mirror        | Endpoint:          | audit       |      |         |                  |
| Admin Status: | enable             |             |      |         |                  |
| Operation     | Status:            | enabled     |      |         |                  |
| Comment:      | Mirror Endpoint    | Audit       |      |         |                  |
| Type: gre     |                    |             |      |         |                  |
| Tunnel:       | source 1.1.1.1     | destination |      | 1.1.1.2 | id 1 vrf default |
| Interface:    | 1/1/3              |             |      |         |                  |
| Output        | Packets: 123456789 |             |      |         |                  |
| Output        | Bytes: 0           |             |      |         |                  |
"OutputPackets"in"showmirrorendpoint[name]"isonlysupportedforstatistics.
"OutputBytes"in"showmirrorendpoint[name]"isnotsupportedduetoASIClimitation.
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |     |              |     |
| -------------- | ----------- | ------- | --- | ------------ | --- |
| Release        |             |         |     | Modification |     |
| 10.07orearlier |             |         |     | --           |     |
| Command        | Information |         |     |              |     |
| Platforms      | Command     | context |     | Authority    |     |
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
| 6400     | (#)     |           |     | rightsforthiscommand. |     |
| -------- | ------- | --------- | --- | --------------------- | --- |
| shutdown | (mirror | endpoint) |     |                       |     |
shutdown
no shutdown
Description
Enablesmirrorendpointfromitsdefaultdisabledstate.Toverifythemirrorendpointwassuccessfully
activated,runtheshow mirror endpoint NAMEcommandandverifythattheAdmin Statusand
Operational Statushaschangedfromdisabledtoenabled.Ifthestatusvalueremainsdisabled,
Mirroring|125

consultthesystemlogstodeterminethereasonforactivationfailure.Todisablethemirrorendpoint,
firstdisabletheremotemirrorsessionontheswitchthat'soriginatingthedata.Next,usetheshutdown
commandtodisablethemirrorendpoint.
Examples
Enablingamirrorendpoint:
| switch(config)#                      | mirror | endpoint | test        |
| ------------------------------------ | ------ | -------- | ----------- |
| switch(config-mirror-endpoint-test)# |        |          | no shutdown |
Disablingamirrorendpoint:
| switch(config)#                      | mirror | endpoint | test     |
| ------------------------------------ | ------ | -------- | -------- |
| switch(config-mirror-endpoint-test)# |        |          | shutdown |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config
| 6300 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
| 6400 |     |     | rightsforthiscommand.                              |
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
<SOURCE-IP> SpecifiesL3encapsulatedIPv4sourceintheformA.B.C.D.
<DESTINATION-IP> SpecifiesL3encapsulatedIPv4destinationintheformA.B.C.D.
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 126

| Parameter  |     |     |     |     | Description                                         |     |
| ---------- | --- | --- | --- | --- | --------------------------------------------------- | --- |
| id         |     |     |     |     | Specifiestunnelidentifierfromtheencapsulatedpacket. |     |
| <VRF_NAME> |     |     |     |     | SpecifiesthenameofVRF forwhichthetunnelbelongsto.   |     |
Examples
Configuringatunnelparametertoamirrorendpoint:
switch(config-mirror-endpoint-test)# source 1.1.1.1 destination 7.7.7.7 id 1 vrf
| default | type | gre |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |         |     |              |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400      |           |             |     |               | rightsforthiscommand. |               |
| --------- | --------- | ----------- | --- | ------------- | --------------------- | ------------- |
| source    | interface |             |     |               |                       |               |
| source    | interface | {<PORT-NUM> |     | | <LAG-NAME>} |                       | [<DIRECTION>] |
| no source | interface | {<PORT-NUM> |     | |             | <LAG-NAME>}           | [<DIRECTION>] |
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
Mirroring|127

| Parameter |     |     | Description                              |     |     |     |
| --------- | --- | --- | ---------------------------------------- | --- | --- | --- |
| both      |     |     | Mirrorbothtransmittedandreceivedpackets. |     |     |     |
| rx        |     |     | Mirroronlyreceivedpackets.               |     |     |     |
| tx        |     |     | Mirroronlytransmittedpackets.            |     |     |     |
Usage
Thereisalimitofsourceinterfacesineachdirectionofagivenmirrorsession:
|     |     |     | Source | interface | limit per mirror | session (4 |
| --- | --- | --- | ------ | --------- | ---------------- | ---------- |
Switch
|      |     |     | possible | sessions) |     |     |
| ---- | --- | --- | -------- | --------- | --- | --- |
| 6300 |     |     | 64       |           |     |     |
| 6400 |     |     | 64       |           |     |     |
However,thereisapracticallimittotheamountoftrafficthatamirrordestinationcantransmit.For
example,mirroringsessionwithmultiple10Gsourcescanoverwhelmasingle10Gdestination.
Whenadding,removing,orchangingtheconfigurationofasourceportinanenabledmirroringsession,packets
fromothermirrorsourcesusingthesamedestinationportmightbeinterrupted.
Examples
Configuringamirroredtrafficsourceinterface:
switch(config-mirror-1)#
source interface
| LAG-NAME | Enter | a LAG  | name. For | example, | lag10 |     |
| -------- | ----- | ------ | --------- | -------- | ----- | --- |
| PORT-NUM | Enter | a port | number    |          |       |     |
Creatingamirroringsessionandconfiguringasourceinterfacetomirrorbothtransmittedandreceived
packets:
| switch(config)#          | mirror | session | 1         |     |            |     |
| ------------------------ | ------ | ------- | --------- | --- | ---------- | --- |
| switch(config-mirror-1)# |        | source  | interface |     | 1/1/1 both |     |
Creatingasecondmirroringsessionandconfiguringtwosourceinterfaces.Oneportmirroringonly
transmittedpacketsandtheothermirroringbothtransmittedandreceivedpackets:
| switch(config)#          | mirror | session | 2         |     |            |     |
| ------------------------ | ------ | ------- | --------- | --- | ---------- | --- |
| switch(config-mirror-2)# |        | source  | interface |     | 1/1/3 tx   |     |
| switch(config-mirror-2)# |        | source  | interface |     | 1/2/1 both |     |
Removingthefirstsourceinterface:
| switch(config-mirror-2)# |     | no  | source | interface | 1/2/3 |     |
| ------------------------ | --- | --- | ------ | --------- | ----- | --- |
Configuringasourceinterfacetomirrorreceivedpacketsonly:
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 128

| switch(config-mirror-3)# |     |     | source | interface | 1/1/2 rx |
| ------------------------ | --- | --- | ------ | --------- | -------- |
Configuringasourceinterfacetomirrorbothtransmittedandreceivedpackets:
| switch(config-mirror-1)# |     |     | source | interface | 1/1/1 both |
| ------------------------ | --- | --- | ------ | --------- | ---------- |
ConfiguringaLAGassourceinterfacetomirrorbothtransmittedandreceivedpackets:
| switch(config-mirror-4)# |     |     | source | interface | lag1 both |
| ------------------------ | --- | --- | ------ | --------- | --------- |
Stoppingthemirroringofreceivedpacketsfromaconfiguredsourceinterface:
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
Thereisalimitof1024sourceVLANsforagivenmirrorsession.Thereisalsoalimitof4096source
VLANsacrossallmirrorsessions.
SameVLANcanbeconfiguredasamirrorsourceformultiplesessions.
Mirroring|129

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

n If the mirror is configured in the rx or tx direction, the packets are mirrored to the mirror

destination.

n If the mirror is configured in the both direction, two copies of the packets are mirrored to the mirror

destination.

The no form command will cease mirroring traffic from the specified source VLAN and remove the
source from the mirror configuration.

Parameter

VLAN-NUM

direction

Examples

Description

Selects the VLAN number.

Specifies the direction of mirroring. tx (transmit), rx (receive), or
both.

Creating a mirror session and adding a VLAN as a source of traffic in both directions on that port:

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

130

| switch# configure | terminal |     |     |     |
| ----------------- | -------- | --- | --- | --- |
switch(config)#
|                          | mirror | session | 1    |         |
| ------------------------ | ------ | ------- | ---- | ------- |
| switch(config-mirror-1)# |        | source  | vlan | 10 both |
CreatingamirrorsessionandaddingtwoVLANsassourcesoftraffic:
directions:
| switch# configure        | terminal |         |      |       |
| ------------------------ | -------- | ------- | ---- | ----- |
| switch(config)#          | mirror   | session | 2    |       |
| switch(config-mirror-2)# |          | source  | vlan | 10 tx |
switch(config-mirror-2)#
|     |     | source | vlan | 20 both |
| --- | --- | ------ | ---- | ------- |
Configuringthesourceinsession2toreceivebyspecifyingthesourceinterfaceconfiguration:
| switch(config-mirror-2)# |     | source | vlan | 10 rx |
| ------------------------ | --- | ------ | ---- | ----- |
Removingthefirstsourceinterfaceinsession2entirely,andremovingthetransmitdirectionfromthe
othersothatmirroringonlyoccursinthereceivedirection:
| switch(config-mirror-2)# |     | source | vlan | 10 rx |
| ------------------------ | --- | ------ | ---- | ----- |
| switch(config-mirror-2)# |     | source | vlan | 20 tx |
Showingmaximumof1024mirrorsourceVLANsallowed:
| switch(config-mirror-2)# |     | source | vlan | 2000 rx |
| ------------------------ | --- | ------ | ---- | ------- |
The maximum number of source VLANs per mirror session is 1024 in each direction
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |     |              |
| ------------------- | ------- | ------- | --- | ------------ |
| Release             |         |         |     | Modification |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
config
| 6300 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | --- | -------------------------------------------------- |
| 6400 |     |     |     | rightsforthiscommand.                              |
Mirroring|131

Chapter 9
|            |          |            | Monitoring | a device | using SNMP |
| ---------- | -------- | ---------- | ---------- | -------- | ---------- |
| Monitoring | a device | using SNMP |            |          |            |
Configuring SNMP:RefertotheSNMP/MIBGuideforinformationonhowtoaddSNMPsoadevicecan
bemonitoredfromanetworkmanagementsystem(NMS).
Configuring an SNMP trap receiver:RefertotheSNMP/MIBGuideandspecificinformationaboutthe
| show snmp | trapcommandtoenableSNMPtraps. |     |     |     |     |
| --------- | ----------------------------- | --- | --- | --- | --- |
132
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries)

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

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

133

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

All PoE configuration commands except quick-poe, threshold configuration and always-on poe
configuration are entered at the config-if context. The PoE threshold command is used at the system
level whereas the always-on poe and power-over-ethernet quick-poe commands are set at the slot
level. These commands can only be configured in the global configuration context.

lldp dot3 poe
lldp dot3 poe
no lldp dot3 poe

Description

Enables 802.3 TLV list in LLDP to advertise for Power over Ethernet Data Link Layer Classification. LLDP
dot3 TLV is by default enabled for PoE.

The no form of this command disables 802.3 TLV list in LLDP.

Examples

On the Aruba 6400 Switch Series, interface identification differs.

Enabling 802.3 TLV list in LLDP:

switch(config)# interface 1/1/1
switch(config-if)# lldp dot3 poe

Disabling 802.3 TLV list in LLDP:

switch(config-if)# no lldp dot3 poe

For more information on features that use this command, refer to the Monitoring Guide for your switch model.

Command History

Release

10.07 or earlier

Modification

--

Power-over-Ethernet | 134

| Command Information |         |         |     |           |
| ------------------- | ------- | ------- | --- | --------- |
| Platforms           | Command | context |     | Authority |
config-if
| 6300         |                         |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ------------ | ----------------------- | --- | --- | -------------------------------------------------- |
| 6400         |                         |     |     | rightsforthiscommand.                              |
| lldp med     | poe                     |     |     |                                                    |
| lldp med poe | [priority-override]     |     |     |                                                    |
| no lldp med  | poe [priority-override] |     |     |                                                    |
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
OntheAruba6400SwitchSeries,interfaceidentificationdiffers.
EnablinganddisablingLLDPMEDPoE:
| switch(config)#    |     | interface | 1/1/1 |     |
| ------------------ | --- | --------- | ----- | --- |
| switch(config-if)# |     | lldp      | med   | poe |
| switch(config-if)# |     | no lldp   | med   | poe |
EnablinganddisablingLLDPMEDPoEpriorityoverride:
| switch(config-if)# |     | lldp | med | poe priority-override |
| ------------------ | --- | ---- | --- | --------------------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |     |              |
| ------------------- | ------- | ------- | --- | ------------ |
| Release             |         |         |     | Modification |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
config-if
| 6300 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | --- | -------------------------------------------------- |
| 6400 |     |     |     | rightsforthiscommand.                              |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 135

power-over-ethernet
power-over-ethernet
no power-over-ethernet
Description
Enablesper-interfacepowerdistribution.Per-portpowerisenabledbydefaultwithprioritylow.PoE
cannotbedisabledforindividualportswhenQuickPoEisenabledfortheentireswitchorlinemodule.
Thenoformofthiscommanddisablesper-interfacepowerdistribution.
Examples
OntheAruba6400SwitchSeries,interfaceidentificationdiffers.
Enablingper-interfacepowerdistribution:
| switch(config)#    |     | interface |                     | 1/1/1 |     |     |
| ------------------ | --- | --------- | ------------------- | ----- | --- | --- |
| switch(config-if)# |     |           | power-over-ethernet |       |     |     |
Disablingper-interfacepowerdistribution:
| switch(config-if)# |     |     | no power-over-ethernet |     |     |     |
| ------------------ | --- | --- | ---------------------- | --- | --- | --- |
ShowingQuickPoEenabled:
| switch(config)# |     | power-over-ethernet |                     |          | quick-poe  | 1/1             |
| --------------- | --- | ------------------- | ------------------- | -------- | ---------- | --------------- |
| switch(config)# |     | no                  | power-over-ethernet |          |            |                 |
| Interface       | PoE | cannot              | be                  | disabled | when Quick | PoE is enabled. |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |     |         |     |              |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| Release        |             |     |         |     | Modification |     |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400                   |     |             |             |             | rightsforthiscommand. |        |
| ---------------------- | --- | ----------- | ----------- | ----------- | --------------------- | ------ |
| power-over-ethernet    |     |             |             | allocate-by |                       |        |
| power-over-ethernet    |     | allocate-by |             |             | {usage | class}       |        |
| no power-over-ethernet |     |             | allocate-by |             | {usage |              | class} |
Description
Power-over-Ethernet|136

Configures the power allocation method. Power allocation method is initially based on usage. PSE
Allocated power value will change to LLDP negotiated power if and when LLDP exchange takes place
between PSE and PD. When there is no LLDP negotiation, PSE Allocated Power Value will be the actual
instantaneous power draw and reserve power based on actual consumption. In allocate-by class, power
allocation is based on PD requested class and PSE allocated power value will be the LLDP negotiated
power when LLDP exchange takes place between PSE and PD. When there is no LLDP negotiation, PSE
Allocate Power will be based on PD class. Reserve power is based on PD Class. By default, power
allocation is by usage.

The power allocation method can be changed on an interface through port-access (User roles or
RADIUS). An allocation method when configured through port-access will replace the user configured
method.

The no form of this command resets the action to default.

Parameter

Description

usage

class

Usage

Configures the usage-based allocation method.

Configures the class-based allocation method.

If you enable pd-class-override for an interface, the allocate-by configuration of that interface will be
automatically changed to class. However, if you change the allocation method to usage when pd-class-
override is still enabled, you will receive an error message stating that "The power allocation method
cannot be changed when pd-class-override is enabled."

To remove pd-class-override, you can use the no power-over-ethernet pd-class-override command .
It is important to note that pd-class-override requires the allocation method to be set to class and is
enforced when configured through CLI. However, if you override the allocation method to usage via
port-access, pd-class-override will not be in effect. Therefore, it is recommended that you do not
override the allocation method to usage through port-access on interfaces configured with pd-class-
override.

Examples

On the Aruba 6400 Switch Series, interface identification differs.

Configuring the power allocation method:

switch(config)# interface 1/1/1
switch(config-if)# power-over-ethernet allocate-by usage
switch(config-if)# power-over-ethernet allocate-by class

Resetting power allocation method:

switch(config-if)# no power-over-ethernet allocate-by class

For more information on features that use this command, refer to the Monitoring Guide for your switch model.

Command History

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

137

| Release             |         |     |         |     | Modification |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- |
| 10.07orearlier      |         |     |         |     | --           |     |
| Command Information |         |     |         |     |              |     |
| Platforms           | Command |     | context |     | Authority    |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400                   |     |           |           |             | rightsforthiscommand. |     |
| ---------------------- | --- | --------- | --------- | ----------- | --------------------- | --- |
| power-over-ethernet    |     |           | always-on |             |                       |     |
| power-over-ethernet    |     | always-on |           | <MODULE-ID> |                       |     |
| no power-over-ethernet |     |           | always-on | <MODULE-ID> |                       |     |
Description
Always-onPoEisafeaturethatprovidestheabilitytotheswitchtocontinuetoprovidepoweracrossa
softreboot.Itisapplicableonlytotheinterfaceswhichwereconnectedanddeliveringbeforethesoft
reboot.Also,powerwillnotbedeliveredifpowertotheswitchisinterrupted.Thiscommandenablesor
disablesthealways-onPoEfeatureattheswitchortheslotlevel.Bydefault,always-onPoEisenabledat
theswitchortheslotlevel.
Thenoformofthiscommanddisablespowerdistributiononsoftreboot.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<MODULE-ID>
Modulenumbertoapplyalways-onPoEconfiguration.
Examples
Enablingper-interfacepowerdistribution:
| switch(config)# |     | power-over-ethernet |     |     | always-on | 1/1 |
| --------------- | --- | ------------------- | --- | --- | --------- | --- |
Disablingper-interfacepowerdistribution:
| switch(config)# |     | no  | power-over-ethernet |     | always-on | 1/1 |
| --------------- | --- | --- | ------------------- | --- | --------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |     |     |     |     |              |     |
| ------------------- | --- | --- | --- | --- | ------------ | --- |
| Release             |     |     |     |     | Modification |     |
| 10.07orearlier      |     |     |     |     | --           |     |
| Command Information |     |     |     |     |              |     |
Power-over-Ethernet|138

| Platforms | Command |     | context | Authority |     |     |     |     |
| --------- | ------- | --- | ------- | --------- | --- | --- | --- | --- |
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
OntheAruba6400SwitchSeries,interfaceidentificationdiffers.
SettingPoEassignedclass:
| switch(config)#    |     | interface | 1/1/1               |     |                |     |     |     |
| ------------------ | --- | --------- | ------------------- | --- | -------------- | --- | --- | --- |
| switch(config-if)# |     |           | power-over-ethernet |     | assigned-class |     |     | 4   |
ResettingPoEassignedclasstodefault:
| switch(config-if)# |     |     | no power-over-ethernet |     | assigned-class |     |     | 4   |
| ------------------ | --- | --- | ---------------------- | --- | -------------- | --- | --- | --- |
ShowingQuickPoEenabled:
| switch(config)# |     | power-over-ethernet |       |     | quick-poe      | 1/1 |     |     |
| --------------- | --- | ------------------- | ----- | --- | -------------- | --- | --- | --- |
| switch(config)# |     | interface           | 1/1/1 |     |                |     |     |     |
| switch(config)# |     | power-over-ethernet |       |     | assigned-class |     | 4   |     |
Interface assigned class cannot be configured when Quick PoE is enabled.
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |     |     |     |              |     |     |     |     |
| ------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| Release             |     |     |     | Modification |     |     |     |     |
| 10.07orearlier      |     |     |     | --           |     |     |     |     |
| Command Information |     |     |     |              |     |     |     |     |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 139

| Platforms | Command |     | context |     | Authority |     |     |
| --------- | ------- | --- | ------- | --- | --------- | --- | --- |
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
| switch(config-if)# |     |     | no power-over-ethernet |     |     | power-pairs | alt-a |
| ------------------ | --- | --- | ---------------------- | --- | --- | ----------- | ----- |
This setting configures the interface to deliver power on the ALT-A
Power-over-Ethernet|140

and ALT-B cable pairs. This is the default and most devices work
properly with this setting, however some older Class 0-4 devices may
| not operate | correctly. |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | --- |
| Continue    | (y/n)?     | y   |     |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |         |     |                   |     |
| ------------------- | ------- | ------- | --- | ----------------- | --- |
| Release             |         |         |     | Modification      |     |
| 10.09               |         |         |     | CommandIntroduced |     |
| Command Information |         |         |     |                   |     |
| Platforms           | Command | context |     | Authority         |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400                   |     |                |                | rightsforthiscommand. |     |
| ---------------------- | --- | -------------- | -------------- | --------------------- | --- |
| power-over-ethernet    |     |                | pre-std-detect |                       |     |
| power-over-ethernet    |     | pre-std-detect |                |                       |     |
| no power-over-ethernet |     | pre-std-detect |                |                       |     |
Description
BeforeIEEE802.3releasedthefirstPoweroverEthernetstandard(802.3af),vendorshadshippedPoE
capableswitchesandPD's.ArubaswitchesarebackwardcompatibleandwillsupportbothIEEE
standardandpre-standard802.3afPoweroverEthernetPD'sconcurrently.ThisCLIallowstheuserto
enableordisablepre-802.3af-standarddevicedetectionandpoweringonthespecificport.Whenpre-
std-detectisenabled,powerwillbedeliveredonPairAonly.Defaultisdisabled.
Thenoformofthiscommandresetstheactiontodefault.
Examples
OntheAruba6400SwitchSeries,interfaceidentificationdiffers.
Enablingpre-standarddevicedetection:
| switch(config)#    |     | interface           | 1/1/1 |     |                |
| ------------------ | --- | ------------------- | ----- | --- | -------------- |
| switch(config-if)# |     | power-over-ethernet |       |     | pre-std-detect |
Disablingpre-standarddevicedetection:
| switch(config-if)# |     | no power-over-ethernet |     |     | pre-std-detect |
| ------------------ | --- | ---------------------- | --- | --- | -------------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 141

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
| switch(config-if)# |     |     | no power-over-ethernet |     | priority high |
| ------------------ | --- | --- | ---------------------- | --- | ------------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |     |         |              |     |
| ------------------- | ------- | --- | ------- | ------------ | --- |
| Release             |         |     |         | Modification |     |
| 10.07orearlier      |         |     |         | --           |     |
| Command Information |         |     |         |              |     |
| Platforms           | Command |     | context | Authority    |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6400
Power-over-Ethernet|142

| power-over-ethernet    |     |           | quick-poe |             |     |     |
| ---------------------- | --- | --------- | --------- | ----------- | --- | --- |
| power-over-ethernet    |     | quick-poe |           | <MODULE-ID> |     |     |
| no power-over-ethernet |     |           | quick-poe | <MODULE-ID  |     |     |
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
OntheAruba6400SwitchSeries,interfaceidentificationdiffers.
EnablinganddisablingquickPoE:
| switch(config)# |     | power-over-ethernet |     |     | quick-poe | 1/2 |
| --------------- | --- | ------------------- | --- | --- | --------- | --- |
switch(config)#
|                    |     | no  | power-over-ethernet |     | quick-poe | 1/2 |
| ------------------ | --- | --- | ------------------- | --- | --------- | --- |
| switch(config-if)# |     |     | power-over-ethernet |     | quick-poe | 1/1 |
PoE must be enabled on all interfaces before enabling Quick PoE
| switch(config-if)# |     |     | power-over-ethernet |     | quick-poe | 1/3 |
| ------------------ | --- | --- | ------------------- | --- | --------- | --- |
All interfaces must use the default assigned class before enabling Quick PoE
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |     |         |     |              |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- |
| Release             |         |     |         |     | Modification |     |
| 10.07orearlier      |         |     |         |     | --           |     |
| Command Information |         |     |         |     |              |     |
| Platforms           | Command |     | context |     | Authority    |     |
config-if
| 6300 |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | --- | -------------------------------------------------- | --- |
| 6400 |     |     |     |     | rightsforthiscommand.                              |     |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 143

| power-over-ethernet    |     |           | threshold |              |     |     |     |
| ---------------------- | --- | --------- | --------- | ------------ | --- | --- | --- |
| power-over-ethernet    |     | threshold |           | <PERCENTAGE> |     |     |     |
| no power-over-ethernet |     |           | threshold | <PERCENTAGE> |     |     |     |
Description
Setsthethresholdatwhichthesystemwillsendanexcesspowerconsumptionnotificationtrap.Default
valueis80percentage.
Thenoformofthiscommandresetstheactiontodefault.
| Parameter    |     |     |     |     | Description                                    |     |     |
| ------------ | --- | --- | --- | --- | ---------------------------------------------- | --- | --- |
| <PERCENTAGE> |     |     |     |     | Excesspowerconsumptiontrapthreshold.Range1-99. |     |     |
Examples
Settingthepower-over-ethernetthreshold:
| switch(config)# |     | power-over-ethernet |     |     | threshold | 75  |     |
| --------------- | --- | ------------------- | --- | --- | --------- | --- | --- |
Resettingthepower-over-ethernetthresholdtodefault:
| switch(config-if)# |     |     | no power-over-ethernet |     |     | threshold | 75  |
| ------------------ | --- | --- | ---------------------- | --- | --- | --------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |     |         |     |              |     |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- | --- |
| Release             |         |     |         |     | Modification |     |     |
| 10.07orearlier      |         |     |         |     | --           |     |     |
| Command Information |         |     |         |     |              |     |     |
| Platforms           | Command |     | context |     | Authority    |     |     |
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400                   |     |      |      |     | rightsforthiscommand. |     |     |
| ---------------------- | --- | ---- | ---- | --- | --------------------- | --- | --- |
| power-over-ethernet    |     |      | trap |     |                       |     |     |
| power-over-ethernet    |     | trap |      |     |                       |     |     |
| no power-over-ethernet |     |      | trap |     |                       |     |     |
Description
Thiscommandenables/disablestheSNMPtrapgenerationforPoErelatedeventsatsystemlevel.PoE
trapgenerationisenabledbydefault.
ThenoformofthiscommandresetstheprioritytodefaultPoEpriority"low".
Examples
Power-over-Ethernet|144

EnablingSNMPtrapgenerationforPoE:
| switch(config)# |     |     | power-over-ethernet |     | trap |     |
| --------------- | --- | --- | ------------------- | --- | ---- | --- |
DisablingSNMPtrapgenerationforPoE:
| switch(config-if)# |     |     | no power-over-ethernet |     |     | trap |
| ------------------ | --- | --- | ---------------------- | --- | --- | ---- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |         |     |              |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecution
| 6400      |              |       |                  |     | rightsforthiscommand. |     |
| --------- | ------------ | ----- | ---------------- | --- | --------------------- | --- |
| show      | lldp         | local |                  |     |                       |     |
| show lldp | local-device |       | [<INTERFACE-ID>] |     |                       |     |
Description
DisplaysinformationadvertisedbytheswitchiftheLLDPfeatureisenabledbyuser.
| Parameter      |     |     |     |     | Description                                  |     |
| -------------- | --- | --- | --- | --- | -------------------------------------------- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port |     |
Examples
OntheAruba6400SwitchSeries,interfaceidentificationdiffers.
ShowingLLDPlocaldevice:
| switch# | show | lldp | local-device | 1/1/10 |     |     |
| ------- | ---- | ---- | ------------ | ------ | --- | --- |
| Local   | Port | Data |              |        |     |     |
===============
| Port-ID   |        |             | : 1/1/10   |     |     |     |
| --------- | ------ | ----------- | ---------- | --- | --- | --- |
| Port-Desc |        |             | : "1/1/10" |     |     |     |
| Port      | VLAN   | ID          | : 0        |     |     |     |
| PoE       | Plus   | Information |            |     |     |     |
| PoE       | Device | Type        | : Type 2   | PSE |     |     |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 145

| Power         | Source   |        | : Primary |     |     |     |
| ------------- | -------- | ------ | --------- | --- | --- | --- |
| Power         | Priority |        | : low     |     |     |     |
| PSE Allocated |          | Power: | 25.0      | W   |     |     |
| PD Requested  |          | Power  | : 25.0    | W   |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command        | History     |         |         |     |              |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show lldp |          | neighbor |                  |     |     |     |
| --------- | -------- | -------- | ---------------- | --- | --- | --- |
| show lldp | neighbor |          | [<INTERFACE-ID>] |     |     |     |
Description
Displaysdetailedinformationaboutaparticularneighborconnectedtoaparticularinterface.
| Parameter      |     |     |     |     | Description                                  |     |
| -------------- | --- | --- | --- | --- | -------------------------------------------- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port |     |
Examples
OntheAruba6400SwitchSeries,interfaceidentificationdiffers.
ShowingLLDPneighborinformationwhenthereisonlyoneneighbor:
switch#
|          | show         | lldp | neighbor-info |     | 1/1/10              |     |
| -------- | ------------ | ---- | ------------- | --- | ------------------- | --- |
| Port     |              |      |               |     | : 1/1/10            |     |
| Neighbor | Entries      |      |               |     | : 1                 |     |
| Neighbor | Entries      |      | Deleted       |     | : 0                 |     |
| Neighbor | Entries      |      | Dropped       |     | : 0                 |     |
| Neighbor | Entries      |      | Aged-Out      |     | : 0                 |     |
| Neighbor | Chassis-Name |      |               |     | : 84:d4:7e:ce:5d:68 |     |
Neighbor Chassis-Description : ArubaOS (MODEL: 325), Version HPE_ANW IAP
| Neighbor | Chassis-ID         |     |           |     | : 84:d4:7e:ce:5d:68 |      |
| -------- | ------------------ | --- | --------- | --- | ------------------- | ---- |
| Neighbor | Management-Address |     |           |     | : 169.254.41.250    |      |
| Chassis  | Capabilities       |     | Available |     | : Bridge,           | WLAN |
| Chassis  | Capabilities       |     | Enabled   |     | :                   |      |
| Neighbor | Port-ID            |     |           |     | : 84:d4:7e:ce:5d:68 |      |
| Neighbor | Port-Desc          |     |           |     | : eth0              |      |
Power-over-Ethernet|146

| TTL      |         |             |     | : 120     |     |
| -------- | ------- | ----------- | --- | --------- | --- |
| Neighbor | Port    | VLAN        | ID  | :         |     |
| Neighbor | PoEplus | information |     | : DOT3    |     |
| Neighbor | Device  | Type        |     | : TYPE2   | PD  |
| Neighbor | Power   | Priority    |     | : Unkown  |     |
| Neighbor | Power   | Source      |     | : Primary |     |
| Neighbor | Power   | Requested   |     | : 25.0 W  |     |
| Neighbor | Power   | Allocated   |     | : 0.0 W   |     |
| Neighbor | Power   | Supported   |     | : No      |     |
| Neighbor | Power   | Enabled     |     | : No      |     |
| Neighbor | Power   | Class       |     | : 5       |     |
| Neighbor | Power   | Paircontrol |     | : No      |     |
| Neighbor | Power   | Pairs       |     | : SIGNAL  |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History     |         |     |         |              |     |
| ------------------- | ------- | --- | ------- | ------------ | --- |
| Release             |         |     |         | Modification |     |
| 10.07orearlier      |         |     |         | --           |     |
| Command Information |         |     |         |              |     |
| Platforms           | Command |     | context | Authority    |     |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
show power-over-ethernet
Aruba6300SwitchSeries:
| show power-over-ethernet |     |     | [member | <MEMBER-ID>] | [brief] |
| ------------------------ | --- | --- | ------- | ------------ | ------- |
Aruba6400SwitchSeries:
| show power-over-ethernet |     |     | [<MODULE-ID>] | [brief] |     |
| ------------------------ | --- | --- | ------------- | ------- | --- |
Aruba6300,6400SwitchSeries:
| show power-over-ethernet |     |     | [<IFRANGE>] | [brief] |     |
| ------------------------ | --- | --- | ----------- | ------- | --- |
Description
Displaysthestatusinformationofthefullsystem.Displaysthebriefstatusofallportorgivenportif
parameterbriefisused.Displaysthedetailedstatusofgivenport.
| Parameter   |     |     |     | Description                                    |     |
| ----------- | --- | --- | --- | ---------------------------------------------- | --- |
| <MODULE-ID> |     |     |     | Displaysdetailedstatusforthegivenmodule.       |     |
| <IFRANGE>   |     |     |     | Portidentifierrange.                           |     |
| <IFNAME>    |     |     |     | Displaythedetailedstatusofgivenport.           |     |
| brief       |     |     |     | Displaythebriefstatusofallportsorthegivenport. |     |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 147

Examples
Showingsampleoutputforshowpower-over-ethernetonstandaloneboxwithVSFcapabiity:
switch#
show power-over-ethernet
| System Power     | Status   | for     | member | 1               |     |
| ---------------- | -------- | ------- | ------ | --------------- | --- |
| Configured       | Power    | Status  |        | : No redundancy |     |
| Operational      | Power    | Status  |        | : No redundancy |     |
| Total Available  |          | Power   |        | : 740 W         |     |
| Total Failover   |          | Pwr     | Avl    | : 0 W           |     |
| Total Redundancy |          | Power   |        | : 0 W           |     |
| Total Power      | Drawn    |         |        | : 0 W +/-       | 6W  |
| Total Power      | Reserved |         |        | : 0 W           |     |
| Total Remaining  |          | Power   |        | : 740 W         |     |
| Trap Threshold   |          |         |        | : 80 %          |     |
| Trap Enabled     |          |         |        | : Yes           |     |
| Always-on        | PoE      | Enabled |        | : 1/1           |     |
| Quick PoE        | Enabled  |         |        | : None          |     |
| Internal         | Power    |         |        |                 |     |
Total Power
| PS (Watts)          |          |         | Status                |                 |     |
| ------------------- | -------- | ------- | --------------------- | --------------- | --- |
| ----- ------------- |          |         | --------------------- |                 |     |
| 1 0                 |          |         | Absent                |                 |     |
| 2 740               |          |         | Ok                    |                 |     |
| System Power        | Status   | for     | member                | 2               |     |
| Configured          | Power    | Status  |                       | : No redundancy |     |
| Operational         | Power    | Status  |                       | : No redundancy |     |
| Total Available     |          | Power   |                       | : 600 W         |     |
| Total Failover      |          | Pwr     | Avl                   | : 0 W           |     |
| Total Redundancy    |          | Power   |                       | : 0 W           |     |
| Total Power         | Drawn    |         |                       | : 0 W +/-       | 6W  |
| Total Power         | Reserved |         |                       | : 0 W           |     |
| Total Remaining     |          | Power   |                       | : 600 W         |     |
| Trap Threshold      |          |         |                       | : 80 %          |     |
| Trap Enabled        |          |         |                       | : Yes           |     |
| Always-on           | PoE      | Enabled |                       | : None          |     |
| Quick PoE           | Enabled  |         |                       | : None          |     |
| Internal            | Power    |         |                       |                 |     |
Total Power
| PS (Watts)          |     |     | Status                |     |     |
| ------------------- | --- | --- | --------------------- | --- | --- |
| ----- ------------- |     |     | --------------------- |     |     |
| 1 0                 |     |     | Absent                |     |     |
| 2 600               |     |     | Ok                    |     |     |
Showingsampleoutputforpower-over-ethernetmember:
| switch# show    | power-over-ethernet |        |        | member          | 1   |
| --------------- | ------------------- | ------ | ------ | --------------- | --- |
| System Power    | Status              | for    | member | 1               |     |
| Configured      | Power               | Status |        | : No redundancy |     |
| Operational     | Power               | Status |        | : No redundancy |     |
| Total Available |                     | Power  |        | : 740 W         |     |
Power-over-Ethernet|148

| Total          | Failover    | Pwr      | Avl | :   | 0 W   |        |     |     |     |
| -------------- | ----------- | -------- | --- | --- | ----- | ------ | --- | --- | --- |
| Total          | Redundancy  | Power    |     | :   | 0 W   |        |     |     |     |
| Total          | Power       | Drawn    |     | :   | 0 W   | +/- 6W |     |     |     |
| Total          | Power       | Reserved |     | :   | 0 W   |        |     |     |     |
| Total          | Remaining   | Power    |     | :   | 740 W |        |     |     |     |
| Trap Threshold |             |          |     | :   | 80 %  |        |     |     |     |
| Trap Enabled   |             |          |     | :   | No    |        |     |     |     |
| Always-on      | PoE         | Enabled  |     | :   | 1/1   |        |     |     |     |
| Quick          | PoE Enabled |          |     | :   | 1/1   |        |     |     |     |
| Internal       | Power       |          |     |     |       |        |     |     |     |
Total Power
| PS    | (Watts)       |     | Status                |     |     |     |     |     |     |
| ----- | ------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
| ----- | ------------- |     | --------------------- |     |     |     |     |     |     |
| 1     | 0             |     | Absent                |     |     |     |     |     |     |
| 2     | 740           |     | Ok                    |     |     |     |     |     |     |
Showingsampleoutputforpower-over-ethernetbriefinaVSFstack:
| switch#    | show power-over-ethernet |              |             |       | brief |              |          |     |     |
| ---------- | ------------------------ | ------------ | ----------- | ----- | ----- | ------------ | -------- | --- | --- |
| Status and | Configuration            |              | Information |       | for   | PoE          |          |     |     |
| Member     | 1 Power                  | Status       |             |       |       |              |          |     |     |
| Available: |                          | 370 W        | Reserved:   | 55.60 |       | W Remaining: | 314.40 W |     |     |
| Always-on  |                          | PoE Enabled: |             | 1/1   |       |              |          |     |     |
| Quick      | PoE                      | Enabled:     | None        |       |       |              |          |     |     |
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
| Port | En Priority |     | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | --- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 2/1/1 | Yes Low |     | Off | Class | 0.0 | W 0.0 | W Searching | None N/A | N/A |
| ----- | ------- | --- | --- | ----- | --- | ----- | ----------- | -------- | --- |
2/1/2 Yes Critical Off Usage 0.0 W 0.0 W Searching None N/A N/A
| 2/1/3      | Yes High |         | Off    | Class | 0.0 | W 0.0          | W Searching | None N/A | N/A |
| ---------- | -------- | ------- | ------ | ----- | --- | -------------- | ----------- | -------- | --- |
| 2/1/4      | No Low   |         | On     | Usage | 0.0 | W 0.0          | W Disabled  | None N/A | N/A |
| *This port | may      | go down | in the | event | of  | a PSU failure. |             |          |     |
^This port is power demoted due to user config or power availabilty.
Showingsampleoutputforpower-over-ethernetbriefforaChassissystem:
| switch#    | show power-over-ethernet |     |             |     | brief |     |     |     |     |
| ---------- | ------------------------ | --- | ----------- | --- | ----- | --- | --- | --- | --- |
| Status and | Configuration            |     | Information |     | for   | PoE |     |     |     |
| Power      | Status                   |     |             |     |       |     |     |     |     |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 149

| Available: | 370 W        | Reserved: | 55.60           |     | W Remaining: | 314.40 W |     |     |
| ---------- | ------------ | --------- | --------------- | --- | ------------ | -------- | --- | --- |
| Always-on  | PoE Enabled: |           | 1/1,1/3,1/4,1/7 |     |              |          |     |     |
| Quick      | PoE Enabled: | None      |                 |     |              |          |     |     |
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
For6400Switchseries:
| switch#    | show power-over-ethernet |             |      | 1/1/1-1/1/2 | brief            |          |     |     |
| ---------- | ------------------------ | ----------- | ---- | ----------- | ---------------- | -------- | --- | --- |
| Status and | Configuration            | Information |      | for         | port 1/1/1-1/1/2 |          |     |     |
| Power      | Status                   |             |      |             |                  |          |     |     |
| Available: | 360 W                    | Reserved:   | 0.00 | W           | Remaining:       | 360.00 W |     |     |
| Always-on  | PoE Enabled:             |             | 1/1  |             |                  |          |     |     |
| Quick      | PoE Enabled:             | None        |      |             |                  |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
Power-over-Ethernet|150

| Port | En  | Priority | Detect | Act | Rsrvd | Draw | Status |     | Sign |     |     |
| ---- | --- | -------- | ------ | --- | ----- | ---- | ------ | --- | ---- | --- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes | Low | Off | Usage | 0.0 | W 0.0 | W Searching |     | N/A | N/A | N/A |
| ----- | --- | --- | --- | ----- | --- | ----- | ----------- | --- | --- | --- | --- |
| 1/1/2 | Yes | Low | Off | Usage | 0.6 | W 0.0 | W Searching |     | N/A | N/A | N/A |
Showingsampleoutputforpower-over-ethernetforamissinglinecard:
| switch# | show   | power-over-ethernet |     | 1/3      | brief |     |     |     |     |     |     |
| ------- | ------ | ------------------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- |
| Module  | 1/3 is | not physically      |     | present. |       |     |     |     |     |     |     |
Showingsampleoutputforpower-over-ethernetbriefforamissingmember:
| switch# | show | power-over-ethernet |     | member   | 3   | brief |     |     |     |     |     |
| ------- | ---- | ------------------- | --- | -------- | --- | ----- | --- | --- | --- | --- | --- |
| Member  | 3 is | not physically      |     | present. |     |       |     |     |     |     |     |
Showingsampleoutputforpower-over-ethernetportwhenphysicalinterfaceisnotpresent:
| switch#   | show  | power-over-ethernet |          | 2/1/1 |     |     |     |     |     |     |     |
| --------- | ----- | ------------------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Interface | 2/1/1 | is not              | present. |       |     |     |     |     |     |     |     |
Showingpower-over-ethernetportwithdualsignaturePDconnected:
| switch#   | show       | power-over-ethernet |     | 1/1/1       |     |               |        |          |     |              |     |
| --------- | ---------- | ------------------- | --- | ----------- | --- | ------------- | ------ | -------- | --- | ------------ | --- |
| Status    | and        | Configuration       |     | Information | for | port 1/1/1*   |        |          |     |              |     |
| Power     | Enable     |                     | :   | Yes         |     | PD signature  |        |          |     | : Dual       |     |
| PoE PairA |            | Status              | :   | Delivering  |     | PoE PairB     | Status |          |     | : Delivering |     |
| Alloc-by  | Configured |                     | :   | Class       |     | Alloc-by      | Actual |          |     | : Class      |     |
| User      | Profile    | Priority            | :   | High        |     | Port Config   |        | Priority |     | : Low        |     |
| Port      | Priority   |                     | :   | High        |     | Pre-std       | Detect |          |     | : Disabled   |     |
| PD Type   |            |                     | :   | Type3       |     | User Assigned |        | Class    |     | : Class6     |     |
PairA Requested Class : Class1 PairB Requested Class : Class4
| PairA    | Assigned | Class | :   | Class1   |     | PairB | Assigned | Class      |     | : Class4     |     |
| -------- | -------- | ----- | --- | -------- | --- | ----- | -------- | ---------- | --- | ------------ | --- |
| Fault    | Status   | PairA | :   | None     |     | Fault | Status   | PairB      |     | : None       |     |
| PD Class | Override |       | :   | Disabled |     | Power | Pairs    | Configured |     | : alt-a      |     |
|          |          |       |     |          |     | Power | Pairs    | Applied    |     | : alt-a-and- |     |
alt-b
| PoE Counter |         | Information |     |     |     |            |           |           |     |     |     |
| ----------- | ------- | ----------- | --- | --- | --- | ---------- | --------- | --------- | --- | --- | --- |
| Over        | Current | Cnt PairA   | :   | 0   |     | MPS Absent |           | Cnt PairA |     | : 0 |     |
| Power       | Denied  | Cnt PairA   | :   | 0   |     | Short      | Cnt PairA |           |     | : 0 |     |
| Over        | Current | Cnt PairB   | :   | 0   |     | MPS Absent |           | Cnt PairB |     | : 0 |     |
| Power       | Denied  | Cnt PairB   | :   | 0   |     | Short      | Cnt PairB |           |     | : 0 |     |
Power Information
| PSE Voltage |     |            | :   | 56.3 V |     | PSE Reserved |       | power |     | : 34.0 | W   |
| ----------- | --- | ---------- | --- | ------ | --- | ------------ | ----- | ----- | --- | ------ | --- |
| PD Current  |     | Draw       | :   | 4.1 A  |     | PD Power     | Draw  |       |     | : 24.6 | W   |
| PD Average  |     | Power Draw | :   | 24.0 W |     | PD Peak      | Power | Draw  |     | : 25.1 | W   |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 151

LLDP Information
| MED Override    |            |       |       |      | :   | Enabled       |     |     |     |
| --------------- | ---------- | ----- | ----- | ---- | --- | ------------- | --- | --- | --- |
| MED Priority    |            |       |       |      | :   | High          |     |     |     |
| PSE TLV         | Configured |       |       |      | :   | dot3, med     |     |     |     |
| PSE TLV         | Sent       | Type  |       |      | :   | dot3-ext      |     |     |     |
| PD TLV          | Sent Type  |       |       |      | :   | med, dot3-ext |     |     |     |
| DS PSE          | Allocated  | Power | Value | Alt  | A : | 2.5 W         |     |     |     |
| DS PD Requested |            | Power | Value | Mode | A : | 2.5 W         |     |     |     |
| DS PSE          | Allocated  | Power | Value | Alt  | B : | 25.0 W        |     |     |     |
| DS PD Requested |            | Power | Value | Mode | B : | 25.0 W        |     |     |     |
Showingpower-over-ethernetportwithsinglesignaturePDconnected:
| switch# show  | power-over-ethernet |          |             | 1/1/1      |     |              |          |       |            |
| ------------- | ------------------- | -------- | ----------- | ---------- | --- | ------------ | -------- | ----- | ---------- |
| Status and    | Configuration       |          | Information |            | for | port 1/1/9*  |          |       |            |
| Power Enable  |                     |          | :           | Yes        |     | PD signature |          |       | : None     |
| PoE Port      | Status              |          | :           | Delivering |     | PD Type      |          |       | : Type3    |
| Alloc-by      | Configured          |          | :           | Usage      |     | Alloc-by     | Actual   |       | : Usage    |
| User Profile  |                     | Priority | :           | High       |     | Port Config  | Priority |       | : Low      |
| Port Priority |                     |          | :           | High       |     | Pre-std      | Detect   |       | : Disabled |
| PD Requested  |                     | Class    | :           | Class1     |     | PSE Assigned | Class    |       | : Class1   |
| Fault Status  |                     |          | :           | None       |     | User set     | Assigned | Class | : Class6   |
PD Class Override : Disabled Power Pairs Configured : alt-a-and-alt-
b
|     |     |     |     |     |     | Power Pairs | Applied |     | : alt-a-and-alt- |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | ---------------- |
b
| PoE Counter  | Information |     |     |     |     |            |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- | ---------- | --- | --- | --- |
| Over Current |             | Cnt | :   | 0   |     | MPS Absent | Cnt |     | : 0 |
| Power Denied |             | Cnt | :   | 0   |     | Short Cnt  |     |     | : 0 |
Power Information
| PSE Voltage |       |      | :   | 56.3 V |     | PSE Reserved | power      |     | : 8.6 W |
| ----------- | ----- | ---- | --- | ------ | --- | ------------ | ---------- | --- | ------- |
| PD Current  | Draw  |      | :   | 1.1 A  |     | PD Power     | Draw       |     | : 8.6 W |
| PD Average  | Power | Draw | :   | 8.0 W  |     | PD Peak      | Power Draw |     | : 9.1 W |
LLDP Information
| LLDP Detect   |            |             |       | : Disabled |     |     |     |     |     |
| ------------- | ---------- | ----------- | ----- | ---------- | --- | --- | --- | --- | --- |
| PSE TLV       | Configured |             |       | : N/A      |     |     |     |     |     |
| PSE TLV       | Sent       | Type        |       | : N/A      |     |     |     |     |     |
| PD TLV        | Sent Type  |             |       | : N/A      |     |     |     |     |     |
| PSE Allocated |            | Power       | Value | : 0.0      | W   |     |     |     |     |
| PD Requested  |            | Power Value |       | : 0.0      | W   |     |     |     |     |
Showingpower-over-ethernetforaportrange:
| switch# show | power-over-ethernet |     |             | 1/1/3-1/1/4 |     |            |     |     |     |
| ------------ | ------------------- | --- | ----------- | ----------- | --- | ---------- | --- | --- | --- |
| Status and   | Configuration       |     | Information |             | for | port 1/1/3 |     |     |     |
Power-over-Ethernet|152

| Power Enable  |          | : Yes        | PD signature |          |       | : None     |
| ------------- | -------- | ------------ | ------------ | -------- | ----- | ---------- |
| PoE Port      | Status   | : Delivering | PD Type      |          |       | : Type3    |
| Alloc-by      | Config   | : Usage      | Alloc-by     | Actual   |       | : Usage    |
| User Profile  | Priority | : High       | Port Config  | Priority |       | : Low      |
| Port Priority |          | : High       | Pre-std      | Detect   |       | : Disabled |
| PD Requested  | Class    | : Class1     | PSE Assigned | Class    |       | : Class1   |
| Fault Status  |          | : None       | User set     | Assigned | Class | : Class6   |
PD Class Override : Disabled Power Pairs Configured : alt-a-and-alt-
b
|     |     |     | Power Pairs | Applied |     | : alt-a-and-alt- |
| --- | --- | --- | ----------- | ------- | --- | ---------------- |
b
| PoE Counter  | Information |     |            |     |     |     |
| ------------ | ----------- | --- | ---------- | --- | --- | --- |
| Over Current | Cnt         | : 0 | MPS Absent | Cnt |     | : 0 |
| Power Denied | Cnt         | : 0 | Short Cnt  |     |     | : 0 |
Power Information
| PSE Voltage |            | : 56.3 V | PSE Reserved | power      |     | : 8.6 W |
| ----------- | ---------- | -------- | ------------ | ---------- | --- | ------- |
| PD Current  | Draw       | : 1.1 A  | PD Power     | Draw       |     | : 8.6 W |
| PD Average  | Power Draw | : 8.0 W  | PD Peak      | Power Draw |     | : 9.1 W |
LLDP Information
| LLDP Detect   |               | : Disabled   |                 |            |       |            |
| ------------- | ------------- | ------------ | --------------- | ---------- | ----- | ---------- |
| PSE TLV       | Configured    | : N/A        |                 |            |       |            |
| PSE TLV       | Sent Type     | : N/A        |                 |            |       |            |
| PD TLV        | Sent Type     | : N/A        |                 |            |       |            |
| PSE Allocated | Power         | Value : 0.0  | W               |            |       |            |
| PD Requested  | Power Value   | : 0.0        | W               |            |       |            |
| Status and    | Configuration | Information  | for port 1/1/4* |            |       |            |
| Power Enable  |               | : Yes        | PD signature    |            |       | : None     |
| PoE Port      | Status        | : Delivering | PD Type         |            |       | : Type3    |
| Alloc-by      | Config        | : Usage      | Alloc-by        | Actual     |       | : Usage    |
| User Profile  | Priority      | : High       | Port Config     | Priority   |       | : Low      |
| Port Priority |               | : High       | Pre-std         | Detect     |       | : Disabled |
| PD Requested  | Class         | : Class1     | PSE Assigned    | Class      |       | : Class1   |
| Fault Status  |               | : None       | User set        | Assigned   | Class | : Class6   |
| PD Class      | Override      | : Disabled   | Power Pairs     | Configured |       | : alt-a    |
|               |               |              | Power Pairs     | Applied    |       | : alt-a    |
| PoE Counter   | Information   |              |                 |            |       |            |
| Over Current  | Cnt           | : 0          | MPS Absent      | Cnt        |       | : 0        |
| Power Denied  | Cnt           | : 0          | Short Cnt       |            |       | : 0        |
Power Information
| PSE Voltage |            | : 56.3 V | PSE Reserved | power      |     | : 4.3 W |
| ----------- | ---------- | -------- | ------------ | ---------- | --- | ------- |
| PD Current  | Draw       | : 1.1 A  | PD Power     | Draw       |     | : 4.3 W |
| PD Average  | Power Draw | : 4.0 W  | PD Peak      | Power Draw |     | : 4.3 W |
LLDP Information
| LLDP Detect   |            | : Disabled  |     |     |     |     |
| ------------- | ---------- | ----------- | --- | --- | --- | --- |
| PSE TLV       | Configured | : N/A       |     |     |     |     |
| PSE TLV       | Sent Type  | : N/A       |     |     |     |     |
| PD TLV        | Sent Type  | : N/A       |     |     |     |     |
| PSE Allocated | Power      | Value : 0.0 | W   |     |     |     |
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 153

| PD Requested | Power | Value : | 0.0 W |
| ------------ | ----- | ------- | ----- |
Formoreinformationonfeaturesthatusethiscommand,refertotheMonitoringGuideforyourswitchmodel.
| Command History |     |     |                                                   |
| --------------- | --- | --- | ------------------------------------------------- |
| Release         |     |     | Modification                                      |
| 10.09           |     |     | Addedpower-pairsconfigurationintheshowpower-over- |
ethernet<IFRANGE>output.
| 10.07orearlier      |         |         | --                                                   |
| ------------------- | ------- | ------- | ---------------------------------------------------- |
| Command Information |         |         |                                                      |
| Platforms           | Command | context | Authority                                            |
| 6300                |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Power-over-Ethernet|154

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
155
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries)

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
ArubaAirWave|156

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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 157

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

Aruba AirWave | 158

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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 159

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
ArubaAirWave|160

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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 161

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
ArubaAirWave|162

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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 163

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

Aruba AirWave | 164

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
AOS-CX10.15.xxxxMonitoringGuide|(6300,6400SwitchSeries) 165

Chapter 12

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

AOS-CX 10.15.xxxx Monitoring Guide | (6300, 6400 Switch Series)

166

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
SupportandOtherResources|167