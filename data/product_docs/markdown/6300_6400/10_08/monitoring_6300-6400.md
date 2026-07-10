AOS-CX 10.08 Monitoring
Guide

6300, 6400 Switch Series

Published: July 2023
Edition: 3

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
| Contents                                          |                                    |        |          |                    | 3   |
| ------------------------------------------------- | ---------------------------------- | ------ | -------- | ------------------ | --- |
| About                                             | this document                      |        |          |                    | 6   |
| Applicableproducts                                |                                    |        |          |                    | 6   |
| Latestversionavailableonline                      |                                    |        |          |                    | 6   |
| Commandsyntaxnotationconventions                  |                                    |        |          |                    | 6   |
| Abouttheexamples                                  |                                    |        |          |                    | 7   |
| Identifyingswitchportsandinterfaces               |                                    |        |          |                    | 7   |
| Identifyingmodularswitchcomponents                |                                    |        |          |                    | 8   |
| Monitoring                                        | hardware                           |        | through  | visual observation | 9   |
| ConfirmingnormaloperationoftheswitchbyreadingLEDs |                                    |        |          |                    | 9   |
| Detectingiftheswitchisnotreadyforafailoverevent   |                                    |        |          |                    | 10  |
| FindingfaultedcomponentsusingtheswitchLEDs        |                                    |        |          |                    | 10  |
| Aruba                                             | 6300/6400                          | Switch | Series   | LEDs               | 12  |
| SwitchandportLEDsfor6300SwitchSeries              |                                    |        |          |                    | 12  |
|                                                   | PowerSupplyfor6300SwitchSeries     |        |          |                    | 14  |
|                                                   | Redundancy                         |        |          |                    | 15  |
| SwitchandportLEDsfor6400SwitchSeries              |                                    |        |          |                    | 15  |
|                                                   | FrontpanelLEDsfor6400SwitchSeries  |        |          |                    | 16  |
|                                                   | PowerSupplyLEDs                    |        |          |                    | 18  |
|                                                   | LinemoduleLEDs                     |        |          |                    | 19  |
| Boot                                              | commands                           |        |          |                    | 21  |
| bootfabric-module                                 |                                    |        |          |                    | 21  |
| bootline-module                                   |                                    |        |          |                    | 22  |
| bootmanagement-module                             |                                    |        |          |                    | 23  |
| bootset-default                                   |                                    |        |          |                    | 24  |
| bootsystem                                        |                                    |        |          |                    | 25  |
| showboot-history                                  |                                    |        |          |                    | 27  |
| Switch                                            | system                             | and    | hardware | commands           | 29  |
| External                                          | storage                            |        |          |                    | 30  |
| Externalstoragecommands                           |                                    |        |          |                    | 30  |
|                                                   | address                            |        |          |                    | 30  |
|                                                   | directory                          |        |          |                    | 31  |
|                                                   | disable                            |        |          |                    | 32  |
|                                                   | enable                             |        |          |                    | 32  |
|                                                   | external-storage                   |        |          |                    | 33  |
|                                                   | password                           |        |          |                    | 34  |
|                                                   | showexternal-storage               |        |          |                    | 35  |
|                                                   | showrunning-configexternal-storage |        |          |                    | 36  |
|                                                   | type                               |        |          |                    | 36  |
|                                                   | username                           |        |          |                    | 37  |
|                                                   | vrf                                |        |          |                    | 38  |
3
AOS-CX10.08MonitoringGuide| (6300,6400SwitchSeries)

| IP-SLA                                 |           |            | 40  |
| -------------------------------------- | --------- | ---------- | --- |
| IP-SLAguidelines                       |           |            | 40  |
| LimitationswithVoIPSLAs                |           |            | 41  |
| IP-SLAcommands                         |           |            | 41  |
| http                                   |           |            | 41  |
| icmp-echo                              |           |            | 42  |
| ip-sla                                 |           |            | 43  |
| ip-slaresponder                        |           |            | 44  |
| showip-slaresponder                    |           |            | 45  |
| showip-slaresponderresults             |           |            | 46  |
| showip-sla<SLA-NAME>                   |           |            | 46  |
| start-test                             |           |            | 49  |
| stop-test                              |           |            | 50  |
| tcp-connect                            |           |            | 50  |
| udp-echo                               |           |            | 51  |
| udp-jitter-voip                        |           |            | 53  |
| vrf                                    |           |            | 54  |
| L1-100Mbps                             | downshift |            | 55  |
| Limitationswithspeeddownshift          |           |            | 55  |
| L1-100Mbpsdownshiftcommands            |           |            | 55  |
| downshiftenable                        |           |            | 55  |
| showinterface                          |           |            | 56  |
| showinterfacedownshift-enable          |           |            | 58  |
| showrunning-configinterface            |           |            | 59  |
| Mirroring                              |           |            | 62  |
| Mirrorstatistics                       |           |            | 62  |
| Classifierpoliciesandmirroringsessions |           |            | 62  |
| VLANasasource                          |           |            | 63  |
| Mirroringcommands                      |           |            | 63  |
| clearmirror                            |           |            | 63  |
| comment                                |           |            | 64  |
| copytcpdump-pcap                       |           |            | 65  |
| copytshark-pcap                        |           |            | 66  |
| destinationcpu                         |           |            | 67  |
| destinationinterface                   |           |            | 68  |
| diagnostic                             |           |            | 69  |
| diagutilitiestcpdump                   |           |            | 69  |
| disable                                |           |            | 72  |
| enable                                 |           |            | 72  |
| mirrorsession                          |           |            | 73  |
| showmirror                             |           |            | 74  |
| sourceinterface                        |           |            | 76  |
| sourcevlan                             |           |            | 78  |
| Monitoring                             | a device  | using SNMP | 80  |
| Power-over-Ethernet                    |           |            | 81  |
| PoEcommands                            |           |            | 82  |
| lldpdot3poe                            |           |            | 82  |
| lldpmedpoe                             |           |            | 83  |
| power-over-ethernet                    |           |            | 83  |
| power-over-ethernetallocate-by         |           |            | 84  |
| power-over-ethernetalways-on           |           |            | 85  |
Contents|4

|                                                  | power-over-ethernetassigned-class |           | 86  |
| ------------------------------------------------ | --------------------------------- | --------- | --- |
|                                                  | power-over-ethernetpre-std-detect |           | 87  |
|                                                  | power-over-ethernetpriority       |           | 88  |
|                                                  | power-over-ethernetquick-poe      |           | 88  |
|                                                  | power-over-ethernetthreshold      |           | 89  |
|                                                  | power-over-ethernettrap           |           | 90  |
|                                                  | showlldplocal                     |           | 91  |
|                                                  | showlldpneighbor                  |           | 92  |
|                                                  | showpower-over-ethernet           |           | 93  |
| Aruba                                            | AirWave                           |           | 98  |
| SNMPsupportandAirWave                            |                                   |           | 98  |
|                                                  | SNMPontheswitch                   |           | 98  |
| SupportedfeatureswithAirWaveandtheAOS-CXswitch   |                                   |           | 99  |
| ConfiguringtheAOS-CXswitchtobemonitoredbyAirWave |                                   |           | 99  |
|                                                  | logging                           |           | 100 |
|                                                  | snmp-servercommunity              |           | 102 |
|                                                  | snmp-serverhost                   |           | 103 |
|                                                  | snmp-servervrf                    |           | 105 |
|                                                  | snmpv3context                     |           | 105 |
|                                                  | snmpv3user                        |           | 106 |
| Support                                          | and Other                         | Resources | 109 |
| AccessingArubaSupport                            |                                   |           | 109 |
| AccessingUpdates                                 |                                   |           | 109 |
|                                                  | ArubaSupportPortal                |           | 109 |
|                                                  | MyNetworking                      |           | 110 |
| WarrantyInformation                              |                                   |           | 110 |
| RegulatoryInformation                            |                                   |           | 110 |
| DocumentationFeedback                            |                                   |           | 110 |
5
AOS-CX10.08MonitoringGuide| (6300,6400SwitchSeries)

Chapter 1
About this document
| About | this document |     |     |
| ----- | ------------- | --- | --- |
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedfor
administratorsresponsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
| Applicable | products |     |     |
| ---------- | -------- | --- | --- |
Thisdocumentappliestothefollowingproducts:
n Aruba6300SwitchSeries(JL658A,JL659A,JL660A,JL661A,JL662A,JL663A,JL664A,JL665A,JL666A,
JL667A,JL668A,JL762A)
n Aruba6400SwitchSeries(JL741A,R0X26A,R0X27A,R0X29A,R0X30A)
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
substitutewithanactualvalueinacommandorincode:
n <example-text>
<example-text>
| n   |     | Foroutputformatswhereitalictextcannotbedisplayed,variables |     |
| --- | --- | ---------------------------------------------------------- | --- |
n
n example-text
areenclosedinanglebrackets(< >).Substitutethetext—including
n example-text
theenclosinganglebrackets—withanactualvalue.
|     |     | n Foroutputformatswhereitalictextcanbedisplayed,variables |     |
| --- | --- | --------------------------------------------------------- | --- |
mightormightnotbeenclosedinanglebrackets.Substitutethe
textincludingtheenclosinganglebrackets,ifany,withanactual
value.
| Verticalbar.AlogicalORthatseparatesmultipleitemsfromwhichyoucan
chooseonlyone.
Anyspacesthatareoneithersideoftheverticalbarareincludedfor
readabilityandarenotarequiredpartofthecommandsyntax.
6
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |
| --------------------------- | ----------------------- | --- | --- |

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

On the 6300 Switch Series

About this document | 7

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

AOS-CX 10.08 Monitoring Guide | (6300, 6400 Switch Series)

8

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

7. Verify that the standby management module is ready to take over as the active management

module. On the standby management module, verify the states of the following LEDs:

AOS-CX 10.08 Monitoring Guide | (6300, 6400 Switch Series)

9

HealthLEDisOnGreen.
n
| n Managementstatestandby(Stby)LEDisOnGreen. |        |        |              |                |       |
| ------------------------------------------- | ------ | ------ | ------------ | -------------- | ----- |
| Detecting                                   | if the | switch | is not ready | for a failover | event |
ThistaskdescribesusingtheswitchLEDstodetectiftheswitchisnotreadyforthelossofafabric
moduleorforafailoverfromtheactivemanagementmoduletothestandbymanagementmodule.
AlthoughyoucandetectpowersupplyfailuresbyviewingtheLEDs,youmustusesoftwarecommandsto
determineifthepowersupplyredundancyissufficienttopowerthechassisifapowersupplyfails.
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
| n Onthereardisplaymodule,theLEDforthefabricmoduleisOff. |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- |
n Onthefabricmodule,thehealthLEDisOff.However,thefabricmoduleisbehindfan1andis
notdirectlyvisible.
| Finding | faulted | components | using | the switch | LEDs |
| ------- | ------- | ---------- | ----- | ---------- | ---- |
ThistaskdescribesusingtheswitchLEDstofindcomponentsthatareinafaultcondition.
AllgreenLEDs—exceptforchassispowerLEDsandtheUsr1LED—areoffwhentheLEDmodeissettoLight
Faults(TheUsr1LEDoftheLEDModesectionoftheactivemanagementmoduleisOnGreenandthedefault
behaviorfortheUsr1LEDisbeingused.).
Monitoringhardwarethroughvisualobservation|10

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

AOS-CX 10.08 Monitoring Guide | (6300, 6400 Switch Series)

11

|         |                   |        |          |               |        | Chapter | 3    |
| ------- | ----------------- | ------ | -------- | ------------- | ------ | ------- | ---- |
|         |                   |        | Aruba    | 6300/6400     | Switch | Series  | LEDs |
| Aruba   | 6300/6400 Switch  | Series | LEDs     |               |        |         |      |
| Switch  | and port          | LEDs   | for 6300 | Switch Series |        |         |      |
| Figure1 | SwitchandPortLEDs |        |          |               |        |         |      |
Table1:SwitchandportLEDs:Labelsanddescription
| Label |     | Description                   |     |     |     |     |     |
| ----- | --- | ----------------------------- | --- | --- | --- | --- | --- |
| 1     |     | SwitchportLEDs                |     |     |     |     |     |
| 2     |     | BackModulestatusLED           |     |     |     |     |     |
| 3     |     | SpeedmodeselectedLED          |     |     |     |     |     |
| 4     |     | PoEmodeselected               |     |     |     |     |     |
| 5     |     | ResetbuttonUsrmodeselectedLED |     |     |     |     |     |
| 6     |     | UID(UnitIdentification)       |     |     |     |     |     |
| 7     |     | GlobalStatusLED               |     |     |     |     |     |
| 8     |     | LEDModestatusLED              |     |     |     |     |     |
| 9     |     | ManagementConsoleLED          |     |     |     |     |     |
Table2:FrontpanelLEDbehavior
12
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- | --- | --- | --- |

| Switch LEDs | Function                  | State    | Meaning |
| ----------- | ------------------------- | -------- | ------- |
| BackLED     | Statusofmodularcomponents | On-Green | Normal  |
installedinthebackofthe
chassis(notapplicablefor SlowFlash-Amber Faultinoneofthemodulesin
|     | 6300Fswitches) |     | thebackofthechassis |
| --- | -------------- | --- | ------------------- |
|     |                | Off | Nomodularcomponents |
installedinthebackofthe
chassis
| PoELED | IndicatesPortLEDsare | Off | PoEmodenotselected |
| ------ | -------------------- | --- | ------------------ |
showingPoEinformation(not
applicablefornonPoE
|     |     | On-Green | PoEmodeselected |
| --- | --- | -------- | --------------- |
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
|        |                      | On-Green | Speedmodeselected       |
| ------ | -------------------- | -------- | ----------------------- |
| StkLED | IndicatesPortLEDsare | Off      | Stackingmodenotselected |
showingstackingmode
|     | information | On-Green | Stackingmodeselected      |
| --- | ----------- | -------- | ------------------------- |
|     |             | On-Amber | Aporthasastackingfailure. |
Stackingmodeselected
|     |     | SlowflashAmber | Aporthasastackingfailure. |
| --- | --- | -------------- | ------------------------- |
Stackingmodenotselected
| UIDLED | User-configurableLED | Off | UserdefinedthelocatorLED: |
| ------ | -------------------- | --- | ------------------------- |
OFF
|     |     | On/FlashBlue(for | UserdefinedthelocatorLED: |
| --- | --- | ---------------- | ------------------------- |
|     |     | 30min)           | On/Flash                  |
GlobalStatus Overallstatusoftheproduct SlowFlash-Green Self-testinprogressduring
| IndicatorLED |     |                 | UBOOT,SVOSandAOS-CX           |
| ------------ | --- | --------------- | ----------------------------- |
|              |     | On-Green        | SuccessfullyinitializedAOS-CX |
|              |     | SlowFlash-Amber | Recoverablefaults(e.g.fans,   |
PSUfault)
|     |     | On-Amber | Criticalfaults(e.g.exceed |
| --- | --- | -------- | ------------------------- |
temperaturelimit)
| OOBMStatus   | StatusofOOBMLink | Off              | OOBMportisnotconnected, |
| ------------ | ---------------- | ---------------- | ----------------------- |
| IndicatorLED | connectivity     |                  | nolinkestablished       |
|              |                  | HalfBright-Green | OOBMportisenabledand    |
establishedlinkwithpartner
Aruba6300/6400SwitchSeriesLEDs|13

| Switch LEDs | Function |     | State    | Meaning                   |
| ----------- | -------- | --- | -------- | ------------------------- |
|             |          |     | On-Green | Experiencinghighbandwidth |
utilization
|     |     |     | ActivityFlicker- | %ofthetimethattheLEDlight |
| --- | --- | --- | ---------------- | ------------------------- |
|     |     |     | Green            | upisroughlyproportionalto |
the%offullbandwidth
utilizationoftheport
*PresstheModeSelectbuttontoswitchbetweenUser(default),PoE,Spd,orStkMode.
Table3:RearPanelLEDbehavior
| Switch LEDs     | Function    |     | State/Mode | Meaning |
| --------------- | ----------- | --- | ---------- | ------- |
| FanModuleStatus | Statusoffan |     | On-Green   | Normal  |
LED
|        |                      |     | Slowflash-Amber | Fanfault                 |
| ------ | -------------------- | --- | --------------- | ------------------------ |
| UIDLED | User-configurableLED |     | Off             | UserdefinethelocatorLED: |
OFF
|           |                     |     | On/Flash(30min)- | UserdefinethelocatorLED: |
| --------- | ------------------- | --- | ---------------- | ------------------------ |
|           |                     |     | blue             | On/Flash                 |
| PSUStatus | Statusofpowersupply |     | OnGreen          | Normal                   |
IndicatorLED
|     |     |     | Off | Nopower,PSUhasinvalidAC |
| --- | --- | --- | --- | ----------------------- |
inputofinvalidDCoutputs
|     |     |     | SlowFlash-Green | Powersupplyhasfaultedor |
| --- | --- | --- | --------------- | ----------------------- |
warning
| Power Supply | for 6300 | Switch | Series |     |
| ------------ | -------- | ------ | ------ | --- |
Fixedformat(F)modelsincludebuilt-inpowersuppliesandmodular(M)modelshaverearslotsforhot
swappablepowersuppliesforcustomizedPoErequirements.
Iftheswitchisconfiguredwithredundantpowersupplies,theswitchwillnotsufferanylossoftrafficor
performanceifapowersupplyfails,exceptforpossiblePoE reallocationonPoEClass4andPoEClass6swithces.
n ArubaX37254VDC1050W110-240VACPowerSupply(JL087A)isa1050wattpowersupplyfor
applicablePoEswitches.Itoffersupto740wattsofPoEpowerandiskeyedsothatitwillnotfitinto
thepowersupplyslotsofnon-PoEArubaswitches.
n ArubaX37254VDC680W100-240VACPowerSupply(JL086A)isa680wattpowersupplyfor
applicablePoEswitches.Itoffersupto370wattsofPoEpowerandiskeyedsothatitwillnotfitinto
thepowersupplyslotsofnon-PoEArubaswitches.
ArubaX37112VDC250W100-240VACPowerSupply( JL085A)isa250wattpowersupplyforthenon-
n
PoEswitches.ThispowersupplydoesnotprovideanyPoEpowerandiskeyedsothatitwillnotfit
intothepowersupplyslotsofArubaPoEswitches.
n ArubaX37254VDC1600W110-240VACPowerSupply(JL670A):A1600watt(high-lineonly)power
supplyforapplicablePoEswitches.Itoffersupto1440wattsofPoEpower,andiskeyedsothatitwill
notfitintothepowersupplyslotsofnon-PoEArubaswitches.
14
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- |

n Aruba6300M1050W36-72VDCPSU(JL758A)isa1050wattDCpowersupplyusedfor6300MPoE
switches.Thisiskeyedsothatitwillnotfitintothepowersupplyslotsofnon-PoEArubaswitches.
n Aruba6300M250W36-72VDCPSU(JL757A)isa250wattDCpowersupplyusedfor6300Mnon-PoE
switches.ThepowersupplydoesnotprovideanyPoEpowerandiskeyedsothatitwillnotfitinto
thepowersupplyslotsoftheArubaPoEswitches.
FordeploymentsthatneedhigherportandPoEdensity,the6300supports60WofPoEineveryportof
a48-portswitchforatotalof2880WofPoE.TheindustrystandardIEEE802.3btHighPowerPoE
support(class6)providesupto60WperportforsupportofthelatestIoTdevicesandAPs.PoEsupport
forIEEE802.3atPoweroverEthernet(PoE+)providesupto30WperportaswellasanyIEEE802.3af-
compliantenddevice
Highavailabilitywithalways-onPoEsuppliesPoEpowerevenduringscheduledrebootsandfirmware
upgradeswhilequickPoEsuppliesPoEpowertopowereddevicesassoonastheswitchispluggedinto
ACpowersothedevicecaninitializeatthesametimeastheswitchOSbootup.
Redundancy
Table1:6300PowerSupplyRedundancy
show env power redundancy:
| PSU1 | PSU2 | Result |     |     |
| ---- | ---- | ------ | --- | --- |
operational redundancy
| JL086A         | JL086A                           | Supported    |             | n+n    |
| -------------- | -------------------------------- | ------------ | ----------- | ------ |
| JL086A         | JL087A                           | Notsupported |             | none   |
| JL086A         | JL670AHL                         | Notsupported |             | none   |
| JL086A         | JL670ALL                         | Notsupported |             | none   |
| JL086A         | JL758A                           | Notsupported |             | none   |
| JL087A         | JL087A                           | Supported    |             | n+n    |
| JL087A         | JL670AHL                         | Notsupported |             | none   |
| JL087A         | JL670ALL                         | Notsupported |             | none   |
| JL087A         | JL758A                           | Supported    |             | none   |
| JL670AHL       | JL670AHL                         | Supported    |             | n+n    |
| JL670ALL       | JL670ALL                         | Supported    |             | n+n    |
| JL670ALL       | JL670AHL                         | Notsupported |             | none   |
| JL670A         | JL758A                           | Notsupported |             | none   |
| JL670ALL(740)  | JL087A(740)                      | Notsupported |             | none   |
| JL670ALL (740) | JL758A(740)                      | Notsupported |             | none   |
| Switch         | and port                         | LEDs for     | 6400 Switch | Series |
| Figure1        | RearpanelLEDsfor6400SwitchSeries |              |             |        |
Aruba6300/6400SwitchSeriesLEDs|15

| 1           |          | Powersupplystatus(1)(2)(3)(4) |        |
| ----------- | -------- | ----------------------------- | ------ |
| 2           |          | ChassispowerLED               |        |
| 3           |          | ChassishealthLED              |        |
| 4           |          | Unitidentification(UID)LED    |        |
| 5           |          | Fantraystatus(1,2)            |        |
| Front panel | LEDs for | 6400 Switch                   | Series |
TheAruba6400switcheshavetwomanagementmodule(MM)slots.Managementmodulessupport
controlplaneactivitiesandin-memoryrunningoftheTimeSeriesDatabase.
Figure1 Managementmoduleslotswithmanagementmodulesinstalled
Whentwomanagementmodulesareinstalled,oneoperatesinactivemodeandtheotheroperatesin
standbymode.Theactiveslotisdeterminedbyelection.Installingtwomanagementmodulesprovides
controlplanehighavailability.
Figure2 Managementmodulefeatures
16
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |
| --------------------------- | ----------------------- | --- | --- |

1

2

3

4

5

6

7

8

9

Mgmt state (Actv) LED

System power LED

Management module health LED (green)

Line module status LEDs

Front Power supply status (1 2 3 4) LEDs

Fan tray status LEDs (1 - 4)

LED mode: Usr1, Usr2 Spd, and PoE LEDs

Auxillary port

Mgmt port (OOBM Port) with Activity/Link
LED

Indicates the status of the management
module after booting. If the MM is the
active MM, then the LED glows steady
green.

When the system is receiving power, glows
steady green.

Indicates status of the switch. LED glows
steady green when switch is ready after
booting from the Network Operating
System (NOS).

Indicates if a line module is installed in a
line module slot (1 through 5 for 6405
switches; 1 through 10 on 6410 switches).
If a line module is installed in a given slot,
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
n Flicker green: Data transfer in progress

Without an active network connection, this
LED is off after power-on and self-test
completes. With an active network
connection, this LED operates as follows:

Aruba 6300/6400 Switch Series LEDs | 17

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
| Power Supply LEDs |     |     |
| ----------------- | --- | --- |
TheAruba6400hasfourpowersupplyunitslotsthatsupporttheArubaX38254DC2700WACpower
supplyunit(PSU).
Figure3 ArubaX38254DC2700WACPowerSupply(JL372A)
1 PowerLED(green)
2 PowerfailLED(amber)
3 Powersupplyhandle
4 Latchreleasetab
18
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |
| --------------------------- | ----------------------- | --- |

n A single PSU is sufficient for fans and management cards to come up and provide user access and

diagnostics.

n At 220 V AC, only two PSUs are required for full operation and a single PSU is sufficient for the fans

and management cards to come up and provide user access/diagnostics.

n At 220 V AC: Installing three PSUs offers 2+1 redundancy and installing all four PSUs offers 2+2

redundancy.

n At 110 V AC: The switch offers N + 1 redundancy.

n The PSUs are hot-swappable. The chassis can be connected to an AC power source for a given PSU

slot while the PSU for that slot is being removed or installed.

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

n At 220 V AC, only two PSUs are required for full operation and a single PSU is sufficient for the fans

and management cards to come up and provide user access/diagnostics.

n At 220 V AC: Installing three PSUs offers 2+1 redundancy and installing all four PSUs offers 2+2

redundancy.

n At 110 V AC: The switch offers N + 1 redundancy.

n The PSUs are hot-swappable. The chassis can be connected to an AC power source for a given PSU

slot while the PSU for that slot is being removed or installed.

Line module LEDs

Aruba 6300/6400 Switch Series LEDs | 19

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

AOS-CX 10.08 Monitoring Guide | (6300, 6400 Switch Series)

20

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
21
AOS-CX10.08MonitoringGuide| (6300,6400SwitchSeries)

| Release             |         |     |         | Modification |
| ------------------- | ------- | --- | ------- | ------------ |
| 10.07orearlier      |         |     |         | --           |
| Command Information |         |     |         |              |
| Platforms           | Command |     | context | Authority    |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --------------- |
boot line-module
| boot line-module |     | <SLOT-ID> |     |     |
| ---------------- | --- | --------- | --- | --- |
Description
Rebootsthespecifiedlinemodule.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<SLOT-ID>
Specifiesthememberandslotofthemoduleintheformat
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
| switch# | boot line-module |     | 1/1 |     |
| ------- | ---------------- | --- | --- | --- |
This command will reboot the specified line module and interfaces on this
module will not send or receive packets while the module is down. Any
traffic passing through the line module will be interrupted. Management
sessions connected through the line module will be affected. It might take
up to 2 minutes to complete rebooting the module. During that time, you can
| monitor     | progress | by viewing | the    | event log. |
| ----------- | -------- | ---------- | ------ | ---------- |
| Do you want | to       | continue   | (y/n)? |            |
y
switch#
| Command History |     |     |     |              |
| --------------- | --- | --- | --- | ------------ |
| Release         |     |     |     | Modification |
| 10.07orearlier  |     |     |     | --           |
Bootcommands|22

Command Information

Platforms

Command context

Authority

6300
6400

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

AOS-CX 10.08 Monitoring Guide | (6300, 6400 Switch Series)

23

Examples
Rebootingtheactivemanagementmodulewhenthestandbymanagementmoduleisavailable:
switch#
|     | boot | management-module |     | active |     |     |     |
| --- | ---- | ----------------- | --- | ------ | --- | --- | --- |
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
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400             |     |          |              |     | forthiscommand. |     |     |
| ---------------- | --- | -------- | ------------ | --- | --------------- | --- | --- |
| boot set-default |     |          |              |     |                 |     |     |
| boot set-default |     | {primary | | secondary} |     |                 |     |     |
Description
Setsthedefaultoperatingsystemimagetousewhenthesystemisbooted.
| Parameter |     |     |     |     | Description                                     |     |     |
| --------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- |
| primary   |     |     |     |     | Selectstheprimarynetworkoperatingsystemimage.   |     |     |
| secondary |     |     |     |     | Selectsthesecondarynetworkoperatingsystemimage. |     |     |
Example
Selectingtheprimaryimageasthedefaultbootimage:
Bootcommands|24

| switch#        | boot set-default |     | primary     |              |
| -------------- | ---------------- | --- | ----------- | ------------ |
| Default        | boot image       | set | to primary. |              |
| Command        | History          |     |             |              |
| Release        |                  |     |             | Modification |
| 10.07orearlier |                  |     |             | --           |
| Command        | Information      |     |             |              |
| Platforms      | Command          |     | context     | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| boot system |          |             |     |            |
| ----------- | -------- | ----------- | --- | ---------- |
| boot system | [primary | | secondary | |   | serviceos] |
Description
Rebootsallmodulesontheswitch.Bydefault,theconfigureddefaultoperatingsystemimageisused.
Optionalparametersenableyoutospecifywhichsystemimagetousefortherebootoperationandfor
futurerebootoperations.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
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
25
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- |

Youcanusetheboot set-defaultcommandtochangetheconfigureddefaultoperatingsystemimage.
n Ifyouselectserviceosastheoptionalparameter,theconfigureddefaultbootimageremainsthe
same,andthesystemrebootsallmanagementmoduleswiththeserviceoperatingsystem.
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
switch#
|            | boot system  | secondary         |               |                |
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
Bootcommands|26

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
show boot-history
| show boot-history | [all] |     |     |
| ----------------- | ----- | --- | --- |
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
CurrentBoot,upfor<SECONDS>seconds
Forthecurrentboot,theshow boot-historycommandshowsthenumberofsecondsthemodulehasbeen
runningonthecurrentsoftware.
Timestampbootreason
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
27
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |
| --------------------------- | ----------------------- | --- | --- |

| Index : | 3                                  |          |           |      |                  |
| ------- | ---------------------------------- | -------- | --------- | ---- | ---------------- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |          |           |      |                  |
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
Bootcommands|28

Chapter 5
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
Switchsystemandhardwarecommandsaregeneralcommandsusedtoconfigurefundamentalsettings
ontheswitch.
RefertotheFundamentalsGuidetoviewtheswitchsystemandhardwarecommands.
29
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- | --- |

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
| Parameter   |     |     | Description                              |     |
| ----------- | --- | --- | ---------------------------------------- | --- |
| <IPV4-ADDR> |     |     | SpecifiestheNASserverIPv4address,Global. |     |
<IPV6-ADDR>
SpecifiestheIPv6addressoftheNASserver.
| <HOSTNAME> |     |     | SpecifiesthehostnameoftheNASserver.String. |     |
| ---------- | --- | --- | ------------------------------------------ | --- |
Examples
CreatingthelogfilesstoragevolumewithIPaddress10.1.1.1:
30
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |
| --------------------------- | --- | ----------------------- | --- | --- |

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
| 6300 |     |     |     | Administratorsorlocalusergroup    |
| ---- | --- | --- | --- | --------------------------------- |
| 6400 |     |     |     | memberswithexecutionrightsforthis |
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
Externalstorage|31

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
32
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- |

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
switch(config)#
|     | no  | external-storage | logfiles |     |
| --- | --- | ---------------- | -------- | --- |
Externalstorage|33

| Command        | History     |     |         |              |
| -------------- | ----------- | --- | ------- | ------------ |
| Release        |             |     |         | Modification |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --------------- |
password
| password    | [{plaintext |     | | ciphertext} | <PASSWORD>] |
| ----------- | ----------- | --- | ------------- | ----------- |
| no password | {plaintext  |     | | ciphertext} | <PASSWORD>  |
Description
Setsthepasswordfornetworkattachedstorageserverlogin.
Thenoformofthiscommandclearsthepasswordfornetworkattachedstorageserverlogin.
| Parameter   |              |     |     | Description               |
| ----------- | ------------ | --- | --- | ------------------------- |
| {ciphertext | | plaintext} |     |     | Selectsthepasswordformat. |
<PASSWORD>
Specifiesthepassword.
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
34
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |
| --------------------------- | --- | ----------------------- | --- | --- |

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
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 | (#) |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --------------- | --- | --- | --- |
Externalstorage|35

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
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     | (#) |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
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
36
| AOS-CX10.08MonitoringGuide| |     |     | (6300,6400SwitchSeries) |     |     |
| --------------------------- | --- | --- | ----------------------- | --- | --- |

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
6300 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 6400 |     |     |     | memberswithexecutionrightsforthis |
| ---- | --- | --- | --- | --------------------------------- |
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
Externalstorage|37

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
6300 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
38
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- |

Platforms

Command context

Authority

6400

members with execution rights for this
command.

External storage | 39

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

AOS-CX 10.08 Monitoring Guide | (6300, 6400 Switch Series)

40

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

IP-SLA | 41

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
name-server <IPV4-ADDR-DNS-SERVER> SpecifiestheDNSserverfordestinationhostname
resolution.
42
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |
| --------------------------- | ----------------------- | --- | --- |

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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
6400
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
IP-SLA|43

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
6300 Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
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
| [source {<SOURCE-IPV4-ADDR> |     |     | | <IFNAME>}] |     |
| --------------------------- | --- | --- | ------------ | --- |
SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
Examples
44
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- |

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
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |        |           |            |     | forthiscommand. |     |     |     |
| ---- | ------ | --------- | ---------- | --- | --------------- | --- | --- | --- |
| show | ip-sla | responder |            |     |                 |     |     |     |
| show | ip-sla | responder | <SLA-NAME> |     |                 |     |     |     |
Description
ShowsthegivenIP-SLAresponderconfigurationandoperationstatus.
| Parameter  |     |     |     |     | Description          |     |     |     |
| ---------- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
| <SLA-NAME> |     |     |     |     | SpecifiestheSLAname. |     |     |     |
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
IP-SLA|45

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |        |           |     |         | forthiscommand. |     |
| ---- | ------ | --------- | --- | ------- | --------------- | --- |
| show | ip-sla | responder |     | results |                 |     |
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
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |        |            |         |     | forthiscommand. |     |
| ---- | ------ | ---------- | ------- | --- | --------------- | --- |
| show | ip-sla | <SLA-NAME> |         |     |                 |     |
| show | ip-sla | <SLA-NAME> | results |     |                 |     |
Description
46
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ----------------------- | --- | --- | --- | --- |

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
IP-SLA|47

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
48
AOS-CX10.08MonitoringGuide| (6300,6400SwitchSeries)

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
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| 6400 |     | (#) |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
start-test
start-test
IP-SLA|49

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
50
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |
| --------------------------- | ----------------------- | --- | --- |

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
| 6300 |     |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | --- | ----------------------------------------- |
| 6400 |     |     |     | executionrightsforthiscommand.            |
udp-echo
udp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>] [payload-
size
<PAYLOAD-SIZE>] [tos <TYPE-OF-SERVICE>] [probe-interval <PROBE-INTERVAL>]
IP-SLA|51

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
52
AOS-CX10.08MonitoringGuide| (6300,6400SwitchSeries)

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
[codec-type <CODEC-TYPE>] Selectsthecodec-typefortheVoipIP-SLAtest.
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
IP-SLA|53

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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 6400 |     |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | --- | ------------------------------ | --- |
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
6300 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
6400
54
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- | --- |

Chapter 8
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
n Linkmaybeestablishedatsub-optimalspeed.
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
55
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |
| --------------------------- | ----------------------- | --- |

| switch(config-if)# |       | show running-config |     | interface |
| ------------------ | ----- | ------------------- | --- | --------- |
| interface          | 1/1/1 |                     |     |           |
downshift-enable
Disablingautomaticspeeddownshift:
| switch(config-if)#  |         | interface           | 1/1/1        |     |
| ------------------- | ------- | ------------------- | ------------ | --- |
| switch(config-if)#  |         | no downshift-enable |              |     |
| Command History     |         |                     |              |     |
| Release             |         |                     | Modification |     |
| 10.07orearlier      |         |                     | --           |     |
| Command Information |         |                     |              |     |
| Platforms           | Command | context             | Authority    |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
show interface
show interface [<IFNNAME>|<IFRANGE>] [brief | physical | extended [non-zero]]
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief | physical]
show interface [lag | loopback | tunnel | vlan ] [<ID>] [extended | non-zero]
Description
Displaysactiveconfigurationsandoperationalstatusinformationforinterfaces.
| Parameter |     |     | Description              |     |
| --------- | --- | --- | ------------------------ | --- |
| <IFNAME>  |     |     | Specifiesainterfacename. |     |
<IFRANGE>
Specifiestheportidentifierrange.
| brief |     |     | Displaysbriefinfointabularformat. |     |
| ----- | --- | --- | --------------------------------- | --- |
extended
Displaysthephysicalconnectioninfointabularformat.
| non-zero |     |     | Displaysonlynonzerostatistics. |     |
| -------- | --- | --- | ------------------------------ | --- |
LAG
DisplaysLAGinterfaceinformation.
| LOOPBACK |     |     | Displaysloopbackinterfaceinformation. |     |
| -------- | --- | --- | ------------------------------------- | --- |
TUNNEL
Displaystunnelinterfaceinformation.
| VLAN |     |     | DisplaysVLANinterfaceinformation. |     |
| ---- | --- | --- | --------------------------------- | --- |
<LAG-ID>
SpecifiestheLAGnumber.Range:1-256
L1-100Mbpsdownshift|56

| Parameter     |     |     |     |     | Description                                    |     |     |
| ------------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- |
| <LOOPBACK-ID> |     |     |     |     | SpecifiestheLOOPBACKnumber.Range:0-255         |     |     |
| <TUNNEL-ID>   |     |     |     |     | SpecifiesthetunnelID.Range:1-255               |     |     |
| <VLAN-ID>     |     |     |     |     | SpecifiestheVLANID.Range:1-4094                |     |     |
| VXLAN         |     |     |     |     | DisplaystheVXLANinterfaceinformation.          |     |     |
| <VXLAN-ID>    |     |     |     |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |     |
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
|           | 2475612      | total           | packets          |                   |     | 1003506711 | total bytes |
| --------- | ------------ | --------------- | ---------------- | ----------------- | --- | ---------- | ----------- |
|           | 2311806      | unicast         |                  | packets           |     |            |             |
|           | 100369       | multicast       |                  | packets           |     |            |             |
|           |              | 63437 broadcast |                  | packets           |     |            |             |
|           |              | 0 errors        |                  |                   |     | 2462773    | dropped     |
|           |              | 0 collision     |                  |                   |     |            |             |
| Interface |              | 1/2/1 is        | down             | (Administratively |     | down)      |             |
| Admin     | state        | is down         |                  |                   |     |            |             |
| State     | information: |                 | Administratively |                   |     | down       |             |
| Link      | transitions: |                 | 0                |                   |     |            |             |
Description:
| Hardware: |     | Ethernet, | MAC | Address: | 70:72:cf:fd:e7:b4 |     |     |
| --------- | --- | --------- | --- | -------- | ----------------- | --- | --- |
MTU 9198
Type QSFP+SR4
Full-duplex
| qos              | trust | none |        |     |     |     |     |
| ---------------- | ----- | ---- | ------ | --- | --- | --- | --- |
| Speed            | 0     | Mb/s |        |     |     |     |     |
| Auto-negotiation |       |      | is off |     |     |     |     |
| Flow-control:    |       | off  |        |     |     |     |     |
57
AOS-CX10.08MonitoringGuide| (6300,6400SwitchSeries)

| Error-control: |         | off |     |     |
| -------------- | ------- | --- | --- | --- |
| VLAN Mode:     | access  |     |     |     |
| Access         | VLAN: 1 |     |     |     |
Rx
|     | 0 total | packets         |         | 0 total bytes |
| --- | ------- | --------------- | ------- | ------------- |
|     | 0       | unicast packets |         |               |
|     | 0       | multicast       | packets |               |
|     | 0       | broadcast       | packets |               |
0 errors 0 dropped
0 CRC/FCS
Tx
|     | 0 total | packets         |         | 0 total bytes |
| --- | ------- | --------------- | ------- | ------------- |
|     | 0       | unicast packets |         |               |
|     | 0       | multicast       | packets |               |
|     | 0       | broadcast       | packets |               |
0 errors 0 dropped
0 collision
Whentheinterfaceiscurrentlylinkedatadownshiftedspeed:
| switch(config-if)# |       | show interface | 1/1/1 |     |
| ------------------ | ----- | -------------- | ----- | --- |
| Interface          | 1/1/1 | is up          |       |     |
...
| Auto-negotiation    |         | is on with | downshift    | active |
| ------------------- | ------- | ---------- | ------------ | ------ |
| Command History     |         |            |              |        |
| Release             |         |            | Modification |        |
| 10.07orearlier      |         |            | --           |        |
| Command Information |         |            |              |        |
| Platforms           | Command | context    | Authority    |        |
6300 config OperatorsorAdministratorsorlocalusergroupmemberswith
| 6400 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show interface |                       | downshift-enable |                  |     |
| -------------- | --------------------- | ---------------- | ---------------- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |                  | downshift-enable |     |
Description
Displaysspeeddownshiftinformation,includingtheinterfacespeedstatusandconfiguration.
| Parameter |     |     | Description              |     |
| --------- | --- | --- | ------------------------ | --- |
| <IFNAME>  |     |     | Specifiesainterfacename. |     |
<IFRANGE>
Specifiestheportidentifierrange.
Examples
L1-100Mbpsdownshift|58

Showingautomaticdownshiftinformation:
| switch(config-if)# |     |     | show interface | downshift-enable |     |
| ------------------ | --- | --- | -------------- | ---------------- | --- |
-------------------------------------------------
|      |         | Downshift |          | Speed  |          |
| ---- | ------- | --------- | -------- | ------ | -------- |
| Port | Enabled |           | | Active | Status | | Config |
-------------------------------------------------
| 1/1/1 | yes |     | yes | 100M-FDx | auto     |
| ----- | --- | --- | --- | -------- | -------- |
| 1/1/2 | yes |     | no  | 1G       | auto     |
| 1/1/3 | yes |     | no  | 100M-FDx | 100M-FDx |
| 1/1/4 | no  |     | no  | --       | auto     |
Showingautomaticdownshiftinformationonperinterface:
| switch(config-if)# |     |     | show interface | 1/1/2 | downshift-enable |
| ------------------ | --- | --- | -------------- | ----- | ---------------- |
-------------------------------------------------
|      |         | Downshift |          | Speed  |          |
| ---- | ------- | --------- | -------- | ------ | -------- |
| Port | Enabled |           | | Active | Status | | Config |
-------------------------------------------------
| 1/1/2          | yes         |     | no      | 1G           | auto |
| -------------- | ----------- | --- | ------- | ------------ | ---- |
| Command        | History     |     |         |              |      |
| Release        |             |     |         | Modification |      |
| 10.07orearlier |             |     |         | --           |      |
| Command        | Information |     |         |              |      |
| Platforms      | Command     |     | context | Authority    |      |
6300 config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
6400
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
59
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | --- | ----------------------- | --- | --- | --- |

| Parameter     |     | Description                                     |     |     |
| ------------- | --- | ----------------------------------------------- | --- | --- |
| TUNNEL        |     | Specifiestunnelinterfaceinformation.            |     |     |
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
L1-100Mbpsdownshift|60

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6300 config OperatorsorAdministratorsorlocalusergroupmemberswith
| 6400 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
61
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |
| --------------------------- | ----------------------- | --- | --- |

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

AOS-CX 10.08 Monitoring Guide | (6300, 6400 Switch Series)

62

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

Clears the mirror statistics for all configured mirror sessions or a specified session

Mirroring | 63

| Parameter |     |     | Description                     |
| --------- | --- | --- | ------------------------------- |
| all       |     |     | Specifiesallconfiguredsessions. |
<SESSION-ID> Specifiesanumericidentifierforthesession.Range:1to4
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
64
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |
| --------------------------- | ----------------------- | --- | --- |

Addingacommenttoamirrorsession:
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
<REMOTE-URL> Specifiestheexternalstoragetowhichthepacketcapturefilewill
besaved.
Usage
Onlyfourfilescanbesavedatanypointontheswitch.Packetcapturefilesarenotsavedafterafailover
| orreboot.Viewalistofsavedfilesusingdiag |     |     | list-files. |
| --------------------------------------- | --- | --- | ----------- |
utilities
Mirroring|65

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
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --------------- | --- | --- | --- |
copy tshark-pcap
| copy tshark-pcap | <REMOTE-URL> | [vrf | <VRF-NAME>] |     |     |     |
| ---------------- | ------------ | ---- | ----------- | --- | --- | --- |
Description
CopiesthetsharkcapturedatatoafileonaTFTPorSFTPserver.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<REMOTE-URL>
SpecifiesthecapturefileonaremoteTFTPorSFTPserver.The
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
66
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- | --- | --- |

| Release             |         |         |     | Modification |
| ------------------- | ------- | ------- | --- | ------------ |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
6300 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6400           |     |     |     | forthiscommand. |
| -------------- | --- | --- | --- | --------------- |
| destination    | cpu |     |     |                 |
| destination    | cpu |     |     |                 |
| no destination | cpu |     |     |                 |
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
| switch#                  | config |             |     |     |
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
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
Mirroring|67

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
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
68
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- |

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
Sincefileanddelete-fileareoptional,thebehaviorofthebasecommanddiag utilities tshark
doesnotsaveanythingtoafile,andinsteaddumpsthetsharksessiontotheconsoleuntilCTRL + cis
entered.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
file
Savescapturedpacketstoatemporaryfile.
| delete-file |     |     | Deletesthemostrecentcapturedfile. |     |     |
| ----------- | --- | --- | --------------------------------- | --- | --- |
Example
Performingdiagnostic:
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
Mirroring|69

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

AOS-CX 10.08 Monitoring Guide | (6300, 6400 Switch Series)

70

n Whenusingcommand -rtoreadafile,donotprovideanydirectorypathcharacters.Uselist-files
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
switch#
|     | diag utilities | tcpdump | command | -r my_capture_file.pcap |     |
| --- | -------------- | ------- | ------- | ----------------------- | --- |
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
| Successfully | removed     | file |                   |     |     |
| ------------ | ----------- | ---- | ----------------- | --- | --- |
| Command      | History     |      |                   |     |     |
| Release      |             |      | Modification      |     |     |
| 10.08        |             |      | Commandintroduced |     |     |
| Command      | Information |      |                   |     |     |
Mirroring|71

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6300 Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
| 6400 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
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
Description
Enablesthemirroringsessionforthecurrentcommandcontext.
Usage
Bydefault,mirroringsessionsaredisabled.
Whenamirroringsessionisenabled,theshow mirrorcommandforthatsessionIDshowsanAdmin
| StatusofenableandanOperation |     |     | Statusofenabled. |     |
| ---------------------------- | --- | --- | ---------------- | --- |
IfsFlowisenabledonaninterfaceandamirroringsessionspecifiesthesameinterfaceasthesourceof
receivedtraffic(thesourceisconfiguredwithadirectionofrxorboth):
72
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- |

n Theattempttoenablethemirroringsessionfailsandanerrorisreturned.
Whenadding,removing,orchangingtheconfigurationofasourceinterfaceinanenabledmirroringsession,
packetsfromothermirrorsourcesusingthesamedestinationinterfacemightbeinterrupted.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
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
| Parameter    |     |     | Description                              |     |
| ------------ | --- | --- | ---------------------------------------- | --- |
| <SESSION-ID> |     |     | Specifiesthesessionidentifier.Range:1to4 |     |
Examples
| switch(config)# | mirror | session | 1   |     |
| --------------- | ------ | ------- | --- | --- |
switch(config-mirror-1)#
Mirroring|73

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
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
74
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |
| --------------------------- | --- | ----------------------- | --- | --- |

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
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingsummaryinformationaboutallconfiguredmirroringsessions:
switch#
show mirror
| ID Admin | Status | Operation | Status |     |
| -------- | ------ | --------- | ------ | --- |
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
| Command        | History     |     |              |     |
| -------------- | ----------- | --- | ------------ | --- |
| Release        |             |     | Modification |     |
| 10.07orearlier |             |     | --           |     |
| Command        | Information |     |              |     |
Mirroring|75

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
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
| rx   |     |     |     |     | Mirroronlyreceivedpackets.               |     |
| tx   |     |     |     |     | Mirroronlytransmittedpackets.            |     |
Usage
Thereisalimitofsourceinterfacesineachdirectionofagivenmirrorsession:
| Switch |     | Source | interface |     | limit |     |
| ------ | --- | ------ | --------- | --- | ----- | --- |
| 6300   |     | 64     |           |     |       |     |
| 6400   |     | 64     |           |     |       |     |
However,thereisapracticallimittotheamountoftrafficthatamirrordestinationcantransmit.For
example,mirroringsessionwithmultiple10Gsourcescanoverwhelmasingle10Gdestination.
Whenadding,removing,orchangingtheconfigurationofasourceportinanenabledmirroringsession,packets
fromothermirrorsourcesusingthesamedestinationportmightbeinterrupted.
Examples
Configuringamirroredtrafficsourceinterface:
76
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ----------------------- | --- | --- | --- | --- |

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
switch(config-mirror-3)#
|     |     | source | interface |     | 1/1/2 rx |
| --- | --- | ------ | --------- | --- | -------- |
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
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
Command Information
Mirroring|77

| Platforms |     | Command |     | context |     |     | Authority |
| --------- | --- | ------- | --- | ------- | --- | --- | --------- |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| source | vlan |     |     |     |     |     |     |
| ------ | ---- | --- | --- | --- | --- | --- | --- |
Syntax
| source    | vlan | <VLAN-NUM> | {rx | | tx  | | both} |       |     |
| --------- | ---- | ---------- | --- | ----- | ------- | ----- | --- |
| no source | vlan | <VLAN-NUM> |     | [rx | | tx |    | both] |     |
Description
AddsorremovesVLANasasourceoftraffictobemirrored.MorethanonesourceVLANcanbe
configuredinamirrorsession.EachVLANmayspecifyitsowndirection.
ThenoversionofthecommandceasesmirroringtrafficfromthespecifiedsourceVLANandremoves
thesourcefromthemirrorconfiguration.
Thereisalimitof1024sourceVLANsineachdirectionofagivenmirrorsession.ThesameVLANcanbe
configuredasamirrorsourceformultiplesessions.
| Command | context |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
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
| switch(config)#          |     |     | mirror | session | 1    |     |      |
| ------------------------ | --- | --- | ------ | ------- | ---- | --- | ---- |
| switch(config-mirror-1)# |     |     |        | source  | vlan | 10  | both |
CreateasecondmirrorsessionandaddVLAN10asatransmitsourcesoftrafficandVLAN20inboth
receiveandtransmitdirections.
| switch(config)#          |     |     | mirror | session | 2    |     |      |
| ------------------------ | --- | --- | ------ | ------- | ---- | --- | ---- |
| switch(config-mirror-2)# |     |     |        | source  | vlan | 10  | tx   |
| switch(config-mirror-2)# |     |     |        | source  | vlan | 20  | both |
Reconfigurethesourceinsession2tobereceiveonlybyrespecifyingthesourceinterfaceconfiguration.
78
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- |

| switch(config-mirror-2)# | source | vlan 10 rx |
| ------------------------ | ------ | ---------- |
Fromthesecondsession,removethefirstsourceinterfaceentirelyandremovethetransmitdirection
fromtheothersothatmirroringonlyoccursinthereceivedirection.
| switch(config-mirror-2)# | no source | vlan 10 |
| ------------------------ | --------- | ------- |
switch(config-mirror-2)#
|     | no source | vlan 20 tx |
| --- | --------- | ---------- |
Messagereceivedwhentryingtoaddmorethan1024mirrorsourceVLANs
| switch(config-mirror-2)# | source | vlan 2000 rx |
| ------------------------ | ------ | ------------ |
The maximum number of source VLANs per mirror session is 1024 in each direction
Mirroring|79

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
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- | --- |

Chapter 11

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

AOS-CX 10.08 Monitoring Guide | (6300, 6400 Switch Series)

81

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

Power-over-Ethernet | 82

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400         |                         |     |     | forthiscommand. |
| ------------ | ----------------------- | --- | --- | --------------- |
| lldp med     | poe                     |     |     |                 |
| lldp med poe | [priority-override]     |     |     |                 |
| no lldp med  | poe [priority-override] |     |     |                 |
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
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --------------- |
power-over-ethernet
power-over-ethernet
no power-over-ethernet
83
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- |

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
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400                   |     |             |             |             | forthiscommand. |          |        |     |
| ---------------------- | --- | ----------- | ----------- | ----------- | --------------- | -------- | ------ | --- |
| power-over-ethernet    |     |             |             | allocate-by |                 |          |        |     |
| power-over-ethernet    |     | allocate-by |             |             | {usage          | | class} |        |     |
| no power-over-ethernet |     |             | allocate-by |             | {usage          | |        | class} |     |
Description
Configuresthepowerallocationmethod.Powerallocationmethodisinitiallybasedonusage.PSE
AllocatedpowervaluewillchangetoLLDPnegotiatedpowerifandwhenLLDPexchangetakesplace
betweenPSEandPD.WhenthereisnoLLDPnegotiation,PSEAllocatedPowerValuewillbetheactual
instantaneouspowerdrawandreservepowerbasedonactualconsumption.Inallocate-byclass,power
allocationisbasedonPDrequestedclassandPSEallocatedpowervaluewillbetheLLDPnegotiated
powerwhenLLDPexchangetakesplacebetweenPSEandPD.WhenthereisnoLLDPnegotiation,PSE
Power-over-Ethernet|84

AllocatePowerwillbebasedonPDclass.ReservepowerisbasedonPDClass.Bydefault,power
allocationisbyusage.
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
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400                   |     |           |           |             | forthiscommand. |     |     |
| ---------------------- | --- | --------- | --------- | ----------- | --------------- | --- | --- |
| power-over-ethernet    |     |           |           | always-on   |                 |     |     |
| power-over-ethernet    |     | always-on |           | <MODULE-ID> |                 |     |     |
| no power-over-ethernet |     |           | always-on | <MODULE-ID> |                 |     |     |
Description
Always-onPoEisafeaturethatprovidestheabilitytotheswitchtocontinuetoprovidepoweracrossa
softreboot.Itisapplicableonlytotheinterfaceswhichwereconnectedanddeliveringbeforethesoft
reboot.Also,powerwillnotbedeliveredifpowertotheswitchisinterrupted.Thiscommandenablesor
disablesthealways-onPoEfeatureattheswitchortheslotlevel.Bydefault,always-onPoEisenabledat
theswitchortheslotlevel.
Thenoformofthiscommanddisablespowerdistributiononsoftreboot.
| Parameter   |     |     |     |     | Description                                   |     |     |
| ----------- | --- | --- | --- | --- | --------------------------------------------- | --- | --- |
| <MODULE-ID> |     |     |     |     | Modulenumbertoapplyalways-onPoEconfiguration. |     |     |
Examples
Enablingper-interfacepowerdistribution:
85
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- |

| switch(config)# |     | power-over-ethernet |     |     | always-on | 1/1 |     |
| --------------- | --- | ------------------- | --- | --- | --------- | --- | --- |
Disablingper-interfacepowerdistribution:
| switch(config)#     |         | no  | power-over-ethernet |              | always-on | 1/1 |     |
| ------------------- | ------- | --- | ------------------- | ------------ | --------- | --- | --- |
| Command History     |         |     |                     |              |           |     |     |
| Release             |         |     |                     | Modification |           |     |     |
| 10.07orearlier      |         |     |                     | --           |           |     |     |
| Command Information |         |     |                     |              |           |     |     |
| Platforms           | Command |     | context             | Authority    |           |     |     |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400                   |     |                |                | forthiscommand. |        |     |     |
| ---------------------- | --- | -------------- | -------------- | --------------- | ------ | --- | --- |
| power-over-ethernet    |     |                | assigned-class |                 |        |     |     |
| power-over-ethernet    |     | assigned-class |                | {3 |            | 4 | 6} |     |     |
| no power-over-ethernet |     |                | assigned-class |                 |        |     |     |
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
switch(config)#
|                    |     | interface | 1/1/1               |     |                |     |     |
| ------------------ | --- | --------- | ------------------- | --- | -------------- | --- | --- |
| switch(config-if)# |     |           | power-over-ethernet |     | assigned-class |     | 4   |
ResettingPoEassignedclasstodefault:
| switch(config-if)# |     |     | no power-over-ethernet |     | assigned-class |     | 4   |
| ------------------ | --- | --- | ---------------------- | --- | -------------- | --- | --- |
ShowingQuickPoEenabled:
Power-over-Ethernet|86

| switch(config)# |     | power-over-ethernet |     |     | quick-poe | 1/1 |     |
| --------------- | --- | ------------------- | --- | --- | --------- | --- | --- |
switch(config)#
|                 |     | interface           | 1/1/1 |     |                |     |     |
| --------------- | --- | ------------------- | ----- | --- | -------------- | --- | --- |
| switch(config)# |     | power-over-ethernet |       |     | assigned-class |     | 4   |
Interface assigned class cannot be configured when Quick PoE is enabled.
| Command History     |         |         |     |              |     |     |     |
| ------------------- | ------- | ------- | --- | ------------ | --- | --- | --- |
| Release             |         |         |     | Modification |     |     |     |
| 10.07orearlier      |         |         |     | --           |     |     |     |
| Command Information |         |         |     |              |     |     |     |
| Platforms           | Command | context |     | Authority    |     |     |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400                   |     |                |                | forthiscommand. |     |     |     |
| ---------------------- | --- | -------------- | -------------- | --------------- | --- | --- | --- |
| power-over-ethernet    |     |                | pre-std-detect |                 |     |     |     |
| power-over-ethernet    |     | pre-std-detect |                |                 |     |     |     |
| no power-over-ethernet |     | pre-std-detect |                |                 |     |     |     |
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
| switch(config)#    |     | interface           | 1/1/1 |     |                |     |     |
| ------------------ | --- | ------------------- | ----- | --- | -------------- | --- | --- |
| switch(config-if)# |     | power-over-ethernet |       |     | pre-std-detect |     |     |
Disablingstandarddevicedetection:
| switch(config-if)#  |     | no power-over-ethernet |     |              | pre-std-detect |     |     |
| ------------------- | --- | ---------------------- | --- | ------------ | -------------- | --- | --- |
| Command History     |     |                        |     |              |                |     |     |
| Release             |     |                        |     | Modification |                |     |     |
| 10.07orearlier      |     |                        |     | --           |                |     |     |
| Command Information |     |                        |     |              |                |     |     |
87
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- | --- | --- | --- |

| Platforms | Command |     | context |     | Authority |     |
| --------- | ------- | --- | ------- | --- | --------- | --- |
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400                   |     |          |          |           | forthiscommand. |               |
| ---------------------- | --- | -------- | -------- | --------- | --------------- | ------------- |
| power-over-ethernet    |     |          |          | priority  |                 |               |
| power-over-ethernet    |     | priority |          | {critical |                 | | high | low} |
| no power-over-ethernet |     |          | priority | {critical |                 | | high | low} |
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
| switch(config-if)# |     |           | power-over-ethernet |       |     | priority high     |
ResettingthePoEprioritytodefault:
| switch(config-if)#  |         |     | no power-over-ethernet |     |              | priority high |
| ------------------- | ------- | --- | ---------------------- | --- | ------------ | ------------- |
| Command History     |         |     |                        |     |              |               |
| Release             |         |     |                        |     | Modification |               |
| 10.07orearlier      |         |     |                        |     | --           |               |
| Command Information |         |     |                        |     |              |               |
| Platforms           | Command |     | context                |     | Authority    |               |
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400                |     |           |     |             | forthiscommand. |     |
| ------------------- | --- | --------- | --- | ----------- | --------------- | --- |
| power-over-ethernet |     |           |     | quick-poe   |                 |     |
| power-over-ethernet |     | quick-poe |     | <MODULE-ID> |                 |     |
no power-over-ethernet
Description
QuickPoEisafeaturethatprovidestheabilityfortheswitchtoprovidepowertotheconnected
powereddeviceassoonasswitchgoesthroughcoldreboot.WhenquickPoEisenabledonthe
subsystemPoEportdisablementandPDdemotionisnotallowed.alsoquickPoEenablementisnot
Power-over-Ethernet|88

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
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablinganddisablingquickPoE:
| switch(config)#    |     | power-over-ethernet |                     |     |     | quick-poe | 1/2 |
| ------------------ | --- | ------------------- | ------------------- | --- | --- | --------- | --- |
| switch(config)#    |     | no                  | power-over-ethernet |     |     | quick-poe | 1/2 |
| switch(config-if)# |     |                     | power-over-ethernet |     |     | quick-poe | 1/1 |
PoE must be enabled on all interfaces before enabling Quick PoE
| switch(config-if)# |     |     | power-over-ethernet |     |     | quick-poe | 1/3 |
| ------------------ | --- | --- | ------------------- | --- | --- | --------- | --- |
All interfaces must use the default assigned class before enabling Quick PoE
| Command History     |         |     |         |     |              |     |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- | --- |
| Release             |         |     |         |     | Modification |     |     |
| 10.07orearlier      |         |     |         |     | --           |     |     |
| Command Information |         |     |         |     |              |     |     |
| Platforms           | Command |     | context |     | Authority    |     |     |
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400                   |     |           |           |              | forthiscommand. |     |     |
| ---------------------- | --- | --------- | --------- | ------------ | --------------- | --- | --- |
| power-over-ethernet    |     |           |           | threshold    |                 |     |     |
| power-over-ethernet    |     | threshold |           | <PERCENTAGE> |                 |     |     |
| no power-over-ethernet |     |           | threshold | <PERCENTAGE> |                 |     |     |
Description
Setsthethresholdatwhichthesystemwillsendanexcesspowerconsumptionnotificationtrap.Default
valueis80percentage.
Thenoformofthiscommandresetstheactiontodefault.
89
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- |

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
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400                   |     |      | forthiscommand. |     |     |
| ---------------------- | --- | ---- | --------------- | --- | --- |
| power-over-ethernet    |     | trap |                 |     |     |
| power-over-ethernet    |     | trap |                 |     |     |
| no power-over-ethernet |     | trap |                 |     |     |
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
Power-over-Ethernet|90

| Release        |             |         |         |     | Modification |
| -------------- | ----------- | ------- | ------- | --- | ------------ |
| 10.07orearlier |             |         |         |     | --           |
| Command        | Information |         |         |     |              |
| Platforms      |             | Command | context |     | Authority    |
6300 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400      |              |       |                  |     | forthiscommand. |
| --------- | ------------ | ----- | ---------------- | --- | --------------- |
| show      | lldp         | local |                  |     |                 |
| show lldp | local-device |       | [<INTERFACE-ID>] |     |                 |
Description
DisplaysinformationadvertisedbytheswitchiftheLLDPfeatureisenabledbyuser.
| Parameter      |     |     |     |     | Description                                  |
| -------------- | --- | --- | --- | --- | -------------------------------------------- |
| <INTERFACE-ID> |     |     |     |     | Specifiesaninterface.Format:member/slot/port |
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
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
91
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | --- | ----------------------- | --- | --- | --- |

| Platforms | Command | context | Authority                                            |     |
| --------- | ------- | ------- | ---------------------------------------------------- | --- |
| 6300      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |
Operator(>)orManager
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
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
Onthe6400SwitchSeries,interfaceidentificationdiffers.
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
| Neighbor        | Chassis-ID         |             | : 84:d4:7e:ce:5d:68 |      |
| --------------- | ------------------ | ----------- | ------------------- | ---- |
| Neighbor        | Management-Address |             | : 169.254.41.250    |      |
| Chassis         | Capabilities       | Available   | : Bridge,           | WLAN |
| Chassis         | Capabilities       | Enabled     | :                   |      |
| Neighbor        | Port-ID            |             | : 84:d4:7e:ce:5d:68 |      |
| Neighbor        | Port-Desc          |             | : eth0              |      |
| TTL             |                    |             | : 120               |      |
| Neighbor        | Port               | VLAN ID     | :                   |      |
| Neighbor        | PoEplus            | information | : DOT3              |      |
| Neighbor        | Device             | Type        | : TYPE2             | PD   |
| Neighbor        | Power              | Priority    | : Unkown            |      |
| Neighbor        | Power              | Source      | : Primary           |      |
| Neighbor        | Power              | Requested   | : 25.0              | W    |
| Neighbor        | Power              | Allocated   | : 0.0 W             |      |
| Neighbor        | Power              | Supported   | : No                |      |
| Neighbor        | Power              | Enabled     | : No                |      |
| Neighbor        | Power              | Class       | : 5                 |      |
| Neighbor        | Power              | Paircontrol | : No                |      |
| Neighbor        | Power              | Pairs       | : SIGNAL            |      |
| Command History |                    |             |                     |      |
| Release         |                    |             | Modification        |      |
| 10.07orearlier  |                    |             | --                  |      |
Power-over-Ethernet|92

| Command   | Information |         |     |         |           |     |
| --------- | ----------- | ------- | --- | ------- | --------- | --- |
| Platforms |             | Command |     | context | Authority |     |
6300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
| 6400 |     | (#) |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show | power-over-ethernet |     |     |     |     |     |
| ---- | ------------------- | --- | --- | --- | --- | --- |
6200SwitchSeries:
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
<MEMBER-ID>
Displaysthedetailedstatusofgivenmember.
| <MODULE-ID> |     |     |     |     | Displaysdetailedstatusforthegivenmodule. |     |
| ----------- | --- | --- | --- | --- | ---------------------------------------- | --- |
<IFRANGE>
Portidentifierrange.
| <IFNAME> |     |     |     |     | Displaythedetailedstatusofgivenport. |     |
| -------- | --- | --- | --- | --- | ------------------------------------ | --- |
brief
Displaythebriefstatusofallportsorthegivenport.
Examples
Showingsampleoutputforshowpower-over-ethernetonstandaloneboxwithVSFcapabiity:
|     | switch#        | show power-over-ethernet |              |        |                 |        |
| --- | -------------- | ------------------------ | ------------ | ------ | --------------- | ------ |
|     | System Power   | Status                   | for          | member | 1               |        |
|     | Configured     |                          | Power Status |        | : No redundancy |        |
|     | Operational    |                          | Power Status |        | : No redundancy |        |
|     | Total          | Available                | Power        |        | : 740 W         |        |
|     | Total          | Failover                 | Pwr          | Avl    | : 0 W           |        |
|     | Total          | Redundancy               | Power        |        | : 0 W           |        |
|     | Total          | Power                    | Drawn        |        | : 0 W           | +/- 6W |
|     | Total          | Power                    | Reserved     |        | : 0 W           |        |
|     | Total          | Remaining                | Power        |        | : 740 W         |        |
|     | Trap Threshold |                          |              |        | : 80 %          |        |
|     | Trap Enabled   |                          |              |        | : Yes           |        |
|     | Always-on      | PoE                      | Enabled      |        | : 1/1           |        |
|     | Quick          | PoE Enabled              |              |        | : None          |        |
|     | Internal       | Power                    |              |        |                 |        |
93
| AOS-CX10.08MonitoringGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | --- | --- | ----------------------- | --- | --- | --- |

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
| switch# show     | power-over-ethernet |         |        | member          | 1   |
| ---------------- | ------------------- | ------- | ------ | --------------- | --- |
| System Power     | Status              | for     | member | 1               |     |
| Configured       | Power               | Status  |        | : No redundancy |     |
| Operational      | Power               | Status  |        | : No redundancy |     |
| Total Available  |                     | Power   |        | : 740 W         |     |
| Total Failover   |                     | Pwr     | Avl    | : 0 W           |     |
| Total Redundancy |                     | Power   |        | : 0 W           |     |
| Total Power      | Drawn               |         |        | : 0 W +/-       | 6W  |
| Total Power      | Reserved            |         |        | : 0 W           |     |
| Total Remaining  |                     | Power   |        | : 740 W         |     |
| Trap Threshold   |                     |         |        | : 80 %          |     |
| Trap Enabled     |                     |         |        | : No            |     |
| Always-on        | PoE                 | Enabled |        | : 1/1           |     |
| Quick PoE        | Enabled             |         |        | : 1/1           |     |
| Internal         | Power               |         |        |                 |     |
Total Power
| PS (Watts)          |     |     | Status                |     |     |
| ------------------- | --- | --- | --------------------- | --- | --- |
| ----- ------------- |     |     | --------------------- |     |     |
| 1 0                 |     |     | Absent                |     |     |
| 2 740               |     |     | Ok                    |     |     |
Showingsampleoutputforpower-over-ethernetbriefinaVSFstack:
| switch# show | power-over-ethernet |     |     | brief |     |
| ------------ | ------------------- | --- | --- | ----- | --- |
Power-over-Ethernet|94

| Status and | Configuration  | Information |       | for | PoE          |          |     |     |
| ---------- | -------------- | ----------- | ----- | --- | ------------ | -------- | --- | --- |
| Member     | 1 Power Status |             |       |     |              |          |     |     |
| Available: | 370 W          | Reserved:   | 55.60 |     | W Remaining: | 314.40 W |     |     |
| Always-on  | PoE Enabled:   |             | 1/1   |     |              |          |     |     |
| Quick      | PoE Enabled:   | None        |       |     |              |          |     |     |
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
| switch#    | show power-over-ethernet |             |     | 1/1/1 | brief      |     |     |     |
| ---------- | ------------------------ | ----------- | --- | ----- | ---------- | --- | --- | --- |
| Status and | Configuration            | Information |     | for   | port 1/1/1 |     |     |     |
95
AOS-CX10.08MonitoringGuide| (6300,6400SwitchSeries)

| Member     | 1Power | Status       |           |       |     |            |          |     |     |
| ---------- | ------ | ------------ | --------- | ----- | --- | ---------- | -------- | --- | --- |
| Available: |        | 370 W        | Reserved: | 55.60 | W   | Remaining: | 314.40 W |     |     |
| Always-on  |        | PoE Enabled: |           | 1/1   |     |            |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En  | Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | --- | -------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes | Low | Off | Class | 0.0 | W 0.0 | W Denied | None 4 | 2   |
| ----- | --- | --- | --- | ----- | --- | ----- | -------- | ------ | --- |
Showingsampleoutputforpower-over-ethernetbriefforinterfacerange:
| switch#    | show              | power-over-ethernet |             | 1/1/1-1/1/2 |     | brief            |          |     |     |
| ---------- | ----------------- | ------------------- | ----------- | ----------- | --- | ---------------- | -------- | --- | --- |
| Status     | and Configuration |                     | Information |             | for | port 1/1/1-1/1/2 |          |     |     |
| Member     | 1Power            | Status              |             |             |     |                  |          |     |     |
| Available: |                   | 370 W               | Reserved:   | 55.60       | W   | Remaining:       | 314.40 W |     |     |
| Always-on  |                   | PoE Enabled:        |             | 1/1         |     |                  |          |     |     |
PoE Pwr Power Pre-std Alloc PSE Pwr PD Pwr PoE Port PD Cls Type
| Port | En  | Priority | Detect | Act | Rsrvd | Draw | Status | Sign |     |
| ---- | --- | -------- | ------ | --- | ----- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes | Low | Off | Class | 0.0 | W 0.0 | W Denied | None 4 | 2   |
| ----- | --- | --- | --- | ----- | --- | ----- | -------- | ------ | --- |
1/1/2 Yes Critical Off Usage 1.6 W 1.5 W Delivering* Single 0 1
Showingsampleoutputforpower-over-ethernetforamissinglinecard:
| switch# | show   | power-over-ethernet |     | 1/3      | brief |     |     |     |     |
| ------- | ------ | ------------------- | --- | -------- | ----- | --- | --- | --- | --- |
| Module  | 1/3 is | not physically      |     | present. |       |     |     |     |     |
Showingsampleoutputforpower-over-ethernetbriefforamissingmember:
| switch# | show | power-over-ethernet |     | member   | 3   | brief |     |     |     |
| ------- | ---- | ------------------- | --- | -------- | --- | ----- | --- | --- | --- |
| Member  | 3 is | not physically      |     | present. |     |       |     |     |     |
Showingsampleoutputforpower-over-ethernetportwhenphysicalinterfaceisnotpresent:
| switch#        | show        | power-over-ethernet |          | 2/1/1 |              |     |     |     |     |
| -------------- | ----------- | ------------------- | -------- | ----- | ------------ | --- | --- | --- | --- |
| Interface      | 2/1/1       | is not              | present. |       |              |     |     |     |     |
| Command        | History     |                     |          |       |              |     |     |     |     |
| Release        |             |                     |          |       | Modification |     |     |     |     |
| 10.07orearlier |             |                     |          |       | --           |     |     |     |     |
| Command        | Information |                     |          |       |              |     |     |     |     |
Power-over-Ethernet|96

| Platforms | Command | context | Authority                                            |
| --------- | ------- | ------- | ---------------------------------------------------- |
| 6300      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
6400 (#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
97
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |
| --------------------------- | ----------------------- | --- | --- |

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
| !Version | ArubaOS-CX | Virtual.10.01. |     |
| -------- | ---------- | -------------- | --- |
| led      | locator on |                |     |
!
!
!
| snmp-server | vrf | default |     |
| ----------- | --- | ------- | --- |
| snmp-server | vrf | mgmt    |     |
98
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |
| --------------------------- | --- | ----------------------- | --- |

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
1. EnableSNMPontheswitchbyenteringthesnmp-servervrfcommand.
|     | switch(config)# | snmp-server | vrf mgmt    |     |     |     |
| --- | --------------- | ----------- | ----------- | --- | --- | --- |
|     | switch(config)# | snmp-server | vrf default |     |     |     |
2. ConfiguretheSNMPv2Ccommunitytopublicbyenteringthesnmp-server community public
command.Inthisinstance,publicisaread-onlycommunitystring.
ArubaAirWave|99

|     |     | switch(config)# | snmp-server |     | community |     | public |     |
| --- | --- | --------------- | ----------- | --- | --------- | --- | ------ | --- |
3. Thecommunity-stringisusedbySNMPv1andSNMPv2Cforunencryptedauthentication.SNMPv3
letsyouencrypttheauthenticationmechanism.ToenableSNMPv3,enterthesnmpv3 userand
|     | snmpv3 | contextcommands. |     |     |     |     |     |     |
| --- | ------ | ---------------- | --- | --- | --- | --- | --- | --- |
switch(config)# snmpv3 user Admin auth sha auth-pass ciphertext
AQBapZHf2d20GYr/xcGUzYzm0zjNf/4VKHtSqbNImqtfYbJYCgAAALkGFJVcSp3nZ3o=
|     |     | priv des | priv-pass ciphertext |     |     |     |     |     |
| --- | --- | -------- | -------------------- | --- | --- | --- | --- | --- |
AQBapb0H2poBQKXPoVsC9L9qzZyfJQnzR7hmTr7LGsOsI7K3CgAAAKP98Rq2jfTrFwQ=
switch(config)#
|     |     |     | snmpv3 | context |     | Admin |     |     |
| --- | --- | --- | ------ | ------- | --- | ----- | --- | --- |
FordiscoveringdevicesinAirWavethroughtheSNMPv3community,theSNMPv3contextnameis
notmandatory.DevicescanstillbediscoveredinArubaAirWavewithouttheSNMPv3context
name.
4. Enterthelogging commandforenablingsyslogforwardingtoaremotesyslogserver,suchas
AirWave:
|     |     | switch(config)# | logging | 10.0.10.2 |     | severity | debug |     |
| --- | --- | --------------- | ------- | --------- | --- | -------- | ----- | --- |
5. SNMPtrapsenableanagenttonotifythemanagementstationofsignificanteventsbywayofan
unsolicitedSNMPmessage.EnableSNMPtrapsbyenteringthesnmp-server hostcommand:
switch(config)# snmp-server host 10.10.10.10 trap version v2c vrf default
SNMPtrapscannotbeforwardedfromAOS-CX10.00switchesthathavetheVRFconfiguredas
mgmt.LaterversionsofAOS-CXsupportSNMPtrapforwardingevenwhentheVRFisconfiguredas
defaultormgmt.
6. ForinformationonhowtoaddadeviceformonitoringintheArubaAirWaveuserinterface,see
thedocumentationforArubaAirWave.
logging
| logging |                            | {<IPV4-ADDR>  | | <IPV6-ADDR> |              | | <HOSTNAME>} |          |                   |             |
| ------- | -------------------------- | ------------- | ------------- | ------------ | ------------- | -------- | ----------------- | ----------- |
|         | [udp                       | [<PORT-NUM>]  | | tcp         | [<PORT-NUM>] |               | |        | tls [<PORT-NUM>]] |             |
|         | [include-auditable-events] |               |               | [severity    |               | <LEVEL>] | [vrf              | <VRF-NAME>] |
| logging |                            | {<IPV4-ADDR>  | | <IPV6-ADDR> |              | | <HOSTNAME>} |          |                   |             |
|         | [tls                       | [<PORT-NUM>]] | [auth-mode    |              | {certificate  |          | | subject-name}]  |             |
[legay-tls-renegotiation] [include-auditable-events] [severity <LEVEL>]
|     | [vrf    | <VRF-NAME>]  |               |     |     |            |     |     |
| --- | ------- | ------------ | ------------- | --- | --- | ---------- | --- | --- |
| no  | logging | {<IPV4-ADDR> | | <IPV6-ADDR> |     | |   | <HOSTNAME> |     |     |
Description
Enablessyslogforwardingtoaremotesyslogserver.
Thenoformofthiscommanddisablessyslogforwardingtoaremotesyslogserver.
100
| AOS-CX10.08MonitoringGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |

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

Aruba AirWave | 101

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
102
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | --- | ----------------------- | --- | --- | --- |

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
ArubaAirWave|103

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
104
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- | --- |

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
ArubaAirWave|105

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
106
| AOS-CX10.08MonitoringGuide| |     |     | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- |

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

Aruba AirWave | 107

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
| !Version | ArubaOS-CX |     | TL.10.00.0003-8017-gdeb0606~dirty |     |     |
| -------- | ---------- | --- | --------------------------------- | --- | --- |
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
108
| AOS-CX10.08MonitoringGuide| |     | (6300,6400SwitchSeries) |     |     |     |
| --------------------------- | --- | ----------------------- | --- | --- | --- |

Chapter 13
|           |           |           | Support | and Other | Resources |
| --------- | --------- | --------- | ------- | --------- | --------- |
| Support   | and Other | Resources |         |           |           |
| Accessing | Aruba     | Support   |         |           |           |
ArubaSupportServices https://www.arubanetworks.com/support-services/
ArubaSupportPortal https://asp.arubanetworks.com/
NorthAmericatelephone
1-800-943-4526(US&CanadaToll-FreeNumber)
+1-408-754-1200(Primary-TollNumber)
+1-650-385-6582(Backup-TollNumber-Useonlywhenallother
numbersarenotworking)
Internationaltelephone https://www.arubanetworks.com/support-services/contact-
support/
BesuretocollectthefollowinginformationbeforecontactingSupport:
n Technicalsupportregistrationnumber(ifapplicable)
n Productname,modelorversion,andserialnumber
n Operatingsystemnameandversion
n Firmwareversion
n Errormessages
n Product-specificreportsandlogs
n Add-onproductsorcomponents
n Third-partyproductsorcomponents
| Other | useful sites |     |     |     |     |
| ----- | ------------ | --- | --- | --- | --- |
Otherwebsitesthatcanbeusedtofindinformation:
AirheadssocialforumsandKnowledge https://community.arubanetworks.com/
Base
Softwarelicensing https://lms.arubanetworks.com/
End-of-Lifeinformation https://www.arubanetworks.com/support-services/end-of-life/
Arubasoftwareanddocumentation https://asp.arubanetworks.com/downloads
| Accessing | Updates |     |     |     |     |
| --------- | ------- | --- | --- | --- | --- |
YoucanaccessupdatesfromtheArubaSupportPortalortheHPEMyNetworkingWebsite.
| Aruba | Support | Portal |     |     |     |
| ----- | ------- | ------ | --- | --- | --- |
109
| AOS-CX10.08MonitoringGuide| | (6300,6400SwitchSeries) |     |     |     |     |
| --------------------------- | ----------------------- | --- | --- | --- | --- |

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
documentation, send any errors, suggestions, or comments to Documentation Feedback
(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

Support and Other Resources | 110