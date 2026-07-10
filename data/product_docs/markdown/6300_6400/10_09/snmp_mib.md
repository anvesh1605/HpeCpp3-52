AOS-CX 10.09 SNMP/MIB
Guide

All AOS-CX Series Switches

Published: April 2022
Edition: 4

Copyright Information

© Copyright 2022 Hewlett Packard Enterprise Development LP.

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

| 2

Contents
Contents
| Contents                            |                                      | 3   |
| ----------------------------------- | ------------------------------------ | --- |
| About this                          | document                             | 5   |
| Applicableproducts                  |                                      | 5   |
| Latestversionavailableonline        |                                      | 5   |
| Commandsyntaxnotationconventions    |                                      | 5   |
| Abouttheexamples                    |                                      | 6   |
| Identifyingswitchportsandinterfaces |                                      | 7   |
| Identifyingmodularswitchcomponents  |                                      | 8   |
| SNMP                                |                                      | 9   |
| SNMPwrite:PoEwritecapabilities      |                                      | 9   |
| SNMPtraps                           |                                      | 9   |
| ConfiguringSNMP                     |                                      | 10  |
| SNMPcommands                        |                                      | 11  |
|                                     | event-trap-enable                    | 11  |
|                                     | lldptrapenable                       | 12  |
|                                     | mac-notifytraps                      | 14  |
|                                     | rmonalarm                            | 16  |
|                                     | rmonalarm{enable|disable}{index|all} | 17  |
|                                     | showmac-notify                       | 18  |
|                                     | showmac-notifyport                   | 18  |
|                                     | showrmonalarm                        | 19  |
|                                     | showsnmpagent-port                   | 21  |
|                                     | showsnmpcommunity                    | 21  |
|                                     | showsnmpsystem                       | 22  |
|                                     | showsnmptrap                         | 23  |
|                                     | showsnmpvrf                          | 23  |
|                                     | showsnmpv3context                    | 24  |
25
|     | showsnmpv3engine-id                           | 25  |
| --- | --------------------------------------------- | --- |
|     | showsnmpv3security-level                      | 25  |
|     | showsnmpv3users                               | 26  |
|     | snmp-serveragent-port                         | 26  |
|     | snmp-servercommunity                          | 27  |
|     | snmp-serverhistorical-counters-monitor        | 29  |
|     | snmp-serverhost                               | 30  |
|     | snmp-serversystem-contact                     | 32  |
|     | snmp-serversystem-description                 | 33  |
|     | snmp-serversystem-location                    | 34  |
|     | snmp-servervrf                                | 34  |
|     | snmp-servertrapaaa-server-reachability-status | 35  |
|     | snmp-servertrapmac-notify                     | 36  |
|     | snmp-servertrap-sourceinterfacevrf            | 37  |
|     | snmp-servertrap                               | 38  |
|     | snmp-servertrapvsx                            | 39  |
|     | snmpv3context                                 | 40  |
|     | snmpv3engine-id                               | 41  |
3
AOS-CX10.09SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

|                                     | snmpv3security-level |           | 42  |
| ----------------------------------- | -------------------- | --------- | --- |
|                                     | snmpv3user           |           | 43  |
| EntityMIBsupport                    |                      |           | 45  |
| LocationoftheMIBfilesontheweb       |                      |           | 45  |
| NewlyintroducedMIBsandTrapsfor10.09 |                      |           | 46  |
|                                     | AAA                  |           | 46  |
|                                     | MODULE               |           | 46  |
|                                     | NETWORKING           |           | 47  |
| OIDsthatsupportsSNMPwrite           |                      |           | 47  |
| Support                             | and Other            | Resources | 48  |
| AccessingArubaSupport               |                      |           | 48  |
| AccessingUpdates                    |                      |           | 49  |
|                                     | ArubaSupportPortal   |           | 49  |
|                                     | MyNetworking         |           | 49  |
| WarrantyInformation                 |                      |           | 49  |
| RegulatoryInformation               |                      |           | 49  |
| DocumentationFeedback               |                      |           | 50  |
Contents|4

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 4100i Switch Series (JL817A, JL818A)

n Aruba 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A)

n Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL704C, JL705C, JL706A, JL707A, JL708A,

JL709A, JL710A, JL711A, JL717C, JL718C)

n Aruba 8400 Switch Series (JL375A, JL376A)

n Aruba 10000 Switch Series (R8P13A, R8P14A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

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

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables are

AOS-CX 10.09 SNMP/MIB Guide | (All AOS-CX Series Switches)

5

Convention

Usage

n example-text

|

{ }

[ ]

… or

...

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

Brackets. Indicates that the enclosed item or items are optional.

Ellipsis:

n In code and screen examples, a vertical or horizontal ellipsis indicates an

omission of information.

n In syntax using brackets and braces, an ellipsis indicates items that can be

repeated. When an item followed by ellipses is enclosed in brackets, zero

or more items can be specified.

About the examples
Examples in this document are representative and might not match your particular switch or environment.

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

In certain configuration contexts, the prompt may include variable information. For example, when in the
VLAN configuration context, a VLAN number appears in the prompt:
switch(config-vlan-100)#

When referring to this context, this document uses the syntax:
switch(config-vlan-<VLAN-ID>)#

About this document | 6

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

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

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

On the 83xx and 10000 Switch Series

AOS-CX 10.09 SNMP/MIB Guide | (All AOS-CX Series Switches)

7

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

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

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

About this document | 8

Chapter 2

SNMP

SNMP

Simple Network Management Protocol (SNMP) is an Internet-standard protocol used for managing and
monitoring the devices connected to a network by collecting, organizing and modifying information about
managed devices on IP networks.

SNMP write: PoE write capabilities

PoE enable

The PoE enable is requested through SNMP to enable the PoE interface. The admin_disable SNMP value is
updated to enable the PoE interface.

PoE disable

The PoE disable is requested through SNMP to disable the PoE interface. The admin_disable SNMP value is
updated to disable the PoE interface.

PoE cycle

The PoE cycle is a feature where you can request a PoE port reset with a timeout ranging from 1 to 60
seconds. The PoE cycle is requested through the SNMP server to disable and enable a PoE interface with an
input timeout of 1 to 60 seconds. The PoE handles the PoE disable and enable events when the SNMP value
is updated for admin_disable correspondingly. The value of timeout ranges from 1-60 seconds. It is a one-
time operation.

SNMP traps

Event log traps

When SNMP is configured, interface daemons event log messages for link-up and link-down events will be
sent as traps.

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

AOS-CX 10.09 SNMP/MIB Guide | (All AOS-CX Series Switches)

9

Standard IF-MIB link-up and link-down traps will be sent on link-state change when an interface is
configured using trap link-status or when user_config:link_state_snmp_trap is set to true. The trap
sends the current information for ifindex, admin status, operational status, and interface name.

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

Contains the OID for the link up or linkdown
trap

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
SNMP agent provides read-write access for specific OIDs. Refer OIDs that supports SNMP write for the list
of OIDs that supports write operations.

Procedure

1. SNMP is not enabled on the switch by default, unless the user enables it over any available VRF or
with the default/mgmt VRF using the command snmp-server vrf <NAME>. For example, use the
command snmp-server vrf mgmt to enable SNMP on the management interface. Use the command
snmp-server vrf default to enable SNMP on the default VRF. Use the command snmp-server vrf
<USERDEFINED_VRF_NAME> to enable SNMP on the user created VRF.

2. Set the system contact, location, and description for the switch with the following commands:

n snmp-server system-contact

n snmp-server system-location

n snmp-server system-description

You can also set the system location and system contact values using SNMP.

3.

If required, change the default SNMP port on which the agent listens for requests with the command
snmp-server agent-port.

4. By default, the agent uses the community string public to protect access through SNMPv1/v2c. Set a

new community string with the command snmp-server community.

5. Configure the trap receivers to which the SNMP agent will send trap notifications with the command

snmp-server host.

6. Create an SNMPv3 context and associate it with any available SNMPv3 user to perform context

specific v3 MIB polling using the command snmpv3 user <V3_USERNAME> context <CONTEXT_NAME>.

SNMP | 10

7. CreateanSNMPv3contextandassociateitwithanavailableSNMPv1/v2ccommunitystringto
performcontextspecificv1/v2cMIBpollingusingthecommandsnmpv3 context <CONTEXT_NAME>
|     | vrf <VRF_NAME> | community | <COMMUNITY_NAME>. |     |     |
| --- | -------------- | --------- | ----------------- | --- | --- |
8. ReviewyourSNMPconfigurationsettingswiththefollowingcommands:
|     | show snmp | agent-port |     |     |     |
| --- | --------- | ---------- | --- | --- | --- |
n
|     | show snmp | community |     |     |     |
| --- | --------- | --------- | --- | --- | --- |
n
|     | n show snmp   | system  |     |     |     |
| --- | ------------- | ------- | --- | --- | --- |
|     | n show snmpv3 | context |     |     |     |
|     | n show snmp   | trap    |     |     |     |
|     | n show snmp   | vrf     |     |     |     |
|     | n show snmpv3 | users   |     |     |     |
|     | show tech     | snmp    |     |     |     |
n
Example 1
Thisexamplecreatesthefollowingconfiguration:
EnablesSNMPontheout-of-bandmanagementinterface(VRFmgmt).
n
Setsthecontact,location,anddescriptionfortheswitchto:JaniceM,Building2,LabSwitch.
n
n SetsthecommunitystringtoLab8899X.
| switch(config)# |     | snmp-server | vrf mgmt           |          |           |
| --------------- | --- | ----------- | ------------------ | -------- | --------- |
| switch(config)# |     | snmp-server | system-contact     |          | JaniceM   |
| switch(config)# |     | snmp-server | system-location    |          | Building2 |
| switch(config)# |     | snmp-server | system-description |          | LabSwitch |
| switch(config)# |     | snmp-server | community          | Lab8899X |           |
Example 2
Thisexamplecreatesthefollowingconfiguration:
CreatesanSNMPv3usernamedAdminusingshaauthenticationwiththeplaintextpassword
n
mypasswordandusingdessecuritywiththeplaintextpasswordmyprivpass.
n AssociatestheSNMPv3userAdminwithacontextnamednewContext.
switch(config)# snmpv3 user Admin auth sha auth-pass plaintext mypassword priv des
|     | priv-pass | plaintext | myprivpass |     |     |
| --- | --------- | --------- | ---------- | --- | --- |
switch(config)#
|     |     | snmpv3 | user Admin context |     | newContext |
| --- | --- | ------ | ------------------ | --- | ---------- |
SNMP commands
event-trap-enable
event-trap-enable
no event-trap-enable
Description
EnablesthenotificationofeventstobesentastrapstotheSNMPmanagementstations.Itisenabledby
default.
Thenoformofthiscommanddisablestheeventtraps.
11
AOS-CX10.09SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

Examples
Enablingtheeventtraps:
switch(config)#
event-trap-enable
Disablingtheeventtraps:
| switch(config)# |     | no event-trap-enable |     |     |
| --------------- | --- | -------------------- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| lldp trap        | enable |     |     |     |
| ---------------- | ------ | --- | --- | --- |
| lldp trap enable |        |     |     |     |
| no lldp trap     | enable |     |     |     |
Description
EnablessendingSNMPtrapsforLLDPrelatedeventsfromaparticularinterface.LLDPtrapgenerationis
enabledbydefaultonalltheinterfacesandhastobedisabledforinterfacesonwhichtrapsarenotrequired
tobegenerated.
ThenoformofthiscommanddisablestheLLDPtrapgeneration.
LLDPtrapgenerationisdisabledbydefaultatthegloballevelandmustbeenabledbeforeanyLLDPtrapsare
sent.
Examples
EnablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | lldp trap | enable |     |
| --------------- | --- | --------- | ------ | --- |
EnablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     | lldp | trap enable |     |
| ------------------ | --- | ---- | ----------- | --- |
SNMP|12

DisablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | no lldp trap | enable |     |     |
| --------------- | --- | ------------ | ------ | --- | --- |
DisablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     | no lldp | trap | enable |     |
| ------------------ | --- | ------- | ---- | ------ | --- |
DisplayingLLDPglobalconfiguration:
switch#
|             | show | lldp configuration |     |     |     |
| ----------- | ---- | ------------------ | --- | --- | --- |
| LLDP Global |      | Configuration      |     |     |     |
=========================
| LLDP Enabled  |         |                | : No |     |     |
| ------------- | ------- | -------------- | ---- | --- | --- |
| LLDP Transmit |         | Interval       | : 30 |     |     |
| LLDP Hold     | Time    | Multiplier     | : 4  |     |     |
| LLDP Transmit |         | Delay Interval | : 2  |     |     |
| LLDP Reinit   |         | Timer Interval | : 2  |     |     |
| LLDP Trap     | Enabled |                | : No |     |     |
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
| 1/1/6 |     | Yes |     | Yes | Yes |
...........
...........
| mgmt |     | Yes |     | Yes | Yes |
| ---- | --- | --- | --- | --- | --- |
DisplayingLLDPConfigurationfortheinterface:
| switch#     | show | lldp configuration |     | 1/1/1 |     |
| ----------- | ---- | ------------------ | --- | ----- | --- |
| LLDP Global |      | Configuration      |     |       |     |
=========================
| LLDP Enabled  |         |                | : Yes |     |     |
| ------------- | ------- | -------------- | ----- | --- | --- |
| LLDP Transmit |         | Interval       | : 30  |     |     |
| LLDP Hold     | Time    | Multiplier     | : 4   |     |     |
| LLDP Transmit |         | Delay Interval | : 2   |     |     |
| LLDP Reinit   |         | Timer Interval | : 2   |     |     |
| LLDP Trap     | Enabled |                | : No  |     |     |
13
AOS-CX10.09SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

| LLDP | Port | Configuration |     |     |     |     |     |
| ---- | ---- | ------------- | --- | --- | --- | --- | --- |
=======================
| PORT |     | TX-ENABLED |     |     | RX-ENABLED |     | INTF-TRAP-ENABLED |
| ---- | --- | ---------- | --- | --- | ---------- | --- | ----------------- |
--------------------------------------------------------------------------
| 1/1/1 |     | Yes |     |     | Yes |     | Yes |
| ----- | --- | --- | --- | --- | --- | --- | --- |
DisplayingLLDPConfigurationforthemanagementinterface:
| switch# | show   | lldp          | configuration |     | mgmt |     |     |
| ------- | ------ | ------------- | ------------- | --- | ---- | --- | --- |
| LLDP    | Global | Configuration |               |     |      |     |     |
=========================
| LLDP | Enabled  |                 |          | :   | Yes |     |     |
| ---- | -------- | --------------- | -------- | --- | --- | --- | --- |
| LLDP | Transmit | Interval        |          | :   | 30  |     |     |
| LLDP | Hold     | Time Multiplier |          | :   | 4   |     |     |
| LLDP | Transmit | Delay           | Interval | :   | 2   |     |     |
| LLDP | Reinit   | Timer           | Interval | :   | 2   |     |     |
| LLDP | Trap     | Enabled         |          | :   | Yes |     |     |
| LLDP | Port     | Configuration   |          |     |     |     |     |
=======================
| PORT |     | TX-ENABLED |     |     | RX-ENABLED |     | INTF-TRAP-ENABLED |
| ---- | --- | ---------- | --- | --- | ---------- | --- | ----------------- |
--------------------------------------------------------------------------
| mgmt |     | Yes |     |     | Yes |     | Yes |
| ---- | --- | --- | --- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms configandconfig-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| mac-notify    |       | traps |                 |     |         |            |     |
| ------------- | ----- | ----- | --------------- | --- | ------- | ---------- | --- |
| mac-notify    | traps | {aged | | learned       | |   | moved   | | removed} |     |
| no mac-notify |       | traps | {aged | learned |     | | moved | | removed} |     |
Description
ConfiguresaLayer2interfacetogenerateSNMPtrapnotificationsforuptofourdifferenttypesofdynamic
MACaddressrelatedeventsonthetrunkoraccessinphysicalorlaginterfaces.
Thenoformofthiscommandremovesthetrapsfromtheinterface.
SNMP|14

Parameter Description
aged NotifieswhenaMACaddressagedoutontheinterface.
learned NotifieswhenaMACaddressislearnedontheinterface.
moved NotifieswhenaMACaddressmovedfromtheinterface.
removed NotifieswhenaMACaddressisremovedfromtheinterface.
MACnotificationtrapadditiontoorremovalfromaninterfacecanbeinanycombination,quantity,ororder.The
additionofexistingconfiguredtrapsorremovalofnon-configuredtrapswillbeacceptedandignored.
Themac-notifyfeaturemustbeenabledgloballyforanyinterfaceconfigurationstogenerateSNMPtraps.
MACnotificationcannotbeconfiguredonaLayer3(routing)interface.ALayer2interfacethatischangedtoa
Layer3interfacethroughtheroutingcommandwilldiscardanyexistingMACnotificationconfigurations.
Usage
ThefollowingarethelimitationforSNMPMACnotifytraps:
n SNMPMACchangenotificationtrapisnotsupportedforVxLAN–Overlayhosts.
MacnotifytrapwillnotgenerateforStaticMACs.
n
vsx-syncisnotsupportedforthisfeature.Hence,youmustenabletheMACnotifytrapsexplicitlyon
n
secondarytoensurethetrapsaregenerated.
MACnotificationtrapeventsarenotgeneratedforthePort-Access-SecurityMACs.
n
Examples
MACnotificationtypesandtheassociatedeventsonlyapplytoLayer2interfaces,henceroutingmightneedtobe
disabledontherelevantinterfaces.
EnablingthetrapsonanL2interface:
| switch(config)#    | interface  | 1/1/1         |         |
| ------------------ | ---------- | ------------- | ------- |
| switch(config-if)# | mac-notify | traps learned |         |
| 1/1/1 is not       | an L2 port |               |         |
| switch(config-if)# | no routing |               |         |
| switch(config-if)# | mac-notify | traps learned | removed |
| switch(config-if)# | mac-notify | traps aged    |         |
| switch(config)#    | interface  | lag101        |         |
| switch(config-if)# | mac-notify | traps removed |         |
Disablingthelearnedandremovedtrapsfromtheinterface1/1/1:
| switch(config)#    | interface     | 1/1/1         |         |
| ------------------ | ------------- | ------------- | ------- |
| switch(config-if)# | no mac-notify | traps learned | removed |
CommandHistory
15
AOS-CX10.09SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

Release

10.08

Modification

Command introduced

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution rights
for this command.
Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.
Auditors or Administrators or local user group members with
execution rights for this command. Auditors can execute this
command from the auditor context (auditor>) only.

rmon alarm
rmon alarm index <INDEX> snmp-oid <SNMP-OID> rising-threshold <RISING-THRESHOLD>

falling-threshold <FALLING-THRESHOLD> [sample-interval <SAMPLE-INTERVAL>] [sample-type

<ABSOLUTE|DELTA>]
no rmon alarm [index <INDEX>]

Description

Stores configuration entries in an alarm table that defines the sample interval, sample-type, and threshold
parameters for an SNMP MIB object. Only the SNMP MIB objects that resolve to an ASN.1 primitive type of
INTEGER (INTEGER, Integer32, Counter32, Counter64, Gauge32, or TimeTicks) will be monitored.

The no form of this command removes all RMON alarms and allows you to specify an index to remove a
particular RMON alarm.

Parameter

index <INDEX>

Description

Specifies the RMON alarm index. Range: 1 to 20.

snmp-oid <SNMP-OID>

Specifies the SNMP MIB object to be monitored by RMON.

rising-threshold <RISING-THRESHOLD>

Specifies the upper threshold value for the RMON alarm.

falling-threshold <FALLING-THRESHOLD>

Specifies the falling threshold value for the RMON alarm. The
falling threshold must be less than the rising threshold.

sample-interval <SAMPLE-INTERVAL>

Sample interval in seconds. Default: 30.

sample-type <ABSOLUTE|DELTA>

Specifies the method of sampling of the SNMP MIB object.
Default: Absolute.

Examples

Configuring RMON for the MIB object ifOutErrors.15 with an index 1, rising threshold of 2147483647 and
falling threshold of -2134 using absolute sampling for a sample interval of 100 seconds:

SNMP | 16

switch(config)# rmon alarm index 1 snmp-oid ifOutErrors.15 rising-threshold
2147483647
|     | falling-threshold |     |     | -2134 | sample-type |     | absolute | sample-interval | 100 |
| --- | ----------------- | --- | --- | ----- | ----------- | --- | -------- | --------------- | --- |
RemovingRMONalarmwiththeindex5:
| switch(config)# |     |     | no rmon | alarm | index | 5   |     |     |     |
| --------------- | --- | --- | ------- | ----- | ----- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     |     |     | --           |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --- | --- | --------- | --- | --- | --- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| rmon    | alarm |         | {enable    | | disable} |        | {index  |        | | all} |     |
| ------- | ----- | ------- | ---------- | ---------- | ------ | ------- | ------ | ------ | --- |
| rmon    | alarm | {enable | | disable} |            | {index | <INDEX> | | all} |        |     |
| no rmon | alarm | [enable | |          | disable]   | [index | <INDEX> | |      | all]   |     |
Description
EnablesanddisablestheRMONalarmanditsindex.RMONalarmisenabledbydefault.
| Parameter |         |     |     |     |     | Description                             |     |     |     |
| --------- | ------- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- |
| enable    |         |     |     |     |     | EnablestheRMONalarmindex                |     |     |     |
| disable   |         |     |     |     |     | DisablestheRMONalarmindex.              |     |     |     |
| index     | <INDEX> |     |     |     |     | SpecifiestheRMONalarmindex.Range:1to20. |     |     |     |
| all       |         |     |     |     |     | SpecifiesalltheRMONalarms.              |     |     |     |
Examples
EnablingordisablingalltheRMONalarm:
| switch(config)# |     |     | rmon | alarm | enable  | all |     |     |     |
| --------------- | --- | --- | ---- | ----- | ------- | --- | --- | --- | --- |
| switch(config)# |     |     | rmon | alarm | disable | all |     |     |     |
EnablingordisablingRMONalarmbyindex:
| switch(config)# |     |     | rmon | alarm | enable  | index | 1   |     |     |
| --------------- | --- | --- | ---- | ----- | ------- | ----- | --- | --- | --- |
| switch(config)# |     |     | rmon | alarm | disable | index | 1   |     |     |
17
| AOS-CX10.09SNMP/MIBGuide| |     |     | (AllAOS-CXSeriesSwitches) |     |     |     |     |     |     |
| ------------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |

CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show mac-notify
show mac-notify
Description
DisplayswhethertheMACnotificationfeatureintheSNMPmoduleisenabledornot.Italsodisplaysthe
trapnotificationtypesconfiguredontheLayer2portsinthesystem.
Examples
ShowingtheMACnotificationconfigurationonallconfiguredportsinthesystem:
| switch#          | show mac-notify |         |           |
| ---------------- | --------------- | ------- | --------- |
| MAC notification | global          | setting | : Enabled |
| Port             | Enabled Traps   |         |           |
---------------------------------------
| 1/1/1  | aged learned | moved |         |
| ------ | ------------ | ----- | ------- |
| 1/1/5  | moved        |       |         |
| lag101 | removed      |       |         |
| lag104 | aged learned | moved | removed |
...
...
CommandHistory
| Release |     |     | Modification      |
| ------- | --- | --- | ----------------- |
| 10.08   |     |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show mac-notify | port |     |     |
| --------------- | ---- | --- | --- |
SNMP|18

| show mac-notify |     | [port <PORTS>] |     |     |
| --------------- | --- | -------------- | --- | --- |
Description
DisplaystheMACnotificationconfigurationonarangeofports.
| Parameter |          |     |     | Description                                |
| --------- | -------- | --- | --- | ------------------------------------------ |
| [port     | <PORTS>] |     |     | Specifiesaport,rangeofports,orlistofports. |
Examples
ShowingtheMACnotificationconfigurationonarangeofports:
switch(config)# show mac-notify port 1/1/1,1/1/3,1/1/5,lag101-lag104
| MAC  | notification | global        | Setting: | Enabled |
| ---- | ------------ | ------------- | -------- | ------- |
| Port |              | Enabled Traps |          |         |
---------------------------------------
| 1/1/1  |     | aged learned | moved |         |
| ------ | --- | ------------ | ----- | ------- |
| 1/1/3  |     | --           |       |         |
| 1/1/5  |     | moved        |       |         |
| lag101 |     | removed      |       |         |
| lag102 |     | --           |       |         |
| lag103 |     | --           |       |         |
| lag104 |     | aged learned | moved | removed |
CommandHistory
| Release |     |     |     | Modification      |
| ------- | --- | --- | --- | ----------------- |
| 10.08   |     |     |     | Commandintroduced |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |
| --------- | --- | -------------- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show      | rmon  | alarm           |     |     |
| --------- | ----- | --------------- | --- | --- |
| show rmon | alarm | [index <INDEX>] |     |     |
Description
DisplaystheRMONalarmconfigurations.
| Parameter |         |     |     | Description                             |
| --------- | ------- | --- | --- | --------------------------------------- |
| index     | <INDEX> |     |     | SpecifiestheRMONalarmindex.Range:1to20. |
Examples
19
| AOS-CX10.09SNMP/MIBGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------- | --- | ------------------------- | --- | --- |

ShowingallRMONalarmconfigurations:
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
switch#
| show              | rmon       | alarm               |
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
SNMP|20

| Falling      | threshold : 10 |     |
| ------------ | -------------- | --- |
| Last sampled | value : 0      |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show snmp            | agent-port |     |
| -------------------- | ---------- | --- |
| show snmp agent-port |            |     |
Description
DisplaysSNMPagentUDPportnumber.
Example
DisplayingSNMPagentUDPportnumber:
| switch#    | show snmp agent-port |     |
| ---------- | -------------------- | --- |
| SNMP agent | port : 161           |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show snmp           | community |     |
| ------------------- | --------- | --- |
| show snmp community |           |     |
Description
DisplaysalistofallconfiguredSNMPv1/v2ccommunities.
21
| AOS-CX10.09SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |
| ------------------------- | ------------------------- | --- |

Usage
WhenausercreatesacustomcommunitybeforeenablinganSNMPagent,AOS-CXautomaticallyremoves
thedefaultpubliccommunityfromthesystem.
Example
DisplayingalistofallconfiguredSNMPv1/v2ccommunities:
| switch#show | snmp community |     |     |     |
| ----------- | -------------- | --- | --- | --- |
SNMP-COMMUNITIES
---------------------------------------------------------------------------
| Community |     | Access-level | ACL Name | ACL Type |
| --------- | --- | ------------ | -------- | -------- |
---------------------------------------------------------------------------
| private        |     | ro                                    | my_acl  | ipv4 |
| -------------- | --- | ------------------------------------- | ------- | ---- |
| private        |     | ro                                    | my_acl  | ipv6 |
| private2       |     | rw                                    | new_Acl | ipv6 |
| private3       |     | rw                                    | none    | none |
| Release        |     | Modification                          |         |      |
| 10.08          |     | AddedACLTypecolumntothecommandoutput. |         |      |
| 10.07orearlier |     | --                                    |         |      |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show snmp        | system |     |     |     |
| ---------------- | ------ | --- | --- | --- |
| show snmp system |        |     |     |     |
Description
DisplaysSNMPdescription,location,andcontactinformation.
Example
DisplayingSNMPdescription,location,andcontactinformation:
| switch#     | show snmp system |     |     |     |
| ----------- | ---------------- | --- | --- | --- |
| SNMP system | information      |     |     |     |
----------------------------
| System description | : Aggregation | router    |     |     |
| ------------------ | ------------- | --------- | --- | --- |
| System location    | : Main lab    |           |     |     |
| System contact     | : John Smith, | Lab Admin |     |     |
CommandHistory
SNMP|22

| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show snmp      | trap |     |     |     |
| -------------- | ---- | --- | --- | --- |
| show snmp trap |      |     |     |     |
Description
DisplaysallconfiguredSNMPtraps/informsreceivers.
Example
DisplayingallconfiguredSNMPtrapandinformsreceivers:
| switch# | show snmp trap |           |                    |          |
| ------- | -------------- | --------- | ------------------ | -------- |
| HOST    |                | PORT TYPE | VER COMMUNITY/USER | NAME VRF |
------------------------------------------------------------------------------------
| 10.10.10.10 |     | 162 trap   | v1 public  | default |
| ----------- | --- | ---------- | ---------- | ------- |
| 10.10.10.10 |     | 162 inform | v2c public | default |
| 10.10.10.10 |     | 162 inform | v3 name    | default |
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show snmp     | vrf |     |     |     |
| ------------- | --- | --- | --- | --- |
| show snmp vrf |     |     |     |     |
Description
DisplaystheVRFonwhichtheSNMPagentserviceisrunning.
Example
DisplayingSNMPservicesenabledonVRF:
23
| AOS-CX10.09SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- |

| switch#show  | snmp vrf |     |     |     |
| ------------ | -------- | --- | --- | --- |
| SNMP enabled | VRF      |     |     |     |
----------------------------
mgmt
default
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show snmpv3 | context |     |     |     |
| ----------- | ------- | --- | --- | --- |
| show snmpv3 | context |     |     |     |
Description
DisplaysallconfiguredSNMPcontexts.
Examples
DisplayingallconfiguredSNMPcontexts:
| switch# | show snmpv3 context |     |     |     |
| ------- | ------------------- | --- | --- | --- |
--------------------------------------------------------------------------
| name |     | vrf |     | community |
| ---- | --- | --- | --- | --------- |
--------------------------------------------------------------------------
| contextA |     | default |     | private |
| -------- | --- | ------- | --- | ------- |
| contextB |     | vrf_A   |     | public  |
switch#
show snmpv3 context
--------------------------------------------------------------------------
| Name | vrf | Community | ype[Instance_id] |     |
| ---- | --- | --------- | ---------------- | --- |
------------------------------------------------------------------
| A   | default | public | vrf |     |
| --- | ------- | ------ | --- | --- |
switch#
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
SNMP|24

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show snmpv3 | engine-id |     |
| ----------- | --------- | --- |
| show snmpv3 | engine-id |     |
Description
DisplaystheconfiguredSNMPv3snmpengine-id.
IftheSNMPv3engine-idisnotconfigured,bydefaultauniqueengine-idiscreatedbytheswitchusinga
combinationoftheenterpriseOIDvalueandtheswitch'smacaddress.
Example
DisplayingtheconfiguredSNMPv3engine-id:
| switch#        | show snmpv3 engine-id           |     |
| -------------- | ------------------------------- | --- |
| SNMP engine-id | : 80:00:B8:5C:08:00:09:1d:de:a5 |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show snmpv3 | security-level |     |
| ----------- | -------------- | --- |
| show snmpv3 | security-level |     |
Description
DisplaystheconfiguredSNMPv3securitylevel.
Examples
DisplayingtheconfiguredSNMPv3securitylevel:
| switch#               | show snmpv3 security-level |     |
| --------------------- | -------------------------- | --- |
| SNMPv3 security-level | : auth                     |     |
25
| AOS-CX10.09SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |
| ------------------------- | ------------------------- | --- |

CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show snmpv3 | users |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
| show snmpv3 | users |     |     |     |     |
Description
DisplaysallconfiguredSNMPv3users.
| Formoredetailsontheuserenabledstatus,seesnmpv3 |     |     |     | security-level. |     |
| ---------------------------------------------- | --- | --- | --- | --------------- | --- |
Example
DisplayingallconfiguredSNMPv3users:
| switch# | show snmpv3 | users |     |     |     |
| ------- | ----------- | ----- | --- | --- | --- |
---------------------------------------------------------------------
| User |     |     | AuthMode | PrivMode | Context Enabled |
| ---- | --- | --- | -------- | -------- | --------------- |
---------------------------------------------------------------------
| name  |     |     | md5 | none | none False |
| ----- | --- | --- | --- | ---- | ---------- |
| name2 |     |     | sha | aes  | none True  |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| snmp-server    | agent-port |          |     |     |     |
| -------------- | ---------- | -------- | --- | --- | --- |
| snmp-server    | agent-port | <PORT>   |     |     |     |
| no snmp-server | agent-port | [<PORT>] |     |     |     |
Description
SNMP|26

SetstheUDPportnumberthattheSNMPmasteragentusestocommunicate.UDPport161isthedefault
port.
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
| switch(config-schedule)# |     |     |     | no snmp-server |     | agent-port | 2000 |
| ------------------------ | --- | --- | --- | -------------- | --- | ---------- | ---- |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    |           | community |          |     |     |     |     |
| -------------- | --------- | --------- | -------- | --- | --- | --- | --- |
| snmp-server    | community |           | <STRING> |     |     |     |     |
| no snmp-server | community |           | <STRING> |     |     |     |     |
Description
AddsanSNMPv1/SNMPv2ccommunitystring.Acommunitystringislikeapasswordthatcontrols
read/writeaccesstotheSNMPagent.Anetworkmanagementprogrammustsupplythisnamewhen
attemptingtogetSNMPinformationfromtheswitch.Amaximumof10communitystringsaresupported.
Onceyoucreateyourowncommunitystring,thedefaultcommunitystring(public)isdeleted.
ThenoformofthiscommandremovesthespecifiedSNMPv1/SNMPv2ccommunitystring.Whenno
communitystringexists,adefaultcommunitystringwiththevaluepublicisautomaticallydefined.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<STRING> SpecifiestheSNMPv1/SNMPv2ccommunitystring.Range:1to32
printableASCIIcharacters,excludingspaceandquestionmark.
27
| AOS-CX10.09SNMP/MIBGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |     |     |     |
| ------------------------- | --- | ------------------------- | --- | --- | --- | --- | --- |

Subcommands
| access-level    | {ro | | rw}     |     |     |     |
| --------------- | --- | --------- | --- | --- | --- |
| no access-level |     | {ro | rw} |     |     |     |
ThissubcommandchangestheaccessleveloftheSNMPcommunity.Thedefaultaccesslevelisread-only
(ro).
Thenoformofthissubcommandchangestheaccesslevelofthecommunitytodefault.
| Parameter      |       |         |            |            | Description                                    |
| -------------- | ----- | ------- | ---------- | ---------- | ---------------------------------------------- |
| ro             |       |         |            |            | SpecifiesRead-OnlyaccesswiththeSNMPcommunity.  |
| rw             |       |         |            |            | SpecifiesRead-WriteaccesswiththeSNMPcommunity. |
| access-list    | {ipv4 | | ipv6} | <ACL-NAME> |            |                                                |
| no access-list | {ipv4 | |       | ipv6}      | <ACL-NAME> |                                                |
ThissubcommandassociatesanACLwiththeSNMPcommunity.IfanACLisnotassociatedwiththeSNMP
community,thedefaultaccessisallowedforallthehosts.
ThenoformofthissubcommandremovesassociationoftheACLwiththeSNMPcommunity.
| Parameter |     |     |     |     | Description              |
| --------- | --- | --- | --- | --- | ------------------------ |
| ipv4      |     |     |     |     | SpecifiestheIPv4ACLtype. |
| ipv6      |     |     |     |     | SpecifiestheIPv6ACLtype. |
<ACL-NAME> SpecifiestheACLname.Itsupportsamaximumof64characters.
Examples
SettingtheSNMPv1/SNMPv2ccommunitystringtoprivate:
| switch(config)# |     | snmp-server |     | community | private |
| --------------- | --- | ----------- | --- | --------- | ------- |
RemovingSNMPv1/SNMPv2ccommunitystringprivate:
| switch(config)# |     | no  | snmp-server | community | private |
| --------------- | --- | --- | ----------- | --------- | ------- |
ConfiguringtheaccesslevelfortheSMNPcommunitytoread-only:
| switch(config-community)# |     |     |     | access-level | ro  |
| ------------------------- | --- | --- | --- | ------------ | --- |
ChangingtheaccessleveloftheSNMP communitytodefault:
| switch(config-community)# |     |     |     | no access-level | rw  |
| ------------------------- | --- | --- | --- | --------------- | --- |
AssociatinganIPv4ACLnamedmy_aclwiththeSMNPcommunity:
| switch(config-community)# |     |     |     | access-list | ipv4 my_acl |
| ------------------------- | --- | --- | --- | ----------- | ----------- |
SNMP|28

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
Example:show access-list hitcounts ip allwillnotshowthehitcountofSNMPACL.
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|                | config-community            |     | forthiscommand. |
| -------------- | --------------------------- | --- | --------------- |
| snmp-server    | historical-counters-monitor |     |                 |
| snmp-server    | historical-counters-monitor |     |                 |
| no snmp-server | historical-counters-monitor |     |                 |
Description
29
| AOS-CX10.09SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------- | ------------------------- | --- | --- |

EnablestheRemoteNetworkMonitoringagent(rmond)tostartcollectinghistoricalinterfacestatistics.The
noformofthiscommandstopsthehistoricalinterfacestatisticscollection.
Example
Enablingthermondagenttostarthistoricalinterfacestatisticscollection:
| switch(config)# | snmp-server | historical-counters-monitor |
| --------------- | ----------- | --------------------------- |
Disablingthermondagenttostophistoricalinterfacestatisticscollection:
| switch(config)# | no snmp-server | historical-counters-monitor |
| --------------- | -------------- | --------------------------- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| snmp-server | host |     |
| ----------- | ---- | --- |
snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
| [port <UDP-PORT>] | [<VRF-NAME>] |     |
| ----------------- | ------------ | --- |
no snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
| [port <UDP-PORT>] | [<VRF-NAME>] |     |
| ----------------- | ------------ | --- |
snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
| [port <UDP-PORT>] | [<VRF-NAME>] |     |
| ----------------- | ------------ | --- |
no snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
| [port <UDP-PORT>] | [<VRF-NAME>] |     |
| ----------------- | ------------ | --- |
snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user <NAME>
| [port <UDP-PORT>] | [<VRF-NAME>] |     |
| ----------------- | ------------ | --- |
no snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user
<NAME>
| [port <UDP-PORT>] | [<VRF-NAME>] |     |
| ----------------- | ------------ | --- |
Description
Configuresatrap/informsreceivertowhichtheSNMPagentcansendSNMPv1/v2c/v3trapsorv2c
informs.Amaximumof30SNMPtraps/informsreceiverscanbeconfigured.
Thenoformofthiscommandremovesthespecifiedtrap/informreceiver.
| Parameter |     | Description |
| --------- | --- | ----------- |
<IPv4-ADDR>
SpecifiestheIPaddressofatrapreceiverinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.Youcan
SNMP|30

| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
removeleadingzeros.Forexample,theaddress
192.169.005.100becomes192.168.5.100.
| <IPv6-ADDR> |     | SpecifiestheIPaddressofatrapreceiverinIPv6format |     |     |
| ----------- | --- | ------------------------------------------------ | --- | --- |
(x:x::x:x).
trap version <VERSION> SpecifiesthetrapnotificationtypeforSNMPv1,v2corv3.
Availableoptionsare:v1,v2corv3.
inform version v2c SpecifiestheinformnotificationtypeforSNMPv2c.
| trap version v3 |     |     |     |     |
| --------------- | --- | --- | --- | --- |
SpecifiesthetrapnotificationtypeforSNMPv3.
| user <NAME> |     | SpecifiestheSNMPv3usernametobeusedintheSNMPtrap |     |     |
| ----------- | --- | ----------------------------------------------- | --- | --- |
notifications.
community <STRING> Specifiesthenameofthecommunitystringtousewhensending
trapnotifications.Range:1-32printableASCIIcharacters,
excludingspaceandquestionmark.Default:public.
<UDP-PORT> SpecifiestheUDPportonwhichnotificationsaresent.Range:1-
65535.Default:162.
<VRF-NAME> SpecifiestheVRFonwhichtheSNMPagentlistensforincoming
requests.
Examples
| switch(config)# | snmp-server    | host 10.10.10.10 | trap version | v1         |
| --------------- | -------------- | ---------------- | ------------ | ---------- |
| switch(config)# | no snmp-server | host 10.10.10.10 | trap         | version v1 |
| switch(config)# | snmp-server    | host a:b::c:d    | trap version | v1         |
| switch(config)# | no snmp-server | host a:b::c:d    | trap version | v1         |
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
switch(config)# snmp-server host a:b::c:d trap version v2c community public
switch(config)# no snmp-server host a:b::c:d trap version v2c community public
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public port
5000
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
port 5000
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public port
| 5000 vrf default |     |     |     |     |
| ---------------- | --- | --- | --- | --- |
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
| port 5000 vrf | default |     |     |     |
| ------------- | ------- | --- | --- | --- |
switch(config)# snmp-server host a:b::c:d trap version v2c community public port
5000
switch(config)# no snmp-server host a:b::c:d trap version v2c community public port
5000
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public
switch(config)# snmp-server host a:b::c:d inform version v2c community public
switch(config)# no snmp-server host a:b::c:d inform version v2c community public
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
port 5000
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public
port 5000
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
| port 5000 vrf | default |     |     |     |
| ------------- | ------- | --- | --- | --- |
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public
31
AOS-CX10.09SNMP/MIBGuide| (AllAOS-CXSeriesSwitches)

| port | 5000 vrf | default |     |     |     |     |     |
| ---- | -------- | ------- | --- | --- | --- | --- | --- |
switch(config)#
snmp-server host a:b::c:d inform version v2c community public port
5000
switch(config)# no snmp-server host a:b::c:d inform version v2c community public
| port | 5000 |     |     |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- |
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# snmp-server host a:b::c:d trap version v3 user Admin
switch(config)# no snmp-server host a:b::c:d trap version v3 user Admin
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin port 2000
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin port 2000
switch(config)#
|     |     | snmp-server | host | a:b::c:d | trap version | v3 user Admin | port 2000 |
| --- | --- | ----------- | ---- | -------- | ------------ | ------------- | --------- |
switch(config)# no snmp-server host a:b::c:d trap version v3 user Admin port 2000
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    |                | system-contact |          |     |     |     |     |
| -------------- | -------------- | -------------- | -------- | --- | --- | --- | --- |
| snmp-server    | system-contact |                | <INFO>   |     |     |     |     |
| no snmp-server | system-contact |                | [<INFO>] |     |     |     |     |
Description
SetsSNMPcontactinformation.
ThenoformofthiscommandremovestheSNMPcontactinformation.
| Parameter |     |     |     | Description                                           |     |     |     |
| --------- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
| <INFO>    |     |     |     | SpecifiesSNMPcontactinformation.Range:1to128printable |     |     |     |
ASCIIcharacters,exceptforquestionmark(?).
Examples
| DefinesSNMPcontactinformationtobeJohn |     |             |                | Smith, | LabAdmin:   |           |     |
| ------------------------------------- | --- | ----------- | -------------- | ------ | ----------- | --------- | --- |
| switch(config)#                       |     | snmp-server | system-contact |        | John Smith, | Lab Admin |     |
RemovesSNMPcontactinformation:
| switch(config)# |     | no snmp-server |     | system-contact |     |     |     |
| --------------- | --- | -------------- | --- | -------------- | --- | --- | --- |
CommandHistory
SNMP|32

| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    | system-description |               |     |
| -------------- | ------------------ | ------------- | --- |
| snmp-server    | system-description | <DESCRIPTION> |     |
| no snmp-server | system-description |               |     |
Description
SetstheSNMPsystemdescription.
ThenoformofthiscommandremovestheSNMPsystemdescription.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<DESCRIPTION> SpecifiestheSNMPsystemdescription.Typicalcontenttoinclude
wouldbethefullnameandversionofthefollowing:
n Hardwaretypeofthesystem
n Softwareoperatingsystem
n Networkingsoftware
Range:1to64printableASCIIcharacters,exceptforthequestion
mark(?).
Examples
DefinestheSNMPsystemdescriptiontobemainSwitch:
| switch(config)# | snmp-server | system-description | mainSwitch |
| --------------- | ----------- | ------------------ | ---------- |
RemovestheSNMPsystemdescription:
| switch(config)# | no snmp-server | system-description | mainSwitch |
| --------------- | -------------- | ------------------ | ---------- |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
33
| AOS-CX10.09SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------- | ------------------------- | --- | --- |

| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    | system-location |        |     |     |
| -------------- | --------------- | ------ | --- | --- |
| snmp-server    | system-location | <INFO> |     |     |
| no snmp-server | system-location |        |     |     |
Description
SetstheSNMPlocationinformation.
ThenoformofthiscommandremovestheSNMPlocationinformation.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INFO>
SpecifiestheSNMPlocationinformation.Range:1to128printable
ASCIIcharacters,exceptforthequestionmark(?).
Examples
| DefinestheSNMPlocationinformationtobeMain |     |     |     | Lab: |
| ----------------------------------------- | --- | --- | --- | ---- |
switch(config)#
|     | snmp-server | system-location |     | Main Lab |
| --- | ----------- | --------------- | --- | -------- |
RemovestheSNMPlocationinformation:
| switch(config)# | no snmp-server |     | system-location |     |
| --------------- | -------------- | --- | --------------- | --- |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    | vrf            |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| snmp-server    | vrf <VRF-NAME> |     |     |     |
| no snmp-server | vrf <VRF-NAME> |     |     |     |
Description
ConfiguresaVRFonwhichtheSNMPagentlistensforincomingrequests.Bydefault,theSNMPagentdoes
notlistenonanyVRF.4100i,6000,and6100onlysupportdefaultVRF.TheSNMPagentcanlistenon
multipleVRFs.
SNMP|34

ThenoformofthiscommandstopstheSNMPagentfromlisteningforincomingrequestsonthespecified
VRF.
| Parameter  |     | Description             |
| ---------- | --- | ----------------------- |
| <VRF-NAME> |     | SpecifiesthenameofaVRF. |
Examples
ConfiguringtheSNMPagenttolistenonVRFdefault.
| switch(config)# | snmp-server | vrf default |
| --------------- | ----------- | ----------- |
ConfiguringtheSNMPagenttolistenonVRFmgmt.
| switch(config)# | snmp-server | vrf mgmt |
| --------------- | ----------- | -------- |
ConfiguringtheSNMPagenttolistenonused-definedVRFmyvrf.
| switch(config)# | snmp-server | vrf myvrf |
| --------------- | ----------- | --------- |
StoppingtheSNMPagentfromlisteningonVRFdefault.
| switch(config)# | no snmp-server | vrf default |
| --------------- | -------------- | ----------- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    | trap aaa-server-reachability-status |     |
| -------------- | ----------------------------------- | --- |
| snmp-server    | trap aaa-server-reachability-status |     |
| no snmp-server | trap aaa-server-reachability-status |     |
Description
EnablestheSNMPtrapforAAAserverstatus.Whenenabled,trapsaresentwheneverAAAserver(RADIUS,
TACACS)statuschangesfromreachabletounreachableandviceversa.
ThenoformofthiscommanddisablessendingSNMPtrapforAAAserverstatus.
Examples
35
| AOS-CX10.09SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |
| ------------------------- | ------------------------- | --- |

EnablingtheSNMPtrapforAAAserverstatus:
| switch(config)# | snmp-server | trap aaa-server-reachability-status |
| --------------- | ----------- | ----------------------------------- |
DisablingtheSNMPtrapforAAAserverstatus:
switch(config)# no snmp-server trap aaa-server-reachability-status
CommandHistory
| Release |     | Modification      |
| ------- | --- | ----------------- |
| 10.09   |     | Commandintroduced |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     | forthiscommand. |
| ---- | --- | --------------- |
6400
| snmp-server    | trap mac-notify |     |
| -------------- | --------------- | --- |
| snmp-server    | trap mac-notify |     |
| no snmp-server | trap mac-notify |     |
Description
EnablestheMACnotificationtrapswithintheSNMPmoduleatagloballevel.Whenenabled,trapsaresent
forinterfacesthatareconfiguredforMACnotificationevents.
ThenoformofthiscommanddisablessendingMACnotificationtrapsatagloballevel.Whendisabled,
existingmac-notifyinterfaceconfigurationispreservedbutMACnotificationeventsonconfigured
interfaceswillnotcauseSNMPtrapstobetransmitted.
Examples
EnablingtheSNMPMACnotificationfeatureinthesystemglobally:
| switch(config)# | snmp-server | trap mac-notify |
| --------------- | ----------- | --------------- |
DisablingtheSNMPMACnotificationfeatureinthesystemglobally:
| switch(config)# | no snmp-server | trap mac-notify |
| --------------- | -------------- | --------------- |
CommandHistory
| Release |     | Modification      |
| ------- | --- | ----------------- |
| 10.08   |     | Commandintroduced |
SNMP|36

CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server | trap-source | interface |     | vrf |     |
| ----------- | ----------- | --------- | --- | --- | --- |
snmp-server trap-source {interface <IF-NAME> | <IPv4-Address> | <IPv6-Address>} [vrf <VRF-
NAME>]
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
| switch(config)# | snmp-server | trap-source |     | 10.0.0.1    | vrf red |
| --------------- | ----------- | ----------- | --- | ----------- | ------- |
| switch(config)# | snmp-server | trap-source |     | 1001::1 vrf | red     |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
37
| AOS-CX10.09SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- | --- |

| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server | trap |     |     |
| ----------- | ---- | --- | --- |
snmp-server trap {cpu-utilization | memory-utilization | rmon-events}
no snmp-server trap {cpu-utilization | memory-utilization | rmon-events}
Description
EnablestheSNMPtraps.TheSNMPtrapsareenabledbydefault.
ThenoformofthiscommanddisablestheSNMPtraps.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
cpu-utilization
EnablestheCPUutilizationtraps.
| memory-utilization |     | Enablesthememoryutilizationtraps. |     |
| ------------------ | --- | --------------------------------- | --- |
rmon-events
EnablestheRMONeventtraps.
Examples
EnablingtheSNMPtraps:
| switch(config)# | snmp-server | trap cpu-utilization |     |
| --------------- | ----------- | -------------------- | --- |
switch(config)#
|                 | snmp-server | trap memory-utilization |     |
| --------------- | ----------- | ----------------------- | --- |
| switch(config)# | snmp-server | trap rmon-events        |     |
DisablingtheSNMPtraps:
| switch(config)# | no snmp-server | trap cpu-utilization    |     |
| --------------- | -------------- | ----------------------- | --- |
| switch(config)# | no snmp-server | trap memory-utilization |     |
| switch(config)# | no snmp-server | trap rmon-events        |     |
DisplayingtheSNMPtrapconfiguration:
| switch(config)# | show running-config     | all | inc | snmp |
| --------------- | ----------------------- | --------- | ---- |
| snmp-server     | trap rmon-events        |           |      |
| snmp-server     | trap cpu-utilization    |           |      |
| snmp-server     | trap memory-utilization |           |      |
DisplayingCPUandMemoryusage:
| switch(config)#    | show system       |     |     |
| ------------------ | ----------------- | --- | --- |
| Hostname           | : XXXX            |     |     |
| System Description | : XX.10.07.0001CI |     |     |
| System Contact     | :                 |     |     |
| System Location    | :                 |     |     |
| Vendor             | : Aruba           |     |     |
Product Name : JLXXXX XXXX Base Chassis/3xFT/18xFans/Cbl Mgr/X462 Bundle
SNMP|38

| Chassis        | Serial Nbr : SG6ZOO9068 |     |     |
| -------------- | ----------------------- | --- | --- |
| Base MAC       | Address : f40343-806400 |     |     |
| AOS-CX Version | : XX.10.07.0001CI       |     |     |
| Time Zone      | : UTC                   |     |     |
| Up Time        | : 8 minutes             |     |     |
| CPU Util       | (%) : 1                 |     |     |
| Memory Usage   | (%) : 10                |     |     |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmp-server    | trap vsx |     |     |
| -------------- | -------- | --- | --- |
| snmp-server    | trap vsx |     |     |
| no snmp-server | trap vsx |     |     |
Description
EnablessendingtheSNMPtrapsforVSXrelatedevents.VSXtrapgenerationisdisabledbydefault.
ThenoformofthiscommanddisablessendingtheSNMPtrapsforVSXrelatedevents.
ThetrapsupportisavailableforthefollowingVSXevents:
n ISLupanddown
KAupanddown
n
MCLAGupanddown
n
| Parameter |     | Description                     |     |
| --------- | --- | ------------------------------- | --- |
| vsx       |     | SpecifiesSNMPtrapsforVSXevents. |     |
Examples
EnablingtheVSXtraps:
| switch(config)# | snmp-server | trap vsx      |      |
| --------------- | ----------- | ------------- | ---- |
| switch(config)# | show vsx    | configuration | trap |
| SNMP traps      | : Enabled   |               |      |
DisablingtheVSXtraps:
39
| AOS-CX10.09SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------- | ------------------------- | --- | --- |

| switch(config)# |         | no       | snmp-server       | trap | vsx  |     |
| --------------- | ------- | -------- | ----------------- | ---- | ---- | --- |
| switch(config)# |         | show     | vsx configuration |      | trap |     |
| SNMP            | traps : | Disabled |                   |      |      |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| snmpv3    | context        |        |                  |            |            |           |
| --------- | -------------- | ------ | ---------------- | ---------- | ---------- | --------- |
| snmpv3    | context <NAME> | vrf    | <VRF-NAME>       | [community |            | <STRING>] |
| no snmpv3 | context        | <NAME> | [vrf <VRF-NAME>] |            | [community | <STRING>] |
Description
CreatesanSNMPv3contextonthespecifiedVRF.
ThenoformofthiscommandremovesthespecifiedSNMPcontext.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<NAME> Specifiesthenameofthecontext.Range:1to32printableASCII
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
SNMP|40

Removing the SNMPv3 context named newContext on VRF myVrf:

switch(config)# no snmpv3 context newContext vrf myVrf

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

config

Administrators or local user group members with execution rights
for this command.

snmpv3 engine-id

Syntax

snmpv3 engine-id <ENGINE-ID>

no snmpv3 engine-id <ENGINE-ID>

Description

Configures the SNMPv3 SNMP engine-id allowing an administrator to configure a unique SNMP engine-id
for the switch. This engine-id is used by the NMS management tool to identify and distinguish multiple
switches on the same network.

The no form of this command restores the default engine-id, created by the switch using a combination of
the enterprise OID value and the switch's mac address.

Command context

config

Parameters

<ENGINE-ID>

SNMPv3 SNMP engine-id in colon separated hexadecimal notation.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the SNMPv3 engine-id:

switch(config)#
switch(config)# snmpv3 engine-id

WORD SNMPv3 snmp engine-id in colon seperated hexadecimal notation

switch(config)# snmpv3 engine-id 01:23:45:67:89:ab:cd:ef:01:23:45:67

Restoring the default SNMPv3 engine-id:

AOS-CX 10.09 SNMP/MIB Guide | (All AOS-CX Series Switches)

41

| switch(config)# |                | no snmpv3 | engine-id       |     |
| --------------- | -------------- | --------- | --------------- | --- |
| snmpv3          | security-level |           |                 |     |
| snmpv3          | security-level | {auth     | | auth-privacy} |     |
| no snmpv3       | security-level | {auth     | | auth-privacy} |     |
Description
ConfigurestheSNMPv3securitylevel.ThesecurityleveldetermineswhichSMNPv3usersdefinedbythe
| commandsnmpv3 |     | userareabletoconnect. |     |     |
| ------------- | --- | --------------------- | --- | --- |
Thenoformofthiscommandchangesthesecuritylevelasfollows:
auth:Setsthesecurityleveltoauth-privacy.
| n no snmpv3 | security-level |     |     |     |
| ----------- | -------------- | --- | --- | --- |
n no snmpv3 security-level auth-privacy:Setsthesecurityleveltonoauthenticationorprivacy,
allowinganySNMPusertoconnect.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
auth SNMPv3usersthatsupportauthentication,orauthenticationand
privacyareallowed.
auth-privacy OnlySNMPv3userswithbothauthenticationandprivacyare
allowed.ThisisthehighestlevelofSNMPv3security.Default.
Examples
SettingtheSNMPv3securityleveltoauthenticationandprivacy:
| switch(config)# |     | snmpv3 | security-level | auth-privacy |
| --------------- | --- | ------ | -------------- | ------------ |
SettingtheSNMPv3securityleveltoauthenticationonly:
| switch(config)# |     | snmpv3 | security-level | auth |
| --------------- | --- | ------ | -------------- | ---- |
SettingtheSNMPv3securityleveltonoauthenticationandnoprivacy:
| switch(config)# |     | no snmpv3 | security-level | auth-privacy |
| --------------- | --- | --------- | -------------- | ------------ |
RestoringthedefaultSNMPv3securityleveltoauthenticationandprivacy:
| switch(config)# |     | no snmpv3 | security-level | auth |
| --------------- | --- | --------- | -------------- | ---- |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
SNMP|42

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution rights
for this command.

snmpv3 user
snmpv3 user <NAME>

[auth <AUTH-PROTO> auth-pass [{plaintext | ciphertext} <AUTH-PASS>]]
[priv <PRIV-PROTO> priv-pass [{plaintext | ciphertext} <PRIV-PASS>]]

no snmpv3 user <NAME>

[auth <AUTH-PROTO> auth-pass [{plaintext | ciphertext} <AUTH-PASS>]]
[priv <PRIV-PROTO> priv-pass [{plaintext | ciphertext} <PRIV-PASS>]]

Description

Creates an SNMPv3 user and adds it to an SNMPv3 context. The SNMPv3 security level (set with command
snmpv3 security-level) determines which users are allowed to authenticate.

The no form of this command removes the specified SNMPv3 user.

Parameter

<NAME>

auth <AUTH-PROTO>

auth-pass [{plaintext |
ciphertext} <AUTH-PASS>]

priv <PRIV-PROTO>

priv-pass [{plaintext |
ciphertext} <PRIV-PASS>]

Description

Specifies the SNMPv3 username. Range 1 to 32 printable ASCII
characters, excluding space and question mark (?).

Selects the authentication protocol used to validate user logins:
md5 or sha1.

Specifies the SNMPv3 user authentication password. Range for
plaintext is 8 to 32 printable ASCII characters, excluding space
and question mark (?). Range for ciphertext is 1 to 256 printable
ASCII characters. Ciphertext is used when copying user
configuration settings between switches.

Selects the SNMPv3 privacy protocol (encryption method): aes or
des.

Specifies the SNMPv3 user privacy encryption password. Range
for plaintext is 8 to 32 printable ASCII characters, excluding
space and question mark (?). Range for ciphertext is 1 to 256
printable ASCII characters. Ciphertext is used when copying user
configuration settings between switches.

When the authentication password is not provided on the command line, plaintext authentication password

prompting occurs upon pressing Enter, followed by privacy encryption protocol prompting, and finally plaintext

encryption password prompting. The entered password characters are masked with asterisks.

When the authentication type and password plus the privacy protocol (encryption method) are provided on the

command line but the encryption password is not provided, plaintext encryption password prompting occurs upon

pressing Enter. The entered password characters are masked with asterisks.

Examples

AOS-CX 10.09 SNMP/MIB Guide | (All AOS-CX Series Switches)

43

Defining SNMPv3 user Admin1 using sha authentication and des privacy encryption with provided
plaintext passwords:

switch(config)# snmpv3 user Admin1 auth sha auth-pass plaintext F82#450h

priv des priv-pass plaintext F82#4eva

Defining SNMPv3 user Admin2 using MD5 authentication and AES privacy encryption with provided
authentication password and privacy encryption type but prompted encryption password:

switch(config)# snmpv3 user Admin2 auth md5 auth-pass plaintext F82#450h

priv aes priv-pass

Enter the privacy encryption key: ********
Re-Enter the privacy encryption key: ********

Defining SNMPv3 user Admin2 using MD5 authentication and AES privacy encryption with plaintext
password prompting and privacy encryption selection:

switch(config)# snmpv3 user Admin2 auth md5 auth-pass
Enter the authentication password: ********
Re-Enter the authentication password: ********

Configure the privacy protocol (y/n)? y
Enter the privacy protocol (aes/des)? aes

Enter the privacy encryption key: ********
Re-Enter the privacy encryption key: ********

Removing SNMPv3 user Admin1:

switch(config)# no snmpv3 user Admin1

Creating an SNMP user on switch 1 and then creating the same user on switch 2 by copying from the switch
1 configuration:

On switch 1, configure a user named Admin3, and then use the show running-config command to display
switch configuration. Save a copy of the full snmpv3 user command (shown by show running-config). This
saved command is used on switch 2.

switch1(config)# snmpv3 user Admin3 auth sha auth-pass plaintext F82#450h

priv des priv-pass plaintext F82#4eva

switch1(config)# exit
switch1# show running-config
Current configuration:
!
!Version AOS-CX xx.xx.xx.xxxxxx
!
snmpv3 user Admin3 auth sha auth-pass ciphertext AQBaf2d...FJVcZ3o=
priv des priv-pass ciphertext AQBaH2p...2jfTFwQ=
ssh server vrf mgmt
!
interface mgmt

no shutdown
ip dhcp

SNMP | 44

| vlan 1 |     |     |     |     |
| ------ | --- | --- | --- | --- |
Onswitch2,executethesnmpv3 usercommandthatyousavedfromswitch1(asshownbyshow running-
config).Thiscreatestheuseronswitch2withthesameconfiguration.
switch2(config)# snmpv3 user Admin3 auth sha auth-pass ciphertext AQBaf2d...FJVcZ3o=
|     |     | priv des priv-pass | ciphertext | AQBaH2p...2jfTFwQ= |
| --- | --- | ------------------ | ---------- | ------------------ |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| Entity MIB | support |     |     |     |
| ---------- | ------- | --- | --- | --- |
TheEntityMIB,rfc6933,allowsnetworkmanagerstoretrievephysicalcontainmentandlogicalrelationships
fordevicesinthenetwork.TheentconfigChangetrapissenttoconfiguredSNMP-serverhostswhena
changeoccurs.Thetrapisconfiguredtosendnotificationsnomorethanonceevery5seconds.Wewillbe
supportingtheEntityMIBforread-only.
Physicalcomponentsthataresupportedinclude:
Stack
n
Chassis
n
Fabriccards
n
n Fantrays
n Fans
n Linecardsandtheirinterfaces
n Managementmodulesandtheintaketemperaturesensor
Powersupplies
n
Theslotsforanyremovablecomponentarealsorepresented.
ThelogicaltableoftheEntityMIBrepresentsconfiguredVLANsandtheassociatedports.
entConfigChangetrap/notificationissenttoconfiguredsnmp-serverhosts.
| Location | of the | MIB files | on the | web |
| -------- | ------ | --------- | ------ | --- |
TheMIBfilesforArubaswitchescanbefoundontheArubaServicePortal.Youcanapplythevariousfilters
tofilterbyproductseries,softwareversions,andsoftwarereleasetypes.
45
| AOS-CX10.09SNMP/MIBGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------- | ------------------------- | --- | --- | --- |

Newly introduced MIBs and Traps for 10.09
The following list contains the newly introduced MIBs and Traps for each software feature. Software is
provided along with the MIB and Traps supported name.

AAA

MIB file

ARUBAWIRED-AAA-MIB

Implemented MIB objects:

n arubaWiredRadiusServerTable

o arubaWiredRadiusServerVrfName

o arubaWiredRadiusServerAddress

o arubaWiredRadiusServerPort

o arubaWiredRadiusServerPortType

o arubaWiredRadiusServerReachabilityStatus

n arubaWiredTacacsServerTable

o arubaWiredTacacsServerVrfName

o arubaWiredTacacsServerAddress

o arubaWiredTacacsServerPort

o arubaWiredTacacsServerReachabilityStatus

Traps supported

n arubaWiredRadiusServerStatusChange

n arubaWiredTacacsServerStatusChange

MODULE

MIB file

ARUBAWIRED-MODULE-MIB

Implemented MIB objects

n arubaWiredModuleTable

o arubaWiredModuleGroupIndex

o arubaWiredModuleTypeIndex

o arubaWiredModuleSlotIndex

o arubaWiredModuleName

o arubaWiredModuleType

o arubaWiredModuleProductDescription

o arubaWiredModuleSerialNumber

o arubaWiredModuleProductNumber

o arubaWiredModuleAdminState

o arubaWiredModulePowerPriority

SNMP | 46

Traps supported

n arubaWiredModuleStateNotification

NETWORKING

MIB file

ARUBAWIRED-NETWORKING-OID

Implemented MIB objects

n arubaWiredSwitchJL717C

n  arubaWiredSwitchJL718C

n  arubaWiredSwitchJL719C

n  arubaWiredSwitchJL720C

n  arubaWiredSwitchJL721C

n  arubaWiredSwitchJL722C

n  arubaWiredSwitchModuleJL717C

n

n

n

arubaWiredSwitchModuleJL718C

arubaWiredSwitchModuleJL719C

arubaWiredSwitchModuleJL720C

n  arubaWiredSwitchModuleJL721C

n  arubaWiredSwitchModuleJL722C

n  arubaWiredSwitchR8S96A

n  arubaWiredSwitchModuleR8S96A

n  arubaWiredSwitch10000PowerSupplySlot

n  arubaWiredSwitch10000FanTraySlot

n

n

arubaWiredSwitchPowerSupplyUnitR8R51A

arubaWiredSwitchPowerSupplyUnitR8R52A

n  arubaWiredSwitchFanTrayR8R53A

n  arubaWiredSwitchFanTrayR8R54A

OIDs that supports SNMP write
The following table contains the OIDs that supports SNMP write:

Software Feature

MIB File

OID

SNMPv2 System

SNMPv2-MIB.mib

n sysContact
n sysName
n sysLocation

PoE

n ARUBAWIRED-POE.mib
n POWER-ETHERNET-MIB

n arubaWiredPoePethPsePortPoECycle
n pethPsePortAdminEnable

Interface

IF-MIB

n ifAdminStatus
n ifAlias

AOS-CX 10.09 SNMP/MIB Guide | (All AOS-CX Series Switches)

47

Support and Other Resources

Chapter 3

Support and Other Resources

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

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/AOS-CX/help_portal/Content/home.htm

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.htm

Airheads social
forums and
Knowledge
Base

AOS-CX Switch
Software
Documentation
Portal

Aruba
Hardware
Documentation
and
Translations

AOS-CX 10.09 SNMP/MIB Guide | (All AOS-CX Series Switches)

48

Portal

Aruba software

https://asp.arubanetworks.com/downloads

Software
licensing

End-of-Life
information

Aruba
Developer Hub

https://lms.arubanetworks.com/

https://www.arubanetworks.com/support-services/end-of-life/

https://developer.arubanetworks.com/

Accessing Updates
You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

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

Warranty Information
To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Regulatory Information
To view the regulatory information for your product, view the Safety and Compliance Information for Server,
Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

Support and Other Resources | 49

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs, product
recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For more
information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation Feedback
Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

AOS-CX 10.09 SNMP/MIB Guide | (All AOS-CX Series Switches)

50