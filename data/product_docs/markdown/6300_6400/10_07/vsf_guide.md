|           | AOS-CX | 10.07     |     | Virtual |       |
| --------- | ------ | --------- | --- | ------- | ----- |
| Switching |        | Framework |     |         | (VSF) |
Guide
|     | 6200, | 6300 | Switch | Series |     |
| --- | ----- | ---- | ------ | ------ | --- |
PartNumber:5200-7889
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
| Contents                                              |                                    | 3   |
| ----------------------------------------------------- | ---------------------------------- | --- |
| About                                                 | this document                      | 5   |
| Applicableproducts                                    |                                    | 5   |
| Latestversionavailableonline                          |                                    | 5   |
| Commandsyntaxnotationconventions                      |                                    | 5   |
| Abouttheexamples                                      |                                    | 6   |
| Identifyingswitchportsandinterfaces                   |                                    | 6   |
| Introduction                                          |                                    | 8   |
| Terminology                                           |                                    | 8   |
| ConnectionTopology                                    |                                    | 9   |
| Feature                                               | overview                           | 10  |
| VSFBehavior                                           |                                    | 10  |
| OneVirtualDevice                                      |                                    | 10  |
| Interoperation                                        |                                    | 14  |
| Linkaggregation                                       |                                    | 14  |
| Stack                                                 | management                         | 16  |
| Consoles                                              |                                    | 16  |
| Managementinterface                                   |                                    | 16  |
| VSFconfiguration                                      |                                    | 16  |
|                                                       | Membernumber                       | 16  |
|                                                       | AccesstoVSFmembers                 | 16  |
|                                                       | VSFlinks                           | 17  |
|                                                       | Memberprovisioning                 | 17  |
|                                                       | Secondarymember                    | 17  |
|                                                       | Memberremove                       | 17  |
| Automatedimagesync                                    |                                    | 18  |
| Reboot                                                |                                    | 18  |
| Memberadditionwithoutauto-stacking                    |                                    | 19  |
| Memberadditionwithauto-stacking                       |                                    | 19  |
| Memberreplacementwithoutauto-stacking                 |                                    | 19  |
| Memberreplacementwithauto-stacking                    |                                    | 19  |
| StackandPortLEDstates                                 |                                    | 19  |
| Configuring                                           | a VSF stack                        | 21  |
| VSFauto-stacking                                      |                                    | 21  |
|                                                       | Peerdiscovery                      | 21  |
|                                                       | Auto-joineligibility               | 21  |
|                                                       | Forceauto-joinsupport              | 21  |
|                                                       | Designatingmasterswitch            | 22  |
|                                                       | Reservedinterfacesforauto-stacking | 23  |
| Formingafour-memberringsetupusingauto-stackingcommand |                                    | 23  |
Forminganeight-memberringsetupmanuallyusinglinkconfigurationwithoutauto-stacking 25
| Misconfigurationrecovery |              | 28  |
| ------------------------ | ------------ | --- |
| Failure                  | and recovery | 30  |
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide| (6200,6300
3
SwitchSeries)

| Stacksplit                        |                    |           |                  | 30  |
| --------------------------------- | ------------------ | --------- | ---------------- | --- |
| Managementinterfacesplitdetection |                    |           |                  | 30  |
| VSF recommendations               |                    | and       | restrictions     | 33  |
| VSF Commands                      |                    |           |                  | 35  |
| vsfmember                         |                    |           |                  | 35  |
| member                            |                    |           |                  | 36  |
| type                              |                    |           |                  | 37  |
| link                              |                    |           |                  | 38  |
| vsfforce-auto-join                |                    |           |                  | 40  |
| vsfstart-auto-stacking            |                    |           |                  | 40  |
| vsfsplit-detect                   |                    |           |                  | 41  |
| vsfsecondary-member               |                    |           |                  | 42  |
| vsfrenumber-to                    |                    |           |                  | 43  |
| vsfmemberreboot                   |                    |           |                  | 44  |
| interface                         |                    |           |                  | 45  |
| shutdown                          |                    |           |                  | 45  |
| showvsf                           |                    |           |                  | 46  |
| showvsfdetail                     |                    |           |                  | 46  |
| showvsflink                       |                    |           |                  | 48  |
| showvsflinkdetail                 |                    |           |                  | 49  |
| showvsflinkerror-detail           |                    |           |                  | 50  |
| showvsflinkerror-detailmember     |                    |           |                  | 51  |
| showvsfmember                     |                    |           |                  | 53  |
| showvsftopology                   |                    |           |                  | 53  |
| Frequently                        | asked              | questions |                  | 55  |
| Frequently                        | asked              | questions | on Auto-stacking | 61  |
| Support                           | and Other          | Resources |                  | 66  |
| AccessingArubaSupport             |                    |           |                  | 66  |
| AccessingUpdates                  |                    |           |                  | 66  |
|                                   | ArubaSupportPortal |           |                  | 66  |
|                                   | MyNetworking       |           |                  | 67  |
| WarrantyInformation               |                    |           |                  | 67  |
| RegulatoryInformation             |                    |           |                  | 67  |
| DocumentationFeedback             |                    |           |                  | 67  |
Contents|4

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

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

n example-text

|

{ }

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

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide | (6200, 6300 Switch Series)

5

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
Examplesinthisdocumentarerepresentativeandmightnotmatchyourparticularswitchorenvironment.
Theslotandportnumbersinthisdocumentareforillustrationonlyandmightbeunavailableonyour
switch.
| Understandingthe | CLI prompts |     |     |
| ---------------- | ----------- | --- | --- |
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
Incertainconfigurationcontexts,thepromptmayincludevariableinformation.Forexample,wheninthe
VLANconfigurationcontext,aVLANnumberappearsintheprompt:
switch(config-vlan-100)#
Whenreferringtothiscontext,thisdocumentusesthesyntax:
switch(config-vlan-<VLAN-ID>)#
Where<VLAN-ID>isavariablerepresentingtheVLANnumber.
| Identifying | switch | ports and | interfaces |
| ----------- | ------ | --------- | ---------- |
Physicalportsontheswitchandtheircorrespondinglogicalsoftwareinterfacesareidentifiedusingthe
format:
member/slot/port
| On the 6200Switch | Series |     |     |
| ----------------- | ------ | --- | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to8.The
primaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis1.
Aboutthisdocument|6

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide (6200, 6300 Switch Series)

7

Chapter 2

Introduction

Introduction

Virtual Switching Framework, or VSF, defines a virtual switch, comprising multiple individual physical
switches, interconnected through standard Ethernet links. These physical switches will operate with one
control plane, visible to peers as a virtual switch stack. This composition simplifies management and
provides the capability to scale the stack.

On-demand scalability in the access layer allows the user to increase the number of ports on a stack as per
needs, without having to manage a new switch. The same stack can scale up or down to match the
requirements.

n 6200F: VSF allows stacks to be formed using any combination of SKUs of the 6200 family. Up to 8

member switches will be allowed. Connections between the switches must use 10G links.

n 6300: VSF allows stacks to be formed using any combination of SKUs of the 6300 family. Up to 10

member switches will be allowed. Connections between the switches must use 10G, 25G, or 50G links. All
VSF links in a stack should operate at the same speed.

Terminology

Table 1: Acronyms used in this book

Term Definition

VSF

Virtual Switching Framework

L2

L3

Layer 2 of the OSI 7-layer model

Layer 3 of the OSI 7-layer model

SKU

Stock Keeping Unit

FRU

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

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide | (6200, 6300 Switch Series)

8

Role

Master

Definition

Controls VSF administration and control plane.

Standby

Standby management and under control of the master; synchronizes control plane with

the master.

Member

All devices in the stack other than the master and standby are called member switches.

The member switch does not run any networking protocols and has no states. The

interfaces on this switch are directly controlled and programmed by the master switch.

Connection Topology
VSF supports up to 8 member stacks (for 6200F devices) or 10 member stacks (for 6300 devices) in ring and
chain topology.

Figure 1 Chain topology

Figure 2 Ring topology

Ring is the recommended deployment topology. It inherently provides resiliency against a single failure of a
link or switch.

Introduction | 9

Chapter 3

Feature overview

Feature overview

VSF is always enabled on supported switches. Within the stack, one switch is the Master that runs all control
plane software and manages the ASICs of all stack members. Any switch apart from primary can be
configured as Standby switch.

VSF Behavior
Each stack member must have a unique member number. When deploying a stack, ensure that each
member has a distinct number by renumbering the switches to the appropriate member numbers. Stack
formation will fail if there is a member number conflict.

n The primary member will become Master and the secondary member will become Standby under normal

circumstances.

n The primary member is member number 1. This setting is not configurable and 1 is the default. A factory-

default switch boots up as a VSF-enabled switch with a member number of 1.

n The secondary member number is user configurable, and there is no default secondary member. It is
recommended that the customer configures a secondary member in the stack, since a stack with a
standby offers resiliency and high-availability.

n No members other than primary and secondary members can become Master or Standby of the stack.

In a standard deployment, uplinks should be from primary and secondary. The management interface from

primary and secondary members should be connected to the management network, providing management

connectivity to the current master.

One Virtual Device
Once the VSF stack is formed, all interconnected switches operate as a single virtual switch with a single
control plane. All interfaces of all switches in the stack are available for configuration and management.

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide | (6200, 6300 Switch Series)

10

Figure 3 Onevirtualdeviceexampletopology
| switch#     | show        | vsf    |         |                   |        |     |     |
| ----------- | ----------- | ------ | ------- | ----------------- | ------ | --- | --- |
| Force       | Autojoin    |        | :       | Disabled          |        |     |     |
| Autojoin    | Eligibility |        | Status: | Not Eligible      |        |     |     |
| MAC Address |             |        | :       | 08:97:34:b0:0e:00 |        |     |     |
| Secondary   |             |        | :       | 2                 |        |     |     |
| Topology    |             |        | :       | Chain             |        |     |     |
| Status      |             |        | :       | No Split          |        |     |     |
| Split       | Detection   | Method | :       | None              |        |     |     |
| Mbr MAC     | Address     |        | Type    |                   | Status |     |     |
ID
| --- ------------------- |     |     | -------------- |     | ----------------- |     |     |
| ----------------------- | --- | --- | -------------- | --- | ----------------- | --- | --- |
| 1 08:97:34:b0:0e:00     |     |     | JL666A         |     | Master            |     |     |
| 2 08:97:34:b1:43:00     |     |     | JL665A         |     | Standby           |     |     |
| 3 08:97:34:b7:cc:00     |     |     | JL663A         |     | Member            |     |     |
| 4                       |     |     | JL662A         |     | Not Present       |     |     |
Interfaceswillbenumberedasnotedinthefollowingtable.
| Name   | MemberNumber |     |     | Slot | Port |     |     |
| ------ | ------------ | --- | --- | ---- | ---- | --- | --- |
| 1/1/1  | 1            |     |     | 1    | 1    |     |     |
| 2/1/14 | 2            |     |     | 1    | 14   |     |     |
| 8/1/12 | 8            |     |     | 1    | 12   |     |     |
Slotnumberisalwaysfixedas1.Allinterfacesareavailableforconfiguration.
switch#
|     | show | interfaces | brief |     |     |     |     |
| --- | ---- | ---------- | ----- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
| Port | Native | Mode | Type |     | Enabled Status | Reason | Speed |
| ---- | ------ | ---- | ---- | --- | -------------- | ------ | ----- |
Featureoverview|11

|     | VLAN |     |     |     | (Mb/s) |
| --- | ---- | --- | --- | --- | ------ |
----------------------------------------------------------------------------------
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
| 6300(config)# | show run       |     |     |     |     |
| ------------- | -------------- | --- | --- | --- | --- |
| Current       | configuration: |     |     |     |     |
!
| !Version          | ArubaOS-CX FL.10.07.xxxx |     |     |     |     |
| ----------------- | ------------------------ | --- | --- | --- | --- |
|                   |                          |     |     |     |     |
| !export-password: | default                  |     |     |     |     |
cli-session
| timeout | 0   |     |     |     |     |
| ------- | --- | --- | --- | --- | --- |
!
!
!
!
!
!
| ssh server           | vrf default |     |     |     |     |
| -------------------- | ----------- | --- | --- | --- | --- |
| ssh server           | vrf mgmt    |     |     |     |     |
| vsf secondary-member | 2           |     |     |     |     |
| vsf member           | 1           |     |     |     |     |
| type                 | jl666a      |     |     |     |     |
| link                 | 1 1/1/26    |     |     |     |     |
| link                 | 2 1/1/25    |     |     |     |     |
| vsf member           | 2           |     |     |     |     |
| type                 | jl666a      |     |     |     |     |
| link                 | 1 2/1/25    |     |     |     |     |
| link                 | 2 2/1/26    |     |     |     |     |
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
| vlan      | access 1 |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
| interface | 1/1/3    |     |     |     |     |
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 12

no shutdown
no routing
vlan access 1

interface 1/1/4
no shutdown
no routing
vlan access 1

interface 1/1/5
no shutdown
no routing
vlan access 1

interface 1/1/6
no shutdown
no routing
vlan access 1

...
...
interface 2/1/1
no shutdown
no routing
vlan access 1

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
vlan access 1

interface 2/1/6
no shutdown
no routing
vlan access 1

...
...

!
!
!
!
!
https-server vrf default
https-server vrf mgmt
switch(config)#

As shown in this configuration, interfaces of all member switches can be configured from the Master.

Once a stack is deployed, the stack configuration is sticky. The user can safely remove all other
configurations with the command erase startup-configuration without disturbing the stack
configurations. To remove all configurations, including the stacking configurations, use the command erase
all zeroize, where all members of the stack will be reset to factory defaults

Feature overview | 13

Interoperation
TheVSFstacksupportseither:
n 6200Fdevices,or
n 6300devices(6300Mor6300F).
VSFstackingcannotbedonewithamixedsetofswitches.Thestackmustbemadeupofonly6200oronly6300
switches.
Aruba6200Fdoesnotsupportmodularunits.
FirmwareversionspriortoAOS-CX10.07arenotinteroperablewith10.07orlaterversions.
Link aggregation
Linkaggregations(L-Agg)canspaninterfacesacrossmultipleindividualswitcheswithinthestack.Load
balancingisperformedonallinterfacesoftheL-AggacrossthestackandisapplicabletoL2andL3L-Aggs.
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
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 14

------------------------------------------------------------------------------
1/1/18 lag1 up
2/1/18 lag1 up
1/1/23 lag2 up
2/1/23 lag2 up
| Partner details | of all interfaces: |     |     |
| --------------- | ------------------ | --- | --- |
------------------------------------------------------------------------------
| Intf Aggr | Port Port | State System-ID | System Aggr |
| --------- | --------- | --------------- | ----------- |
| Name      | Id Pri    |                 | Pri Key     |
------------------------------------------------------------------------------
1/1/18 lag1
2/1/18 lag1
1/1/23 lag2
2/1/23 lag2
Featureoverview|15

Chapter 4

Stack management

Stack management

Consoles
The serial console of the Master switch provides a full CLI configuration interface for a user with valid
credentials. The serial console of the other stack members, including the Standby, provides a reduced CLI
configuration interface, with only a limited set of commands for troubleshooting the stack.

In a standard deployment, connect to the console interface of the master and standby switch. This enables
the stack master console to be reachable after a stack failover to the new Master.

Any switch configuration or monitoring must be performed from the console of the stack Master switch only.

Management interface
In a VSF stack, only the management interface on the Master switch will be assigned an IP address
(configured or assigned by DHCP). The stack allows connectivity to management protocols and Console
through the management interface on the Master.

VSF configuration
The following aspects of VSF are user-configurable.

Member number

To add a device to a VSF stack, the device must be renumbered to the corresponding member ID. The user
can specify the member number of the switch. The default member number is 1.

n For the 6200F device, the default number can be changed to any value from 2 through 8. (The device

supports up to 8 members.)

n For 6300 devices, the default number can be changed to any value from 2 through 10. (The device

supports up to 10 members.)

Refer to vsf renumber-to and Misconfiguration recovery for information about renumbering a member.

Changing the member number causes the switch to reboot and all configuration on the switch is removed.

A switch with a member number other than 1 cannot boot completely unless it has reachability to a VSF
master switch via VSF link. If a renumbered member is unable to communicate with the master switch and is
waiting in booting state, the user can:

n Go to a recovery console with a ctrl+c sequence and collect the diagnostic information, or

n Reset the VSF configuration.

Access to VSF members

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide | (6200, 6300 Switch Series)

16

In addition to serial console connections, any stack member can be accessed from any other member using
the member command.

Refer to member for information about console connection to a member switch.

VSF links

The user can specify the interfaces which comprise the VSF links. Refer to link for information about
specifying interfaces.

When the interface is configured, any existing configuration is removed, including VLAN memberships,
ACL/Quality of Service rules and any speed/duplex/MTU configuration.

Once the interface becomes part of a VSF link, no protocol or feature will be allowed to run on it as it is now
part of the fabric.

A VSF link will be a routed interface.

Member provisioning

VSF allows the user to provision or pre-configure any member before the member is physically added to the
stack. Provisioning the member allows the user to complete the required configuration as if the member is
present in the stack. When the member eventually joins the stack, it will boot up with the configuration
made on the pre-provisioned interfaces.

To provision a member, the part number of the member must be specified. Refer to type for information
about provisioning a member.

If a member tries to join the stack with a different part number to the one provisioned on the Master, the

renumbered member will be removed from the stack and will reboot with factory defaults.

Secondary member

The stack will not have a standby member by default. A secondary member can be configured from
available members and it will be assigned the role of stack standby.

Member number 1 can never be configured as a secondary member.

When configured as secondary, a stack member that is already present in the stack will reboot and rejoin the
stack as the standby.

A provisioned member can be configured as a secondary member. When the member joins the stack, it will
boot up in the standby role, without any further reboot.

If a secondary member is already configured and physically present in the stack, removing the secondary
will cause the secondary member to reboot and join as a member.

Refer to vsf secondary-member for information about configuring a secondary member.

In the case of auto-stacking, member 2 is automatically configured as secondary member through
LED button press or vsf start-auto-stacking command.

Member remove

A member can be removed from a running stack. All configuration associated with the member will be
removed.

Stack management | 17

If the member is physically present in the stack at the time it is removed, all VSF configurations on that
member will be erased and it will lose its identity as a member of the stack from which it was removed. The
member will come back as member 1 with factory default configuration.

It is not advisable to remove the member that is the master of the stack. If the master has to be removed, the

recommendation is to switch over and wait for the old master to come up as standby before removing it.

Refer to the vsf member command for information about removing a member.

Though it is not recommended as it can cause traffic outages, if an active member needs to be removed
from a stack, member must be physically removed after issuing no vsf member command. Else, the member
will join the stack back through auto-stacking. Alternatively, the links can be disabled first and the member
can be removed from the master. The removed member must be reset to factory-default once it boots to
recovery.

Automated image sync
In a VSF environment, all stack members run the same software image. If the user upgrades the software on
the Master by downloading a new software image using SFTP/TFTP, all members of the stack will
simultaneously upgrade.

When forming a stack, if the software version on a member is different from the version of the Master, the
member will automatically update itself to the same version as the Master. The member will reboot itself to
run the updated version before joining the stack.

Automated image sync is not applicable if the master is running the firmware version 10.07 or later and the

member is booted with firmware version 10.06 or earlier versions and vice-versa.

Reboot
An individual stack member can be rebooted from a CLI command.

n The member will reboot and re-join the stack, with the same role that it had prior to the reboot.

n If the stack topology is a ring, no traffic disruption is expected on any other stack members when a single

member is rebooted.

n If the stack topology is a chain, rebooting a member may cause a stack split, resulting in members being
unreachable from the master. This result can cause significant disruption of the stack, so use this option
with caution.

n If the member is the stack Standby, there will be no Standby in the stack until the member reboots and

re-joins the stack. At this point, the member will again have the role of Standby.

n If the member is the stack Master, the command will trigger a failover and the Standby switch will take

over as Master of the stack.

n If the Standby is unavailable at the time of master reboot, the whole stack will reboot.

The whole stack can also be rebooted by using the boot system command.

n All members will reboot and the stack will re-form.

n Traffic will be disrupted for the duration of the reboot.

Refer to vsf member reboot for information about rebooting a member.

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide (6200, 6300 Switch Series)

18

Member addition without auto-stacking
A member can be added to the stack to augment an existing stack. The member being added can be a
factory-default switch or a switch with pre-existing configuration.

1. Configure interfaces to VSF links on the member being added.

2. Renumber the member being added.

The member will not join the stack if there is a member number conflict.

3. Renumbering will cause a reboot of the switch.

4. Connect the configured VSF links to a previously configured VSF link on the stack.

5. The member joins the stack, with default configuration on its interfaces. Any previous configuration

on the member will be lost.

Member addition with auto-stacking
A new factory default switch can be added into an existing stack by physically connecting it to a given
member of the stack on the auto-stacking reserved interfaces. The newly added member will be
automatically assigned with member ID and go for a reboot. After reboot, the newly added member will join
the stack.

For more information auto-stacking reserved interfaces, Reserved interfaces for auto-stacking.

Member replacement without auto-stacking
The replacement member must be of the same part number as the switch being replaced.

1. Power off or disconnect all physical connections of the member that will be replaced.

2. Configure interfaces to VSF links on the replacement member. These interfaces must match the

interfaces configured on the switch being replaced.

3. Renumber the replacement member to the same number as the switch being replaced.

4. Renumbering will cause a reboot of the switch.

5. Connect the replacement member to the stack.

6. The member joins the stack, with the same configuration as the member it is replacing.

Member replacement with auto-stacking
Disconnect all the physical connections of the member that will be replaced and connect the new
replacement member to the same interfaces as the switch being replaced. The new member joins the stack,
with the same configuration as the member it is replacing.

The replacement member must be of the same part number as the switch being replaced.

Stack and Port LED states
The following table describes the different states of stack Stk LED.

Stack management | 19

Table 3: Stk LED States

State

Meaning

Stacking Mode is selected.

Stacking Mode is selected and stacking-related error has occurred.

Stacking Mode is not selected but still stacking-related error has occurred.

On -
Green

On -
Amber

Slow
flash
Amber

Off

Stacking mode is not selected.

The following table describes the different states of Port LED based on stack configurations and role of the
members in the stack.

Table 4: Port LED States

State

Meaning

On -
Green

Half-
bright
green

Slow
flash
green

Current Stack Member and is operational.

For example, if Port 3 is on green, this indicates that the current chassis is

member 3 in the stack.

Total members in the Stack.

Except port LEDs indicating the master and current member, all other ports
LEDs glow half-bright green.

Master of the Stack.

In a six-member stack, one of the six port LEDs glows slow flashing green

indicating that unit in the stack is the master. For example, if Stack Member 4 is

the master, Port 4 LED glow slow flashing green.

On-

The stack member is not reachable or in booting condition.

Amber

When the member is fully booted and joined the stack successfully, then LED

glows solid green.

Slow

flash

amber

The stack member is in a known fault condition. Only the global Status LED of

faulted member glows slow flash amber.

Off

The stack Member does not exist in the stack.

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide (6200, 6300 Switch Series)

20

Chapter 5

Configuring a VSF stack

Configuring a VSF stack

The following sections describe the prerequisites and procedures to configure a VSF stack.

VSF auto-stacking
VSF auto-stacking feature provides a mechanism to automatically form a stack when the stack members are
physically connected in a desired topology. This reduces the number of user intervention touch points to
form a VSF stack.

A manual stack formation procedure generally requires the user to explicitly log in to each of the switch,
configure the links, renumber it, and then make the physical connection to form a VSF stack of desired size
and topology. This is error prone since there are multiple touch-points involved in the whole work-flow for
each member. The auto-stacking feature eases this problem by reducing the number of touch-points
involved to simple physical connections of the links. A new factory default switch can be added into an
existing stack by physically connecting it to a given member of the stack. The new switch will automatically
assigned with member ID and it will go for a reboot. After reboot, the newly added member will join the
stack.

There are two major components to the auto-stacking solution:

n Peer discovery—Initiated from the master using one of the methods described in Designating master

switch.

n Auto-join Eligibility—Determined by the configuration state of each stack member. A switch with a factory

default configuration is auto-join eligible.

Peer discovery

Auto-stacking peer discovery is a uni-directional process. It starts with the VSF link containing the higher
denomination VSF port, sending a VSF peer discovery protocol packet. The peer receives the packet,
determines if it is valid, and sends a response with information including its auto-join eligibility, MAC address,
and part number. If the peer is auto-join eligible, the VSF member and link configurations are automatically
added to the running-configuration of the master.

Auto-join eligibility

A switch in its factory defaults configuration state is considered to be auto-join eligible. If the auto-join
eligible switch is connected to existing stack, it will automatically reboot and join the stack. Once it moves out
of factory default configuration state, it is not considered as auto-join eligible and cannot automatically join
an existing stack. However, user can still manually configure the links, renumber the device to make it part of
a stack. For more information, see Forming an eight-member ring setup manually using link configuration
without auto-stacking.

Force auto-join support

Only a switch with factory default configuration is considered to be auto-join eligible. In order to support
factory express deployments where the user wants to add a switch which is in its non-factory default
configuration, the force auto-join configuration support is provided. Use the vsf force-auto-join

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide | (6200, 6300 Switch Series)

21

command to force the switch to join the stack automatically. Once the user sets force auto-join in the switch
configuration, the switch will be considered as auto-join eligible and will join the stack even though the
switch does not have the factory default configuration.

Force auto-join will work only if the switch does not have any pre-existing VSF configurations.

Designating master switch

Auto-Stacking feature requires the master of the stack to be configured with VSF links. Optionally,
secondary or standby device can also be configured.

Following are different methods to designate the master:

n

Using LED mode button: Physically connect the switches in a desired topology on the reserved VSF link
ports and press the LED mode button until the mode changes to Stk on a factory defaults switch. This
will automatically configure member 2 as the secondary member and VSF links. In addition to VSF
secondary and link configurations , ztp force-provision will also be configured on the master switch.
The status of stack formation can be verified using Stk LED and Port LEDs states. For more information
on LED states, see Stack and Port LED states.

n Using start auto-stacking CLI: Physically connect the switches in a desired topology on the reserved VSF
link port and execute the vsf start-auto-stacking command to automatically configure links. The
command also configures member 2 as secondary. For more information, see Forming a four-member
ring setup using auto-stacking command

Example:

switch(config)# vsf start-auto-stacking
This will configure links and secondary on master

Do you want to continue (y/n)? y

For information on interfaces that should be configured as VSF links, refer to the Reserved interfaces for
auto-stacking section.

To use this command, the switch must be in the factory default configuration.

n Using link configuration CLI: Execute the vsf member command to configure VSF links on the master.

Example:

6300(vsf-member-1)# link 1 1/1/26
6300(vsf-member-1)# link 2 1/1/25

To form an ordered stack, it is recommended to configure higher denomination interface first into

VSF link .

n TFTP download: Full stack configuration can be downloaded into the master of the stack. The

recommendation is to first download the configuration to the startup and then move the startup to the
running configuration .

Configuring a VSF stack | 22

n ZTP download: Full stack configuration can be downloaded into the master of the stack from TFTP server

using ZTP. Once the configuration has been downloaded and applied, auto-stacking peer discovery
proceeds and forms a stack.

For more information on ZTP, refer to the Zero Touch Provisioning chapter in the Fundamentals Guide.

If full stack configuration is downloaded into the master through TFTP/ZTP, the physical connections

between the switches should be made according to the downloaded configuration.

Reserved interfaces for auto-stacking

Based on the product type of a switch, the following two interfaces are reserved for the auto-stacking
process:

n 24-port switch models: 25 and 26

n 48-port switch models: 49 and 50

Users can physically connect the switch to an existing stack on one of these reserved auto-stacking
interfaces.

The following table shows the list of reserved auto-stacking interfaces based on the product type and
platform:

Reserved Interfaces

Platform

6300

6300

6200

6200

SKU Part Number

Ports reserved for Auto-Stacking

JL658A
JL660A
JL662A
JL664A
JL666A
JL668A

JL659A
JL661A
JL663A
JL665A
JL667A
JL762A

JL724A
JL725A

JL726A
JL727A
JL728A

25 and 26

49 and 50

25 and 26

49 and 50

Forming a four-member ring setup using auto-stacking
command
Prerequisites

n All switches must be in the factory default configuration.

n All stack members must be connected in a desired topology on the reserved VSF link ports. For more

information, see Reserved interfaces for auto-stacking.

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide (6200, 6300 Switch Series)

23

In the following procedure, the vsf start-auto-stacking command is used to form a four-member stack
with the ring topology:

Figure 4 Four-member ring setup

Procedure

1. Rack up all the four switches and physically connect them on the reserved auto-stacking interfaces in

a ring setup . For more information on reserved interfaces, see

Alternatively, you can also add members one after another.

2. Designate the first switch of the rack using the vsf start-auto-stacking command as the master.

The links and secondary member will be automatically configured on the master.

switch(config)# vsf start-auto-stacking

Since the switches are already physically connected, starting with the second switch, each switch in
the stack reboots automatically and join the stack one after another automatically. The running
configuration will appear as shown below:

6300# show run
Current configuration:
!
!Version ArubaOS-CX FL.10.07.xxxx
!export-password: default
cli-session

timeout 0

!
!
!
!
!
!
ssh server vrf default
ssh server vrf mgmt
vsf secondary-member 2
vsf member 1

type jl668a
link 1 1/1/26
link 2 1/1/25

vsf member 2

Configuring a VSF stack | 24

|     | type       | jl668a   |     |     |     |     |
| --- | ---------- | -------- | --- | --- | --- | --- |
|     | link       | 1 2/1/25 |     |     |     |     |
|     | link       | 2 2/1/26 |     |     |     |     |
|     | vsf member | 3        |     |     |     |     |
|     | type       | jl668a   |     |     |     |     |
|     | link       | 1 3/1/26 |     |     |     |     |
|     | link       | 2 3/1/25 |     |     |     |     |
|     | vsf member | 4        |     |     |     |     |
|     | type       | jl668a   |     |     |     |     |
|     | link       | 1 4/1/25 |     |     |     |     |
|     | link       | 2 4/1/26 |     |     |     |     |
3. Issuea"showvsf"commandtoensurethattheringhassuccessfullyformed.Youcanalsoverify
stackformationusingdifferentLED states.FormoreinformationonLEDstates,StackandPortLED
states.
|     | 6300(config)#   | show        | vsf     |                   |     |     |
| --- | --------------- | ----------- | ------- | ----------------- | --- | --- |
|     | Force Autojoin  |             | :       | Disabled          |     |     |
|     | Autojoin        | Eligibility | Status: | Not Eligible      |     |     |
|     | MAC Address     |             | :       | 70:72:cf:ef:b7:f2 |     |     |
|     | Secondary       |             | :       | 2                 |     |     |
|     | Topology        |             | :       | Ring              |     |     |
|     | Status          |             | :       | No Split          |     |     |
|     | Split Detection | Method      | :       | None              |     |     |
|     | Mbr Mac Address |             | type    | Status            |     |     |
ID
|     | --- ------------------- |     | -------------- | --------------- |     |     |
| --- | ----------------------- | --- | -------------- | --------------- | --- | --- |
|     | 1 70:72:cf:ef:b7:f2     |     | JL668A         | Master          |     |     |
|     | 2 90:20:c2:23:67:40     |     | JL668A         | Standby         |     |     |
|     | 3 90:20:c2:24:71:c0     |     | JL668A         | Member          |     |     |
|     | 4 38:21:c7:5a:33:40     |     | JL668A         | Member          |     |     |
IffullstackconfigurationisdownloadedontothemasterthroughTFTP/ZTP,thephysical
connectionsbetweentheswitchesshouldbemadeaccordingtothedownloadedconfiguration.
| Forming       | an  | eight-member |               | ring setup | manually | using link |
| ------------- | --- | ------------ | ------------- | ---------- | -------- | ---------- |
| configuration |     | without      | auto-stacking |            |          |            |
ManualconfigurationofaVSFstackrequirestheusertoindividuallyconfigureeachswitchinthestack.This
processprovidesthebestcontrolfortheusertoconfigureVSFmembernumberandlinks.
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 25

Figure 5 Eight-memberringsetup
Procedure
Toformaneight-memberringsetupasshown,donotmaketheconnectionsinitially.Connecttheports
onlyaftereachdeviceisfullyconfigured.
1. Logintothefirstdevice,numbered1.
a. Thedefaultmembernumberis1,sonomembernumberchangeisrequired.
b. Attheprompt,enterthefollowingcommands:
switch# configure
| switch(config)#       | vsf member | 1        |
| --------------------- | ---------- | -------- |
| switch(vsf-member-1)# | link       | 1 1/1/25 |
| switch(vsf-member-1)# | link       | 2 1/1/26 |
c. Theprecedingsequenceofcommandswillconfigurethelinksformember1.
d. Ports25and26areconfiguredaslink1and2respectively.
2. Logintotheseconddevice,numbered2.
a. Executethefollowingcommands.
switch# configure
| switch (config)#      | vsf member | 1        |
| --------------------- | ---------- | -------- |
| switch(vsf-member-1)# | link       | 1 1/1/25 |
| switch(vsf-member-1)# | link       | 2 1/1/26 |
ConfiguringaVSFstack|26

| switch(vsf-member-1)# |         |          | exit          |     |            |             |
| --------------------- | ------- | -------- | ------------- | --- | ---------- | ----------- |
| switch(config)#       |         | vsf      | renumber-to   |     | 2          |             |
| This will             | save    | the VSF  | configuration |     | and reboot | the switch. |
| Do you                | want to | continue | (y/n)?        | y   |            |             |
b. Theprecedingsequenceofcommandswillconfigurethelinksonmember2.
c. Thedefaultmembernumberis"1".Thecommand"vsfrenumber-to"changesthismember
number.
d. Linksareconfiguredbeforerenumbering,andthememberidentifierintheinterfacenameis"1"
atthispoint.
e. Theswitchwillrebootafterexecutingtherenumbercommand.
3. Physicallyconnectmember2tomember1asshowninthefigure.
a. Thisactionwillcausemember2tojointhestack,withmember1asthemaster.
b. Thisresultcanbeverifiedbyexecuting"showvsf"onmember1.
4. Repeatsteps2and3,foreachstackmember3through8.
a. Besuretospecifythemembernumbercorrectlyoneachmember.
b. Ifamembernumberconflictisdetected,thememberwillNOTjointhestack.
5. Oncemember8hassuccessfullyjoinedthestack,connectmember8link2tomember1link1,to
completethering.
Issueashow vsfcommandtoensurethattheringhassuccessfullyformed.
| switch# show         | vsf |         |                     |          |          |     |
| -------------------- | --- | ------- | ------------------- | -------- | -------- | --- |
| Force Autojoin       |     |         | : Disabled          |          |          |     |
| Autojoin Eligibility |     | Status: | Not                 | Eligible |          |     |
| MAC Address          |     |         | : 38:21:c7:5d:d0:c0 |          |          |     |
| Secondary            |     |         | :                   |          |          |     |
| Topology             |     |         | : Ring              |          |          |     |
| Status               |     |         | : Active            |          | Fragment |     |
| Split Detection      |     | Method  | : None              |          |          |     |
| Mbr Mac Address      |     |         | type                |          | Status   |     |
ID
| --- ------------------- |     |     | -------------- |     | --------------- |     |
| ----------------------- | --- | --- | -------------- | --- | --------------- | --- |
| 1 38:21:c7:5d:d0:c0     |     |     | JL668A         |     | Master          |     |
| 2 38:21:c7:6a:10:c0     |     |     | JL668A         |     | Member          |     |
| 3 38:21:c7:5c:15:80     |     |     | JL668A         |     | Member          |     |
| 4 38:21:c7:5a:61:40     |     |     | JL668A         |     | Member          |     |
| 5 38:21:c7:62:66:00     |     |     | JL668A         |     | Member          |     |
| 6 38:21:c7:58:22:40     |     |     | JL668A         |     | Member          |     |
| 7 38:21:c7:5a:9c:00     |     |     | JL668A         |     | Member          |     |
| 8 38:21:c7:63:a5:00     |     |     | JL668A         |     | Member          |     |
6. Theprecedingstepswillformaneight-memberstackwithoutastandby.Tomakeanymemberthe
standby(forexample,member8),usethesecondarycommand:
a. FromtheprimaryVSFmember,configuremember8asVSFsecondarymember:
| swtich(config)# |     | vsf | secondary-member |     | 8   |     |
| --------------- | --- | --- | ---------------- | --- | --- | --- |
This will save the configuration and reboot the specified switch.
| Do you | want to | continue | (y/n)? | y   |     |     |
| ------ | ------- | -------- | ------ | --- | --- | --- |
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 27

switch(config)#
b. Thisactionwillrebootmember8anditwillrejoinasstandby.
| switch# show         | vsf    |                     |          |
| -------------------- | ------ | ------------------- | -------- |
| Force Autojoin       |        | : Disabled          |          |
| Autojoin Eligibility |        | Status: Not         | Eligible |
| MAC Address          |        | : 38:21:c7:5d:d0:c0 |          |
| Secondary            |        | : 8                 |          |
| Topology             |        | : Ring              |          |
| Status               |        | : Active            | Fragment |
| Split Detection      | Method | : None              |          |
| Mbr Mac Address      |        | type                | Status   |
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
| 8 38:21:c7:63:a5:00     |     | JL668A         | Standby         |
7. Alternatively,beforeaddingmember8tothestack,pre-configurethesecondaryas8andthen
renumberdevice8.Thisactionwillensurethatdevice8willjointhestackdirectlyasstandby.
Misconfiguration recovery
Ifaswitchfailstojointhestackbecauseofmisconfiguration,usethefollowingproceduretorestorethe
switchbacktoafactorydefaultconfiguration.
Theusermusthavemanagementconnectivitytothefailedmemberforsupportfilesfromthememberin
recoverymode.
1. PressCtrl+Contheswitchconsole.
Ifthememberisnotabletoreachmaster,itwillgotorecoveryconsoleafter10minutes.You
canpressCtrl+Ctoredirecttheswitchtotherecoveryconsoleimmediately.
2. Loginusingadministratorcredentials.
3. Attheprompt,issuethevsf-factory-resetcommand.
^C
Login: admin
Password:
recovery# vsf-factory-reset
ConfiguringaVSFstack|28

4. This resets the member to factory-default settings and the switch will come up with a default member

ID of 1.

5. Now the user can reconfigure the VSF link and renumber it to the preferred member ID.

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide (6200, 6300 Switch Series)

29

Chapter 6

Failure and recovery

Failure and recovery

The following section describes failure and recovery scenarios for stack split issues.

Stack split
Multiple link or member failures can result in a complete stack split, with the master and standby switch in
different split fragments. In this case, both master and standby switches will become master switches. Each
stack fragment will continue operating with the same configuration and state, and forward traffic between
all stations that the fragment can reach.

The downside of this scenario is that each stack fragment will have the same MAC address and IP addresses.
To avoid this scenario, configure split detection (described in the following section) which would bring down
the interfaces on one fragment to prevent duplicate MAC/IPs.

Management interface split detection

For more information, refer to vsf split-detect .

VSF stack supports management split detection, which requires users to connect the management interfaces
of the primary and secondary stack members to the same L2 network.

The Primary stack member is member "1", whereas the secondary member is the user-configured secondary
switch. Once the stack is split, both of these switches become master of their respective fragments. The
fragment with "1" as master is referred to as the primary fragment, and the fragment with the secondary
switch as master is the secondary fragment.

It is also possible to connect the management interfaces of primary and secondary to one another for split

detection.

If the secondary fragment discovers that the primary fragment is operational, it will bring down all front-
plane non-VSF interfaces on the secondary fragment to minimize network disruption due to duplicate MAC
or IP addresses.

The interfaces will remain down until the stack is reconnected or the primary fragment goes down. The
interfaces of the primary fragment will always remain operational.

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide | (6200, 6300 Switch Series)

30

Theshow vsfoutputinthePrimaryfragmentwilllooklikethis:
switch#
show vsf
| Force Autojoin       |        | : Disabled          |          |
| -------------------- | ------ | ------------------- | -------- |
| Autojoin Eligibility |        | Status: Not         | Eligible |
| MAC Address          |        | : 08:97:34:b0:0e:00 |          |
| Secondary            |        | : 2                 |          |
| Topology             |        | : Chain             |          |
| Status               |        | : Active            | Fragment |
| Split Detection      | Method | : mgmt              |          |
| Mbr Mac Address      |        | type                | Status   |
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
| switch# show         | vsf |             |          |
| -------------------- | --- | ----------- | -------- |
| Force Autojoin       |     | : Disabled  |          |
| Autojoin Eligibility |     | Status: Not | Eligible |
Failureandrecovery|31

| MAC Address     |        | : 08:97:34:b0:0e:00 |          |
| --------------- | ------ | ------------------- | -------- |
| Secondary       |        | : 2                 |          |
| Topology        |        | : Chain             |          |
| Status          |        | : Inactive          | Fragment |
| Split Detection | Method | : mgmt              |          |
| Mbr Mac Address |        | type                | Status   |
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
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 32

VSF recommendations and restrictions

Chapter 7

VSF recommendations and restrictions

The following recommendations and restrictions apply to VSF.

n Before applying a configuration on a stack through checkpoint restore or TFTP/SFTP/USB download,
make sure that current VSF-specific configurations and the intended configurations match exactly. In
other words, the VSF stack and the intended configuration must have the same:

o Total number of members

o Member types

o Member number/ID

o VSF link configurations

n A functional stack must be configured with a standby for redundancy purposes. If the master fails and

there is no standby, the stack will fail.

n If the master fails and there is a standby device, the standby becomes the new master and will take over

stack management. When the old master device is replaced, it seamlessly becomes the standby device for
the stack and there no disruption.

The MAC address of the stack will remain the same until the entire stack is rebooted, after which the stack
MAC address will be the MAC address of the new master. However, once recovered, it is not advisable to use
the removed master elsewhere in the same network until the stack is rebooted to avoid MAC address
conflicts.

n After downloading firmware to a stack, the stack must be rebooted to complete the upgrade process.
Adding or rebooting individual members before the upgrade process is completed can cause the
individual member to fail while joining the stack. A member with 10.07 software version cannot join a
stack running on earlier versions.

n If there is a discrepancy between a VSF member link configuration on the master and the VSF member

link configuration on the member, the link configuration on the member is used.

n If there is a split, failure in the connectivity between management interfaces of the master and standby
might result in two active fragments. This issue can occur even if management split-detect is enabled.

n Replacing member 1 in a stack without a standby with a new switch booted as member 1 will reset all

configurations on the stack.

n Do not connect a renumbered member to multiple primary devices through VSF links.

n Before removing an individual interface from VSF link using the command no link <x> <interface>,

ensure that the interface is admin shutdown at both local and peer ends. For example: Interface 1/1/25
on member 1 link 1 is connected to 2/1/25 on member 2 link 2. The user intends to remove 1/1/25 from
link 1 of member 1. Both the interfaces 1/1/25 and 2/1/25 have to be admin shutdown before actually
removing them from the link configuration. To delete the link completely using the no link <x>
command, all individual interfaces in the VSF link have to be admin shutdown both at local and peer ends.

n There may be instances in which a master switch with vsf secondary <id> configuration is unable to

discover the standby switch. In such cases, the master switch will wait for up to 6 minutes to detect the
standby switch.

n When applying a configuration on a stack from Central/NetEdit/ZTP/TFTP or through a checkpoint

restore to remove members from the stack, consider the following recommendations:

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide | (6200, 6300 Switch Series)

33

a.

If you are removing members that are physically present, it is recommended to remove one
member at a time. In the case of ring topology, once a single member is removed, the topology will
get transitioned to a chain topology. After that, members must be removed starting from the
farthest end.

b.

If you are removing provisioned members, then you can remove multiple members at the same
time.

Removing more than one member at a time through configuration restoration

(ZTP/Central/Checkpoint) might result in non-deterministic behavior. This might cause the members

to reboot and drop to the console.

n If the entire stack configuration needs to be provisioned manually using CLIs, ensure that the master’s

VSF link configuration is done at the last.

n For TFTP download, the recommended work-flow is to copy the configuration to startup first, and then

copy to running-configuration. The direct download of TFTP to running-configuration is not
recommended.

n

It is not recommended to change the VSF configurations (links & secondary) on the master when one or
more members of the stack are booting.

VSF recommendations and restrictions | 34

Chapter 8

VSF Commands

VSF Commands

vsf member

Syntax

vsf member <MEMBER-ID>
no vsf member <MEMBER-ID>

Description

Creates VSF member context in the switch for the specified member.

The no form of this command removes the specified member from the stack. All configuration associated
with the member, as well as the subsystems and interfaces of the member will also be removed.

If the member is physically present in the stack at the time it is removed, it will reboot with the default
configuration and lose its identity as a member of the stack from which it was removed.

When a physically present member is removed, it may cause the stack to split.

Command context

config

Parameters

<MEMBER-ID>

VSF member identifier.

n Range for 6200F devices: 1-8.

n Range for 6300 devices: 1-10.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring a VSF member:

switch(config)# vsf member 2
switch(vsf-member-2)#

Removing a non-master member from the stack:

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide | (6200, 6300 Switch Series)

35

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
Commandcontext
Manager(#)
Parameters
<MEMBER-ID>
VSFmemberID.Required.
n Rangefor6200Fdevices:1-8.
Rangefor6300devices:1-10.
n
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
VSFstackisformedwithtwomembers:
| switch#             | member     | 2          |           |           |          |              |
| ------------------- | ---------- | ---------- | --------- | --------- | -------- | ------------ |
| admin@172.17.17.2's |            |            | password: |           |          |              |
| Last login:         | 2019-09-30 |            |           | 11:42:17  | from the | console      |
| User "admin"        |            | has logged |           | in 1 time | in the   | past 30 days |
member-2#
Membertoself:
| switch# | member    | 1   |      |     |     |     |
| ------- | --------- | --- | ---- | --- | --- | --- |
| Already | on member |     | id 1 |     |     |     |
VSFstackisnotformedandmembernotavailable:
VSFCommands|36

| switch# member | 2               |     |     |     |
| -------------- | --------------- | --- | --- | --- |
| No stack       | role for member | id  | 2   |     |
type
Syntax
type <TYPE>
Description
ConfiguresthepartnumberoftheVSFmemberbeingprovisioned.Afterprovisioning,theinterfacesofthe
memberareavailableforconfiguration.
Whenthemembereventuallyjoinsthestack,itwillbootupwiththeconfigurationmadeonthepre-
provisionedinterfaces.
Toprovisionamember,themembernumberandthepartnumberofthemembermustbespecified.
Commandcontext
vsf-member-<ID>
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
| jl762a                 | 6300M 48G 4SFP56  |         | Pwr2Prt        | Switch            |
| switch(vsf-member-2)#  |                   | type    | jl662a         |                   |
| switch(vsf-member-2)#  |                   | show    | running-config |                   |
| Current configuration: |                   |         |                |                   |
!
| !Version | ArubaOS-CX |     |     |     |
| -------- | ---------- | --- | --- | --- |
!
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 37

!
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

Once an interface is part of a VSF link, all existing configuration on the interface is removed and the interface
will operate as a VSF interface. At least one interface must be specified for the creation of a VSF link. VSF
interfaces carry VSF traffic and can only be connected to other VSF interfaces.

The no form of the command can be used to remove interfaces from a link or remove configuration from
the link completely.

When configuration is removed from a link, it may cause the stack to split.

Command context

vsf-member-<ID>

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

VSF Link number

VSF Commands | 38

| switch(vsf-member-1)# |     |           |     | link 1     |       |     |
| --------------------- | --- | --------- | --- | ---------- | ----- | --- |
| IFRANGE               |     | Interface |     | identifier | range |     |
<cr>
| switch(vsf-member-1)# |     |     |     | link 1 | 1/1/49-1/1/50 |     |
| --------------------- | --- | --- | --- | ------ | ------------- | --- |
<cr>
| switch(vsf-member-1)# |     |     |     | link 2 | 1/1/52 |     |
| --------------------- | --- | --- | --- | ------ | ------ | --- |
<cr>
| switch(vsf-member-1)# |     |     |     | link 1 | 1/1/51 |     |
| --------------------- | --- | --- | --- | ------ | ------ | --- |
<cr>
| switch(vsf-member-1)# |                |     |     | show running-config |     |     |
| --------------------- | -------------- | --- | --- | ------------------- | --- | --- |
| Current               | configuration: |     |     |                     |     |     |
!
| !Version | ArubaOS-CX |     | SL.10.02.0020-741-g11104d6~dirty |     |     |     |
| -------- | ---------- | --- | -------------------------------- | --- | --- | --- |
!
!
!
!
| ssh maximum-auth-attempts |     |     |     | 6   |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- |
!
!
!
!
!
vlan 1
| interface | 1/1/49 |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- |
no shutdown
| interface | 1/1/50 |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- |
no shutdown
| interface | 1/1/51 |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- |
no shutdown
| interface | 1/1/52 |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- |
no shutdown
| vsf member | 1               |     |     |     |     |     |
| ---------- | --------------- | --- | --- | --- | --- | --- |
| type       | jl661a          |     |     |     |     |     |
| link       | 1 1/1/49-1/1/51 |     |     |     |     |     |
| link       | 2 1/1/52        |     |     |     |     |     |
exit
| switch(vsf-member-1)# |     |      |            | no link | 1 1/1/47        |     |
| --------------------- | --- | ---- | ---------- | ------- | --------------- | --- |
| Port 1/1/47           |     | does | not belong | to      | link 1.         |     |
| switch(vsf-member-1)# |     |      |            | no link | 1 1/1/48-1/1/49 |     |
| Port 1/1/48           |     | does | not belong | to      | link 1.         |     |
| switch(vsf-member-1)# |     |      |            | no link | 2 1/1/49-1/1/51 |     |
| Port 1/1/50           |     | does | not belong | to      | link 2.         |     |
| switch(vsf-member-1)# |     |      |            | no link | 1               |     |
<cr>
| switch(vsf-member-1)# |                |             |           | no link             | 1                      |       |
| --------------------- | -------------- | ----------- | --------- | ------------------- | ---------------------- | ----- |
| This will             | cause          | the         | stack     | to                  | split.                 |       |
| Do you                | want           | to continue |           | (y/n)?              | y                      |       |
| switch(vsf-member-1)# |                |             |           | no link             | 2                      |       |
| This will             | cause          | the         | stack     | to                  | split and the residual | stack |
| fragment              | will           | become      | unusable. |                     |                        |       |
| Do you                | want           | to continue |           | (y/n)?              | y                      |       |
| switch(vsf-member-1)# |                |             |           | show running-config |                        |       |
| Current               | configuration: |             |           |                     |                        |       |
!
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 39

!Version ArubaOS-CX SL.10.02.0020-741-g11104d6~dirty
!
!
!
!
ssh maximum-auth-attempts 6
!
!
!
!
!
vlan 1
interface 1/1/52

no shutdown

vsf member 1

type jl661a

exit

Before removing an individual interface from the VSF link using the no vsf link <x> <interface>
command, ensure that the interface is admin shutdown at both local and peer ends.

vsf force-auto-join

Syntax

vsf force-auto-join

Description

Forces the switch with non-factory default configuration to join a stack. The switch should not have any
existing VSF configurations for force auto-join to work. If VSF configurations are made after force auto-join
is enabled, the switch will no longer be eligible for auto-join.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Forcing a switch with non-factory default configuration to join a stack:

switch(config)# vsf force-auto-join

vsf start-auto-stacking

Syntax

vsf start-auto-stacking

Description

Configures the secondary member and VSF links automatically. To use this command, the switch must be in
the factory default configuration.

VSF Commands | 40

Thiscommandisapplicableonlyontheprimaryswitch.Theprimaryswitchmustbeinfactorydefaultcondition
andmustnothaveanyVSFconfiguration.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringaVSFsecondarymemberandVSFlinkonmaster:
| switch(config)# | vsf              | start-auto-stacking |           |           |     |
| --------------- | ---------------- | ------------------- | --------- | --------- | --- |
| This will       | configure        | links and           | secondary | on master |     |
| Do you          | want to continue | (y/n)?              | y         |           |     |
Runningtheconfigurationonnon-factorydefaultswitch:
| switch(config)# | vsf               | start-auto-stacking |         |         |                |
| --------------- | ----------------- | ------------------- | ------- | ------- | -------------- |
| The switch      | is having         | non-factory         | default | running | configuration. |
| Command         | is not applicable |                     |         |         |                |
Runningtheconfigurationonnon-primaryswitch:
| switch(config)# | vsf           | start-auto-stacking |            |        |     |
| --------------- | ------------- | ------------------- | ---------- | ------ | --- |
| The command     | is applicable | only                | on Primary | switch |     |
vsf split-detect
Syntax
| vsf split-detect | <MGMT-INTERFACE> |     |     |     |     |
| ---------------- | ---------------- | --- | --- | --- | --- |
Description
ConfigurestheVSFsplitdetectionmethodthatspecifiesthemechanismusedforstackfragmentdiscovery
whenthereisastacksplit.
Oncethestackfragmentsarediscovered,thefragmenthavingtheprimarymemberalwayswins.Allnon-VSF
interfacesonthelosingstackfragmentwillbebroughtdowntominimizenetworkdisruptiondueto
duplicateMAC/IP.
Commandcontext
config
Parameters
<MGMT-INTERFACE>
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 41

Configures mgmt-interface as the split detection method. Connect the management interfaces of the
primary and secondary members to the same L2 network. Optionally, the management interfaces of
primary and secondary can be directly connected to each other.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring mgmt-interface as the split detection method:

switch(config)# vsf split-detect mgmt

Removing split detection from the stack:

switch(config)# no vsf split-detect

vsf secondary-member

Syntax

vsf secondary-member <MEMBER-ID>

Description

Configures a secondary member from the available members. The secondary member will normally operate
as the Standby member of the stack.

Member 1 cannot be configured as the secondary member.

Command context

config

Parameters

<MEMBER-ID>

Secondary member number. Required.

n Range for 6200F devices: 2-8.

n Range for 6300 devices: 2-10.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring and un-configuring a secondary member:

switch(config)# vsf secondary-member 3
This will save the configuration and reboot the specified switch.
Do you want to continue (y/n)? y

VSF Commands | 42

switch(config)#
|               |         | no vsf   | secondary-member |           |
| ------------- | ------- | -------- | ---------------- | --------- |
| The secondary |         | member   | will go for      | a reboot. |
| Do you        | want to | continue | (y/n)? y         |           |
Configuringasecondarymemberwhensecondarymemberisalreadyconfigured:
| switch(config)# |     | vsf secondary-member |     | 3   |
| --------------- | --- | -------------------- | --- | --- |
This will save the configuration and reboot the specified switch.
| Do you | want to   | continue | (y/n)? y         |     |
| ------ | --------- | -------- | ---------------- | --- |
| switch | (config)# | vsf      | secondary-member | 4   |
A secondary member is already configured. Existing secondary member
will be unconfigured and rebooted to join the stack as a member. The
specified switch is then rebooted and will join the stack as the new
standby.
| Do you | want to | continue | (y/n)? y |     |
| ------ | ------- | -------- | -------- | --- |
Configuringasecondarymemberwhenoneormoremembersarebooting:
| switch(config)# |     | vsf secondary-member |     | 3   |
| --------------- | --- | -------------------- | --- | --- |
One or more members are currently booting. Allowing this configuration
| may cause | stack   | to split | leading | to traffic disruption. |
| --------- | ------- | -------- | ------- | ---------------------- |
| Do you    | want to | continue | (y/n)?  |                        |
y
This will save the configuration and reboot the specified switch.
| Do you            | want to | continue | (y/n)? y         |     |
| ----------------- | ------- | -------- | ---------------- | --- |
| switch(config)#no |         | vsf      | secondary-member |     |
One or more members are currently booting. Allowing this configuration
| may cause     | stack   | to split | leading     | to traffic disruption. |
| ------------- | ------- | -------- | ----------- | ---------------------- |
| Do you        | want to | continue | (y/n)? y    |                        |
| The secondary |         | member   | will go for | a reboot.              |
| Do you        | want to | continue | (y/n)? y    |                        |
vsf renumber-to
Syntax
| vsf renumber-to |     | <MEMBER-ID> |     |     |
| --------------- | --- | ----------- | --- | --- |
Description
RenumbersVSFmember1toavaluefrom2through10(for6300devices)and2through8(forthe6200F
device).Changingthemembernumbercausestheswitchtorebootwiththenewmembernumber.Only
member1canberenumbered.
VSFlinksmustbeconfiguredbeforerenumberingaswitch.Renumberingwillbedisallowedifnolinksare
configuredorthereareprovisioned/physicallypresentmembers.
Commandcontext
config
Parameters
<MEMBER-ID>
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 43

Membernumbertowhichthememberwillberenumbered.Required.
Rangefor6200Fdevices:2-8.
n
Rangefor6300devices:2-10.
n
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
RenumberingprimaryVSFmemberfrom1to2:
| switch(config)# |     | vsf | renumber-to | 2   |     |     |     |
| --------------- | --- | --- | ----------- | --- | --- | --- | --- |
Member 1 cannot be renumbered until all other members are removed.
| switch(config)# |           | vsf      | renumber-to       | 2     |       |        |                |
| --------------- | --------- | -------- | ----------------- | ----- | ----- | ------ | -------------- |
| Member          | 1 cannot  | be       | renumbered        | until | a VSF | link   | is configured. |
| switch(config)# |           | vsf      | renumber-to       | 2     |       |        |                |
| This            | will save | the      | VSF configuration |       | and   | reboot | the switch.    |
| Do you          | want to   | continue | (y/n)?            | y     |       |        |                |
| vsf member      |           | reboot   |                   |       |       |        |                |
Syntax
| vsf member | <MEMBER-ID> |     | reboot |     |     |     |     |
| ---------- | ----------- | --- | ------ | --- | --- | --- | --- |
Description
RebootsthespecifiedVSFmember.Uponreboot,ifthemasterisreachable,thememberwillrejointhe
stack.
Commandcontext
Manager(#)
Parameters
<MEMBER-ID>
Membernumbertoberebooted.Required.
Rangefor6200Fdevices:1-8.
n
n Rangefor6300devices:1-10.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Rebootingtheprimaryswitchofthestack:
| switch#   | vsf member |        | 1 reboot  |        |       |         |           |
| --------- | ---------- | ------ | --------- | ------ | ----- | ------- | --------- |
| Rebooting | the        | master | switch    | of the | stack | without | a standby |
| will      | make the   | stack  | unusable. |        |       |         |           |
VSFCommands|44

| Do you  | want to    | continue | (y/n)? | y   |
| ------- | ---------- | -------- | ------ | --- |
| switch# | vsf member | 1        | reboot |     |
The master switch will reboot and the standby will become the master.
| Do you    | want to    | continue | (y/n)?    | y       |
| --------- | ---------- | -------- | --------- | ------- |
| switch#   | vsf member | 2        | reboot    |         |
| This will | reboot     | the      | specified | switch. |
| Do you    | want to    | continue | (y/n)?    | y       |
interface
Syntax
interface <IFRANGE>
Description
EntersconfigurationcontextforoneormoreVSFlinkinterfaces.
Commandcontext
config
Parameters
<IFRANGE>
PORTidentifierrange.Required.
VSFlinkinterfacescannotbeincludedinarangewithotherinterfaces.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enteringconfigurationcontext:
| switch(config)# |     | interface | 1/1/1 |     |
| --------------- | --- | --------- | ----- | --- |
shutdown
Syntax
shutdown
Description
ShutsdownoneormoreVSFlinkinterfaces.
Commandcontext
config-if-vsf
Authority
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 45

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShuttingdownaVSFlinkinterface:
| switch(config)#                      | interface | 1/1/1-1/1/2 |          |
| ------------------------------------ | --------- | ----------- | -------- |
| switch(config-if-vsf-<1/1/1-1/1/2>)# |           |             | shutdown |
ShutdownconfigurationforVSFinterfacesisnotpersistentacrossreboots.
show vsf
Syntax
show vsf
Description
DisplaysthelistofprovisionedVSFstackmembers.
Commandcontext
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingthelistofprovisionedVSFstackmembers:
| switch# show         | vsf    |                     |          |
| -------------------- | ------ | ------------------- | -------- |
| Force Autojoin       |        | : Disabled          |          |
| Autojoin Eligibility |        | Status: Not         | Eligible |
| MAC Address          |        | : 08:97:34:b0:0e:00 |          |
| Secondary            |        | : 2                 |          |
| Topology             |        | : Chain             |          |
| Status               |        | : Active            | Fragment |
| Split Detection      | Method | : mgmt              |          |
| Mbr MAC Address      |        | Type                | Status   |
ID
| --- ------------------- |     | -------------- | ----------------- |
| ----------------------- | --- | -------------- | ----------------- |
| 1 08:97:34:b0:0e:00     |     | JL666A         | Master            |
| 2 08:97:34:b1:43:00     |     | JL665A         | In Other Fragment |
| 3 08:97:34:b7:cc:00     |     | JL663A         | Member            |
| 4                       |     | JL662A         | Not Present       |
| show vsf detail         |     |                |                   |
Syntax
VSFCommands|46

show vsf detail
Description
DisplaysdetailedinformationrelatedtothecurrentstateoftheVSFstackandthestackmembers.
Commandcontext
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# show vsf | detail |     |     |     |     |
| ---------------- | ------ | --- | --- | --- | --- |
VSF Stack
| MAC Address            |         | : ec:eb:b8:d0:80:40  |             |           |        |
| ---------------------- | ------- | -------------------- | ----------- | --------- | ------ |
| Secondary              |         | : 2                  |             |           |        |
| Topology               |         | : Chain              |             |           |        |
| Status                 |         | : No Split           |             |           |        |
| Uptime                 |         | : 0d 0h 23m          |             |           |        |
| Split Detection        | Method  | : None               |             |           |        |
| Software Version       |         | : SL.10.02.0000-7755 |             |           |        |
| Force Autojoin         |         | : Disabled           |             |           |        |
| Autojoin Eligibility   | Status  | : Not Eligible       |             |           |        |
| Autojoin Ineligibility | Reason: | Configuration        | changes     | detected  |        |
| Name                   |         | : Aruba-VSF-6300F    |             |           |        |
| Contact                |         | :                    |             |           |        |
| Location               |         | :                    |             |           |        |
| Member ID              |         | : 1                  |             |           |        |
| MAC Address            |         | : ec:eb:b8:d0:80:40  |             |           |        |
| Type                   |         | : JL666A             |             |           |        |
| Model                  |         | : Aruba 6300F        | 24G PoE CLS | 4 /4SFP56 | Switch |
| Status                 |         | : Master             |             |           |        |
| ROM Version            |         | : SL.10.02.0000-7755 |             |           |        |
| Serial Number          |         | : CN7ZK90012         |             |           |        |
| Uptime                 |         | : 0d 0h 23m          |             |           |        |
| CPU Utilization        |         | : 0%                 |             |           |        |
| Memory Utilization     |         | : 20%                |             |           |        |
| VSF link 1             |         | : Up, connected      | to peer     | member 2, | link 1 |
| VSF link 2             |         | : Down               |             |           |        |
| Member ID              |         | : 2                  |             |           |        |
| MAC Address            |         | : eb:ec:d8:e0:50:60  |             |           |        |
| Type                   |         | : JL666A             |             |           |        |
| Model                  |         | : Aruba 6300F        | 24G PoE CLS | 4 /4SFP56 | Switch |
| Status                 |         | : Standby            |             |           |        |
| ROM Version            |         | : SL.10.02.0000-7755 |             |           |        |
| Serial Number          |         | : CN7ZK90012         |             |           |        |
| Uptime                 |         | : 0d 0h 23m          |             |           |        |
| CPU Utilization        |         | : 0%                 |             |           |        |
| Memory Utilization     |         | : 15%                |             |           |        |
| VSF link 1             |         | : Up, connected      | to peer     | member 1, | link 1 |
| VSF link 2             |         | : Down               |             |           |        |
| Member ID              |         | : 3                  |             |           |        |
| MAC Address            |         | :                    |             |           |        |
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 47

| Type               |     | : JL666A      |             |           |        |
| ------------------ | --- | ------------- | ----------- | --------- | ------ |
| Model              |     | : Aruba 6300F | 24G PoE CLS | 4 /4SFP56 | Switch |
| Status             |     | : Not Present |             |           |        |
| ROM Version        |     | :             |             |           |        |
| Serial Number      |     | :             |             |           |        |
| Uptime             |     | :             |             |           |        |
| CPU Utilization    |     | :             |             |           |        |
| Memory Utilization |     | :             |             |           |        |
| VSF link 1         |     | :             |             |           |        |
| VSF link 2         |     | :             |             |           |        |
| show vsf link      |     |               |             |           |        |
Syntax
show vsf link
Description
DisplaystheVSFlinkstateforeachmember.
Commandcontext
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# show    | vsf link       |                             |     |     |     |
| --------------- | -------------- | --------------------------- | --- | --- | --- |
| VSF Member 1    |                |                             |     |     |     |
| Link            | Peer Peer      |                             |     |     |     |
| Link State      | Member Link    | Interfaces                  |     |     |     |
| ---- ---------- | ------- ------ | --------------------------- |     |     |     |
| 1 up            | 2 1            | 1/1/50                      |     |     |     |
| 2 up            | 10 2           | 1/1/49                      |     |     |     |
| VSF Member 2    |                |                             |     |     |     |
| Link            | Peer Peer      |                             |     |     |     |
| Link State      | Member Link    | Interfaces                  |     |     |     |
| ---- ---------- | ------- ------ | --------------------------- |     |     |     |
| 1 up            | 1 1            | 2/1/49                      |     |     |     |
| 2 up            | 3 1            | 2/1/50                      |     |     |     |
| VSF Member 3    |                |                             |     |     |     |
| Link            | Peer Peer      |                             |     |     |     |
| Link State      | Member Link    | Interfaces                  |     |     |     |
| ---- ---------- | ------- ------ | --------------------------- |     |     |     |
| 1 up            | 2 2            | 3/1/25                      |     |     |     |
| 2 up            | 4 1            | 3/1/26                      |     |     |     |
| VSF Member 4    |                |                             |     |     |     |
VSFCommands|48

| Link            | Peer Peer      |                             |     |     |     |
| --------------- | -------------- | --------------------------- | --- | --- | --- |
| Link State      | Member Link    | Interfaces                  |     |     |     |
| ---- ---------- | ------- ------ | --------------------------- |     |     |     |
| 1 up            | 3 2            | 4/1/25                      |     |     |     |
| 2 up            | 5 1            | 4/1/26                      |     |     |     |
| show vsf link   | detail         |                             |     |     |     |
Syntax
| show vsf link detail |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- |
Description
Showsdetailedinformationoftheinterfacesconfiguredonlinksofallstackmembers.
Commandcontext
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# show  | vsf link detail |             |                |             |          |
| ------------- | --------------- | ----------- | -------------- | ----------- | -------- |
| VSF Member: 1 | Link 1          |             |                |             |          |
| Port State    |                 | Status Code | Peer Interface | Peer System | MAC Peer |
Product Type
------- -------------------- ----------- -------------- ------------------ ----
-------------
| 1/1/27 up |     | S   | 2/1/27 | 38:21:c7:5c:e4:c0 |     |
| --------- | --- | --- | ------ | ----------------- | --- |
JL668A
| 1/1/28 error |     | M   | 1/1/27 | 38:21:c7:5c:d7:40 |     |
| ------------ | --- | --- | ------ | ----------------- | --- |
JL668A
| VSF Member: 2 | Link 1 |             |                |             |          |
| ------------- | ------ | ----------- | -------------- | ----------- | -------- |
| Port State    |        | Status Code | Peer Interface | Peer System | MAC Peer |
Product Type
------- -------------------- ----------- -------------- ------------------ ----
-------------
| 2/1/27 up |     | S   | 1/1/27 | 38:21:c7:5c:99:80 |     |
| --------- | --- | --- | ------ | ----------------- | --- |
JL668A
| 2/1/28 error  |        | T           |                |             |          |
| ------------- | ------ | ----------- | -------------- | ----------- | -------- |
| VSF Member: 2 | Link 2 |             |                |             |          |
| Port State    |        | Status Code | Peer Interface | Peer System | MAC Peer |
Product Type
------- -------------------- ----------- -------------- ------------------ ----
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 49

-------------
| 2/1/25 | up  |     |     | S   | 3/1/26 |     | 38:21:c7:5c:f0:00 |     |
| ------ | --- | --- | --- | --- | ------ | --- | ----------------- | --- |
JL668A
| 2/1/26      | down   |     |     | D      |           |           |             |          |
| ----------- | ------ | --- | --- | ------ | --------- | --------- | ----------- | -------- |
| VSF Member: | 3 Link | 1   |     |        |           |           |             |          |
| Port        | State  |     |     | Status | Code Peer | Interface | Peer System | MAC Peer |
| Product     | Type   |     |     |        |           |           |             |          |
------- -------------------- ----------- -------------- ------------------ ----
-------------
| 3/1/27 | error |     |     | L   | 3/1/28 |     | 38:21:c7:5c:f0:00 |     |
| ------ | ----- | --- | --- | --- | ------ | --- | ----------------- | --- |
JL668A
| 3/1/28 | error |     |     | L   | 3/1/27 |     | 38:21:c7:5c:f0:00 |     |
| ------ | ----- | --- | --- | --- | ------ | --- | ----------------- | --- |
JL668A
| VSF Member: | 3 Link | 2   |     |        |           |           |             |          |
| ----------- | ------ | --- | --- | ------ | --------- | --------- | ----------- | -------- |
| Port        | State  |     |     | Status | Code Peer | Interface | Peer System | MAC Peer |
| Product     | Type   |     |     |        |           |           |             |          |
------- -------------------- ----------- -------------- ------------------ ----
-------------
| 3/1/25 | down |     |     | D   |        |     |                   |     |
| ------ | ---- | --- | --- | --- | ------ | --- | ----------------- | --- |
| 3/1/26 | up   |     |     | S   | 2/1/25 |     | 38:21:c7:5c:e4:c0 |     |
JL668A
Flag abbreviation:
| S - Success |     | D - | Interface | physically | down | T   | - Peer timed | out |
| ----------- | --- | --- | --------- | ---------- | ---- | --- | ------------ | --- |
L - Loop detected on the interface AP - Peer autojoin in progress
P - Peer with incompatible product type ANE - Peer is not autojoin
eligible
SV - Peer with incompatible software version AF - Peer autojoin validations
failed
| M - Peer   | with       | inconsistent |             | system MAC    | address         |           |          |     |
| ---------- | ---------- | ------------ | ----------- | ------------- | --------------- | --------- | -------- | --- |
| ILC - Peer | with       | inconsistent |             | VSF link      | configuration   |           |          |     |
| AMI - Peer | with       | multiple     | VSF         | interfaces    | attempting      | to        | autojoin |     |
| ACM - Peer | attempting |              | to autojoin | on            | non-provisioned | interface |          |     |
| AND - Peer | with       | non-default  |             | VSF interface | attempting      | to        | autojoin |     |
AID - Peer autojoin failed as it is connected in incorrect direction
AFN - Peer autojoin failed as there is no free member number available
| show vsf | link | error-detail |     |     |     |     |     |     |
| -------- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
Syntax
| show vsf link | error-detail |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Description
Showsdetailederrorinformationoftheinterfacesconfiguredonlinksofallstackmembers.Also,the
correctiveactionisalsorecommendedtorecoverfromtheerror.
Commandcontext
Manager(#)
Authority
VSFCommands|50

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Showingerrorinformationoftheinterfacesabouttheloopdetection:
| switch#     | show vsf link | error-detail |             |          |                   |     |     |
| ----------- | ------------- | ------------ | ----------- | -------- | ----------------- | --- | --- |
| VSF Member: | 2 Link        | 1            |             |          |                   |     |     |
| Port        |               |              | : 2/1/27    |          |                   |     |     |
| Status      | Code          |              | : L - `Loop | detected | on the interface` |     |     |
Error Description : There is a loop detected between interfaces 2/1/27 and
2/1/28
|     |     |     | of member | 2 indicating | wrong cabling. |     |     |
| --- | --- | --- | --------- | ------------ | -------------- | --- | --- |
Suggested Corrective Action : VSF interfaces 2/1/27 and 2/1/28 are connected back to
| back -      |        |     |             |                  |                   |     |     |
| ----------- | ------ | --- | ----------- | ---------------- | ----------------- | --- | --- |
|             |        |     | please      | fix the cabling. |                   |     |     |
| VSF Member: | 2 Link | 1   |             |                  |                   |     |     |
| Port        |        |     | : 2/1/28    |                  |                   |     |     |
| Status      | code   |     | : L - `Loop | detected         | on the interface` |     |     |
Error Description : There is a loop detected between interfaces 2/1/28 and
2/1/27
|     |     |     | of member | 2 indicating | wrong cabling. |     |     |
| --- | --- | --- | --------- | ------------ | -------------- | --- | --- |
Suggested Corrective Action : VSF interfaces 2/1/28 and 2/1/27 are connected back to
| back -      |         |     |           |                  |     |     |     |
| ----------- | ------- | --- | --------- | ---------------- | --- | --- | --- |
|             |         |     | please    | fix the cabling. |     |     |     |
| VSF Member: | 10 Link | 1   |           |                  |     |     |     |
| Port        |         |     | : 10/1/26 |                  |     |     |     |
Status Code : AFN - `Peer autojoin failed as there is no free
| member | number available` |     |     |     |     |     |     |
| ------ | ----------------- | --- | --- | --- | --- | --- | --- |
Error Description : Maximum stack size has been reached or there are no
free
|     |     |     | provisioned | member       | entries available | matching the | peer |
| --- | --- | --- | ----------- | ------------ | ----------------- | ------------ | ---- |
|     |     |     | switch      | with product | type JL667A.      |              |      |
Suggested Corrective Action : Remove a member using “no vsf member x” CLI and then
|     |     |     | physically | disconnect | and reconnect | the new switch |     |
| --- | --- | --- | ---------- | ---------- | ------------- | -------------- | --- |
with
|          |                   |     | product | type JL667A | for adding | it into the stack. |     |
| -------- | ----------------- | --- | ------- | ----------- | ---------- | ------------------ | --- |
| show vsf | link error-detail |     |         | member      |            |                    |     |
Syntax
| show vsf link | error-detail | member | <MEMBER-ID> |     |     |     |     |
| ------------- | ------------ | ------ | ----------- | --- | --- | --- | --- |
Description
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 51

Showserrorinformationandthesuggestiveactiontoresolvetheerroroftheinterfacesconfiguredonlinks
ofaparticularstackmember.
Commandcontext
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
Showingerrorinformationandthesuggestiveactionformember1:
| switch# show | vsf link error-detail | member   | 1   |     |     |     |     |
| ------------ | --------------------- | -------- | --- | --- | --- | --- | --- |
| VVSF Member: | 1 Link 1              |          |     |     |     |     |     |
| Port         |                       | : 1/1/52 |     |     |     |     |     |
Status Code : M - `Peer with inconsistent system MAC address`
Error Description : All interfaces within a single VSF link must terminate
into
|     |     | the same | peer | switch. | Interface | 1/1/52 | of member 1 |
| --- | --- | -------- | ---- | ------- | --------- | ------ | ----------- |
link 1 is
|     |     | connected | to a | wrong | peer with | MAC 38:21:c7:5c:26:40. |     |
| --- | --- | --------- | ---- | ----- | --------- | ---------------------- | --- |
Suggested Corrective Action : Multiple VSF neighbors detected on this VSF link 1.
Interface
|     |     | 1/1/52 | is connected | to  | device | MAC 38:21:c7:5c:26:40. |     |
| --- | --- | ------ | ------------ | --- | ------ | ---------------------- | --- |
Please make
|           |         | sure the | VSF interfaces |     | of  | link 1 terminate | on the |
| --------- | ------- | -------- | -------------- | --- | --- | ---------------- | ------ |
| same peer | device. |          |                |     |     |                  |        |
Showingerrorinformationandthesuggestiveactionformember4:
| switch# show | vsf link error-detail | member   | 4   |     |     |     |     |
| ------------ | --------------------- | -------- | --- | --- | --- | --- | --- |
| VSF Member:  | 4 Link 1              |          |     |     |     |     |     |
| Port         |                       | : 4/1/27 |     |     |     |     |     |
Status Code : AND - `Peer with non-default VSF interface attempting
to autojoin`
Error Description : Switch with MAC 38:21:c7:5c:a0:c0 is connected on port
1/1/27 which
|     |     | is a non | default | autojoin | VSF | interface. |     |
| --- | --- | -------- | ------- | -------- | --- | ---------- | --- |
Suggested Corrective Action : Auto-join failed on device with MAC 38:21:c7:5c:a0:c0.
VSFCommands|52

Please connect
|           |         | this       | device via interfaces | 25 or 26 | - those are | the |
| --------- | ------- | ---------- | --------------------- | -------- | ----------- | --- |
| auto-join | capable |            |                       |          |             |     |
|           |         | interfaces | on this device.       |          |             |     |
| show vsf  | member  |            |                       |          |             |     |
Syntax
| show vsf member | <MEMBER-ID> |     |     |     |     |     |
| --------------- | ----------- | --- | --- | --- | --- | --- |
Description
DisplaysinformationaboutthespecifiedVSFmember.
Commandcontext
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
| switch# show    | vsf member  | 1                    |                          |        |     |     |
| --------------- | ----------- | -------------------- | ------------------------ | ------ | --- | --- |
| Member ID       |             | : 1                  |                          |        |     |     |
| MAC Address     |             | : ec:eb:b8:d0:80:40  |                          |        |     |     |
| Type            |             | : JL557A             |                          |        |     |     |
| Model           |             | : Aruba JL557A       | 2930F-48G-740W-PoE+-4SFP | Switch |     |     |
| Status          |             | : Master             |                          |        |     |     |
| ROM Version     |             | : SL.10.02.0000-7755 |                          |        |     |     |
| Serial          | Number      | : CN7ZK90012         |                          |        |     |     |
| Uptime          |             | : 0d 0h 18m          |                          |        |     |     |
| CPU Utilization |             | : 0%                 |                          |        |     |     |
| Memory          | Utilization | : 15%                |                          |        |     |     |
| VSF link        | 1           | : Down               |                          |        |     |     |
| VSF link        | 2           | : Down               |                          |        |     |     |
| show vsf        | topology    |                      |                          |        |     |     |
Syntax
show vsf topology
Description
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 53

DisplaysinformationaboutVSFstackmemberconnections.
Commandcontext
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
switch#
show vsf topology
|            | Stby        | Master |
| ---------- | ----------- | ------ |
| +---+      | +---+ +---+ |        |
| | 3 |1==2| | 2 |1==1|    | 1 |    |
| +---+      | +---+ +---+ |        |
VSFCommands|54

Chapter 9
|            |                 |     |     | Frequently | asked | questions |
| ---------- | --------------- | --- | --- | ---------- | ----- | --------- |
| Frequently | asked questions |     |     |            |       |           |
WhatisVSF?
VirtualSwitchingFramework,orVSF,definesasinglevirtualswitchcomprisedofmultipleindividualphysical
switchesthatareinterconnectedthroughstandardEthernetlinks.TheselinksarereferredtoasVSFlinks.
Thesephysicalswitcheswillfunctionasonedevicewithaunifiedcontrolandmanagementplane.
MultiportVSFlinksaresupported.
| Whatare | the supportedplatformsfor |     | VSF? |     |     |     |
| ------- | ------------------------- | --- | ---- | --- | --- | --- |
TheAruba6300F/MSwitchSeriessupportsVSF.
VSFcanbeformedwithacombinationofanyoftheAruba6300F/MSwitchSeries(JL658A,JL659A,JL660A,
JL661A,JL662A,JL663A,JL664A,JL665A,JL666A,JL667A,JL668A,JL762A)oracombinationofanyofthe
Aruba6200FSwitchSeries(JL724A,JL725A,JL726A,JL727A,JL728A).
Aruba6200FSwitchSeriesonlysupportsfixedSKUs.
WhatportspeedsdoVSFlinkssupport?
ForAruba6300F/MSwitchSeries:Alluplinkportswith10G,25G,and50GspeedscanbeconfiguredasVSF
links.
ForAruba6200FSwitchSeries:Alluplinkportswith10GspeedcanbeconfiguredasVSFlinks.
ArubarecommendsthatallVSFlinksbeconfiguredtorunatthesamespeed.
| Can VSFbe | disabled? |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- |
UserscannotdisableVSF.AfactorydefaultswitchbootsupasaVSF-enableddevicewithitsMemberIDset
to1.
| Whatisa | primaryswitch | in VSFstack?Isitconfigurable? |     |     |     |     |
| ------- | ------------- | ----------------------------- | --- | --- | --- | --- |
OnlytheswitchwithaMemberIDof1willbetheprimaryswitchinaVSFstack.Thisswitchwillfunctionas
thestackmasterandwilldrivethecontrolandmanagementplaneforthestack.
| Whatisa | secondaryswitch | in a VSFstack?Isitconfigurable? |     |     |     |     |
| ------- | --------------- | ------------------------------- | --- | --- | --- | --- |
Thesecondaryswitchwillfunctionasthestandbyinastack.Inthecaseofauto-stacking,secondarymember
isautomaticallyconfiguredthroughbuttonpressorvsf start-auto-stackingcommand.
Inaddition,anymemberotherthanMember1canbeconfiguredmanuallyasthesecondaryswitchusing
| thevsf | secondary-member | <MEMBER-ID>command. |     |     |     |     |
| ------ | ---------------- | ------------------- | --- | --- | --- | --- |
Arubastronglyrecommendsthatyouconfigureasecondarymember(standby)forstackhigh-availability.
How manysecondarymember switchesare configurable in a VSFstack?
AVSFstackcanbeconfiguredwithonesecondarymemberonly.
Once itisconfigured,isitpossible tochange the secondarymember?
55
| AOS-CX10.07VirtualSwitchingFramework(VSF)Guide| |     | (6200,6300SwitchSeries) |     |     |     |     |
| ----------------------------------------------- | --- | ----------------------- | --- | --- | --- | --- |

Yes, a new secondary member can be configured using the vsf secondary-member <MEMBER-ID> command.
The old standby device will boot first and join the stack with the member role. Then, the newly configured
secondary member will go for boot and join the stack with the standby role.

The secondary member configuration can only be changed when Member 1 is master of the stack.

How are master and standby for a stack determined?

By default, the primary member (Member 1) becomes the master of the stack and the user-configured
secondary member becomes the standby.

The secondary member synchronizes all its states with the master. If the current master (Member 1) fails,
the standby (secondary member) will seamlessly transition to the master role. In this state, if Member 1
comes back up, it will take the standby role.

Only primary and secondary members can take up master and standby roles in a stack.

What is the role of other members in a stack?

All devices other than the master and standby are called members. These devices do not have any network,
control, or management plane functions. Their interfaces are directly controlled and managed by the master
switch.

Is there any restriction in the order of VSF member numbering?

There is no restriction on the order in which VSF members can be numbered. Each member, however, must
have a unique number in the range of 1-10 (for 6300 switches) or 1-8 (for 6200F switches).

What is the supported stack height and topology?

n 6200F platforms can stack up to 8 members with no modular SKU (only fixed SKU).

n 6300 F/M platforms can stack up to 10 members in a chain or ring topology.

Ring is the recommended topology. This topology requires that each member is configured with two VSF
links, interconnecting each member with two other members in the stack.

Can features be configured on a VSF link?

Once an interface becomes part of a VSF link, no standard network layer protocol or feature can run on that
interface because it is part of the VSF stack fabric.

Will configurations in an individual member switch be retained after joining a stack?

Individual member device configurations are not retained after the switch is renumbered and becomes part
of a stack.

How do the consoles of each member in a stack work?

The console of the master switch provides a full CLI that can be used to manage the stack. Consoles of other
stack members, including the standby, have a limited set of CLI commands that are useful for
troubleshooting the device from a stacking functionality standpoint.

How does an image upgrade for a stack work?

To upgrade a stack to a new firmware image, use the copy <TFTP/SFTP> image command to download the
image to the device. The image will be downloaded to the stack master first and then synced with other
members of the stack automatically.

After downloading the firmware, reboot the stack using the boot system <PRIMARY/SECONDARY> command.
This action completes the upgrade process.

Frequently asked questions | 56

Addingorrebootingindividualmembersbeforetheupgradeprocessiscompletecancausetheindividual
membertofailwhilejoiningthestack.
| Istwo-member |     |     | ringsupported? |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Yes.ItissupportedfromAOS-CX10.07onwards.
|     | Showrun       | vsf    |     |     | showvsf           |             |        |         |        | showvsftopology |               |      |
| --- | ------------- | ------ | --- | --- | ----------------- | ----------- | ------ | ------- | ------ | --------------- | ------------- | ---- |
|     | 6300(config)# |        |     |     | 6300(config)#     |             | show   | vsf     |        |                 | 6300(config)# |      |
|     | show          | run    | vsf |     |                   |             |        |         |        |                 | show vsf      | topo |
|     | vsf           |        |     |     | Force Autojoin    |             |        |         | :      |                 | Mstr          |      |
|     | secondary-    |        |     |     | Disabled          |             |        |         |        |                 | Stdby         |      |
|     | member        | 2      |     |     | Autojoin          | Eligibility |        | Status: | Not    |                 | +---+         |      |
|     | vsf           | member | 1   |     | Eligible          |             |        |         |        |                 | +---+         |      |
|     |               | type   |     |     | MAC Address       |             |        |         | :      |                 | | 1 |1==1|    | 2 |  |
|     | jl668a        |        |     |     | 90:20:c2:20:a2:80 |             |        |         |        |                 | +---+         |      |
|     |               | link   | 1   |     | Secondary         |             |        |         | : 2    |                 | +---+         |      |
|     | 1/1/26        |        |     |     | Topology          |             |        |         | : Ring |                 | 2             |      |
|     |               | link   | 2   |     | Status            |             |        |         | : No   |                 | 2             |      |
|     | 1/1/25        |        |     |     | Split             |             |        |         |        |                 | +========+    |      |
|     | vsf           | member | 2   |     | Split Detection   |             | Method |         | : None |                 |               |      |
type
jl668a
|     |        | link | 1   |     | Mbr Mac                 | Address |     |     | type       |     |     |     |
| --- | ------ | ---- | --- | --- | ----------------------- | ------- | --- | --- | ---------- | --- | --- | --- |
|     | 2/1/25 |      |     |     | Status                  |         |     |     |            |     |     |     |
|     |        | link | 2   |     | ID                      |         |     |     |            |     |     |     |
|     | 2/1/26 |      |     |     | --- ------------------- |         |     |     | ---------- |     |     |     |
|     |        |      |     |     | ---- ---------------    |         |     |     |            |     |     |     |
|     |        |      |     |     | 1 90:20:c2:20:a2:80     |         |     |     | JL668A     |     |     |     |
Master
|     |     |     |     |     | 2 38:21:c7:5a:a5:40 |     |     |     | JL668A |     |     |     |
| --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | ------ | --- | --- | --- |
Standby
Can I adda member tothe VSFstackwhen the member isrunningan image with a
| differentversion |     |     | than | the | stack? |     |     |     |     |     |     |     |
| ---------------- | --- | --- | ---- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Whenadevicejoinsastackanditsfirmwareversionisdifferentfromtheversiononthemaster,themaster
willpushitsfirmwarecopytothedevice.Oncethedevicereceivesacopyofthefirmware,itwillrebootand
rejointhestack,nowrunningthesameversionasthemaster.
Thisisnotsupportedifeithermembersorthemasterrunningonfirmwarepriorto10.07version.
| Whathappenswhen |     |     |     | the | VSFmaster | switch |     | goesdown? |     |     |     |     |
| --------------- | --- | --- | --- | --- | --------- | ------ | --- | --------- | --- | --- | --- | --- |
Thestandbyswitch,ifpresent,willtaketheroleofthemaster.Theoldmasterswitchwillbootandjointhe
stackasthestandbyswitch.Thistransitionwillbeseamlesswithlimitednetworkimpact.
Intheabsenceofastandby(nosecondarymemberconfiguration),masterdevicefailurecausesthe
remainingVSFmemberstorebootandcomebackup.Atthispoint,memberswillenterastateinwhichthey
arewaitingforthemastertocomebackup.Duringthistime,frontplaneportsofthememberswillbe
down.
How doI recover a device thathasnotjoineda stackdue tomisconfiguration?
Thevsf renumber-tocommandisusedtotriggeradevicetotakeupitsnewmembernumberandlightup
itsVSFlinks.Thiscommandcausesthedevicetoreboot,comebackupandwaitformessagesfromthe
AOS-CX10.07VirtualSwitchingFramework(VSF)Guide(6200,6300SwitchSeries) 57

stack master. If the VSF link is configured incorrectly or the member number is wrong, the device could be
waiting in this state indefinitely.

To recover a device in this state, execute the following commands:

1. Execute the ctrl+c command on the device console. This action launches the recovery console.

2. Execute the vsf-factory-reset command on the recovery console.

This action resets the device to factory-default.

n The device will come back up as member ID 1 with no VSF link configuration.

n The device can be configured with the correct member number and VSF links.

n The vsf renumber-to command will trigger this configuration to take effect.

The recovery console also has commands that allow the user to copy support files to an external server. This
functionality is useful for troubleshooting stacking-related issues.

How do the management ports of each member in a stack work?

In a stack, only the master management interface is active. The management interface can be assigned an IP
address for device management purposes. When a master device fails, the standby becomes master and
activates its management interface.

How does replacing the master switch in a stack work?

The replacement device must be of the same part number as the switch being replaced. You must also have
a standby switch configured for replacing the master of a stack without losing configuration.

Complete the following steps:

1. Execute the vsf switchover command to trigger the standby switch to take over the master role.

2. Once the stack is up with the new master, remove all physical connections from the old master switch

that is being replaced.

3. Configure VSF interfaces/links on the new device. It is of critical importance to match the interfaces

configured on the switch being replaced.

4. Physically connect the new device to the stack through configured VSF links.

5. The new switch will join the stack and take up the role of standby.

What is the workflow for replacing a standby or member switch?

The replacement device must be of the same part number as the switch being replaced.

Complete the following steps:

1. Configure VSF interfaces/links on the new device. It is of critical importance to match the interfaces

configured on the switch being replaced.

2. Renumber the new device to match the switch being replaced.

3. Physically connect the new device to the stack through configured VSF links.

4. The new switch will join the stack and take up the standby or a member role based on the secondary

configuration for the stack.

What happens if a VSF link fails?

n If the stack topology is a ring, it will degenerate to a chain when a VSF link in the stack fails.

n If the topology is a chain, a VSF link failure will result in a stack being split into two independent stack

fragments.

Frequently asked questions | 58

n When a stack splits and the master and standby of the stack become part of two different fragments, the

standby takes up the master role for its fragment. Network disruption can result because the two
fragments are simultaneously active. Aruba highly recommends enabling VSF split-detection to gracefully
handle split brain scenarios.

n If a stack splits and the master and standby are in the same fragment with the other members on a

different fragment, the members-only fragment will:

o Reboot.

o Come back up.

o Wait for communication from the stack master.

What is VSF split-detect?

When a stack splits, the split-detect feature provides a mechanism for the fragments to discover each other.

Once the two stack fragments are discovered, the fragment that has the primary member becomes the
active fragment and keeps its front plane (non-VSF) interfaces up and running. The other fragment becomes
inactive and all non-VSF interfaces on the inactive fragment are brought down to avoid network disruption.

How do I configure split-detect?

VSF supports split-detection through the management interface.

Connect the management interfaces of the primary and secondary members to the same management
VLAN/network or connect them directly to one another. The CLI command to enable split detection is vsf
split-detect mgmt.

How do I remove the non-VSF configurations in a stack?

Use the erase startup-config command on the VSF stack. This action will remove all non-VSF related
configurations from the startup-config. Then reboot the stack.

Can a VSF member be removed from a stack?

Yes, remove a member from the stack using the no vsf member <MEMBER-ID> command. All configurations
associated with the member will also be removed. The member will boot and come back up with the factory
default configuration.

How do I remove the master switch from the stack?

Aruba does not recommend removing a member that is master of a stack.

If the master switch has to be removed, complete a switchover and wait for:

n the standby to take up the master role, and

n the old master to reboot and join the stack as standby.

Then use a member remove command to remove the device from the stack.

How can I boot the whole VSF stack and individual members using CLI?

The boot system command can be used to boot the whole stack.

To boot an individual member, use the vsf member

<MEMBER-ID> reboot command.

Is modifying the VSF-specific configuration using Checkpoint restore or TFTP/SFTP/USB
download supported?

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide (6200, 6300 Switch Series)

59

This functionality is not supported. Before applying a configuration on a stack through Checkpoint restore
or TFTP/SFTP/USB download, you must ensure that the following configurations match exactly:

n The current stack VSF configurations.

n The VSF configurations that are part of the configuration file that is being restored or downloaded from

the server.

Specifically, the current VSF stack and the Checkpoint/downloaded configuration that will be applied on the
stack must have the same:

n Number of members

n Member part number (J#)

n Member number

n VSF link configurations

n Secondary member configuration

n Split-detect configuration

How can I dismantle a stack?

A VSF stack can be dismantled by using the erase all zeroize command.

This action will cause each member to reboot, come back up with factory defaults, and function as
individual/standalone devices.

How do I collect support files for a stacked device?

The copy support-files all command executed on the master console will collect support and
troubleshooting information from all members that are part of the stack.

If a member is not part of the stack, you must run the same command from the recovery console of the
respective member.

If a stack has split into two fragments, both fragments will have a master. Execute the same command on
the master console of both fragments.

Can VSF configurations be changed when some of the members are booting?

No. It is recommended to change VSF configurations only when the stack is in steady state.

To ensure that there is no stack split , it is recommended to form the VSF stack in the ring topology before
changing the VSF configurations. This might result in reboot of some of the members.

Is there a way to troubleshoot if the members did not join the stack?

Yes. Use the show vsf link error-details command to check if any of the VSF links are down due to
error scenarios. For most of the error scenarios, corrective action is also recommended to resolve the issue.

Frequently asked questions | 60

Frequently asked questions on Auto-
stacking

Chapter 10

Frequently asked questions on Auto-stacking

What is VSF auto-stacking?

VSF auto-stacking feature provides a mechanism to automatically form a stack when the stack members are
physically connected in a desired topology. This reduces the user intervention touch points to form a VSF
stack. You can add a new switch to the existing stack by physically connecting it to a member of the stack. A
member ID is automatically assigned to the new switch and rebooted. After rebooting, the newly added
member joins the stack.

Is it mandatory to connect the new switch in the direction of higher denomination
master port only after configuring the VSF links on the master for auto-stacking?

Yes. Auto-stacking process always starts only in the direction of higher denomination port of the master. If
no switches are connected to the higher denomination port, auto-stacking process will not start.

If a new switch added for stacking is connected in the direction of lower denomination port of the master,
the master will show it as an error. Use the show vsf link error-detail command to see the error and its
recommendation to fix the error.

Can the size of the stack be extended in the direction of lower denomination port of the
master?

No. You can still renumber manually and add the members to the stack. But the newly added member will
not join the stack automatically through auto-stacking.

What are the different methods to designate the master to bring up a stack using auto-
stacking?

There are five different ways to designate the master and bring up the stack using auto-stacking. The
different ways are:

1. Configuring the VSF links manually on the master switch.

2. Executing the vsf start-auto-stacking command using CLI on the master switch.

3. Pressing the Stk LED mode button on the master switch.

4. Downloading full stack configuration using ZTP.

5. Downloading full stack using TFTP, SFTP, NetEdit, or REST.

What happens when the master is designated manually by configuring lower
denomination port as VSF port first?

This can potentially lead to formation of out-of-order stack since auto stacking happens only in the direction
of highest denomination port. If physical connections are already made, the newly added switch might not
join the stack.

What is the eligibility criteria for a switch to be connected to an existing stack through
auto-stacking?

For a switch to connect to an existing stack, it must be in the auto-join eligible state. A switch in its factory
default state is considered to be auto-join eligible.

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide | (6200, 6300 Switch Series)

61

When will a switch becomes auto-join eligible? Is there a way to make a switch auto-
join eligible again to take part in the auto-join process to form the stack?

If a switch moves out of factory default configuration state, then the switch cannot join an existing stack.

In this case, use the vsf force-auto-join command to make a non-factory default switch to auto-join
eligible again. Once the user sets force auto-join in the switch configuration, the switch will be considered as
auto-join eligible and will join the stack even though the switch does not have factory default configuration.

vsf force-auto-join command will only work if the switch does not have any pre-existing VSF
configurations such as secondary or VSF links. If the switch has VSF configurations already, then the
recommendation is to unconfigure and reconfigure vsf force-auto-join once all VSF configurations are
removed from the switch.

Is it mandatory to use only the internally reserved ports to bring up a stack through
auto-stacking ?

No. If you need to form a stack using vsf start-auto-stacking command or by pressing Stk LED mode
button, then it is mandatory to use the internally reserved VSF ports.

Based on the product type of a switch, the following two interfaces are reserved for the auto-stacking
process:

n 24-port switch models: 25 and 26

n 48-port switch models: 49 and 50

However, if the stack is formed by any of the other methods , you must ensure that the physical
interconnections on the stack ports between different members of the topology is matching with the
provisioned configuration on the master.

Can a stack be formed through auto-stacking when the master is running on 10.07
firmware version and the newly added member is running on firmware version prior to
10.07?

No. It is mandatory to have all the switches running on 10.7 or later releases to form a stack through auto-
stacking .

You cannot form a stack through auto-stacking if either master or the stack members running on different
firmware versions prior to 10.07.

Will a stack be formed if the Stk mode button is pressed on all the members before
physically connecting the cables?

No. Pressing the Stk mode button on all the members will configure VSF links and secondary on the
switches which will make the members not eligible for auto-join. The members will join with the stack only
when it becomes auto-join eligible again.

Pressing Stk LED mode button is to designate the master. So, press Stk LED mode button only on the
switch which is supposed to be the master of the stack. There should be only one master for a VSF stack.

Will a stack be formed if vsf start-auto-stacking is executed on all the members before
connecting the cables physically?

No. Executing the vsf start-auto-stacking command will configure VSF links and secondary on a switch
which will make the switch not eligible for auto-join, The members will join with the stack only when they
become auto-join eligible again.

Executing vsf start-auto-stacking is to designate the master. So, execute the command on the switch
which is supposed to be the master of the stack. There should be only one master for a VSF stack.

What will happen if Stk mode button is pressed on the master of an active stack?

Frequently asked questions on Auto-stacking | 62

Since the VSF configurations are already present , pressing the Stk mode button will not have any effect on
the stack configuration. But the LEDs of the stack will now glow to depict the state of the stack.

For more details on the LED states, Stack and Port LED states

What will happen if the vsf start-auto-stacking command is executed on the master of
an active stack?

Since the VSF configurations are already present , configuring vsf start-auto-stacking will not have any
effect on the stack configuration. An error message also will be displayed to show that the switch does not
have factory default configuration.

After downloading the VSF stack configuration to the master through TFTP/ZTP/NetEdit,
what happens if a new member added has a different SKU than the one provisioned for
that particular member-id through auto-stacking?

If the existing stack size configuration is less than maximum size supported (10 for 6300 switch series, 8 for
6200 switch series) , the newly added member will join the stack with the least member-id available , but not
with the provisioned member id.

If the existing stack size configuration is already the maximum size supported, then the newly added
member will go for a reboot , but will not join the stack. This member will again come up with the factory
default configuration as there is a SKU mismatch.

What happens if the Stk mode button is pressed when the cables are not connected
properly on the reserved interfaces, later connected correctly on the reserved
interfaces?

Members switches go for a reboot and join the stack when the cables are connected on the reserved
interfaces correctly.

Is multi-port VSF configuration supported to bring up a VSF stack through auto-
stacking?

Forming a stack using auto-stacking with multi-ports can be done only when the configuration of all the
members are fully pre-provisioned on Member 1.

By default, Stk mode button press or vsf start-auto-stacking command configures only one port per
VSF link. So even if multiple ports were connected physically, stack will come up with single port per VSF link
only.

Can cables of different speed be connected to the members to form a stack through
auto-stacking?

Yes. Though it is supported , it is always recommended to have the entire stack with cable of same speed for
VSF links.

What happens when non-reserved ports of the newly added switch is connected to the
auto-stacking reserved ports of member 1?

Newly added member will not go for a reboot unless there is a provisioned configuration of the member
matching with non-reserved ports on member 1.

To use Stk mode button or vsf start-auto-stacking command, the cables must be connected to the
reserved interfaces on the new switch to start the auto-stacking process. For more information on reserved
interfaces, see Reserved interfaces for auto-stacking

Can the Stk mode button or vsf start-auto-stacking command be used on a switch which
has some VSF configuration already?

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide (6200, 6300 Switch Series)

63

No. To use Stk mode button or vsf start-auto-stacking command, the switch must be in factory-default
configuration.

Is there a way to download configuration automatically after forming a stack via Stk
mode button press?

Yes. Once the stack is formed , ztp force-provision will be automatically enabled on the stack. But you
must have an uplink connectivity to DHCP Server (which can provide the ZTP options) and TFTP server to
download the firmware and configuration files.

Can I download the full stack configuration via TFTP to the running configuration
directly?

Full stack configuration can be downloaded into the master of the stack. The recommendation is to first
download the configuration to the start-up and then move the startup to the running configuration.
Copying the configuration first to startup will help in detecting errors in the deployed configuration. Once
the configuration is copied to startup without any errors, then the startup configuration can be applied to
the running configuration. This will also ensure that auto-stacking process did not start prematurely. The
stacking process might start prematurely if the configuration is applied directly to the running
configuration.

How to check whether the switch is auto-join eligible or not?

Executing the show vsf or show vsf details command shows an entry called Autojoin Eligibility
Status which shows whether the switch is eligible or not eligible .

Is it possible to change the secondary member of the stack which is formed through vsf
start-auto-stacking or stk mode button press?

Yes. You can execute the vsf secondary-member <member-id> on the master to change the secondary
member. This will reboot the member 2 (default secondary) and make it to join the stack as member. Then
the newly configured secondary member will go for a reboot and joins the stack as standby. Changing the
secondary member can only be done from the primary switch (member 1).

Will the switch stay as auto-join eligible if any new VSF configurations are made after
executing the vsf force-auto-join command?

No. vsf force-auto-join is a command used to make an auto-join ineligible switch to auto-join eligible
again. If the VSF configuration of the switch gets changed again after executing the vsf force-auto-join
command, the switch will become auto-join ineligible again. When the VSF configurations are removed ,
switch will automatically become auto-join eligible.

What happens if a member configuration is removed from the master of a stack using
the no vsf member <id> command?

If the member is part of the stack (not in “Not Present” state) and its ports are connected through reserved
auto-stacking ports, then the removed switch will join back the stack after it comes up as standalone. This is
because the auto-stacking starts on the reserved ports. So, after member removal, make sure you
immediately disconnect the cables physically as well.

Will both auto-stacking and ZTP process start simultaneously if the master is designated
using the configuration download through ZTP,?

No. The auto-stacking process will start only after the completion of ZTP process.

Is there any difference between forming the stack using the vsf start-auto-stacking
command and Stk mode button?

Frequently asked questions on Auto-stacking | 64

There is no difference in forming the stack. But the ztp force-provision configuration will be added in
addition to the VSF related configurations only when the stack is formed using the Stk mode button press.
If the stack has an uplink connectivity to DHCP server, then the configuration and firmware for the stack can
be downloaded from a TFTP server through ZTP.

Does auto-stacking support ring topology without the need for any configuration
changes?

Yes. By default, auto-stacking feature configures two links on each of the VSF members. In case, if there is a
need to change the stack from chain to ring topology, connect the first member with the last member of the
stack with a cable on the auto-stacking reserved ports.

Can I use reserved auto-stacking interfaces as normal data ports?

Yes. The reserved auto-stacking interfaces can be used as normal data ports.

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide (6200, 6300 Switch Series)

65

Support and Other Resources

Chapter 11

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

AOS-CX 10.07 Virtual Switching Framework (VSF) Guide | (6200, 6300 Switch Series)

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