AOS-CX 10.13 SNMP/MIB
Guide

All AOS-CX Series Switches

Published: January 2024

Version: 2

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

AOS-CX 10.13 SNMP/MIB Guide | (All AOS-CX Series Switches)

3

Contents
| About this                          | document                                      | 6   |
| ----------------------------------- | --------------------------------------------- | --- |
| Applicableproducts                  |                                               | 6   |
| Latestversionavailableonline        |                                               | 6   |
| Commandsyntaxnotationconventions    |                                               | 6   |
| Abouttheexamples                    |                                               | 7   |
| Identifyingswitchportsandinterfaces |                                               | 8   |
| Identifyingmodularswitchcomponents  |                                               | 9   |
| SNMP                                |                                               | 11  |
| SNMPwrite:PoEwritecapabilities      |                                               | 11  |
| SNMPwrite:VLANwritecapabilities     |                                               | 11  |
| SNMPwrite:Configurations            |                                               | 12  |
| SNMPMIBview                         |                                               | 14  |
|                                     | ConfiguringSNMPMIB view                       | 15  |
|                                     | SNMPMIBviewlimitations                        | 15  |
| SNMPtraps                           |                                               | 15  |
| ConfiguringSNMP                     |                                               | 16  |
| SNMPcommands                        |                                               | 19  |
|                                     | event-trap-enable                             | 19  |
|                                     | lldptrapenable                                | 19  |
|                                     | mac-notifytraps                               | 22  |
|                                     | rmonalarm                                     | 24  |
|                                     | rmonalarm{enable|disable}{index|all}          | 25  |
|                                     | showconfiguration-changestrap                 | 26  |
|                                     | showmac-notify                                | 27  |
|                                     | showmac-notifyport                            | 27  |
|                                     | showrmonalarm                                 | 28  |
|                                     | showsnmpagent-port                            | 30  |
|                                     | showsnmpcommunity                             | 30  |
|                                     | showsnmpsystem                                | 31  |
|                                     | showsnmptrap                                  | 32  |
|                                     | showsnmpviews                                 | 32  |
|                                     | showsnmpvrf                                   | 33  |
|                                     | showsnmpv3context                             | 34  |
|                                     | showsnmpv3engine-id                           | 35  |
|                                     | showsnmpv3security-level                      | 35  |
|                                     | showsnmpv3users                               | 36  |
|                                     | snmp-serveragent-port                         | 37  |
|                                     | snmp-servercommunity                          | 37  |
|                                     | snmp-servercommunityview                      | 40  |
|                                     | snmp-serverhistorical-counters-monitor        | 41  |
|                                     | snmp-serverhost                               | 41  |
|                                     | snmp-serverresponse-source                    | 43  |
|                                     | snmp-serversnmpv3-only                        | 45  |
|                                     | snmp-serversystem-contact                     | 45  |
|                                     | snmp-serversystem-description                 | 46  |
|                                     | snmp-serversystem-location                    | 47  |
|                                     | snmp-servertrap                               | 48  |
|                                     | snmp-servertrapaaa-server-reachability-status | 49  |
4
AOS-CX10.13SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

|                                    | snmp-servertrapconfiguration-changes     |           | 50  |
| ---------------------------------- | ---------------------------------------- | --------- | --- |
|                                    | snmp-servertrapmac-notify                |           | 51  |
|                                    | snmp-servertrapmodule                    |           | 51  |
|                                    | snmp-servertrapport-security             |           | 52  |
|                                    | snmp-servertrapsnmp                      |           | 53  |
|                                    | snmp-servertrap-sourceinterfacevrf       |           | 54  |
|                                    | snmp-servertrapvsx                       |           | 55  |
|                                    | snmp-serverview                          |           | 56  |
|                                    | snmp-servervrf                           |           | 57  |
|                                    | snmpv3context                            |           | 58  |
|                                    | snmpv3engine-id                          |           | 59  |
|                                    | snmpv3security-level                     |           | 60  |
|                                    | snmpv3user                               |           | 61  |
|                                    | snmpv3userview                           |           | 64  |
| EntityMIBsupport                   |                                          |           | 65  |
| LocationoftheMIBfilesontheweb      |                                          |           | 66  |
| UpdatedMIBsandTrapsforAOS-CX10.13  |                                          |           | 66  |
|                                    | ChangesIntroducedin10.13.0001/10.13.0005 |           | 66  |
|                                    | RFCSupport                               |           | 66  |
|                                    | Fans                                     |           | 66  |
|                                    | NETWORKINGOID                            |           | 66  |
|                                    | SystemInformation                        |           | 67  |
|                                    | ESOConsortium                            |           | 67  |
|                                    | AuthenticationProtocols                  |           | 68  |
|                                    | ARUBAVSF                                 |           | 68  |
|                                    | LEDLocator                               |           | 68  |
|                                    | SwitchImage                              |           | 68  |
|                                    | PowerStatus                              |           | 69  |
|                                    | DeprecatedMIB                            |           | 69  |
|                                    | ObsoleteMIB                              |           | 69  |
|                                    | Newtraps                                 |           | 69  |
| OIDsthatsupportSNMPread-write      |                                          |           | 69  |
| OIDsthatsupportSNMPread-create     |                                          |           | 70  |
| Support                            | and Other                                | Resources | 71  |
| AccessingHPEArubaNetworkingSupport |                                          |           | 71  |
| AccessingUpdates                   |                                          |           | 72  |
|                                    | ArubaSupportPortal                       |           | 72  |
|                                    | MyNetworking                             |           | 72  |
| WarrantyInformation                |                                          |           | 72  |
| RegulatoryInformation              |                                          |           | 73  |
| DocumentationFeedback              |                                          |           | 73  |
|5

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
R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A, JL724B, JL725B, JL726B, JL727B, JL728B,
S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,  S0M87A,  S0M88A,  S0M89A,  S0M90A,
S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A, S0X44A)

n Aruba 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B, R0X40C, R0X41A,
R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C, R0X26A, R0X27A,
JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

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

AOS-CX 10.13 SNMP/MIB Guide | (All AOS-CX Series Switches)

6

Convention

Usage

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

About this document | 7

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

On the 4100i Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the 6000 and 6100 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

On the 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.
The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

AOS-CX 10.13 SNMP/MIB Guide | (All AOS-CX Series Switches)

8

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

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

About this document | 9

o member: 1.

o member: 1 or 2.

n The display module on the rear of the switch is not labeled with a member or slot number.

AOS-CX 10.13 SNMP/MIB Guide | (All AOS-CX Series Switches)

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

AOS-CX 10.13 SNMP/MIB Guide | (All AOS-CX Series Switches)

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
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 13

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
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 15

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
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 17

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

SNMP | 18

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
19
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches)

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
|20

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
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 21

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

| 22

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
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 23

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
| no rmon alarm | [index <INDEX>] |     |     |     |     |
| ------------- | --------------- | --- | --- | --- | --- |
Description
Storesconfigurationentriesinanalarmtablethatdefinesthesampleinterval,sample-type,and
thresholdparametersforanSNMPMIBobject.OnlytheSNMPMIBobjectsthatresolvetoanASN.1
primitivetypeofINTEGER(INTEGER,Integer32,Counter32,Counter64,Gauge32,orTimeTicks)willbe
monitored.
ThenoformofthiscommandremovesallRMONalarmsandallowsyoutospecifyanindextoremove
aparticularRMONalarm.
| Parameter           |     |     | Description                             |     |     |
| ------------------- | --- | --- | --------------------------------------- | --- | --- |
| index <INDEX>       |     |     | SpecifiestheRMONalarmindex.Range:1to20. |     |     |
| snmp-oid <SNMP-OID> |     |     |                                         |     |     |
SpecifiestheSNMPMIBobjecttobemonitoredbyRMON.
rising-threshold <RISING-THRESHOLD> SpecifiestheupperthresholdvaluefortheRMONalarm.
|24

| Parameter |     |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- |
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
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 25

| Parameter |     |     |     | Description                |     |
| --------- | --- | --- | --- | -------------------------- | --- |
| all       |     |     |     | SpecifiesalltheRMONalarms. |     |
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
| Command History |     |     |     |                   |     |
| --------------- | --- | --- | --- | ----------------- | --- |
| Release         |     |     |     | Modification      |     |
| 10.10           |     |     |     | Commandintroduced |     |
|26

| Command Information |         |         |     |           |
| ------------------- | ------- | ------- | --- | --------- |
| Platforms           | Command | context |     | Authority |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
show mac-notify
show mac-notify
Description
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
| Command History     |         |         |     |                   |
| ------------------- | ------- | ------- | --- | ----------------- |
| Release             |         |         |     | Modification      |
| 10.08               |         |         |     | Commandintroduced |
| Command Information |         |         |     |                   |
| Platforms           | Command | context |     | Authority         |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show mac-notify |       | port     |     |     |
| --------------- | ----- | -------- | --- | --- |
| show mac-notify | [port | <PORTS>] |     |     |
Description
DisplaystheMACnotificationconfigurationonarangeofports.
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 27

| Parameter |          |     |     |     | Description                                |
| --------- | -------- | --- | --- | --- | ------------------------------------------ |
| [port     | <PORTS>] |     |     |     | Specifiesaport,rangeofports,orlistofports. |
Examples
ShowingtheMACnotificationconfigurationonarangeofports:
switch(config)# show mac-notify port 1/1/1,1/1/3,1/1/5,lag101-lag104
| MAC  | notification |         | global | Setting: | Enabled |
| ---- | ------------ | ------- | ------ | -------- | ------- |
| Port |              | Enabled |        | Traps    |         |
---------------------------------------
| 1/1/1     |             | aged    | learned | moved   |                   |
| --------- | ----------- | ------- | ------- | ------- | ----------------- |
| 1/1/3     |             | --      |         |         |                   |
| 1/1/5     |             | moved   |         |         |                   |
| lag101    |             | removed |         |         |                   |
| lag102    |             | --      |         |         |                   |
| lag103    |             | --      |         |         |                   |
| lag104    |             | aged    | learned | moved   | removed           |
| Command   | History     |         |         |         |                   |
| Release   |             |         |         |         | Modification      |
| 10.08     |             |         |         |         | Commandintroduced |
| Command   | Information |         |         |         |                   |
| Platforms |             | Command |         | context | Authority         |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show      | rmon  | alarm  |     |          |     |
| --------- | ----- | ------ | --- | -------- | --- |
| show rmon | alarm | [index |     | <INDEX>] |     |
Description
DisplaystheRMONalarmconfigurations.
| Parameter |         |     |     |     | Description                             |
| --------- | ------- | --- | --- | --- | --------------------------------------- |
| index     | <INDEX> |     |     |     | SpecifiestheRMONalarmindex.Range:1to20. |
Examples
ShowingallRMONalarmconfigurations:
| switch# | show | rmon | alarm |     |     |
| ------- | ---- | ---- | ----- | --- | --- |
| Index   |      |      |       | : 1 |     |
|28

| Enabled           | : true                  |          |
| ----------------- | ----------------------- | -------- |
| Status            | : valid                 |          |
| MIB object        | : ifOutErrors.15        |          |
| Sample type       | : delta                 |          |
| Sampling          | interval : 6535 seconds |          |
| Rising threshold  | : 100                   |          |
| Falling threshold | : 10                    |          |
| Last sampled      | value : 0               |          |
| Last sample       | time : 2020-09-21       | 05:58:11 |
| Index             | : 3                     |          |
| Enabled           | : true                  |          |
| Status            | : invalid               |          |
| MIB object        | : IF-MIB::ifDescr.19    |          |
| Sample type       | : absolute              |          |
| Sampling          | interval : 10000        | seconds  |
| Rising threshold  | : 4000                  |          |
| Falling threshold | : 10                    |          |
| Last sampled      | value : 0               |          |
ShowingRMONalarmwithalarmindex1:
switch#
| show              | rmon alarm index        | 1        |
| ----------------- | ----------------------- | -------- |
| Index             | : 1                     |          |
| Enabled           | : true                  |          |
| Status            | : valid                 |          |
| MIB object        | : ifOutErrors.15        |          |
| Sample type       | : delta                 |          |
| Sampling          | interval : 6535 seconds |          |
| Rising threshold  | : 100                   |          |
| Falling threshold | : 10                    |          |
| Last sampled      | value : 0               |          |
| Last sample       | time : 2020-06-21       | 05:58:11 |
ShowingdisabledRMONalarminformation:
| switch# show      | rmon alarm              |          |
| ----------------- | ----------------------- | -------- |
| Index             | : 1                     |          |
| Enabled           | : false                 |          |
| Status            | : valid                 |          |
| MIB object        | : ifOutErrors.15        |          |
| Sample type       | : delta                 |          |
| Sampling          | interval : 6535 seconds |          |
| Rising threshold  | : 100                   |          |
| Falling threshold | : 10                    |          |
| Last sampled      | value : 0               |          |
| Last sample       | time : 2020-09-21       | 05:58:11 |
| Index             | : 3                     |          |
| Enabled           | : false                 |          |
| Status            | : invalid               |          |
| MIB object        | : IF-MIB::ifDescr.19    |          |
| Sample type       | : absolute              |          |
| Sampling          | interval : 10000        | seconds  |
| Rising threshold  | : 4000                  |          |
| Falling threshold | : 10                    |          |
| Last sampled      | value : 0               |          |
| Command History   |                         |          |
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 29

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show snmp            | agent-port |     |     |
| -------------------- | ---------- | --- | --- |
| show snmp agent-port |            |     |     |
Description
DisplaysSNMPagentUDPportnumber.
Example
DisplayingSNMPagentUDPportnumber:
| switch# show        | snmp agent-port |         |              |
| ------------------- | --------------- | ------- | ------------ |
| SNMP agent          | port : 161      |         |              |
| Command History     |                 |         |              |
| Release             |                 |         | Modification |
| 10.07orearlier      |                 |         | --           |
| Command Information |                 |         |              |
| Platforms           | Command         | context | Authority    |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show snmp           | community |     |     |
| ------------------- | --------- | --- | --- |
| show snmp community |           |     |     |
Description
DisplaysalistofallconfiguredSNMPv1/v2ccommunities.
Usage
WhenausercreatesacustomcommunitybeforeenablinganSNMPagent,AOS-CXautomatically
removesthedefaultpubliccommunityfromthesystem.
Example
DisplayingalistofallconfiguredSNMPv1/v2ccommunities:
|30

| switch#show | snmp community |     |     |     |     |
| ----------- | -------------- | --- | --- | --- | --- |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show snmp        | system |     |     |     |     |
| ---------------- | ------ | --- | --- | --- | --- |
| show snmp system |        |     |     |     |     |
Description
DisplaysSNMPdescription,location,andcontactinformation.
Example
DisplayingSNMPdescription,location,andcontactinformation:
| switch# show | snmp system |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- |
| SNMP system  | information |     |     |     |     |
----------------------------
| System description  |        | : Aggregation | router       |     |     |
| ------------------- | ------ | ------------- | ------------ | --- | --- |
| System location     | : Main | lab           |              |     |     |
| System contact      | : John | Smith, Lab    | Admin        |     |     |
| Command History     |        |               |              |     |     |
| Release             |        |               | Modification |     |     |
| 10.07orearlier      |        |               | --           |     |     |
| Command Information |        |               |              |     |     |
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 31

| Platforms | Command | context | Authority |     |     |
| --------- | ------- | ------- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show snmp      | trap |     |     |     |     |
| -------------- | ---- | --- | --- | --- | --- |
| show snmp trap |      |     |     |     |     |
Description
DisplaysallconfiguredSNMPtraps/informsreceivers.
Example
DisplayingallconfiguredSNMPtrapandinformsreceivers:
| switch# show | snmp trap |     |           |                    |          |
| ------------ | --------- | --- | --------- | ------------------ | -------- |
| HOST         |           |     | PORT TYPE | VER COMMUNITY/USER | NAME VRF |
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
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show snmp       | views |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- |
| show snmp views |       |     |     |     |     |
Description
DisplaysthelistofalltheconfiguredSNMPviews.
Usage
ThefollowingtablecontainsthestatusanditsdescriptionoftheconfiguredSNMPviews:
|32

| Status |     |     | Description |
| ------ | --- | --- | ----------- |
pending_validation DefaultvaluethatindicatesSNMPviewisyettobevalidated.
| operational |     |     | OIDandmaskvalidated. |
| ----------- | --- | --- | -------------------- |
InvalidOID/mask.
invalid
ValidationfailedforreasonsotherthanOID/mask.
failed
Examples
DisplayingthelistofalltheconfiguredSNMPviews:
| switch# show | snmp views |     |     |
| ------------ | ---------- | --- | --- |
------------------------------------------------------
| SNMP MIB | Views |     |     |
| -------- | ----- | --- | --- |
------------------------------------------------------
| View :              | new                |         |                   |
| ------------------- | ------------------ | ------- | ----------------- |
| OID Tree:           | sysUpTime.0        |         |                   |
| Mask :              | ff                 |         |                   |
| Type :              | included           |         |                   |
| Status :            | pending_validation |         |                   |
| View :              | admin              |         |                   |
| OID Tree:           | ifIndex.1          |         |                   |
| Mask :              | ff:a0              |         |                   |
| Type :              | included           |         |                   |
| Status :            | operational        |         |                   |
| View :              | user               |         |                   |
| OID Tree:           | sysb               |         |                   |
| Mask :              | none               |         |                   |
| Type :              | excluded           |         |                   |
| Status :            | invalid            |         |                   |
| View :              | admin              |         |                   |
| OID Tree:           | .1.3.6.1.2.1.1     |         |                   |
| Mask :              | none               |         |                   |
| Type :              | excluded           |         |                   |
| Status :            | operational        |         |                   |
| Command History     |                    |         |                   |
| Release             |                    |         | Modification      |
| 10.10               |                    |         | Commandintroduced |
| Command Information |                    |         |                   |
| Platforms           | Command            | context | Authority         |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show snmp | vrf |     |     |
| --------- | --- | --- | --- |
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 33

| show snmp vrf |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
Description
DisplaystheVRFonwhichtheSNMPagentserviceisrunning.
Example
DisplayingSNMPservicesenabledonVRF:
| switch#show  | snmp vrf |     |     |     |     |
| ------------ | -------- | --- | --- | --- | --- |
| SNMP enabled | VRF      |     |     |     |     |
----------------------------
mgmt
default
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show snmpv3 | context |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- |
| show snmpv3 | context |     |     |     |     |
Description
DisplaysallconfiguredSNMPcontexts.
Examples
DisplayingallconfiguredSNMPcontexts:
| switch# show | snmpv3 | context |     |     |     |
| ------------ | ------ | ------- | --- | --- | --- |
--------------------------------------------------------------------------
| name |     |     | vrf |     | community |
| ---- | --- | --- | --- | --- | --------- |
--------------------------------------------------------------------------
| contextA     |        |         | default |     | private |
| ------------ | ------ | ------- | ------- | --- | ------- |
| contextB     |        |         | vrf_A   |     | public  |
| switch# show | snmpv3 | context |         |     |         |
--------------------------------------------------------------------------
| Name | vrf |     | Community | ype[Instance_id] |     |
| ---- | --- | --- | --------- | ---------------- | --- |
------------------------------------------------------------------
| A   | default |     | public | vrf |     |
| --- | ------- | --- | ------ | --- | --- |
switch#
|34

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show snmpv3 | engine-id |     |     |
| ----------- | --------- | --- | --- |
| show snmpv3 | engine-id |     |     |
Description
DisplaystheconfiguredSNMPv3snmpengine-id.
IftheSNMPv3engine-idisnotconfigured,bydefaultauniqueengine-idiscreatedbytheswitchusinga
combinationoftheenterpriseOIDvalueandtheswitch'smacaddress.
Example
DisplayingtheconfiguredSNMPv3engine-id:
| switch# show        | snmpv3                          | engine-id |              |
| ------------------- | ------------------------------- | --------- | ------------ |
| SNMP engine-id      | : 80:00:B8:5C:08:00:09:1d:de:a5 |           |              |
| Command History     |                                 |           |              |
| Release             |                                 |           | Modification |
| 10.07orearlier      |                                 |           | --           |
| Command Information |                                 |           |              |
| Platforms           | Command                         | context   | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show snmpv3 | security-level |     |     |
| ----------- | -------------- | --- | --- |
| show snmpv3 | security-level |     |     |
Description
DisplaystheconfiguredSNMPv3securitylevel.
Examples
DisplayingtheconfiguredSNMPv3securitylevel:
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 35

| switch# show          | snmpv3  | security-level |              |     |     |
| --------------------- | ------- | -------------- | ------------ | --- | --- |
| SNMPv3 security-level |         | : auth         |              |     |     |
| Command History       |         |                |              |     |     |
| Release               |         |                | Modification |     |     |
| 10.07orearlier        |         |                | --           |     |     |
| Command Information   |         |                |              |     |     |
| Platforms             | Command | context        | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
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
| 10.07orearlier      |     |     | --  |     |     |
| ------------------- | --- | --- | --- | --- | --- |
| Command Information |     |     |     |     |     |
|36

| Platforms | Command |     | context |     | Authority |     |     |
| --------- | ------- | --- | ------- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
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
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 37

AddsanSNMPv1/SNMPv2ccommunitystring.Acommunitystringislikeapasswordthatcontrols
read/writeaccesstotheSNMPagent.Anetworkmanagementprogrammustsupplythisnamewhen
attemptingtogetSNMPinformationfromtheswitch.Amaximumof10communitystringsare
supported.Onceyoucreateyourowncommunitystring,thedefaultcommunitystring(public)is
deleted.
ThenoformofthiscommandremovesthespecifiedSNMPv1/SNMPv2ccommunitystring.Whenno
communitystringexists,adefaultcommunitystringwiththevaluepublicisautomaticallydefined.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<STRING>
SpecifiestheSNMPv1/SNMPv2ccommunitystring.Range:1to32
printableASCIIcharacters,excludingspaceandquestionmark.
Subcommands
| access-level    | {ro | | rw}     |     |     |
| --------------- | --- | --------- | --- | --- |
| no access-level |     | {ro | rw} |     |     |
ThissubcommandchangestheaccessleveloftheSNMPcommunity.Thedefaultaccesslevelisread-
only(ro).
Thenoformofthissubcommandchangestheaccesslevelofthecommunitytodefault.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
ro
SpecifiesRead-OnlyaccesswiththeSNMPcommunity.
| rw             |       |         | SpecifiesRead-WriteaccesswiththeSNMPcommunity. |     |
| -------------- | ----- | ------- | ---------------------------------------------- | --- |
| access-list    | {ipv4 | | ipv6} | <ACL-NAME>                                     |     |
| no access-list | {ipv4 | | ipv6} | <ACL-NAME>                                     |     |
ThissubcommandassociatesanACLwiththeSNMPcommunity.IfanACLisnotassociatedwiththe
SNMPcommunity,thedefaultaccessisallowedforallthehosts.
ThenoformofthissubcommandremovesassociationoftheACLwiththeSNMPcommunity.
| Parameter |     |     | Description              |     |
| --------- | --- | --- | ------------------------ | --- |
| ipv4      |     |     | SpecifiestheIPv4ACLtype. |     |
| ipv6      |     |     | SpecifiestheIPv6ACLtype. |     |
<ACL-NAME> SpecifiestheACLname.Itsupportsamaximumof64characters.
Examples
SettingtheSNMPv1/SNMPv2ccommunitystringtoprivate:
| switch(config)# |     | snmp-server | community | private |
| --------------- | --- | ----------- | --------- | ------- |
RemovingSNMPv1/SNMPv2ccommunitystringprivate:
| switch(config)# |     | no snmp-server | community | private |
| --------------- | --- | -------------- | --------- | ------- |
|38

ConfiguringtheaccesslevelfortheSMNPcommunitytoread-only:
| switch(config-community)# |     | access-level | ro  |
| ------------------------- | --- | ------------ | --- |
ChangingtheaccessleveloftheSNMP communitytodefault:
| switch(config-community)# |     | no access-level | rw  |
| ------------------------- | --- | --------------- | --- |
AssociatinganIPv4ACLnamedmy_aclwiththeSMNPcommunity:
switch(config-community)#
|     |     | access-list | ipv4 my_acl |
| --- | --- | ----------- | ----------- |
RemovingtheassociatedIPv4ACLnamedmy_aclfromtheSNMPcommunity:
| switch(config-community)# |     | no access-list | ipv4 my_acl |
| ------------------------- | --- | -------------- | ----------- |
ThedenyruleisnotsupportedforSNMPACL.
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
| access-list | ipv4          | ipv4_acl  |     |
| access-list | ipv6          | ipv6_acl  |     |
ConfigurationnotsupportedforSNMPACL:
| access-list | ip ipv4_acl   |           |     |
| ----------- | ------------- | --------- | --- |
| 10 deny     | any 6.6.6.6   | 6.6.6.1   |     |
| access-list | ipv6 ipv6_acl |           |     |
| 10 deny     | any 6001::6   | 6000::1   |     |
| snmp-server | vrf default   |           |     |
| snmp-server | community     | my_comm_1 |     |
| access-list | ipv4          | ipv4_acl  |     |
| access-list | ipv6          | ipv6_acl  |     |
hitcountsforSNMPACLwillnotbeincremented.
Example:showaccess-listhitcountsipallwillnotshowthehitcountofSNMPACL.
| Command History |     |     |     |
| --------------- | --- | --- | --- |
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 39

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
|40

| Platforms | Command |     | context |     | Authority |
| --------- | ------- | --- | ------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|                | config-community            |                             |     |     | rightsforthiscommand. |
| -------------- | --------------------------- | --------------------------- | --- | --- | --------------------- |
| snmp-server    |                             | historical-counters-monitor |     |     |                       |
| snmp-server    | historical-counters-monitor |                             |     |     |                       |
| no snmp-server | historical-counters-monitor |                             |     |     |                       |
Description
EnablestheRemoteNetworkMonitoringagent(rmond)tostartcollectinghistoricalinterfacestatistics.
Thenoformofthiscommandstopsthehistoricalinterfacestatisticscollection.
Example
Enablingthermondagenttostarthistoricalinterfacestatisticscollection:
| switch(config)# |     | snmp-server |     | historical-counters-monitor |     |
| --------------- | --- | ----------- | --- | --------------------------- | --- |
Disablingthermondagenttostophistoricalinterfacestatisticscollection:
| switch(config)# |             | no  | snmp-server |     | historical-counters-monitor |
| --------------- | ----------- | --- | ----------- | --- | --------------------------- |
| Command         | History     |     |             |     |                             |
| Release         |             |     |             |     | Modification                |
| 10.07orearlier  |             |     |             |     | --                          |
| Command         | Information |     |             |     |                             |
| Platforms       | Command     |     | context     |     | Authority                   |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| snmp-server |     | host |     |     |     |
| ----------- | --- | ---- | --- | --- | --- |
snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
| [port <UDP-PORT>] |     | [<VRF-NAME>] |     |     |     |
| ----------------- | --- | ------------ | --- | --- | --- |
no snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
| [port <UDP-PORT>] |     | [<VRF-NAME>] |     |     |     |
| ----------------- | --- | ------------ | --- | --- | --- |
snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
| [port <UDP-PORT>] |     | [<VRF-NAME>] |     |     |     |
| ----------------- | --- | ------------ | --- | --- | --- |
no snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
| [port <UDP-PORT>] |     | [<VRF-NAME>] |     |     |     |
| ----------------- | --- | ------------ | --- | --- | --- |
snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user
| <NAME> [port | <UDP-PORT>] |     | [<VRF-NAME>] |     |     |
| ------------ | ----------- | --- | ------------ | --- | --- |
no snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user
| <NAME> [port | <UDP-PORT>] |     | [<VRF-NAME>] |     |     |
| ------------ | ----------- | --- | ------------ | --- | --- |
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 41

Description

Configures a trap/informs receiver to which the SNMP agent can send SNMP v1/v2c/v3 traps or v2c
informs. A maximum of 30 SNMP traps/informs receivers can be configured.

The no form of this command removes the specified trap/inform receiver.

Parameter

<IPv4-ADDR>

Description

Specifies the IP address of a trap receiver in IPv4 format (x.x.x.x),
where x is a decimal number from 0 to 255. You can remove
leading zeros. For example, the address 192.169.005.100
becomes 192.168.5.100.

<IPv6-ADDR>

Specifies the IP address of a trap receiver in IPv6 format (x:x::x:x).

trap version <VERSION>

Specifies the trap notification type for SNMPv1, v2c or v3.
Available options are: v1, v2c or v3.

inform version v2c

Specifies the inform notification type for SNMPv2c.

trap version v3

user <NAME>

community <STRING>

<UDP-PORT>

<VRF-NAME>

Examples

Specifies the trap notification type for SNMPv3.

Specifies the SNMPv3 user name to be used in the SNMP trap
notifications.

Specifies the name of the community string to use when sending
trap notifications. Range: 1 - 32 printable ASCII characters,
excluding space and question mark. Default: public.

Specifies the UDP port on which notifications are sent. Range: 1 -
65535. Default: 162.

Specifies the VRF on which the SNMP agent listens for incoming
requests.

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

| 42

public
switch(config)#
|     | snmp-server | host | a:b::c:d inform version | v2c community | public |
| --- | ----------- | ---- | ----------------------- | ------------- | ------ |
switch(config)# no snmp-server host a:b::c:d inform version v2c community public
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
switch(config)#
snmp-server host a:b::c:d inform version v2c community public port
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
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server | response-source |     |     |     |     |
| ----------- | --------------- | --- | --- | --- | --- |
snmp-server response-source {interface <IF-NAME> | <IPv4-ADDRESS> | <IPv6-ADDRESS>} [vrf
<VRF-NAME>]
no snmp-server response-source {interface <IF-NAME | <IPv4-ADDRESS> | <IPv6-ADDRESS>}
[vrf <VRF-NAME>]
Description
ConfiguresthesourceinterfaceorIPaddressforsendingSNMPresponses.EachSNMP can
independentlyhaveitsownuniqueresponsesourceIPaddress.
ThenoformofthiscommandremovesthesourceinterfacenameorIPaddressforsendingSNMP
responses.
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 43

n

It is recommended to use the loopback interface or ip address of the loopback interface as the response

source. If a device does not support a loopback interface, then configure SVI interface or SVI IP address as

the response source.

n The active gateway IP address cannot be configured as the response source.

n It is recommended to limit the maximum number of response source to five.

n The interface used for the response source should be in the up state. If the interface is down, the default

source IP will be used.

n The use of udp6 is mandatory for IPv6 SNMP operations. For example, you can use the following syntax:

snmpwalk -v2c -c public -m ALL udp6:[2100::2] .1.3.6.1.2.1.1.

Parameter

Description

interface <IF-NAME>

Specifies the source interface name. The interface can be a
physical interface, loopback interface, or VLAN interface.

<IPv4-ADDRESS>

<IPv6-ADDRESS>

vrf <VRF-NAME>

Examples

Specifies the IPv4 address of the source interface for the SNMP
response.

Specifies the IPv6 address of the source interface for the SNMP
response.

Specifies the VRF name associated to the source interface for the
SNMP response.

Configuring a response source for the interface 1/1/12:

switch(config)# snmp-server response-source interface 1/1/12 vrf red

Configuring a response source for interface loopback10:

switch(config)# snmp-server response-source interface loopback10 vrf red

Configuring a response source for the IPv4 address 10.0.0.1:

switch(config)# snmp-server response-source 10.0.0.1 vrf sample

Configuring a response source for the IPv6 address 2001::1:

switch(config)# snmp-server response-source 2001::1 vrf default

Command History

| 44

| Release   |             |         | Modification                |
| --------- | ----------- | ------- | --------------------------- |
| 10.13     |             |         | AddedsupportforIPv6address. |
| 10.10     |             |         | Commandintroduced.          |
| Command   | Information |         |                             |
| Platforms | Command     | context | Authority                   |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    | snmpv3-only |     |     |
| -------------- | ----------- | --- | --- |
| snmp-server    | snmpv3-only |     |     |
| no snmp-server | snmpv3-only |     |     |
Description
AcceptsSNMPv3messagesonly,SNMPv1andSNMPv2cwillbedisabled.BydefaultSNMPv1,SNMPv2c
andSNMPv3willallbeenabled.
ThenoformofthiscommandrestoresthedefaultsettingandreenablesSNMPv1andSNMPv2c.
Examples
ConfiguringSNMPv3messagesonly,anddisablingSNMPv1andSNMPv2c:
switch(config)#
snmp-server snmpv3-only
| Command   | History     |         |                   |
| --------- | ----------- | ------- | ----------------- |
| Release   |             |         | Modification      |
| 10.10     |             |         | Commandintroduced |
| Command   | Information |         |                   |
| Platforms | Command     | context | Authority         |
6300 config Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8100
8320
8325
8360
8400
9300
10000
| snmp-server    | system-contact |          |     |
| -------------- | -------------- | -------- | --- |
| snmp-server    | system-contact | <INFO>   |     |
| no snmp-server | system-contact | [<INFO>] |     |
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 45

Description
SetsSNMPcontactinformation.
ThenoformofthiscommandremovestheSNMPcontactinformation.
| Parameter |     |     |     | Description                                           |     |
| --------- | --- | --- | --- | ----------------------------------------------------- | --- |
| <INFO>    |     |     |     | SpecifiesSNMPcontactinformation.Range:1to128printable |     |
ASCIIcharacters,exceptforquestionmark(?).
Examples
| DefinesSNMPcontactinformationtobeJohn |     |     |     | Smith, Lab | Admin: |
| ------------------------------------- | --- | --- | --- | ---------- | ------ |
switch(config)# snmp-server system-contact John Smith, Lab Admin
RemovesSNMPcontactinformation:
| switch(config)# |             | no  | snmp-server | system-contact |     |
| --------------- | ----------- | --- | ----------- | -------------- | --- |
| Command         | History     |     |             |                |     |
| Release         |             |     |             | Modification   |     |
| 10.07orearlier  |             |     |             | --             |     |
| Command         | Information |     |             |                |     |
| Platforms       | Command     |     | context     | Authority      |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    |                    | system-description |     |               |     |
| -------------- | ------------------ | ------------------ | --- | ------------- | --- |
| snmp-server    | system-description |                    |     | <DESCRIPTION> |     |
| no snmp-server | system-description |                    |     |               |     |
Description
SetstheSNMPsystemdescription.
ThenoformofthiscommandremovestheSNMPsystemdescription.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<DESCRIPTION> SpecifiestheSNMPsystemdescription.Typicalcontenttoinclude
wouldbethefullnameandversionofthefollowing:
n Hardwaretypeofthesystem
n Softwareoperatingsystem
n Networkingsoftware
Range:1to64printableASCIIcharacters,exceptforthequestion
mark(?).
|46

Examples
DefinestheSNMPsystemdescriptiontobemainSwitch:
switch(config)#
|     |     | snmp-server |     | system-description |     |     | mainSwitch |
| --- | --- | ----------- | --- | ------------------ | --- | --- | ---------- |
RemovestheSNMPsystemdescription:
| switch(config)# |             | no  | snmp-server |     | system-description |     | mainSwitch |
| --------------- | ----------- | --- | ----------- | --- | ------------------ | --- | ---------- |
| Command         | History     |     |             |     |                    |     |            |
| Release         |             |     |             |     | Modification       |     |            |
| 10.07orearlier  |             |     |             |     | --                 |     |            |
| Command         | Information |     |             |     |                    |     |            |
| Platforms       | Command     |     | context     |     | Authority          |     |            |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    |                 | system-location |     |        |     |     |     |
| -------------- | --------------- | --------------- | --- | ------ | --- | --- | --- |
| snmp-server    | system-location |                 |     | <INFO> |     |     |     |
| no snmp-server | system-location |                 |     |        |     |     |     |
Description
SetstheSNMPlocationinformation.
ThenoformofthiscommandremovestheSNMPlocationinformation.
| Parameter |     |     |     |     | Description                                      |     |     |
| --------- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- |
| <INFO>    |     |     |     |     | SpecifiestheSNMPlocationinformation.Range:1to128 |     |     |
printableASCIIcharacters,exceptforthequestionmark(?).
Examples
| DefinestheSNMPlocationinformationtobeMain |     |             |     |                 |     | Lab: |     |
| ----------------------------------------- | --- | ----------- | --- | --------------- | --- | ---- | --- |
| switch(config)#                           |     | snmp-server |     | system-location |     | Main | Lab |
RemovestheSNMPlocationinformation:
| switch(config)# |         | no  | snmp-server |     | system-location |     |     |
| --------------- | ------- | --- | ----------- | --- | --------------- | --- | --- |
| Command         | History |     |             |     |                 |     |     |
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 47

| Release             |         |         | Modification |     |
| ------------------- | ------- | ------- | ------------ | --- |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
|48

| switch(config)#    | show | system            |     |
| ------------------ | ---- | ----------------- | --- |
| Hostname           |      | : XXXX            |     |
| System Description |      | : XX.10.07.0001CI |     |
| System Contact     |      | :                 |     |
| System Location    |      | :                 |     |
| Vendor             |      | : Aruba           |     |
Product Name : JLXXXX XXXX Base Chassis/3xFT/18xFans/Cbl Mgr/X462 Bundle
| Chassis Serial | Nbr               | : SG6ZOO9068    |     |
| -------------- | ----------------- | --------------- | --- |
| Base MAC       | Address           | : f40343-806400 |     |
| AOS-CX Version | : XX.10.07.0001CI |                 |     |
| Time Zone      |                   | : UTC           |     |
| Up Time        |                   | : 8 minutes     |     |
| CPU Util       | (%)               | : 1             |     |
| Memory Usage   | (%)               | : 10            |     |
cpu-utilizationandmemory-utilizationarenotsupportedin4100i,6000and6100switchseries.Formore
informationonfeaturesthatusethiscommand,refertotheSNMP/MIBGuideforyourswitchmodel.
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
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 49

DisablingtheSNMPtrapforAAAserverstatus:
switch(config)# no snmp-server trap aaa-server-reachability-status
| Command History |     |     |     |                                                    |
| --------------- | --- | --- | --- | -------------------------------------------------- |
| Release         |     |     |     | Modification                                       |
| 10.10           |     |     |     | Commandintroducedon4100i,6000,6100,8100,8320,8325, |
8360,8400,9300,and10000
| 10.09               |         |         |     | Commandintroducedon6200,6300and6400 |
| ------------------- | ------- | ------- | --- | ----------------------------------- |
| Command Information |         |         |     |                                     |
| Platforms           | Command | context |     | Authority                           |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
configuration-changes
SpecifiesSNMPtrapsforconfigurationchanges.
Examples
EnablingtheSNMPtrapsforconfigurationchanges:
| switch(config)# | snmp-server |     | trap | configuration-changes |
| --------------- | ----------- | --- | ---- | --------------------- |
DisablingtheSNMPtrapsforconfigurationchanges:
| switch(config)#     | no  | snmp-server |     | trap configuration-changes |
| ------------------- | --- | ----------- | --- | -------------------------- |
| Command History     |     |             |     |                            |
| Release             |     |             |     | Modification               |
| 10.10               |     |             |     | Commandintroduced          |
| Command Information |     |             |     |                            |
|50

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
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
| switch(config)#     | no      | snmp-server |     | trap mac-notify   |
| ------------------- | ------- | ----------- | --- | ----------------- |
| Command History     |         |             |     |                   |
| Release             |         |             |     | Modification      |
| 10.08               |         |             |     | Commandintroduced |
| Command Information |         |             |     |                   |
| Platforms           | Command | context     |     | Authority         |
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
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 51

| Parameter |     |     |     | Description                        |
| --------- | --- | --- | --- | ---------------------------------- |
| module    |     |     |     | SpecifiesSNMPtrapsformoduleevents. |
Examples
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
config
| 6400           |                    |               |     | Administratorsorlocalusergroupmemberswithexecution |
| -------------- | ------------------ | ------------- | --- | -------------------------------------------------- |
| 8400           |                    |               |     | rightsforthiscommand.                              |
| snmp-server    | trap               | port-security |     |                                                    |
| snmp-server    | trap port-security |               |     |                                                    |
| no snmp-server | trap port-security |               |     |                                                    |
Description
EnablesSNMPport-securityviolationtrapsonthesystem.Port-securityviolationtrapsareenabledby
default.
ThenoformofthiscommanddisablestheSNMPport-securityviolationtrapsonthesystem.
| Parameter     |     |     |     | Description                         |
| ------------- | --- | --- | --- | ----------------------------------- |
| port-security |     |     |     | SpecifiesSNMPtrapsforport-security. |
Examples
EnablingtheSNMPport-securityviolationtrapsonthesystem:
|52

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
rightsforthiscommand.
6000
6100
6200
6300
6400
8100
8360
| snmp-server | trap | snmp |     |     |
| ----------- | ---- | ---- | --- | --- |
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
| Parameter      |     |     | Description                    |     |
| -------------- | --- | --- | ------------------------------ | --- |
| authentication |     |     | Enablestheauthenticationtraps. |     |
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 53

| Parameter  |     |     | Description                                       |     |     |
| ---------- | --- | --- | ------------------------------------------------- | --- | --- |
| coldstart  |     |     | Enablesthecoldstarttraps.                         |     |     |
| warmstart  |     |     | Enablesthewarmstarttraps.                         |     |     |
| <VRF_NAME> |     |     | SpecifiestheVRFname.EnablestheSNMPv2trapsforaVRF. |     |     |
Examples
EnablingallSNMPv2traps:
| switch(config)# | snmp-server |     | trap | snmp |     |
| --------------- | ----------- | --- | ---- | ---- | --- |
EnablingonlySNMPv2authenticationtraps:
| switch(config)# | snmp-server |     | trap | snmp | authentication |
| --------------- | ----------- | --- | ---- | ---- | -------------- |
DisablingallSNMPtraps:
switch(config)#
|                     | no      | snmp-server |     | trap snmp         |     |
| ------------------- | ------- | ----------- | --- | ----------------- | --- |
| Command History     |         |             |     |                   |     |
| Release             |         |             |     | Modification      |     |
| 10.10               |         |             |     | Commandintroduced |     |
| Command Information |         |             |     |                   |     |
| Platforms           | Command | context     |     | Authority         |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
|54

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
physicalinterface,loopbackinterface,LAGinterface,orVLAN
interface.
<IPv4-Address>
SpecifiestheIPv4addressofsourceinterfacefortheSNMPtrap.
<IPv6-Address> SpecifiestheIPv6addressofsourceinterfacefortheSNMPtrap.
<VRF-NAME>
SpecifiesthenameofaVRFassociatedtothesourceinterfacefor
theSNMPtrap.
Examples
ConfiguringSNMPtrapsourceinterfaceforaVRF.
switch(config)#
|     | snmp-server | trap-source | interface | 1/1/12 vrf | sample |
| --- | ----------- | ----------- | --------- | ---------- | ------ |
switch(config)# snmp-server trap-source interface loopback10 vrf sample
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
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server    | trap     | vsx |     |     |     |
| -------------- | -------- | --- | --- | --- | --- |
| snmp-server    | trap vsx |     |     |     |     |
| no snmp-server | trap vsx |     |     |     |     |
Description
EnablessendingtheSNMPtrapsforVSXrelatedevents.VSXtrapgenerationisdisabledbydefault.
ThenoformofthiscommanddisablessendingtheSNMPtrapsforVSXrelatedevents.
ThetrapsupportisavailableforthefollowingVSXevents:
n ISLupanddown
KAupanddown
n
n MCLAGupanddown
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 55

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
| Platforms           | Command    | context     |               | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmp-server | view |     |     |     |
| ----------- | ---- | --- | --- | --- |
snmp-server view <VIEWNAME> <OID_TREE> [<MASK>] <included/excluded>
no snmp-server view <VIEWNAME> <OID_TREE> [<MASK>] <included/excluded>
Description
ConfiguresanSNMPMIBview.
ThenoformofthiscommandremovesthespecifiedSNMPMIBview.
| Parameter  |     |     |     | Description                                    |
| ---------- | --- | --- | --- | ---------------------------------------------- |
| <VIEWNAME> |     |     |     | SpecifiesthenameoftheSNMPMIBview.Supportsuptoa |
maximumof32characters.
<OID_TREE> SpecifiestheOIDtreetobeincludedorexcludedinSNMPMIB
|56

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
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
| Command History     |         |         |                    |     |
| ------------------- | ------- | ------- | ------------------ | --- |
| Release             |         |         | Modification       |     |
| 10.10               |         |         | Commandintroduced. |     |
| Command Information |         |         |                    |     |
| Platforms           | Command | context | Authority          |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
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
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 57

ThenoformofthiscommandstopstheSNMPagentfromlisteningforincomingrequestsonthe
specifiedVRF.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<VRF-NAME>
SpecifiesthenameofaVRF.
Examples
ConfiguringtheSNMPagenttolistenonVRFdefault.
| switch(config)# |     | snmp-server |     | vrf | default |     |
| --------------- | --- | ----------- | --- | --- | ------- | --- |
ConfiguringtheSNMPagenttolistenonVRFmgmt.
| switch(config)# |     | snmp-server |     | vrf | mgmt |     |
| --------------- | --- | ----------- | --- | --- | ---- | --- |
ConfiguringtheSNMPagenttolistenonused-definedVRFmyvrf.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmpv3    | context        |        |                |             |            |           |
| --------- | -------------- | ------ | -------------- | ----------- | ---------- | --------- |
| snmpv3    | context <NAME> |        | vrf <VRF-NAME> |             | [community | <STRING>] |
| no snmpv3 | context        | <NAME> | [vrf           | <VRF-NAME>] | [community | <STRING>] |
Description
CreatesanSNMPv3contextonthespecifiedVRF.
ThenoformofthiscommandremovesthespecifiedSNMPcontext.
|58

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<NAME> Specifiesthenameofthecontext.Range:1to32printableASCII
characters,excludingspaceandquestionmark(?).
vrf <VRF-NAME>
SpecifiestheVRFassociatedwiththecontext.Default:default.
community <STRING> SpecifiestheSNMPcommunitystringassociatedwiththecontext.
Range:1to32printableASCIIcharacters,excludingspaceand
questionmark.Default:public.
Examples
CreatinganSNMPv3contextnamednewContext:
| switch(config)# |     | snmpv3 | context | newContext |     |
| --------------- | --- | ------ | ------- | ---------- | --- |
CreatinganSNMPv3contextnamednewContextonVRFmyVrfandwithcommunitystringprivate.
switch(config)# snmpv3 context newContext vrf myVrf community private
RemovingtheSNMPv3contextnamednewContextonVRFmyVrf:
| switch(config)# |             | no  | snmpv3 context | newContext   | vrf myVrf |
| --------------- | ----------- | --- | -------------- | ------------ | --------- |
| Command         | History     |     |                |              |           |
| Release         |             |     |                | Modification |           |
| 10.07orearlier  |             |     |                | --           |           |
| Command         | Information |     |                |              |           |
| Platforms       | Command     |     | context        | Authority    |           |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 59

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
ConfigurestheSNMPv3securitylevel.ThesecurityleveldetermineswhichSMNPv3usersdefinedby
| thecommandsnmpv3 |     | userareabletoconnect. |     |     |
| ---------------- | --- | --------------------- | --- | --- |
Thenoformofthiscommandchangesthesecuritylevelasfollows:
n no snmpv3 security-level auth:Setsthesecurityleveltoauth-privacy.
n no snmpv3 security-level auth-privacy:Setsthesecurityleveltonoauthenticationorprivacy,
allowinganySNMPusertoconnect.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
auth SNMPv3usersthatsupportauthentication,orauthenticationand
privacyareallowed.
auth-privacy OnlySNMPv3userswithbothauthenticationandprivacyare
allowed.ThisisthehighestlevelofSNMPv3security.Default.
|60

Examples
SettingtheSNMPv3securityleveltoauthenticationandprivacy:
switch(config)#
|     | snmpv3 | security-level |     | auth-privacy |
| --- | ------ | -------------- | --- | ------------ |
SettingtheSNMPv3securityleveltoauthenticationonly:
| switch(config)# | snmpv3 | security-level |     | auth |
| --------------- | ------ | -------------- | --- | ---- |
SettingtheSNMPv3securityleveltonoauthenticationandnoprivacy:
| switch(config)# | no  | snmpv3 security-level |     | auth-privacy |
| --------------- | --- | --------------------- | --- | ------------ |
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
[auth <AUTH-PROTO> auth-pass [{plaintext | ciphertext} <AUTH-PASS>]]
[priv <PRIV-PROTO> priv-pass [{plaintext | ciphertext} <PRIV-PASS>]]
| [access-level |     | ro|rw] |     |     |
| ------------- | --- | ------ | --- | --- |
Description
CreatesanSNMPv3userandaddsittoanSNMPv3context.TheSNMPv3securitylevel(setwith
commandsnmpv3 security-level)determineswhichusersareallowedtoauthenticate.
ThenoformofthiscommandremovesthespecifiedSNMPv3user.
WhenupdatingtheauthenticationprotocolsandprivacyprotocolsfortheexistingSNMPv3users,youmustalso
updatetheaccesslevel.Otherwise,theaccesslevelwillbesettoread-only.
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 61

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

NOTE: Authentication passwords that
include special characters must be enclosed
in single quotation marks ('). For example,
'priv-pwd20246!@#'.

When the authentication password is not provided on the command line, plaintext authentication password

prompting occurs upon pressing Enter, followed by privacy encryption protocol prompting, and finally plaintext

encryption password prompting. The entered password characters are masked with asterisks.

| 62

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
CreatinganSNMPuseronswitch1andthencreatingthesameuseronswitch2bycopyingfromthe
switch1configuration:
Onswitch1,configureausernamedAdmin3,andthenusetheshow running-configcommandto
displayswitchconfiguration.Saveacopyofthefullsnmpv3 usercommand(shownbyshow running-
config).Thissavedcommandisusedonswitch2.
switch1(config)# snmpv3 user Admin3 auth sha auth-pass plaintext F82#450h
|                  |                | priv           | des | priv-pass |     | plaintext | F82#4eva |
| ---------------- | -------------- | -------------- | --- | --------- | --- | --------- | -------- |
| switch1(config)# |                | exit           |     |           |     |           |          |
| switch1#         | show           | running-config |     |           |     |           |          |
| Current          | configuration: |                |     |           |     |           |          |
!
| !Version | AOS-CX | xx.xx.xx.xxxxxx |     |     |     |     |     |
| -------- | ------ | --------------- | --- | --- | --- | --- | --- |
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 63

!
snmpv3 user Admin3 auth sha auth-pass ciphertext AQBaf2d...FJVcZ3o=
| priv | des    | priv-pass |      | ciphertext | AQBaH2p...2jfTFwQ= |     |     |
| ---- | ------ | --------- | ---- | ---------- | ------------------ | --- | --- |
| ssh  | server | vrf       | mgmt |            |                    |     |     |
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
| level   | rw      |     |     |     |     |                                                      |     |
| ------- | ------- | --- | --- | --- | --- | ---------------------------------------------------- | --- |
| Command | History |     |     |     |     |                                                      |     |
| Release |         |     |     |     |     | Modification                                         |     |
| 10.13   |         |     |     |     |     | Followingauthenticationprotocolsaresupported:sha224, |     |
sha256,sha384,andsha512.
Followingprivacyprotocolsaresupported:aes192andaes256.
| 10.09          |             |         |     |         |     | Theaccess-levelparameterwasintroduced. |     |
| -------------- | ----------- | ------- | --- | ------- | --- | -------------------------------------- | --- |
| 10.07orearlier |             |         |     |         |     | --                                     |     |
| Command        | Information |         |     |         |     |                                        |     |
| Platforms      |             | Command |     | context |     | Authority                              |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| snmpv3    | user |             | view |                  |             |     |     |
| --------- | ---- | ----------- | ---- | ---------------- | ----------- | --- | --- |
| snmpv3    | user | <USER-NAME> |      | view <VIEW-NAME> |             |     |     |
| no snmpv3 | user | <USER-NAME> |      | view             | <VIEW-NAME> |     |     |
Description
AssociatesauserwithanexistingSNMPMIBview.
ThenoformofthiscommandremovestheassociateduserfromthespecifiedSNMPMIBview.
|64

| Parameter   |     |     | Description                                     |     |
| ----------- | --- | --- | ----------------------------------------------- | --- |
| <USER-NAME> |     |     | SpecifiestheusernamefortheSNMPMIB view.Acceptsa |     |
maximumof32characters.
<VIEWNAME>
SpecifiestheviewnamefortheSNMPMIB view.Acceptsa
maximumof32characters.
Examples
AddingauserintheexistingSNMPMIBview:
switch(config)#
|     | snmpv3 | user | nw-admin | view my-nw-view |
| --- | ------ | ---- | -------- | --------------- |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| Entity MIB | support |     |     |     |
| ---------- | ------- | --- | --- | --- |
TheEntityMIB,rfc6933,allowsnetworkmanagerstoretrievephysicalcontainmentandlogical
relationshipsfordevicesinthenetwork.TheentconfigChangetrapissenttoconfiguredSNMP-server
hostswhenachangeoccurs.Thetrapisconfiguredtosendnotificationsnomorethanonceevery5
seconds.WewillbesupportingtheEntityMIBforread-only.
Physicalcomponentsthataresupportedinclude:
n Stack
n Chassis
n Fabriccards
n Fantrays
n Fans
AOS-CX10.13SNMP/MIBGuide|(AllAOS-CXSeriesSwitches) 65

n Line cards and their interfaces

n Management modules and the intake temperature sensor

n Power supplies

The slots for any removable component are also represented. The logical table of the Entity MIB
represents configured VLANs and the associated ports. The entConfigChange trap/notification is sent to
configured snmp-server hosts.

Location of the MIB files on the web

The MIB files for Aruba switches can be found on the Aruba Service Portal. You can apply the various
filters to filter by product series, software versions, and software release types.

Updated MIBs and Traps for AOS-CX 10.13

The following list contains the newly introduced, deprecated, and obsolete MIBs and Traps for each
software feature. Software is provided along with the MIB and Traps supported name.

Changes Introduced in 10.13.0001/10.13.0005

RFC Support

AOS-CX supports STD 62 for SNMP, which includes RFC3411, RFC3412, RFC3413, RFC3414, RFC3415,
RFC3416, RFC3417, and RFC3418.

Fans

MIB file

ARUBA-WIRED-FAN-MIB.mib

Implemented changes

On some 6200F and 6300F switches (JL728A/B, JL665A) with a PSU (Power Supply Unit) fan, the fan is
controlled by the PSU and not by the AOS-CX operating system. As a result, in AOS-CX10.12 and earlier
versions, the SNMPWalk output for the fan's RPM is always displayed as 0, which is the default value.
Starting with AOS-CX 10.13 version, the SNMPWalk output will indicate a value of -1 if the fan has no
RPM readback capabiltiy.

NETWORKING OID

MIB file

ARUBAWIRED-NETWORKING-OID.mib

Implemented MIB objects

n arubaWiredSwitchJL724B

n arubaWiredSwitchJL725B

n arubaWiredSwitchJL726B

n arubaWiredSwitchJL727B

n arubaWiredSwitchJL728B

n arubaWiredSwitchS0M81A

| 66

n arubaWiredSwitchS0M82A

n arubaWiredSwitchS0M83A

n arubaWiredSwitchS0M84A

n arubaWiredSwitchS0M85A

n arubaWiredSwitchS0M86A

n arubaWiredSwitchS0M87A

n arubaWiredSwitchS0M88A

n arubaWiredSwitchS0M89A

n arubaWiredSwitchS0M90A

n arubaWiredSwitchS0G13A

n arubaWiredSwitchS0G14A

n arubaWiredSwitchS0G15A

n arubaWiredSwitchS0G16A

n arubaWiredSwitchS0G17A

n arubaWiredSwitchModuleJL724B

n arubaWiredSwitchModuleJL725B

n arubaWiredSwitchModuleJL726B

n arubaWiredSwitchModuleJL727B

n arubaWiredSwitchModuleJL728B

n arubaWiredSwitchModuleS0M81A

n arubaWiredSwitchModuleS0M82A

n arubaWiredSwitchModuleS0M83A

n arubaWiredSwitchModuleS0M84A

n arubaWiredSwitchModuleS0M85A

n arubaWiredSwitchModuleS0M86A

n arubaWiredSwitchModuleS0M87A

n arubaWiredSwitchModuleS0M88A

n arubaWiredSwitchModuleS0M89A

n arubaWiredSwitchModuleS0M90A

n arubaWiredSwitchModuleS0G13A

n arubaWiredSwitchModuleS0G14A

n arubaWiredSwitchModuleS0G15A

n arubaWiredSwitchModuleS0G16A

n arubaWiredSwitchModuleS0G17A

System Information

MIB file

ARUBAWIRED-SYSTEMINFO-MIB.mib

Implemented objects

n arubaWiredSystemInfoCpuAvgOneMin

n arubaWiredSystemInfoCpuAvgFiveMin

ESO Consortium

AOS-CX 10.13 SNMP/MIB Guide | (All AOS-CX Series Switches)

67

MIB file

ESO-CONSORTIUM-MIB.mib

Implemented objects

n Implemented MIB objects

n usm3DESPrivProtocol

n usmAESCfb128PrivProtocol

n usmAESCfb192PrivProtocol

n usmAESCfb256PrivProtocol

Authentication Protocols

MIB file

SNMP-USM-HMAC-SHA2-MIB.mib

Implemented MIB objects

n usmHMAC128SHA224AuthProtocol

n usmHMAC192SHA256AuthProtocol

n usmHMAC256SHA384AuthProtocol

n usmHMAC384SHA512AuthProtocol

ARUBA VSF

MIB file

ARUBAWIRED-VSFv2-MIB.mib

Implemented MIB objects

arubaWiredVsfv2MemberEntPhysicalIndex

LED Locator

MIB file

ARUBAWIRED-LED-LOCATOR-MIB.mib

Implemented MIB objects

n arubaWiredLedLocatorTable

o arubaWiredLedLocatorGroupIndex

o arubaWiredLedLocatorName

o arubaWiredLedLocatorState

Switch Image

MIB file

ARUBAWIRED-SWITCH-IMAGE-MIB.mib

Implemented MIB objects

| 68

n arubaWiredDefaultBoot

n arubaWiredDefaultBootEnum

n arubaWiredBootProfileTimeout

n arubaWiredSwitchImageTable

o arubaWiredSwitchImageTypeEnum

o arubaWiredSwitchImageType

o arubaWiredSwitchImageVersion

o arubaWiredSwitchImageSize

o arubaWiredSwitchImageBuildDate

o arubaWiredSwitchImageSha

Power Status

MIB file

POWER-STAT-MIB.mib

Implemented MIB objects

n arubaWiredPowerStatTable

o arubaWiredPowerStatGroupIndex

o arubaWiredPowerStatTypeIndex

o arubaWiredPowerStatSlotIndex

o arubaWiredPowerStatName

o arubaWiredPowerStatType

o arubaWiredPowerStatPowerConsumed

o arubaWiredPowerStatPowerConsumedAverage

o arubaWiredPowerStatPowerConsumedAveragePeriod

Deprecated MIB

ARUBAWIRED-VSF-MIB.mib

Obsolete MIB

IPV6-MIB.mib

New traps

MAC notification

ARUBAWIRED-MACNOTIFY-MIB.mib

Implemented traps

n arubaWiredMacNotifyFromDest

n arubaWiredMacNotifyToDest

OIDs that support SNMP read-write

The following table contains the OIDs that support SNMP read-write:

AOS-CX 10.13 SNMP/MIB Guide | (All AOS-CX Series Switches)

69

| Software Feature |     | MIB File       |     | OID          |
| ---------------- | --- | -------------- | --- | ------------ |
| SNMPv2System     |     | SNMPv2-MIB.mib |     | n sysContact |
n sysName
n sysLocation
| PoE |     | ARUBAWIRED-POE.mib |     | arubaWiredPoePethPsePortPoECycle |
| --- | --- | ------------------ | --- | -------------------------------- |
|     |     | POWER-ETHERNET-MIB |     | pethPsePortAdminEnable           |
VLAN IEEE8021QBridge-Mib n ieee8021QBridgeVlanStaticEgressPorts
n ieee8021QBridgeVlanStaticRowStatus
n ieee8021QBridgeVlanStaticUntaggedPorts
n ieee8021QBridgePvid
n ieee8021QBridgeMvrpEnabledStatus
|     |     | Dot1QBridge-Mib |     | n Dot1QBridgeVlanStaticEgressPorts |
| --- | --- | --------------- | --- | ---------------------------------- |
n Dot1qVlanStaticRowStatus
n Dot1QBridgeVlanStaticUntaggedPorts
n Dot1QBridgePvid
Dot1QBridgeMvrpEnabledStatus
n
Interface
|     |     | IF-MIB |     | n ifAdminStatus |
| --- | --- | ------ | --- | --------------- |
n ifAlias
|     |     | ARUBAWIRED-INTERFACE- |     | n arubaWiredInterfaceAutoneg |
| --- | --- | --------------------- | --- | ---------------------------- |
MIB
n arubaWiredInterfaceDuplex
n arubaWiredInterfaceSpeeds
| PortSecurity |     | ARUBAWIRED- |     | n arubaWiredPortSecurityGlobalEnab |
| ------------ | --- | ----------- | --- | ---------------------------------- |
PORTSECURITY-MIB
n arubaWiredPortSecurityEnable
n arubaWiredClientLimit
n arubaWiredViolationAction
n arubaWiredRecoveryTimer
n arubaWiredShutdownRecovery
n arubaWiredStickyEnable
| OIDs that | support | SNMP | read-create |     |
| --------- | ------- | ---- | ----------- | --- |
ThefollowingtablecontainstheOIDsthatsupportSNMPread-create:
| Software Feature |     | MIB File |     | OID |
| ---------------- | --- | -------- | --- | --- |
PortSecurity ARUBAWIRED-PORTSECURITY- n arubaWiredClientMacVidList
MIB
n arubaWiredMacAddrRowStatus
|70

Chapter 4

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

AOS-CX
Software
Technical Update

https://developer.arubanetworks.com/hpe-aruba-networking-aoscx/docs/about

https://community.arubanetworks.com/

Videos on new features introduced in this release:

https://www.youtube.com/playlist?list=PLsYGHuNuBZcbWPEjjHuVMqP-Q_UL3CskS

AOS-CX 10.13 SNMP/MIB Guide | (All AOS-CX Series Switches)

71

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

Support and Other Resources | 72

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

AOS-CX 10.13 SNMP/MIB Guide | (All AOS-CX Series Switches)

73