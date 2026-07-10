AOS-CX 10.16.xxxx SNMP/MIB
Guide

All AOS-CX Series Switches

Published: November 2025

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

AOS-CX 10.16.xxxx SNMP/MIB Guide | (All AOS-CX Series Switches)

3

Contents
| About this                          | document                               | 6   |
| ----------------------------------- | -------------------------------------- | --- |
| Applicableproducts                  |                                        | 6   |
| Latestversionavailableonline        |                                        | 7   |
| Commandsyntaxnotationconventions    |                                        | 7   |
| Abouttheexamples                    |                                        | 7   |
| Identifyingswitchportsandinterfaces |                                        | 8   |
| Identifyingmodularswitchcomponents  |                                        | 9   |
| SNMP                                |                                        | 11  |
| SNMPwrite:PoEwritecapabilities      |                                        | 11  |
| SNMPwrite:VLANwritecapabilities     |                                        | 11  |
| SNMPwrite:Configurations            |                                        | 12  |
| SNMPMIBview                         |                                        | 14  |
|                                     | ConfiguringSNMPMIB view                | 15  |
|                                     | SNMPMIBviewlimitations                 | 15  |
| SNMPtraps                           |                                        | 15  |
| ConfiguringSNMP                     |                                        | 16  |
| UpdatedMIBsforAOS-CX10.16.xxxx      |                                        | 18  |
| SNMPandArubaCentral                 |                                        | 20  |
| SNMPcommands                        |                                        | 21  |
|                                     | event-trap-enable                      | 21  |
|                                     | lldptrapenable                         | 21  |
|                                     | mac-notifytraps                        | 24  |
|                                     | rmonalarm                              | 26  |
|                                     | rmonalarm{enable|disable}{index|all}   | 27  |
|                                     | showconfiguration-changestrap          | 28  |
|                                     | showmac-notify                         | 28  |
|                                     | showmac-notifyport                     | 29  |
|                                     | showrmonalarm                          | 30  |
|                                     | showsnmpagent-port                     | 31  |
|                                     | showsnmpcommunity                      | 32  |
|                                     | showsnmpsystem                         | 33  |
|                                     | showsnmptrap                           | 34  |
|                                     | showsnmpviews                          | 34  |
|                                     | showsnmpvrf                            | 36  |
|                                     | showsnmpv3context                      | 36  |
|                                     | showsnmpv3engine-id                    | 37  |
|                                     | showsnmpv3security-level               | 37  |
|                                     | showsnmpv3users                        | 38  |
|                                     | snmp-serveragent-port                  | 39  |
|                                     | snmp-servercommunity                   | 39  |
|                                     | snmp-servercommunityview               | 42  |
|                                     | snmp-serverhistorical-counters-monitor | 43  |
|                                     | snmp-serverhost                        | 43  |
|                                     | snmp-serverresponse-source             | 47  |
|                                     | snmp-serversnmpv3-only                 | 48  |
|                                     | snmp-serversystem-contact              | 49  |
|                                     | snmp-serversystem-description          | 50  |
|                                     | snmp-serversystem-location             | 51  |
4
AOS-CX10.16.xxxxSNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

|                                    | snmp-servertrap                               |           | 51  |
| ---------------------------------- | --------------------------------------------- | --------- | --- |
|                                    | snmp-servertrapaaa-server-reachability-status |           | 53  |
|                                    | snmp-servertrapconfiguration-changes          |           | 53  |
|                                    | snmp-servertrapmac-notify                     |           | 54  |
|                                    | snmp-servertrapmodule                         |           | 55  |
|                                    | snmp-servertrapport-security                  |           | 56  |
|                                    | snmp-servertrapsnmp                           |           | 57  |
|                                    | snmp-servertrap-sourceinterfacevrf            |           | 58  |
|                                    | snmp-servertrapvsx                            |           | 59  |
|                                    | snmp-serverview                               |           | 60  |
|                                    | snmp-servervrf                                |           | 61  |
|                                    | snmpv3context                                 |           | 62  |
|                                    | snmpv3engine-id                               |           | 63  |
|                                    | snmpv3security-level                          |           | 63  |
|                                    | snmpv3user                                    |           | 64  |
|                                    | snmpv3userview                                |           | 68  |
| EntityMIBsupport                   |                                               |           | 68  |
| LocationoftheMIBfilesontheweb      |                                               |           | 69  |
| OIDsthatsupportSNMPread-write      |                                               |           | 69  |
| OIDsthatsupportSNMPread-create     |                                               |           | 70  |
| Support                            | and Other                                     | Resources | 71  |
| AccessingHPEArubaNetworkingSupport |                                               |           | 71  |
| AccessingUpdates                   |                                               |           | 72  |
| WarrantyInformation                |                                               |           | 72  |
| RegulatoryInformation              |                                               |           | 72  |
| DocumentationFeedback              |                                               |           | 72  |
|5

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing HPE Aruba Networking switches on
a network.

Applicable products

This document applies to the following products:

n HPE Aruba Networking 4100i Switch Series (JL817A, JL818A)

n HPE Aruba Networking 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A,

S4R20A, S4R21A, S4R22A, S4R23A, S4R24A, S4R25A, S4R26A, S4R27A, S4R28, S4R29A)

n HPE Aruba Networking 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

n HPE Aruba Networking 5420 Switch Series (S0U67A, S0U55A, S0U63A, S0U64A, S0U65A, S0U75A,

S0U72A, S0U78A, S0U58A, S0U73A, S0U74A, S0U71A, S0U76A, S0U70A, S0U77A, S0U60A, S0U61A,
S0U62A, S0U66A, S0U68A)

n HPE Aruba Networking 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A, R8Q68A,
R8Q69A, R8Q70A, R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A, JL724B, JL725B,
JL726B, JL727B, JL728B, S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,  S0M87A,  S0M88A,
S0M89A,  S0M90A, S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

n HPE Aruba Networking 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A,

JL665A, JL666A, JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A, S0X44A, S3L75A,
S3L76A, S3L77A, S4P41A,S4P42A, S4P43A, S4P44A, S4P45A, S4P46A, S4P47A, S4P48A)

n HPE Aruba Networking 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B,
R0X40C, R0X41A, R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C,
R0X26A, R0X27A, JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

n HPE Aruba Networking 8100 Switch Series (R9W94A, R9W95A, R9W96A, R9W97A)

n HPE Aruba Networking 8320 Switch Series (JL479A, JL579A, JL581A)

n HPE Aruba Networking 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n HPE Aruba Networking 8325H Switch Series (S4B20A, S4B21A, S4B22A, S4B23A, S2T42A, S2T46A,

S2T47A, S2T48A)

n HPE Aruba Networking 8325P Switch Series (S0G12A, S4A48A)

n HPE Aruba Networking 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A,

JL709A, JL710A, JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C, JL709C, JL710C, JL711C,
JL704C, JL705C, JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

n HPE Aruba Networking 8400 Switch Series (JL366A, JL363A, JL687A)

n HPE Aruba Networking 9300 Switch Series (R9A29A, R9A30A, R8Z96A, S0F81A, S0F82A, S0F83A)

n HPE Aruba Networking 9300S Switch Series (S0F81A, S0F82A, S0F83A, S0F84A, S0F85A, S0F86A,

S0F88A, S0F95A, S0F96A)

n HPE Aruba Networking 10000 Switch Series (R8P13A, R8P14A)

n HPE Aruba Networking 10040 Switch Series (S4R58A, S4R59A)

AOS-CX 10.16.xxxx SNMP/MIB Guide | (All AOS-CX Series Switches)

6

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
| [ ] |     | Brackets.Indicatesthattheencloseditemoritemsareoptional. |     |
| --- | --- | -------------------------------------------------------- | --- |
| …or |     | Ellipsis:                                                |     |
... Incodeandscreenexamples,averticalorhorizontalellipsisindicatesan
n
omissionofinformation.
|     |     | n Insyntaxusingbracketsandbraces,anellipsisindicatesitemsthatcanbe |     |
| --- | --- | ------------------------------------------------------------------ | --- |
repeated.Whenanitemfollowedbyellipsesisenclosedinbrackets,zero
ormoreitemscanbespecified.
| About | the examples |     |     |
| ----- | ------------ | --- | --- |
Examplesinthisdocumentarerepresentativeandmightnotmatchyourparticularswitchor
environment.
Theslotandportnumbersinthisdocumentareforillustrationonlyandmightbeunavailableonyour
switch.
| Understanding | the | CLI prompts |     |
| ------------- | --- | ----------- | --- |
Aboutthisdocument|7

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

On the HPE Aruba Networking 4100i Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6000 and 6100 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

AOS-CX 10.16.xxxx SNMP/MIB Guide | (All AOS-CX Series Switches)

8

On the HPE Aruba Networking 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.
The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the HPE Aruba Networking 6400 and 5420 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
member 1.

On the HPE Aruba Networking 8xxx, 93xx, and 10xxx Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on physical port 4 in slot 1 on

member 1.

On the HPE Aruba Networking 8400 Switch Series

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

About this document | 9

n Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

o member: 1.

o tray: 1 to 4.

o fan: 1 to 4.

n Fabric modules are not labeled on the switch but are labeled in software in the format:

member/module:

o member: 1.

o member: 1 or 2.

n The display module on the rear of the switch is not labeled with a member or slot number.

AOS-CX 10.16.xxxx SNMP/MIB Guide | (All AOS-CX Series Switches)

10

Chapter 2

SNMP

SNMP

Simple Network Management Protocol (SNMP) is an Internet-standard protocol used for managing and
monitoring the devices connected to a network by collecting, organizing, and modifying information
about managed devices on IP networks.

AOS-CX switches support RFC3411, RFC3412, RFC3413, RFC3414, RFC3415, RFC3416, RFC3417, and RFC3418 for

SNMP.

SNMP write: PoE write capabilities

PoE enable

The PoE enable is requested through SNMP to enable the PoE interface. The admin_disable SNMP value
is updated to enable the PoE interface.

PoE disable

The PoE disable is requested through SNMP to disable the PoE interface. The admin_disable SNMP
value is updated to disable the PoE interface.

PoE cycle

The PoE cycle is a feature where you can request a PoE port reset with a timeout ranging from 1 to 60
seconds. The PoE cycle is requested through the SNMP server to disable and enable a PoE interface with
an input timeout of 1 to 60 seconds. The PoE handles the PoE disable and enable events when the SNMP
value is updated for admin_disable correspondingly. It is a one-time operation.

PoE priority

PoE priority handles the power priority to decide the number of ports to be powered up according to the
set priority. This SNMP request sets the PoE interface PoE priority to one of these three values:

n critical

n high

n low (The default priority is low)

SNMP write: VLAN write capabilities

VLAN Add or Delete

The index for the ieee8021QBridgeVlanStaticTable and dot1qVlanStaticTable is VLAN. To create or delete
a VLAN, either configure:

AOS-CX 10.16.xxxx SNMP/MIB Guide | (All AOS-CX Series Switches)

11

n ieee8021QBridgeVlanStaticRowStatus Mib object in ieee8021QBridgeVlanStaticTable

or

n dot1QBridgeVlanStaticRowStatus Mib object in dot1qVlanStaticTable

Set the value to 4 to create a new VLAN, and set the value to 6 to delete an existing VLAN.

Add or Delete Tagged Port(s) to a VLAN

The index for the ieee8021QBridgeVlanStaticTable and dot1qVlanStaticTable is VLAN. To set or clear
port(s) as tagged members for the VLAN, either configure:

n ieee8021QBridgeVlanStaticEgressPorts Mib object in ieee8021QBridgeVlanStaticTable

or

n dot1QBridgeVlanStaticEgressPorts Mib object in dot1qVlanStaticTable

Changes to a bit in this object affect per-port and per-VLAN registrar control.

Add or Delete Untagged Port(s) to a VLAN

The index for the ieee8021QBridgeVlanStaticTable and dot1qVlanStaticTable is VLAN. To set or clear
port(s) as untagged members for the VLAN, either configure:

n ieee8021QBridgeVlanStaticUntaggedPorts Mib object in ieee8021QBridgeVlanStaticTable

or

n dot1QBridgeVlanStaticEgressPorts Mib object in dot1qVlanStaticTable

Changes to a bit in this object affect the per-port, per-VLAN Registrar control.

Enable or Disable MVRP to Port

The index for the ieee8021QBridgePortVlanTable and dot1qPortVlanTable is port. To enable or disable
port level MVRP status, either configure:

n ieee8021QBridgeMvrpEnabledStatus Mib object in ieee8021QBridgePortVlanTable

or

n dot1QBridgeMvrpEnabledStatus Mib object in dot1qPortVlanTable

The value true(1) indicates that MVRP is enabled on the device and false(2) indicates that MVRP is
disabled for all ports on the device.

Add untagged VLAN to a Port

The index for the ieee8021QBridgePortVlanTable and dot1qPortVlanTable is port. To set untagged vlan
for the port, either configure:

n ieee8021QBridgePvid Mib object in ieee8021QBridgePortVlanTable

or

n dot1QBridgePvids Mib object in dot1qPortVlanTable

SNMP write: Configurations

Prerequisites

SNMP | 12

Theswitchmustbeconfiguredforexternalaccess(suchasmanagementinterfaceandIPaddressing)
andSNMPenabled(suchasSNMPv2andSNMPv3).
| switch(config)#         | interface   |        | mgmt           |               |              |     |
| ----------------------- | ----------- | ------ | -------------- | ------------- | ------------ | --- |
| switch(config-if-mgmt)# |             |        | no shutdown    |               |              |     |
| switch(config-if-mgmt)# |             |        | ip static      | 10.10.10.4/24 |              |     |
| switch(config)#         | snmp-server |        | vrf            | mgmt          |              |     |
| switch(config)#         | no          | snmpv3 | security-level |               | auth-privacy |     |
switch(config)# snmpv3 user test auth md5 auth-pass plaintext password priv aes
| priv-pass | plaintext | password | access-level |     | rw  |     |
| --------- | --------- | -------- | ------------ | --- | --- | --- |
SNMP set examples
ThefollowingexamplesareexecutedfromanexternalclientcommunicatingthroughSNMPtothe
switch.TheydescribesbothcommandsyntaxandOIDinterpretations:
| n copy running-config |     | startup-config |     |     |     |     |
| --------------------- | --- | -------------- | --- | --- | --- | --- |
snmpset -v3 -t100 -u test -l authPriv -a md5 -A password -x aes -X password
| 10.10.10.4                                  | 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5 |     |     |     |                  | i 4 |
| ------------------------------------------- | ----------------------------------------- | --- | --- | --- | ---------------- | --- |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5    |                                           |     |     |     | i 3              |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5    |                                           |     |     |     | i 2              |     |
| OID                                         |                                           |     |     |     | Description      |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5i4 |                                           |     |     |     | Createoperation. |     |
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5i3 SetsourcetypetoRunningConfig.
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5i2 SetdestinationtypetoStartupConfig.
| n copy startup-config |     | running-config |     |     |     |     |
| --------------------- | --- | -------------- | --- | --- | --- | --- |
snmpset -v3 -t100 -u test -l authPriv -a md5 -A password -x aes -X password
| 10.10.10.4                                  | 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5 |     |     |     |                  | i 4 |
| ------------------------------------------- | ----------------------------------------- | --- | --- | --- | ---------------- | --- |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5    |                                           |     |     |     | i 2              |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5    |                                           |     |     |     | i 3              |     |
| OID                                         |                                           |     |     |     | Description      |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5i4 |                                           |     |     |     | Createoperation. |     |
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5i2 SetsourcetypetoStartupConfig.
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5i3 SetdestinationtypetoRunningConfig.
| n copy REMOTE-URL | running-config |     |     |     |     |     |
| ----------------- | -------------- | --- | --- | --- | --- | --- |
snmpset -v3 -t100 -u test -l authPriv -a md5 -A password -x aes -X password
| 10.10.10.4                               | 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5 |     |     |     |     | i 4 |
| ---------------------------------------- | ----------------------------------------- | --- | --- | --- | --- | --- |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5 |                                           |     |     |     | i 1 |     |
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 13

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5 i 3
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.4.5 i 4
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.6.5 i 1
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.7.5 s "file"
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.9.5 s "10.10.10.1"
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.12.5 s "mgmt"
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.10.5 s "user"
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.11.5 s "password"
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.13.5 i 1

OID

Description

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5 i 4

Create operation.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5 i 1

Set source type to external file.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5 i 3

Set destination type to RunningConfig.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.4.5 i 4

Set protocol to SFTP.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.6.5 i 1

Set file format to CLI.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.7.5 s "file"

Set file name.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.9.5 s "10.10.10.1"

Set IP from server.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.12.5 s "mgmt"

Set VRF.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.10.5 s "user"

Set username to authenticate, if applicable.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.11.5 s "password"

Set password to authenticate, if applicable.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.13.5 i 1

Enable Notification on completion, if required.

n copy running-config checkpoint ckpt1

snmpset -v3 -t100 -u test -l authPriv -a md5 -A password -x aes -X password
10.10.10.4 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5 i 4
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5 i 3
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5 i 4
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.5.5 s "ckp1"

OID

Description

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5 i 4

Create operation.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5 i 3

Set source type to RunningConfig.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5 i 4

Set destination type to Checkpoint.

1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.5.5 s "ckp1"

Set checkpoint name to ckp1.

SNMP MIB view

SNMP | 14

SNMPMIBviewisagroupofviewsubtreesintheMIBhierarchy.Aviewsubtreeisidentifiedbythe
pairingofanObjectIdentifier(OID)subtreevaluewithabitstringmaskvalue.EachMIBviewisdefined
bytheviewsubtreesthatisincludedorexcludedfromtheMIBview.YoucanusetheMIBviewsto
controltheOIDrangethatSNMPv3usersorSNMPv1/v2communitycanaccess.
| Configuring | SNMP | MIB view |     |     |
| ----------- | ---- | -------- | --- | --- |
ThefollowingparametersarerequiredtoconfiguretheSNMPMIBview:
n Viewname-SpecifiesthenameoftheSNMPMIBview.Viewnamescansupportuptoamaximumof
32alphanumericcharacters.
n Type-WhethertoincludeorexcludetheviewsubtreeorgroupofsubtreesfromtheSNMPMIBview.
n OID-AnOIDstringforthesubtreetoincludeorexcludefromtheSNMPMIBview.
Forexample,thesystemsubtreeisspecifiedbytheOIDstring.1.3.6.1.2.1.1.
n Mask-ItisanOIDmask.Themaskis47charactersinlength.
o Theformatisxx:xx....(:).EachOIDmaskis16octetsinlength.
o Anoctetistwohexadecimalcharactersseparatedby:(colon).Onlyhexadecimalcharactersare
acceptedinthisfield.
Forexample,OIDmaskFF:A0is11111111:10100000.
| SNMP MIB | view limitations |     |     |     |
| -------- | ---------------- | --- | --- | --- |
Ansnmpwalkwithacommunityorv3userattachedtocontexttakesprecedenceoverSNMPMIBview.If
thecontextisattachedtotheuserorcommunity,theSNMPMIBviewconfiguredtothev3useror
communitywillnottakeeffect.
Example:
| snmp view   | admin system | ff included |            |       |
| ----------- | ------------ | ----------- | ---------- | ----- |
| snmp-server | community    | admin       | view admin |       |
| snmpv3      | context new  | vrf default | community  | admin |
| snmpv3      | user nw_user | context     | new        |       |
| snmpv3      | user nw_user | view admin  |            |       |
ArubaproprietaryMIBnameswithout::(doublecolon)seperatedrootMIBnamesarenotsupportedfor
SNMPMIBview.
n ThefollowingexamplesaresupportedforSNMPMIBview:
snmp-server view user_view .1.3.6.1.4.1.47196.4.1.1.3.11.6.1.1.4 FF included
snmp-server view admin_1 ARUBAWIRED-MODULE-MIB::arubaWiredModuleName FF included
n ThefollowingexampleisnotsupportedforSNMPMIBview:
| snmp-server | view new_view | arubaWiredModuleName |     | included |
| ----------- | ------------- | -------------------- | --- | -------- |
SNMP traps
Event log traps
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 15

When SNMP is configured, interface daemons event log messages for link-up and link-down events will
be sent as traps.

Event log trap OID: 1.3.6.1.4.1.47196.4.1.1.3.4.1.1

Parameter

OID

Description

sysUpTimeInstance

1.3.6.1.2.1.1.3.0

Contains the uptime for the system in
centiseconds

snmpTrapOID

1.3.6.1.6.3.1.1.4.1

Contains the OID for the event log trap

eventIndex

1.3.6.1.2.1.16.9.1.1.1

Contains an index that uniquely identifies
an event

eventDescription

1.3.6.1.2.1.16.9.1.1.2

Contains the event log message

Link-up and link-down traps

Standard IF-MIB link-up and link-down traps will be sent on link-state change when an interface is
configured using trap link-status or when user_config:link_state_snmp_trap is set to true. The
trap sends the current information for ifindex, admin status, operational status, and interface name.

Link up trap OID: 1.3.6.1.6.3.1.1.5.4

Link down trap OID: 1.3.6.1.6.3.1.1.5.3

Parameter

OID

Description

sysUpTimeInstance

1.3.6.1.2.1.1.3.0

snmpTrapOID

1.3.6.1.6.3.1.1.4.1

Contains the uptime for the system in
centiseconds

Contains the OID for the link up or
linkdown trap

ifIndex

1.3.6.1.2.1.2.2.1.1.X

Contains the ifindex for the interface

ifAdminStatus

1.3.6.1.2.1.2.2.1.7.X

Contains the admin status for the interface

ifOperStatus

1.3.6.1.2.1.2.2.1.8.X

Contains the operational status for the
interface

ifDescr

1.3.6.1.2.1.2.2.1.2.X

Contains the name for the interface

Configuring SNMP

SNMP agent provides read-write access for specific OIDs. Refer OIDs that support SNMP read-write for
the list of OIDs that supports read-write operations.

Best practices is to use a 5-second (-t5) timeout in a scaled environment, when the network traffic is high or
when there is significant load on the switch.

Procedure

1. SNMP is not enabled on the switch by default, unless the user enables it over any available VRF or
with the default/mgmt VRF using the command snmp-server vrf <NAME>. For example, use the

SNMP | 16

commandsnmp-server vrf mgmttoenableSNMPonthemanagementinterface.Usethe
commandsnmp-server vrf defaulttoenableSNMPonthedefaultVRF.Usethecommand
snmp-server vrf <USERDEFINED_VRF_NAME>toenableSNMPontheusercreatedVRF.
2. Setthesystemcontact,location,anddescriptionfortheswitchwiththefollowingcommands:
| snmp-server | system-contact |     |     |     |
| ----------- | -------------- | --- | --- | --- |
n
| snmp-server | system-location |     |     |     |
| ----------- | --------------- | --- | --- | --- |
n
| n snmp-server | system-description |     |     |     |
| ------------- | ------------------ | --- | --- | --- |
YoucanalsosetthesystemlocationandsystemcontactvaluesusingSNMP.
3. Ifrequired,changethedefaultSNMPportonwhichtheagentlistensforrequestswiththe
| commandsnmp-server |     | agent-port. |     |     |
| ------------------ | --- | ----------- | --- | --- |
4. Bydefault,theagentusesthecommunitystringpublictoprotectaccessthroughSNMPv1/v2c.
Setanewcommunitystringwiththecommandsnmp-server community.
5. ConfigurethetrapreceiverstowhichtheSNMPagentwillsendtrapnotificationswiththe
| commandsnmp-server |     | host. |     |     |
| ------------------ | --- | ----- | --- | --- |
6. CreateanSNMPv3contextandassociateitwithanyavailableSNMPv3usertoperformcontext
specificv3MIBpollingusingthecommandsnmpv3 user <V3_USERNAME> context <CONTEXT_
NAME>.
7. CreateanSNMPv3contextandassociateitwithanavailableSNMPv1/v2ccommunitystringto
performcontextspecificv1/v2cMIBpollingusingthecommandsnmpv3 context <CONTEXT_
| NAME> | vrf <VRF_NAME> | community | <COMMUNITY_NAME>. |     |
| ----- | -------------- | --------- | ----------------- | --- |
8. ReviewyourSNMPconfigurationsettingswiththefollowingcommands:
| n show | snmp agent-port |     |     |     |
| ------ | --------------- | --- | --- | --- |
| show   | snmp community  |     |     |     |
n
| show | snmp system |     |     |     |
| ---- | ----------- | --- | --- | --- |
n
| n show | snmpv3 context |     |     |     |
| ------ | -------------- | --- | --- | --- |
| n show | snmp trap      |     |     |     |
| n show | snmp vrf       |     |     |     |
| n show | snmpv3 users   |     |     |     |
| n show | tech snmp      |     |     |     |
Example 1
Thisexamplecreatesthefollowingconfiguration:
n EnablesSNMPontheout-of-bandmanagementinterface(VRFmgmt).
n Setsthecontact,location,anddescriptionfortheswitchto:JaniceM,Building2,LabSwitch.
SetsthecommunitystringtoLab8899X.
n
| switch(config)# | snmp-server | vrf                | mgmt     |           |
| --------------- | ----------- | ------------------ | -------- | --------- |
| switch(config)# | snmp-server | system-contact     |          | JaniceM   |
| switch(config)# | snmp-server | system-location    |          | Building2 |
| switch(config)# | snmp-server | system-description |          | LabSwitch |
| switch(config)# | snmp-server | community          | Lab8899X |           |
Example 2
Thisexamplecreatesthefollowingconfiguration:
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 17

n Creates an SNMPv3 user named Admin using sha authentication with the plaintext password

mypassword and using des security with the plaintext password myprivpass.

n Associates the SNMPv3 user Admin with a context named newContext.

switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des

priv-pass plaintext myprivpass

switch(config)# snmpv3 user Admin context newContext

The CIPT MIB does not support the SNMP SET operation for the following objects:

n arubaWiredCiptEnable

n arubaWiredCiptProbeEnable

n arubaWiredCiptVlanConfig

n arubaWiredCiptPortEnable

n arubaWiredCiptPortUpdateInterval

n arubaWiredCiptPortClientLimit

Updated MIBs for AOS-CX 10.16.xxxx

New MIB objects

The following objects have been added to the ARUBAWIRED-VSFv2-MIB.mib:

n arubaWiredVsfv2SplitDetectVlanId

n arubaWiredVsfv2SplitDetectOperStatus

n arubaWiredVsfv2SplitDetectStatusDownReason

n arubaWiredVsfv2SplitDetectCountersTx

n arubaWiredVsfv2SplitDetectCountersRx

n arubaWiredVsfv2SplitDetectCountersRxDrop

The following objects have been added to the ARUBAWIRED-NETWORKING-OID.mib

n arubaWiredSwitchS4R58A

n arubaWiredSwitchS4R59A

n arubaWiredSwitchModuleS4R50A

n arubaWiredSwitchModuleS4R51A

n arubaWiredSwitchModuleS4R52A

n arubaWiredSwitchModuleS4R53A

n arubaWiredSwitchModuleS4R58A

n arubaWiredSwitchModuleS4R59A

The following objects have been added to the ARUBAWIRED-PM-MIB.mib:

SNMP | 18

n arubaWiredPmXcvrDomTable

o arubaWiredPmXcvrDomPortDesc

o arubaWiredPmXcvrDomTemp

o arubaWiredPmXcvrDomTempHiAlarmThreshold

o arubaWiredPmXcvrDomTempHiAlarm

o arubaWiredPmXcvrDomTempLoAlarmThreshold

o arubaWiredPmXcvrDomTempLoAlarm

o arubaWiredPmXcvrDomTempHiWarnThreshold

o arubaWiredPmXcvrDomTempHiWarn

o arubaWiredPmXcvrDomTempLoWarnThreshold

o arubaWiredPmXcvrDomTempLoWarn

o arubaWiredPmXcvrDomVoltage

o arubaWiredPmXcvrDomVccHiAlarmThreshold

o arubaWiredPmXcvrDomVccHiAlarm

o arubaWiredPmXcvrDomVccLoAlarmThreshold

o arubaWiredPmXcvrDomVccLoAlarm

o arubaWiredPmXcvrDomVccHiWarnThreshold

o arubaWiredPmXcvrDomVccHiWarn

o arubaWiredPmXcvrDomVccLoWarnThreshold

o arubaWiredPmXcvrDomVccLoWarn

o arubaWiredPmXcvrDomTxBiasHiAlarmThreshold

o arubaWiredPmXcvrDomTxBiasLoAlarmThreshold

o arubaWiredPmXcvrDomTxBiasHiWarnThreshold

o arubaWiredPmXcvrDomTxBiasLoWarnThreshold

o arubaWiredPmXcvrDomTxPwrHiAlarmThreshold

o arubaWiredPmXcvrDomTxPwrLoAlarmThreshold

o arubaWiredPmXcvrDomTxPwrHiWarnThreshold

o arubaWiredPmXcvrDomTxPwrLoWarnThreshold

o arubaWiredPmXcvrDomRxPwrHiAlarmThreshold

o arubaWiredPmXcvrDomRxPwrLoAlarmThreshold

o arubaWiredPmXcvrDomRxPwrHiWarnThreshold

o arubaWiredPmXcvrDomRxPwrLoWarnThreshold

o arubaWiredPmXcvrDomTimeStamp

n arubaWiredPmXcvrLaneDomTable

o arubaWiredPmXcvrLaneDomIndex

o arubaWiredPmXcvrLaneDomTxBias

o arubaWiredPmXcvrLaneDomTxBiasHiAlarm

o arubaWiredPmXcvrLaneDomTxBiasLoAlarm

o arubaWiredPmXcvrLaneDomTxBiasHiWarn

o arubaWiredPmXcvrLaneDomTxBiasLoWarn

o arubaWiredPmXcvrLaneDomTxPower

AOS-CX 10.16.xxxx SNMP/MIB Guide | (All AOS-CX Series Switches)

19

o arubaWiredPmXcvrLaneDomTxPwrHiAlarm

o arubaWiredPmXcvrLaneDomTxPwrLoAlarm

o arubaWiredPmXcvrLaneDomTxPwrHiWarn

o arubaWiredPmXcvrLaneDomTxPwrLoWarn

o arubaWiredPmXcvrLaneDomRxPower

o arubaWiredPmXcvrLaneDomRxPwrHiAlarm

o arubaWiredPmXcvrLaneDomRxPwrLoAlarm

o arubaWiredPmXcvrLaneDomRxPwrHiWarn

o arubaWiredPmXcvrLaneDomRxPwrLoW

The following objects have been added to the ARUBAWIRED-POE-MIB.mib:

n arubaWiredPoePethMainPseAveragePoePower

n arubaWiredPoePethPsePortAveragePoePower

The following objects have been added to the ARUBAWIRED-POE-MIB.mib:

n arubaWiredPoePethMainPseAveragePoePower

n arubaWiredPoePethPsePortAveragePoePower

SNMP and Aruba Central

Note the following behaviors when using Aruba Central to monitor your AOS-CX Switches:

n When Aruba Central disconnects, SNMP is restarted to operate in Read-Write mode.

n When the switch reconnects to Aruba Central, SNMP is restarted to operate in Read-Only mode, to

prevent configuration updates via the command-line interface or SNMP.

n If a monitoring tool polls the switch while SNMP is restarting, the polling request may fail.

SNMP | 20

Chapter 3
| SNMP commands |     |     |     |
| ------------- | --- | --- | --- |
event-trap-enable
event-trap-enable
no event-trap-enable
Description
EnablesthenotificationofeventstobesentastrapstotheSNMPmanagementstations.Itisenabledby
default.
Thenoformofthiscommanddisablestheeventtraps.
Examples
Enablingtheeventtraps:
| switch(config)# | event-trap-enable |     |     |
| --------------- | ----------------- | --- | --- |
Disablingtheeventtraps:
| switch(config)#     | no      | event-trap-enable |              |
| ------------------- | ------- | ----------------- | ------------ |
| Command History     |         |                   |              |
| Release             |         |                   | Modification |
| 10.07orearlier      |         |                   | --           |
| Command Information |         |                   |              |
| Platforms           | Command | context           | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| lldp trap        | enable |     |     |
| ---------------- | ------ | --- | --- |
| lldp trap enable |        |     |     |
| no lldp trap     | enable |     |     |
Description
EnablessendingSNMPtrapsforLLDPrelatedeventsfromaparticularinterface.LLDPtrapgenerationis
enabledbydefaultonalltheinterfacesandhastobedisabledforinterfacesonwhichtrapsarenot
requiredtobegenerated.
ThenoformofthiscommanddisablestheLLDPtrapgeneration.
21
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches)

LLDPtrapgenerationisdisabledbydefaultatthegloballevelandmustbeenabledbeforeanyLLDPtrapsare
sent.
Examples
EnablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | lldp trap | enable |     |     |
| --------------- | --- | --------- | ------ | --- | --- |
EnablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     | lldp | trap | enable |     |
| ------------------ | --- | ---- | ---- | ------ | --- |
DisablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | no lldp | trap | enable |     |
| --------------- | --- | ------- | ---- | ------ | --- |
DisablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     | no lldp | trap | enable |     |
| ------------------ | --- | ------- | ---- | ------ | --- |
DisplayingLLDPglobalconfiguration:
| switch#     | show | lldp configuration |     |     |     |
| ----------- | ---- | ------------------ | --- | --- | --- |
| LLDP Global |      | Configuration      |     |     |     |
=========================
| LLDP Enabled  |         |                |     | : No |     |
| ------------- | ------- | -------------- | --- | ---- | --- |
| LLDP Transmit |         | Interval       |     | : 30 |     |
| LLDP Hold     | Time    | Multiplier     |     | : 4  |     |
| LLDP Transmit |         | Delay Interval |     | : 2  |     |
| LLDP Reinit   |         | Timer Interval |     | : 2  |     |
| LLDP Trap     | Enabled |                |     | : No |     |
TLVs Advertised
===============
| Management | Address |     |     |     |     |
| ---------- | ------- | --- | --- | --- | --- |
Port Description
Port VLAN-ID
System Description
System Name
| LLDP Port | Configuration |     |     |     |     |
| --------- | ------------- | --- | --- | --- | --- |
=======================
| PORT |     | TX-ENABLED |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | --- | ---------- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| 1/1/1 |     | Yes |     | Yes | Yes |
| ----- | --- | --- | --- | --- | --- |
| 1/1/2 |     | Yes |     | Yes | Yes |
| 1/1/3 |     | Yes |     | Yes | Yes |
| 1/1/4 |     | Yes |     | Yes | Yes |
| 1/1/5 |     | Yes |     | Yes | Yes |
|22

| 1/1/6 | Yes |     | Yes | Yes |
| ----- | --- | --- | --- | --- |
...........
...........
| mgmt | Yes |     | Yes | Yes |
| ---- | --- | --- | --- | --- |
DisplayingLLDPConfigurationfortheinterface:
| switch#     | show lldp configuration |     | 1/1/1 |     |
| ----------- | ----------------------- | --- | ----- | --- |
| LLDP Global | Configuration           |     |       |     |
=========================
| LLDP Enabled  |                 |          | : Yes |     |
| ------------- | --------------- | -------- | ----- | --- |
| LLDP Transmit | Interval        |          | : 30  |     |
| LLDP Hold     | Time Multiplier |          | : 4   |     |
| LLDP Transmit | Delay           | Interval | : 2   |     |
| LLDP Reinit   | Timer Interval  |          | : 2   |     |
| LLDP Trap     | Enabled         |          | : No  |     |
| LLDP Port     | Configuration   |          |       |     |
=======================
| PORT | TX-ENABLED |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | ---------- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| 1/1/1 | Yes |     | Yes | Yes |
| ----- | --- | --- | --- | --- |
DisplayingLLDPConfigurationforthemanagementinterface:
| switch#     | show lldp configuration |     | mgmt |     |
| ----------- | ----------------------- | --- | ---- | --- |
| LLDP Global | Configuration           |     |      |     |
=========================
| LLDP Enabled  |                 |          | : Yes |     |
| ------------- | --------------- | -------- | ----- | --- |
| LLDP Transmit | Interval        |          | : 30  |     |
| LLDP Hold     | Time Multiplier |          | : 4   |     |
| LLDP Transmit | Delay           | Interval | : 2   |     |
| LLDP Reinit   | Timer Interval  |          | : 2   |     |
| LLDP Trap     | Enabled         |          | : Yes |     |
| LLDP Port     | Configuration   |          |       |     |
=======================
| PORT | TX-ENABLED |     | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | ---------- | --- | ---------- | ----------------- |
--------------------------------------------------------------------------
| mgmt           | Yes         |         | Yes          | Yes |
| -------------- | ----------- | ------- | ------------ | --- |
| Command        | History     |         |              |     |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms configandconfig-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 23

mac-notify traps
mac-notify traps {aged | learned | moved | removed}
no mac-notify traps {aged | learned | moved | removed}

Description

Configures a Layer 2 or VXLAN interface to generate SNMP trap notifications for up to four different
types of MAC address related events on the trunk or access in physical or lag interfaces.

MAC notification trap addition to or removal from an interface can be in any combination, quantity, or
order. The addition of existing configured traps or removal of non-configured traps will be accepted and
ignored.

The mac-notify feature must be enabled globally for any interface configurations to generate SNMP traps.

Enabling mac-notify traps may impact the system performance on networks with a large number of mac-notify

events.

The no form of this command removes the traps from the interface.

Parameter

Description

aged

learned

moved

removed

Notifies when a MAC address aged out on the interface.

Notifies when a MAC address is learned on the interface.

Notifies when a MAC address moved from the interface.

Notifies when a MAC address is removed from the interface.

MAC notification cannot be configured on a Layer 3 (routing) interface. A Layer 2 interface that is changed to a
Layer 3 interface through the routing command will discard any existing MAC notification configurations.

When MACs are learned on VXLAN tunnels or port-access port-security enabled ports, the move scenario is

handled by the EVPN/port-access feature respectively. It performs the move by deleting the MAC from the old

port and installing it on the new port. In this scenario, MAC trap notifications, if enabled, will reflect that by

producing removed and learned notifications.

Usage

n MAC notify trap will not generate for static MACs.

n vsx-sync is not supported. You must enable the MAC notify traps explicitly on secondary to ensure

the traps are generated.

n For EVPN MAC move between the following interfaces, the respective event types are produced (not

always removed or learned)

o Port to port: moved

o Port to tunnel: removed/learned

o Tunnel to port: removed/learned

o Tunnel to Tunnel: moved

Examples

| 24

MACnotificationtypesandtheassociatedeventsonlyapplytoLayer2andVXLANinterfaces,hencerouting
mightneedtobedisabledontherelevantinterfaces.
EnableMACnotificationtrapswithintheSNMPmoduleatagloballevel:
| switch(config)# |     | snmp-server |     | trap |     |     |     |     |     |     |
| --------------- | --- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- |
aaa-server-reachability-status Enable SNMP trap for AAA server reachability
status
| configuration-changes |     |     |     |     | Enable configuration |        |             | changes | traps        |     |
| --------------------- | --- | --- | --- | --- | -------------------- | ------ | ----------- | ------- | ------------ | --- |
| cpu-utilization       |     |     |     |     | Enable high          | CPU    | utilization |         | traps        |     |
| link-status           |     |     |     |     | Enable link          | status | traps       | for     | all physical |     |
interfaces
| mac-notify         |     |     |     |     | Enable MAC           | table   | change      | notification |        | traps |
| ------------------ | --- | --- | --- | --- | -------------------- | ------- | ----------- | ------------ | ------ | ----- |
| memory-utilization |     |     |     |     | Enable high          | memory  | utilization |              | traps  |       |
| module             |     |     |     |     | Enable module        |         | event traps |              |        |       |
| port-security      |     |     |     |     | Enable port-security |         |             | violation    | traps. |       |
|                    |     |     |     |     | (Default:            | enable) |             |              |        |       |
| rmon-events        |     |     |     |     | Enable RMON          | event   | traps       |              |        |       |
| snmp               |     |     |     |     | Enable snmp          | traps   |             |              |        |       |
Formoreinformation,seesnmp-servertrapmac-notify.
EnablingthetrapsonanL2interface:
| switch(config)#    |     | interface    | 1/1/1   |           |         |     |     |     |     |     |
| ------------------ | --- | ------------ | ------- | --------- | ------- | --- | --- | --- | --- | --- |
| switch(config-if)# |     | mac-notify   |         | traps     | learned |     |     |     |     |     |
| 1/1/1 is not       | an  | L2 interface |         | or tunnel |         |     |     |     |     |     |
| switch(config-if)# |     | no           | routing |           |         |     |     |     |     |     |
switch(config-if)#
|                          |     | mac-notify |            | traps | learned | removed |         |     |     |     |
| ------------------------ | --- | ---------- | ---------- | ----- | ------- | ------- | ------- | --- | --- | --- |
| switch(config-if)#       |     | mac-notify |            | traps | moved   |         |         |     |     |     |
| switch(config-if)#       |     | mac-notify |            | traps | aged    |         |         |     |     |     |
| switch(config)#          |     | interface  | vxlan      | 1     |         |         |         |     |     |     |
| switch(config-vxlan-if)# |     |            | mac-notify |       | traps   | learned | removed |     |     |     |
switch(config)#
|                    |     | interface  | lag101 |       |         |     |     |     |     |     |
| ------------------ | --- | ---------- | ------ | ----- | ------- | --- | --- | --- | --- | --- |
| switch(config-if)# |     | mac-notify |        | traps | removed |     |     |     |     |     |
Disablingthelearnedandremovedtrapsfromtheinterface1/1/1:
| switch(config)#          |     | interface | 1/1/1      |            |               |         |         |     |     |     |
| ------------------------ | --- | --------- | ---------- | ---------- | ------------- | ------- | ------- | --- | --- | --- |
| switch(config-if)#       |     | no        | mac-notify |            | traps learned |         | removed |     |     |     |
| switch(config)#          |     | interface | vxlan      | 1          |               |         |         |     |     |     |
| switch(config-vxlan-if)# |     |           | no         | mac-notify | traps         | learned | removed |     |     |     |
EnablesendingSNMPnotificationsforMACtablechanges:
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 25

| switch(config-vxlan-if)# |        | mac-notify | traps         |          |                  |
| ------------------------ | ------ | ---------- | ------------- | -------- | ---------------- |
| aged                     | Notify | when       | a MAC address | aged out | on the interface |
learned Notify when a MAC address was learned on the interface
| moved | Notify | when | a MAC address | moved from | the interface |
| ----- | ------ | ---- | ------------- | ---------- | ------------- |
removed Notify when a MAC address was removed from the interface
switch(config-vxlan-if)# mac-notify traps learned aged removed moved
| Command History     |         |         |                                                  |     |     |
| ------------------- | ------- | ------- | ------------------------------------------------ | --- | --- |
| Release             |         |         | Modification                                     |     |     |
| 10.13.1000          |         |         | SupportforSNMPMACnotifytrapsonVXLANtunnels.      |     |     |
| 10.10               |         |         | Supportforportaccessfeatureswithmac-notifyadded. |     |     |
| 10.08               |         |         | Commandintroduced.                               |     |     |
| Command Information |         |         |                                                  |     |     |
| Platforms           | Command | context | Authority                                        |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
rmon alarm
rmon alarm index <INDEX> snmp-oid <SNMP-OID> rising-threshold <RISING-THRESHOLD>
falling-threshold <FALLING-THRESHOLD> [sample-interval <SAMPLE-INTERVAL>] [sample-
type <ABSOLUTE|DELTA>]
| no rmon alarm | [index <INDEX>] |     |     |     |     |
| ------------- | --------------- | --- | --- | --- | --- |
Description
Storesconfigurationentriesinanalarmtablethatdefinesthesampleinterval,sample-type,and
thresholdparametersforanSNMPMIBobject.OnlytheSNMPMIBobjectsthatresolvetoanASN.1
primitivetypeofINTEGER(INTEGER,Integer32,Counter32,Counter64,Gauge32,orTimeTicks)willbe
monitored.
ThenoformofthiscommandremovesallRMONalarmsandallowsyoutospecifyanindextoremovea
particularRMONalarm.
| Parameter     |     |     | Description                             |     |     |
| ------------- | --- | --- | --------------------------------------- | --- | --- |
| index <INDEX> |     |     | SpecifiestheRMONalarmindex.Range:1to20. |     |     |
snmp-oid <SNMP-OID> SpecifiestheSNMPMIBobjecttobemonitoredbyRMON.
rising-threshold <RISING-THRESHOLD> SpecifiestheupperthresholdvaluefortheRMONalarm.
falling-threshold <FALLING-THRESHOLD> SpecifiesthefallingthresholdvaluefortheRMONalarm.
Thefallingthresholdmustbelessthantherising
threshold.
sample-interval <SAMPLE-INTERVAL> Sampleintervalinseconds.Default:30.
sample-type <ABSOLUTE|DELTA> SpecifiesthemethodofsamplingoftheSNMPMIBobject.
Default:Absolute.
|26

Examples
ConfiguringRMONfortheMIBobjectifOutErrors.15withanindex1,risingthresholdof2147483647
andfallingthresholdof-2134usingabsolutesamplingforasampleintervalof100seconds:
switch(config)# rmon alarm index 1 snmp-oid ifOutErrors.15 rising-threshold
2147483647
falling-threshold -2134 sample-type absolute sample-interval 100
RemovingRMONalarmwiththeindex5:
| switch(config)# |             |         | no rmon | alarm   | index | 5            |     |
| --------------- | ----------- | ------- | ------- | ------- | ----- | ------------ | --- |
| Command         | History     |         |         |         |       |              |     |
| Release         |             |         |         |         |       | Modification |     |
| 10.07orearlier  |             |         |         |         |       | --           |     |
| Command         | Information |         |         |         |       |              |     |
| Platforms       |             | Command |         | context |       | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| rmon       | alarm   | {enable |            | | disable} |        | {index  | | all} |
| ---------- | ------- | ------- | ---------- | ---------- | ------ | ------- | ------ |
| rmon alarm | {enable |         | | disable} |            | {index | <INDEX> | | all} |
| no rmon    | alarm   | [enable | |          | disable]   | [index | <INDEX> | | all] |
Description
EnablesanddisablestheRMONalarmanditsindex.RMONalarmisenabledbydefault.
| Parameter |         |     |     |     |     | Description                             |     |
| --------- | ------- | --- | --- | --- | --- | --------------------------------------- | --- |
| enable    |         |     |     |     |     | EnablestheRMONalarmindex                |     |
| disable   |         |     |     |     |     | DisablestheRMONalarmindex.              |     |
| index     | <INDEX> |     |     |     |     | SpecifiestheRMONalarmindex.Range:1to20. |     |
| all       |         |     |     |     |     | SpecifiesalltheRMONalarms.              |     |
Examples
EnablingordisablingalltheRMONalarm:
| switch(config)# |     |     | rmon | alarm | enable  | all |     |
| --------------- | --- | --- | ---- | ----- | ------- | --- | --- |
| switch(config)# |     |     | rmon | alarm | disable | all |     |
EnablingordisablingRMONalarmbyindex:
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 27

| switch(config)# |     | rmon alarm | enable | index | 1   |
| --------------- | --- | ---------- | ------ | ----- | --- |
switch(config)#
|                     |         | rmon alarm | disable | index        | 1   |
| ------------------- | ------- | ---------- | ------- | ------------ | --- |
| Command History     |         |            |         |              |     |
| Release             |         |            |         | Modification |     |
| 10.07orearlier      |         |            |         | --           |     |
| Command Information |         |            |         |              |     |
| Platforms           | Command | context    |         | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show configuration-changes |     |     |      | trap |     |
| -------------------------- | --- | --- | ---- | ---- | --- |
| show configuration-changes |     |     | trap |      |     |
Description
ShowstheSNMPconfigurationchangestrapsettings.
Example
ShowingtheSNMPconfigurationchangestrap:
| switch# show       | configuration-changes |         |      | trap      |     |
| ------------------ | --------------------- | ------- | ---- | --------- | --- |
| SNMP Configuration |                       | changes | trap | : Enabled |     |
```
| Command History     |                      |         |     |                   |     |
| ------------------- | -------------------- | ------- | --- | ----------------- | --- |
| Release             |                      |         |     | Modification      |     |
| 10.10               |                      |         |     | Commandintroduced |     |
| Command Information |                      |         |     |                   |     |
| Platforms           | Command              | context |     | Authority         |     |
| Allplatforms        | Operator(>)orManager |         |     |                   |     |
(#)
show mac-notify
show mac-notify
Description
|28

DisplayswhethertheMACnotificationfeatureintheSNMPmoduleisenabledornot.Italsodisplaysthe
trapnotificationtypesconfiguredontheLayer2portsinthesystem.
Examples
ShowingtheMACnotificationconfigurationonallconfiguredportsinthesystem:
| switch# show     | mac-notify |        |         |           |
| ---------------- | ---------- | ------ | ------- | --------- |
| MAC notification |            | global | setting | : Enabled |
| Port             | Enabled    | Traps  |         |           |
---------------------------------------
| 1/1/1  | aged    | learned | moved |         |
| ------ | ------- | ------- | ----- | ------- |
| 1/1/5  | moved   |         |       |         |
| lag101 | removed |         |       |         |
| lag104 | aged    | learned | moved | removed |
...
...
| Command History     |                      |         |     |                   |
| ------------------- | -------------------- | ------- | --- | ----------------- |
| Release             |                      |         |     | Modification      |
| 10.08               |                      |         |     | Commandintroduced |
| Command Information |                      |         |     |                   |
| Platforms           | Command              | context |     | Authority         |
| Allplatforms        | Operator(>)orManager |         |     |                   |
(#)
| show mac-notify |       | port     |     |     |
| --------------- | ----- | -------- | --- | --- |
| show mac-notify | [port | <PORTS>] |     |     |
Description
DisplaystheMACnotificationconfigurationonarangeofports.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
[port <PORTS>]
Specifiesaport,rangeofports,orlistofports.
Examples
ShowingtheMACnotificationconfigurationonarangeofports:
switch(config)# show mac-notify port 1/1/1,1/1/3,1/1/5,lag101-lag104
| MAC notification |         | global | Setting: | Enabled |
| ---------------- | ------- | ------ | -------- | ------- |
| Port             | Enabled | Traps  |          |         |
---------------------------------------
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 29

| 1/1/1        |             | aged                 | learned | moved |                   |
| ------------ | ----------- | -------------------- | ------- | ----- | ----------------- |
| 1/1/3        |             | --                   |         |       |                   |
| 1/1/5        |             | moved                |         |       |                   |
| lag101       |             | removed              |         |       |                   |
| lag102       |             | --                   |         |       |                   |
| lag103       |             | --                   |         |       |                   |
| lag104       |             | aged                 | learned | moved | removed           |
| Command      | History     |                      |         |       |                   |
| Release      |             |                      |         |       | Modification      |
| 10.08        |             |                      |         |       | Commandintroduced |
| Command      | Information |                      |         |       |                   |
| Platforms    |             | Command              | context |       | Authority         |
| Allplatforms |             | Operator(>)orManager |         |       |                   |
(#)
| show      | rmon  | alarm  |          |     |     |
| --------- | ----- | ------ | -------- | --- | --- |
| show rmon | alarm | [index | <INDEX>] |     |     |
Description
DisplaystheRMONalarmconfigurations.
| Parameter |         |     |     |     | Description                             |
| --------- | ------- | --- | --- | --- | --------------------------------------- |
| index     | <INDEX> |     |     |     | SpecifiestheRMONalarmindex.Range:1to20. |
Examples
ShowingallRMONalarmconfigurations:
| switch#  | show      | rmon  | alarm                |         |          |
| -------- | --------- | ----- | -------------------- | ------- | -------- |
| Index    |           |       | : 1                  |         |          |
| Enabled  |           |       | : true               |         |          |
| Status   |           |       | : valid              |         |          |
| MIB      | object    |       | : ifOutErrors.15     |         |          |
| Sample   | type      |       | : delta              |         |          |
| Sampling | interval  |       | : 6535               | seconds |          |
| Rising   | threshold |       | : 100                |         |          |
| Falling  | threshold |       | : 10                 |         |          |
| Last     | sampled   | value | : 0                  |         |          |
| Last     | sample    | time  | : 2020-09-21         |         | 05:58:11 |
| Index    |           |       | : 3                  |         |          |
| Enabled  |           |       | : true               |         |          |
| Status   |           |       | : invalid            |         |          |
| MIB      | object    |       | : IF-MIB::ifDescr.19 |         |          |
| Sample   | type      |       | : absolute           |         |          |
| Sampling | interval  |       | : 10000              | seconds |          |
|30

| Rising threshold  |       | : 4000 |     |
| ----------------- | ----- | ------ | --- |
| Falling threshold |       | : 10   |     |
| Last sampled      | value | : 0    |     |
ShowingRMONalarmwithalarmindex1:
| switch# show      | rmon alarm | index            | 1        |
| ----------------- | ---------- | ---------------- | -------- |
| Index             |            | : 1              |          |
| Enabled           |            | : true           |          |
| Status            |            | : valid          |          |
| MIB object        |            | : ifOutErrors.15 |          |
| Sample type       |            | : delta          |          |
| Sampling          | interval   | : 6535 seconds   |          |
| Rising threshold  |            | : 100            |          |
| Falling threshold |            | : 10             |          |
| Last sampled      | value      | : 0              |          |
| Last sample       | time       | : 2020-06-21     | 05:58:11 |
ShowingdisabledRMONalarminformation:
| switch# show        | rmon     | alarm                |              |
| ------------------- | -------- | -------------------- | ------------ |
| Index               |          | : 1                  |              |
| Enabled             |          | : false              |              |
| Status              |          | : valid              |              |
| MIB object          |          | : ifOutErrors.15     |              |
| Sample type         |          | : delta              |              |
| Sampling            | interval | : 6535 seconds       |              |
| Rising threshold    |          | : 100                |              |
| Falling threshold   |          | : 10                 |              |
| Last sampled        | value    | : 0                  |              |
| Last sample         | time     | : 2020-09-21         | 05:58:11     |
| Index               |          | : 3                  |              |
| Enabled             |          | : false              |              |
| Status              |          | : invalid            |              |
| MIB object          |          | : IF-MIB::ifDescr.19 |              |
| Sample type         |          | : absolute           |              |
| Sampling            | interval | : 10000 seconds      |              |
| Rising threshold    |          | : 4000               |              |
| Falling threshold   |          | : 10                 |              |
| Last sampled        | value    | : 0                  |              |
| Command History     |          |                      |              |
| Release             |          |                      | Modification |
| 10.07orearlier      |          |                      | --           |
| Command Information |          |                      |              |
| Platforms           | Command  | context              | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show snmp | agent-port |     |     |
| --------- | ---------- | --- | --- |
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 31

| show snmp agent-port |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- |
Description
DisplaysSNMPagentUDPportnumber.
Example
DisplayingSNMPagentUDPportnumber:
| switch# show        | snmp agent-port      |         |              |     |     |
| ------------------- | -------------------- | ------- | ------------ | --- | --- |
| SNMP agent          | port : 161           |         |              |     |     |
| Command History     |                      |         |              |     |     |
| Release             |                      |         | Modification |     |     |
| 10.07orearlier      |                      |         | --           |     |     |
| Command Information |                      |         |              |     |     |
| Platforms           | Command              | context | Authority    |     |     |
| Allplatforms        | Operator(>)orManager |         |              |     |     |
(#)
| show snmp           | community |     |     |     |     |
| ------------------- | --------- | --- | --- | --- | --- |
| show snmp community |           |     |     |     |     |
Description
DisplaysalistofallconfiguredSNMPv1/v2ccommunities.
Usage
WhenausercreatesacustomcommunitybeforeenablinganSNMPagent,AOS-CXautomatically
removesthedefaultpubliccommunityfromthesystem.
Example
DisplayingalistofallconfiguredSNMPv1/v2ccommunities:
| switch#show | snmp community |     |     |     |     |
| ----------- | -------------- | --- | --- | --- | --- |
SNMP-COMMUNITIES
-------------------------------------------------------------------
| Community |     | Access-level | ACL Name | ACL Type | View |
| --------- | --- | ------------ | -------- | -------- | ---- |
-------------------------------------------------------------------
| private  |     | ro  | my_acl  | ipv4 | view1 |
| -------- | --- | --- | ------- | ---- | ----- |
| private  |     | ro  | my_acl  | ipv6 | none  |
| private2 |     | rw  | new_Acl | ipv6 | view2 |
| private3 |     | rw  | none    | none | none  |
WhentheswitchisconfiguredtouseSNMPv3only,theoutputoftheshow snmp community
commanddisplaysthemessageSNMP v1/v2c is disabled while snmpv3-only mode is configured:
|32

| switch# show | snmp | community |     |     |     |     |
| ------------ | ---- | --------- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
--------
| Community |     |     |     | Access-level | ACL Name | ACL Type |
| --------- | --- | --- | --- | ------------ | -------- | -------- |
View
----------------------------------------------------------------------------------
--------
| SNMP v1/v2c | is disabled |     | while | snmpv3-only | mode is configured |     |
| ----------- | ----------- | --- | ----- | ----------- | ------------------ | --- |
Theoutputoftheshowsnmpcommunitycommanddoesnotdisplaythismessagewhenthecommandisissued
froma10040Switchseries.
| Command History |     |     |     |                                                     |     |     |
| --------------- | --- | --- | --- | --------------------------------------------------- | --- | --- |
| Release         |     |     |     | Modification                                        |     |     |
| 10.14           |     |     |     | Theoutputofthiscommandnowdisplaysanerrormessagewhen |     |     |
theswitchisinSNMPv3-onlymode.
| 10.10 |     |     |     | OutputhasbeenupdatedwithSNMPviewdetails.AViewcolumn |     |     |
| ----- | --- | --- | --- | --------------------------------------------------- | --- | --- |
isaddedtothecommandoutput.
| 10.08               |         |     |         | AddedACLTypecolumntothecommandoutput. |     |     |
| ------------------- | ------- | --- | ------- | ------------------------------------- | --- | --- |
| 10.07orearlier      |         |     |         | --                                    |     |     |
| Command Information |         |     |         |                                       |     |     |
| Platforms           | Command |     | context | Authority                             |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show snmp        | system |     |     |     |     |     |
| ---------------- | ------ | --- | --- | --- | --- | --- |
| show snmp system |        |     |     |     |     |     |
Description
DisplaysSNMPdescription,location,andcontactinformation.
Example
DisplayingSNMPdescription,location,andcontactinformation:
| switch# show | snmp        | system |     |     |     |     |
| ------------ | ----------- | ------ | --- | --- | --- | --- |
| SNMP system  | information |        |     |     |     |     |
----------------------------
| System description |     | :      | Aggregation | router |     |     |
| ------------------ | --- | ------ | ----------- | ------ | --- | --- |
| System location    |     | : Main | lab         |        |     |     |
| System contact     | :   | John   | Smith, Lab  | Admin  |     |     |
| Command History    |     |        |             |        |     |     |
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 33

| Release             |                      |         | Modification |     |     |     |
| ------------------- | -------------------- | ------- | ------------ | --- | --- | --- |
| 10.07orearlier      |                      |         | --           |     |     |     |
| Command Information |                      |         |              |     |     |     |
| Platforms           | Command              | context | Authority    |     |     |     |
| Allplatforms        | Operator(>)orManager |         |              |     |     |     |
(#)
| show snmp      | trap |     |     |     |     |     |
| -------------- | ---- | --- | --- | --- | --- | --- |
| show snmp trap |      |     |     |     |     |     |
Description
DisplaysallconfiguredSNMPtraps/informsreceivers.
Example
DisplayingallconfiguredSNMPtrapandinformsreceivers:
| switch# show | snmp trap |     |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- | --- |
HOST PORT TYPE VER COMMUNITY/USER NAME VRF NOTIFICATION TYPES
----------------------------------------------------------------------------------
-
| 10.10.10.10 | 162 | trap v1    | public | default | bgp        |      |
| ----------- | --- | ---------- | ------ | ------- | ---------- | ---- |
| 10.10.10.10 | 162 | inform v2c | public | default | bgp, ospf, | fan, |
mstp
| 10.10.10.10         | 162                  | inform v3 | name                     | default |     |     |
| ------------------- | -------------------- | --------- | ------------------------ | ------- | --- | --- |
| Command History     |                      |           |                          |         |     |     |
| Release             |                      |           | Modification             |         |     |     |
| 10.14               |                      |           | Updatedtheexampleoutput. |         |     |     |
| 10.07orearlier      |                      |           | --                       |         |     |     |
| Command Information |                      |           |                          |         |     |     |
| Platforms           | Command              | context   | Authority                |         |     |     |
| Allplatforms        | Operator(>)orManager |           |                          |         |     |     |
(#)
| show snmp       | views |     |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- | --- |
| show snmp views |       |     |     |     |     |     |
Description
|34

Displays the list of all the configured SNMP views.

Usage

The following table contains the status and its description of the configured SNMP views:

Status

Description

pending_validation

Default value that indicates SNMP view is yet to be validated.

operational

invalid

failed

Examples

OID and mask validated.

Invalid OID/mask.

Validation failed for reasons other than OID/mask.

Displaying the list of all the configured SNMP views:

switch# show snmp views
------------------------------------------------------
SNMP MIB Views
------------------------------------------------------
: new
View
OID Tree: sysUpTime.0
: ff
Mask
: included
Type
: pending_validation
Status

: admin

View
OID Tree: ifIndex.1
Mask
Type
Status

: ff:a0
: included
: operational

View
: user
OID Tree: sysb
: none
Mask
: excluded
Type
: invalid
Status

View
: admin
OID Tree: .1.3.6.1.2.1.1
Mask
Type
Status

: none
: excluded
: operational

Command History

Release

10.10

Command Information

Modification

Command introduced

AOS-CX 10.16.xxxx SNMP/MIB Guide | (All AOS-CX Series Switches)

35

| Platforms    | Command              | context | Authority |     |
| ------------ | -------------------- | ------- | --------- | --- |
| Allplatforms | Operator(>)orManager |         |           |     |
(#)
| show snmp     | vrf |     |     |     |
| ------------- | --- | --- | --- | --- |
| show snmp vrf |     |     |     |     |
Description
DisplaystheVRFonwhichtheSNMPagentserviceisrunning.
Example
DisplayingSNMPservicesenabledonVRF:
| switch#show  | snmp vrf |     |     |     |
| ------------ | -------- | --- | --- | --- |
| SNMP enabled | VRF      |     |     |     |
----------------------------
mgmt
default
| Command History     |                      |         |              |     |
| ------------------- | -------------------- | ------- | ------------ | --- |
| Release             |                      |         | Modification |     |
| 10.07orearlier      |                      |         | --           |     |
| Command Information |                      |         |              |     |
| Platforms           | Command              | context | Authority    |     |
| Allplatforms        | Operator(>)orManager |         |              |     |
(#)
| show snmpv3 | context |     |     |     |
| ----------- | ------- | --- | --- | --- |
| show snmpv3 | context |     |     |     |
Description
DisplaysallconfiguredSNMPcontexts.
Examples
DisplayingallconfiguredSNMPcontexts:
| switch# show | snmpv3 | context |     |     |
| ------------ | ------ | ------- | --- | --- |
--------------------------------------------------------------------------
| name |     |     | vrf | community |
| ---- | --- | --- | --- | --------- |
--------------------------------------------------------------------------
| contextA |     |     | default | private |
| -------- | --- | --- | ------- | ------- |
| contextB |     |     | vrf_A   | public  |
|36

| switch# show | snmpv3 | context |     |     |
| ------------ | ------ | ------- | --- | --- |
--------------------------------------------------------------------------
| Name | vrf |     | Community | ype[Instance_id] |
| ---- | --- | --- | --------- | ---------------- |
------------------------------------------------------------------
| A   | default |     | public | vrf |
| --- | ------- | --- | ------ | --- |
switch#
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms
Operator(>)orManager
(#)
| show snmpv3 | engine-id |     |     |     |
| ----------- | --------- | --- | --- | --- |
| show snmpv3 | engine-id |     |     |     |
Description
DisplaystheconfiguredSNMPv3snmpengine-id.
IftheSNMPv3engine-idisnotconfigured,bydefaultauniqueengine-idiscreatedbytheswitchusinga
combinationoftheenterpriseOIDvalueandtheswitch'smacaddress.
Example
DisplayingtheconfiguredSNMPv3engine-id:
| switch# show        | snmpv3                          | engine-id |              |     |
| ------------------- | ------------------------------- | --------- | ------------ | --- |
| SNMP engine-id      | : 80:00:B8:5C:08:00:09:1d:de:a5 |           |              |     |
| Command History     |                                 |           |              |     |
| Release             |                                 |           | Modification |     |
| 10.07orearlier      |                                 |           | --           |     |
| Command Information |                                 |           |              |     |
| Platforms           | Command                         | context   | Authority    |     |
| Allplatforms        | Operator(>)orManager            |           |              |     |
(#)
| show snmpv3 | security-level |     |     |     |
| ----------- | -------------- | --- | --- | --- |
| show snmpv3 | security-level |     |     |     |
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 37

Description
DisplaystheconfiguredSNMPv3securitylevel.
Examples
DisplayingtheconfiguredSNMPv3securitylevel:
| switch# show          | snmpv3               | security-level |              |     |     |
| --------------------- | -------------------- | -------------- | ------------ | --- | --- |
| SNMPv3 security-level |                      | : auth         |              |     |     |
| Command History       |                      |                |              |     |     |
| Release               |                      |                | Modification |     |     |
| 10.07orearlier        |                      |                | --           |     |     |
| Command Information   |                      |                |              |     |     |
| Platforms             | Command              | context        | Authority    |     |     |
| Allplatforms          | Operator(>)orManager |                |              |     |     |
(#)
| show snmpv3 | users |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
| show snmpv3 | users |     |     |     |     |
Description
DisplaysallconfiguredSNMPv3users.
Formoredetailsontheuserenabledstatus,seesnmpv3 security-level.
Example
DisplayingallconfiguredSNMPv3users:
| switch# show | snmpv3 | users |     |     |     |
| ------------ | ------ | ----- | --- | --- | --- |
------------------------------------------------------------------------
| User | AuthMode | PrivMode | Status Context | Access-level | View |
| ---- | -------- | -------- | -------------- | ------------ | ---- |
------------------------------------------------------------------------
| name | md5 | none | Enabled context2 | ro  | view1 |
| ---- | --- | ---- | ---------------- | --- | ----- |
context1
context3
| name2           | none | none | Disabled none                                       | ro  | view2 |
| --------------- | ---- | ---- | --------------------------------------------------- | --- | ----- |
| name3           | none | none | Disabled none                                       | ro  | none  |
| Command History |      |      |                                                     |     |       |
| Release         |      |      | Modification                                        |     |       |
| 10.10           |      |      | OutputhasbeenupdatedwithSNMPviewdetails.AViewcolumn |     |       |
isaddedtothecommandoutput.
| 10.07orearlier |     |     | --  |     |     |
| -------------- | --- | --- | --- | --- | --- |
|38

| Command      | Information          |     |         |     |           |     |     |
| ------------ | -------------------- | --- | ------- | --- | --------- | --- | --- |
| Platforms    | Command              |     | context |     | Authority |     |     |
| Allplatforms | Operator(>)orManager |     |         |     |           |     |     |
(#)
| snmp-server    |            | agent-port |          |     |     |     |     |
| -------------- | ---------- | ---------- | -------- | --- | --- | --- | --- |
| snmp-server    | agent-port |            | <PORT>   |     |     |     |     |
| no snmp-server | agent-port |            | [<PORT>] |     |     |     |     |
Description
SetstheUDPportnumberthattheSNMPmasteragentusestocommunicate.UDPport161isthe
defaultport.
ThenoformofthiscommandsetstheSNMPmasteragentporttothedefaultvalue.
| Parameter |     |     |     |     | Description                                         |     |     |
| --------- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- |
| <PORT>    |     |     |     |     | SpecifiestheUDPportnumberthattheSNMPmasteragentwill |     |     |
use.Range:1to65535.Default:161.
Examples
SettingtheSNMPmasteragentportto2000:
| switch(config)# |     | snmp-server |     | agent-port |     | 2000 |     |
| --------------- | --- | ----------- | --- | ---------- | --- | ---- | --- |
ResettingtheSNMPmasteragentporttothedefaultvalue:
| switch(config-schedule)# |             |     |         | no snmp-server |              | agent-port | 2000 |
| ------------------------ | ----------- | --- | ------- | -------------- | ------------ | ---------- | ---- |
| Command                  | History     |     |         |                |              |            |      |
| Release                  |             |     |         |                | Modification |            |      |
| 10.07orearlier           |             |     |         |                | --           |            |      |
| Command                  | Information |     |         |                |              |            |      |
| Platforms                | Command     |     | context |                | Authority    |            |      |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    |           | community |          |     |     |     |     |
| -------------- | --------- | --------- | -------- | --- | --- | --- | --- |
| snmp-server    | community |           | <STRING> |     |     |     |     |
| no snmp-server | community |           | <STRING> |     |     |     |     |
Description
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 39

AddsanSNMPv1/SNMPv2ccommunitystring.Acommunitystringislikeapasswordthatcontrols
read/writeaccesstotheSNMPagent.Anetworkmanagementprogrammustsupplythisnamewhen
attemptingtogetSNMPinformationfromtheswitch.Amaximumof10communitystringsare
supported.Onceyoucreateyourowncommunitystring,thedefaultcommunitystring(public)is
deleted.
ThenoformofthiscommandremovesthespecifiedSNMPv1/SNMPv2ccommunitystring.Whenno
communitystringexists,adefaultcommunitystringwiththevaluepublicisautomaticallydefined.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<STRING>
SpecifiestheSNMPv1/SNMPv2ccommunitystring.Range:1to32
printableASCIIcharacters,excludingspaceandquestionmark.
Subcommands
| access-level    | {ro | | rw}     |     |     |     |
| --------------- | --- | --------- | --- | --- | --- |
| no access-level |     | {ro | rw} |     |     |     |
ThissubcommandchangestheaccessleveloftheSNMPcommunity.Thedefaultaccesslevelisread-
only(ro).
Thenoformofthissubcommandchangestheaccesslevelofthecommunitytodefault.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
ro
SpecifiesRead-OnlyaccesswiththeSNMPcommunity.
| rw             |     |         |            | SpecifiesRead-WriteaccesswiththeSNMPcommunity. |     |
| -------------- | --- | ------- | ---------- | ---------------------------------------------- | --- |
| access-list    | {ip | | ipv6} | <ACL-NAME> |                                                |     |
| no access-list | {ip | | ipv6} | <ACL-NAME> |                                                |     |
ThissubcommandassociatesanACLwiththeSNMPcommunity.IfanACLisnotassociatedwiththe
SNMPcommunity,thedefaultaccessisallowedforallthehosts.
ThenoformofthissubcommandremovesassociationoftheACLwiththeSNMPcommunity.
| Parameter |     |     |     | Description              |     |
| --------- | --- | --- | --- | ------------------------ | --- |
| ip        |     |     |     | SpecifiestheIPv4ACLtype. |     |
| ipv6      |     |     |     | SpecifiestheIPv6ACLtype. |     |
<ACL-NAME> SpecifiestheACLname.Itsupportsamaximumof64characters.
Examples
SettingtheSNMPv1/SNMPv2ccommunitystringtoprivate:
| switch(config)# |     | snmp-server |     | community | private |
| --------------- | --- | ----------- | --- | --------- | ------- |
RemovingSNMPv1/SNMPv2ccommunitystringprivate:
| switch(config)# |     | no snmp-server |     | community | private |
| --------------- | --- | -------------- | --- | --------- | ------- |
|40

ConfiguringtheaccesslevelfortheSMNPcommunitytoread-only:
| switch(config-community)# |     | access-level | ro  |
| ------------------------- | --- | ------------ | --- |
ChangingtheaccessleveloftheSNMP communitytodefault:
| switch(config-community)# |     | no access-level | rw  |
| ------------------------- | --- | --------------- | --- |
AssociatinganIPv4ACLnamedmy_aclwiththeSMNPcommunity:
switch(config-community)#
|     |     | access-list | ip my_acl |
| --- | --- | ----------- | --------- |
RemovingtheassociatedIPv4ACLnamedmy_aclfromtheSNMPcommunity:
| switch(config-community)# |     | no access-list | ip my_acl |
| ------------------------- | --- | -------------- | --------- |
ConfigurationsupportedforSNMPACL:
| access-list | ip ipv4_acl   |           |     |
| ----------- | ------------- | --------- | --- |
| 10 permit   | any 4.4.4.4   | 4.4.4.1   |     |
| 20 permit   | any 3.3.3.3   | 3.3.3.1   |     |
| access-list | ipv6 ipv6_acl |           |     |
| 10 permit   | any 2001::2   | 2001::1   |     |
| 20 permit   | any 3001::2   | 3001::1   |     |
| snmp-server | vrf default   |           |     |
| snmp-server | community     | my_comm_1 |     |
| access-list | ip            | ipv4_acl  |     |
| access-list | ipv6          | ipv6_acl  |     |
ConfigurationnotsupportedforSNMPACL:
| access-list | ip ipv4_acl   |           |     |
| ----------- | ------------- | --------- | --- |
| 10 deny     | any 6.6.6.6   | 6.6.6.1   |     |
| access-list | ipv6 ipv6_acl |           |     |
| 10 deny     | any 6001::6   | 6000::1   |     |
| snmp-server | vrf default   |           |     |
| snmp-server | community     | my_comm_1 |     |
| access-list | ip            | ipv4_acl  |     |
| access-list | ipv6          | ipv6_acl  |     |
hitcountsforSNMPACLwillnotbeincremented.
Example:showaccess-listhitcountsipallwillnotshowthehitcountofSNMPACL.
| Command History |     |                                                    |     |
| --------------- | --- | -------------------------------------------------- | --- |
| Release         |     | Modification                                       |     |
| 10.14           |     | Replacedtheipv4parameterwiththeipparameter.Theipv4 |     |
parameterisdeprecated.
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 41

| Release        |             |         |         |     | Modification |
| -------------- | ----------- | ------- | ------- | --- | ------------ |
| 10.07orearlier |             |         |         |     | --           |
| Command        | Information |         |         |     |              |
| Platforms      |             | Command | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|                |           | config-community |          |       | rightsforthiscommand. |
| -------------- | --------- | ---------------- | -------- | ----- | --------------------- |
| snmp-server    |           | community        |          | view  |                       |
| snmp-server    | community |                  | <STRING> | [view | <VIEW-NAME>]          |
| no snmp-server |           | community        | <STRING> |       | [view <VIEW-NAME>]    |
Description
AssociatesanSNMP MIBviewwiththeSNMPcommunity.
ThenoformofthiscommandremovestheassociatedSNMPMIBviewfromtheSNMPcommunity.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<STRING> SpecifiestheSNMPv1/SNMPv2ccommunitystring.Range:1to32
printableASCIIcharacters,excludingspaceandquestionmark.
| <VIEW-NAME> |     |     |     |     | SpecifiestheviewnamefortheSNMPMIB view.Acceptsa |
| ----------- | --- | --- | --- | --- | ----------------------------------------------- |
maximumof32characters.
Examples
ConfiguringtheSNMPv1/SNMPv2ccommunity:
| switch(config)# |     |     | snmp-server | community | my_community |
| --------------- | --- | --- | ----------- | --------- | ------------ |
switch(config-community)#
AddingSNMP MIBviewtotheSNMPcommunity:
| switch(config-community)# |     |     |     | view | name1 |
| ------------------------- | --- | --- | --- | ---- | ----- |
RemovingSNMP MIBviewfromtheSNMP community:
| switch(config-community)# |             |     |     | no view | name1             |
| ------------------------- | ----------- | --- | --- | ------- | ----------------- |
| Command                   | History     |     |     |         |                   |
| Release                   |             |     |     |         | Modification      |
| 10.10                     |             |     |     |         | Commandintroduced |
| Command                   | Information |     |     |         |                   |
|42

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|                | config-community            |     |     | rightsforthiscommand. |
| -------------- | --------------------------- | --- | --- | --------------------- |
| snmp-server    | historical-counters-monitor |     |     |                       |
| snmp-server    | historical-counters-monitor |     |     |                       |
| no snmp-server | historical-counters-monitor |     |     |                       |
Description
EnablestheRemoteNetworkMonitoringagent(rmond)tostartcollectinghistoricalinterfacestatistics.
Thenoformofthiscommandstopsthehistoricalinterfacestatisticscollection.
Example
Enablingthermondagenttostarthistoricalinterfacestatisticscollection:
| switch(config)# | snmp-server |     | historical-counters-monitor |     |
| --------------- | ----------- | --- | --------------------------- | --- |
Disablingthermondagenttostophistoricalinterfacestatisticscollection:
| switch(config)#     | no                   | snmp-server |     | historical-counters-monitor |
| ------------------- | -------------------- | ----------- | --- | --------------------------- |
| Command History     |                      |             |     |                             |
| Release             |                      |             |     | Modification                |
| 10.07orearlier      |                      |             |     | --                          |
| Command Information |                      |             |     |                             |
| Platforms           | Command              | context     |     | Authority                   |
| Allplatforms        | Operator(>)orManager |             |     |                             |
(#)
| snmp-server | host |     |     |     |
| ----------- | ---- | --- | --- | --- |
snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]
no snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]
snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]
no snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]
snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user
<NAME> [port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]
no snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user
<NAME> [port <UDP-PORT>] [<VRF-NAME>] [notification-type <NOTIFICATION-TYPE>]
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 43

Description

Configures a trap/informs receiver to which the SNMP agent can send SNMP v1/v2c/v3 traps or v2c
informs. A maximum of 30 SNMP traps/informs receivers can be configured.

The no form of this command removes the specified trap/inform receiver.

Avoid configuring the same receiver for both SNMP traps and informs on the same UDP port for v1, v2, and v3.

Parameter

<IPv4-ADDR>

<IPv6-ADDR>

trap version <VERSION>

Description

Specifies the IP address of a trap receiver in IPv4 format
(x.x.x.x), where x is a decimal number from 0 to 255. You can
remove leading zeros. For example, the address
192.169.005.100 becomes 192.168.5.100.

Specifies the IP address of a trap receiver in IPv6 format
(x:x::x:x).

Specifies the trap notification type for SNMPv1, v2c or v3.
Available options are: v1, v2c or v3.

inform version v2c

Specifies the inform notification type for SNMPv2c.

trap version v3

user <NAME>

community <STRING>

<UDP-PORT>

<VRF-NAME>

<notification-type>

Specifies the trap notification type for SNMPv3.

Specifies the SNMPv3 user name to be used in the SNMP trap
notifications.

Specifies the name of the community string to use when
sending trap notifications. Range: 1 - 32 printable ASCII
characters, excluding space and question mark. Default:
public.

Specifies the UDP port on which notifications are sent. Range:
1 - 65535. Default: 162.

Specifies the VRF on which the SNMP agent listens for
incoming requests.

Specifies the type of notification to be sent to the trap
receiver. If no type is specified, all notifications are sent.
The supported notification types are:

n aaa-server
n alarm
n bgp
n card
n config
n entity
n fan
n interface
n lldp
n loop-protect
n mac-notify
n mstp
n mvrp
n ospf

| 44

Parameter

Description

n ospfv3
n port-security
n power
n power-ethernet
n rmon
n rpvst
n stp
n temperature
n vrrp
n vsf
n vsx

Examples

switch(config)# snmp-server host 10.10.10.10 trap version v1
switch(config)# no snmp-server host 10.10.10.10 trap version v1
switch(config)# snmp-server host a:b::c:d trap version v1
switch(config)# no snmp-server host a:b::c:d trap version v1
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
switch(config)# snmp-server host a:b::c:d trap version v2c community public
switch(config)# no snmp-server host a:b::c:d trap version v2c community public
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public
port 5000
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
port 5000
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public
port 5000 vrf default
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
port 5000 vrf default
switch(config)# snmp-server host a:b::c:d trap version v2c community public port
5000
switch(config)# no snmp-server host a:b::c:d trap version v2c community public
port 5000
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community
public
switch(config)# snmp-server host a:b::c:d inform version v2c community public
switch(config)# no snmp-server host a:b::c:d inform version v2c community public
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
port 5000
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community
public port 5000
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
port 5000 vrf default
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community
public port 5000 vrf default
switch(config)# snmp-server host a:b::c:d inform version v2c community public port
5000
switch(config)# no snmp-server host a:b::c:d inform version v2c community public
port 5000
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# snmp-server host a:b::c:d trap version v3 user Admin
switch(config)# no snmp-server host a:b::c:d trap version v3 user Admin
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin port 2000
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin port

AOS-CX 10.16.xxxx SNMP/MIB Guide | (All AOS-CX Series Switches)

45

2000
switch(config)#
|     | snmp-server |     | host | a:b::c:d | trap | version |     | v3 user Admin | port 2000 |
| --- | ----------- | --- | ---- | -------- | ---- | ------- | --- | ------------- | --------- |
switch(config)# no snmp-server host a:b::c:d trap version v3 user Admin port 2000
SNMPtrapnotificationtypeexamples:
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public
| notification-type | bgp fan | interface |     | power | entity |     |     |     |     |
| ----------------- | ------- | --------- | --- | ----- | ------ | --- | --- | --- | --- |
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
| notification-type | bgp |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
switch(config)# snmp-server host a:b::c:d inform version v3 user Admin
| notification-type | bgp fan | interface |     | power-ethernet |     |     |     |     |     |
| ----------------- | ------- | --------- | --- | -------------- | --- | --- | --- | --- | --- |
switch(config)# no snmp-server host a:b::c:d inform version v3 user Admin
| notification-type | bgp interface |     |     |     |     |     |     |     |     |
| ----------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
switch(config)# snmp-server host a:b::c:d inform version v3 user Admin
| notification-type | ?     |       |                |     |     |     |     |     |     |
| ----------------- | ----- | ----- | -------------- | --- | --- | --- | --- | --- | --- |
| aaa-server        | Sends | AAA   | notifications. |     |     |     |     |     |     |
| alarm             | Sends | Alarm | notifications. |     |     |     |     |     |     |
bgp Sends Border Gateway Protocol (BGP) state change notifications.
| card      | Sends | Card          | notifications. |                |     |                |     |     |     |
| --------- | ----- | ------------- | -------------- | -------------- | --- | -------------- | --- | --- | --- |
| config    | Sends | Configuration |                | change         |     | notifications. |     |     |     |
| entity    | Sends | Entity        | notifications. |                |     |                |     |     |     |
| fan       | Sends | Fan           | notifications. |                |     |                |     |     |     |
| interface | Sends | Interface     |                | notifications. |     |                |     |     |     |
lldp Sends Link Layer Discovery Protocol (LLDP) notifications.
| loop-protect | Sends | Loop | Protect | notifications. |     |     |     |     |     |
| ------------ | ----- | ---- | ------- | -------------- | --- | --- | --- | --- | --- |
| mac-notify   | Sends | MAC  | Notify  | notifications. |     |     |     |     |     |
mstp Sends Multiple Spanning Tree Protocol (MSTP) notifications.
mvrp Sends Multiple VLAN Registration Protocol (MVRP) notifications.
| ospf | Sends | Open | Shortest | Path | First |     | (OSPFv2) | notifications. |     |
| ---- | ----- | ---- | -------- | ---- | ----- | --- | -------- | -------------- | --- |
ospfv3 Sends Open Shortest Path First version 3 (OSPFv3) notifications.
| port-security  | Sends | Port   | Security       | notifications. |            |       |                |                |     |
| -------------- | ----- | ------ | -------------- | -------------- | ---------- | ----- | -------------- | -------------- | --- |
| power          | Sends | Power  | notifications. |                |            |       |                |                |     |
| power-ethernet | Sends | Power  | over           | Ethernet       |            | (PoE) | notifications. |                |     |
| rmon           | Sends | Remote | Network        |                | Monitoring |       | (RMON)         | notifications. |     |
rpvst Sends Rapid Per VLAN Spanning Tree (RPVST) notifications.
| snmp | Sends | Sends | Simple | Network |     | Management |     | Protocol | (SNMP) |
| ---- | ----- | ----- | ------ | ------- | --- | ---------- | --- | -------- | ------ |
notifications.
| stp         | Sends | Spanning    |     | Tree Protocol  |     | (STP) | notifications. |     |     |
| ----------- | ----- | ----------- | --- | -------------- | --- | ----- | -------------- | --- | --- |
| temperature | Sends | Temperature |     | notifications. |     |       |                |     |     |
vrrp Sends Virtual Router Redundancy Protocol (VRRP) notifications.
| vsf | Sends | Virtual | Switching |     | Framework |     | (VSF) | notifications. |     |
| --- | ----- | ------- | --------- | --- | --------- | --- | ----- | -------------- | --- |
| vsx | Sends | Virtual | System    |     | Extension |     | (VSX) | notifications. |     |
ShowSNMPtrapexample:
| switch(config)# | show snmp | trap |     |     |     |     |     |     |     |
| --------------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
------------------------------
| Host         | Port Type |     | Version | Community-Name/User-Name |     |     |     |     | vrf |
| ------------ | --------- | --- | ------- | ------------------------ | --- | --- | --- | --- | --- |
| Notification | Types     |     |         |                          |     |     |     |     |     |
----------------------------------------------------------------------------------
------------------------------
|46

| 192.168.12.239      | 162        | trap    | v3 kgbhat1   | mgmt fan |
| ------------------- | ---------- | ------- | ------------ | -------- |
| 192.168.16.190      | 162        | trap    | v2c public   | mgmt     |
| config, entity,     | interface, |         | rmon         |          |
| Command History     |            |         |              |          |
| Release             |            |         | Modification |          |
| 10.07orearlier      |            |         | --           |          |
| Command Information |            |         |              |          |
| Platforms           | Command    | context | Authority    |          |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server | response-source |     |     |     |
| ----------- | --------------- | --- | --- | --- |
snmp-server response-source {interface <IF-NAME> | <IPv4-ADDRESS> | <IPv6-ADDRESS>} [vrf
<VRF-NAME>]
no snmp-server response-source {interface <IF-NAME | <IPv4-ADDRESS> | <IPv6-ADDRESS>}
[vrf <VRF-NAME>]
Description
ConfiguresthesourceinterfaceorIPaddressforsendingSNMPresponses.EachSNMP can
independentlyhaveitsownuniqueresponsesourceIPaddress.
ThenoformofthiscommandremovesthesourceinterfacenameorIPaddressforsendingSNMP
responses.
n Itisrecommendedtousetheloopbackinterfaceoripaddressoftheloopbackinterfaceastheresponse
source.Ifadevicedoesnotsupportaloopbackinterface,thenconfigureSVIinterfaceorSVIIPaddressas
theresponsesource.
n TheactivegatewayIPaddresscannotbeconfiguredastheresponsesource.
n Itisrecommendedtolimitthemaximumnumberofresponsesourcetofive.
n Theinterfaceusedfortheresponsesourceshouldbeintheupstate.Iftheinterfaceisdown,thedefault
sourceIPwillbeused.
n Theuseofudp6ismandatoryforIPv6SNMPoperations.Forexample,youcanusethefollowingsyntax:
snmpwalk-v2c-cpublic-mALLudp6:[2100::2].1.3.6.1.2.1.1.
| Parameter           |     |     | Description |     |
| ------------------- | --- | --- | ----------- | --- |
| interface <IF-NAME> |     |     |             |     |
Specifiesthesourceinterfacename.Theinterfacecanbea
physicalinterface,loopbackinterface,orVLANinterface.
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 47

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPv4-ADDRESS> Specifies theIPv4addressofthesourceinterfacefortheSNMP
response.
<IPv6-ADDRESS>
Specifies theIPv6addressofthesourceinterfacefortheSNMP
response.
vrf <VRF-NAME> SpecifiestheVRFnameassociatedtothesourceinterfaceforthe
SNMPresponse.
Examples
Configuringaresponsesourcefortheinterface1/1/12:
switch(config)# snmp-server response-source interface 1/1/12 vrf red
Configuringaresponsesourceforinterfaceloopback10:
switch(config)# snmp-server response-source interface loopback10 vrf red
ConfiguringaresponsesourcefortheIPv4address10.0.0.1:
switch(config)# snmp-server response-source 10.0.0.1 vrf sample
ConfiguringaresponsesourcefortheIPv6address2001::1:
switch(config)# snmp-server response-source 2001::1 vrf default
| Command History     |         |         |                             |
| ------------------- | ------- | ------- | --------------------------- |
| Release             |         |         | Modification                |
| 10.13               |         |         | AddedsupportforIPv6address. |
| 10.10               |         |         | Commandintroduced.          |
| Command Information |         |         |                             |
| Platforms           | Command | context | Authority                   |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    | snmpv3-only |     |     |
| -------------- | ----------- | --- | --- |
| snmp-server    | snmpv3-only |     |     |
| no snmp-server | snmpv3-only |     |     |
Description
|48

AcceptsSNMPv3messagesonly,SNMPv1andSNMPv2cwillbedisabled.BydefaultSNMPv1,SNMPv2c
andSNMPv3willallbeenabled.
ThenoformofthiscommandrestoresthedefaultsettingandreenablesSNMPv1andSNMPv2c.
Examples
ConfiguringSNMPv3messagesonly,anddisablingSNMPv1andSNMPv2c:
| switch(config)# |             | snmp-server |         | snmpv3-only |                   |     |
| --------------- | ----------- | ----------- | ------- | ----------- | ----------------- | --- |
| Command         | History     |             |         |             |                   |     |
| Release         |             |             |         |             | Modification      |     |
| 10.10           |             |             |         |             | Commandintroduced |     |
| Command         | Information |             |         |             |                   |     |
| Platforms       | Command     |             | context |             | Authority         |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    |                | system-contact |        |          |     |     |
| -------------- | -------------- | -------------- | ------ | -------- | --- | --- |
| snmp-server    | system-contact |                | <INFO> |          |     |     |
| no snmp-server | system-contact |                |        | [<INFO>] |     |     |
Description
SetsSNMPcontactinformation.
ThenoformofthiscommandremovestheSNMPcontactinformation.
| Parameter |     |     |     |     | Description                                           |     |
| --------- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
| <INFO>    |     |     |     |     | SpecifiesSNMPcontactinformation.Range:1to128printable |     |
ASCIIcharacters,exceptforquestionmark(?).
Examples
| DefinesSNMPcontactinformationtobeJohn |     |     |     |     | Smith, Lab | Admin: |
| ------------------------------------- | --- | --- | --- | --- | ---------- | ------ |
switch(config)# snmp-server system-contact John Smith, Lab Admin
RemovesSNMPcontactinformation:
| switch(config)# |         | no  | snmp-server |     | system-contact |     |
| --------------- | ------- | --- | ----------- | --- | -------------- | --- |
| Command         | History |     |             |     |                |     |
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 49

| Release        |             |     |         |     | Modification |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    |                    | system-description |     |               |     |     |
| -------------- | ------------------ | ------------------ | --- | ------------- | --- | --- |
| snmp-server    | system-description |                    |     | <DESCRIPTION> |     |     |
| no snmp-server | system-description |                    |     |               |     |     |
Description
SetstheSNMPsystemdescription.
ThenoformofthiscommandremovestheSNMPsystemdescription.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<DESCRIPTION> SpecifiestheSNMPsystemdescription.Typicalcontenttoinclude
wouldbethefullnameandversionofthefollowing:
|     |     |     |     |     | n Hardwaretypeofthesystem |     |
| --- | --- | --- | --- | --- | ------------------------- | --- |
|     |     |     |     |     | n Softwareoperatingsystem |     |
|     |     |     |     |     | n Networkingsoftware      |     |
Range:1to64printableASCIIcharacters,exceptforthequestion
mark(?).
Examples
DefinestheSNMPsystemdescriptiontobemainSwitch:
| switch(config)# |     | snmp-server |     | system-description |     | mainSwitch |
| --------------- | --- | ----------- | --- | ------------------ | --- | ---------- |
RemovestheSNMPsystemdescription:
| switch(config)# |             | no  | snmp-server |     | system-description | mainSwitch |
| --------------- | ----------- | --- | ----------- | --- | ------------------ | ---------- |
| Command         | History     |     |             |     |                    |            |
| Release         |             |     |             |     | Modification       |            |
| 10.07orearlier  |             |     |             |     | --                 |            |
| Command         | Information |     |             |     |                    |            |
|50

| Platforms | Command |     | context |     | Authority |     |
| --------- | ------- | --- | ------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    |                 | system-location |     |        |     |     |
| -------------- | --------------- | --------------- | --- | ------ | --- | --- |
| snmp-server    | system-location |                 |     | <INFO> |     |     |
| no snmp-server | system-location |                 |     |        |     |     |
Description
SetstheSNMPlocationinformation.
ThenoformofthiscommandremovestheSNMPlocationinformation.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<INFO>
SpecifiestheSNMPlocationinformation.Range:1to128printable
ASCIIcharacters,exceptforthequestionmark(?).
Examples
| DefinestheSNMPlocationinformationtobeMain |     |             |     |                 |     | Lab:     |
| ----------------------------------------- | --- | ----------- | --- | --------------- | --- | -------- |
| switch(config)#                           |     | snmp-server |     | system-location |     | Main Lab |
RemovestheSNMPlocationinformation:
| switch(config)# |             | no  | snmp-server |     | system-location |     |
| --------------- | ----------- | --- | ----------- | --- | --------------- | --- |
| Command         | History     |     |             |     |                 |     |
| Release         |             |     |             |     | Modification    |     |
| 10.07orearlier  |             |     |             |     | --              |     |
| Command         | Information |     |             |     |                 |     |
| Platforms       | Command     |     | context     |     | Authority       |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server |     | trap |     |     |     |     |
| ----------- | --- | ---- | --- | --- | --- | --- |
snmp-server trap {cpu-utilization | memory-utilization | rmon-events}
no snmp-server trap {cpu-utilization | memory-utilization | rmon-events}
Description
EnablestheSNMPtraps.TheSNMPtrapsareenabledbydefault.
ThenoformofthiscommanddisablestheSNMPtraps.
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 51

| Parameter          |     | Description                       |     |
| ------------------ | --- | --------------------------------- | --- |
| cpu-utilization    |     | EnablestheCPUutilizationtraps.    |     |
| memory-utilization |     | Enablesthememoryutilizationtraps. |     |
| rmon-events        |     | EnablestheRMONeventtraps.         |     |
Examples
EnablingtheSNMPtraps:
| switch(config)# | snmp-server | trap cpu-utilization    |     |
| --------------- | ----------- | ----------------------- | --- |
| switch(config)# | snmp-server | trap memory-utilization |     |
| switch(config)# | snmp-server | trap rmon-events        |     |
DisablingtheSNMPtraps:
| switch(config)# | no snmp-server | trap cpu-utilization    |     |
| --------------- | -------------- | ----------------------- | --- |
| switch(config)# | no snmp-server | trap memory-utilization |     |
switch(config)#
|     | no snmp-server | trap rmon-events |     |
| --- | -------------- | ---------------- | --- |
DisplayingtheSNMPtrapconfiguration:
| switch(config)#  | show running-config | all | inc | snmp |
| ---------------- | ------------------- | --------- | ---- |
| snmp-server trap | rmon-events         |           |      |
| snmp-server trap | cpu-utilization     |           |      |
| snmp-server trap | memory-utilization  |           |      |
DisplayingCPUandMemoryusage:
| switch(config)#    | show system       |     |     |
| ------------------ | ----------------- | --- | --- |
| Hostname           | : XXXX            |     |     |
| System Description | : XX.10.07.0001CI |     |     |
| System Contact     | :                 |     |     |
| System Location    | :                 |     |     |
| Vendor             | : Aruba           |     |     |
Product Name : JLXXXX XXXX Base Chassis/3xFT/18xFans/Cbl Mgr/X462 Bundle
| Chassis Serial   | Nbr : SG6ZOO9068  |     |     |
| ---------------- | ----------------- | --- | --- |
| Base MAC Address | : f40343-806400   |     |     |
| AOS-CX Version   | : XX.10.07.0001CI |     |     |
| Time Zone        | : UTC             |     |     |
| Up Time          | : 8 minutes       |     |     |
| CPU Util (%)     | : 1               |     |     |
| Memory Usage     | (%) : 10          |     |     |
Command History
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
Command Information
|52

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    | trap                                | aaa-server-reachability-status |     |
| -------------- | ----------------------------------- | ------------------------------ | --- |
| snmp-server    | trap aaa-server-reachability-status |                                |     |
| no snmp-server | trap aaa-server-reachability-status |                                |     |
Description
EnablestheSNMPtrapforAAAserverstatus.Whenenabled,trapsaresentwheneverAAAserver
(RADIUS,TACACS)statuschangesfromreachabletounreachableandviceversa.
ThenoformofthiscommanddisablessendingSNMPtrapforAAAserverstatus.
Examples
EnablingtheSNMPtrapforAAAserverstatus:
switch(config)# snmp-server trap aaa-server-reachability-status
DisablingtheSNMPtrapforAAAserverstatus:
switch(config)# no snmp-server trap aaa-server-reachability-status
| Command History |     |     |                                                    |
| --------------- | --- | --- | -------------------------------------------------- |
| Release         |     |     | Modification                                       |
| 10.10           |     |     | Commandintroducedon4100i,6000,6100,8100,8320,8325, |
8360,8400,9300,and10000switches.
| 10.09               |         |         | Commandintroducedon6200,6300and6400switches. |
| ------------------- | ------- | ------- | -------------------------------------------- |
| Command Information |         |         |                                              |
| Platforms           | Command | context | Authority                                    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    | trap                       | configuration-changes |     |
| -------------- | -------------------------- | --------------------- | --- |
| snmp-server    | trap configuration-changes |                       |     |
| no snmp-server | trap configuration-changes |                       |     |
Description
EnablessendingSNMPtrapswhenevertheconfigurationchanges.Configurationtrapgenerationis
disabledbydefault.
ThenoformofthiscommanddisablessendingSNMPtrapsforconfigurationchanges.
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 53

| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
configuration-changes SpecifiesSNMPtrapsforconfigurationchanges.
Examples
EnablingtheSNMPtrapsforconfigurationchanges:
| switch(config)# | snmp-server |     | trap | configuration-changes |
| --------------- | ----------- | --- | ---- | --------------------- |
DisablingtheSNMPtrapsforconfigurationchanges:
| switch(config)#     | no      | snmp-server |     | trap configuration-changes |
| ------------------- | ------- | ----------- | --- | -------------------------- |
| Command History     |         |             |     |                            |
| Release             |         |             |     | Modification               |
| 10.10               |         |             |     | Commandintroduced          |
| Command Information |         |             |     |                            |
| Platforms           | Command | context     |     | Authority                  |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    | trap            | mac-notify |     |     |
| -------------- | --------------- | ---------- | --- | --- |
| snmp-server    | trap mac-notify |            |     |     |
| no snmp-server | trap mac-notify |            |     |     |
Description
EnablestheMACnotificationtrapswithintheSNMPmoduleatagloballevel.Whenenabled,trapsare
sentforinterfacesthatareconfiguredforMACnotificationevents.
ThenoformofthiscommanddisablessendingMACnotificationtrapsatagloballevel.Whendisabled,
existingmac-notifyinterfaceconfigurationispreservedbutMACnotificationeventsonconfigured
interfaceswillnotcauseSNMPtrapstobetransmitted.
Examples
EnablingtheSNMPMACnotificationfeatureinthesystemglobally:
| switch(config)# | snmp-server |     | trap | mac-notify |
| --------------- | ----------- | --- | ---- | ---------- |
DisablingtheSNMPMACnotificationfeatureinthesystemglobally:
| switch(config)# | no  | snmp-server |     | trap mac-notify |
| --------------- | --- | ----------- | --- | --------------- |
| Command History |     |             |     |                 |
|54

| Release             |         |         |     | Modification      |
| ------------------- | ------- | ------- | --- | ----------------- |
| 10.08               |         |         |     | Commandintroduced |
| Command Information |         |         |     |                   |
| Platforms           | Command | context |     | Authority         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    | trap        | module |     |     |
| -------------- | ----------- | ------ | --- | --- |
| snmp-server    | trap module |        |     |     |
| no snmp-server | trap module |        |     |     |
Description
EnablesSNMPtrapgenerationformodules.Moduletrapgenerationisenabledbydefault.Generates
themoduleeventtrapswheneveramodularlineorfabriccardchangesstate,whichincludesinserted,
removed,ready,anddown,aswellaswhenamodularcardisunrecognized.
ThenoformofthiscommanddisablestheSNMPtrapgenerationformoduleevents.
| Parameter |     |     |     | Description                        |
| --------- | --- | --- | --- | ---------------------------------- |
| module    |     |     |     | SpecifiesSNMPtrapsformoduleevents. |
Examples
EnablingtheSNMPtrapsformodules:
| switch(config)# | snmp-server |     | trap | module |
| --------------- | ----------- | --- | ---- | ------ |
DisablingtheSNMPtrapsformodules:
| switch(config)#     | no   | snmp-server    |     | trap module       |
| ------------------- | ---- | -------------- | --- | ----------------- |
| switch(config)#     | show | running-config |     |                   |
| no snmp-server      | trap | module         |     |                   |
| Command History     |      |                |     |                   |
| Release             |      |                |     | Modification      |
| 10.10               |      |                |     | Commandintroduced |
| Command Information |      |                |     |                   |
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 55

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6400 config Administratorsorlocalusergroupmemberswithexecution
| 8400 |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --------------------- |
9300
9300S
10040
| snmp-server    | trap               | port-security |     |     |
| -------------- | ------------------ | ------------- | --- | --- |
| snmp-server    | trap port-security |               |     |     |
| no snmp-server | trap port-security |               |     |     |
Description
EnablesSNMPport-securityviolationtrapsonthesystem.Port-securityviolationtrapsareenabledby
default.
ThenoformofthiscommanddisablestheSNMPport-securityviolationtrapsonthesystem.
| Parameter     |     |     |     | Description                         |
| ------------- | --- | --- | --- | ----------------------------------- |
| port-security |     |     |     | SpecifiesSNMPtrapsforport-security. |
Examples
EnablingtheSNMPport-securityviolationtrapsonthesystem:
| switch(config)# | snmp-server |     | trap | port-security |
| --------------- | ----------- | --- | ---- | ------------- |
DisablingtheSNMPport-securityviolationtrapsonthesystem:
| switch(config)#     | no      | snmp-server |     | trap port-security |
| ------------------- | ------- | ----------- | --- | ------------------ |
| Command History     |         |             |     |                    |
| Release             |         |             |     | Modification       |
| 10.10               |         |             |     | Commandintroduced  |
| Command Information |         |             |     |                    |
| Platforms           | Command | context     |     | Authority          |
4100i config Administratorsorlocalusergroupmemberswithexecution
| 5420 |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --------------------- |
6000
6100
6200
6300
6400
8100
8360
|56

| snmp-server | trap snmp |     |     |
| ----------- | --------- | --- | --- |
snmp-server trap snmp {authentication | coldstart | warmstart} [vrf <VRF_NAME>]
no snmp-server trap snmp {authentication | coldstart | warmstart} [vrf <VRF_NAME>]
Description
EnablesSNMPv2MIBtraps.TheSNMPv2trapsaredisabledbydefault.
ThenoformofthiscommanddisablestheSNMPv2MIBtraps.
SNMPv2MIBsupportsthefollowingtraps:
n authentication: AuthenticationtrapissentwhentheSNMPserverreceivesaprotocolmessagethat
isnotproperlyauthenticated.
n coldstart: Acoldstarttrapissentwhentheswitchreboots.
n warmstart: AwarmstarttrapissentwhenthereisauserinterventiontoenableordisabletheSNMP
serviceontheswitch.
SNMPv2AuthenticationtrapsdonotsupportsourceIPconfiguration.
| Parameter      |     | Description                                       |     |
| -------------- | --- | ------------------------------------------------- | --- |
| authentication |     | Enablestheauthenticationtraps.                    |     |
| coldstart      |     | Enablesthecoldstarttraps.                         |     |
| warmstart      |     | Enablesthewarmstarttraps.                         |     |
| <VRF_NAME>     |     | SpecifiestheVRFname.EnablestheSNMPv2trapsforaVRF. |     |
Examples
EnablingallSNMPv2traps:
| switch(config)# | snmp-server | trap snmp |     |
| --------------- | ----------- | --------- | --- |
EnablingonlySNMPv2authenticationtraps:
| switch(config)# | snmp-server | trap snmp | authentication |
| --------------- | ----------- | --------- | -------------- |
DisablingallSNMPtraps:
| switch(config)# | no snmp-server | trap | snmp |
| --------------- | -------------- | ---- | ---- |
Command History
| Release |     | Modification      |     |
| ------- | --- | ----------------- | --- |
| 10.10   |     | Commandintroduced |     |
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 57

| Command Information |         |         |           |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- |
| Platforms           | Command | context | Authority |     |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server | trap-source |     | interface | vrf |     |
| ----------- | ----------- | --- | --------- | --- | --- |
snmp-server trap-source {interface <IF-NAME> | <IPv4-Address> | <IPv6-Address>} [vrf
<VRF-NAME>]
no snmp-server trap-source {interface <IF-NAME> | <IPv4-Address> | <IPv6-Address>} [vrf
<VRF-NAME>]
Description
ConfiguresSNMPtrapsourceinterfaceorIPaddressforaVRF.
ThenoformofthiscommandremovestheSNMPtrap-sourceconfigurationforaVRF.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<IF-NAME>
Specifiesthesourceinterfacename.Interfacenamecanbe
physicalinterface,loopbackinterface,LAGinterface,orVLAN
interface.
<IPv4-Address> SpecifiestheIPv4addressofsourceinterfacefortheSNMPtrap.
<IPv6-Address> SpecifiestheIPv6addressofsourceinterfacefortheSNMPtrap.
<VRF-NAME> SpecifiesthenameofaVRFassociatedtothesourceinterfacefor
theSNMPtrap.
Examples
ConfiguringSNMPtrapsourceinterfaceforaVRF.
switch(config)# snmp-server trap-source interface 1/1/12 vrf sample
switch(config)# snmp-server trap-source interface loopback10 vrf sample
switch(config)# snmp-server trap-source interface vlan23 vrf sample
ConfiguringSNMPtrapsourceIPaddressforaVRF.
| switch(config)#     | snmp-server |     | trap-source  | 10.0.0.1    | vrf red |
| ------------------- | ----------- | --- | ------------ | ----------- | ------- |
| switch(config)#     | snmp-server |     | trap-source  | 1001::1 vrf | red     |
| Command History     |             |     |              |             |         |
| Release             |             |     | Modification |             |         |
| 10.07orearlier      |             |     | --           |             |         |
| Command Information |             |     |              |             |         |
|58

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    | trap     | vsx |     |     |
| -------------- | -------- | --- | --- | --- |
| snmp-server    | trap vsx |     |     |     |
| no snmp-server | trap vsx |     |     |     |
Description
EnablessendingtheSNMPtrapsforVSXrelatedevents.VSXtrapgenerationisdisabledbydefault.
ThenoformofthiscommanddisablessendingtheSNMPtrapsforVSXrelatedevents.
ThetrapsupportisavailableforthefollowingVSXevents:
ISLupanddown
n
n KAupanddown
n MCLAGupanddown
| Parameter |     |     |     | Description                     |
| --------- | --- | --- | --- | ------------------------------- |
| vsx       |     |     |     | SpecifiesSNMPtrapsforVSXevents. |
Examples
EnablingtheVSXtraps:
| switch(config)# | snmp-server |     | trap          | vsx  |
| --------------- | ----------- | --- | ------------- | ---- |
| switch(config)# | show        | vsx | configuration | trap |
| SNMP traps      | : Enabled   |     |               |      |
DisablingtheVSXtraps:
| switch(config)#     | no         | snmp-server |               | trap vsx     |
| ------------------- | ---------- | ----------- | ------------- | ------------ |
| switch(config)#     | show       | vsx         | configuration | trap         |
| SNMP traps          | : Disabled |             |               |              |
| Command History     |            |             |               |              |
| Release             |            |             |               | Modification |
| 10.07orearlier      |            |             |               | --           |
| Command Information |            |             |               |              |
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 59

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server | view |     |     |     |
| ----------- | ---- | --- | --- | --- |
snmp-server view <VIEWNAME> <OID_TREE> [<MASK>] <included/excluded>
no snmp-server view <VIEWNAME> <OID_TREE> [<MASK>] <included/excluded>
Description
ConfiguresanSNMPMIBview.
ThenoformofthiscommandremovesthespecifiedSNMPMIBview.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<VIEWNAME>
SpecifiesthenameoftheSNMPMIBview.Supportsuptoa
maximumof32characters.
<OID_TREE> SpecifiestheOIDtreetobeincludedorexcludedinSNMPMIB
view.
| <MASK> |     |     | SpecifiestheOIDmaskvalue.Thevaluesmustbeinhexadecimal |     |
| ------ | --- | --- | ----------------------------------------------------- | --- |
characterseparatedwith:(colon).
<included/excluded> SpecifiestheOIDtreethatisincludedinorexcludedfromthe
SNMP MIB view.
Usage
Youcanconfigureamaximumof50SNMPMIBviews.ThefollowingVTYmessageisdisplayedwhenthe
configurationexceedsthemaximumSNMPMIBviews:
switch(config)# snmp-server view name51 1.3.6.1.2.1.1 fe:00 included
| Configuration | failed: | Maximum allowed | views | are configured. |
| ------------- | ------- | --------------- | ----- | --------------- |
Examples
ConfiguringtheSNMP MIB views:
switch(config)# snmp-server view name1 .1.3.6.1.2.1.2.2.1.1.1 FF:A0 included
switch(config)# snmp-server view name2 IF-MIB::ifindex included
switch(config)# snmp-server view name4 1.3.6.1.2.1.1 fe:00 included
RemovinganSNMPMIBview:
switch(config)# no snmp-server view name4 1.3.6.1.2.1.1 fe:00 included
| Command History |     |     |                    |     |
| --------------- | --- | --- | ------------------ | --- |
| Release         |     |     | Modification       |     |
| 10.10           |     |     | Commandintroduced. |     |
|60

| Command Information |         |         |     |           |
| ------------------- | ------- | ------- | --- | --------- |
| Platforms           | Command | context |     | Authority |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    | vrf            |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| snmp-server    | vrf <VRF-NAME> |     |     |     |
| no snmp-server | vrf <VRF-NAME> |     |     |     |
Description
ConfiguresaVRFonwhichtheSNMPagentlistensforincomingrequests.Bydefault,theSNMPagent
doesnotlistenonanyVRF.4100i,6000,and6100onlysupportdefaultVRF.The SNMP agent can
| listen on multiple | VRFs. |     |     |     |
| ------------------ | ----- | --- | --- | --- |
ThenoformofthiscommandstopstheSNMPagentfromlisteningforincomingrequestsonthe
specifiedVRF.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<VRF-NAME>
SpecifiesthenameofaVRF.
Examples
ConfiguringtheSNMPagenttolistenonVRFdefault.
| switch(config)# | snmp-server |     | vrf | default |
| --------------- | ----------- | --- | --- | ------- |
ConfiguringtheSNMPagenttolistenonVRFmgmt.
| switch(config)# | snmp-server |     | vrf | mgmt |
| --------------- | ----------- | --- | --- | ---- |
ConfiguringtheSNMPagenttolistenonused-definedVRFmyvrf.
| switch(config)# | snmp-server |     | vrf | myvrf |
| --------------- | ----------- | --- | --- | ----- |
StoppingtheSNMPagentfromlisteningonVRFdefault.
| switch(config)#     | no  | snmp-server |     | vrf default  |
| ------------------- | --- | ----------- | --- | ------------ |
| Command History     |     |             |     |              |
| Release             |     |             |     | Modification |
| 10.07orearlier      |     |             |     | --           |
| Command Information |     |             |     |              |
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 61

| Platforms |     | Command | context | Authority |     |     |
| --------- | --- | ------- | ------- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmpv3    | context |        |                  |            |            |           |
| --------- | ------- | ------ | ---------------- | ---------- | ---------- | --------- |
| snmpv3    | context | <NAME> | vrf <VRF-NAME>   | [community |            | <STRING>] |
| no snmpv3 | context | <NAME> | [vrf <VRF-NAME>] |            | [community | <STRING>] |
Description
CreatesanSNMPv3contextonthespecifiedVRF.
ThenoformofthiscommandremovesthespecifiedSNMPcontext.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<NAME>
Specifiesthenameofthecontext.Range:1to32printableASCII
characters,excludingspaceandquestionmark(?).
vrf <VRF-NAME> SpecifiestheVRFassociatedwiththecontext.Default:default.
community <STRING> SpecifiestheSNMPcommunitystringassociatedwiththecontext.
Range:1to32printableASCIIcharacters,excludingspaceand
questionmark.Default:public.
Examples
CreatinganSNMPv3contextnamednewContext:
| switch(config)# |     | snmpv3 | context | newContext |     |     |
| --------------- | --- | ------ | ------- | ---------- | --- | --- |
CreatinganSNMPv3contextnamednewContextonVRFmyVrfandwithcommunitystringprivate.
switch(config)# snmpv3 context newContext vrf myVrf community private
RemovingtheSNMPv3contextnamednewContextonVRFmyVrf:
| switch(config)# |             | no      | snmpv3 context | newContext   |     | vrf myVrf |
| --------------- | ----------- | ------- | -------------- | ------------ | --- | --------- |
| Command         | History     |         |                |              |     |           |
| Release         |             |         |                | Modification |     |           |
| 10.07orearlier  |             |         |                | --           |     |           |
| Command         | Information |         |                |              |     |           |
| Platforms       |             | Command | context        | Authority    |     |           |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
|62

| snmpv3    | engine-id |             |     |     |
| --------- | --------- | ----------- | --- | --- |
| snmpv3    | engine-id | <ENGINE-ID> |     |     |
| no snmpv3 | engine-id | <ENGINE-ID> |     |     |
Description
ConfigurestheSNMPv3SNMPengine-idallowinganadministratortoconfigureauniqueSNMPengine-
idfortheswitch.Thisengine-idisusedbytheNMSmanagementtooltoidentifyanddistinguish
multipleswitchesonthesamenetwork.
Thenoformofthiscommandrestoresthedefaultengine-id,createdbytheswitchusingacombination
oftheenterpriseOIDvalueandtheswitch'smacaddress.
| Parameter   |     |     |     | Description                                    |
| ----------- | --- | --- | --- | ---------------------------------------------- |
| <ENGINE-ID> |     |     |     | SNMPv3SNMPengine-idincolonseparatedhexadecimal |
notation.
Examples
ConfiguringtheSNMPv3engine-id:
switch(config)#
| switch(config)# |     | snmpv3 | engine-id |     |
| --------------- | --- | ------ | --------- | --- |
WORD SNMPv3 snmp engine-id in colon seperated hexadecimal notation
switch(config)# snmpv3 engine-id 01:23:45:67:89:ab:cd:ef:01:23:45:67
RestoringthedefaultSNMPv3engine-id:
| switch(config)# |             | no  | snmpv3 engine-id |              |
| --------------- | ----------- | --- | ---------------- | ------------ |
| Command         | History     |     |                  |              |
| Release         |             |     |                  | Modification |
| 10.07orearlier  |             |     |                  | --           |
| Command         | Information |     |                  |              |
| Platforms       | Command     |     | context          | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmpv3    | security-level |     |                       |     |
| --------- | -------------- | --- | --------------------- | --- |
| snmpv3    | security-level |     | {auth | auth-privacy} |     |
| no snmpv3 | security-level |     | {auth | auth-privacy} |     |
Description
ConfigurestheSNMPv3securitylevel.ThesecurityleveldetermineswhichSMNPv3usersdefinedbythe
| commandsnmpv3 |     | userareabletoconnect. |     |     |
| ------------- | --- | --------------------- | --- | --- |
Thenoformofthiscommandchangesthesecuritylevelasfollows:
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 63

n no snmpv3 security-level auth:Setsthesecurityleveltoauth-privacy.
n no snmpv3 security-level auth-privacy:Setsthesecurityleveltonoauthenticationorprivacy,
allowinganySNMPusertoconnect.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
auth SNMPv3usersthatsupportauthentication,orauthenticationand
privacyareallowed.
auth-privacy OnlySNMPv3userswithbothauthenticationandprivacyare
allowed.ThisisthehighestlevelofSNMPv3security.Default.
Examples
SettingtheSNMPv3securityleveltoauthenticationandprivacy:
| switch(config)# | snmpv3 | security-level |     | auth-privacy |
| --------------- | ------ | -------------- | --- | ------------ |
SettingtheSNMPv3securityleveltoauthenticationonly:
| switch(config)# | snmpv3 | security-level |     | auth |
| --------------- | ------ | -------------- | --- | ---- |
SettingtheSNMPv3securityleveltonoauthenticationandnoprivacy:
switch(config)#
|     | no  | snmpv3 security-level |     | auth-privacy |
| --- | --- | --------------------- | --- | ------------ |
RestoringthedefaultSNMPv3securityleveltoauthenticationandprivacy:
| switch(config)#     | no      | snmpv3 security-level |              | auth |
| ------------------- | ------- | --------------------- | ------------ | ---- |
| Command History     |         |                       |              |      |
| Release             |         |                       | Modification |      |
| 10.07orearlier      |         |                       | --           |      |
| Command Information |         |                       |              |      |
| Platforms           | Command | context               | Authority    |      |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmpv3 user |        |     |     |     |
| ----------- | ------ | --- | --- | --- |
| snmpv3 user | <NAME> |     |     |     |
[auth <AUTH-PROTO> auth-pass [{plaintext | ciphertext} <AUTH-PASS>]]
[priv <PRIV-PROTO> priv-pass [{plaintext | ciphertext} <PRIV-PASS>]]
| [access-level  | ro|rw] |     |     |     |
| -------------- | ------ | --- | --- | --- |
| no snmpv3 user | <NAME> |     |     |     |
|64

[auth <AUTH-PROTO> auth-pass [{plaintext | ciphertext} <AUTH-PASS>]]
[priv <PRIV-PROTO> priv-pass [{plaintext | ciphertext} <PRIV-PASS>]]
[access-level ro|rw]

Description

Creates an SNMPv3 user and adds it to an SNMPv3 context. The SNMPv3 security level (set with
command snmpv3 security-level) determines which users are allowed to authenticate.

The no form of this command removes the specified SNMPv3 user.

When updating the authentication protocols and privacy protocols for the existing SNMPv3 users, you must also

update the access level. Otherwise, the access level will be set to read-only.

Parameter

<NAME>

access-level

auth <AUTH-PROTO>

auth-pass [{plaintext | ciphertext} <AUTH-PASS>]

priv <PRIV-PROTO>

priv-pass [{plaintext | ciphertext} <PRIV-PASS>]

Description

Specifies the SNMPv3 username. Range 1 to
32 printable ASCII characters, excluding
space and question mark (?).

Configures the access level for the SNMPv3
user:

n ro: Allow read-only access for the

SNMPv3 user

n rw: Allow read-write access for the

SNMPv3 user

Sets the authentication protocol used to
validate user logins. Supported protocols
are md5, sha, sha224, sha256, sha384, and
sha512.

Specifies the SNMPv3 user authentication
password. Range for plaintext is 8 to 32
printable ASCII characters, excluding space
and question mark (?). Range for ciphertext
is 1 to 256 printable ASCII characters.
Ciphertext is used when copying user
configuration settings between switches.

NOTE: Authentication passwords that
include special characters must be enclosed
in single quotation marks ('). For example,
'auth-pwd20246!@#'.

Sets the SNMPv3 privacy protocol
(encryption method). Supported privacy
protocols are aes, aes192, aes256, and des.

Specifies the SNMPv3 user privacy
encryption password. Range for plaintext is
8 to 32 printable ASCII characters, excluding
space and question mark (?). Range for
ciphertext is 1 to 256 printable ASCII
characters. Ciphertext is used when copying
user configuration settings between
switches.

AOS-CX 10.16.xxxx SNMP/MIB Guide | (All AOS-CX Series Switches)

65

| Parameter |     |     |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | --- | --- | ----------- |
NOTE:Authenticationpasswordsthat
includespecialcharactersmustbeenclosed
insinglequotationmarks(').Forexample,
'priv-pwd20246!@#'.
Whentheauthenticationpasswordisnotprovidedonthecommandline,plaintextauthenticationpassword
promptingoccursuponpressingEnter,followedbyprivacyencryptionprotocolprompting,andfinallyplaintext
encryptionpasswordprompting.Theenteredpasswordcharactersaremaskedwithasterisks.
Whentheauthenticationtypeandpasswordplustheprivacyprotocol(encryptionmethod)areprovidedonthe
commandlinebuttheencryptionpasswordisnotprovided,plaintextencryptionpasswordpromptingoccurs
uponpressingEnter.Theenteredpasswordcharactersaremaskedwithasterisks.
Examples
DefiningSNMPv3userAdmin1usingshaauthenticationanddesprivacyencryptionwithprovided
plaintextpasswords:
switch(config)# snmpv3 user Admin1 auth sha auth-pass plaintext F82#450h
|     |     | priv | des | priv-pass |     | plaintext | F82#4eva |
| --- | --- | ---- | --- | --------- | --- | --------- | -------- |
DefiningSNMPv3userAdmin2usingMD5authenticationandAESprivacyencryptionwithprovided
authenticationpasswordandprivacyencryptiontypebutpromptedencryptionpassword:
switch(config)# snmpv3 user Admin2 auth md5 auth-pass plaintext F82#450h
|           |         | priv       | aes        | priv-pass |               |          |     |
| --------- | ------- | ---------- | ---------- | --------- | ------------- | -------- | --- |
| Enter the | privacy | encryption |            |           | key: ******** |          |     |
| Re-Enter  | the     | privacy    | encryption |           | key:          | ******** |     |
DefiningSNMPv3userAdmin2usingMD5authenticationandAESprivacyencryptionwithplaintext
passwordpromptingandprivacyencryptionselection:
| switch(config)# |                | snmpv3         | user       | Admin2     |               | auth md5 | auth-pass |
| --------------- | -------------- | -------------- | ---------- | ---------- | ------------- | -------- | --------- |
| Enter the       | authentication |                |            | password:  |               | ******** |           |
| Re-Enter        | the            | authentication |            | password:  |               | ******** |           |
| Configure       | the            | privacy        | protocol   |            | (y/n)?        | y        |           |
| Enter the       | privacy        | protocol       |            | (aes/des)? |               | aes      |           |
| Enter the       | privacy        | encryption     |            |            | key: ******** |          |           |
| Re-Enter        | the            | privacy        | encryption |            | key:          | ******** |           |
RemovingSNMPv3userAdmin1:
| switch(config)# |     | no  | snmpv3 | user | Admin1 |     |     |
| --------------- | --- | --- | ------ | ---- | ------ | --- | --- |
|66

CreatinganSNMPuseronswitch1andthencreatingthesameuseronswitch2bycopyingfromthe
switch1configuration:
Onswitch1,configureausernamedAdmin3,andthenusetheshow running-configcommandto
displayswitchconfiguration.Saveacopyofthefullsnmpv3 usercommand(shownbyshow running-
config).Thissavedcommandisusedonswitch2.
switch1(config)# snmpv3 user Admin3 auth sha auth-pass plaintext F82#450h
|                        | priv                | des priv-pass | plaintext | F82#4eva |
| ---------------------- | ------------------- | ------------- | --------- | -------- |
| switch1(config)#       | exit                |               |           |          |
| switch1#               | show running-config |               |           |          |
| Current configuration: |                     |               |           |          |
!
| !Version | AOS-CX xx.xx.xx.xxxxxx |     |     |     |
| -------- | ---------------------- | --- | --- | --- |
!
snmpv3 user Admin3 auth sha auth-pass ciphertext AQBaf2d...FJVcZ3o=
| priv des   | priv-pass | ciphertext AQBaH2p...2jfTFwQ= |     |     |
| ---------- | --------- | ----------------------------- | --- | --- |
| ssh server | vrf mgmt  |                               |     |     |
!
| interface   | mgmt |     |     |     |
| ----------- | ---- | --- | --- | --- |
| no shutdown |      |     |     |     |
| ip dhcp     |      |     |     |     |
vlan 1
Onswitch2,executethesnmpv3 usercommandthatyousavedfromswitch1(asshownbyshow
running-config).Thiscreatestheuseronswitch2withthesameconfiguration.
switch2(config)# snmpv3 user Admin3 auth sha auth-pass ciphertext
AQBaf2d...FJVcZ3o=
|     | priv | des priv-pass | ciphertext | AQBaH2p...2jfTFwQ= |
| --- | ---- | ------------- | ---------- | ------------------ |
Thefollowingcommandsetsaread-writeaccesslevelforanSNMPv3userwiththeusernameuser1.
switch(config)# snmpv3 user user1 auth md5 auth-pass plaintext abc1234 access-
| level rw        |     |     |                                                      |     |
| --------------- | --- | --- | ---------------------------------------------------- | --- |
| Command History |     |     |                                                      |     |
| Release         |     |     | Modification                                         |     |
| 10.13           |     |     | Followingauthenticationprotocolsaresupported:sha224, |     |
sha256,sha384,andsha512.
Followingprivacyprotocolsaresupported:aes192andaes256.
| 10.09               |         |         | Theaccess-levelparameterwasintroduced. |     |
| ------------------- | ------- | ------- | -------------------------------------- | --- |
| 10.07orearlier      |         |         | --                                     |     |
| Command Information |         |         |                                        |     |
| Platforms           | Command | context | Authority                              |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 67

| snmpv3    | user | view        |      |                  |     |     |
| --------- | ---- | ----------- | ---- | ---------------- | --- | --- |
| snmpv3    | user | <USER-NAME> | view | <VIEW-NAME>      |     |     |
| no snmpv3 | user | <USER-NAME> |      | view <VIEW-NAME> |     |     |
Description
AssociatesauserwithanexistingSNMPMIBview.
ThenoformofthiscommandremovestheassociateduserfromthespecifiedSNMPMIBview.
| Parameter   |     |     |     |     | Description                                     |     |
| ----------- | --- | --- | --- | --- | ----------------------------------------------- | --- |
| <USER-NAME> |     |     |     |     | SpecifiestheusernamefortheSNMPMIB view.Acceptsa |     |
maximumof32characters.
| <VIEWNAME> |     |     |     |     | SpecifiestheviewnamefortheSNMPMIB view.Acceptsa |     |
| ---------- | --- | --- | --- | --- | ----------------------------------------------- | --- |
maximumof32characters.
Examples
AddingauserintheexistingSNMPMIBview:
| switch(config)# |     | snmpv3 |     | user nw-admin |     | view my-nw-view |
| --------------- | --- | ------ | --- | ------------- | --- | --------------- |
RemovingtheuserfromtheSNMPMIBview:
| switch(config)# |     | no  | snmpv3 | user | nw-admin | view my-nw-view |
| --------------- | --- | --- | ------ | ---- | -------- | --------------- |
AttachingunconfiguredorunknownSNMPviewtoanSNMPv3user:
| switch(config)# |             | snmpv3  |             | user nw-admin |                   | view myView |
| --------------- | ----------- | ------- | ----------- | ------------- | ----------------- | ----------- |
| View            | myView      | is not  | configured. |               |                   |             |
| Command         | History     |         |             |               |                   |             |
| Release         |             |         |             |               | Modification      |             |
| 10.10           |             |         |             |               | Commandintroduced |             |
| Command         | Information |         |             |               |                   |             |
| Platforms       |             | Command | context     |               | Authority         |             |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| Entity | MIB | support |     |     |     |     |
| ------ | --- | ------- | --- | --- | --- | --- |
TheEntityMIB,rfc6933,allowsnetworkmanagerstoretrievephysicalcontainmentandlogical
relationshipsfordevicesinthenetwork.TheentconfigChangetrapissenttoconfiguredSNMP-server
hostswhenachangeoccurs.Thetrapisconfiguredtosendnotificationsnomorethanonceevery5
seconds.WewillbesupportingtheEntityMIBforread-only.
|68

Physicalcomponentsthataresupportedinclude:
n Stack
n Chassis
n Fabriccards
n Fantrays
n Fans
n Linecardsandtheirinterfaces
n Managementmodulesandtheintaketemperaturesensor
Powersupplies
n
Theslotsforanyremovablecomponentarealsorepresented.ThelogicaltableoftheEntityMIB
representsconfiguredVLANsandtheassociatedports.TheentConfigChangetrap/notificationissentto
configuredsnmp-serverhosts.
| Location | of the | MIB files | on the | web |
| -------- | ------ | --------- | ------ | --- |
TheMIBfilesforArubaswitchescanbefoundontheArubaServicePortal.Youcanapplythevarious
filterstofilterbyproductseries,softwareversions,andsoftwarereleasetypes.
| OIDs that | support | SNMP | read-write |     |
| --------- | ------- | ---- | ---------- | --- |
ThefollowingtablecontainstheOIDsthatsupportSNMPread-write:
| Software     | Feature | MIB File       |     | OID          |
| ------------ | ------- | -------------- | --- | ------------ |
| SNMPv2System |         | SNMPv2-MIB.mib |     | n sysContact |
n sysName
n sysLocation
| PoE |     | ARUBAWIRED-POE.mib |     | arubaWiredPoePethPsePortPoECycle |
| --- | --- | ------------------ | --- | -------------------------------- |
|     |     | POWER-ETHERNET-MIB |     | pethPsePortAdminEnable           |
VLAN
|     |     | IEEE8021QBridge-Mib |     | n ieee8021QBridgeVlanStaticEgressPorts |
| --- | --- | ------------------- | --- | -------------------------------------- |
n ieee8021QBridgeVlanStaticRowStatus
n ieee8021QBridgeVlanStaticUntaggedPorts
n ieee8021QBridgePvid
n ieee8021QBridgeMvrpEnabledStatus
|     |     | Dot1QBridge-Mib |     | n Dot1QBridgeVlanStaticEgressPorts |
| --- | --- | --------------- | --- | ---------------------------------- |
n Dot1qVlanStaticRowStatus
n Dot1QBridgeVlanStaticUntaggedPorts
n Dot1QBridgePvid
n Dot1QBridgeMvrpEnabledStatus
| Interface |     | IF-MIB |     | n ifAdminStatus |
| --------- | --- | ------ | --- | --------------- |
n ifAlias
|     |     | ARUBAWIRED-INTERFACE- |     | n arubaWiredInterfaceAutoneg |
| --- | --- | --------------------- | --- | ---------------------------- |
MIB
AOS-CX10.16.xxxxSNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 69

| Software Feature |     | MIB File |     | OID |
| ---------------- | --- | -------- | --- | --- |
n arubaWiredInterfaceDuplex
n arubaWiredInterfaceSpeeds
| PortSecurity |     | ARUBAWIRED- |     |     |
| ------------ | --- | ----------- | --- | --- |
n arubaWiredPortSecurityGlobalEnab
PORTSECURITY-MIB
n arubaWiredPortSecurityEnable
n arubaWiredClientLimit
arubaWiredViolationAction
n
n arubaWiredRecoveryTimer
n arubaWiredShutdownRecovery
n arubaWiredStickyEnable
| OIDs that | support | SNMP | read-create |     |
| --------- | ------- | ---- | ----------- | --- |
ThefollowingtablecontainstheOIDsthatsupportSNMPread-create:
| Software Feature |     | MIB File                 |     | OID |
| ---------------- | --- | ------------------------ | --- | --- |
| PortSecurity     |     | ARUBAWIRED-PORTSECURITY- |     |     |
n arubaWiredClientMacVidList
MIB
n arubaWiredMacAddrRowStatus
|70

Chapter 4

Support and Other Resources

Support and Other Resources

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

https://www.hpe.com/us/en/networking/hpe-aruba-networking-
support-services.html

AOS-CX Switch Software Documentation
Portal

https://arubanetworking.hpe.com/techdocs/AOS-CX/help_
portal/Content/home.htm

HPE Aruba Networking Support Portal

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

AOS-CX 10.16.xxxx SNMP/MIB Guide | (All AOS-CX Series Switches)

71

HPEAruba https://arubanetworking.hpe.com/techdocs/hardware/DocumentationPortal/Content/home.
| Networking | htmm |     |
| ---------- | ---- | --- |
Hardware
Documentation
andTranslations
Portal
| HPEAruba | https://networkingsupport.hpe.com/downloads |     |
| -------- | ------------------------------------------- | --- |
Networking
software
| Software | https://licensemanagement.hpe.com/ |     |
| -------- | ---------------------------------- | --- |
licensingand
FeaturePacks
| End-of-Life | https://networkingsupport.hpe.com/end-of-life |     |
| ----------- | --------------------------------------------- | --- |
information
| Accessing | Updates |     |
| --------- | ------- | --- |
YoucanaccessupdatesfromtheHPEArubaNetworkingSupportPortalat
https://networkingsupport.hpe.com.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://networkingsupport.hpe./notifications/subscriptions(requiresanactiveHPEArubaNetworking
SupportPortalaccounttomanagesubscriptions).SecuritynoticesareviewablewithoutanHPEAruba
NetworkingSupportPortalaccount.
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
HPEArubaNetworkingiscommittedtoprovidingourcustomerswithinformationaboutthechemical
substancesinourproductsasneededtocomplywithlegalrequirements,environmentaldata(company
programs,productrecycling,energyefficiency),andsafetyinformationandcompliancedata,(RoHSand
WEEE).Formoreinformation,seehttps://www.arubanetworks.com/company/about-us/environmental-
citizenship/.
| Documentation |     | Feedback |
| ------------- | --- | -------- |
HPEArubaNetworkingiscommittedtoprovidingdocumentationthatmeetsyourneeds.Tohelpus
improvethedocumentation,sendanyerrors,suggestions,orcommentstoDocumentationFeedback
SupportandOtherResources|72

(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.16.xxxx SNMP/MIB Guide | (All AOS-CX Series Switches)

73