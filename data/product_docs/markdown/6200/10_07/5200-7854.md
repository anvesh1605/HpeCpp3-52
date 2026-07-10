AOS-CX 10.07 High
Availability Guide

Part Number: 5200-7854
Published: April 2021
Edition: 1

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

Acknowledgments

Intel®, Itanium®, Optane™, Pentium®, Xeon®, Intel Inside®, and the Intel Inside logo are trademarks of
Intel Corporation in the U.S. and other countries.

Microsoft® and Windows® are either registered trademarks or trademarks of Microsoft Corporation in the
United States and/or other countries.

Adobe® and Acrobat® are trademarks of Adobe Systems Incorporated.

Java® and Oracle® are registered trademarks of Oracle and/or its affiliates.

UNIX® is a registered trademark of The Open Group.

All third-party marks are property of their respective owners.

| 2

Contents
Contents
| Contents                                   |                                | 3   |
| ------------------------------------------ | ------------------------------ | --- |
| About this                                 | Document                       | 5   |
| ApplicableProducts                         |                                | 5   |
| LatestVersionAvailableOnline               |                                | 5   |
| CommandSyntaxNotationConventions           |                                | 5   |
| AbouttheExamples                           |                                | 6   |
| IdentifyingSwitchPortsandInterfaces        |                                | 6   |
| IdentifyingModularSwitchComponents         |                                | 8   |
| High Availability                          |                                | 9   |
| HighAvailabilityOverview                   |                                | 9   |
| ManagementModuleFailoverOverview           |                                | 10  |
| AAAonSwitcheswithMultipleManagementModules |                                | 12  |
| HighAvailabilityCommands                   |                                | 12  |
|                                            | redundancyswitchover           | 12  |
| BFD                                        |                                | 14  |
| BFDFeatures                                |                                | 14  |
| ConfiguringBFDforanIPv4StaticRoute         |                                | 15  |
| ConfiguringBFDforBGP                       |                                | 16  |
| ConfiguringBFDForOSPFv2                    |                                | 18  |
| ConfiguringBFDForOSPFv3                    |                                | 19  |
| ConfiguringBFDforPIMOverIPv4               |                                | 21  |
| ConfiguringBFDforPIMOverIPv6               |                                | 22  |
| ConfiguringBFDforVRRP                      |                                | 24  |
| BFDCommands                                |                                | 25  |
|                                            | bfd                            | 25  |
|                                            | bfd<IPV4-ADDR>                 | 25  |
|                                            | bfdall-interfaces              | 26  |
|                                            | bfddetect-multiplier           | 27  |
|                                            | bfddisable                     | 27  |
|                                            | bfdenable(Context:config-hsc)  | 28  |
|                                            | bfddisable(Context:config-hsc) | 28  |
|                                            | bfdechodisable                 | 29  |
|                                            | bfdecho-src-ip-address         | 30  |
|                                            | bfdmin-echo-receive-interval   | 30  |
|                                            | bfdmin-receive-interval        | 31  |
|                                            | bfdmin-transmit-interval       | 32  |
|                                            | clearbfdstatistics             | 33  |
|                                            | ipospfbfd                      | 33  |
|                                            | ipospfbfddisable               | 34  |
|                                            | iproutebfd                     | 34  |
|                                            | ipv6ospfv3bfd                  | 35  |
|                                            | ipv6ospfv3bfddisable           | 36  |
|                                            | neighborfall-overbfd           | 37  |
|                                            | showbfd                        | 37  |
|                                            | showbfdinterface               | 39  |
|                                            | showhsc                        | 41  |
3
AOS-CX10.07HighAvailabilityGuide| UserGuide

| ERPS                               |                                             |     | 42  |
| ---------------------------------- | ------------------------------------------- | --- | --- |
| Limitations,Conflicts,orExclusions |                                             |     | 42  |
| ERPSCommands                       |                                             |     | 44  |
|                                    | clearerpsring<ringid>instance<id>           |     | 44  |
|                                    | clearerpsstatistics                         |     | 45  |
|                                    | erpsring                                    |     | 45  |
|                                    | erpsring<ringid><port0|port1>interface      |     | 46  |
|                                    | erpsring<ringid>description                 |     | 47  |
|                                    | erpsring<ringid>guard-interval              |     | 47  |
|                                    | erpsring<ringid>hold-off-interval           |     | 48  |
|                                    | erpsring<ringid>instance                    |     | 49  |
|                                    | erpsring<ringid>instance<id>control-vlan    |     | 50  |
|                                    | erpsring<ringid>instance<id>description     |     | 50  |
|                                    | erpsring<ringid>instance<id>enable          |     | 51  |
|                                    | erpsring<ringid>instance<id>protected-vlans |     | 52  |
erpsring<ringid>instance<id>protection-switch{{manual|force}<port0>|<port1>} 53
|                       | erpsring<ringid>instance<id>revertive |           | 54  |
| --------------------- | ------------------------------------- | --------- | --- |
|                       | erpsring<ringid>instance<id>role      |           | 55  |
|                       | erpsring<ringid>instance<id>rpl       |           | 56  |
|                       | erpsring<ringid>meg-level             |           | 57  |
|                       | erpsring<ringid>parent-ring           |           | 58  |
|                       | erpsring<ringid>sub-ring              |           | 58  |
|                       | erpsring<ringid>tcn-propogation       |           | 59  |
|                       | erpsring<ringid>transmission-interval |           | 60  |
|                       | erpsring<ringid>wtr-interval          |           | 60  |
|                       | showerpsstatistics                    |           | 61  |
|                       | showerpsstatus                        |           | 62  |
|                       | showerpssummary                       |           | 65  |
| Support               | and Other                             | Resources | 66  |
| AccessingArubaSupport |                                       |           | 66  |
| AccessingUpdates      |                                       |           | 66  |
|                       | ArubaSupportPortal                    |           | 66  |
|                       | MyNetworking                          |           | 67  |
| WarrantyInformation   |                                       |           | 67  |
| RegulatoryInformation |                                       |           | 67  |
| DocumentationFeedback |                                       |           | 67  |
Contents|4

Chapter 1

About this Document

About this Document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable Products
This document applies to the following products:

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A)

n Aruba 8400 Switch Series (JL375A, JL376A)

Latest Version Available Online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command Syntax Notation Conventions

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

n example-text

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables are
enclosed in angle brackets (< >). Substitute the text—including the
enclosing angle brackets—with an actual value.

n For output formats where italic text can be displayed, variables might

or might not be enclosed in angle brackets. Substitute the text
including the enclosing angle brackets, if any, with an actual value.

AOS-CX 10.07 High Availability Guide | User Guide

5

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

About the Examples
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

Where <VLAN-ID> is a variable representing the VLAN number.

Identifying Switch Ports and Interfaces

About this Document | 6

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

n slot: Line module number. Always 1.

n port: Physical number of a port on a line module.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

n slot: Line module number. Always 1.

n port: Physical number of a port on a line module.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the 6400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

On the 83xx Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Line module number. Always 1.

n port: Physical number of a port on a line module

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on

physical port 4 in slot 1 on member 1.

On the 8400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/5 and 1/6.

o Line modules are on the front of the switch in slots 1/1 through 1/4, and 1/7 through 1/10.

n port: Physical number of a port on a line module

AOS-CX 10.07 High Availability Guide | User Guide

7

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

Identifying Modular Switch Components

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

High Availability

High Availability

The High Availability (HA) feature has three components:

n Redundant Management

n OVSDB synchronization

n Filesystem replication

High Availability Overview
Key goals of HA include:

n Achieve five-nines (99.999%) availability of switching traffic through minimization of unplanned network

outages.

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

AOS-CX 10.07 High Availability Guide | User Guide

9

o Standby MM configuration

o Software version update

The Active MM controls infrastructure, files, and the database. If the Active MM is removed, all management
passes to the Standby MM.

n Fabric redundancy (fabric cards)

n Network interface redundancy (line cards)

n Power management (power supplies)

n Software redundancy: Software (including daemons) provides redundancy in software by supporting

one or more of the following methods:

o Nonstop switching restart:

l The daemon reads its last known state or the current hardware state from OVSDB.

l The daemon adjusts its internal state to match the last known state.

l There is no traffic interruption and no moment in time where the last known configuration is not

in effect.

l The daemon restarts fast enough to respond to protocols that require peer communication

without timing out.

l Examples include LACP, ACLS, TCAM entries, and MSTP.

o Graceful restart:

l Current state is still read from OVSDB. Traffic follows the rules of this state until the protocol has

fully recovered.

l Connections to other switches are re-established.

l Current state is republished to peers, which can then respond back with adjustments.

l Examples include routing protocols.

o Full state reset:

l Any non-default runtime state the daemon has in hardware or OVSDB is forced back to the default

state.

l Any connections are closed and have to be manually restarted.

l This is primarily for user-facing daemons and features for which the default state does not have a

large impact on traffic.

l Examples include SSH, web server, TFTP, and CLI.

Management Module Failover Overview
There are two types of Management Module (MM) failover:

n Controlled failover: The user triggers this type of failover by rebooting the Active MM or running the

redundancy switchover command.

n Uncontrolled failover: This type of failover is triggered by unexpected events like a crash on the Active

MM or hot removal of the Active MM.

In a dual MM chassis, the Standby MM detects failover events in one of the following ways:

n A mailbox interrupt is received from the Active MM to indicate takeover. This interrupt can come for

controlled or uncontrolled failover (except for a hot removal).

n Active MM hot removal detection.

High Availability | 10

n Heartbeat loss detected on the Standby MM for more than 10 seconds.

If the Active MM is not responding and is still not detected by the first two methods, it will be caught

by this method.

Failover requirements:

n The Standby MM must be present to trigger a failover. An Unassigned MM will never trigger a failover.

n The Redundant Management Daemon (hpe-rdntmgmtd) is responsible for triggering failover from the

Standby MM.

n When a failover is triggered, the Standby MM becomes the Active MM while the previously Active MM is

rebooted.

Standby recovery requirements:

n The Active MM must be present to trigger a recovery.

n The Redundant Management Daemon (hpe-rdntmgmtd) is responsible for triggering recover from the

Active MM.

n When a recovery is triggered, the Active MM reboots the nonresponsive Standby MM. This action occurs

for any of the following conditions:

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

o Detect the recover condition due to heartbeat fail count increasing past the maximum of 7 and

triggering recover.

o Initiate reboot of Standby MM.

n Standby MM will join as a standby after reboot.

Condition: Planned reboot of Active MM:

n A planned reboot on the Active MM will send a failover command to the Standby MM.

n The hpe-rdntmgmtd daemon on the Standby MM will:

o Process this command and perform a failover immediately instead of waiting for the failover monitor

to detect it using heartbeats.

o Initiate reboot of the Active MM.

n Active MM will join as a standby after reboot.

Condition: Removal of Active MM:

AOS-CX 10.07 High Availability Guide | User Guide

11

n Removal of the Active MM from Slot 1 triggers the hpe-rdntmgmtd daemon on the Standby MM to

initiate failover immediately instead of waiting for the failover monitor to detect it using heartbeats.

n Active MM will join as a standby after reboot.

Condition: Crash on Active MM:

n A crash on the Active MM is handled by the crash handler, which sends a failover command to the

Standby MM.

n The hpe-rdntmgmtd daemon on the Standby MM will:

o Process this command and perform failover immediately instead of waiting for the failover monitor

to detect it using heartbeats.

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

AAA on Switches with Multiple Management Modules
Consider the following when working with local authentication, authorization, and accounting (AAA) on
switchers with multiple management modules:

n Local authentication:

o The user database is synchronized between the Active and Standby management modules.

o Only local users belonging to the administrators group and using local password authentication are
permitted to log in to the Standby management module. Alternatively, the Standby management
module can be accessed from the Active management module by providing a logged in admin user
password.

n Local authorization:

o A few nonconfiguration commands are available on the Standby management module.

o For expert users, the bash shell is available on the Standby management module.

n Local accounting:

o The audit logs used for local accounting are available only on the Active Management Module.

High Availability Commands

redundancy switchover

High Availability | 12

Syntax

redundancy switchover

Description

Causes the switch to immediately switch over to the Standby Management Module. This command must be
executed from the Active Management Module and will fail if the Standby Management Module is in a failed
state or not present.

Command context

Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Examples

This example shows the redundancy switchover command on an active management module with a
standby management module that is present.

switch#redundancy switchover
This command causes the switch to immediately switchover to the Standby Management
Module.
Do you want to continue [y/n]?

This example shows the redundancy switchover command on an active management module with a
standby management module that is absent.

switch#redundancy switchover
Standby Management Module not found, switchover request ignored.

This example shows the redundancy switchover command on a standby management module.

switch#redundancy switchover
Redundancy switchover must be performed from the Active Management Module,
switchover request ignored.

AOS-CX 10.07 High Availability Guide | User Guide

13

Chapter 3

BFD

BFD

The BFD feature and thus this entire chapter is not applicable to the 6200 Switch Series.

Bidirectional Forwarding Detection (BFD) provides a general-purpose, standard, medium- and protocol-
independent fast failure detection mechanism. It can detect and monitor the connectivity of links in IP to
detect communication failures quickly. BFD operates independently of media, data protocols, and routing
protocols.

BFD establishes a session between two network devices to detect failures on the bidirectional forwarding
paths between the devices and provide services for upper-layer protocols. BFD provides no neighbor
discovery mechanism. Protocols that BFD services notify BFD of devices to which it needs to establish
sessions. After a session is established, if no BFD control packet is received from the peer within the
negotiated BFD interval, BFD notifies a failure to the protocol, which then takes appropriate measures.

BFD operates in two modes:

n Asynchronous mode: In this mode, an operating device periodically sends BFD control packets to another
device. If the other device does not receive BFD control packet from the peer within the specified interval,
it tears down the BFD session.

n Demand mode: in this mode, it is assumed that an operating device has an independent way of verifying
that it has connectivity to the peer. Once a BFD session is established, one device may request that the
other device stops sending BFD control packets, except when the connection must be explicitly validated,
in which case a short sequence of BFD control packets is exchanged. Demand mode may operate
independently in each direction, or simultaneously.

BFD also has an echo function. When echo is active, an operating device periodically sends BFD echo
packets. The peer device returns the received BFD echo packets back without processing them (it loops
them through its forwarding path). If the sending device does not receive BFD echo packets from the peer
within a specified interval, the session is considered down. Since the echo function is handling the task of
detection, the rate of periodic transmission of control packets may be reduced in asynchronous mode, and
eliminated in demand mode.

BFD Features
BGP, OSPFv2, OSPFv3, PIMv4 and PIMv6, static routes, and VRRP are clients of BFD.

Supported:

n BFD v1

n Asynchronous mode + echo

n IPv6 (8400, 6400 and 6300 switches only)

n Asynchronous mode on IPv6 tunnel interfaces (8400 switches only)

n Asynchronous mode for VxLAN tunnels (8325, 8360 and 8400 switches only)

n Single hop

n IPv4

AOS-CX 10.07 High Availability Guide | User Guide

14

n RoP, SVI, and LAG interfaces

n VSX synchronization. For more information, see the Virtual Switching Extension (VSX) Guide for your

switch and software version.

n Loopbacks are supported for VxLAN sessions (8325, 8360 and 8400 switches only), and static routes

(6300, 6400 and 8400 switches only). Same IP version restrictions apply.

Not supported:

n MIB support

n IPv6 (832x switches only)

n Demand mode

n Micro-BFD

n Authentication

n Echo function on tunnel interfaces

n BFD sessions are not supported on tunnel interfaces (6300, 6400, and 8320 switches only)

n IPv6 BFD sessions are not supported (8320, 8325, and 8360 switches only)

n Echo function for IPv6

n Asynchronous mode on tunnel interfaces (832x switches only)

n Multi-hop configurations. BFD works only for directly connected neighbors. BFD neighbors must be no

more than one IP hop away.

n Passive and virtual link interfaces. Loopbacks are not supported on the 8320, 8325 and 8360 switches

with the exception of VXLAN sessions on 8325 and 8360 switches.

n Exceeding a maximum of 20 BFD sessions with interval values of 300ms. Spurious sessions flaps will

occur when the limit of sessions is exceeded.

n Minimum intervals of 300ms are only compatible with the async_vxlan mode (BFD sessions across

VxLAN) and is not user configurable.

n Setting minimum transmit time interval between 500 ms and 1000 ms, and bfd detect-multiplier less

than 3 might result in spurious flaps.

Configuring BFD for an IPv4 Static Route

Procedure

1. Enable BFD support with the command bfd.

2. Enable BFD on an IPv4 static route with the command ip route bfd.

3. For most deployments, the default values for the following features do not need to be changed. If

your deployment requires different settings, change the default values with the indicated command:

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

500 milliseconds

bfd min-echo-receive-interval

BFD | 15

| BFD setting |     | Default value | Commandtochange | it  |
| ----------- | --- | ------------- | --------------- | --- |
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
| 4. ReviewBFDconfigurationsettingswiththecommandsshow |     |     | bfd. |     |
| ---------------------------------------------------- | --- | --- | ---- | --- |
Example
EnablingBFDonastaticIPv4route.
| switch# config     |             |                      |     |     |
| ------------------ | ----------- | -------------------- | --- | --- |
| switch(config)#    | bfd         |                      |     |     |
| switch# interface  | 1/1/1       |                      |     |     |
| switch(config-if)# | no shutdown |                      |     |     |
| switch(config-if)# | ip address  | 192.168.1.1/24       |     |     |
| switch(config-if)# | exit        |                      |     |     |
| switch(config)#    | ip route    | 10.0.2.0/24 20.0.0.2 | bfd |     |
| Configuring        | BFD for     | BGP                  |     |     |
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. CreateaBGPpeerandinitiateaconnectiontoitwiththecommandneighbor remote-as.
3. EnableBFDonaBGPinterfacewiththecommandneighbor fall-over bfd.
4. Defineanaddressfamilyandactivateitwiththecommandsaddress-familyandneighbor
activate.
5. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
| BFD setting         |     | Default value | Commandtochange       | it  |
| ------------------- | --- | ------------- | --------------------- | --- |
| SetstheBFDdetection |     | 5             | bfd detect-multiplier |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
| 6. ReviewBFDconfigurationsettingswiththecommandsshow |     |     | bfd. |     |
| ---------------------------------------------------- | --- | --- | ---- | --- |
AOS-CX10.07HighAvailabilityGuide|UserGuide 16

Example
EnablingBFDonaBGPinterface.
switch#
config
| switch(config)#                | bfd    |                |            |              |            |          |     |     |
| ------------------------------ | ------ | -------------- | ---------- | ------------ | ---------- | -------- | --- | --- |
| switch(config)#                | router | bgp 100        |            |              |            |          |     |     |
| switch(config-router)#         |        | neighbor       | 10.1.231.2 |              | remote-as  | 100      |     |     |
| switch(config-router)#         |        | neighbor       | 10.1.231.2 |              | fall-over  | bfd      |     |     |
| switch(config-router)#         |        | address-family |            | ipv4-unicast |            |          |     |     |
| switch(config-router-ipv4-uc)# |        |                | neighbor   |              | 10.1.231.2 | activate |     |     |
| switch(config-router-ipv4-uc)# |        |                | exit       |              |            |          |     |     |
| switch(config-router)#         |        | exit           |            |              |            |          |     |     |
| switch(config)#                | exit   |                |            |              |            |          |     |     |
switch#
show ip bgp neighbors
| Codes: ^ Inherited | from | peer-group |     |     |     |     |     |     |
| ------------------ | ---- | ---------- | --- | --- | --- | --- | --- | --- |
VRF : default
| BGP Neighbor        | 9.0.0.1   | (External)    |        |          |                   |            |         |           |
| ------------------- | --------- | ------------- | ------ | -------- | ----------------- | ---------- | ------- | --------- |
| Description         |           | :             |        |          |                   |            |         |           |
| Peer-group          |           | :             |        |          |                   |            |         |           |
| Remote              | Router Id | : 0.0.0.0     |        |          | Local             | Router     | Id      | : (null)  |
| Remote              | AS        | : 100         |        |          | Local             | AS         |         | : 100     |
| Remote              | Port      | : 0           |        |          | Local             | Port       |         | : 0       |
| State               |           | : Idle        |        |          | Admin             | Status     |         | : Up      |
| Conn. Established   |           | : 0           |        |          | Conn.             | Dropped    |         | : 0       |
| Passive             |           | : No          |        |          | Update-Source     |            |         | :         |
| Cfg. Hold           | Time      | : 180         |        |          | Cfg.              | Keep       | Alive   | : 60      |
| Neg. Hold           | Time      | : 0           |        |          | Neg.              | Keep       | Alive   | : 0       |
| Up/Down             | Time      | : 00h:00m:00s |        |          | Alt.              | Local-AS   |         | : 0       |
| Local-AS            | Prepend   | : No          |        |          |                   |            |         |           |
| Fall-over           |           | : No          |        |          | BFD               |            |         | : Enabled |
| Password            |           | :             |        |          |                   |            |         |           |
| Last Err            | Sent      | : No          | Error  |          |                   |            |         |           |
| Last SubErr         | Sent      | : No          | Error  |          |                   |            |         |           |
| Last Err            | Rcvd      | : No          | Error  |          |                   |            |         |           |
| Last SubErr         | Rcvd      | : No          | Error  |          |                   |            |         |           |
| Graceful-Restart    |           | : Enabled     |        |          | Rt.               | Reflect.   | Client: | No        |
| Gr. Restart         | Time      | : 120         |        |          | Gr.               | Stalepath  | Time    | : 150     |
| Max. Prefix         |           | : 0           |        |          | Send              | Community  |         | :         |
| Allow-AS            | in        | : 0           |        |          | Remove            | Private-AS |         | : No      |
| Advt. Interval      |           | : 30          |        |          | TTL               |            |         | : 255     |
| Soft Reconfig       | In        | :             |        |          | Local             | Cluster-ID |         | :         |
| Nexthop-Self        |           | :             |        |          | Default-Originate |            |         | :         |
| Weight              |           | : 0           |        |          |                   |            |         |           |
| TTL Security        | Hops      | : 0           |        |          |                   |            |         |           |
| Routemap            | In        | :             |        |          |                   |            |         |           |
| Routemap            | Out       | :             |        |          |                   |            |         |           |
| Message statistics: |           |               |        |          |                   |            |         |           |
|                     |           | Sent          | Rcvd   |          |                   |            |         |           |
|                     |           | -----         | ------ |          |                   |            |         |           |
| Open                |           | 0             |        | 0        |                   |            |         |           |
| Notification        |           | 0             |        | 0        |                   |            |         |           |
| Updates             |           | 0             |        | 0        |                   |            |         |           |
| Keepalives          |           | 0             |        | 0        |                   |            |         |           |
| Route Refresh       |           | 0             |        | 0        |                   |            |         |           |
| Total               |           | 0             |        | 0        |                   |            |         |           |
| Capability          |           | Advertised    |        | Received |                   |            |         |           |
BFD|17

---------------------------------------------
| Route Refresh |         | No         | No  |     |
| ------------- | ------- | ---------- | --- | --- |
| Graceful      | Restart | No         | No  |     |
| Four Octet    | ASN     | No         | No  |     |
| Configuring   | BFD     | For OSPFv2 |     |     |
Prerequisites
OSPFv2mustbeenabled.
n
n ICMPmustbedisabled.
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. EnableBFDonallOSPFinterfaceswiththecommandbfd all-interfaces,orenableBFDona
| specificinterfacewiththecommandip |     | ospf | bfd. |     |
| --------------------------------- | --- | ---- | ---- | --- |
3. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
| BFD setting         |     | Default value | Commandtochange       | it  |
| ------------------- | --- | ------------- | --------------------- | --- |
| SetstheBFDdetection |     | 5             | bfd detect-multiplier |     |
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
4. ReviewBFDconfigurationsettingswiththecommandsshow bfd.
Examples
ThisexampleshowshowtoenableBFDonallOSPFv2interfaces.
| switch# config  |     |     |     |     |
| --------------- | --- | --- | --- | --- |
| switch(config)# | bfd |     |     |     |
switch(config)#
|                        | router    | ospf 1             |     |     |
| ---------------------- | --------- | ------------------ | --- | --- |
| switch(config-ospf-1)# |           | area 1             |     |     |
| switch(config-ospf-1)# |           | bfd all-interfaces |     |     |
| switch(config-ospf-1)# |           | exit               |     |     |
| switch(config)         | router    | ospf 2             |     |     |
| switch(config-ospf-2)# |           | area 2             |     |     |
| switch(config-ospf-2)# |           | bfd all-interfaces |     |     |
| switch(config-ospf-2)# |           | exit               |     |     |
| switch(config)#        | interface | 1/1/1              |     |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 18

| switch(config-if)# |     | no  | shutdown |     |     |     |     |     |
| ------------------ | --- | --- | -------- | --- | --- | --- | --- | --- |
switch(config-if)#
|                    |      | ip           | address  | 192.168.1.1/24 |     |     |     |     |
| ------------------ | ---- | ------------ | -------- | -------------- | --- | --- | --- | --- |
| switch(config-if)# |      | ip           | ospf     | 1 area         | 1   |     |     |     |
| switch(config-if)# |      | exit         |          |                |     |     |     |     |
| switch(config)#    |      | interface    |          | 1/1/2          |     |     |     |     |
| switch(config-if)# |      | no           | shutdown |                |     |     |     |     |
| switch(config-if)# |      | ip           | address  | 192.168.1.2/24 |     |     |     |     |
| switch(config-if)# |      | ip           | ospf     | 2 area         | 2   |     |     |     |
| switch(config-if)# |      | exit         |          |                |     |     |     |     |
| switch(config)#    |      | exit         |          |                |     |     |     |     |
| switch#            | show | bfd          |          |                |     |     |     |     |
| Admin status       |      | : Enabled    |          |                |     |     |     |     |
| Echo source        |      | IP : 2.2.2.2 |          |                |     |     |     |     |
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
| switch#                | config |           |          |                |     |     |     |     |
| ---------------------- | ------ | --------- | -------- | -------------- | --- | --- | --- | --- |
| switch(config)#        |        | bfd       |          |                |     |     |     |     |
| switch(config)#        |        | router    | ospf     | 1              |     |     |     |     |
| switch(config-ospf-1)# |        |           | area     | 1              |     |     |     |     |
| switch(config-ospf-1)# |        |           | exit     |                |     |     |     |     |
| switch(config)#        |        | interface |          | 1/1/1          |     |     |     |     |
| switch(config-if)#     |        | no        | shutdown |                |     |     |     |     |
| switch(config-if)#     |        | ip        | address  | 192.168.1.1/24 |     |     |     |     |
switch(config-if)#
|                     |               | ip          | ospf   | 1 area  | 1   |     |     |     |
| ------------------- | ------------- | ----------- | ------ | ------- | --- | --- | --- | --- |
| switch(config-if)#  |               | ip          | ospf   | bfd     |     |     |     |     |
| switch(config-if)#  |               | exit        |        |         |     |     |     |     |
| switch(config)#     |               | exit        |        |         |     |     |     |     |
| switch#             | show          | bfd session | 1      |         |     |     |     |     |
| BFD Session         |               | Information | –      | Session | 1   |     |     |     |
| Min Tx              | Interval      | (sec)       | : 10   |         |     |     |     |     |
| Min Rx              | Interval      | (sec)       | : 10   |         |     |     |     |     |
| Min Echo            | Rx            | Interval    | (msec) | : 700   |     |     |     |     |
| Detect              | Multiplier    | : 3         |        |         |     |     |     |     |
| Application         |               | : OSPF      |        |         |     |     |     |     |
| Local Discriminator |               | :           | 1      |         |     |     |     |     |
| Remote              | Discriminator |             | : 1    |         |     |     |     |     |
| Echo :              | Enabled       |             |        |         |     |     |     |     |
| Local Diagnostic    |               | : N/A       |        |         |     |     |     |     |
| Remote              | Diagnostic:   | N/A         |        |         |     |     |     |     |
| Flap count:         |               | 0           |        |         |     |     |     |     |
| Internal            | state:        | Up          |        |         |     |     |     |     |
Interface Source IP Destination IP State Pkt In Pkt Out Pkt Drop
--------- --------------- --------------- ---------- -------- -------- --------
| 1/1/1       | 192.168.1.1 |     |     | 100.100.100.101 |     | Up  | 100 101 | 0   |
| ----------- | ----------- | --- | --- | --------------- | --- | --- | ------- | --- |
| Configuring |             | BFD | For | OSPFv3          |     |     |         |     |
Prerequisites
BFD|19

OSPFv3mustbeenabled.
n
ICMPmustbedisabled.
n
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. EnableBFDonallOSPFinterfaceswiththecommandbfd all-interfaces,orenableBFDona
| specificinterfacewiththecommandipv6 |     |     | ospfv3 | bfd. |     |
| ----------------------------------- | --- | --- | ------ | ---- | --- |
3. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
| BFD setting         |     |     | Default value | Commandtochange       | it  |
| ------------------- | --- | --- | ------------- | --------------------- | --- |
| SetstheBFDdetection |     |     | 5             | bfd detect-multiplier |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
| 4. ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     | bfd. |     |
| ---------------------------------------------------- | --- | --- | --- | ---- | --- |
Examples
ThisexampleshowshowtoenableBFDonanallOSPFv3interfaces.
| switch# config           |           |                    |           |     |     |
| ------------------------ | --------- | ------------------ | --------- | --- | --- |
| switch(config)#          | bfd       |                    |           |     |     |
| switch(config)#          | router    | ospfv3             | 1         |     |     |
| switch(config-ospfv3-1)# |           | area               | 1         |     |     |
| switch(config-ospfv3-1)# |           | router-id          | 1.1.1.1   |     |     |
| switch(config-ospfv3-1)# |           | bfd all-interfaces |           |     |     |
| switch(config-ospfv3-1)# |           | exit               |           |     |     |
| switch(config)           | router    | ospfv3 2           |           |     |     |
| switch(config-ospfv3-2)# |           | area               | 2         |     |     |
| switch(config-ospfv3-2)# |           | router-id          | 1.1.1.2   |     |     |
| switch(config-ospfv3-2)# |           | bfd all-interfaces |           |     |     |
| switch(config-ospfv3-2)# |           | exit               |           |     |     |
| switch(config)#          | interface | 1/1/1              |           |     |     |
| switch(config-if)#       | no        | shutdown           |           |     |     |
| switch(config-if)#       | ipv6      | address            | 100::1/64 |     |     |
| switch(config-if)#       | ipv6      | ospfv3             | 1 area 1  |     |     |
| switch(config-if)#       | exit      |                    |           |     |     |
| switch(config)#          | interface | 1/1/2              |           |     |     |
| switch(config-if)#       | no        | shutdown           |           |     |     |
| switch(config-if)#       | ipv6      | address            | 100::2/64 |     |     |
| switch(config-if)#       | ipv6      | ospfv3             | 2 area 2  |     |     |
| switch(config-if)#       | exit      |                    |           |     |     |
| switch(config)#          | exit      |                    |           |     |     |
| switch# show             | bfd       |                    |           |     |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 20

| Admin status: | enabled |               |     |     |     |     |     |     |     |
| ------------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| Echo source   | IP:     | 100.100.100.1 |     |     |     |     |     |     |     |
Statistics:
| Total number      | of          | control | packets |     | transmitted: | 20  |             |     |      |
| ----------------- | ----------- | ------- | ------- | --- | ------------ | --- | ----------- | --- | ---- |
| Total number      | of          | control | packets |     | received:    | 17  |             |     |      |
| Total number      | of          | control | packets |     | dropped:     | 0   |             |     |      |
| Session Interface |             | VRF     | Source  |     | IP           |     | Destination | IP  | Echo |
| State             | Application |         |         |     |              |     |             |     |      |
------- --------- ------- --------------- --------------- --------
| ------------ | ------------ |     |     |     |     |     |     |     |     |
| ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
1 tunnel1 default fe80::94f1:28a0:1ef:700 fe80::94f1:28a0:1ef:a100 enabled
| up  | ospfv3 |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
2 tunnel1 default fe80::94e2:37b1:1ef:111 fe80::94e2:37b1:1ef:555 enabled
| up  | ospfv3 |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ThisexampleshowshowtoenableBFDonaspecificOSPFv3interface.
| switch# config  |     |        |        |     |     |     |     |     |     |
| --------------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- |
| switch(config)# |     | bfd    |        |     |     |     |     |     |     |
| switch(config)# |     | router | ospfv3 | 1   |     |     |     |     |     |
switch(config-ospfv3-1)#
|                          |     |           | area      | 1   |           |     |     |     |     |
| ------------------------ | --- | --------- | --------- | --- | --------- | --- | --- | --- | --- |
| switch(config-ospfv3-1)# |     |           | router-id |     | 1.1.1.1   |     |     |     |     |
| switch(config-ospfv3-1)# |     |           | exit      |     |           |     |     |     |     |
| switch(config)#          |     | interface | 1/1/1     |     |           |     |     |     |     |
| switch(config-if)#       |     | no        | shutdown  |     |           |     |     |     |     |
| switch(config-if)#       |     | ipv6      | address   |     | 100::1/64 |     |     |     |     |
| switch(config-if)#       |     | ipv6      | ospfv3    | 1   | area      | 1   |     |     |     |
| switch(config-if)#       |     | ipv6      | ospfv3    | bfd |           |     |     |     |     |
| switch(config-if)#       |     | exit      |           |     |           |     |     |     |     |
| switch(config)#          |     | exit      |           |     |           |     |     |     |     |
switch#
| show          | bfd     | interface     |     | 1/1/1 |     |     |     |     |     |
| ------------- | ------- | ------------- | --- | ----- | --- | --- | --- | --- | --- |
| Admin status: | enabled |               |     |       |     |     |     |     |     |
| Echo source   | IP:     | 100.100.100.1 |     |       |     |     |     |     |     |
Statistics:
| Total number      | of          | control | packets |        | transmitted: | 20  |             |     |      |
| ----------------- | ----------- | ------- | ------- | ------ | ------------ | --- | ----------- | --- | ---- |
| Total number      | of          | control | packets |        | received:    | 17  |             |     |      |
| Total number      | of          | control | packets |        | dropped:     | 0   |             |     |      |
| Session Interface |             | VRF     |         | Source | IP           |     | Destination | IP  | Echo |
| State             | Application |         |         |        |              |     |             |     |      |
------- --------- --------- --------------- --------------- -------
| - ------------ |     | ------------ |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
1 tunnel1 default fe80::94f1:28a0:1ef:700 fe80::94f1:28a0:1ef:a100 enabled
| up          | ospfv3 |     |     |     |      |      |     |     |     |
| ----------- | ------ | --- | --- | --- | ---- | ---- | --- | --- | --- |
| Configuring |        | BFD | for | PIM | Over | IPv4 |     |     |     |
Prerequisites
PIMmustbeenabledgloballyandonthespecificinterfacethatwillsupportBFD.
Procedure
BFD|21

1. EnableBFDsupportwiththecommandbfd.
2. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
|     | BFD setting         |     |     |     | Default | value |     | Commandtochange       |     | it  |
| --- | ------------------- | --- | --- | --- | ------- | ----- | --- | --------------------- | --- | --- |
|     | SetstheBFDdetection |     |     |     | 5       |       |     | bfd detect-multiplier |     |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
3. SwitchtotheinterfaceonwhichyouwanttoenableBFDwiththecommandinterface.
| 4.  | EnableBFDsupportwiththecommandip                  |     |     |     |     | pim-sparse |     | bfd. |     |     |
| --- | ------------------------------------------------- | --- | --- | --- | --- | ---------- | --- | ---- | --- | --- |
| 5.  | ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     |     |            |     | bfd. |     |     |
Examples
ThisexampleshowshowtoconfigurePIMandenableBFDoninterface1/1/2.
|     | switch# config      |         |           |            |             |     |     |     |     |     |
| --- | ------------------- | ------- | --------- | ---------- | ----------- | --- | --- | --- | --- | --- |
|     | switch(config)#     |         | bfd       |            |             |     |     |     |     |     |
|     | switch(config)#     |         | router    | pim        |             |     |     |     |     |     |
|     | switch(config-pim)# |         | enable    |            |             |     |     |     |     |     |
|     | switch(config-pim)# |         | exit      |            |             |     |     |     |     |     |
|     | switch(config)#     |         | interface |            | 1/1/2       |     |     |     |     |     |
|     | switch(config-if)#  |         | no        | shutdown   |             |     |     |     |     |     |
|     | switch(config-if)#  |         | ip        | address    | 10.1.1.1/24 |     |     |     |     |     |
|     | switch(config-if)#  |         | ip        | pim-sparse | enable      |     |     |     |     |     |
|     | switch(config-if)#  |         | ip        | pim-sparse | bfd         |     |     |     |     |     |
|     | switch(config-if)#  |         | exit      |            |             |     |     |     |     |     |
|     | switch(config)#     |         | exit      |            |             |     |     |     |     |     |
|     | switch# show        | bfd     |           |            |             |     |     |     |     |     |
|     | Admin status:       | enabled |           |            |             |     |     |     |     |     |
Statistics:
|     | Total number      | of          | control | packets | transmitted: |     | 7   |             |     |      |
| --- | ----------------- | ----------- | ------- | ------- | ------------ | --- | --- | ----------- | --- | ---- |
|     | Total number      | of          | control | packets | received:    |     | 8   |             |     |      |
|     | Total number      | of          | control | packets | dropped:     | 0   |     |             |     |      |
|     | Session Interface |             | VRF     |         | Source IP    |     |     | Destination | IP  | Echo |
|     | State             | Application |         |         |              |     |     |             |     |      |
------- --------- --------- ------------------- ---------------------- -------- ----
|     | -------- ------------ |     |         |     |     |     |     |          |     |            |
| --- | --------------------- | --- | ------- | --- | --- | --- | --- | -------- | --- | ---------- |
|     | 1 1/1/2               |     | default |     | N/A |     |     | 10.1.1.2 |     | enabled up |
pim
| Configuring |     |     | BFD | for | PIM Over |     | IPv6 |     |     |     |
| ----------- | --- | --- | --- | --- | -------- | --- | ---- | --- | --- | --- |
Prerequisites
AOS-CX10.07HighAvailabilityGuide|UserGuide 22

PIMmustbeenabledgloballyandonthespecificinterfacethatwillsupportBFD.
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
| BFD setting         |     |     |     | Default | value |     | Commandtochange       |     | it  |     |
| ------------------- | --- | --- | --- | ------- | ----- | --- | --------------------- | --- | --- | --- |
| SetstheBFDdetection |     |     |     | 5       |       |     | bfd detect-multiplier |     |     |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
3. SwitchtotheinterfaceonwhichyouwanttoenableBFDwiththecommandinterface.
| 4. EnableBFDsupportwiththecommandip                  |     |     |     |     | pim-sparse |     | bfd. |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | ---------- | --- | ---- | --- | --- | --- |
| 5. ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     |     |            |     | bfd. |     |     |     |
Examples
ThisexampleshowshowtoconfigurePIMandenableBFDoninterface1/1/2.
| switch# config      |         |           |            |            |     |     |     |     |     |     |
| ------------------- | ------- | --------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
| switch(config)#     |         | bfd       |            |            |     |     |     |     |     |     |
| switch(config)#     |         | router    | pim6       |            |     |     |     |     |     |     |
| switch(config-pim)# |         | enable    |            |            |     |     |     |     |     |     |
| switch(config-pim)# |         | exit      |            |            |     |     |     |     |     |     |
| switch(config)#     |         | interface |            | 1/1/2      |     |     |     |     |     |     |
| switch(config-if)#  |         | no        | shutdown   |            |     |     |     |     |     |     |
| switch(config-if)#  |         | ipv6      | address    | 2130::1/64 |     |     |     |     |     |     |
| switch(config-if)#  |         | ipv6      | mld        | enable     |     |     |     |     |     |     |
| switch(config-if)#  |         | ip        | pim-sparse | enable     |     |     |     |     |     |     |
| switch(config-if)#  |         | ip        | pim-sparse | bfd        |     |     |     |     |     |     |
| switch(config-if)#  |         | exit      |            |            |     |     |     |     |     |     |
| switch(config)#     |         | exit      |            |            |     |     |     |     |     |     |
| switch# show        | bfd     |           |            |            |     |     |     |     |     |     |
| Admin status:       | enabled |           |            |            |     |     |     |     |     |     |
| Echo source         | IP:     | <none>    |            |            |     |     |     |     |     |     |
Statistics:
| Total number      | of  | control     | packets | transmitted: |     | 8   |             |     |     |      |
| ----------------- | --- | ----------- | ------- | ------------ | --- | --- | ----------- | --- | --- | ---- |
| Total number      | of  | control     | packets | received:    |     | 8   |             |     |     |      |
| Total number      | of  | control     | packets | dropped:     | 0   |     |             |     |     |      |
| Session Interface |     | VRF         |         | Source IP    |     |     | Destination | IP  |     | Echo |
| State             |     | Application |         |              |     |     |             |     |     |      |
------- --------- --------- ------------------- ----------------------------- ------
| -- ------------ |     | ------------ |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
BFD|23

| 1           | 1/1/2 |     | default |     | N/A  |     | fe80::94f1:2821:2ef:6300 |     |
| ----------- | ----- | --- | ------- | --- | ---- | --- | ------------------------ | --- |
| enabled     |       | up  | pimv6   |     |      |     |                          |     |
| Configuring |       |     | BFD     | for | VRRP |     |                          |     |
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. EnableBFDonaVRRPinterfacewiththecommandbfd<IPV4-ADDR>.
3. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
|     | BFD                 | setting |     |     | Default value |     | Commandtochange       | it  |
| --- | ------------------- | ------- | --- | --- | ------------- | --- | --------------------- | --- |
|     | SetstheBFDdetection |         |     |     | 5             |     | bfd detect-multiplier |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
4. ReviewBFDconfigurationsettingswiththecommandsshow bfd.
Example
EnablingBFDonaVRRPinterface.
|     | switch#                 | config    |          |                      |                  |      |      |     |
| --- | ----------------------- | --------- | -------- | -------------------- | ---------------- | ---- | ---- | --- |
|     | switch(config)#         |           | bfd      |                      |                  |      |      |     |
|     | switch#                 | interface | 1/1/1    |                      |                  |      |      |     |
|     | switch(config-if)#      |           | no       | shutdown             |                  |      |      |     |
|     | switch(config-if)#      |           | ip       | address              | 192.168.1.1/24   |      |      |     |
|     | switch(config-if)#      |           | vrrp     | 1                    | address-family   | ipv4 |      |     |
|     | switch(config-if-vrrp)# |           |          | bfd                  | 192.158.1.2      |      |      |     |
|     | switch(config-if-vrrp)# |           |          | exit                 |                  |      |      |     |
|     | switch#                 | show      | vrrp     |                      |                  |      |      |     |
|     | VRRP is                 | enabled   |          |                      |                  |      |      |     |
|     | Interface               | 1/1/1     | - Group  | 1                    | - Address-Family |      | IPv4 |     |
|     | State                   | is MASTER |          |                      |                  |      |      |     |
|     | State                   | duration  | 56 mins  | 57.826               | secs             |      |      |     |
|     | Virtual                 | IP        | address  | is 192.168.1.1       |                  |      |      |     |
|     | Virtual                 | MAC       | address  | is 00:00:5e:00:01:01 |                  |      |      |     |
|     | Advertisement           |           | interval | is                   | 1000 msec        |      |      |     |
|     | Preemption              |           | enabled  |                      |                  |      |      |     |
|     | Priority                | is        | 100      |                      |                  |      |      |     |
|     | BFD is                  | enabled   |          |                      |                  |      |      |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 24

Master Router is 192.168.1.1 (local), priority is 100
Master Advertisement interval is 1000 msec
Master Down interval is unknown
Tracked object ID is 1, and state Down

BFD Commands

bfd

Syntax

bfd
no bfd

Description

Enables BFD support on the switch. BFD is disabled by default.

The no form of this command disables BFD and removes all related configuration settings. To disable BFD,
but retain configuration settings, use the command bfd disable.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling BFD support:

switch(config)# bfd

Disabling BFD support and removing all configuration settings:

switch(config)# no bfd

bfd <IPV4-ADDR>

Syntax

bfd <IPV4-ADDR>

no bfd <IPV4-ADDR>

Description

Enables BFD under VRRP for the specified IP address. BFD is asynchronous and echo mode is supported.

The no form of this command disables BFD under VRRP for the specified IP address.

Command context

config-if-vrrp

Parameters

BFD | 25

<IPV4-ADDR>
SpecifiestheaddressonwhichtoenableBFDinIPv4format(x.x.x.x),wherexisadecimalnumber
from0to255.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDontheaddress10.0.0.1onVRRP1:
| switch(config)#         | interface | 1/1/1            |      |
| ----------------------- | --------- | ---------------- | ---- |
| switch(config-if)#      | routing   |                  |      |
| switch(config-if)#      | vrrp      | 1 address-family | ipv4 |
| switch(config-if-vrrp)# |           | bfd 10.0.0.1     |      |
DisablingBFDontheaddress10.0.0.1onVRRP1:
| switch(config)#    | interface | 1/1/1 |     |
| ------------------ | --------- | ----- | --- |
| switch(config-if)# | routing   |       |     |
switch(config-if)#
|                         | vrrp | 1 address-family | ipv4 |
| ----------------------- | ---- | ---------------- | ---- |
| switch(config-if-vrrp)# |      | no bfd 10.0.0.1  |      |
bfd all-interfaces
Syntax
bfd all-interfaces
no bfd all-interfaces
Description
EnablesBFDonallOSPFv2orOSPFv3interfaces.
ThenoformofthiscommanddisablesBFDonallOSPFv2/OSPFv3orPIMIPv4/IPv6interfaces,excluding
thoseonwhichBFDwasenabledattheinterfacelevelwiththecommandsip ospf bfdandipv6 ospfv3
bfd.
Commandcontext
config-ospf-<INSTANCE-TAG>
config-ospfv3-<INSTANCE-TAG>
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingBFDonallOSPFv2interfaces:
| switch(config)#        | router | ospf 1             |     |
| ---------------------- | ------ | ------------------ | --- |
| switch(config-ospf-1)# |        | bfd all-interfaces |     |
DisablingBFDonallOSPFv2interfaces:
AOS-CX10.07HighAvailabilityGuide|UserGuide 26

| switch(config)# | router ospf | 1   |     |
| --------------- | ----------- | --- | --- |
switch(config-ospf-1)#
|     | no  | bfd all-interfaces |     |
| --- | --- | ------------------ | --- |
EnablingBFDonallOSPFv3interfaces:
| switch(config)#          | router ospfv3 | 1                  |     |
| ------------------------ | ------------- | ------------------ | --- |
| switch(config-ospfv3-1)# |               | bfd all-interfaces |     |
DisablingBFDonallOSPFv3interfaces:
| switch(config)#          | router ospfv3 | 1                     |     |
| ------------------------ | ------------- | --------------------- | --- |
| switch(config-ospfv3-1)# |               | no bfd all-interfaces |     |
bfd detect-multiplier
Syntax
| bfd detect-multiplier | <MULTIPLIER> |     |     |
| --------------------- | ------------ | --- | --- |
no bfd detect-multiplier
Description
SetsBFDdetectionmultiplieronaninterface.
ThenoformofthiscommandsetstheBFDdetectionmultipliertothedefaultvalueof5.
Commandcontext
config-if
Parameters
<MULTIPLIER>
SpecifiestheBFDdetectionmultiplier.Range:1to5.Default:5.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingtheBFDdetectionmultiplierto3:
| switch(config-if)# | bfd detect-multiplier |     | 3   |
| ------------------ | --------------------- | --- | --- |
SettingtheBFDdetectionmultipliertothedefaultvalue:
| switch(config-if)# | no bfd | detect-multiplier |     |
| ------------------ | ------ | ----------------- | --- |
bfd disable
Syntax
bfd disable
BFD|27

Description
DisablesBFDontheswitch,butretainsallconfigurationsettings.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DisablingBFD:
| switch(config)# | bfd disable |             |
| --------------- | ----------- | ----------- |
| bfd enable      | (Context:   | config-hsc) |
Syntax
| switch(config-hsc)# | bfd enable |        |
| ------------------- | ---------- | ------ |
| switch(config-hsc)# | no bfd     | enable |
Description
EnablesordisablesBFDforHSCfeature.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
n BFDmustbeenabledgloballytoworkforHSC.
Examples
EnablingBFDsupportforHSC:
| switch(config)#     | hsc |        |
| ------------------- | --- | ------ |
| switch(config-hsc)# | bfd | enable |
DisablingBFDsupportforHSC:
| switch(config)#     | hsc       |             |
| ------------------- | --------- | ----------- |
| switch(config-hsc)# | no        | bfd enable  |
| bfd disable         | (Context: | config-hsc) |
Syntax
| switch(config-hsc)# | bfd disable |     |
| ------------------- | ----------- | --- |
AOS-CX10.07HighAvailabilityGuide|UserGuide 28

Description

Disables BFD for HSC feature.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Example

Disabling BFD support for HSC:

switch(config)# hsc
switch(config-hsc)# bfd disable

bfd echo disable

Syntax

bfd echo disable
no bfd echo disable

Description

Disables support for BFD echo packets. Echo packet support is enabled by default.

The no form of this command enables support for BFD echo packets.

Toggling this feature on 8325 or 8360 switches may cause route flapping.

Command context

config
config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Enabling BFD echo packet support on all interfaces:

switch(config)# no bfd echo disable

Disabling BFD echo packet support on all interfaces:

switch(config)# bfd echo disable

Enabling BFD echo packet support on interface 1/1/1:

BFD | 29

| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
|     | bfd | echo disable |     |
| --- | --- | ------------ | --- |
DisablingBFDechopacketsupportoninterface1/1/1:
| switch(config)#    | interface | 1/1/1        |     |
| ------------------ | --------- | ------------ | --- |
| switch(config-if)# | no bfd    | echo disable |     |
bfd echo-src-ip-address
Syntax
| bfd echo-src-ip-address | <IPV4-ADDR> |     |     |
| ----------------------- | ----------- | --- | --- |
no bfd echo-src-ip-address
Description
SetsthesourceIPv4addressforBFDechopackets.Thisaddressisusedinallechosessions.
ThesourceIPaddressmustnotbeonthesamenetworksegmentasanyswitchinterface,otherwisealarge
numberofICMPredirectpacketsmaybesentbytheremotedevice,causingnetworkcongestion.
ThenoformofthiscommandremovesthesourceIPv4addressforBFDechopackets,whichcausesthe
switchtostopsendingechopackets.Whenavalidvalueisset,allsessionswithapeerthatiscapableof
receivingechopackets,willstarttransmittingechopackets.BFDcontrolsessionscontinuetorun
concurrentlywithechopackets.
Commandcontext
config
Parameters
<IPV4-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingthesourceIPaddressto198.51.100.1:
| switch(config)# | bfd echo-src-ip-address |     | 198.51.100.1 |
| --------------- | ----------------------- | --- | ------------ |
RemovingthesourceIPaddress:
| switch(config)# | no bfd | echo-src-ip-address |     |
| --------------- | ------ | ------------------- | --- |
bfd min-echo-receive-interval
Syntax
AOS-CX10.07HighAvailabilityGuide|UserGuide 30

bfd min-echo-receive-interval <INTERVAL>

no bfd min-echo-receive-interval

Description

Sets the minimum time interval between received BFD echo packets.

The no form of this command sets the minimum interval between received BFD echo packets to the default
value of 500 milliseconds.

Command context

config

Parameters

<INTERVAL>

Specifies the minimum reception interval in milliseconds. A value of 0 means that the switch does not
support reception of BFD echo packets. Range: 0, 50 to 1000. Default: 500.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the minimum reception interval to 1000 milliseconds:

switch(config)# bfd min-echo-receive-interval 1000

Setting the minimum reception interval to the default value:

switch(config)# no bfd min-echo-receive-interval

bfd min-receive-interval

Syntax

bfd min-receive-interval <INTERVAL>

no bfd min-receive-interval

Description

Sets the minimum time interval between received BFD control packets on an interface.

The no form of this command sets the minimum interval between received BFD control packets to the
default value of 3000 milliseconds.

Command context

config-if

Parameters

<INTERVAL>

Specifies the minimum receive interval in milliseconds. A value of 0 means that the switch does not
support reception of BFD control packets. Range: 500 to 20000. 3000. Default: 3000.

Authority

BFD | 31

Administrators or local user group members with execution rights for this command.

Examples

Setting the minimum receive interval to 1000 milliseconds:

switch(config-if)# bfd min-receive-interval 1000

Setting the minimum receive interval to the default value:

switch(config-if)# no bfd min-receive-interval

bfd min-transmit-interval

Syntax

bfd min-transmit-interval <INTERVAL>

no bfd min-transmit-interval

Description

Sets the minimum time interval between transmitted BFD control packets on an interface.

The no form of this command sets the minimum interval between transmitted BFD control packets to the
default value of 3000 ms.

Command context

config-if

Parameters

<INTERVAL>

Specifies the minimum transmit interval in milliseconds. Range: 500 to 20000 (6300, 6400, 8360, 8400).
50 to 20000 (8320, 8325). Default: 3000.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n If the minimum time interval is set between 500 ms and 1000 ms, then bfd detect-multiplier must be

set to at least 3.

n If bfd detect-multiplier is set to 1, then the minimum transmit interval must be set to at least 3000

ms.

n Whenever the minimum time interval is set to a value less than 1000 ms, BFD automatically adjusts the

transmission interval to 1000 ms if any of the following conditions apply:

o The session is operating in asynchronous mode and echo is enabled.

o The session state is in any other state than up.

As described in RFC 5880, this behavior occurs because BFD echo provides quick detection which allows
the BFD asynchronous session to lower its traffic/resource requirements.

Examples

AOS-CX 10.07 High Availability Guide | User Guide

32

Settingtheminimumtransmitintervalto500ms:
| switch(config-if)# |     | bfd min-transmit-interval |     | 500 |
| ------------------ | --- | ------------------------- | --- | --- |
Settingtheminimumtransmitintervaltothedefaultvalue:
| switch(config-if)# |                | no bfd | min-transmit-interval |     |
| ------------------ | -------------- | ------ | --------------------- | --- |
| clear              | bfd statistics |        |                       |     |
Syntax
| clear bfd | statistics | [session | <ID>] |     |
| --------- | ---------- | -------- | ----- | --- |
Description
ClearsstatisticsforallBFDsessionsorforaspecificBFDsession.
Commandscontext
Manager(#)
Parameters
| session | <ID> |     |     |     |
| ------- | ---- | --- | --- | --- |
SpecifiesasessionID.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ClearingstatisticsforallBFDsessions:
| switch# | clear | bfd statistics |     |     |
| ------- | ----- | -------------- | --- | --- |
ClearingstatisticsforBFDsession1:
| switch# | clear | bfd statistics | session 1 |     |
| ------- | ----- | -------------- | --------- | --- |
| ip ospf | bfd   |                |           |     |
Syntax
| ip ospf    | bfd |     |     |     |
| ---------- | --- | --- | --- | --- |
| no ip ospf | bfd |     |     |     |
Description
EnablesBFDforOSPFv2onthecurrentinterface.TheinterfacemusthaveOSPFv2enabledonit.This
overridestheglobalsettingsdefinedwiththecommandbfd all-interfaces.
Thenoformofthiscommandsetsthecurrentinterfacetotheglobalsettingsdefinedwiththecommand
bfd all-interfaces.
BFD|33

Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDoninterface1/1/1:
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | ip ospf   | bfd   |
DisablingBFDoninterface1/1/1:
| switch(config)#     | interface | 1/1/1    |
| ------------------- | --------- | -------- |
| switch(config-if)#  | no ip     | ospf bfd |
| ip ospf bfd disable |           |          |
Syntax
ip ospf bfd disable
Description
DisablesBFDforOSPFv2onthecurrentinterface.Thisoverridestheglobalsettingsdefinedwiththe
| commandbfd all-interfaces. |     |     |
| -------------------------- | --- | --- |
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDoninterface1/1/1:
| switch(config)#    | interface | 1/1/1       |
| ------------------ | --------- | ----------- |
| switch(config-if)# | ip ospf   | bfd disable |
ip route bfd
Syntax
ip route <DEST-IPV4-ADDR>/<NETMASK> [<NEXT-HOP-IP-ADDR> | <INTERFACE>] [bfd]
Description
AOS-CX10.07HighAvailabilityGuide|UserGuide 34

EnablesordisablesBFDonthespecifiedstaticroute.TodisableBFD,issuethecommandwithoutthebfd
option.
Commandcontext
config
Parameters
<DEST-IPV4-ADDR>
SpecifiesaroutedestinationinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
<NETMASK>
SpecifiesthenumberofbitsintheaddressmaskinCIDRformat(x),wherexisadecimalnumberfrom0
to128.
<NEXT-HOP-IP-ADDR>
SpecifiesthenexthopaddressforreachingthedestinationinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255.
<INTERFACE>
Specifiesthenexthopasanoutgoinginterface.
bfd
EnablesBFDonthestaticroute.OmitthisparametertodisableBFD.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDonastaticroute:
| switch(config)#    | interface  | 1/1/1       |     |
| ------------------ | ---------- | ----------- | --- |
| switch(config-if)# | ip address | 20.1.1.2/24 |     |
switch(config-if)# no shutdownswitch(config-if)#routingswitch(config-if)# exit
| switch(config)# | ip route | 192.0.0.0/8 | 20.1.1.1 bfd |
| --------------- | -------- | ----------- | ------------ |
DisablingBFDonastaticroute:
| switch(config)# | ip route | 192.0.0.0/8 | 20.1.1.1 |
| --------------- | -------- | ----------- | -------- |
EnablingBFDonastaticroute:
| switch(config)#    | interface  | 1/1/1       |     |
| ------------------ | ---------- | ----------- | --- |
| switch(config-if)# | ip address | 20.1.1.2/24 |     |
switch(config-if)# no shutdownswitch(config-if)#routingswitch(config-if)# exit
| switch(config)# | ip route | 192.0.0.0/8 | 1/1/1 bfd |
| --------------- | -------- | ----------- | --------- |
DisablingBFDonastaticroute:
| switch(config)# | ip route | 192.0.0.0/8 | 1/1/1 |
| --------------- | -------- | ----------- | ----- |
| ipv6 ospfv3     | bfd      |             |       |
BFD|35

Syntax

ipv6 ospfv3 bfd
no ipv6 ospfv3 bfd

Description

Enables BFD for OSPFv3 on the current interface. The interface must have OSPFv3 enabled on it. This
overrides the global settings defined with the command bfd all-interfaces.

The no form of this command sets the current interface to the global settings defined with the command
bfd all-interfaces.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling BFD:

switch(config-if)# ipv6 ospfv3 bfd

Disabling BFD:

switch(config-if)# no ipv6 ospfv3 bfd

ipv6 ospfv3 bfd disable

Syntax

ipv6 ospfv3 bfd disable

Description

Disables BFD on the current OSPFv3 interface. This overrides the global settings defined with the command
bfd all-interfaces.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Enabling BFD on interface 1/1/1:

switch(config)# interface 1/1/1switch(config-if)# routedswitch(config-if)# ipv6 ospfv3
bfd disable

AOS-CX 10.07 High Availability Guide | User Guide

36

| neighbor | fall-over |     | bfd |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- | --- | --- |
Syntax
| neighbor    | {<IP-ADDRESS>|<PEER-GROUP-NAME>} |     |     |     | fall-over |           | bfd |
| ----------- | -------------------------------- | --- | --- | --- | --------- | --------- | --- |
| no neighbor | {<IP-ADDRESS>|<PEER-GROUP-NAME>} |     |     |     |           | fall-over | bfd |
Description
EnablesBGPtoregisterwithBFDtoreceivefastpeeringsessiondeactivationmessagesfromBFD.
ThenoformofthiscommanddisablesBGPforBFD.
Currently,BFDissupportedonlywithIPv4neighbors.SupporttoenableBFDwithIPv6neighborswillbeaddedina
futurerelease.
Commandcontext
config-router
Parameters
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
<PEER-GROUP-NAME>
Specifiesapeergroup.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| switch(config-router)# |     |     | neighbor    | 1.1.1.1 | fall-over    |           |     |
| ---------------------- | --- | --- | ----------- | ------- | ------------ | --------- | --- |
| switch(config-router)# |     |     | no neighbor |         | 1.1.1.1      | fall-over | bfd |
| switch(config-router)# |     |     | neighbor    | PG      | fall-over    |           |     |
| switch(config-router)# |     |     | no neighbor |         | PG fall-over |           | bfd |
| show bfd               |     |     |             |         |              |           |     |
Syntax
| show bfd | [session | <ID>] | [all-vrfs | | vrf | <NAME>] | [vsx-peer] |     |
| -------- | -------- | ----- | --------- | ----- | ------- | ---------- | --- |
Description
ShowsinformationforallBFDsessionsorforaspecificBFDsession.
Commandscontext
| Manager (#) |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
Parameters
| session | <ID> |     |     |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- | --- |
SessionID.
all-vrfs
BFD|37

AllVRFs.
vrf <NAME>
SpecifiesthenameofaVRF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
PossiblevaluesforStateare:
n Up
n Down
n AdminDown
n Init
| PossiblevaluesforLocal | diagnosticandRemote |     | diagnosticare: |     |     |
| ---------------------- | ------------------- | --- | -------------- | --- | --- |
n Controldetectiontimeexpired(1):ThesessionhasstoppedreceivingBFDcontrolpacketsfromthepeer
afteronedetectiontime.
n Echofunctionfailed:ThesessionhasstoppedreceivingBFDEchopackets,sothesessionwasdeclared
Down.
n Neighborsignaledsessiondown:ApacketfromthepeerwasreceivedwitheitherAdminDownorDown
state.
n Forwardingplanereset:Notsetinthisrelease.
n Pathdown:TheforwardingpathwhenDown.
n Concatenatedpathdown:Notsetinthisrelease.
n Administrativelydown:TheadministratorhasdisabledBFD.
Reverseconcatenatedpathdown:Notsetinthisrelease.
n
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
------- --------- --------- ------------------------------- ------------------------
| ------- -------- | -------- | ------------ |     |            |     |
| ---------------- | -------- | ------------ | --- | ---------- | --- |
| 1 vlan10         | blue     | 10.10.10.1   |     | 10.10.10.2 |     |
| disabled         | up       | ospf         |     |            |     |
| 1 vlan10         | blue     | N/A          |     | 10.10.10.2 |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 38

|     | disabled | up    | static_routes |     |     |            |     |
| --- | -------- | ----- | ------------- | --- | --- | ---------- | --- |
| 2   | vlan40   | red   | 40.10.10.1    |     |     | 40.10.10.2 |     |
|     | disabled | up    | ospf          |     |     |            |     |
| 3   | vlan30   | red   | 30.10.10.1    |     |     | 30.10.10.2 |     |
|     | disabled | up    | ospf          |     |     |            |     |
| 4   | vlan20   | blue  | 20.10.10.1    |     |     | 20.10.10.2 |     |
|     | disabled | up    | ospf          |     |     |            |     |
| 5   | vlan50   | black | 50.10.10.1    |     |     | 50.10.10.2 |     |
|     | disabled | up    | ospf          |     |     |            |     |
| 6   | vlan60   | black | 60.10.10.1    |     |     | 60.10.10.2 |     |
|     | disabled | up    | ospf          |     |     |            |     |
7 vlan10 blue fe80::409:7380:a62:2400 fe80::409:7380:a49:a200
|     | disabled | up  | ospfv3 |     |     |     |     |
| --- | -------- | --- | ------ | --- | --- | --- | --- |
ShowinginformationforBFDsession1:
| switch#     | show bfd    | session | 1         |     |     |     |     |
| ----------- | ----------- | ------- | --------- | --- | --- | --- | --- |
| BFD Session | Information |         | – Session | 1   |     |     |     |
VRF: blue
| Min Tx              | Interval      | (msec) | : 10000 |     |     |     |     |
| ------------------- | ------------- | ------ | ------- | --- | --- | --- | --- |
| Min Rx              | Interval      | (msec) | : 10000 |     |     |     |     |
| Min Echo            | Rx Interval   | (msec) | : 700   |     |     |     |     |
| Detect              | Multiplier    | : 3    |         |     |     |     |     |
| Application         | : ospf        |        |         |     |     |     |     |
| Local Discriminator |               | : 1    |         |     |     |     |     |
| Remote              | Discriminator | :      | 1       |     |     |     |     |
Echo : Enabled
| Local Diagnostic |             | : no_diagnostic       |     |     |     |     |     |
| ---------------- | ----------- | --------------------- | --- | --- | --- | --- | --- |
| Remote           | Diagnostic: | administratively_down |     |     |     |     |     |
| State flaps:     | 0           |                       |     |     |     |     |     |
Interface Source IP Destination IP State Pkt In Pkt Out Pkt Drop
--------- --------------- --------------- ---------- -------- -------- --------
| 1/1/1 | 100.100.100.100 |     | 100.100.100.101 |     | Up  | 100 101 | 0   |
| ----- | --------------- | --- | --------------- | --- | --- | ------- | --- |
ShowinginformationforallBFDsessionsrelatedtoaparticularVRFinthesystem:
| switch#       | show bfd | vrf blue  |     |     |     |     |     |
| ------------- | -------- | --------- | --- | --- | --- | --- | --- |
| Admin status: | enabled  |           |     |     |     |     |     |
| Echo source   | IP:      | 100.1.1.1 |     |     |     |     |     |
Statistics:
| Total number | of        | control | packets     | transmitted: | 2226 |             |     |
| ------------ | --------- | ------- | ----------- | ------------ | ---- | ----------- | --- |
| Total number | of        | control | packets     | received:    | 2222 |             |     |
| Total number | of        | control | packets     | dropped:     | 0    |             |     |
| Session      | Interface | VRF     | Source      | IP           |      | Destination | IP  |
|              | Echo      | State   | Application |              |      |             |     |
------- --------- --------- ------------------------------- ------------------------
| ------- | -------- | -------- | ------------  |     |     |            |     |
| ------- | -------- | -------- | ------------- | --- | --- | ---------- | --- |
| 1       | vlan10   | blue     | 10.10.10.1    |     |     | 10.10.10.2 |     |
|         | disabled | up       | ospf          |     |     |            |     |
| 1       | vlan10   | blue     | N/A           |     |     | 10.10.10.2 |     |
|         | disabled | up       | static_routes |     |     |            |     |
| 4       | vlan20   | blue     | 20.10.10.1    |     |     | 20.10.10.2 |     |
|         | disabled | up       | ospf          |     |     |            |     |
7 vlan10 blue fe80::409:7380:a62:2400 fe80::409:7380:a49:a200
|          | disabled  | up  | ospfv3 |     |     |     |     |
| -------- | --------- | --- | ------ | --- | --- | --- | --- |
| show bfd | interface |     |        |     |     |     |     |
BFD|39

Syntax
| show bfd interface |     | <NAME> |     |     |     |     |     |
| ------------------ | --- | ------ | --- | --- | --- | --- | --- |
Description
ShowsinformationforallBFDsessionsrelatedtothespecifiedinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
interface <NAME>
Specifiesaninterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShowinginformationforallBFDsessionsrelatedtothespecifiedinterface:
switch#
|                      | show bfd       | interface | vlan10    |     |     |     |     |
| -------------------- | -------------- | --------- | --------- | --- | --- | --- | --- |
| BFD session          | information    |           | - Session |     | 1   |     |     |
| Min Tx               | interval       | (msec):   | 3000      |     |     |     |     |
| Min Rx               | interval       | (msec):   | 3000      |     |     |     |     |
| Min echo             | Rx interval    |           | (msec):   | 500 |     |     |     |
| Detect               | multiplier:    | 5         |           |     |     |     |     |
| Application:         | ospf           |           |           |     |     |     |     |
| Local discriminator: |                |           | 13211     |     |     |     |     |
| Remote               | discriminator: |           | 13211     |     |     |     |     |
Echo: disabled
| Local diagnostic: |             | no_diagnostic |        |     |          |             |     |
| ----------------- | ----------- | ------------- | ------ | --- | -------- | ----------- | --- |
| Remote            | diagnostic: | no_diagnostic |        |     |          |             |     |
| State flaps:      | 0           |               |        |     |          |             |     |
| Interface         | Source      | IP            |        |     |          | Destination | IP  |
| State             |             | Pkt           | Rx Pkt | Tx  | Pkt drop |             |     |
--------- --------------------------------------- ----------------------------------
| ----- ------------ |            | -------- |     | -------- | -------- |            |     |
| ------------------ | ---------- | -------- | --- | -------- | -------- | ---------- | --- |
| vlan10             | 10.10.10.1 |          |     |          |          | 10.10.10.2 |     |
| up                 |            | 453      | 455 |          | 0        |            |     |
===============================================
| BFD session          | information    |         | - Session |     | 1   |     |     |
| -------------------- | -------------- | ------- | --------- | --- | --- | --- | --- |
| Min Tx               | interval       | (msec): | 3000      |     |     |     |     |
| Min Rx               | interval       | (msec): | 3000      |     |     |     |     |
| Min echo             | Rx interval    |         | (msec):   | 500 |     |     |     |
| Detect               | multiplier:    | 5       |           |     |     |     |     |
| Application:         | static_routes  |         |           |     |     |     |     |
| Local discriminator: |                |         | 13211     |     |     |     |     |
| Remote               | discriminator: |         | 13211     |     |     |     |     |
Echo: disabled
| Local diagnostic: |             | no_diagnostic |        |     |          |             |     |
| ----------------- | ----------- | ------------- | ------ | --- | -------- | ----------- | --- |
| Remote            | diagnostic: | no_diagnostic |        |     |          |             |     |
| State flaps:      | 0           |               |        |     |          |             |     |
| Interface         | Source      | IP            |        |     |          | Destination | IP  |
| State             |             | Pkt           | Rx Pkt | Tx  | Pkt drop |             |     |
--------- --------------------------------------- ----------------------------------
| ----- ------------ |     | -------- |     | -------- | -------- |     |     |
| ------------------ | --- | -------- | --- | -------- | -------- | --- | --- |
AOS-CX10.07HighAvailabilityGuide|UserGuide 40

| vlan10 | N/A |     |     |     |     | 10.10.10.2 |     |
| ------ | --- | --- | --- | --- | --- | ---------- | --- |
| up     |     | 453 | 455 |     | 0   |            |     |
===============================================
| BFD session          | information    |         | - Session |     | 7   |     |     |
| -------------------- | -------------- | ------- | --------- | --- | --- | --- | --- |
| Min Tx               | interval       | (msec): | 3000      |     |     |     |     |
| Min Rx               | interval       | (msec): | 3000      |     |     |     |     |
| Min echo             | Rx interval    |         | (msec):   | 500 |     |     |     |
| Detect               | multiplier:    | 5       |           |     |     |     |     |
| Application:         |                | ospfv3  |           |     |     |     |     |
| Local discriminator: |                |         | 1402      |     |     |     |     |
| Remote               | discriminator: |         | 1402      |     |     |     |     |
Echo: disabled
| Local diagnostic: |             | no_diagnostic |        |     |          |             |     |
| ----------------- | ----------- | ------------- | ------ | --- | -------- | ----------- | --- |
| Remote            | diagnostic: | no_diagnostic |        |     |          |             |     |
| State flaps:      |             | 0             |        |     |          |             |     |
| Interface         | Source      | IP            |        |     |          | Destination | IP  |
| State             |             | Pkt           | Rx Pkt | Tx  | Pkt drop |             |     |
--------- --------------------------------------- ----------------------------------
| ----- ------------ |                         | -------- |     | -------- | -------- |                         |     |
| ------------------ | ----------------------- | -------- | --- | -------- | -------- | ----------------------- | --- |
| vlan10             | fe80::409:7380:a62:2400 |          |     |          |          | fe80::409:7380:a49:a200 |     |
| up                 |                         | 58       | 58  |          | 0        |                         |     |
show hsc
Syntax
show hsc
Description
Displaysconnectioninformationfortheremotecontroller.
Commandcontext
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Displayingconnectioninformationfortheremotecontroller:
| switch#         | show | hsc     |            |     |               |     |     |
| --------------- | ---- | ------- | ---------- | --- | ------------- | --- | --- |
| BFD status      | :    | Enabled |            |     |               |     |     |
| Controller      | IP   | Port    | Connection |     | Connection    |     |     |
| address         |      |         | status     |     | state         |     |     |
| --------------- |      | ------- | ---------- |     | ------------- |     |     |
| 192.168.16.17   |      | 6640    | UP         |     | ACTIVE        |     |     |
| 192.168.16.17   |      | 6650    | UP         |     | IDLE          |     |     |
| 192.168.16.17   |      | 6660    | DOWN       |     | BACKOFF       |     |     |
BFD|41

Chapter 4

ERPS

ERPS

ERPS supported on the following switches:

n 6300

n 6400

n 8320

n 8325

n 8360

n 8400

Ethernet Ring Protection Switching (ERPS) is a protocol defined by the International Telecommunication
Union - Telecommunication Standardization Sector (ITU-T) to eliminate loops at Layer 2. Because the
standard number is ITU-T G.8032/Y1344, ERPS is also called G.8032. ERPS defines Ring Auto Protection
Switching (RAPS) Protocol Data Units (PDUs) and protection switching mechanisms.

ERPS has two versions:

n ERPSv1 released by ITU-T in June 2008, and

n ERPSv2 released in August 2010.

EPRSv2, fully compatible with ERPSv1, provides the following enhanced functions:

n Multi-ring topologies, such as intersecting rings

n RAPS PDU transmission on non-virtual-channels (NVCs) in sub-rings

n Forced Switch (FS) and Manual Switch (MS)

n Revertive and non-revertive switching

Generally, redundant links are used on an Ethernet switching network such as a ring network to provide link
backup and enhance network reliability. The use of redundant links, however, may result in creating network
loops, causing broadcast storms, and rendering the MAC address table unstable. As a result, communication
quality deteriorates, and communication services may even be interrupted.

Ethernet networks demand faster protection switching. STP does not meet the requirement for fast
convergence.

ERPS, a standard ITU-T protocol, prevent loops on ring networks. It optimizes detection and performs fast
convergence. ERPS allows all ERPS-capable devices on a ring network to communicate.

Benefits of ERPS include:

n Prevents broadcast storms and implements fast traffic switchover on a network where there are loops.

n Provides fast convergence and carrier-class reliability.

n Allows all ERPS-capable devices on a ring network to communicate.

Limitations, Conflicts, or Exclusions

AOS-CX 10.07 High Availability Guide | User Guide

42

n ERPS coexists with STP with the following limitations:

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

n Active GW is not recommended on VLANs that are not part of VSX-LAGs. This can lead to two active GWs

on a ring when ISL fails as SVIs of those VLANs are not shut down on VSX-secondary. This results in
frequent MAC moves for gateway MAC address across ring nodes.

n On such deployments, where gateways are serving VLANs across the ring, VRRP is recommended.

n Multiple major-rings (MRs) are not supported in a VSX solution since VSX-ISL can be part of a maximum

of one MR.

n Topologies must have either a subring or MCLAG to connect downstream switches and not a mix of

both.

n Square VSX topology cannot be part of single MR since MCLAG is not supported as a ring port.

n On switches with both ERPS and STP enabled, a loop involving ring ports and STP ports is not protected.

n Redundant links from downstream switches to ring nodes must be VSX-LAGs.

n Do not enable loop-protect, MVRP, and MCLAG on ERPS ring ports. Enabling these features on an ERPS

ring port leads to undefined behavior.

n HA limitations:

o With UDLD, redundancy switchover is not hitless and results in traffic loss.

o UDLD can be used only on ring nodes that are connected through repeaters. This limitation is not

applicable with VSX because UDLD does not have to be enabled on ISL, and LAN traffic can reach a
ring through ISL. This limitation is applicable for VSF switchover.

n Increase the guard interval to 1-2 seconds to prevent Ethernet ring nodes from acting on outdated R-APS

messages and the possibility of forming a closed loop.

n Avoid using vlan trunk allowed all on interconnection link interfaces. Doing so causes looping of the

subring R-APS packet and causes undefined behavior for all rings configured on the switch.

n Protected VLANs in a subring that are not part of a major ring are allowed to accommodate guest VLANs.
Clients on those VLANs can only reach the gateway for further routing. These clients cannot reach other
clients on the same VLAN. Such VLANs must have VRRP enabled gateways on both ring interconnection
nodes.

n RPL neighbor configuration on the rings increases convergence time to the order of 300ms across link

failures. Networks critical of convergence time carrying real-time traffic must avoid RPL neighbor
configuration.

ERPS | 43

n Users must explicitly handle the dynamic change of a port from trunk to access in the following cases:

o Defaulting a LAG interface that is part of an ERPS ring.

o Swapping or removing an ISL link from a VSX that is part of an ERPS ring.

These cases lead to traffic loss in the ERPS ring, so before performing any of these actions, users must
consider the protocol used on the interface. If it is part of an ERPS ring, configure the port back to trunk
from access.

n Enabling ip neighbor-flood on SVI interfaces is recommended for faster convergence of routed traffic.

This is not supported on 6300 or 6400 switches.

n SNMP is not supported with ERPS.

n VLANs that have ring ports must be included in protected VLAN lists of at least one ERPS instance.

If VLANs with ring ports are not included in protected VLAN lists, the VLAN-port combination is not

managed by ERPS or STP and the port state of the VLAN becomes undefined causing a loop in the

network.

ERPS Commands

clear erps ring <ringid> instance <id>

Syntax

clear erps ring <ringid> instance <id>

Description

Removes the protection switching and triggers reversion both in revertive and non-revertive operation. This
command will not change the configured revertive operation mode.

Command context

Operator (>) or Manager (#)

Parameters

<ringid>

Required, specifies the ID of the ring. Range: 1-239.

<id>

Required, specifies the ID of the ring instance. Range: 1-2.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Removes the protection switching and triggers reversion for ring 3, instance 2:

switch# clear erps ring 3 instance 2

AOS-CX 10.07 High Availability Guide | User Guide

44

clear erps statistics

Syntax

clear erps statistics [ring <id>] [instance <id>]

Description

This command clears the ERPS statistics for a ring or a ring instance.

Command context

Operator (>) or Manager (#)

Parameters

<ringid>

Optional, specifies the ID of the ring. Range: 1-239.

<id>

Optional, specifies the ID of the ring instance. Range: 1-64.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Clear ERPS statistics for ring 1:

switch# clear erps statistics ring 1

Clear ERPS statistics for instance 1 of ring 1:

switch# clear erps statistics ring 1 instance 1

erps ring

Syntax

erps ring <ringid>
no erps ring <ringid>

Description

This command creates an ERPS ring with a given ID.

The no form of this command removes all the configurations of the ring, including instances.

Command context

config

Parameters

<ringid>

Required, specifies the ID of the ring. Range: 1-239

Authority

ERPS | 45

Administrators or local user group members with execution rights for this command.

Examples

Create an ERPS ring:

switch(config)# erps ring 2
switch(config-ring-2)#

Remove an ERPS ring:

switch(config)# no erps ring 2
switch(config-ring-2)#

erps ring <ringid> <port0|port1> interface

Syntax

erps ring <ringid>

<port0|port1> interface <ifname>

Description

This command configures the ERPS ring member port. An L2 interface in the switch is associated to one of
the two member ports of an ERPS ring. In case of an interconnection node, only port0 is applicable for the
sub-ring.

The no form of this command removes the association of the ring port to the L2 interface on the switch.

Command context

config-erps-ring-<ringid>

Parameters

<ringid>

Required, specifies the ID of the ring. Range: 1-239

<port0>

Required, set port0 of the ring.

<port1>

Required, set port1 of the ring.

<ifname>

Required, interface name (string).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configure the ERPS ring member port:

switch(config)# erps ring 3
switch(config-erps-ring-3)# port0 interface 1/1/1

Remove the association of the ring port to the L2 interface on the switch:

AOS-CX 10.07 High Availability Guide | User Guide

46

| switch(config)#             | erps     | ring 3      |     |
| --------------------------- | -------- | ----------- | --- |
| switch(config-erps-ring-3)# |          | no port0    |     |
| erps ring                   | <ringid> | description |     |
Syntax
| erps ring | <ringid> |     |     |
| --------- | -------- | --- | --- |
description <line>
Description
Thiscommandaddsdescriptiveinformationtohelpadministratorsandoperatorsunderstandthepurpose
ofaring.1-64printableASCIIcharactersareallowed.
Thenoformofthiscommandremovestheringinstancedescription.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<line>
Required,specifiesthedescriptiontext.Maximumlengthis64characters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Adddescriptiveinformationtoaring:
| switch(config)#            | erps | ring 3      |              |
| -------------------------- | ---- | ----------- | ------------ |
| switch(config-erps-ring-3) |      | description | HPE RnD ring |
Removedescriptiveinformationfromaring:
| switch(config)#            | erps     | ring 3         |     |
| -------------------------- | -------- | -------------- | --- |
| switch(config-erps-ring-3) |          | no description |     |
| erps ring                  | <ringid> | guard-interval |     |
Syntax
| erps ring      | <ringid> |                   |     |
| -------------- | -------- | ----------------- | --- |
| guard-interval |          | <10 milliseconds> |     |
Description
GuardtimerisusedinnodesrecoveringfromalocalfailuretoavoidloopsduetoearlierSignalFail(SF)
messagesthatmaybeinthering.
ERPS|47

The configuration specifies the guard timer duration in units of 10 ms. The timer period must be greater
than the maximum expected forwarding delay in which an R-APS message traverses the entire ring. The
default value is 50.

The no form of this command removes the configured value of the guard interval and sets it to the default
value of 50.

Command context

config-erps-ring-<ringid>

Parameters

<ringid>

Required, specifies the ID of the ring. Range: 1-239

<10 milliseconds>

Required, specifies the guard timer duration in units of 10 ms. Default: 50.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Specify the guard timer duration:

switch(config)# erps ring 3
switch(config-erps-ring-3)# guard-interval 100

Remove the configured value of the guard interval and set it to the default value of 50:

switch(config)# erps ring 3
switch(config-erps-ring-3)# no guard-interval

erps ring <ringid> hold-off-interval

Syntax

erps ring <ringid>

hold-off-interval <100 milliseconds>

Description

Specifies hold-off interval in units of 100 ms. If specified, a defect is not reported immediately. Instead, the
hold-off timer is started. On expiration of the timer, if the defect still exists, it is reported to protection
switching. The default value for hold-off timer is 0.

The no form of this command removes the configured value of the hold-off interval and sets it to the
default value of 0.

Command context

config-erps-ring-<ringid>

Parameters

<ringid>

Required, specifies the ID of the ring. Range: 1-239

<100 milliseconds>

AOS-CX 10.07 High Availability Guide | User Guide

48

Required, specifies the hold-off interval in units of 100 ms. Default: 0.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Specify the hold-off interval:

switch(config)# erps ring 3
switch(config-erps-ring-3)# hold-off-interval 100

Remove the configured value of the hold-off interval and set it to the default value of 0:

switch(config)# erps ring 3
switch(config-erps-ring-3)# no hold-off-interval

erps ring <ringid> instance

Syntax

erps ring <ringid>

instance <id>

Description

On a common ERPS network, a physical ring can be configured with a single ERPS ring, and only one blocked
port can be specified in the ring. When the ERPS ring is in normal state, the blocked port prohibits all service
packets from passing through. As a result, all service data is transmitted through one path over the ERPS
ring, and the other link on the blocked port becomes idle, leading to ineffective use of bandwidth.

To improve link use efficiency, logical rings can be configured in the same physical ring in the ERPS multi-
instance. A port may have different roles in different ERPS rings and different ERPS rings use different
control VLANs.

An ERPS ring must be configured with an ERP instance, and each ERP instance specifies a range of VLANs.
The topology calculated for a specific ERPS ring only takes effect in the ERPS ring. Different VLANs can use
separate paths, implementing traffic load balancing and link backup.

The no form of this command removes the instance of the ring.

Command context

config-erps-ring-<ringid>

Parameters

<ringid>

Required, specifies the ID of the ring. Range: 1-239

<id>

Required, specifies the ERPS ring instance identifier. Range: 1-2.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Create a ring instance:

ERPS | 49

| switch(config)#        |     | erps | ring | 3        |     |     |
| ---------------------- | --- | ---- | ---- | -------- | --- | --- |
| switch(config-ring-3)# |     |      |      | instance | 2   |     |
Removearinginstance:
| switch(config)#        |               | erps | ring     | 3           |                   |     |
| ---------------------- | ------------- | ---- | -------- | ----------- | ----------------- | --- |
| switch(config-ring-3)# |               |      |          | no instance | 2                 |     |
| erps                   | ring <ringid> |      | instance |             | <id> control-vlan |     |
Syntax
| erps | ring <ringid> |      |              |     |       |     |
| ---- | ------------- | ---- | ------------ | --- | ----- | --- |
|      | instance      | <id> | control-vlan |     | <vid> |     |
Description
Thiscommandaddsacontrol-channelVLANtoaringinstance.InanERPSring,thecontrolVLANshouldbe
usedonlytoforwardRAPSPDUsandnotservicepackets.AllthedevicesinanERPSringinstancemustbe
configuredwiththesamecontrolVLAN,anddifferentERPSringinstancesmustusedifferentcontrolVLANs.
Thenoformofthiscommandremovesthecontrol-channelVLANoftheringinstance.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<vid>
Required,VLANID.Range:1-4094.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Addacontrol-channelVLANtoaringinstance:
| switch(config)#                   |     | erps | ring | 3   |              |     |
| --------------------------------- | --- | ---- | ---- | --- | ------------ | --- |
| switch(config-erps-ring-3)#       |     |      |      |     | instance 2   |     |
| switch(config-erps-ring-3-inst-2) |     |      |      |     | control-vlan | 10  |
Removethecontrol-channelVLANoftheringinstance:
| switch(config)#                   |               | erps | ring     | 3   |                  |     |
| --------------------------------- | ------------- | ---- | -------- | --- | ---------------- | --- |
| switch(config-erps-ring-3)#       |               |      |          |     | instance 2       |     |
| switch(config-erps-ring-3-inst-2) |               |      |          |     | no control-vlan  |     |
| erps                              | ring <ringid> |      | instance |     | <id> description |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 50

Syntax
| erps | ring <ringid> |      |             |     |        |     |
| ---- | ------------- | ---- | ----------- | --- | ------ | --- |
|      | instance      | <id> | description |     | <line> |     |
Description
Thiscommandaddsdescriptiveinformationtohelpadministratorsandoperatorsunderstandthepurpose
ofaringinstance.1-64printableASCIIcharactersareallowed.
Thenoformofthiscommandremovestheringinstancedescription.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<line>
Required,descriptiveinformationabouttheringinstance.1-64printableASCIIcharactersallowed.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Addringinstancedescription:
| switch(config)#                   |     | erps | ring | 3        |             |                  |
| --------------------------------- | --- | ---- | ---- | -------- | ----------- | ---------------- |
| switch(config-erps-ring-3)#       |     |      |      | instance | 2           |                  |
| switch(config-erps-ring-3-inst-2) |     |      |      |          | description | HPE RnD DataVlan |
Removeringinstancedescription:
| switch(config)#                   |               | erps | ring     | 3        |                |     |
| --------------------------------- | ------------- | ---- | -------- | -------- | -------------- | --- |
| switch(config-erps-ring-3)#       |               |      |          | instance | 2              |     |
| switch(config-erps-ring-3-inst-2) |               |      |          |          | no description |     |
| erps                              | ring <ringid> |      | instance |          | <id> enable    |     |
Syntax
| erps | ring <ringid> |      |        |     |     |     |
| ---- | ------------- | ---- | ------ | --- | --- | --- |
|      | instance      | <id> | enable |     |     |     |
Description
Thisconfigurationenablesprotectionswitchingonthegiveninstanceofthering.Itisdisabledbydefault.
Thenoformofthiscommanddisablesprotectionswitchingonthegiveninstanceofthering.
Commandcontext
config-erps-ring-<ringid>
Parameters
ERPS|51

<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enableprotectionswitchingonthegiveninstanceofthering:
| switch(config)#                   |     | erps ring | 3        |        |
| --------------------------------- | --- | --------- | -------- | ------ |
| switch(config-erps-ring-3)#       |     |           | instance | 2      |
| switch(config-erps-ring-3-inst-2) |     |           |          | enable |
Disableprotectionswitchingonthegiveninstanceofthering:
| switch(config)#                   |               | erps ring | 3        |                      |
| --------------------------------- | ------------- | --------- | -------- | -------------------- |
| switch(config-erps-ring-3)#       |               |           | instance | 2                    |
| switch(config-erps-ring-3-inst-2) |               |           |          | no enable            |
| erps                              | ring <ringid> | instance  |          | <id> protected-vlans |
Syntax
| erps | ring <ringid> |                      |     |            |
| ---- | ------------- | -------------------- | --- | ---------- |
|      | instance      | <id> protected-vlans |     | <vid-list> |
Description
ThiscommandspecifiesthesetofVLANsthatareprotectedbythisringinstance.
ThenoformofthiscommandremovesasetofVLANsthatareprotectedbythisringinstance.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<vd-list>
Required,rangeofVLANstobeprotectedbythisringinstance.Range:1-4094.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SpecifyasetofVLANsthatareprotectedbythisringinstance:
AOS-CX10.07HighAvailabilityGuide|UserGuide 52

| switch(config)#                   |     | erps ring | 3        |                 |     |         |
| --------------------------------- | --- | --------- | -------- | --------------- | --- | ------- |
| switch(config-erps-ring-3)#       |     |           | instance |                 | 2   |         |
| switch(config-erps-ring-3-inst-2) |     |           |          | protected-vlans |     | 1,10-50 |
RemoveasetofVLANsthatareprotectedbythisringinstance:
| switch(config)#                   |     | erps ring | 3        |     |                 |       |
| --------------------------------- | --- | --------- | -------- | --- | --------------- | ----- |
| switch(config-erps-ring-3)#       |     |           | instance |     | 2               |       |
| switch(config-erps-ring-3-inst-2) |     |           |          | no  | protected-vlans | 11,13 |
erps ring <ringid> instance <id> protection-switch {{manual|force}
<port0>|<port1>}
Syntax
erps ring <ringid> instance <id> protection-switch {{manual|force} <port0>|<port1>}
Description
Blocksaspecificringinterfaceinoneofthetwofollowingways:
n Force:Theswitchblocksaspecificringinterfaceregardlessoftheprotectionswitchingstateofthering
instance.
n Manual:Theswitchblocksaspecificringinterfaceifnootherprotectionswitcheventisactiveonthering
instance.
Theusercanverifywhethertheprotection-switchissuccessfulbyverifyingthestatusofinstanceandportstate
overwhichthiscommandisexecuted.
| switch# | erps     | ring 1 instance |          | 1 protection-switch |     | force port0 |
| ------- | -------- | --------------- | -------- | ------------------- | --- | ----------- |
| switch# | show     | erps status     |          |                     |     |             |
| Status  | for ERPS | Ring 1          | Instance | 1:                  |     |             |
====================================
| Ring ID        |           |          |     | : 1             |         |     |
| -------------- | --------- | -------- | --- | --------------- | ------- | --- |
| Instance       | ID        |          |     | : 1             |         |     |
| Port0          |           |          |     | : 1/1/5         | (Block) |     |
| Port1          |           |          |     | : 1/1/6         | (Up)    |     |
| Node Role      | (RPL)     |          |     | : Owner         | (port0) |     |
| Control        | VLAN      |          |     | : 50            |         |     |
| Protected      | VLAN      |          |     | : 1-49          |         |     |
| Subring        | (TCN)     |          |     | : No (No)       |         |     |
| Revertive      | Operation |          |     | : Revertive     |         |     |
| MEG Level      |           |          |     | : 7             |         |     |
| Transmission   |           | Interval |     | : 5 sec         |         |     |
| Guard Interval |           |          |     | : 0 sec         | 500 ms  |     |
| Hold-Off       | Interval  |          |     | : 0 sec         | 0 ms    |     |
| WTR Interval   |           |          |     | : 1 min         |         |     |
| Status         |           |          |     | : Forced-switch |         |     |
| Oper Down      | Reason    |          |     | : None          |         |     |
Commandcontext
Operator(>)orManager(#)
Parameters
ERPS|53

<ringid>

Required, specifies the ID of the ring. Range: 1-239.

<id>

Required, specifies the ID of the ring instance. Range: 1-2.

manual

A type of protection switch event in which the switch blocks a specific ring interface if no other protection
switch event is active on the ring instance.

force

A type of protection switch even in which the switch blocks a specific ring interface regardless of the
protection switching state of the ring instance.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Block ring 3, interface 2, port 0 if no other protection switch event is active on the ring instance:

switch# erps ring 3 instance 2 protection-switch manual port0

Block ring 3, instance 2, regardless of the protection switching state of the ring instance:

switch# erps ring 3 instance 2 protection-switch force port1

erps ring <ringid> instance <id> revertive

Syntax

erps ring <ringid> instance <id> revertive

Description

Configures the default revertive mode of operation for an ERPS ring. In revertive operation, after the
conditions causing protection switching are cleared, traffic channels are restored to the recovered link
blocking the RPL. This configuration is meaningful only on the RPL node.

The no form of this command configures non-revertive mode of operation for an ERPS ring. In non-revertive
operation, the traffic channels continue to use the RPL, if it has not failed, after conditions causing
protection switching are cleared. This configuration is meaningful only on the RPL node.

Command context

config-erps-ring-<ringid>

Parameters

<ringid>

Required, specifies the ID of the ring. Range: 1-239

<id>

Required, specifies the ERPS ring instance identifier. Range: 1-2.

Authority

Administrators or local user group members with execution rights for this command.

AOS-CX 10.07 High Availability Guide | User Guide

54

Examples
ConfiguringthedefaultrevertivemodeofoperationforERPSring3,instance2:
| switch(config)#                    | erps | ring 3   |           |
| ---------------------------------- | ---- | -------- | --------- |
| switch(config-erps-ring-3)#        |      | instance | 2         |
| switch(config-erps-ring-3-inst-2)# |      |          | revertive |
Configuringnon-revertivemodeofoperationforERPSring3,instance2:
| switch(config)#                    | erps     | ring 3   |              |
| ---------------------------------- | -------- | -------- | ------------ |
| switch(config-erps-ring-3)#        |          | instance | 2            |
| switch(config-erps-ring-3-inst-2)# |          |          | no revertive |
| erps ring                          | <ringid> | instance | <id> role    |
Syntax
| erps ring | <ringid> |                               |     |
| --------- | -------- | ----------------------------- | --- |
| instance  | <id>     | role <rpl-owner|rpl-neighbor> |     |
Description
InERPS,thereisacentralnodecalledRPLOwnerNodewhichblocksoneoftheportstoensurethatthereis
noloopformedfortheEthernettraffic.ThelinkblockedbytheRPLownernodeiscalledtheRingProtection
LinkorRPL.ThenodeattheotherendoftheRPLisknownasRPLNeighborNode.ItusesR-APScontrol
messagestocoordinatetheactivitiesofswitchingon/offtheRPLlink.
Thiscommandspecifiestheroleofthenodeasownerorneighbor.
Thenoformofthiscommandremovestheconfigurationofthenoderolefromtheinstance.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<rpl-owner>
BlockstrafficatoneendoftheRPL.TheblockedendsendsoutperiodicR-APS.
<rpl-neighbor>
BlockstrafficatoneendoftheRPL.TheblockedenddoesnotgenerateperiodicR-APS.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Specifytheroleofthenodeasowner:
ERPS|55

| switch(config)#                   | erps | ring 3   |                |
| --------------------------------- | ---- | -------- | -------------- |
| switch(config-erps-ring-3)#       |      | instance | 2              |
| switch(config-erps-ring-3-inst-2) |      |          | role rpl-owner |
Specifytheroleofthenodeasneighbor:
| switch(config)#                   | erps | ring 3   |                    |
| --------------------------------- | ---- | -------- | ------------------ |
| switch(config-erps-ring-3)#       |      | instance | 3                  |
| switch(config-erps-ring-3-inst-2) |      |          | role rpl-neighbour |
Removetheconfigurationofthenoderolefromtheinstance:
| switch(config)#                   | erps     | ring 3   |          |
| --------------------------------- | -------- | -------- | -------- |
| switch(config-erps-ring-3)#       |          | instance | 2        |
| switch(config-erps-ring-3-inst-2) |          |          | no role  |
| erps ring                         | <ringid> | instance | <id> rpl |
Syntax
| erps ring | <ringid> |                   |     |
| --------- | -------- | ----------------- | --- |
| instance  | <id>     | rpl <port0|port1> |     |
Description
InERPS,thereisacentralnodecalledRPLOwnerNodewhichblocksoneoftheportstoensurethatthereis
noloopformedfortheEthernettraffic.ThelinkblockedbytheRPLownernodeiscalledtheRingProtection
LinkorRPL.ThenodeattheotherendoftheRPLisknownasRPLNeighborNode.ItusesR-APScontrol
messagestocoordinatetheactivitiesofswitchingtheRPLlinkonandoff.
ThiscommandspecifieswhichoftheERPSringportsistheRPL.
ThenoformofthiscommandremovestheRPLportconfigurationfromtheERPSringinstance.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<port0>
Required,configureport0tobeRPLportinthisERPSringinstance.
<port1>
Required,configureport1tobeRPLportinthisERPSringinstance.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configureport0tobeRPLportinthisERPSringinstance:
AOS-CX10.07HighAvailabilityGuide|UserGuide 56

| switch(config)#                   | erps | ring | 3        |           |
| --------------------------------- | ---- | ---- | -------- | --------- |
| switch(config-erps-ring-3)#       |      |      | instance | 2         |
| switch(config-erps-ring-3-inst-2) |      |      | role     | rpl-owner |
| switch(config-erps-ring-3-inst-2) |      |      | rpl      | port0     |
Configureport1tobeRPLportinthisERPSringinstance:
| switch(config)#                   | erps | ring | 3        |               |
| --------------------------------- | ---- | ---- | -------- | ------------- |
| switch(config-erps-ring-3)#       |      |      | instance | 3             |
| switch(config-erps-ring-3-inst-2) |      |      | role     | rpl-neighbour |
| switch(config-erps-ring-3-inst-2) |      |      | rpl      | port1         |
RemovetheRPLportconfigurationfromtheERPSringInstance:
| switch(config)#                   | erps     | ring      | 3        |           |
| --------------------------------- | -------- | --------- | -------- | --------- |
| switch(config-erps-ring-3)#       |          |           | instance | 2         |
| switch(config-erps-ring-3-inst-2) |          |           | no       | rpl port0 |
| erps ring                         | <ringid> | meg-level |          |           |
Syntax
| erps ring | <ringid> |     |     |     |
| --------- | -------- | --- | --- | --- |
meg-level <-0-7>
Description
TheR-APSmessagestransmittedbyERPStaketheformofOAMPDUsasdefinedinG.8013.EachOAMPDU
istransmittedataspecifiedlevelknownastheMaintenanceEntityGroup(MEG)level.Thiscommand
configuresthelevelwithwhichtheERPSpacketsmustbetransmitted.
ThenoformofthiscommandremovestheconfiguredMEGlevelandsetsittothedefaultvalueof7.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<0-7>
Required,specifiesthemeg-level.Range:0-7.Default:7.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Specifythemeg-level:
| switch(config)#             | erps | ring | 3         |     |
| --------------------------- | ---- | ---- | --------- | --- |
| switch(config-erps-ring-3)# |      |      | meg-level | 4   |
Removetheconfiguredmeg-levelandsetittothedefaultvalueof7:
ERPS|57

| switch(config)#             | erps     | ring        | 3            |     |
| --------------------------- | -------- | ----------- | ------------ | --- |
| switch(config-erps-ring-3)# |          |             | no meg-level |     |
| erps ring                   | <ringid> | parent-ring |              |     |
Syntax
| erps ring | <ringid> |     |     |     |
| --------- | -------- | --- | --- | --- |
parent-ring <ringid>
Description
Thiscommandassociatesasub-ringtoaparent-ringandisrequiredforthesub-ringtonotifytheparent-
ringonchangeintopology.
Thenoformofthiscommandremovestheparentringidentifier.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<ringid>
Required,specifiestheIDoftheparent-ring.Range:1-239
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Associateasub-ringtoaparent-ring:
| switch(config)#             | erps | ring | 3           |     |
| --------------------------- | ---- | ---- | ----------- | --- |
| switch(config-erps-ring-3)# |      |      | parent-ring | 2   |
Removeaparent-ringidentifier:
| switch(config)#             | erps     | ring     | 3              |     |
| --------------------------- | -------- | -------- | -------------- | --- |
| switch(config-erps-ring-3)# |          |          | no parent-ring | 2   |
| erps ring                   | <ringid> | sub-ring |                |     |
Syntax
| erps ring | <ringid> |     |     |     |
| --------- | -------- | --- | --- | --- |
sub-ring
Description
Thiscommandistoconfigureasub-ring.Ifnotspecified,theringisamajor-ring.
Thenoformofthiscommandremovesthesub-ringconfigurationoftheringandconfiguresittobeamajor-
ring.
AOS-CX10.07HighAvailabilityGuide|UserGuide 58

Command context

config-erps-ring-<ringid>

Parameters

<ringid>

Required, specifies the ID of the ring. Range: 1-239

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configure a sub-ring:

switch(config)# erps ring 2
switch(config-erps-ring-2)# sub-ring

Remove the sub-ring configuration from ring 2 and configure it to be a major-ring:

switch(config)# erps ring 2
switch(config-erps-ring-2)# no sub-ring

erps ring <ringid> tcn-propogation

Syntax

erps ring <ringid>

tcn-propogation

Description

This command is to configure a sub-ring interconnection node to pass a topology change notification to the
ring instance for the parent ring whenever the topology of the sub-ring changes. The parent ring instance
performs a Forwarding Database (FDB) flush and sends a protocol message to ensure that other nodes on
the parent ring also perform an FDB flush.

The no form of this command disables topology change notifications.

Command context

config-erps-ring-<ringid>

Parameters

<ringid>

Required, specifies the ID of the ring. Range: 1-239

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configure topology change notifications:

ERPS | 59

| switch(config)# | erps | ring | 2   |     |
| --------------- | ---- | ---- | --- | --- |
switch(config-erps-ring-2)#
tcn-propogation
Disabletopologychangenotifications:
| switch(config)#             | erps     | ring                  | 2                  |     |
| --------------------------- | -------- | --------------------- | ------------------ | --- |
| switch(config-erps-ring-2)# |          |                       | no tcn-propogation |     |
| erps ring                   | <ringid> | transmission-interval |                    |     |
Syntax
| erps ring             | <ringid> |     |           |     |
| --------------------- | -------- | --- | --------- | --- |
| transmission-interval |          |     | <seconds> |     |
Description
SpecifiestheR-APSperiodictransmissionintervalinunitsofseconds.Defaultis5seconds.
Thenoformofthiscommandremovestheconfiguredvalueofthetransmissionintervalandsetsittothe
defaultvalueof5seconds.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<seconds>
Required,specifiestheR-APSperiodictransmissionintervalinunitsofseconds.Range:5seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SpecifytheR-APSperiodictransmissionintervalas10seconds:
| switch(config)#             | erps | ring | 3                     |     |
| --------------------------- | ---- | ---- | --------------------- | --- |
| switch(config-erps-ring-3)# |      |      | transmission-interval | 10  |
Removetheconfiguredvalueofthetransmissionintervalandsetittothedefaultvalueof5seconds:
| switch(config)#             | erps     | ring         | 3                        |     |
| --------------------------- | -------- | ------------ | ------------------------ | --- |
| switch(config-erps-ring-3)# |          |              | no transmission-interval |     |
| erps ring                   | <ringid> | wtr-interval |                          |     |
Syntax
| erps ring    | <ringid> |           |     |     |
| ------------ | -------- | --------- | --- | --- |
| wtr-interval |          | <minutes> |     |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 60

Description

The RPL owner node uses a delay timer before initiating an RPL block in case of both revertive mode of
operation or before reverting to idle state after clearing operator commands (FS, MS).

The Wait to Restore (WTR) timer can be configured in 1-minute increments up to 12 minutes. The default
value is 5 minutes. When recovering from an SF, the delay timer must be long enough to allow the
recovering network to become stable. In the default revertive mode of operation, the WTR timer is used to
prevent frequent operation of protection switching due to intermittent SF defects.

The no form of this command removes the configured value of the wtr-interval and sets it to the default
value of 5 minutes.

Command context

config-erps-ring-<ringid>

Parameters

<ringid>

Required, specifies the ID of the ring. Range: 1-239

<seconds>

Required, specifies the wtr-interval in minutes. Range: 1-12. Default: 5.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Specify the wtr-interval:

switch(config)# erps ring 3
switch(config-erps-ring-3)# wtr-interval 7

Remove the configured value of the wtr-interval and set it to the default value of 5 minutes:

switch(config)# erps ring 3
switch(config-erps-ring-3)# no wtr-interval

show erps statistics

Syntax

show erps statistics [ring <ringid>] [instance <id> [port0|port1]]

Description

This command displays ERPS statistics. The statistics can be displayed for the ring, the instance, or the
instance ports.

Command context

Operator (>) or Manager (#)

Parameters

<ringid>

Optional, specifies the ID of the ring. Range: 1-239.

ERPS | 61

<id>
Optional,specifiestheIDoftheringinstance.Range:1-2.
<port0>
Optional,specifiestheringmemberport0.
<port1>
Optional,specifiestheringmemberport1.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
| switch#    | show erps statistics | ring       | 1   |
| ---------- | -------------------- | ---------- | --- |
| Statistics | for ERPS ring        | 1 instance | 1:  |
======================================
|                | Port0         |            | Port1        |
| -------------- | ------------- | ---------- | ------------ |
|                | -----         |            | -----        |
| Local Failures | 4             |            | 1            |
| R-APS          | Port0(Tx/Rx)  |            | Port1(Tx/Rx) |
| -----          | ------------  |            | ------------ |
| NR             | 1/1           |            | 1/1          |
| NR,RB          | 0/1           |            | 0/1          |
| SF             | 1/0           |            | 1/0          |
| MS             | 0/0           |            | 0/10         |
| FS             | 30/0          |            | 0/0          |
| Statistics     | for ERPS ring | 1 instance | 2:           |
======================================
|                | Port0                |            | Port1        |
| -------------- | -------------------- | ---------- | ------------ |
|                | -----                |            | -----        |
| Local Failures | 4                    |            | 1            |
| R-APS          | Port0(Tx/Rx)         |            | Port1(Tx/Rx) |
| -----          | ------------         |            | ------------ |
| NR             | 1/1                  |            | 1/1          |
| NR,RB          | 0/1                  |            | 0/1          |
| SF             | 1/0                  |            | 1/0          |
| MS             | 0/0                  |            | 0/10         |
| FS             | 30/0                 |            | 0/0          |
| switch#        | show erps statistics |            |              |
| Statistics     | for ERPS Ring        | 1 Instance | 1 :          |
==========================================
|                | Port0        |     | Port1        |
| -------------- | ------------ | --- | ------------ |
|                | -----        |     | -----        |
| Local Failures | 4            |     | 1            |
| R-APS          | Port0(Tx/Rx) |     | Port1(Tx/Rx) |
| -------        | ----------   |     | -----------  |
| NR             | 33/9         |     | 33/9         |
| NR,RB          | 58/0         |     | 58/0         |
| SF             | 4/0          |     | 4/0          |
| MS             | 0/0          |     | 0/0          |
| FS             | 0/0          |     | 0/0          |
| show erps      | status       |     |              |
AOS-CX10.07HighAvailabilityGuide|UserGuide 62

Syntax

show erps status [ring <ringid>] [instance <id>]

Description

This command displays detailed information about a specific ring or all instances of a ring.

The ring instance may be in one of the following states:

n Idle: The ring instance is operational.

n Initializing: The ring instance is not operational.

n Protection: Protection switching has been triggered by a local or remote link failure.

n Pending: Pending clearance of a previous protection switch.

n Down: Ring instance is not active.

n Manual-switch: Manual protection switching triggered by Admin-down.

n Force-switch: Forced protection switching triggered by admin.

A ring instance has the following reasons for "down" state:

n Disabled: Ring instance is administratively disabled.

n

n

Inconsistent Port Config: The same port is configured as port0 and port1 or RPL port is configured by
Admin-down.

Incomplete Port Config: Only one or no ring port is configured.

n Protected VLANs Not Configured: Protected VLAN list is empty.

n Control VLAN Not Configured: Control VLAN is not configured.

The ring ports can be in one of the following states:

n Up: Port forwards control and data traffic.

n Blocked: Port blocks both control and data traffic.

Command context

Operator (>) or Manager (#)

Parameters

<ringid>

Optional, specifies the ID of the ring. Range: 1-239.

<id>

Optional, specifies the ID of the ring instance. Range: 1-2.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Show ERPS status for ring 1 and instance 1:

Status for ERPS Ring 1 Instance 1
=================================
: 1
Ring ID
: ring_1
Ring description

ERPS | 63

| Instance       | ID          |     | : 1               |           |            |
| -------------- | ----------- | --- | ----------------- | --------- | ---------- |
| Instance       | description |     | : inst_1          |           |            |
| Port0          |             |     | : 1/0/1 (Blocked) |           |            |
| Port1          |             |     | : 1/0/2 (Up)      |           |            |
| Node Role      | (RPL)       |     | : Owner (Port0)   |           |            |
| Control        | VLAN        |     | : 100             |           |            |
| Protected      | VLAN        |     | : None            |           |            |
| Subring        | (TCN)       |     | : Yes (Yes)       |           |            |
| Revertive      | Operation   |     | : Revertive       |           |            |
| MEG Level      |             |     | : 1               |           |            |
| Transmission   | Interval    |     | : 5 sec           |           |            |
| Guard Interval |             |     | : 500 ms          |           |            |
| Hold-Off       | Interval    |     | : 1 sec           |           |            |
| WTR Interval   |             |     | : 5 min           |           |            |
| Status         |             |     | : Initializing    |           |            |
| Oper Down      | Reason      |     | : Protected       | Vlans Not | Configured |
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
| Revertive        | Operation   |     | : Revertive       |     |     |
| MEG Level        |             |     | : 1               |     |     |
| Transmission     | Interval    |     | : 5 sec           |     |     |
| Guard Interval   |             |     | : 500 ms          |     |     |
| Hold-Off         | Interval    |     | : 1 sec           |     |     |
| WTR Interval     |             |     | : 5 min           |     |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 64

| Status    |         | : Admin-Down |     |     |     |
| --------- | ------- | ------------ | --- | --- | --- |
| Oper Down | Reason  | : None       |     |     |     |
| show erps | summary |              |     |     |     |
Syntax
show erps summary
Description
ThiscommanddisplaysasummaryoftheERPSconfigurationandstatefortheERPSringinstances.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
| switch# | show erps summary |     |     |     |     |
| ------- | ----------------- | --- | --- | --- | --- |
ERPS Summary
============
| Flags:       | R - RPL, M - Major | Ring, S | - Sub Ring, | T - TCN | Enabled |
| ------------ | ------------------ | ------- | ----------- | ------- | ------- |
|              | * - RPL port       |         |             |         |         |
| Per-Instance | Summary            |         |             |         |         |
====================
| Ring Instance | Port0  | Port1  | Status        |     | Flags |
| ------------- | ------ | ------ | ------------- | --- | ----- |
| ---- -------- | -----  | -----  | ------        |     | ----- |
| 1 1           | 1/1/1  | *1/1/2 | Pending       |     | R,M   |
| 1 2           | 1/1/1  | 1/1/2  | Idle          |     | M     |
| 2 1           | *1/1/3 | -      | Protection    |     | R,S,T |
| 2 2           | 1/1/3  | -      | Admin-down    |     | S,T   |
| 3 1           | 1/1/4  | 1/1/5  | Manual-switch |     | M     |
| 3 2           | 1/1/4  | 1/1/5  | Force-switch  |     | M     |
ERPS|65

Support and Other Resources

Chapter 5

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

AOS-CX 10.07 High Availability Guide | User Guide

66

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

Support and Other Resources | 67