AOS-CX 10.12 Monitoring
Guide

6200 Switch Series

Published: August 2023
Edition: 2

Copyright Information

© Copyright 2023 Hewlett Packard Enterprise Development LP.

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
| Contents                                          |                                  |         |                    | 3   |
| ------------------------------------------------- | -------------------------------- | ------- | ------------------ | --- |
| About                                             | this document                    |         |                    | 6   |
| Applicableproducts                                |                                  |         |                    | 6   |
| Latestversionavailableonline                      |                                  |         |                    | 6   |
| Commandsyntaxnotationconventions                  |                                  |         |                    | 6   |
| Abouttheexamples                                  |                                  |         |                    | 7   |
| Identifyingswitchportsandinterfaces               |                                  |         |                    | 7   |
| Monitoring                                        | hardware                         | through | visual observation | 9   |
| ConfirmingnormaloperationoftheswitchbyreadingLEDs |                                  |         |                    | 9   |
| Detectingiftheswitchisnotreadyforafailoverevent   |                                  |         |                    | 10  |
| FindingfaultedcomponentsusingtheswitchLEDs        |                                  |         |                    | 10  |
| IP Flow                                           | Information                      | Export  |                    | 12  |
| SupportedPlatform                                 |                                  |         |                    | 12  |
| Flowmonitors                                      |                                  |         |                    | 12  |
| Flowexporters                                     |                                  |         |                    | 12  |
| Destinations                                      |                                  |         |                    | 13  |
| FlowRecords                                       |                                  |         |                    | 13  |
| ConfiguringIPFlowInformationExport                |                                  |         |                    | 14  |
|                                                   | Stepone:CreateFlowRecords        |         |                    | 14  |
|                                                   | Steptwo:Configureflowexporter(s) |         |                    | 15  |
|                                                   | Stepthree:Configureamonitor(s)   |         |                    | 16  |
Stepfour:(Optional)EnableApplicationRecognitionandapplyaflowmonitortointer-
|                         | faces                              |              |          | 17  |
| ----------------------- | ---------------------------------- | ------------ | -------- | --- |
| FAQsandTroubleshooting  |                                    |              |          | 17  |
| Boot                    | commands                           |              |          | 19  |
| bootset-default         |                                    |              |          | 19  |
| bootsystem              |                                    |              |          | 19  |
| showboot-history        |                                    |              |          | 21  |
| Switch                  | system                             | and hardware | commands | 24  |
| External                | storage                            |              |          | 25  |
| Externalstoragecommands |                                    |              |          | 25  |
|                         | address                            |              |          | 25  |
|                         | directory                          |              |          | 26  |
|                         | disable                            |              |          | 27  |
|                         | enable                             |              |          | 27  |
|                         | external-storage                   |              |          | 28  |
|                         | password(external-storage)         |              |          | 29  |
|                         | showexternal-storage               |              |          | 30  |
|                         | showrunning-configexternal-storage |              |          | 31  |
|                         | type                               |              |          | 31  |
|                         | username                           |              |          | 32  |
3
AOS-CX10.12MonitoringGuide| (6200SwitchSeries)

| vrf                                    |           |            | 33  |
| -------------------------------------- | --------- | ---------- | --- |
| IP-SLA                                 |           |            | 35  |
| IP-SLAguidelines                       |           |            | 35  |
| LimitationswithVoIPSLAs                |           |            | 36  |
| IP-SLAcommands                         |           |            | 36  |
| https                                  |           |            | 36  |
| ip-slaresponder                        |           |            | 38  |
| showip-slaresponder                    |           |            | 38  |
| showip-slaresponderresults             |           |            | 39  |
| showip-sla{<SLA-NAME>[results]|all}    |           |            | 40  |
| L1-100Mbps                             | downshift |            | 45  |
| Limitationswithspeeddownshift          |           |            | 45  |
| L1-100Mbpsdownshiftcommands            |           |            | 45  |
| downshiftenable                        |           |            | 45  |
| showinterface                          |           |            | 46  |
| showinterfacedownshift-enable          |           |            | 50  |
| showrunning-configinterface            |           |            | 51  |
| Mirroring                              |           |            | 54  |
| Mirrorstatistics                       |           |            | 54  |
| Classifierpoliciesandmirroringsessions |           |            | 54  |
| VLANasasource                          |           |            | 55  |
| Mirroringcommands                      |           |            | 55  |
| clearmirror                            |           |            | 55  |
| clearmirrorendpoint                    |           |            | 56  |
| comment                                |           |            | 57  |
| copytcpdump-pcap                       |           |            | 58  |
| copytshark-pcap                        |           |            | 59  |
| destinationcpu                         |           |            | 60  |
| destinationinterface                   |           |            | 60  |
| destinationtunnel                      |           |            | 61  |
| diagnostic                             |           |            | 63  |
| diagutilitiestcpdump                   |           |            | 64  |
| disable                                |           |            | 66  |
| enable                                 |           |            | 67  |
| mirrorsession                          |           |            | 68  |
| mirrorendpoint                         |           |            | 68  |
| showmirror                             |           |            | 69  |
| showmirrorendpoint                     |           |            | 71  |
| shutdown                               |           |            | 72  |
| source                                 |           |            | 73  |
| sourceinterface                        |           |            | 73  |
| sourcevlan                             |           |            | 75  |
| Monitoring                             | a device  | using SNMP | 78  |
| Power-over-Ethernet                    |           |            | 79  |
| PoEcommands                            |           |            | 80  |
| lldpdot3poe                            |           |            | 80  |
| lldpmedpoe                             |           |            | 81  |
| power-over-ethernet                    |           |            | 81  |
| power-over-ethernetallocate-by         |           |            | 82  |
| power-over-ethernetalways-on           |           |            | 83  |
| power-over-ethernetassigned-class      |           |            | 84  |
Contents|4

|                                                  | power-over-ethernetpre-std-detect |           | 85  |
| ------------------------------------------------ | --------------------------------- | --------- | --- |
|                                                  | power-over-ethernetpriority       |           | 86  |
|                                                  | power-over-ethernetquick-poe      |           | 87  |
|                                                  | power-over-ethernetthreshold      |           | 88  |
|                                                  | power-over-ethernettrap           |           | 88  |
|                                                  | showlldplocal                     |           | 89  |
|                                                  | showlldpneighbor                  |           | 90  |
|                                                  | showpower-over-ethernet           |           | 91  |
| Aruba                                            | AirWave                           |           | 95  |
| SNMPsupportandAirWave                            |                                   |           | 95  |
|                                                  | SNMPontheswitch                   |           | 95  |
| SupportedfeatureswithAirWaveandtheAOS-CXswitch   |                                   |           | 96  |
| ConfiguringtheAOS-CXswitchtobemonitoredbyAirWave |                                   |           | 96  |
| AirWavecommands                                  |                                   |           | 97  |
|                                                  | logging                           |           | 97  |
|                                                  | snmp-servercommunity              |           | 99  |
|                                                  | snmp-serverhost                   |           | 100 |
|                                                  | snmp-servervrf                    |           | 102 |
|                                                  | snmpv3context                     |           | 102 |
|                                                  | snmpv3user                        |           | 103 |
| Support                                          | and Other                         | Resources | 106 |
| AccessingArubaSupport                            |                                   |           | 106 |
| AccessingUpdates                                 |                                   |           | 107 |
|                                                  | ArubaSupportPortal                |           | 107 |
|                                                  | MyNetworking                      |           | 107 |
| WarrantyInformation                              |                                   |           | 107 |
| RegulatoryInformation                            |                                   |           | 107 |
| DocumentationFeedback                            |                                   |           | 108 |
5
AOS-CX10.12MonitoringGuide| (6200SwitchSeries)

Chapter 1
About this document
| About | this document |     |     |
| ----- | ------------- | --- | --- |
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedfor
administratorsresponsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
| Applicable | products |     |     |
| ---------- | -------- | --- | --- |
Thisdocumentappliestothefollowingproducts:
n Aruba6200SwitchSeries(JL724A,JL725A,JL726A,JL727A,JL728A,R8Q67A,R8Q68A,R8Q69A,R8Q70A,
R8Q71A,R8V08A,R8V09A,R8V10A,R8V11A,R8V12A,R8Q72A)
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
<example-text> substitutewithanactualvalueinacommandorincode:
n
n <example-text>
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
| Verticalbar.AlogicalORthatseparatesmultipleitemsfromwhichyoucan
chooseonlyone.
Anyspacesthatareoneithersideoftheverticalbarareincludedfor
readabilityandarenotarequiredpartofthecommandsyntax.
{ } Braces.Indicatesthatatleastoneoftheencloseditemsisrequired.
6
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

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
| On the 6200 Switch | Series |     |     |
| ------------------ | ------ | --- | --- |
Aboutthisdocument|7

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

8

Monitoring hardware through visual
observation

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

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

9

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
Monitoringhardwarethroughvisualobservation|10

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

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

11

Chapter 3

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

Supported Platform
The following table list the scales and supported platforms for IPFIX.

Table 1: Scale and supported platforms for IPFIX

Platform

IPFIX

Maximum
Flows

Maximum
pps

Maximum
TCAM

TCAM is shared between multiple features and is allocated based on first-in, first-out principle. This
could result in a scale impact if the environment already has other features using TCAM and the usage is
going beyond the available or allocated TCAM limit.

n In case of TCAM overflow, an error or warning message is displayed under the event logs.

Flow monitors
A flow monitor is applied to an interface to perform network traffic monitoring. A flow monitor consists
of a flow record, a flow cache, and optional flow exporters. A flow record must be created and assigned
to the flow monitor for the monitoring process to function. Flow data is compiled from the network
traffic on the interface and stored in the flow cache based on the match (key) and collect (non-key) fields
in the flow record. Data from the flow cache is exported by the flow exporters assigned to the flow
monitor. A maximum of sixteen flow monitors can be created. There is a limit of two flow exporters that
can be applied to a single flow monitor.

Flow exporters

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

12

A flow exporter defines where and how to export flow reports. Flow exporters are created as
standalone entities in the `config` context to provide flow monitors the ability to export flow reports. A
single flow exporter can be assigned to one or more flow monitors, and multiple flow exporters can be
assigned to a single flow monitor.

Destinations
The destination specifies where flow reports are sent. There are two possible types of destination for a
flow exporter:

1.

(default) Hostname or IP address of a device with an optional VRF

2. Traffic Insight instance

A flow exporter can only send flow reports to one destination. The destination type specifies which
destination to use. If no destination type is specified, the default destination type is the first one (a
hostname or IP address of a device with an optional VRF). If a VRF is not specified, the default VRF will be
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

IP Flow Information Export | 13

| Configuring |     | IP Flow |     | Information |     | Export |     |     |
| ----------- | --- | ------- | --- | ----------- | --- | ------ | --- | --- |
ThefollowinglistdescribesthestepsrequiredtoconfigureaIP flowinformationexport(IPFIX)solution:
n Stepone:Createflowrecords
n Steptwo:Configureflowexporter(s)
n Stepthree:Configuremonitor(s)
n Stepfour:Applyaflowmonitorstointerface(s)
| Step one: | Create |     | Flow | Records |     |     |     |     |
| --------- | ------ | --- | ---- | ------- | --- | --- | --- | --- |
FlowRecordsareusedtodefinethedatathatwillbeaddedtotheIPFIXtemplate.Configureonerecord
forIPv4andoneforIPv6.
| switch(config)#             |     | flow                                        | record | flowRecordv4    |             |             |      |       |
| --------------------------- | --- | ------------------------------------------- | ------ | --------------- | ----------- | ----------- | ---- | ----- |
| switch(config-flow-record)# |     |                                             |        | match ipv4      | protocol    |             |      |       |
| switch(config-flow-record)# |     |                                             |        | match ipv4      | source      | add         |      |       |
| switch(config-flow-record)# |     |                                             |        | match ipv4      | destination |             | add  |       |
| switch(config-flow-record)# |     |                                             |        | match ipv4      | version     |             |      |       |
| switch(config-flow-record)# |     |                                             |        | match transport |             | destination |      | port  |
| switch(config-flow-record)# |     |                                             |        | match transport |             | source      | port |       |
| switch(config-flow-record)# |     |                                             |        | collect         | counter     | bytes       |      |       |
| switch(config-flow-record)# |     |                                             |        | collect         | counter     | packets     |      |       |
| switch(config-flow-record)# |     |                                             |        | collect         | application |             | name |       |
| switch(config-flow-record)# |     |                                             |        | collect         | timestamp   | absolute    |      | first |
| switch(config-flow-record)# |     |                                             |        | collect         | timestamp   | absolute    |      | last  |
| switch(config)#             |     | flow                                        | record | flowRecordv6    |             |             |      |       |
| switch(config-flow-record)# |     |                                             |        | match ipv6      | protocol    |             |      |       |
| switch(config-flow-record)# |     |                                             |        | match ipv6      | source      | add         |      |       |
| switch(config-flow-record)# |     |                                             |        | match ipv6      | destination |             | add  |       |
| switch(config-flow-record)# |     |                                             |        | match ipv6      | version     |             |      |       |
| switch(config-flow-record)# |     |                                             |        | match transport |             | destination |      | port  |
| switch(config-flow-record)# |     |                                             |        | match transport |             | source      | port |       |
| switch(config-flow-record)# |     |                                             |        | collect         | counter     | bytes       |      |       |
| switch(config-flow-record)# |     |                                             |        | collect         | counter     | packets     |      |       |
| switch(config-flow-record)# |     |                                             |        | collect         | application |             | name |       |
| switch(config-flow-record)# |     |                                             |        | collect         | timestamp   | absolute    |      | first |
| switch(config-flow-record)# |     |                                             |        | collect         | timestamp   | absolute    |      | last  |
| Next,usetheshow             |     | flow recordcommandtoverifytheconfiguration. |        |                 |             |             |      |       |
| switch(config)#             |     | show                                        | flow   | record          |             |             |      |       |
--------------------------------------------------------------------------------
| Flow record |     | 'flowRecordv4' |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Match            | Fields      |         |       |     |     |     |     |     |
| ---------------- | ----------- | ------- | ----- | --- | --- | --- | --- | --- |
| ipv4 destination |             | address |       |     |     |     |     |     |
| ipv4 protocol    |             |         |       |     |     |     |     |     |
| ipv4 source      |             | address |       |     |     |     |     |     |
| ipv4 version     |             |         |       |     |     |     |     |     |
| transport        | destination |         | port  |     |     |     |     |     |
| transport        | source      | port    |       |     |     |     |     |     |
| Collect          | Fields      |         |       |     |     |     |     |     |
| application      |             | name    |       |     |     |     |     |     |
| counter          | bytes       |         |       |     |     |     |     |     |
| counter          | packets     |         |       |     |     |     |     |     |
| timestamp        | absolute    |         | first |     |     |     |     |     |
14
| AOS-CX10.12MonitoringGuide| |     | (6200SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |

| timestamp | absolute |     | last |     |     |     |     |
| --------- | -------- | --- | ---- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Flow record | 'flowRecordv6' |     |     |     |     |     |     |
| ----------- | -------------- | --- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Match            | Fields      |         |       |             |     |     |     |
| ---------------- | ----------- | ------- | ----- | ----------- | --- | --- | --- |
| ipv6 destination |             | address |       |             |     |     |     |
| ipv6 protocol    |             |         |       |             |     |     |     |
| ipv6 source      | address     |         |       |             |     |     |     |
| ipv6 version     |             |         |       |             |     |     |     |
| transport        | destination |         | port  |             |     |     |     |
| transport        | source      | port    |       |             |     |     |     |
| Collect          | Fields      |         |       |             |     |     |     |
| application      | name        |         |       |             |     |     |     |
| counter          | bytes       |         |       |             |     |     |     |
| counter          | packets     |         |       |             |     |     |     |
| timestamp        | absolute    |         | first |             |     |     |     |
| timestamp        | absolute    |         | last  |             |     |     |     |
| Step two:        | Configure   |         | flow  | exporter(s) |     |     |     |
Ithisstep,youcandefineanexportertosendtoanexternaldestinationbyhostnameorIPaddress,or
toaninternaldestinationsuchasTrafficInsight..TheexamplebelowconfiguresIPFIXtoexportdatato
anexternaladdress/hostname:
| switch(config)# |     | flow | exporter | flowExternal |     |     |     |
| --------------- | --- | ---- | -------- | ------------ | --- | --- | --- |
switch(config-flow-exporter)# destination type hostname-or-ip-addr
| switch(config-flow-exporter)# |     |     |     | destination | 11.1.1.1 |     |     |
| ----------------------------- | --- | --- | --- | ----------- | -------- | --- | --- |
| switch(config-flow-exporter)# |     |     |     | show flow   | exporter |     |     |
--------------------------------------------------------------------------------
| Flow exporter |     | 'flowExternal |     |     |     |     |     |
| ------------- | --- | ------------- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------------
| Status      |               |     | : Accepted |     |            |     |     |
| ----------- | ------------- | --- | ---------- | --- | ---------- | --- | --- |
| Export      | Protocol      |     | : ipfix    |     |            |     |     |
| Destination | Type          |     | : Hostname | or  | IP address |     |     |
| Destination |               |     | : 11.1.1.1 |     |            |     |     |
| Transport   | Configuration |     |            |     |            |     |     |
| Protocol    |               |     | : udp      |     |            |     |     |
| Port        |               |     | : 4739     |     |            |     |     |
ToconfigureIPFIXtoexporttoTrafficInsight,firstconfigureTrafficInsight.
| switch(config)#       |     | traffic-insight |         | TI        |                   |     |     |
| --------------------- | --- | --------------- | ------- | --------- | ----------------- | --- | --- |
| switch(config-ti-TI)# |     |                 | source  | ipfix     |                   |     |     |
| switch(config-ti-TI)# |     |                 | monitor | topN type | topN-flows        |     |     |
| switch(config-ti-TI)# |     |                 | monitor | dns type  | application-flows |     |     |
| switch(config-ti-TI)# |     |                 | enable  |           |                   |     |     |
Next,configuretheflowexporterforTrafficInsight
| switch(config)#               |     | flow | exporter | flowExpTI       |                 |                 |     |
| ----------------------------- | --- | ---- | -------- | --------------- | --------------- | --------------- | --- |
| switch(config-flow-exporter)# |     |      |          | export-protocol |                 | ipfix           |     |
| switch(config-flow-exporter)# |     |      |          | destination     | type            | traffic-insight |     |
| switch(config-flow-exporter)# |     |      |          | destination     | traffic-insight |                 | TI  |
Youcanusetheshow flow exportercommandtoverifytheflowexporterconfigurationforTraffic
Insight
IPFlowInformationExport |15

| switch(config)# | show | flow exporter | flowExpTI |
| --------------- | ---- | ------------- | --------- |
--------------------------------------------------------------------------------
| Flow exporter | 'flowExpTI' |     |     |
| ------------- | ----------- | --- | --- |
--------------------------------------------------------------------------------
| Status          |               | : Accepted |         |
| --------------- | ------------- | ---------- | ------- |
| Export Protocol |               | : ipfix    |         |
| Destination     | Type          | : Traffic  | Insight |
| Destination     |               | : TI       |         |
| Transport       | Configuration |            |         |
| Protocol        | :             | udp        |         |
| Port            | :             | 4739       |         |
Finally,usetheshow run traffic-insightcommandtoverifytheTrafficInsightconfiguration:
| switch(config)# | show | run traffic-insight |     |
| --------------- | ---- | ------------------- | --- |
| traffic-insight | TI   |                     |     |
enable
| source ipfix |     |     |     |
| ------------ | --- | --- | --- |
!
| monitor     | topN type topN-flows | entries           | 5   |
| ----------- | -------------------- | ----------------- | --- |
| monitor     | appFlow type         | application-flows |     |
| Step three: | Configure            | a monitor(s)      |     |
First,configureanIPv4flowmonitor.
| switch(config)#               | flow | monitor flowMonv4 |              |
| ----------------------------- | ---- | ----------------- | ------------ |
| switch(config-flow-monitor)#  |      | record            | flowRecordv4 |
| Switch (config-flow-monitor)# |      | exporter          | flowExternal |
| switch(config-flow-monitor)#  |      | exit              |              |
Next,configureanIPv6flowmonitor.
| switch(config)#              | flow | monitor flowMonv6 |              |
| ---------------------------- | ---- | ----------------- | ------------ |
| switch(config-flow-monitor)# |      | record            | flowRecordv6 |
| switch(config-flow-monitor)# |      | exporter          | flowExternal |
| switch(config-flow-monitor)# |      | exit              |              |
Oncebothflowmonitorsarecreated,usetheshow flow monitorcommandtoverifytheflowmonitor
configurations.
| switch(config-flow-monitor)# |     | show | flow monitor |
| ---------------------------- | --- | ---- | ------------ |
--------------------------------------------------------------------------------
| Flow monitor | 'flowMonv4' |     |     |
| ------------ | ----------- | --- | --- |
--------------------------------------------------------------------------------
| Status              |         | : Accepted     |     |
| ------------------- | ------- | -------------- | --- |
| Flow Record         |         | : flowRecordv4 |     |
| Flow Exporter(s)    |         | : flowExternal |     |
| Cache Configuration |         |                |     |
| Inactive            | Timeout | : 30           |     |
| Active Timeout      |         | : 1800         |     |
--------------------------------------------------------------------------------
| Flow monitor | 'flowMonv6' |     |     |
| ------------ | ----------- | --- | --- |
16
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

--------------------------------------------------------------------------------
| Status           |     |     | : Accepted     |     |     |
| ---------------- | --- | --- | -------------- | --- | --- |
| Flow Record      |     |     | : flowRecordv6 |     |     |
| Flow Exporter(s) |     |     | : flowExternal |     |     |
Cache Configuration
| Inactive | Timeout | :   | 30   |     |     |
| -------- | ------- | --- | ---- | --- | --- |
| Active   | Timeout | :   | 1800 |     |     |
Step four: (Optional) Enable Application Recognition and apply a
| flow monitor | to  | interfaces |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- |
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
| FAQs and | Troubleshooting |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
n WhenIPFIXisusedwithApplicationRecognition,thesefeaturesdonotsupportLAGsorMCLAGs(VSX
LAGs).
n Thefollowingmessagesaredisplayedtoindicateanillegalargument:
o %Theflowexporter<EXPORTER-NAME>doesnotexist.
o %Theflowrecord<RECORD-NAME>doesnotexist.
IPFlowInformationExport |17

o % The flow monitor <MONITOR-NAME> does not exist.

o Invalid destination IP address or hostname entered.

o Unable to create the flow exporter. The maximum allowed number of flow exporters (16) has

been reached.

o Unable to create the flow record. The maximum allowed number of flow records (16) has been

reached.

o Unable to create the flow monitor. The maximum allowed number of flow monitors (16) has been

reached.

o Flow monitor cannot be applied while interface is part of LAG <LAG-NAME>.

o Flow monitor could not be applied.

o Flow monitor could not be unapplied

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

18

Chapter 4

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

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

19

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

Rebooting the system from the secondary operating system image, setting the secondary operating
system image as the configured default boot image:

Boot commands | 20

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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show boot-history
| show boot-history | [all] |     |     |     |
| ----------------- | ----- | --- | --- | --- |
Description
Showsbootinformation.Whennoparametersarespecified,showsthemostrecentinformationabout
thebootoperation,andthethreepreviousbootoperationsfortheactivemanagementmodule.When
theallparameterisspecified,showsthebootinformationfortheactivemanagementmoduleandall
availablelinemodules.Toviewboot-historyonthestandby,thecommandmustbesentonthestandby
console.
| Parameter |     |     | Description                                         |     |
| --------- | --- | --- | --------------------------------------------------- | --- |
| all       |     |     | Showsbootinformationfortheactivemanagementmoduleand |     |
allavailablelinemodules.
Usage
21
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

Thiscommanddisplaystheboot-index,boot-ID,anduptimeinsecondsforthecurrentboot.Ifthereis
apreviousboot,itdisplaysboot-index,boot-ID,reboottime(basedonthetimezoneconfiguredinthe
system)andrebootreasons.Previousbootinformationisdisplayedinreversechronologicalorder.
Index
Thepositionofthebootinthehistoryfile.Range:0to3.
Boot ID
AuniqueIDfortheboot.Asystem-generated128-bitstring.
| Current Boot, | up for | <SECONDS> seconds |     |
| ------------- | ------ | ----------------- | --- |
Forthecurrentboot,theshow boot-historycommandshowsthenumberofsecondsthemodulehasbeen
runningonthecurrentsoftware.
| Timestamp | boot reason |     |     |
| --------- | ----------- | --- | --- |
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
| switch#    | show boot-history | all |     |
| ---------- | ----------------- | --- | --- |
| Management | module            |     |     |
=================
| Index : | 3                                  |                |         |
| ------- | ---------------------------------- | -------------- | ------- |
| Boot ID | : f1bf071bdd04492bbf8439c6e479d612 |                |         |
| Current | Boot, up for                       | 22 hrs 12 mins | 22 secs |
| Index : | 2                                  |                |         |
Bootcommands|22

| Boot ID     | : edfa2d6598d24e989668306c4a56a06d |                    |                  |
| ----------- | ---------------------------------- | ------------------ | ---------------- |
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
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
23
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

Chapter 5
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
Switchsystemandhardwarecommandsaregeneralcommandsusedtoconfigurefundamentalsettings
ontheswitch.
RefertotheFundamentalsGuidetoviewtheswitchsystemandhardwarecommands.
24
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

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
25
| AOS-CX10.12MonitoringGuide| |     | (6200SwitchSeries) |     |     |
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
| 6200 |     |     |     | Administratorsorlocalusergroup |
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
Externalstorage|26

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
27
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |
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
switch(config)#
|     | no  | external-storage | logfiles |     |
| --- | --- | ---------------- | -------- | --- |
Externalstorage|28

| Command        | History     |     |         |              |     |     |     |
| -------------- | ----------- | --- | ------- | ------------ | --- | --- | --- |
| Release        |             |     |         | Modification |     |     |     |
| 10.07orearlier |             |     |         | --           |     |     |     |
| Command        | Information |     |         |              |     |     |     |
| Platforms      | Command     |     | context | Authority    |     |     |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
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
29
| AOS-CX10.12MonitoringGuide| |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

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
6200 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
|     | (#) |     | forthiscommand. |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- |
Externalstorage|30

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
6200 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
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
31
| AOS-CX10.12MonitoringGuide| |     |     | (6200SwitchSeries) |     |     |
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
6200 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
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
Externalstorage|32

| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
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
6200 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
33
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

Platforms

Command context

Authority

members with execution rights for this
command.

External storage | 34

Chapter 7

IP-SLA

IP-SLA

The IP Service Level Agreement (IP-SLA) is a feature that enables the measuring of network performance
between two nodes in a network for different service level agreement parameters such as round-trip
time (RTT), one-way delay, jitter, reachability, packet loss, and voice quality scores. These two nodes can
span across area in access, distribution or core inside a LAN as well as across WAN between core to core
or core to Data Centre switches. This feature helps you measure the SLA for different protocols or
applications such as UDP echo, UDP jitter (for voice and video), TCP connect, HTTP, HTTPS, and ICMP
echo. This guide provides details for managing and monitoring different types of IP-SLAs.

IP-SLA sessions configured via CLI are always persistent. The support for ephemeral sessions, which are non-

persistent, is provided only through REST for use with Aruba Central. Hence, the non-persistent sessions
configured through REST will not be displayed in the output of the show running-config command. The non-
persistent IP-SLA source and responder session can be modified or deleted only through REST.

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

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

35

default-class priority 6 rate 99999 burst 9999

n Deviations with respect to PVOS results: The packet losses due to internal switch-related issues like
interface shutdown or interface flaps will not be considered as 'Probes Timed-out error', as the IP-
SLA solution is to measure network performance and anomalies. Rather, this kind of packet loss will
be counted in internal counters like 'Destination address unreachable'.

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

IP-SLA | 36

| Parameter   |     |     | Description                               |     |     |
| ----------- | --- | --- | ----------------------------------------- | --- | --- |
| {get | raw} |     |     | SelectsHTTPSrequesttypeasgetorrawwherethe |     |     |
systemwillgenerateorprovideHTTPSpayload.
| URL |     |     | SpecifiesHTTPSURLaddressofsyntax.https://<HOST |     |     |
| --- | --- | --- | ---------------------------------------------- | --- | --- |
NAME/IP-ADDRESS>:<PORT>/<PATH>.
| source {<SOURCE-IPV4-ADDR> |     | | <IFNAME>} |     |     |     |
| -------------------------- | --- | ----------- | --- | --- | --- |
SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
source-port <PORT-NUM> SpecifiesthevalueofthesourceportfortheIP-SLA
probes.
cache disable SelectscacheoptionfortheHTTPSserver.Bydefaultthe
optionisenabled.
name-server <IPV4-ADDR-DNS-SERVER> SpecifiestheIPv4addressofDNSserver.
probe-interval <PROBE-INTERVAL> Specifiestheprobeintervalinseconds.Range:30to
604800.
version <VERSION-NUMBER>
SpecifiesthesourceinterfacetouseforsendingIP-SLA
probes.
| https-raw-request | <RAW-PAYLOAD> |     | HTTPSrawrequest.String. |     |     |
| ----------------- | ------------- | --- | ----------------------- | --- | --- |
Examples
switch(config-ipsla-1)# https get https://device.arubanetworks.com/root/home.html
| switch(config-ipsla-1)# |     | https get | https://2.2.2.2 | source 1/1/1 |     |
| ----------------------- | --- | --------- | --------------- | ------------ | --- |
switch(config-ipsla-1)#
|     |     | https get | https://device.arubanetworks.com |     | source 2.2.2.1 |
| --- | --- | --------- | -------------------------------- | --- | -------------- |
switch(config-ipsla-1)# https get https://device.arubanetworks.com/root/home.html
| source-interface | 1/1/1 |     |     |     |     |
| ---------------- | ----- | --- | --- | --- | --- |
switch(config-ipsla-1)# https get https://device.arubanetworks.com name-server
10.10.10.2
switch(config-ipsla-1)# https raw https://device.arubanetworks.com/root/home.html
| raw-request | “GET /en/US/hmpgs/index.html” |     |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- | --- |
switch(config-ipsla-1)# no https get https://2.2.2.2 source 1/1/1
| switch(config-ipsla-1)# |     | no https | raw |     |     |
| ----------------------- | --- | -------- | --- | --- | --- |
https://device.arubanetworks.com/root/home.html raw-request “GET
/en/US/hmpgs/index.html”
| Command History     |         |         |                    |           |     |
| ------------------- | ------- | ------- | ------------------ | --------- | --- |
| Release             |         |         | Modification       |           |     |
| 10.12.1000          |         |         | Commandintroduced. |           |     |
| Command Information |         |         |                    |           |     |
| Platforms           | Command | context |                    | Authority |     |
6200 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
37
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

ip-sla responder
ip-sla responder <SLA-NAME> {udp-echo | tcp-connect | udp-jitter-voip} <PORT-NUM>
| [source | {<SOURCE-IPV4-ADDR> | |   | <IFNAME>}][vrf | <VRF-NAME>] |
| ------- | ------------------- | --- | -------------- | ----------- |
no ip-sla responder <SLA-NAME> {udp-echo | tcp-connect | udp-jitter-voip} <PORT-NUM>
| [source | {<SOURCE-IPV4-ADDR> | |   | <IFNAME>}][vrf | <VRF-NAME>] |
| ------- | ------------------- | --- | -------------- | ----------- |
Description
SelectstheIP-SLAresponder.Therespondercanbeconfiguredforudp-echo,tcp-connect,udp-jitter-
voiptype.ItrequirestheSLAname,SLAtype,andportnumberasarguments.SourceIP/interfaceIDisa
mustfortypeudp-jitter-voipandoptionalforothertypes.
ThenoformofthiscommandremovestheIP-SLAresponder.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<SLA-NAME>
SpecifiestheSLAname.Length:1to64characters.
| udp-echo |     |     | Enablesresponderforudp-echoprobes. |     |
| -------- | --- | --- | ---------------------------------- | --- |
tcp-connect
SelectsTCPconnectastheIP-SLAtestmechanism.
| vrf <VRF-NAME> |     |     | SpecifiesthenameoftheVRFtouse. |     |
| -------------- | --- | --- | ------------------------------ | --- |
udp-jitter-voip
SelectsVOIPjitterastheIP-SLAtestmechanism.
| <PORT-NUM> |     |     | SpecifiestheportnumbertolistenforIP-SLAprobes. |     |
| ---------- | --- | --- | ---------------------------------------------- | --- |
Range:1to65535.
| [source {<SOURCE-IPV4-ADDR> |     | | <IFNAME>}] |     |     |
| --------------------------- | --- | ------------ | --- | --- |
SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
Examples
switch(config)# ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
switch(config)# ip-sla responder SLA1 udp-echo 8000 source 1/1/1
switch(config)# no ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
config
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip-sla | responder |     |     |     |
| ----------- | --------- | --- | --- | --- |
IP-SLA|38

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

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

6200

config

Administrators or local user group members with execution rights
for this command.

show ip-sla responder results
show ip-sla responder <SLA-NAME> <SOURCE-IPV4-ADDR> <PORT-NUM> results

Description

Shows the given ip-sla responder statistics for a given source IP and port. This command is only
applicable for the sources where source IP and port are configured.

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

39

| Parameter          |     |     |     |     | Description                            |     |
| ------------------ | --- | --- | --- | --- | -------------------------------------- | --- |
| <SLA-NAME>         |     |     |     |     | SpecifiestheSLAname.                   |     |
| <SOURCE-IPV4-ADDR> |     |     |     |     | SpecifiesthesourceIPV4address.         |     |
| <PORT-NUM>         |     |     |     |     | Specifiestheportnumber.Range:1to65535. |     |
Examples
| switch#        |             | show ip-sla | responder |          | SLA1 2.2.2.1 | 8000 results |
| -------------- | ----------- | ----------- | --------- | -------- | ------------ | ------------ |
|                | IP-SLA      | Type        | :         | Udp-echo |              |              |
|                | VRF         | Name        | :         | Default  |              |              |
|                | Source      | IP          | :         | 2.2.2.1  |              |              |
|                | Source      | Port        | :         | 8000     |              |              |
|                | Responder   | Port        | :         | 8888     |              |              |
|                | Responder   | IP          | :         | 2.2.2.3  |              |              |
|                | Responder   | Interface   | :         |          |              |              |
|                | Responder   | Status      | :         | Running  |              |              |
|                | Packets     | Received    | :         | 2        |              |              |
|                | Packets     | Sent        | :         | 2        |              |              |
| Command        | History     |             |           |          |              |              |
| Release        |             |             |           |          | Modification |              |
| 10.07orearlier |             |             |           |          | --           |              |
| Command        | Information |             |           |          |              |              |
| Platforms      |             | Command     | context   |          | Authority    |              |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | ip-sla | {<SLA-NAME> |           | [results] |        | | all} |
| ---- | ------ | ----------- | --------- | --------- | ------ | ------ |
| show | ip-sla | {<SLA-NAME> | [results] |           | | all} |        |
Description
ShowsthegivenIP-SLAsourceconfigurationandstatus.
| Parameter  |     |     |     |     | Description                                  |     |
| ---------- | --- | --- | --- | --- | -------------------------------------------- | --- |
| <SLA-NAME> |     |     |     |     | SpecifiestheSLAname.                         |     |
| results    |     |     |     |     | ShowsthestatisticscalculatedforanSLAtype.    |     |
| all        |     |     |     |     | Showsallip-slasourceconfigurationsandstatus. |     |
Examples
IP-SLA|40

| switch#         | show         | ip-sla            | xyz            | results  |               |                   |             |
| --------------- | ------------ | ----------------- | -------------- | -------- | ------------- | ----------------- | ----------- |
|                 | IP-SLA       | session           | status         |          |               |                   |             |
|                 | IP-SLA       | Name              |                |          |               | : xyz             |             |
|                 | IP-SLA       | Type              |                |          |               | : tcp-connect     |             |
|                 | Destination  |                   | Host           | Name/IP  | Address:      | 2.2.2.1           |             |
|                 | Destination  |                   | Port           |          |               | : 8888            |             |
|                 | Source       | IP                | Address/IFName |          |               | : 2.2.2.2         |             |
|                 | Source       | Port              |                |          |               | : 5555            |             |
|                 | Status       |                   |                |          |               | : running         |             |
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
|                 | Minimum      | RTT(ms)           |                |          |               | : 12              |             |
|                 | Maximum      | RTT(ms)           |                |          |               | : 12              |             |
|                 | Average      | RTT(ms)           |                |          |               | : 12              |             |
|                 | DNS RTT(ms)  |                   |                |          |               | : 0               |             |
|                 | TCP RTT(ms)  |                   |                |          |               | : 12              |             |
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
|                 | Source       | Port              |                |          |               | : 5555            |             |
|                 | Status       |                   |                |          |               | : running         |             |
|                 | IP-SLA       | Session           | Cumulative     |          | Counters      |                   |             |
|                 | Total        | Probes            | Transmitted    |          |               | : 1               |             |
|                 | Probes       | Timed-out         |                |          |               | : 0               |             |
|                 | Bind         | Error             |                |          |               | : 0               |             |
|                 | Destination  |                   | Address        |          | Unreachable   | : 0               |             |
|                 | DNS          | Resolution        |                | Failures |               | : 0               |             |
|                 | Reception    |                   | Error          |          |               | : 0               |             |
|                 | Transmission |                   | Error          |          |               | : 0               |             |
41
AOS-CX10.12MonitoringGuide| (6200SwitchSeries)

| IP-SLA        | Latest Probe Results |     |            |                     |     |
| ------------- | -------------------- | --- | ---------- | ------------------- | --- |
| Last          | Probe Time           |     | : 2018 Jul | 13 02:02:48         |     |
| Packets       | Sent                 |     | : 1        |                     |     |
| Packets       | Received             |     | : 1        |                     |     |
| Packet        | Loss in Test         |     | : 0.0000%  |                     |     |
| Minimum       | RTT(ms)              |     | : 1        |                     |     |
| Maximum       | RTT(ms)              |     | : 1        |                     |     |
| Average       | RTT(ms)              |     | : 1        |                     |     |
| DNS           | RTT(ms)              |     | : 0        |                     |     |
| Min           | Positive SD          |     | : 1        | Min Positive DS     | : 2 |
| Max           | Positive SD          |     | : 1        | Max Positive DS     | : 2 |
| Positive      | SD Number            |     | : 2        | Positive DS Number  | : 2 |
| Positive      | SD Sum               |     | : 2        | Positive DS Sum     | : 4 |
| Positive      | SD Average           |     | : 5        | Positive DS Average | : 5 |
| Min           | Negative SD          |     | : 1        | Min Negative DS     | : 1 |
| Max           | Negative SD          |     | : 1        | Max Negative DS     | : 1 |
| Negative      | SD Number            |     | : 2        | Negative DS Number  | : 4 |
| Negative      | SD Sum               |     | : 2        | Negative DS Sum     | : 4 |
| Negative      | SD Average           |     | : 5        | Negative DS Average | : 5 |
| Max           | SD Delay             |     | : 0        | Max DS Delay        | : 0 |
| Min           | SD Delay             |     | : 0        | Min DS Delay        | : 0 |
| Average       | SD Delay             |     | : 0        | Average DS Delay    | : 0 |
| Voice Scores: |                      |     |            |                     |     |
| MOS           | Score                |     | : 4.38     | ICPIF               | : 0 |
switch(config)#
|                         | show ip-sla | m3op              |     |     |     |
| ----------------------- | ----------- | ----------------- | --- | --- | --- |
| IP-SLA                  | Name        | : jitter-sla      |     |     |     |
| Status                  |             | : running         |     |     |     |
| IP-SLA                  | Type        | : udp-jitter-voip |     |     |     |
| VRF                     |             | : ipslasrc        |     |     |     |
| Source                  | IP          | : 2.2.2.2         |     |     |     |
| Source                  | Interface   | :                 |     |     |     |
| Domain                  | Name Server | :                 |     |     |     |
| TOS                     |             | : 10              |     |     |     |
| Probe Interval(seconds) |             | : 90              |     |     |     |
| Advantage               | Factor      | : 0               |     |     |     |
| Codec Type              |             | : g711a           |     |     |     |
| switch(config)#         | show ip-sla | https-sla         |     |     |     |
| SLA Name                |             | : https-sla       |     |     |     |
| Status                  |             | : running         |     |     |     |
| SLA Type                |             | : https           |     |     |     |
| VRF                     |             | : default         |     |     |     |
| Source                  | Port        | : 1027            |     |     |     |
| Source                  | IP          | : 1.1.1.1         |     |     |     |
| Source                  | Interface   | :                 |     |     |     |
| Domain                  | Name Server | :                 |     |     |     |
| Probe Interval(seconds) |             | : 60              |     |     |     |
| HTTPS Request           | Type        | : raw             |     |     |     |
| HTTPS URL               |             | : https://1.1.1.2 |     |     |     |
| Cache                   |             | : Enabled         |     |     |     |
| HTTPS Proxy             | URL         | :                 |     |     |     |
| HTTP Version            | Number      | :                 |     |     |     |
switch(config)#
|     | show ip-sla | all |     |     |     |
| --- | ----------- | --- | --- | --- | --- |
IP-SLA|42

| IP-SLA          | session           | status              |          |                    |     |                      |             |     |
| --------------- | ----------------- | ------------------- | -------- | ------------------ | --- | -------------------- | ----------- | --- |
| IP-SLA          | Name              |                     |          |                    | :   | 707 (non-persistent) |             |     |
| IP-SLA          | Type              |                     |          |                    | :   | https                |             |     |
| Destination     |                   | Host Name/IP        | Address  |                    | :   | NA                   |             |     |
| Destination     |                   | Port                |          |                    | :   | NA                   |             |     |
| Source          | IP Address/IFName |                     |          |                    | :   |                      |             |     |
| Source          | Port              |                     |          |                    | :   |                      |             |     |
| Status          |                   |                     |          |                    | :   | running              |             |     |
| IP-SLA          | Session           | Cumulative          | Counters |                    |     |                      |             |     |
| Total Probes    |                   | Transmitted         |          |                    | :   | 1                    |             |     |
| Probes          | Timed-out         |                     |          |                    | :   | 0                    |             |     |
| Bind Error      |                   |                     |          |                    | :   | 0                    |             |     |
| Destination     |                   | Address Unreachable |          |                    | :   | 0                    |             |     |
| DNS Resolution  |                   | Failures            |          |                    | :   | 0                    |             |     |
| Reception       | Error             |                     |          |                    | :   | 0                    |             |     |
| Transmission    |                   | Error               |          |                    | :   | 0                    |             |     |
| IP-SLA          | Latest            | Probe Results       |          |                    |     |                      |             |     |
| Last Probe      | Time              |                     |          |                    | :   | 2023 Jun             | 05 13:10:19 |     |
| Packets         | Sent              |                     |          |                    | :   | 1                    |             |     |
| Packets         | Received          |                     |          |                    | :   | 1                    |             |     |
| Packet          | Loss              | in Test             |          |                    | :   | 0.0000%              |             |     |
| Minimum         | RTT(ms)           |                     |          |                    | :   | 20                   |             |     |
| Maximum         | RTT(ms)           |                     |          |                    | :   | 20                   |             |     |
| Average         | RTT(ms)           |                     |          |                    | :   | 20                   |             |     |
| DNS RTT(ms)     |                   |                     |          |                    | :   | 0                    |             |     |
| TCP RTT(ms)     |                   |                     |          |                    | :   | 12                   |             |     |
| TLS RTT(ms)     |                   |                     |          |                    | :   | 8                    |             |     |
| switch(config)# |                   | show ip-sla         |          | http-sla           |     |                      |             |     |
| IP-SLA          | Name              |                     |          | : http-sla         |     |                      |             |     |
| Status          |                   |                     |          | : running          |     |                      |             |     |
| IP-SLA          | Type              |                     |          | : http             |     |                      |             |     |
| VRF             |                   |                     |          | : ipslasrc         |     |                      |             |     |
| Source          | IP                |                     |          | : 2.2.2.2          |     |                      |             |     |
| Source          | Interface         |                     |          | :                  |     |                      |             |     |
| Domain          | Name              | Server              |          | : 10.10.10.2       |     |                      |             |     |
| Probe           | Interval(seconds) |                     |          | : 90               |     |                      |             |     |
| HTTP            | Request           | Type                |          | : get              |     |                      |             |     |
| HTTP/HTTPS      |                   | URL                 |          | : abcd.com/ws/home |     |                      |             |     |
| Cache           |                   |                     |          | : Enabled          |     |                      |             |     |
| HTTP            | Proxy             | URL                 |          | :                  |     |                      |             |     |
| HTTP            | Version           | Number              |          | : 1.1              |     |                      |             |     |
```
| ##### IP-SLA |     | status description |     |     |     |     |     |     |
| ------------ | --- | ------------------ | --- | --- | --- | --- | --- | --- |
```
| | Status |     |     |     | | Description |     |     |     | |   |
| -------- | --- | --- | --- | ------------- | --- | --- | --- | --- |
|-------------------------|------------------------------------------------|
| | running |     |     |     | | SLA | is  | fully | operational | |   |
| --------- | --- | --- | --- | ----- | --- | ----- | ----------- | --- |
| Bind Error | Another service is using the same source port |
| | Interface |     | Down |     | | Interface |     | status | is not up |     |
| ----------- | --- | ---- | --- | ----------- | --- | ------ | --------- | --- |
| Dns Resolution Error | Failed to resolve destination hostname |
43
AOS-CX10.12MonitoringGuide| (6200SwitchSeries)

|     | | No       | Route |       | |   | No available    | route          | to the | responder   | |   |
| --- | ---------- | ----- | ----- | --- | --------------- | -------------- | ------ | ----------- | --- |
|     | | Internal |       | Error | |   | Unexpected      | error prevents |        | SLA session | |   |
|     | | Disabled |       |       | |   | SLA is disabled |                |        |             | |   |
|Configuration Incomplete | Configuration is not complete to enable the SLA|
```
| ##### | IP  | SLA session | cumulative |     | counters | description |     |     |     |
| ----- | --- | ----------- | ---------- | --- | -------- | ----------- | --- | --- | --- |
```
|     | | Status |     |     |     | | Description |     |     |     |     |
| --- | -------- | --- | --- | --- | ------------- | --- | --- | --- | --- |
|
|--------------------------------|--------------------------------------------
------------------------------|
|Probes Timed-out | Total numbers of probes failed to receive
| response. |        |       |                 | |   |         |         |     |                     |        |
| --------- | ------ | ----- | --------------- | --- | ------- | ------- | --- | ------------------- | ------ |
|           | |Bind  | Error |                 |     | | Total | numbers | of  | probes transmission | failed |
| as        | source | port  | not available.| |     |         |         |     |                     |        |
|Destination Address Unreachable | Total numbers of probes transmission failed
| due | to route | unavailable. |     | |   |     |     |     |     |     |
| --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|DNS Resolution Failures | Total numbers of probes failed due to DNS
| resolution     |               | failure.    |               | |   |                                       |         |     |                   |     |
| -------------- | ------------- | ----------- | ------------- | --- | ------------------------------------- | ------- | --- | ----------------- | --- |
|                | |Reception    |             | Error         |     | | Total                               | numbers | of  | probes failed due | to  |
| internal       |               | error       | in reception. |     | |                                     |         |     |                   |     |
|                | |Transmission |             | Error         |     | | Total                               | numbers | of  | probes failed due | to  |
| internal       |               | errr in     | transmission. |     | |                                     |         |     |                   |     |
| Command        |               | History     |               |     |                                       |         |     |                   |     |
| Release        |               |             |               |     | Modification                          |         |     |                   |     |
| 10.12.1000     |               |             |               |     | UpdatedtodisplayhttpsasanIP-SLA type. |         |     |                   |     |
| 10.07orearlier |               |             |               |     | --                                    |         |     |                   |     |
| Command        |               | Information |               |     |                                       |         |     |                   |     |
| Platforms      |               | Command     | context       |     | Authority                             |         |     |                   |     |
6200 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
(#)
IP-SLA|44

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
45
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |
| --------------------------- | ------------------ | --- |

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
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Showsadditionalstatistics,includingthetxfilteredandrx
filteredcounters.
n Rxfilterpacketsareprotocolpacketsreceivedwhenthe
protocolisdisabledontheswitchandthereisonlyoneportin
theVLAN.ProtocolsincludeOSPF,PIM,RIP,LACP,andLLDP.
n AnexampleofaTxfilteredpacketwouldbeamulticastpacket
beingfilteredfromgoingoutoftheingressport.
L1-100Mbpsdownshift|46

Parameter Description
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
non-zero Showsonlynonzerostatistics.
LAG
ShowsLAGinterfaceinformation.
monitor Continuouslymonitorinterfacestatistics.
LOOPBACK
Showsloopbackinterfaceinformation.
TUNNEL Showstunnelinterfaceinformation.
VLAN
ShowsVLANinterfaceinformation.
<LAG-ID> SpecifiestheLAGnumber.Range:1-256
<LOOPBACK-ID>
SpecifiestheLOOPBACKnumber.Range:0-255
<TUNNEL-ID> SpecifiesthetunnelID.Range:1-255
<VLAN-ID>
SpecifiestheVLANID.Range:1-4094
VXLAN ShowstheVXLANinterfaceinformation.
<VXLAN-ID>
SpecifiestheVXLANinterfaceidentifier.Default:1
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
47
AOS-CX10.12MonitoringGuide| (6200SwitchSeries)

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
L1-100Mbpsdownshift|48

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
Inhuman-readableformat,the< 1symbolforUtilizationindicatesthattheamountofpacketsisbetween
zeroandone.Thisistrueincaseswherethenumberofbytesincreasesbutthenumberofpacketsandthe
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
49
AOS-CX10.12MonitoringGuide| (6200SwitchSeries)

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
| Command | History |     |     |     |                        |     |
| ------- | ------- | --- | --- | --- | ---------------------- | --- |
| Release |         |     |     |     | Modification           |     |
| 10.11   |         |     |     |     | Addedmonitorparameter. |     |
10.10
Addedhuman-readableparameter.
| 10.07orearlier |             |     |         |     | --        |     |
| -------------- | ----------- | --- | ------- | --- | --------- | --- |
| Command        | Information |     |         |     |           |     |
| Platforms      | Command     |     | context |     | Authority |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show interface |                       | downshift-enable |     |     |                  |     |
| -------------- | --------------------- | ---------------- | --- | --- | ---------------- | --- |
| show interface | [<IFNNAME>|<IFRANGE>] |                  |     |     | downshift-enable |     |
L1-100Mbpsdownshift|50

Description
Displaysspeeddownshiftinformation,includingtheinterfacespeedstatusandconfiguration.
| Parameter |     |     |     | Description              |     |
| --------- | --- | --- | --- | ------------------------ | --- |
| <IFNAME>  |     |     |     | Specifiesainterfacename. |     |
<IFRANGE>
Specifiestheportidentifierrange.
Examples
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
switch(config-if)#
|     |     |     | show interface | 1/1/2 | downshift-enable |
| --- | --- | --- | -------------- | ----- | ---------------- |
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
6200 config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show running-config |     |           | interface |                       |     |
| ------------------- | --- | --------- | --------- | --------------------- | --- |
| show running-config |     | interface |           | [<IFNNAME>|<IFRANGE>] |     |
show running-config interface [lag | loopback | tunnel | vlan ] [<ID>]
Description
Displaysactiveconfigurationsofvariousswitchinterfaces.
51
| AOS-CX10.12MonitoringGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

| Parameter     |     | Description                                     |     |     |
| ------------- | --- | ----------------------------------------------- | --- | --- |
| <IFNAME>      |     | Specifiesainterfacename.                        |     |     |
| <IFRANGE>     |     | Specifiestheportidentifierrange.                |     |     |
| LAG           |     | SpecifiesLAGinterfaceinformation                |     |     |
| LOOPBACK      |     | Specifiesloopbackinterfaceinformation.          |     |     |
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
| switch(config-if)# | show       | running-config | interface | loopback |
| ------------------ | ---------- | -------------- | --------- | -------- |
| No loopback        | interfaces | configured.    |           |          |
| Command History    |            |                |           |          |
L1-100Mbpsdownshift|52

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
53
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

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

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

54

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

Mirroring | 55

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
| switch# | clear mirror | endpoint |     |
| ------- | ------------ | -------- | --- |
Clearingmirrorstatisticsformirrorendpointtest:
56
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| switch#             | clear mirror | endpoint test |              |
| ------------------- | ------------ | ------------- | ------------ |
| Command History     |              |               |              |
| Release             |              |               | Modification |
| 10.07orearlier      |              |               | --           |
| Command Information |              |               |              |
| Platforms           | Command      | context       | Authority    |
6200 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
|     | (#) |     | forthiscommand. |
| --- | --- | --- | --------------- |
comment
comment <COMMENT>
no comment
Description
Specifiesacommentforthemirroringsession.
Whenusedinmirrorendpointcommandcontext,specifiesacommentforthemirrorendpoint.
Thenoformofthiscommandremovesthecomment.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<COMMENT>
Acommentstringofupto64characterscomposedofletters,
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
Mirroring|57

switch(config-mirror-endpoint-test)# comment Monitor endpoint traffic
Replacingtheexistingcommentformirrorendpoint:
switch(config-mirror-endpoint-test)# comment Monitor statistics on each endpoint
interfaces
| Command        | History     |         |              |           |     |     |     |
| -------------- | ----------- | ------- | ------------ | --------- | --- | --- | --- |
| Release        |             |         | Modification |           |     |     |     |
| 10.07orearlier |             |         | --           |           |     |     |     |
| Command        | Information |         |              |           |     |     |     |
| Platforms      | Command     | context |              | Authority |     |     |     |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
|     | config-mirror-endpoint |     |     | executionrightsforthiscommand. |     |     |     |
| --- | ---------------------- | --- | --- | ------------------------------ | --- | --- | --- |
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
| root@10.0.0.2's      | passowrd:            |     |                    |     |          |           |       |
| -------------------- | -------------------- | --- | ------------------ | --- | -------- | --------- | ----- |
| Connected            | to 10.0.0.2.         |     |                    |     |          |           |       |
| sftp > put           | my_capture_file.pcap |     | file.pcap          |     |          |           |       |
| Uploading            | my_capture_file.pcap |     | to /root/file.pcap |     |          |           |       |
| my_capture_file.pcap |                      |     |                    |     | 100% 156 | 219.8KB/s | 00:00 |
| Copied               | successfuly.         |     |                    |     |          |           |       |
| Command              | History              |     |                    |     |          |           |       |
58
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- | --- |

| Release   |             |         | Modification      |     |     |     |
| --------- | ----------- | ------- | ----------------- | --- | --- | --- |
| 10.08     |             |         | Commandintroduced |     |     |     |
| Command   | Information |         |                   |     |     |     |
| Platforms | Command     | context | Authority         |     |     |     |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
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
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Mirroring|59

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
60
| AOS-CX10.12MonitoringGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

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
Configuringamirroringsessionandaddinganinterfaceasadestination:
| switch(config)#          |     | mirror | session     | 1   |           |     |       |
| ------------------------ | --- | ------ | ----------- | --- | --------- | --- | ----- |
| switch(config-mirror-1)# |     |        | destination |     | interface |     | 1/1/1 |
Replacingtheexistingdestinationwithdifferentinterface:
switch(config-mirror-1)#
|     |     |     | destination |     | interface |     | 1/1/12 |
| --- | --- | --- | ----------- | --- | --------- | --- | ------ |
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
config-mirror-<SESSION-ID>
| Allplatforms |     |     |     |     |     | Administratorsorlocalusergroupmemberswith |     |
| ------------ | --- | --- | --- | --- | --- | ----------------------------------------- | --- |
executionrightsforthiscommand.
| destination       | tunnel |               |            |        |                    |     |     |
| ----------------- | ------ | ------------- | ---------- | ------ | ------------------ | --- | --- |
| destination       | tunnel | <TUNNEL-IPV4> |            | source | <SOURCE-IPv4-ADDR> |     |     |
| dscp <DSCP-VALUE> |        | vrf           | <VRF-NAME> |        |                    |     |     |
| no destination    | tunnel |               |            |        |                    |     |     |
Description
Mirroring|61

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

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

62

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
| 6200 |     |     | Administratorsorlocalusergroupmemberswith |
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
Mirroring|63

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
64
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |     |
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

Mirroring | 65

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
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
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
66
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |     |
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
Whenadding,removing,orchangingtheconfigurationofasourceinterfaceinanenabledmirroringsession,
packetsfromothermirrorsourcesusingthesamedestinationinterfacemightbeinterrupted.
Example
Configuringandenablingamirroringsession:
| switch(config)# | mirror | session | 3   |     |
| --------------- | ------ | ------- | --- | --- |
switch(config-mirror-3)#
|                          |     | source      | interface | 1/1/2 rx |
| ------------------------ | --- | ----------- | --------- | -------- |
| switch(config-mirror-3)# |     | destination | interface | 1/1/3    |
switch(config-mirror-3)# comment Monitor router port ingress-only traffic
| switch(config-mirror-3)# |     | enable |              |     |
| ------------------------ | --- | ------ | ------------ | --- |
| Command History          |     |        |              |     |
| Release                  |     |        | Modification |     |
| 10.07orearlier           |     |        | --           |     |
Mirroring|67

| Command Information |         |         |     |           |
| ------------------- | ------- | ------- | --- | --------- |
| Platforms           | Command | context |     | Authority |
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
| mirror endpoint    |        |     |     |     |
| ------------------ | ------ | --- | --- | --- |
| mirror endpoint    | <NAME> |     |     |     |
| no mirror endpoint | <NAME> |     |     |     |
Description
68
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

Createsthespecifiedmirrorendpointorentersitscontextifitalreadyexists.Thespecificsofamirror
endpointarecreatedoralteredwhileinthemirrorendpointcontextandthemirrorendpointisenabled
ordisabledfromthiscontext.ItmaybepossibletosupportdifferentencapsulationsbydifferentASICs.
Forexample,UDPforPVOScompatibility.TerminationofGREencapsulationisalsosupported.
Thenoformofthiscommandremovesanexistingmirrorendpoint.Anenabledmirrorendpointis
automaticallydisabledfirstbeforeremoval.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<NAME>
Specifiesmirrorendpointname.
Examples
Creatingamirrorendpointnamedtest:
| switch(config)# | mirror | endpoint | test |
| --------------- | ------ | -------- | ---- |
Deletingmirrorendpointnamedtest
| switch(config)#     | no      | mirror endpoint | test         |
| ------------------- | ------- | --------------- | ------------ |
| Command History     |         |                 |              |
| Release             |         |                 | Modification |
| 10.07orearlier      |         |                 | --           |
| Command Information |         |                 |              |
| Platforms           | Command | context         | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show mirror
| show mirror | [<SESSION-ID>] |     |     |
| ----------- | -------------- | --- | --- |
Description
Showsinformationaboutmirroringsessions.If<SESSION-ID>isnotspecified,thenthecommand
showsasummaryofallconfiguredmirroringsessions.If<SESSION-ID>isspecified,thenthecommand
showsdetailedinformationaboutthespecifiedmirroringsession.
| Parameter    |     |     | Description                              |
| ------------ | --- | --- | ---------------------------------------- |
| <SESSION-ID> |     |     | Specifiesthesessionidentifier.Range:1to4 |
Usage
Mirroring|69

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
70
AOS-CX10.12MonitoringGuide| (6200SwitchSeries)

| Output Bytes: | 0   |     |     |     |
| ------------- | --- | --- | --- | --- |
switch#
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
| show mirror | endpoint          |     |     |     |
| ----------- | ----------------- | --- | --- | --- |
| show mirror | endpoint [<NAME>] |     |     |     |
Description
Showsalistofallconfiguredmirrorendpoints,theirAdminStatusandtheirOperationStatus.
Theoptionalparameterwilldisplaythedetailsofthespecifiedmirrorendpointifitexists.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<NAME> Specifiesnameofthemirrorendpointinstancetobedisplayed.
Examples
Showingasummaryofallconfiguredmirrorendpointsontheswitch:
| switch# | show mirror  | endpoint  |        |     |
| ------- | ------------ | --------- | ------ | --- |
| Name    | Admin Status | Operation | Status |     |
----- -------------- ----------------------------------------------------
| test    | enable  | enabled  |     |     |
| ------- | ------- | -------- | --- | --- |
| monitor | disable | disabled |     |     |
Showingthedetailsofenabledmirrorendpointaudit:
| switch#          | show mirror       | endpoint audit |         |                  |
| ---------------- | ----------------- | -------------- | ------- | ---------------- |
| Mirror Endpoint: | audit             |                |         |                  |
| Admin Status:    | enable            |                |         |                  |
| Operation        | Status:           | enabled        |         |                  |
| Comment:         | Mirror Endpoint   | Audit          |         |                  |
| Type: gre        |                   |                |         |                  |
| Tunnel:          | source 1.1.1.1    | destination    | 1.1.1.2 | id 1 vrf default |
| Interface:       | 1/1/1-1/1/10,lag1 |                |         |                  |
| Output Packets:  | 123456789         |                |         |                  |
| Output Bytes:    | 8912345678        |                |         |                  |
Mirroring|71

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
|     | (#) |     | forthiscommand. |
| --- | --- | --- | --------------- |
shutdown
shutdown
no shutdown
Description
Enablesmirrorendpointfromitsdefaultdisabledstate.Toverifythemirrorendpointwassuccessfully
activated,runtheshow NAMEcommandandverifythattheAdmin Statusand
|     | mirror | endpoint |     |
| --- | ------ | -------- | --- |
Operational Statushaschangedfromdisabledtoenabled.Ifthestatusvalueremainsdisabled,
consultthesystemlogstodeterminethereasonforactivationfailure.Todisablethemirrorendpoint,
firstdisabletheremotemirrorsessionontheswitchthat'soriginatingthedata.Next,usetheshutdown
commandtodisablethemirrorendpoint.
Examples
Enablingamirrorendpoint:
| switch(config)#                      | mirror | endpoint | test        |
| ------------------------------------ | ------ | -------- | ----------- |
| switch(config-mirror-endpoint-test)# |        |          | no shutdown |
Disablingamirrorendpoint:
| switch(config)#                      | mirror  | endpoint | test         |
| ------------------------------------ | ------- | -------- | ------------ |
| switch(config-mirror-endpoint-test)# |         |          | shutdown     |
| Command History                      |         |          |              |
| Release                              |         |          | Modification |
| 10.07orearlier                       |         |          | --           |
| Command Information                  |         |          |              |
| Platforms                            | Command | context  | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
72
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

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
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<SOURCE-IP> SpecifiesL3encapsulatedIPv4sourceintheformA.B.C.D.
<DESTINATION-IP>
SpecifiesL3encapsulatedIPv4destinationintheformA.B.C.D.
| id  |     |     |     |     | Specifiestunnelidentifierfromtheencapsulatedpacket. |     |
| --- | --- | --- | --- | --- | --------------------------------------------------- | --- |
<VRF_NAME>
SpecifiesthenameofVRF forwhichthetunnelbelongsto.
Examples
Configuringatunnelparametertoamirrorendpoint:
switch(config-mirror-endpoint-test)# source 1.1.1.1 destination 7.7.7.7 id 1 vrf
| default        | type        | gre     |         |     |              |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Command        | History     |         |         |     |              |     |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| source    | interface |             |     |               |             |               |
| --------- | --------- | ----------- | --- | ------------- | ----------- | ------------- |
| source    | interface | {<PORT-NUM> |     | | <LAG-NAME>} |             | [<DIRECTION>] |
| no source | interface | {<PORT-NUM> |     | |             | <LAG-NAME>} | [<DIRECTION>] |
Description
Configuresthespecifiedinterface(eitheranEthernetportoraLAG)asasourceoftraffictobemirrored.
Mirroring|73

Thenoformofthiscommandceasesmirroringtrafficfromthespecifiedsourceinterfaceandremoves
thesourceinterfacefromthemirroringsessionconfiguration.
| Parameter  |     | Description                                    |     |     |
| ---------- | --- | ---------------------------------------------- | --- | --- |
| <PORT-NUM> |     | Specifiesaphysicalportontheswitch.Usetheformat |     |     |
member/slot/port(forexample,1/3/1).
<LAG-NAME> SpecifiestheidentifierfortheLAG(linkaggregationgroup).
<DIRECTION>
Selectsthedirectionoftraffictobemirroredfromthissource
interface.Thereisnodefaultforthisparameter.Validvaluesare
thefollowing:
| both |     | Mirrorbothtransmittedandreceivedpackets. |     |     |
| ---- | --- | ---------------------------------------- | --- | --- |
| rx   |     | Mirroronlyreceivedpackets.               |     |     |
| tx   |     | Mirroronlytransmittedpackets.            |     |     |
Usage
Thereisalimitofsourceinterfacesineachdirectionofagivenmirrorsession:
|     |     | Source | interface limit per mirror | session (4 |
| --- | --- | ------ | -------------------------- | ---------- |
Switch
|      |     | possible | sessions) |     |
| ---- | --- | -------- | --------- | --- |
| 6200 |     | 64       |           |     |
However,thereisapracticallimittotheamountoftrafficthatamirrordestinationcantransmit.For
example,mirroringsessionwithmultiple10Gsourcescanoverwhelmasingle10Gdestination.
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
| switch(config)#          | mirror session | 1                |            |     |
| ------------------------ | -------------- | ---------------- | ---------- | --- |
| switch(config-mirror-1)# |                | source interface | 1/1/1 both |     |
Creatingasecondmirroringsessionandconfiguringtwosourceinterfaces.Oneportmirroringonly
transmittedpacketsandtheothermirroringbothtransmittedandreceivedpackets:
74
AOS-CX10.12MonitoringGuide| (6200SwitchSeries)

| switch(config)# |     |     | mirror | session | 2   |     |
| --------------- | --- | --- | ------ | ------- | --- | --- |
switch(config-mirror-2)#
|                          |     |     |     | source | interface | 1/1/3 tx   |
| ------------------------ | --- | --- | --- | ------ | --------- | ---------- |
| switch(config-mirror-2)# |     |     |     | source | interface | 1/2/1 both |
Removingthefirstsourceinterface:
| switch(config-mirror-2)# |     |     |     | no  | source interface | 1/2/3 |
| ------------------------ | --- | --- | --- | --- | ---------------- | ----- |
Configuringasourceinterfacetomirrorreceivedpacketsonly:
| switch(config-mirror-3)# |     |     |     | source | interface | 1/1/2 rx |
| ------------------------ | --- | --- | --- | ------ | --------- | -------- |
Configuringasourceinterfacetomirrorbothtransmittedandreceivedpackets:
switch(config-mirror-1)#
|     |     |     |     | source | interface | 1/1/1 both |
| --- | --- | --- | --- | ------ | --------- | ---------- |
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
Description
MirroringwithVLANasasourceissupportedinthefollowingtrafficdirections:
Mirroring|75

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

n If the mirror is configured in the rx or tx direction, the packets are mirrored to the mirror

destination.

n If the mirror is configured in the both direction, two copies of the packets are mirrored to the mirror

destination.

The no form command will cease mirroring traffic from the specified source VLAN and remove the
source from the mirror configuration.

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

76

| Parameter |     |     |     | Description           |
| --------- | --- | --- | --- | --------------------- |
| VLAN-NUM  |     |     |     | SelectstheVLANnumber. |
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
| switch#                  | configure | terminal |      |         |
| ------------------------ | --------- | -------- | ---- | ------- |
| switch(config)#          | mirror    | session  | 2    |         |
| switch(config-mirror-2)# |           | source   | vlan | 10 tx   |
| switch(config-mirror-2)# |           | source   | vlan | 20 both |
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
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Mirroring|77

Chapter 10
|            |          |            | Monitoring | a device | using SNMP |
| ---------- | -------- | ---------- | ---------- | -------- | ---------- |
| Monitoring | a device | using SNMP |            |          |            |
Configuring SNMP:RefertotheSNMP/MIBGuideforinformationonhowtoaddSNMPsoadevicecan
bemonitoredfromanetworkmanagementsystem(NMS).
Configuring an SNMP trap receiver:RefertotheSNMP/MIBGuideandspecificinformationaboutthe
trapcommandtoenableSNMPtraps.
show snmp
78
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

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

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

79

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

Power-over-Ethernet | 80

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
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
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
power-over-ethernet
power-over-ethernet
no power-over-ethernet
Description
81
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

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
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
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
Power-over-Ethernet|82

Thepowerallocationmethodcanbechangedonaninterfacethroughport-access(Userrolesor
RADIUS).Anallocationmethodwhenconfiguredthroughport-accesswillreplacetheuserconfigured
method.
Thenoformofthiscommandresetstheactiontodefault.
| Parameter |     |     |     | Description                               |     |     |
| --------- | --- | --- | --- | ----------------------------------------- | --- | --- |
| usage     |     |     |     | Configurestheusage-basedallocationmethod. |     |     |
class
Configurestheclass-basedallocationmethod.
Usage
Ifyouenablepd-class-override foraninterface,theallocate-byconfigurationofthatinterfacewill
beautomaticallychangedtoclass.However,ifyouchangetheallocationmethodtousagewhenpd-
class-overrideisstillenabled,youwillreceiveanerrormessagestatingthat"Thepowerallocation
methodcannotbechangedwhenpd-class-overrideisenabled."
Toremovepd-class-override,youcanusetheno power-over-ethernet pd-class-override
command.Itisimportanttonotethatpd-class-overriderequirestheallocationmethodtobesetto
classandisenforcedwhenconfiguredthroughCLI.However,ifyouoverridetheallocationmethodto
usageviaport-access,pd-class-overridewillnotbeineffect.Therefore,itisrecommendedthatyou
donotoverridetheallocationmethodtousagethroughport-accessoninterfacesconfiguredwithpd-
class-override.
Examples
Configuringthepowerallocationmethod:
| switch(config)#    |     | interface           | 1/1/1 |     |             |       |
| ------------------ | --- | ------------------- | ----- | --- | ----------- | ----- |
| switch(config-if)# |     | power-over-ethernet |       |     | allocate-by | usage |
| switch(config-if)# |     | power-over-ethernet |       |     | allocate-by | class |
Resettingpowerallocationmethod:
| switch(config-if)#  |         | no power-over-ethernet |     |              | allocate-by | class |
| ------------------- | ------- | ---------------------- | --- | ------------ | ----------- | ----- |
| Command History     |         |                        |     |              |             |       |
| Release             |         |                        |     | Modification |             |       |
| 10.07orearlier      |         |                        |     | --           |             |       |
| Command Information |         |                        |     |              |             |       |
| Platforms           | Command | context                |     | Authority    |             |       |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet |     |           | always-on   |     |     |     |
| ------------------- | --- | --------- | ----------- | --- | --- | --- |
| power-over-ethernet |     | always-on | <MODULE-ID> |     |     |     |
83
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- |

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
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Power-over-Ethernet|84

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
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
85
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |

Disablingstandarddevicedetection:
| switch(config-if)#  |         |     | no power-over-ethernet |              | pre-std-detect |
| ------------------- | ------- | --- | ---------------------- | ------------ | -------------- |
| Command History     |         |     |                        |              |                |
| Release             |         |     |                        | Modification |                |
| 10.07orearlier      |         |     |                        | --           |                |
| Command Information |         |     |                        |              |                |
| Platforms           | Command |     | context                | Authority    |                |
config-if
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| switch(config-if)#  |     |     | no power-over-ethernet |              | priority high |
| ------------------- | --- | --- | ---------------------- | ------------ | ------------- |
| Command History     |     |     |                        |              |               |
| Release             |     |     |                        | Modification |               |
| 10.07orearlier      |     |     |                        | --           |               |
| Command Information |     |     |                        |              |               |
Power-over-Ethernet|86

| Platforms | Command |     | context | Authority |     |     |
| --------- | ------- | --- | ------- | --------- | --- | --- |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet |     |           | quick-poe   |     |     |     |
| ------------------- | --- | --------- | ----------- | --- | --- | --- |
| power-over-ethernet |     | quick-poe | <MODULE-ID> |     |     |     |
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
| Parameter   |     |     |     | Description                                    |     |     |
| ----------- | --- | --- | --- | ---------------------------------------------- | --- | --- |
| <MODULE-ID> |     |     |     | SpecifiesmodulenumberforquickPoEconfiguration. |     |     |
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
| Command History     |     |     |     |              |     |     |
| ------------------- | --- | --- | --- | ------------ | --- | --- |
| Release             |     |     |     | Modification |     |     |
| 10.07orearlier      |     |     |     | --           |     |     |
| Command Information |     |     |     |              |     |     |
87
| AOS-CX10.12MonitoringGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

| Platforms | Command |     | context |     | Authority |     |     |
| --------- | ------- | --- | ------- | --- | --------- | --- | --- |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| switch(config-if)#  |         |     | no power-over-ethernet |     |              | threshold | 75  |
| ------------------- | ------- | --- | ---------------------- | --- | ------------ | --------- | --- |
| Command History     |         |     |                        |     |              |           |     |
| Release             |         |     |                        |     | Modification |           |     |
| 10.07orearlier      |         |     |                        |     | --           |           |     |
| Command Information |         |     |                        |     |              |           |     |
| Platforms           | Command |     | context                |     | Authority    |           |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| power-over-ethernet    |     |      | trap |     |     |     |     |
| ---------------------- | --- | ---- | ---- | --- | --- | --- | --- |
| power-over-ethernet    |     | trap |      |     |     |     |     |
| no power-over-ethernet |     |      | trap |     |     |     |     |
Description
Thiscommandenables/disablestheSNMPtrapgenerationforPoErelatedeventsatsystemlevel.PoE
trapgenerationisenabledbydefault.
ThenoformofthiscommandresetstheprioritytodefaultPoEpriority"low".
Power-over-Ethernet|88

Examples
EnablingSNMPtrapgenerationforPoE:
switch(config)#
|     |     |     | power-over-ethernet |     | trap |     |
| --- | --- | --- | ------------------- | --- | ---- | --- |
DisablingSNMPtrapgenerationforPoE:
| switch(config-if)# |             |         | no power-over-ethernet |     |              | trap |
| ------------------ | ----------- | ------- | ---------------------- | --- | ------------ | ---- |
| Command            | History     |         |                        |     |              |      |
| Release            |             |         |                        |     | Modification |      |
| 10.07orearlier     |             |         |                        |     | --           |      |
| Command            | Information |         |                        |     |              |      |
| Platforms          |             | Command | context                |     | Authority    |      |
config-if
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| switch# |      | show lldp | local-device |     | 1/1/10 |     |
| ------- | ---- | --------- | ------------ | --- | ------ | --- |
| Local   | Port | Data      |              |     |        |     |
===============
| Port-ID   |           |             | : 1/1/10   |     |     |     |
| --------- | --------- | ----------- | ---------- | --- | --- | --- |
| Port-Desc |           |             | : "1/1/10" |     |     |     |
| Port      | VLAN      | ID          | : 0        |     |     |     |
| PoE       | Plus      | Information |            |     |     |     |
| PoE       | Device    | Type        | : Type     | 2   | PSE |     |
| Power     | Source    |             | : Primary  |     |     |     |
| Power     | Priority  |             | : low      |     |     |     |
| PSE       | Allocated | Power:      | 25.0       | W   |     |     |
| PD        | Requested | Power       | : 25.0     | W   |     |     |
89
| AOS-CX10.12MonitoringGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
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
| Neighbor | Chassis-ID         |             | : 84:d4:7e:ce:5d:68 |      |
| -------- | ------------------ | ----------- | ------------------- | ---- |
| Neighbor | Management-Address |             | : 169.254.41.250    |      |
| Chassis  | Capabilities       | Available   | : Bridge,           | WLAN |
| Chassis  | Capabilities       | Enabled     | :                   |      |
| Neighbor | Port-ID            |             | : 84:d4:7e:ce:5d:68 |      |
| Neighbor | Port-Desc          |             | : eth0              |      |
| TTL      |                    |             | : 120               |      |
| Neighbor | Port               | VLAN ID     | :                   |      |
| Neighbor | PoEplus            | information | : DOT3              |      |
| Neighbor | Device             | Type        | : TYPE2             | PD   |
| Neighbor | Power              | Priority    | : Unkown            |      |
| Neighbor | Power              | Source      | : Primary           |      |
| Neighbor | Power              | Requested   | : 25.0              | W    |
| Neighbor | Power              | Allocated   | : 0.0 W             |      |
Power-over-Ethernet|90

|                | Neighbor    | Power   | Supported   |         | : No         |     |
| -------------- | ----------- | ------- | ----------- | ------- | ------------ | --- |
|                | Neighbor    | Power   | Enabled     |         | : No         |     |
|                | Neighbor    | Power   | Class       |         | : 5          |     |
|                | Neighbor    | Power   | Paircontrol |         | : No         |     |
|                | Neighbor    | Power   | Pairs       |         | : SIGNAL     |     |
| Command        | History     |         |             |         |              |     |
| Release        |             |         |             |         | Modification |     |
| 10.07orearlier |             |         |             |         | --           |     |
| Command        | Information |         |             |         |              |     |
| Platforms      |             | Command |             | context | Authority    |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show | power-over-ethernet |     |     |         |              |         |
| ---- | ------------------- | --- | --- | ------- | ------------ | ------- |
| show | power-over-ethernet |     |     | [member | <MEMBER-ID>] | [brief] |
Description
Displaysthestatusinformationofthefullsystem.
| Parameter   |     |     |     |     | Description                             |     |
| ----------- | --- | --- | --- | --- | --------------------------------------- | --- |
| <MEMBER-ID> |     |     |     |     | Displaysthedetailedstatusofgivenmember. |     |
<IFNAME>
Displaythedetailedstatusofgivenport.
| brief |     |     |     |     | Displaythebriefstatusofallportsorthegivenport. |     |
| ----- | --- | --- | --- | --- | ---------------------------------------------- | --- |
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
91
| AOS-CX10.12MonitoringGuide| |     |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- | --- |

| Quick PoE | Enabled |     |     | : None |     |
| --------- | ------- | --- | --- | ------ | --- |
| Internal  | Power   |     |     |        |     |
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
Power-over-Ethernet|92

| switch#    | show power-over-ethernet |             |       | brief |              |          |     |     |
| ---------- | ------------------------ | ----------- | ----- | ----- | ------------ | -------- | --- | --- |
| Status and | Configuration            | Information |       | for   | PoE          |          |     |     |
| Member     | 1 Power Status           |             |       |       |              |          |     |     |
| Available: | 370 W                    | Reserved:   | 55.60 |       | W Remaining: | 314.40 W |     |     |
| Always-on  | PoE Enabled:             |             | 1/1   |       |              |          |     |     |
| Quick      | PoE Enabled:             | None        |       |       |              |          |     |     |
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
93
AOS-CX10.12MonitoringGuide| (6200SwitchSeries)

| Port | En Priority | Detect | Act Rsrvd | Draw | Status | Sign |     |
| ---- | ----------- | ------ | --------- | ---- | ------ | ---- | --- |
------- --- ------ ------- ----- ------ ------ --------- ----- --- ----
| 1/1/1 | Yes Low | Off | Class 0.0 | W 0.0 | W Denied | None 4 | 2   |
| ----- | ------- | --- | --------- | ----- | -------- | ------ | --- |
1/1/2 Yes Critical Off Usage 1.6 W 1.5 W Delivering* Single 0 1
Showingsampleoutputforpower-over-ethernetforamissinglinecard:
| switch# | show power-over-ethernet |            | 1/3 brief |     |     |     |     |
| ------- | ------------------------ | ---------- | --------- | --- | --- | --- | --- |
| Module  | 1/3 is not               | physically | present.  |     |     |     |     |
Showingsampleoutputforpower-over-ethernetbriefforamissingmember:
| switch# | show power-over-ethernet |     | member   | 3 brief |     |     |     |
| ------- | ------------------------ | --- | -------- | ------- | --- | --- | --- |
| Member  | 3 is not physically      |     | present. |         |     |     |     |
Showingsampleoutputforpower-over-ethernetportwhenphysicalinterfaceisnotpresent:
| switch#        | show power-over-ethernet |              | 2/1/1        |     |     |     |     |
| -------------- | ------------------------ | ------------ | ------------ | --- | --- | --- | --- |
| Interface      | 2/1/1 is                 | not present. |              |     |     |     |     |
| Command        | History                  |              |              |     |     |     |     |
| Release        |                          |              | Modification |     |     |     |     |
| 10.07orearlier |                          |              | --           |     |     |     |     |
| Command        | Information              |              |              |     |     |     |     |
| Platforms      | Command                  | context      | Authority    |     |     |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
Power-over-Ethernet|94

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
95
| AOS-CX10.12MonitoringGuide| |     | (6200SwitchSeries) |     |
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
ArubaAirWave|96

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
97
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |
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

Aruba AirWave | 98

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
99
| AOS-CX10.12MonitoringGuide| |     | (6200SwitchSeries) |     |     |     |
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
ArubaAirWave|100

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
101
| AOS-CX10.12MonitoringGuide| | (6200SwitchSeries) |     |     |     |     |
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
ArubaAirWave|102

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<NAME> Specifiesthenameofthecontext.Range:1to32printableASCII
characters,excludingspaceandquestionmark(?).
vrf <VRF-NAME> SpecifiestheVRFassociatedwiththecontext.Default:default.
| community | <STRING> |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
SpecifiestheSNMPcommunitystringassociatedwiththecontext.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
103
| AOS-CX10.12MonitoringGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

Parameter

Description

priv <PRIV-PROTOCOL>

priv-pass {plaintext | ciphertext} <PRIV-PWORD>

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

On switch 1, configure a user called Admin, then issue the show running-config command to display
switch configuration settings. The snmpv3 user command uses the ciphertext option to protect the
users's passwords.

switch1(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword
priv des priv-pass plaintext myprivpass
switch1(config)# exit
switch1# show running-config

Aruba AirWave | 104

| Current | configuration: |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
105
| AOS-CX10.12MonitoringGuide| |     | (6200SwitchSeries) |     |     |     |
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

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

106

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
SupportandOtherResources|107

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

AOS-CX 10.12 Monitoring Guide | (6200 Switch Series)

108