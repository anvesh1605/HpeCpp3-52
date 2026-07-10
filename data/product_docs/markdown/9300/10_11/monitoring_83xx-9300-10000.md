AOS-CX 10.11 Monitoring
Guide

8320, 8325, 8360, 9300, 10000 Switch Series

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
| Contents                            |                                  |         |                    | 3   |
| ----------------------------------- | -------------------------------- | ------- | ------------------ | --- |
| About                               | this document                    |         |                    | 6   |
| Applicableproducts                  |                                  |         |                    | 6   |
| Latestversionavailableonline        |                                  |         |                    | 6   |
| Commandsyntaxnotationconventions    |                                  |         |                    | 6   |
| Abouttheexamples                    |                                  |         |                    | 7   |
| Identifyingswitchportsandinterfaces |                                  |         |                    | 7   |
| Monitoring                          | hardware                         | through | visual observation | 9   |
| DiagnosingwiththeLEDs               |                                  |         |                    | 9   |
| IP Flow                             | Information                      | Export  |                    | 13  |
| Flowmonitors                        |                                  |         |                    | 13  |
| Flowexporters                       |                                  |         |                    | 13  |
| Destinations                        |                                  |         |                    | 13  |
| FlowRecords                         |                                  |         |                    | 14  |
| ConfiguringIPFlowInformationExport  |                                  |         |                    | 14  |
|                                     | Stepone:CreateFlowRecords        |         |                    | 14  |
|                                     | Steptwo:Configureflowexporter(s) |         |                    | 16  |
|                                     | Stepthree:Configureamonitor(s)   |         |                    | 17  |
Stepfour:(Optional)EnableApplicationRecognitionandapplyaflowmonitortointer-
|                         | faces                |              |          | 17  |
| ----------------------- | -------------------- | ------------ | -------- | --- |
| FAQsandTroubleshooting  |                      |              |          | 18  |
| Flowmonitoringcommands  |                      |              |          | 18  |
|                         | flowexporter         |              |          | 19  |
|                         | flowmonitor          |              |          | 20  |
|                         | flowrecord           |              |          | 22  |
|                         | ipv4|ipv6flowmonitor |              |          | 24  |
|                         | showflowexporter     |              |          | 25  |
|                         | showflowmonitor      |              |          | 26  |
|                         | showflowrecord       |              |          | 28  |
| Boot                    | commands             |              |          | 30  |
| bootset-default         |                      |              |          | 30  |
| bootsystem              |                      |              |          | 30  |
| showboot-history        |                      |              |          | 32  |
| Switch                  | system               | and hardware | commands | 35  |
| External                | storage              |              |          | 36  |
| Externalstoragecommands |                      |              |          | 36  |
|                         | address              |              |          | 36  |
|                         | directory            |              |          | 37  |
|                         | disable              |              |          | 38  |
|                         | enable               |              |          | 38  |
|                         | external-storage     |              |          | 39  |
3
AOS-CX10.11MonitoringGuide| (83xx,9300,10000SwitchSeries)

|                                     | password(external-storage)         |            | 40  |
| ----------------------------------- | ---------------------------------- | ---------- | --- |
|                                     | showexternal-storage               |            | 41  |
|                                     | showrunning-configexternal-storage |            | 42  |
|                                     | type                               |            | 42  |
|                                     | username                           |            | 43  |
|                                     | vrf                                |            | 44  |
| IP-SLA                              |                                    |            | 46  |
| IP-SLAguidelines                    |                                    |            | 46  |
| LimitationswithVoIPSLAs             |                                    |            | 47  |
| IP-SLAcommands                      |                                    |            | 47  |
|                                     | http                               |            | 47  |
|                                     | icmp-echo                          |            | 48  |
|                                     | ip-sla                             |            | 49  |
|                                     | ip-slaresponder                    |            | 50  |
|                                     | showip-slaresponder                |            | 51  |
|                                     | showip-slaresponderresults         |            | 52  |
|                                     | showip-sla<SLA-NAME>               |            | 53  |
|                                     | start-test                         |            | 56  |
|                                     | stop-test                          |            | 56  |
|                                     | tcp-connect                        |            | 57  |
|                                     | udp-echo                           |            | 58  |
|                                     | udp-jitter-voip                    |            | 59  |
|                                     | vrf                                |            | 61  |
|                                     | showinterface                      |            | 61  |
| Mirroring                           |                                    |            | 67  |
| MirroringstatisticsandsFlow         |                                    |            | 67  |
| Limitations                         |                                    |            | 67  |
| Mirroringcommands                   |                                    |            | 68  |
|                                     | clearmirror                        |            | 68  |
|                                     | clearmirrorendpoint                |            | 68  |
|                                     | comment                            |            | 69  |
|                                     | copytcpdump-pcap                   |            | 70  |
|                                     | copytshark-pcap                    |            | 71  |
|                                     | destinationcpu                     |            | 72  |
|                                     | destinationinterface               |            | 73  |
|                                     | destinationtunnel                  |            | 74  |
|                                     | diagnostic                         |            | 76  |
|                                     | diagutilitiestcpdump               |            | 77  |
|                                     | disable                            |            | 79  |
|                                     | enable                             |            | 80  |
|                                     | mirrorsession                      |            | 80  |
|                                     | mirrorendpoint                     |            | 81  |
|                                     | showmirror                         |            | 82  |
|                                     | showmirrorendpoint                 |            | 84  |
|                                     | shutdown                           |            | 85  |
|                                     | source                             |            | 85  |
|                                     | sourceinterface                    |            | 86  |
|                                     | sourcevlan                         |            | 88  |
| Monitoring                          | a device                           | using SNMP | 91  |
| Breakout                            | cable support                      |            | 92  |
| Limitationswithbreakoutcablesupport |                                    |            | 92  |
| Breakoutcablesupportcommands        |                                    |            | 92  |
Contents|4

|                                                  | split                |           | 92  |
| ------------------------------------------------ | -------------------- | --------- | --- |
| Aruba                                            | AirWave              |           | 96  |
| SNMPsupportandAirWave                            |                      |           | 96  |
|                                                  | SNMPontheswitch      |           | 96  |
| SupportedfeatureswithAirWaveandtheAOS-CXswitch   |                      |           | 97  |
| ConfiguringtheAOS-CXswitchtobemonitoredbyAirWave |                      |           | 97  |
| AirWavecommands                                  |                      |           | 98  |
|                                                  | logging              |           | 98  |
|                                                  | snmp-servercommunity |           | 100 |
|                                                  | snmp-serverhost      |           | 101 |
|                                                  | snmp-servervrf       |           | 103 |
|                                                  | snmpv3context        |           | 103 |
|                                                  | snmpv3user           |           | 104 |
| Support                                          | and Other            | Resources | 107 |
| AccessingArubaSupport                            |                      |           | 107 |
| AccessingUpdates                                 |                      |           | 108 |
|                                                  | ArubaSupportPortal   |           | 108 |
|                                                  | MyNetworking         |           | 108 |
| WarrantyInformation                              |                      |           | 108 |
| RegulatoryInformation                            |                      |           | 108 |
| DocumentationFeedback                            |                      |           | 109 |
5
AOS-CX10.11MonitoringGuide| (83xx,9300,10000SwitchSeries)

Chapter 1
About this document
| About | this document |     |     |
| ----- | ------------- | --- | --- |
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedfor
administratorsresponsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
| Applicable | products |     |     |
| ---------- | -------- | --- | --- |
Thisdocumentappliestothefollowingproducts:
n Aruba8320SwitchSeries(JL479A,JL579A,JL581A)
Aruba8325SwitchSeries(JL624A,JL625A,JL626A,JL627A)
n
n Aruba8360SwitchSeries(JL700A,JL701A,JL702A,JL703A,JL706A,JL707A,JL708A,JL709A,JL710A,
JL711A,JL700C,JL701C,JL702C,JL703C,JL706C,JL707C,JL708C,JL709C,JL710C,JL711C,JL704C,JL705C,
JL719C,JL718C,JL717C,JL720C,JL722C,JL721C)
n Aruba9300SwitchSeries(R9A29A,R9A30A,R8Z96A)
n Aruba10000SwitchSeries(R8P13A,R8P14A)
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
6
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | ----------------------------- | --- | --- |

Convention

Usage

|

{ }

[ ]

… or

...

Vertical bar. A logical OR that separates multiple items from which you can
choose only one.
Any spaces that are on either side of the vertical bar are included for
readability and are not a required part of the command syntax.

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

About this document | 7

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 83xx, 9300, and 10000 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on

physical port 4 in slot 1 on member 1.

AOS-CX 10.11 Monitoring Guide | (83xx, 9300, 10000 Switch Series)

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
ForcompleteinformationonLEDbehaviorsforyourAOS-CXswitch,refertotheInstallationandGetting
StartedGuideforthatswitchseries,availablefordownloadfromtheArubaSwitchDocumentationsectionofthe
ArubaHardwareDocumentationandTranslationsPortal.
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
9
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- | --- | --- | --- |

PS1/PS2 LEDs

Global Status

Fan

Port LED

Diagnostic Tip

On green

On green

-

On, but the port is not
communicating

6

**Either the PS1 or PS2 LED is on amber, but not both.
Table 3: Diagnostic tips

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
not plugged into an active A

Verify that the power cord is plugged into an active
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

Try disconnecting power from the switch and wait a

assemblies may have failed.

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

Monitoring hardware through visual observation | 10

Tip

Problem

Solution

a 10G transceiver is installed in a port configured

for 25G, or the reverse.

n A 10GBase-T transceiver may be installed in an

incompatible port. Only ports 1, 2, 4, 5, 7, 8, 10, and

11 support 10GBase-T transceivers.

n The transceiver may have failed.
n The switch port may have failed.

Check the switch Event Log and show interface

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

AOS-CX 10.11 Monitoring Guide | (83xx, 9300, 10000 Switch Series)

11

Tip

Problem

Solution

a switch configuration change. Use the console

interface or, if you have configured an IP address

on the switch, use the web browser interface to

determine the state of the port and re-enable the

port if necessary.

n Verify that the switch port configuration matches

the configuration of the attached device. For

example, if the switch port is configured as “Full-

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

AOS-CX 10.11 Monitoring Guide | (83xx, 9300, 10000 Switch Series)

13

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

IP Flow Information Export | 14

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
15
AOS-CX10.11MonitoringGuide| (83xx,9300,10000SwitchSeries)

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
IPFlowInformationExport |16

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
17
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | ----------------------------- | --- | --- |

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
| Flow monitoring |     | commands |     |     |     |
| --------------- | --- | -------- | --- | --- | --- |
IPFlowInformationExport |18

flow exporter
| flow exporter   | <name>        |       |     |     |     |
| --------------- | ------------- | ----- | --- | --- | --- |
| export-protocol |               | ipfix |     |     |     |
| description     | <description> |       |     |     |     |
destination
| <hostname> |                      | [vrf vrfname] |                    |     |     |
| ---------- | -------------------- | ------------- | ------------------ | --- | --- |
| <IPaddr>   | [vrf                 | vrfname]      |                    |     |     |
| <ip6addr>  |                      | [vrf vrfname] |                    |     |     |
| type       | {hostname-or-ip-addr |               | | traffic-insight} |     |     |
no ..
| template  | data | timeout <timeout> |     |     |     |
| --------- | ---- | ----------------- | --- | --- | --- |
| transport | udp  | <port>            |     |     |     |
Description
AflowexporteristhepartoftheIPFlowInformationExport(IPFIX)featurethatdefineshowaflow
monitorexportsflowreports.Youcanassignthesameflowexporterconfigurationtomorethanone
flowmonitor.Eachflowexporterincludesadestinationsettingthatidentifiesthedevicetowhichthe
flowreportsaresent.Eachflowmonitorsupportsamaximumoftwodifferentflowexporter
configurations,sendingflowrecordstouptotwodestinations.
| Parameter       |     |       |     | Description                             |     |
| --------------- | --- | ----- | --- | --------------------------------------- | --- |
| <name>          |     |       |     | Nameoftheflowexporter,upto64characters. |     |
| export-protocol |     | ipfix |     | Defineanexportprotocolfortheflow        |     |
exporter.Thedefaultipfixprotocolistheonly
protocolcurrentlyavailable.
description <description> Adescriptionoftheflowexporter,upto256
charactersandspaces.
| destination | <hostname>|<IPaddr>|<ip6addr> |     |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- | --- |
Theexportersendsflowrecordstothis
destination.Thedestinationcanbedefinedasa
hostname,oranIPv4orIPv6IPaddress.
| [vrf | vrfname] |     |     | Youcanoptionallyincludethenameofthe |     |
| ---- | -------- | --- | --- | ----------------------------------- | --- |
destinationVRFinthedestinationdefinition.
| no .. |     |     |     | Negateanyconfiguredparameter. |     |
| ----- | --- | --- | --- | ----------------------------- | --- |
template data timeout <timeout> Aflowexportertemplatedescribestheformatof
exportedflowreports.Therefore,flowreports
cannotbedecodedproperlywithoutthe
correspondingtemplates.Thissettingdefineshow
oftentheflowexporterwillresendtemplatesto
theflowmonitor.Thesupportedrangeis1-86400
seconds,andthedefaultis600seconds.
| transport | udp <port> |     |     | Transportprotocolandportforsendingflow |     |
| --------- | ---------- | --- | --- | -------------------------------------- | --- |
recordreports.Thedefaultportisport4739,
Examples
Thefollowingexamplecreatesaflowexporterconfigurationnamedexporter-1.
| switch(config)#               |     | flow exporter | exporter-1  |           |          |
| ----------------------------- | --- | ------------- | ----------- | --------- | -------- |
| switch(config-flow-exporter)# |     |               | destination | 192.0.2.1 | vrf VRF1 |
19
| AOS-CX10.11MonitoringGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| --------------------------- | --- | ----------------------------- | --- | --- | --- |

| switch(config-flow-exporter)# |     |     | template data | timeout 1200 |
| ----------------------------- | --- | --- | ------------- | ------------ |
switch(config-flow-exporter)# description Exports flows to 192.0.2.1
Related Commands
| Command |     |     | Description |     |
| ------- | --- | --- | ----------- | --- |
flow record
Definedatatobeincludedinaflowrecordbyconfiguringflow
recordmatchandcollectfields
flow monitor Defineaflowmonitorconfiguration,includingtheflowexporter
andflowrecordassociatedtothatmonitor.
show flow exporter Displayflowexporterconfiguration,status,andstatistics.
| Command History     |         |         |                    |     |
| ------------------- | ------- | ------- | ------------------ | --- |
| Release             |         |         | Modification       |     |
| 10.11               |         |         | Commandintroduced. |     |
| Command Information |         |         |                    |     |
| Platforms           | Command | context | Authority          |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
|     | config-flow-exporter |     | rightsforthiscommand. |     |
| --- | -------------------- | --- | --------------------- | --- |
flow monitor
| flow monitor  | <name>          |     |           |     |
| ------------- | --------------- | --- | --------- | --- |
| exporter      | <name>          |     |           |     |
| cache timeout | active|inactive |     | <timeout> |     |
| description   | <description>   |     |           |     |
| record <name> |                 |     |           |     |
Description
AflowmonitoristhepartoftheIPFlowInformationExport(IPFIX)featurethatperformsnetwork
monitoringfortheselectedinterface.Aflowmonitorconfigurationconsistsofaflowrecord,aflow
cache,andoneormoreassociatedflowexporters.Aflowmonitorcompilesdatafromthenetwork
trafficontheinterfaceandstoresitintheflowcacheinaformatdefinedbytheflowrecord.Theflow
exportersassociatedwiththemonitorthenexportdatafromtheflowcachetotheflowexporter
destination.
| Parameter |     |     |     | Description                            |
| --------- | --- | --- | --- | -------------------------------------- |
| <name>    |     |     |     | Nameoftheflowmonitor,upto64characters. |
cache timeout active|inactive <timeout> Usethecachetimeoutparametertodefineanactive
orinactivetimeoutfortheflowmonitor.Aflow
monitorclosesaflowsessionthatisactiveforlonger
thantheactivetimeoutorinactiveforlongerthanthe
IPFlowInformationExport |20

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
inactivetimeout.
Thesupportedtimeoutrangesforboththeactive
timeoutandinactivetimeoutare30-604800seconds,
andthedefaultis30seconds.
| description |     |     | Adescriptionupto256characterslong,including |
| ----------- | --- | --- | ------------------------------------------- |
spaces.
| exporter <name> |     |     | Assignaflowexportertoaflowmonitor.Eachflow |
| --------------- | --- | --- | ------------------------------------------ |
monitorsupportsamaximumoftwodifferentflow
exporters,sendingflowrecordstouptotwo
destinations.
| record <name> |     |     | Assignsaflowrecordtoaflowmonitor. |
| ------------- | --- | --- | --------------------------------- |
Examples
Thefollowingexamplecreatesaflowmonitorconfigurationnamedmonitor-1.
| switch(config)# | flow monitor | monitor-1 |     |
| --------------- | ------------ | --------- | --- |
switch(config-flow-monitor)# description Monitor for analyzing basic ipv4 traffic
| switch(config-flow-monitor)# |     | exporter flow-exporter-1 |              |
| ---------------------------- | --- | ------------------------ | ------------ |
| switch(config-flow-monitor)# |     | exporter flow-exporter-2 |              |
| switch(config-flow-monitor)# |     | record flow-record-1     |              |
| switch(config-flow-monitor)# |     | cache timeout            | inactive 300 |
| switch(config-flow-monitor)# |     | cache timeout            | active 1500  |
Thefollowingworkflowchangestheflowrecordassignedtoaflowmonitor.
| switch(config)#              | flow monitor | flow-monitor-1       |     |
| ---------------------------- | ------------ | -------------------- | --- |
| switch(config-flow-monitor)# |              | record flow-record-2 |     |
Related Commands
| Command       |     | Description                                 |     |
| ------------- | --- | ------------------------------------------- | --- |
| flow exporter |     | Definehowaflowmonitorexportstheflowreports. |     |
flow record Definedatatobeincludedinaflowrecordbyconfiguringflow
recordmatchandcollectfields
flow monitor Enableflowmonitoringoninboundtrafficcomingintoan
interfacebyassigningaflowmonitortothatinterface.
Command History
| Release |     | Modification       |     |
| ------- | --- | ------------------ | --- |
| 10.11   |     | Commandintroduced. |     |
Command Information
21
AOS-CX10.11MonitoringGuide| (83xx,9300,10000SwitchSeries)

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
8360 config Administratorsorlocalusergroupmemberswithexecution
|     | config-flow-monitor |     | rightsforthiscommand. |     |
| --- | ------------------- | --- | --------------------- | --- |
flow record
| flow record | <name> |     |     |     |
| ----------- | ------ | --- | --- | --- |
match
| ipv4|ipv6 | {protocol|version}|{source|destination |     |      | address} |
| --------- | -------------------------------------- | --- | ---- | -------- |
| transport | {source|destination}                   |     | port |          |
collect
| application | name            |              |     |     |
| ----------- | --------------- | ------------ | --- | --- |
| counter     | {packets|bytes} |              |     |     |
| timestamp   | absolute        | {first|last} |     |     |
| description | <description>   |              |     |     |
Description
Definedatatobeincludedinaflowrecordbyconfiguringflowrecordmatchandcollectfields.The
matchattributesdefinewhatmakesthetrafficflowunique.Trafficwithmatchingattributes(for
example,trafficcomingfromthesameinterface,senttothesamedestinationwiththesameprotocol)
areclassifiedasasingleflow.Informationforsomeorallofthematchedsettingscanbecollectedand
exportedtoadestinationdefinedbytheflowexporterassignedtotheflowmonitor.
Trafficmustmatchamatchruledefinitionbeforeitcanbecollectedandsent.Youcannotcollectandsenddata
thatisnotmatched.
| Parameter |     |     | Description                                       |     |
| --------- | --- | --- | ------------------------------------------------- | --- |
| <name>    |     |     | Nameoftheflowmonitor,upto64characters.            |     |
| match     |     |     | matchtrafficaccordingtooneormoreofthefollowingkey |     |
attributes:
n ipv4—matchtrafficonanIPv4network
o destinationaddress—Matchtraffictothesamedestination
addressonanIPv4network
o sourceaddress—Matchtrafficfromthesamesource
addressonanIPv4network
o protocol—MatchtrafficusingthesameIPprotocolonan
IPv4network
o version—MatchtrafficusingthesameIPversiononanIPv4
network
n ipv6—matchtrafficonanIPv6network
o
destinationaddress—Matchtraffictothesamedestination
addressonanIPv6network
o
sourceaddress—Matchtrafficfromthesamesource
addressonanIPv6network
o
protocol—MatchtrafficusingthesameIPprotocolonan
IPv6network
IPFlowInformationExport |22

| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
o version—MatchtrafficusingthesameIPversiononanIPv6
network
|     |     | n   | transport—Configuretransportfiledsfortheflow |     |
| --- | --- | --- | -------------------------------------------- | --- |
o destinationport—Matchtrafficbythesamedestination
transportport
o sourceport—Matchtrafficfromthesamesourcetransport
port
description Adescriptionfortheflowrecordupto256characterslong,
includingspaces
| collect |     | Configuresdatafieldstobeincludedaflowrecord. |                                                  |     |
| ------- | --- | -------------------------------------------- | ------------------------------------------------ | --- |
|         |     | n                                            | applicationname—Includetheapplicationnameasanon- |     |
keyfieldinaflowrecord
|     |     | n   | counter—Configurecounterfieldsintheflow |     |
| --- | --- | --- | --------------------------------------- | --- |
o
packets—Collectcounterdataforpacketsintheflow
o bytes—Collectcounterdataforbytesintheflow
|     |     | n   | timestamp—Configuretimestampfieldsofthepacketinthe |     |
| --- | --- | --- | -------------------------------------------------- | --- |
flow
o
absolutefirst—Collectabsolutetimestampofthefirst
packetobserved
o
absolutelast—Collectabsolutetimestampofthelast
packetobserved
Examples
AddingIPv4andtransportmatchfieldstoflowrecordflow-record-1.
| switch(config)#             | flow record | flow-record-1   |                |         |
| --------------------------- | ----------- | --------------- | -------------- | ------- |
| switch(config-flow-record)# |             | match ipv4      | source address |         |
| switch(config-flow-record)# |             | match ipv4      | destination    | address |
| switch(config-flow-record)# |             | match ipv4      | protocol       |         |
| switch(config-flow-record)# |             | match ipv4      | version        |         |
| switch(config-flow-record)# |             | match transport | source         | port    |
| switch(config-flow-record)# |             | match transport | destination    | port    |
switch(config-flow-record)# description Record used for basic ipv4 traffic
analysis
RemovingtheIPv4destinationmatchfieldfromtheflowrecorddefinedinthepreviousexample.
| switch(config)#             | flow record | flow-record-1 |                  |         |
| --------------------------- | ----------- | ------------- | ---------------- | ------- |
| switch(config-flow-record)# |             | no match      | ipv4 destination | address |
Addingcounterandtimestampcollectfieldstoflowrecordflow-record-1.
| switch(config)#             | flow record | flow-record-1 |                 |     |
| --------------------------- | ----------- | ------------- | --------------- | --- |
| switch(config-flow-record)# |             | collect       | counter packets |     |
| switch(config-flow-record)# |             | collect       | counter bytes   |     |
23
AOS-CX10.11MonitoringGuide| (83xx,9300,10000SwitchSeries)

| switch(config-flow-record)# |          |     |     | collect | timestamp   | absolute | first |
| --------------------------- | -------- | --- | --- | ------- | ----------- | -------- | ----- |
| switch(config-flow-record)# |          |     |     | collect | timestamp   | absolute | last  |
| Related                     | Commands |     |     |         |             |          |       |
| Command                     |          |     |     |         | Description |          |       |
flow exporter
Definehowaflowmonitorexportstheflowreports.
flow monitor Defineaflowmonitorconfiguration,includingtheflowexporter
andflowrecordassociatedtothatmonitor.
| show flow | record      |     |         |     | Displayflowrecordconfigurationandstatus. |     |     |
| --------- | ----------- | --- | ------- | --- | ---------------------------------------- | --- | --- |
| Command   | History     |     |         |     |                                          |     |     |
| Release   |             |     |         |     | Modification                             |     |     |
| 10.11     |             |     |         |     | Commandintroduced.                       |     |     |
| Command   | Information |     |         |     |                                          |     |     |
| Platforms | Command     |     | context |     | Authority                                |     |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
|              | config-flow-record |         |        |     | rightsforthiscommand. |     |     |
| ------------ | ------------------ | ------- | ------ | --- | --------------------- | --- | --- |
| ipv4|ipv6    | flow               | monitor |        |     |                       |     |     |
| [no] ip|ipv6 | flow               | monitor | <name> | in  |                       |     |     |
Description
Enableflowmonitoringoninboundandoutboundinterfacesbyassigningaflowmonitortothat
interface.OnlyphysicalinterfacesandLAGinterfacescanbemonitored.Aflowmonitorcannotbe
appliedtoaninterfacethatispartofaLAG.Ifanunsupportedapplicationisattempted,anerror
messagewillbedisplayed.Iftheflowmonitorisassociatedwithaflowrecordthatcontainsapplication
fieldsascollectfields,thenApplicationRecognitionshouldbeenabledonthesameinterface.
The[no]formofcommanddisablestheflowmonitoring.
Examples
Associateaflowmonitorconfigurationnamedflow-monitor-1 andflow-monitor-2 forIPv4orIPv6
trafficrespectivelyonphysicalinterface.
| switch(config)#    |     | interface |           | 1/1/1   |                |     |     |
| ------------------ | --- | --------- | --------- | ------- | -------------- | --- | --- |
| switch(config-if)# |     |           | ip flow   | monitor | flow-monitor-1 |     | in  |
| switch(config-if)# |     |           | ipv6 flow | monitor | flow-monitor-2 |     | in  |
Associateaflowmonitorconfigurationnamedflow-monitor-3andflow-monitor-4 forIPv4orIPv6
trafficrespectivelyonaLaginterface.
IPFlowInformationExport |24

| switch(config)#        | interface | lag       | 1       |                |     |
| ---------------------- | --------- | --------- | ------- | -------------- | --- |
| switch(config-lag-if)# |           | ip flow   | monitor | flow-monitor-3 | in  |
| switch(config-lag-if)# |           | ipv6 flow | monitor | flow-monitor-4 | in  |
Related Commands
| Command       |     |     | Description                                 |     |     |
| ------------- | --- | --- | ------------------------------------------- | --- | --- |
| flow exporter |     |     | Definehowaflowmonitorexportstheflowreports. |     |     |
flow record Definedatatobeincludedinaflowrecordbyconfiguringflow
recordmatchandcollectfields
flow monitor Defineaflowmonitorconfiguration,includingtheflowexporter
andflowrecordassociatedtothatmonitor.
| Command History     |         |         |                    |     |     |
| ------------------- | ------- | ------- | ------------------ | --- | --- |
| Release             |         |         | Modification       |     |     |
| 10.11               |         |         | Commandintroduced. |     |     |
| Command Information |         |         |                    |     |     |
| Platforms           | Command | context | Authority          |     |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
|                    | config-flow-monitor  |     | rightsforthiscommand. |     |     |
| ------------------ | -------------------- | --- | --------------------- | --- | --- |
| show flow          | exporter             |     |                       |     |     |
| show flow exporter | [<name>][statistics] |     |                       |     |     |
Description
Displayflowexporterconfigurationandstatus.Whennoexporternameisspecified,theoutputofthis
commanddisplaysinformationforallflowexporters.
Theoutputofthiscommandcanindicatethefollowingstatustypes:
n Accepted
n Rejected(Internalerror:exporterdoesnotexist)
n Rejected(Internalerror:destinationtypedoesnotexist)
n Rejected(DestinationtypeisTrafficInsight,butnodestinationisspecified)
Rejected(DestinationtypeisTrafficInsight,butthespecifiedTrafficInsightinstancedoesnotexist)
n
n Rejected(DestinationtypeisTrafficInsight,butthespecifiedTrafficInsightinstanceisnotenabled)
n Rejected(DestinationtypeisTrafficInsight,butthespecifiedTrafficInsightinstancesourceisnot
IPFIX)
n Rejected(Internalerror:destinationtypeisTrafficInsight,butthespecifiedTrafficInsightinstanceis
invalid)
Rejected(DestinationtypeishostnameorIPaddress,butnodestinationisspecified)
n
25
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- | --- |

n Rejected(DestinationtypeishostnameorIPaddress,butthespecifiedhostnameorIPaddressis
invalid)
| Parameter |     |     | Description            |     |
| --------- | --- | --- | ---------------------- | --- |
| <name>    |     |     | Nameoftheflowexporter. |     |
Examples
Displaytheconfigurationofaflowexporternamedexporter-1.
| switch# | show flow | exporter exporter-1 |     |     |
| ------- | --------- | ------------------- | --- | --- |
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
Related Commands
| Command             |         |         | Description                                 |     |
| ------------------- | ------- | ------- | ------------------------------------------- | --- |
| flow exporter       |         |         | Definehowaflowmonitorexportstheflowreports. |     |
| Command History     |         |         |                                             |     |
| Release             |         |         | Modification                                |     |
| 10.11               |         |         | Commandintroduced.                          |     |
| Command Information |         |         |                                             |     |
| Platforms           | Command | context | Authority                                   |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
|                   | config-flow-exporter |     | rightsforthiscommand. |     |
| ----------------- | -------------------- | --- | --------------------- | --- |
| show flow         | monitor              |     |                       |     |
| show flow monitor | [<name>][statistics] |     |                       |     |
Description
Displayflowmonitorconfigurationandstatus.Whennomonitornameisspecified,theoutputofthis
commanddisplaysinformationforallflowmonitors.
Theoutputofthiscommandcanindicatethefollowingstatustypes:
IPFlowInformationExport |26

n Accepted
n Rejected(Internalerror:monitordoesnotexist)
Rejected(Arecordmustbeassignedtothemonitor,butnorecordisassigned)
n
n Rejected(Thestateoftheassignedrecordisrejected)
n Rejected(Internalerror:failureinprocessingtherecordconfiguration)
n Rejected(Thestateofoneormoreoftheassignedflowexportersisrejected)
| Parameter  |     |     | Description                              |     |
| ---------- | --- | --- | ---------------------------------------- | --- |
| <name>     |     |     | Nameoftheflowmonitor.                    |     |
| statistics |     |     | Displayadditionalflowandcachestatistics. |     |
Examples
Displaytheconfigurationofaflowmoitornamedflow-monitor-1.
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
| Inactive     | Timeout      | : 1800    |            |     |
| ------------ | ------------ | --------- | ---------- | --- |
| Active       | Timeout      | : 300     |            |     |
| switch# show | flow monitor | monitor-1 | statistics |     |
--------------------------------------------------------------------------------
| Flow monitor | 'monitor-1' |     |     |     |
| ------------ | ----------- | --- | --- | --- |
--------------------------------------------------------------------------------
| Current Entries |         | : 2 |     |     |
| --------------- | ------- | --- | --- | --- |
| Flows Added     |         | : 4 |     |     |
| Total Flows     | Aged    | : 2 |     |     |
| Active          | Timeout | : 1 |     |     |
| Inactive        | Timeout | : 1 |     |     |
Related Commands
| Command |     |     | Description |     |
| ------- | --- | --- | ----------- | --- |
flow monitor Defineaflowmonitorconfiguration,includingtheflowexporter
andflowrecordassociatedtothatmonitor.
| Command History     |     |     |                    |     |
| ------------------- | --- | --- | ------------------ | --- |
| Release             |     |     | Modification       |     |
| 10.11               |     |     | Commandintroduced. |     |
| Command Information |     |     |                    |     |
27
AOS-CX10.11MonitoringGuide| (83xx,9300,10000SwitchSeries)

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
8360 config Administratorsorlocalusergroupmemberswithexecution
|                  | config-flow-exporter |     | rightsforthiscommand. |     |
| ---------------- | -------------------- | --- | --------------------- | --- |
| show flow        | record               |     |                       |     |
| show flow record | [<name>]             |     |                       |     |
Description
Displayflowrecordconfigurationandstatus.Whennorecordnameisspecified,theoutputofthis
commanddisplaysinformationforallflowrecords.
Theoutputofthiscommandcanindicatethefollowingstatustypes:
n Accepted
n Rejected(Internalerror:failedtoprocessrecord)
n Rejected(MixofIPv4andIPv6matchfieldsisnotallowed.SpecifymatchfieldsofthesameIPversion
(IPv4orIPv6))
n Rejected(Incompletematchfields.Themandatorymatchfieldsare:version,sourceaddress,
destinationaddress,
n protocol,transportdestinationport,andtransportsourceport)
| Parameter |     |     | Description          |     |
| --------- | --- | --- | -------------------- | --- |
| <name>    |     |     | Nameoftheflowrecord. |     |
Examples
Displaytheconfigurationofaflowrecordnamedflow-record-1.
| switch# | show flow | record record-1 |     |     |
| ------- | --------- | --------------- | --- | --- |
--------------------------------------------------------------------------------
| Flow record | 'record-1' |     |     |     |
| ----------- | ---------- | --- | --- | --- |
--------------------------------------------------------------------------------
| Description  |                | : Used for | IPv4 traffic | analysis |
| ------------ | -------------- | ---------- | ------------ | -------- |
| Status       |                | : Accepted |              |          |
| Match Fields |                |            |              |          |
| ipv4         | destination    | address    |              |          |
| ipv4         | protocol       |            |              |          |
| ipv4         | source address |            |              |          |
| ipv4         | version        |            |              |          |
| transport    | destination    | port       |              |          |
| transport    | source         | port       |              |          |
| Collect      | Fields         |            |              |          |
| application  | name           |            |              |          |
| counter      | bytes          |            |              |          |
| counter      | packets        |            |              |          |
Related Commands
IPFlowInformationExport |28

| Command |     |     | Description |
| ------- | --- | --- | ----------- |
flow record Definedatatobeincludedinaflowrecordbyconfiguringflow
recordmatchandcollectfields
| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.11               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
8360 config Administratorsorlocalusergroupmemberswithexecution
|     | config-flow-exporter |     | rightsforthiscommand. |
| --- | -------------------- | --- | --------------------- |
29
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | ----------------------------- | --- | --- |

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

AOS-CX 10.11 Monitoring Guide | (83xx, 9300, 10000 Switch Series)

30

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

Boot commands | 31

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
32
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- |

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
Bootcommands|33

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
34
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | ----------------------------- | --- | --- |

Chapter 5
|               |              | Switch   | system | and hardware | commands |
| ------------- | ------------ | -------- | ------ | ------------ | -------- |
| Switch system | and hardware | commands |        |              |          |
Switchsystemandhardwarecommandsaregeneralcommandsusedtoconfigurefundamentalsettings
ontheswitch.
RefertotheFundamentalsGuidetoviewtheswitchsystemandhardwarecommands.
35
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- | --- |

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
36
| AOS-CX10.11MonitoringGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | --- | ----------------------------- | --- | --- |

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
9300
10000
directory
| directory <DIRECTORY-NAME> |                  |     |     |     |
| -------------------------- | ---------------- | --- | --- | --- |
| no directory               | <DIRECTORY-NAME> |     |     |     |
Description
Selectsanexistingdirectoryontheexternalstoragevolume.
Thenoformofthiscommandclearsadirectoryofanexternalstoragevolume.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<DIRECTORY-NAME>
Specifiestheexternalstoragedirectoryformappingthevolume.
Examples
Creatingavolumenamedlogfilesthatismappedunder/homeontheserver:
switch(config)#
|                                           | external-storage |     | logfiles  |       |
| ----------------------------------------- | ---------------- | --- | --------- | ----- |
| switch(config-external-storage-logfiles)# |                  |     | directory | /home |
Clearingthedirectory/home:
| switch(config)#                           | external-storage |     | logfiles     |       |
| ----------------------------------------- | ---------------- | --- | ------------ | ----- |
| switch(config-external-storage-logfiles)# |                  |     | no directory | /home |
| Command History                           |                  |     |              |       |
Externalstorage|37

| Release             |         |         | Modification |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8320 config-external-storage-<VOLUME-NAME> OperatorsorAdministratorsorlocal
| 8325 |     |     |     | usergroupmemberswithexecution |
| ---- | --- | --- | --- | ----------------------------- |
rightsforthiscommand.Operatorscan
8360
executethiscommandfromthe
9300
| 10000 |     |     |     | operatorcontext(>)only. |
| ----- | --- | --- | --- | ----------------------- |
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
config-external-storage-<VOLUME-NAME>
| 8320 |     |     |     | OperatorsorAdministratorsorlocal  |
| ---- | --- | --- | --- | --------------------------------- |
| 8325 |     |     |     | usergroupmemberswithexecution     |
| 8360 |     |     |     | rightsforthiscommand.Operatorscan |
| 9300 |     |     |     | executethiscommandfromthe         |
operatorcontext(>)only.
10000
enable
enable
no enable
Description
38
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- |

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
| 9300 |     |     |     | executethiscommandfromthe         |
operatorcontext(>)only.
10000
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
Externalstorage|39

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
9300
10000
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
40
| AOS-CX10.11MonitoringGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | --- | ----------------------------- | --- | --- |

| switch(config)# | external-storage |     | logfiles |     |     |     |
| --------------- | ---------------- | --- | -------- | --- | --- | --- |
switch(config-external-storage-logfiles)#
|                |             |         |              | no password | plaintext | Xj#9 |
| -------------- | ----------- | ------- | ------------ | ----------- | --------- | ---- |
| Command        | History     |         |              |             |           |      |
| Release        |             |         | Modification |             |           |      |
| 10.07orearlier |             |         | --           |             |           |      |
| Command        | Information |         |              |             |           |      |
| Platforms      | Command     | context |              |             | Authority |      |
8320 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
memberswithexecutionrightsforthis
8325
command.
8360
9300
10000
show external-storage
| show external-storage |     | [<VOLUME-NAME>] |     |     |     |     |
| --------------------- | --- | --------------- | --- | --- | --- | --- |
Description
Showsexternalstorageconfigurationandstateforallvolumesorforaspecifiedvolume.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<VOLUME-NAME>
Specifiestheexternalstoragevolumenamethattheshow
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
| Command        | History     |     |              |     |     |     |
| -------------- | ----------- | --- | ------------ | --- | --- | --- |
| Release        |             |     | Modification |     |     |     |
| 10.07orearlier |             |     | --           |     |     |     |
| Command        | Information |     |              |     |     |     |
Externalstorage|41

| Platforms |     | Command | context |     | Authority |
| --------- | --- | ------- | ------- | --- | --------- |
8320 Administratorsorlocalusergroupmemberswithexecutionrights
Operator(>)orManager
| 8325 |     | (#) |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
8360
9300
10000
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
8320 Administratorsorlocalusergroupmemberswithexecutionrights
Operator(>)orManager
| 8325 |     | (#) |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
8360
9300
10000
type
| type {nfsv3 |        | | nfsv4 | | scp} |     |     |
| ----------- | ------ | ------- | ------ | --- | --- |
| no type     | {nfsv3 | | nfsv4 | | scp} |     |     |
Description
42
| AOS-CX10.11MonitoringGuide| |     |     | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | --- | --- | ----------------------------- | --- | --- |

Setsthenetworkattachedstorageaccesstypeforreachingtheexternalstoragevolume.
Thenoformofthiscommanddeletesanexternalstoragevolume.
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
| Command History                           |                  |         |              |           |
| Release                                   |                  |         | Modification |           |
| 10.07orearlier                            |                  |         | --           |           |
| Command Information                       |                  |         |              |           |
| Platforms                                 | Command          | context |              | Authority |
8320 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 8325 |     |     |     | memberswithexecutionrightsforthis |
| ---- | --- | --- | --- | --------------------------------- |
| 8360 |     |     |     | command.                          |
9300
10000
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
Externalstorage|43

Examples
Creatingavolumenamedlogfileswiththeusernamenassuser:
switch(config)#
|                                           | external-storage |     | logfiles |         |
| ----------------------------------------- | ---------------- | --- | -------- | ------- |
| switch(config-external-storage-logfiles)# |                  |     | username | nasuser |
Clearingtheusernamenasuserfromaccessingthelogfilesvolume:
| switch(config)#                           | external-storage |         | logfiles     |           |
| ----------------------------------------- | ---------------- | ------- | ------------ | --------- |
| switch(config-external-storage-logfiles)# |                  |         | no username  | nasuser   |
| Command History                           |                  |         |              |           |
| Release                                   |                  |         | Modification |           |
| 10.07orearlier                            |                  |         | --           |           |
| Command Information                       |                  |         |              |           |
| Platforms                                 | Command          | context |              | Authority |
8320 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
| 8325 |     |     |     | memberswithexecutionrightsforthis |
| ---- | --- | --- | --- | --------------------------------- |
| 8360 |     |     |     | command.                          |
9300
10000
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
44
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- |

| switch(config)# | external-storage |     | logfiles |     |
| --------------- | ---------------- | --- | -------- | --- |
switch(config-external-storage-logfiles)#
no vrf nas
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8320 config-external-storage-<VOLUME-NAME> Administratorsorlocalusergroup
memberswithexecutionrightsforthis
8325
command.
8360
9300
10000
Externalstorage|45

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

AOS-CX 10.11 Monitoring Guide | (83xx, 9300, 10000 Switch Series)

46

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

IP-SLA | 47

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
9300
10000
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
48
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | ----------------------------- | --- | --- |

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
name-server <IPV4-ADDR-DNS-SERVER> SpecifiestheDNSserverfordestinationhostname
resolution.
payload-size <PAYLOAD-SIZE> SpecifiesthepayloadsizeofanSLAprobe.Range:0to
1440.
tos <TYPE-OF-SERVICE>
Specifiesthetypeofservetobeusedintheprobe
packets.Range:0to255.
probe-interval <PROBE-INTERVAL> Specifiestheprobeintervalinseconds.Range:5to
604800.
Examples
switch(config)#
|                             | ip-sla | test |           |                |         |
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
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | --- | ------------------------------ | --- |
8360
9300
10000
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
IP-SLA|49

Examples
CreatinganIP-SLA:
switch(config)#
|     | ip-sla | 1   |     |     |
| --- | ------ | --- | --- | --- |
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
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8360
9300
10000
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
| Parameter      |     |     | Description                                |     |
| -------------- | --- | --- | ------------------------------------------ | --- |
| <SLA-NAME>     |     |     | SpecifiestheSLAname.                       |     |
| udp-echo       |     |     | Enablesresponderforudp-echoprobes.         |     |
| tcp-connect    |     |     | SelectsTCPconnectastheIP-SLAtestmechanism. |     |
| vrf <VRF-NAME> |     |     | SpecifiesthenameoftheVRFtouse.             |     |
50
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- |

| Parameter       |     |     |     | Description                                    |
| --------------- | --- | --- | --- | ---------------------------------------------- |
| udp-jitter-voip |     |     |     | SelectsVOIPjitterastheIP-SLAtestmechanism.     |
| <PORT-NUM>      |     |     |     | SpecifiestheportnumbertolistenforIP-SLAprobes. |
Range:1to65535.
| [source | {<SOURCE-IPV4-ADDR> |     | | <IFNAME>}] |     |
| ------- | ------------------- | --- | ------------ | --- |
SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
Examples
switch(config)# ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
switch(config)# ip-sla responder SLA1 udp-echo 8000 source 1/1/1
switch(config)# no ip-sla responder SLA1 udp-echo 8000 source 2.2.2.2
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8360
9300
10000
| show ip-sla | responder |            |     |     |
| ----------- | --------- | ---------- | --- | --- |
| show ip-sla | responder | <SLA-NAME> |     |     |
Description
ShowsthegivenIP-SLAresponderconfigurationandoperationstatus.
| Parameter  |     |     | Description          |     |
| ---------- | --- | --- | -------------------- | --- |
| <SLA-NAME> |     |     | SpecifiestheSLAname. |     |
Examples
| switch(config)# |      | show ip-sla | responder | SLA3 |
| --------------- | ---- | ----------- | --------- | ---- |
| SLA             | Name | :           | SLA3      |      |
| IP-SLA          | Type | :           | Udp-echo  |      |
IP-SLA|51

|                | VRF         |           | : Default |              |     |
| -------------- | ----------- | --------- | --------- | ------------ | --- |
|                | Responder   | Port      | : 8000    |              |     |
|                | Responder   | IP        | : 2.2.2.3 |              |     |
|                | Responder   | Interface | : 1/1/1   |              |     |
|                | Responder   | Status    | : Running |              |     |
| Command        | History     |           |           |              |     |
| Release        |             |           |           | Modification |     |
| 10.07orearlier |             |           |           | --           |     |
| Command        | Information |           |           |              |     |
| Platforms      |             | Command   | context   | Authority    |     |
config
8320 Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --------------- | --- |
8360
9300
10000
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
| Command | History   |             |            |              |              |
52
| AOS-CX10.11MonitoringGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| --------------------------- | --- | ----------------------------- | --- | --- | --- |

| Release        |             |         |     |         | Modification |     |     |
| -------------- | ----------- | ------- | --- | ------- | ------------ | --- | --- |
| 10.07orearlier |             |         |     |         | --           |     |     |
| Command        | Information |         |     |         |              |     |     |
| Platforms      |             | Command |     | context | Authority    |     |     |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- |
8360
9300
10000
| show | ip-sla | <SLA-NAME> |     |         |     |     |     |
| ---- | ------ | ---------- | --- | ------- | --- | --- | --- |
| show | ip-sla | <SLA-NAME> |     | results |     |     |     |
Description
ShowsthegivenIP-SLAsourceconfigurationandstatus.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<SLA-NAME>
SpecifiestheSLAname.
| results |     |     |     |     | ShowsthestatisticscalculatedforanSLAtype. |     |     |
| ------- | --- | --- | --- | --- | ----------------------------------------- | --- | --- |
Examples
| switch# |              | show ip-sla |                   | xyz results  |             |               |             |
| ------- | ------------ | ----------- | ----------------- | ------------ | ----------- | ------------- | ----------- |
|         | IP-SLA       | session     |                   | status       |             |               |             |
|         | IP-SLA       |             | Name              |              |             | : xyz         |             |
|         | IP-SLA       |             | Type              |              |             | : tcp-connect |             |
|         | Destination  |             |                   | Host Name/IP | Address:    | 2.2.2.1       |             |
|         | Destination  |             |                   | Port         |             | : 8888        |             |
|         | Source       |             | IP Address/IFName |              |             | : 2.2.2.2     |             |
|         | Source       |             | Port              |              |             | : 5555        |             |
|         | Status       |             |                   |              |             | : Running     |             |
|         | IP-SLA       | session     |                   | cumulative   | counters    |               |             |
|         | Total        | Probes      |                   | Transmitted  |             | : 1           |             |
|         | Probes       |             | Timed-out         |              |             | : 0           |             |
|         | Bind         | Error       |                   |              |             | : 0           |             |
|         | Destination  |             |                   | Address      | Unreachable | : 0           |             |
|         | DNS          | Resolution  |                   | Failures     |             | : 0           |             |
|         | Reception    |             | Error             |              |             | : 0           |             |
|         | Transmission |             |                   | Error        |             | : 0           |             |
|         | IP-SLA       | Latest      | Probe             | Results      |             |               |             |
|         | Last         | Probe       | Time              |              |             | : 2018 Jul    | 13 02:00:35 |
|         | Packets      |             | Sent              |              |             | : 1           |             |
|         | Packets      |             | Received          |              |             | : 1           |             |
|         | Packet       |             | Loss              | in Test      |             | : 0.0000%     |             |
|         | Minimum      | RTT(ms)     |                   |              |             | : 0.7900      |             |
IP-SLA|53

|                 | Maximum RTT(ms)         |                   |              |               | : 0.7900          |              |            |     |
| --------------- | ----------------------- | ----------------- | ------------ | ------------- | ----------------- | ------------ | ---------- | --- |
|                 | Average RTT(ms)         |                   |              |               | : 0.7900          |              |            |     |
|                 | DNS RTT(ms)             |                   |              |               | : 0.0000          |              |            |     |
|                 | TCP RTT(ms)             |                   |              |               | : 0.9710          |              |            |     |
| switch(config)# |                         | show              | ip-sla       | xyz           |                   |              |            |     |
|                 | IP-SLA Name             |                   |              | : xyz         |                   |              |            |     |
|                 | Status                  |                   |              | : scheduled   |                   |              |            |     |
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
54
AOS-CX10.11MonitoringGuide| (83xx,9300,10000SwitchSeries)

|                 | Voice        | Scores:           |                    |     |              |     |     |     |     |     |
| --------------- | ------------ | ----------------- | ------------------ | --- | ------------ | --- | --- | --- | --- | --- |
|                 | MOS          | Score             |                    |     | : 4.38 ICPIF |     |     |     | :   | 0   |
| switch(config)# |              | show ip-sla       | m3op               |     |              |     |     |     |     |     |
|                 | IP-SLA       | Name              | : jitter-sla       |     |              |     |     |     |     |     |
|                 | Status       |                   | : Running          |     |              |     |     |     |     |     |
|                 | IP-SLA       | Type              | : udp-jitter-voip  |     |              |     |     |     |     |     |
|                 | VRF          |                   | : ipslasrc         |     |              |     |     |     |     |     |
|                 | Source       | IP                | : 2.2.2.2          |     |              |     |     |     |     |     |
|                 | Source       | Interface         | :                  |     |              |     |     |     |     |     |
|                 | Domain       | Name Server       | :                  |     |              |     |     |     |     |     |
|                 | TOS          |                   | : 10               |     |              |     |     |     |     |     |
|                 | Probe        | Interval(seconds) | : 90               |     |              |     |     |     |     |     |
|                 | Advantage    | Factor            | : 0                |     |              |     |     |     |     |     |
|                 | Codec        | Type              | : g711a            |     |              |     |     |     |     |     |
| switch(config)# |              | show ip-sla       | http-sla           |     |              |     |     |     |     |     |
|                 | IP-SLA       | Name              | : http-sla         |     |              |     |     |     |     |     |
|                 | Status       |                   | : Running          |     |              |     |     |     |     |     |
|                 | IP-SLA       | Type              | : http             |     |              |     |     |     |     |     |
|                 | VRF          |                   | : ipslasrc         |     |              |     |     |     |     |     |
|                 | Source       | IP                | : 2.2.2.2          |     |              |     |     |     |     |     |
|                 | Source       | Interface         | :                  |     |              |     |     |     |     |     |
|                 | Domain       | Name Server       | : 10.10.10.2       |     |              |     |     |     |     |     |
|                 | Probe        | Interval(seconds) | : 90               |     |              |     |     |     |     |     |
|                 | HTTP Request | Type              | : GET              |     |              |     |     |     |     |     |
|                 | HTTP/HTTPS   | URL               | : abcd.com/ws/home |     |              |     |     |     |     |     |
|                 | Cache        |                   | : Enabled          |     |              |     |     |     |     |     |
|                 | HTTP Proxy   | URL               | :                  |     |              |     |     |     |     |     |
|                 | HTTP Version | Number            | : 1.1              |     |              |     |     |     |     |     |
```
| ##### | IP-SLA | status description |     |     |     |     |     |     |     |     |
| ----- | ------ | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
```
|     | | Status |     | | Description |     |     |     |     |     |     | |   |
| --- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|-------------------------|------------------------------------------------|
|     | | Running |     | | SLA | is  | fully operational |     |     |     |     | |   |
| --- | --------- | --- | ----- | --- | ----------------- | --- | --- | --- | --- | --- |
| Bind Error | Another service is using the same source port |
|     | | Interface | Down | | Interface |     | status | is not | up  |     |     |     |
| --- | ----------- | ---- | ----------- | --- | ------ | ------ | --- | --- | --- | --- |
| Dns Resolution Error | Failed to resolve destination hostname |
|     | | No Route |       | | No         | available | route    | to the   | responder |         |     | |   |
| --- | ---------- | ----- | ------------ | --------- | -------- | -------- | --------- | ------- | --- | --- |
|     | | Internal | Error | | Unexpected |           | error    | prevents | SLA       | session |     | |   |
|     | | Disabled |       | | SLA        | is        | disabled |          |           |         |     | |   |
|Configuration Incomplete | Configuration is not complete to enable the SLA|
```
| ##### | IP SLA | session cumulative | counters |     | description |     |     |     |     |     |
| ----- | ------ | ------------------ | -------- | --- | ----------- | --- | --- | --- | --- | --- |
```
|     | | Status |     |     | |   | Description |     |     |     |     |     |
| --- | -------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
|
|--------------------------------|--------------------------------------------
------------------------------|
|Probes Timed-out | Total numbers of probes failed to receive
| response. |       |                      | |   |     |               |     |        |              |     |        |
| --------- | ----- | -------------------- | --- | --- | ------------- | --- | ------ | ------------ | --- | ------ |
|           | |Bind | Error                |     | |   | Total numbers | of  | probes | transmission |     | failed |
| as source |       | port not available.| |     |     |               |     |        |              |     |        |
|Destination Address Unreachable | Total numbers of probes transmission failed
| due | to route | unavailable. | |   |     |     |     |     |     |     |     |
| --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|DNS Resolution Failures | Total numbers of probes failed due to DNS
| resolution |            | failure. | |   |     |               |     |        |        |     |     |
| ---------- | ---------- | -------- | --- | --- | ------------- | --- | ------ | ------ | --- | --- |
|            | |Reception | Error    |     | |   | Total numbers | of  | probes | failed | due | to  |
IP-SLA|55

| internal            | error in              | reception. | |            |         |           |            |     |
| ------------------- | --------------------- | ---------- | ------------ | ------- | --------- | ---------- | --- |
| |Transmission       |                       | Error      | | Total      | numbers | of probes | failed due | to  |
| internal            | errr in transmission. |            | |            |         |           |            |     |
| Command History     |                       |            |              |         |           |            |     |
| Release             |                       |            | Modification |         |           |            |     |
| 10.07orearlier      |                       |            | --           |         |           |            |     |
| Command Information |                       |            |              |         |           |            |     |
| Platforms           | Command               | context    | Authority    |         |           |            |     |
8320 Administratorsorlocalusergroupmemberswithexecutionrights
Operator(>)orManager
| 8325 | (#) |     | forthiscommand. |     |     |     |     |
| ---- | --- | --- | --------------- | --- | --- | --- | --- |
8360
9300
10000
start-test
start-test
Description
StartstheIP-SLAprobes.
Examples
| switch(config)#             | ip-sla  | test       |              |           |     |     |     |
| --------------------------- | ------- | ---------- | ------------ | --------- | --- | --- | --- |
| switch(config-ip-sla-test)# |         | start-test |              |           |     |     |     |
| Command History             |         |            |              |           |     |     |     |
| Release                     |         |            | Modification |           |     |     |     |
| 10.07orearlier              |         |            | --           |           |     |     |     |
| Command Information         |         |            |              |           |     |     |     |
| Platforms                   | Command | context    |              | Authority |     |     |     |
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand. |     |     |     |
| ---- | --- | --- | --- | ------------------------------ | --- | --- | --- |
8360
9300
10000
stop-test
stop-test
56
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- | --- | --- | --- |

Description
StopstheIP-SLAprobes.
Examples
| switch(config)#             | ip-sla  | test      |     |
| --------------------------- | ------- | --------- | --- |
| switch(config-ip-sla-test)# |         | stop-test |     |
| Command                     | History |           |     |
Release Modification
10.07orearlier --
| Command   | Information |         |           |
| --------- | ----------- | ------- | --------- |
| Platforms | Command     | context | Authority |
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | ------------------------------ |
8360
9300
10000
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
| <PORT-NUM>                  |     |              | DestinationportfortheIP-SLA.Range:1to65535. |
| --------------------------- | --- | ------------ | ------------------------------------------- |
| [source {<SOURCE-IPV4-ADDR> |     | | <IFNAME>}] |                                             |
SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
| [source-port | <PORT-NUM>]             |     | SpecifiestheportfortheIP-SLAtest. |
| ------------ | ----------------------- | --- | --------------------------------- |
| [name-server | <IPV4-ADDR-DNS-SERVER>] |     |                                   |
SpecifiestheDNSserverfordestinationhostname
resolution.
[probe-interval <PROBE-INTERVAL>] Probeintervalinseconds.Range:30to604800.
Examples
IP-SLA|57

| switch(config-ipsla-1)# |     | tcp-connect | 2.2.2.2 | 8080 |     |     |
| ----------------------- | --- | ----------- | ------- | ---- | --- | --- |
switch(config-ipsla-1)#
|     |     |     | tcp-connect | 2.2.2.2 8080 | source 2.2.2.1 | source-port |
| --- | --- | --- | ----------- | ------------ | -------------- | ----------- |
6000
switch(config-ipsla-1)# tcp-connect 2.2.2.2 8080 source 1/1/1 source-port
6000
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
| source 2.2.2.1 | source-port | 6000 |     |     |     |     |
| -------------- | ----------- | ---- | --- | --- | --- | --- |
switch(config-ipsla-1)# tcp-connect https://device.arubanetworks.com 8080
| source 1/1/1 | source-port | 6000 |     |     |     |     |
| ------------ | ----------- | ---- | --- | --- | --- | --- |
switch(config-ipsla-1)#
|                     |            |         | tcp-connect  | https://device.arubanetworks.com |     | 8080 |
| ------------------- | ---------- | ------- | ------------ | -------------------------------- | --- | ---- |
| name-server         | 10.10.10.2 |         |              |                                  |     |      |
| Command History     |            |         |              |                                  |     |      |
| Release             |            |         | Modification |                                  |     |      |
| 10.07orearlier      |            |         | --           |                                  |     |      |
| Command Information |            |         |              |                                  |     |      |
| Platforms           | Command    | context |              | Authority                        |     |      |
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
8325
8360
9300
10000
udp-echo
udp-echo {<DEST-IPV4-ADDR>|<HOSTNAME>} <PORT-NUM> [source {<SOURCE-IPV4-ADDR> |
<IFNAME>} [source-port <PORT-NUM>]] [name-server <IPV4-ADDR-DNS-SERVER>] [payload-
size
<PAYLOAD-SIZE>] [tos <TYPE-OF-SERVICE>] [probe-interval <PROBE-INTERVAL>]
Description
ConfiguresUDPechoastheIP-SLAtestmechanism.Requiresdestinationaddress/hostnameand
destinationportnumberfortheIP-SLAofudp-echoSLAtype.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
{<DEST-IPV4-ADDR> | <HOSTNAME>} SelectsthedestinationIPv4addressfortheIP-SLAor
thehostnameofthedestination.
| <PORT-NUM> |     |     |     | SpecifiesthedestinationportfortheIP-SLA.Range:1 |     |     |
| ---------- | --- | --- | --- | ----------------------------------------------- | --- | --- |
to65535.
[source {<SOURCE-IPV4-ADDR> | <IFNAME>}] SelectsthesourceIPv4addressforSLAprobesorthe
sourceinterfacetouseforsendingIP-SLAprobes.
| [source-port | <PORT-NUM>] |     |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- | --- |
SpecifiessourceportfortheIP-SLAtest.Range:1to
65535.
58
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
[name-server <IPV4-ADDR-DNS-SERVER>] SpecifiestheDNSserverfordestinationhostname
resolution.
[payload-size <PAYLOAD-SIZE>] SpecifiesthepayloadsizeofanSLAprobe.Range:28
to1440.
[<TYPE-OF-SERVICE>]
Typeofservice.Range:0to255.
probe-interval <PROBE-INTERVAL> Probeintervalinseconds.Range:5to604800.
Examples
| switch(config-ipsla-1)# |     | udp-echo 2.2.2.2 | 8080        |         |
| ----------------------- | --- | ---------------- | ----------- | ------- |
| switch(config-ipsla-1)# |     | udp-echo 2.2.2.2 | 8080 source | 2.2.2.1 |
switch(config-ipsla-1)#
|                         |     | udp-echo https://device.arubanetworks.com |             | 8080  |
| ----------------------- | --- | ----------------------------------------- | ----------- | ----- |
| switch(config-ipsla-1)# |     | udp-echo 2.2.2.2                          | 8080 source | 1/1/1 |
switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 2.2.2.1 payload-size 50
switch(config-ipsla-1)# udp-echo 2.2.2.2 8080 source 1/1/1 payload-size 50
| switch(config-ipsla-1)# |     | udp-echo 2.2.2.2 | 8080 payload-size | 50  |
| ----------------------- | --- | ---------------- | ----------------- | --- |
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080 source
2.2.2.1
| payload-size |     | 50  |     |     |
| ------------ | --- | --- | --- | --- |
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080 source
1/1/1
| payload-size |     | 50  |     |     |
| ------------ | --- | --- | --- | --- |
switch(config-ipsla-1)# udp-echo https://device.arubanetworks.com 8080
| name-server         | 10.10.10.2 |              |           |     |
| ------------------- | ---------- | ------------ | --------- | --- |
| Command History     |            |              |           |     |
| Release             |            | Modification |           |     |
| 10.07orearlier      |            | --           |           |     |
| Command Information |            |              |           |     |
| Platforms           | Command    | context      | Authority |     |
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | ------------------------------ | --- |
8360
9300
10000
udp-jitter-voip
udp-jitter-voip {<DEST-IPV4-ADDR> | <HOSTNAME>} <PORT-NUM> [codec-type <CODEC-TYPE>]
[advantage-factor <VALUE>] [source {<SOURCE-IPV4-ADDR> | <IFNAME>} [source-port
<PORT-NUM>]]
[name-server <IPV4-ADDR-DNS-SERVER>][probe-interval <PROBE-INTERVAL>] [tos <TYPE-OF-
SERVICE>]
Description
IP-SLA|59

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
[source-port <PORT-NUM>] SpecifiesthevalueofsourceportfortheIP-SLA
probes.
| [name-server | <IPV4-ADDR-DNS-SERVER>] |     |     |
| ------------ | ----------------------- | --- | --- |
SpecifiestheDNSserverfordestinationhostname
resolution.
tos <TYPE-OF-SERVICE> Specifiesthetypeofservice.Range:0to255.
probe-interval <PROBE-INTERVAL> Specifiestheprobeintervalinseconds.Range:120to
604800.
Examples
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10 codec-
type g711a
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10
| codec-type | g711a source | 2.2.2.1 |     |
| ---------- | ------------ | ------- | --- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
| advantage-factor | 10 codec-type | g711a |     |
| ---------------- | ------------- | ----- | --- |
switch(config-ipsla-1)# udp-jitter-voip 2.2.2.2 8080 advantage-factor 10
| codec-type | g711a source | 1/1/1 |     |
| ---------- | ------------ | ----- | --- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
| advantage-factor | 10 codec-type | g711a source | 2.2.2.1 |
| ---------------- | ------------- | ------------ | ------- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
| advantage-factor | 10 codec-type | g711a source | 1/1/1 |
| ---------------- | ------------- | ------------ | ----- |
switch(config-ipsla-1)# udp-jitter-voip https://device.arubanetworks.com 8080
advantage-factor 10 codec-type g711a name-server 10.10.10.2 probe-interval 120
| source 10.1.1.1 | source-port | 8888 tos 10 |     |
| --------------- | ----------- | ----------- | --- |
| Command         | History     |             |     |
Release Modification
10.07orearlier --
| Command | Information |     |     |
| ------- | ----------- | --- | --- |
60
AOS-CX10.11MonitoringGuide| (83xx,9300,10000SwitchSeries)

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
8360
9300
10000
vrf
vrf <VRF-NAME>
no vrf [<VRF-NAME>]
Description
ConfigurestheVRFonwhichtheSLAwillsendorreceivepackets.Bydefault,thedefaultVRFisused.
ThenoformofthecommandremovesVRFfromSLA.
| Parameter  |     |     | Description                               |     |
| ---------- | --- | --- | ----------------------------------------- | --- |
| <VRF-NAME> |     |     | SpecifiesaVRFname.Length:Default:default. |     |
Examples
| switch(config-ip-sla-test)# |         | vrf     | ipslasrc     |           |
| --------------------------- | ------- | ------- | ------------ | --------- |
| switch(config-ip-sla-test)# |         | no      | vrf          |           |
| Command History             |         |         |              |           |
| Release                     |         |         | Modification |           |
| 10.07orearlier              |         |         | --           |           |
| Command Information         |         |         |              |           |
| Platforms                   | Command | context |              | Authority |
8320 config-ip-sla-<IP-SLA-NAME> Administratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
8360
9300
10000
| show interface |                       |     |        |             |
| -------------- | --------------------- | --- | ------ | ----------- |
| show interface | [<IFNNAME>|<IFRANGE>] |     | [brief | | physical] |
show interface [<IFNNAME>|<IFRANGE>] [extended [non-zero] | [human-readable]]
| show interface | [<IFNNAME>] | monitor | [human-readable] |     |
| -------------- | ----------- | ------- | ---------------- | --- |
show interface [lag | loopback | tunnel | vlan ] [<ID>] [brief]
show interface lag [<LAG-ID>] [extended [non-zero] | [human-readable]]
| show interface | lag [<LAG-ID>]   | monitor | [human-readable] |     |
| -------------- | ---------------- | ------- | ---------------- | --- |
| show interface | vxlan <VXLAN-ID> | [brief  | | physical]      |     |
IP-SLA|61

| show interface | vxlan <VXLAN-ID> | [brief | | physical] |     |
| -------------- | ---------------- | ------ | ----------- | --- |
Description
Showsactiveconfigurationsandoperationalstatusinformationforinterfaces.
| Parameter |     | Description                                    |     |     |
| --------- | --- | ---------------------------------------------- | --- | --- |
| <IFNAME>  |     | Specifiesainterfacename.                       |     |     |
| <IFRANGE> |     | Specifiestheportidentifierrange.               |     |     |
| brief     |     | Showsbriefinfointabularformat.                 |     |     |
| physical  |     | Showsthephysicalconnectioninfointabularformat. |     |     |
| extended  |     | Showsadditionalstatistics.                     |     |     |
human-readable Showsstatisticsroundedtothenearestpowerof1000,for
example,1K,345M,2G.ThisisavailableonlyintheCLI interface
output.
non-zero
Showsonlynonzerostatistics.
| LAG |     | ShowsLAGinterfaceinformation. |     |     |
| --- | --- | ----------------------------- | --- | --- |
monitor
Continuouslymonitorinterfacestatistics.
| LOOPBACK |     | Showsloopbackinterfaceinformation. |     |     |
| -------- | --- | ---------------------------------- | --- | --- |
TUNNEL
Showstunnelinterfaceinformation.
| VLAN |     | ShowsVLANinterfaceinformation. |     |     |
| ---- | --- | ------------------------------ | --- | --- |
<LAG-ID>
SpecifiestheLAGnumber.Range:1-256
| <LOOPBACK-ID> |     | SpecifiestheLOOPBACKnumber.Range:0-255 |     |     |
| ------------- | --- | -------------------------------------- | --- | --- |
<TUNNEL-ID>
SpecifiesthetunnelID.Range:1-255
| <VLAN-ID> |     | SpecifiestheVLANID.Range:1-4094 |     |     |
| --------- | --- | ------------------------------- | --- | --- |
VXLAN
ShowstheVXLANinterfaceinformation.
| <VXLAN-ID> |     | SpecifiestheVXLANinterfaceidentifier.Default:1 |     |     |
| ---------- | --- | ---------------------------------------------- | --- | --- |
Examples
Showinginterfaceinformationwhenitisconfiguredasaroute-onlyport(thepersonaitemisonly
availableonthe10000SwitchSeries):
| switch#           | show interface | 1/1/1             |                 |           |
| ----------------- | -------------- | ----------------- | --------------- | --------- |
| Interface         | 1/1/1 is up    |                   |                 |           |
| Admin state       | is up          |                   |                 |           |
| Link state:       | up for         | 2 days (since Sun | Jun 21 05:30:22 | UTC 2020) |
| Link transitions: | 1              |                   |                 |           |
| Description:      | backup         | data center link  |                 |           |
| Persona:          | access         |                   |                 |           |
62
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- |

| Hardware: | Ethernet, | MAC | Address: | 70:72:cf:fd:e7:b4 |     |     |     |     |
| --------- | --------- | --- | -------- | ----------------- | --- | --- | --- | --- |
MTU 1500
Type 1GbT
Full-duplex
| qos trust        | none |             |     |         |     |     |       |         |
| ---------------- | ---- | ----------- | --- | ------- | --- | --- | ----- | ------- |
| Speed 1000       | Mb/s |             |     |         |     |     |       |         |
| Auto-negotiation |      | is on       |     |         |     |     |       |         |
| Flow-control:    |      | off         |     |         |     |     |       |         |
| Error-control:   |      | off         |     |         |     |     |       |         |
| MDI mode:        | MDIX |             |     |         |     |     |       |         |
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
ShowinginformationwhentheinterfaceisshutdownduringaVSX split(thepersonaitemisonly
availableonthe10000SwitchSeries):
| switch(config-if)# |       | show     | interface | 1/1/1  |     |     |     |     |
| ------------------ | ----- | -------- | --------- | ------ | --- | --- | --- | --- |
| Interface          | 1/1/1 | is down  |           |        |     |     |     |     |
| Admin state        | is    | up       |           |        |     |     |     |     |
| State information: |       | Disabled |           | by VSX |     |     |     |     |
Link state: down for 3 days (since Tue Mar 16 05:20:47 UTC 2021)
IP-SLA|63

| Link transitions: |     | 0   |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:
| Persona:  | access    |     |          |                   |     |     |     |     |     |
| --------- | --------- | --- | -------- | ----------------- | --- | --- | --- | --- | --- |
| Hardware: | Ethernet, | MAC | Address: | 04:09:73:62:90:e7 |     |     |     |     |     |
MTU 1500
Type SFP+DAC3
Full-duplex
| qos trust        | none            |                 |     |         |     |     |       |         |     |
| ---------------- | --------------- | --------------- | --- | ------- | --- | --- | ----- | ------- | --- |
| Speed 0          | Mb/s            |                 |     |         |     |     |       |         |     |
| Auto-negotiation |                 | is off          |     |         |     |     |       |         |     |
| Flow-control:    |                 | off             |     |         |     |     |       |         |     |
| Error-control:   |                 | off             |     |         |     |     |       |         |     |
| VLAN Mode:       | native-untagged |                 |     |         |     |     |       |         |     |
| Native           | VLAN:           | 1               |     |         |     |     |       |         |     |
| Allowed          | VLAN            | List: 1502-1505 |     |         |     |     |       |         |     |
| Rate collection  |                 | interval:       | 300 | seconds |     |     |       |         |     |
| Rate             |                 |                 |     | RX      |     | TX  | Total | (RX+TX) |     |
---------------- -------------------- -------------------- --------------------
| Mbits /     | sec |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| ----------- | --- | --- | --- | ---- | --- | ---- | --- | ----- | ---- |
| KPkts /     | sec |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Unicast     |     |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Multicast   |     |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Broadcast   |     |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Utilization |     |     |     | 0.00 |     | 0.00 |     |       | 0.00 |
| Statistic   |     |     |     | RX   |     | TX   |     | Total |      |
---------------- -------------------- -------------------- --------------------
| Packets      |     |     |     | 0   |     | 0   |     |     | 0   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unicast      |     |     |     | 0   |     | 0   |     |     | 0   |
| Multicast    |     |     |     | 0   |     | 0   |     |     | 0   |
| Broadcast    |     |     |     | 0   |     | 0   |     |     | 0   |
| Bytes        |     |     |     | 0   |     | 0   |     |     | 0   |
| Jumbos       |     |     |     | 0   |     | 0   |     |     | 0   |
| Dropped      |     |     |     | 0   |     | 0   |     |     | 0   |
| Pause Frames |     |     |     | 0   |     | 0   |     |     | 0   |
| Errors       |     |     |     | 0   |     | 0   |     |     | 0   |
| CRC/FCS      |     |     |     | 0   |     | n/a |     |     | 0   |
| Collision    |     |     |     | n/a |     | 0   |     |     | 0   |
| Runts        |     |     |     | 0   |     | n/a |     |     | 0   |
| Giants       |     |     |     | 0   |     | n/a |     |     | 0   |
Showingthemonitorinformation:
Inmonitormode,theCLI refreshesdataautomaticallyuntilitisexitedbyenteringq.Pressing?opensthehelp
menutodisplaywhichoptionsareavailableinthiscontext.
| switch(config-if)# |       | show  | interface | 1/1/1 monitor |     |     |       |         |     |
| ------------------ | ----- | ----- | --------- | ------------- | --- | --- | ----- | ------- | --- |
| Interface          | 1/1/1 | is up |           |               |     |     |       |         |     |
| Rate               |       |       |           | RX            |     | TX  | Total | (RX+TX) |     |
---------------- -------------------- -------------------- --------------------
| MBits /     | sec |     |     | 30196.43 | 30196.43 |       |     | 60392.85  |      |
| ----------- | --- | --- | --- | -------- | -------- | ----- | --- | --------- | ---- |
| MPkts /     | sec |     |     | 58977.39 | 58977.40 |       |     | 117954.79 |      |
| Unicast     |     |     |     | 0.00     |          | 0.00  |     |           | 0.00 |
| Multicast   |     |     |     | 58977.39 | 58977.40 |       |     | 117954.79 |      |
| Broadcast   |     |     |     | 0.00     |          | 0.00  |     |           | 0.00 |
| Utilization | %   |     |     | 75.49    |          | 75.49 |     | 150.98    |      |
64
AOS-CX10.11MonitoringGuide| (83xx,9300,10000SwitchSeries)

| Statistic |     |     |     | RX  |     | TX  | Total | (RX+TX) |
| --------- | --- | --- | --- | --- | --- | --- | ----- | ------- |
---------------- -------------------- -------------------- --------------------
| Packets   |                |            | 4756527649   |     | 4756527865   |     | 9513055514   |            |
| --------- | -------------- | ---------- | ------------ | --- | ------------ | --- | ------------ | ---------- |
| Unicast   |                |            |              | 0   |              | 0   |              | 0          |
| Multicast |                |            | 4756527649   |     | 4756527865   |     | 9513055514   |            |
| Broadcast |                |            |              | 2   |              | 0   |              | 2          |
| Bytes     |                |            | 304417778668 |     | 304417795428 |     | 608835574096 |            |
| Jumbos    |                |            |              | 0   |              | 0   |              | 0          |
| Dropped   |                |            |              | 0   | 19028847730  |     | 19028847730  |            |
| Pause     | Frames         |            |              | 0   |              | 0   |              | 0          |
| Errors    |                |            |              | 0   |              | 0   |              | 0          |
| CRC/FCS   |                |            |              | 0   |              | n/a |              | 0          |
|           |                |            |              |     |              |     | help:        | ?, quit: q |
| Help for  | Interface      | Monitor    |              |     |              |     |              |            |
| h Toggle  | human-readable |            | mode         |     |              |     |              |            |
| c Clear   | interface      | statistics |              |     |              |     |              |            |
| Does      | not apply      | to         | rates        |     |              |     |              |            |
| Arrows,   | PgUp, PgDn,    | Home,      | End          |     |              |     |              |            |
| Navigate  | interface      |            | statistics   |     |              |     |              |            |
Delay: 2
|     |     |     |     |     |     |     | help: | ?, quit: q |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- |
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
| Packets   |     |     |     | 577K |     | 577K |     | 1M  |
| --------- | --- | --- | --- | ---- | --- | ---- | --- | --- |
| Unicast   |     |     |     | 577K |     | 577K |     | 1M  |
| Multicast |     |     |     | 0    |     | 51   |     | 51  |
| Broadcast |     |     |     | 0    |     | 15   |     | 15  |
| Bytes     |     |     |     | 744M |     | 745M |     | 1G  |
| Jumbos    |     |     |     | 0    |     | 0    |     | 0   |
IP-SLA|65

| Dropped      |     |     | 0   | 0   | 0   |
| ------------ | --- | --- | --- | --- | --- |
| Filtered     |     |     | 0   | 0   | 0   |
| Pause Frames |     |     | 0   | 0   | 0   |
| Errors       |     |     | 0   | 0   | 0   |
| CRC/FCS      |     |     | 0   | n/a | 0   |
| Collision    |     |     | n/a | 0   | 0   |
| Runts        |     |     | 0   | n/a | 0   |
| Giants       |     |     | 0   | n/a | 0   |
...
| Command History |     |     |              |     |     |
| --------------- | --- | --- | ------------ | --- | --- |
| Release         |     |     | Modification |     |     |
10.11
Addedmonitorparameter.
| 10.10               |         |         | Addedhuman-readableparameter.                    |     |     |
| ------------------- | ------- | ------- | ------------------------------------------------ | --- | --- |
| 10.09               |         |         | Addedpersonainformationforthe10000 SwitchSeries. |     |     |
| 10.07orearlier      |         |         | --                                               |     |     |
| Command Information |         |         |                                                  |     |     |
| Platforms           | Command | context | Authority                                        |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
66
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- | --- |

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

AOS-CX 10.11 Monitoring Guide | (83xx, 9300, 10000 Switch Series)

67

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
| clear mirror | endpoint |     |     |
| ------------ | -------- | --- | --- |
Mirroring|68

AppliesonlytotheAruba8360SwitchSeries.
| clear mirror | endpoint | [<NAME>] |     |
| ------------ | -------- | -------- | --- |
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
| switch#             | clear mirror | endpoint test |              |
| ------------------- | ------------ | ------------- | ------------ |
| Command History     |              |               |              |
| Release             |              |               | Modification |
| 10.07orearlier      |              |               | --           |
| Command Information |              |               |              |
| Platforms           | Command      | context       | Authority    |
8360 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
|     | (#) |     | forthiscommand. |
| --- | --- | --- | --------------- |
comment
comment <COMMENT>
no comment
Description
Specifiesacommentforthemirroringsession.
Whenusedinmirrorendpointcommandcontext,specifiesacommentforthemirrorendpoint.
Thenoformofthiscommandremovesthecomment.
69
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | ----------------------------- | --- | --- |

Parameter Description
<COMMENT> Acommentstringofupto64characterscomposedofletters,
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
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
|     | config-mirror-endpoint |     | executionrightsforthiscommand. |
| --- | ---------------------- | --- | ------------------------------ |
copy tcpdump-pcap
| copy tcpdump-pcap | <FILE-NAME> | <REMOTE-URL> |     |
| ----------------- | ----------- | ------------ | --- |
Description
Savespacketcapturefilestoexternalstorage.
Mirroring|70

| Parameter   |     |     | Description                          |     |     |     |
| ----------- | --- | --- | ------------------------------------ | --- | --- | --- |
| <FILE-NAME> |     |     | Specifiesthepacketcapturefiletosave. |     |     |     |
<REMOTE-URL> Specifiestheexternalstoragetowhichthepacketcapturefilewill
besaved.
Usage
Onlyfourfilescanbesavedatanypointontheswitch.Packetcapturefilesarenotsavedafterafailover
| orreboot.Viewalistofsavedfilesusingdiag |     |     | utilities | list-files. |     |     |
| --------------------------------------- | --- | --- | --------- | ----------- | --- | --- |
Examples
Savingmy_capture_file.pcaptosftp://root@10.0.0.2/file.pcap:
switch# copy tcpdump-pcap my_capture_file.pcap sftp://root@10.0.0.2/file.pcap
| root@10.0.0.2's      | passowrd:            |         |                    |          |           |       |
| -------------------- | -------------------- | ------- | ------------------ | -------- | --------- | ----- |
| Connected            | to 10.0.0.2.         |         |                    |          |           |       |
| sftp > put           | my_capture_file.pcap |         | file.pcap          |          |           |       |
| Uploading            | my_capture_file.pcap |         | to /root/file.pcap |          |           |       |
| my_capture_file.pcap |                      |         |                    | 100% 156 | 219.8KB/s | 00:00 |
| Copied               | successfuly.         |         |                    |          |           |       |
| Command              | History              |         |                    |          |           |       |
| Release              |                      |         | Modification       |          |           |       |
| 10.08                |                      |         | Commandintroduced  |          |           |       |
| Command              | Information          |         |                    |          |           |       |
| Platforms            | Command              | context | Authority          |          |           |       |
8320 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --------------- | --- | --- | --- |
8360
9300
10000
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
71
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- | --- | --- |

Example
CopyingthecapturedatatoafileonSFTPserver10.0.0.2:
switch#
|                 | copy tshark-pcap | sftp://root@10.0.0.2/file.pcap |              |          |           |       |
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
| 8325 |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --------------- | --- | --- | --- |
8360
9300
10000
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
| switch#                  | config |             |     |     |     |     |
| ------------------------ | ------ | ----------- | --- | --- | --- | --- |
| switch(config)#          | mirror | session     | 1   |     |     |     |
| switch(config-mirror-1)# |        | destination | cpu |     |     |     |
Removingthedestinationentirely.
Mirroring|72

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
| Parameter      |     |     |     |     | Description                                    |     |
| -------------- | --- | --- | --- | --- | ---------------------------------------------- | --- |
| <INTERFACE-ID> |     |     |     |     | Specifiesainterface.Format:member/slot/port.   |     |
| <LAG-NAME>     |     |     |     |     | SpecifiesaLAG(linkaggregationgroup)identifier. |     |
Usage
Supportedmirrordestinations:Layer2orLayer3Ethernetports,LAGs,orCPUasaMirrorDestination.
AportthatisalreadyamemberofaLAGisnotavalidmirrordestination.
Configuringadifferentdestinationinterfaceinanenabledmirroringsessioncausesallmirroredtraffic
tousethenewdestinationinterface.Thisactionmightcauseatemporarysuspensionofmirrored
sourcetrafficduringthereconfiguration.
Examples
Configuringamirroringsessionandaddinganinterfaceasadestination:
| switch(config)#          |     | mirror | session     | 1   |           |       |
| ------------------------ | --- | ------ | ----------- | --- | --------- | ----- |
| switch(config-mirror-1)# |     |        | destination |     | interface | 1/1/1 |
Replacingtheexistingdestinationwithdifferentinterface:
| switch(config-mirror-1)# |     |     | destination |     | interface | 1/1/12 |
| ------------------------ | --- | --- | ----------- | --- | --------- | ------ |
Removingadestination:
73
| AOS-CX10.11MonitoringGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

| switch(config-mirror-1)# |     | no destination | interface | 1/1/12 |
| ------------------------ | --- | -------------- | --------- | ------ |
Switch Destination interface limit per mirror session (4 possible sessions)
| 8320           | 1           |              |           |     |
| -------------- | ----------- | ------------ | --------- | --- |
| 8325           | 1           |              |           |     |
| 8360           | 64          |              |           |     |
| 9300           | 1           |              |           |     |
| 10000          | 1           |              |           |     |
| Command        | History     |              |           |     |
| Release        |             | Modification |           |     |
| 10.07orearlier |             | --           |           |     |
| Command        | Information |              |           |     |
| Platforms      | Command     | context      | Authority |     |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
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
Mirroring|74

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

AOS-CX 10.11 Monitoring Guide | (83xx, 9300, 10000 Switch Series)

75

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
8320 config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | ------------------------------ | --- |
8360
9300
10000
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
| switch#        | diagnostic          |                     |              |            |
| -------------- | ------------------- | ------------------- | ------------ | ---------- |
| switch#        | diagnostic          | utilities tshark    | file         |            |
| Inspecting     | traffic             | mirrored to the CPU | until Ctrl-C | is entered |
| ^CEnding       | traffic inspection. |                     |              |            |
| Command        | History             |                     |              |            |
| Release        |                     | Modification        |              |            |
| 10.07orearlier |                     | --                  |              |            |
| Command        | Information         |                     |              |            |
Mirroring|76

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
77
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | ----------------------------- | --- | --- |

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

Mirroring | 78

switch# diag utilities tcpdump delete-file my_capture_file.pcap
| Successfully        | removed | file    |                   |     |
| ------------------- | ------- | ------- | ----------------- | --- |
| Command History     |         |         |                   |     |
| Release             |         |         | Modification      |     |
| 10.08               |         |         | Commandintroduced |     |
| Command Information |         |         |                   |     |
| Platforms           | Command | context | Authority         |     |
8320 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
9300
10000
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
79
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- |

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
Mirroring|80

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
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| mirror endpoint |     |     |     |
| --------------- | --- | --- | --- |
AppliesonlytotheAruba8360SwitchSeries.
| mirror endpoint    | <NAME> |     |     |
| ------------------ | ------ | --- | --- |
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
Examples
Creatingamirrorendpointnamedtest:
81
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | ----------------------------- | --- | --- |

| switch(config)# |     | mirror | endpoint | test |
| --------------- | --- | ------ | -------- | ---- |
Deletingmirrorendpointnamedtest
| switch(config)# |             | no mirror | endpoint | test         |
| --------------- | ----------- | --------- | -------- | ------------ |
| Command         | History     |           |          |              |
| Release         |             |           |          | Modification |
| 10.07orearlier  |             |           |          | --           |
| Command         | Information |           |          |              |
| Platforms       | Command     |           | context  | Authority    |
8360 config Administratorsorlocalusergroupmemberswithexecutionrights
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
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
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
Mirroring|82

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
| Command        | History     |     |              |     |
| -------------- | ----------- | --- | ------------ | --- |
| Release        |             |     | Modification |     |
| 10.07orearlier |             |     | --           |     |
| Command        | Information |     |              |     |
83
AOS-CX10.11MonitoringGuide| (83xx,9300,10000SwitchSeries)

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show mirror | endpoint |     |     |     |
| ----------- | -------- | --- | --- | --- |
AppliesonlytotheAruba8360SwitchSeries.
| show mirror | endpoint [<NAME>] |     |     |     |
| ----------- | ----------------- | --- | --- | --- |
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
| switch#             | show mirror       | endpoint audit |              |                  |
| ------------------- | ----------------- | -------------- | ------------ | ---------------- |
| Mirror Endpoint:    | audit             |                |              |                  |
| Admin Status:       | enable            |                |              |                  |
| Operation           | Status:           | enabled        |              |                  |
| Comment:            | Mirror Endpoint   | Audit          |              |                  |
| Type: gre           |                   |                |              |                  |
| Tunnel:             | source 1.1.1.1    | destination    | 1.1.1.2      | id 1 vrf default |
| Interface:          | 1/1/1-1/1/10,lag1 |                |              |                  |
| Output Packets:     | 123456789         |                |              |                  |
| Output Bytes:       | 8912345678        |                |              |                  |
| Command History     |                   |                |              |                  |
| Release             |                   |                | Modification |                  |
| 10.07orearlier      |                   |                | --           |                  |
| Command Information |                   |                |              |                  |
Mirroring|84

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8360 Administratorsorlocalusergroupmemberswithexecutionrights
Operator(>)orManager
|     | (#) |     | forthiscommand. |
| --- | --- | --- | --------------- |
shutdown
AppliesonlytotheAruba8360SwitchSeries.
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
| switch(config)# | mirror | endpoint | test |
| --------------- | ------ | -------- | ---- |
switch(config-mirror-endpoint-test)#
no shutdown
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
8360 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
source
AppliesonlytotheAruba8360SwitchSeries.
85
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |
| --------------------------- | ----------------------------- | --- | --- |

source <SOURCE-IP> destination <DESTINATION-IP> id <1-4294967295> [vrf <VRF_NAME>] [type
{gre}]
no source
Description
Configurestunnelparametersofthemirrorendpoint.Configuringatunnelparametertoamirror
endpointwillreplacetheexistingconfiguration.BydefaulttheVRFisdefault,userscanalsoexplicitly
provideacustomVRF.ThedefaulttunneltypeisconsideredtobeGREandusersalsohavetheoptionto
explicitlygivetypeasGRE.
Thenoformremovesthetunnelparametersofthemirrorendpoint.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<SOURCE-IP> SpecifiesL3encapsulatedIPv4sourceintheformA.B.C.D.
<DESTINATION-IP>
SpecifiesL3encapsulatedIPv4destinationintheformA.B.C.D.
| id  |     |     |     |     | Specifiestunnelidentifierfromtheencapsulatedpacket. |     |     |     |
| --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
<VRF_NAME>
SpecifiesthenameofVRF forwhichthetunnelbelongsto.
Examples
Configuringatunnelparametertoamirrorendpoint:
switch(config-mirror-endpoint-test)#
|                |             |         |         |     | source 1.1.1.1 | destination | 7.7.7.7 | id 1 vrf |
| -------------- | ----------- | ------- | ------- | --- | -------------- | ----------- | ------- | -------- |
| default        | type        | gre     |         |     |                |             |         |          |
| Command        | History     |         |         |     |                |             |         |          |
| Release        |             |         |         |     | Modification   |             |         |          |
| 10.07orearlier |             |         |         |     | --             |             |         |          |
| Command        | Information |         |         |     |                |             |         |          |
| Platforms      |             | Command | context |     | Authority      |             |         |          |
8360 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| source    | interface |             |     |               |               |     |     |     |
| --------- | --------- | ----------- | --- | ------------- | ------------- | --- | --- | --- |
| source    | interface | {<PORT-NUM> |     | | <LAG-NAME>} | [<DIRECTION>] |     |     |     |
| no source | interface | {<PORT-NUM> |     | | <LAG-NAME>} | [<DIRECTION>] |     |     |     |
Description
Configuresthespecifiedinterface(eitheranEthernetportoraLAG)asasourceoftraffictobemirrored.
Thenoformofthiscommandceasesmirroringtrafficfromthespecifiedsourceinterfaceandremoves
thesourceinterfacefromthemirroringsessionconfiguration.
Mirroring|86

| Parameter  |     | Description                                    |     |     |
| ---------- | --- | ---------------------------------------------- | --- | --- |
| <PORT-NUM> |     | Specifiesaphysicalportontheswitch.Usetheformat |     |     |
member/slot/port(forexample,1/3/1).
<LAG-NAME> SpecifiestheidentifierfortheLAG(linkaggregationgroup).
<DIRECTION> Selectsthedirectionoftraffictobemirroredfromthissource
interface.Thereisnodefaultforthisparameter.Validvaluesare
thefollowing:
both
Mirrorbothtransmittedandreceivedpackets.
| rx  |     | Mirroronlyreceivedpackets. |     |     |
| --- | --- | -------------------------- | --- | --- |
tx
Mirroronlytransmittedpackets.
Usage
Thereisalimitofsourceinterfacesineachdirectionofagivenmirrorsession:
|     |     | Source | interface limit per mirror | session (4 |
| --- | --- | ------ | -------------------------- | ---------- |
Switch
|       |     | possible | sessions) |     |
| ----- | --- | -------- | --------- | --- |
| 8320  |     | 128      |           |     |
| 8325  |     | 128      |           |     |
| 8360  |     | 64       |           |     |
| 9300  |     | 128      |           |     |
| 10000 |     | 72       |           |     |
However,thereisapracticallimittotheamountoftrafficthatamirrordestinationcantransmit.For
example,mirroringsessionwithmultiple10Gsourcescanoverwhelmasingle10Gdestination.
Youcanconfigurethesamesourceinterfaceinmultiplemirroringsessions,ifrequired.
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
87
AOS-CX10.11MonitoringGuide| (83xx,9300,10000SwitchSeries)

| switch(config)# | mirror | session | 1   |     |
| --------------- | ------ | ------- | --- | --- |
switch(config-mirror-1)#
|     |     | source | interface | 1/1/1 both |
| --- | --- | ------ | --------- | ---------- |
Creatingasecondmirroringsessionandconfiguringtwosourceinterfaces.Oneportmirroringonly
transmittedpacketsandtheothermirroringbothtransmittedandreceivedpackets:
switch(config)#
|                          | mirror | session | 2         |            |
| ------------------------ | ------ | ------- | --------- | ---------- |
| switch(config-mirror-2)# |        | source  | interface | 1/1/3 tx   |
| switch(config-mirror-2)# |        | source  | interface | 1/2/1 both |
Removingthefirstsourceinterface:
| switch(config-mirror-2)# |     | no  | source interface | 1/2/3 |
| ------------------------ | --- | --- | ---------------- | ----- |
Configuringasourceinterfacetomirrorreceivedpacketsonly:
| switch(config-mirror-3)# |     | source | interface | 1/1/2 rx |
| ------------------------ | --- | ------ | --------- | -------- |
Configuringasourceinterfacetomirrorbothtransmittedandreceivedpackets:
| switch(config-mirror-1)# |     | source | interface | 1/1/1 both |
| ------------------------ | --- | ------ | --------- | ---------- |
ConfiguringaLAGassourceinterfacetomirrorbothtransmittedandreceivedpackets:
| switch(config-mirror-4)# |     | source | interface | lag1 both |
| ------------------------ | --- | ------ | --------- | --------- |
Stoppingthemirroringofreceivedpacketsfromaconfiguredsourceinterface:
| switch(config-mirror-4)# |         | no      | source interface | lag1 rx   |
| ------------------------ | ------- | ------- | ---------------- | --------- |
| Command History          |         |         |                  |           |
| Release                  |         |         | Modification     |           |
| 10.07orearlier           |         |         | --               |           |
| Command Information      |         |         |                  |           |
| Platforms                | Command | context |                  | Authority |
Allplatforms config-mirror-<SESSION-ID> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| source vlan |     |     |     |     |
| ----------- | --- | --- | --- | --- |
AppliesonlytotheAruba8360SwitchSeries.
Mirroring|88

source vlan <VLAN-NUM> {rx | tx | both}
no source vlan <VLAN-NUM> {rx | tx | both}

Description

Mirroring with VLAN as a source is supported in the following traffic directions:

n both - traffic received and transmitted

n rx - only received traffic

n tx - only transmitted traffic

More than one source VLAN can be configured in a mirror session. Each such VLAN may specify its own
direction.

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

AOS-CX 10.11 Monitoring Guide | (83xx, 9300, 10000 Switch Series)

89

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
8360 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Mirroring|90

Chapter 9
|            |          |            | Monitoring | a device | using SNMP |
| ---------- | -------- | ---------- | ---------- | -------- | ---------- |
| Monitoring | a device | using SNMP |            |          |            |
Configuring SNMP:RefertotheSNMP/MIBGuideforinformationonhowtoaddSNMPsoadevicecan
bemonitoredfromanetworkmanagementsystem(NMS).
Configuring an SNMP trap receiver:RefertotheSNMP/MIBGuideandspecificinformationaboutthe
trapcommandtoenableSNMPtraps.
show snmp
91
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- | --- |

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

n The JL720A Aruba 8360-48XT4C models (ordered SKU #s JL706A/JL707A) do not support split ports.

Breakout cable support commands

split
split [<COUNT>][<SPEED>][confirm]
no split [confirm]

Description

Splits a port into multiple interfaces. Only ports capable of supporting breakout cables or SR4/eSR4
optics can be split.

Parameter

<COUNT>

<SPEED>

confirm

Usage

Description

Specifies the number of child interfaces to activate upon splitting
the port. Default: 4.

Specifies the speed for the child interfaces.

Specifies the confirmation of port splitting.

n Some switch interfaces support different split counts depending on the installed transceiver. For

these interfaces, the number of child interfaces to activate can be specified. If omitted, the default is
4. For transceivers capable of supporting multiple split modes, the closest mode with enough lanes is
used.

n Some transceivers also support multiple split modes with different speeds. For example, 2x200G or
2x100G. When a speed is not specified, the highest available speed for the split count is used. To
select a different split mode with a lower speed, the desired speed must be specified.

AOS-CX 10.11 Monitoring Guide | (83xx, 9300, 10000 Switch Series)

92

Whenthecurrenttransceiverdoesnotsupporttheconfiguredsplitspeed,theinterfacewillremaindownwithan
`Invalidspeed`error.
Thesplittableportsforallmodelsareshowninthetablebelow:
| Model | Description |     | Port info |
| ----- | ----------- | --- | --------- |
Aruba8320Series
| n JL479A | Aruba83204810/640X47252Bdl |     | 49-54(40G) |
| -------- | -------------------------- | --- | ---------- |
n JL579A
|     | Aruba83203240GX47252Bdl |     | 5-28(40G-center24ports) |
| --- | ----------------------- | --- | ----------------------- |
n JL581A
|     | Aruba832048T/640X47252Bdl |     | 49-54(40G) |
| --- | ------------------------- | --- | ---------- |
Aruba836032Y4Cmodels
| JL717A(basesystem) | Displayedbyshow | system |     |
| ------------------ | --------------- | ------ | --- |
n JL700APort-to-Powermodel Aruba8360-32Y4CPrt2Pwr3F2PSBdl 33-36(40Gor100G)
33-36(40Gor100G)
| n JL701APower-to-Portmodel | Aruba8360-32Y4CPwr2Prt3F2PSBdl |     |     |
| -------------------------- | ------------------------------ | --- | --- |
Aruba836016Y2Cmodels
| JL718A(basesystem) | Displayedbyshow | system |     |
| ------------------ | --------------- | ------ | --- |
n JL702APort-to-Powermodel Aruba8360-16Y2CPrt2Pwr3F2PSBdl 17-18(40Gor100G)
17-18(40Gor100G)
| n JL703APower-to-Portmodel | Aruba8360-16Y2CPwr2Prt3F2PSBdl |     |     |
| -------------------------- | ------------------------------ | --- | --- |
Aruba836048XT4Cmodels
| JL720A(basesystem) | Displayedbyshow | system |     |
| ------------------ | --------------- | ------ | --- |
n JL706APort-to-Powermodel Aruba8360-48XT4CPrt2Pwr3F2PS NOSUPPORTforSplitports
| n JL707APower-to-Portmodel | Bdl                          |     |     |
| -------------------------- | ---------------------------- | --- | --- |
| Aruba8360-12Cmodels        | Aruba8360-48XT4CPwr2Prt3F2PS |     |     |
Bdl
| JL721A(basesystem)         |                 |        | 1-12(40Gor100G) |
| -------------------------- | --------------- | ------ | --------------- |
| n JL708APort-to-Powermodel |                 |        | 1-12(40Gor100G) |
|                            | Displayedbyshow | system |                 |
n JL709APower-to-Portmodel
| Aruba836024XF2Cmodels | Aruba8360-12CPwr2Prt3F2PSBdl |     |                  |
| --------------------- | ---------------------------- | --- | ---------------- |
|                       | Aruba8360-12CPrt2Pwr3F2PSBdl |     | 25-26(40Gor100G) |
JL722A(basesystem)
25-26(40Gor100G)
n JL710APort-to-Powermodel
|     | Displayedbyshow | system |     |
| --- | --------------- | ------ | --- |
n JL711APower-to-Portmodel
Aruba8360-24XF2CPrt2Pwr3F2PS
Bdl
Aruba8360-24XF2CPwr2Pwr3F2PS
Bdl
| Aruba8325 | Aruba8325-48Y8C48p25G8p100G |     | 49-56(40Gor100G) |
| --------- | --------------------------- | --- | ---------------- |
| ( JL635A) | Swch                        |     |                  |
| Aruba8325 | Aruba8325-48Y8CFB6F2PSBdl   |     | 49-56(40Gor100G) |
( JL624A)
| Aruba8325 | Aruba8325-48Y8CBF6F2PSBdl |     | 49-56(40Gor100G) |
| --------- | ------------------------- | --- | ---------------- |
( JL625A)
| Aruba8325 |     |     | 1-32(40Gor100G) |
| --------- | --- | --- | --------------- |
JL626AAruba8325-32CFB6F2PS
( JL626A)
Bdl
Breakoutcablesupport|93

| Model     |     |     | Description |     |     |     | Port            | info |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- | --------------- | ---- | --- | --- |
| Aruba8325 |     |     |             |     |     |     | 1-32(40Gor100G) |      |     |     |
Aruba8325-32CBF6F2PSBdl
( JL627A)
| Aruba8325 |     |     | Aruba8325-32C32p100GSwch |     |     |     | 1-32(40Gor100G) |     |     |     |
| --------- | --- | --- | ------------------------ | --- | --- | --- | --------------- | --- | --- | --- |
(JL636A)
Examples
Beforesplittinganinterface(exampleona8325SeriesSwitch):
| switch(config)# |     | show interface |     | 1/1/56 | brief |     |     |     |     |     |
| --------------- | --- | -------------- | --- | ------ | ----- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
--
| Port | Native | Mode | Type |     | Enabled Status | Reason |     |     | Speed |     |
| ---- | ------ | ---- | ---- | --- | -------------- | ------ | --- | --- | ----- | --- |
| Desc | VLAN   |      |      |     |                |        |     |     |       |     |
----------------------------------------------------------------------------------
--
1/1/56 -- routed QSFP+DA1 no down Administratively down -- --
Aftersplitting:
| switch(config)#    |     | interface | 1/1/56 |     |     |     |     |     |     |     |
| ------------------ | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| switch(config-if)# |     | split     |        |     |     |     |     |     |     |     |
This command will disable the specified port, clear its configuration,
| and split        | it into | multiple | interfaces. |                          |     |     |       |     |     |     |
| ---------------- | ------- | -------- | ----------- | ------------------------ | --- | --- | ----- | --- | --- | --- |
| Continue         | (y/n)?  | y        |             |                          |     |     |       |     |     |     |
| 8325(config-if)# |         | show     | interface   | 1/1/56,1/1/56:1-1/1/56:4 |     |     | brief |     |     |     |
----------------------------------------------------------------------------------
--
| Port | Native | Mode | Type |     | Enabled Status |     | Reason |     | Speed |     |
| ---- | ------ | ---- | ---- | --- | -------------- | --- | ------ | --- | ----- | --- |
Desc
|     | VLAN |     |     |     |     |     |     |     | (Mb/s) |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
----------------------------------------------------------------------------------
--
| 1/1/56   | --  | routed | QSFP+DA1 |     | no down |     | Interface | split | --    | --  |
| -------- | --- | ------ | -------- | --- | ------- | --- | --------- | ----- | ----- | --- |
| 1/1/56:1 | --  | routed | QSFP+DA1 |     | yes up  |     |           |       | 10000 | --  |
| 1/1/56:2 | --  | routed | QSFP+DA1 |     | yes up  |     |           |       | 10000 | --  |
| 1/1/56:3 | --  | routed | QSFP+DA1 |     | yes up  |     |           |       | 10000 | --  |
| 1/1/56:4 | --  | routed | QSFP+DA1 |     | yes up  |     |           |       | 10000 | --  |
Unsplittingaportonaswitchthatdoesnotrequireareboot:
| switch(config)#    |     | interface | 1/1/1 |     |     |     |     |     |     |     |
| ------------------ | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| switch(config-if)# |     | no        | split |     |     |     |     |     |     |     |
This command will disable the split interfaces for this port and clear
| their configuration. |        |     |     |     |     |     |     |     |     |     |
| -------------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Continue             | (y/n)? | y   |     |     |     |     |     |     |     |     |
Splittinganinterfacetwowaysona9300SeriesSwitch:
94
| AOS-CX10.11MonitoringGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |     |     |     |     |
| --------------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |

| switch(config)# |     | interface |     | 1/1/1 |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- |
switch(config-if)#
|     |     |     | split | 2   |     |     |
| --- | --- | --- | ----- | --- | --- | --- |
This command will disable the specified port, clear its configuration,
| and split          | it     | into | multiple | interfaces. |       |     |
| ------------------ | ------ | ---- | -------- | ----------- | ----- | --- |
| Continue           | (y/n)? | y    |          |             |       |     |
| switch(config-if)# |        |      | show     | interface   | brief |     |
---------------------------------------------------------------------------------
Port Native Mode Type Enabled Status Reason Speed Description
|     | VLAN |     |     |     |     | (Mb/s) |
| --- | ---- | --- | --- | --- | --- | ------ |
---------------------------------------------------------------------------------
| 1/1/1:1 | --  | routed |     | 400G-SR8 | yes up | 200000 |
| ------- | --- | ------ | --- | -------- | ------ | ------ |
| 1/1/2:1 | --  | routed |     | 400G-SR8 | yes up | 200000 |
```
Changingtheinterfaceto2x100Gmode:
| switch(config)#    |     | interface |       | 1/1/1  |     |     |
| ------------------ | --- | --------- | ----- | ------ | --- | --- |
| switch(config-if)# |     |           | split | 2 100g |     |     |
This command will clear the configuration for all split interfaces of
this port.
| Continue           | (y/n)? | y   |      |           |       |     |
| ------------------ | ------ | --- | ---- | --------- | ----- | --- |
| switch(config-if)# |        |     | show | interface | brief |     |
--------------------------------------------------------------------------------
Port Native Mode Type Enabled Status Reason Speed Description
|     | VLAN |     |     |     |     | (Mb/s) |
| --- | ---- | --- | --- | --- | --- | ------ |
--------------------------------------------------------------------------------
| 1/1/1:1        | --          | routed |         | 400G-SR8 | yes up                          | 100000 |
| -------------- | ----------- | ------ | ------- | -------- | ------------------------------- | ------ |
| 1/1/2:1        | --          | routed |         | 400G-SR8 | yes up                          | 100000 |
| Command        | History     |        |         |          |                                 |        |
| Release        |             |        |         |          | Modification                    |        |
| 10.10.1000     |             |        |         |          | Addedparameters:<COUNT>,<SPEED> |        |
| 10.07orearlier |             |        |         |          | --                              |        |
| Command        | Information |        |         |          |                                 |        |
| Platforms      | Command     |        | context |          | Authority                       |        |
8320 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --- | --------------- | --- |
8360
9300
10000
Breakoutcablesupport|95

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
96
| AOS-CX10.11MonitoringGuide| |     | (83xx,9300,10000SwitchSeries) |     |
| --------------------------- | --- | ----------------------------- | --- |

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
ArubaAirWave|97

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
98
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- |

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

Aruba AirWave | 99

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
100
| AOS-CX10.11MonitoringGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| --------------------------- | --- | ----------------------------- | --- | --- | --- |

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
ArubaAirWave|101

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
102
| AOS-CX10.11MonitoringGuide| | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| --------------------------- | ----------------------------- | --- | --- | --- | --- |

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
ArubaAirWave|103

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
104
| AOS-CX10.11MonitoringGuide| |     |     | (83xx,9300,10000SwitchSeries) |     |     |     |     |
| --------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |

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

Aruba AirWave | 105

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
106
| AOS-CX10.11MonitoringGuide| |     | (83xx,9300,10000SwitchSeries) |     |     |     |
| --------------------------- | --- | ----------------------------- | --- | --- | --- |

Support and Other Resources

Chapter 12

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

AOS-CX 10.11 Monitoring Guide | (83xx, 9300, 10000 Switch Series)

107

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
SupportandOtherResources|108

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

AOS-CX 10.11 Monitoring Guide | (83xx, 9300, 10000 Switch Series)

109