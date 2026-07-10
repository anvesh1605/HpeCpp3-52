AOS-CX 10.11 Monitoring
Guide

8400 Switch Series

Published: February 2023
Edition: 2

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
| Contents                                          |                                  |        |         |                    |               | 3   |
| ------------------------------------------------- | -------------------------------- | ------ | ------- | ------------------ | ------------- | --- |
| About                                             | this document                    |        |         |                    |               | 6   |
| Applicableproducts                                |                                  |        |         |                    |               | 6   |
| Latestversionavailableonline                      |                                  |        |         |                    |               | 6   |
| Commandsyntaxnotationconventions                  |                                  |        |         |                    |               | 6   |
| Abouttheexamples                                  |                                  |        |         |                    |               | 7   |
| Identifyingswitchportsandinterfaces               |                                  |        |         |                    |               | 7   |
| Identifyingmodularswitchcomponents                |                                  |        |         |                    |               | 8   |
| Aruba                                             | 8400 switch                      | series | member, | slot, and          | port notation | 9   |
| LineModulesandManagementModules                   |                                  |        |         |                    |               | 9   |
| Monitoring                                        | hardware                         |        | through | visual observation |               | 11  |
| ConfirmingnormaloperationoftheswitchbyreadingLEDs |                                  |        |         |                    |               | 11  |
| Detectingiftheswitchisnotreadyforafailoverevent   |                                  |        |         |                    |               | 12  |
| FindingfaultedcomponentsusingtheswitchLEDs        |                                  |        |         |                    |               | 12  |
| IP Flow                                           | Information                      |        | Export  |                    |               | 14  |
| Flowmonitors                                      |                                  |        |         |                    |               | 14  |
| Flowexporters                                     |                                  |        |         |                    |               | 14  |
| Destinations                                      |                                  |        |         |                    |               | 14  |
| FlowRecords                                       |                                  |        |         |                    |               | 15  |
| ConfiguringIPFlowInformationExport                |                                  |        |         |                    |               | 15  |
|                                                   | Stepone:CreateFlowRecords        |        |         |                    |               | 15  |
|                                                   | Steptwo:Configureflowexporter(s) |        |         |                    |               | 17  |
|                                                   | Stepthree:Configureamonitor(s)   |        |         |                    |               | 18  |
Stepfour:(Optional)EnableApplicationRecognitionandapplyaflowmonitortointer-
|                         | faces     |     |          |          |     | 18  |
| ----------------------- | --------- | --- | -------- | -------- | --- | --- |
| FAQsandTroubleshooting  |           |     |          |          |     | 19  |
| Boot                    | commands  |     |          |          |     | 20  |
| bootfabric-module       |           |     |          |          |     | 20  |
| bootline-module         |           |     |          |          |     | 21  |
| bootmanagement-module   |           |     |          |          |     | 22  |
| bootset-default         |           |     |          |          |     | 23  |
| bootsystem              |           |     |          |          |     | 24  |
| showboot-history        |           |     |          |          |     | 26  |
| Switch                  | system    | and | hardware | commands |     | 28  |
| External                | storage   |     |          |          |     | 29  |
| Externalstoragecommands |           |     |          |          |     | 29  |
|                         | address   |     |          |          |     | 29  |
|                         | directory |     |          |          |     | 30  |
|                         | disable   |     |          |          |     | 31  |
|                         | enable    |     |          |          |     | 31  |
3
AOS-CX10.11MonitoringGuide| (8400SwitchSeries)

|                                        | external-storage                   |            | 32  |
| -------------------------------------- | ---------------------------------- | ---------- | --- |
|                                        | password(external-storage)         |            | 33  |
|                                        | showexternal-storage               |            | 34  |
|                                        | showrunning-configexternal-storage |            | 35  |
|                                        | type                               |            | 35  |
|                                        | username                           |            | 36  |
|                                        | vrf                                |            | 37  |
| IP-SLA                                 |                                    |            | 39  |
| IP-SLAguidelines                       |                                    |            | 39  |
| LimitationswithVoIPSLAs                |                                    |            | 40  |
| IP-SLAcommands                         |                                    |            | 40  |
|                                        | http                               |            | 40  |
|                                        | icmp-echo                          |            | 41  |
|                                        | ip-sla                             |            | 42  |
|                                        | ip-slaresponder                    |            | 43  |
|                                        | showip-slaresponder                |            | 44  |
|                                        | showip-slaresponderresults         |            | 45  |
|                                        | showip-sla<SLA-NAME>               |            | 45  |
|                                        | start-test                         |            | 48  |
|                                        | stop-test                          |            | 49  |
|                                        | tcp-connect                        |            | 49  |
|                                        | udp-echo                           |            | 50  |
|                                        | udp-jitter-voip                    |            | 52  |
|                                        | vrf                                |            | 53  |
|                                        | showinterface                      |            | 54  |
| Mirroring                              |                                    |            | 59  |
| MirroringandsFlow                      |                                    |            | 59  |
| Mirrorstatistics                       |                                    |            | 60  |
| Classifierpoliciesandmirroringsessions |                                    |            | 60  |
| Mirroringcommands                      |                                    |            | 61  |
|                                        | clearmirror                        |            | 61  |
|                                        | comment                            |            | 62  |
|                                        | copytcpdump-pcap                   |            | 63  |
|                                        | copytshark-pcap                    |            | 64  |
|                                        | destinationcpu                     |            | 64  |
|                                        | destinationinterface               |            | 65  |
|                                        | destinationtunnel                  |            | 66  |
|                                        | diagnostic                         |            | 68  |
|                                        | diagutilitiestcpdump               |            | 69  |
|                                        | disable                            |            | 71  |
|                                        | enable                             |            | 72  |
|                                        | mirrorsession                      |            | 73  |
|                                        | showmirror                         |            | 73  |
|                                        | sourceinterface                    |            | 75  |
|                                        | sourcevlan                         |            | 77  |
| Monitoring                             | a device                           | using SNMP | 80  |
| Breakout                               | cable support                      |            | 81  |
| Limitationswithbreakoutcablesupport    |                                    |            | 81  |
| Breakoutcablesupportcommands           |                                    |            | 81  |
|                                        | split                              |            | 81  |
| Aruba AirWave                          |                                    |            | 84  |
Contents|4

| SNMPsupportandAirWave                            |                      |           | 84  |
| ------------------------------------------------ | -------------------- | --------- | --- |
|                                                  | SNMPontheswitch      |           | 84  |
| SupportedfeatureswithAirWaveandtheAOS-CXswitch   |                      |           | 85  |
| ConfiguringtheAOS-CXswitchtobemonitoredbyAirWave |                      |           | 85  |
| AirWavecommands                                  |                      |           | 86  |
|                                                  | logging              |           | 86  |
|                                                  | snmp-servercommunity |           | 88  |
|                                                  | snmp-serverhost      |           | 89  |
|                                                  | snmp-servervrf       |           | 91  |
|                                                  | snmpv3context        |           | 91  |
|                                                  | snmpv3user           |           | 92  |
| Support                                          | and Other            | Resources | 95  |
| AccessingArubaSupport                            |                      |           | 95  |
| AccessingUpdates                                 |                      |           | 96  |
|                                                  | ArubaSupportPortal   |           | 96  |
|                                                  | MyNetworking         |           | 96  |
| WarrantyInformation                              |                      |           | 96  |
| RegulatoryInformation                            |                      |           | 96  |
| DocumentationFeedback                            |                      |           | 97  |
5
AOS-CX10.11MonitoringGuide| (8400SwitchSeries)

Chapter 1
About this document
| About | this document |     |     |
| ----- | ------------- | --- | --- |
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedfor
administratorsresponsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
| Applicable | products |     |     |
| ---------- | -------- | --- | --- |
Thisdocumentappliestothefollowingproducts:
n Aruba8400SwitchSeries(JL366A,JL363A,JL687A)
| Latest | version | available | online |
| ------ | ------- | --------- | ------ |
Updatestothisdocumentcanoccurafterinitialpublication.Forthelatestversionsofproduct
documentation,seethelinksprovidedinSupportandOtherResources.
| Command    | syntax | notation | conventions |
| ---------- | ------ | -------- | ----------- |
| Convention |        | Usage    |             |
example-text Identifiescommandsandtheiroptionsandoperands,codeexamples,
filenames,pathnames,andoutputdisplayedinacommandwindow.Items
thatappearliketheexampletextinthepreviouscolumnaretobeentered
exactlyasshownandarerequiredunlessenclosedinbrackets([ ]).
example-text Incodeandscreenexamples,indicatestextenteredbyauser.
Anyofthefollowing: Identifiesaplaceholder—suchasaparameteroravariable—thatyoumust
n <example-text> substitutewithanactualvalueinacommandorincode:
<example-text>
n
|     |     | n Foroutputformatswhereitalictextcannotbedisplayed,variables |     |
| --- | --- | ------------------------------------------------------------ | --- |
n example-text
areenclosedinanglebrackets(< >).Substitutethetext—including
n example-text
theenclosinganglebrackets—withanactualvalue.
|     |     | n Foroutputformatswhereitalictextcanbedisplayed,variables |     |
| --- | --- | --------------------------------------------------------- | --- |
mightormightnotbeenclosedinanglebrackets.Substitutethe
textincludingtheenclosinganglebrackets,ifany,withanactual
value.
|
Verticalbar.AlogicalORthatseparatesmultipleitemsfromwhichyoucan
chooseonlyone.
Anyspacesthatareoneithersideoftheverticalbarareincludedfor
readabilityandarenotarequiredpartofthecommandsyntax.
{ } Braces.Indicatesthatatleastoneoftheencloseditemsisrequired.
| [ ] |     | Brackets.Indicatesthattheencloseditemoritemsareoptional. |     |
| --- | --- | -------------------------------------------------------- | --- |
6
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

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
format:
member/slot/port

On the 8400 Switch Series

About this document | 7

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

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

8

|            |               |         |           |               |        | Chapter       | 2     |
| ---------- | ------------- | ------- | --------- | ------------- | ------ | ------------- | ----- |
|            |               | Aruba   | 8400      | switch        | series | member,       | slot, |
|            |               |         |           |               | and    | port notation |       |
| Aruba 8400 | switch series | member, | slot, and | port notation |        |               |       |
Thesoftwarenotationfordescribingmember,slot,andportinformationdependsontheswitch
hardware.
ThephysicalinterfacesontheAruba8400SwitchSeriesusetheformat:
member/slot/port
member
Specifiesthechassisnumber.Inthisreleaseofthesoftware,thevalueofmemberisalways1.
slot
Specifiesphysicallocationintheswitchchassis.
port
Specifiesthephysicalportonthemodule.
Theslotnumbersareuniquetoeachtypeofcomponent—incontrasttobeinguniquewithinachassis.
| Line Modules | and | Management |     | Modules |     |     |     |
| ------------ | --- | ---------- | --- | ------- | --- | --- | --- |
Linemodulesareonthefrontoftheswitchinslots1/1through1/4and1/7through1/10.
Thenumberofportsdependonthelinemodule.Linemoduleportsarelabeledinsoftwareasportor
interface,dependingonthecontext.
Forexample,interface 1/1/1isthelogicalinterfaceassociatedwiththephysicalinterfacemember1,
slot1,port1.
Managementmodulesareonthefrontoftheswitchinslots1/5and1/6.
Figure1 Aruba8400SwitchSerieslinemoduleandmanagementmoduleslots
Power supplies
Powersuppliesareonthefrontoftheswitchbehindthebezelabovethelinemodulesandmanagement
modules.PowersuppliesarelabeledinsoftwareasMember/PSU:1/1through1/4.
9
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- | --- |

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

Aruba 8400 switch series member, slot, and port notation | 10

Monitoring hardware through visual
observation

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

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

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
ThestandbymanagementmodulehealthLEDisSlowFlashGreenwhentheserviceoperating
n
systemisrunningorduringanoperatingsystemupdate.
n ThestandbymanagementmoduleBootingLEDisSlowFlashGreenwhentheAOS-CX
operatingsystemisbooting.
| n Thestandbymanagementstateactive(Actv)LEDisOff.  |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- |
| n Thestandbymanagementstatestandby(Stby)LEDisOff. |     |     |     |     |     |
OntheactivemanagementmoduleintheStatusFrontManagementModulessection,theLED
n
forthestandbymanagementmoduleisSlowFlashGreen.
3. Detectifafabricmoduleisshutdownornotpresent.Ifafabricmoduleisshutdownornot
present,theLEDstatesareasfollows:
n Ontheactivemanagementmodule,intheStatusRearsection,theLEDforthefabricmoduleis
Off.
| n Onthereardisplaymodule,theLEDforthefabricmoduleisOff. |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- |
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

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

13

Chapter 4

IP Flow Information Export

IP Flow Information Export

IP Flow Information Export (IPFIX) is an embedded network flow analysis tool that compiles
characteristic and measured properties of flows and sends flow reports to external flow collectors. IPFIX
is configurable via CLI or REST. With IPFIX, customers configure flow records with match (key) fields and
collection (non-key) fields. Match fields are the set of fields that define a flow, such as IP address or UDP
port. Collection fields are the set of fields that identify information to collect for a flow, such as packet
and byte counters.

Compatibility with Application Recognition and Traffic Insight

The AOS-CX traffic insight feature allows monitoring of large amount of data that it collects from
various flow exporters like IPFIX, and provides the ability to filter, aggregate, and sort the data based on
user flow monitor requests. Traffic insight tracks different monitor requests simultaneously and
provides monitor reports per request. If the application recognition feature is also enabled, then the
application data and the flow properties collected by AR and IPFIX are exported to external or internal
IPFIX collectors. For more information on configuring these features, refer to the AOS-CX Security Guide.

Flow monitors
A flow monitor is applied to an interface to perform network traffic monitoring. A flow monitor consists
of a flow record, a flow cache, and optional flow exporters. A flow record must be created and assigned
to the flow monitor for the monitoring process to function. Flow data is compiled from the network
traffic on the interface and stored in the flow cache based on the match (key) and collect (non-key) fields
in the flow record. Data from the flow cache is exported by the flow exporters assigned to the flow
monitor. A maximum of sixteen flow monitors can be created. There is a limit of two flow exporters that
can be applied to a single flow monitor.

Flow exporters
A flow exporter defines where and how to export flow reports. Flow exporters are created as standalone
entities in the `config` context to provide flow monitors the ability to export flow reports. A single flow
exporter can be assigned to one or more flow monitors, and multiple flow exporters can be assigned to
a single flow monitor.

Destinations
The destination specifies where flow reports are sent. There are two possible types of destination for a
flow exporter:

1.

(default) Hostname or IP address of a device with an optional VRF

2. Traffic Insight instance

A flow exporter can only send flow reports to one destination. The destination type specifies which
destination to use. If no destination type is specified, the default destination type is the first one (a
hostname or IP address of a device with an optional VRF). If a VRF is not specified, the default VRF will be

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

14

used. A destination of each type can be configured, but only the one corresponding to the destination
type is used. If a destination corresponding to the destination type is not specified, then the flow
exporter configuraion is incomplete. If a new destination of a particular type is configured, it will replace
the destination of that type that was previously configured.

Flow Records
A flow record defines match (key) fields and collection (non-key) fields. Match fields are the set of fields
that define a flow, such as IP address or UDP port. Collection fields are the set of fields that identify
information to collect for a flow, such as packet and byte counters. A maximum of sixteen flow records
can be created.

There are six mandatory match fields, of which the IP match fields must be of the same type (IPv4 or
IPv6).

A flow record is invalid if it does not contain one of the supported sets of match fields.

The supported sets of match fields are:

1. All IPv4:

n IPv4 version

n IPv4 destination address

n IPv4 protocol

n Transport destination port

n Transport source port

2. All IPv6:

n IPv6 version

n IPv6 destination address

n IPv6 protocol

n Transport destination port

n Transport source port

Configuring IP Flow Information Export
The following list describes the steps required to configure a IP flow information export (IPFIX) solution:

n Step one: Create flow records

n Step two: Configure flow exporter(s)

n Step three: Configure monitor(s)

n Step four: Apply a flow monitors to interface(s)

Step one: Create Flow Records

Flow Records are used to define the data that will be added to the IPFIX template. Configure one record
for IPv4 and one for IPv6.

switch(config)# flow record flowRecordv4
switch(config-flow-record)# match ipv4 protocol

IP Flow Information Export | 15

| switch(config-flow-record)# |                                             | match ipv4          | source      | add         |       |
| --------------------------- | ------------------------------------------- | ------------------- | ----------- | ----------- | ----- |
| switch(config-flow-record)# |                                             | match ipv4          | destination | add         |       |
| switch(config-flow-record)# |                                             | match ipv4          | version     |             |       |
| switch(config-flow-record)# |                                             | match transport     |             | destination | port  |
| switch(config-flow-record)# |                                             | match transport     |             | source port |       |
| switch(config-flow-record)# |                                             | collect             | counter     | bytes       |       |
| switch(config-flow-record)# |                                             | collect             | counter     | packets     |       |
| switch(config-flow-record)# |                                             | collect             | application | name        |       |
| switch(config-flow-record)# |                                             | collect             | timestamp   | absolute    | first |
| switch(config-flow-record)# |                                             | collect             | timestamp   | absolute    | last  |
| switch(config)#             | flow                                        | record flowRecordv6 |             |             |       |
| switch(config-flow-record)# |                                             | match ipv6          | protocol    |             |       |
| switch(config-flow-record)# |                                             | match ipv6          | source      | add         |       |
| switch(config-flow-record)# |                                             | match ipv6          | destination | add         |       |
| switch(config-flow-record)# |                                             | match ipv6          | version     |             |       |
| switch(config-flow-record)# |                                             | match transport     |             | destination | port  |
| switch(config-flow-record)# |                                             | match transport     |             | source port |       |
| switch(config-flow-record)# |                                             | collect             | counter     | bytes       |       |
| switch(config-flow-record)# |                                             | collect             | counter     | packets     |       |
| switch(config-flow-record)# |                                             | collect             | application | name        |       |
| switch(config-flow-record)# |                                             | collect             | timestamp   | absolute    | first |
| switch(config-flow-record)# |                                             | collect             | timestamp   | absolute    | last  |
| Next,usetheshow             | flow recordcommandtoverifytheconfiguration. |                     |             |             |       |
| switch(config)#             | show                                        | flow record         |             |             |       |
--------------------------------------------------------------------------------
| Flow record | 'flowRecordv4' |     |     |     |     |
| ----------- | -------------- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
Match Fields
| ipv4 destination | address |     |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- |
ipv4 protocol
| ipv4 source | address |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- |
ipv4 version
| transport   | destination | port  |     |     |     |
| ----------- | ----------- | ----- | --- | --- | --- |
| transport   | source port |       |     |     |     |
| Collect     | Fields      |       |     |     |     |
| application | name        |       |     |     |     |
| counter     | bytes       |       |     |     |     |
| counter     | packets     |       |     |     |     |
| timestamp   | absolute    | first |     |     |     |
| timestamp   | absolute    | last  |     |     |     |
--------------------------------------------------------------------------------
| Flow record | 'flowRecordv6' |     |     |     |     |
| ----------- | -------------- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
Match Fields
| ipv6 destination | address |     |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- |
ipv6 protocol
| ipv6 source | address |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- |
ipv6 version
| transport   | destination | port  |     |     |     |
| ----------- | ----------- | ----- | --- | --- | --- |
| transport   | source port |       |     |     |     |
| Collect     | Fields      |       |     |     |     |
| application | name        |       |     |     |     |
| counter     | bytes       |       |     |     |     |
| counter     | packets     |       |     |     |     |
| timestamp   | absolute    | first |     |     |     |
| timestamp   | absolute    | last  |     |     |     |
16
AOS-CX10.11MonitoringGuide| (8400SwitchSeries)

| Step two: | Configure |     | flow | exporter(s) |     |     |     |     |
| --------- | --------- | --- | ---- | ----------- | --- | --- | --- | --- |
Ithisstep,youcandefineanexportertosendtoanexternaldestinationbyhostnameorIPaddress,or
toaninternaldestinationsuchasTrafficInsight..TheexamplebelowconfiguresIPFIXtoexportdatato
anexternaladdress/hostname:
| switch(config)# |     | flow | exporter | flowExternal |     |     |     |     |
| --------------- | --- | ---- | -------- | ------------ | --- | --- | --- | --- |
switch(config-flow-exporter)# destination type hostname-or-ip-addr
| switch(config-flow-exporter)# |     |     |     | destination |      | 11.1.1.1 |     |     |
| ----------------------------- | --- | --- | --- | ----------- | ---- | -------- | --- | --- |
| switch(config-flow-exporter)# |     |     |     | show        | flow | exporter |     |     |
--------------------------------------------------------------------------------
| Flow exporter |     | 'flowExternal |     |     |     |     |     |     |
| ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Status      |               |     | : Accepted |     |     |            |     |     |
| ----------- | ------------- | --- | ---------- | --- | --- | ---------- | --- | --- |
| Export      | Protocol      |     | : ipfix    |     |     |            |     |     |
| Destination | Type          |     | : Hostname |     | or  | IP address |     |     |
| Destination |               |     | : 11.1.1.1 |     |     |            |     |     |
| Transport   | Configuration |     |            |     |     |            |     |     |
| Protocol    |               |     | : udp      |     |     |            |     |     |
| Port        |               |     | : 4739     |     |     |            |     |     |
ToconfigureIPFIXtoexporttoTrafficInsight,firstconfigureTrafficInsight.
| switch(config)#       |     | traffic-insight |         |       | TI   |                   |     |     |
| --------------------- | --- | --------------- | ------- | ----- | ---- | ----------------- | --- | --- |
| switch(config-ti-TI)# |     |                 | source  | ipfix |      |                   |     |     |
| switch(config-ti-TI)# |     |                 | monitor | topN  | type | topN-flows        |     |     |
| switch(config-ti-TI)# |     |                 | monitor | dns   | type | application-flows |     |     |
| switch(config-ti-TI)# |     |                 | enable  |       |      |                   |     |     |
Next,configuretheflowexporterforTrafficInsight
| switch(config)#               |     | flow | exporter | flowExpTI       |     |                 |                 |     |
| ----------------------------- | --- | ---- | -------- | --------------- | --- | --------------- | --------------- | --- |
| switch(config-flow-exporter)# |     |      |          | export-protocol |     |                 | ipfix           |     |
| switch(config-flow-exporter)# |     |      |          | destination     |     | type            | traffic-insight |     |
| switch(config-flow-exporter)# |     |      |          | destination     |     | traffic-insight |                 | TI  |
Youcanusetheshow flow exportercommandtoverifytheflowexporterconfigurationforTraffic
Insight
| switch(config)# |     | show | flow exporter |     | flowExpTI |     |     |     |
| --------------- | --- | ---- | ------------- | --- | --------- | --- | --- | --- |
--------------------------------------------------------------------------------
| Flow exporter |     | 'flowExpTI' |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Status      |               |     | : Accepted |     |         |     |     |     |
| ----------- | ------------- | --- | ---------- | --- | ------- | --- | --- | --- |
| Export      | Protocol      |     | : ipfix    |     |         |     |     |     |
| Destination | Type          |     | : Traffic  |     | Insight |     |     |     |
| Destination |               |     | : TI       |     |         |     |     |     |
| Transport   | Configuration |     |            |     |         |     |     |     |
| Protocol    |               |     | : udp      |     |         |     |     |     |
| Port        |               |     | : 4739     |     |         |     |     |     |
Finally,usetheshow run traffic-insightcommandtoverifytheTrafficInsightconfiguration:
| switch(config)# |     | show | run traffic-insight |     |     |     |     |     |
| --------------- | --- | ---- | ------------------- | --- | --- | --- | --- | --- |
IPFlowInformationExport |17

| traffic-insight | TI  |     |     |
| --------------- | --- | --- | --- |
enable
| source ipfix |     |     |     |
| ------------ | --- | --- | --- |
!
| monitor     | topN type topN-flows           | entries      | 5   |
| ----------- | ------------------------------ | ------------ | --- |
| monitor     | appFlow type application-flows |              |     |
| Step three: | Configure                      | a monitor(s) |     |
First,configureanIPv4flowmonitor.
| switch(config)#               | flow monitor | flowMonv4 |              |
| ----------------------------- | ------------ | --------- | ------------ |
| switch(config-flow-monitor)#  |              | record    | flowRecordv4 |
| Switch (config-flow-monitor)# |              | exporter  | flowExternal |
| switch(config-flow-monitor)#  |              | exit      |              |
Next,configureanIPv6flowmonitor.
| switch(config)#              | flow monitor | flowMonv6 |              |
| ---------------------------- | ------------ | --------- | ------------ |
| switch(config-flow-monitor)# |              | record    | flowRecordv6 |
| switch(config-flow-monitor)# |              | exporter  | flowExternal |
| switch(config-flow-monitor)# |              | exit      |              |
Oncebothflowmonitorsarecreated,usetheshow flow monitorcommandtoverifytheflowmonitor
configurations.
| switch(config-flow-monitor)# |     | show flow | monitor |
| ---------------------------- | --- | --------- | ------- |
--------------------------------------------------------------------------------
| Flow monitor | 'flowMonv4' |     |     |
| ------------ | ----------- | --- | --- |
--------------------------------------------------------------------------------
| Status              |           | : Accepted     |     |
| ------------------- | --------- | -------------- | --- |
| Flow Record         |           | : flowRecordv4 |     |
| Flow Exporter(s)    |           | : flowExternal |     |
| Cache Configuration |           |                |     |
| Inactive            | Timeout : | 30             |     |
| Active Timeout      | :         | 1800           |     |
--------------------------------------------------------------------------------
| Flow monitor | 'flowMonv6' |     |     |
| ------------ | ----------- | --- | --- |
--------------------------------------------------------------------------------
| Status              |           | : Accepted     |     |
| ------------------- | --------- | -------------- | --- |
| Flow Record         |           | : flowRecordv6 |     |
| Flow Exporter(s)    |           | : flowExternal |     |
| Cache Configuration |           |                |     |
| Inactive            | Timeout : | 30             |     |
| Active Timeout      | :         | 1800           |     |
Step four: (Optional) Enable Application Recognition and apply a
| flow monitor | to interfaces |     |     |
| ------------ | ------------- | --- | --- |
EnableApplicationRecognitiononlyifyouareusingIPFIXtosendanapplicationID.Youdonotneedtoenable
ApplicationRecognitionforIPFIXtobeenabletoreportinformationtoanexternalcollectororforinternal
analyticsreports
18
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

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
| FAQs and | Troubleshooting |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
n WhenIPFIXisusedwithApplicationRecognition,thesefeaturesdonotsupportLAGsorMCLAGs(VSX
LAGs).
Thefollowingmessagesaredisplayedtoindicateanillegalargument:
n
o %Theflowexporter<EXPORTER-NAME>doesnotexist.
o %Theflowrecord<RECORD-NAME>doesnotexist.
o %Theflowmonitor<MONITOR-NAME>doesnotexist.
o InvaliddestinationIPaddressorhostnameentered.
o Unabletocreatetheflowexporter.Themaximumallowednumberofflowexporters(16)has
beenreached.
o Unabletocreatetheflowrecord.Themaximumallowednumberofflowrecords(16)hasbeen
reached.
o Unabletocreatetheflowmonitor.Themaximumallowednumberofflowmonitors(16)hasbeen
reached.
o FlowmonitorcannotbeappliedwhileinterfaceispartofLAG<LAG-NAME>.
o Flowmonitorcouldnotbeapplied.
o
Flowmonitorcouldnotbeunapplied
IPFlowInformationExport |19

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
20
AOS-CX10.11MonitoringGuide| (8400SwitchSeries)

| Release             |         |     |         | Modification |
| ------------------- | ------- | --- | ------- | ------------ |
| 10.07orearlier      |         |     |         | --           |
| Command Information |         |     |         |              |
| Platforms           | Command |     | context | Authority    |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
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
Bootcommands|21

Platforms

Command context

Authority

8400

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

Hewlett Packard Enterprise recommends that you use the boot management-module command instead of
pressing the module reset button to reboot a management module because if you are rebooting the only
available management module, the boot management-module command enables you to save the
configuration, cancel the reboot, or both.

Examples

Rebooting the active management module when the standby management module is available:

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

22

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
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
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
Bootcommands|23

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
24
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |
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
Bootcommands|25

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
26
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |
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
Bootcommands|27

Chapter 6
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
Switchsystemandhardwarecommandsaregeneralcommandsusedtoconfigurefundamentalsettings
ontheswitch.
RefertotheFundamentalsGuidetoviewtheswitchsystemandhardwarecommands.
28
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |     |
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
| External | storage | commands |     |     |
| -------- | ------- | -------- | --- | --- |
address
| address    | {<IPV4-ADDR> | | <IPV6-ADDR> | | hostname | <HOSTNAME>} |
| ---------- | ------------ | ------------- | ---------- | ----------- |
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
29
| AOS-CX10.11MonitoringGuide| |     | (8400SwitchSeries) |     |     |
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
| 8400 |     |     |     | Administratorsorlocalusergroup |
| ---- | --- | --- | --- | ------------------------------ |
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
Externalstorage|30

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
31
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

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
switch(config)#
|     | no  | external-storage | logfiles |     |
| --- | --- | ---------------- | -------- | --- |
Externalstorage|32

| Command        | History     |     |         |              |     |     |     |
| -------------- | ----------- | --- | ------- | ------------ | --- | --- | --- |
| Release        |             |     |         | Modification |     |     |     |
| 10.07orearlier |             |     |         | --           |     |     |     |
| Command        | Information |     |         |              |     |     |     |
| Platforms      | Command     |     | context | Authority    |     |     |     |
8400 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| password    | (external-storage) |               |             |             |     |     |     |
| ----------- | ------------------ | ------------- | ----------- | ----------- | --- | --- | --- |
| password    | [{plaintext        | | ciphertext} |             | <PASSWORD>] |     |     |     |
| no password | {plaintext         | |             | ciphertext} | <PASSWORD>  |     |     |     |
Description
Setsthepasswordfornetworkattachedstorageserverlogin.
Thenoformofthiscommandclearsthepasswordfornetworkattachedstorageserverlogin.
| Parameter   |              |     |     | Description               |     |     |     |
| ----------- | ------------ | --- | --- | ------------------------- | --- | --- | --- |
| {ciphertext | | plaintext} |     |     | Selectsthepasswordformat. |     |     |     |
| <PASSWORD>  |              |     |     | Specifiesthepassword.     |     |     |     |
NOTE:Whenthepasswordisnotprovidedonthecommandline,
plaintextpasswordpromptingoccursuponpressingEnter.The
enteredpasswordcharactersaremaskedwithasterisks.
Examples
CreatingavolumenamedlogfileswithpasswordXj#9:
| switch(config)# |     | external-storage |     | logfiles |     |     |     |
| --------------- | --- | ---------------- | --- | -------- | --- | --- | --- |
switch(config-external-storage-logfiles)#
|     |     |     |     |     | password | plaintext | Xj#9 |
| --- | --- | --- | --- | --- | -------- | --------- | ---- |
Creatingavolumenamedbak1withapromptedplaintextpassword:
| switch(config)#                       |         | external-storage |           | bak1       |     |     |     |
| ------------------------------------- | ------- | ---------------- | --------- | ---------- | --- | --- | --- |
| switch(config-external-storage-bak1)# |         |                  |           | password   |     |     |     |
| Enter                                 | the NAS | server           | password: | ********** |     |     |     |
| Re-Enter                              | the     | NAS server       | password: | ********** |     |     |     |
Clearingthepasswordforvolumelogfiles:
| switch(config)# |     | external-storage |     | logfiles |     |     |     |
| --------------- | --- | ---------------- | --- | -------- | --- | --- | --- |
switch(config-external-storage-logfiles)#
|         |         |     |     |     | no password | plaintext | Xj#9 |
| ------- | ------- | --- | --- | --- | ----------- | --------- | ---- |
| Command | History |     |     |     |             |           |      |
33
| AOS-CX10.11MonitoringGuide| |     | (8400SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

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
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
|     | (#) |     | forthiscommand. |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- |
Externalstorage|34

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
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
|     |     | (#) |     |     | forthiscommand. |
| --- | --- | --- | --- | --- | --------------- |
type
| type {nfsv3 |        | | nfsv4 | | scp} |     |     |
| ----------- | ------ | ------- | ------ | --- | --- |
| no type     | {nfsv3 | | nfsv4 | | scp} |     |     |
Description
Setsthenetworkattachedstorageaccesstypeforreachingtheexternalstoragevolume.
Thenoformofthiscommanddeletesanexternalstoragevolume.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
nfsv3
SpecifiestheNFSv3networkaccessprotocol.
| nfsv4 |     |     |     |     | SpecifiestheNFSv4networkaccessprotocol. |
| ----- | --- | --- | --- | --- | --------------------------------------- |
scp
SpecifiestheSCPnetworkaccessprotocol.
35
| AOS-CX10.11MonitoringGuide| |     |     | (8400SwitchSeries) |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- |

Examples
CreatingthelogfilesvolumeusingNFSV4:
switch(config)#
|                                           | external-storage |     | logfiles   |     |
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
| username <USER-NAME> |             |     |     |     |
| -------------------- | ----------- | --- | --- | --- |
| no username          | <USER-NAME> |     |     |     |
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
Externalstorage|36

| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
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
| switch(config)#                           | external-storage |     | logfiles |     |
| ----------------------------------------- | ---------------- | --- | -------- | --- |
| switch(config-external-storage-logfiles)# |                  |     | vrf nas  |     |
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
37
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

Platforms

Command context

Authority

members with execution rights for this
command.

External storage | 38

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

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

39

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

IP-SLA | 40

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
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
icmp-echo
icmp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} [source {<SOURCE-IPV4-ADDR> | <IFNAME>}]
[name-server <IPV4-ADDR-DNS-SERVER>] [payload-size <PAYLOAD-SIZE>]
| [tos <TYPE-OF-SERVICE>] |     | [probe-interval | <PROBE-INTERVAL>] |
| ----------------------- | --- | --------------- | ----------------- |
Description
ConfiguresICMPechoastheIP-SLAtestmechanism.RequiresdestinationaddressfortheIP-SLAtest.
| Parameter         |               |     | Description |
| ----------------- | ------------- | --- | ----------- |
| {<DEST-IPV4-ADDR> | | <HOSTNAME>} |     |             |
SelectsthedestinationIPv4addressfortheIP-SLAor
thehostnameofthedestination.
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
name-server <IPV4-ADDR-DNS-SERVER> SpecifiestheDNSserverfordestinationhostname
resolution.
41
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |
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
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
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
<IP-SLA-NAME> SpecifiesanIP-SLAprofilename.Length:1to63characters.
Examples
CreatinganIP-SLA:
IP-SLA|42

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
8400 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
43
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

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
8400 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | ip-sla | responder |            |     |     |     |     |     |
| ---- | ------ | --------- | ---------- | --- | --- | --- | --- | --- |
| show | ip-sla | responder | <SLA-NAME> |     |     |     |     |     |
Description
ShowsthegivenIP-SLAresponderconfigurationandoperationstatus.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<SLA-NAME>
SpecifiestheSLAname.
Examples
| switch(config)# |             |           | show | ip-sla responder |              | SLA3 |     |     |
| --------------- | ----------- | --------- | ---- | ---------------- | ------------ | ---- | --- | --- |
|                 | SLA         | Name      |      | : SLA3           |              |      |     |     |
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
IP-SLA|44

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
8400 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | ip-sla | responder |     | results |     |     |
| ---- | ------ | --------- | --- | ------- | --- | --- |
show ip-sla responder <SLA-NAME> <SOURCE-IPV4-ADDR> <PORT-NUM> results
Description
Showsthegivenip-slaresponderstatisticsforagivensourceIPandport.Thiscommandisonly
applicableforthesourceswheresourceIPandportareconfigured.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<SLA-NAME>
SpecifiestheSLAname.
| <SOURCE-IPV4-ADDR> |     |     |     |     | SpecifiesthesourceIPV4address. |     |
| ------------------ | --- | --- | --- | --- | ------------------------------ | --- |
<PORT-NUM>
Specifiestheportnumber.Range:1to65535.
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
8400 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | ip-sla | <SLA-NAME> |         |     |     |     |
| ---- | ------ | ---------- | ------- | --- | --- | --- |
| show | ip-sla | <SLA-NAME> | results |     |     |     |
Description
45
| AOS-CX10.11MonitoringGuide| |     | (8400SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

ShowsthegivenIP-SLAsourceconfigurationandstatus.
| Parameter  |     |     |     |     | Description                               |     |     |
| ---------- | --- | --- | --- | --- | ----------------------------------------- | --- | --- |
| <SLA-NAME> |     |     |     |     | SpecifiestheSLAname.                      |     |     |
| results    |     |     |     |     | ShowsthestatisticscalculatedforanSLAtype. |     |     |
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
|                 | Destination  |                   | Port           |          |               | : 8888            |             |
|                 | Source       | IP                | Address/IFName |          |               | :                 |             |
IP-SLA|46

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
47
AOS-CX10.11MonitoringGuide| (8400SwitchSeries)

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
8400 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
(#)
start-test
start-test
IP-SLA|48

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
49
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

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
| [probe-interval | <PROBE-INTERVAL>] |     |     |     |
| --------------- | ----------------- | --- | --- | --- |
Probeintervalinseconds.Range:30to604800.
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
config-ip-sla-<IP-SLA-NAME>
| 8400 |     |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | --- | ----------------------------------------- |
executionrightsforthiscommand.
udp-echo
udp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>] [payload-
size
<PAYLOAD-SIZE>] [tos <TYPE-OF-SERVICE>] [probe-interval <PROBE-INTERVAL>]
IP-SLA|50

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
[source-port <PORT-NUM>]
SpecifiessourceportfortheIP-SLAtest.Range:1to
65535.
[name-server <IPV4-ADDR-DNS-SERVER>] SpecifiestheDNSserverfordestinationhostname
resolution.
[payload-size <PAYLOAD-SIZE>] SpecifiesthepayloadsizeofanSLAprobe.Range:28
to1440.
| [<TYPE-OF-SERVICE>] |     | Typeofservice.Range:0to255. |     |
| ------------------- | --- | --------------------------- | --- |
probe-interval <PROBE-INTERVAL> Probeintervalinseconds.Range:5to604800.
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
Command Information
51
AOS-CX10.11MonitoringGuide| (8400SwitchSeries)

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

IP-SLA | 52

| advantage-factor | 10  | codec-type | g711a source | 1/1/1 |     |
| ---------------- | --- | ---------- | ------------ | ----- | --- |
switch(config-ipsla-1)#
|     |     |     | udp-jitter-voip | https://device.arubanetworks.com | 8080 |
| --- | --- | --- | --------------- | -------------------------------- | ---- |
advantage-factor 10 codec-type g711a name-server 10.10.10.2 probe-interval 120
| source 10.1.1.1     | source-port |         | 8888 tos 10  |           |     |
| ------------------- | ----------- | ------- | ------------ | --------- | --- |
| Command History     |             |         |              |           |     |
| Release             |             |         | Modification |           |     |
| 10.07orearlier      |             |         | --           |           |     |
| Command Information |             |         |              |           |     |
| Platforms           | Command     | context |              | Authority |     |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
vrf
vrf <VRF-NAME>
no vrf [<VRF-NAME>]
Description
ConfigurestheVRFonwhichtheSLAwillsendorreceivepackets.Bydefault,thedefaultVRFisused.
ThenoformofthecommandremovesVRFfromSLA.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<VRF-NAME>
SpecifiesaVRFname.Length:Default:default.
Examples
| switch(config-ip-sla-test)# |         |         | vrf ipslasrc |           |     |
| --------------------------- | ------- | ------- | ------------ | --------- | --- |
| switch(config-ip-sla-test)# |         |         | no vrf       |           |     |
| Command History             |         |         |              |           |     |
| Release                     |         |         | Modification |           |     |
| 10.07orearlier              |         |         | --           |           |     |
| Command Information         |         |         |              |           |     |
| Platforms                   | Command | context |              | Authority |     |
8400 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
53
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

| show interface |                       |     |                    |
| -------------- | --------------------- | --- | ------------------ |
| show interface | [<IFNNAME>|<IFRANGE>] |     | [brief | physical] |
show interface [<IFNNAME>|<IFRANGE>] [extended [non-zero] | [human-readable]]
| show interface | [<IFNNAME>] | monitor | [human-readable] |
| -------------- | ----------- | ------- | ---------------- |
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief]
show interface lag [<LAG-ID>] [extended [non-zero] | [human-readable]]
| show interface | lag [<LAG-ID>] | monitor | [human-readable] |
| -------------- | -------------- | ------- | ---------------- |
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
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
| non-zero      |     |     | Showsonlynonzerostatistics.                    |
| ------------- | --- | --- | ---------------------------------------------- |
| LAG           |     |     | ShowsLAGinterfaceinformation.                  |
| monitor       |     |     | Continuouslymonitorinterfacestatistics.        |
| LOOPBACK      |     |     | Showsloopbackinterfaceinformation.             |
| TUNNEL        |     |     | Showstunnelinterfaceinformation.               |
| VLAN          |     |     | ShowsVLANinterfaceinformation.                 |
| <LAG-ID>      |     |     | SpecifiestheLAGnumber.Range:1-256              |
| <LOOPBACK-ID> |     |     | SpecifiestheLOOPBACKnumber.Range:0-255         |
| <TUNNEL-ID>   |     |     | SpecifiesthetunnelID.Range:1-255               |
| <VLAN-ID>     |     |     | SpecifiestheVLANID.Range:1-4094                |
| VXLAN         |     |     | ShowstheVXLANinterfaceinformation.             |
| <VXLAN-ID>    |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |
Examples
Showinginterfaceinformationwhenitisconfiguredasaroute-onlyport:
| switch# | show interface | 1/1/1 |     |
| ------- | -------------- | ----- | --- |
IP-SLA|54

| Interface         | 1/1/1     | is up       |          |                   |                 |           |     |     |
| ----------------- | --------- | ----------- | -------- | ----------------- | --------------- | --------- | --- | --- |
| Admin state       | is        | up          |          |                   |                 |           |     |     |
| Link state:       | up        | for 2 days  | (since   | Sun               | Jun 21 05:30:22 | UTC 2020) |     |     |
| Link transitions: |           | 1           |          |                   |                 |           |     |     |
| Description:      |           | backup data | center   | link              |                 |           |     |     |
| Hardware:         | Ethernet, | MAC         | Address: | 70:72:cf:fd:e7:b4 |                 |           |     |     |
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
55
AOS-CX10.11MonitoringGuide| (8400SwitchSeries)

| switch(config-if)# |       | show     | interface | 1/1/1 |     |     |     |
| ------------------ | ----- | -------- | --------- | ----- | --- | --- | --- |
| Interface          | 1/1/1 | is down  |           |       |     |     |     |
| Admin state        | is    | up       |           |       |     |     |     |
| State information: |       | Disabled | by        | VSX   |     |     |     |
Link state: down for 3 days (since Tue Mar 16 05:20:47 UTC 2021)
| Link transitions: |     | 0   |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- |
Description:
| Hardware: | Ethernet, | MAC | Address: | 04:09:73:62:90:e7 |     |     |     |
| --------- | --------- | --- | -------- | ----------------- | --- | --- | --- |
MTU 1500
Type SFP+DAC3
Full-duplex
| qos trust        | none            |                 |     |         |     |       |         |
| ---------------- | --------------- | --------------- | --- | ------- | --- | ----- | ------- |
| Speed 0          | Mb/s            |                 |     |         |     |       |         |
| Auto-negotiation |                 | is off          |     |         |     |       |         |
| Flow-control:    |                 | off             |     |         |     |       |         |
| Error-control:   |                 | off             |     |         |     |       |         |
| VLAN Mode:       | native-untagged |                 |     |         |     |       |         |
| Native           | VLAN:           | 1               |     |         |     |       |         |
| Allowed          | VLAN            | List: 1502-1505 |     |         |     |       |         |
| Rate collection  |                 | interval:       | 300 | seconds |     |       |         |
| Rate             |                 |                 |     | RX      | TX  | Total | (RX+TX) |
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
Showingthemonitorinformation:
Inmonitormode,theCLI refreshesdataautomaticallyuntilitisexitedbyenteringq.Pressing?opensthehelp
menutodisplaywhichoptionsareavailableinthiscontext.
switch(config-if)#
|           |       | show  | interface | 1/1/1 monitor |     |       |         |
| --------- | ----- | ----- | --------- | ------------- | --- | ----- | ------- |
| Interface | 1/1/1 | is up |           |               |     |       |         |
| Rate      |       |       |           | RX            | TX  | Total | (RX+TX) |
---------------- -------------------- -------------------- --------------------
IP-SLA|56

| MBits       | / sec |     |     | 30196.43 |       |     | 30196.43 |       | 60392.85  |        |
| ----------- | ----- | --- | --- | -------- | ----- | --- | -------- | ----- | --------- | ------ |
| MPkts       | / sec |     |     | 58977.39 |       |     | 58977.40 |       | 117954.79 |        |
| Unicast     |       |     |     |          | 0.00  |     | 0.00     |       |           | 0.00   |
| Multicast   |       |     |     | 58977.39 |       |     | 58977.40 |       | 117954.79 |        |
| Broadcast   |       |     |     |          | 0.00  |     | 0.00     |       |           | 0.00   |
| Utilization | %     |     |     |          | 75.49 |     | 75.49    |       |           | 150.98 |
| Statistic   |       |     |     |          | RX    |     | TX       | Total | (RX+TX)   |        |
---------------- -------------------- -------------------- --------------------
| Packets   |                |            |              | 4756527649 |     | 4756527865   |     |              | 9513055514  |         |
| --------- | -------------- | ---------- | ------------ | ---------- | --- | ------------ | --- | ------------ | ----------- | ------- |
| Unicast   |                |            |              |            | 0   |              | 0   |              |             | 0       |
| Multicast |                |            |              | 4756527649 |     | 4756527865   |     |              | 9513055514  |         |
| Broadcast |                |            |              |            | 2   |              | 0   |              |             | 2       |
| Bytes     |                |            | 304417778668 |            |     | 304417795428 |     | 608835574096 |             |         |
| Jumbos    |                |            |              |            | 0   |              | 0   |              |             | 0       |
| Dropped   |                |            |              |            | 0   | 19028847730  |     |              | 19028847730 |         |
| Pause     | Frames         |            |              |            | 0   |              | 0   |              |             | 0       |
| Errors    |                |            |              |            | 0   |              | 0   |              |             | 0       |
| CRC/FCS   |                |            |              |            | 0   |              | n/a |              |             | 0       |
|           |                |            |              |            |     |              |     | help:        | ?,          | quit: q |
| Help for  | Interface      | Monitor    |              |            |     |              |     |              |             |         |
| h Toggle  | human-readable |            | mode         |            |     |              |     |              |             |         |
| c Clear   | interface      | statistics |              |            |     |              |     |              |             |         |
| Does      | not apply      | to         | rates        |            |     |              |     |              |             |         |
| Arrows,   | PgUp, PgDn,    | Home,      | End          |            |     |              |     |              |             |         |
| Navigate  | interface      |            | statistics   |            |     |              |     |              |             |         |
Delay: 2
|     |     |     |     |     |     |     |     | help: | ?,  | quit: q |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- |
Showingtheoutputforinterface1/1/1inhuman-readableformat:
Inhuman-readableformat,the< 1symbolforUtilizationindicatesthattheamountofpacketsisbetween
zeroandone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsandthe
Utilizationvalueisnotdisplayedeveninthenormaloutput,wherethehuman-readableparameterisnot
includedinthecommand.
| switch(config-if)# |       | show  | interface |     | 1/1/1 human-readable |     |     |       |         |     |
| ------------------ | ----- | ----- | --------- | --- | -------------------- | --- | --- | ----- | ------- | --- |
| Interface          | 1/1/1 | is up |           |     |                      |     |     |       |         |     |
| Rate               |       |       |           |     | RX                   |     | TX  | Total | (RX+TX) |     |
---------------- -------------------- -------------------- --------------------
| Bits /      | sec |     |     |     | 3M  |     | 3M  |     |     | 6M    |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| Pkts /      | sec |     |     |     | 316 |     | 316 |     |     | 633   |
| Unicast     |     |     |     |     | 319 |     | 319 |     |     | 638   |
| Multicast   |     |     |     |     | 0   |     | 0   |     |     | 0     |
| Broadcast   |     |     |     |     | 0   |     | 0   |     |     | 0     |
| Utilization | %   |     |     |     | < 1 |     | < 1 |     |     | < 1   |
| Statistic   |     |     |     |     | RX  |     | TX  |     |     | Total |
---------------- -------------------- -------------------- --------------------
57
AOS-CX10.11MonitoringGuide| (8400SwitchSeries)

| Packets      |     |     | 577K | 577K | 1M  |
| ------------ | --- | --- | ---- | ---- | --- |
| Unicast      |     |     | 577K | 577K | 1M  |
| Multicast    |     |     | 0    | 51   | 51  |
| Broadcast    |     |     | 0    | 15   | 15  |
| Bytes        |     |     | 744M | 745M | 1G  |
| Jumbos       |     |     | 0    | 0    | 0   |
| Dropped      |     |     | 0    | 0    | 0   |
| Filtered     |     |     | 0    | 0    | 0   |
| Pause Frames |     |     | 0    | 0    | 0   |
| Errors       |     |     | 0    | 0    | 0   |
| CRC/FCS      |     |     | 0    | n/a  | 0   |
| Collision    |     |     | n/a  | 0    | 0   |
| Runts        |     |     | 0    | n/a  | 0   |
| Giants       |     |     | 0    | n/a  | 0   |
...
| Command History |     |     |                        |     |     |
| --------------- | --- | --- | ---------------------- | --- | --- |
| Release         |     |     | Modification           |     |     |
| 10.11           |     |     | Addedmonitorparameter. |     |     |
10.10
Addedhuman-readableparameter.
| 10.07orearlier      |         |         | --        |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- |
| Command Information |         |         |           |     |     |
| Platforms           | Command | context | Authority |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
IP-SLA|58

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

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

59

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

Mirroring | 60

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

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

61

Clearingmirrorstatisticsformirrorsession1:
| switch#             | clear mirror | 1       |              |
| ------------------- | ------------ | ------- | ------------ |
| Command History     |              |         |              |
| Release             |              |         | Modification |
| 10.07orearlier      |              |         | --           |
| Command Information |              |         |              |
| Platforms           | Command      | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Mirroring|62

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
| Parameter |     |     | Description |     |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- | --- |
<FILE-NAME>
Specifiesthepacketcapturefiletosave.
<REMOTE-URL> Specifiestheexternalstoragetowhichthepacketcapturefilewill
besaved.
Usage
Onlyfourfilescanbesavedatanypointontheswitch.Packetcapturefilesarenotsavedafterafailover
| orreboot.Viewalistofsavedfilesusingdiag |     |     | utilities | list-files. |     |     |     |
| --------------------------------------- | --- | --- | --------- | ----------- | --- | --- | --- |
Examples
Savingmy_capture_file.pcaptosftp://root@10.0.0.2/file.pcap:
switch# copy tcpdump-pcap my_capture_file.pcap sftp://root@10.0.0.2/file.pcap
| root@10.0.0.2's      | passowrd:            |     |                    |     |          |           |       |
| -------------------- | -------------------- | --- | ------------------ | --- | -------- | --------- | ----- |
| Connected            | to 10.0.0.2.         |     |                    |     |          |           |       |
| sftp > put           | my_capture_file.pcap |     | file.pcap          |     |          |           |       |
| Uploading            | my_capture_file.pcap |     | to /root/file.pcap |     |          |           |       |
| my_capture_file.pcap |                      |     |                    |     | 100% 156 | 219.8KB/s | 00:00 |
| Copied               | successfuly.         |     |                    |     |          |           |       |
| Command              | History              |     |                    |     |          |           |       |
| Release              |                      |     | Modification       |     |          |           |       |
| 10.08                |                      |     | Commandintroduced  |     |          |           |       |
| Command              | Information          |     |                    |     |          |           |       |
63
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- | --- |

| Platforms | Command | context | Authority |     |     |     |
| --------- | ------- | ------- | --------- | --- | --- | --- |
8400 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
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
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| destination    | cpu |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- |
| destination    | cpu |     |     |     |     |     |
| no destination | cpu |     |     |     |     |     |
Description
Mirroring|64

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
65
| AOS-CX10.11MonitoringGuide| |     | (8400SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

Supportedmirrordestinations:Layer2orLayer3Ethernetports,LAGs,tunnel,orCPUasaMirror
Destination.AportthatisalreadyamemberofaLAGisnotavalidmirrordestination.
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
| 8400                | 1       |     |         |     |              |           |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --------- | --- |
| Command History     |         |     |         |     |              |           |     |
| Release             |         |     |         |     | Modification |           |     |
| 10.07orearlier      |         |     |         |     | --           |           |     |
| Command Information |         |     |         |     |              |           |     |
| Platforms           | Command |     | context |     |              | Authority |     |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| destination | tunnel |     |     |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- | --- | --- |
destination tunnel <TUNNEL-IPV4-ADDR> source <SOURCE-IPv4-ADDR>
| dscp <DSCP-VALUE> |        | vrf | <VRF-NAME> | id  | <SPAN-ID> |     |     |
| ----------------- | ------ | --- | ---------- | --- | --------- | --- | --- |
| no destination    | tunnel |     |            |     |           |     |     |
Description
Specifiesthetunnelwhereallmirroredtrafficforthesessionistransmitted.Onlyonetunneldestination
isallowedpersession.
Mirroring|66

You may configure multiple mirror sessions with the same source/destination IP address pair, however,
only one of those sessions sharing the same source/destination IP address pair can be enabled at a
given time.

Multiple Mirror Sessions can be enabled with the same source/destination IP address pair if the span
IDs are different for sessions. By default it is assigned 0 if not specified.

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

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

67

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
config-mirror-<SESSION-ID>
| 8400 |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | ----------------------------------------- |
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
Sincefileanddelete-fileareoptional,thebehaviorofthebasecommanddiag utilities tshark
doesnotsaveanythingtoafile,andinsteaddumpsthetsharksessiontotheconsoleuntilCTRL + cis
entered.
| Parameter   |     | Description                           |     |
| ----------- | --- | ------------------------------------- | --- |
| file        |     | Savescapturedpacketstoatemporaryfile. |     |
| delete-file |     | Deletesthemostrecentcapturedfile.     |     |
Example
Performingdiagnostic:
Mirroring|68

| switch#        | diagnostic  |             |              |              |            |
| -------------- | ----------- | ----------- | ------------ | ------------ | ---------- |
| switch#        | diagnostic  | utilities   | tshark       | file         |            |
| Inspecting     | traffic     | mirrored    | to the CPU   | until Ctrl-C | is entered |
| ^CEnding       | traffic     | inspection. |              |              |            |
| Command        | History     |             |              |              |            |
| Release        |             |             | Modification |              |            |
| 10.07orearlier |             |             | --           |              |            |
| Command        | Information |             |              |              |            |
| Platforms      | Command     | context     | Authority    |              |            |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| delete file | <FILE-NAME> |     | Deletesspecifiedtcpdumplistfiles.               |     |     |
| ----------- | ----------- | --- | ----------------------------------------------- | --- | --- |
| list-files  |             |     | Listsallthetcpdumpcapturefilessavedonthedevice. |     |     |
vrf <VRF-NAME> CapturespacketsonthespecifiedVRF.IfnoVRF isnamed,the
defaultisused.
count <COUNT-NUM> Runsthetcpdumpcommanduntilthespecifiednumberof
packetsarecaptured.Range: 1-2147483647.
proto <PROTO-NUM> CapturespacketsofaparticulartypebasedonIPprotocol
number.Range: 0-255.
| host-ip <IP-ADDR> |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- |
CapturespacketsmatchingwiththesourceordestinationIP
address.
source-ip <IP-ADDR> CapturespacketsfromthespecifiedIPaddress.
destination-ip <IP-ADDR> CapturespacketssenttothespecifiedIPaddress.
host-port <PORT> Capturespacketsmatchingwiththesourceordestinationport.
69
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

Parameter

Description

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

switch# diag utilities tcpdump list-files
my_capture_file.pcap

Reading my_capture_file.pcap:

Mirroring | 70

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
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Disablingamirroringsession:
71
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

| switch(config)# | mirror | session | 3   |     |
| --------------- | ------ | ------- | --- | --- |
switch(config-mirror-3)#
disable
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
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
Theattempttoenablethemirroringsessionfailsandanerrorisreturned.
n
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
| switch(config-mirror-3)# |     | enable |     |     |
| ------------------------ | --- | ------ | --- | --- |
| Command History          |     |        |     |     |
Mirroring|72

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show mirror
73
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

show mirror [<SESSION-ID>] [vsx-peer]

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

Mirroring | 74

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

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

75

| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
interface.Thereisnodefaultforthisparameter.Validvaluesare
thefollowing:
| both |     | Mirrorbothtransmittedandreceivedpackets. |     |     |
| ---- | --- | ---------------------------------------- | --- | --- |
rx
Mirroronlyreceivedpackets.
| tx  |     | Mirroronlytransmittedpackets. |     |     |
| --- | --- | ----------------------------- | --- | --- |
Usage
Thereisalimitofsourceinterfacesineachdirectionofagivenmirrorsession:
|     |     | Source | interface limit per mirror | session (4 |
| --- | --- | ------ | -------------------------- | ---------- |
Switch
|      |     | possible | sessions) |     |
| ---- | --- | -------- | --------- | --- |
| 8400 |     | 256      |           |     |
| 9300 |     | 128      |           |     |
However,thereisapracticallimittotheamountoftrafficthatamirrordestinationcantransmit.For
example,mirroringsessionwithmultiple10Gsourcescanoverwhelmasingle10Gdestination.
Youcanconfigurethesamesourceinterfaceinmultiplemirroringsessions,butonlyoneofthose
mirroringsessionscanbeenabledatatime.
Classifierpolicieswithmirroractionscanalsobeusedtomatchandmirrornetworktraffic.Although
mirroractionsofclassifierpoliciesmustspecifyanenabledmirroringsession,thetrafficmatchingand
mirroringactionsareseparatefromandtakepriorityoverbasicmirroringsessions.Forexample,
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
| switch(config-mirror-1)# |              | source interface |                |     |
| ------------------------ | ------------ | ---------------- | -------------- | --- |
| LAG-NAME                 | Enter a LAG  | name. For        | example, lag10 |     |
| PORT-NUM                 | Enter a port | number           |                |     |
Creatingamirroringsessionandconfiguringasourceinterfacetomirrorbothtransmittedandreceived
packets:
Mirroring|76

| switch(config)# |     |     | mirror | session | 1   |     |
| --------------- | --- | --- | ------ | ------- | --- | --- |
switch(config-mirror-1)#
|     |     |     |     | source | interface | 1/1/1 both |
| --- | --- | --- | --- | ------ | --------- | ---------- |
Creatingasecondmirroringsessionandconfiguringtwosourceinterfaces.Oneportmirroringonly
transmittedpacketsandtheothermirroringbothtransmittedandreceivedpackets:
switch(config)#
|                          |     |     | mirror | session | 2         |            |
| ------------------------ | --- | --- | ------ | ------- | --------- | ---------- |
| switch(config-mirror-2)# |     |     |        | source  | interface | 1/1/3 tx   |
| switch(config-mirror-2)# |     |     |        | source  | interface | 1/2/1 both |
Removingthefirstsourceinterface:
| switch(config-mirror-2)# |     |     |     | no  | source interface | 1/2/3 |
| ------------------------ | --- | --- | --- | --- | ---------------- | ----- |
Configuringasourceinterfacetomirrorreceivedpacketsonly:
| switch(config-mirror-3)# |     |     |     | source | interface | 1/1/2 rx |
| ------------------------ | --- | --- | --- | ------ | --------- | -------- |
Configuringasourceinterfacetomirrorbothtransmittedandreceivedpackets:
| switch(config-mirror-1)# |     |     |     | source | interface | 1/1/1 both |
| ------------------------ | --- | --- | --- | ------ | --------- | ---------- |
ConfiguringaLAGassourceinterfacetomirrorbothtransmittedandreceivedpackets:
| switch(config-mirror-4)# |     |     |     | source | interface | lag1 both |
| ------------------------ | --- | --- | --- | ------ | --------- | --------- |
Stoppingthemirroringofreceivedpacketsfromaconfiguredsourceinterface:
| switch(config-mirror-4)# |             |         |     | no      | source interface | lag1 rx   |
| ------------------------ | ----------- | ------- | --- | ------- | ---------------- | --------- |
| Command                  | History     |         |     |         |                  |           |
| Release                  |             |         |     |         | Modification     |           |
| 10.07orearlier           |             |         |     |         | --               |           |
| Command                  | Information |         |     |         |                  |           |
| Platforms                |             | Command |     | context |                  | Authority |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| source    | vlan |            |     |       |            |     |
| --------- | ---- | ---------- | --- | ----- | ---------- | --- |
| source    | vlan | <VLAN-NUM> | {rx | | tx  | | both}    |     |
| no source | vlan | <VLAN-NUM> |     | {rx | | tx | both} |     |
77
| AOS-CX10.11MonitoringGuide| |     | (8400SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

Description

Mirroring with VLAN as a source is supported in the following traffic directions:

n both - traffic received and transmitted

n rx - only received traffic

n tx - only transmitted traffic

More than one source VLAN can be configured in a mirror session. Each such VLAN may specify its own
direction.

There is a limit of 6 source VLANs for a given mirror session. There is also a limit of 6 source VLANs
across all mirror sessions.

Same VLAN may not be configured as a mirror source for multiple sessions.

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

Also, bridged packets are the only packets mirrored in the rx direction.

n If the mirror is configured in tx direction, packets are mirrored in post-routed form with the source

MAC as the switch address. Destination MAC is the nexthop gateway or station.

n If the mirror is configured in both direction, one copy of the packet will be mirrored.

n To mirror routed packets received on a VLAN and transmitted out a different VLAN, enable tx

mirroring on the destination VLAN.

Control plane packets generated by the switch's CPU are processed both in theingress and the egress
packet processing pipeline. The following are the behavior for mirroring with VLAN as source:

n If the mirror is configured in the rx or tx direction, the packets are mirrored to the mirror

destination.

Mirroring | 78

n Ifthemirrorisconfiguredinthebothdirection,twocopiesofthepacketsaremirroredtothemirror
destination.
ThenoformcommandwillceasemirroringtrafficfromthespecifiedsourceVLANandremovethe
sourcefromthemirrorconfiguration.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
VLAN-NUM
SelectstheVLANnumber.
direction Specifiesthedirectionofmirroring.tx(transmit),rx(receive),or
both.
Examples
CreatingamirrorsessionandaddingaVLANasasourceoftrafficinbothdirectionsonthatport:
| switch#                  | configure | terminal |      |         |
| ------------------------ | --------- | -------- | ---- | ------- |
| switch(config)#          | mirror    | session  | 1    |         |
| switch(config-mirror-1)# |           | source   | vlan | 10 both |
CreatingamirrorsessionandaddingtwoVLANsassourcesoftraffic:
directions:
switch#
configure terminal
| switch(config)#          | mirror | session | 2    |         |
| ------------------------ | ------ | ------- | ---- | ------- |
| switch(config-mirror-2)# |        | source  | vlan | 10 tx   |
| switch(config-mirror-2)# |        | source  | vlan | 20 both |
Configuringthesourceinsession2toreceivebyspecifyingthesourceinterfaceconfiguration:
| switch(config-mirror-2)# |     | source | vlan | 10 rx |
| ------------------------ | --- | ------ | ---- | ----- |
Removingthefirstsourceinterfaceinsession2entirely,andremovingthetransmitdirectionfromthe
othersothatmirroringonlyoccursinthereceivedirection:
| switch(config-mirror-2)# |         | source  | vlan | 10 rx        |
| ------------------------ | ------- | ------- | ---- | ------------ |
| switch(config-mirror-2)# |         | source  | vlan | 20 tx        |
| Command History          |         |         |      |              |
| Release                  |         |         |      | Modification |
| 10.07orearlier           |         |         |      | --           |
| Command Information      |         |         |      |              |
| Platforms                | Command | context |      | Authority    |
8400 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
79
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

Chapter 10
|            |          |            | Monitoring | a device | using SNMP |
| ---------- | -------- | ---------- | ---------- | -------- | ---------- |
| Monitoring | a device | using SNMP |            |          |            |
Configuring SNMP:RefertotheSNMP/MIBGuideforinformationonhowtoaddSNMPsoadevicecan
bemonitoredfromanetworkmanagementsystem(NMS).
Configuring an SNMP trap receiver:RefertotheSNMP/MIBGuideandspecificinformationaboutthe
trapcommandtoenableSNMPtraps.
show snmp
80
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

Chapter 11
Breakout cable support
| Breakout | cable support |     |
| -------- | ------------- | --- |
Portsdefaulttoanunsplitstate.Whenaportis'split',thesplitinterfacesbecomeactiveandcanbe
configuredindependently.Forexample,whena40GQSFP+portissplitfourways,eachsplitinterface
behaveslikeaseparate10GSFP+port.Thesplitinterfaceshavethesamenameasthebaseportwithan
addedsuffixtorepresenttheirlaneofthebreakoutcableoropticalchannelonSR4optics.Splittingan
interfaceremovesmostoftheport'sconfigurationsettingsandmakesitinactive.Theportwillnolonger
appearinmanyshowinterfacecommandsandmostconfigurationcommandsarenotallowed;thesplit
interfacenamemustbeused.
Thesamethinghappensinreversewhenaninterfaceisunsplit.However,notethatthe'split'and'no
split'commandsarealwaysperformedintheunsplitport'scontext.
| Limitations | with breakout | cable support |
| ----------- | ------------- | ------------- |
n The8400switchdoesnotsupportDACbreakoutcables,onlyopticalbreakoutcables.
n TheJL365AAruba8400X8p40GQSFP+AdvmoduledoesnotsupportPriority-BasedFlowControl
(PFC)onsplitports.
n TheJL366AAruba8400X6p40G/100GQSFP28Advmoduledoesnotsupport100Gbreakoutcables;it
onlysupportssplitportsatthe40Gspeed(into4x10Glinks).
| Breakout | cable support | commands |
| -------- | ------------- | -------- |
split
split [<COUNT>][<SPEED>][confirm]
| no split [confirm] |     |     |
| ------------------ | --- | --- |
Description
Splitsaportintomultipleinterfaces.OnlyportscapableofsupportingbreakoutcablesorSR4/eSR4
opticscanbesplit.
| Parameter |     | Description |
| --------- | --- | ----------- |
<COUNT> Specifiesthenumberofchildinterfacestoactivateuponsplitting
theport.Default:4.
| <SPEED> |     | Specifiesthespeedforthechildinterfaces.  |
| ------- | --- | ---------------------------------------- |
| confirm |     | Specifiestheconfirmationofportsplitting. |
Usage
Someswitchinterfacessupportdifferentsplitcountsdependingontheinstalledtransceiver.For
n
theseinterfaces,thenumberofchildinterfacestoactivatecanbespecified.Ifomitted,thedefaultis
4.Fortransceiverscapableofsupportingmultiplesplitmodes,theclosestmodewithenoughlanesis
81
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |
| --------------------------- | ------------------ | --- |

used.
n Sometransceiversalsosupportmultiplesplitmodeswithdifferentspeeds.Forexample,2x200Gor
2x100G.Whenaspeedisnotspecified,thehighestavailablespeedforthesplitcountisused.To
selectadifferentsplitmodewithalowerspeed,thedesiredspeedmustbespecified.
Thesplittableportsforallmodelsareshowninthetablebelow:
| Model |     |     |     | Description |     |     | Port info |     |
| ----- | --- | --- | --- | ----------- | --- | --- | --------- | --- |
Aruba8400Xmodules
n JL365A
|     |     |     |     | Aruba8400X8p40GQSFP+AdvMod |     |     | 1-8(40G) |     |
| --- | --- | --- | --- | -------------------------- | --- | --- | -------- | --- |
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
| Command  | History |        |         |     |     |     |     |     |
Breakoutcablesupport|82

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8400 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
83
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

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
84
| AOS-CX10.11MonitoringGuide| |     | (8400SwitchSeries) |     |
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
ArubaAirWave|85

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
86
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

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

Aruba AirWave | 87

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
88
| AOS-CX10.11MonitoringGuide| |     | (8400SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

RemovingSNMPv1/SNMPv2ccommunitystringprivate:
| switch(config)#     | no      | snmp-server | community    | private |
| ------------------- | ------- | ----------- | ------------ | ------- |
| Command History     |         |             |              |         |
| Release             |         |             | Modification |         |
| 10.07orearlier      |         |             | --           |         |
| Command Information |         |             |              |         |
| Platforms           | Command | context     | Authority    |         |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| Configuringsnmpv3 | informsisnotsupported. |     |             |     |
| ----------------- | ---------------------- | --- | ----------- | --- |
| Parameter         |                        |     | Description |     |
<IPv4-ADDR>
SpecifiestheIPaddressofatrapreceiverinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.Youcan
removeleadingzeros.Forexample,theaddress
192.169.005.100becomes192.168.5.100.
trap version <VERSION> SpecifiesthetrapnotificationtypeforSNMPv1orv2c.Available
optionsare:v1orv2c.
inform version v2c SpecifiestheinformnotificationtypeforSNMPv2c.
ArubaAirWave|89

| Parameter    |     | Description                                     |     |     |     |
| ------------ | --- | ----------------------------------------------- | --- | --- | --- |
| trap version | v3  | SpecifiesthetrapnotificationtypeforSNMPv3.      |     |     |     |
| user <NAME>  |     | SpecifiestheSNMPv3usernametobeusedintheSNMPtrap |     |     |     |
notifications.
| community | <STRING> |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
Specifiesthenameofthecommunitystringtousewhensending
trapnotifications.Range:1-32printableASCIIcharacters,
excludingspaceandquestionmark.Default:public.
<UDP-PORT>
SpecifiestheUDPportonwhichnotificationsaresent.Range:1-
65535.Default:162.
vrf <VRF-NAME> SpecifiesthenameoftheVRFonwhichtosendthenotifications.
Examples
| switch(config)# | snmp-server | host 10.10.10.10 | trap version | v1  |     |
| --------------- | ----------- | ---------------- | ------------ | --- | --- |
switch(config)# no snmp-server host 10.10.10.10 trap version v1
switch(config)#
|     | snmp-server | host 10.10.10.10 | trap version | v2c community | public |
| --- | ----------- | ---------------- | ------------ | ------------- | ------ |
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
switch(config)#
snmp-server host 10.10.10.10 inform version v2c community public
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
| public port | 5000 vrf default |     |     |     |     |
| ----------- | ---------------- | --- | --- | --- | --- |
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin port 2000
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin port
2000
| Command        | History     |              |     |     |     |
| -------------- | ----------- | ------------ | --- | --- | --- |
| Release        |             | Modification |     |     |     |
| 10.07orearlier |             | --           |     |     |     |
| Command        | Information |              |     |     |     |
90
| AOS-CX10.11MonitoringGuide| | (8400SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

| Platforms | Command |     | context |     | Authority |     |
| --------- | ------- | --- | ------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmpv3    | context        |        |                |             |            |           |
| --------- | -------------- | ------ | -------------- | ----------- | ---------- | --------- |
| snmpv3    | context <NAME> |        | vrf <VRF-NAME> |             | [community | <STRING>] |
| no snmpv3 | context        | <NAME> | [vrf           | <VRF-NAME>] |            |           |
Description
CreatesanSNMPv3contextonthespecifiedVRF.
ThenoformofthiscommandremovesthespecifiedSNMPcontext.
ArubaAirWave|91

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<NAME> Specifiesthenameofthecontext.Range:1to32printableASCII
characters,excludingspaceandquestionmark(?).
vrf <VRF-NAME> SpecifiestheVRFassociatedwiththecontext.Default:default.
| community |     | <STRING> |     |     |     |     |     |
| --------- | --- | -------- | --- | --- | --- | --- | --- |
SpecifiestheSNMPcommunitystringassociatedwiththecontext.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
92
| AOS-CX10.11MonitoringGuide| |     |     | (8400SwitchSeries) |     |     |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- | --- | --- |

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

Aruba AirWave | 93

Onswitch1,configureausercalledAdmin,thenissuetheshow running-configcommandtodisplay
switchconfigurationsettings.Thesnmpv3usercommandusestheciphertextoptiontoprotectthe
users'spasswords.
switch1(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword
| priv des | priv-pass | plaintext |     | myprivpass |     |
| -------- | --------- | --------- | --- | ---------- | --- |
switch1(config)#
exit
| switch1# | show           | running-config |     |     |     |
| -------- | -------------- | -------------- | --- | --- | --- |
| Current  | configuration: |                |     |     |     |
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
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
94
| AOS-CX10.11MonitoringGuide| |     | (8400SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

Support and Other Resources

Chapter 13

Support and Other Resources

Accessing Aruba Support

Aruba Support Services

https://www.arubanetworks.com/support-services/

AOS-CX Switch Software Documentation
Portal

https://www.arubanetworks.com/techdocs/AOS-CX/help_
portal/Content/home.htm

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

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/AOS-CX/help_portal/Content/home.htm

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

95

Portal
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
SupportandOtherResources|96

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

AOS-CX 10.11 Monitoring Guide | (8400 Switch Series)

97