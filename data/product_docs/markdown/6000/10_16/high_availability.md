AOS-CX 10.16.xxxx High
Availability Guide

All Switch Series

Published: October 2025

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

Acknowledgments

Intel®, Itanium®, Optane™, Pentium®, Xeon®, Intel Inside®, and the Intel Inside logo are trademarks of
Intel Corporation in the U.S. and other countries.

Microsoft® and Windows® are either registered trademarks or trademarks of Microsoft Corporation in
the United States and/or other countries.

Adobe® and Acrobat® are trademarks of Adobe Systems Incorporated.

Java® and Oracle® are registered trademarks of Oracle and/or its affiliates.

UNIX® is a registered trademark of The Open Group.

All third-party marks are property of their respective owners.

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

3

Contents
| About this                                 | document                                    | 7   |
| ------------------------------------------ | ------------------------------------------- | --- |
| Applicableproducts                         |                                             | 7   |
| Latestversionavailableonline               |                                             | 8   |
| Commandsyntaxnotationconventions           |                                             | 8   |
| Abouttheexamples                           |                                             | 8   |
| Identifyingswitchportsandinterfaces        |                                             | 9   |
| Identifyingmodularswitchcomponents         |                                             | 10  |
| High Availability                          |                                             | 12  |
| HighAvailabilityOverview                   |                                             | 12  |
|                                            | HighAvailabilityswitchoverbehaviors         | 13  |
| ManagementModuleFailoverOverview           |                                             | 14  |
|                                            | HighAvailabilityswitchoverbehaviors         | 15  |
| AAAonSwitcheswithMultipleManagementModules |                                             | 16  |
| HighAvailabilityCommands                   |                                             | 16  |
|                                            | redundancyswitchover                        | 16  |
| BFD                                        |                                             | 18  |
| BFDFeatures                                |                                             | 18  |
| ConfiguringBFDforanIPv4StaticRoute         |                                             | 19  |
| ConfiguringBFDforBGP                       |                                             | 20  |
| ConfiguringBFDforOSPFv2                    |                                             | 22  |
| ConfiguringBFDforOSPFv3                    |                                             | 24  |
| ConfiguringBFDforOSPFv3AF                  |                                             | 25  |
| ConfiguringBFDforPIMOverIPv4               |                                             | 27  |
| ConfiguringBFDforPIMOverIPv6               |                                             | 28  |
| ConfiguringBFDforVRRP                      |                                             | 30  |
| BFDCommands                                |                                             | 31  |
|                                            | bfd                                         | 31  |
|                                            | bfd<IPV4-ADDR>                              | 32  |
|                                            | bfdall-interfaces(OSPF)                     | 33  |
|                                            | bfddetect-multiplier                        | 34  |
|                                            | bfddisable                                  | 35  |
|                                            | bfdenable(Context:config-hsc)               | 36  |
|                                            | bfddisable(Context:config-hsc)              | 37  |
|                                            | bfdechodisable                              | 38  |
|                                            | bfdecho-src-ip-address                      | 39  |
|                                            | bfdmin-echo-receive-interval                | 40  |
|                                            | bfdmin-receive-interval                     | 41  |
|                                            | bfdmin-transmit-interval                    | 42  |
|                                            | clearbfdstatistics                          | 43  |
|                                            | ipospfbfd                                   | 44  |
|                                            | ipospfbfddisable                            | 45  |
|                                            | iproutebfd                                  | 46  |
|                                            | ipv6ospfv3bfd                               | 47  |
|                                            | ipv6ospfv3bfddisable                        | 48  |
|                                            | neighborfall-overbfd(context:config-router) | 49  |
|                                            | ospfv3-afipv4bfd                            | 50  |
|                                            | ospfv3-afipv6bfd                            | 51  |
5
AOS-CX10.16.xxxxHighAvailabilityGuide| (AllSwitchSeries)

|                                    | showbfd                                     |     | 52  |
| ---------------------------------- | ------------------------------------------- | --- | --- |
|                                    | showbfdinterface                            |     | 57  |
|                                    | showhsc                                     |     | 59  |
| ERPS                               |                                             |     | 60  |
| Limitations,Conflicts,orExclusions |                                             |     | 61  |
| ERPSCommands                       |                                             |     | 62  |
|                                    | clearerpsring<RINGID>instance<ID>           |     | 62  |
|                                    | clearerpsstatistics                         |     | 63  |
|                                    | erpsring                                    |     | 64  |
|                                    | erpsring<RINGID><port0|port1>interface      |     | 65  |
|                                    | erpsring<RINGID>description                 |     | 66  |
|                                    | erpsring<RINGID>guard-interval              |     | 67  |
|                                    | erpsring<RINGID>hold-off-interval           |     | 68  |
|                                    | erpsring<RINGID>instance                    |     | 69  |
|                                    | erpsring<RINGID>instance<ID>control-vlan    |     | 70  |
|                                    | erpsring<RINGID>instance<ID>description     |     | 72  |
|                                    | erpsring<RINGID>instance<ID>enable          |     | 73  |
|                                    | erpsring<RINGID>instance<ID>protected-vlans |     | 74  |
erpsring<RINGID>instance<ID>protection-switch{manual|force}
|                                    | <PORT0>|<PORT1>                       |           | 75  |
| ---------------------------------- | ------------------------------------- | --------- | --- |
|                                    | erpsring<RINGID>instance<ID>revertive |           | 77  |
|                                    | erpsring<RINGID>instance<ID>role      |           | 78  |
|                                    | erpsring<RINGID>instance<ID>rpl       |           | 79  |
|                                    | erpsring<RINGID>meg-level             |           | 81  |
|                                    | erpsring<RINGID>parent-ring           |           | 82  |
|                                    | erpsring<RINGID>sub-ring              |           | 83  |
|                                    | erpsring<RINGID>tcn-propogation       |           | 84  |
|                                    | erpsring<RINGID>transmission-interval |           | 85  |
|                                    | erpsring<RINGID>wtr-interval          |           | 86  |
|                                    | showerpsstatistics                    |           | 87  |
|                                    | showerpsstatus                        |           | 89  |
|                                    | showerpssummary                       |           | 91  |
| Support                            | and Other                             | Resources | 93  |
| AccessingHPEArubaNetworkingSupport |                                       |           | 93  |
| AccessingUpdates                   |                                       |           | 94  |
| WarrantyInformation                |                                       |           | 94  |
| RegulatoryInformation              |                                       |           | 94  |
| DocumentationFeedback              |                                       |           | 94  |
|6

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

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

7

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
Aboutthisdocument|8

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

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

9

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

About this document | 10

n Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

o member: 1.

o tray: 1 to 4.

o fan: 1 to 4.

n Fabric modules are not labeled on the switch but are labeled in software in the format:

member/module:

o member: 1.

o member: 1 or 2.

n The display module on the rear of the switch is not labeled with a member or slot number.

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

11

Chapter 2

High Availability

High Availability

The High Availability (HA) feature has three components:

n Redundant Management

n OVSDB synchronization

n Filesystem replication

High Availability Overview

Key goals of HA include:

n Achieve five-nines (99.999%) availability of switching traffic through minimization of unplanned

network outages.

n Fault tolerant: No single active component failure will cause an outage.

n Live replacement of hardware with minimal or no disruption.

Terminology:

n MM: Abbreviation for management module

n MM to MM link: Refers to the 10GbE-KR Ethernet link between two MMs

n OVSDB: Abbreviation for Open vSwitch Database

n Active MM: Management module that has control of the chassis

n Standby MM: Backup management module for the active management module

n JSON-RPC: Remote procedure call protocol encoded in JSON

Key parts of the HA feature include:

Network redundancy: Protocols and redundant network paths provide redundancy in the network,
enabling traffic to continue flowing if a network link or network switch fails.

Hardware redundancy: Redundant hardware components (power supplies, fabric cards, management
modules) allow continued switching traffic or system management in the event of a hardware failure or
hardware maintenance. This functionality is supported through:

n Fast failover (management failover)

n Hot insert and removal (all field-replaceable hardware components)

Redundancy of specific, field-replaceable hardware components includes:

n Redundancy management (management modules), which is in charge of:

o HA infrastructure

o File synchronization

o OVSDB synchronization

o MM failover

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

12

o Standby MM configuration

o Software version update

The Active MM controls infrastructure, files, and the database. If the Active MM is removed, all
management passes to the Standby MM.

n Fabric redundancy (fabric cards)

n Network interface redundancy (line cards)

n Power management (power supplies)

n Software redundancy: Software (including daemons) provides redundancy in software by

supporting one or more of the following methods:

o Nonstop switching restart:

l The daemon reads its last known state or the current hardware state from OVSDB.

l The daemon adjusts its internal state to match the last known state.

l There is no traffic interruption and no moment in time where the last known configuration is

not in effect.

l The daemon restarts fast enough to respond to protocols that require peer communication

without timing out.

l Examples include LACP, ACLS, TCAM entries, and MSTP.

o Graceful restart:

l Current state is still read from OVSDB. Traffic follows the rules of this state until the protocol

has fully recovered.

l Connections to other switches are re-established.

l Current state is republished to peers, which can then respond back with adjustments.

l Examples include routing protocols.

o Full state reset:

l Any non-default runtime state the daemon has in hardware or OVSDB is forced back to the

default state.

l Any connections are closed and have to be manually restarted.

l This is primarily for user-facing daemons and features for which the default state does not

have a large impact on traffic.

l Examples include SSH, web server, TFTP, and CLI.

High Availability switchover behaviors

The following behaviors are expected during an HA switchover event.

n The count of console login attempts is cleared (reset to 0).

n The count of login attempts for the aaa authentication limit-login-attempts feature is cleared

(reset to 0).

n The output of the command show authentication locked-out-userslist is cleared of users locked

out via the console.

n The output of the command show authentication locked-out-users list is cleared of users locked

out via SSH, TELNET, or REST (as verified on an SSH channel.)

High Availability | 13

Management Module Failover Overview

There are two types of Management Module (MM) failover:

n Controlled failover: The user triggers this type of failover by rebooting the Active MM or running

the redundancy switchover command.

n Uncontrolled failover: This type of failover is triggered by unexpected events like a crash on the

Active MM or hot removal of the Active MM.

In a dual MM chassis, the Standby MM detects failover events in one of the following ways:

n A mailbox interrupt is received from the Active MM to indicate takeover. This interrupt can come for

controlled or uncontrolled failover (except for a hot removal).

n Active MM hot removal detection.

n Heartbeat loss detected on the Standby MM for more than 10 seconds.

If the Active MM is not responding and is still not detected by the first two methods, it will be caught

by this method.

Failover requirements:

n The Standby MM must be present to trigger a failover. An Unassigned MM will never trigger a

failover.

n The Redundant Management Daemon (hpe-rdntmgmtd) is responsible for triggering failover from the

Standby MM.

n When a failover is triggered, the Standby MM becomes the Active MM while the previously Active MM

is rebooted.

Standby recovery requirements:

n The Active MM must be present to trigger a recovery.

n The Redundant Management Daemon (hpe-rdntmgmtd) is responsible for triggering recover from the

Active MM.

n When a recovery is triggered, the Active MM reboots the nonresponsive Standby MM. This action

occurs for any of the following conditions:

Condition: Heartbeat lost from Active MM:

n The failover monitor thread on the Standby MM will increment the heartbeat failed count.

n The hpe-rdntmgmtd daemon on the Standby MM will:

o Detect the failover condition due to heartbeat fail count increasing past the maximum of 10 and

triggering failover

o Initiate reboot of the Active MM.

n Active MM will join as a standby after reboot.

Condition: Heartbeat lost from Standby MM:

n The recover monitor thread on the Active MM will increment the heartbeat failed count.

n The hpe-rdntmgmtd daemon on the Active MM will:

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

14

o Detect the recover condition due to heartbeat fail count increasing past the maximum of 7 and

triggering recover.

o Initiate reboot of Standby MM.

n Standby MM will join as a standby after reboot.

Condition: Planned reboot of Active MM:

n A planned reboot on the Active MM will send a failover command to the Standby MM.

n The hpe-rdntmgmtd daemon on the Standby MM will:

o Process this command and perform a failover immediately instead of waiting for the failover

monitor to detect it using heartbeats.

o Initiate reboot of the Active MM.

n Active MM will join as a standby after reboot.

Condition: Removal of Active MM:

n Removal of the Active MM from Slot 1 triggers the hpe-rdntmgmtd daemon on the Standby MM to

initiate failover immediately instead of waiting for the failover monitor to detect it using heartbeats.

n Active MM will join as a standby after reboot.

Condition: Crash on Active MM:

n A crash on the Active MM is handled by the crash handler, which sends a failover command to the

Standby MM.

n The hpe-rdntmgmtd daemon on the Standby MM will:

o Process this command and perform failover immediately instead of waiting for the failover

monitor to detect it using heartbeats.

o Initiate reboot of the Active MM.

n Active MM will join as a standby after reboot.

Condition: redundancy switchover command:

n User executes the redundancy switchover command on the Active MM.

n This action will send a takeover signal to the Standby MM and reboot the Active MM.

n The hpe-rdntmgmtd daemon on Standby MM will process this takeover signal and perform failover

immediately.

n Active MM will join as a standby after reboot.

Why did my second MM not take over after Active failed?

This action will happen if the second MM is not Standby-Ready.

The second MM must be elected as Standby and in a ready state before failover. If not, a double fault occurs and

the second MM will not take over.

High Availability switchover behaviors

The following behaviors are expected during an HA switchover event:

High Availability | 15

n The count of console login attempts is cleared (reset to 0).

n The count of login attempts for the aaa authentication limit-login-attempts feature is cleared

(reset to 0).

n The output of the command show authentication locked-out-users list is cleared of users locked

out via the console.

n The output of the command show authentication locked-out-users list is cleared of users locked

out via SSH, TELNET, or REST (as verified on an SSH channel.)

AAA on Switches with Multiple Management Modules

Consider the following when working with local authentication, authorization, and accounting (AAA) on
switchers with multiple management modules:

n Local authentication:

o The user database is synchronized between the Active and Standby management modules.

o Only local users belonging to the administrators group and using local password authentication

are permitted to log in to the Standby management module. Alternatively, the Standby
management module can be accessed from the Active management module by providing a
logged in admin user password.

n Local authorization:

o A few nonconfiguration commands are available on the Standby management module.

o For expert users, the bash shell is available on the Standby management module.

n Local accounting:

o The audit logs used for local accounting are available only on the Active Management Module.

High Availability Commands

redundancy switchover
redundancy switchover

Description

Causes the switch to immediately switch over to the Standby Management Module. This command must
be executed from the Active Management Module and will fail if the Standby Management Module is in
a failed state or not present.

Examples

This example shows the redundancy switchover command on an active management module with a
standby management module that is present.

switch#redundancy switchover
This command causes the switch to immediately switchover to the Standby Management
Module.
Do you want to continue [y/n]?

This example shows the redundancy switchover command on an active management module with a
standby management module that is absent.

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

16

| switch#redundancy | switchover |     |     |
| ----------------- | ---------- | --- | --- |
Standby Management Module not found, switchover request ignored.
Thisexampleshowstheredundancyswitchovercommandonastandbymanagementmodule.
| switch#redundancy | switchover |     |     |
| ----------------- | ---------- | --- | --- |
Redundancy switchover must be performed from the Active Management Module,
| switchover          | request | ignored. |              |
| ------------------- | ------- | -------- | ------------ |
| Command History     |         |          |              |
| Release             |         |          | Modification |
| 10.07orearlier      |         |          | --           |
| Command Information |         |          |              |
| Platforms           | Command | context  | Authority    |
5420 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
HighAvailability|17

Chapter 3

BFD

BFD

The BFD feature and thus this entire chapter is not applicable to the 5420 and 6200 Switch Series.

Bidirectional Forwarding Detection (BFD) provides a general-purpose, standard, medium- and protocol-
independent fast failure detection mechanism. It can detect and monitor the connectivity of links in IP to
detect communication failures quickly. BFD operates independently of media, data protocols, and
routing protocols.

BFD establishes a session between two network devices to detect failures on the bidirectional
forwarding paths between the devices and provide services for upper-layer protocols. BFD provides no
neighbor discovery mechanism. Protocols that BFD services notify BFD of devices to which it needs to
establish sessions. After a session is established, if no BFD control packet is received from the peer
within the negotiated BFD interval, BFD notifies a failure to the protocol, which then takes appropriate
measures.

BFD operates in two modes:

n Asynchronous mode: In this mode, an operating device periodically sends BFD control packets to
another device. If the other device does not receive BFD control packet from the peer within the
specified interval, it tears down the BFD session.

n Demand mode: in this mode, it is assumed that an operating device has an independent way of
verifying that it has connectivity to the peer. Once a BFD session is established, one device may
request that the other device stops sending BFD control packets, except when the connection must
be explicitly validated, in which case a short sequence of BFD control packets is exchanged. Demand
mode may operate independently in each direction, or simultaneously.

BFD also has an echo function. When echo is active, an operating device periodically sends BFD echo
packets. The peer device returns the received BFD echo packets back without processing them (it loops
them through its forwarding path). If the sending device does not receive BFD echo packets from the
peer within a specified interval, the session is considered down. Since the echo function is handling the
task of detection, the rate of periodic transmission of control packets may be reduced in asynchronous
mode, and eliminated in demand mode.

BFD Features

BGP, OSPFv2, OSPFv3, PIMv4 and PIMv6, static routes, and VRRP are clients of BFD.

Supported:

n BFD v1

n Asynchronous mode + echo

n IPv6 (6300, 6400, 8100, 8320, 8325/8325H/8325P, 8360, 8400, 9300/9300S, 10000, 10040 switches

only)

n Asynchronous mode on IPv6 tunnel interfaces (8400 switches only)

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

18

n Asynchronous mode for VxLAN tunnels (8325, 8360, and 8400, and 9300/9300S, 10000, 10040

switches only)

n Single hop

n IPv4

n RoP, SVI, and LAG interfaces

n VSX synchronization. For more information, see the Virtual Switching Extension (VSX) Guide for your

switch and software version.

n Loopbacks are supported for VxLAN sessions (8325/8325H/8325P, 8360 and 8400 switches only), and

static routes (6300, 6400 and 8400 switches only). Same IP version restrictions apply.

Not supported:

n MIB support

n Demand mode

n Micro-BFD

n Authentication

n Echo function on tunnel interfaces

n BFD sessions are not supported on tunnel interfaces (6300, 6400, and 8320 switches only)

n Echo function for IPv6

n Asynchronous mode on tunnel interfaces (832x, 9300/9300S and 10040 switches only)

n Multi-hop configurations. BFD works only for directly connected neighbors. BFD neighbors must be

no more than one IP hop away.

n Passive and virtual link interfaces.

n Exceeding a maximum of 20 BFD sessions with interval values of 300ms. Spurious sessions flaps will

occur when the limit of sessions is exceeded.

n Minimum intervals of 300ms are only compatible with the async_vxlan mode (BFD sessions across

VxLAN) and is not user configurable.

n Setting minimum transmit time interval between 500 ms and 1000 ms, and bfd deect-multiplier

less than 3 might result in spurious flaps.

Configuring BFD for an IPv4 Static Route

Procedure

1. Enable BFD support with the command bfd.

2. Enable BFD on an IPv4 static route with the command ip route bfd.

3. For most deployments, the default values for the following features do not need to be changed. If

your deployment requires different settings, change the default values with the indicated
command:

BFD setting

Default value

Command to change it

Sets the BFD detection
multiplier on an interface.

5

bfd detect-multiplier

Sets the minimum time
interval between received

500 milliseconds

bfd min-echo-receive-interval

BFD | 19

| BFD setting |     | Default | value Command | to change | it  |
| ----------- | --- | ------- | ------------- | --------- | --- |
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimes
leadtoBFDsessionflapsdependingupontrafficconditions.
| 4. ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     | bfd. |     |
| ---------------------------------------------------- | --- | --- | --- | ---- | --- |
Example
EnablingBFDonastaticIPv4route.
| switch# config     |             |                |              |     |     |
| ------------------ | ----------- | -------------- | ------------ | --- | --- |
| switch(config)#    | bfd         |                |              |     |     |
| switch# interface  | 1/1/1       |                |              |     |     |
| switch(config-if)# | no shutdown |                |              |     |     |
| switch(config-if)# | ip address  | 192.168.1.1/24 |              |     |     |
| switch(config-if)# | exit        |                |              |     |     |
| switch(config)#    | ip route    | 10.0.2.0/24    | 20.0.0.2 bfd |     |     |
| Configuring        | BFD for     | BGP            |              |     |     |
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. CreateaBGPpeerandinitiateaconnectiontoitwiththecommandneighbor remote-as.
3. EnableBFDonaBGPinterfacewiththecommandneighbor fall-over bfd.
4. Defineanaddressfamilyandactivateitwiththecommandsaddress-familyandneighbor
activate.
5. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicated
command:
| BFD setting         |     | Default | value Command         | to change | it  |
| ------------------- | --- | ------- | --------------------- | --------- | --- |
| SetstheBFDdetection |     | 5       | bfd detect-multiplier |           |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 20

Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimes
leadtoBFDsessionflapsdependingupontrafficconditions.
| 6. ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     |     |     | bfd. |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- |
Example
EnablingBFDonaBGPinterface.
| switch# config                 |        |                |            |              |            |          |     |     |
| ------------------------------ | ------ | -------------- | ---------- | ------------ | ---------- | -------- | --- | --- |
| switch(config)#                | bfd    |                |            |              |            |          |     |     |
| switch(config)#                | router | bgp 100        |            |              |            |          |     |     |
| switch(config-router)#         |        | neighbor       | 10.1.231.2 |              | remote-as  | 100      |     |     |
| switch(config-router)#         |        | neighbor       | 10.1.231.2 |              | fall-over  | bfd      |     |     |
| switch(config-router)#         |        | address-family |            | ipv4-unicast |            |          |     |     |
| switch(config-router-ipv4-uc)# |        |                | neighbor   |              | 10.1.231.2 | activate |     |     |
| switch(config-router-ipv4-uc)# |        |                | exit       |              |            |          |     |     |
| switch(config-router)#         |        | exit           |            |              |            |          |     |     |
switch(config)#
exit
| switch# show       | ip bgp | neighbors  |     |     |     |     |     |     |
| ------------------ | ------ | ---------- | --- | --- | --- | --- | --- | --- |
| Codes: ^ Inherited | from   | peer-group |     |     |     |     |     |     |
VRF : default
| BGP Neighbor        | 9.0.0.1   | (External)    |        |     |                   |            |         |           |
| ------------------- | --------- | ------------- | ------ | --- | ----------------- | ---------- | ------- | --------- |
| Description         |           | :             |        |     |                   |            |         |           |
| Peer-group          |           | :             |        |     |                   |            |         |           |
| Remote              | Router Id | : 0.0.0.0     |        |     | Local             | Router     | Id      | : (null)  |
| Remote              | AS        | : 100         |        |     | Local             | AS         |         | : 100     |
| Remote              | Port      | : 0           |        |     | Local             | Port       |         | : 0       |
| State               |           | : Idle        |        |     | Admin             | Status     |         | : Up      |
| Conn. Established   |           | : 0           |        |     | Conn.             | Dropped    |         | : 0       |
| Passive             |           | : No          |        |     | Update-Source     |            |         | :         |
| Cfg. Hold           | Time      | : 180         |        |     | Cfg.              | Keep       | Alive   | : 60      |
| Neg. Hold           | Time      | : 0           |        |     | Neg.              | Keep       | Alive   | : 0       |
| Up/Down             | Time      | : 00h:00m:00s |        |     | Alt.              | Local-AS   |         | : 0       |
| Local-AS            | Prepend   | : No          |        |     |                   |            |         |           |
| Fall-over           |           | : No          |        |     | BFD               |            |         | : Enabled |
| Password            |           | :             |        |     |                   |            |         |           |
| Last Err            | Sent      | : No          | Error  |     |                   |            |         |           |
| Last SubErr         | Sent      | : No          | Error  |     |                   |            |         |           |
| Last Err            | Rcvd      | : No          | Error  |     |                   |            |         |           |
| Last SubErr         | Rcvd      | : No          | Error  |     |                   |            |         |           |
| Graceful-Restart    |           | : Enabled     |        |     | Rt.               | Reflect.   | Client: | No        |
| Gr. Restart         | Time      | : 120         |        |     | Gr.               | Stalepath  | Time    | : 150     |
| Max. Prefix         |           | : 0           |        |     | Send              | Community  |         | :         |
| Allow-AS            | in        | : 0           |        |     | Remove            | Private-AS |         | : No      |
| Advt. Interval      |           | : 30          |        |     | TTL               |            |         | : 255     |
| Soft Reconfig       | In        | :             |        |     | Local             | Cluster-ID |         | :         |
| Nexthop-Self        |           | :             |        |     | Default-Originate |            |         | :         |
| Weight              |           | : 0           |        |     |                   |            |         |           |
| TTL Security        | Hops      | : 0           |        |     |                   |            |         |           |
| Routemap            | In        | :             |        |     |                   |            |         |           |
| Routemap            | Out       | :             |        |     |                   |            |         |           |
| Message statistics: |           |               |        |     |                   |            |         |           |
|                     |           | Sent          | Rcvd   |     |                   |            |         |           |
|                     |           | -----         | ------ |     |                   |            |         |           |
| Open                |           | 0             |        | 0   |                   |            |         |           |
| Notification        |           | 0             |        | 0   |                   |            |         |           |
| Updates             |           | 0             |        | 0   |                   |            |         |           |
BFD|21

|     | Keepalives    |     | 0          | 0        |     |     |     |
| --- | ------------- | --- | ---------- | -------- | --- | --- | --- |
|     | Route Refresh |     | 0          | 0        |     |     |     |
|     | Total         |     | 0          | 0        |     |     |     |
|     | Capability    |     | Advertised | Received |     |     |     |
---------------------------------------------
|             | Route Refresh |         | No         |     | No  |     |     |
| ----------- | ------------- | ------- | ---------- | --- | --- | --- | --- |
|             | Graceful      | Restart | No         |     | No  |     |     |
|             | Four Octet    | ASN     | No         |     | No  |     |     |
| Configuring |               | BFD     | for OSPFv2 |     |     |     |     |
Prerequisites
n OSPFv2mustbeenabled.
n ICMPmustbedisabled.
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. EnableBFDonallOSPFinterfaceswiththecommandbfd all-interfaces,orenableBFDona
|     | specificinterfacewiththecommandip |     |     | ospf | bfd. |     |     |
| --- | --------------------------------- | --- | --- | ---- | ---- | --- | --- |
3. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicated
command:
|     | BFD setting         |     | Default | value | Command               | to change | it  |
| --- | ------------------- | --- | ------- | ----- | --------------------- | --------- | --- |
|     | SetstheBFDdetection |     | 5       |       | bfd detect-multiplier |           |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,settingadetectionmultiplierof1)can
sometimesleadtoBFDsessionflapsdependingupontrafficconditions.
| 4.  | ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     |     | bfd. |     |
| --- | ------------------------------------------------- | --- | --- | --- | --- | ---- | --- |
Examples
ThisexampleshowshowtoenableBFDonallOSPFv2interfaces.
|     | switch# config         |        |                    |     |     |     |     |
| --- | ---------------------- | ------ | ------------------ | --- | --- | --- | --- |
|     | switch(config)#        | bfd    |                    |     |     |     |     |
|     | switch(config)#        | router | ospf 1             |     |     |     |     |
|     | switch(config-ospf-1)# |        | area 1             |     |     |     |     |
|     | switch(config-ospf-1)# |        | bfd all-interfaces |     |     |     |     |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 22

| switch(config-ospf-1)# |     |     | exit |     |     |     |     |     |
| ---------------------- | --- | --- | ---- | --- | --- | --- | --- | --- |
switch(config)
|                        |     | router    | ospf     | 2              |     |     |     |     |
| ---------------------- | --- | --------- | -------- | -------------- | --- | --- | --- | --- |
| switch(config-ospf-2)# |     |           | area     | 2              |     |     |     |     |
| switch(config-ospf-2)# |     |           | bfd      | all-interfaces |     |     |     |     |
| switch(config-ospf-2)# |     |           | exit     |                |     |     |     |     |
| switch(config)#        |     | interface |          | 1/1/1          |     |     |     |     |
| switch(config-if)#     |     | no        | shutdown |                |     |     |     |     |
| switch(config-if)#     |     | ip        | address  | 192.168.1.1/24 |     |     |     |     |
| switch(config-if)#     |     | ip        | ospf     | 1 area         | 1   |     |     |     |
| switch(config-if)#     |     | exit      |          |                |     |     |     |     |
| switch(config)#        |     | interface |          | 1/1/2          |     |     |     |     |
switch(config-if)#
no shutdown
| switch(config-if)# |      | ip        | address | 192.168.1.2/24 |     |     |     |     |
| ------------------ | ---- | --------- | ------- | -------------- | --- | --- | --- | --- |
| switch(config-if)# |      | ip        | ospf    | 2 area         | 2   |     |     |     |
| switch(config-if)# |      | exit      |         |                |     |     |     |     |
| switch(config)#    |      | exit      |         |                |     |     |     |     |
| switch#            | show | bfd       |         |                |     |     |     |     |
| Admin status       |      | : Enabled |         |                |     |     |     |     |
| Echo source        | IP   | : 2.2.2.2 |         |                |     |     |     |     |
Statistics:
| Total Number |     | of Control | Packets |     | Transmitted | : 42 |     |     |
| ------------ | --- | ---------- | ------- | --- | ----------- | ---- | --- | --- |
| Total Number |     | of Control | Packets |     | Received    | : 42 |     |     |
| Total Number |     | of Control | Packets |     | Dropped     | : 0  |     |     |
Session Interface Source IP Destination IP Echo State Application
------- --------- --------------- --------------- -------- ---------- -----------
| 1   | 1/1/1 | 192.168.1.1 |     |     | 100.100.100.101 |     | Enabled Up | OSPF |
| --- | ----- | ----------- | --- | --- | --------------- | --- | ---------- | ---- |
| 2   | 1/2/2 | 192.168.1.2 |     |     | 10.1.5.6        |     | Enabled Up | OSPF |
ThisexampleshowshowtoenableBFDonaspecificOSPFv2interface.
| switch#         | config |     |     |     |     |     |     |     |
| --------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| switch(config)# |        | bfd |     |     |     |     |     |     |
switch(config)#
|                        |     | router    | ospf     | 1              |     |     |     |     |
| ---------------------- | --- | --------- | -------- | -------------- | --- | --- | --- | --- |
| switch(config-ospf-1)# |     |           | area     | 1              |     |     |     |     |
| switch(config-ospf-1)# |     |           | exit     |                |     |     |     |     |
| switch(config)#        |     | interface |          | 1/1/1          |     |     |     |     |
| switch(config-if)#     |     | no        | shutdown |                |     |     |     |     |
| switch(config-if)#     |     | ip        | address  | 192.168.1.1/24 |     |     |     |     |
| switch(config-if)#     |     | ip        | ospf     | 1 area         | 1   |     |     |     |
| switch(config-if)#     |     | ip        | ospf     | bfd            |     |     |     |     |
| switch(config-if)#     |     | exit      |          |                |     |     |     |     |
| switch(config)#        |     | exit      |          |                |     |     |     |     |
switch#
|                     | show          | bfd session | 1      |         |     |     |     |     |
| ------------------- | ------------- | ----------- | ------ | ------- | --- | --- | --- | --- |
| BFD Session         | Information   |             | –      | Session | 1   |     |     |     |
| Min Tx              | Interval      | (sec)       | : 10   |         |     |     |     |     |
| Min Rx              | Interval      | (sec)       | : 10   |         |     |     |     |     |
| Min Echo            | Rx Interval   |             | (msec) | : 700   |     |     |     |     |
| Detect              | Multiplier    | : 3         |        |         |     |     |     |     |
| Application         | :             | OSPF        |        |         |     |     |     |     |
| Local Discriminator |               | :           | 1      |         |     |     |     |     |
| Remote              | Discriminator |             | : 1    |         |     |     |     |     |
Echo : Enabled
| Local Diagnostic |             | : N/A |     |     |     |     |     |     |
| ---------------- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
| Remote           | Diagnostic: | N/A   |     |     |     |     |     |     |
| Flap count:      | 0           |       |     |     |     |     |     |     |
| Internal         | state:      | Up    |     |     |     |     |     |     |
Interface Source IP Destination IP State Pkt In Pkt Out Pkt Drop
--------- --------------- --------------- ---------- -------- -------- --------
| 1/1/1 | 192.168.1.1 |     |     | 100.100.100.101 |     | Up  | 100 101 | 0   |
| ----- | ----------- | --- | --- | --------------- | --- | --- | ------- | --- |
BFD|23

| Configuring |     | BFD for | OSPFv3 |     |     |     |     |
| ----------- | --- | ------- | ------ | --- | --- | --- | --- |
Prerequisites
n OSPFv3mustbeenabled.
n ICMPmustbedisabled.
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. EnableBFDonallOSPFinterfaceswiththecommandbfd all-interfaces,orenableBFDona
|     | specificinterfacewiththecommandipv6 |     |     | ospfv3 | bfd. |     |     |
| --- | ----------------------------------- | --- | --- | ------ | ---- | --- | --- |
3. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicated
command:
|     | BFD setting         |     |     | Default value | Command               | to change | it  |
| --- | ------------------- | --- | --- | ------------- | --------------------- | --------- | --- |
|     | SetstheBFDdetection |     |     | 5             | bfd detect-multiplier |           |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimes
leadtoBFDsessionflapsdependingupontrafficconditions.
| 4.  | ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     |     | bfd. |     |
| --- | ------------------------------------------------- | --- | --- | --- | --- | ---- | --- |
Examples
ThisexampleshowshowtoenableBFDonanallOSPFv3interfaces.
|     | switch# config  |        |        |     |     |     |     |
| --- | --------------- | ------ | ------ | --- | --- | --- | --- |
|     | switch(config)# | bfd    |        |     |     |     |     |
|     | switch(config)# | router | ospfv3 | 1   |     |     |     |
switch(config-ospfv3-1)#
area 1
|     | switch(config-ospfv3-1)# |           | router-id | 1.1.1.1        |     |     |     |
| --- | ------------------------ | --------- | --------- | -------------- | --- | --- | --- |
|     | switch(config-ospfv3-1)# |           | bfd       | all-interfaces |     |     |     |
|     | switch(config-ospfv3-1)# |           | exit      |                |     |     |     |
|     | switch(config)           | router    | ospfv3    | 2              |     |     |     |
|     | switch(config-ospfv3-2)# |           | area      | 2              |     |     |     |
|     | switch(config-ospfv3-2)# |           | router-id | 1.1.1.2        |     |     |     |
|     | switch(config-ospfv3-2)# |           | bfd       | all-interfaces |     |     |     |
|     | switch(config-ospfv3-2)# |           | exit      |                |     |     |     |
|     | switch(config)#          | interface | 1/1/1     |                |     |     |     |
switch(config-if)#
|     |                    | no        | shutdown |           |     |     |     |
| --- | ------------------ | --------- | -------- | --------- | --- | --- | --- |
|     | switch(config-if)# | ipv6      | address  | 100::1/64 |     |     |     |
|     | switch(config-if)# | ipv6      | ospfv3   | 1 area 1  |     |     |     |
|     | switch(config-if)# | exit      |          |           |     |     |     |
|     | switch(config)#    | interface | 1/1/2    |           |     |     |     |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 24

| switch(config-if)# |     | no  | shutdown |     |     |     |     |     |     |
| ------------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
switch(config-if)#
|                    |         | ipv6          | address |     | 100::2/64 |     |     |     |     |
| ------------------ | ------- | ------------- | ------- | --- | --------- | --- | --- | --- | --- |
| switch(config-if)# |         | ipv6          | ospfv3  | 2   | area      | 2   |     |     |     |
| switch(config-if)# |         | exit          |         |     |           |     |     |     |     |
| switch(config)#    |         | exit          |         |     |           |     |     |     |     |
| switch# show       | bfd     |               |         |     |           |     |     |     |     |
| Admin status:      | enabled |               |         |     |           |     |     |     |     |
| Echo source        | IP:     | 100.100.100.1 |         |     |           |     |     |     |     |
Statistics:
| Total number      | of          | control | packets |     | transmitted: | 20  |             |     |      |
| ----------------- | ----------- | ------- | ------- | --- | ------------ | --- | ----------- | --- | ---- |
| Total number      | of          | control | packets |     | received:    | 17  |             |     |      |
| Total number      | of          | control | packets |     | dropped:     | 0   |             |     |      |
| Session Interface |             | VRF     | Source  |     | IP           |     | Destination | IP  | Echo |
| State             | Application |         |         |     |              |     |             |     |      |
------- --------- ------- --------------- --------------- -------
| - ------------ |     | ------------ |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
1 tunnel1 default fe80::94f1:28a0:1ef:700 fe80::94f1:28a0:1ef:a100 enabled
| up  | ospfv3 |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
2 tunnel1 default fe80::94e2:37b1:1ef:111 fe80::94e2:37b1:1ef:555 enabled
| up  | ospfv3 |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ThisexampleshowshowtoenableBFDonaspecificOSPFv3interface.
| switch# config           |     |           |           |     |         |     |     |     |     |
| ------------------------ | --- | --------- | --------- | --- | ------- | --- | --- | --- | --- |
| switch(config)#          |     | bfd       |           |     |         |     |     |     |     |
| switch(config)#          |     | router    | ospfv3    | 1   |         |     |     |     |     |
| switch(config-ospfv3-1)# |     |           | area      | 1   |         |     |     |     |     |
| switch(config-ospfv3-1)# |     |           | router-id |     | 1.1.1.1 |     |     |     |     |
| switch(config-ospfv3-1)# |     |           | exit      |     |         |     |     |     |     |
| switch(config)#          |     | interface | 1/1/1     |     |         |     |     |     |     |
switch(config-if)#
|                    |         | no            | shutdown |       |           |     |     |     |     |
| ------------------ | ------- | ------------- | -------- | ----- | --------- | --- | --- | --- | --- |
| switch(config-if)# |         | ipv6          | address  |       | 100::1/64 |     |     |     |     |
| switch(config-if)# |         | ipv6          | ospfv3   | 1     | area      | 1   |     |     |     |
| switch(config-if)# |         | ipv6          | ospfv3   | bfd   |           |     |     |     |     |
| switch(config-if)# |         | exit          |          |       |           |     |     |     |     |
| switch(config)#    |         | exit          |          |       |           |     |     |     |     |
| switch# show       | bfd     | interface     |          | 1/1/1 |           |     |     |     |     |
| Admin status:      | enabled |               |          |       |           |     |     |     |     |
| Echo source        | IP:     | 100.100.100.1 |          |       |           |     |     |     |     |
Statistics:
| Total number      | of  | control     | packets |        | transmitted: | 20  |             |     |      |
| ----------------- | --- | ----------- | ------- | ------ | ------------ | --- | ----------- | --- | ---- |
| Total number      | of  | control     | packets |        | received:    | 17  |             |     |      |
| Total number      | of  | control     | packets |        | dropped:     | 0   |             |     |      |
| Session Interface |     | VRF         |         | Source | IP           |     | Destination | IP  | Echo |
| State             |     | Application |         |        |              |     |             |     |      |
------- --------- --------- --------------- --------------- -----
| --- ------------ |     | ------------ |     |     |     |     |     |     |     |
| ---------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
1 tunnel1 default fe80::94f1:28a0:1ef:700 fe80::94f1:28a0:1ef:a100
| enabled up  |     |     | ospfv3 |        |     |     |     |     |     |
| ----------- | --- | --- | ------ | ------ | --- | --- | --- | --- | --- |
| Configuring |     | BFD | for    | OSPFv3 |     | AF  |     |     |     |
EnablingBFDSupportforOSPFv3AFoverIPv6enablesOSPFv3AFtoregisterwithBidirectional
ForwardingDetection(BFD)toreceiveforwardingpathdetectionfailuremessages.Youcaneither
configureBFDforOSPFv3AFgloballyonallinterfacesorconfigureitselectivelyononeormore
BFD|25

interfaces. BFD creates a session in asynchronous mode as soon as the switch reaches the 2-Way state
with a neighbor. Once the session is established BFD will commence sending echos for path failure
detection.

OSPFv3 AF uses IPv6 for neighborship in both IPv4 and IPv6 unicast address-families. Therefore, only a
single BFD session is created to monitor the IPv6 link-local address, even when both address-families
are enabled on the same interface.

There are two methods for enabling BFD for OSPFv3 AF:

1. Enable BFD for all interfaces enabled for OSPFv3 AF by using the BFD all-interfaces command in

address-family configuration mode

2. Enable BFD for a subset of interfaces that have OSPFv3 AF enabled by using the ospfv3-af bfd

command in interface configuration mode

OSPFv3 AF needs to be enabled prior to enabling BFD on one or more interfaces.

Prerequisites

n OSPFv3 AF must be enabled.

n ICMP must be disabled.

Procedure

1. Enable BFD support with the command bfd.

2. Enable BFD on all OSPF interfaces with the command bfd all-interfaces, or enable BFD on a

specific interface using the command ospfv3-af ipv4 bfd or ospfv3-af ipv6 bfd.

3. For most deployments, the default values for the following features do not need to be changed. If

your deployment requires different settings, change the default values with the indicated
command:

BFD setting

Default value

Command to change it

Sets the BFD detection
multiplier on an interface.

5

bfd detect-multiplier

Sets the minimum time
interval between received
BFD echo packets.

Sets the minimum time
interval between transmitted
BFD control packets on an
interface.

500 milliseconds

bfd min-echo-receive-interval

3000 milliseconds

bfd min-transmit-interval

Configuring the timers to be too aggressive (for example, detect-multiplier of 1) can sometimes
lead to BFD session flaps depending upon traffic conditions.

4. Review BFD configuration settings with the commands show bfd.

Examples

Enabling BFD on all OSPFv3 AF Interfaces

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

26

| switch(config)# |     |     | router | ospfv3-af |     | 1   |     |     |     |
| --------------- | --- | --- | ------ | --------- | --- | --- | --- | --- | --- |
switch(config-ospfv3-af-1)#
|                                |        |          |           |           | address-family |                    | ipv4 unicast   |     |     |
| ------------------------------ | ------ | -------- | --------- | --------- | -------------- | ------------------ | -------------- | --- | --- |
| switch(config-ospfv3-ipv4-uc)# |        |          |           |           |                | bfd all-interfaces |                |     |     |
| Disabling                      | BFD    | on all   | OSPFv3    | AF        | Interfaces     |                    |                |     |     |
| switch(config)#                |        |          | router    | ospfv3-af |                | 1                  |                |     |     |
| switch(config-ospfv3-af-1)#    |        |          |           |           | address-family |                    | ipv4 unicast   |     |     |
| switch(config-ospfv3-ipv4-uc)# |        |          |           |           |                | no bfd             | all-interfaces |     |     |
| Enabling                       | BFD on | a single |           | OSPFv3    | AF             | interface          |                |     |     |
| switch(config)#                |        |          | interface |           | 1/1/1          |                    |                |     |     |
switch(config-if)#
|                    |     |         | ospfv3-af |           | ipv4  | bfd          |         |     |     |
| ------------------ | --- | ------- | --------- | --------- | ----- | ------------ | ------- | --- | --- |
| switch(config-if)# |     |         | ospfv3-af |           | ipv6  | bfd          |         |     |     |
| Disabling          | BFD | on a    | single    | OSPFv3    | AF    | interface    |         |     |     |
| switch(config)#    |     |         | interface |           | 1/1/1 |              |         |     |     |
| switch(config-if)# |     |         | ospfv3-af |           | ipv4  | bfd          | disable |     |     |
| switch(config-if)# |     |         | ospfv3-af |           | ipv6  | bfd          | disable |     |     |
| Setting BFD        | as  | default | on        | an OSPFv3 |       | AF interface |         |     |     |
| switch(config)#    |     |         | interface |           | 1/1/1 |              |         |     |     |
switch(config-if)#
|                    |          |         | no   | ospfv3-af    |     | ipv4 bfd |     |     |     |
| ------------------ | -------- | ------- | ---- | ------------ | --- | -------- | --- | --- | --- |
| switch(config-if)# |          |         | no   | ospfv3-af    |     | ipv6 bfd |     |     |     |
| Showing            | BFD with | OSPFv3  |      | AF neighbors |     |          |     |     |     |
| switch(config)#    |          |         | show | bfd          |     |          |     |     |     |
| Admin              | status:  | enabled |      |              |     |          |     |     |     |
| Echo               | source   | IP:     | N/A  |              |     |          |     |     |     |
Statistics:
| Total   | number    | of  | control | packets |        | transmitted: | 1   |             |     |
| ------- | --------- | --- | ------- | ------- | ------ | ------------ | --- | ----------- | --- |
| Total   | number    | of  | control | packets |        | received:    | 2   |             |     |
| Total   | number    | of  | control | packets |        | dropped:     | 0   |             |     |
| Session | Interface |     | VRF     |         | Source | IP           |     | Destination | IP  |
------- --------- -------- ------------------------ --------------------------
1 1/1/1 default fe80::98f2:b301:468:de52 fe80::98f2:b301:1068:ecae
| Echo        | State  | Protocol   |     |     |     |      |      |     |     |
| ----------- | ------ | ---------- | --- | --- | --- | ---- | ---- | --- | --- |
| -----       | ------ | ---------- |     |     |     |      |      |     |     |
| N/A         | up     | ospfv3_af  |     |     |     |      |      |     |     |
| Configuring |        |            | BFD | for | PIM | Over | IPv4 |     |     |
Prerequisites
PIMmustbeenabledgloballyandonthespecificinterfacethatwillsupportBFD.
BFD|27

Procedure
1. EnableBFDsupportwiththecommandbfd.
2. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicated
command:
|     | BFD setting         |     |     |     | Default | value | Command |                   | to change | it  |     |
| --- | ------------------- | --- | --- | --- | ------- | ----- | ------- | ----------------- | --------- | --- | --- |
|     | SetstheBFDdetection |     |     |     | 5       |       | bfd     | detect-multiplier |           |     |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimes
leadtoBFDsessionflapsdependingupontrafficconditions.
3. SwitchtotheinterfaceonwhichyouwanttoenableBFDwiththecommandinterface.
| 4.  | EnableBFDsupportwiththecommandip                  |     |     |     |     | pim-sparse |     | bfd. |      |     |     |
| --- | ------------------------------------------------- | --- | --- | --- | --- | ---------- | --- | ---- | ---- | --- | --- |
| 5.  | ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     |     |            |     |      | bfd. |     |     |
Examples
ThisexampleshowshowtoconfigurePIMandenableBFDoninterface1/1/2.
|     | switch# config      |     |           |       |     |     |     |     |     |     |     |
| --- | ------------------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
|     | switch(config)#     |     | bfd       |       |     |     |     |     |     |     |     |
|     | switch(config)#     |     | router    | pim   |     |     |     |     |     |     |     |
|     | switch(config-pim)# |     | enable    |       |     |     |     |     |     |     |     |
|     | switch(config-pim)# |     | exit      |       |     |     |     |     |     |     |     |
|     | switch(config)#     |     | interface | 1/1/2 |     |     |     |     |     |     |     |
switch(config-if)#
|     |                    |         | no   | shutdown   |             |     |     |     |     |     |     |
| --- | ------------------ | ------- | ---- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
|     | switch(config-if)# |         | ip   | address    | 10.1.1.1/24 |     |     |     |     |     |     |
|     | switch(config-if)# |         | ip   | pim-sparse | enable      |     |     |     |     |     |     |
|     | switch(config-if)# |         | ip   | pim-sparse | bfd         |     |     |     |     |     |     |
|     | switch(config-if)# |         | exit |            |             |     |     |     |     |     |     |
|     | switch(config)#    |         | exit |            |             |     |     |     |     |     |     |
|     | switch# show       | bfd     |      |            |             |     |     |     |     |     |     |
|     | Admin status:      | enabled |      |            |             |     |     |     |     |     |     |
Statistics:
|     | Total number      | of          | control | packets | transmitted: |     | 7   |             |     |     |      |
| --- | ----------------- | ----------- | ------- | ------- | ------------ | --- | --- | ----------- | --- | --- | ---- |
|     | Total number      | of          | control | packets | received:    |     | 8   |             |     |     |      |
|     | Total number      | of          | control | packets | dropped:     | 0   |     |             |     |     |      |
|     | Session Interface |             | VRF     |         | Source IP    |     |     | Destination | IP  |     | Echo |
|     | State             | Application |         |         |              |     |     |             |     |     |      |
------- --------- --------- ------------------- ---------------------- -------- --
|     | ---------- | ------------ |         |     |     |     |     |          |     |     |            |
| --- | ---------- | ------------ | ------- | --- | --- | --- | --- | -------- | --- | --- | ---------- |
|     | 1 1/1/2    |              | default |     | N/A |     |     | 10.1.1.2 |     |     | enabled up |
pim
| Configuring |     |     | BFD | for | PIM Over | IPv6 |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | -------- | ---- | --- | --- | --- | --- | --- |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 28

Prerequisites
PIMmustbeenabledgloballyandonthespecificinterfacethatwillsupportBFD.
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicated
command:
| BFD setting         |     |     |     | Default value |     | Command               | to change | it  |     |
| ------------------- | --- | --- | --- | ------------- | --- | --------------------- | --------- | --- | --- |
| SetstheBFDdetection |     |     |     | 5             |     | bfd detect-multiplier |           |     |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimes
leadtoBFDsessionflapsdependingupontrafficconditions.
3. SwitchtotheinterfaceonwhichyouwanttoenableBFDwiththecommandinterface.
| 4. EnableBFDsupportwiththecommandip |     |     |     |     |     | bfd. |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
pim-sparse
| 5. ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     |     |     |     | bfd. |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
Examples
ThisexampleshowshowtoconfigurePIMandenableBFDoninterface1/1/2.
| switch# config      |         |               |            |            |     |     |     |     |     |
| ------------------- | ------- | ------------- | ---------- | ---------- | --- | --- | --- | --- | --- |
| switch(config)#     |         | bfd           |            |            |     |     |     |     |     |
| switch(config)#     |         | router        | pim6       |            |     |     |     |     |     |
| switch(config-pim)# |         | enable        |            |            |     |     |     |     |     |
| switch(config-pim)# |         | exit          |            |            |     |     |     |     |     |
| switch(config)#     |         | interface     | 1/1/2      |            |     |     |     |     |     |
| switch(config-if)#  |         | no shutdown   |            |            |     |     |     |     |     |
| switch(config-if)#  |         | ipv6          | address    | 2130::1/64 |     |     |     |     |     |
| switch(config-if)#  |         | ipv6          | mld enable |            |     |     |     |     |     |
| switch(config-if)#  |         | ip pim-sparse |            | enable     |     |     |     |     |     |
| switch(config-if)#  |         | ip pim-sparse |            | bfd        |     |     |     |     |     |
| switch(config-if)#  |         | exit          |            |            |     |     |     |     |     |
| switch(config)#     |         | exit          |            |            |     |     |     |     |     |
| switch# show        | bfd     |               |            |            |     |     |     |     |     |
| Admin status:       | enabled |               |            |            |     |     |     |     |     |
| Echo source         | IP:     | <none>        |            |            |     |     |     |     |     |
Statistics:
| Total number      | of  | control     | packets | transmitted: |     | 8           |     |     |      |
| ----------------- | --- | ----------- | ------- | ------------ | --- | ----------- | --- | --- | ---- |
| Total number      | of  | control     | packets | received:    | 8   |             |     |     |      |
| Total number      | of  | control     | packets | dropped:     | 0   |             |     |     |      |
| Session Interface |     | VRF         | Source  | IP           |     | Destination | IP  |     | Echo |
| State             |     | Application |         |              |     |             |     |     |      |
------- --------- --------- ------------------- ----------------------------- ----
BFD|29

|             | ---- ------------ |       | ------------ |       |      |     |                          |     |     |
| ----------- | ----------------- | ----- | ------------ | ----- | ---- | --- | ------------------------ | --- | --- |
|             | 1                 | 1/1/2 | default      |       | N/A  |     | fe80::94f1:2821:2ef:6300 |     |     |
|             | enabled           | up    |              | pimv6 |      |     |                          |     |     |
| Configuring |                   |       | BFD          | for   | VRRP |     |                          |     |     |
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. EnableBFDonaVRRPinterfacewiththecommandbfd<IPV4-ADDR>.
3. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicated
command:
|     | BFD                 | setting |     |     | Default value |     | Command               | to change | it  |
| --- | ------------------- | ------- | --- | --- | ------------- | --- | --------------------- | --------- | --- |
|     | SetstheBFDdetection |         |     |     | 5             |     | bfd detect-multiplier |           |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimes
leadtoBFDsessionflapsdependingupontrafficconditions.
|     | 4. ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     |     |     |     | bfd. |     |
| --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- |
Example
EnablingBFDonaVRRPinterface.
|     | switch#         | config |     |     |     |     |     |     |     |
| --- | --------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     | switch(config)# |        | bfd |     |     |     |     |     |     |
switch#
|     |                         | interface | 1/1/1    |                      |                |      |     |     |     |
| --- | ----------------------- | --------- | -------- | -------------------- | -------------- | ---- | --- | --- | --- |
|     | switch(config-if)#      |           | no       | shutdown             |                |      |     |     |     |
|     | switch(config-if)#      |           | ip       | address              | 192.168.1.1/24 |      |     |     |     |
|     | switch(config-if)#      |           | vrrp     | 1 address-family     |                | ipv4 |     |     |     |
|     | switch(config-if-vrrp)# |           |          | bfd                  | 192.158.1.2    |      |     |     |     |
|     | switch(config-if-vrrp)# |           |          | exit                 |                |      |     |     |     |
|     | switch#                 | show      | vrrp     |                      |                |      |     |     |     |
|     | VRRP is                 | enabled   |          |                      |                |      |     |     |     |
|     | Interface               | 1/1/1     | - Group  | 1 -                  | Address-Family | IPv4 |     |     |     |
|     | State                   | is ACTIVE |          |                      |                |      |     |     |     |
|     | State                   | duration  | 56 mins  | 57.826               | secs           |      |     |     |     |
|     | Virtual                 | IP        | address  | is 10.0.0.1          |                |      |     |     |     |
|     | Virtual                 | MAC       | address  | is 00:00:5e:00:01:01 |                |      |     |     |     |
|     | Advertisement           |           | interval | is                   | 1000 msec      |      |     |     |     |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 30

| Preemption | enabled       |          |          |           |              |        |
| ---------- | ------------- | -------- | -------- | --------- | ------------ | ------ |
| Priority   | is            | 100      |          |           |              |        |
| Active     | Router        | is       | 10.0.0.2 | (local),  | priority     | is 100 |
| Active     | Advertisement |          | interval |           | is 1000 msec |        |
| Active     | Down          | interval | is       | unknown   |              |        |
| Tracked    | object        | ID       | is 1,    | and state | Down         |        |
BFD Commands
bfd
bfd
no bfd
Description
EnablesBFDsupportontheswitch.BFDisdisabledbydefault.
ThenoformofthiscommanddisablesBFDandremovesallrelatedconfigurationsettings.Todisable
BFD,butretainconfigurationsettings,usethecommandbfddisable.
Examples
EnablingBFDsupport:
| switch(config)# |     | bfd |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
DisablingBFDsupportandremovingallconfigurationsettings:
| switch(config)#     |         | no  | bfd     |     |              |     |
| ------------------- | ------- | --- | ------- | --- | ------------ | --- |
| Command History     |         |     |         |     |              |     |
| Release             |         |     |         |     | Modification |     |
| 10.07orearlier      |         |     |         |     | --           |     |
| Command Information |         |     |         |     |              |     |
| Platforms           | Command |     | context |     | Authority    |     |
6300except config Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     |     |     | rightsforthiscommand. |     |
| ----------- | --- | --- | --- | --- | --------------------- | --- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
BFD|31

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
9300
9300S
10000
10040
bfd <IPV4-ADDR>
bfd <IPV4-ADDR>
no bfd <IPV4-ADDR>
Description
EnablesBFDunderVRRPforthespecifiedIPaddress.BFDisasynchronousandechomodeis
supported.
ThenoformofthiscommanddisablesBFDunderVRRPforthespecifiedIPaddress.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IPV4-ADDR> SpecifiestheaddressonwhichtoenableBFDinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.
Examples
OntheHPEArubaNetworking6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDontheaddress10.0.0.1onVRRP1:
| switch(config)#         |     | interface 1/1/1       |     |      |
| ----------------------- | --- | --------------------- | --- | ---- |
| switch(config-if)#      |     | routing               |     |      |
| switch(config-if)#      |     | vrrp 1 address-family |     | ipv4 |
| switch(config-if-vrrp)# |     | bfd 10.0.0.1          |     |      |
DisablingBFDontheaddress10.0.0.1onVRRP1:
| switch(config)#         |         | interface 1/1/1       |              |      |
| ----------------------- | ------- | --------------------- | ------------ | ---- |
| switch(config-if)#      |         | routing               |              |      |
| switch(config-if)#      |         | vrrp 1 address-family |              | ipv4 |
| switch(config-if-vrrp)# |         | no bfd                | 10.0.0.1     |      |
| Command History         |         |                       |              |      |
| Release                 |         |                       | Modification |      |
| 10.07orearlier          |         |                       | --           |      |
| Command Information     |         |                       |              |      |
| Platforms               | Command | context               | Authority    |      |
config-if-vrrp
6300except Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |     |
| ----------- | --- | --- | --------------------- | --- |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 32

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| bfd all-interfaces |     | (OSPF) |     |     |
| ------------------ | --- | ------ | --- | --- |
bfd all-interfaces
no bfd all-interfaces
Description
EnablesBFDonallOSPFv2orOSPFv3interfaces.
ThenoformofthiscommanddisablesBFDonallactiveOSPFv2/OSPFv3orIPv4/IPv6interfaces,
excludingthoseonwhichBFDwasenabledattheinterfacelevelwiththecommandsip ospf bfdand
| ipv6 ospfv3 | bfd. |     |     |     |
| ----------- | ---- | --- | --- | --- |
Examples
EnablingBFDonallOSPFv2interfaces:
| switch(config)#        | router | ospf | 1              |     |
| ---------------------- | ------ | ---- | -------------- | --- |
| switch(config-ospf-1)# |        | bfd  | all-interfaces |     |
DisablingBFDonallOSPFv2interfaces:
| switch(config)#        | router | ospf | 1                  |     |
| ---------------------- | ------ | ---- | ------------------ | --- |
| switch(config-ospf-1)# |        | no   | bfd all-interfaces |     |
EnablingBFDonallOSPFv3interfaces:
| switch(config)#          | router | ospfv3 | 1                  |     |
| ------------------------ | ------ | ------ | ------------------ | --- |
| switch(config-ospfv3-1)# |        |        | bfd all-interfaces |     |
DisablingBFDonallOSPFv3interfaces:
| switch(config)#          | router | ospfv3 | 1      |                |
| ------------------------ | ------ | ------ | ------ | -------------- |
| switch(config-ospfv3-1)# |        |        | no bfd | all-interfaces |
| Command History          |        |        |        |                |
BFD|33

| Release             |         | Modification |           |
| ------------------- | ------- | ------------ | --------- |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
6300except config-ospf-<INSTANCE-TAG> Administratorsorlocalusergroupmemberswith
for S3L75A, config-ospfv3-<INSTANCE-TAG> executionrightsforthiscommand.
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
bfd detect-multiplier
| bfd detect-multiplier    |     | <MULTIPLIER> |     |
| ------------------------ | --- | ------------ | --- |
| no bfd detect-multiplier |     | <MULTIPLIER> |     |
Description
SetsBFDdetectionmultiplieronaninterface.
ThenoformofthiscommandremovestheconfiguredBFDdetectionmultiplier.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<MULTIPLIER> SpecifiestheBFDdetectionmultiplier.Range:1to5.Default:5.
Examples
SettingtheBFDdetectionmultiplierto3:
| switch(config-if)# |     | bfd detect-multiplier | 3   |
| ------------------ | --- | --------------------- | --- |
RemovingtheBFDdetectionmultiplier:
| switch(config-if)# |     | no bfd detect-multiplier | 3   |
| ------------------ | --- | ------------------------ | --- |
SettingtheBFDdetectionmultipliertothedefaultvalue:
| switch(config-if)# |     | no bfd detect-multiplier |     |
| ------------------ | --- | ------------------------ | --- |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 34

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6300except config-if Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |
| ----------- | --- | --- | --------------------- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
bfd disable
bfd disable
Description
DisablesBFDontheswitch,butretainsallconfigurationsettings.
Examples
DisablingBFD:
| switch(config)#     | bfd     | disable |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6300except config Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |
| ----------- | --- | --- | --------------------- |
S3L76A,
S3L77A
BFD|35

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| bfd enable          | (Context: | config-hsc) |     |
| ------------------- | --------- | ----------- | --- |
| switch(config-hsc)# | bfd       | enable      |     |
| switch(config-hsc)# | no        | bfd enable  |     |
Description
EnablesordisablesBFDforHSCfeature.
Usage
BFDmustbeenabledgloballytoworkforHSC.
Examples
EnablingBFDsupportforHSC:
| switch(config)#     | hsc |            |     |
| ------------------- | --- | ---------- | --- |
| switch(config-hsc)# |     | bfd enable |     |
DisablingBFDsupportforHSC:
| switch(config)#     | hsc         |               |              |
| ------------------- | ----------- | ------------- | ------------ |
| switch(config-hsc)# |             | no bfd enable |              |
| Command             | History     |               |              |
| Release             |             |               | Modification |
| 10.07orearlier      |             |               | --           |
| Command             | Information |               |              |
| Platforms           | Command     | context       | Authority    |
6300except config Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |
| ----------- | --- | --- | --------------------- |
S3L76A,
S3L77A
6400
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 36

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| bfd disable         | (Context: | config-hsc) |     |
| ------------------- | --------- | ----------- | --- |
| switch(config-hsc)# | bfd       | disable     |     |
Description
DisablesBFDforHSCfeature.
Example
DisablingBFDsupportforHSC:
| switch(config)#     | hsc     |             |              |
| ------------------- | ------- | ----------- | ------------ |
| switch(config-hsc)# |         | bfd disable |              |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
6300except config Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |
| ----------- | --- | --- | --------------------- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
BFD|37

| bfd echo | disable |     |     |     |
| -------- | ------- | --- | --- | --- |
bfd echo disable
| no bfd echo | disable |     |     |     |
| ----------- | ------- | --- | --- | --- |
Description
DisablessupportforBFDechopackets.Echopacketsupportisenabledbydefault.
ThenoformofthiscommandenablessupportforBFDechopackets.
Togglingthisfeatureon8100,8325,8360,9300,9300S,10040switchesmaycauserouteflapping.
BFDIPv6Echoisnotsupported.
Authority
Examples
OntheHPEArubaNetworking6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDechopacketsupportonallinterfaces:
| switch(config)# | no  | bfd echo | disable |     |
| --------------- | --- | -------- | ------- | --- |
DisablingBFDechopacketsupportonallinterfaces:
| switch(config)# | bfd | echo | disable |     |
| --------------- | --- | ---- | ------- | --- |
EnablingBFDechopacketsupportoninterface1/1/1:
| switch(config)#    | interface |          | 1/1/1   |     |
| ------------------ | --------- | -------- | ------- | --- |
| switch(config-if)# |           | bfd echo | disable |     |
DisablingBFDechopacketsupportoninterface1/1/1:
| switch(config)# | interface |     | 1/1/1 |     |
| --------------- | --------- | --- | ----- | --- |
switch(config-if)#
|                     |         | no bfd  | echo | disable      |
| ------------------- | ------- | ------- | ---- | ------------ |
| Command History     |         |         |      |              |
| Release             |         |         |      | Modification |
| 10.07orearlier      |         |         |      | --           |
| Command Information |         |         |      |              |
| Platforms           | Command | context |      | Authority    |
6300except config Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, | config-if |     |     | rightsforthiscommand. |
| ----------- | --------- | --- | --- | --------------------- |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 38

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
bfd echo-src-ip-address
| bfd echo-src-ip-address    |     | <IPV4-ADDR> |     |     |
| -------------------------- | --- | ----------- | --- | --- |
| no bfd echo-src-ip-address |     | <IPV4-ADDR> |     |     |
Description
SetsthesourceIPv4addressforBFDechopackets.Thisaddressisusedinallechosessions.
ThesourceIPaddressmustnotbeonthesamenetworksegmentasanyswitchinterface,otherwisealarge
numberofICMPredirectpacketsmaybesentbytheremotedevice,causingnetworkcongestion.
ThenoformofthiscommandremovesthesourceIPv4addressforBFDechopackets,whichcausesthe
switchtostopsendingechopackets.Whenavalidvalueisset,allsessionswithapeerthatiscapableof
receivingechopackets,willstarttransmittingechopackets.BFDcontrolsessionscontinuetorun
concurrentlywithechopackets.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IPV4-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.
Examples
SettingthesourceIPaddressto198.51.100.1:
| switch(config)# | bfd | echo-src-ip-address |     | 198.51.100.1 |
| --------------- | --- | ------------------- | --- | ------------ |
RemovingthesourceIPaddress198.51.100.1:
| switch(config)# | no  | bfd echo-src-ip-address |              | 198.51.100.1 |
| --------------- | --- | ----------------------- | ------------ | ------------ |
| Command History |     |                         |              |              |
| Release         |     |                         | Modification |              |
| 10.07orearlier  |     |                         | --           |              |
BFD|39

| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
config
6300except Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |     |
| ----------- | --- | --- | --------------------- | --- |
S3L76A,
S3L77A
6400
8100
8360
8400
bfd min-echo-receive-interval
| bfd min-echo-receive-interval    |     | <INTERVAL> |     |     |
| -------------------------------- | --- | ---------- | --- | --- |
| no bfd min-echo-receive-interval |     | <INTERVAL> |     |     |
Description
SetstheminimumtimeintervalbetweenreceivedBFDechopackets.
ThenoformofthiscommandremovestheconfiguredBFDechopacketsinterval.Iftheintervalisnot
set,thedefaultintervalisused.
BFDIPv6Echoisnotsupported.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERVAL> Specifiestheminimumreceptionintervalinmilliseconds.Avalue
of0meansthattheswitchdoesnotsupportreceptionofBFD
echopackets.Range:0,50to1000.Default:500.
Examples
Settingtheminimumreceptionintervalto1000milliseconds:
| switch(config)# | bfd | min-echo-receive-interval |     | 1000 |
| --------------- | --- | ------------------------- | --- | ---- |
Removingtheminimumreceptioninterval:
| switch(config)# | no  | bfd min-echo-receive-interval |     | 1000 |
| --------------- | --- | ----------------------------- | --- | ---- |
Settingtheminimumreceptionintervaltothedefaultvalue:
| switch(config)# | no  | bfd min-echo-receive-interval |              |     |
| --------------- | --- | ----------------------------- | ------------ | --- |
| Command History |     |                               |              |     |
| Release         |     |                               | Modification |     |
| 10.07orearlier  |     |                               | --           |     |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 40

| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
config
6300except Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |     |
| ----------- | --- | --- | --------------------- | --- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
bfd min-receive-interval
| bfd min-receive-interval    |     | <INTERVAL> |     |     |
| --------------------------- | --- | ---------- | --- | --- |
| no bfd min-receive-interval |     | <INTERVAL> |     |     |
Description
SetstheminimumtimeintervalbetweenreceivedBFDcontrolpacketsonaninterface.
ThenoformofthiscommandremovestheconfiguredBFDminimumintervalonaninterface.Ifthe
intervalisnotset,thedefaultintervalisused.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERVAL> Specifiestheminimumreceiveintervalinmilliseconds.Avalueof
0meansthattheswitchdoesnotsupportreceptionofBFD
controlpackets.Range:500to20000100to20000.Default:3000.
Examples
Settingtheminimumreceiveintervalto1000milliseconds:
| switch(config-if)# |     | bfd min-receive-interval |     | 1000 |
| ------------------ | --- | ------------------------ | --- | ---- |
Removingtheminimumreceiveinterval:
| switch(config-if)# |     | no bfd min-receive-interval |     | 1000 |
| ------------------ | --- | --------------------------- | --- | ---- |
Settingtheminimumreceiveintervaltothedefaultvalue:
| switch(config-if)# |     | no bfd min-receive-interval |     |     |
| ------------------ | --- | --------------------------- | --- | --- |
| Command History    |     |                             |     |     |
BFD|41

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

config-if

Administrators or local user group members with execution
rights for this command.

6300 except
for S3L75A,
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040

bfd min-transmit-interval
bfd min-transmit-interval <INTERVAL>
no bfd min-transmit-interval <INTERVAL>

Description

Sets the minimum time interval between transmitted BFD control packets on an interface.

The no form of this command removes the configured BFD minimum transmitted interval on an
interface. If the interval is not set, the default interval is used.

Parameter

<INTERVAL>

Usage

Description

Specifies the minimum transmit interval in milliseconds. Range:
500 to 20000 (6300, 6400, 8100, 8360, 8400 Switch Series). 50 to
20000 (8320, 8325/8324H/8325P, 9300/9300S. 10000, 10040).
Default: 3000.

n If the minimum time interval is set between 500 ms and 1000 ms, then bfd detect-multiplier must

be set to at least 3.

n If bfd detect-multiplier is set to 1, then the minimum transmit interval must be set to at least 3000

ms.

n Whenever the minimum time interval is set to a value less than 1000 ms, BFD automatically adjusts

the transmission interval to 1000 ms if any of the following conditions apply:

o The session is operating in asynchronous mode and echo is enabled.

o The session state is in any other state than up.

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

42

AsdescribedinRFC5880,thisbehavioroccursbecauseBFDechoprovidesquickdetectionwhichallows
theBFDasynchronoussessiontoloweritstraffic/resourcerequirements.
BFDIPv6Echoisnotsupported.
Examples
Settingtheminimumtransmitintervalto500ms:
| switch(config-if)# |     | bfd min-transmit-interval |     | 500 |
| ------------------ | --- | ------------------------- | --- | --- |
Removingtheminimumtransmitinterval:
| switch(config-if)# |     | no bfd min-transmit-interval |     | 500 |
| ------------------ | --- | ---------------------------- | --- | --- |
Settingtheminimumtransmitintervaltothedefaultvalue:
| switch(config-if)# |             | no bfd min-transmit-interval |              |     |
| ------------------ | ----------- | ---------------------------- | ------------ | --- |
| Command            | History     |                              |              |     |
| Release            |             |                              | Modification |     |
| 10.07orearlier     |             |                              | --           |     |
| Command            | Information |                              |              |     |
| Platforms          | Command     | context                      | Authority    |     |
6300except config-if Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |     |
| ----------- | --- | --- | --------------------- | --- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| clear     | bfd statistics |                |     |     |
| --------- | -------------- | -------------- | --- | --- |
| clear bfd | statistics     | [session <ID>] |     |     |
Description
ClearsstatisticsforallBFDsessionsorforaspecificBFDsession.
BFD|43

| Parameter    |     |     | Description          |
| ------------ | --- | --- | -------------------- |
| session <ID> |     |     | SpecifiesasessionID. |
Examples
ClearingstatisticsforallBFDsessions:
| switch# clear | bfd statistics |     |     |
| ------------- | -------------- | --- | --- |
ClearingstatisticsforBFDsession1:
| switch# clear       | bfd statistics | session | 1            |
| ------------------- | -------------- | ------- | ------------ |
| Command History     |                |         |              |
| Release             |                |         | Modification |
| 10.07orearlier      |                |         | --           |
| Command Information |                |         |              |
| Platforms           | Command        | context | Authority    |
6300except Manager(#) Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |
| ----------- | --- | --- | --------------------- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| ip ospf bfd |     |     |     |
| ----------- | --- | --- | --- |
ip ospf bfd
| no ip ospf bfd |     |     |     |
| -------------- | --- | --- | --- |
Description
EnablesBFDforOSPFv2onthecurrentinterface.TheinterfacemusthaveOSPFv2enabledonit.This
overridestheglobalsettingsdefinedwiththecommandbfd all-interfaces.
Thenoformofthiscommandsetsthecurrentinterfacetotheglobalsettingsdefinedwiththe
| commandbfd | all-interfaces. |     |     |
| ---------- | --------------- | --- | --- |
Examples
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 44

OntheHPEArubaNetworking6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1 |     |
| ------------------ | --- | --------- | ----- | --- |
| switch(config-if)# |     | ip ospf   | bfd   |     |
DisablingBFDoninterface1/1/1:
| switch(config)#     |         | interface | 1/1/1    |              |
| ------------------- | ------- | --------- | -------- | ------------ |
| switch(config-if)#  |         | no ip     | ospf bfd |              |
| Command History     |         |           |          |              |
| Release             |         |           |          | Modification |
| 10.07orearlier      |         |           |          | --           |
| Command Information |         |           |          |              |
| Platforms           | Command | context   |          | Authority    |
6300except config-if Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     |     | rightsforthiscommand. |
| ----------- | --- | --- | --- | --------------------- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| ip ospf bfd | disable |     |     |     |
| ----------- | ------- | --- | --- | --- |
| ip ospf bfd | disable |     |     |     |
Description
DisablesBFDforOSPFv2onthecurrentinterface.Thisoverridestheglobalsettingsdefinedwiththe
| commandbfd | all-interfaces. |     |     |     |
| ---------- | --------------- | --- | --- | --- |
Examples
OntheHPEArubaNetworking6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDoninterface1/1/1:
BFD|45

| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
|                     |         | ip ospf bfd | disable      |
| ------------------- | ------- | ----------- | ------------ |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
6300except config-if Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |
| ----------- | --- | --- | --------------------- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| ip route bfd |     |     |     |
| ------------ | --- | --- | --- |
ip route <DEST-IPV4-ADDR>/<NETMASK> [<NEXT-HOP-IP-ADDR> | <INTERFACE>] [bfd]
no ip route <DEST-IPV4-ADDR>/<NETMASK> [<NEXT-HOP-IP-ADDR> | <INTERFACE>] [bfd]
Description
EnablesordisablesBFDonthespecifiedstaticroute.TodisableBFD,issuethecommandwithoutthe
bfdoption.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<DEST-IPV4-ADDR> SpecifiesaroutedestinationinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.
<NETMASK> SpecifiesthenumberofbitsintheaddressmaskinCIDRformat
(x),wherexisadecimalnumberfrom0to128.
<NEXT-HOP-IP-ADDR>
SpecifiesthenexthopaddressforreachingthedestinationinIPv4
format(x.x.x.x),wherexisadecimalnumberfrom0to255.
| <INTERFACE> |     |     | Specifiesthenexthopasanoutgoinginterface. |
| ----------- | --- | --- | ----------------------------------------- |
bfd
EnablesBFDonthestaticroute.Omitthisparametertodisable
BFD.
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 46

Examples
OntheHPEArubaNetworking6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDonastaticroute:
| switch(config)#    |     | interface   | 1/1/1       |              |
| ------------------ | --- | ----------- | ----------- | ------------ |
| switch(config-if)# |     | ip address  | 20.1.1.2/24 |              |
| switch(config-if)# |     | no shutdown |             |              |
| switch(config-if)# |     | routing     |             |              |
| switch(config-if)# |     | exit        |             |              |
| switch(config)#    |     | ip route    | 192.0.0.0/8 | 20.1.1.1 bfd |
DisablingBFDonastaticroute:
| switch(config)#     |         | ip route | 192.0.0.0/8 | 20.1.1.1     |
| ------------------- | ------- | -------- | ----------- | ------------ |
| Command History     |         |          |             |              |
| Release             |         |          |             | Modification |
| 10.07orearlier      |         |          |             | --           |
| Command Information |         |          |             |              |
| Platforms           | Command | context  |             | Authority    |
6300except config Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     |     | rightsforthiscommand. |
| ----------- | --- | --- | --- | --------------------- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| ipv6 ospfv3    | bfd |     |     |     |
| -------------- | --- | --- | --- | --- |
| ipv6 ospfv3    | bfd |     |     |     |
| no ipv6 ospfv3 | bfd |     |     |     |
Description
EnablesBFDforOSPFv3onthecurrentinterface.TheinterfacemusthaveOSPFv3enabledonit.This
overridestheglobalsettingsdefinedwiththecommandbfd all-interfaces.
Thenoformofthiscommandsetsthecurrentinterfacetotheglobalsettingsdefinedwiththe
| commandbfd | all-interfaces. |     |     |     |
| ---------- | --------------- | --- | --- | --- |
Examples
BFD|47

EnablingBFD:
| switch(config-if)# |     | ipv6 ospfv3 | bfd |
| ------------------ | --- | ----------- | --- |
DisablingBFD:
| switch(config-if)# |     | no ipv6 ospfv3 | bfd |
| ------------------ | --- | -------------- | --- |
EnablingBFDonasubinterface:
switch(config-subif)#
|     |     | ipv6 ospfv3 | bfd |
| --- | --- | ----------- | --- |
DisablingBFDonasubinterface:
| switch(config-subif)# |     | no ipv6 | ospfv3 bfd                                  |
| --------------------- | --- | ------- | ------------------------------------------- |
| Command History       |     |         |                                             |
| Release               |     |         | Modification                                |
| 10.14                 |     |         | Supportaddedforthe9300and9300Sswitchseries. |
10.12.1000 SupportaddedforIPv6neighborsonthe8100,8320,8325,8360,
and10000SwitchSeries.
| 10.07orearlier      |         |         | --        |
| ------------------- | ------- | ------- | --------- |
| Command Information |         |         |           |
| Platforms           | Command | context | Authority |
6300except config-if Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |
| ----------- | --- | --- | --------------------- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| ipv6 ospfv3 | bfd disable |     |     |
| ----------- | ----------- | --- | --- |
| ipv6 ospfv3 | bfd disable |     |     |
Description
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 48

DisablesBFDonthecurrentOSPFv3interface.Thisoverridestheglobalsettingsdefinedwiththe
commandbfdall-interfaces.
Examples
OntheHPEArubaNetworking6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDoninterface1/1/1:
| switch(config)#    |         | interface | 1/1/1       |                                             |         |     |
| ------------------ | ------- | --------- | ----------- | ------------------------------------------- | ------- | --- |
| switch(config-if)# |         |           | routing     |                                             |         |     |
| switch(config-if)# |         |           | ipv6 ospfv3 | bfd                                         | disable |     |
| Command            | History |           |             |                                             |         |     |
| Release            |         |           |             | Modification                                |         |     |
| 10.14              |         |           |             | Supportaddedforthe9300and9300Sswitchseries. |         |     |
10.12.1000 SupportaddedforIPv6neighborsonthe8100,8320,8325,8360,
and10000SwitchSeries.
| 10.07orearlier |             |     |         | --        |     |     |
| -------------- | ----------- | --- | ------- | --------- | --- | --- |
| Command        | Information |     |         |           |     |     |
| Platforms      | Command     |     | context | Authority |     |     |
6300except config-if Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     |     | rightsforthiscommand. |     |     |
| ----------- | --- | --- | --- | --------------------- | --- | --- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| neighbor    | fall-over                        |     | bfd (context: |     | config-router) |     |
| ----------- | -------------------------------- | --- | ------------- | --- | -------------- | --- |
| neighbor    | {<IP-ADDRESS>|<PEER-GROUP-NAME>} |     |               |     | fall-over      | bfd |
| no neighbor | {<IP-ADDRESS>|<PEER-GROUP-NAME>} |     |               |     | fall-over      | bfd |
Description
EnablesBGPtoregisterwithBFDtoreceivefastpeeringsessiondeactivationmessagesfromBFD.
ThenoformofthiscommanddisablesBGPforBFD.
BFD|49

BFDissupportedwithIPv6neighborsonthe6300,6400,8100,8320,8325,8360,8400,9xxxand100xxswitch
series.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.
| <PEER-GROUP-NAME> |     |     | Specifiesapeergroup. |     |
| ----------------- | --- | --- | -------------------- | --- |
Examples
switch(config-router)#
|                        |     | neighbor    | 1.1.1.1 fall-over |     |
| ---------------------- | --- | ----------- | ----------------- | --- |
| switch(config-router)# |     | no neighbor | 1.1.1.1 fall-over | bfd |
| switch(config-router)# |     | neighbor    | PG fall-over      |     |
switch(config-router)#
|                 |     | no neighbor | PG fall-over                                     | bfd |
| --------------- | --- | ----------- | ------------------------------------------------ | --- |
| Command History |     |             |                                                  |     |
| Release         |     |             | Modification                                     |     |
| 10.14           |     |             | Supportaddedforthe9300and9300Sswitchseries.      |     |
| 10.12.1000      |     |             | CommandaddedforIPv6neighborsonthe8100,8320,8325, |     |
8360,and10000SwitchSeries.
| 10.07orearlier      |         |         | --        |     |
| ------------------- | ------- | ------- | --------- | --- |
| Command Information |         |         |           |     |
| Platforms           | Command | context | Authority |     |
6300except config-router Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     | rightsforthiscommand. |     |
| ----------- | --- | --- | --------------------- | --- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| ospfv3-af      | ipv4 bfd |     |     |     |
| -------------- | -------- | --- | --- | --- |
| ospfv3-af ipv4 | bfd      |     |     |     |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 50

| no ospfv3-af | ipv4 bfd |     |     |
| ------------ | -------- | --- | --- |
Description
EnablesBFDforOSPFv3AFonthecurrentinterface.TheinterfacemusthaveOSPFv3AFenabledonit.
ThenoformofthiscommanddisablesBFDonthecurrentinterface.
OSPFv3AFIPv4sessionsareestablishedthroughtheIPv6link-localaddress.Therefore,aBFDsessionisalso
createdfortheIPv6link-localaddresstomonitorthepathandestablishneighborship.
Examples
EnablingBFD:
| switch(config-if)# |     | ospfv3-af | ipv4 bfd |
| ------------------ | --- | --------- | -------- |
DisablingBFD:
| switch(config-if)#  |         | no ospfv3-af | ipv4 bfd           |
| ------------------- | ------- | ------------ | ------------------ |
| Command History     |         |              |                    |
| Release             |         |              | Modification       |
| 10.15               |         |              | Commandintroduced. |
| Command Information |         |              |                    |
| Platforms           | Command | context      | Authority          |
5420 config-if Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6300,except
for S3L75A,
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| ospfv3-af      | ipv6 bfd |     |     |
| -------------- | -------- | --- | --- |
| ospfv3-af ipv6 | bfd      |     |     |
| no ospfv3-af   | ipv6 bfd |     |     |
Description
BFD|51

EnablesBFDforOSPFv3AFonthecurrentinterface.TheinterfacemusthaveOSPFv3AFenabledonit.
ThenoformofthiscommanddisablesBFDonthecurrentinterface.
Examples
EnablingBFD:
| switch(config-if)# |     | ospfv3-af | ipv6 | bfd |     |
| ------------------ | --- | --------- | ---- | --- | --- |
DisablingBFD:
| switch(config-if)#  |         | no ospfv3-af |     | ipv6 bfd           |     |
| ------------------- | ------- | ------------ | --- | ------------------ | --- |
| Command History     |         |              |     |                    |     |
| Release             |         |              |     | Modification       |     |
| 10.15               |         |              |     | Commandintroduced. |     |
| Command Information |         |              |     |                    |     |
| Platforms           | Command | context      |     | Authority          |     |
config-if
| 5420 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- |
| 6200 |     |     |     | rightsforthiscommand.                              |     |
6300,except
for S3L75A,
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
show bfd
| show bfd [session | <ID>] | [all-vrfs |     | | vrf <NAME>] | [vsx-peer] |
| ----------------- | ----- | --------- | --- | ------------- | ---------- |
Description
ShowsinformationforallBFDsessionsorforaspecificBFDsession.
| Parameter    |     |     |     | Description |     |
| ------------ | --- | --- | --- | ----------- | --- |
| session <ID> |     |     |     |             |     |
SessionID.
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 52

| Parameter  |     | Description             |     |     |     |
| ---------- | --- | ----------------------- | --- | --- | --- |
| all-vrfs   |     | AllVRFs.                |     |     |     |
| vrf <NAME> |     | SpecifiesthenameofaVRF. |     |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
PossiblevaluesforStateare:
n Up
n Down
n AdminDown
n Init
| PossiblevaluesforLocal | diagnosticandRemote |     | diagnosticare: |     |     |
| ---------------------- | ------------------- | --- | -------------- | --- | --- |
n Controldetectiontimeexpired(1):ThesessionhasstoppedreceivingBFDcontrolpacketsfromthe
peerafteronedetectiontime.
n Echofunctionfailed:ThesessionhasstoppedreceivingBFDEchopackets,sothesessionwas
declaredDown.
n Neighborsignaledsessiondown:ApacketfromthepeerwasreceivedwitheitherAdminDownor
Downstate.
n Forwardingplanereset:Notsetinthisrelease.
n Pathdown:TheforwardingpathwhenDown.
n Concatenatedpathdown:Notsetinthisrelease.
n Administrativelydown:TheadministratorhasdisabledBFD.
n Reverseconcatenatedpathdown:Notsetinthisrelease.
BFDIPv6Echoisnotsupported.
Examples
ShowinginformationforallBFDsessions:
| switch# show | bfd          |     |     |     |     |
| ------------ | ------------ | --- | --- | --- | --- |
| Admin status | : Enabled    |     |     |     |     |
| Echo source  | IP : 2.2.2.2 |     |     |     |     |
Statistics:
| Total Number      | of Control | Packets Transmitted | : 42 |             |     |
| ----------------- | ---------- | ------------------- | ---- | ----------- | --- |
| Total Number      | of Control | Packets Received    | : 42 |             |     |
| Total Number      | of Control | Packets Dropped     | : 0  |             |     |
| Session Interface | VRF        | Source IP           |      | Destination | IP  |
| Echo              | State      | Application         |      |             |     |
------- --------- --------- ------------------------------- ----------------------
BFD|53

| ---------               | -------- | --------  | ------------            |          |     |        |            |     |
| ----------------------- | -------- | --------- | ----------------------- | -------- | --- | ------ | ---------- | --- |
| 1                       | vlan10   | blue      | 10.10.10.1              |          |     |        | 10.10.10.2 |     |
|                         | disabled | up        | ospf                    |          |     |        |            |     |
| 1                       | vlan10   | blue      | N/A                     |          |     |        | 10.10.10.2 |     |
|                         | disabled | up        | static_routes           |          |     |        |            |     |
| 2                       | vlan40   | red       | 40.10.10.1              |          |     |        | 40.10.10.2 |     |
|                         | disabled | up        | ospf                    |          |     |        |            |     |
| 3                       | vlan30   | red       | 30.10.10.1              |          |     |        | 30.10.10.2 |     |
|                         | disabled | up        | ospf                    |          |     |        |            |     |
| 4                       | vlan20   | blue      | 20.10.10.1              |          |     |        | 20.10.10.2 |     |
|                         | disabled | up        | ospf                    |          |     |        |            |     |
| 5                       | vlan50   | black     | 50.10.10.1              |          |     |        | 50.10.10.2 |     |
|                         | disabled | up        | ospf                    |          |     |        |            |     |
| 6                       | vlan60   | black     | 60.10.10.1              |          |     |        | 60.10.10.2 |     |
|                         | disabled | up        | ospf                    |          |     |        |            |     |
| 7                       | vlan10   | blue      | fe80::409:7380:a62:2400 |          |     |        |            |     |
| fe80::409:7380:a49:a200 |          |           |                         | disabled | up  | ospfv3 |            |     |
| Admin status            | :        | Enabled   |                         |          |     |        |            |     |
| Echo source             | IP       | : 2.2.2.2 |                         |          |     |        |            |     |
Statistics:
| Total Number | of        | Control | Packets     | Transmitted | : 42 |     |             |     |
| ------------ | --------- | ------- | ----------- | ----------- | ---- | --- | ----------- | --- |
| Total Number | of        | Control | Packets     | Received    | : 42 |     |             |     |
| Total Number | of        | Control | Packets     | Dropped     | : 0  |     |             |     |
| Session      | Interface | VRF     | Source      | IP          |      |     | Destination | IP  |
|              | Echo      | State   | Application |             |      |     |             |     |
------- --------- --------- ------------------------------- ----------------------
| ---------               | -------- | -------- | ------------            |          |     |        |            |     |
| ----------------------- | -------- | -------- | ----------------------- | -------- | --- | ------ | ---------- | --- |
| 1                       | vlan10   | blue     | 10.10.10.1              |          |     |        | 10.10.10.2 |     |
|                         | disabled | up       | ospf                    |          |     |        |            |     |
| 1                       | vlan10   | blue     | N/A                     |          |     |        | 10.10.10.2 |     |
|                         | disabled | up       | static_routes           |          |     |        |            |     |
| 2                       | vlan40   | red      | 40.10.10.1              |          |     |        | 40.10.10.2 |     |
|                         | disabled | up       | ospf                    |          |     |        |            |     |
| 3                       | vlan30   | red      | 30.10.10.1              |          |     |        | 30.10.10.2 |     |
|                         | disabled | up       | ospf                    |          |     |        |            |     |
| 4                       | vlan20   | blue     | 20.10.10.1              |          |     |        | 20.10.10.2 |     |
|                         | disabled | up       | ospf                    |          |     |        |            |     |
| 5                       | vlan50   | black    | 50.10.10.1              |          |     |        | 50.10.10.2 |     |
|                         | disabled | up       | ospf                    |          |     |        |            |     |
| 6                       | vlan60   | black    | 60.10.10.1              |          |     |        | 60.10.10.2 |     |
|                         | disabled | up       | ospf                    |          |     |        |            |     |
| 7                       | vlan10   | blue     | fe80::409:7380:a62:2400 |          |     |        |            |     |
| fe80::409:7380:a49:a200 |          |          |                         | disabled | up  | ospfv3 |            |     |
ShowinginformationforBFDsession1:
| switch#     | show bfd    | session | 1         |     |     |     |     |     |
| ----------- | ----------- | ------- | --------- | --- | --- | --- | --- | --- |
| BFD Session | Information |         | – Session | 1   |     |     |     |     |
VRF: blue
| Min Tx              | Interval      | (msec) | : 10000 |     |     |     |     |     |
| ------------------- | ------------- | ------ | ------- | --- | --- | --- | --- | --- |
| Min Rx              | Interval      | (msec) | : 10000 |     |     |     |     |     |
| Min Echo            | Rx Interval   | (msec) | :       | 700 |     |     |     |     |
| Detect              | Multiplier    | : 3    |         |     |     |     |     |     |
| Application         | : ospf        |        |         |     |     |     |     |     |
| Local Discriminator |               | :      | 1       |     |     |     |     |     |
| Remote              | Discriminator | :      | 1       |     |     |     |     |     |
Echo : Enabled
| Local Diagnostic |             | : no_diagnostic       |     |     |     |     |     |     |
| ---------------- | ----------- | --------------------- | --- | --- | --- | --- | --- | --- |
| Remote           | Diagnostic: | administratively_down |     |     |     |     |     |     |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 54

| State flaps: | 0   |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Interface Source IP Destination IP State Pkt In Pkt Out Pkt Drop
--------- --------------- --------------- ---------- -------- -------- --------
| 1/1/1       | 100.100.100.100 |     | 100.100.100.101 |     |     | Up  |     | 100 | 101 | 0   |
| ----------- | --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| BFD Session | Information     |     | – Session       | 1   |     |     |     |     |     |     |
VRF: blue
| Min Tx              | Interval      | (msec) | : 10000  |     |     |     |     |     |     |     |
| ------------------- | ------------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
| Min Rx              | Interval      | (msec) | : 10000  |     |     |     |     |     |     |     |
| Min Echo            | Rx Interval   |        | (msec) : | 700 |     |     |     |     |     |     |
| Detect              | Multiplier    | : 3    |          |     |     |     |     |     |     |     |
| Application         | : ospf        |        |          |     |     |     |     |     |     |     |
| Local Discriminator |               | :      | 1        |     |     |     |     |     |     |     |
| Remote              | Discriminator |        | : 1      |     |     |     |     |     |     |     |
Echo : Enabled
| Local Diagnostic |             | : no_diagnostic       |     |     |     |     |     |     |     |     |
| ---------------- | ----------- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Remote           | Diagnostic: | administratively_down |     |     |     |     |     |     |     |     |
| State flaps:     | 0           |                       |     |     |     |     |     |     |     |     |
Interface Source IP Destination IP State Pkt In Pkt Out Pkt Drop
--------- --------------- --------------- ---------- -------- -------- --------
| 1/1/1 | 100.100.100.100 |     | 100.100.100.101 |     |     | Up  |     | 100 | 101 | 0   |
| ----- | --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
ShowinginformationforallBFDsessionsrelatedtoaparticularVRFinthesystem:
| switch#       | show bfd | vrf       | blue |     |     |     |     |     |     |     |
| ------------- | -------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| Admin status: | enabled  |           |      |     |     |     |     |     |     |     |
| Echo source   | IP:      | 100.1.1.1 |      |     |     |     |     |     |     |     |
Statistics:
| Total number | of        | control | packets     | transmitted: |     | 2226 |     |     |             |     |
| ------------ | --------- | ------- | ----------- | ------------ | --- | ---- | --- | --- | ----------- | --- |
| Total number | of        | control | packets     | received:    |     | 2222 |     |     |             |     |
| Total number | of        | control | packets     | dropped:     | 0   |      |     |     |             |     |
| Session      | Interface | VRF     | Source      | IP           |     |      |     |     | Destination | IP  |
|              | Echo      | State   | Application |              |     |      |     |     |             |     |
------- --------- --------- ------------------------------- ----------------------
| ---------               | -------- | -------- | ------------            |          |     |     |        |     |            |     |
| ----------------------- | -------- | -------- | ----------------------- | -------- | --- | --- | ------ | --- | ---------- | --- |
| 1                       | vlan10   | blue     | 10.10.10.1              |          |     |     |        |     | 10.10.10.2 |     |
|                         | disabled | up       | ospf                    |          |     |     |        |     |            |     |
| 1                       | vlan10   | blue     | N/A                     |          |     |     |        |     | 10.10.10.2 |     |
|                         | disabled | up       | static_routes           |          |     |     |        |     |            |     |
| 4                       | vlan20   | blue     | 20.10.10.1              |          |     |     |        |     | 20.10.10.2 |     |
|                         | disabled | up       | ospf                    |          |     |     |        |     |            |     |
| 7                       | vlan10   | blue     | fe80::409:7380:a62:2400 |          |     |     |        |     |            |     |
| fe80::409:7380:a49:a200 |          |          |                         | disabled | up  |     | ospfv3 |     |            |     |
ShowingBFD informationwhennoBFDsessionsarepresent:
| switch#      | show bfd |         |                     |          |     |     |     |     |     |     |
| ------------ | -------- | ------- | ------------------- | -------- | --- | --- | --- | --- | --- | --- |
| Operational  | status   | :       | BFD is operational. |          |     |     |     |     |     |     |
| Admin status | :        | Enabled |                     |          |     |     |     |     |     |     |
| Echo source  | IP       | : <IP>  | or <none>           | or <N/A> |     |     |     |     |     |     |
Statistics:
| Total Number | of        | Control | Packets | Transmitted |     | : 0         |     |     |      |       |
| ------------ | --------- | ------- | ------- | ----------- | --- | ----------- | --- | --- | ---- | ----- |
| Total Number | of        | Control | Packets | Received    | :   | 0           |     |     |      |       |
| Total Number | of        | Control | Packets | Dropped     | :   | 0           |     |     |      |       |
| Session      | Interface | VRF     | Source  | IP          |     | Destination |     | IP  | Echo | State |
Protocol
------- --------- --------- -------------- ------------------- ------- --------- -
---------
BFD|55

| No BFD sessions |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ShowinformationwhenBFD isloadedinhardware:
| switch# show | bfd    |         |                     |     |       |     |     |     |
| ------------ | ------ | ------- | ------------------- | --- | ----- | --- | --- | --- |
| Operational  | status | :       | BFD is operational. |     |       |     |     |     |
| Admin status | :      | Enabled |                     |     |       |     |     |     |
| Echo source  | IP     | : <IP>  | or <none>           | or  | <N/A> |     |     |     |
Statistics:
| Total Number      | of  | Control | Packets | Transmitted |     | : 0         |         |       |
| ----------------- | --- | ------- | ------- | ----------- | --- | ----------- | ------- | ----- |
| Total Number      | of  | Control | Packets | Received    |     | : 0         |         |       |
| Total Number      | of  | Control | Packets | Dropped     |     | : 0         |         |       |
| Session Interface |     | VRF     | Source  |             | IP  | Destination | IP Echo | State |
Protocol
------- --------- --------- -------------- ------------------- ------- --------- -
---------
| No BFD sessions |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ShowinginformationwhenBFD isloadedinhardwarebutadministrativelydisabled:
| switch# show | bfd    |          |                 |     |           |     |     |     |
| ------------ | ------ | -------- | --------------- | --- | --------- | --- | --- | --- |
| Operational  | status | :        | BFD is globally |     | disabled. |     |     |     |
| Admin status | :      | Disabled |                 |     |           |     |     |     |
| Echo source  | IP     | : <IP>   | or <none>       | or  | <N/A>     |     |     |     |
Statistics:
| Total Number      | of  | Control | Packets | Transmitted |     | : 0         |         |       |
| ----------------- | --- | ------- | ------- | ----------- | --- | ----------- | ------- | ----- |
| Total Number      | of  | Control | Packets | Received    |     | : 0         |         |       |
| Total Number      | of  | Control | Packets | Dropped     |     | : 0         |         |       |
| Session Interface |     | VRF     | Source  |             | IP  | Destination | IP Echo | State |
Protocol
------- --------- --------- -------------- ------------------- ------- --------- -
---------
| No BFD sessions     |         |     |         |     |                                              |     |     |     |
| ------------------- | ------- | --- | ------- | --- | -------------------------------------------- | --- | --- | --- |
| Command History     |         |     |         |     |                                              |     |     |     |
| Release             |         |     |         |     | Modification                                 |     |     |     |
| 10.16               |         |     |         |     | Addedoperationalstatusfieldtotheoutput.      |     |     |     |
| 10.16               |         |     |         |     | Commandintroducedon10000SwitchSeries.        |     |     |     |
| 10.16               |         |     |         |     | Commandintroducedon8325Hand8325SwitchSeries. |     |     |     |
| 10.07orearlier      |         |     |         |     | --                                           |     |     |     |
| Command Information |         |     |         |     |                                              |     |     |     |
| Platforms           | Command |     | context |     | Authority                                    |     |     |     |
6300except Manager(#) Administratorsorlocalusergroupmemberswithexecution
| for S3L75A, |     |     |     |     | rightsforthiscommand. |     |     |     |
| ----------- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 56

| Platforms |     | Command | context |     | Authority |     |     |     |
| --------- | --- | ------- | ------- | --- | --------- | --- | --- | --- |
S3L76A,
S3L77A
6400
8100
8320
8325
8325H
8325P
8325S
8325W
8360
8400
9300
9300S
10000
10040
| show     | bfd interface |        |     |     |     |     |     |     |
| -------- | ------------- | ------ | --- | --- | --- | --- | --- | --- |
| show bfd | interface     | <NAME> |     |     |     |     |     |     |
Description
ShowsinformationforallBFDsessionsrelatedtothespecifiedinterface.
| Parameter |        |     |     |     | Description |     |     |     |
| --------- | ------ | --- | --- | --- | ----------- | --- | --- | --- |
| interface | <NAME> |     |     |     |             |     |     |     |
Specifiesaninterface.
BFDIPv6Echoisnotsupported.
Examples
ShowinginformationforallBFDsessionsrelatedtothespecifiedinterface:
| switch#      | show           | bfd         | interface     | vlan10    |     |          |             |     |
| ------------ | -------------- | ----------- | ------------- | --------- | --- | -------- | ----------- | --- |
| BFD          | session        | information |               | - Session | 1   |          |             |     |
| Min          | Tx interval    | (msec):     |               | 3000      |     |          |             |     |
| Min          | Rx interval    | (msec):     |               | 3000      |     |          |             |     |
| Min          | echo Rx        | interval    | (msec):       | 500       |     |          |             |     |
| Detect       | multiplier:    |             | 5             |           |     |          |             |     |
| Application: |                | ospf        |               |           |     |          |             |     |
| Local        | discriminator: |             | 13211         |           |     |          |             |     |
| Remote       | discriminator: |             | 13211         |           |     |          |             |     |
| Echo:        | disabled       |             |               |           |     |          |             |     |
| Local        | diagnostic:    |             | no_diagnostic |           |     |          |             |     |
| Remote       | diagnostic:    |             | no_diagnostic |           |     |          |             |     |
| State        | flaps:         | 0           |               |           |     |          |             |     |
| Interface    |                | Source      | IP            |           |     |          | Destination | IP  |
|              | State          |             | Pkt           | Rx Pkt    | Tx  | Pkt drop |             |     |
--------- --------------------------------------- --------------------------------
| ------- | ------------ |            | -------- |     | -------- | -------- |            |     |
| ------- | ------------ | ---------- | -------- | --- | -------- | -------- | ---------- | --- |
| vlan10  |              | 10.10.10.1 |          |     |          |          | 10.10.10.2 |     |
BFD|57

|     | up  | 453 | 455 |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
===============================================
| BFD          | session information | -             | Session | 1   |          |             |     |
| ------------ | ------------------- | ------------- | ------- | --- | -------- | ----------- | --- |
| Min          | Tx interval (msec): | 3000          |         |     |          |             |     |
| Min          | Rx interval (msec): | 3000          |         |     |          |             |     |
| Min          | echo Rx interval    | (msec):       | 500     |     |          |             |     |
| Detect       | multiplier:         | 5             |         |     |          |             |     |
| Application: | static_routes       |               |         |     |          |             |     |
| Local        | discriminator:      | 13211         |         |     |          |             |     |
| Remote       | discriminator:      | 13211         |         |     |          |             |     |
| Echo:        | disabled            |               |         |     |          |             |     |
| Local        | diagnostic:         | no_diagnostic |         |     |          |             |     |
| Remote       | diagnostic:         | no_diagnostic |         |     |          |             |     |
| State        | flaps: 0            |               |         |     |          |             |     |
| Interface    | Source              | IP            |         |     |          | Destination | IP  |
|              | State               | Pkt Rx        | Pkt     | Tx  | Pkt drop |             |     |
--------- --------------------------------------- --------------------------------
| ------- | ------------ | -------- | -------- |     | -------- |            |     |
| ------- | ------------ | -------- | -------- | --- | -------- | ---------- | --- |
| vlan10  | N/A          |          |          |     |          | 10.10.10.2 |     |
|         | up           | 453      | 455      |     | 0        |            |     |
===============================================
| BFD          | session information | -             | Session | 7   |          |             |     |
| ------------ | ------------------- | ------------- | ------- | --- | -------- | ----------- | --- |
| Min          | Tx interval (msec): | 3000          |         |     |          |             |     |
| Min          | Rx interval (msec): | 3000          |         |     |          |             |     |
| Min          | echo Rx interval    | (msec):       | 500     |     |          |             |     |
| Detect       | multiplier:         | 5             |         |     |          |             |     |
| Application: | ospfv3              |               |         |     |          |             |     |
| Local        | discriminator:      | 1402          |         |     |          |             |     |
| Remote       | discriminator:      | 1402          |         |     |          |             |     |
| Echo:        | disabled            |               |         |     |          |             |     |
| Local        | diagnostic:         | no_diagnostic |         |     |          |             |     |
| Remote       | diagnostic:         | no_diagnostic |         |     |          |             |     |
| State        | flaps: 0            |               |         |     |          |             |     |
| Interface    | Source              | IP            |         |     |          | Destination | IP  |
|              | State               | Pkt Rx        | Pkt     | Tx  | Pkt drop |             |     |
--------- --------------------------------------- --------------------------------
| -------        | ------------            | -------- | -------- |              | -------- |                         |     |
| -------------- | ----------------------- | -------- | -------- | ------------ | -------- | ----------------------- | --- |
| vlan10         | fe80::409:7380:a62:2400 |          |          |              |          | fe80::409:7380:a49:a200 |     |
|                | up                      | 58       | 58       |              | 0        |                         |     |
| Command        | History                 |          |          |              |          |                         |     |
| Release        |                         |          |          | Modification |          |                         |     |
| 10.07orearlier |                         |          |          | --           |          |                         |     |
| Command        | Information             |          |          |              |          |                         |     |
| Platforms      | Command                 | context  |          | Authority    |          |                         |     |
6300 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
| 6400 | (#) |     |     | rightsforthiscommand. |     |     |     |
| ---- | --- | --- | --- | --------------------- | --- | --- | --- |
8100
8320
8325
8325H
8325P
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 58

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8360
8400
9300
9300S
10000
10040
show hsc
show hsc
Description
Displaysconnectioninformationfortheremotecontroller.
Example
Displayingconnectioninformationfortheremotecontroller:
| switch#         | show hsc    |            |               |
| --------------- | ----------- | ---------- | ------------- |
| BFD status      | : Enabled   |            |               |
| Controller      | IP Port     | Connection | Connection    |
| address         |             | status     | state         |
| --------------- | -------     | ---------- | ------------- |
| 192.168.16.17   | 6640        | UP         | ACTIVE        |
| 192.168.16.17   | 6650        | UP         | IDLE          |
| 192.168.16.17   | 6660        | DOWN       | BACKOFF       |
| Command         | History     |            |               |
| Release         |             |            | Modification  |
| 10.07orearlier  |             |            | --            |
| Command         | Information |            |               |
| Platforms       | Command     | context    | Authority     |
6300except Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
for S3L75A, executionrightsforthiscommand.Operatorscanexecutethis
| S3L76A, |     |     | commandfromtheoperatorcontext(>)only. |
| ------- | --- | --- | ------------------------------------- |
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
BFD|59

Chapter 4

ERPS

ERPS

Ethernet Ring Protection Switching (ERPS) is a protocol defined by the International Telecommunication
Union - Telecommunication Standardization Sector (ITU-T) to eliminate loops at Layer 2. Because the
standard number is ITU-T G.8032/Y1344, ERPS is also called G.8032. ERPS defines Ring Auto Protection
Switching (RAPS) Protocol Data Units (PDUs) and protection switching mechanisms.

ERPS supported on the following switches:

n 4100i

n 6300

n 6400

n 8320

n 8325/8325H/8325P

n 8360

n 8400

n 9300/9300S

n 10000

ERPS has two versions:

n ERPSv1 released by ITU-T in June 2008, and

n ERPSv2 released in August 2010.

EPRSv2, fully compatible with ERPSv1, provides the following enhanced functions:

n Multi-ring topologies, such as intersecting rings

n RAPS PDU transmission on non-virtual-channels (NVCs) in sub-rings

n Forced Switch (FS) and Manual Switch (MS)

n Revertive and non-revertive switching

Generally, redundant links are used on an Ethernet switching network such as a ring network to provide
link backup and enhance network reliability. The use of redundant links, however, may result in creating
network loops, causing broadcast storms, and rendering the MAC address table unstable. As a result,
communication quality deteriorates, and communication services may even be interrupted.

Ethernet networks demand faster protection switching. STP does not meet the requirement for fast
convergence.

ERPS, a standard ITU-T protocol, prevent loops on ring networks. It optimizes detection and performs
fast convergence. ERPS allows all ERPS-capable devices on a ring network to communicate.

Benefits of ERPS include:

n Prevents broadcast storms and implements fast traffic switchover on a network where there are

loops.

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

60

n Provides fast convergence and carrier-class reliability.

n Allows all ERPS-capable devices on a ring network to communicate.

Limitations, Conflicts, or Exclusions

n ERPS coexists with STP with the following limitations:

o ERPS control VLANs shall not be part of RPVST.

o Ring ports are excluded from STP operation.

It is not recommended to configure any Spanning Tree interface context-related commands on the

ERPS ring port. Before configuring ring port ensure all Spanning Tree interface context-related

commands are removed from the interface.

o With VSX, STP operates on ISL ports despite being ring ports.

o Only default MSTP instance (CIST) is supported with ERPS.

o ERPS cannot be enabled with more than 252 RPVST instances. This limitation is applicable for all

supported platforms.

n Dynamic VLANs (MVRP) are not supported on ERPS ring ports.

n MCLAG configuration on ERPS ring ports is not supported.

n ERPS and loop protect are not supported on the same port. If enabled together, the behavior is

undefined.

n Active GW is not recommended on VLANs that are not part of VSX-LAGs. This can lead to two active

GWs on a ring when ISL fails as SVIs of those VLANs are not shut down on VSX-secondary. This results
in frequent MAC moves for gateway MAC address across ring nodes.

n On such deployments, where gateways are serving VLANs across the ring, VRRP is recommended.

n Multiple major-rings (MRs) are not supported in a VSX solution since VSX-ISL can be part of a

maximum of one MR.

n Topologies must have either a subring or MCLAG to connect downstream switches and not a mix of

both.

n Square VSX topology cannot be part of single MR since MCLAG is not supported as a ring port.

n On switches with both ERPS and STP enabled, a loop involving ring ports and STP ports is not

protected.

n Redundant links from downstream switches to ring nodes must be VSX-LAGs.

n Do not enable loop-protect, MVRP, and MCLAG on ERPS ring ports. Enabling these features on an

ERPS ring port leads to undefined behavior.

n HA limitations:

o With UDLD, redundancy switchover is not hitless and results in traffic loss.

o UDLD can be used only on ring nodes that are connected through repeaters. This limitation is not
applicable with VSX because UDLD does not have to be enabled on ISL, and LAN traffic can reach
a ring through ISL. This limitation is applicable for VSF switchover.

n Increase the guard interval to 1-2 seconds to prevent Ethernet ring nodes from acting on outdated R-

APS messages and the possibility of forming a closed loop.

n Avoid using vlan trunk allowed all on interconnection link interfaces. Doing so causes looping of
the subring R-APS packet and causes undefined behavior for all rings configured on the switch.

ERPS | 61

n Protected VLANs in a subring that are not part of a major ring are allowed to accommodate guest

VLANs. Clients on those VLANs can only reach the gateway for further routing. These clients cannot
reach other clients on the same VLAN. Such VLANs must have VRRP enabled gateways on both ring
interconnection nodes.

n RPL neighbor configuration on the rings increases convergence time to the order of 300ms across

link failures. Networks critical of convergence time carrying real-time traffic must avoid RPL neighbor
configuration.

n Users must explicitly handle the dynamic change of a port from trunk to access in the following

cases:

o Defaulting a LAG interface that is part of an ERPS ring.

o Swapping or removing an ISL link from a VSX that is part of an ERPS ring.

These cases lead to traffic loss in the ERPS ring, so before performing any of these actions, users
must consider the protocol used on the interface. If it is part of an ERPS ring, configure the port back
to trunk from access.

n Enabling ip neighbor-flood on SVI interfaces is recommended for faster convergence of routed

traffic.

n SNMP is not supported with ERPS.

n VLANs that have ring ports must be included in protected VLAN lists of at least one ERPS instance.

If VLANs with ring ports are not included in protected VLAN lists, the VLAN-port combination is not

managed by ERPS or STP and the port state of the VLAN becomes undefined causing a loop in the

network.

ERPS Commands

clear erps ring <RINGID> instance <ID>
clear erps ring <RINGID> instance <ID>

Description

Removes the protection switching and triggers reversion both in revertive and non-revertive operation.
This command will not change the configured revertive operation mode.

Parameter

<RINGID>

<ID>

Examples

Description

Required, specifies the ID of the ring. Range: 1-239.

Required, specifies the ID of the ring instance. Range: 1-2.

Removes the protection switching and triggers reversion for ring 3, instance 2:

switch# clear erps ring 3 instance 2

Command History

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

62

| Release        |             |         |         | Modification |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- |
| 10.07orearlier |             |         |         | --           |     |
| Command        | Information |         |         |              |     |
| Platforms      |             | Command | context | Authority    |     |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
5420 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | --- | ------------------------------------- | --- |
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| clear erps | statistics |     |             |           |       |
| ---------- | ---------- | --- | ----------- | --------- | ----- |
| clear erps | statistics |     | [ring <ID>] | [instance | <ID>] |
Description
ThiscommandclearstheERPSstatisticsforaringoraringinstance.
| Parameter |     |     |     | Description                                          |     |
| --------- | --- | --- | --- | ---------------------------------------------------- | --- |
| <RINGID>  |     |     |     | Optional,specifiestheIDofthering.Range:1-239.        |     |
| <ID>      |     |     |     | Optional,specifiestheIDoftheringinstance.Range:1-64. |     |
Examples
ClearERPSstatisticsforring1:
| switch# | clear | erps | statistics | ring 1 |     |
| ------- | ----- | ---- | ---------- | ------ | --- |
ClearERPSstatisticsforinstance1ofring1:
| switch#        | clear   | erps | statistics | ring 1       | instance 1 |
| -------------- | ------- | ---- | ---------- | ------------ | ---------- |
| Command        | History |      |            |              |            |
| Release        |         |      |            | Modification |            |
| 10.07orearlier |         |      |            | --           |            |
ERPS|63

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
5420 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
erps ring
| erps ring <RINGID> |          |     |     |
| ------------------ | -------- | --- | --- |
| no erps ring       | <RINGID> |     |     |
Description
ThiscommandcreatesanERPSringwithagivenID.
Thenoformofthiscommandremovesalltheconfigurationsofthering,includinginstances.
| Parameter |     |     | Description                                  |
| --------- | --- | --- | -------------------------------------------- |
| <RINGID>  |     |     | Required,specifiestheIDofthering.Range:1-239 |
Examples
CreateanERPSring:
| switch(config)# | erps | ring | 2   |
| --------------- | ---- | ---- | --- |
switch(config-ring-2)#
RemoveanERPSring:
| switch(config)# | no  | erps ring | 2   |
| --------------- | --- | --------- | --- |
switch(config-ring-2)#
| Command History     |     |     |              |
| ------------------- | --- | --- | ------------ |
| Release             |     |     | Modification |
| 10.07orearlier      |     |     | --           |
| Command Information |     |     |              |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 64

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
4100i config Administratorsorlocalusergroupmemberswithexecution
| 5420 |     |     |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --- | --- | --------------------- | --- |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps | ring          | <RINGID> | <port0|port1> |          |     | interface |
| ---- | ------------- | -------- | ------------- | -------- | --- | --------- |
| erps | ring <RINGID> |          |               |          |     |           |
|      | <port0|port1> |          | interface     | <ifname> |     |           |
Description
ThiscommandconfigurestheERPSringmemberport.AnL2interfaceintheswitchisassociatedtoone
ofthetwomemberportsofanERPSring.Incaseofaninterconnectionnode,onlyport0isapplicable
forthesub-ring.
ThenoformofthiscommandremovestheassociationoftheringporttotheL2interfaceontheswitch.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<RINGID>
Required,specifiestheIDofthering.Range:1-239
| <PORT0> |     |     |     |     | Required,setport0ofthering. |     |
| ------- | --- | --- | --- | --- | --------------------------- | --- |
<PORT1>
Required,setport1ofthering.
| <ifname> |     |     |     |     | Required,interfacename(string). |     |
| -------- | --- | --- | --- | --- | ------------------------------- | --- |
Examples
ConfiguretheERPSringmemberport:
| switch(config)#             |     |     | erps ring | 3     |           |       |
| --------------------------- | --- | --- | --------- | ----- | --------- | ----- |
| switch(config-erps-ring-3)# |     |     |           | port0 | interface | 1/1/1 |
RemovetheassociationoftheringporttotheL2interfaceontheswitch:
| switch(config)#             |         |     | erps ring | 3   |       |     |
| --------------------------- | ------- | --- | --------- | --- | ----- | --- |
| switch(config-erps-ring-3)# |         |     |           | no  | port0 |     |
| Command                     | History |     |           |     |       |     |
ERPS|65

| Release        |             |     | Modification |           |
| -------------- | ----------- | --- | ------------ | --------- |
| 10.07orearlier |             |     | --           |           |
| Command        | Information |     |              |           |
| Platforms      | Command     |     | context      | Authority |
4100i config-erps-ring-<ringid> Administratorsorlocalusergroupmemberswith
| 5420 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring   | <RINGID> |        | description |     |
| ----------- | -------- | ------ | ----------- | --- |
| erps ring   | <RINGID> |        |             |     |
| description |          | <LINE> |             |     |
Description
Thiscommandaddsdescriptiveinformationtohelpadministratorsandoperatorsunderstandthe
purposeofaring.1-64printableASCIIcharactersareallowed.
Thenoformofthiscommandremovestheringinstancedescription.
| Parameter |     |     | Description                                  |     |
| --------- | --- | --- | -------------------------------------------- | --- |
| <RINGID>  |     |     | Required,specifiestheIDofthering.Range:1-239 |     |
<LINE> Required,specifiesthedescriptiontext.Maximumlengthis64
characters.
Examples
Adddescriptiveinformationtoaring:
| switch(config)#            |     | erps | ring 3      |              |
| -------------------------- | --- | ---- | ----------- | ------------ |
| switch(config-erps-ring-3) |     |      | description | HPE RnD ring |
Removedescriptiveinformationfromaring:
| switch(config)#            |     | erps | ring 3         |     |
| -------------------------- | --- | ---- | -------------- | --- |
| switch(config-erps-ring-3) |     |      | no description |     |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 66

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

config-erps-ring-<ringid>

Administrators or local user group members with
execution rights for this command.

4100i
5420
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040

erps ring <RINGID> guard-interval
erps ring <RINGID>

guard-interval <10 milliseconds>

Description

Guard timer is used in nodes recovering from a local failure to avoid loops due to earlier Signal Fail (SF)
messages that may be in the ring.

The configuration specifies the guard timer duration in units of 10 ms. The timer period must be greater
than the maximum expected forwarding delay in which an R-APS message traverses the entire ring. The
default value is 50.

The no form of this command removes the configured value of the guard interval and sets it to the
default value of 50.

Parameter

<RINGID>

<10 milliseconds>

Description

Required, specifies the ID of the ring. Range: 1-239

Required, specifies the guard timer duration in units of 10 ms.
Default: 50.

Examples

Specify the guard timer duration:

ERPS | 67

| switch(config)#             |     | erps | ring | 3              |     |
| --------------------------- | --- | ---- | ---- | -------------- | --- |
| switch(config-erps-ring-3)# |     |      |      | guard-interval | 100 |
Removetheconfiguredvalueoftheguardintervalandsetittothedefaultvalueof50:
| switch(config)#             |             | erps | ring    | 3                 |           |
| --------------------------- | ----------- | ---- | ------- | ----------------- | --------- |
| switch(config-erps-ring-3)# |             |      |         | no guard-interval |           |
| Command                     | History     |      |         |                   |           |
| Release                     |             |      |         | Modification      |           |
| 10.07orearlier              |             |      |         | --                |           |
| Command                     | Information |      |         |                   |           |
| Platforms                   | Command     |      | context |                   | Authority |
4100i config-erps-ring-<ringid> Administratorsorlocalusergroupmemberswith
| 5420 |     |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | --- | ------------------------------ |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring         | <RINGID> |     | hold-off-interval |               |     |
| ----------------- | -------- | --- | ----------------- | ------------- | --- |
| erps ring         | <RINGID> |     |                   |               |     |
| hold-off-interval |          |     | <100              | milliseconds> |     |
Description
Specifieshold-offintervalinunitsof100ms.Ifspecified,adefectisnotreportedimmediately.Instead,
thehold-offtimerisstarted.Onexpirationofthetimer,ifthedefectstillexists,itisreportedto
protectionswitching.Thedefaultvalueforhold-offtimeris0.
Thenoformofthiscommandremovestheconfiguredvalueofthehold-offintervalandsetsittothe
defaultvalueof0.
| Parameter |     |     |     | Description                                  |     |
| --------- | --- | --- | --- | -------------------------------------------- | --- |
| <RINGID>  |     |     |     | Required,specifiestheIDofthering.Range:1-239 |     |
<100 milliseconds> Required,specifiesthehold-offintervalinunitsof100ms.
Default:0.
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 68

Examples
Specifythehold-offinterval:
| switch(config)#             |     | erps | ring | 3                 |     |
| --------------------------- | --- | ---- | ---- | ----------------- | --- |
| switch(config-erps-ring-3)# |     |      |      | hold-off-interval | 100 |
Removetheconfiguredvalueofthehold-offintervalandsetittothedefaultvalueof0:
| switch(config)#             |             | erps | ring    | 3                    |           |
| --------------------------- | ----------- | ---- | ------- | -------------------- | --------- |
| switch(config-erps-ring-3)# |             |      |         | no hold-off-interval |           |
| Command                     | History     |      |         |                      |           |
| Release                     |             |      |         | Modification         |           |
| 10.07orearlier              |             |      |         | --                   |           |
| Command                     | Information |      |         |                      |           |
| Platforms                   | Command     |      | context |                      | Authority |
config-erps-ring-<ringid>
| 4100i |     |     |     |     | Administratorsorlocalusergroupmemberswith |
| ----- | --- | --- | --- | --- | ----------------------------------------- |
| 5420  |     |     |     |     | executionrightsforthiscommand.            |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring | <RINGID> |     | instance |     |     |
| --------- | -------- | --- | -------- | --- | --- |
| erps ring | <RINGID> |     |          |     |     |
instance <ID>
Description
OnacommonERPSnetwork,aphysicalringcanbeconfiguredwithasingleERPSring,andonlyone
blockedportcanbespecifiedinthering.WhentheERPSringisinnormalstate,theblockedport
prohibitsallservicepacketsfrompassingthrough.Asaresult,allservicedataistransmittedthrough
onepathovertheERPSring,andtheotherlinkontheblockedportbecomesidle,leadingtoineffective
useofbandwidth.
Toimprovelinkuseefficiency,logicalringscanbeconfiguredinthesamephysicalringintheERPS
multi-instance.AportmayhavedifferentrolesindifferentERPSringsanddifferentERPSringsuse
differentcontrolVLANs.
ERPS|69

AnERPSringmustbeconfiguredwithanERPinstance,andeachERPinstancespecifiesarangeof
VLANs.ThetopologycalculatedforaspecificERPSringonlytakeseffectintheERPSring.Different
VLANscanuseseparatepaths,implementingtrafficloadbalancingandlinkbackup.
Thenoformofthiscommandremovestheinstanceofthering.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<RINGID>
Required,specifiestheIDofthering.Range:1-239
<ID> Required,specifiestheERPSringinstanceidentifier.Range:1-2.
Examples
Createaringinstance:
| switch(config)#        |     |     | erps ring | 3        |     |     |
| ---------------------- | --- | --- | --------- | -------- | --- | --- |
| switch(config-ring-3)# |     |     |           | instance | 2   |     |
Removearinginstance:
| switch(config)#        |             |         | erps ring | 3           |              |           |
| ---------------------- | ----------- | ------- | --------- | ----------- | ------------ | --------- |
| switch(config-ring-3)# |             |         |           | no instance | 2            |           |
| Command                | History     |         |           |             |              |           |
| Release                |             |         |           |             | Modification |           |
| 10.07orearlier         |             |         |           |             | --           |           |
| Command                | Information |         |           |             |              |           |
| Platforms              |             | Command | context   |             |              | Authority |
4100i config-erps-ring-<ringid> Administratorsorlocalusergroupmemberswith
| 5420 |     |     |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | --- | --- | ------------------------------ |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps | ring          | <RINGID> | instance     |     | <ID>  | control-vlan |
| ---- | ------------- | -------- | ------------ | --- | ----- | ------------ |
| erps | ring <RINGID> |          |              |     |       |              |
|      | instance      | <ID>     | control-vlan |     | <VID> |              |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 70

Description
Thiscommandaddsacontrol-channelVLANtoaringinstance.InanERPSring,thecontrolVLANshould
beusedonlytoforwardRAPSPDUsandnotservicepackets.AllthedevicesinanERPSringinstance
mustbeconfiguredwiththesamecontrolVLAN,anddifferentERPSringinstancesmustusedifferent
controlVLANs.
Thenoformofthiscommandremovesthecontrol-channelVLANoftheringinstance.
| Parameter |     |     | Description                                  |     |
| --------- | --- | --- | -------------------------------------------- | --- |
| <RINGID>  |     |     | Required,specifiestheIDofthering.Range:1-239 |     |
<ID> Required,specifiestheERPSringinstanceidentifier.Range:1-2.
| <VID> |     |     | Required,VLANID.Range:1-4094. |     |
| ----- | --- | --- | ----------------------------- | --- |
Examples
Addacontrol-channelVLANtoaringinstance:
| switch(config)#                   | erps | ring 3   |              |     |
| --------------------------------- | ---- | -------- | ------------ | --- |
| switch(config-erps-ring-3)#       |      | instance | 2            |     |
| switch(config-erps-ring-3-inst-2) |      |          | control-vlan | 10  |
Removethecontrol-channelVLANoftheringinstance:
| switch(config)#                   | erps    | ring 3   |                 |     |
| --------------------------------- | ------- | -------- | --------------- | --- |
| switch(config-erps-ring-3)#       |         | instance | 2               |     |
| switch(config-erps-ring-3-inst-2) |         |          | no control-vlan |     |
| Command History                   |         |          |                 |     |
| Release                           |         |          | Modification    |     |
| 10.07orearlier                    |         |          | --              |     |
| Command Information               |         |          |                 |     |
| Platforms                         | Command | context  | Authority       |     |
4100i config-erps-ring-<ringid> Administratorsorlocalusergroupmemberswith
| 5420 |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | ------------------------------ | --- |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
ERPS|71

| Platforms |     | Command | context |     |     | Authority |
| --------- | --- | ------- | ------- | --- | --- | --------- |
9300S
10000
10040
| erps | ring          | <RINGID> | instance    |     | <ID>   | description |
| ---- | ------------- | -------- | ----------- | --- | ------ | ----------- |
| erps | ring <RINGID> |          |             |     |        |             |
|      | instance      | <ID>     | description |     | <LINE> |             |
Description
Thiscommandaddsdescriptiveinformationtohelpadministratorsandoperatorsunderstandthe
purposeofaringinstance.1-64printableASCIIcharactersareallowed.
Thenoformofthiscommandremovestheringinstancedescription.
| Command   | context |     |     |     |                                              |     |
| --------- | ------- | --- | --- | --- | -------------------------------------------- | --- |
| Parameter |         |     |     |     | Description                                  |     |
| <RINGID>  |         |     |     |     | Required,specifiestheIDofthering.Range:1-239 |     |
<ID> Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<LINE> Required,descriptiveinformationabouttheringinstance.1-64
printableASCIIcharactersallowed.
Examples
Addringinstancedescription:
| switch(config)#                   |     |     | erps ring | 3        |             |                  |
| --------------------------------- | --- | --- | --------- | -------- | ----------- | ---------------- |
| switch(config-erps-ring-3)#       |     |     |           | instance | 2           |                  |
| switch(config-erps-ring-3-inst-2) |     |     |           |          | description | HPE RnD DataVlan |
Removeringinstancedescription:
| switch(config)#                   |             |     | erps ring | 3        |                |     |
| --------------------------------- | ----------- | --- | --------- | -------- | -------------- | --- |
| switch(config-erps-ring-3)#       |             |     |           | instance | 2              |     |
| switch(config-erps-ring-3-inst-2) |             |     |           |          | no description |     |
| Command                           | History     |     |           |          |                |     |
| Release                           |             |     |           |          | Modification   |     |
| 10.07orearlier                    |             |     |           |          | --             |     |
| Command                           | Information |     |           |          |                |     |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 72

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
4100i config-erps-ring-<ringid> Administratorsorlocalusergroupmemberswith
| 5420 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring | <RINGID> | instance | <ID> | enable |
| --------- | -------- | -------- | ---- | ------ |
| erps ring | <RINGID> |          |      |        |
| instance  | <ID>     | enable   |      |        |
Description
Thisconfigurationenablesprotectionswitchingonthegiveninstanceofthering.Itisdisabledby
default.
Thenoformofthiscommanddisablesprotectionswitchingonthegiveninstanceofthering.
| Parameter |     |     | Description                                  |     |
| --------- | --- | --- | -------------------------------------------- | --- |
| <RINGID>  |     |     | Required,specifiestheIDofthering.Range:1-239 |     |
<ID> Required,specifiestheERPSringinstanceidentifier.Range:1-2.
Examples
Enableprotectionswitchingonthegiveninstanceofthering:
| switch(config)#                   | erps | ring 3   |        |     |
| --------------------------------- | ---- | -------- | ------ | --- |
| switch(config-erps-ring-3)#       |      | instance | 2      |     |
| switch(config-erps-ring-3-inst-2) |      |          | enable |     |
Disableprotectionswitchingonthegiveninstanceofthering:
| switch(config)#                   | erps    | ring 3   |              |     |
| --------------------------------- | ------- | -------- | ------------ | --- |
| switch(config-erps-ring-3)#       |         | instance | 2            |     |
| switch(config-erps-ring-3-inst-2) |         |          | no enable    |     |
| Command                           | History |          |              |     |
| Release                           |         |          | Modification |     |
| 10.07orearlier                    |         |          | --           |     |
ERPS|73

| Command   | Information |         |         |     |     |           |     |
| --------- | ----------- | ------- | ------- | --- | --- | --------- | --- |
| Platforms |             | Command | context |     |     | Authority |     |
config-erps-ring-<ringid>
| 4100i |     |     |     |     |     | Administratorsorlocalusergroupmemberswith |     |
| ----- | --- | --- | --- | --- | --- | ----------------------------------------- | --- |
| 5420  |     |     |     |     |     | executionrightsforthiscommand.            |     |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps | ring          | <RINGID> | instance        |     | <ID>       | protected-vlans |     |
| ---- | ------------- | -------- | --------------- | --- | ---------- | --------------- | --- |
| erps | ring <RINGID> |          |                 |     |            |                 |     |
|      | instance      | <ID>     | protected-vlans |     | <VID-LIST> |                 |     |
Description
ThiscommandspecifiesthesetofVLANsthatareprotectedbythisringinstance.
ThenoformofthiscommandremovesasetofVLANsthatareprotectedbythisringinstance.
| Parameter |     |     |     |     |     | Description                                      |     |
| --------- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- |
| <RINGID>  |     |     |     |     |     | Required,specifiestheIDofthering.Range:1-239     |     |
| <ID>      |     |     |     |     |     | Required,specifiestheERPSringinstanceidentifier. |     |
Range:1-2.
|     |     |     |     | <VLAN-ID-LIST> |     | Required,rangeofVLANstobeprotectedbythis |     |
| --- | --- | --- | --- | -------------- | --- | ---------------------------------------- | --- |
ringinstance.Range:1-4094.
NOTE:ThelistofprotectedVLANIDscannotexceed
254characters.
Examples
SpecifyasetofVLANsthatareprotectedbythisringinstance:
| switch(config)#                   |     |     | erps ring | 3        |                 |     |         |
| --------------------------------- | --- | --- | --------- | -------- | --------------- | --- | ------- |
| switch(config-erps-ring-3)#       |     |     |           | instance | 2               |     |         |
| switch(config-erps-ring-3-inst-2) |     |     |           |          | protected-vlans |     | 1,10-50 |
RemoveasetofVLANsthatareprotectedbythisringinstance:
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 74

| switch(config)#                   | erps | ring 3   |                    |       |
| --------------------------------- | ---- | -------- | ------------------ | ----- |
| switch(config-erps-ring-3)#       |      | instance | 2                  |       |
| switch(config-erps-ring-3-inst-2) |      |          | no protected-vlans | 11,13 |
Thefollowingexampleshowsancommandwithinvalidsyntaxbecausethe<VLAN-ID-LIST>string
exceeds254characters.
| switch(config)#             | erps | ring 3   |     |     |
| --------------------------- | ---- | -------- | --- | --- |
| switch(config-erps-ring-3)# |      | instance | 2   |     |
switch(config-erps-ring-3-inst-2) protected-vlans 1,3,6,8-10,16,32,40,46,94,97-
100,103
108,112,120-121,128,136,144,160,176,192,199-200,208,224,228,232,236,240,300-
301,310
313,315,500-507,600-621,699,851,998,1001-1002,1004-1006,1008,1011,1018-1022,1027-
1029,1100
| 1102,1105-1121,1145,1147-1149,2500-2519, |     |     | 2520 |     |
| ---------------------------------------- | --- | --- | ---- | --- |
Configured Protected VLAN string size cannot be more than 254 characters.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
4100i config-erps-ring-<ringid> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
5420
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
erps ring <RINGID> instance <ID> protection-switch {manual|force}
<PORT0>|<PORT1>
erps ring <RINGID> instance <ID> protection-switch {{manual|force} <PORT0>|<PORT1>}
Description
Blocksaspecificringinterfaceinoneofthetwofollowingways:
ERPS|75

n Force:Theswitchblocksaspecificringinterfaceregardlessoftheprotectionswitchingstateofthe
ringinstance.
n Manual:Theswitchblocksaspecificringinterfaceifnootherprotectionswitcheventisactiveonthe
ringinstance.
Theusercanverifywhethertheprotection-switchissuccessfulbyverifyingthestatusofinstanceandportstate
overwhichthiscommandisexecuted.
| switch# | erps ring     | 1 instance | 1 protection-switch |     | force port0 |
| ------- | ------------- | ---------- | ------------------- | --- | ----------- |
| switch# | show erps     | status     |                     |     |             |
| Status  | for ERPS Ring | 1 Instance | 1:                  |     |             |
====================================
| Ring ID        |           |     | : 1                                          |         |     |
| -------------- | --------- | --- | -------------------------------------------- | ------- | --- |
| Instance       | ID        |     | : 1                                          |         |     |
| Port0          |           |     | : 1/1/5                                      | (Block) |     |
| Port1          |           |     | : 1/1/6                                      | (Up)    |     |
| Node Role      | (RPL)     |     | : Owner                                      | (port0) |     |
| Control        | VLAN      |     | : 50                                         |         |     |
| Protected      | VLAN      |     | : 1-49                                       |         |     |
| Subring        | (TCN)     |     | : No (No)                                    |         |     |
| Revertive      | Operation |     | : Revertive                                  |         |     |
| MEG Level      |           |     | : 7                                          |         |     |
| Transmission   | Interval  |     | : 5 sec                                      |         |     |
| Guard Interval |           |     | : 0 sec                                      | 500 ms  |     |
| Hold-Off       | Interval  |     | : 0 sec                                      | 0 ms    |     |
| WTR Interval   |           |     | : 1 min                                      |         |     |
| Status         |           |     | : Forced-switch                              |         |     |
| Oper Down      | Reason    |     | : None                                       |         |     |
| Parameter      |           |     | Description                                  |         |     |
| <RINGID>       |           |     | Required,specifiestheIDofthering.Range:1-239 |         |     |
<ID> Required,specifiestheERPSringinstanceidentifier.Range:1-2.
| manual |     |     | Atypeofprotectionswitcheventinwhichtheswitchblocksa |     |     |
| ------ | --- | --- | --------------------------------------------------- | --- | --- |
specificringinterfaceifnootherprotectionswitcheventisactive
ontheringinstance.
force
Atypeofprotectionswitcheventinwhichtheswitchblocksa
specificringinterfaceregardlessoftheprotectionswitchingstate
oftheringinstance.
Examples
Blockring3,interface2,port0ifnootherprotectionswitcheventisactiveontheringinstance:
| switch# | erps ring | 3 instance | 2 protection-switch |     | manual port0 |
| ------- | --------- | ---------- | ------------------- | --- | ------------ |
Blockring3,instance2,regardlessoftheprotectionswitchingstateoftheringinstance:
| switch# | erps ring | 3 instance | 2 protection-switch |     | force port1 |
| ------- | --------- | ---------- | ------------------- | --- | ----------- |
| Command | History   |            |                     |     |             |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 76

| Release        |             |     |         | Modification |
| -------------- | ----------- | --- | ------- | ------------ |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
5420 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | --- | ------------------------------------- |
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps      | ring <RINGID> |          | instance       | <ID> revertive |
| --------- | ------------- | -------- | -------------- | -------------- |
| erps ring | <RINGID>      | instance | <ID> revertive |                |
Description
ConfiguresthedefaultrevertivemodeofoperationforanERPSring.Inrevertiveoperation,afterthe
conditionscausingprotectionswitchingarecleared,trafficchannelsarerestoredtotherecoveredlink
blockingtheRPL.ThisconfigurationismeaningfulonlyontheRPLnode.
Thenoformofthiscommandconfiguresnon-revertivemodeofoperationforanERPSring.Innon-
revertiveoperation,thetrafficchannelscontinuetousetheRPL,ifithasnotfailed,afterconditions
causingprotectionswitchingarecleared.ThisconfigurationismeaningfulonlyontheRPLnode.
| Parameter |     |     |     | Description                                  |
| --------- | --- | --- | --- | -------------------------------------------- |
| <RINGID>  |     |     |     | Required,specifiestheIDofthering.Range:1-239 |
<ID> Required,specifiestheERPSringinstanceidentifier.Range:1-2.
Examples
ConfiguringthedefaultrevertivemodeofoperationforERPSring3,instance2:
| switch(config)#                    |     | erps | ring 3   |           |
| ---------------------------------- | --- | ---- | -------- | --------- |
| switch(config-erps-ring-3)#        |     |      | instance | 2         |
| switch(config-erps-ring-3-inst-2)# |     |      |          | revertive |
Configuringnon-revertivemodeofoperationforERPSring3,instance2:
ERPS|77

| switch(config)#                    | erps        | ring 3   |              |           |
| ---------------------------------- | ----------- | -------- | ------------ | --------- |
| switch(config-erps-ring-3)#        |             | instance | 2            |           |
| switch(config-erps-ring-3-inst-2)# |             |          | no           | revertive |
| Command                            | History     |          |              |           |
| Release                            |             |          | Modification |           |
| 10.07orearlier                     |             |          | --           |           |
| Command                            | Information |          |              |           |
| Platforms                          | Command     | context  |              | Authority |
4100i config-erps-ring-<ringid> Administratorsorlocalusergroupmemberswith
| 5420 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring | <RINGID> | instance                      | <ID> | role |
| --------- | -------- | ----------------------------- | ---- | ---- |
| erps ring | <RINGID> |                               |      |      |
| instance  | <ID>     | role <RPL-OWNER|RPL-NEIGHBOR> |      |      |
Description
InERPS,thereisacentralnodecalledRPLOwnerNodewhichblocksoneoftheportstoensurethat
thereisnoloopformedfortheEthernettraffic.ThelinkblockedbytheRPLownernodeiscalledthe
RingProtectionLinkorRPL.ThenodeattheotherendoftheRPLisknownasRPLNeighborNode.It
usesR-APScontrolmessagestocoordinatetheactivitiesofswitchingon/offtheRPLlink.
Thiscommandspecifiestheroleofthenodeasownerorneighbor.
Thenoformofthiscommandremovestheconfigurationofthenoderolefromtheinstance.
| Parameter |     |     | Description                                  |     |
| --------- | --- | --- | -------------------------------------------- | --- |
| <RINGID>  |     |     | Required,specifiestheIDofthering.Range:1-239 |     |
<ID> Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<RPL-OWNER> BlockstrafficatoneendoftheRPL.Theblockedendsendsout
periodicR-APS.
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 78

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<RPL-NEIGHBOR> BlockstrafficatoneendoftheRPL.Theblockedenddoesnot
generateperiodicR-APS.
Examples
Specifytheroleofthenodeasowner:
| switch(config)#                   | erps | ring 3   |      |           |
| --------------------------------- | ---- | -------- | ---- | --------- |
| switch(config-erps-ring-3)#       |      | instance | 2    |           |
| switch(config-erps-ring-3-inst-2) |      |          | role | rpl-owner |
Specifytheroleofthenodeasneighbor:
| switch(config)#                   | erps | ring 3   |      |               |
| --------------------------------- | ---- | -------- | ---- | ------------- |
| switch(config-erps-ring-3)#       |      | instance | 3    |               |
| switch(config-erps-ring-3-inst-2) |      |          | role | rpl-neighbour |
Removetheconfigurationofthenoderolefromtheinstance:
| switch(config)#                   | erps        | ring 3   |              |           |
| --------------------------------- | ----------- | -------- | ------------ | --------- |
| switch(config-erps-ring-3)#       |             | instance | 2            |           |
| switch(config-erps-ring-3-inst-2) |             |          | no role      |           |
| Command                           | History     |          |              |           |
| Release                           |             |          | Modification |           |
| 10.07orearlier                    |             |          | --           |           |
| Command                           | Information |          |              |           |
| Platforms                         | Command     | context  |              | Authority |
config-erps-ring-<ringid>
| 4100i |     |     |     | Administratorsorlocalusergroupmemberswith |
| ----- | --- | --- | --- | ----------------------------------------- |
| 5420  |     |     |     | executionrightsforthiscommand.            |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring | <RINGID> | instance | <ID> | rpl |
| --------- | -------- | -------- | ---- | --- |
ERPS|79

erps ring <RINGID>

instance <ID> rpl <port0|port1>

Description

In ERPS, there is a central node called RPL Owner Node which blocks one of the ports to ensure that
there is no loop formed for the Ethernet traffic. The link blocked by the RPL owner node is called the
Ring Protection Link or RPL. The node at the other end of the RPL is known as RPL Neighbor Node. It
uses R-APS control messages to coordinate the activities of switching the RPL link on and off.

This command specifies which of the ERPS ring ports is the RPL.

The no form of this command removes the RPL port configuration from the ERPS ring instance.

Parameter

Description

<RINGID>

<ID>

<PORT0>

<PORT1>

Examples

Required, specifies the ID of the ring. Range: 1-239

Required, specifies the ERPS ring instance identifier. Range: 1-2.

Required, configure port0 to be RPL port in this ERPS ring
instance.

Required, configure port1 to be RPL port in this ERPS ring
instance.

Configure port0 to be RPL port in this ERPS ring instance:

switch(config)# erps ring 3
switch(config-erps-ring-3)# instance 2
switch(config-erps-ring-3-inst-2) role rpl-owner
switch(config-erps-ring-3-inst-2) rpl port0

Configure port1 to be RPL port in this ERPS ring instance:

switch(config)# erps ring 3
switch(config-erps-ring-3)# instance 3
switch(config-erps-ring-3-inst-2) role rpl-neighbour
switch(config-erps-ring-3-inst-2) rpl port1

Remove the RPL port configuration from the ERPS ring Instance:

switch(config)# erps ring 3
switch(config-erps-ring-3)# instance 2
switch(config-erps-ring-3-inst-2) no rpl port0

Command History

Release

10.07 or earlier

Command Information

Modification

--

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

80

| Platforms | Command |     | context |     | Authority |
| --------- | ------- | --- | ------- | --- | --------- |
4100i config-erps-ring-<ringid> Administratorsorlocalusergroupmemberswith
| 5420 |     |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | --- | ------------------------------ |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring | <RINGID> |     | meg-level |     |     |
| --------- | -------- | --- | --------- | --- | --- |
| erps ring | <RINGID> |     |           |     |     |
meg-level <-0-7>
Description
TheR-APSmessagestransmittedbyERPStaketheformofOAMPDUsasdefinedinG.8013.EachOAM
PDUistransmittedataspecifiedlevelknownastheMaintenanceEntityGroup(MEG)level.This
commandconfiguresthelevelwithwhichtheERPSpacketsmustbetransmitted.
ThenoformofthiscommandremovestheconfiguredMEGlevelandsetsittothedefaultvalueof7.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<RINGID>
Required,specifiestheIDofthering.Range:1-239
| <0-7> |     |     |     | Required,specifiesthemeg-level.Range:0-7.Default:7. |     |
| ----- | --- | --- | --- | --------------------------------------------------- | --- |
Examples
Specifythemeg-level:
| switch(config)#             |     | erps | ring | 3         |     |
| --------------------------- | --- | ---- | ---- | --------- | --- |
| switch(config-erps-ring-3)# |     |      |      | meg-level | 4   |
Removetheconfiguredmeg-levelandsetittothedefaultvalueof7:
| switch(config)#             |         | erps | ring | 3            |     |
| --------------------------- | ------- | ---- | ---- | ------------ | --- |
| switch(config-erps-ring-3)# |         |      |      | no meg-level |     |
| Command                     | History |      |      |              |     |
| Release                     |         |      |      | Modification |     |
| 10.07orearlier              |         |      |      | --           |     |
ERPS|81

| Command   | Information |     |         |     |           |
| --------- | ----------- | --- | ------- | --- | --------- |
| Platforms | Command     |     | context |     | Authority |
config-erps-ring-<ringid>
| 4100i |     |     |     |     | Administratorsorlocalusergroupmemberswith |
| ----- | --- | --- | --- | --- | ----------------------------------------- |
| 5420  |     |     |     |     | executionrightsforthiscommand.            |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring   | <RINGID> |          | parent-ring |     |     |
| ----------- | -------- | -------- | ----------- | --- | --- |
| erps ring   | <RINGID> |          |             |     |     |
| parent-ring |          | <RINGID> |             |     |     |
Description
Thiscommandassociatesasub-ringtoaparent-ringandisrequiredforthesub-ringtonotifythe
parent-ringonchangeintopology.
Thenoformofthiscommandremovestheparentringidentifier.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<RINGID>
Required,specifiestheIDofthering.Range:1-239
| <RINGID> |     |     |     | Required,specifiestheIDoftheparent-ring.Range:1-239 |     |
| -------- | --- | --- | --- | --------------------------------------------------- | --- |
Examples
Associateasub-ringtoaparent-ring:
| switch(config)#             |     | erps | ring | 3           |     |
| --------------------------- | --- | ---- | ---- | ----------- | --- |
| switch(config-erps-ring-3)# |     |      |      | parent-ring | 2   |
Removeaparent-ringidentifier:
| switch(config)#             |         | erps | ring | 3              |     |
| --------------------------- | ------- | ---- | ---- | -------------- | --- |
| switch(config-erps-ring-3)# |         |      |      | no parent-ring | 2   |
| Command                     | History |      |      |                |     |
| Release                     |         |      |      | Modification   |     |
| 10.07orearlier              |         |      |      | --             |     |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 82

| Command   | Information |     |         |           |
| --------- | ----------- | --- | ------- | --------- |
| Platforms | Command     |     | context | Authority |
config-erps-ring-<ringid>
| 4100i |     |     |     | Administratorsorlocalusergroupmemberswith |
| ----- | --- | --- | --- | ----------------------------------------- |
| 5420  |     |     |     | executionrightsforthiscommand.            |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring | <RINGID> |     | sub-ring |     |
| --------- | -------- | --- | -------- | --- |
| erps ring | <RINGID> |     |          |     |
sub-ring
Description
Thiscommandistoconfigureasub-ring.Ifnotspecified,theringisamajor-ring.
Thenoformofthiscommandremovesthesub-ringconfigurationoftheringandconfiguresittobea
major-ring.
Parameter Description
<RINGID>
Required,specifiestheIDofthering.Range:1-239
Examples
Configureasub-ring:
| switch(config)#             |     | erps | ring 2   |     |
| --------------------------- | --- | ---- | -------- | --- |
| switch(config-erps-ring-2)# |     |      | sub-ring |     |
Removethesub-ringconfigurationfromring2andconfigureittobeamajor-ring:
| switch(config)#             |         | erps | ring 2      |     |
| --------------------------- | ------- | ---- | ----------- | --- |
| switch(config-erps-ring-2)# |         |      | no sub-ring |     |
| Command                     | History |      |             |     |
Release Modification
10.07orearlier --
ERPS|83

| Command   | Information |     |         |           |
| --------- | ----------- | --- | ------- | --------- |
| Platforms | Command     |     | context | Authority |
config-erps-ring-<ringid>
| 4100i |     |     |     | Administratorsorlocalusergroupmemberswith |
| ----- | --- | --- | --- | ----------------------------------------- |
| 5420  |     |     |     | executionrightsforthiscommand.            |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring | <RINGID> |     | tcn-propogation |     |
| --------- | -------- | --- | --------------- | --- |
| erps ring | <RINGID> |     |                 |     |
tcn-propogation
Description
Thiscommandistoconfigureasub-ringinterconnectionnodetopassatopologychangenotificationto
theringinstancefortheparentringwheneverthetopologyofthesub-ringchanges.Theparentring
instanceperformsaForwardingDatabase(FDB)flushandsendsaprotocolmessagetoensurethat
othernodesontheparentringalsoperformanFDBflush.
Thenoformofthiscommanddisablestopologychangenotifications.
Parameter Description
<RINGID> Required,specifiestheIDofthering.Range:1-239
<RINGID>
Required,specifiestheIDofthering.Range:1-239
Examples
Configuretopologychangenotifications:
| switch(config)#             |     | erps | ring 2          |     |
| --------------------------- | --- | ---- | --------------- | --- |
| switch(config-erps-ring-2)# |     |      | tcn-propogation |     |
Disabletopologychangenotifications:
| switch(config)#             |         | erps | ring 2             |     |
| --------------------------- | ------- | ---- | ------------------ | --- |
| switch(config-erps-ring-2)# |         |      | no tcn-propogation |     |
| Command                     | History |      |                    |     |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 84

Release Modification
10.07orearlier --
| Command   | Information |         |           |     |
| --------- | ----------- | ------- | --------- | --- |
| Platforms | Command     | context | Authority |     |
4100i config-erps-ring-<ringid> Administratorsorlocalusergroupmemberswith
| 5420 |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | ------------------------------ | --- |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring             | <RINGID> | transmission-interval |     |     |
| --------------------- | -------- | --------------------- | --- | --- |
| erps ring             | <RINGID> |                       |     |     |
| transmission-interval |          | <SECONDS>             |     |     |
Description
SpecifiestheR-APSperiodictransmissionintervalinunitsofseconds.Defaultis5seconds.
Thenoformofthiscommandremovestheconfiguredvalueofthetransmissionintervalandsetsitto
thedefaultvalueof5seconds.
Parameter Description
<RINGID> Required,specifiestheIDofthering.Range:1-239
<SECONDS> Required,specifiestheR-APSperiodictransmissionintervalin
unitsofseconds.Range:5seconds.
Examples
SpecifytheR-APSperiodictransmissionintervalas10seconds:
| switch(config)#             | erps | ring 3                |     |     |
| --------------------------- | ---- | --------------------- | --- | --- |
| switch(config-erps-ring-3)# |      | transmission-interval |     | 10  |
Removetheconfiguredvalueofthetransmissionintervalandsetittothedefaultvalueof5seconds:
| switch(config)#             | erps | ring 3                   |     |     |
| --------------------------- | ---- | ------------------------ | --- | --- |
| switch(config-erps-ring-3)# |      | no transmission-interval |     |     |
ERPS|85

| Command | History |     |     |
| ------- | ------- | --- | --- |
Release Modification
10.07orearlier --
| Command   | Information |         |           |
| --------- | ----------- | ------- | --------- |
| Platforms | Command     | context | Authority |
4100i config-erps-ring-<ringid> Administratorsorlocalusergroupmemberswith
| 5420 |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | ------------------------------ |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| erps ring    | <RINGID>  | wtr-interval |     |
| ------------ | --------- | ------------ | --- |
| erps ring    | <RINGID>  |              |     |
| wtr-interval | <MINUTES> |              |     |
Description
TheRPLownernodeusesadelaytimerbeforeinitiatinganRPLblockincaseofbothrevertivemodeof
operationorbeforerevertingtoidlestateafterclearingoperatorcommands(FS,MS).
TheWaittoRestore(WTR)timercanbeconfiguredin1-minuteincrementsupto12minutes.The
defaultvalueis5minutes.WhenrecoveringfromanSF,thedelaytimermustbelongenoughtoallow
therecoveringnetworktobecomestable.Inthedefaultrevertivemodeofoperation,theWTRtimeris
usedtopreventfrequentoperationofprotectionswitchingduetointermittentSFdefects.
Thenoformofthiscommandremovestheconfiguredvalueofthewtr-intervalandsetsittothedefault
valueof5minutes.
| Parameter |     |           | Description                                         |
| --------- | --- | --------- | --------------------------------------------------- |
| <RINGID>  |     |           | Required,specifiestheIDofthering.Range:1-239        |
|           |     | <MINUTES> | Required,specifiesthewtr-intervalinminutes.Range:1- |
12.Default:5.
Examples
Specifythewtr-interval:
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 86

| switch(config)#             | erps | ring | 3            |     |
| --------------------------- | ---- | ---- | ------------ | --- |
| switch(config-erps-ring-3)# |      |      | wtr-interval | 7   |
Removetheconfiguredvalueofthewtr-intervalandsetittothedefaultvalueof5minutes:
| switch(config)#             | erps    | ring    | 3               |           |
| --------------------------- | ------- | ------- | --------------- | --------- |
| switch(config-erps-ring-3)# |         |         | no wtr-interval |           |
| Command History             |         |         |                 |           |
| Release                     |         |         | Modification    |           |
| 10.07orearlier              |         |         | --              |           |
| Command Information         |         |         |                 |           |
| Platforms                   | Command | context |                 | Authority |
4100i config-erps-ring-<ringid> Administratorsorlocalusergroupmemberswith
| 5420 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6200
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| show erps | statistics |     |     |     |
| --------- | ---------- | --- | --- | --- |
show erps statistics [ring <RINGID>] [instance <ID> [<PORT0>|<PORT1>]]
Description
ThiscommanddisplaysERPSstatistics.Thestatisticscanbedisplayedforthering,theinstance,orthe
instanceports.
| Parameter |     |     | Description                                   |     |
| --------- | --- | --- | --------------------------------------------- | --- |
| <RINGID>  |     |     | Optional,specifiestheIDofthering.Range:1-239. |     |
<ID>
Optional,specifiestheIDoftheringinstance.Range:1-2.
| <PORT0> |     |     | Optional,specifiestheringmemberport0. |     |
| ------- | --- | --- | ------------------------------------- | --- |
<PORT1>
Optional,specifiestheringmemberport1.
ERPS|87

Examples
| switch#    | show | erps statistics |        | ring     | 1   |     |
| ---------- | ---- | --------------- | ------ | -------- | --- | --- |
| Statistics | for  | ERPS            | ring 1 | instance |     | 1:  |
======================================
|                |     | Port0        |        |          |     | Port1        |
| -------------- | --- | ------------ | ------ | -------- | --- | ------------ |
|                |     | -----        |        |          |     | -----        |
| Local Failures |     | 4            |        |          |     | 1            |
| R-APS          |     | Port0(Tx/Rx) |        |          |     | Port1(Tx/Rx) |
| -----          |     | ------------ |        |          |     | ------------ |
| NR             |     | 1/1          |        |          |     | 1/1          |
| NR,RB          |     | 0/1          |        |          |     | 0/1          |
| SF             |     | 1/0          |        |          |     | 1/0          |
| MS             |     | 0/0          |        |          |     | 0/10         |
| FS             |     | 30/0         |        |          |     | 0/0          |
| Statistics     | for | ERPS         | ring 1 | instance |     | 2:           |
======================================
|                |      | Port0        |            |          |     | Port1        |
| -------------- | ---- | ------------ | ---------- | -------- | --- | ------------ |
|                |      | -----        |            |          |     | -----        |
| Local Failures |      | 4            |            |          |     | 1            |
| R-APS          |      | Port0(Tx/Rx) |            |          |     | Port1(Tx/Rx) |
| -----          |      | ------------ |            |          |     | ------------ |
| NR             |      | 1/1          |            |          |     | 1/1          |
| NR,RB          |      | 0/1          |            |          |     | 0/1          |
| SF             |      | 1/0          |            |          |     | 1/0          |
| MS             |      | 0/0          |            |          |     | 0/10         |
| FS             |      | 30/0         |            |          |     | 0/0          |
| switch#        | show | erps         | statistics |          |     |              |
| Statistics     | for  | ERPS         | Ring 1     | Instance |     | 1 :          |
==========================================
|                |             | Port0        |         |     |              | Port1        |
| -------------- | ----------- | ------------ | ------- | --- | ------------ | ------------ |
|                |             | -----        |         |     |              | -----        |
| Local Failures |             | 4            |         |     |              | 1            |
| R-APS          |             | Port0(Tx/Rx) |         |     |              | Port1(Tx/Rx) |
| -------        |             | ----------   |         |     |              | -----------  |
| NR             |             | 33/9         |         |     |              | 33/9         |
| NR,RB          |             | 58/0         |         |     |              | 58/0         |
| SF             |             | 4/0          |         |     |              | 4/0          |
| MS             |             | 0/0          |         |     |              | 0/0          |
| FS             |             | 0/0          |         |     |              | 0/0          |
| Command        | History     |              |         |     |              |              |
| Release        |             |              |         |     | Modification |              |
| 10.07orearlier |             |              |         |     | --           |              |
| Command        | Information |              |         |     |              |              |
| Platforms      | Command     |              | context |     | Authority    |              |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 5420 |     |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
(#)
commandfromtheoperatorcontext(>)only.
6200
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 88

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| show      | erps status |                 |           |       |
| --------- | ----------- | --------------- | --------- | ----- |
| show erps | status      | [ring <RINGID>] | [instance | <ID>] |
Description
Thiscommanddisplaysdetailedinformationaboutaspecificringorallinstancesofaring.
Theringinstancemaybeinoneofthefollowingstates:
n Idle:Theringinstanceisoperational.
n Initializing:Theringinstanceisnotoperational.
n Protection:Protectionswitchinghasbeentriggeredbyalocalorremotelinkfailure.
n Pending:Pendingclearanceofapreviousprotectionswitch.
Down:Ringinstanceisnotactive.
n
n Manual-switch:ManualprotectionswitchingtriggeredbyAdmin-down.
n Force-switch:Forcedprotectionswitchingtriggeredbyadmin.
Aringinstancehasthefollowingreasonsfor"down"state:
n Disabled:Ringinstanceisadministrativelydisabled.
n Inconsistent Port Config:Thesameportisconfiguredasport0andport1orRPLportisconfigured
byAdmin-down.
| n Incomplete | Port     | Config:Onlyoneornoringportisconfigured.  |     |     |
| ------------ | -------- | ---------------------------------------- | --- | --- |
| n Protected  | VLANs    | Not Configured:ProtectedVLANlistisempty. |     |     |
| n Control    | VLAN Not | Configured:ControlVLANisnotconfigured.   |     |     |
Theringportscanbeinoneofthefollowingstates:
n Up:Portforwardscontrolanddatatraffic.
n Blocked:Portblocksbothcontrolanddatatraffic.
| Parameter |     |     | Description                                         |     |
| --------- | --- | --- | --------------------------------------------------- | --- |
| <RINGID>  |     |     | Optional,specifiestheIDofthering.Range:1-239.       |     |
| <ID>      |     |     | Optional,specifiestheIDoftheringinstance.Range:1-2. |     |
Examples
ERPS|89

ShowERPSstatusforring1andinstance1:
| Status | for ERPS Ring | 1 Instance | 1   |     |     |
| ------ | ------------- | ---------- | --- | --- | --- |
=================================
| Ring ID          |             |     | : 1               |           |            |
| ---------------- | ----------- | --- | ----------------- | --------- | ---------- |
| Ring description |             |     | : ring_1          |           |            |
| Instance         | ID          |     | : 1               |           |            |
| Instance         | description |     | : inst_1          |           |            |
| Port0            |             |     | : 1/0/1 (Blocked) |           |            |
| Port1            |             |     | : 1/0/2 (Up)      |           |            |
| Node Role        | (RPL)       |     | : Owner (Port0)   |           |            |
| Control          | VLAN        |     | : 100             |           |            |
| Protected        | VLAN        |     | : None            |           |            |
| Subring          | (TCN)       |     | : Yes (Yes)       |           |            |
| Revertive        | Operation   |     | : Revertive       |           |            |
| MEG Level        |             |     | : 1               |           |            |
| Transmission     | Interval    |     | : 5 sec           |           |            |
| Guard Interval   |             |     | : 500 ms          |           |            |
| Hold-Off         | Interval    |     | : 1 sec           |           |            |
| WTR Interval     |             |     | : 5 min           |           |            |
| Status           |             |     | : Initializing    |           |            |
| Oper Down        | Reason      |     | : Protected       | Vlans Not | Configured |
ShowERPSstatusforring1:
| switch# | show erps     | status ring | 1   |     |     |
| ------- | ------------- | ----------- | --- | --- | --- |
| Status  | for ERPS Ring | 1 Instance  | 1   |     |     |
=================================
| Ring ID          |               |            | : 1               |     |     |
| ---------------- | ------------- | ---------- | ----------------- | --- | --- |
| Ring description |               |            | : ring_1          |     |     |
| Instance         | ID            |            | : 1               |     |     |
| Instance         | description   |            | : inst_1          |     |     |
| Port0            |               |            | : 1/0/1 (Blocked) |     |     |
| Port1            |               |            | : 1/0/2 (Up)      |     |     |
| Node Role        | (RPL)         |            | : Owner (Port0)   |     |     |
| Control          | VLAN          |            | : 100             |     |     |
| Protected        | VLAN          |            | : 1-10            |     |     |
| Subring          | (TCN)         |            | : Yes (Yes)       |     |     |
| Revertive        | Operation     |            | : Non-Revertive   |     |     |
| MEG Level        |               |            | : 1               |     |     |
| Transmission     | Interval      |            | : 5 sec           |     |     |
| Guard Interval   |               |            | : 500 ms          |     |     |
| Hold-Off         | Interval      |            | : 1 sec           |     |     |
| WTR Interval     |               |            | : 5 min           |     |     |
| Status           |               |            | : Idle            |     |     |
| Oper Down        | Reason        |            | : None            |     |     |
| Status           | for ERPS Ring | 1 Instance | 2                 |     |     |
=================================
| Ring ID          |             |     | : 1               |     |     |
| ---------------- | ----------- | --- | ----------------- | --- | --- |
| Ring description |             |     | : ring_1          |     |     |
| Instance         | ID          |     | : 2               |     |     |
| Instance         | description |     | : inst_2          |     |     |
| Port0            |             |     | : 1/0/3 (Blocked) |     |     |
| Port1            |             |     | : 1/0/4 (Up)      |     |     |
| Node Role        | (RPL)       |     | : Owner (Port0)   |     |     |
| Control          | VLAN        |     | : 110             |     |     |
| Protected        | VLAN        |     | : 20-30           |     |     |
| Subring          | (TCN)       |     | : No              |     |     |
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 90

| Revertive      | Operation   | :       | Revertive    |     |
| -------------- | ----------- | ------- | ------------ | --- |
| MEG Level      |             | :       | 1            |     |
| Transmission   | Interval    | :       | 5 sec        |     |
| Guard Interval |             | :       | 500 ms       |     |
| Hold-Off       | Interval    | :       | 1 sec        |     |
| WTR Interval   |             | :       | 5 min        |     |
| Status         |             | :       | Admin-Down   |     |
| Oper Down      | Reason      | :       | None         |     |
| Command        | History     |         |              |     |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
5420 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | ------------------------------------- | --- |
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| show erps | summary |     |     |     |
| --------- | ------- | --- | --- | --- |
| show erps | summary |     |     |     |
Description
ThiscommanddisplaysasummaryoftheERPSconfigurationandstatefortheERPSringinstances.
Examples
| switch# | show erps summary |     |     |     |
| ------- | ----------------- | --- | --- | --- |
ERPS Summary
============
| Flags: | R - RPL, M - | Major Ring, | S - Sub Ring, | T - TCN Enabled |
| ------ | ------------ | ----------- | ------------- | --------------- |
* - RPL port
| Per-Instance | Summary |     |     |     |
| ------------ | ------- | --- | --- | --- |
====================
ERPS|91

| Ring Instance       | Port0   |         | Port1        | Status        | Flags |
| ------------------- | ------- | ------- | ------------ | ------------- | ----- |
| ---- --------       | -----   |         | -----        | ------        | ----- |
| 1 1                 | 1/1/1   |         | *1/1/2       | Pending       | R,M   |
| 1 2                 | 1/1/1   |         | 1/1/2        | Idle          | M     |
| 2 1                 | *1/1/3  |         | -            | Protection    | R,S,T |
| 2 2                 | 1/1/3   |         | -            | Admin-down    | S,T   |
| 3 1                 | 1/1/4   |         | 1/1/5        | Manual-switch | M     |
| 3 2                 | 1/1/4   |         | 1/1/5        | Force-switch  | M     |
| Command History     |         |         |              |               |       |
| Release             |         |         | Modification |               |       |
| 10.07orearlier      |         |         | --           |               |       |
| Command Information |         |         |              |               |       |
| Platforms           | Command | context | Authority    |               |       |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
5420 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     | commandfromtheoperatorcontext(>)only. |     |     |
| ---- | --- | --- | ------------------------------------- | --- | --- |
6300
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
AOS-CX10.16.xxxxHighAvailabilityGuide|(AllSwitchSeries) 92

Chapter 5

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

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

93

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
SupportandOtherResources|94

(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.16.xxxx High Availability Guide | (All Switch Series)

95