AOS-CX Virtual Switching
Framework (VSF) Guide for
6200, 6300 Switch Series

Published: April 2023
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

| 2

Contents
Contents
| Contents                            |                    |                  | 3   |
| ----------------------------------- | ------------------ | ---------------- | --- |
| About                               | this document      |                  | 5   |
| Applicableproducts                  |                    |                  | 5   |
| Latestversionavailableonline        |                    |                  | 5   |
| Commandsyntaxnotationconventions    |                    |                  | 5   |
| Abouttheexamples                    |                    |                  | 6   |
| Identifyingswitchportsandinterfaces |                    |                  | 7   |
| Introduction                        |                    |                  | 9   |
| Terminology                         |                    |                  | 9   |
| Featuredescription                  |                    |                  | 9   |
| Connectiontopology                  |                    |                  | 10  |
| Feature                             | overview           |                  | 11  |
| VSFbehavior                         |                    |                  | 11  |
| Onevirtualdevice                    |                    |                  | 11  |
| Interoperation                      |                    |                  | 14  |
| Linkaggregation                     |                    |                  | 15  |
| Stack                               | management         |                  | 17  |
| Consoles                            |                    |                  | 17  |
| Managementinterface                 |                    |                  | 17  |
| VSFconfiguration                    |                    |                  | 17  |
|                                     | Membernumber       |                  | 17  |
|                                     | AccesstoVSFmembers |                  | 17  |
|                                     | VSFlinks           |                  | 18  |
|                                     | Memberprovisioning |                  | 18  |
|                                     | Secondarymember    |                  | 18  |
|                                     | Memberremove       |                  | 18  |
| Automatedimagesync                  |                    |                  | 19  |
| Reboot                              |                    |                  | 19  |
| Memberaddition                      |                    |                  | 19  |
| Memberreplacement                   |                    |                  | 20  |
| Configuring                         | a VSF              | stack            | 21  |
| Prerequisites                       |                    |                  | 21  |
| Forminganeight-memberringsetup      |                    |                  | 21  |
| Misconfigurationrecovery            |                    |                  | 24  |
| Failure                             | and recovery       |                  | 25  |
| Stacksplit                          |                    |                  | 25  |
| Managementinterfacesplitdetection   |                    |                  | 25  |
| VSF recomendations                  |                    | and restrictions | 28  |
| VSF commands                        |                    |                  | 30  |
| vsfmember                           |                    |                  | 30  |
| member                              |                    |                  | 31  |
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300Switch
3
Series| UserGuide

| type                  |                    |           | 32  |
| --------------------- | ------------------ | --------- | --- |
| link                  |                    |           | 33  |
| vsfsplit-detect       |                    |           | 35  |
| vsfsecondary-member   |                    |           | 36  |
| vsfrenumber-to        |                    |           | 36  |
| vsfmemberreboot       |                    |           | 37  |
| interface             |                    |           | 38  |
| shutdown              |                    |           | 38  |
| showvsf               |                    |           | 39  |
| showvsfdetail         |                    |           | 40  |
| showvsflink           |                    |           | 41  |
| showvsfmember         |                    |           | 42  |
| showvsftopology       |                    |           | 42  |
| Frequently            | asked              | questions | 44  |
| Support               | and other          | resources | 50  |
| AccessingArubaSupport |                    |           | 50  |
| Accessingupdates      |                    |           | 50  |
|                       | ArubaSupportPortal |           | 50  |
|                       | MyNetworking       |           | 51  |
| Warrantyinformation   |                    |           | 51  |
| Regulatoryinformation |                    |           | 51  |
| Documentationfeedback |                    |           | 51  |
Contents|4

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

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
documentation, see the links provided in Support and other resources.

Command syntax notation conventions

Convention

Usage

example-text

Identifies commands and their options and operands, code examples,
filenames, pathnames, and output displayed in a command window. Items
that appear like the example text in the previous column are to be entered
exactly as shown and are required unless enclosed in brackets ([ ]).

example-text

In code and screen examples, indicates text entered by a user.

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series | User Guide

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

Variable information in CLI prompts

About this document | 6

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

On the 6100 Switch Series

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

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
member 1.

On the 83xx Switch Series

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series User Guide

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

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

About this document | 8

Chapter 2

Introduction

Introduction

Terminology

Table 1: Acronyms used in this book

Term

Definition

VSF

Virtual Switching Framework

L2

L3

SKU

FRU

Layer 2 of the OSI 7-layer model

Layer 3 of the OSI 7-layer model

Stock Keeping Unit

Field Replaceable Unit

ASIC

Application-Specific-Integrated Circuit

L-Agg

Link Aggregation

CLI

Command Line Interface

Table 2: Role types

Role

Primary

Definition

The primary member is member number 1.

Secondary

The configured secondary member.

Master

Standby

Controls VSF administration and control plane.

Standby management and under control of the master; synchronizes control plan with

the master.

Member

All devices in the stack other than the master and standby are called member switches.

The member switch does not run any networking protocols and has no states. The

interfaces on this switch are directly controlled and programmed by the master switch.

Feature description
Virtual Switching Framework, or VSF, defines a virtual switch, comprising multiple individual physical
switches, interconnected through standard Ethernet links. These physical switches will operate with one

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series | User Guide

9

control plane, visible to peers as a virtual switch stack. This composition simplifies management and
provides the capability to scale the stack.

On-demand scalability in the access layer allows the user to increase the number of ports on a stack as
per needs, without having to manage a new switch. The same stack can scale up or down to match the
requirements.

n 6200F: VSF allows stacks to be formed using any combination of SKUs of the 6200 family. Up to 8

member switches will be allowed. Connections between the switches must use 10G links.

n 6300: VSF allows stacks to be formed using any combination of SKUs of the 6300 family. Up to 10
member switches will be allowed. Connections between the switches must use 10G, 25G, or 50G
links. All VSF links in a stack should operate at the same speed.

Connection topology
VSF supports up to 8 member stacks (for 6200F devices) or 10 member stacks (for 6300 devices) in ring
and chain topology.

Figure 1 Chain topology

Figure 2 Ring topology

Ring is the recommended deployment topology. It inherently provides resiliency against a single failure
of a link or switch.

Introduction | 10

Chapter 3

Feature overview

Feature overview

VSF is always enabled on supported switches. Within the stack, one switch is the Master that runs all
control plane software and manages the ASICs of all stack members. Any switch apart from primary can
be configured as Standby switch.

VSF behavior
Each stack member must have a unique member number. When deploying a stack, ensure that each
member has a distinct number by renumbering the switches to the appropriate member numbers.
Stack formation will fail if there is a member number conflict.

n The primary member will become Master and the secondary member will become Standby under

normal circumstances.

n The primary member is member number 1. This setting is not configurable and 1 is the default. A

factory-default switch boots up as a VSF-enabled switch with a member number of 1.

n The secondary member number is user configurable, and there is no default secondary member. It is
recommended that the customer configures a secondary member in the stack, since a stack with a
standby offers resiliency and high-availability.

n No members other than primary and secondary members can become Master or Standby of the

stack.

In a standard deployment, uplinks should be from primary and secondary. The management interface from

primary and secondary members should be connected to the management network, providing management

connectivity to the current master.

One virtual device
Once the VSF stack is formed, all interconnected switches operate as a single virtual switch with a single
control plane. All interfaces of all switches in the stack are available for configuration and management.

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series | User Guide

11

Figure 3 Onevirtualdeviceexampletopology
| switch#         | show vsf |                     |        |     |     |
| --------------- | -------- | ------------------- | ------ | --- | --- |
| MAC Address     |          | : 08:97:34:b0:0e:00 |        |     |     |
| Secondary       |          | : 2                 |        |     |     |
| Topology        |          | : Ring              |        |     |     |
| Status          |          | : No Split          |        |     |     |
| Split Detection | Method   | : None              |        |     |     |
| Mbr MAC         | Address  | Type                | Status |     |     |
ID
| --- ------------------- |     | -------------- | ----------------- |     |     |
| ----------------------- | --- | -------------- | ----------------- | --- | --- |
| 1 08:97:34:b0:0e:00     |     | JL666A         | Master            |     |     |
| 2 08:97:34:b1:43:00     |     | JL665A         | Standby           |     |     |
| 3 08:97:34:b7:cc:00     |     | JL663A         | Member            |     |     |
| 4 08:97:34:b6:42:00     |     | JL662A         | Member            |     |     |
Interfaceswillbenumberedasnotedinthefollowingtable.
|      | Member Num- |      |      |     |     |
| ---- | ----------- | ---- | ---- | --- | --- |
| Name |             | Slot | Port |     |     |
ber
| 1/1/1  | 1   | 1   | 1   |     |     |
| ------ | --- | --- | --- | --- | --- |
| 2/1/14 | 2   | 1   | 14  |     |     |
| 8/1/12 | 8   | 1   | 12  |     |     |
Slotnumberisalwaysfixedas1.Allinterfacesareavailableforconfiguration.
| switch# | show interfaces | brief |     |     |     |
| ------- | --------------- | ----- | --- | --- | --- |
----------------------------------------------------------------------------------
| Port | Native Mode | Type | Enabled Status | Reason | Speed  |
| ---- | ----------- | ---- | -------------- | ------ | ------ |
|      | VLAN        |      |                |        | (Mb/s) |
----------------------------------------------------------------------------------
Featureoverview|12

| 1/1/1 | 10 access | SFP+DA3 | yes up  |                   | 10000 |
| ----- | --------- | ------- | ------- | ----------------- | ----- |
| 1/1/2 | -- routed | --      | no down | No XCVR installed | --    |
| 1/1/3 | -- routed | --      | no down | No XCVR installed | --    |
| 1/1/4 | -- routed | --      | no down | No XCVR installed | --    |
| 1/1/5 | -- routed | --      | no down | No XCVR installed | --    |
| 1/1/6 | -- routed | --      | no down | No XCVR installed | --    |
...
| 1/1/33 | -- routed | --      | no down | No XCVR installed | --    |
| ------ | --------- | ------- | ------- | ----------------- | ----- |
| 1/1/34 | -- routed | --      | no down | No XCVR installed | --    |
| 1/1/35 | -- routed | --      | no down | No XCVR installed | --    |
| 1/1/36 | -- routed | --      | no down | No XCVR installed | --    |
| 2/1/1  | 10 access | SFP+DA3 | yes up  |                   | 10000 |
| 2/1/2  | -- routed | --      | no down | No XCVR installed | --    |
| 2/1/3  | -- routed | --      | no down | No XCVR installed | --    |
| 2/1/4  | -- routed | --      | no down | No XCVR installed | --    |
...
| 2/1/35 | -- routed | --  | no down | No XCVR installed | --  |
| ------ | --------- | --- | ------- | ----------------- | --- |
| 2/1/36 | -- routed | --  | no down | No XCVR installed | --  |
AsinglecontrolplaneoperatesfortheentireVSFstack.
| switch# | show run       |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- |
| Current | configuration: |     |     |     |     |
!
| !Version          | ArubaOS-CX FL.10.04.0001AQ |     |     |     |     |
| ----------------- | -------------------------- | --- | --- | --- | --- |
| !export-password: | default                    |     |     |     |     |
cli-session
| timeout | 0   |     |     |     |     |
| ------- | --- | --- | --- | --- | --- |
!
!
!
!
| ssh server | vrf default |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- |
| ssh server | vrf mgmt    |     |     |     |     |
!
!
!
!
!
vlan 1
spanning-tree
| interface | mgmt |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
no shutdown
ip dhcp
| interface | 1/1/1 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
no routing
| vlan      | access 1 |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
| interface | 1/1/2    |     |     |     |     |
no shutdown
no routing
| vlan | access 1 |     |     |     |     |
| ---- | -------- | --- | --- | --- | --- |
interface
1/1/3
no shutdown
no routing
| vlan      | access 1 |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
| interface | 1/1/4    |     |     |     |     |
no shutdown
no routing
| vlan      | access 1 |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
| interface | 1/1/5    |     |     |     |     |
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeriesUserGuide 13

no shutdown
no routing
vlan access 1

interface 1/1/6
no shutdown
no routing
vlan access

...
...
interface 2/1/1
no shutdown
no routing
vlan access
interface 2/1/2
no shutdown
no routing
vlan access 1

interface 2/1/3
no shutdown
no routing
vlan access 1

interface 2/1/4
no shutdown
no routing
vlan access 1

interface 2/1/5
no shutdown
no routing
vlan access

...
...
vsf secondary-member 2
vsf member 1

type jl668a
link 1 1/1/27
link 2 1/1/28

vsf member 2

type jl668a
link 1 2/1/27
link 2 2/1/28

As shown in this configuration, interfaces of all member switches can be configured from the Master.

Once a stack is deployed, the stack configuration is sticky. The user can safely remove all other
configurations with the command erase startup-configuration without disturbing the stack
configurations. To remove all configurations, including the stacking configurations, use the command
erase all zeroize, where all members of the stack will be reset to factory defaults

Interoperation
The VSF stack supports either:

n 6200F devices, or

n 6300 devices (6300M or 6300F).

VSF stacking cannot be done with a mixed set of switches. The stack must be made up of only 6200 or only 6300

switches.

Feature overview | 14

Aruba6200Fdoesnotsupportmodularunits.
Link aggregation
Linkaggregations(L-Agg)canspaninterfacesacrossmultipleindividualswitcheswithinthestack.Load
balancingisperformedonallinterfacesoftheL-AggacrossthestackandisapplicabletoL2andL3L-
Aggs.
| interface | lag 1 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
no routing
| vlan | access 1 |     |     |     |     |
| ---- | -------- | --- | --- | --- | --- |
loop-protect
| interface | lag 2 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
| bfd       | min-transmit-interval   | 1000 |     |     |     |
| --------- | ----------------------- | ---- | --- | --- | --- |
| ip        | address 192.168.12.7/24 |      |     |     |     |
| interface | 1/1/18                  |      |     |     |     |
no shutdown
| lag       | 1      |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
| interface | 2/1/18 |     |     |     |     |
no shutdown
| lag       | 1      |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
| interface | 1/1/23 |     |     |     |     |
no shutdown
| lag       | 2      |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
| interface | 2/1/23 |     |     |     |     |
no shutdown
| lag     | 2                    |     |     |     |     |
| ------- | -------------------- | --- | --- | --- | --- |
| switch# | show lacp interfaces |     |     |     |     |
State abbreviations :
| A - Active        | P - Passive      | F - Aggregable | I - | Individual |     |
| ----------------- | ---------------- | -------------- | --- | ---------- | --- |
| S - Short-timeout | L - Long-timeout | N - InSync     | O - | OutofSync  |     |
C - Collecting D - Distributing
| X - State     | m/c expired        | E - Default | neighbor | state |     |
| ------------- | ------------------ | ----------- | -------- | ----- | --- |
| Actor details | of all interfaces: |             |          |       |     |
------------------------------------------------------------------------------
| Intf | Aggr Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | -------------- | --------------- | --- | ----------- | ---------- |
|      | Name Id Pri    |                 |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/18  | lag1                       |     |     |     | up  |
| ------- | -------------------------- | --- | --- | --- | --- |
| 2/1/18  | lag1                       |     |     |     | up  |
| 1/1/23  | lag2                       |     |     |     | up  |
| 2/1/23  | lag2                       |     |     |     | up  |
| Partner | details of all interfaces: |     |     |     |     |
------------------------------------------------------------------------------
| Intf | Aggr Port Port | State System-ID |     | System Aggr |     |
| ---- | -------------- | --------------- | --- | ----------- | --- |
|      | Name Id Pri    |                 |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/1/18 | lag1 |     |     |     |     |
| ------ | ---- | --- | --- | --- | --- |
| 2/1/18 | lag1 |     |     |     |     |
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeriesUserGuide 15

1/1/23
2/1/23

lag2
lag2

Feature overview | 16

Chapter 4

Stack management

Stack management

Consoles
The serial console of the Master switch provides a full CLI configuration interface for a user with valid
credentials. The serial console of the other stack members, including the Standby, provides a reduced
CLI configuration interface, with only a limited set of commands for troubleshooting the stack.

In a standard deployment, connect to the console interface of the master and standby switch. This
enables the stack master console to be reachable after a stack failover to the new Master.

Any switch configuration or monitoring must be performed from the console of the stack Master switch only.

Management interface
In a VSF stack, only the management interface on the Master switch will be assigned an IP address
(configured or assigned by DHCP). The stack allows connectivity to management protocols and Console
through the management interface on the Master.

VSF configuration
The following aspects of VSF are user-configurable.

Member number

To add a device to a VSF stack, the device must be renumbered to the corresponding member ID. The
user can specify the member number of the switch. The default member number is 1.

n For the 6200F device, the default number can be changed to any value from 2 through 8. (The device

supports up to 8 members.)

n For 6300 devices, the default number can be changed to any value from 2 through 10. (The device

supports up to 10 members.)

Refer to vsf renumber-to and Misconfiguration recovery for information about renumbering a member.

Changing the member number causes the switch to reboot and all configuration on the switch is removed.

A switch with a member number other than 1 cannot boot completely unless it has reachability to a VSF
master switch via VSF link. If a renumbered member is unable to communicate with the master switch
and is waiting in booting state, the user can:

n Go to a recovery console with a ctrl+c sequence and collect the diagnostic information, or

n Reset the VSF configuration.

Access to VSF members

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series | User Guide

17

In addition to serial console connections, any stack member can be accessed from any other member
using the member command.

Refer to member for information about console connection to a member switch.

VSF links

The user can specify the interfaces which comprise the VSF links. Refer to link for information about
specifying interfaces.

When the interface is configured, any existing configuration is removed, including VLAN memberships,
ACL/Quality of Service rules and any speed/duplex/MTU configuration.

Once the interface becomes part of a VSF link, no protocol or feature will be allowed to run on it as it is
now part of the fabric.

A VSF link will be a routed interface.

Member provisioning

VSF allows the user to provision or pre-configure any member before the member is physically added to
the stack. Provisioning the member allows the user to complete the required configuration as if the
member is present in the stack. When the member eventually joins the stack, it will boot up with the
configuration made on the pre-provisioned interfaces.

To provision a member, the part number of the member must be specified. Refer to type for
information about provisioning a member.

If a member tries to join the stack with a different part number to the one provisioned on the Master, the

member will be removed from the stack and will reboot with factory defaults.

Secondary member

The stack will not have a standby member by default. A secondary member can be configured from
available members and it will be assigned the role of stack standby.

Member number 1 can never be configured as a secondary member.

When configured as secondary, a stack member that is already present in the stack will reboot and
rejoin the stack as the standby.

A provisioned member can be configured as a secondary member. When the member joins the stack, it
will boot up in the standby role, without any further reboot.

If a secondary member is already configured and physically present in the stack, removing the
secondary will cause the secondary member to reboot and join as a member.

Refer to vsf secondary-member for information about configuring a secondary member.

To change secondary configuration, first unconfigure the secondary, wait for the device to join as a
member, and then configure a new secondary

Member remove

A member can be removed from a running stack. All configuration associated with the member will be
removed.

Stack management | 18

If the member is physically present in the stack at the time it is removed, all VSF configurations on that
member will be erased and it will lose its identity as a member of the stack from which it was removed.
The member will come back as member 1 with factory default configuration.

It is not advisable to remove the member that is the master of the stack. If the master has to be removed, the

recommendation is to switch over and wait for the old master to come up as standby before removing it.

Refer to vsf member for information about removing a member.

Automated image sync
In a VSF environment, all stack members run the same software image. If the user upgrades the
software on the Master by downloading a new software image using SFTP/TFTP, all members of the
stack will simultaneously upgrade.

When forming a stack, if the software version on a member is different from the version of the Master,
the member will automatically update itself to the same version as the Master. The member will reboot
itself to run the updated version before joining the stack.

Reboot
An individual stack member can be rebooted from a CLI command.

n The member will reboot and re-join the stack, with the same role that it had prior to the reboot.

n If the stack topology is a ring, no traffic disruption is expected on any other stack members when a

single member is rebooted.

n If the stack topology is a chain, rebooting a member may cause a stack split, resulting in members

being unreachable from the master. This result can cause significant disruption of the stack, so use
this option with caution.

n If the member is the stack Standby, there will be no Standby in the stack until the member reboots

and re-joins the stack. At this point, the member will again have the role of Standby.

n If the member is the stack Master, the command will trigger a failover and the Standby switch will

take over as Master of the stack.

n If the Standby is unavailable at the time of master reboot, the whole stack will reboot.

The whole stack can also be rebooted by using the boot system command.

n All members will reboot and the stack will re-form.

n Traffic will be disrupted for the duration of the reboot.

Refer to vsf member reboot for information about rebooting a member.

Member addition
A member can be added to the stack to augment an existing stack. The member being added can be a
factory-default switch or a switch with pre-existing configuration.

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series User Guide

19

1. Configure interfaces to VSF links on the member being added.

2. Renumber the member being added.

The member will not join the stack if there is a member number conflict.

3. Renumbering will cause a reboot of the switch.

4. Connect the configured VSF links to a previously configured VSF link on the stack.

5. The member joins the stack, with default configuration on its interfaces. Any previous

configuration on the member will be lost.

Member replacement
The replacement member must be of the same part number as the switch being replaced.

1. Power off or disconnect all physical connections of the member that will be replaced.

2. Configure interfaces to VSF links on the replacement member. These interfaces must match the

interfaces configured on the switch being replaced.

3. Renumber the replacement member to the same number as the switch being replaced.

4. Renumbering will cause a reboot of the switch.

5. Connect the replacement member to the stack.

6. The member joins the stack, with the same configuration as the member it is replacing.

Stack management | 20

Chapter 5
Configuring a VSF stack
| Configuring | a VSF stack |     |
| ----------- | ----------- | --- |
ThefollowingsectionsdescribetheprerequisitesandprocedurestoconfigureaVSF stack.
Prerequisites
ManualconfigurationofaVSFstackrequirestheusertoindividuallyconfigureeachswitchinthestack.
ThisprocessprovidesthebestcontrolfortheusertoconfigureVSFmembernumberandlinks.
| Figure 4 Eight-memberringsetup |                 |            |
| ------------------------------ | --------------- | ---------- |
| Forming                        | an eight-member | ring setup |
21
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeries| UserGuide

Toformaneight-memberringsetupasshown,donotmaketheconnectionsinitially.Connecttheports
onlyaftereachdeviceisfullyconfigured.
Procedure
1. Logintothefirstdevice,numbered1.
a. Thedefaultmembernumberis1,sonomembernumberchangeisrequired.
b. Attheprompt,enterthefollowingcommands:
| switch#               | configure |     |          |        |     |     |
| --------------------- | --------- | --- | -------- | ------ | --- | --- |
| switch(config)#       |           | vsf | member 1 |        |     |     |
| switch(vsf-member-1)# |           |     | link 1   | 1/1/25 |     |     |
| switch(vsf-member-1)# |           |     | link 2   | 1/1/26 |     |     |
c. Theprecedingsequenceofcommandswillconfigurethelinksformember1.
d. Ports25and26areconfiguredaslink1and2respectively.
2. Logintotheseconddevice,numbered2.
a. Executethefollowingcommands.
| switch#               | configure |          |               |        |            |             |
| --------------------- | --------- | -------- | ------------- | ------ | ---------- | ----------- |
| switch                | (config)# | vsf      | member 1      |        |            |             |
| switch(vsf-member-1)# |           |          | link 1        | 1/1/25 |            |             |
| switch(vsf-member-1)# |           |          | link 2        | 1/1/26 |            |             |
| switch(vsf-member-1)# |           |          | exit          |        |            |             |
| switch(config)#       |           | vsf      | renumber-to   | 2      |            |             |
| This will             | save      | the VSF  | configuration |        | and reboot | the switch. |
| Do you                | want to   | continue | (y/n)?        | y      |            |             |
b. Theprecedingsequenceofcommandswillconfigurethelinksonmember2.
c. Thedefaultmembernumberis"1".Thecommand"vsfrenumber-to"changesthismember
number.
d. Linksareconfiguredbeforerenumbering,andthememberidentifierintheinterfacenameis
"1"atthispoint.
e. Theswitchwillrebootafterexecutingtherenumbercommand.
3. Physicallyconnectmember2tomember1asshowninthefigure.
a. Thisactionwillcausemember2tojointhestack,withmember1asthemaster.
b. Thisresultcanbeverifiedbyexecuting"showvsf"onmember1.
| switch#         | show    | vsf    |                     |       |        |     |
| --------------- | ------- | ------ | ------------------- | ----- | ------ | --- |
| MAC Address     |         |        | : 38:21:c7:5d:d0:c0 |       |        |     |
| Secondary       |         |        | :                   |       |        |     |
| Topology        |         |        | : Chain             |       |        |     |
| Status          |         |        | : No                | Split |        |     |
| Split Detection |         | Method | : None              |       |        |     |
| Mbr Mac         | Address |        | type                |       | Status |     |
ID
| --- ------------------- |     |     | -------------- |     | --------------- |     |
| ----------------------- | --- | --- | -------------- | --- | --------------- | --- |
| 1 38:21:c7:5d:d0:c0     |     |     | JL668A         |     | Master          |     |
| 2 38:21:c7:6a:10:c0     |     |     | JL668A         |     | Member          |     |
ConfiguringaVSFstack|22

4. Repeatsteps2and3,foreachstackmember3through8.
a. Besuretospecifythemembernumbercorrectlyoneachmember.
b. Ifamembernumberconflictisdetected,thememberwillNOTjointhestack.
5. Oncemember8hassuccessfullyjoinedthestack,connectmember8link2tomember1link1,to
completethering.
Issuea"showvsf"commandtoensurethattheringhassuccessfullyformed.
| switch# show    | vsf    |                     |        |
| --------------- | ------ | ------------------- | ------ |
| MAC Address     |        | : 38:21:c7:5d:d0:c0 |        |
| Secondary       |        | :                   |        |
| Topology        |        | : Ring              |        |
| Status          |        | : No Split          |        |
| Split Detection | Method | : None              |        |
| Mbr Mac Address |        | type                | Status |
ID
| --- ------------------- |     | -------------- | --------------- |
| ----------------------- | --- | -------------- | --------------- |
| 1 38:21:c7:5d:d0:c0     |     | JL668A         | Master          |
| 2 38:21:c7:6a:10:c0     |     | JL668A         | Member          |
| 3 38:21:c7:5c:15:80     |     | JL668A         | Member          |
| 4 38:21:c7:5a:61:40     |     | JL668A         | Member          |
| 5 38:21:c7:62:66:00     |     | JL668A         | Member          |
| 6 38:21:c7:58:22:40     |     | JL668A         | Member          |
| 7 38:21:c7:5a:9c:00     |     | JL668A         | Member          |
| 8 38:21:c7:63:a5:00     |     | JL668A         | Member          |
6. Theprecedingstepswillformaneight-memberstackwithoutastandby.Tomakeanymember
thestandby(forexample,member8),usethesecondarycommand:
a. FromtheprimaryVSFmember,configuremember8asVSFsecondarymember:
swtich(config)#
|     | vsf | secondary-member | 8   |
| --- | --- | ---------------- | --- |
This will save the configuration and reboot the specified switch.
| Do you want | to continue | (y/n)? y |     |
| ----------- | ----------- | -------- | --- |
switch(config)#
b. Thisactionwillrebootmember8anditwillrejoinasstandby.
| switch# show    | vsf                 |        |     |
| --------------- | ------------------- | ------ | --- |
| MAC Address     | : 38:21:c7:5d:d0:c0 |        |     |
| Secondary       | : 8                 |        |     |
| Topology        | : Ring              |        |     |
| Status :        | No Split            |        |     |
| Split Detection | Method              | : None |     |
| Mbr Mac Address | type                | Status |     |
ID
| --- ----------------- |     | ----- --------------- |     |
| --------------------- | --- | --------------------- | --- |
| 1 38:21:c7:5d:d0:c0   |     | JL668A Master         |     |
| 2 38:21:c7:6a:10:c0   |     | JL668A Member         |     |
| 3 38:21:c7:5c:15:80   |     | JL668A Member         |     |
| 4 38:21:c7:5a:61:40   |     | JL668A Member         |     |
| 5 38:21:c7:62:66:00   |     | JL668A Member         |     |
| 6 38:21:c7:58:22:40   |     | JL668A Member         |     |
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeriesUserGuide 23

7
8

38:21:c7:5a:9c:00 JL668A Member
38:21:c7:63:a5:00 JL668A Standby

7. Alternatively, before adding member 8 to the stack, pre-configure the secondary as 8 and then
renumber device 8. This action will ensure that device 8 will join the stack directly as standby.

Misconfiguration recovery
If a switch fails to join the stack because of misconfiguration, use the following procedure to restore the
switch back to a factory default configuration.

The user must have management connectivity to the failed member for support files from the member in

recovery mode.

Procedure

1. Press Ctrl+C on the switch console.

2. Log in using administrator credentials.

3. At the prompt, issue the vsf-factory-reset command.

^C
Login: admin
Password:

recovery# vsf-factory-reset

4. This resets the member to factory-default settings and the switch will come up with a default

member ID of 1.

5. Now the user can reconfigure the VSF link and renumber it to the preferred member ID.

Configuring a VSF stack | 24

Chapter 6

Failure and recovery

Failure and recovery

The following section describes failure and recovery scenarios for stack split issues.

Stack split
Multiple link or member failures can result in a complete stack split, with the master and standby switch
in different split fragments. In this case, both master and standby switches will become master switches.
Each stack fragment will continue operating with the same configuration and state, and forward traffic
between all stations that the fragment can reach.

The downside of this scenario is that each stack fragment will have the same MAC address and IP
addresses. To avoid this scenario, configure split detection (described in the following section) which
would bring down the interfaces on one fragment to prevent duplicate MAC/IPs.

Management interface split detection

For more information, refer to vsf split-detect .

VSF stack supports management split detection, which requires users to connect the management
interfaces of the primary and secondary stack members to the same L2 network.

The Primary stack member is member "1", whereas the secondary member is the user-configured
secondary switch. Once the stack is split, both of these switches become master of their respective
fragments. The fragment with "1" as master is referred to as the primary fragment, and the fragment
with the secondary switch as master is the secondary fragment.

It is also possible to connect the management interfaces of primary and secondary to one another for split

detection.

If the secondary fragment discovers that the primary fragment is operational, it will bring down all front-
plane non-VSF interfaces on the secondary fragment to minimize network disruption due to duplicate
MAC or IP addresses.

The interfaces will remain down until the stack is reconnected or the primary fragment goes down. The
interfaces of the primary fragment will always remain operational.

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series | User Guide

25

Theshow vsfoutputinthePrimaryfragmentwilllooklikethis:
| switch# show    | vsf    |                     |        |
| --------------- | ------ | ------------------- | ------ |
| MAC Address     |        | : 38:21:c7:5c:f4:c0 |        |
| Secondary       |        | : 2                 |        |
| Topology        |        | : Standalone        |        |
| Status          |        | : Active Fragment   |        |
| Split Detection | Method | : mgmt              |        |
| Mbr Mac Address |        | type                | Status |
ID
| --- ------------------- |     | -------------- | ---------------   |
| ----------------------- | --- | -------------- | ----------------- |
| 1 38:21:c7:5c:f4:c0     |     | JL668A         | Master            |
| 2                       |     | JL668A         | In Other Fragment |
| 3                       |     | JL668A         | In Other Fragment |
| 4                       |     | JL668A         | In Other Fragment |
switch#
| switch# show | vsf topology |     |     |
| ------------ | ------------ | --- | --- |
Mstr
+---+
| 1 |
+---+
switch#
Theshow vsfoutputinthesecondaryfragmentwilllooklikethis:
| switch# show    | vsf    |                     |          |
| --------------- | ------ | ------------------- | -------- |
| MAC Address     |        | : 38:21:c7:5c:f4:c0 |          |
| Secondary       |        | : 2                 |          |
| Topology        |        | : Chain             |          |
| Status          |        | : Inactive          | Fragment |
| Split Detection | Method | : mgmt              |          |
| Mbr Mac Address |        | type                | Status   |
Failureandrecovery|26

ID
| --- ------------------- |     | -------------- | ---------------   |
| ----------------------- | --- | -------------- | ----------------- |
| 1                       |     | JL668A         | In Other Fragment |
| 2 38:21:c7:5c:77:40     |     | JL668A         | Master            |
| 3 38:21:c7:5a:a5:80     |     | JL668A         | Member            |
| 4 38:21:c7:5c:b3:00     |     | JL668A         | Member            |
switch#
| switch# show | vsf topology |     |     |
| ------------ | ------------ | --- | --- |
Mstr
| +---+      | +---+ +---+ |     |     |
| ---------- | ----------- | --- | --- |
| | 4 |1==2| | 3 |1==2|    | 2 | |     |
| +---+      | +---+ +---+ |     |     |
switch#
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeriesUserGuide 27

VSF recomendations and restrictions

Chapter 7

VSF recomendations and restrictions

The following recommendations and restrictions apply to VSF.

n Before applying a configuration on a stack through checkpoint restore or TFTP/SFTP/USB download,
make sure that current VSF-specific configurations and the intended configurations match exactly. In
other words, the VSF stack and the intended configuration must have the same:

o Total number of members

o Member types

o Member number/ID

o VSF link configurations

o Secondary member configuration

o Split-detect configuration

n A functional stack must be configured with a standby for redundancy purposes. If the master fails

and there is no standby, the stack will fail.

n If the master fails and there is a standby device, the standby becomes the new master and will take

over stack management. When the old master device is replaced, it seamlessly becomes the standby
device for the stack and there no disruption.

The MAC address of the stack will remain the same until the entire stack is rebooted, after which the
stack MAC address will be the MAC address of the new master. However, once recovered, it is not
advisable to use the removed master elsewhere in the same network until the stack is rebooted to avoid
MAC address conflicts.

n After downloading firmware to a stack, the stack must be rebooted to complete the upgrade process.
Adding or rebooting individual members before the upgrade process is completed can cause the
individual member to fail while joining the stack.

n If there is a discrepancy between a VSF member link configuration on the master and the VSF
member link configuration on the member, the link configuration on the member is used.

n Configure only one link between a pair of stack members. This recommendation is also applicable for

a two-member VSF stack.

n If there is a split, failure in the connectivity between management interfaces of the master and

standby might result in two active fragments. This issue can occur even if management split-detect is
enabled.

n Ring topology is not supported for two-member VSF.

n Replacing member 1 in a stack without a standby with a new switch booted as member 1 will reset all

configurations on the stack.

n Do not connect a renumbered member to multiple primary devices through VSF links.

n Before removing an individual interface from VSF link using the command no vsf link <x>

<interface>, ensure that the interface is admin shutdown at both local and peer ends. For example:
Interface 1/1/25 on member 1 link 1 is connected to 2/1/25 on member 2 link 2. The user intends to
remove 1/1/25 from link 1 of member 1. Both the interfaces 1/1/25 and 2/1/25 have to be admin
shutdown before actually removing them from the link configuration. To delete the link completely

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series | User Guide

28

using the no link <x> command, all individual interfaces in the VSF link have to be admin shutdown
both at local and peer ends.

n Before removing an individual interface from the VSF link using the no vsf link <x> <interface>

command, ensure that the interface is admin shutdown at both local and peer ends.

Example: Interface 1/1/25 on member 1 link 1 is connected to 2/1/25 on member 2 link 2. The user
intends to remove 1/1/25 from link 1 of member 1. Interfaces 1/1/25 and 2/1/25 must be admin
shutdown before removing them from the link configuration.

Before deleting the link using the no link <x> command, all individual interfaces in the VSF link must
be admin shutdown both at local and peer ends.

n There may be instances in which a master switch with vsf secondary <id> configuration is unable
to discover the standby switch. In such cases, the master switch will wait for up to 10 minutes to
detect the standby switch.

VSF recomendations and restrictions | 29

Chapter 8

VSF commands

VSF commands

VSF commands do not apply to the 6400 series switches.

vsf member

Syntax

vsf member <MEMBER-ID>
no vsf member <MEMBER-ID>

Description

Creates VSF member context in the switch for the specified member.

The no form of this command removes the specified member from the stack. All configuration
associated with the member, as well as the subsystems and interfaces of the member will also be
removed.

If the member is physically present in the stack at the time it is removed, it will reboot with the default
configuration and lose its identity as a member of the stack from which it was removed.

When a physically present member is removed, it may cause the stack to split.

Command context

config

Parameters

<MEMBER-ID>

VSF member identifier. Required.

n Range for 6200F devices: 1-8.

n Range for 6300 devices: 1-10.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring a VSF member:

switch(config)# vsf member 2
switch(vsf-member-2)#

Removing a non-master member from the stack:

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series | User Guide

30

| switch(config)# |     | no       | vsf  | member 2        |     |              |
| --------------- | --- | -------- | ---- | --------------- | --- | ------------ |
| The specified   |     | switch   | will | be unconfigured |     | and rebooted |
| Do you want     | to  | continue |      | (y/n)?          | y   |              |
Removingtherunningmastershouldbedonewithcautionasitcanmakethestackunusableifthereisno
standby.
member
Syntax
member <MEMBER-ID>
Description
ConnectstothespecifiedmemberinaVSFenvironment.
| Command | context |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
Manager(#)
Parameters
<MEMBER-ID>
VSFmemberID.Required.
n Rangefor6200Fdevices:1-8.
n Rangefor6300devices:1-10.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
VSFstackisformedwithtwomembers:
| switch#             | member     | 2          |           |           |          |              |
| ------------------- | ---------- | ---------- | --------- | --------- | -------- | ------------ |
| admin@172.17.17.2's |            |            | password: |           |          |              |
| Last login:         | 2019-09-30 |            |           | 11:42:17  | from the | console      |
| User "admin"        |            | has logged |           | in 1 time | in the   | past 30 days |
member#
Membertoself:
| switch# | member    | 1   |      |     |     |     |
| ------- | --------- | --- | ---- | --- | --- | --- |
| Already | on member |     | id 1 |     |     |     |
VSFstackisnotformedandmembernotavailable:
VSFcommands|31

| switch# member | 2               |     |     |     |
| -------------- | --------------- | --- | --- | --- |
| No stack       | role for member | id  | 2   |     |
type
Syntax
type <TYPE>
Description
ConfiguresthepartnumberoftheVSFmemberbeingprovisioned.Afterprovisioning,theinterfacesof
thememberareavailableforconfiguration.
Whenthemembereventuallyjoinsthestack,itwillbootupwiththeconfigurationmadeonthepre-
provisionedinterfaces.
Toprovisionamember,themembernumberandthepartnumberofthemembermustbespecified.
| Command context |     |     |     |     |
| --------------- | --- | --- | --- | --- |
vsf-member-<ID>#
Parameters
<TYPE>
Thepartnumberofthememberbeingprovisioned.Required.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringthepartnumberofaVSFmember:
switch(vsf-member-2)#
| type The               | part number       | of      | the member     | being provisioned |
| ---------------------- | ----------------- | ------- | -------------- | ----------------- |
| switch(vsf-member-2)#  |                   | type    | ?              |                   |
| jl658a                 | 6300M 24SFP+      | /4SFP56 | Switch         |                   |
| jl659a                 | 6300M 48SR        | PoE CLS | 6 /4SFP56      | Switch            |
| jl660a                 | 6300M 24SR        | PoE CLS | 6 /4SFP56      | Switch            |
| jl661a                 | 6300M 48G PoE     | CLS     | 4 /4SFP56      | Switch            |
| jl662a                 | 6300M 24G PoE     | CLS     | 4 /4SFP56      | Switch            |
| jl663a                 | 6300M 48G /4SFP56 |         | Switch         |                   |
| jl664a                 | 6300M 24G /4SFP56 |         | Switch         |                   |
| jl665a                 | 6300F 48G PoE     | CLS     | 4 /4SFP56      | Switch            |
| jl666a                 | 6300F 24G PoE     | CLS     | 4 /4SFP56      | Switch            |
| jl667a                 | 6300F 48G /4SFP56 |         | Switch         |                   |
| jl668a                 | 6300F 24G /4SFP56 |         | Switch         |                   |
| switch(vsf-member-2)#  |                   | type    | jl662a         |                   |
| switch(vsf-member-2)#  |                   | show    | running-config |                   |
| Current configuration: |                   |         |                |                   |
!
| !Version | ArubaOS-CX |     |     |     |
| -------- | ---------- | --- | --- | --- |
!
!
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeriesUserGuide 32

!
!
ssh maximum-auth-attempts 6
!
!
!
!
!
vlan 1
vsf member 1

type jl661a

exit
vsf member 2

type jl662a

exit

link

Syntax

link <LINK-ID> [<IFRANGE>]

Description

Creates or modifies a VSF link. The user can specify the physical interfaces that make up the VSF link.

Once an interface is part of a VSF link, all existing configuration on the interface is removed and the
interface will operate as a VSF interface. At least one interface must be specified for the creation of a
VSF link. VSF interfaces carry VSF traffic and can only be connected to other VSF interfaces.

The no form of the command can be used to remove interfaces from a link or remove configuration
from the link completely.

When configuration is removed from a link, it may cause the stack to split.

Command context

vsf-member-<ID>#

Parameters

<LINK-ID>

The VSF link number. Required. Range: 1-2.

<IFRANGE>

The interface identifier range. Required.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating and modifying VSF links:

switch(vsf-member-1)# link
<1-2>
switch(vsf-member-1)# link 1

VSF Link number

VSF commands | 33

| IFRANGE | Interface | identifier | range |
| ------- | --------- | ---------- | ----- |
<cr>
| switch(vsf-member-1)# |     | link 1 1/1/51 |     |
| --------------------- | --- | ------------- | --- |
<cr>
| switch(vsf-member-1)# |     | link 1 1/1/49-1/1/50 |     |
| --------------------- | --- | -------------------- | --- |
<cr>
| switch(vsf-member-1)# |     | link 2 1/1/52 |     |
| --------------------- | --- | ------------- | --- |
<cr>
| switch(vsf-member-1)# |     | link 1 1/1/49 |     |
| --------------------- | --- | ------------- | --- |
<cr>
| switch(vsf-member-5)# |                | show running-config |     |
| --------------------- | -------------- | ------------------- | --- |
| Current               | configuration: |                     |     |
!
| !Version | ArubaOS-CX |     |     |
| -------- | ---------- | --- | --- |
!
!
!
!
| ssh maximum-auth-attempts |     | 6   |     |
| ------------------------- | --- | --- | --- |
!
!
!
!
!
vlan 1
| interface | 1/1/49 |     |     |
| --------- | ------ | --- | --- |
no shutdown
| interface | 1/1/52 |     |     |
| --------- | ------ | --- | --- |
no shutdown
| vsf member | 1        |     |     |
| ---------- | -------- | --- | --- |
| type       | jl661a   |     |     |
| link       | 1 1/1/49 |     |     |
| link       | 2 1/1/52 |     |     |
exit
| switch(vsf-member-1)# |     | no link 1 |     |
| --------------------- | --- | --------- | --- |
<cr>
| switch(vsf-member-1)# |                  | no link 1       |     |
| --------------------- | ---------------- | --------------- | --- |
| This will             | cause the        | stack to split. |     |
| Do you                | want to continue | (y/n)? y        |     |
| switch(vsf-member-1)# |                  | no link 2       |     |
This will cause the stack to split and the residual stack fragment will become
unusable.
| Do you                | want to continue | (y/n)? y            |     |
| --------------------- | ---------------- | ------------------- | --- |
| switch(vsf-member-1)# |                  | show running-config |     |
| Current               | configuration:   |                     |     |
!
| !Version | ArubaOS-CX | SL.10.02.0020-741-g11104d6~dirty |     |
| -------- | ---------- | -------------------------------- | --- |
!
!
!
!
| ssh maximum-auth-attempts |     | 6   |     |
| ------------------------- | --- | --- | --- |
!
!
!
!
!
vlan 1
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeriesUserGuide 34

interface 1/1/52

no shutdown

vsf member 1

type jl661a

exit

Before removing an individual interface from the VSF link using the no vsf link <x> <interface>
command, ensure that the interface is admin shutdown at both local and peer ends.

Example: Interface 1/1/25 on member 1 link 1 is connected to 2/1/25 on member 2 link 2. The user
intends to remove 1/1/25 from link 1 of member 1. Interfaces 1/1/25 and 2/1/25 must be admin
shutdown before removing them from the link configuration.

Before deleting the link using the no link <x> command, all individual interfaces in the VSF link must
be admin shutdown both at local and peer ends.

vsf split-detect

Syntax

vsf split-detect <MGMT-INTERFACE>

Description

Configures the VSF split detection method that specifies the mechanism used for stack fragment
discovery when there is a stack split.

Once the stack fragments are discovered, the fragment having the primary member always wins. All
non-VSF interfaces on the losing stack fragment will be brought down to minimize network disruption
due to duplicate MAC/IP.

Command context

config

Parameters

<MGMT-INTERFACE>

Configures mgmt-interface as the split detection method. Connect the management interfaces of the
primary and secondary members to the same L2 network. Optionally, the management interfaces of
primary and secondary can be directly connected to each other.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring mgmt-interface as the split detection method:

switch(config)# vsf split-detect mgmt-interface

Removing split detection from the stack:

switch(config)# no vsf split-detect

VSF commands | 35

vsf secondary-member
Syntax
| vsf secondary-member | <MEMBER-ID> |     |     |     |
| -------------------- | ----------- | --- | --- | --- |
Description
Configuresasecondarymemberfromtheavailablemembers.Thesecondarymemberwillnormally
operateastheStandbymemberofthestack.
Thestackdoesnothaveasecondarymemberbydefault.Ifasecondarymemberisalreadyconfigured,
theusermustun-configuretheoldsecondarymemberandthenconfigurenewsecondarymember.
Member1cannotbeconfiguredasthesecondarymember.
| Command context |     |     |     |     |
| --------------- | --- | --- | --- | --- |
config
Parameters
<MEMBER-ID>
Secondarymembernumber.Required.
n Rangefor6200Fdevices:2-8.
n Rangefor6300devices:2-10.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringandun-configuringasecondarymember:
switch(config)#
|     | vsf | secondary-member | 3   |     |
| --- | --- | ---------------- | --- | --- |
This will save the configuration and reboot the specified switch.
| Do you want     | to continue | (y/n)? y         |                 |        |
| --------------- | ----------- | ---------------- | --------------- | ------ |
| switch(config)# | vsf         | secondary-member | 4               |        |
| The existing    | secondary   | member must      | be unconfigured | first. |
| switch(config)# | no vsf      | secondary-member |                 |        |
| The secondary   | member      | will go for      | a reboot.       |        |
| Do you want     | to continue | (y/n)? y         |                 |        |
vsf renumber-to
Syntax
| vsf renumber-to | <MEMBER-ID> |     |     |     |
| --------------- | ----------- | --- | --- | --- |
Description
RenumbersVSFmember1toavaluefrom2through10(for6300devices)and2through8(forthe
6200Fdevice).Changingthemembernumbercausestheswitchtorebootwiththenewmember
number.Onlymember1canberenumbered.
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeriesUserGuide 36

VSFlinksmustbeconfiguredbeforerenumberingaswitch.Renumberingwillbedisallowedifnolinksare
configuredorthereareprovisioned/physicallypresentmembers.
| Command | context |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
config
Parameters
<MEMBER-ID>
Membernumbertowhichthememberwillberenumbered.Required.
n Rangefor6200Fdevices:2-8.
n Rangefor6300devices:2-10.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
RenumberingprimaryVSFmemberfrom1to2:
| switch(config)# |     | vsf | renumber-to | 2   |     |     |
| --------------- | --- | --- | ----------- | --- | --- | --- |
Member 1 cannot be renumbered until all other members are removed.
| switch(config)# |           | vsf           | renumber-to   | 2     |            |                |
| --------------- | --------- | ------------- | ------------- | ----- | ---------- | -------------- |
| Member          | 1 cannot  | be renumbered |               | until | a VSF link | is configured. |
| switch(config)# |           | vsf           | renumber-to   | 2     |            |                |
| This            | will save | the VSF       | configuration |       | and reboot | the switch.    |
| Do you          | want to   | continue      | (y/n)?        | y     |            |                |
| vsf member      |           | reboot        |               |       |            |                |
Syntax
| vsf member | <MEMBER-ID> |     | reboot |     |     |     |
| ---------- | ----------- | --- | ------ | --- | --- | --- |
Description
RebootsthespecifiedVSFmember.Uponreboot,ifthemasterisreachable,thememberwillrejointhe
stack.
| Command | context |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
Manager(#)
Parameters
<MEMBER-ID>
Membernumbertoberebooted.Required.
n Rangefor6200Fdevices:1-8.
n Rangefor6300devices:1-10.
Authority
VSFcommands|37

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Rebootingtheprimaryswitchofthestack:
| switch#   | vsf member       | 1 reboot  |              |         |           |
| --------- | ---------------- | --------- | ------------ | ------- | --------- |
| Rebooting | the master       | switch    | of the stack | without | a standby |
| will make | the stack        | unusable. |              |         |           |
| Do you    | want to continue | (y/n)?    | y            |         |           |
| switch#   | vsf member       | 1 reboot  |              |         |           |
The master switch will reboot and the standby will become the master.
| Do you    | want to continue | (y/n)?        | y       |     |     |
| --------- | ---------------- | ------------- | ------- | --- | --- |
| switch#   | vsf member       | 2 reboot      |         |     |     |
| This will | reboot           | the specified | switch. |     |     |
| Do you    | want to continue | (y/n)?        | y       |     |     |
interface
Syntax
interface <IFRANGE>
Description
EntersconfigurationcontextforoneormoreVSFlinkinterfaces.
| Command | context |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- |
config
Parameters
<IFRANGE>
PORTidentifierrange.Required.
VSFlinkinterfacescannotbeincludedinarangewithotherinterfaces.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enteringconfigurationcontext:
| switch(config)# | int | 1/1/1 |     |     |     |
| --------------- | --- | ----- | --- | --- | --- |
shutdown
Syntax
shutdown
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeriesUserGuide 38

Description
ShutsdownoneormoreVSFlinkinterfaces.
Command context
config-if-vsf
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShuttingdownaVSFlinkinterface:
| switch(config)#                      | int 1/1/1-1/1/2 |     |          |
| ------------------------------------ | --------------- | --- | -------- |
| switch(config-if-vsf-<1/1/1-1/1/2>)# |                 |     | shutdown |
ShutdownconfigurationforVSFinterfacesisnotpersistentacrossreboots.
show vsf
Syntax
show vsf
Description
DisplaysthelistofprovisionedVSFstackmembers.
Command context
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# show    | vsf    |                     |        |
| --------------- | ------ | ------------------- | ------ |
| MAC Address     |        | : 08:97:34:b0:0e:00 |        |
| Secondary       |        | : 2                 |        |
| Topology        |        | : Ring              |        |
| Status          |        | : No Split          |        |
| Split Detection | Method | : None              |        |
| Mbr MAC Address |        | Type                | Status |
ID
| --- ------------------- |     | -------------- | ----------------- |
| ----------------------- | --- | -------------- | ----------------- |
| 1 08:97:34:b0:0e:00     |     | JL666A         | Master            |
| 2 08:97:34:b1:43:00     |     | JL665A         | Standby           |
| 3 08:97:34:b7:cc:00     |     | JL663A         | Member            |
| 4                       |     | JL662A         | Not Present       |
VSFcommands|39

| switch# show    | vsf    |                     |        |     |
| --------------- | ------ | ------------------- | ------ | --- |
| MAC Address     |        | : 08:97:34:b0:0e:00 |        |     |
| Secondary       |        | : 2                 |        |     |
| Topology        |        | : Ring              |        |     |
| Status          |        | : Active Fragment   |        |     |
| Split Detection | Method | : mgmt-interface    |        |     |
| Mbr MAC Address |        | Type                | Status |     |
ID
| --- ------------------- |     | -------------- | ----------------- |     |
| ----------------------- | --- | -------------- | ----------------- | --- |
| 1 08:97:34:b0:0e:00     |     | JL666A         | Master            |     |
| 2 08:97:34:b1:43:00     |     | JL665A         | In Other Fragment |     |
| 3 08:97:34:b7:cc:00     |     | JL663A         | Member            |     |
| 4                       |     | JL662A         | Not Present       |     |
| show vsf detail         |     |                |                   |     |
Syntax
show vsf detail
Description
DisplaysdetailedinformationrelatedtothecurrentstateoftheVSFstackandthestackmembers.
Command context
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# show | vsf detail |     |     |     |
| ------------ | ---------- | --- | --- | --- |
VSF Stack
| MAC Address      |        | : ec:eb:b8:d0:80:40  |                       |        |
| ---------------- | ------ | -------------------- | --------------------- | ------ |
| Secondary        |        | : 2                  |                       |        |
| Topology         |        | : Ring               |                       |        |
| Status           |        | : No Split           |                       |        |
| Uptime           |        | : 0d 0h 23m          |                       |        |
| Split Detection  | Method | : None               |                       |        |
| Software Version |        | : SL.10.02.0000-7755 |                       |        |
| Name             |        | : Aruba-VSF-6300F    |                       |        |
| Contact          |        | :                    |                       |        |
| Location         |        | :                    |                       |        |
| Member ID        | :      | 1                    |                       |        |
| MAC Address      | :      | ec:eb:b8:d0:80:40    |                       |        |
| Type             | :      | JL666A               |                       |        |
| Model            | :      | Aruba 6300F          | 24G PoE CLS 4 /4SFP56 | Switch |
| Status           | :      | Master               |                       |        |
| ROM Version      | :      | SL.10.02.0000-7755   |                       |        |
| Serial Number    | :      | CN7ZK90012           |                       |        |
| Uptime           | :      | 0d 0h 23m            |                       |        |
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeriesUserGuide 40

| CPU Utilization    | :   | 0%                 |             |           |        |
| ------------------ | --- | ------------------ | ----------- | --------- | ------ |
| Memory Utilization | :   | 20%                |             |           |        |
| VSF link           | 1 : | Up, connected      | to peer     | member 2, | link 1 |
| VSF link           | 2 : | Down               |             |           |        |
| Member ID          | :   | 2                  |             |           |        |
| MAC Address        | :   | eb:ec:d8:e0:50:60  |             |           |        |
| Type               | :   | JL666A             |             |           |        |
| Model              | :   | Aruba 6300F        | 24G PoE CLS | 4 /4SFP56 | Switch |
| Status             | :   | Standby            |             |           |        |
| ROM Version        | :   | SL.10.02.0000-7755 |             |           |        |
| Serial Number      | :   | CN7ZK90012         |             |           |        |
| Uptime             | :   | 0d 0h 23m          |             |           |        |
| CPU Utilization    | :   | 0%                 |             |           |        |
| Memory Utilization | :   | 15%                |             |           |        |
| VSF link           | 1 : | Up, connected      | to peer     | member 1, | link 1 |
| VSF link           | 2 : | Down               |             |           |        |
| Member ID          | :   | 3                  |             |           |        |
| MAC Address        | :   |                    |             |           |        |
| Type               | :   | JL666A             |             |           |        |
| Model              | :   | Aruba 6300F        | 24G PoE CLS | 4 /4SFP56 | Switch |
| Status             | :   | Not Present        |             |           |        |
| ROM Version        | :   |                    |             |           |        |
| Serial Number      | :   |                    |             |           |        |
| Uptime             | :   |                    |             |           |        |
| CPU Utilization    | :   |                    |             |           |        |
| Memory Utilization | :   |                    |             |           |        |
| VSF link           | 1 : |                    |             |           |        |
| VSF link           | 2 : |                    |             |           |        |
| show vsf link      |     |                    |             |           |        |
Syntax
show vsf link
Description
DisplaystheVSFlinkstateforeachmember.
| Command context |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# show | vsf link    |                                |     |     |     |
| ------------ | ----------- | ------------------------------ | --- | --- | --- |
| VSF Member   | 1           |                                |     |     |     |
| Link         | Peer Peer   |                                |     |     |     |
| Link State   | Member Link | Interfaces                     |     |     |     |
| ---- ------  | ------ ---- | ------------------------------ |     |     |     |
VSFcommands|41

| 1 Down   | 0      | 0 1/1/1,1/1/5,1/1/8,1/1/9 |     |     |
| -------- | ------ | ------------------------- | --- | --- |
| 2 Down   | 0      | 0 1/1/11-1/1/13,1/1/15    |     |     |
| show vsf | member |                           |     |     |
Syntax
| show vsf member | <MEMBER-ID> |     |     |     |
| --------------- | ----------- | --- | --- | --- |
Description
DisplaysinformationaboutthespecifiedVSFmember.
| Command context |     |     |     |     |
| --------------- | --- | --- | --- | --- |
Manager(#)
Parameters
<MEMBER-ID>
VSFmemberidentifier.Required.
n Rangefor6200Fdevices:1-8.
n Rangefor6300devices:1-10.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# show    | vsf member  | 1                    |                          |        |
| --------------- | ----------- | -------------------- | ------------------------ | ------ |
| Member ID       |             | : 1                  |                          |        |
| MAC Address     |             | : ec:eb:b8:d0:80:40  |                          |        |
| Type            |             | : JL557A             |                          |        |
| Model           |             | : Aruba JL557A       | 2930F-48G-740W-PoE+-4SFP | Switch |
| Status          |             | : Master             |                          |        |
| ROM Version     |             | : SL.10.02.0000-7755 |                          |        |
| Serial          | Number      | : CN7ZK90012         |                          |        |
| Uptime          |             | : 0d 0h 18m          |                          |        |
| CPU Utilization |             | : 0%                 |                          |        |
| Memory          | Utilization | : 15%                |                          |        |
| VSF link        | 1           | : Down               |                          |        |
| VSF link        | 2           | : Down               |                          |        |
| show vsf        | topology    |                      |                          |        |
Syntax
show vsf topology
Description
DisplaysinformationaboutVSFstackmemberconnections.
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeriesUserGuide 42

| Command | context |     |
| ------- | ------- | --- |
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#    | show vsf topology |        |
| ---------- | ----------------- | ------ |
|            | Stby              | Master |
| +---+      | +---+ +---+       |        |
| | 3 |1==2| | 2 |1==1|          | 1 |    |
| +---+      | +---+ +---+       |        |
VSFcommands|43

Chapter 9

Frequently asked questions

Frequently asked questions

What is VSF?

Virtual Switching Framework, or VSF, defines a single virtual switch comprised of multiple individual
physical switches that are interconnected through standard Ethernet links. These links are referred to as
VSF links.

These physical switches will function as one device with a unified control and management plane.

Multiport VSF links are supported.

What are the supported platforms for VSF?

The Aruba 6300F/M Switch Series supports VSF.

VSF can be formed with a combination of any of the Aruba 6300F/M Switch Series (JL658A, JL659A,
JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A, JL667A, JL668A) or a combination of any of the
Aruba 6200F Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A).

Aruba 6200F Switch Series only supports fixed SKUs.

What port speeds do VSF links support?

For Aruba 6300F/M Switch Series: All uplink ports with 10G, 25G, and 50G speeds can be configured as
VSF links.

For Aruba 6200F Switch Series: All uplink ports with 10G speed can be configured as VSF links.

Aruba recommends that all VSF links be configured to run at the same speed.

Can VSF be disabled?

Users cannot disable VSF. A factory default switch boots up as a VSF-enabled device with its Member ID
set to 1.

What is a primary switch in VSF stack? Is it configurable?

Only the switch with a Member ID of 1 will be the primary switch in a VSF stack. This switch will function
as the stack master and will drive the control and management plane for the stack.

What is a secondary switch in a VSF stack? Is it configurable?

The secondary switch will function as the standby in a stack. There is no secondary switch by default.
Any member other than Member 1 can be configured as the secondary switch using the vsf secondary-
member <MEMBER-ID> command.

Aruba strongly recommends that you configure a secondary member (standby) for stack high-
availability.

How many secondary member switches are configurable in a VSF stack?

A VSF stack can be configured with one secondary member only.

Once it is configured, is it possible to change the secondary member?

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series | User Guide

44

Yes. Remove the current secondary member using the no vsf secondary-member command. This
action will trigger the member to reboot and join the stack (not a standby anymore).

A new secondary member can be configured using the vsf secondary-member <MEMBER-ID> command.
The device will reboot and rejoin the stack back as standby.

The secondary member configuration can only be changed when Member 1 is master of the stack.

How are master and standby for a stack determined?

By default, the primary member (Member 1) becomes the master of the stack and the user-configured
secondary member becomes the standby.

The secondary member synchronizes all its states with the master. If the current master (Member 1)
fails, the standby (secondary member) will seamlessly transition to the master role. In this state, if
Member 1 comes back up, it will take the standby role.

Only primary and secondary members can take up master and standby roles in a stack.

What is the role of other members in a stack?

All devices other than the master and standby are called members. These devices do not have any
network, control, or management plane functions. Their interfaces are directly controlled and managed
by the master switch.

Is there any restriction in the order of VSF member numbering?

There is no restriction on the order in which VSF members can be numbered. Each member, however,
must have a unique number in the range of 1-10 (for 6300 switches) or 1-8 (for 6200F switches).

What is the supported stack height and topology?

n 6200F platforms can stack up to 8 members with no modular SKU (only fixed SKU).

n 6300 F/M platforms can stack up to 10 members in a chain or ring topology.

Ring is the recommended topology. This topology requires that each member is configured with two
VSF links, interconnecting each member with two other members in the stack.

On a two-member stack, configure only one VSF link that connects to its peer.

There is no concept of a ring topology in a two-member stack.

Can features be configured on a VSF link?

Once an interface becomes part of a VSF link, no standard network layer protocol or feature can run on
that interface because it is part of the VSF stack fabric.

Will configurations in an individual member switch be retained after joining a stack?

Individual member device configurations are not retained after the switch is renumbered and becomes
part of a stack.

How do the consoles of each member in a stack work?

The console of the master switch provides a full CLI that can be used to manage the stack. Consoles of
other stack members, including the standby, have a limited set of CLI commands that are useful for
troubleshooting the device from a stacking functionality standpoint.

How does an image upgrade for a stack work?

Frequently asked questions | 45

To upgrade a stack to a new firmware image, use the copy <TFTP/SFTP> image command to download
the image to the device. The image will be downloaded to the stack master first and then be distributed
to the other members of the stack automatically.

After downloading the firmware, reboot the stack using the boot system <PRIMARY/SECONDARY>
command. This action completes the upgrade process.

Adding or rebooting individual members before the upgrade process is complete can cause the
individual member to fail while joining the stack.

Can I add a member to the VSF stack when the member is running an image with a
different version than the stack?

When a device joins a stack and its firmware version is different from the version on the master, the
master will push its firmware copy to the device. Once the device receives a copy of the firmware, it will
reboot and rejoin the stack, now running the same version as the master.

What happens when the VSF master switch goes down?

The standby switch, if present, will take the role of the master. The old master switch will boot and join
the stack as the standby switch. This transition will be seamless with limited network impact.

In the absence of a standby (no secondary member configuration), master device failure causes the
remaining VSF members to reboot and come back up. At this point, members will enter a state in which
they are waiting for the master to come back up. During this time, front plane ports of the members will
be down.

How do I recover a device that has not joined a stack due to misconfiguration?

The vsf renumber-to command is used to trigger a device to take up its new member number and light
up its VSF links. This command causes the device to reboot, come back up and wait for messages from
the stack master. If the VSF link is configured incorrectly or the member number is wrong, the device
could be waiting in this state indefinitely.

To recover a device in this state, execute the following commands:

1. Execute the ctrl+c command on the device console. This action launches the recovery console.

2. Execute the vsf-factory-reset command on the recovery console.

This action resets the device to factory-default.

n The device will come back up as member ID 1 with no VSF link configuration.

n The device can be configured with the correct member number and VSF links.

n The vsf renumber-to command will trigger this configuration to take effect.

The recovery console also has commands that allow the user to copy support files to an external server.
This functionality is useful for troubleshooting stacking-related issues.

How do the management ports of each member in a stack work?

In a stack, only the master management interface is active. The management interface can be assigned
an IP address for device management purposes. When a master device fails, the standby becomes
master and activates its management interface.

How does replacing the master switch in a stack work?

The replacement device must be of the same part number as the switch being replaced. You must also
have a standby switch configured for replacing the master of a stack without losing configuration.

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series User Guide

46

Complete the following steps:

1. Execute the vsf switchover command to trigger the standby switch to take over the master role.

2. Once the stack is up with the new master, remove all physical connections from the old master

switch that is being replaced.

3. Configure VSF interfaces/links on the new device. It is of critical importance to match the

interfaces configured on the switch being replaced.

4. Physically connect the new device to the stack through configured VSF links.

5. The new switch will join the stack and take up the role of standby.

What is the workflow for replacing a standby or member switch?

The replacement device must be of the same part number as the switch being replaced.

Complete the following steps:

1. Configure VSF interfaces/links on the new device. It is of critical importance to match the

interfaces configured on the switch being replaced.

2. Renumber the new device to match the switch being replaced.

3. Physically connect the new device to the stack through configured VSF links.

4. The new switch will join the stack and take up the standby or a member role based on the

secondary configuration for the stack.

What happens if a VSF link fails?

n If the stack topology is a ring, it will degenerate to a chain when a VSF link in the stack fails.

n If the topology is a chain, a VSF link failure will result in a stack being split into two independent stack

fragments.

n When a stack splits and the master and standby of the stack become part of two different fragments,
the standby takes up the master role for its fragment. Network disruption can result because the two
fragments are simultaneously active. Aruba highly recommends enabling VSF split-detection to
gracefully handle split brain scenarios.

n If a stack splits and the master and standby are in the same fragment with the other members on a

different fragment, the members-only fragment will:

o Reboot.

o Come back up.

o Wait for communication from the stack master.

What is VSF split-detect?

When a stack splits, the split-detect feature provides a mechanism for the fragments to discover each
other.

Once the two stack fragments are discovered, the fragment that has the primary member becomes the
active fragment and keeps its front plane (non-VSF) interfaces up and running. The other fragment
becomes inactive and all non-VSF interfaces on the inactive fragment are brought down to avoid
network disruption.

How do I configure split-detect?

VSF supports split-detection through the management interface.

Frequently asked questions | 47

Connectthemanagementinterfacesoftheprimaryandsecondarymemberstothesamemanagement
VLAN/networkorconnectthemdirectlytooneanother.TheCLIcommandtoenablesplitdetectionis
| vsf split-detect | mgmt.    |             |                |             |
| ---------------- | -------- | ----------- | -------------- | ----------- |
| How do           | I remove | the non-VSF | configurations | in a stack? |
Usetheerase startup-configcommandontheVSFstack.Thisactionwillremoveallnon-VSFrelated
configurationsfromthestartup-config.Thenrebootthestack.
| Can a | VSF member | be removed | from a stack? |     |
| ----- | ---------- | ---------- | ------------- | --- |
Yes,removeamemberfromthestackusingtheno vsf member <MEMBER-ID>command.All
configurationsassociatedwiththememberwillalsoberemoved.Thememberwillbootandcomeback
upwiththefactorydefaultconfiguration.
| How do | I remove | the master | switch from | the stack? |
| ------ | -------- | ---------- | ----------- | ---------- |
Arubadoesnotrecommendremovingamemberthatismasterofastack.
Ifthemasterswitchhastoberemoved,completeaswitchoverandwaitfor:
n thestandbytotakeupthemasterrole,and
n theoldmastertorebootandjointhestackasstandby.
Thenuseamemberremovecommandtoremovethedevicefromthestack.
How can I boot the whole VSF stack and individual members using CLI?
| Theboot                            | systemcommandcanbeusedtobootthewholestack. |     |        |     |
| ---------------------------------- | ------------------------------------------ | --- | ------ | --- |
| Tobootanindividualmember,usethevsf |                                            |     | member |     |
| <MEMBER-ID>                        | rebootcommand.                             |     |        |     |
Is modifying the VSF-specific configuration using Checkpoint restore or TFTP/SFTP/USB
| download | supported? |     |     |     |
| -------- | ---------- | --- | --- | --- |
Thisfunctionalityisnotsupported.BeforeapplyingaconfigurationonastackthroughCheckpoint
restoreorTFTP/SFTP/USBdownload,youmustensurethatthefollowingconfigurationsmatchexactly:
n ThecurrentstackVSFconfigurations.
n TheVSFconfigurationsthatarepartoftheconfigurationfilethatisbeingrestoredordownloaded
fromtheserver.
Specifically,thecurrentVSFstackandtheCheckpoint/downloadedconfigurationthatwillbeappliedon
thestackmusthavethesame:
Numberofmembers
n
n Memberpartnumber(J#)
n Membernumber
n VSFlinkconfigurations
n Secondarymemberconfiguration
n Split-detectconfiguration
| How can                                 | I dismantle | a stack? |     |                     |
| --------------------------------------- | ----------- | -------- | --- | ------------------- |
| AVSFstackcanbedismantledbyusingtheerase |             |          |     | all zeroizecommand. |
Thisactionwillcauseeachmembertoreboot,comebackupwithfactorydefaults,andfunctionas
individual/standalonedevices.
AOS-CXVirtualSwitchingFramework(VSF)Guidefor6200,6300SwitchSeriesUserGuide 48

How do I collect support files for a stacked device?

The copy support-files all command executed on the master console will collect support and
troubleshooting information from all members that are part of the stack.

If a member is not part of the stack, you must run the same command from the recovery console of the
respective member.

If a stack has split into two fragments, both fragments will have a master. Execute the same command
on the master console of both fragments.

Why do I see the message 'Warning - management/VSF role decision pending, HPE
Credential Manager daemon may shut down and restart.'

During the boot time, this message might appear due to a delay in discovering the role, or if the VSF
links took longer than usual to became operational. The message is only informational and will not
cause any functionality impact.

Frequently asked questions | 49

Chapter 10

Support and other resources

Support and other resources

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

Accessing updates
You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

AOS-CX Virtual Switching Framework (VSF) Guide for 6200, 6300 Switch Series | User Guide

50

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

Warranty information
To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Regulatory information
To view the regulatory information for your product, view the Safety and Compliance Information for
Server, Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs,
product recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For
more information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation feedback
Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback
(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

Support and other resources | 51