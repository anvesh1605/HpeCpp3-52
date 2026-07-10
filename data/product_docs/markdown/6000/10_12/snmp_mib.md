AOS-CX 10.12 SNMP/MIB
Guide

All AOS-CX Series Switches

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

| 2

Contents
Contents
| Contents                            |                                        | 3   |
| ----------------------------------- | -------------------------------------- | --- |
| About this                          | document                               | 5   |
| Applicableproducts                  |                                        | 5   |
| Latestversionavailableonline        |                                        | 5   |
| Commandsyntaxnotationconventions    |                                        | 5   |
| Abouttheexamples                    |                                        | 6   |
| Identifyingswitchportsandinterfaces |                                        | 7   |
| Identifyingmodularswitchcomponents  |                                        | 8   |
| SNMP                                |                                        | 9   |
| SNMPwrite:PoEwritecapabilities      |                                        | 9   |
| SNMPwrite:VLANwritecapabilities     |                                        | 9   |
| SNMPwrite:Configurations            |                                        | 10  |
| SNMPMIBview                         |                                        | 12  |
|                                     | ConfiguringSNMPMIB view                | 12  |
|                                     | SNMPMIBviewlimitations                 | 13  |
| SNMPtraps                           |                                        | 13  |
| ConfiguringSNMP                     |                                        | 14  |
| SNMPcommands                        |                                        | 17  |
|                                     | event-trap-enable                      | 17  |
|                                     | lldptrapenable                         | 17  |
|                                     | mac-notifytraps                        | 20  |
|                                     | rmonalarm                              | 21  |
|                                     | rmonalarm{enable|disable}{index|all}   | 22  |
|                                     | showconfiguration-changestrap          | 23  |
|                                     | showmac-notify                         | 24  |
|                                     | showmac-notifyport                     | 24  |
|                                     | showrmonalarm                          | 25  |
|                                     | showsnmpagent-port                     | 27  |
|                                     | showsnmpcommunity                      | 27  |
|                                     | showsnmpsystem                         | 28  |
|                                     | showsnmptrap                           | 29  |
|                                     | showsnmpviews                          | 29  |
|                                     | showsnmpvrf                            | 31  |
|                                     | showsnmpv3context                      | 31  |
|                                     | showsnmpv3engine-id                    | 32  |
|                                     | showsnmpv3security-level               | 33  |
|                                     | showsnmpv3users                        | 33  |
|                                     | snmp-serveragent-port                  | 34  |
|                                     | snmp-servercommunity                   | 35  |
|                                     | snmp-servercommunityview               | 37  |
|                                     | snmp-serverhistorical-counters-monitor | 38  |
|                                     | snmp-serverhost                        | 39  |
|                                     | snmp-serverresponse-source             | 41  |
|                                     | snmp-serversnmpv3-only                 | 42  |
|                                     | snmp-serversystem-contact              | 42  |
|                                     | snmp-serversystem-description          | 43  |
3
AOS-CX10.12SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

|                                   | snmp-serversystem-location                    |           | 44  |
| --------------------------------- | --------------------------------------------- | --------- | --- |
|                                   | snmp-servertrap                               |           | 45  |
|                                   | snmp-servertrapaaa-server-reachability-status |           | 46  |
|                                   | snmp-servertrapconfiguration-changes          |           | 47  |
|                                   | snmp-servertrapmac-notify                     |           | 48  |
|                                   | snmp-servertrapmodule                         |           | 48  |
|                                   | snmp-servertrapport-security                  |           | 49  |
|                                   | snmp-servertrapsnmp                           |           | 50  |
|                                   | snmp-servertrap-sourceinterfacevrf            |           | 51  |
|                                   | snmp-servertrapvsx                            |           | 52  |
|                                   | snmp-serverview                               |           | 53  |
|                                   | snmp-servervrf                                |           | 54  |
|                                   | snmpv3context                                 |           | 55  |
|                                   | snmpv3engine-id                               |           | 56  |
|                                   | snmpv3security-level                          |           | 57  |
|                                   | snmpv3user                                    |           | 58  |
|                                   | snmpv3userview                                |           | 60  |
| EntityMIBsupport                  |                                               |           | 61  |
| LocationoftheMIBfilesontheweb     |                                               |           | 62  |
| UpdatedMIBsandTrapsforAOS-CX10.12 |                                               |           | 62  |
|                                   | NETWORKINGOID                                 |           | 62  |
|                                   | LLDP                                          |           | 62  |
|                                   | PowerSupply                                   |           | 62  |
|                                   | SystemInformation                             |           | 63  |
| OIDsthatsupportSNMPread-write     |                                               |           | 63  |
| OIDsthatsupportSNMPread-create    |                                               |           | 64  |
| Support                           | and Other                                     | Resources | 65  |
| AccessingArubaSupport             |                                               |           | 65  |
| AccessingUpdates                  |                                               |           | 66  |
|                                   | ArubaSupportPortal                            |           | 66  |
|                                   | MyNetworking                                  |           | 66  |
| WarrantyInformation               |                                               |           | 66  |
| RegulatoryInformation             |                                               |           | 66  |
| DocumentationFeedback             |                                               |           | 67  |
Contents|4

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 4100i Switch Series (JL817A, JL818A)

n Aruba 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A)

n Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A, R8Q68A, R8Q69A, R8Q70A,

R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A)

n Aruba 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B, R0X40C, R0X41A,
R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C, R0X26A, R0X27A,
JL741A)

n Aruba 8100 Switch Series (R9W94A, R9W95A, R9W96A, R9W97A)

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C, JL709C, JL710C, JL711C, JL704C, JL705C,
JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

n Aruba 8400 Switch Series (JL366A, JL363A, JL687A)

n Aruba 9300 Switch Series (R9A29A, R9A30A, R8Z96A)

n Aruba 10000 Switch Series (R8P13A, R8P14A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

Usage

example-text

Identifies commands and their options and operands, code examples,
filenames, pathnames, and output displayed in a command window. Items
that appear like the example text in the previous column are to be entered
exactly as shown and are required unless enclosed in brackets ([ ]).

AOS-CX 10.12 SNMP/MIB Guide | (All AOS-CX Series Switches)

5

Convention

Usage

example-text

In code and screen examples, indicates text entered by a user.

Any of the following:
n <example-text>
n <example-text>
n example-text

n example-text

|

{ }

[ ]

… or

...

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

About this document | 6

| Variable information |     | in CLI prompts |     |
| -------------------- | --- | -------------- | --- |
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
| On the 4100i | Switch | Series |     |
| ------------ | ------ | ------ | --- |
n member:Always1.VSFisnotsupportedonthisswitch.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4ontheswitch.
| On the 6000 | and 6100 | Switch Series |     |
| ----------- | -------- | ------------- | --- |
n member:Always1.VSFisnotsupportedonthisswitch.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4ontheswitch.
| On the 6200 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to8.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis
1.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4inslot1on
member1.
| On the 6300 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to10.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis
1.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4onmember1.
| On the 6400 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
7
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------- | ------------------------- | --- | --- |

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
member 1.

On the 83xx, 9300, and 10000 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on

physical port 4 in slot 1 on member 1.

On the 8400 Switch Series

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

About this document | 8

Chapter 2

SNMP

SNMP

Simple Network Management Protocol (SNMP) is an Internet-standard protocol used for managing and
monitoring the devices connected to a network by collecting, organizing, and modifying information
about managed devices on IP networks.

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

n ieee8021QBridgeVlanStaticRowStatus Mib object in ieee8021QBridgeVlanStaticTable

or

n dot1QBridgeVlanStaticRowStatus Mib object in dot1qVlanStaticTable

Set the value to 4 to create a new VLAN, and set the value to 6 to delete an existing VLAN.

Add or Delete Tagged Port(s) to a VLAN

AOS-CX 10.12 SNMP/MIB Guide | (All AOS-CX Series Switches)

9

Theindexfortheieee8021QBridgeVlanStaticTableanddot1qVlanStaticTableisVLAN.Tosetorclear
port(s)astaggedmembersfortheVLAN,eitherconfigure:
n ieee8021QBridgeVlanStaticEgressPortsMibobjectinieee8021QBridgeVlanStaticTable
or
n dot1QBridgeVlanStaticEgressPortsMibobjectindot1qVlanStaticTable
Changestoabitinthisobjectaffectper-portandper-VLANregistrarcontrol.
| Add or | Delete | Untagged |     | Port(s) |     | to a VLAN |     |
| ------ | ------ | -------- | --- | ------- | --- | --------- | --- |
Theindexfortheieee8021QBridgeVlanStaticTableanddot1qVlanStaticTableisVLAN.Tosetorclear
port(s)asuntaggedmembersfortheVLAN,eitherconfigure:
n ieee8021QBridgeVlanStaticUntaggedPortsMibobjectinieee8021QBridgeVlanStaticTable
or
n dot1QBridgeVlanStaticEgressPortsMibobjectindot1qVlanStaticTable
Changestoabitinthisobjectaffecttheper-port,per-VLANRegistrarcontrol.
| Enable | or Disable |     | MVRP | to  | Port |     |     |
| ------ | ---------- | --- | ---- | --- | ---- | --- | --- |
Theindexfortheieee8021QBridgePortVlanTableanddot1qPortVlanTableisport.Toenableordisable
portlevelMVRPstatus,eitherconfigure:
n ieee8021QBridgeMvrpEnabledStatusMibobjectinieee8021QBridgePortVlanTable
or
n dot1QBridgeMvrpEnabledStatusMibobjectindot1qPortVlanTable
Thevaluetrue(1)indicatesthatMVRPisenabledonthedeviceandfalse(2)indicatesthatMVRPis
disabledforallportsonthedevice.
| Add untagged |     | VLAN | to  | a Port |     |     |     |
| ------------ | --- | ---- | --- | ------ | --- | --- | --- |
Theindexfortheieee8021QBridgePortVlanTableanddot1qPortVlanTableisport.Tosetuntaggedvlan
fortheport,eitherconfigure:
n ieee8021QBridgePvidMibobjectinieee8021QBridgePortVlanTable
or
n dot1QBridgePvidsMibobjectindot1qPortVlanTable
| SNMP | write: |     | Configurations |     |     |     |     |
| ---- | ------ | --- | -------------- | --- | --- | --- | --- |
Prerequisites
Theswitchmustbeconfiguredforexternalaccess(suchasmanagementinterfaceandIPaddressing)
andSNMPenabled(suchasSNMPv2andSNMPv3).
| switch(config)#         |     |     | interface   |        | mgmt           |               |              |
| ----------------------- | --- | --- | ----------- | ------ | -------------- | ------------- | ------------ |
| switch(config-if-mgmt)# |     |     |             |        | no shutdown    |               |              |
| switch(config-if-mgmt)# |     |     |             |        | ip static      | 10.10.10.4/24 |              |
| switch(config)#         |     |     | snmp-server |        |                | vrf mgmt      |              |
| switch(config)#         |     |     | no          | snmpv3 | security-level |               | auth-privacy |
SNMP|10

switch(config)# snmpv3 user test auth md5 auth-pass plaintext password priv aes
| priv-pass | plaintext | password access-level | rw  |     |
| --------- | --------- | --------------------- | --- | --- |
SNMP set examples
ThefollowingexamplesareexecutedfromanexternalclientcommunicatingthroughSNMPtothe
switch.TheydescribesbothcommandsyntaxandOIDinterpretations:
| n copy running-config |     | startup-config |     |     |
| --------------------- | --- | -------------- | --- | --- |
snmpset -v3 -t100 -u test -l authPriv -a md5 -A password -x aes -X password
| 10.10.10.4                                  | 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5 |     |                  | i 4 |
| ------------------------------------------- | ----------------------------------------- | --- | ---------------- | --- |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5    |                                           |     | i 3              |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5    |                                           |     | i 2              |     |
| OID                                         |                                           |     | Description      |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5i4 |                                           |     | Createoperation. |     |
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5i3 SetsourcetypetoRunningConfig.
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5i2 SetdestinationtypetoStartupConfig.
| n copy startup-config |     | running-config |     |     |
| --------------------- | --- | -------------- | --- | --- |
snmpset -v3 -t100 -u test -l authPriv -a md5 -A password -x aes -X password
| 10.10.10.4                                  | 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5 |     |                  | i 4 |
| ------------------------------------------- | ----------------------------------------- | --- | ---------------- | --- |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5    |                                           |     | i 2              |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5    |                                           |     | i 3              |     |
| OID                                         |                                           |     | Description      |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5i4 |                                           |     | Createoperation. |     |
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5i2 SetsourcetypetoStartupConfig.
1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5i3 SetdestinationtypetoRunningConfig.
| n copy REMOTE-URL | running-config |     |     |     |
| ----------------- | -------------- | --- | --- | --- |
snmpset -v3 -t100 -u test -l authPriv -a md5 -A password -x aes -X password
| 10.10.10.4                                | 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.18.5 |     |                | i 4 |
| ----------------------------------------- | ----------------------------------------- | --- | -------------- | --- |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.2.5  |                                           |     | i 1            |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.3.5  |                                           |     | i 3            |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.4.5  |                                           |     | i 4            |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.6.5  |                                           |     | i 1            |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.7.5  |                                           |     | s "file"       |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.9.5  |                                           |     | s "10.10.10.1" |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.12.5 |                                           |     | s "mgmt"       |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.10.5 |                                           |     | s "user"       |     |
| 1.3.6.1.4.1.47196.4.1.1.3.20.1.0.1.1.11.5 |                                           |     | s "password"   |     |
11
AOS-CX10.12SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

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
SNMP MIB view is a group of view subtrees in the MIB hierarchy. A view subtree is identified by the
pairing of an Object Identifier (OID) subtree value with a bit string mask value. Each MIB view is defined
by the view subtrees that is included or excluded from the MIB view. You can use the MIB views to
control the OID range that SNMPv3 users or SNMP v1/v2 community can access.

Configuring SNMP MIB view

SNMP | 12

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
WhenSNMPisconfigured,interfacedaemonseventlogmessagesforlink-upandlink-downeventswill
besentastraps.
EventlogtrapOID:1.3.6.1.4.1.47196.4.1.1.3.4.1.1
13
AOS-CX10.12SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

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
command snmp-server vrf mgmt to enable SNMP on the management interface. Use the
command snmp-server vrf default to enable SNMP on the default VRF. Use the command
snmp-server vrf <USERDEFINED_VRF_NAME> to enable SNMP on the user created VRF.

SNMP | 14

2. Setthesystemcontact,location,anddescriptionfortheswitchwiththefollowingcommands:
| n snmp-server | system-contact     |     |     |     |
| ------------- | ------------------ | --- | --- | --- |
| n snmp-server | system-location    |     |     |     |
| n snmp-server | system-description |     |     |     |
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
| NAME> vrf | <VRF_NAME> | community | <COMMUNITY_NAME>. |     |
| --------- | ---------- | --------- | ----------------- | --- |
8. ReviewyourSNMPconfigurationsettingswiththefollowingcommands:
| n show | snmp agent-port |     |     |     |
| ------ | --------------- | --- | --- | --- |
| n show | snmp community  |     |     |     |
| n show | snmp system     |     |     |     |
| n show | snmpv3 context  |     |     |     |
| n show | snmp trap       |     |     |     |
| show   | snmp vrf        |     |     |     |
n
| n show | snmpv3 users |     |     |     |
| ------ | ------------ | --- | --- | --- |
| n show | tech snmp    |     |     |     |
Example 1
Thisexamplecreatesthefollowingconfiguration:
n EnablesSNMPontheout-of-bandmanagementinterface(VRFmgmt).
n Setsthecontact,location,anddescriptionfortheswitchto:JaniceM,Building2,LabSwitch.
n SetsthecommunitystringtoLab8899X.
| switch(config)# | snmp-server | vrf             | mgmt |           |
| --------------- | ----------- | --------------- | ---- | --------- |
| switch(config)# | snmp-server | system-contact  |      | JaniceM   |
| switch(config)# | snmp-server | system-location |      | Building2 |
switch(config)#
|                 | snmp-server | system-description |          | LabSwitch |
| --------------- | ----------- | ------------------ | -------- | --------- |
| switch(config)# | snmp-server | community          | Lab8899X |           |
Example 2
Thisexamplecreatesthefollowingconfiguration:
CreatesanSNMPv3usernamedAdminusingshaauthenticationwiththeplaintextpassword
n
mypasswordandusingdessecuritywiththeplaintextpasswordmyprivpass.
n AssociatestheSNMPv3userAdminwithacontextnamednewContext.
15
AOS-CX10.12SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des

priv-pass plaintext myprivpass

switch(config)# snmpv3 user Admin context newContext

SNMP | 16

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
17
AOS-CX10.12SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

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
|18

| 1/1/6 | Yes | Yes | Yes |
| ----- | --- | --- | --- |
...........
...........
| mgmt | Yes | Yes | Yes |
| ---- | --- | --- | --- |
DisplayingLLDPConfigurationfortheinterface:
| switch#     | show lldp configuration | 1/1/1 |     |
| ----------- | ----------------------- | ----- | --- |
| LLDP Global | Configuration           |       |     |
=========================
| LLDP Enabled  |                 | : Yes |     |
| ------------- | --------------- | ----- | --- |
| LLDP Transmit | Interval        | : 30  |     |
| LLDP Hold     | Time Multiplier | : 4   |     |
| LLDP Transmit | Delay Interval  | : 2   |     |
| LLDP Reinit   | Timer Interval  | : 2   |     |
| LLDP Trap     | Enabled         | : No  |     |
| LLDP Port     | Configuration   |       |     |
=======================
| PORT | TX-ENABLED | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | ---------- | ---------- | ----------------- |
--------------------------------------------------------------------------
| 1/1/1 | Yes | Yes | Yes |
| ----- | --- | --- | --- |
DisplayingLLDPConfigurationforthemanagementinterface:
| switch#     | show lldp configuration | mgmt |     |
| ----------- | ----------------------- | ---- | --- |
| LLDP Global | Configuration           |      |     |
=========================
| LLDP Enabled  |                 | : Yes |     |
| ------------- | --------------- | ----- | --- |
| LLDP Transmit | Interval        | : 30  |     |
| LLDP Hold     | Time Multiplier | : 4   |     |
| LLDP Transmit | Delay Interval  | : 2   |     |
| LLDP Reinit   | Timer Interval  | : 2   |     |
| LLDP Trap     | Enabled         | : Yes |     |
| LLDP Port     | Configuration   |       |     |
=======================
| PORT | TX-ENABLED | RX-ENABLED | INTF-TRAP-ENABLED |
| ---- | ---------- | ---------- | ----------------- |
--------------------------------------------------------------------------
| mgmt           | Yes         | Yes          | Yes |
| -------------- | ----------- | ------------ | --- |
| Command        | History     |              |     |
| Release        |             | Modification |     |
| 10.07orearlier |             | --           |     |
| Command        | Information |              |     |
19
AOS-CX10.12SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
configandconfig-if
forthiscommand.
| mac-notify    | traps       |                 |         |            |
| ------------- | ----------- | --------------- | ------- | ---------- |
| mac-notify    | traps {aged | | learned       | | moved | | removed} |
| no mac-notify | traps       | {aged | learned | | moved | | removed} |
Description
ConfiguresaLayer2interfacetogenerateSNMPtrapnotificationsforuptofourdifferenttypesof
dynamicMACaddressrelatedeventsonthetrunkoraccessinphysicalorlaginterfaces.
Thenoformofthiscommandremovesthetrapsfromtheinterface.
| Parameter |     |     | Description                                       |     |
| --------- | --- | --- | ------------------------------------------------- | --- |
| aged      |     |     | NotifieswhenaMACaddressagedoutontheinterface.     |     |
| learned   |     |     | NotifieswhenaMACaddressislearnedontheinterface.   |     |
| moved     |     |     | NotifieswhenaMACaddressmovedfromtheinterface.     |     |
| removed   |     |     | NotifieswhenaMACaddressisremovedfromtheinterface. |     |
MACnotificationtrapadditiontoorremovalfromaninterfacecanbeinanycombination,quantity,ororder.The
additionofexistingconfiguredtrapsorremovalofnon-configuredtrapswillbeacceptedandignored.
Themac-notifyfeaturemustbeenabledgloballyforanyinterfaceconfigurationstogenerateSNMPtraps.
MACnotificationcannotbeconfiguredonaLayer3(routing)interface.ALayer2interfacethatischangedtoa
Layer3interfacethroughtheroutingcommandwilldiscardanyexistingMACnotificationconfigurations.
IncasesofMACslearnedonport-access port-securityenabledports,themovescenarioishandledbythe
port-accessfeaturethroughthedeletionoftheMACfromtheoldpartandinstallationonthenewport.Inthis
scenario,MACtrapnotifications,ifenabled,willreflectthatbyproducingremovedandlearnednotifications.
Usage
ThefollowingarethelimitationforSNMPMACnotifytraps:
n SNMPMACchangenotificationtrapisnotsupportedforVxLAN–Overlayhosts.
n MacnotifytrapwillnotgenerateforStaticMACs.
n vsx-syncisnotsupportedforthisfeature.Hence,youmustenabletheMACnotifytrapsexplicitlyon
secondarytoensurethetrapsaregenerated.
Examples
MACnotificationtypesandtheassociatedeventsonlyapplytoLayer2interfaces,henceroutingmightneedto
bedisabledontherelevantinterfaces.
EnablingthetrapsonanL2interface:
|20

| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)#
|                    |        | mac-notify |        | traps learned |         |
| ------------------ | ------ | ---------- | ------ | ------------- | ------- |
| 1/1/1 is           | not an | L2 port    |        |               |         |
| switch(config-if)# |        | no routing |        |               |         |
| switch(config-if)# |        | mac-notify |        | traps learned | removed |
| switch(config-if)# |        | mac-notify |        | traps moved   |         |
| switch(config-if)# |        | mac-notify |        | traps aged    |         |
| switch(config)#    |        | interface  | lag101 |               |         |
| switch(config-if)# |        | mac-notify |        | traps removed |         |
Disablingthelearnedandremovedtrapsfromtheinterface1/1/1:
| switch(config)#     |         | interface     | 1/1/1 |                                                  |         |
| ------------------- | ------- | ------------- | ----- | ------------------------------------------------ | ------- |
| switch(config-if)#  |         | no mac-notify |       | traps learned                                    | removed |
| Command History     |         |               |       |                                                  |         |
| Release             |         |               |       | Modification                                     |         |
| 10.10               |         |               |       | Supportforportaccessfeatureswithmac-notifyadded. |         |
| 10.08               |         |               |       | Commandintroduced                                |         |
| Command Information |         |               |       |                                                  |         |
| Platforms           | Command | context       |       | Authority                                        |         |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
commandfromtheauditorcontext(auditor>)only.
rmon alarm
rmon alarm index <INDEX> snmp-oid <SNMP-OID> rising-threshold <RISING-THRESHOLD>
falling-threshold <FALLING-THRESHOLD> [sample-interval <SAMPLE-INTERVAL>] [sample-
type <ABSOLUTE|DELTA>]
| no rmon alarm | [index | <INDEX>] |     |     |     |
| ------------- | ------ | -------- | --- | --- | --- |
Description
Storesconfigurationentriesinanalarmtablethatdefinesthesampleinterval,sample-type,and
thresholdparametersforanSNMPMIBobject.OnlytheSNMPMIBobjectsthatresolvetoanASN.1
primitivetypeofINTEGER(INTEGER,Integer32,Counter32,Counter64,Gauge32,orTimeTicks)willbe
monitored.
ThenoformofthiscommandremovesallRMONalarmsandallowsyoutospecifyanindextoremovea
particularRMONalarm.
21
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- | --- |

| Parameter |         |     |     |     |     | Description                             |     |
| --------- | ------- | --- | --- | --- | --- | --------------------------------------- | --- |
| index     | <INDEX> |     |     |     |     | SpecifiestheRMONalarmindex.Range:1to20. |     |
snmp-oid <SNMP-OID> SpecifiestheSNMPMIBobjecttobemonitoredbyRMON.
rising-threshold <RISING-THRESHOLD> SpecifiestheupperthresholdvaluefortheRMONalarm.
falling-threshold <FALLING-THRESHOLD> SpecifiesthefallingthresholdvaluefortheRMONalarm.
Thefallingthresholdmustbelessthantherising
threshold.
| sample-interval |     |     | <SAMPLE-INTERVAL> |     |     |     |     |
| --------------- | --- | --- | ----------------- | --- | --- | --- | --- |
Sampleintervalinseconds.Default:30.
sample-type <ABSOLUTE|DELTA> SpecifiesthemethodofsamplingoftheSNMPMIBobject.
Default:Absolute.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| rmon       | alarm   | {enable |            | | disable} |        | {index  | | all} |
| ---------- | ------- | ------- | ---------- | ---------- | ------ | ------- | ------ |
| rmon alarm | {enable |         | | disable} |            | {index | <INDEX> | | all} |
| no rmon    | alarm   | [enable | |          | disable]   | [index | <INDEX> | | all] |
Description
EnablesanddisablestheRMONalarmanditsindex.RMONalarmisenabledbydefault.
|22

| Parameter     |     |     |     | Description                             |     |
| ------------- | --- | --- | --- | --------------------------------------- | --- |
| enable        |     |     |     | EnablestheRMONalarmindex                |     |
| disable       |     |     |     | DisablestheRMONalarmindex.              |     |
| index <INDEX> |     |     |     | SpecifiestheRMONalarmindex.Range:1to20. |     |
| all           |     |     |     | SpecifiesalltheRMONalarms.              |     |
Examples
EnablingordisablingalltheRMONalarm:
| switch(config)# |     | rmon alarm | enable  | all |     |
| --------------- | --- | ---------- | ------- | --- | --- |
| switch(config)# |     | rmon alarm | disable | all |     |
EnablingordisablingRMONalarmbyindex:
| switch(config)#     |         | rmon alarm | enable  | index        | 1   |
| ------------------- | ------- | ---------- | ------- | ------------ | --- |
| switch(config)#     |         | rmon alarm | disable | index        | 1   |
| Command History     |         |            |         |              |     |
| Release             |         |            |         | Modification |     |
| 10.07orearlier      |         |            |         | --           |     |
| Command Information |         |            |         |              |     |
| Platforms           | Command | context    |         | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show configuration-changes |     |     |      | trap |     |
| -------------------------- | --- | --- | ---- | ---- | --- |
| show configuration-changes |     |     | trap |      |     |
Description
ShowstheSNMPconfigurationchangestrapsettings.
Example
ShowingtheSNMPconfigurationchangestrap:
| switch#            | show configuration-changes |         |      | trap      |     |
| ------------------ | -------------------------- | ------- | ---- | --------- | --- |
| SNMP Configuration |                            | changes | trap | : Enabled |     |
```
| Command History |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
23
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- | --- |

| Release             |         |         |     | Modification      |
| ------------------- | ------- | ------- | --- | ----------------- |
| 10.10               |         |         |     | Commandintroduced |
| Command Information |         |         |     |                   |
| Platforms           | Command | context |     | Authority         |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
show mac-notify
show mac-notify
Description
DisplayswhethertheMACnotificationfeatureintheSNMPmoduleisenabledornot.Italsodisplaysthe
trapnotificationtypesconfiguredontheLayer2portsinthesystem.
Examples
ShowingtheMACnotificationconfigurationonallconfiguredportsinthesystem:
| switch#          | show mac-notify |        |         |           |
| ---------------- | --------------- | ------ | ------- | --------- |
| MAC notification |                 | global | setting | : Enabled |
| Port             | Enabled         | Traps  |         |           |
---------------------------------------
| 1/1/1  | aged    | learned | moved |         |
| ------ | ------- | ------- | ----- | ------- |
| 1/1/5  | moved   |         |       |         |
| lag101 | removed |         |       |         |
| lag104 | aged    | learned | moved | removed |
...
...
| Command History     |         |         |     |                   |
| ------------------- | ------- | ------- | --- | ----------------- |
| Release             |         |         |     | Modification      |
| 10.08               |         |         |     | Commandintroduced |
| Command Information |         |         |     |                   |
| Platforms           | Command | context |     | Authority         |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show mac-notify |       | port     |     |     |
| --------------- | ----- | -------- | --- | --- |
| show mac-notify | [port | <PORTS>] |     |     |
|24

Description
DisplaystheMACnotificationconfigurationonarangeofports.
| Parameter |          |     |     |     | Description                                |
| --------- | -------- | --- | --- | --- | ------------------------------------------ |
| [port     | <PORTS>] |     |     |     | Specifiesaport,rangeofports,orlistofports. |
Examples
ShowingtheMACnotificationconfigurationonarangeofports:
switch(config)# show mac-notify port 1/1/1,1/1/3,1/1/5,lag101-lag104
| MAC  | notification |         | global | Setting: | Enabled |
| ---- | ------------ | ------- | ------ | -------- | ------- |
| Port |              | Enabled | Traps  |          |         |
---------------------------------------
| 1/1/1     |             | aged    | learned | moved |                   |
| --------- | ----------- | ------- | ------- | ----- | ----------------- |
| 1/1/3     |             | --      |         |       |                   |
| 1/1/5     |             | moved   |         |       |                   |
| lag101    |             | removed |         |       |                   |
| lag102    |             | --      |         |       |                   |
| lag103    |             | --      |         |       |                   |
| lag104    |             | aged    | learned | moved | removed           |
| Command   | History     |         |         |       |                   |
| Release   |             |         |         |       | Modification      |
| 10.08     |             |         |         |       | Commandintroduced |
| Command   | Information |         |         |       |                   |
| Platforms |             | Command | context |       | Authority         |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
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
25
| AOS-CX10.12SNMP/MIBGuide| |     |     | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------- | --- | --- | ------------------------- | --- | --- |

| switch# show      | rmon alarm |                     |
| ----------------- | ---------- | ------------------- |
| Index             | :          | 1                   |
| Enabled           | :          | true                |
| Status            | :          | valid               |
| MIB object        | :          | ifOutErrors.15      |
| Sample type       | :          | delta               |
| Sampling          | interval : | 6535 seconds        |
| Rising threshold  | :          | 100                 |
| Falling threshold | :          | 10                  |
| Last sampled      | value :    | 0                   |
| Last sample       | time :     | 2020-09-21 05:58:11 |
| Index             | :          | 3                   |
| Enabled           | :          | true                |
| Status            | :          | invalid             |
| MIB object        | :          | IF-MIB::ifDescr.19  |
| Sample type       | :          | absolute            |
| Sampling          | interval : | 10000 seconds       |
| Rising threshold  | :          | 4000                |
| Falling threshold | :          | 10                  |
| Last sampled      | value :    | 0                   |
ShowingRMONalarmwithalarmindex1:
| switch# show      | rmon alarm | index 1             |
| ----------------- | ---------- | ------------------- |
| Index             | :          | 1                   |
| Enabled           | :          | true                |
| Status            | :          | valid               |
| MIB object        | :          | ifOutErrors.15      |
| Sample type       | :          | delta               |
| Sampling          | interval : | 6535 seconds        |
| Rising threshold  | :          | 100                 |
| Falling threshold | :          | 10                  |
| Last sampled      | value :    | 0                   |
| Last sample       | time :     | 2020-06-21 05:58:11 |
ShowingdisabledRMONalarminformation:
| switch# show      | rmon       | alarm               |
| ----------------- | ---------- | ------------------- |
| Index             | :          | 1                   |
| Enabled           | :          | false               |
| Status            | :          | valid               |
| MIB object        | :          | ifOutErrors.15      |
| Sample type       | :          | delta               |
| Sampling          | interval : | 6535 seconds        |
| Rising threshold  | :          | 100                 |
| Falling threshold | :          | 10                  |
| Last sampled      | value :    | 0                   |
| Last sample       | time :     | 2020-09-21 05:58:11 |
| Index             | :          | 3                   |
| Enabled           | :          | false               |
| Status            | :          | invalid             |
| MIB object        | :          | IF-MIB::ifDescr.19  |
| Sample type       | :          | absolute            |
| Sampling          | interval : | 10000 seconds       |
| Rising threshold  | :          | 4000                |
| Falling threshold | :          | 10                  |
| Last sampled      | value :    | 0                   |
|26

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show snmp            | agent-port |     |     |
| -------------------- | ---------- | --- | --- |
| show snmp agent-port |            |     |     |
Description
DisplaysSNMPagentUDPportnumber.
Example
DisplayingSNMPagentUDPportnumber:
| switch#             | show snmp | agent-port |              |
| ------------------- | --------- | ---------- | ------------ |
| SNMP agent          | port :    | 161        |              |
| Command History     |           |            |              |
| Release             |           |            | Modification |
| 10.07orearlier      |           |            | --           |
| Command Information |           |            |              |
| Platforms           | Command   | context    | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show snmp           | community |     |     |
| ------------------- | --------- | --- | --- |
| show snmp community |           |     |     |
Description
DisplaysalistofallconfiguredSNMPv1/v2ccommunities.
Usage
WhenausercreatesacustomcommunitybeforeenablinganSNMPagent,AOS-CXautomatically
removesthedefaultpubliccommunityfromthesystem.
27
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------- | ------------------------- | --- | --- |

Example
DisplayingalistofallconfiguredSNMPv1/v2ccommunities:
switch#show
snmp community
SNMP-COMMUNITIES
-------------------------------------------------------------------
| Community |     | Access-level | ACL Name | ACL Type | View |
| --------- | --- | ------------ | -------- | -------- | ---- |
-------------------------------------------------------------------
| private         |     | ro  | my_acl                                              | ipv4 | view1 |
| --------------- | --- | --- | --------------------------------------------------- | ---- | ----- |
| private         |     | ro  | my_acl                                              | ipv6 | none  |
| private2        |     | rw  | new_Acl                                             | ipv6 | view2 |
| private3        |     | rw  | none                                                | none | none  |
| Command History |     |     |                                                     |      |       |
| Release         |     |     | Modification                                        |      |       |
| 10.10           |     |     | OutputhasbeenupdatedwithSNMPviewdetails.AViewcolumn |      |       |
isaddedtothecommandoutput.
| 10.08               |         |         | AddedACLTypecolumntothecommandoutput. |     |     |
| ------------------- | ------- | ------- | ------------------------------------- | --- | --- |
| 10.07orearlier      |         |         | --                                    |     |     |
| Command Information |         |         |                                       |     |     |
| Platforms           | Command | context | Authority                             |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show snmp        | system |     |     |     |     |
| ---------------- | ------ | --- | --- | --- | --- |
| show snmp system |        |     |     |     |     |
Description
DisplaysSNMPdescription,location,andcontactinformation.
Example
DisplayingSNMPdescription,location,andcontactinformation:
| switch#     | show snmp   | system |     |     |     |
| ----------- | ----------- | ------ | --- | --- | --- |
| SNMP system | information |        |     |     |     |
----------------------------
| System description |        | : Aggregation | router |     |     |
| ------------------ | ------ | ------------- | ------ | --- | --- |
| System location    | :      | Main lab      |        |     |     |
| System contact     | : John | Smith, Lab    | Admin  |     |     |
| Command History    |        |               |        |     |     |
|28

| Release             |         |         | Modification |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show snmp      | trap |     |     |     |     |
| -------------- | ---- | --- | --- | --- | --- |
| show snmp trap |      |     |     |     |     |
Description
DisplaysallconfiguredSNMPtraps/informsreceivers.
Example
DisplayingallconfiguredSNMPtrapandinformsreceivers:
| switch# | show snmp | trap |           |                    |          |
| ------- | --------- | ---- | --------- | ------------------ | -------- |
| HOST    |           |      | PORT TYPE | VER COMMUNITY/USER | NAME VRF |
----------------------------------------------------------------------------------
--
| 10.10.10.10 |     |     | 162 trap | v1 public |     |
| ----------- | --- | --- | -------- | --------- | --- |
default
| 10.10.10.10 |     |     | 162 inform | v2c public |     |
| ----------- | --- | --- | ---------- | ---------- | --- |
default
| 10.10.10.10 |     |     | 162 inform | v3 name |     |
| ----------- | --- | --- | ---------- | ------- | --- |
default
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show snmp       | views |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- |
| show snmp views |       |     |     |     |     |
Description
DisplaysthelistofalltheconfiguredSNMPviews.
29
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- | --- |

Usage

The following table contains the status and its description of the configured SNMP views:

Status

Description

pending_validation

Default value that indicates SNMP view is yet to be validated.

operational

OID and mask validated.

invalid

failed

Examples

Invalid OID/mask.

Validation failed for reasons other than OID/mask.

Displaying the list of all the configured SNMP views:

switch# show snmp views
------------------------------------------------------
SNMP MIB Views
------------------------------------------------------
View
: new
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

: user
View
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

| 30

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
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
| show snmpv3 | context |     |     |     |
| ----------- | ------- | --- | --- | --- |
| show snmpv3 | context |     |     |     |
Description
DisplaysallconfiguredSNMPcontexts.
Examples
DisplayingallconfiguredSNMPcontexts:
| switch# | show snmpv3 | context |     |     |
| ------- | ----------- | ------- | --- | --- |
--------------------------------------------------------------------------
| name |     |     | vrf | community |
| ---- | --- | --- | --- | --------- |
--------------------------------------------------------------------------
31
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- |

| contextA |             |         | default |     | private |
| -------- | ----------- | ------- | ------- | --- | ------- |
| contextB |             |         | vrf_A   |     | public  |
| switch#  | show snmpv3 | context |         |     |         |
--------------------------------------------------------------------------
| Name | vrf |     | Community | ype[Instance_id] |     |
| ---- | --- | --- | --------- | ---------------- | --- |
------------------------------------------------------------------
| A   | default |     | public | vrf |     |
| --- | ------- | --- | ------ | --- | --- |
switch#
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show snmpv3 | engine-id |     |     |     |     |
| ----------- | --------- | --- | --- | --- | --- |
| show snmpv3 | engine-id |     |     |     |     |
Description
DisplaystheconfiguredSNMPv3snmpengine-id.
IftheSNMPv3engine-idisnotconfigured,bydefaultauniqueengine-idiscreatedbytheswitchusinga
combinationoftheenterpriseOIDvalueandtheswitch'smacaddress.
Example
DisplayingtheconfiguredSNMPv3engine-id:
| switch#             | show snmpv3                     | engine-id |              |     |     |
| ------------------- | ------------------------------- | --------- | ------------ | --- | --- |
| SNMP engine-id      | : 80:00:B8:5C:08:00:09:1d:de:a5 |           |              |     |     |
| Command History     |                                 |           |              |     |     |
| Release             |                                 |           | Modification |     |     |
| 10.07orearlier      |                                 |           | --           |     |     |
| Command Information |                                 |           |              |     |     |
|32

| Platforms | Command | context | Authority |     |     |
| --------- | ------- | ------- | --------- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show snmpv3 | security-level |     |     |     |     |
| ----------- | -------------- | --- | --- | --- | --- |
| show snmpv3 | security-level |     |     |     |     |
Description
DisplaystheconfiguredSNMPv3securitylevel.
Examples
DisplayingtheconfiguredSNMPv3securitylevel:
| switch#               | show snmpv3 | security-level |              |     |     |
| --------------------- | ----------- | -------------- | ------------ | --- | --- |
| SNMPv3 security-level |             | : auth         |              |     |     |
| Command History       |             |                |              |     |     |
| Release               |             |                | Modification |     |     |
| 10.07orearlier        |             |                | --           |     |     |
| Command Information   |             |                |              |     |     |
| Platforms             | Command     | context        | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show snmpv3 | users |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
| show snmpv3 | users |     |     |     |     |
Description
DisplaysallconfiguredSNMPv3users.
Formoredetailsontheuserenabledstatus,seesnmpv3 security-level.
Example
DisplayingallconfiguredSNMPv3users:
| switch# | show snmpv3 | users |     |     |     |
| ------- | ----------- | ----- | --- | --- | --- |
------------------------------------------------------------------------
| User | AuthMode | PrivMode | Status Context | Access-level | View |
| ---- | -------- | -------- | -------------- | ------------ | ---- |
------------------------------------------------------------------------
| name | md5 | none | Enabled context2 | ro  | view1 |
| ---- | --- | ---- | ---------------- | --- | ----- |
context1
context3
33
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- | --- |

| name2   | none    |     | none |     | Disabled                                            | none | ro  | view2 |
| ------- | ------- | --- | ---- | --- | --------------------------------------------------- | ---- | --- | ----- |
| name3   | none    |     | none |     | Disabled                                            | none | ro  | none  |
| Command | History |     |      |     |                                                     |      |     |       |
| Release |         |     |      |     | Modification                                        |      |     |       |
| 10.10   |         |     |      |     | OutputhasbeenupdatedwithSNMPviewdetails.AViewcolumn |      |     |       |
isaddedtothecommandoutput.
| 10.07orearlier |             |     |         |     | --        |     |     |     |
| -------------- | ----------- | --- | ------- | --- | --------- | --- | --- | --- |
| Command        | Information |     |         |     |           |     |     |     |
| Platforms      | Command     |     | context |     | Authority |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| snmp-server    |            | agent-port |          |     |     |     |     |     |
| -------------- | ---------- | ---------- | -------- | --- | --- | --- | --- | --- |
| snmp-server    | agent-port |            | <PORT>   |     |     |     |     |     |
| no snmp-server | agent-port |            | [<PORT>] |     |     |     |     |     |
Description
SetstheUDPportnumberthattheSNMPmasteragentusestocommunicate.UDPport161isthe
defaultport.
ThenoformofthiscommandsetstheSNMPmasteragentporttothedefaultvalue.
| Parameter |     |     |     |     | Description                                         |     |     |     |
| --------- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
| <PORT>    |     |     |     |     | SpecifiestheUDPportnumberthattheSNMPmasteragentwill |     |     |     |
use.Range:1to65535.Default:161.
Examples
SettingtheSNMPmasteragentportto2000:
| switch(config)# |     | snmp-server |     | agent-port |     | 2000 |     |     |
| --------------- | --- | ----------- | --- | ---------- | --- | ---- | --- | --- |
ResettingtheSNMPmasteragentporttothedefaultvalue:
| switch(config-schedule)# |         |     |     | no snmp-server |              | agent-port | 2000 |     |
| ------------------------ | ------- | --- | --- | -------------- | ------------ | ---------- | ---- | --- |
| Command                  | History |     |     |                |              |            |      |     |
| Release                  |         |     |     |                | Modification |            |      |     |
| 10.07orearlier           |         |     |     |                | --           |            |      |     |
|34

| Command   | Information |         |     |           |
| --------- | ----------- | ------- | --- | --------- |
| Platforms | Command     | context |     | Authority |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    | community |          |     |     |
| -------------- | --------- | -------- | --- | --- |
| snmp-server    | community | <STRING> |     |     |
| no snmp-server | community | <STRING> |     |     |
Description
AddsanSNMPv1/SNMPv2ccommunitystring.Acommunitystringislikeapasswordthatcontrols
read/writeaccesstotheSNMPagent.Anetworkmanagementprogrammustsupplythisnamewhen
attemptingtogetSNMPinformationfromtheswitch.Amaximumof10communitystringsare
supported.Onceyoucreateyourowncommunitystring,thedefaultcommunitystring(public)is
deleted.
ThenoformofthiscommandremovesthespecifiedSNMPv1/SNMPv2ccommunitystring.Whenno
communitystringexists,adefaultcommunitystringwiththevaluepublicisautomaticallydefined.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<STRING> SpecifiestheSNMPv1/SNMPv2ccommunitystring.Range:1to32
printableASCIIcharacters,excludingspaceandquestionmark.
Subcommands
| access-level    | {ro | | rw}   |     |     |
| --------------- | ----- | ----- | --- | --- |
| no access-level | {ro   | | rw} |     |     |
ThissubcommandchangestheaccessleveloftheSNMPcommunity.Thedefaultaccesslevelisread-
only(ro).
Thenoformofthissubcommandchangestheaccesslevelofthecommunitytodefault.
| Parameter      |         |         |            | Description                                    |
| -------------- | ------- | ------- | ---------- | ---------------------------------------------- |
| ro             |         |         |            | SpecifiesRead-OnlyaccesswiththeSNMPcommunity.  |
| rw             |         |         |            | SpecifiesRead-WriteaccesswiththeSNMPcommunity. |
| access-list    | {ipv4 | | ipv6}   | <ACL-NAME> |                                                |
| no access-list | {ipv4   | | ipv6} | <ACL-NAME> |                                                |
ThissubcommandassociatesanACLwiththeSNMPcommunity.IfanACLisnotassociatedwiththe
SNMPcommunity,thedefaultaccessisallowedforallthehosts.
ThenoformofthissubcommandremovesassociationoftheACLwiththeSNMPcommunity.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
ipv4
SpecifiestheIPv4ACLtype.
| ipv6 |     |     |     | SpecifiestheIPv6ACLtype. |
| ---- | --- | --- | --- | ------------------------ |
35
| AOS-CX10.12SNMP/MIBGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------- | --- | ------------------------- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<ACL-NAME> SpecifiestheACLname.Itsupportsamaximumof64characters.
Examples
SettingtheSNMPv1/SNMPv2ccommunitystringtoprivate:
| switch(config)# | snmp-server |     | community | private |
| --------------- | ----------- | --- | --------- | ------- |
RemovingSNMPv1/SNMPv2ccommunitystringprivate:
| switch(config)# | no  | snmp-server | community | private |
| --------------- | --- | ----------- | --------- | ------- |
ConfiguringtheaccesslevelfortheSMNPcommunitytoread-only:
| switch(config-community)# |     |     | access-level | ro  |
| ------------------------- | --- | --- | ------------ | --- |
ChangingtheaccessleveloftheSNMP communitytodefault:
| switch(config-community)# |     |     | no access-level | rw  |
| ------------------------- | --- | --- | --------------- | --- |
AssociatinganIPv4ACLnamedmy_aclwiththeSMNPcommunity:
| switch(config-community)# |     |     | access-list | ipv4 my_acl |
| ------------------------- | --- | --- | ----------- | ----------- |
RemovingtheassociatedIPv4ACLnamedmy_aclfromtheSNMPcommunity:
| switch(config-community)# |     |     | no access-list | ipv4 my_acl |
| ------------------------- | --- | --- | -------------- | ----------- |
ThedenyruleisnotsupportedforSNMPACL.
ConfigurationsupportedforSNMPACL:
| access-list | ip ipv4_acl   |           |         |     |
| ----------- | ------------- | --------- | ------- | --- |
| 10 permit   | any 4.4.4.4   |           | 4.4.4.1 |     |
| 20 permit   | any 3.3.3.3   |           | 3.3.3.1 |     |
| access-list | ipv6 ipv6_acl |           |         |     |
| 10 permit   | any 2001::2   |           | 2001::1 |     |
| 20 permit   | any 3001::2   |           | 3001::1 |     |
| snmp-server | vrf default   |           |         |     |
| snmp-server | community     | my_comm_1 |         |     |
| access-list | ipv4          | ipv4_acl  |         |     |
| access-list | ipv6          | ipv6_acl  |         |     |
ConfigurationnotsupportedforSNMPACL:
|36

| access-list |      | ip        | ipv4_acl        |     |     |
| ----------- | ---- | --------- | --------------- | --- | --- |
| 10          | deny | any       | 6.6.6.6 6.6.6.1 |     |     |
| access-list |      | ipv6      | ipv6_acl        |     |     |
| 10          | deny | any       | 6001::6 6000::1 |     |     |
| snmp-server |      | vrf       | default         |     |     |
| snmp-server |      | community | my_comm_1       |     |     |
| access-list |      |           | ipv4 ipv4_acl   |     |     |
| access-list |      |           | ipv6 ipv6_acl   |     |     |
hitcountsforSNMPACLwillnotbeincremented.
Example:show access-list hitcounts ip allwillnotshowthehitcountofSNMPACL.
| Command        | History     |         |         |     |              |
| -------------- | ----------- | ------- | ------- | --- | ------------ |
| Release        |             |         |         |     | Modification |
| 10.07orearlier |             |         |         |     | --           |
| Command        | Information |         |         |     |              |
| Platforms      |             | Command | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|                |           | config-community |          |       | forthiscommand.    |
| -------------- | --------- | ---------------- | -------- | ----- | ------------------ |
| snmp-server    |           | community        |          | view  |                    |
| snmp-server    | community |                  | <STRING> | [view | <VIEW-NAME>]       |
| no snmp-server |           | community        | <STRING> |       | [view <VIEW-NAME>] |
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
37
| AOS-CX10.12SNMP/MIBGuide| |     |     | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------- | --- | --- | ------------------------- | --- | --- |

| switch(config-community)# |     |     | view | name1 |
| ------------------------- | --- | --- | ---- | ----- |
RemovingSNMP MIBviewfromtheSNMP community:
| switch(config-community)# |         |         | no view | name1             |
| ------------------------- | ------- | ------- | ------- | ----------------- |
| Command History           |         |         |         |                   |
| Release                   |         |         |         | Modification      |
| 10.10                     |         |         |         | Commandintroduced |
| Command Information       |         |         |         |                   |
| Platforms                 | Command | context |         | Authority         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|                | config-community            |     |     | forthiscommand. |
| -------------- | --------------------------- | --- | --- | --------------- |
| snmp-server    | historical-counters-monitor |     |     |                 |
| snmp-server    | historical-counters-monitor |     |     |                 |
| no snmp-server | historical-counters-monitor |     |     |                 |
Description
EnablestheRemoteNetworkMonitoringagent(rmond)tostartcollectinghistoricalinterfacestatistics.
Thenoformofthiscommandstopsthehistoricalinterfacestatisticscollection.
Example
Enablingthermondagenttostarthistoricalinterfacestatisticscollection:
| switch(config)# | snmp-server |     | historical-counters-monitor |     |
| --------------- | ----------- | --- | --------------------------- | --- |
Disablingthermondagenttostophistoricalinterfacestatisticscollection:
| switch(config)#     | no  | snmp-server |     | historical-counters-monitor |
| ------------------- | --- | ----------- | --- | --------------------------- |
| Command History     |     |             |     |                             |
| Release             |     |             |     | Modification                |
| 10.07orearlier      |     |             |     | --                          |
| Command Information |     |             |     |                             |
|38

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| snmp-server | host |     |     |
| ----------- | ---- | --- | --- |
snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
| [port <UDP-PORT>] | [<VRF-NAME>] |     |     |
| ----------------- | ------------ | --- | --- |
no snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
| [port <UDP-PORT>] | [<VRF-NAME>] |     |     |
| ----------------- | ------------ | --- | --- |
snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
| [port <UDP-PORT>] | [<VRF-NAME>] |     |     |
| ----------------- | ------------ | --- | --- |
no snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
| [port <UDP-PORT>] | [<VRF-NAME>] |     |     |
| ----------------- | ------------ | --- | --- |
snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user
| <NAME> [port | <UDP-PORT>] | [<VRF-NAME>] |     |
| ------------ | ----------- | ------------ | --- |
no snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user
| <NAME> [port | <UDP-PORT>] | [<VRF-NAME>] |     |
| ------------ | ----------- | ------------ | --- |
Description
Configuresatrap/informsreceivertowhichtheSNMPagentcansendSNMPv1/v2c/v3trapsorv2c
informs.Amaximumof30SNMPtraps/informsreceiverscanbeconfigured.
Thenoformofthiscommandremovesthespecifiedtrap/informreceiver.
| Parameter   |     |     | Description                                      |
| ----------- | --- | --- | ------------------------------------------------ |
| <IPv4-ADDR> |     |     | SpecifiestheIPaddressofatrapreceiverinIPv4format |
(x.x.x.x),wherexisadecimalnumberfrom0to255.Youcan
removeleadingzeros.Forexample,theaddress
192.169.005.100becomes192.168.5.100.
| <IPv6-ADDR> |     |     | SpecifiestheIPaddressofatrapreceiverinIPv6format |
| ----------- | --- | --- | ------------------------------------------------ |
(x:x::x:x).
trap version <VERSION> SpecifiesthetrapnotificationtypeforSNMPv1,v2corv3.
Availableoptionsare:v1,v2corv3.
inform version v2c SpecifiestheinformnotificationtypeforSNMPv2c.
| trap version | v3  |     |     |
| ------------ | --- | --- | --- |
SpecifiesthetrapnotificationtypeforSNMPv3.
| user <NAME> |     |     | SpecifiestheSNMPv3usernametobeusedintheSNMPtrap |
| ----------- | --- | --- | ----------------------------------------------- |
notifications.
| community | <STRING> |     |     |
| --------- | -------- | --- | --- |
Specifiesthenameofthecommunitystringtousewhensending
trapnotifications.Range:1-32printableASCIIcharacters,
excludingspaceandquestionmark.Default:public.
<UDP-PORT>
SpecifiestheUDPportonwhichnotificationsaresent.Range:1-
65535.Default:162.
<VRF-NAME> SpecifiestheVRFonwhichtheSNMPagentlistensforincoming
requests.
39
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------- | ------------------------- | --- | --- |

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
2000
switch(config)# snmp-server host a:b::c:d trap version v3 user Admin port 2000
switch(config)# no snmp-server host a:b::c:d trap version v3 user Admin port 2000

Command History

Release

10.07 or earlier

Command Information

Modification

--

| 40

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server | response-source |     |     |
| ----------- | --------------- | --- | --- |
snmp-server response source {interface <name>}|<ip> vrf <VRF_NAME>
| no snmp-server | response | source {interface | <name>}|{<ip>} |
| -------------- | -------- | ----------------- | -------------- |
Description
ConfiguresthesourceinterfaceorIPaddressorsendingSNMPresponses.
ThenoformofthiscommandremovesthesourceinterfacenameorIPaddressforsendingSNMP
responses.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
interface <name>|<ip> Specifyasourceinterfacename.Theinterfacenamecanbea
physicalinterface,loopbackinterfaceorVLANinterface.
| <ip> |     |     | Specify theIPv4addressofsourceinterfacefortheSNMP |
| ---- | --- | --- | ------------------------------------------------- |
response.
vrf <VRF_NAME> VRFassociatedtothesourceinterfacefortheSNMPresponse.
Examples
Configuringaresponsesourceforinterface1/1/12:
switch(config)# snmp-server response-source interface 1/1/12 vrf vrftest1
Configuringaresponsesourceforinterfaceloopback10:
switch(config)# snmp-server response-source interface loopback vrf vrftest2
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.10               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6400
8100
8320
8325
8360
41
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------- | ------------------------- | --- | --- |

| Platforms | Command |     | context | Authority |
| --------- | ------- | --- | ------- | --------- |
8400
9300
10000
| snmp-server    |             | snmpv3-only |     |     |
| -------------- | ----------- | ----------- | --- | --- |
| snmp-server    | snmpv3-only |             |     |     |
| no snmp-server | snmpv3-only |             |     |     |
Description
AcceptsSNMPv3messagesonly,SNMPv1andSNMPv2cwillbedisabled.BydefaultSNMPv1,SNMPv2c
andSNMPv3willallbeenabled.
ThenoformofthiscommandrestoresthedefaultsettingandreenablesSNMPv1andSNMPv2c.
Examples
ConfiguringSNMPv3messagesonly,anddisablingSNMPv1andSNMPv2c:
| switch(config)# |             | snmp-server | snmpv3-only |                   |
| --------------- | ----------- | ----------- | ----------- | ----------------- |
| Command         | History     |             |             |                   |
| Release         |             |             |             | Modification      |
| 10.10           |             |             |             | Commandintroduced |
| Command         | Information |             |             |                   |
| Platforms       | Command     |             | context     | Authority         |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --------------- |
8100
8320
8325
8360
8400
9300
10000
| snmp-server    |                | system-contact |          |     |
| -------------- | -------------- | -------------- | -------- | --- |
| snmp-server    | system-contact |                | <INFO>   |     |
| no snmp-server | system-contact |                | [<INFO>] |     |
Description
SetsSNMPcontactinformation.
ThenoformofthiscommandremovestheSNMPcontactinformation.
|42

| Parameter |     |     |     | Description                                           |     |
| --------- | --- | --- | --- | ----------------------------------------------------- | --- |
| <INFO>    |     |     |     | SpecifiesSNMPcontactinformation.Range:1to128printable |     |
ASCIIcharacters,exceptforquestionmark(?).
Examples
| DefinesSNMPcontactinformationtobeJohn |     |     |     | Smith, Lab | Admin: |
| ------------------------------------- | --- | --- | --- | ---------- | ------ |
switch(config)# snmp-server system-contact John Smith, Lab Admin
RemovesSNMPcontactinformation:
| switch(config)# |             | no snmp-server |     | system-contact |     |
| --------------- | ----------- | -------------- | --- | -------------- | --- |
| Command         | History     |                |     |                |     |
| Release         |             |                |     | Modification   |     |
| 10.07orearlier  |             |                |     | --             |     |
| Command         | Information |                |     |                |     |
| Platforms       | Command     | context        |     | Authority      |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    |                    | system-description |               |     |     |
| -------------- | ------------------ | ------------------ | ------------- | --- | --- |
| snmp-server    | system-description |                    | <DESCRIPTION> |     |     |
| no snmp-server | system-description |                    |               |     |     |
Description
SetstheSNMPsystemdescription.
ThenoformofthiscommandremovestheSNMPsystemdescription.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<DESCRIPTION>
SpecifiestheSNMPsystemdescription.Typicalcontenttoinclude
wouldbethefullnameandversionofthefollowing:
|     |     |     |     | n Hardwaretypeofthesystem |     |
| --- | --- | --- | --- | ------------------------- | --- |
|     |     |     |     | n Softwareoperatingsystem |     |
Networkingsoftware
n
Range:1to64printableASCIIcharacters,exceptforthequestion
mark(?).
Examples
DefinestheSNMPsystemdescriptiontobemainSwitch:
43
| AOS-CX10.12SNMP/MIBGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------- | --- | ------------------------- | --- | --- | --- |

| switch(config)# |     | snmp-server |     | system-description |     |     | mainSwitch |
| --------------- | --- | ----------- | --- | ------------------ | --- | --- | ---------- |
RemovestheSNMPsystemdescription:
| switch(config)# |             | no  | snmp-server |     | system-description |     | mainSwitch |
| --------------- | ----------- | --- | ----------- | --- | ------------------ | --- | ---------- |
| Command         | History     |     |             |     |                    |     |            |
| Release         |             |     |             |     | Modification       |     |            |
| 10.07orearlier  |             |     |             |     | --                 |     |            |
| Command         | Information |     |             |     |                    |     |            |
| Platforms       | Command     |     | context     |     | Authority          |     |            |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    |                 | system-location |     |        |     |     |     |
| -------------- | --------------- | --------------- | --- | ------ | --- | --- | --- |
| snmp-server    | system-location |                 |     | <INFO> |     |     |     |
| no snmp-server | system-location |                 |     |        |     |     |     |
Description
SetstheSNMPlocationinformation.
ThenoformofthiscommandremovestheSNMPlocationinformation.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<INFO>
SpecifiestheSNMPlocationinformation.Range:1to128
printableASCIIcharacters,exceptforthequestionmark(?).
Examples
| DefinestheSNMPlocationinformationtobeMain |     |     |     |     |     | Lab: |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | ---- | --- |
switch(config)#
|     |     | snmp-server |     | system-location |     | Main | Lab |
| --- | --- | ----------- | --- | --------------- | --- | ---- | --- |
RemovestheSNMPlocationinformation:
| switch(config)# |         | no  | snmp-server |     | system-location |     |     |
| --------------- | ------- | --- | ----------- | --- | --------------- | --- | --- |
| Command         | History |     |             |     |                 |     |     |
| Release         |         |     |             |     | Modification    |     |     |
| 10.07orearlier  |         |     |             |     | --              |     |     |
|44

| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server | trap |     |     |     |
| ----------- | ---- | --- | --- | --- |
snmp-server trap {cpu-utilization | memory-utilization | rmon-events}
no snmp-server trap {cpu-utilization | memory-utilization | rmon-events}
Description
EnablestheSNMPtraps.TheSNMPtrapsareenabledbydefault.
ThenoformofthiscommanddisablestheSNMPtraps.
| Parameter          |     |     | Description                       |     |
| ------------------ | --- | --- | --------------------------------- | --- |
| cpu-utilization    |     |     | EnablestheCPUutilizationtraps.    |     |
| memory-utilization |     |     | Enablesthememoryutilizationtraps. |     |
| rmon-events        |     |     | EnablestheRMONeventtraps.         |     |
Examples
EnablingtheSNMPtraps:
| switch(config)# | snmp-server |     | trap cpu-utilization    |     |
| --------------- | ----------- | --- | ----------------------- | --- |
| switch(config)# | snmp-server |     | trap memory-utilization |     |
| switch(config)# | snmp-server |     | trap rmon-events        |     |
DisablingtheSNMPtraps:
| switch(config)# | no  | snmp-server | trap cpu-utilization    |     |
| --------------- | --- | ----------- | ----------------------- | --- |
| switch(config)# | no  | snmp-server | trap memory-utilization |     |
| switch(config)# | no  | snmp-server | trap rmon-events        |     |
DisplayingtheSNMPtrapconfiguration:
| switch(config)# | show                    | running-config | all | inc | snmp |
| --------------- | ----------------------- | -------------- | --------- | ---- |
| snmp-server     | trap rmon-events        |                |           |      |
| snmp-server     | trap cpu-utilization    |                |           |      |
| snmp-server     | trap memory-utilization |                |           |      |
DisplayingCPUandMemoryusage:
| switch(config)#    | show | system            |     |     |
| ------------------ | ---- | ----------------- | --- | --- |
| Hostname           |      | : XXXX            |     |     |
| System Description |      | : XX.10.07.0001CI |     |     |
| System Contact     |      | :                 |     |     |
| System Location    |      | :                 |     |     |
45
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- |

| Vendor |     | : Aruba |     |
| ------ | --- | ------- | --- |
Product Name : JLXXXX XXXX Base Chassis/3xFT/18xFans/Cbl Mgr/X462 Bundle
| Chassis             | Serial Nbr        | : SG6ZOO9068    |              |
| ------------------- | ----------------- | --------------- | ------------ |
| Base MAC            | Address           | : f40343-806400 |              |
| AOS-CX Version      | : XX.10.07.0001CI |                 |              |
| Time Zone           |                   | : UTC           |              |
| Up Time             |                   | : 8 minutes     |              |
| CPU Util            | (%)               | : 1             |              |
| Memory Usage        | (%)               | : 10            |              |
| Command History     |                   |                 |              |
| Release             |                   |                 | Modification |
| 10.07orearlier      |                   |                 | --           |
| Command Information |                   |                 |              |
| Platforms           | Command           | context         | Authority    |
6300 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8100
8320
8325
8360
8400
9300
10000
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
| Command History |     |     |     |
| --------------- | --- | --- | --- |
|46

| Release |     |     |     | Modification                                       |
| ------- | --- | --- | --- | -------------------------------------------------- |
| 10.10   |     |     |     | Commandintroducedon4100i,6000,6100,8100,8320,8325, |
8360,8400,9300,and10000
| 10.09               |         |         |     | Commandintroducedon6200,6300and6400 |
| ------------------- | ------- | ------- | --- | ----------------------------------- |
| Command Information |         |         |     |                                     |
| Platforms           | Command | context |     | Authority                           |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    | trap                       | configuration-changes |     |     |
| -------------- | -------------------------- | --------------------- | --- | --- |
| snmp-server    | trap configuration-changes |                       |     |     |
| no snmp-server | trap configuration-changes |                       |     |     |
Description
EnablessendingSNMPtrapswhenevertheconfigurationchanges.Configurationtrapgenerationis
disabledbydefault.
ThenoformofthiscommanddisablessendingSNMPtrapsforconfigurationchanges.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
47
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- |

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
| switch(config)#     | no      | snmp-server |     | trap mac-notify   |
| ------------------- | ------- | ----------- | --- | ----------------- |
| Command History     |         |             |     |                   |
| Release             |         |             |     | Modification      |
| 10.08               |         |             |     | Commandintroduced |
| Command Information |         |             |     |                   |
| Platforms           | Command | context     |     | Authority         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    | trap        | module |     |     |
| -------------- | ----------- | ------ | --- | --- |
| snmp-server    | trap module |        |     |     |
| no snmp-server | trap module |        |     |     |
Description
EnablesSNMPtrapgenerationformodules.Moduletrapgenerationisenabledbydefault.Generates
themoduleeventtrapswheneveramodularlineorfabriccardchangesstate,whichincludesinserted,
removed,ready,anddown,aswellaswhenamodularcardisunrecognized.
ThenoformofthiscommanddisablestheSNMPtrapgenerationformoduleevents.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
module
SpecifiesSNMPtrapsformoduleevents.
Examples
|48

EnablingtheSNMPtrapsformodules:
| switch(config)# | snmp-server |     | trap | module |
| --------------- | ----------- | --- | ---- | ------ |
DisablingtheSNMPtrapsformodules:
| switch(config)#     | no      | snmp-server    |     | trap module       |
| ------------------- | ------- | -------------- | --- | ----------------- |
| switch(config)#     | show    | running-config |     |                   |
| no snmp-server      | trap    | module         |     |                   |
| Command History     |         |                |     |                   |
| Release             |         |                |     | Modification      |
| 10.10               |         |                |     | Commandintroduced |
| Command Information |         |                |     |                   |
| Platforms           | Command | context        |     | Authority         |
6400 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8400           |                    |               |     | forthiscommand. |
| -------------- | ------------------ | ------------- | --- | --------------- |
| snmp-server    | trap               | port-security |     |                 |
| snmp-server    | trap port-security |               |     |                 |
| no snmp-server | trap port-security |               |     |                 |
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
| switch(config)# | no  | snmp-server |     | trap port-security |
| --------------- | --- | ----------- | --- | ------------------ |
49
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- |

| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.10               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
6100
6200
6300
6400
8100
8360
| snmp-server | trap | snmp |     |
| ----------- | ---- | ---- | --- |
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
|50

| switch(config)# | snmp-server |     | trap | snmp |     |
| --------------- | ----------- | --- | ---- | ---- | --- |
EnablingonlySNMPv2authenticationtraps:
| switch(config)# | snmp-server |     | trap | snmp | authentication |
| --------------- | ----------- | --- | ---- | ---- | -------------- |
DisablingallSNMPtraps:
| switch(config)#     | no      | snmp-server |     | trap snmp         |     |
| ------------------- | ------- | ----------- | --- | ----------------- | --- |
| Command History     |         |             |     |                   |     |
| Release             |         |             |     | Modification      |     |
| 10.10               |         |             |     | Commandintroduced |     |
| Command Information |         |             |     |                   |     |
| Platforms           | Command | context     |     | Authority         |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server | trap-source |     | interface |     | vrf |
| ----------- | ----------- | --- | --------- | --- | --- |
snmp-server trap-source {interface <IF-NAME> | <IPv4-Address> | <IPv6-Address>} [vrf
<VRF-NAME>]
no snmp-server trap-source {interface <IF-NAME> | <IPv4-Address> | <IPv6-Address>} [vrf
<VRF-NAME>]
Description
ConfiguresSNMPtrapsourceinterfaceorIPaddressforaVRF.
ThenoformofthiscommandremovestheSNMPtrap-sourceconfigurationforaVRF.
| Parameter |     |     |     | Description                                        |     |
| --------- | --- | --- | --- | -------------------------------------------------- | --- |
| <IF-NAME> |     |     |     | Specifiesthesourceinterfacename.Interfacenamecanbe |     |
physicalinterface,loopbackinterface,LAGinterface,orVLAN
interface.
<IPv4-Address> SpecifiestheIPv4addressofsourceinterfacefortheSNMPtrap.
<IPv6-Address> SpecifiestheIPv6addressofsourceinterfacefortheSNMPtrap.
<VRF-NAME> SpecifiesthenameofaVRFassociatedtothesourceinterfacefor
theSNMPtrap.
Examples
ConfiguringSNMPtrapsourceinterfaceforaVRF.
51
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- | --- |

switch(config)# snmp-server trap-source interface 1/1/12 vrf sample
switch(config)#
|     | snmp-server | trap-source | interface | loopback10 | vrf sample |
| --- | ----------- | ----------- | --------- | ---------- | ---------- |
switch(config)# snmp-server trap-source interface vlan23 vrf sample
ConfiguringSNMPtrapsourceIPaddressforaVRF.
| switch(config)#     | snmp-server | trap-source | 10.0.0.1     | vrf red |     |
| ------------------- | ----------- | ----------- | ------------ | ------- | --- |
| switch(config)#     | snmp-server | trap-source | 1001::1      | vrf red |     |
| Command History     |             |             |              |         |     |
| Release             |             |             | Modification |         |     |
| 10.07orearlier      |             |             | --           |         |     |
| Command Information |             |             |              |         |     |
| Platforms           | Command     | context     | Authority    |         |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    | trap     | vsx |     |     |     |
| -------------- | -------- | --- | --- | --- | --- |
| snmp-server    | trap vsx |     |     |     |     |
| no snmp-server | trap vsx |     |     |     |     |
Description
EnablessendingtheSNMPtrapsforVSXrelatedevents.VSXtrapgenerationisdisabledbydefault.
ThenoformofthiscommanddisablessendingtheSNMPtrapsforVSXrelatedevents.
ThetrapsupportisavailableforthefollowingVSXevents:
n ISLupanddown
n KAupanddown
n MCLAGupanddown
| Parameter |     |     | Description                     |     |     |
| --------- | --- | --- | ------------------------------- | --- | --- |
| vsx       |     |     | SpecifiesSNMPtrapsforVSXevents. |     |     |
Examples
EnablingtheVSXtraps:
| switch(config)# | snmp-server | trap              | vsx  |     |     |
| --------------- | ----------- | ----------------- | ---- | --- | --- |
| switch(config)# | show        | vsx configuration | trap |     |     |
| SNMP traps      | : Enabled   |                   |      |     |     |
|52

DisablingtheVSXtraps:
| switch(config)#     | no         | snmp-server       | trap         | vsx  |
| ------------------- | ---------- | ----------------- | ------------ | ---- |
| switch(config)#     | show       | vsx configuration |              | trap |
| SNMP traps          | : Disabled |                   |              |      |
| Command History     |            |                   |              |      |
| Release             |            |                   | Modification |      |
| 10.07orearlier      |            |                   | --           |      |
| Command Information |            |                   |              |      |
| Platforms           | Command    | context           | Authority    |      |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| Configuration | failed: | Maximum | allowed | views are configured. |
| ------------- | ------- | ------- | ------- | --------------------- |
Examples
53
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- |

ConfiguringtheSNMP MIB views:
switch(config)# snmp-server view name1 .1.3.6.1.2.1.2.2.1.1.1 FF:A0 included
switch(config)# snmp-server view name2 IF-MIB::ifindex included
switch(config)# snmp-server view name4 1.3.6.1.2.1.1 fe:00 included
RemovinganSNMPMIBview:
switch(config)# no snmp-server view name4 1.3.6.1.2.1.1 fe:00 included
| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.10               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    | vrf            |     |     |
| -------------- | -------------- | --- | --- |
| snmp-server    | vrf <VRF-NAME> |     |     |
| no snmp-server | vrf <VRF-NAME> |     |     |
Description
ConfiguresaVRFonwhichtheSNMPagentlistensforincomingrequests.Bydefault,theSNMPagent
doesnotlistenonanyVRF.4100i,6000,and6100onlysupportdefaultVRF.TheSNMPagentcanlisten
onmultipleVRFs.
ThenoformofthiscommandstopstheSNMPagentfromlisteningforincomingrequestsonthe
specifiedVRF.
| Parameter  |     |     | Description             |
| ---------- | --- | --- | ----------------------- |
| <VRF-NAME> |     |     | SpecifiesthenameofaVRF. |
Examples
ConfiguringtheSNMPagenttolistenonVRFdefault.
| switch(config)# | snmp-server | vrf | default |
| --------------- | ----------- | --- | ------- |
ConfiguringtheSNMPagenttolistenonVRFmgmt.
switch(config)#
|     | snmp-server | vrf | mgmt |
| --- | ----------- | --- | ---- |
ConfiguringtheSNMPagenttolistenonused-definedVRFmyvrf.
|54

| switch(config)# |     | snmp-server |     | vrf | myvrf |     |
| --------------- | --- | ----------- | --- | --- | ----- | --- |
StoppingtheSNMPagentfromlisteningonVRFdefault.
| switch(config)# |             | no  | snmp-server |     | vrf default  |     |
| --------------- | ----------- | --- | ----------- | --- | ------------ | --- |
| Command         | History     |     |             |     |              |     |
| Release         |             |     |             |     | Modification |     |
| 10.07orearlier  |             |     |             |     | --           |     |
| Command         | Information |     |             |     |              |     |
| Platforms       | Command     |     | context     |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmpv3    | context        |        |                |             |            |           |
| --------- | -------------- | ------ | -------------- | ----------- | ---------- | --------- |
| snmpv3    | context <NAME> |        | vrf <VRF-NAME> |             | [community | <STRING>] |
| no snmpv3 | context        | <NAME> | [vrf           | <VRF-NAME>] | [community | <STRING>] |
Description
CreatesanSNMPv3contextonthespecifiedVRF.
ThenoformofthiscommandremovesthespecifiedSNMPcontext.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<NAME>
Specifiesthenameofthecontext.Range:1to32printableASCII
characters,excludingspaceandquestionmark(?).
vrf <VRF-NAME> SpecifiestheVRFassociatedwiththecontext.Default:default.
| community | <STRING> |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- |
SpecifiestheSNMPcommunitystringassociatedwiththecontext.
Range:1to32printableASCIIcharacters,excludingspaceand
questionmark.Default:public.
Examples
CreatinganSNMPv3contextnamednewContext:
| switch(config)# |     | snmpv3 | context |     | newContext |     |
| --------------- | --- | ------ | ------- | --- | ---------- | --- |
CreatinganSNMPv3contextnamednewContextonVRFmyVrfandwithcommunitystringprivate.
switch(config)# snmpv3 context newContext vrf myVrf community private
55
| AOS-CX10.12SNMP/MIBGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |     |     |
| ------------------------- | --- | ------------------------- | --- | --- | --- | --- |

RemovingtheSNMPv3contextnamednewContextonVRFmyVrf:
| switch(config)# |             | no snmpv3 | context | newContext   | vrf myVrf |
| --------------- | ----------- | --------- | ------- | ------------ | --------- |
| Command         | History     |           |         |              |           |
| Release         |             |           |         | Modification |           |
| 10.07orearlier  |             |           |         | --           |           |
| Command         | Information |           |         |              |           |
| Platforms       | Command     | context   |         | Authority    |           |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmpv3    | engine-id |             |     |     |     |
| --------- | --------- | ----------- | --- | --- | --- |
| snmpv3    | engine-id | <ENGINE-ID> |     |     |     |
| no snmpv3 | engine-id | <ENGINE-ID> |     |     |     |
Description
ConfigurestheSNMPv3SNMPengine-idallowinganadministratortoconfigureauniqueSNMPengine-
idfortheswitch.Thisengine-idisusedbytheNMSmanagementtooltoidentifyanddistinguish
multipleswitchesonthesamenetwork.
Thenoformofthiscommandrestoresthedefaultengine-id,createdbytheswitchusingacombination
oftheenterpriseOIDvalueandtheswitch'smacaddress.
| Parameter   |     |     |     | Description                                    |     |
| ----------- | --- | --- | --- | ---------------------------------------------- | --- |
| <ENGINE-ID> |     |     |     | SNMPv3SNMPengine-idincolonseparatedhexadecimal |     |
notation.
Examples
ConfiguringtheSNMPv3engine-id:
switch(config)#
| switch(config)# |     | snmpv3 | engine-id |     |     |
| --------------- | --- | ------ | --------- | --- | --- |
WORD SNMPv3 snmp engine-id in colon seperated hexadecimal notation
switch(config)# snmpv3 engine-id 01:23:45:67:89:ab:cd:ef:01:23:45:67
RestoringthedefaultSNMPv3engine-id:
| switch(config)# |         | no snmpv3 | engine-id |     |     |
| --------------- | ------- | --------- | --------- | --- | --- |
| Command         | History |           |           |     |     |
|56

| Release        |             |     |         | Modification |     |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmpv3    | security-level |     |                       |     |     |
| --------- | -------------- | --- | --------------------- | --- | --- |
| snmpv3    | security-level |     | {auth | auth-privacy} |     |     |
| no snmpv3 | security-level |     | {auth | auth-privacy} |     |     |
Description
ConfigurestheSNMPv3securitylevel.ThesecurityleveldetermineswhichSMNPv3usersdefinedbythe
| commandsnmpv3 |     | userareabletoconnect. |     |     |     |
| ------------- | --- | --------------------- | --- | --- | --- |
Thenoformofthiscommandchangesthesecuritylevelasfollows:
n no snmpv3 security-level auth:Setsthesecurityleveltoauth-privacy.
n no snmpv3 security-level auth-privacy:Setsthesecurityleveltonoauthenticationorprivacy,
allowinganySNMPusertoconnect.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
auth
SNMPv3usersthatsupportauthentication,orauthenticationand
privacyareallowed.
auth-privacy OnlySNMPv3userswithbothauthenticationandprivacyare
allowed.ThisisthehighestlevelofSNMPv3security.Default.
Examples
SettingtheSNMPv3securityleveltoauthenticationandprivacy:
| switch(config)# |     | snmpv3 | security-level |     | auth-privacy |
| --------------- | --- | ------ | -------------- | --- | ------------ |
SettingtheSNMPv3securityleveltoauthenticationonly:
| switch(config)# |     | snmpv3 | security-level |     | auth |
| --------------- | --- | ------ | -------------- | --- | ---- |
SettingtheSNMPv3securityleveltonoauthenticationandnoprivacy:
| switch(config)# |     | no  | snmpv3 security-level |     | auth-privacy |
| --------------- | --- | --- | --------------------- | --- | ------------ |
RestoringthedefaultSNMPv3securityleveltoauthenticationandprivacy:
| switch(config)# |     | no  | snmpv3 security-level |     | auth |
| --------------- | --- | --- | --------------------- | --- | ---- |
57
| AOS-CX10.12SNMP/MIBGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------- | --- | ------------------------- | --- | --- | --- |

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmpv3 user |        |     |     |
| ----------- | ------ | --- | --- |
| snmpv3 user | <NAME> |     |     |
[auth <AUTH-PROTO> auth-pass [{plaintext | ciphertext} <AUTH-PASS>]]
[priv <PRIV-PROTO> priv-pass [{plaintext | ciphertext} <PRIV-PASS>]]
| [access-level  | ro|rw] |     |     |
| -------------- | ------ | --- | --- |
| no snmpv3 user | <NAME> |     |     |
[auth <AUTH-PROTO> auth-pass [{plaintext | ciphertext} <AUTH-PASS>]]
[priv <PRIV-PROTO> priv-pass [{plaintext | ciphertext} <PRIV-PASS>]]
| [access-level |     | ro|rw] |     |
| ------------- | --- | ------ | --- |
Description
CreatesanSNMPv3userandaddsittoanSNMPv3context.TheSNMPv3securitylevel(setwith
commandsnmpv3 security-level)determineswhichusersareallowedtoauthenticate.
ThenoformofthiscommandremovesthespecifiedSNMPv3user.
| Parameter |     |     | Description                                         |
| --------- | --- | --- | --------------------------------------------------- |
| <NAME>    |     |     | SpecifiestheSNMPv3username.Range1to32printableASCII |
characters,excludingspaceandquestionmark(?).
| access-level |     |     | ConfiguretheaccesslevelfortheSNMPv3user: |
| ------------ | --- | --- | ---------------------------------------- |
n ro:Allowread-onlyaccessfortheSNMPv3user
n rw:Allowread-writeaccessfortheSNMPv3user
auth <AUTH-PROTO> Selectstheauthenticationprotocolusedtovalidateuserlogins:
md5orsha1.
auth-pass [{plaintext | SpecifiestheSNMPv3userauthenticationpassword.Rangefor
ciphertext} <AUTH-PASS>] plaintextis8to32printableASCIIcharacters,excludingspace
andquestionmark(?).Rangeforciphertextis1to256
printableASCIIcharacters.Ciphertextisusedwhencopyinguser
configurationsettingsbetweenswitches.
priv <PRIV-PROTO> SelectstheSNMPv3privacyprotocol(encryptionmethod):aesor
des.
priv-pass [{plaintext | SpecifiestheSNMPv3userprivacyencryptionpassword.Range
ciphertext} <PRIV-PASS>] forplaintextis8to32printableASCIIcharacters,excluding
spaceandquestionmark(?).Rangeforciphertextis1to256
|58

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
printableASCIIcharacters.Ciphertextisusedwhencopyinguser
configurationsettingsbetweenswitches.
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
| switch(config)# |                | snmpv3         | user     | Admin2     |        | auth md5 | auth-pass |
| --------------- | -------------- | -------------- | -------- | ---------- | ------ | -------- | --------- |
| Enter the       | authentication |                |          | password:  |        | ******** |           |
| Re-Enter        | the            | authentication |          | password:  |        | ******** |           |
| Configure       | the            | privacy        | protocol |            | (y/n)? | y        |           |
| Enter the       | privacy        | protocol       |          | (aes/des)? |        |          |           |
aes
| Enter the | privacy | encryption |            |     | key: ******** |          |     |
| --------- | ------- | ---------- | ---------- | --- | ------------- | -------- | --- |
| Re-Enter  | the     | privacy    | encryption |     | key:          | ******** |     |
RemovingSNMPv3userAdmin1:
| switch(config)# |     | no  | snmpv3 | user | Admin1 |     |     |
| --------------- | --- | --- | ------ | ---- | ------ | --- | --- |
CreatinganSNMPuseronswitch1andthencreatingthesameuseronswitch2bycopyingfromthe
switch1configuration:
59
AOS-CX10.12SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

Onswitch1,configureausernamedAdmin3,andthenusetheshow running-configcommandto
displayswitchconfiguration.Saveacopyofthefullsnmpv3 usercommand(shownbyshow running-
config).Thissavedcommandisusedonswitch2.
switch1(config)# snmpv3 user Admin3 auth sha auth-pass plaintext F82#450h
|                  |     |                | priv           | des priv-pass |     | plaintext | F82#4eva |
| ---------------- | --- | -------------- | -------------- | ------------- | --- | --------- | -------- |
| switch1(config)# |     |                | exit           |               |     |           |          |
| switch1#         |     | show           | running-config |               |     |           |          |
| Current          |     | configuration: |                |               |     |           |          |
!
| !Version |     | AOS-CX | xx.xx.xx.xxxxxx |     |     |     |     |
| -------- | --- | ------ | --------------- | --- | --- | --- | --- |
!
snmpv3 user Admin3 auth sha auth-pass ciphertext AQBaf2d...FJVcZ3o=
| priv | des    | priv-pass | ciphertext |     | AQBaH2p...2jfTFwQ= |     |     |
| ---- | ------ | --------- | ---------- | --- | ------------------ | --- | --- |
| ssh  | server | vrf       | mgmt       |     |                    |     |     |
!
| interface |     | mgmt |     |     |     |     |     |
| --------- | --- | ---- | --- | --- | --- | --- | --- |
no shutdown
ip dhcp
| vlan | 1   |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
Onswitch2,executethesnmpv3 usercommandthatyousavedfromswitch1(asshownbyshow
running-config).Thiscreatestheuseronswitch2withthesameconfiguration.
switch2(config)# snmpv3 user Admin3 auth sha auth-pass ciphertext
AQBaf2d...FJVcZ3o=
|     |     |     | priv | des priv-pass |     | ciphertext | AQBaH2p...2jfTFwQ= |
| --- | --- | --- | ---- | ------------- | --- | ---------- | ------------------ |
Thefollowingcommandsetsaread-writeaccesslevelforanSNMPv3userwiththeusernameuser1.
switch(config)# snmpv3 user user1 auth md5 auth-pass plaintext abc1234 access-
| level          | rw          |         |     |         |     |                                       |     |
| -------------- | ----------- | ------- | --- | ------- | --- | ------------------------------------- | --- |
| Command        | History     |         |     |         |     |                                       |     |
| Release        |             |         |     |         |     | Modification                          |     |
| 10.09          |             |         |     |         |     | Theaccess-levelparameterisintroduced. |     |
| 10.07orearlier |             |         |     |         |     | --                                    |     |
| Command        | Information |         |     |         |     |                                       |     |
| Platforms      |             | Command |     | context |     | Authority                             |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmpv3    | user |             | view |                  |             |     |     |
| --------- | ---- | ----------- | ---- | ---------------- | ----------- | --- | --- |
| snmpv3    | user | <USER-NAME> |      | view <VIEW-NAME> |             |     |     |
| no snmpv3 | user | <USER-NAME> |      | view             | <VIEW-NAME> |     |     |
Description
|60

AssociatesauserwithanexistingSNMPMIBview.
ThenoformofthiscommandremovestheassociateduserfromthespecifiedSNMPMIBview.
| Parameter   |     |     | Description                                     |     |
| ----------- | --- | --- | ----------------------------------------------- | --- |
| <USER-NAME> |     |     | SpecifiestheusernamefortheSNMPMIB view.Acceptsa |     |
maximumof32characters.
| <VIEWNAME> |     |     | SpecifiestheviewnamefortheSNMPMIB view.Acceptsa |     |
| ---------- | --- | --- | ----------------------------------------------- | --- |
maximumof32characters.
Examples
AddingauserintheexistingSNMPMIBview:
| switch(config)# | snmpv3 | user | nw-admin | view my-nw-view |
| --------------- | ------ | ---- | -------- | --------------- |
RemovingtheuserfromtheSNMPMIBview:
| switch(config)# | no  | snmpv3 | user nw-admin | view my-nw-view |
| --------------- | --- | ------ | ------------- | --------------- |
AttachingunconfiguredorunknownSNMPviewtoanSNMPv3user:
| switch(config)#     | snmpv3  | user        | nw-admin          | view myView |
| ------------------- | ------- | ----------- | ----------------- | ----------- |
| View myView         | is not  | configured. |                   |             |
| Command History     |         |             |                   |             |
| Release             |         |             | Modification      |             |
| 10.10               |         |             | Commandintroduced |             |
| Command Information |         |             |                   |             |
| Platforms           | Command | context     | Authority         |             |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| Entity MIB | support |     |     |     |
| ---------- | ------- | --- | --- | --- |
TheEntityMIB,rfc6933,allowsnetworkmanagerstoretrievephysicalcontainmentandlogical
relationshipsfordevicesinthenetwork.TheentconfigChangetrapissenttoconfiguredSNMP-server
hostswhenachangeoccurs.Thetrapisconfiguredtosendnotificationsnomorethanonceevery5
seconds.WewillbesupportingtheEntityMIBforread-only.
Physicalcomponentsthataresupportedinclude:
Stack
n
n Chassis
61
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- |

n Fabric cards

n Fan trays

n Fans

n Line cards and their interfaces

n Management modules and the intake temperature sensor

n Power supplies

The slots for any removable component are also represented. The logical table of the Entity MIB
represents configured VLANs and the associated ports. The entConfigChange trap/notification is sent to
configured snmp-server hosts.

Location of the MIB files on the web
The MIB files for Aruba switches can be found on the Aruba Service Portal. You can apply the various
filters to filter by product series, software versions, and software release types.

Updated MIBs and Traps for AOS-CX 10.12
The following list contains the newly introduced MIBs and Traps for each software feature. Software is
provided along with the MIB and Traps supported name.

NETWORKING OID

MIB file

ARUBAWIRED-NETWORKING-OID.mib

Implemented MIB objects

n arubaWiredSwitchR9W94A

n arubaWiredSwitchR9W95A

n arubaWiredSwitchR9W96A

n arubaWiredSwitchR9W97A

n arubaWiredSwitchModuleR9W94A

n arubaWiredSwitchModuleR9W95A

n arubaWiredSwitchModuleR9W96A

n arubaWiredSwitchModuleR9W97A

LLDP

MIB file

ARUBAWIRED-LLDP-MIB

Implemented MIB objects

n arubaWiredLldpScalarConfig

o arubaWiredLldpMgmtAddrVlanId

Power Supply

| 62

MIB file
ARUBAWIRED-POWERSUPPLY-MIB
| Implemented | MIB objects |     |     |     |
| ----------- | ----------- | --- | --- | --- |
arubaWiredPSUStateEnum
| System Information |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
MIB file
ARUBAWIRED-SYSTEMINFO-MIB
| Implemented | MIB objects |     |     |     |
| ----------- | ----------- | --- | --- | --- |
n arubaWiredSystemInfoCpuAvgOneMin
n arubaWiredSystemInfoCpuAvgFiveMin
| OIDs that | support | SNMP | read-write |     |
| --------- | ------- | ---- | ---------- | --- |
ThefollowingtablecontainstheOIDsthatsupportSNMPread-write:
| Software Feature |     | MIB File       |     | OID          |
| ---------------- | --- | -------------- | --- | ------------ |
| SNMPv2System     |     | SNMPv2-MIB.mib |     | n sysContact |
n sysName
n sysLocation
PoE
|     |     | ARUBAWIRED-POE.mib |     | arubaWiredPoePethPsePortPoECycle |
| --- | --- | ------------------ | --- | -------------------------------- |
|     |     | POWER-ETHERNET-MIB |     | pethPsePortAdminEnable           |
VLAN IEEE8021QBridge-Mib n ieee8021QBridgeVlanStaticEgressPorts
n ieee8021QBridgeVlanStaticRowStatus
n ieee8021QBridgeVlanStaticUntaggedPorts
n ieee8021QBridgePvid
n ieee8021QBridgeMvrpEnabledStatus
Dot1QBridge-Mib
n Dot1QBridgeVlanStaticEgressPorts
n Dot1qVlanStaticRowStatus
n Dot1QBridgeVlanStaticUntaggedPorts
n Dot1QBridgePvid
n Dot1QBridgeMvrpEnabledStatus
Interface
|     |     | IF-MIB |     | n ifAdminStatus |
| --- | --- | ------ | --- | --------------- |
n ifAlias
|     |     | ARUBAWIRED-INTERFACE- |     | arubaWiredInterfaceAutoneg |
| --- | --- | --------------------- | --- | -------------------------- |
n
MIB
n arubaWiredInterfaceDuplex
n arubaWiredInterfaceSpeeds
| PortSecurity |     | ARUBAWIRED- |     |     |
| ------------ | --- | ----------- | --- | --- |
n arubaWiredPortSecurityGlobalEnab
PORTSECURITY-MIB
n arubaWiredPortSecurityEnable
63
| AOS-CX10.12SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- |

| Software Feature |     | MIB File |     | OID |
| ---------------- | --- | -------- | --- | --- |
n arubaWiredClientLimit
n arubaWiredViolationAction
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
|64

Support and Other Resources

Chapter 4

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

AOS-CX 10.12 SNMP/MIB Guide | (All AOS-CX Series Switches)

65

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
SupportandOtherResources|66

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

AOS-CX 10.12 SNMP/MIB Guide | (All AOS-CX Series Switches)

67