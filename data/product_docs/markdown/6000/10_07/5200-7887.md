| AOS-CX |     | 10.07 |     | SNMP/MIB |     |     |
| ------ | --- | ----- | --- | -------- | --- | --- |
Guide
| 6100, | 6200, | 6300, | 6400,  | 8320,  | 8325, | 8360, |
| ----- | ----- | ----- | ------ | ------ | ----- | ----- |
|       |       | 8400  | Switch | Series |       |       |
PartNumber:5200-7887
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

| 2

Contents
Contents
| Contents                            |                                        | 3   |
| ----------------------------------- | -------------------------------------- | --- |
| About this                          | Document                               | 5   |
| Applicableproducts                  |                                        | 5   |
| Latestversionavailableonline        |                                        | 5   |
| Commandsyntaxnotationconventions    |                                        | 5   |
| Abouttheexamples                    |                                        | 6   |
| Identifyingswitchportsandinterfaces |                                        | 7   |
| Identifyingmodularswitchcomponents  |                                        | 8   |
| SNMP                                |                                        | 9   |
| SNMPwrite:PoEwritecapabilities      |                                        | 9   |
| SNMPtraps                           |                                        | 9   |
| ConfiguringSNMP                     |                                        | 10  |
| SNMPcommands                        |                                        | 11  |
|                                     | event-trap-enable                      | 11  |
|                                     | lldptrapenable                         | 12  |
|                                     | rmonalarm                              | 14  |
|                                     | rmonalarm{enable|disable}{index|all}   | 15  |
|                                     | showrmonalarm                          | 16  |
|                                     | showsnmpagent-port                     | 17  |
|                                     | showsnmpcommunity                      | 18  |
|                                     | showsnmpsystem                         | 18  |
|                                     | showsnmptrap                           | 19  |
|                                     | showsnmpvrf                            | 19  |
|                                     | showsnmpv3context                      | 20  |
|                                     | showsnmpv3engine-id                    | 21  |
|                                     | showsnmpv3security-level               | 21  |
|                                     | showsnmpv3users                        | 21  |
|                                     | snmp-serveragent-port                  | 22  |
|                                     | SNMPservercommunitycommands            | 23  |
|                                     | snmp-servercommunity                   | 23  |
|                                     | access-level                           | 23  |
|                                     | access-list                            | 24  |
|                                     | snmp-serverhistorical-counters-monitor | 25  |
|                                     | snmp-serverhost                        | 25  |
|                                     | snmp-serversystem-contact              | 27  |
|                                     | snmp-serversystem-description          | 28  |
|                                     | snmp-serversystem-location             | 29  |
|                                     | snmp-servervrf                         | 29  |
|                                     | snmp-servertrap-sourceinterfacevrf     | 30  |
|                                     | snmp-servertrap                        | 31  |
|                                     | snmp-servertrapvsx                     | 32  |
|                                     | snmpv3context                          | 33  |
|                                     | snmpv3engine-id                        | 34  |
|                                     | snmpv3security-level                   | 35  |
|                                     | snmpv3user                             | 36  |
| EntityMIBsupport                    |                                        | 38  |
3
AOS-CX10.07SNMP/MIBGuide| (6xxxand8xxxSwitchSeries)

| LocationoftheMIBfilesontheweb       |                    |           | 38  |
| ----------------------------------- | ------------------ | --------- | --- |
| NewlyintroducedMIBsandTrapsfor10.07 |                    |           | 38  |
|                                     | PoE                |           | 38  |
|                                     | PORT-ACCESS        |           | 39  |
|                                     | RPVST              |           | 39  |
|                                     | VSX                |           | 39  |
| OIDsthatsupportsSNMPwrite           |                    |           | 40  |
| Support                             | and Other          | Resources | 41  |
| AccessingArubaSupport               |                    |           | 41  |
| AccessingUpdates                    |                    |           | 41  |
|                                     | ArubaSupportPortal |           | 41  |
|                                     | MyNetworking       |           | 42  |
| WarrantyInformation                 |                    |           | 42  |
| RegulatoryInformation               |                    |           | 42  |
| DocumentationFeedback               |                    |           | 42  |
Contents|4

Chapter 1

About this Document

About this Document

This document describes features of the AOS-CX SNMP MIB. It is intended for administrators responsible for
installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A)

n Aruba 8400 Switch Series (JL375A, JL376A)

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

AOS-CX 10.07 SNMP/MIB Guide | (6xxx and 8xxx Switch Series)

5

Convention

Usage

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

About this Document | 6

switch(config-vlan-100)#

When referring to this context, this document uses the syntax:
switch(config-vlan-<VLAN-ID>)#

Where <VLAN-ID> is a variable representing the VLAN number.

Identifying switch ports and interfaces
Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 6100 Switch Series

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

On the 83xx Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

AOS-CX 10.07 SNMP/MIB Guide | (6xxx and 8xxx Switch Series)

7

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

About this Document | 8

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

AOS-CX 10.07 SNMP/MIB Guide | (6xxx and 8xxx Switch Series)

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
Syntax
event-trap-enable
no event-trap-enable
Description
AOS-CX10.07SNMP/MIBGuide|(6xxxand8xxxSwitchSeries) 11

Enables the notification of events to be sent as traps to the SNMP management stations. It is enabled by
default.

The no form of this command disables the event traps.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling the event traps:

switch(config)# event-trap-enable

Disabling the event traps:

switch(config)# no event-trap-enable

lldp trap enable

Syntax

lldp trap enable

no lldp trap enable

Description

Enables sending SNMP traps for LLDP related events from a particular interface. LLDP trap generation is
enabled by default on all the interfaces and has to be disabled for interfaces on which traps are not required
to be generated.

The no form of this command disables the LLDP trap generation.

LLDP trap generation is disabled by default at the global level and must be enabled before any LLDP traps are

sent.

Command context

config and config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling LLDP trap generation on global level:

switch(config)# lldp trap enable

Enabling LLDP trap generation on interface level:

SNMP | 12

| switch(config-if)# |     | lldp trap | enable |     |     |
| ------------------ | --- | --------- | ------ | --- | --- |
DisablingLLDPtrapgenerationongloballevel:
| switch(config)# |     | no lldp trap | enable |     |     |
| --------------- | --- | ------------ | ------ | --- | --- |
DisablingLLDPtrapgenerationoninterfacelevel:
| switch(config-if)# |     | no lldp | trap | enable |     |
| ------------------ | --- | ------- | ---- | ------ | --- |
DisplayingLLDPglobalconfiguration:
| switch#     | show | lldp configuration |     |     |     |
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
| LLDP Enabled  |      |            | : Yes |     |     |
| ------------- | ---- | ---------- | ----- | --- | --- |
| LLDP Transmit |      | Interval   | : 30  |     |     |
| LLDP Hold     | Time | Multiplier | : 4   |     |     |
AOS-CX10.07SNMP/MIBGuide|(6xxxand8xxxSwitchSeries) 13

| LLDP Transmit | Delay Interval | : 2  |     |
| ------------- | -------------- | ---- | --- |
| LLDP Reinit   | Timer Interval | : 2  |     |
| LLDP Trap     | Enabled        | : No |     |
| LLDP Port     | Configuration  |      |     |
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
| mgmt | Yes | Yes | Yes |
| ---- | --- | --- | --- |
rmon alarm
Syntax
rmon alarm index <INDEX> snmp-oid <SNMP-OID> rising-threshold <RISING-THRESHOLD>
falling-threshold <FALLING-THRESHOLD> [sample-interval <SAMPLE-INTERVAL>] [sample-type
<ABSOLUTE|DELTA>]
| no rmon alarm | [index <INDEX>] |     |     |
| ------------- | --------------- | --- | --- |
Description
Storesconfigurationentriesinanalarmtablethatdefinesthesampleinterval,sample-type,andthreshold
parametersforanSNMPMIBobject.OnlytheSNMPMIBobjectsthatresolvetoanASN.1primitivetypeof
INTEGER(INTEGER,Integer32,Counter32,Counter64,Gauge32,orTimeTicks)willbemonitored.
ThenoformofthiscommandremovesallRMONalarmsandallowsyoutospecifyanindextoremovea
particularRMONalarm.
Commandcontext
config
Parameters
index <INDEX>
SpecifiestheRMONalarmindex.Range:1to20.
snmp-oid <SNMP-OID>
SpecifiestheSNMPMIBobjecttobemonitoredbyRMON.
SNMP|14

| rising-threshold |     | <RISING-THRESHOLD> |     |     |     |     |     |     |
| ---------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
SpecifiestheupperthresholdvaluefortheRMONalarm.
| falling-threshold |     | <FALLING-THRESHOLD> |     |     |     |     |     |     |
| ----------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
SpecifiesthefallingthresholdvaluefortheRMONalarm.Thefallingthresholdmustbelessthanthe
risingthreshold.
| sample-interval |     | <SAMPLE-INTERVAL> |     |     |     |     |     |     |
| --------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
Sampleintervalinseconds.Default:30.
| sample-type |     | <ABSOLUTE|DELTA> |     |     |     |     |     |     |
| ----------- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
SpecifiesthemethodofsamplingoftheSNMPMIBobject.Default:Absolute.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringRMONfortheMIBobjectifOutErrors.15withanindex1,risingthresholdof2147483647and
fallingthresholdof-2134usingabsolutesamplingforasampleintervalof100seconds:
switch(config)# rmon alarm index 1 snmp-oid ifOutErrors.15 rising-threshold
2147483647
|     | falling-threshold |     | -2134 | sample-type |     | absolute | sample-interval | 100 |
| --- | ----------------- | --- | ----- | ----------- | --- | -------- | --------------- | --- |
RemovingRMONalarmwiththeindex5:
| switch(config)# |       | no rmon | alarm      | index | 5      |     |        |     |
| --------------- | ----- | ------- | ---------- | ----- | ------ | --- | ------ | --- |
| rmon            | alarm | {enable | | disable} |       | {index |     | | all} |     |
Syntax
| rmon | alarm {enable | | disable} |     | {index <INDEX> |     | | all} |     |     |
| ---- | ------------- | ---------- | --- | -------------- | --- | ------ | --- | --- |
Description
EnablesanddisablestheRMONalarmanditsindex.RMONalarmisenabledbydefault.
Commandcontext
config
Parameters
enable
EnablestheRMONalarmindex
disable
DisablestheRMONalarmindex.
index <INDEX>
SpecifiestheRMONalarmindex.Range:1to20.
all
SpecifiesalltheRMONalarms.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
AOS-CX10.07SNMP/MIBGuide|(6xxxand8xxxSwitchSeries) 15

Examples
EnablingordisablingalltheRMONalarm:
switch(config)#
|                 |     | rmon alarm | enable all  |     |
| --------------- | --- | ---------- | ----------- | --- |
| switch(config)# |     | rmon alarm | disable all |     |
EnablingordisablingRMONalarmbyindex:
| switch(config)# |            | rmon alarm | enable index  | 1   |
| --------------- | ---------- | ---------- | ------------- | --- |
| switch(config)# |            | rmon alarm | disable index | 1   |
| show            | rmon alarm |            |               |     |
Syntax
| show rmon | alarm | [index <INDEX>] |     |     |
| --------- | ----- | --------------- | --- | --- |
Description
DisplaystheRMONalarmconfigurations.
Commandcontext
config
Parameters
index <INDEX>
SpecifiestheRMONalarmindex.Range:1to20.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShowingallRMONalarmconfigurations:
| switch#  | show        | rmon alarm           |          |     |
| -------- | ----------- | -------------------- | -------- | --- |
| Index    |             | : 1                  |          |     |
| Enabled  |             | : true               |          |     |
| Status   |             | : valid              |          |     |
| MIB      | object      | : ifOutErrors.15     |          |     |
| Sample   | type        | : delta              |          |     |
| Sampling | interval    | : 6535               | seconds  |     |
| Rising   | threshold   | : 100                |          |     |
| Falling  | threshold   | : 10                 |          |     |
| Last     | sampled     | value : 0            |          |     |
| Last     | sample time | : 2020-09-21         | 05:58:11 |     |
| Index    |             | : 3                  |          |     |
| Enabled  |             | : true               |          |     |
| Status   |             | : invalid            |          |     |
| MIB      | object      | : IF-MIB::ifDescr.19 |          |     |
| Sample   | type        | : absolute           |          |     |
| Sampling | interval    | : 10000              | seconds  |     |
| Rising   | threshold   | : 4000               |          |     |
SNMP|16

| Falling threshold | : 10      |     |
| ----------------- | --------- | --- |
| Last sampled      | value : 0 |     |
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
| show snmp         | agent-port |                     |
Syntax
show snmp agent-port
Description
DisplaysSNMPagentUDPportnumber.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
AOS-CX10.07SNMP/MIBGuide|(6xxxand8xxxSwitchSeries) 17

Example

Displaying SNMP agent UDP port number:

switch# show snmp agent-port
SNMP agent port : 161

show snmp community

Syntax

show snmp community

Description

Displays a list of all configured SNMPv1/v2c communities.

Command context

Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Usage

When a user creates a custom community before enabling an SNMP agent, AOS-CX automatically removes
the default public community from the system.

Example

Displaying a list of all configured SNMPv1/v2c communities:

Before any community is created by user

switch# show snmp community
---------------------
SNMP communities
---------------------
public

After community is created by user

switch#show snmp community
---------------------
SNMP communities
---------------------
private
private2

show snmp system

Syntax

show snmp system

Description

SNMP | 18

DisplaysSNMPdescription,location,andcontactinformation.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
DisplayingSNMPdescription,location,andcontactinformation:
| switch# show | snmp system |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- |
| SNMP system  | information |     |     |     |     |
----------------------------
| System description | : Aggregation | router    |     |     |     |
| ------------------ | ------------- | --------- | --- | --- | --- |
| System location    | : Main lab    |           |     |     |     |
| System contact     | : John Smith, | Lab Admin |     |     |     |
| show snmp          | trap          |           |     |     |     |
Syntax
show snmp trap
Description
DisplaysallconfiguredSNMPtraps/informsreceivers.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
DisplayingallconfiguredSNMPtrapandinformsreceivers:
| switch# show | snmp trap |     |           |                    |          |
| ------------ | --------- | --- | --------- | ------------------ | -------- |
| HOST         |           |     | PORT TYPE | VER COMMUNITY/USER | NAME VRF |
------------------------------------------------------------------------------------
| 10.10.10.10 |     |     | 162 trap   | v1 public  | default |
| ----------- | --- | --- | ---------- | ---------- | ------- |
| 10.10.10.10 |     |     | 162 inform | v2c public | default |
| 10.10.10.10 |     |     | 162 inform | v3 name    | default |
| show snmp   | vrf |     |            |            |         |
Syntax
show snmp vrf
Description
AOS-CX10.07SNMP/MIBGuide|(6xxxand8xxxSwitchSeries) 19

DisplaystheVRFonwhichtheSNMPagentserviceisrunning.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
DisplayingSNMPservicesenabledonVRF:
| switch#show  | snmp vrf |     |     |     |
| ------------ | -------- | --- | --- | --- |
| SNMP enabled | VRF      |     |     |     |
----------------------------
mgmt
default
| show snmpv3 | context |     |     |     |
| ----------- | ------- | --- | --- | --- |
Syntax
| show snmpv3 context |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
Description
DisplaysallconfiguredSNMPcontexts.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
DisplayingallconfiguredSNMPcontexts:
| switch# show | snmpv3 context |     |     |     |
| ------------ | -------------- | --- | --- | --- |
--------------------------------------------------------------------------
| name |     | vrf |     | community |
| ---- | --- | --- | --- | --------- |
--------------------------------------------------------------------------
| contextA     |                | default |     | private |
| ------------ | -------------- | ------- | --- | ------- |
| contextB     | vrf_A          | public  |     |         |
| switch# show | snmpv3 context |         |     |         |
--------------------------------------------------------------------------
| Name | vrf | Community | ype[Instance_id] |     |
| ---- | --- | --------- | ---------------- | --- |
------------------------------------------------------------------
| A   | default | public | vrf |     |
| --- | ------- | ------ | --- | --- |
switch#
SNMP|20

show snmpv3 engine-id

Syntax

show snmpv3 engine-id

Description

Displays the configured SNMPv3 snmp engine-id.

If the SNMPv3 engine-id is not configured, by default a unique engine-id is created by the switch using a
combination of the enterprise OID value and the switch's mac address.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Displaying the configured SNMPv3 engine-id:

switch# show snmpv3 engine-id
SNMP engine-id : 80:00:B8:5C:08:00:09:1d:de:a5

show snmpv3 security-level

Syntax

show snmpv3 security-level

Description

Displays the configured SNMPv3 security level.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Displaying the configured SNMPv3 security level:

switch# show snmpv3 security-level
SNMPv3 security-level : auth

show snmpv3 users

Syntax

show snmpv3 users

AOS-CX 10.07 SNMP/MIB Guide | (6xxx and 8xxx Switch Series)

21

Description
DisplaysallconfiguredSNMPv3users.
Formoredetailsontheuserenabledstatus,seesnmpv3security-level.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
DisplayingallconfiguredSNMPv3users:
| switch# | show | snmpv3 | users |     |     |     |
| ------- | ---- | ------ | ----- | --- | --- | --- |
---------------------------------------------------------------------
| User |     |     |     | AuthMode | PrivMode | Context Enabled |
| ---- | --- | --- | --- | -------- | -------- | --------------- |
---------------------------------------------------------------------
| name        |     |            |     | md5 | none | none False |
| ----------- | --- | ---------- | --- | --- | ---- | ---------- |
| name2       |     |            |     | sha | aes  | none True  |
| snmp-server |     | agent-port |     |     |      |            |
Syntax
| snmp-server    | agent-port |     | <PORT>   |     |     |     |
| -------------- | ---------- | --- | -------- | --- | --- | --- |
| no snmp-server | agent-port |     | [<PORT>] |     |     |     |
Description
SetstheUDPportnumberthattheSNMPmasteragentusestocommunicate.UDPport161isthedefault
port.
ThenoformofthiscommandsetstheSNMPmasteragentporttothedefaultvalue.
Commandcontext
config
Parameters
<PORT>
SpecifiestheUDPportnumberthattheSNMPmasteragentwilluse.Range:1to65535.Default:161.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingtheSNMPmasteragentportto2000:
| switch(config)# |     | snmp-server | agent-port |     | 2000 |     |
| --------------- | --- | ----------- | ---------- | --- | ---- | --- |
ResettingtheSNMPmasteragentporttothedefaultvalue:
SNMP|22

| switch(config-schedule)# |           |           |     | no snmp-server | agent-port | 2000 |
| ------------------------ | --------- | --------- | --- | -------------- | ---------- | ---- |
| SNMP                     | server    | community |     | commands       |            |      |
| snmp-server              | community |           |     |                |            |      |
Syntax
| snmp-server    | community |           | <STRING> |     |     |     |
| -------------- | --------- | --------- | -------- | --- | --- | --- |
| no snmp-server |           | community | <STRING> |     |     |     |
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
| switch(config)# |     | no  | snmp-server | community | private |     |
| --------------- | --- | --- | ----------- | --------- | ------- | --- |
access-level
Syntax
| access-level    | <ro|rw> |         |     |     |     |     |
| --------------- | ------- | ------- | --- | --- | --- | --- |
| no access-level |         | <ro|rw> |     |     |     |     |
Description
ChangestheaccessleveloftheSNMPcommunity.Thedefaultaccesslevelisread-only(ro).
AOS-CX10.07SNMP/MIBGuide|(6xxxand8xxxSwitchSeries) 23

The no form of this command changes the access level of the community to default.

Command context

config-community

Parameters

ro

rw

Specifies Read-Only access with the SNMP community.

Specifies Read-Write access with the SNMP community.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling the SNMP community:

switch(config)# snmp-server community my_community
switch(config-community)#

Configuring the access level for the SMNP community:

switch(config-community)# access-level rw

Changing the access level of the SNMP community to default:

switch(config-community)# no access-level rw

access-list

Syntax

access-list <ACL-NAME>

no access-list <ACL-NAME>

Description

Associates an ACL with the SNMP community. If an ACL is not associated with the SNMP community, the
default access is allowed for all the hosts.

The no form of this command removes association of the ACL with the SNMP community.

Command context

config-community

Parameters

<ACL-NAME>

Specifies the ACL name. It supports a maximum of 64 characters.

Authority

Administrators or local user group members with execution rights for this command.

SNMP | 24

Examples
EnablingtheSNMPcommunity:
switch(config)#
|     | snmp-server | community | my_community |
| --- | ----------- | --------- | ------------ |
switch(config-community)#
AssociatinganACLwiththeSMNPcommunity:
| switch(config-community)# |     | access-list | my_acl |
| ------------------------- | --- | ----------- | ------ |
RemovingtheassociatedACLwiththeSNMPcommunity:
| switch(config-community)# |     | no access-list | my_acl |
| ------------------------- | --- | -------------- | ------ |
hitcountsforSNMPACLwillnotbeincremented.
Example:show access-list hitcounts ip allwillnotshowthehitcountofSNMPACL.
| snmp-server | historical-counters-monitor |     |     |
| ----------- | --------------------------- | --- | --- |
Syntax
snmp-server historical-counters-monitor
| no snmp-server historical-counters-monitor |     |     |     |
| ------------------------------------------ | --- | --- | --- |
Description
EnablestheRemoteNetworkMonitoringagent(rmond)tostartcollectinghistoricalinterfacestatistics.The
noformofthiscommandstopsthehistoricalinterfacestatisticscollection.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Enablingthermondagenttostarthistoricalinterfacestatisticscollection:
| switch(config)# | snmp-server | historical-counters-monitor |     |
| --------------- | ----------- | --------------------------- | --- |
Disablingthermondagenttostophistoricalinterfacestatisticscollection:
| switch(config)# | no snmp-server | historical-counters-monitor |     |
| --------------- | -------------- | --------------------------- | --- |
| snmp-server     | host           |                             |     |
AOS-CX10.07SNMP/MIBGuide|(6xxxand8xxxSwitchSeries) 25

Syntax

snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>]

no snmp-server host <IPv4-ADDR | IPv6-ADDR> trap version <VERSION> [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>]

snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>]

no snmp-server host <IPv4-ADDR | IPv6-ADDR> inform version v2c [community <STRING>]
[port <UDP-PORT>] [<VRF-NAME>]

snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user <NAME>
[port <UDP-PORT>] [<VRF-NAME>]

no snmp-server host <IPv4-ADDR | IPv6-ADDR> [trap version v3 | inform version v3] user
<NAME>
[port <UDP-PORT>] [<VRF-NAME>]
Description

Configures a trap/informs receiver to which the SNMP agent can send SNMP v1/v2c/v3 traps or v2c
informs. A maximum of 30 SNMP traps/informs receivers can be configured.

The no form of this command removes the specified trap/inform receiver.

Command context

config

Parameters

<IPv4-ADDR>

Specifies the IP address of a trap receiver in IPv4 format (x.x.x.x), where x is a decimal number from 0
to 255. You can remove leading zeros. For example, the address 192.169.005.100 becomes
192.168.5.100.

<IPv6-ADDR>

Specifies the IP address of a trap receiver in IPv6 format (x:x::x:x).

trap version <VERSION>

Specifies the trap notification type for SNMPv1, v2c or v3. Available options are: v1, v2c or v3.

inform version v2c

Specifies the inform notification type for SNMPv2c.

trap version v3

Specifies the trap notification type for SNMPv3.

user <NAME>

Specifies the SNMPv3 user name to be used in the SNMP trap notifications.

community <STRING>

Specifies the name of the community string to use when sending trap notifications. Range: 1 - 32
printable ASCII characters, excluding space and question mark. Default: public.

<UDP-PORT>

Specifies the UDP port on which notifications are sent. Range: 1 - 65535. Default: 162.

<VRF-NAME>

Specifies the VRF on which the SNMP agent listens for incoming requests.

Authority

Administrators or local user group members with execution rights for this command.

Examples

SNMP | 26

| switch(config)# |     | snmp-server |     | host 10.10.10.10 |     | trap version |     | v1  |
| --------------- | --- | ----------- | --- | ---------------- | --- | ------------ | --- | --- |
switch(config)#
|                 |     | no snmp-server |     | host 10.10.10.10 |      | trap         | version | v1  |
| --------------- | --- | -------------- | --- | ---------------- | ---- | ------------ | ------- | --- |
| switch(config)# |     | snmp-server    |     | host a:b::c:d    | trap | version      | v1      |     |
| switch(config)# |     | no snmp-server |     | host a:b::c:d    |      | trap version |         | v1  |
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
switch(config)# snmp-server host a:b::c:d trap version v2c community public
switch(config)# no snmp-server host a:b::c:d trap version v2c community public
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public port
5000
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
| port | 5000 |     |     |     |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
switch(config)# snmp-server host 10.10.10.10 trap version v2c community public port
| 5000 | vrf default |     |     |     |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
switch(config)# no snmp-server host 10.10.10.10 trap version v2c community public
| port | 5000 vrf | default |     |     |     |     |     |     |
| ---- | -------- | ------- | --- | --- | --- | --- | --- | --- |
switch(config)# snmp-server host a:b::c:d trap version v2c community public port
5000
switch(config)# no snmp-server host a:b::c:d trap version v2c community public port
5000
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
switch(config)#
no snmp-server host 10.10.10.10 inform version v2c community public
switch(config)# snmp-server host a:b::c:d inform version v2c community public
switch(config)# no snmp-server host a:b::c:d inform version v2c community public
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
| port | 5000 |     |     |     |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public
| port | 5000 |     |     |     |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
switch(config)# snmp-server host 10.10.10.10 inform version v2c community public
| port | 5000 vrf | default |     |     |     |     |     |     |
| ---- | -------- | ------- | --- | --- | --- | --- | --- | --- |
switch(config)# no snmp-server host 10.10.10.10 inform version v2c community public
| port | 5000 vrf | default |     |     |     |     |     |     |
| ---- | -------- | ------- | --- | --- | --- | --- | --- | --- |
switch(config)# snmp-server host a:b::c:d inform version v2c community public port
5000
switch(config)# no snmp-server host a:b::c:d inform version v2c community public
| port | 5000 |     |     |     |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# no snmp-server host 10.10.10.10 trap version v3 user Admin
switch(config)# snmp-server host a:b::c:d trap version v3 user Admin
switch(config)# no snmp-server host a:b::c:d trap version v3 user Admin
switch(config)# snmp-server host 10.10.10.10 trap version v3 user Admin port 2000
switch(config)#
no snmp-server host 10.10.10.10 trap version v3 user Admin port 2000
switch(config)# snmp-server host a:b::c:d trap version v3 user Admin port 2000
switch(config)# no snmp-server host a:b::c:d trap version v3 user Admin port 2000
| snmp-server |     | system-contact |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
Syntax
| snmp-server    | system-contact |     | <INFO>   |     |     |     |     |     |
| -------------- | -------------- | --- | -------- | --- | --- | --- | --- | --- |
| no snmp-server | system-contact |     | [<INFO>] |     |     |     |     |     |
Description
SetsSNMPcontactinformation.
ThenoformofthiscommandremovestheSNMPcontactinformation.
Commandcontext
config
Parameters
AOS-CX10.07SNMP/MIBGuide|(6xxxand8xxxSwitchSeries) 27

<INFO>

Specifies SNMP contact information. Range: 1 to 128 printable ASCII characters, except for question
mark (?).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines SNMP contact information to be John Smith, Lab Admin:

switch(config)# snmp-server system-contact John Smith, Lab Admin

Removes SNMP contact information:

switch(config)# no snmp-server system-contact

snmp-server system-description

Syntax

snmp-server system-description <DESCRIPTION>

no snmp-server system-description

Description

Sets the SNMP system description.

The no form of this command removes the SNMP system description.

Command context

config

Parameters

<DESCRIPTION>

Specifies the SNMP system description. Typical content to include would be the full name and version of
the following:

n Hardware type of the system

n Software operating system

n Networking software

Range: 1 to 64 printable ASCII characters, except for the question mark (?).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines the SNMP system description to be mainSwitch:

SNMP | 28

| switch(config)# | snmp-server | system-description | mainSwitch |
| --------------- | ----------- | ------------------ | ---------- |
RemovestheSNMPsystemdescription:
| switch(config)# | no snmp-server  | system-description | mainSwitch |
| --------------- | --------------- | ------------------ | ---------- |
| snmp-server     | system-location |                    |            |
Syntax
| snmp-server    | system-location | <INFO> |     |
| -------------- | --------------- | ------ | --- |
| no snmp-server | system-location |        |     |
Description
SetstheSNMPlocationinformation.
ThenoformofthiscommandremovestheSNMPlocationinformation.
Commandcontext
config
Parameters
<INFO>
SpecifiestheSNMPlocationinformation.Range:1to128printableASCIIcharacters,exceptforthe
questionmark(?).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| DefinestheSNMPlocationinformationtobeMain |             |                 | Lab:     |
| ----------------------------------------- | ----------- | --------------- | -------- |
| switch(config)#                           | snmp-server | system-location | Main Lab |
RemovestheSNMPlocationinformation:
| switch(config)# | no snmp-server | system-location |     |
| --------------- | -------------- | --------------- | --- |
| snmp-server     | vrf            |                 |     |
Syntax
| snmp-server    | vrf <VRF-NAME> |     |     |
| -------------- | -------------- | --- | --- |
| no snmp-server | vrf <VRF-NAME> |     |     |
Description
ConfiguresaVRFonwhichtheSNMPagentlistensforincomingrequests.Bydefault,theSNMPagentdoes
notlistenonanyVRF.6100onlysupportsdefaultVRF.TheSNMPagentcanlistenonmultipleVRFs.
AOS-CX10.07SNMP/MIBGuide|(6xxxand8xxxSwitchSeries) 29

The no form of this command stops the SNMP agent from listening for incoming requests on the specified
VRF.

Command context

config

Parameters

<VRF-NAME>

Specifies the name of a VRF.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the SNMP agent to listen on VRF default.

switch(config)# snmp-server vrf default

Configuring the SNMP agent to listen on VRF mgmt.

switch(config)# snmp-server vrf mgmt

Configuring the SNMP agent to listen on used-defined VRF myvrf.

switch(config)# snmp-server vrf myvrf

Stopping the SNMP agent from listening on VRF default.

switch(config)# no snmp-server vrf default

snmp-server trap-source interface vrf

Syntax

snmp-server trap-source {interface <IF-NAME> | <IPv4-Address> | <IPv6-Address>} [vrf <VRF-
NAME>]

no snmp-server trap-source {interface <IF-NAME> | <IPv4-Address> | <IPv6-Address>} [vrf
<VRF-NAME>]

Description

Configures SNMP trap source interface or IP address for a VRF.

The no form of this command removes the SNMP trap-source configuration for a VRF.

Command context

config

Parameters

<IF-NAME>

SNMP | 30

Specifies the source interface name. Interface name can be physical interface, loopback interface, LAG
interface, or VLAN interface.

<IPv4-Address>

Specifies the IPv4 address of source interface for the SNMP trap.

<IPv6-Address>

Specifies the IPv6 address of source interface for the SNMP trap.

<VRF-NAME>

Specifies the name of a VRF associated to the source interface for the SNMP trap.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring SNMP trap source interface for a VRF.

switch(config)# snmp-server trap-source interface 1/1/12 vrf sample
switch(config)# snmp-server trap-source interface loopback10 vrf sample
switch(config)# snmp-server trap-source interface vlan23 vrf sample

Configuring SNMP trap source IP address for a VRF.

switch(config)# snmp-server trap-source 10.0.0.1 vrf red
switch(config)# snmp-server trap-source 1001::1 vrf red

snmp-server trap

Syntax

snmp-server trap {cpu-utilization | memory-utilization | rmon-events}
no snmp-server trap {cpu-utilization | memory-utilization | rmon-events}

Description

Enables the SNMP traps. The SNMP traps are enabled by default.

The no form of this command disables the SNMP traps.

Command context

config

Parameters

cpu-utilization

Enables the CPU utilization traps.

memory-utilization

Enables the memory utilization traps.

rmon-events

Enables the RMON event traps.

Authority

Administrators or local user group members with execution rights for this command.

Examples

AOS-CX 10.07 SNMP/MIB Guide | (6xxx and 8xxx Switch Series)

31

EnablingtheSNMPtraps:
| switch(config)# | snmp-server |     | trap cpu-utilization    |     |
| --------------- | ----------- | --- | ----------------------- | --- |
| switch(config)# | snmp-server |     | trap memory-utilization |     |
| switch(config)# | snmp-server |     | trap rmon-events        |     |
DisablingtheSNMPtraps:
| switch(config)# | no  | snmp-server | trap cpu-utilization |     |
| --------------- | --- | ----------- | -------------------- | --- |
switch(config)#
|                 | no  | snmp-server | trap memory-utilization |     |
| --------------- | --- | ----------- | ----------------------- | --- |
| switch(config)# | no  | snmp-server | trap rmon-events        |     |
DisplayingtheSNMPtrapconfiguration:
| switch(config)# | show                    | running-config | all | inc | snmp |
| --------------- | ----------------------- | -------------- | --------- | ---- |
| snmp-server     | trap rmon-events        |                |           |      |
| snmp-server     | trap cpu-utilization    |                |           |      |
| snmp-server     | trap memory-utilization |                |           |      |
DisplayingCPUandMemoryusage:
switch(config)#
|                    | show | system            |     |     |
| ------------------ | ---- | ----------------- | --- | --- |
| Hostname           |      | : XXXX            |     |     |
| System Description |      | : XX.10.07.0001CI |     |     |
| System Contact     |      | :                 |     |     |
| System Location    |      | :                 |     |     |
| Vendor             |      | : Aruba           |     |     |
Product Name : JLXXXX XXXX Base Chassis/3xFT/18xFans/Cbl Mgr/X462 Bundle
| Chassis      | Serial Nbr | : SG6ZOO9068      |     |     |
| ------------ | ---------- | ----------------- | --- | --- |
| Base MAC     | Address    | : f40343-806400   |     |     |
| ArubaOS-CX   | Version    | : XX.10.07.0001CI |     |     |
| Time Zone    |            | : UTC             |     |     |
| Up Time      |            | : 8 minutes       |     |     |
| CPU Util     | (%)        | : 1               |     |     |
| Memory Usage | (%)        | : 10              |     |     |
| snmp-server  | trap       | vsx               |     |     |
Syntax
| snmp-server    | trap vsx |     |     |     |
| -------------- | -------- | --- | --- | --- |
| no snmp-server | trap vsx |     |     |     |
Description
EnablessendingtheSNMPtrapsforVSXrelatedevents.VSXtrapgenerationisdisabledbydefault.
ThenoformofthiscommanddisablessendingtheSNMPtrapsforVSXrelatedevents.
ThetrapsupportisavailableforthefollowingVSXevents:
n ISLupanddown
KAupanddown
n
MCLAGupanddown
n
Commandcontext
SNMP|32

config
Parameters
vsx
SpecifiesSNMPtrapsforVSXevents.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingtheVSXtraps:
switch(config)#
|                 |         | snmp-server |                   | trap vsx |      |
| --------------- | ------- | ----------- | ----------------- | -------- | ---- |
| switch(config)# |         | show        | vsx configuration |          | trap |
| SNMP            | traps : | Enabled     |                   |          |      |
DisablingtheVSXtraps:
| switch(config)# |     | no  | snmp-server | trap | vsx |
| --------------- | --- | --- | ----------- | ---- | --- |
switch(config)#
|        |         | show     | vsx configuration |     | trap |
| ------ | ------- | -------- | ----------------- | --- | ---- |
| SNMP   | traps : | Disabled |                   |     |      |
| snmpv3 | context |          |                   |     |      |
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
AOS-CX10.07SNMP/MIBGuide|(6xxxand8xxxSwitchSeries) 33

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating an SNMPv3 context named newContext:

switch(config)# snmpv3 context newContext

Creating an SNMPv3 context named newContext on VRF myVrf and with community string private.

switch(config)# snmpv3 context newContext vrf myVrf community private

Removing the SNMPv3 context named newContext on VRF myVrf:

switch(config)# no snmpv3 context newContext vrf myVrf

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

SNMP | 34

RestoringthedefaultSNMPv3engine-id:
| switch(config)# |                | no snmpv3 | engine-id |     |
| --------------- | -------------- | --------- | --------- | --- |
| snmpv3          | security-level |           |           |     |
Syntax
| snmpv3    | security-level | {auth | | auth-privacy} |     |
| --------- | -------------- | ----- | --------------- | --- |
| no snmpv3 | security-level | {auth | | auth-privacy} |     |
Description
ConfigurestheSNMPv3securitylevel.ThesecurityleveldetermineswhichSMNPv3usersdefinedbythe
| commandsnmpv3 |     | userareabletoconnect. |     |     |
| ------------- | --- | --------------------- | --- | --- |
Thenoformofthiscommandchangesthesecuritylevelasfollows:
n no snmpv3 security-level auth:Setsthesecurityleveltoauth-privacy.
n no snmpv3 security-level auth-privacy:Setsthesecurityleveltonoauthenticationorprivacy,
allowinganySNMPusertoconnect.
Commandcontext
config
Parameters
auth
SNMPv3usersthatsupportauthentication,orauthenticationandprivacyareallowed.
auth-privacy
OnlySNMPv3userswithbothauthenticationandprivacyareallowed.Thisisthehighestlevelof
SNMPv3security.Default.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
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
AOS-CX10.07SNMP/MIBGuide|(6xxxand8xxxSwitchSeries) 35

switch(config)# no snmpv3 security-level auth

snmpv3 user

Syntax

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

Command context

config

Parameters

<NAME>

Specifies the SNMPv3 username. Range 1 to 32 printable ASCII characters, excluding space and question
mark (?).

auth <AUTH-PROTO>

Selects the authentication protocol used to validate user logins: md5 or sha1.

auth-pass [{plaintext | ciphertext} <AUTH-PASS>]

Specifies the SNMPv3 user authentication password. Range for plaintext is 8 to 32 printable ASCII
characters, excluding space and question mark (?). Range for ciphertext is 1 to 256 printable ASCII
characters. Ciphertext is used when copying user configuration settings between switches.

priv <PRIV-PROTO>

Selects the SNMPv3 privacy protocol (encryption method): aes or des.

priv-pass [{plaintext | ciphertext} <PRIV-PASS>]

Specifies the SNMPv3 user privacy encryption password. Range for plaintext is 8 to 32 printable ASCII
characters, excluding space and question mark (?). Range for ciphertext is 1 to 256 printable ASCII
characters. Ciphertext is used when copying user configuration settings between switches.

When the authentication password is not provided on the command line, plaintext authentication password

prompting occurs upon pressing Enter, followed by privacy encryption protocol prompting, and finally plaintext

encryption password prompting. The entered password characters are masked with asterisks.

When the authentication type and password plus the privacy protocol (encryption method) are provided on the

command line but the encryption password is not provided, plaintext encryption password prompting occurs upon

pressing Enter. The entered password characters are masked with asterisks.

Authority

Administrators or local user group members with execution rights for this command.

Examples

SNMP | 36

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
!Version ArubaOS-CX xx.xx.xx.xxxxxx
!
snmpv3 user Admin3 auth sha auth-pass ciphertext AQBaf2d...FJVcZ3o=
priv des priv-pass ciphertext AQBaH2p...2jfTFwQ=
ssh server vrf mgmt
!
interface mgmt

no shutdown
ip dhcp

AOS-CX 10.07 SNMP/MIB Guide | (6xxx and 8xxx Switch Series)

37

vlan 1

On switch 2, execute the snmpv3 user command that you saved from switch 1 (as shown by show running-
config). This creates the user on switch 2 with the same configuration.

switch2(config)# snmpv3 user Admin3 auth sha auth-pass ciphertext AQBaf2d...FJVcZ3o=

priv des priv-pass ciphertext AQBaH2p...2jfTFwQ=

Entity MIB support
The Entity MIB, rfc 6933, allows network managers to retrieve physical containment and logical
relationships for devices in the network. The entconfigChange trap is sent to configured SNMP-server hosts
when a change occurs. The trap is configured to send notifications no more than once every 5 seconds. We
will be supporting the Entity MIB for read-only.

Physical components that are supported include:

n Stack

n Chassis

n Fabric cards

n Fan trays

n Fans

n Line cards and their interfaces

n Management modules and the intake temperature sensor

n Power supplies

The slots for any removable component are also represented.

The logical table of the Entity MIB represents configured VLANs and the associated ports.

entConfigChange trap/notification is sent to configured snmp-server hosts.

Location of the MIB files on the web
The MIB files for Aruba switches can be found on the Aruba Service Portal. You can apply the various filters
to filter by product series, software versions, and software release types.

Newly introduced MIBs and Traps for 10.07
The following list contains the newly introduced MIBs and Traps for each software feature. Software is
provided along with the MIB and Traps supported name.

PoE

MIB file

ARUBAWIRED-POE-MIB

Implemented MIB objects:

n arubaWiredPoePethPsePortPoECycle

SNMP | 38

PORT-ACCESS

MIB file

ARUBAWIRED-PORT-ACCESS-MIB.mib

Implemented MIB objects

n arubaWiredPortAccessClientTable

o arubaWiredPacPortName

o arubaWiredPacMac

o arubaWiredPacUserName

o arubaWiredPacAppliedRole

o arubaWiredPacAppliedRoleType

o arubaWiredPacOnboardedMethods

o arubaWiredPacAuthState

o arubaWiredPacAutzFailureReason

o arubaWiredPacVlanId

n arubaWiredPortAccessRoleTable

o arubaWiredParName

o arubaWiredParOrigin

o arubaWiredParUbtGatewayRole

o arubaWiredParUbtGatewayClearpassRole

o arubaWiredParGatewayZone

o arubaWiredParVlanId

o arubaWiredParVlanMode

RPVST

MIB file

ARUBAWIRED-RPVST-MIB

Implemented MIB objects

n arubaWiredRpvstCurrentVportCount

n arubaWiredRpvstMstpInterconnectVlan

VSX

MIB file

ARUBAWIRED-VSX-MIB.mib

Traps supported

n mclagLocalUpPeerUp

n mclagLocalUpPeerDown

n mclagLocalDownPeerUp

n mclagLocalDownPeerDown

AOS-CX 10.07 SNMP/MIB Guide | (6xxx and 8xxx Switch Series)

39

| OIDs that | supports | SNMP | write |     |
| --------- | -------- | ---- | ----- | --- |
ThefollowingtablecontainstheOIDsthatsupportsSNMPwrite:
| Software Feature |     | MIB File       |     | OID          |
| ---------------- | --- | -------------- | --- | ------------ |
| SNMPv2System     |     | SNMPv2-MIB.mib |     | n sysContact |
n sysName
sysLocation
n
| PoE |     | ARUBAWIRED-POE.mib   |     | arubaWiredPoePethPsePortPoECycle |
| --- | --- | -------------------- | --- | -------------------------------- |
|     |     | n                    |     | n                                |
|     |     | n POWER-ETHERNET-MIB |     | n pethPsePortAdminEnable         |
SNMP|40

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

Airheads social forums and Knowledge
Base

https://community.arubanetworks.com/

Software licensing

https://lms.arubanetworks.com/

End-of-Life information

https://www.arubanetworks.com/support-services/end-of-life/

Aruba software and documentation

https://asp.arubanetworks.com/downloads

Accessing Updates
You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

AOS-CX 10.07 SNMP/MIB Guide | (6xxx and 8xxx Switch Series)

41

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

Support and Other Resources | 42