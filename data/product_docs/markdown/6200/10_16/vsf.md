| AOS-CX    |     | 10.16.xxx |     | Virtual |       |
| --------- | --- | --------- | --- | ------- | ----- |
| Switching |     | Framework |     |         | (VSF) |
Guide
| 4100i, | 6100, | 6200, | 6300 | Switch | Series |
| ------ | ----- | ----- | ---- | ------ | ------ |
Published:October2025
Version:1

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

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

3

Contents
| About                               | this document                                   |         | 8   |
| ----------------------------------- | ----------------------------------------------- | ------- | --- |
| Applicableproducts                  |                                                 |         | 8   |
| Latestversionavailableonline        |                                                 |         | 8   |
| Commandsyntaxnotationconventions    |                                                 |         | 8   |
| Abouttheexamples                    |                                                 |         | 9   |
| Identifyingswitchportsandinterfaces |                                                 |         | 10  |
| Protocol                            | and feature                                     | details | 11  |
| Terminology                         |                                                 |         | 11  |
| ConnectionTopology                  |                                                 |         | 12  |
|                                     | Ringtopology                                    |         | 12  |
|                                     | Chaintopology                                   |         | 13  |
| VSFBehavior                         |                                                 |         | 13  |
| OneVirtualDevice                    |                                                 |         | 14  |
| VSFauto-stacking                    |                                                 |         | 17  |
|                                     | Peerdiscovery                                   |         | 17  |
|                                     | Auto-joinEligibility                            |         | 17  |
|                                     | Reservedinterfacesforauto-stacking              |         | 17  |
|                                     | Forceauto-joinsupport                           |         | 19  |
| Interoperation                      |                                                 |         | 20  |
| Linkaggregation                     |                                                 |         | 20  |
| VSF portshaping                     |                                                 |         | 21  |
| SupportedVSFportspeeds              |                                                 |         | 22  |
| VSFSupportonSmartRatePorts          |                                                 |         | 23  |
| Configuration                       | task                                            | list    | 24  |
| Stackdeploymentusingauto-stacking   |                                                 |         | 24  |
|                                     | Designatingconductorswitch                      |         | 24  |
|                                     | Auto-stackingusingLED modebutton                |         | 25  |
|                                     | Auto-stackingusingCLI command                   |         | 26  |
|                                     | Auto-stackingusingzero-touchprovisioning(ZTP)   |         | 27  |
|                                     | Auto-stackingusingHPEArubaNetworkingCXmobileapp |         | 27  |
| Manualconfiguration                 |                                                 |         | 28  |
|                                     | VSFlinks                                        |         | 29  |
|                                     | Secondarymember                                 |         | 29  |
|                                     | Membernumber                                    |         | 29  |
|                                     | Memberprovisioning                              |         | 29  |
|                                     | AccesstoVSFmembers                              |         | 30  |
| Stackmanagement                     |                                                 |         | 30  |
|                                     | Consoles                                        |         | 30  |
|                                     | Managementinterface                             |         | 30  |
|                                     | Splitdetection                                  |         | 30  |
|                                     | Automatedimagesync                              |         | 33  |
|                                     | Reboot                                          |         | 33  |
|                                     | Memberadditionwithauto-stacking                 |         | 33  |
|                                     | Memberadditionwithoutauto-stacking              |         | 33  |
|                                     | Memberreplacementwithauto-stacking              |         | 34  |
|                                     | Memberreplacementwithoutauto-stacking           |         | 34  |
|                                     | Memberremoval                                   |         | 34  |
5
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide| (4100i,6100,6200,6300SwitchSeries)

StackandPortLEDstates 34
| Use cases                                             |     |     | 36  |
| ----------------------------------------------------- | --- | --- | --- |
| Formingafour-memberringsetupusingauto-stackingcommand |     |     | 36  |
Formingafour-memberchainsetupusinglinkconfigurationcommandwithauto-join 38
Forminganeight-memberringsetupmanuallyusinglinkconfigurationwithoutauto-stack-
| ing            |          |         | 39  |
| -------------- | -------- | ------- | --- |
| VSF In-Service | Software | Upgrade | 43  |
Upgradescope 43
| VSFISSUoperation |     |     | 43  |
| ---------------- | --- | --- | --- |
Step1:Imagedownloadandvalidation 43
Step2:Installtheimageinthestandby&members 43
Step3:Freezethesystem 44
Step4:Performtheupgradeforthelinemodules 44
Step5:Recoverthepreviousstate 44
Step6:Failoveroccursbetweentheconductorandthestandby 44
Step7:ThepreviousConductorwillupgradeitsimage 44
| VSFISSUconsiderations |     |     | 44  |
| --------------------- | --- | --- | --- |
| VSFISSUlimitations    |     |     | 45  |
Hardwarefaults 45
Prohibitedoperations 45
Recommendations 45
Scheduledjobs 45
InformationnotupdatedduringISSU 45
Showtech 45
Featuresthatdon'tsupportuninterruptedoperationduringISSU 45
| AAA                               |     |     | 46  |
| --------------------------------- | --- | --- | --- |
| PIMwithMSDP                       |     |     | 46  |
| DynautzISSU                       |     |     | 46  |
| BFDISSU                           |     |     | 46  |
| NAE                               |     |     | 46  |
| Featurereadinesscheck             |     |     | 46  |
| Restrictions                      |     |     | 46  |
| VSFISSUerrorsandrecovery          |     |     | 46  |
| VSF commands                      |     |     | 48  |
| clearvsfsplit-detectionstatistics |     |     | 48  |
| description                       |     |     | 48  |
| interface                         |     |     | 49  |
| issurollback-timer                |     |     | 50  |
| issuupdate-software               |     |     | 51  |
| link                              |     |     | 56  |
| member                            |     |     | 57  |
| showissu                          |     |     | 58  |
| showvsf                           |     |     | 63  |
| showvsfdetail                     |     |     | 66  |
| showvsfmember                     |     |     | 69  |
| showvsflink                       |     |     | 69  |
| showvsflinkdetail                 |     |     | 70  |
| showvsflinkerror-detail           |     |     | 72  |
| showvsflinkerror-detailmember     |     |     | 74  |
| showvsfsplit-detection            |     |     | 76  |
| showvsftopology                   |     |     | 77  |
| shutdown                          |     |     | 78  |
| type                              |     |     | 79  |
|6

| vsfegress-shape                    |                                          |                 |           |                        | 80  |
| ---------------------------------- | ---------------------------------------- | --------------- | --------- | ---------------------- | --- |
| vsfforce-auto-join                 |                                          |                 |           |                        | 82  |
| vsfmember                          |                                          |                 |           |                        | 83  |
| vsfmemberreboot                    |                                          |                 |           |                        | 84  |
| vsfrenumber-to                     |                                          |                 |           |                        | 85  |
| vsfsecondary-member                |                                          |                 |           |                        | 86  |
| vsfsplit-detectmgmt                |                                          |                 |           |                        | 88  |
| vsfsplit-detectvlan                |                                          |                 |           |                        | 89  |
| vsfstart-auto-stacking             |                                          |                 |           |                        | 91  |
| Configuration                      |                                          | conflict        |           | finder recommendations | 93  |
| Considerations                     |                                          | and             | best      | practices              | 96  |
| Debugging                          | and                                      | troubleshooting |           |                        | 98  |
| Stacksplit                         |                                          |                 |           |                        | 98  |
|                                    | Step1: Verifysplithasoccurred            |                 |           |                        | 98  |
|                                    | Step2:Identifyfailedlinkormember         |                 |           |                        | 99  |
|                                    | Step3:Recoverorreplacefailedlinkormember |                 |           |                        | 100 |
|                                    | Step4:Verifyproperstackoperation         |                 |           |                        | 100 |
| Misconfigurationrecovery           |                                          |                 |           |                        | 100 |
| VSF switchoverbehaviors            |                                          |                 |           |                        | 101 |
| Frequently                         | asked                                    |                 | questions |                        | 102 |
| General                            |                                          |                 |           |                        | 102 |
| Auto-stacking                      |                                          |                 |           |                        | 111 |
| Support                            | and                                      | Other           | Resources |                        | 118 |
| AccessingHPEArubaNetworkingSupport |                                          |                 |           |                        | 118 |
| AccessingUpdates                   |                                          |                 |           |                        | 119 |
| WarrantyInformation                |                                          |                 |           |                        | 119 |
| RegulatoryInformation              |                                          |                 |           |                        | 119 |
| DocumentationFeedback              |                                          |                 |           |                        | 119 |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 7

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing HPE Aruba Networking switches on
a network.

Applicable products

This document applies to the following products:

n HPE Aruba Networking 4100i Switch Series (JL817A, JL818A)

n HPE Aruba Networking 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A, R9Y04A)

n HPE Aruba Networking 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A, R8Q68A,
R8Q69A, R8Q70A, R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A, JL724B, JL725B,
JL726B, JL727B, JL728B, S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,  S0M87A,  S0M88A,
S0M89A,  S0M90A, S0G13A, S0G14A, S0G15A, S0G16A, S0G17A, R8V13A)

n HPE Aruba Networking 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A,

JL665A, JL666A, JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A, S0X44A, S3L75A,
S3L76A, S3L77A, S4P41A,S4P42A, S4P43A, S4P44A, S4P45A, S4P46A, S4P47A, S4P49A, S0G03A,
S0G05A, S0F99A, S0G01A, S0G96A, S0G98A, S4P48A, S0G04A, S0G06A, S0G00A, S0G95A, S0G97A,
S0G02A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

example-text

Usage

Identifies commands and their options and operands, code examples,
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

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables
are enclosed in angle brackets (< >). Substitute the text—including
the enclosing angle brackets—with an actual value.

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

8

Convention

Usage

|

{ }

[ ]

… or

...

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

In certain configuration contexts, the prompt may include variable information. For example, when in
the VLAN configuration context, a VLAN number appears in the prompt:
switch(config-vlan-100)#

When referring to this context, this document uses the syntax:
switch(config-vlan-<VLAN-ID>)#

Where <VLAN-ID> is a variable representing the VLAN number.

About this document | 9

Identifying switch ports and interfaces

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format: member/slot/port.

On the HPE Aruba Networking 4100i Switch Series

n member: The member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to
4. The primary switch is always member 1. If the switch is not a member of a VSF stack, then member
is 1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6100 Switch Series

n member: The member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to
6. The primary switch is always member 1. If the switch is not a member of a VSF stack, then member
is 1.

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

On the HPE Aruba Networking 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.
The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

10

Chapter 2

Protocol and feature details

Protocol and feature details

Virtual Switching Framework, or VSF, allows network administrators to stack multiple individual switches
into a single logical device using standard Ethernet links. VSF stacks provide increased network capacity
and improved redundancy, allowing administrators to scale stack size with user and device
requirements while simplifying configuration complexity and providing a single point of management
access with a shared control plane across all stack members.

n 4100i: VSF allows stacks to be formed using any combination of SKUs of the 4100i family. Up to 4

member switches will be allowed. Connections between the switches must use 1G SFP/SFP+ either
with 1G copper or 10G ports. All VSF links in a stack should operate at the same speed.

n 6100: VSF allows stacks to be formed using any combination of SKUs of the 6100 family except 12-
port SKU. A 12-port switch will form a VSF stack only with other 12-port switches. Up to 6 member
switches will be allowed. Connections between the switches must use 1G SFP/SFP+ either with 1G
copper or 10G ports. All VSF links in a stack should operate at the same speed.

n 6200: VSF allows stacks to be formed using any combination of 24 and 48-port SKUs of the 6200

family. (A 6200F 12-port switch will form a VSF stack only with other 6200F 12-port switches.) Up to 8
member switches will be allowed. Connections between the switches must use 1G SFP/SFP+ either
with 1G copper downlink ports, 10G links, or SmartRate ports.

n 6300: VSF allows stacks to be formed using any combination of SKUs of the 6300 family. Up to 10

member switches will be allowed. Connections between the switches must use 10G, 25G, 50G links,
or SmartRate ports. All VSF links in a stack should operate at the same speed.

The VSF stack, containing only the S0E91A and S0X44A SKUs, supports 10G, 25G, and 100G speed
links. If a VSF stack includes a mix of S0E91A/S0X44A SKU and other SKUs, then it supports 10G,and
25G VSF links only.

4100 and 6100 switch series do not support using ports with different speeds for VSF links.

In 6100 and 6200 switch series, 12-port switches cannot form a stack with 24-port or 48-port switches.

In 6300 switch series, S3L75A, S3L76A and S3L77A SKUs can only stack with other S3L75A, S3L76A and S3L77A

SKUs.

VSF is enabled by default on all supported switch models and cannot be disabled. Within the stack, one
switch (normally the primary, member 1) is the Conductor that runs all control plane software and
manages the ASICs of all stack members. Any switch apart from primary can be configured as Standby
switch, which maintains a synchronized copy of the Conductor's configuration database and is capable
of assuming the Conductor role in the event of a failure of, or loss of connectivity to, the Conductor.

Terminology

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

11

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

The primary member is member ID 1; normally operates as the stack Conductor.

Secondary

User-configurable using any valid member ID other than 1; normally operates as the

stack Standby.

Conductor

The Conductor maintains the VSF stack configuration, software images, and control
plane.

Standby

The Standby maintains a synchronized copy of the VSF stack configuration from the

Conductor; automatically assumes the Conductor role if connectivity is lost to the

existing Conductor due to hardware or link failures.

Member

The member switch does not run any networking protocols and has no states. The

interfaces on this switch are directly controlled and programmed by the conductor

switch.

Connection Topology

VSF supports up to 4 member stacks (for 4100i devices), 6 member stacks (for 6100 devices), 8 member
stacks (for 6200F devices) and 10 member stacks (for 6300 devices) in ring and chain topologies.

Ring topology

A two-member ring topology is not supported on 4100 and 6100 series switches. For link-level redundancy in

two-member stacks, it is recommended to bundle multiple interfaces into a single VSF link using a chain

topology.

In a ring topology, each stack member has a VSF link connection to two other members, providing
resiliency against link and member switch hardware failures as any single failure does not isolate

Protocol and feature details | 12

remaining stack members from each other. HPE Aruba Networking strongly recommends deploying
VSF stacks using ring topologies whenever feasible.

Figure 1 Ring topology

Chain topology

In a chain topology, there is only one path between any two stack members. A VSF link or hardware
failure in a chain topology may cause a stack split and result in network disruption; VSF split detection
may be used to mitigate this scenario.

Figure 2 Chain topology

VSF Behavior

Each stack member must have a unique member ID number. Auto-stacking automatically assigns the
lowest available member ID when adding a new member to the stack; if deploying or expanding a stack
manually, ensure that each new member is assigned a valid member ID not already in use by an existing
stack member, as a member ID conflict will result in the new member failing to join the stack.

n During normal stack operation, the primary member will assume the Conductor role and the

secondary member will assume the Standby role during normal operation.

n The primary member is member number 1. This setting is not configurable and 1 is the default. A

factory-default switch boots up as a VSF-enabled switch with a member number of 1.

n The secondary member number is user configurable; when auto-stacking is used via the push-button
or CLI methods, member 2 is automatically assigned as the secondary. It is recommended that the
customer configures a secondary member in the stack, since a stack with a standby offers resiliency
and high availability.

n No members other than primary and secondary members can become Conductor or Standby of the

stack.

In a standard deployment, uplinks should be from primary and secondary. The management interface from

primary and secondary members should be connected to the management network, providing management

connectivity to the current conductor.

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

13

| One Virtual |     | Device |     |     |     |     |
| ----------- | --- | ------ | --- | --- | --- | --- |
OncetheVSFstackisformed,allinterconnectedswitchesoperateasasinglevirtualswitchwithasingle
controlplane.Allinterfacesofallswitchesinthestackareavailableforconfigurationandmanagement.
Figure1 Onevirtualdeviceexampletopology
| switch#     | show        | vsf    |         |                     |          |        |
| ----------- | ----------- | ------ | ------- | ------------------- | -------- | ------ |
| Force       | Autojoin    |        |         | : Disabled          |          |        |
| Autojoin    | Eligibility |        | Status: | Not                 | Eligible |        |
| MAC Address |             |        |         | : 08:97:34:b0:0e:00 |          |        |
| Egress      | Shape       |        |         | : Enabled           |          |        |
| Egress      | Shape       | Rate   |         | : None              |          |        |
| Secondary   |             |        |         | : 2                 |          |        |
| Topology    |             |        |         | : Chain             |          |        |
| Status      |             |        |         | : No                | Split    |        |
| Split       | Detection   | Method |         | : None              |          |        |
| Mbr MAC     | Address     |        |         | Type                |          | Status |
ID
| --- ------------------- |     |     |     | -------------- |     | ----------------- |
| ----------------------- | --- | --- | --- | -------------- | --- | ----------------- |
| 1 38:21:c7:5c:62:40     |     |     |     | JL668A         |     | Conductor         |
| 2 18:7a:3b:1b:68:c0     |     |     |     | R8S90A         |     | Standby           |
| 3 38:21:c7:5c:57:c0     |     |     |     | JL668A         |     | Member            |
| 4 18:7a:3b:1b:66:40     |     |     |     | R8S89A         |     | Member            |
Interfaceswillbenumberedasnotedinthefollowingtable.
| Name   | Member |     | Number |     | Slot | Port |
| ------ | ------ | --- | ------ | --- | ---- | ---- |
| 1/1/1  | 1      |     |        |     | 1    | 1    |
| 2/1/14 | 2      |     |        |     | 1    | 14   |
| 8/1/12 | 8      |     |        |     | 1    | 12   |
Protocolandfeaturedetails|14

ForVSF-capableswitches,theslotnumberisalways1.Allinterfacesexceptforthoseassignedto
VSF linksareavailablefornormalconfiguration.
| switch# | show interfaces | brief |     |     |     |
| ------- | --------------- | ----- | --- | --- | --- |
----------------------------------------------------------------------------------
| Port | Native Mode | Type | Enabled Status | Reason | Speed  |
| ---- | ----------- | ---- | -------------- | ------ | ------ |
|      | VLAN        |      |                |        | (Mb/s) |
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
| !Version          | AOS-CX FL.10.07.xxxx |     |     |     |     |
| ----------------- | -------------------- | --- | --- | --- | --- |
| !export-password: | default              |     |     |     |     |
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
| vsf secondary-member |             | 2   |     |     |     |
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
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 15

vlan access 1

interface 1/1/2
no shutdown
no routing
vlan access 1

interface 1/1/3
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

As shown in this configuration, interfaces of all member switches can be configured from the
Conductor.

Protocol and feature details | 16

Once a stack is deployed, the stack configuration is persistent and stored separate from the startup
configuration. The user can safely remove the startup configuration with the command erase startup-
configuration without disturbing the stacking topology. To remove all configurations, including the
stacking topology, use the command erase all zeroizewhich will automatically reboot and zeroize all
stack members, restoring them to a factory default state.

VSF auto-stacking

VSF auto-stacking feature provides a mechanism to automatically form a stack when the stack members
are physically connected in a desired topology. This reduces the number of user intervention touch
points to form a VSF stack.

A manual stack formation procedure generally requires the user to explicitly log in to each of the switch,
configure the links, renumber it, and then make the physical connection to form a VSF stack of desired
size and topology. This is error prone since there are multiple touch-points involved in the whole work-
flow for each member. The auto-stacking feature eases this problem by reducing the number of touch-
points involved to simple physical connections of the links. A new factory default switch can be added
into an existing stack by physically connecting it to a VSF link port on an existing stack member. The new
switch will automatically be assigned the lowest available member ID and will automatically reboot.
After reboot, the newly added member will join the stack.

There are two major components to the auto-stacking solution:

n Peer discovery—Initiated from the conductor using one of the methods described in Designating

conductor switch.

n Auto-join Eligibility—Determined by the configuration state of each stack member. A switch with a

factory default configuration is auto-join eligible.

Peer discovery

Auto-stacking peer discovery is a uni-directional process. It starts with the VSF link containing the higher-
numbered VSF port, sending a VSF peer discovery protocol packet to a connected peer switch. The peer
receives the packet, determines if it is valid, and sends a response with information including its auto-
join eligibility, MAC address, and part number. If the peer is auto-join eligible, the VSF member and link
configurations are automatically added to the running configuration of the conductor.

Auto-join Eligibility

Auto-join eligibility determines whether a switch will join a VSF stack if connected to a configured
VSF link port on an existing stack member. A switch in its factory defaults configuration state is
considered to be auto-join eligible. If the auto-join eligible switch is connected to existing stack, it will
automatically reboot and join the stack. Once a switch is no longer using a factory default configuration,
it is no longer auto-join eligible and will not automatically join an existing stack. A CLI command is
available to override this behavior; see Force auto-join support for details. However, user can still
manually configure the links, renumber the device to make it part of a stack.

Reserved interfaces for auto-stacking

The following two interfaces are reserved for the auto-stacking process for most switches:

n 12-port switch models: 13 and 14

n 24-port switch models: 25 and 26

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

17

n 40-portswitchmodels:41and42
n 48-portswitchmodels:49and50
Userscanphysicallyconnecttheswitchtoanexistingstackononeofthesereservedauto-stacking
interfaces.
The6300SwitchseriesmodelsR8S89A,R8S90A,R8S91AandR8S92Areservethelastpairofportsforother
features,andreservethefirstpageofportsforstacking@50Gspeeds.
Thefollowingtableshowsthelistofreservedauto-stackinginterfacesbasedontheproducttypeand
platform:
ReservedInterfaces
| Platform | SKU Part Number       | Ports reserved | for Auto-Stacking |
| -------- | --------------------- | -------------- | ----------------- |
| 4100i    | JL817A                | 13,14          |                   |
| 4100i    | JL818A                | 25,26          |                   |
| 6100     | JL679A                | 13,14          |                   |
| 6100     | JL677A,JL678A         | 25,26          |                   |
| 6100     | JL675A,JL676A,R9Y04A  | 49,50          |                   |
| 6200     | R8Q72A,R8V13A         | 13,14          |                   |
| 6200     | JL724B,JL725B,S0M81A, | 25,26          |                   |
S0M82A,S0M86A,S0M87A,
S0G13A,S0G14A,JL724A,
JL725A,R8Q67A,R8Q68A,
R8V08A,R8V09A
| 6200 | JL726A,JL727A,JL728A, | 49,50 |     |
| ---- | --------------------- | ----- | --- |
R8Q69A,R8Q70A,R8Q71A,
R8V10A,R8V11A,R8V12A,
JL726B,JL727B,JL728B,
S0M83A,S0M84A,S0M85A,
S0M88A,S0M89A,S0M90A,
S0G15A,S0G16A,S0G17A
| 6300 | JL658A,JL660A,JL662A,JL664A, | 25,26 |     |
| ---- | ---------------------------- | ----- | --- |
JL666A,JL668A,S0G03A,
S0G05A,S0F99A,S0G01A,
S0G96A,S0G98A,R8S89A,
R8S92A,S4P44A,S4P48A
| 6300 | S4P42A,S4P46A                | 41,42 |     |
| ---- | ---------------------------- | ----- | --- |
| 6300 | JL659A,JL661A,JL663A,JL665A, | 49,50 |     |
JL667A,JL762A,S0G04A,
S0G06A,S0G00A,S0G95A,
S0G97A,S0G02A,R8S90A,
R8S91A,S0E91A,S0X44A,
S4P41A,S4P43A,S4P45A,
S4P47A
Protocolandfeaturedetails|18

| Platform | SKU Part Number | Ports reserved | for Auto-Stacking |
| -------- | --------------- | -------------- | ----------------- |
| 6300L    | S3L75A          | 25,26          |                   |
| 6300L    | S3L76A,S3L77A   | 49,50          |                   |
Force auto-join support
Onlyaswitchwithfactorydefaultconfigurationisconsideredtobeauto-joineligible.Inordertosupport
factoryexpressdeploymentswheretheuserwantstoaddaswitchwhichisinitsnon-factorydefault
configuration,theforceauto-joinconfigurationsupportisprovided.Usethevsf force-auto-join
commandtoforcetheswitchtojointhestackautomatically.Oncetheusersetsforceauto-joininthe
switchconfiguration,theswitchwillbeconsideredasauto-joineligibleandwilljointhestackeven
thoughtheswitchdoesnothavethefactorydefaultconfiguration.
Forceauto-joinwillworkonlyiftheswitchdoesnothaveanypre-existingVSFconfigurations.
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 19

Interoperation
AVSFstacksupportsanycombinationofmodelswithinasupportedswitchfamily:
n 6200Fswitches,or
n 6300switches(6300L,6300M,and6300F).
Stackingisnotsupportedacrossswitchfamilies.Forexample,aVSFstackcanincludeeither4100i,6100,6200or
6300switches,butnotamix.Additionally,6100switchseriesJL679ASKUscanonlystackwithotherJL679ASKUs,
6200switchseriesmodelsR8Q72AandR8V13ASKUscanonlystackwithotherR8Q72AandR8V13ASKUs,and
6300LswitchseriesS3L75A,S3L76AandS3L77ASKUscanonlystackwithotherS3L75A,S3L76AandS3L77A
SKUs.
FirmwareversionspriortoAOS-CX10.07arenotinteroperablewith10.07orlaterversions.
Link aggregation
Linkaggregations(L-Agg)mayspaninterfacesacrossmultiplestackmembers.Loadbalancingis
performedonallinterfacesoftheL-AggacrossthestackandisapplicabletobothL2andL3L-Aggs.
| interface | lag 1 |     |     |
| --------- | ----- | --- | --- |
no shutdown
no routing
| vlan | access 1 |     |     |
| ---- | -------- | --- | --- |
loop-protect
| interface | lag 2 |     |     |
| --------- | ----- | --- | --- |
no shutdown
| bfd       | min-transmit-interval 1000 |     |     |
| --------- | -------------------------- | --- | --- |
| ip        | address 192.168.12.7/24    |     |     |
| interface | 1/1/18                     |     |     |
no shutdown
| lag       | 1      |     |     |
| --------- | ------ | --- | --- |
| interface | 2/1/18 |     |     |
no shutdown
| lag       | 1      |     |     |
| --------- | ------ | --- | --- |
| interface | 1/1/23 |     |     |
no shutdown
| lag       | 2      |     |     |
| --------- | ------ | --- | --- |
| interface | 2/1/23 |     |     |
no shutdown
| lag     | 2                    |     |     |
| ------- | -------------------- | --- | --- |
| switch# | show lacp interfaces |     |     |
State abbreviations :
| A - Active        | P - Passive      | F - Aggregable | I - Individual |
| ----------------- | ---------------- | -------------- | -------------- |
| S - Short-timeout | L - Long-timeout | N - InSync     | O - OutofSync  |
C - Collecting D - Distributing
| X - State     | m/c expired        | E - Default | neighbor state |
| ------------- | ------------------ | ----------- | -------------- |
| Actor details | of all interfaces: |             |                |
Protocolandfeaturedetails|20

------------------------------------------------------------------------------
| Intf Aggr | Port Port | State System-ID | System Aggr | Forwarding |
| --------- | --------- | --------------- | ----------- | ---------- |
| Name      | Id Pri    |                 | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/18 lag1     |                    |     |     | up  |
| --------------- | ------------------ | --- | --- | --- |
| 2/1/18 lag1     |                    |     |     | up  |
| 1/1/23 lag2     |                    |     |     | up  |
| 2/1/23 lag2     |                    |     |     | up  |
| Partner details | of all interfaces: |     |     |     |
------------------------------------------------------------------------------
| Intf Aggr | Port Port | State System-ID | System Aggr |     |
| --------- | --------- | --------------- | ----------- | --- |
| Name      | Id Pri    |                 | Pri Key     |     |
------------------------------------------------------------------------------
1/1/18 lag1
2/1/18 lag1
1/1/23 lag2
2/1/23 lag2
VSF port shaping
TheVSF portshapingfeatureensuresseamlessstackingbetweenS0E91A/S0X44ASKUandother6300
SKUs.TheS0E91AandS0X44ASKUhaveaspeedlimitof100Gports,whilethespeedlimitofother6300
SKUsarelimitedupto50Gports.ToensurethatallVSFinterfacesrunatthelowestcommonspeed
supportedbytheentireVSFstack,portshapingisused.ThisfeatureisapplicableonlyintheVSFstack
containingatleastoneS0E91AorS0X44ASKUmember.IfalltheS0E91A/S0X44ASKUmembersare
removedfromthestack,portshapingwillnotwork.
VSFportshapingconfigurationisenabledbydefault.Usethecommand'novsfegress-shape'todisable
portshaping.Seevsfegress-shapefordetails.
Thisfeatureisapplicableonlyfor6300switchseries(exceptforS3L75A,S3L76AandS3L77A).
 Portshapingistriggeredforrecalculatingthespeedinthefollowingscenarios:
n Newmemberadditiontotheexistingstack.
n ExistingMemberremovalfromthestack.
n Linkstatechangesfromuptodownordowntoup.
n VSFconfigurationchanges.
n Topologytransitionsfromring-to-chainandchain-to-ring.
Portshapingwillbeappliedonlytothestackmembersthatareupandoperational.
Limitations
ThefollowingarelimitationsassociatedwiththeVSF portshapingfeature:
n Portshapingisnotsupportedon4100i,6100and6200switchseries.
n Inthe6300switchseries,thisfeatureisapplicableonlyinaVSF stackcontainingatleastoneS0E91A
orS0X44ASKUmember.
n Inthecaseoftwo-memberstack,portshapingwillworkonlywithringtopology.
n Portshapingisnotapplicableforthestandaloneconductordevice.
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 21

| Supported     | VSF         | port speeds |
| ------------- | ----------- | ----------- |
| For 4100i and | 6100 switch | series      |
4100iand6100stackssupportonlyhomogeneousportspeedsacrossthestackwhichmeansonlyone
portspeedissupportedacrossallVSFportsinthestack.Theportspeedisinternallysettothehighest
speedcapablebythefirstVSFinterfacethatisconfigured.
Iftheuserwantstochangetheportspeed,thenallVSFlinksmustbeunconfiguredandthedesiredport
canbeaddedasthefirstVSFinterface,whichwillsettheportspeedtothedesiredvalue.
Inthecaseoftransceiverports,thespeedisdeterminedbythebaytype.AnSFP+bay,ifconfiguredasthe1st
VSFinterface,willsettheportspeedto10G.
Protocolandfeaturedetails|22

| VSF Support | on SmartRate | Ports |     |
| ----------- | ------------ | ----- | --- |
AOS-CXsupportsVSFonSmartRateports.Thefollowingtableliststheplatformsandthesupported
SmartRatespeed.
Table1:SupportedSmartRateSpeed
Supported
| Platform | Product Type |     |     |
| -------- | ------------ | --- | --- |
SmartRate Speed
| 6300  | R8S89A,S0E91A,S0X44A                      |     | 10GSmartRate    |
| ----- | ----------------------------------------- | --- | --------------- |
| 6300  | R8S90A,R8S91A,JL659A,JL660A,S0G04A,S0G05A |     | 5GSmartRate     |
| 6300L | S3L75A                                    |     | 10GSmartRate    |
| 6300L | S3L76A,S3L77A                             |     | 5GSmartRate     |
| 6200  | R8Q71A,R8V12A                             |     | 5GSmartRate     |
| 6300  | S4P41A,S4P42A,S4P45A,S4P46A               |     | 5G/10GSmartRate |
SKUsS4P41A,S4P42A,S4P45AandS4P46AsupportSmartRateportswithdual-modeandcanoperateeitheron
5Gor10G.
Dynamicspeedchangesofdual-modeSRportsbetween5Gand10G,arenotsupportedwhenstackinginterfaces
areinuse.Ifthestackisupandoperatingwithdual-modeSRportsat5Gspeed,andtheuserwishestochange
thespeedto10G(orviceversa),usingthecommandsystem interface-group <GROUP> member <MEMBER-
| ID> speed <SPEED>,thestackmaysplit. |     |     |     |
| ----------------------------------- | --- | --- | --- |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 23

Chapter 3

Configuration task list

Configuration task list

The following sections describe the prerequisites and procedures to configure a VSF stack.

Stack deployment using auto-stacking

Utilize the VSF auto-stacking feature to quickly deploy pre-cabled stacks with minimal configuration
required.

Designating conductor switch

Auto-Stacking feature requires the conductor of the stack to be configured with VSF links. Optionally, a
secondary or standby device can also be configured.

The following are different methods to designate the conductor:

n Using LED mode button: Physically connect the switches in the desired topology on the reserved VSF
link ports and press the LED mode button until the mode changes to Stk on a factory default switch.
This will automatically configure member 2 as the secondary member and configure the reserved
VSF link ports as VSF links 1 and 2. In addition to VSF secondary and link configurations , ztp force-
provision will also be configured on the conductor switch. The status of stack formation can be
verified using Stk LED and Port LEDs states. For more information on LED states, see Stack and Port
LED states.

Auto-Stacking configures the higher-numbered reserved port on member 1 (14, 26, 42 or 50,

depending on the SKU) as VSF link 1, and the lower-numbered reserved port (13, 25, 41 or 49,

depending on the SKU) as VSF link 2, unless explicitly defined in a configuration downloaded by ZTP.

n Using start auto-stacking CLI: Physically connect the switches in a desired topology on the reserved
VSF link port and execute the vsf start-auto-stacking command to automatically configure links.
The command also configures member 2 as secondary. For more information, see Forming a four-
member ring setup using auto-stacking command

Example:

switch(config)# vsf start-auto-stacking
This will configure links and secondary on conductor

Do you want to continue (y/n)? y

For information on interfaces that should be configured as VSF links, refer to the Reserved
interfaces for auto-stacking section.

To use this command, the switch must be in the factory default configuration.

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

24

n Using link configuration CLI: Execute the vsf member command to configure VSF links on the

conductor.

Example:

6300(vsf-member-1)# link 1 1/1/26
6300(vsf-member-1)# link 2 1/1/25

To form an ordered stack, it is recommended to configure higher denomination interface first into

VSF link .

n TFTP download: Full stack configuration can be downloaded into the conductor of the stack. The

recommendation is to first download the configuration to the startup and then move the startup to
the running configuration.

n ZTP download: Full stack configuration can be downloaded into the conductor of the stack from TFTP

server using ZTP. Once the configuration has been downloaded and applied, auto-stacking peer
discovery proceeds and forms a stack.

For more information on ZTP, refer to the Zero Touch Provisioning chapter in the Fundamentals Guide.

If full stack configuration is downloaded into the conductor through TFTP/ZTP, the physical

connections between the switches should be made according to the downloaded configuration.

Auto-stacking using LED mode button

Prerequisites

n All switches must be in the factory default configuration.

n All stack members must be connected in a ring topology on the reserved VSF link ports. For more

information, see Reserved interfaces for auto-stacking.

n Operator must be connected to the conductor’s USB-C console port or a terminal server connected

to the USB-A port via a supported adapter or cable.

n This feature is not supported on 4100i or 6100 switch series.

Procedure

1. Physically connect the switches in a desired topology on the reserved VSF link ports.

2. Press the LED mode button on the conductor until the mode changes to “Stk”. The stack

members reboot one after another and join the stack.

During stacking operation, the port LEDs are displayed in three different states:

n Flashing green—Indicates that the member is the conductor.

n Flashing orange—Indicates that the member is rebooting to join the stack or offline due to

error condition.

n Solid green—Indicates that the member joined the stack and is operational.

For more information on stacking LED states, refer to the Monitoring Guide.

3.

Issue a "show vsf" command to ensure that the stack has successfully formed. Alternatively, you
can also verify the stack formation using LED states.

Configuration task list | 25

| switch (config)#     | show   | vsf                 |          |
| -------------------- | ------ | ------------------- | -------- |
| Force Autojoin       |        | : Disabled          |          |
| Autojoin Eligibility |        | Status: Not         | Eligible |
| MAC Address          |        | : 70:72:cf:ef:b7:f2 |          |
| Egress Shape         |        | : Enabled           |          |
| Egress Shape         | Rate   | : None              |          |
| Secondary            |        | : 2                 |          |
| Topology             |        | : Chain             |          |
| Status               |        | : No                | Split    |
| Split Detection      | Method | : None              |          |
| Mbr Mac Address      |        | type                | Status   |
ID
| --- ------------------- |     | -------------- | --------------- |
| ----------------------- | --- | -------------- | --------------- |
| 1 70:72:cf:ef:b7:f2     |     | JL664A         | Conductor       |
| 2 90:20:c2:23:67:40     |     | JL664A         | Standby         |
| 3 90:20:c2:24:71:c0     |     | JL667A         | Member          |
| 4 38:21:c7:5a:33:40     |     | JL668A         | Member          |
Auto-stacking using CLI command
Prerequisites
n Allswitchesmustbeinthefactorydefaultconfiguration.
n AllstackmembersmustbeconnectedinaringtopologyonthereservedVSFlinkports.Formore
| information,see Reservedinterfacesforauto-stacking. |     |     |     |
| --------------------------------------------------- | --- | --- | --- |
n Operatormustbeconnectedtotheconductor’sUSB-Cconsoleportoraterminalserverconnected
totheUSB-Aportviaasupportedadapterorcable.
Procedure
1. PhysicallyconnecttheswitchesinadesiredtopologyonthereservedVSFlinkports.
2. Connecttotheswitchconsoleandloginusingtheadminuser;setapasswordwhenprompted.
3. Issuethevsf start-auto-stackingfromtheconfigurationcontexttostartauto-stacking.The
stackmembersrebootoneafteranotherandjointhestack.
4.
| switch(config)# | vsf | start-auto-stacking |     |
| --------------- | --- | ------------------- | --- |
5. Issuea"showvsf"commandtoensurethatthestackhassuccessfullyformed.Alternatively,you
canalsoverifythestackformationusingLEDstates.
| switch(config)#      | show   | vsf                 |          |
| -------------------- | ------ | ------------------- | -------- |
| Force Autojoin       |        | : Disabled          |          |
| Autojoin Eligibility |        | Status: Not         | Eligible |
| MAC Address          |        | : 70:72:cf:ef:b7:f2 |          |
| Egress Shape         |        | : Enabled           |          |
| Egress Shape         | Rate   | : None              |          |
| Secondary            |        | : 2                 |          |
| Topology             |        | : Chain             |          |
| Status               |        | : No                | Split    |
| Split Detection      | Method | : None              |          |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 26

| Mbr Mac | Address | type | Status |     |     |
| ------- | ------- | ---- | ------ | --- | --- |
ID
| --- ------------------- |                  | -------------- | --------------- |       |     |
| ----------------------- | ---------------- | -------------- | --------------- | ----- | --- |
| 1 70:72:cf:ef:b7:f2     |                  | JL664A         | Conductor       |       |     |
| 2 90:20:c2:23:67:40     |                  | JL664A         | Standby         |       |     |
| 3 90:20:c2:24:71:c0     |                  | JL667A         | Member          |       |     |
| 4 38:21:c7:5a:33:40     |                  | JL668A         | Member          |       |     |
| Auto-stacking           | using zero-touch | provisioning   |                 | (ZTP) |     |
Prerequisites
n Allswitchesmustbeinfactorydefaultconfiguration.
n Theconductorswitchmustbeconnectedtothemanagementnetwork.
n AllstackmustbeconnectedinaringtopologyusingSFPusingSFPuplinkportswithaminimumVSF
linkspeedof10Gbps.
n AsupportedZTPmethod,suchasaTFTPservermustbedefinedbyDHCPoptions.
| ZTP auto-stacking | via DHCP |     |     |     |     |
| ----------------- | -------- | --- | --- | --- | --- |
AOS-CXusesthefollowingDHCPoptionstospecifynetworklocationsandfilenamesforautomatic
configurationandsoftwareimagedownloads:
n Option60:VendorClassIdentifier(VCI).
VCIprovidedinDHCPrequestfromswitchismatchedtoanOption43vendorclassdefinedontheDHCP
servertoprovideconfigurationfilenameonTFTPserver.
n Option66:TFTPservername(IPv4address)
n Option43:Vendor-specificinformation
o suboption144:Nameoftheconfigurationfile
o Sub-option145:Nameofthefirmwareimagefile
Usetheshow dhcp client vendor-class-identifiercommandfromtheconductorswitchtodisplay
theVCIstringneededtoconfiguretheDHCPOption43vendorclassontheDHCPserver
OntheDHCPserver,configurepredefinedoption144foreachvendorclassthatwillbeusedtospecify
thefilenamewiththeZTPconfigurationtobedownloadedbythestackmember.
Optionally,youcanalsoconfigureoption145withthefilenameforanAOS-CXsoftwareimagethatwill
bedownloadedbytheconductorforautomaticimageupgrades.
ZTPauto-stackingisinitiatedbypoweringupstackmembers,withtheconductor(member1)receivinga
DHCPaddresswithTFTPconfigdownloadparametersinDHCPsuboption144.Theconductor
downloadstheZTPconfigurationfromtheTFTPserver,whichincludesconfigurationforallmembers.If
VSFlinksaredefinedandconnected,theyareusedforpeerdiscovery;otherwise,thereservedVSFlink
portsareconfiguredandusedinstead.
Oncetheconfigurationhasbeendownloadedandapplied,auto-stackingpeerdiscoveryproceedsand
formsastack.
FormoreinformationonZTP,refertotheZeroTouchProvisioningchapterintheFundamentalsGuide.
| Auto-stacking | using HPE | Aruba Networking |     | CX mobile | app |
| ------------- | --------- | ---------------- | --- | --------- | --- |
Prerequisites
Configurationtasklist|27

n All switches must be in the factory default configuration.

n All stack members must be connected in a ring topology.

n Bluetooth adapters are installed in all stack member USB-A ports.

n Supported iOS, iPadOS, or Android mobile device is running the HPE Aruba Networking CX mobile

app version 2.0 or later.

Procedure

Note: Spanning Tree is enabled by default on 4100i, 6100, 6200, and 6300 switch families, which will prevent a

loop from forming when VSF link cables are connected prior to the stack being fully provisioned.

1. On the mobile device with the HPE Aruba Networking CX mobile app installed, first use Bluetooth
to discover and connect to the switch that will be the stack primary; each switch should show up
in the device list using the format 6x00-SERIAL_NUMBER.

2. Once the device is connected to the switch, launch the HPE Aruba Networking CX mobile app.

Within a few seconds, the app should display an active Bluetooth connection to the switch with
the message Login Required. Tap the Initial Config button to start the stack configuration.

3. On the Device Login screen, leave the Connection Type as Bluetooth. Enter the username admin
and leave the password field blank, then tap the Log In button at the bottom of the screen.

4. On the Initial Config screen, tap the Stack button to begin stack setup. The app will automatically
discover all switches that are connected to the primary via VSF link cables, connect to them via
Bluetooth, and will display them in the topology view on the screen.

5. To change member IDs or assign a member as the stack secondary, tap the switch in the topology
view. Enabling the LED switch for each switch causes the blue UID LED on its front panel to flash;
use them to verify that the physical stack layout matches the displayed topology. Select
Configure Members to apply member IDs and secondary configuration to all switches in the
stack, which will cause each member other than the primary to reboot.

6. Once all switches have rebooted and joined the stack, the message Stack Set Up Successful! will

be displayed. Select Configure Stack to continue.

7.

If NetEdit will be used to manage the stack, enter the NetEdit server address, username, and
password, then tap Log In; if not, then tap Skip.

8. Choose the desired switch management interface from the dropdown menu; configure the stack
hostname, admin password, and management IP interface (static or DHCP); Alternately, you may
deploy a custom configuration template (saved on your device or available on a connected file
sharing service such as OneDrive, Dropbox, or iCloud Drive) by tapping the interface dropdown
menu, and selecting Import Custom Template… Once the desired configuration has been
selected, tap Next to continue.

9. Review the configuration generated by the app or imported from a template; then, tap Deploy to

apply the configuration to the stack.

10. Once the configuration has been successfully deployed, the connection between the device and
the switch (now the stack primary) will turn green, and the message Device Deployment
Successful! will be displayed. Tap Done to return to the app’s main page.

Manual configuration

In cases where auto-stacking or the HPE Aruba Networking CX mobile app cannot be used to provision a
stack, stack members can be configured manually.

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

28

VSF links

The user can specify the interfaces which comprise the VSF links. Refer to link for information about
specifying interfaces.

When the interface is configured, any existing configuration is removed, including VLAN memberships,
ACL/Quality of Service rules and any speed/duplex/MTU configuration.

Once the interface becomes part of a VSF link, no protocol or feature will be allowed to run on it as it is
now part of the fabric.

A VSF link will be a routed interface.

Secondary member

When auto-stacking is used to provision a stack, member 2 is automatically designated as the
secondary. A secondary member can be designated from the Conductor using any valid stack member
ID other than 1 before or after that member has actually joined the stack.

Member number 1 can never be configured as a secondary member.

An existing non-secondary stack member that is designated as the secondary will reboot and rejoin the
stack to assume the Standby role. If a member not present in the stack is designated as the secondary,
that member will automatically assume the Standby role without an additional reboot when it
subsequently joins the stack.

If a secondary member is already configured and present in the stack, removing the secondary
designation will cause that member to reboot and rejoin the stack with the Member role.

Refer to vsf secondary-member for information about configuring a secondary member.

In the case of auto-stacking, member 2 is automatically configured as secondary member through
LED button press or vsf start-auto-stacking command.

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
conductor switch via VSF link. If a renumbered member is unable to communicate with the conductor
switch and is waiting in booting state, the user can:

n Go to a recovery console with a ctrl+c sequence and collect the diagnostic information, or

n Reset the VSF configuration.

Member provisioning

Configuration task list | 29

VSF allows the user to provision or pre-configure any member before the member is physically added to
the stack. Provisioning the member allows the user to complete the required configuration as if the
member is present in the stack. When the member eventually joins the stack, it will boot up with the
configuration made on the pre-provisioned interfaces.

To provision a member, the part number of the member must be specified. Refer to type for
information about provisioning a member.

If a member tries to join the stack with a different part number to the one provisioned on the Conductor, the

renumbered member will be removed from the stack and will reboot with factory defaults.

Access to VSF members

In addition to serial console connections, any stack member can be accessed from any other member
using the member command.

Refer to member for information about console connection to a member switch.

Stack management

Consoles

The serial console of the Conductor switch provides a full CLI configuration interface for a user with
valid credentials. The serial console of the other stack members, including the Standby, provides a
reduced CLI configuration interface, with only a limited set of commands for troubleshooting the stack.

In a standard deployment, connect to the console interface of the conductor and standby switch. This
enables the stack conductor console to be reachable after a stack failover to the new Conductor.

Any switch configuration or monitoring must be performed from the console of the stack Conductor switch only.

Management interface

In a VSF stack, only the management interface on the Conductor switch will be assigned an IP address
(configured or assigned by DHCP). The stack allows connectivity to management protocols and Console
through the management interface on the Conductor.

The management interface is applicable only for 6200 and 6300 devices.

Split detection

4100i and 6100 Switch Series

4100i and 6100 switch series which do not have OOBM ports, use front-plane ports to detect active
stack fragments upon split. These ports should be part of a VSF Multi-Active Detection (MAD) VLAN. Only
one MAD VLAN can be configured. One front-plane port from primary and one front-plane port from
secondary should be part of a MAD VLAN as access ports and interconnected either directly or over the
same Layer 2 (L2) network.

Limitations:

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

30

n Any other protocol which may alter the functionality of split detection should not be enabled on MAD

VLAN and front-plane ports used for split detection.

n Only one port from primary and secondary can be assigned to the MAD VLAN.

n Trunk and Aggregation ports cannot be assigned to the MAD VLAN.

n The default VLAN cannot also be the MAD VLAN.

For more information, refer to vsf split-detect vlan .

6200, 6300 and 6300L Switch Series

On 6200, 6300 and 6300L switch series VSF stack supports split detection utilizing the management
interfaces, which requires users to connect the management interfaces of the primary and secondary
stack members to the same L2 network.

It is also possible to connect the management interfaces of primary and secondary directly to one another for

split detection.

In the event of a stack split where the primary and secondary members are on opposite sides of the
split, if the secondary fragment discovers that the primary fragment is operational via the management
port connection, it will bring down all front-plane non-VSF interfaces on the secondary fragment to
minimize network disruption due to duplicate MAC or IP addresses.

The interfaces will remain down until the stack is reconnected or the primary fragment goes down. The
interfaces of the primary fragment will always remain operational.

The show vsf output in the Primary fragment will look like this:

Configuration task list | 31

| switch#         | show        | vsf    |                     |          |          |
| --------------- | ----------- | ------ | ------------------- | -------- | -------- |
| Force Autojoin  |             |        | : Disabled          |          |          |
| Autojoin        | Eligibility |        | Status: Not         | Eligible |          |
| MAC Address     |             |        | : 08:97:34:b0:0e:00 |          |          |
| Egress Shape    |             |        | : Enabled           |          |          |
| Egress Shape    |             | Rate   | : None              |          |          |
| Secondary       |             |        | : 2                 |          |          |
| Topology        |             |        | : Chain             |          |          |
| Status          |             |        | : Active            |          | Fragment |
| Split Detection |             | Method | : mgmt              |          |          |
| Mbr Mac         | Address     |        | type                |          | Status   |
ID
| --- ------------------- |     |     | -------------- |     | ---------------   |
| ----------------------- | --- | --- | -------------- | --- | ----------------- |
| 1 38:21:c7:5c:f4:c0     |     |     | JL668A         |     | Conductor         |
| 2                       |     |     | JL668A         |     | In Other Fragment |
| 3                       |     |     | JL668A         |     | In Other Fragment |
| 4                       |     |     | JL668A         |     | In Other Fragment |
switch#
| switch# | show | vsf topology |     |     |     |
| ------- | ---- | ------------ | --- | --- | --- |
Conductor
+---+
| 1 |
+---+
switch#
Theshow vsfoutputinthesecondaryfragmentwilllooklikethis:
| switch#         | show        | vsf    |                     |          |          |
| --------------- | ----------- | ------ | ------------------- | -------- | -------- |
| Force Autojoin  |             |        | : Disabled          |          |          |
| Autojoin        | Eligibility |        | Status: Not         | Eligible |          |
| MAC Address     |             |        | : 08:97:34:b0:0e:00 |          |          |
| Egress Shape    |             |        | : Enabled           |          |          |
| Egress Shape    |             | Rate   | : None              |          |          |
| Secondary       |             |        | : 2                 |          |          |
| Topology        |             |        | : Chain             |          |          |
| Status          |             |        | : Inactive          |          | Fragment |
| Split Detection |             | Method | : mgmt              |          |          |
| Mbr Mac         | Address     |        | type                |          | Status   |
ID
| --- ------------------- |     |     | -------------- |     | ---------------   |
| ----------------------- | --- | --- | -------------- | --- | ----------------- |
| 1                       |     |     | JL668A         |     | In Other Fragment |
| 2 38:21:c7:5c:77:40     |     |     | JL668A         |     | Conductor         |
| 3 38:21:c7:5a:a5:80     |     |     | JL668A         |     | Member            |
| 4 38:21:c7:5c:b3:00     |     |     | JL668A         |     | Member            |
switch#
| switch# | show | vsf topology |     |     |     |
| ------- | ---- | ------------ | --- | --- | --- |
Conductor
| +---+      | +---+ | +---+  |     |     |     |
| ---------- | ----- | ------ | --- | --- | --- |
| | 4 |1==2| | 3     | |1==2| | 2 | |     |     |
| +---+      | +---+ | +---+  |     |     |     |
switch#
Formoreinformation,refertovsfsplit-detectmgmt.
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 32

Automated image sync

In a VSF environment, all stack members run the same software image. If the user upgrades the
software on the Conductor by downloading a new software image using SFTP/TFTP, all members of the
stack will simultaneously upgrade.

When forming a stack, if the software version on a member is different from the version of the
Conductor, the member will automatically update itself to the same version as the Conductor. The
member will reboot itself to run the updated version before joining the stack.

Automated image sync is not applicable if the conductor is running the firmware version 10.07 or later and the

member is booted with firmware version 10.06 or earlier versions and vice-versa.

Reboot

An individual stack member can be rebooted from a CLI command.

n The member will reboot and re-join the stack, with the same role that it had prior to the reboot.

n If the stack topology is a ring, no traffic disruption is expected on any other stack members when a

single member is rebooted.

n If the stack topology is a chain, rebooting a member may cause a stack split, resulting in members
being unreachable from the conductor. This result can cause significant disruption of the stack, so
use this option with caution.

n If the member is the stack Standby, there will be no Standby in the stack until the member reboots

and re-joins the stack. At this point, the member will again have the role of Standby.

n If the member is the stack Conductor, the command will trigger a failover and the Standby switch will

take over as Conductor of the stack.

n If the Standby is unavailable at the time of conductor reboot, the whole stack will reboot.

The whole stack can also be rebooted by using the boot system command.

n All members will reboot and the stack will re-form.

n Traffic will be disrupted for the duration of the reboot.

Refer to vsf member reboot for information about rebooting a member.

Member addition with auto-stacking

A new factory default switch can be added into an existing stack by physically connecting it to a given
member of the stack on the auto-stacking reserved interfaces. The newly added member will be
automatically assigned with member ID and go for a reboot. After reboot, the newly added member will
join the stack.

For more information auto-stacking reserved interfaces, Reserved interfaces for auto-stacking.

Member addition without auto-stacking

A member can be added to the stack to augment an existing stack. The member being added can be a
factory-default switch or a switch with pre-existing configuration.

Configuration task list | 33

1. Configure interfaces to VSF links on the member being added.

2. Renumber the member being added.

The member will not join the stack if there is a member number conflict.

3. Renumbering will cause a reboot of the switch.

4. Connect the configured VSF links to a previously configured VSF link on the stack.

5. The member joins the stack, with default configuration on its interfaces. Any previous

configuration on the member will be lost.

Member replacement with auto-stacking

Disconnect all the physical connections of the member that will be replaced and connect the new
replacement member to the same interfaces as the switch being replaced. The new member joins the
stack, with the same configuration as the member it is replacing.

The replacement member must be of the same part number as the switch being replaced.

Member replacement without auto-stacking

The replacement member must be of the same part number as the switch being replaced.

1. Power off or disconnect all physical connections of the member that will be replaced.

2. Configure interfaces to VSF links on the replacement member. These interfaces must match the

interfaces configured on the switch being replaced.

3. Renumber the replacement member to the same number as the switch being replaced.

4. Renumbering will cause a reboot of the switch.

5. Connect the replacement member to the stack.

6. The member joins the stack, with the same configuration as the member it is replacing.

Member removal

A member can be removed from a running stack. All configuration associated with the member will be
removed.

If the member is physically present in the stack at the time it is removed, all VSF configurations on that
member will be erased and it will lose its identity as a member of the stack from which it was removed.
The member will come back as member 1 with factory default configuration.

It is not advisable to remove the member that is the conductor of the stack. If the conductor has to be removed,

the recommendation is to switch over and wait for the old conductor to come up as standby before removing it.

Refer to the vsf member command for information about removing a member.

Though it is not recommended as it can cause traffic outages, if an active member needs to be removed
from a stack, member must be physically removed after issuing no vsf member command. Else, the
member will join the stack back through auto-stacking. Alternatively, the links can be disabled first and
the member can be removed from the conductor. The removed member must be reset to factory-
default once it boots to recovery.

Stack and Port LED states

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

34

The following table describes the different states of stack Stk LED for 6200 and 6300 switch series.

Table 1: Stk LED States

State

Meaning

On - Green

Stacking Mode is selected.

On - Amber

Stacking Mode is selected and stacking-related error has occurred.

Slow flash Amber

Stacking Mode is not selected but still stacking-related error has occurred.

Off

Stacking mode is not selected.

The following table describes the different states of speed Spd LED for 4100i and 6100 switch series.

Table 2: Spd LED States

State

Meaning

On - Green

Speed Mode is selected.

Slow flash Green

Stacking Mode is selected.

Off

Speed and Stacking mode are not selected.

The following table describes the different states of Port LED based on stack configurations and role of
the members in the stack.

Table 3: Port LED States

State

Meaning

On - Green

Current Stack Member and is operational.
For example, if Port 3 is on green, this indicates that the current chassis is member 3 in
the stack.

Half-bright green

Total members in the Stack.
Except port LEDs indicating the conductor and current member, all other ports LEDs glow
half-bright green.

Slow flash green

Conductor of the Stack.
In a six-member stack, one of the six port LEDs glows slow flashing green indicating that
unit in the stack is the conductor. For example, if Stack Member 4 is the conductor, Port 4
LED glow slow flashing green.

On- Amber

The stack member is not reachable or in booting condition.
When the member is fully booted and joined the stack successfully, then LED glows solid
green.

Slow flash amber

The stack member is in a known fault condition. Only the global Status LED of faulted
member glows slow flash amber.

Off

The stack Member does not exist in the stack.

Configuration task list | 35

Chapter 4

Use cases

Use cases

The following sections describe the prerequisites and procedures to configure a VSF stack.

Forming a four-member ring setup using auto-stacking
command

Prerequisites

n All switches must be in the factory default configuration.

n All stack members must be connected in a desired topology on the reserved VSF link ports. For more

information, see Reserved interfaces for auto-stacking.

In the following procedure, the vsf start-auto-stacking command is used to form a four-member
stack with the ring topology:

Figure 1 Four-member ring setup

Procedure

1. Rack up all the four switches and physically connect them on the reserved auto-stacking

interfaces in a ring setup . For more information on reserved interfaces, see

Alternatively, you can also add members one after another.

2. Designate the first switch of the rack using the vsf start-auto-stacking command as the

conductor. The links and secondary member will be automatically configured on the conductor.

switch(config)# vsf start-auto-stacking

Since the switches are already physically connected, starting with the second switch, each switch
in the stack reboots automatically and join the stack one after another automatically. The running
configuration will appear as shown below:

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

36

| 6300# show             | run |     |     |
| ---------------------- | --- | --- | --- |
| Current configuration: |     |     |     |
!
| !Version AOS-CX   | FL.10.07.xxxx |         |     |
| ----------------- | ------------- | ------- | --- |
| !export-password: |               | default |     |
cli-session
| timeout | 0   |     |     |
| ------- | --- | --- | --- |
!
!
!
!
!
!
| ssh server           | vrf default |     |     |
| -------------------- | ----------- | --- | --- |
| ssh server           | vrf mgmt    |     |     |
| vsf secondary-member |             | 2   |     |
| vsf member           | 1           |     |     |
| type jl668a          |             |     |     |
| link 1               | 1/1/26      |     |     |
| link 2               | 1/1/25      |     |     |
| vsf member           | 2           |     |     |
| type jl668a          |             |     |     |
| link 1               | 2/1/25      |     |     |
| link 2               | 2/1/26      |     |     |
| vsf member           | 3           |     |     |
| type jl668a          |             |     |     |
| link 1               | 3/1/26      |     |     |
| link 2               | 3/1/25      |     |     |
| vsf member           | 4           |     |     |
| type jl668a          |             |     |     |
| link 1               | 4/1/25      |     |     |
| link 2               | 4/1/26      |     |     |
3. Issuea"showvsf"commandtoensurethattheringhassuccessfullyformed.Youcanalsoverify
stackformationusingdifferentLED states.FormoreinformationonLEDstates,StackandPort
LEDstates.
| 6300(config)#        | show   | vsf                 |          |
| -------------------- | ------ | ------------------- | -------- |
| Force Autojoin       |        | : Disabled          |          |
| Autojoin Eligibility |        | Status: Not         | Eligible |
| MAC Address          |        | : 70:72:cf:ef:b7:f2 |          |
| Egress Shape         |        | : Enabled           |          |
| Egress Shape         | Rate   | : None              |          |
| Secondary            |        | : 2                 |          |
| Topology             |        | : Ring              |          |
| Status               |        | : No                | Split    |
| Split Detection      | Method | : None              |          |
| Mbr Mac Address      |        | type                | Status   |
ID
| --- ------------------- |     | -------------- | --------------- |
| ----------------------- | --- | -------------- | --------------- |
| 1 70:72:cf:ef:b7:f2     |     | JL668A         | Conductor       |
| 2 90:20:c2:23:67:40     |     | JL668A         | Standby         |
| 3 90:20:c2:24:71:c0     |     | JL668A         | Member          |
| 4 38:21:c7:5a:33:40     |     | JL668A         | Member          |
Usecases|37

IffullstackconfigurationisdownloadedontotheconductorthroughTFTP/ZTP,thephysical
connectionsbetweentheswitchesshouldbemadeaccordingtothedownloadedconfiguration.
| Forming       | a four-member |     | chain setup    | using link |
| ------------- | ------------- | --- | -------------- | ---------- |
| configuration | command       |     | with auto-join |            |
ManualconfigurationofaVSFstackrequirestheusertoindividuallyconfigureeachswitchinthestack.
| Figure1 Four-memberchainsetup |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- |
Procedure
1. Executethefollowingcommandonthemember1:
switch# configure
| switch(config)#       |     | vsf member | 1        |     |
| --------------------- | --- | ---------- | -------- | --- |
| switch(vsf-member-1)# |     | link       | 1 1/1/26 |     |
| switch(config)#       |     | vsf member | 2        |     |
2. Physicallyconnectmember2tomember1ontheauto-stackingreservedinterfaces.Forexample,
ifpartnumberoftheswitchisJL659A,thenreservedauto-stackinginterfacesare25and26.Once
thephysicalconnectionsaremade,member2willrebootautomaticallyandjointhestackas
standbyswitchwithmember1astheconductor.Therunningconfigurationontheconductor
whenmember2jointhestackwillappearasshownbelow:
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 38

|     | vsf secondary-member |     | 2   |     |     |     |
| --- | -------------------- | --- | --- | --- | --- | --- |
|     | vsf member           | 1   |     |     |     |     |
type jl659a
|     | link 1 1/1/26 |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- |
|     | vsf member    | 2   |     |     |     |     |
type jl661a
|     | link 1 2/1/25 |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- |
Theconductor'sVSF linkmustbeconnectedtointerfaceofhighervalue.Forexample,whenyou
areconnectingmember2tomember1,youmustconnectinterface26ofmember1to
interface25ofmember2.Otherwiswe,themember2willnotjoininauto-stacking.
3. Physicallyconnectmember3tomember2ontheauto-stackingreservedinterfaces.Themember
3willrebootautomaticallyandjointhestackasmember.
4. Repeatthestep3forstackmember4.Oncetheauto-stackingprocessiscomplete,member4will
rebootautomaticallyandjointhestackasmember4.Thisformsachaintopology.
5. Issuea"showvsf"commandtoensurethattheringhassuccessfullyformed.Youcanalsoverify
thestackformationusingLEDstates.FormoreinformationonLEDstates,StackandPortLED
states.
|     | switch(config)# | show        | vsf     |                     |        |     |
| --- | --------------- | ----------- | ------- | ------------------- | ------ | --- |
|     | Force Autojoin  |             |         | : Disabled          |        |     |
|     | Autojoin        | Eligibility | Status: | Not Eligible        |        |     |
|     | MAC Address     |             |         | : 70:72:cf:ef:b7:f2 |        |     |
|     | Egress Shape    |             |         | : Enabled           |        |     |
|     | Egress Shape    | Rate        |         | : None              |        |     |
|     | Secondary       |             |         | : 2                 |        |     |
|     | Topology        |             |         | : Chain             |        |     |
|     | Status          |             |         | : No Split          |        |     |
|     | Split Detection | Method      |         | : None              |        |     |
|     | Mbr Mac Address |             | type    |                     | Status |     |
ID
|     | --- ------------------- |     | -------------- |     | --------------- |     |
| --- | ----------------------- | --- | -------------- | --- | --------------- | --- |
|     | 1 70:72:cf:ef:b7:f2     |     | JL659A         |     | Conductor       |     |
|     | 2 90:20:c2:23:67:40     |     | JL661A         |     | Standby         |     |
|     | 3 90:20:c2:24:71:c0     |     | JL668A         |     | Member          |     |
|     | 4 38:21:c7:5a:33:40     |     | JL668A         |     | Member          |     |
IffullstackconfigurationisdownloadedintotheconductorthroughTFTP/ZTP,thephysical
connectionsbetweentheswitchesshouldbemadeaccordingtothedownloadedconfiguration.
| Forming       | an  | eight-member |               | ring | setup manually | using link |
| ------------- | --- | ------------ | ------------- | ---- | -------------- | ---------- |
| configuration |     | without      | auto-stacking |      |                |            |
ManualconfigurationofaVSFstackrequirestheusertoindividuallyconfigureeachswitchinthestack.
ThisprocessprovidesthebestcontrolfortheusertoconfigureVSFmembernumberandlinks.
| Figure1 | Eight-memberringsetup |     |     |     |     |     |
| ------- | --------------------- | --- | --- | --- | --- | --- |
Usecases|39

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
| switch (config)#      | vsf member      | 1        |
| --------------------- | --------------- | -------- |
| switch(vsf-member-1)# | link            | 1 1/1/25 |
| switch(vsf-member-1)# | link            | 2 1/1/26 |
| switch(vsf-member-1)# | exit            |          |
| switch(config)#       | vsf renumber-to | 2        |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 40

| This will | save    | the VSF  | configuration |     | and reboot | the switch. |
| --------- | ------- | -------- | ------------- | --- | ---------- | ----------- |
| Do you    | want to | continue | (y/n)?        | y   |            |             |
b. Theprecedingsequenceofcommandswillconfigurethelinksonmember2.
c. Thedefaultmembernumberis"1".Thecommand"vsfrenumber-to"changesthismember
number.
d. Linksareconfiguredbeforerenumbering,andthememberidentifierintheinterfacenameis
"1"atthispoint.
e. Theswitchwillrebootafterexecutingtherenumbercommand.
3. Physicallyconnectmember2tomember1asshowninthefigure.
a. Thisactionwillcausemember2tojointhestack,withmember1astheconductor.
b. Thisresultcanbeverifiedbyexecuting"showvsf"onmember1.
4. Repeatsteps2and3,foreachstackmember3through8.
a. Besuretospecifythemembernumbercorrectlyoneachmember.
b. Ifamembernumberconflictisdetected,thememberwillNOTjointhestack.
5. Oncemember8hassuccessfullyjoinedthestack,connectmember8link2tomember1link1,to
completethering.
Issueashow vsfcommandtoensurethattheringhassuccessfullyformed.
| switch# show         | vsf  |         |                     |          |          |     |
| -------------------- | ---- | ------- | ------------------- | -------- | -------- | --- |
| Force Autojoin       |      |         | : Disabled          |          |          |     |
| Autojoin Eligibility |      | Status: | Not                 | Eligible |          |     |
| MAC Address          |      |         | : 38:21:c7:5d:d0:c0 |          |          |     |
| Egress Shape         |      |         | : Enabled           |          |          |     |
| Egress Shape         | Rate |         | : None              |          |          |     |
| Secondary            |      |         | :                   |          |          |     |
| Topology             |      |         | : Ring              |          |          |     |
| Status               |      |         | : Active            |          | Fragment |     |
| Split Detection      |      | Method  | : None              |          |          |     |
| Mbr Mac Address      |      |         | type                |          | Status   |     |
ID
| --- ------------------- |     |     | -------------- |     | --------------- |     |
| ----------------------- | --- | --- | -------------- | --- | --------------- | --- |
| 1 38:21:c7:5d:d0:c0     |     |     | JL668A         |     | Conductor       |     |
| 2 38:21:c7:6a:10:c0     |     |     | JL668A         |     | Member          |     |
| 3 38:21:c7:5c:15:80     |     |     | JL668A         |     | Member          |     |
| 4 38:21:c7:5a:61:40     |     |     | JL668A         |     | Member          |     |
| 5 38:21:c7:62:66:00     |     |     | JL668A         |     | Member          |     |
| 6 38:21:c7:58:22:40     |     |     | JL668A         |     | Member          |     |
| 7 38:21:c7:5a:9c:00     |     |     | JL668A         |     | Member          |     |
| 8 38:21:c7:63:a5:00     |     |     | JL668A         |     | Member          |     |
6. Theprecedingstepswillformaneight-memberstackwithoutastandby.Tomakeanymember
thestandby(forexample,member8),usethesecondarycommand:
a. FromtheprimaryVSFmember,configuremember8asVSFsecondarymember:
| swtich(config)# |     | vsf | secondary-member |     | 8   |     |
| --------------- | --- | --- | ---------------- | --- | --- | --- |
This will save the configuration and reboot the specified switch.
| Do you | want to | continue | (y/n)? | y   |     |     |
| ------ | ------- | -------- | ------ | --- | --- | --- |
Usecases|41

switch(config)#
b. Thisactionwillrebootmember8anditwillrejoinasstandby.
| switch# show         | vsf    |                     |          |
| -------------------- | ------ | ------------------- | -------- |
| Force Autojoin       |        | : Disabled          |          |
| Autojoin Eligibility |        | Status: Not         | Eligible |
| MAC Address          |        | : 38:21:c7:5d:d0:c0 |          |
| Egress Shape         |        | : Enabled           |          |
| Egress Shape         | Rate   | : None              |          |
| Secondary            |        | : 8                 |          |
| Topology             |        | : Ring              |          |
| Status               |        | : Active            | Fragment |
| Split Detection      | Method | : None              |          |
| Mbr Mac Address      |        | type                | Status   |
ID
| --- ------------------- |     | -------------- | --------------- |
| ----------------------- | --- | -------------- | --------------- |
| 1 38:21:c7:5d:d0:c0     |     | JL668A         | Conductor       |
| 2 38:21:c7:6a:10:c0     |     | JL668A         | Member          |
| 3 38:21:c7:5c:15:80     |     | JL668A         | Member          |
| 4 38:21:c7:5a:61:40     |     | JL668A         | Member          |
| 5 38:21:c7:62:66:00     |     | JL668A         | Member          |
| 6 38:21:c7:58:22:40     |     | JL668A         | Member          |
| 7 38:21:c7:5a:9c:00     |     | JL668A         | Member          |
| 8 38:21:c7:63:a5:00     |     | JL668A         | Standby         |
7. Alternatively,beforeaddingmember8tothestack,pre-configurethesecondaryas8andthen
renumberdevice8.Thisactionwillensurethatdevice8willjointhestackdirectlyasstandby.
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 42

VSF In-Service Software Upgrade

Chapter 5

VSF In-Service Software Upgrade

In VSF In-Service Software Upgrade (ISSU), the firmware image of the stack can be updated dynamically
with minimal downtime. The conductor, standby and members of the stack are upgraded dynamically
without having the necessity for them to reboot at all. This means that the traffic won't be interrupted
during the upgrade and if an error happens and traffic is interrupted to keep the interruption as short as

possible. HPE Aruba Networking's switch architecture decouples the control plane and the data plane,
so it is possible to implement an ISSU mechanism by keeping the data plane up while the control plane
manages the upgrade.

VSF ISSU is supported only on the HPE Aruba Networking 6300 Switch Series (except for S3L75A,S3L76A and

S3L77A).

VSF ISSU is supported for upgrades between minor releases.

The VSF ISSU feature uses ISSU commands for its operations (configuration & show commands). Refer to the VSF

commands section for command details.

Upgrade scope

The current ISSU feature is intended for upgrades between minor releases. This is suitable for stable
networks that need critical bug fixes or security fixes instead of full version upgrades to get new
functionality.

VSF ISSU operation

ISSU in the 6300 consists of a series of steps designed to keep the system in a stable state while the
firmware is upgraded and to recover this state after such upgrade.

Step 1: Image download and validation

The first step of the process is to download the image with the new version of the firmware to the
alternate flash. Verification is performed by the switch that it complies with the internal rules and the
security checks (e.g. valid signed image).

Upon successful verification, the new image will be installed in the bank that doesn't store the image
currently running on the switch. The old image will be kept in the alternative bank in case a fail back
process needs to be triggered due to an error.

The ISSU validation triggers after the ISSU operation is started. User can perform the validation without
triggering ISSU as well by using the CLI. For more information, refer the issu update-software command.

Step 2: Install the image in the standby & members

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

43

Once the new image is verified, the standby and members of the stack will be upgraded with this image
without having them to reboot.

Step 3: Freeze the system

Once the standby and members of the stack are successfully upgraded, the system's state will be
frozen. This means that no further configuration will be allowed until the ISSU is complete. In fact, no
configuration via CLI, REST, or SNMP is allowed once the ISSU process starts (Step 1) in order to make
sure that the system doesn't become unstable once ISSU has started. Informational queries are still
allowed. Any change in the network such as MAC learning will not be reflected until ISSU is complete.
Please refer to Information not updated during ISSU for additional information.

Step 4: Perform the upgrade for the line modules

The Line Card (LC) modules services on standby and all the members of the stack will be upgraded at
this time, however they will not be rebooted.

Step 5: Recover the previous state

The previous state will be recovered and synchronized with the new firmware running in the standby.
Some features can't recover the previous state at this point and therefore do not support uninterrupted
operation during ISSU. Please refer to Features that don't support uninterrupted operation during ISSU
for more information.

Step 6: Failover occurs between the conductor and the standby

The Standby will take over and becomes the new conductor running the new firmware version. All
sessions will be closed and the user will be required to log in again.

Step 7: The previous Conductor will upgrade its image

The previous conductor will upgrade its image and take the role of Standby and joins the stack without
reboot. The ISSU is complete at this point.

VSF ISSU considerations

The first requirement for ISSU is to ensure that traffic continues to pass through the stack
uninterrupted during the upgrade operation. In the event that something goes wrong traffic must be
restored as soon as possible. This could mean falling back to the previous image, or in some cases to
fall forward to the new one.

The upgrade process can take minutes to complete. During that time as many control plane protocols
as possible will remain operational, however some of them need to stop processing packets or avoid
reacting to events. Please refer to VSF ISSU limitations for additional information. The amount of time
when they are not operational will be kept as small as possible.

In order to start ISSU, the stack topology must be a Ring. The Standby and all members must be
operational and running. If any of them is in another state (e.g., booting) then the ISSU process will not
start.

VSF In-Service Software Upgrade | 44

VSF ISSU limitations

The ISSU process currently has the following limitations:

Hardware faults

It is recommended that hardware faults are resolved prior to performing ISSU. Fan faults and abnormal
temperature statuses should be addressed. Fans may increase in speed during the ISSU process.

Prohibited operations

During ISSU the following operations are not permitted:

n Any hardware hot swap

n Pressing any button

Performing any of these operations during an ISSU could put the system in an error state that could
adversely affect the ISSU.

The system may not be able to address failures during the ISSU. For example, if network protocols
require blocking a port, flush MAC, or routing tables, etc. the switch would not be able to react to those
tasks until the ISSU is complete.

Recommendations

Before initiating ISSU, it is recommended to enable spanning-tree root-guard on the supposed
designated ports of the VSF stack. This ensures and enforces the root bridge placement in the network.

Scheduled jobs

Since no configuration is allowed during the ISSU, it is possible that some scheduled jobs will fail if they
are attempted while the ISSU is in progress. It is recommended to not execute any scheduled job during
ISSU.

Information not updated during ISSU

During ISSU the following information may not be current until after ISSU completes:

n Link state. Transitions may not be reflected until ISSU is done.

n Temperatures.

n Power consumption values.

n System state as indicated by LEDs.

n MAC Learning.

n Change in MAC for a neighbor via Gratuitous ARP.

n Some counters will stop increasing their value during ISSU.

Show tech

The show tech command is enabled during ISSU using the CLI, however it isn't possible to use it with the
REST API.

Features that don't support uninterrupted operation during ISSU

During ISSU the following features may be interrupted until after ISSU completes:

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

45

AAA

1. During ISSU new client authentication will occur on other members except the VSF conductor that

is rebooting. Clients will not be able to access to the network until ISSU is complete.

2. Session timeout/inactivity timeout applied to clients will be delayed. Clients will remain longer

than the configured timer.

PIM with MSDP

Currently, PIM is not supported in ISSU on RP routers, therefore traffic loss is expected during ISSU on
RP routers where PIM and MSDP are enabled.

Dynautz ISSU

All Dynamic Authorization requests will be rejected with NAK during ISSU operation. Captive portal
workflow will be affected due to NAK received for Dynauth requests during ISSU.

BFD ISSU

It's important to note that this mechanism is only recommended for sessions that have a failure
detection time higher than 6 seconds (e.g. Tx=Rx=3000 and Detect Multiplier=2, or Tx=Rx=2000 and
Detect Multiplier=3). The setup should have less than 64 sessions, otherwise the ISSU failover might not
be hitless for all sessions.

NAE

NAE will have a momentary disruption during ISSU events due to the failover event. See the Network
Analytics Engine Guide for more information.

Feature readiness check

ISSU and feature readiness check will fail if the feature ready check does not pass. The feature ready
check validates that none of the following features are in a failed state:

n ACLs, object groups, and their applications

n Classifier policies, classes, and their applications

n Port-access polices, classes, and their applications

n Port-access group-based policies, classes, and their applications

n Active PBR actions and their applications

In general, if any of the above is in a failed state it is recommended to fix it and then upgrade to the
newer operating system image using the system reboot method instead of ISSU. Some failed states will
remain even after it is fixed on a running system and a reboot is good best practice for clearing it.

Restrictions

The following caveats apply:

1. VSF ISSU is not supported on 4100i, 6100 or 6200 platforms.

2. VSF ISSU is not supported on S3L75A, S3L76A, and S3L77A SKUs.

VSF ISSU errors and recovery

If any VSF stack member encounters an error during the "Initiate ISSU" or "Validate System Readiness"
phases then the ISSU process will be aborted.

VSF In-Service Software Upgrade | 46

If any VSF stack member encounters an error during the "Upgrade Standby and Member Modules" or
"Upgrade Line Module Services" phases, then the stack will be unable to recover. The entire stack will
reboot with the upgraded image directly.

If any stack member encounters an error during failover, the whole stack will be rebooted. The system
will boot with the new image. The error will be handled as a fail forward.

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

47

Chapter 6
VSF commands
VSF commands
| clear     | vsf             | split-detection |           |     | statistics |     |
| --------- | --------------- | --------------- | --------- | --- | ---------- | --- |
| clear vsf | split-detection |                 | statistic |     |            |     |
Description
ResetstheVSFsplit-detectionstatisticscounterstozero.
Example
Thefollowingexamplerunstheclear vsf split-detection statisticscommandtoclearsVSFsplit-
detectionstatisticcounters,thenusestheoptionalshow vsf split-detection statisticscommandto
verifythatthesestatisticswerecorrectlyresetbacktozero:
| switch# | clear | vsf | split-detection |     | statistics |     |
| ------- | ----- | --- | --------------- | --- | ---------- | --- |
switch#
| switch# | show  | vsf       | split-detection |     | statistics |     |
| ------- | ----- | --------- | --------------- | --- | ---------- | --- |
| VSF     | Split | Detection | Statistics:     |     |            |     |
===============================
| Total      | Packets     | Transmitted |         |           |                   | = 0 |
| ---------- | ----------- | ----------- | ------- | --------- | ----------------- | --- |
| Total      | Packets     | Received    |         |           |                   | = 0 |
| Total      | Packets     | Received    | And     | Discarded |                   | = 0 |
| Command    | History     |             |         |           |                   |     |
| Release    |             |             |         |           | Modification      |     |
| 10.16.1000 |             |             |         |           | Commandintroduced |     |
| Command    | Information |             |         |           |                   |     |
| Platforms  |             | Command     | context |           | Authority         |     |
| 4100       |             | Manager(#)  |         |           |                   |     |
6100
6200
6300
description
description
no description
Description
AddsadescriptionforoneormoreVSFlinkinterfaces.
Thenoformofthiscommandremovestheinterfacedescription.
48
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries)

Examples
AddingadescriptionforVSFlinkinterface1/1/25:
switch(config)#
|                        | interface | 1/1/25      |            |        |
| ---------------------- | --------- | ----------- | ---------- | ------ |
| switch(config-if-vsf)# |           | description | mem 1 intf | 1/1/25 |
Removingthedescriptionfrominterface1/1/25
| switch(config)#        | int     | 1/1/25         |                                             |     |
| ---------------------- | ------- | -------------- | ------------------------------------------- | --- |
| switch(config-if-vsf)# |         | no description |                                             |     |
| Command History        |         |                |                                             |     |
| Release                |         |                | Modification                                |     |
| 10.16.1000             |         |                | Commandintroducedon4100and6100Switchseries. |     |
| 10.10                  |         |                | Commandintroduced.                          |     |
| Command Information    |         |                |                                             |     |
| Platforms              | Command | context        | Authority                                   |     |
4100 config-if-vsf Administratorsorlocalusergroupmemberswithexecution
| 6100 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
6200
6300
interface
| interface <IFRANGE> |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
Description
EntersconfigurationcontextforoneormoreVSFlinkinterfaces.
VSFlinkinterfacescannotbeincludedinarangewithotherinterfaces.
| Parameter |     |     | Description                   |     |
| --------- | --- | --- | ----------------------------- | --- |
| <IFRANGE> |     |     | Poetidentifierrange.Required. |     |
Examples
Enteringconfigurationcontext:
| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
| Command History |           |       |     |     |
VSFcommands|49

| Release             |         |         | Modification                                |
| ------------------- | ------- | ------- | ------------------------------------------- |
| 10.16.1000          |         |         | Commandintroducedon4100and6100Switchseries. |
| 10.07orearlier      |         |         | --                                          |
| Command Information |         |         |                                             |
| Platforms           | Command | context | Authority                                   |
4100 config Administratorsorlocalusergroupmemberswithexecution
| 6100 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6200
6300
issu rollback-timer
| issu rollback-timer | [wait-time | <TIME>] |     |
| ------------------- | ---------- | ------- | --- |
Description
EnablestheISSUrollbacktimeronthesystem.Therollbacktimerautomaticallyrollsthesystembackto
theconfigurationandOSimageusedbeforestartingtheISSU,unlesstheupgradeisconfirmedwith
issu update-software confirm.Changingtherollback-timerwillnotaffectanactivetimerandwill
applyonthenextISSU.Tocanceltheactivetimer,confirmthepreviousISSUwithissu update-
| software confirm.Disabledbydefault. |     |     |     |
| ----------------------------------- | --- | --- | --- |
Thenoformofthiscommanddisablestherollbacktimeronthesystem.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<TIME> Specifieshowmanyminutesthesystemwillwaitforconfirmation
thatthelastISSUisacceptedbeforetriggeringasystemreboot
androllbacktothepreviousconfigurationandOSversion.This
changewillnotaffectanactivetimerandwillapplyonthenext
ISSU.Range:30-1440.
Examples
EnablingtheISSUrollbacktimer:
| switch(config)# | issu | rollback-timer |     |
| --------------- | ---- | -------------- | --- |
DisablingtheISSUrollbacktimer:
| switch(config)# | no  | issu rollback-timer |     |
| --------------- | --- | ------------------- | --- |
DisablingtheISSUrollbacktimeronthesystemwhileapreviousISSU'stimerisactive:
| switch(config)# | no  | issu rollback-timer |     |
| --------------- | --- | ------------------- | --- |
The ISSU rollback timer is active. This change will apply on the next ISSU
operation
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 50

To cancel the active timer, confirm the previous ISSU with 'issu update-software
confirm'
SettingtheISSUrollbacktimerwaittimeto80minutes:
| switch# issu | rollback-timer |     | wait-time | 80  |
| ------------ | -------------- | --- | --------- | --- |
SettingtheISSUrollbacktimerwaittimeto81minuteswhileapreviousISSU'stimerisactive:
| switch# issu | rollback-timer |     | wait-time | 81  |
| ------------ | -------------- | --- | --------- | --- |
The ISSU rollback timer is active. This change will apply on the next ISSU
operation
ResettingtheISSUrollbacktimerwaittimetodefault:
| switch(config)# | no  | issu rollback-timer |              | wait-time |
| --------------- | --- | ------------------- | ------------ | --------- |
| Command History |     |                     |              |           |
| Release         |     |                     | Modification |           |
10.11
Commandintroduced
| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
6300,except config Administratorsorlocalusergroupmemberswithexecution
| forS3L75A, |     |     | rightsforthiscommand. |     |
| ---------- | --- | --- | --------------------- | --- |
S3L76Aand
S3L77A
issu update-software
| issu update-software | [validate|confirm] |     |     |     |
| -------------------- | ------------------ | --- | --- | --- |
Description
InitiatesISSUtothealternatebootlocation.Theneweroperatingsystemimagemustbedownloadedto
thealternatebootlocationpriortorunningthiscommand.Additionally,thecurrentrunningoperating
systemversionmustmatchtheversionthatisstoredinthecurrentbootlocationorISSUwillnotbe
allowed.
Thisoperationisdisruptiveandwillresultinthemanagementinterfacebeingdisconnectedduringtheprocess.
StartinganISSUwillcausetherunningconfigurationtobesavedincaseanerrorisencounteredthat
requiresareboottorecovertheswitch.Inaddition,aspecialconfigurationcheckpointwillbestoredto
diskandisusedtorollbacktothepre-ISSUfirmware.DuringtheISSUprocessallmanagement
VSFcommands|51

methods (CLI, REST, WebUI) will be blocked from making configuration changes to the switch. The
configuration block is active from the time ISSU starts until the time ISSU switchover is complete. fter
the ISSU switchover is completed, switch configuration can resume.

Parameter

validate

confirm

Description

Runs all pre-ISSU validations without executing the actual
upgrade. The validation runs in the background, however its
results will be displayed in real time for approximately the next
three minutes . If the validation is not finished within that time
frame or if the display is aborted with Control+C or Control+Z, the
results can be queried using the show issu validation
command.

Confirms the software update and cancels the configured rollback
timer. If the rollback timer is configured then this command has
to be executed after an ISSU before the timer expires. Else, the
pre-ISSU checkpoint is copied to the startup configuration and the
system is rebooted to the image used before ISSU.
Note: To perform an intentional system rollback before the
timer expires, a manual downgrade must be executed
through the following steps:

1. Copy the pre-ISSU checkpoint to the startup configuration

using the copy checkpoint pre-issu-startup-config
startup-config command.

2. Boot to the previous image using the boot system

command.

Usage

Note the following points before running this command:

n The newer operating system image must be downloaded to the alternate boot location prior to

running this command.

n The current running operating system version must match the version that is stored in the current

boot location or ISSU will not be allowed.

n This operation is disruptive and will result in the management interface being disconnected during

the process.

n The running configuration will be stored in case an error is encountered that requires a reboot to

recover the switch.

n During the ISSU process all management methods (CLI, REST, WebUI) are blocked from making

configuration changes to the switch. The configuration changes are not allowed from the time ISSU
starts until ISSU switchover is complete. fter the ISSU switchover is completed, switch configuration
can resume.

n In case of ISSU, conductor gets transitioned to standby role without reboot.

n The stack topology must be a ring before initiating ISSU. ISSU is not supported in chain topologies

and the process is aborted if the ISSU is initiated.

n During the ISSU process, the show core-dump all, show tech all, and copy support-files

commands all may fail to run or display correct output.

Examples

Initiating an ISSU:

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

52

| switch#          | issu update-software |           |     |            |          |         |     |
| ---------------- | -------------------- | --------- | --- | ---------- | -------- | ------- | --- |
| This command     | will                 | perform   | an  | in-service | software | upgrade |     |
| using pre-staged |                      | secondary |     | operating  | system   | image   |     |
FL.10.13.1000M
| This will | save | the current |     | running | configuration |     |     |
| --------- | ---- | ----------- | --- | ------- | ------------- | --- | --- |
WARNING:
| The rollback | timer | is  | enabled | and | configured | to 30 | minutes. |
| ------------ | ----- | --- | ------- | --- | ---------- | ----- | -------- |
After the upgrade is done, execute "issu update-software confirm"
to confirm the new image works as expected. If the command is not
| entered,  | the system | will       | be  | rebooted | to the               | previous | version. |
| --------- | ---------- | ---------- | --- | -------- | -------------------- | -------- | -------- |
| Continue  | (y/n)?     | y          |     |          |                      |          |          |
| Starting  | in-service | software   |     | upgrade. |                      |          |          |
| Use "show | issu"      | to monitor |     | status   | and progress.        |          |          |
| Use "show | events     | -c issu"   | to  | view     | event notifications. |          |          |
InitiatinganISSU,butstoppingitwithoutconfirmingtheupgrade:
| switch(config)#  |      | issu update-software |     |            |          |         |     |
| ---------------- | ---- | -------------------- | --- | ---------- | -------- | ------- | --- |
| This command     | will | perform              | an  | in-service | software | upgrade |     |
| using pre-staged |      | secondary            |     | operating  | system   | image   |     |
FL.10.13.1000M
| This will | save | the current |     | running | configuration |     |     |
| --------- | ---- | ----------- | --- | ------- | ------------- | --- | --- |
WARNING:
| The rollback | timer | is  | enabled | and | configured | to 30 | minutes. |
| ------------ | ----- | --- | ------- | --- | ---------- | ----- | -------- |
After the upgrade is done, execute "issu update-software confirm"
to confirm the new image works as expected. If the command is not
| entered,   | the system | will    | be  | rebooted | to the     | previous | version. |
| ---------- | ---------- | ------- | --- | -------- | ---------- | -------- | -------- |
| Continue   | (y/n)?     | n       |     |          |            |          |          |
| In-service | software   | upgrade |     | aborted. | No changes | were     | made.    |
ConfirmingtheISSUconfigurationwhentherollbacktimerhasbeenconfiguredandstarted:
| switch# | issu update-software |     |     | confirm |     |     |     |
| ------- | -------------------- | --- | --- | ------- | --- | --- | --- |
The ISSU has been confirmed and the rollback timer has been cancelled.
ConfirmingtheISSUconfigurationwhentherollbacktimerhasnotstarted:
VSFcommands|53

| switch#     | issu update-software | confirm       |           |           |
| ----------- | -------------------- | ------------- | --------- | --------- |
| No rollback | timer has            | been started, | no action | was done. |
ExecutinganISSU"dryrun"whereallpre-ISSUvalidationsarerunwithoutexecutingtheactualupgrade:
| switch# | issu update-software | validate |     |     |
| ------- | -------------------- | -------- | --- | --- |
ISSU Validation
=======================
| Condition |     | Status |     |     |
| --------- | --- | ------ | --- | --- |
-----------------------------------------------------------
| Current        | Image Valid | ---       |     |     |
| -------------- | ----------- | --------- | --- | --- |
| Target Image   | Valid       | ---       |     |     |
| Target Version | Compatible  | ---       |     |     |
| Management     | Modules     | Ready --- |     |     |
| Line Modules   | Ready       | ---       |     |     |
| Features       | Ready       | ---       |     |     |
In Progress[/]
ExecutinganISSU"dryrun"whereallpre-ISSUvalidationsarerunandtheuserabortstheISSU
validationonscreendisplaywithoutuserconfirmation:
| switch# | issu update-software | validate |     |     |
| ------- | -------------------- | -------- | --- | --- |
ISSU Validation
=======================
| Condition |     | Status |     |     |
| --------- | --- | ------ | --- | --- |
-----------------------------------------------------------
| Current        | Image Valid | Pass      |     |     |
| -------------- | ----------- | --------- | --- | --- |
| Target Image   | Valid       | Pass      |     |     |
| Target Version | Compatible  | Failed    |     |     |
| Management     | Modules     | Ready --- |     |     |
| Line Modules   | Ready       | ---       |     |     |
| Features       | Ready       | ---       |     |     |
In Progress[\]
To view the validation progress and results, execute "show issu validation"
ExecutinganISSU"dryrun"whereallpre-ISSUvalidationsarerunwithoutexecutingtheactualupgrade
andthevalidationprogresshasfinishedsuccessfully:
| switch# | issu update-software | validate |     |     |
| ------- | -------------------- | -------- | --- | --- |
ISSU Validation
=======================
| Condition |     | Status |     |     |
| --------- | --- | ------ | --- | --- |
-----------------------------------------------------------
| Current      | Image Valid | Pass |     |     |
| ------------ | ----------- | ---- | --- | --- |
| Target Image | Valid       | Pass |     |     |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 54

| Target Version  | Compatible |           | Pass |     |
| --------------- | ---------- | --------- | ---- | --- |
| Management      | Modules    | Ready     | Pass |     |
| Line Modules    | Ready      |           | Pass |     |
| Features        | Ready      |           | Pass |     |
| ISSU Validation | has        | completed |      |     |
ExecutinganISSUvalidationwhileapreviousISSUisunconfirmed,i.e.therollbacktimerisstillrunning:
| switch# | issu update-software |     | validate |     |
| ------- | -------------------- | --- | -------- | --- |
The previous ISSU has not been confirmed. Please confirm it with
'issu update-software confirm' before starting a new ISSU or running a validation.
ExecutinganISSU"dryrun"whenthevalidationsaretakingmorethanthreeminutestocomplete,then
checkingtheresultofthevalidationafterwards:
| switch# | issu update-software |     | validate |     |
| ------- | -------------------- | --- | -------- | --- |
ISSU validation is taking longer than expected. Check the final result with 'show
issu validation'
| switch# | show issu validation |     |     |     |
| ------- | -------------------- | --- | --- | --- |
ISSU Validation
=======================
| Condition |     |     | Status |     |
| --------- | --- | --- | ------ | --- |
-----------------------------------------------------------
| Current        | Image Valid |       | Pass |     |
| -------------- | ----------- | ----- | ---- | --- |
| Target Image   | Valid       |       | Pass |     |
| Target Version | Compatible  |       | Pass |     |
| Management     | Modules     | Ready | Pass |     |
| Line Modules   | Ready       |       | Pass |     |
| Features       | Ready       |       | Pass |     |
FollowingexampleshowsISSUperformedwithchaintopology:
| switch#        | issu update-software |         |                                    |          |
| -------------- | -------------------- | ------- | ---------------------------------- | -------- |
| Stack topology | is not               | a ring. | ISSU upgrade                       | aborted. |
| Command        | History              |         |                                    |          |
| Release        |                      |         | Modification                       |          |
| 10.11          |                      |         | Validateandconfirmparametersadded. |          |
| 10.10          |                      |         | Commandintroduced.                 |          |
| Command        | Information          |         |                                    |          |
| Platforms      | Command              | context | Authority                          |          |
config
6300,except Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
VSFcommands|55

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
forS3L75A,
S3L76Aand
S3L77A
link
| link <LINK-ID>    | [<IFRANGE>][description |     | <DESCRIPTION>] |
| ----------------- | ----------------------- | --- | -------------- |
| no link <LINK-ID> | [<IFRANGE>][description |     | <DESCRIPTION>] |
Description
CreatesormodifiesaVSFlink.TheusercanspecifythephysicalinterfacesthatmakeuptheVSFlink.
OnceaninterfaceispartofaVSFlink,allexistingconfigurationontheinterfaceisremovedandthe
interfacewilloperateasaVSFinterface.AtleastoneinterfacemustbespecifiedforthecreationofaVSF
link.VSFinterfacescarryVSFtrafficandcanonlybeconnectedtootherVSFinterfaces.Beforeremoving
anindividualinterfacefromtheVSFlinkusingtheno vsf link <x> <interface>command,ensure
thattheinterfaceisadministrativelyshutdownatbothlocalandpeerends.
Interface(s)configuredwithMACseccannotbeaddedasVSFlinks.YouhavetoremovetheMACsecconfiguration
beforeaddinganinterfacetoaVSFlink.
Thenoformofthecommandcanbeusedtoremoveinterfacesfromalinkorremovethelink
completely.
Whenconfigurationisremovedfromalink,itmaycausethestacktosplit.
| Parameter |     |     | Description                  |
| --------- | --- | --- | ---------------------------- |
| <LINK-ID> |     |     | TheVSFlinknumber.Range:1to2. |
| <IFRANGE> |     |     | Theinterfaceidentifierrange. |
<DESCRIPTION>
Addsadescriptionforthelink.Range:1to64printableASCII
characters.
Examples
CreatingaVSFlinkcalledlink 1withaninterfacerangeof1/1/51andadescription,andaVSFlinkcalled
link 2withaninterfacerangeof1/1/52:
| switch(vsf-member-1)# |     | link 1 1/1/51 |     |
| --------------------- | --- | ------------- | --- |
switch(vsf-member-1)# link 1 description link 1 connected to member 2
| switch(vsf-member-1)# |          | link 2 1/1/52 |     |
| --------------------- | -------- | ------------- | --- |
| RemovingVSFlink       | 1andlink | 2completely:  |     |
| switch(vsf-member-1)# |          | no link 1     |     |
| switch(vsf-member-1)# |          | no link 2     |     |
Removinganassignedinterface1/1/51fromVSFlink 1:
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 56

| switch(vsf-member-1)# |     | no link | 1 1/1/51 |     |
| --------------------- | --- | ------- | -------- | --- |
AttemptingtoaddaninterfaceconfiguredwithMACsectoaVSFlink:
| switch(vsf-member-1)# |     | link 1 | 1/1/51 |     |
| --------------------- | --- | ------ | ------ | --- |
VSF link cannot be configured on an interface with MACsec policy enabled.
| Command History     |         |         |                                             |     |
| ------------------- | ------- | ------- | ------------------------------------------- | --- |
| Release             |         |         | Modification                                |     |
| 10.16.1000          |         |         | Commandintroducedon4100and6100Switchseries. |     |
| 10.10               |         |         | Addedthedescriptionparameter.               |     |
| 10.07orearlier      |         |         | --                                          |     |
| Command Information |         |         |                                             |     |
| Platforms           | Command | context | Authority                                   |     |
4100 vsf-member-<ID> Administratorsorlocalusergroupmemberswithexecution
| 6100 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
6200
6300
member
member <MEMBER-ID>
Description
ConnectstothespecifiedmemberinaVSFenvironment.
| Parameter   |     |     | Description  |     |
| ----------- | --- | --- | ------------ | --- |
| <MEMBER-ID> |     |     | VSFmemberID. |     |
n Rangefor4100idevices:1-4
n Rangefor6100devices:1-6
n Rangefor6200Fdevices:1-8.
n Rangefor6300devices:1-10.
Examples
VSFstackisformedwithtwomembers:
| switch# member      | 2          |           |                  |         |
| ------------------- | ---------- | --------- | ---------------- | ------- |
| admin@172.17.17.2's |            | password: |                  |         |
| Last login:         | 2019-09-30 | 11:42:17  | from the console |         |
| User "admin"        | has logged | in 1      | time in the past | 30 days |
VSFcommands|57

member-2#
Membertoself:
| switch# | member 1  |      |     |
| ------- | --------- | ---- | --- |
| Already | on member | id 1 |     |
VSFstackisnotformedandmembernotavailable:
| switch#        | member 2    |             |                                                    |
| -------------- | ----------- | ----------- | -------------------------------------------------- |
| No stack       | role for    | member id 2 |                                                    |
| Command        | History     |             |                                                    |
| Release        |             |             | Modification                                       |
| 10.16.1000     |             |             | Commandintroducedon4100and6100Switchseries.        |
| 10.07orearlier |             |             | --                                                 |
| Command        | Information |             |                                                    |
| Platforms      | Command     | context     | Authority                                          |
| 4100           |             |             | Administratorsorlocalusergroupmemberswithexecution |
Manager(#)
| 6100 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6200
6300
show issu
| show issu [brief|history|validation] |     |     |     |
| ------------------------------------ | --- | --- | --- |
Description
ShowsinformationaboutthecurrentstateofISSU.IfnoISSUiscurrentlyinprogress,thecommand
displaystheprogressdetailsofthelastISSU.
ThecommandwiththebriefparameterdisplaysashortsummaryoftheISSUstateandindicatesifthe
systemisreadytoacceptanISSUcommandandwhetherornotanISSUisinprogress.Ifthebrief
parameterisnotincluded,thenmoredetailsaboutaninprogressISSUorthelastISSUaredisplayed.
| Parameter |     |     | Description                              |
| --------- | --- | --- | ---------------------------------------- |
| brief     |     |     | ShowsashortsummaryoftheISSUstate.        |
| history   |     |     | ShowsdetailsofISSUsoftwareupdatehistory. |
validation ShowsinformationaboutthecurrentstateofanISSUvalidation.
Examples
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 58

ShowingdetailedISSUstatuswithanISSUinprogressforthefirsttime:
| switch# | show issu |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- |
ISSU Summary
============
| ISSU Status | : In Progress |     |     |     |     |
| ----------- | ------------- | --- | --- | --- | --- |
Current Version : FL.10.13.0005K Upgrade Version : FL.10.13.1000M
| Upgrade   | Image : secondary   |     | Start Date | : 2023-11-08 | 07:01:47 |
| --------- | ------------------- | --- | ---------- | ------------ | -------- |
| Last ISSU | Result: --          |     |            |              |          |
| Rollback  | timer : Not started |     |            |              |          |
ISSU Progress
=============
| Upgrade | Operation |     | Status | Start Date |     |
| ------- | --------- | --- | ------ | ---------- | --- |
------------------------------------------------------------------------
| Initiate      | ISSU                 |         | Complete    | 2023-11-08 | 07:01:47 |
| ------------- | -------------------- | ------- | ----------- | ---------- | -------- |
| Validate      | System Readiness     |         | In Progress | 2023-11-08 | 07:01:47 |
| Upgrade       | Standby and Member   | Modules | Pending     | --         |          |
| Upgrade       | Line Module Services |         | Pending     | --         |          |
| Prepare       | for Switchover       |         | Pending     | --         |          |
| Finalize      | Upgrade              |         | Pending     | --         |          |
| ISSU Complete |                      |         | Pending     | --         |          |
ShowingdetailedstatusforVSFISSU:
| switch# | show issu |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- |
ISSU Summary
============
| ISSU Status | : In Progress |     |     |     |     |
| ----------- | ------------- | --- | --- | --- | --- |
Current Version : FL.10.11.0001 Upgrade Version : FL.10.11.1000BD
| Upgrade   | Image : secondary   |     | Start Date | : 2023-02-02 | 14:22:31 |
| --------- | ------------------- | --- | ---------- | ------------ | -------- |
| Last ISSU | Result: --          |     |            |              |          |
| Rollback  | timer : Not started |     |            |              |          |
ISSU Progress
=============
| Upgrade | Operation |     | Status | Start Date |     |
| ------- | --------- | --- | ------ | ---------- | --- |
------------------------------------------------------------------------
| Initiate | ISSU             |     | Complete | 2023-02-02 | 14:22:31 |
| -------- | ---------------- | --- | -------- | ---------- | -------- |
| Validate | System Readiness |     | Complete | 2023-02-02 | 14:22:31 |
Upgrade Standby and Member Modules In Progress 2023-02-02 14:22:54
| Upgrade       | Line Module Services |     | Pending | --  |     |
| ------------- | -------------------- | --- | ------- | --- | --- |
| Prepare       | for Switchover       |     | Pending | --  |     |
| Finalize      | Upgrade              |     | Pending | --  |     |
| ISSU Complete |                      |     | Pending | --  |     |
ShowingdetailedISSUstatuswithISSUinprogressaftersuccessfullycompletingapreviousISSU:
| switch# | show issu |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- |
ISSU Summary
===========
| ISSU Status | : In progress |     |     |     |     |
| ----------- | ------------- | --- | --- | --- | --- |
Current Version : FL.10.10.0001 Upgrade Version : FL.10.10.0002
| Upgrade   | Image : secondary |          | Start Date | : 2021-10-15 | 08:37:49 |
| --------- | ----------------- | -------- | ---------- | ------------ | -------- |
| Last ISSU | Result: Completed | (Without | errors)    |              |          |
ISSU Progress
=============
| Upgrade | Operation |     | Status | Start Date |     |
| ------- | --------- | --- | ------ | ---------- | --- |
VSFcommands|59

------------------------------------------------------------------------
| Initiate | ISSU             |     | Complete | 2021-10-13 | 23:05:41 |
| -------- | ---------------- | --- | -------- | ---------- | -------- |
| Validate | System Readiness |     | Complete | 2021-10-13 | 23:05:41 |
Upgrade Standby Management Module Complete 2021-10-13 23:05:41
| Upgrade       | Line Modules   |     | In Progress | 2021-10-13 | 23:07:07 |
| ------------- | -------------- | --- | ----------- | ---------- | -------- |
| Prepare       | for Switchover |     | Pending     | --         |          |
| Finalize      | Upgrade        |     | Pending     | --         |          |
| ISSU Complete |                |     | Pending     | --         |          |
ShowingdetailedISSUstatuswithISSUinprogressafterabortingthepreviousISSU:
| switch# | show issu |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- |
ISSU Summary
===========
| ISSU Status | :   | In progress |     |     |     |
| ----------- | --- | ----------- | --- | --- | --- |
Current Version : FL.10.10.0001 Upgrade Version : FL.10.10.0002
| Upgrade | Image : | secondary | Start Date | : 2021-10-15 | 08:37:49 |
| ------- | ------- | --------- | ---------- | ------------ | -------- |
Last ISSU Result: Aborted (One or more line modules are not ready to start ISSU)
ISSU Progress
=============
| Upgrade | Operation |     | Status | Start Date |     |
| ------- | --------- | --- | ------ | ---------- | --- |
------------------------------------------------------------------------
| Initiate | ISSU             |     | Complete | 2021-10-13 | 23:05:41 |
| -------- | ---------------- | --- | -------- | ---------- | -------- |
| Validate | System Readiness |     | Complete | 2021-10-13 | 23:05:41 |
Upgrade Standby Management Module Complete 2021-10-13 23:05:41
| Upgrade       | Line Modules   |     | In Progress | 2021-10-13 | 23:07:07 |
| ------------- | -------------- | --- | ----------- | ---------- | -------- |
| Prepare       | for Switchover |     | Pending     | --         |          |
| Finalize      | Upgrade        |     | Pending     | --         |          |
| ISSU Complete |                |     | Pending     | --         |          |
ShowingdetailedISSUstatuswithnoISSUinprogressandnopreviousISSUperformed:
switch#
show issu
ISSU Summary
===========
| ISSU Status | :         | Ready         |                 |      |     |
| ----------- | --------- | ------------- | --------------- | ---- | --- |
| Current     | Version : | FL.10.10.0001 | Upgrade Version | : -- |     |
| Upgrade     | Image :   | --            | Start Date      | : -- |     |
| Last ISSU   | Result:   | -- (--)       |                 |      |     |
ISSU Progress
=============
| Upgrade | Operation |     | Status | Start Date |     |
| ------- | --------- | --- | ------ | ---------- | --- |
------------------------------------------------------------------------
| Initiate      | ISSU               |        | --  | --  |     |
| ------------- | ------------------ | ------ | --- | --- | --- |
| Validate      | System Readiness   |        | --  | --  |     |
| Upgrade       | Standby Management | Module | --  | --  |     |
| Upgrade       | Line Modules       |        | --  | --  |     |
| Prepare       | for Switchover     |        | --  | --  |     |
| Perform       | Switchover         |        | --  | --  |     |
| Finalize      | Upgrade            |        | --  | --  |     |
| ISSU Complete |                    |        | --  | --  |     |
ShowingdetailedISSUstatusaftercompletionandbeforesystemisreadytostartanewISSU:
| switch# | show issu |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- |
ISSU Summary
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 60

===========
| ISSU Status |         | : Not ready     |          |                 |      |     |
| ----------- | ------- | --------------- | -------- | --------------- | ---- | --- |
| Current     | Version | : FL.10.10.0001 |          | Upgrade Version | : -- |     |
| Upgrade     | Image   | : --            |          | Start Date      | : -- |     |
| Last ISSU   | Result: | Completed       | (Without | errors)         |      |     |
ISSU Progress
=============
| Upgrade | Operation |     |     | Status | Start Date |     |
| ------- | --------- | --- | --- | ------ | ---------- | --- |
------------------------------------------------------------------------
| Initiate | ISSU   |           |     | Complete | 2021-10-13 | 23:05:41 |
| -------- | ------ | --------- | --- | -------- | ---------- | -------- |
| Validate | System | Readiness |     | Complete | 2021-10-13 | 23:05:41 |
Upgrade Standby Management Module Complete 2021-10-13 23:05:41
| Upgrade       | Line           | Modules |     | Complete | 2021-10-13 | 23:07:07 |
| ------------- | -------------- | ------- | --- | -------- | ---------- | -------- |
| Prepare       | for Switchover |         |     | Complete | 2021-10-13 | 23:07:50 |
| Finalize      | Upgrade        |         |     | Complete | 2021-10-13 | 23:07:53 |
| ISSU Complete |                |         |     | Complete | 2021-10-13 | 23:08:10 |
ShowingdetailedISSUstatusafteranerroroccurredandtheprocessisaborted:
| switch# | show | issu |     |     |     |     |
| ------- | ---- | ---- | --- | --- | --- | --- |
ISSU Summary
============
| ISSU Status |     | : Aborted |     |     |     |     |
| ----------- | --- | --------- | --- | --- | --- | --- |
Current Version : FL.10.10.0001 Upgrade Version : FL.10.10.0002
| Upgrade   | Image   | : secondary |         | Start Date        | : 2021-12-09 | 19:17:15 |
| --------- | ------- | ----------- | ------- | ----------------- | ------------ | -------- |
| Last ISSU | Result: | Aborted     | (System | failed to prepare | for ISSU)    |          |
ISSU Progress
=============
| Upgrade | Operation |     |     | Status | Start Date |     |
| ------- | --------- | --- | --- | ------ | ---------- | --- |
------------------------------------------------------------------------
| Initiate | ISSU   |           |     | Complete | 2021-12-09 | 19:17:15 |
| -------- | ------ | --------- | --- | -------- | ---------- | -------- |
| Validate | System | Readiness |     | Complete | 2021-12-09 | 19:17:15 |
Upgrade Standby Management Module Complete 2021-12-09 19:17:15
| Upgrade       | Line           | Modules |     | Error   | 2021-12-09 | 19:19:22 |
| ------------- | -------------- | ------- | --- | ------- | ---------- | -------- |
| Prepare       | for Switchover |         |     | Aborted | --         |          |
| Finalize      | Upgrade        |         |     | Aborted | --         |          |
| ISSU Complete |                |         |     | Aborted | --         |          |
ShowingsummaryofISSUstatuswithnoISSUinprogresswheresystemisreadytostartanewISSU
andwithnopreviousISSUperformed:
| switch# | show | issu brief |     |     |     |     |
| ------- | ---- | ---------- | --- | --- | --- | --- |
ISSU Summary
===========
| ISSU Status |         | : Ready         |     |                 |      |     |
| ----------- | ------- | --------------- | --- | --------------- | ---- | --- |
| Current     | Version | : FL.10.10.0001 |     | Upgrade Version | : -- |     |
| Upgrade     | Image   | : --            |     | Start Date      | : -- |     |
| Last ISSU   | Result: | -- (--)         |     |                 |      |     |
ShowingsummaryofISSUstatuswithnoISSUinprogresswheresystemisreadytostartanewISSU
andaftersuccessfullycompletingapreviousISSU:
| switch# | show | issu brief |     |     |     |     |
| ------- | ---- | ---------- | --- | --- | --- | --- |
ISSU Summary
===========
VSFcommands|61

| ISSU Status | : Ready                 |          |                 |      |     |
| ----------- | ----------------------- | -------- | --------------- | ---- | --- |
| Current     | Version : FL.10.10.0001 |          | Upgrade Version | : -- |     |
| Upgrade     | Image : --              |          | Start Date      | : -- |     |
| Last ISSU   | Result: Completed       | (Without | errors)         |      |     |
ShowingasummaryofISSUstatuswithnoISSUinprogresswheresystemisreadytostartanewISSU
amdafterabortingthepreviousISSU:
| switch# | show issu brief |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- |
ISSU Summary
===========
| ISSU Status | : Ready                 |     |                 |      |     |
| ----------- | ----------------------- | --- | --------------- | ---- | --- |
| Current     | Version : FL.10.10.0001 |     | Upgrade Version | : -- |     |
| Upgrade     | Image : --              |     | Start Date      | : -- |     |
Last ISSU Result: Aborted (One or more line modules are not ready to start ISSU)
ShowingasummaryofISSUstatuswithISSUinprogress:
| switch# | show issu brief |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- |
ISSU Summary
===========
| ISSU Status | : In progress |     |     |     |     |
| ----------- | ------------- | --- | --- | --- | --- |
Current Version : FL.10.10.0001 Upgrade Version : FL.10.10.0002
| Upgrade   | Image : secondary |          | Start Date | : 2021-10-15 | 08:37:49 |
| --------- | ----------------- | -------- | ---------- | ------------ | -------- |
| Last ISSU | Result: Completed | (Without | errors)    |              |          |
ShowingasummaryofISSUstatuswithnoISSUinprogresswherethesystemisnotreadytostarta
newISSU:
| switch# | show issu brief |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- |
ISSU Summary
===========
| ISSU Status | : Not ready |     |     |     |     |
| ----------- | ----------- | --- | --- | --- | --- |
Current Version : FL.10.10.0001 Upgrade Version : FL.10.10.0002
| Upgrade   | Image : secondary |          | Start Date | : 2021-10-15 | 08:37:49 |
| --------- | ----------------- | -------- | ---------- | ------------ | -------- |
| Last ISSU | Result: Completed | (Without | errors)    |              |          |
ShowingsummaryofISSUstatusafteranerroroccurredandtheprocessisaborted:
| switch# | show issu brief |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- |
ISSU Summary
============
| ISSU Status | : Aborted |     |     |     |     |
| ----------- | --------- | --- | --- | --- | --- |
Current Version : FL.10.10.0001 Upgrade Version : FL.10.10.0002
| Upgrade   | Image : secondary |         | Start Date        | : 2021-12-09 | 19:17:15 |
| --------- | ----------------- | ------- | ----------------- | ------------ | -------- |
| Last ISSU | Result: Aborted   | (System | failed to prepare | for ISSU)    |          |
ShowingISSUvalidationstatuspercondition/validation:
| switch# | show issu validation |     |     |     |     |
| ------- | -------------------- | --- | --- | --- | --- |
ISSU Validation
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 62

=======================
| Condition |     |     | Status |     |
| --------- | --- | --- | ------ | --- |
-----------------------------------------------------------
| Current        | Image Valid   |     | --- |     |
| -------------- | ------------- | --- | --- | --- |
| Target Image   | Valid         |     | --- |     |
| Target Version | Compatible    |     | --- |     |
| Management     | Modules Ready |     | --- |     |
| Line Modules   | Ready         |     | --- |     |
| Features       | Ready         |     | --- |     |
ShowingISSUhistory:
| switch#    | show issu history       |         |                                  |           |
| ---------- | ----------------------- | ------- | -------------------------------- | --------- |
| Upgrade:   | 1                       |         |                                  |           |
| From       | Version : FL.10.11.0001 |         |                                  |           |
| To Version | : FL.10.11.1000         |         |                                  |           |
| Start      | Time : 2022-09-14       |         | 15:37:33                         |           |
| End Time   | : 2022-09-14            |         | 15:40:45                         |           |
| Status     | : Completed             |         |                                  |           |
| Command    | History                 |         |                                  |           |
| Release    |                         |         | Modification                     |           |
| 10.11.1000 |                         |         | Historyparameterintroduced.      |           |
| 10.11      |                         |         | Supportfor6300SwitchSeriesadded. |           |
| 10.10      |                         |         | Commandintroduced                |           |
| Command    | Information             |         |                                  |           |
| Platforms  |                         | Command | context                          | Authority |
6300,exceptforS3L75A, Manager(#) Administratorsorlocalusergroupmemberswith
| S3L76AandS3L77A |     |     |     | executionrightsforthiscommand. |
| --------------- | --- | --- | --- | ------------------------------ |
show vsf
show vsf
Description
DisplaystheinformationabouttheconfigurationandstatusofaVSFstackanditsmembers.
Example
ShowingtheinformationabouttheconfigurationandstatusofaVSFstackanditsmembers.
AppliesonlytoHPEArubaNetworking4100i,6100Switchseries.
| switch#        | show vsf |     |           |     |
| -------------- | -------- | --- | --------- | --- |
| Force Autojoin |          |     | : Enabled |     |
VSFcommands|63

| Autojoin Eligibility |        | Status: | Eligible            |       |        |
| -------------------- | ------ | ------- | ------------------- | ----- | ------ |
| MAC Address          |        |         | : 90:20:c2:05:30:c0 |       |        |
| Secondary            |        |         | : 2                 |       |        |
| Topology             |        |         | : Chain             |       |        |
| Status               |        |         | : No                | Split |        |
| Split Detection      | Method |         | : vlan              |       |        |
| Split Detection      | VlAN   |         | : 10                |       |        |
| Mbr Mac Address      |        |         | type                |       | Status |
ID
| --- ------------------- |     |     | -------------- |     | --------------- |
| ----------------------- | --- | --- | -------------- | --- | --------------- |
| 1 90:20:c2:05:30:c0     |     |     | JL675A         |     | Conductor       |
| 2 90:20:c2:06:30:40     |     |     | JL676A         |     | Standby         |
ShowingtheinformationabouttheconfigurationandstatusofaVSFstackanditsmembers:
(AppliesonlytoHPEArubaNetworking6200,6300and6300LSwitchSeries)
| switch# show         | vsf    |         |                     |          |          |
| -------------------- | ------ | ------- | ------------------- | -------- | -------- |
| Force Autojoin       |        |         | : Disabled          |          |          |
| Autojoin Eligibility |        | Status: | Not                 | Eligible |          |
| MAC Address          |        |         | : 08:97:34:b0:0e:00 |          |          |
| Egress Shape         |        |         | : Enabled           |          |          |
| Egress Shape         | Rate   |         | : 10000000          |          | kbps     |
| Secondary            |        |         | : 2                 |          |          |
| Topology             |        |         | : Chain             |          |          |
| Status               |        |         | : Active            |          | Fragment |
| Split Detection      | Method |         | : mgmt              |          |          |
| Mbr Mac Address      |        |         | type                |          | Status   |
ID
| --- ------------------- |     |     | -------------- |     | ---------------   |
| ----------------------- | --- | --- | -------------- | --- | ----------------- |
| 1 08:97:34:b0:0e:00     |     |     | JL666A         |     | Conductor         |
| 2 08:97:34:b1:43:00     |     |     | JL665A         |     | In Other Fragment |
| 3 08:97:34:b7:cc:00     |     |     | S0E91A         |     | Member            |
| 4                       |     |     | JL662A         |     | Not Present       |
ShowingtheinformationabouttheconfigurationandstatusofaVSFstackanditsstackmembers(with
S0E91AorS0X44ASKUmember):
(AppliesonlytoHPEArubaNetworking6300SwitchSeries)
| switch# show         | vsf    |         |                     |          |        |
| -------------------- | ------ | ------- | ------------------- | -------- | ------ |
| Force Autojoin       |        |         | : Disabled          |          |        |
| Autojoin Eligibility |        | Status: | Not                 | Eligible |        |
| MAC Address          |        |         | : 08:97:34:b0:0e:00 |          |        |
| Egress Shape         |        |         | : Enabled           |          |        |
| Egress Shape         | Rate   |         | : 10000000          |          | kbps   |
| Secondary            |        |         | : 2                 |          |        |
| Topology             |        |         | : Chain             |          |        |
| Status               |        |         | : No                | Split    |        |
| Split Detection      | Method |         | : None              |          |        |
| Mbr MAC Address      |        |         | Type                |          | Status |
ID
| --- ------------------- |     |     | -------------- |     | ----------------- |
| ----------------------- | --- | --- | -------------- | --- | ----------------- |
| 1 08:97:34:b0:0e:00     |     |     | JL666A         |     | Conductor         |
| 2 08:97:34:b1:43:00     |     |     | JL665A         |     | Standby           |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 64

| 3 08:97:34:b7:cc:00 |     |     | SOE91A |     | Member      |
| ------------------- | --- | --- | ------ | --- | ----------- |
| 4                   |     |     | JL662A |     | Not Present |
ShowingtheinformationabouttheconfigurationandstatusofaVSFstackanditsstackmemberswith
egressshaperateispopulatedwithNot Appliedindicatingthatportshapingfailedtoapplyononeor
moreactiveVSFinterfaces:
(AppliesonlytoHPEArubaNetworking6300SwitchSeries)
switch#
show vsf
| Force Autojoin  |             |         | : Disabled          |          |        |
| --------------- | ----------- | ------- | ------------------- | -------- | ------ |
| Autojoin        | Eligibility | Status: | Not                 | Eligible |        |
| MAC Address     |             |         | : 08:97:34:b0:0e:00 |          |        |
| Egress Shape    |             |         | : Enabled           |          |        |
| Egress Shape    | Rate        |         | : Not               | Applied  |        |
| Secondary       |             |         | : 2                 |          |        |
| Topology        |             |         | : Chain             |          |        |
| Status          |             |         | : No                | Split    |        |
| Split Detection | Method      |         | : None              |          |        |
| Mbr MAC Address |             |         | Type                |          | Status |
ID
| --- ------------------- |     |     | -------------- |     | ----------------- |
| ----------------------- | --- | --- | -------------- | --- | ----------------- |
| 1 08:97:34:b0:0e:00     |     |     | JL666A         |     | Conductor         |
| 2 08:97:34:b1:43:00     |     |     | JL665A         |     | Standby           |
| 3 08:97:34:b7:cc:00     |     |     | SOE91A         |     | Member            |
TheEgressShapedisplaysthestatusofVSFportshaping(Enabled/Disabled).TheEgressShapeRatedisplays
theoperationalspeedofthestackwhentheVSFportshapingisapplied.Anerrormessageisdisplayedifport
shapingfailstoapplytotheinterface.ThepurposeoftheVSF portshapingfeatureistoensurethatall
VSF interfaceoperateatalowestcommonportspeedacrossthestack.ThisfeatureissupportedonlyintheHPE
ArubaNetworking6300Switchseries.
ShowingVSFinformationwhentheportspeedhasbeenmodifiedona4100ior6100Switchseries
| usingthevsf port-speedcommand: |             |         |                     |          |        |
| ------------------------------ | ----------- | ------- | ------------------- | -------- | ------ |
| 6100# show                     | vsf         |         |                     |          |        |
| Force Autojoin                 |             |         | : Disabled          |          |        |
| Autojoin                       | Eligibility | Status: | Not                 | Eligible |        |
| MAC Address                    |             |         | : 90:20:c2:05:30:c0 |          |        |
| Operational                    | Port Speed  |         | : 1G                |          |        |
| Secondary                      |             |         | : 2                 |          |        |
| Topology                       |             |         | : Chain             |          |        |
| Status                         |             |         | : No                | Split    |        |
| Split Detection                | Method      |         | : vlan              |          |        |
| Split Detection                | VLAN        |         | : 100               |          |        |
| Mbr Mac Address                |             |         | type                |          | Status |
ID
| --- ------------------- |     |            | -------------- |     | --------------- |
| ----------------------- | --- | ---------- | -------------- | --- | --------------- |
| 1 90:20:c2:05:30:c0     |     |            | JL675A         |     | Conductor       |
| 2 90:20:c2:06:30:40     |     |            | JL676A         |     |                 |
| 6100(config)#           | vsf | port-speed | 10g            |     |                 |
This command will reboot the stack and reset the VSF port speed to configured
VSFcommands|65

value
| Do you want     | to continue |         | (y/n)?              | y        |        |
| --------------- | ----------- | ------- | ------------------- | -------- | ------ |
| 6100# show      | vsf         |         |                     |          |        |
| Force Autojoin  |             |         | : Disabled          |          |        |
| Autojoin        | Eligibility | Status: | Not                 | Eligible |        |
| MAC Address     |             |         | : 90:20:c2:05:30:c0 |          |        |
| Operational     | Port Speed  |         | : 10G               |          |        |
| Secondary       |             |         | : 2                 |          |        |
| Topology        |             |         | : Chain             |          |        |
| Status          |             |         | : No                | Split    |        |
| Split Detection | Method      |         | : vlan              |          |        |
| Split Detection | VLAN        |         | : 100               |          |        |
| Mbr Mac Address |             |         | type                |          | Status |
ID
| --- ------------------- |     |     | -------------- |                                                      | --------------- |
| ----------------------- | --- | --- | -------------- | ---------------------------------------------------- | --------------- |
| 1 90:20:c2:05:30:c0     |     |     | JL675A         |                                                      | Conductor       |
| 2 90:20:c2:06:30:40     |     |     | JL676A         |                                                      | Standby         |
| Command History         |     |     |                |                                                      |                 |
| Release                 |     |     |                | Modification                                         |                 |
| 10.16.1000              |     |     |                | Commandintroducedon4100and6100Switchseries.          |                 |
| 10.15                   |     |     |                | CommandupdatedtodisplayEgressShape.Applicableonlyfor |                 |
6300SwitchSeries.
10.13.1000 CommandupdatedtodisplayEgressShapeRate.Applicableonly
for6300SwitchSeries.
| 10.07orearlier      |            |         |     | --        |     |
| ------------------- | ---------- | ------- | --- | --------- | --- |
| Command Information |            |         |     |           |     |
| Platforms           | Command    | context |     | Authority |     |
| 4100                | Manager(#) |         |     |           |     |
6100
6200
6300
| show vsf | detail |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- |
show vsf detail
Description
DisplaysdetailedinformationrelatedtothecurrentstateoftheVSFstackandthestackmembers.
Example
Theoutputbelowshowsexampleinformationfora6300Switchseries.Theinformationinthetypeand
fieldswillvary,dependingupontheindividualswitchmodeltype.
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 66

| switch# show vsf | detail |     |     |     |
| ---------------- | ------ | --- | --- | --- |
VSF Stack
| MAC Address            |         | : ec:eb:b8:d0:80:40   |                  |           |
| ---------------------- | ------- | --------------------- | ---------------- | --------- |
| Egress Shape           |         | : Enabled             |                  |           |
| Egress Shape           | Rate    | : Not Applied         |                  |           |
| Secondary              |         | : 2                   |                  |           |
| Topology               |         | : Chain               |                  |           |
| Status                 |         | : No Split            |                  |           |
| Uptime                 |         | : 0d 0h 23m           |                  |           |
| Split Detection        | Method  | : None                |                  |           |
| Software Version       |         | : SL.10.02.0000-7755  |                  |           |
| Force Autojoin         |         | : Disabled            |                  |           |
| Autojoin Eligibility   | Status  | : Not Eligible        |                  |           |
| Autojoin Ineligibility | Reason: | Configuration         | changes detected |           |
| Name                   |         | : HPE-ANW-VSF-<model> |                  |           |
| Contact                |         | :                     |                  |           |
| Location               |         | :                     |                  |           |
| Member ID              |         | : 1                   |                  |           |
| MAC Address            |         | : ec:eb:b8:d0:80:40   |                  |           |
| Type                   |         | : <part number>       |                  |           |
| Model                  |         | : <model>             |                  |           |
| Status                 |         | : Conductor           |                  |           |
| ROM Version            |         | : SL.10.02.0000-7755  |                  |           |
| Serial Number          |         | : CN7ZK90012          |                  |           |
| Uptime                 |         | : 0d 0h 23m           |                  |           |
| CPU Utilization        |         | : 0%                  |                  |           |
| Memory Utilization     |         | : 20%                 |                  |           |
| VSF link 1             |         | : Up, connected       | to peer member   | 2, link 1 |
| VSF link 2             |         | : Down                |                  |           |
| Member ID              |         | : 2                   |                  |           |
| MAC Address            |         | : eb:ec:d8:e0:50:60   |                  |           |
| Type                   |         | : <part number>       |                  |           |
| Model                  |         | : <model>             |                  |           |
| Status                 |         | : Standby             |                  |           |
| ROM Version            |         | : SL.10.02.0000-7755  |                  |           |
| Serial Number          |         | : CN7ZK90012          |                  |           |
| Uptime                 |         | : 0d 0h 23m           |                  |           |
| CPU Utilization        |         | : 0%                  |                  |           |
| Memory Utilization     |         | : 15%                 |                  |           |
| VSF link 1             |         | : Up, connected       | to peer member   | 1, link 1 |
| VSF link 2             |         | : Down                |                  |           |
| Member ID              |         | : 3                   |                  |           |
| MAC Address            |         | :                     |                  |           |
| Type                   |         | : <part number>       |                  |           |
| Model                  |         | : <model>             |                  |           |
| Status                 |         | : Not Present         |                  |           |
| ROM Version            |         | :                     |                  |           |
| Serial Number          |         | :                     |                  |           |
| Uptime                 |         | :                     |                  |           |
| CPU Utilization        |         | :                     |                  |           |
| Memory Utilization     |         | :                     |                  |           |
| VSF link 1             |         | :                     |                  |           |
| VSF link 2             |         | :                     |                  |           |
Theoutputbelowshowsexampleinformationfora4100,6100or6200Switchseries.Theinformation
inthetypeandfieldswillvary,dependingupontheindividualswitchmodeltype.
VSFcommands|67

| switch(config)# |             | show        | vsf     |                     |          |        |     |
| --------------- | ----------- | ----------- | ------- | ------------------- | -------- | ------ | --- |
| Force           | Autojoin    |             |         | : Disabled          |          |        |     |
| Autojoin        |             | Eligibility | Status: | Not                 | Eligible |        |     |
| MAC             | Address     |             |         | : bc:d7:a5:03:39:c0 |          |        |     |
| Secondary       |             |             |         | :                   |          |        |     |
| Topology        |             |             |         | : Standalone        |          |        |     |
| Status          |             |             |         | : No                | Split    |        |     |
| Split           | Detection   | Method      |         | : None              |          |        |     |
| Mbr             | Mac Address |             |         | type                |          | Status |     |
ID
| ---             | ------------------- |               |        | ------------------ |                       | --------------- |          |
| --------------- | ------------------- | ------------- | ------ | ------------------ | --------------------- | --------------- | -------- |
| 1               | bc:c7:a5:23:39:c0   |               |        | <part              | number>               | Conductor       |          |
| switch(config)# |                     | show          | vsf    | detail             |                       |                 |          |
|                 | VSF                 | Stack         |        |                    |                       |                 |          |
|                 | MAC                 | Address       |        |                    | : bc:d7:a5:03:39:c0   |                 |          |
|                 | Secondary           |               |        |                    | :                     |                 |          |
|                 | Topology            |               |        |                    | : standalone          |                 |          |
|                 | Status              |               |        |                    | : No Split            |                 |          |
|                 | Split               | Detection     | Method |                    | : None                |                 |          |
|                 | Software            | Version       |        |                    | : RL.10.16.1000G      |                 |          |
|                 | Force               | Autojoin      |        |                    | : Disabled            |                 |          |
|                 | Autojoin            | Eligibility   |        | Status             | : Not Eligible        |                 |          |
|                 | Autojoin            | Ineligibility |        | Reason:            | Configuration         | changes         | detected |
|                 | Name                |               |        |                    | : HPE-ANW-VSF-<model> |                 |          |
|                 | Contact             |               |        |                    | :                     |                 |          |
Location
| Member         | ID          |             |         |     | : 1                                         |        |                     |
| -------------- | ----------- | ----------- | ------- | --- | ------------------------------------------- | ------ | ------------------- |
|                | MAC         | Address     |         |     | : bc:c7:a5:23:39:c0                         |        |                     |
|                | Type        |             |         |     | : <part                                     | number |                     |
|                | Model       |             |         |     | : <model>                                   |        |                     |
|                | Status      |             |         |     | : Conductor                                 |        |                     |
|                | ROM         | Version     |         |     | : <XX>.01.17.0001                           |        |                     |
|                | Serial      | Number      |         |     | : TW42KYC01D                                |        |                     |
|                | Uptime      |             |         |     | : 10 weeks,                                 | 1 day, | 23 hours, 9 minutes |
|                | CPU         | Utilization |         |     | : 5%                                        |        |                     |
|                | Memory      | Utilization |         |     | : 11%                                       |        |                     |
|                | VSF         | Link 1      |         |     | :                                           |        |                     |
|                | VSF         | Link 2      |         |     | :                                           |        |                     |
| Command        | History     |             |         |     |                                             |        |                     |
| Release        |             |             |         |     | Modification                                |        |                     |
| 10.16.1000     |             |             |         |     | Commandintroducedon4100and6100Switchseries. |        |                     |
| 10.07orearlier |             |             |         |     | --                                          |        |                     |
| Command        | Information |             |         |     |                                             |        |                     |
| Platforms      |             | Command     | context |     | Authority                                   |        |                     |
4100
Manager(#)
6100
6200
6300
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 68

| show vsf        | member      |     |     |
| --------------- | ----------- | --- | --- |
| show vsf member | <MEMBER-ID> |     |     |
Description
DisplaysinformationaboutthespecifiedVSFmember.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<MEMBER-ID>
VSFmemberID.
n Rangefor4100idevices:1-4
n Rangefor6100devices:1-6
n Rangefor6200Fdevices:1-8.
n Rangefor6300devices:1-10.
Example
| switch# show        | vsf member  | 1                      |                                             |
| ------------------- | ----------- | ---------------------- | ------------------------------------------- |
| Member ID           |             | : 1                    |                                             |
| MAC Address         |             | : ec:eb:b8:d0:80:40    |                                             |
| Type                |             | : <part number>        |                                             |
| Model               |             | : <model>              |                                             |
| Status              |             | : Conductor            |                                             |
| ROM Version         |             | : <xx>.10.02.0000-7755 |                                             |
| Serial              | Number      | : CN7ZK903012          |                                             |
| Uptime              |             | : 0d 0h 18m            |                                             |
| CPU Utilization     |             | : 0%                   |                                             |
| Memory              | Utilization | : 15%                  |                                             |
| VSF link            | 1           | : Down                 |                                             |
| VSF link            | 2           | : Down                 |                                             |
| Command History     |             |                        |                                             |
| Release             |             |                        | Modification                                |
| 10.16.1000          |             |                        | Commandintroducedon4100and6100Switchseries. |
| 10.07orearlier      |             |                        | --                                          |
| Command Information |             |                        |                                             |
| Platforms           | Command     | context                | Authority                                   |
| 4100                | Manager(#)  |                        |                                             |
6100
6200
6300
| show vsf | link |     |     |
| -------- | ---- | --- | --- |
show vsf link
Description
VSFcommands|69

DisplaystheVSFlinkstateforeachmember.
Example
| switch# show        | vsf link   |         |                                             |
| ------------------- | ---------- | ------- | ------------------------------------------- |
| VSF Member          | 1          |         |                                             |
| Link                | Peer       | Peer    |                                             |
| Link State          | Member     | Link    | Interfaces                                  |
| ---- ----------     | -------    | ------  | ---------------------------                 |
| 1 up                | 2          | 1       | 1/1/50                                      |
| 2 up                | 10         | 2       | 1/1/49                                      |
| VSF Member          | 2          |         |                                             |
| Link                | Peer       | Peer    |                                             |
| Link State          | Member     | Link    | Interfaces                                  |
| ---- ----------     | -------    | ------  | ---------------------------                 |
| 1 up                | 1          | 1       | 2/1/49                                      |
| 2 up                | 3          | 1       | 2/1/50                                      |
| VSF Member          | 3          |         |                                             |
| Link                | Peer       | Peer    |                                             |
| Link State          | Member     | Link    | Interfaces                                  |
| ---- ----------     | -------    | ------  | ---------------------------                 |
| 1 up                | 2          | 2       | 3/1/25                                      |
| 2 up                | 4          | 1       | 3/1/26                                      |
| VSF Member          | 4          |         |                                             |
| Link                | Peer       | Peer    |                                             |
| Link State          | Member     | Link    | Interfaces                                  |
| ---- ----------     | -------    | ------  | ---------------------------                 |
| 1 up                | 3          | 2       | 4/1/25                                      |
| 2 up                | 5          | 1       | 4/1/26                                      |
| Command History     |            |         |                                             |
| Release             |            |         | Modification                                |
| 10.16.1000          |            |         | Commandintroducedon4100and6100Switchseries. |
| 10.07orearlier      |            |         | --                                          |
| Command Information |            |         |                                             |
| Platforms           | Command    | context | Authority                                   |
| 4100                | Manager(#) |         |                                             |
6100
6200
6300
| show vsf      | link detail |     |     |
| ------------- | ----------- | --- | --- |
| show vsf link | detail      |     |     |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 70

Description
Showsdetailedinformationoftheinterfacesconfiguredonlinksofallstackmembers.
Example
| switch# | show vsf | link detail |     |     |     |     |
| ------- | -------- | ----------- | --- | --- | --- | --- |
VSF Member: 1 Link 1 Description: link 1 connected to member 2
Port State Status Code Peer Interface Peer System MAC Peer Product
Type
------- -------- ----------- -------------- ------------------ --------------
---
| 1/1/27 | up    | S   | 2/1/27 | 38:21:f7:4c:a4:c0 |     | <model> |
| ------ | ----- | --- | ------ | ----------------- | --- | ------- |
| 1/1/28 | error | M   | 1/1/27 | 38:21:d7:4e:d7:40 |     | <model> |
VSF Member: 2 Link 1 Description: link 1 connected to member 1
Port State Status Code Peer Interface Peer System MAC Peer Product
Type
------- -------- ----------- -------------- ------------------ --------------
---
| 2/1/27 | up    | S   | 1/1/27 | 38:21:b7:4a:99:80 |     | <model> |
| ------ | ----- | --- | ------ | ----------------- | --- | ------- |
| 2/1/28 | error | T   |        |                   |     |         |
VSF Member: 2 Link 2 Description: link 2 connected to member 3
Port State Status Code Peer Interface Peer System MAC Peer Product
Type
------- -------- ----------- -------------- ------------------ --------------
---
| 2/1/25      | up     | S              | 3/1/26 | 38:20:c7:4a:f0:00 |     | <model> |
| ----------- | ------ | -------------- | ------ | ----------------- | --- | ------- |
| 2/1/26      | down   | D              |        |                   |     |         |
| VSF Member: | 3 Link | 1 Description: | link   | 1 in loop         |     |         |
Port State Status Code Peer Interface Peer System MAC Peer Product
Type
------- -------- ----------- -------------- ------------------ --------------
---
| 3/1/27      | error  | L   | 3/1/28 | 38:21:c7:4c:f0:00 |     | <model> |
| ----------- | ------ | --- | ------ | ----------------- | --- | ------- |
| 3/1/28      | error  | L   | 3/1/27 | 38:21:c7:4c:f0:00 |     | <model> |
| VSF Member: | 3 Link | 2   |        |                   |     |         |
Port State Status Code Peer Interface Peer System MAC Peer Product
Type
------- -------- ----------- -------------- ------------------ --------------
---
| 3/1/25 | down | D   |        |                   |     |         |
| ------ | ---- | --- | ------ | ----------------- | --- | ------- |
| 3/1/26 | up   | S   | 2/1/25 | 38:22:c7:4c:e4:c0 |     | <model> |
Flag abbreviation:
| S - Success |          | D - Interface    | physically | down | T - Peer  | timed out   |
| ----------- | -------- | ---------------- | ---------- | ---- | --------- | ----------- |
| L - Loop    | detected | on the interface |            |      | AP - Peer | autojoin in |
progress
P - Peer with incompatible product type ANE - Peer is not autojoin
eligible
VSFcommands|71

SV - Peer with incompatible software version AF - Peer autojoin validations
failed
| M - Peer   | with       | inconsistent |        | system         | MAC  | address         |               |             |     |
| ---------- | ---------- | ------------ | ------ | -------------- | ---- | --------------- | ------------- | ----------- | --- |
| ILC - Peer | with       | inconsistent |        | VSF            | link | configuration   |               |             |     |
| AMS - Peer | autojoin   |              | failed | as it          | has  | MACsec          | configuration |             |     |
| AMI - Peer | with       | multiple     |        | VSF interfaces |      | attempting      |               | to autojoin |     |
| ACM - Peer | attempting |              | to     | autojoin       | on   | non-provisioned |               | interface   |     |
AND - Peer with non-default VSF interface attempting to autojoin
AID - Peer autojoin failed as it is connected in incorrect direction
AFN - Peer autojoin failed as there is no free member number available
Showingoutputfora6100or4100iswitchseriesconfiguredwithanPortSpeedMismatch(PSM)status
duetomisconfiguredportspeed:
| 6100# show  | vsf | link | detail |     |     |     |     |     |     |
| ----------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- |
| VSF Member: | 1   | Link | 1      |     |     |     |     |     |     |
Port State Status Code Peer Interface Peer System MAC Peer Product
Type
------- ------ ----------- -------------- ----------------- -----------
| 1/1/28      | up  | S    |     | 2/1/25 |     |     | f8:60:f0:c9:70:40 |     | JL678A |
| ----------- | --- | ---- | --- | ------ | --- | --- | ----------------- | --- | ------ |
| VSF Member: | 1   | Link | 2   |        |     |     |                   |     |        |
Port State Status Code Peer Interface Peer System MAC Peer Product Type
------- ----- ----------- -------------- ----------------- -----------
| 1/1/19      | error | PSM  |     | 2/1/2 |     |     | f8:60:f0:c9:70:40 |     | JL678A |
| ----------- | ----- | ---- | --- | ----- | --- | --- | ----------------- | --- | ------ |
| VSF Member: | 2     | Link | 1   |       |     |     |                   |     |        |
Port State Status Code Peer Interface Peer System MAC Peer Product Type
------- ------ ----------- -------------- ----------------- -----------
| 2/1/25      | up  | S    |     | 1/1/28 |     |     | ec:50:aa:2e:2f:80 |     | JL678A |
| ----------- | --- | ---- | --- | ------ | --- | --- | ----------------- | --- | ------ |
| VSF Member: | 2   | Link | 2   |        |     |     |                   |     |        |
Port State Status Code Peer Interface Peer System MAC Peer Product Type
------- ----- ----------- -------------- ----------------- -----------
| 2/1/2          | error       | PSM |         | 1/1/19 |                                             |     | ec:50:aa:2e:2f:80 |     | JL678A |
| -------------- | ----------- | --- | ------- | ------ | ------------------------------------------- | --- | ----------------- | --- | ------ |
| Command        | History     |     |         |        |                                             |     |                   |     |        |
| Release        |             |     |         |        | Modification                                |     |                   |     |        |
| 10.16.1000     |             |     |         |        | Commandintroducedon4100and6100Switchseries. |     |                   |     |        |
| 10.07orearlier |             |     |         |        | --                                          |     |                   |     |        |
| Command        | Information |     |         |        |                                             |     |                   |     |        |
| Platforms      | Command     |     | context |        | Authority                                   |     |                   |     |        |
4100
Manager(#)
6100
6200
6300
| show vsf      | link         | error-detail |     |     |     |     |     |     |     |
| ------------- | ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
| show vsf link | error-detail |              |     |     |     |     |     |     |     |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 72

Description
Showsdetailederrorinformationoftheinterfacesconfiguredonlinksofallstackmembers.Also,the
correctiveactionisalsorecommendedtorecoverfromtheerror.
Example
Showingerrorinformationfortheinterfacesregardingloopdetection:
| switch(config)# | show vsf | link error-detail |          |     |        |            |     |     |
| --------------- | -------- | ----------------- | -------- | --- | ------ | ---------- | --- | --- |
| VSF Member: 2   | Link 1   |                   |          |     |        |            |     |     |
| Port            |          | : 2/1/27          |          |     |        |            |     |     |
| Status Code     |          | : L - `Loop       | detected |     | on the | interface` |     |     |
Error Description : There is a loop detected between interfaces 2/1/27
and
|     |     | 2/1/28 | of member | 2 indicating |     | wrong | cabling. |     |
| --- | --- | ------ | --------- | ------------ | --- | ----- | -------- | --- |
Suggested Corrective Action : VSF interfaces 2/1/27 and 2/1/28 are connected back
to
|               |        | back -      | please   | fix the | cabling.       |     |     |     |
| ------------- | ------ | ----------- | -------- | ------- | -------------- | --- | --- | --- |
| VSF Member: 2 | Link 1 |             |          |         |                |     |     |     |
| Port          |        | : 2/1/28    |          |         |                |     |     |     |
| Status code   |        | : L - `Loop | detected | on      | the interface` |     |     |     |
Error Description : There is a loop detected between interfaces 2/1/28
and
|     |     | 2/1/27 | of member | 2 indicating |     | wrong | cabling. |     |
| --- | --- | ------ | --------- | ------------ | --- | ----- | -------- | --- |
Suggested Corrective Action : VSF interfaces 2/1/28 and 2/1/27 are connected back
to
|                |        | back -    | please | fix the | cabling. |     |     |     |
| -------------- | ------ | --------- | ------ | ------- | -------- | --- | --- | --- |
| VSF Member: 10 | Link 1 |           |        |         |          |     |     |     |
| Port           |        | : 10/1/26 |        |         |          |     |     |     |
Status Code : AFN - `Peer autojoin failed as there is no free
|     |     | member | number | available` |     |     |     |     |
| --- | --- | ------ | ------ | ---------- | --- | --- | --- | --- |
Error Description : Maximum stack size has been reached or there are no
|     |     | free provisioned |     | member | entries | available |     | matching |
| --- | --- | ---------------- | --- | ------ | ------- | --------- | --- | -------- |
the
|     |     | peer switch | with | product | type | JL667A. |     |     |
| --- | --- | ----------- | ---- | ------- | ---- | ------- | --- | --- |
Suggested Corrective Action : Remove a member using “no vsf member x” CLI and then
|     |     | physically   | disconnect |        | and reconnect |        | the | new switch |
| --- | --- | ------------ | ---------- | ------ | ------------- | ------ | --- | ---------- |
|     |     | with product | type       | JL667A | for           | adding | it  | into the   |
stack.
ShowingerrorinformationwhenpeermemberisconnectedtoVSFlinkviaitsMACsec-configured
interfaceforautojoin:
| switch(config)# | show vsf | link error-detail |     |     |     |     |     |     |
| --------------- | -------- | ----------------- | --- | --- | --- | --- | --- | --- |
| VSF Member: 2   | Link 2   |                   |     |     |     |     |     |     |
VSFcommands|73

| Port   |      |     | : 2/1/26 |         |          |        |     |        |        |     |
| ------ | ---- | --- | -------- | ------- | -------- | ------ | --- | ------ | ------ | --- |
| Status | Code |     | : AMS    | - `Peer | autojoin | failed | as  | it has | MACsec |     |
configuration`
Error Description : Autojoin failed as interface 2/1/26 is connected to
|     |     |     | peer  | with | MAC    | 38:21:c7:5c:d4:00 |     | on  | interface | 1/1/27 |
| --- | --- | --- | ----- | ---- | ------ | ----------------- | --- | --- | --------- | ------ |
|     |     |     | which | has  | MACsec | configuration.    |     |     |           |        |
Suggested Corrective Action : MACsec configuration should be removed from the
|     |     |     | peer | with | MAC | 38:21:c7:5c:d4:00 |     | on  | interface | 1/1/27. |
| --- | --- | --- | ---- | ---- | --- | ----------------- | --- | --- | --------- | ------- |
Showinginformationabouta4100ior6100switchseriesconfiguredwithanincorrectportspeed:
| 6100(config)# | show   | vsf link | error-detail |     |     |     |     |     |     |     |
| ------------- | ------ | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| VSF Member:   | 1 Link | 1        |              |     |     |     |     |     |     |     |
| Port          |        |          | : 1/1/49     |     |     |     |     |     |     |     |
Status Code : IPS - `Peer switch with inconsistent VSF port speed`
| Error Description |                 |     | : Peer | switch | is  | operating | at a | different |     |     |
| ----------------- | --------------- | --- | ------ | ------ | --- | --------- | ---- | --------- | --- | --- |
| vsf port          | speed of 1Gbps. |     |        |        |     |           |      |           |     |     |
Suggested Corrective Action : Change vsf port speed to 1Gbps on this switch
| or change      | vsf port    | speed   | to 10Gbps | on                                          | the peer | switch. |     |     |     |     |
| -------------- | ----------- | ------- | --------- | ------------------------------------------- | -------- | ------- | --- | --- | --- | --- |
| Command        | History     |         |           |                                             |          |         |     |     |     |     |
| Release        |             |         |           | Modification                                |          |         |     |     |     |     |
| 10.16.1000     |             |         |           | Commandintroducedon4100and6100Switchseries. |          |         |     |     |     |     |
| 10.07orearlier |             |         |           | --                                          |          |         |     |     |     |     |
| Command        | Information |         |           |                                             |          |         |     |     |     |     |
| Platforms      | Command     | context |           | Authority                                   |          |         |     |     |     |     |
| 4100           | Manager(#)  |         |           |                                             |          |         |     |     |     |     |
6100
6200
6300
| show vsf      | link error-detail |        |     | member      |     |     |     |     |     |     |
| ------------- | ----------------- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- |
| show vsf link | error-detail      | member |     | <MEMBER-ID> |     |     |     |     |     |     |
Description
Showserrorinformationandthesuggestiveactiontoresolvetheerroroftheinterfacesconfiguredon
linksofaparticularstackmember.
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 74

| Parameter   |     |     | Description                   |     |     |     |     |     |     |     |
| ----------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
| <MEMBER-ID> |     |     | VSFmemberidentifier.Required. |     |     |     |     |     |     |     |
|             |     |     | n Rangefor4100idevices:1-4.   |     |     |     |     |     |     |     |
|             |     |     | n Rangefor6100devices:1-6.    |     |     |     |     |     |     |     |
|             |     |     | n Rangefor6200Fdevices:1-8.   |     |     |     |     |     |     |     |
|             |     |     | n Rangefor6300devices:1-10.   |     |     |     |     |     |     |     |
Example
Showingerrorinformationandthesuggestiveactionformember1:
| switch# show | vsf link error-detail |          | member |     | 1   |     |     |     |     |     |
| ------------ | --------------------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| VSF Member:  | 1 Link 1              |          |        |     |     |     |     |     |     |     |
| Port         |                       | : 1/1/52 |        |     |     |     |     |     |     |     |
Status Code : M - `Peer with inconsistent system MAC address`
Error Description : All interfaces within a single VSF link must
terminate
|     |     | into   | the | same   | peer | switch.   | Interface |      | 1/1/52 | of        |
| --- | --- | ------ | --- | ------ | ---- | --------- | --------- | ---- | ------ | --------- |
|     |     | member |     | 1 link | 1 is | connected |           | to a | wrong  | peer with |
MAC 38:21:c7:5c:26:40.
Suggested Corrective Action : Multiple VSF neighbors detected on this VSF link 1.
|     |     | Interface          |     | 1/1/52 |     | is connected |      | to device |     | MAC |
| --- | --- | ------------------ | --- | ------ | --- | ------------ | ---- | --------- | --- | --- |
|     |     | 38:21:c7:5c:26:40. |     |        |     | Please       | make | sure      | the | VSF |
interfaces
|     |     | of  | link | 1 terminate |     | on the | same | peer | device. |     |
| --- | --- | --- | ---- | ----------- | --- | ------ | ---- | ---- | ------- | --- |
Showingerrorinformationandthesuggestiveactionformember4:
| switch# show | vsf link error-detail |          | member |       | 4    |             |     |     |           |     |
| ------------ | --------------------- | -------- | ------ | ----- | ---- | ----------- | --- | --- | --------- | --- |
| VSF Member:  | 4 Link 1              |          |        |       |      |             |     |     |           |     |
| Port         |                       | : 4/1/27 |        |       |      |             |     |     |           |     |
| Status Code  |                       | : AND    | -      | `Peer | with | non-default |     | VSF | interface |     |
attempting
to autojoin`
Error Description : Switch with MAC 38:21:c7:5c:a0:c0 is connected on
port
|     |     | 1/1/27 |     | which | is a | non default |     | autojoin |     | VSF |
| --- | --- | ------ | --- | ----- | ---- | ----------- | --- | -------- | --- | --- |
interface.
Suggested Corrective Action : Auto-join failed on device with MAC
38:21:c7:5c:a0:c0.
|     |     | Please |     | connect | this      | device | via     | interfaces |     | 25 or 26 - |
| --- | --- | ------ | --- | ------- | --------- | ------ | ------- | ---------- | --- | ---------- |
|     |     | those  | are | the     | auto-join |        | capable | interfaces |     | on this    |
device.
Showingerrorinformationwhenthepeermemberisconnectedtomember2’sVSFlinkviaitsMACsec-
configuredinterfaceforautojoin:
VSFcommands|75

| switch(config)# | show   | vsf | link error-detail |         | member 2        |           |        |     |
| --------------- | ------ | --- | ----------------- | ------- | --------------- | --------- | ------ | --- |
| VSF Member:     | 2 Link | 2   |                   |         |                 |           |        |     |
| Port            |        |     | : 2/1/26          |         |                 |           |        |     |
| Status Code     |        |     | : AMS             | - `Peer | autojoin failed | as it has | MACsec |     |
configuration`
Error Description : Autojoin failed as interface 2/1/26 is connected to
|     |     |     | peer  | with | MAC 38:21:c7:5c:d4:00 | on  | interface | 1/1/27 |
| --- | --- | --- | ----- | ---- | --------------------- | --- | --------- | ------ |
|     |     |     | which | has  | MACsec configuration. |     |           |        |
Suggested Corrective Action : MACsec configuration should be removed from the
|             |        |     | peer     | with    | MAC 38:21:c7:5c:d4:00 | on        | interface | 1/1/27 |
| ----------- | ------ | --- | -------- | ------- | --------------------- | --------- | --------- | ------ |
| VSF Member: | 2 Link | 2   |          |         |                       |           |           |        |
| Port        |        |     | : 2/1/26 |         |                       |           |           |        |
| Status Code |        |     | : AMS    | - `Peer | autojoin failed       | as it has | MACsec    |        |
configuration`
Error Description : Autojoin failed as interface 2/1/26 is connected to
|     |     |     | peer  | with | MAC 38:21:c7:5c:d4:00 | on  | interface | 1/1/27 |
| --- | --- | --- | ----- | ---- | --------------------- | --- | --------- | ------ |
|     |     |     | which | has  | MACsec configuration. |     |           |        |
Suggested Corrective Action : MACsec configuration should be removed from the
|     |     |     | peer | with | MAC 38:21:c7:5c:d4:00 | on  | interface | 1/1/27 |
| --- | --- | --- | ---- | ---- | --------------------- | --- | --------- | ------ |
Showingoutputwhenthereisnoerror-detailforaparticularmember:
| switch# show        | vsf link        | error-detail |     | member                                      | 2   |     |     |     |
| ------------------- | --------------- | ------------ | --- | ------------------------------------------- | --- | --- | --- | --- |
| No Error            | found in member |              | 2   |                                             |     |     |     |     |
| Command History     |                 |              |     |                                             |     |     |     |     |
| Release             |                 |              |     | Modification                                |     |     |     |     |
| 10.16.1000          |                 |              |     | Commandintroducedon4100and6100Switchseries. |     |     |     |     |
| 10.07orearlier      |                 |              |     | --                                          |     |     |     |     |
| Command Information |                 |              |     |                                             |     |     |     |     |
| Platforms           | Command         | context      |     | Authority                                   |     |     |     |     |
| 4100                | Manager(#)      |              |     |                                             |     |     |     |     |
6100
6200
6300
| show vsf                 | split-detection |                     |     |     |     |     |     |     |
| ------------------------ | --------------- | ------------------- | --- | --- | --- | --- | --- | --- |
| show vsf split-detection |                 | [status|statistics] |     |     |     |     |     |     |
Description
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 76

DisplaystheVSFsplitdetectionstatusorstatistics.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
status Displayswhetherthesplitdetectionoperationalstatusisupor
down.
statistics Displaysinformationrelatedtotransmittedandreceivedpackets.
Examples
| switch#         | show | vsf split-detection |     |     | status |        |
| --------------- | ---- | ------------------- | --- | --- | ------ | ------ |
| Split Detection |      | Method              |     |     |        | : mgmt |
Split Detection Operational Status : Down (Mgmt interface admin state is down)
| switch#         | show | vsf split-detection |            |     | status |        |
| --------------- | ---- | ------------------- | ---------- | --- | ------ | ------ |
| Split Detection |      | Method              |            |     |        | : vlan |
| Split Detection |      | VLAN                |            |     |        | : 9    |
| Split Detection |      | VLAN                | Interfaces |     |        | :      |
Split Detection Operational status : Down (VLAN 9 is not configured)
| switch#   | show      | vsf split-detection |             |     | statistics |     |
| --------- | --------- | ------------------- | ----------- | --- | ---------- | --- |
| VSF Split | Detection |                     | Statistics: |     |            |     |
===============================
| Total Packets |             | Transmitted |         |           |                    | = 10 |
| ------------- | ----------- | ----------- | ------- | --------- | ------------------ | ---- |
| Total Packets |             | Received    |         |           |                    | = 20 |
| Total Packets |             | Received    | And     | Discarded |                    | = 20 |
| Command       | History     |             |         |           |                    |      |
| Release       |             |             |         |           | Modification       |      |
| 10.16.1000    |             |             |         |           | Commandintroduced. |      |
| Command       | Information |             |         |           |                    |      |
| Platforms     | Command     |             | context |           | Authority          |      |
| 4100i         | Manager(#)  |             |         |           |                    |      |
6100
6200
6300
| show vsf | topology |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- |
show vsf topology
Description
DisplaysinformationaboutVSFstackmemberconnections.
Example
VSFcommands|77

| switch#        | show vsf topology |           |                                             |
| -------------- | ----------------- | --------- | ------------------------------------------- |
|                | Stby              | Conductor |                                             |
| +---+          | +---+ +---+       |           |                                             |
| | 3 |1==2|     | 2 |1==1|          | 1 |       |                                             |
| +---+          | +---+ +---+       |           |                                             |
| Command        | History           |           |                                             |
| Release        |                   |           | Modification                                |
| 10.16.1000     |                   |           | Commandintroducedon4100and6100Switchseries. |
| 10.07orearlier |                   |           | --                                          |
| Command        | Information       |           |                                             |
| Platforms      | Command           | context   | Authority                                   |
| 4100           | Manager(#)        |           |                                             |
6100
6200
6300
shutdown
shutdown
no shutdown
Description
ShutsdownoneormoreVSFlinkinterfaces.
ThenoformofthiscommandturnsononeormoreVSFlinkinterfaces.
Examples
ShuttingdownaVSFlinkinterface:
| switch(config)#                      | interface | 1/1/1-1/1/2 |          |
| ------------------------------------ | --------- | ----------- | -------- |
| switch(config-if-vsf-<1/1/1-1/1/2>)# |           |             | shutdown |
ShutdownconfigurationforVSFinterfacesisnotpersistentacrossreboots.
| Command        | History     |     |                                             |
| -------------- | ----------- | --- | ------------------------------------------- |
| Release        |             |     | Modification                                |
| 10.16.1000     |             |     | Commandintroducedon4100and6100Switchseries. |
| 10.07orearlier |             |     | --                                          |
| Command        | Information |     |                                             |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 78

| Platforms | Command | context |     | Authority |     |
| --------- | ------- | ------- | --- | --------- | --- |
4100 config-if-vsf Administratorsorlocalusergroupmemberswithexecution
| 6100 |     |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --- | --------------------- | --- |
6200
6300
type
type <TYPE>
no type <TYPE>
Description
ConfiguresthepartnumberoftheVSFmemberbeingprovisioned.Afterprovisioning,theinterfacesof
thememberareavailableforconfiguration.
Whenthemembereventuallyjoinsthestack,itwillbootupwiththeconfigurationmadeonthepre-
provisionedinterfaces.
Toprovisionamember,themembernumberandthepartnumberofthemembermustbespecified.
ThenoformofthiscommandremovestheconfigurationforthepartnumberoftheVSFmember
provisioned.
| Parameter |     |     |     | Description                                        |     |
| --------- | --- | --- | --- | -------------------------------------------------- | --- |
| <TYPE>    |     |     |     | Thepartnumberofthememberbeingprovisioned.Required. |     |
Examples
ConfiguringthepartnumberofaVSFmember:
switch(vsf-member-2)#
| type The               | part number   |         | of the         | member  | being provisioned |
| ---------------------- | ------------- | ------- | -------------- | ------- | ----------------- |
| switch(vsf-member-2)#  |               | type    | ?              |         |                   |
| jl658a                 | 6300M 24SFP+  | /4SFP56 |                | Switch  |                   |
| jl659a                 | 6300M 48SR    | PoE     | CLS 6          | /4SFP56 | Switch            |
| jl660a                 | 6300M 24SR    | PoE     | CLS 6          | /4SFP56 | Switch            |
| jl661a                 | 6300M 48G     | PoE     | CLS 4 /4SFP56  |         | Switch            |
| jl662a                 | 6300M 24G     | PoE     | CLS 4 /4SFP56  |         | Switch            |
| jl663a                 | 6300M 48G     | /4SFP56 | Switch         |         |                   |
| jl664a                 | 6300M 24G     | /4SFP56 | Switch         |         |                   |
| jl665a                 | 6300F 48G     | PoE     | CLS 4 /4SFP56  |         | Switch            |
| jl666a                 | 6300F 24G     | PoE     | CLS 4 /4SFP56  |         | Switch            |
| jl667a                 | 6300F 48G     | /4SFP56 | Switch         |         |                   |
| jl668a                 | 6300F 24G     | /4SFP56 | Switch         |         |                   |
| jl762a                 | 6300M 48G     | 4SFP56  | Pwr2Prt        | Switch  |                   |
| s3l75a                 | HPE ANW 6300L |         | 24SRX CL6      | 2L      | 2Y L2 Switch      |
| s3l76a                 | HPE ANW 6300L |         | 48SR5 CL8      | 2L      | 2Y L2 Switch      |
| s3l77a                 | HPE ANW 6300L |         | 48SR5 2L       | 2P      | LRM L2 Switch     |
| switch(vsf-member-2)#  |               | type    | jl662a         |         |                   |
| switch(vsf-member-2)#  |               | show    | running-config |         |                   |
| Current configuration: |               |         |                |         |                   |
!
| !Version | AOS-CX |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- |
VSFcommands|79

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
| vsf member | 1      |     |     |
| ---------- | ------ | --- | --- |
| type       | jl661a |     |     |
exit
| vsf member | 2      |     |     |
| ---------- | ------ | --- | --- |
| type       | jl662a |     |     |
exit
| Command History     |         |         |                                             |
| ------------------- | ------- | ------- | ------------------------------------------- |
| Release             |         |         | Modification                                |
| 10.16.1000          |         |         | Commandintroducedon4100and6100Switchseries. |
| 10.07orearlier      |         |         | --                                          |
| Command Information |         |         |                                             |
| Platforms           | Command | context | Authority                                   |
4100 vsf-member-<ID> Administratorsorlocalusergroupmemberswithexecution
| 6100 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6200
6300
vsf egress-shape
vsf egress-shape
no egress-shape
Description
WhentheVSFlinksareofdifferentinterfacespeeds,thecommandensuresthatallVSFinterfacesina
stackoperateatachosencommondenominatorinterfacespeedwhenthereisatleastoneactivestack
memberoftypeS0E91AorS0X44Ainthestack.
ThenoformofthiscommandremovesthecommondenominatorspeedfromallVSFlinksandensure
thatalltheVSFlinksoperateattheiroriginalspeed.
VSFegress-shapeisenabledbydefaultontheswitch.
Thisfeatureisapplicableonlyfor6300switchseries(exceptforS3L75A,S3L76AandS3L77A).
| Parameter    |     |     | Description                             |
| ------------ | --- | --- | --------------------------------------- |
| egress-shape |     |     | EnablesegressshapingonallVSFinterfaces. |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 80

Examples
Example1:
switch(config)#vsf
egress-shape
| switch# show         | vsf    |                     |          |
| -------------------- | ------ | ------------------- | -------- |
| Force Autojoin       |        | : Disabled          |          |
| Autojoin Eligibility |        | Status: Not         | Eligible |
| MAC Address          |        | : 38:21:c7:5c:62:40 |          |
| Egress Shape         |        | : Enabled           |          |
| Egress Shape         | Rate   | : None              |          |
| Secondary            |        | : 2                 |          |
| Topology             |        | : Ring              |          |
| Status               |        | : No                | Split    |
| Split Detection      | Method | : None              |          |
| Mbr Mac Address      |        | type                | Status   |
ID
| --- ------------------- |     | -------------- | --------------- |
| ----------------------- | --- | -------------- | --------------- |
| 1 38:21:c7:5c:62:40     |     | JL668A         | Conductor       |
| 2 18:7a:3b:1b:68:c0     |     | R8S90A         | Standby         |
| 3 38:21:c7:5c:57:c0     |     | JL668A         | Member          |
| 4 18:7a:3b:1b:66:40     |     | R8S89A         | Member          |
Example2:
| switch(config)#vsf   |        | egress-shape        |          |
| -------------------- | ------ | ------------------- | -------- |
| switch# show         | vsf    |                     |          |
| Force Autojoin       |        | : Disabled          |          |
| Autojoin Eligibility |        | Status: Not         | Eligible |
| MAC Address          |        | : 38:21:c7:5c:62:40 |          |
| Egress Shape         |        | : Enabled           |          |
| Egress Shape         | Rate   | : None              |          |
| Secondary            |        | : 2                 |          |
| Topology             |        | : Ring              |          |
| Status               |        | : No                | Split    |
| Split Detection      | Method | : None              |          |
| Mbr Mac Address      |        | type                | Status   |
ID
| --- ------------------- |     | -------------- | --------------- |
| ----------------------- | --- | -------------- | --------------- |
| 1 38:21:c7:5c:62:40     |     | JL668A         | Conductor       |
| 2 18:7a:3b:1b:68:c0     |     | R8S90A         | Standby         |
| 3 38:21:c7:5c:57:c0     |     | JL668A         | Member          |
| 4 18:7a:3b:1b:66:40     |     | S0E91A         | Member          |
Example3:
| switch(config)#vsf   |     | egress-shape        |          |
| -------------------- | --- | ------------------- | -------- |
| switch# show         | vsf |                     |          |
| Force Autojoin       |     | : Disabled          |          |
| Autojoin Eligibility |     | Status: Not         | Eligible |
| MAC Address          |     | : 38:21:c7:5c:62:40 |          |
| Egress Shape         |     | : Enabled           |          |
VSFcommands|81

| Egress Shape    | Rate   |     | : 10000000 |       | kbps   |
| --------------- | ------ | --- | ---------- | ----- | ------ |
| Secondary       |        |     | : 2        |       |        |
| Topology        |        |     | : Ring     |       |        |
| Status          |        |     | : No       | Split |        |
| Split Detection | Method |     | : None     |       |        |
| Mbr Mac Address |        |     | type       |       | Status |
ID
| --- ------------------- |     |     | -------------- |     | --------------- |
| ----------------------- | --- | --- | -------------- | --- | --------------- |
| 1 38:21:c7:5c:62:40     |     |     | JL668A         |     | Conductor       |
| 2 18:7a:3b:1b:68:c0     |     |     | R8S90A         |     | Standby         |
| 3 38:21:c7:5c:57:c0     |     |     | JL668A         |     | Member          |
| 4 18:7a:3b:1b:66:40     |     |     | S0E91A         |     | Member          |
Example4:
| switch(config)#no |             | vsf egress-shape |                     |          |        |
| ----------------- | ----------- | ---------------- | ------------------- | -------- | ------ |
| switch# show      | vsf         |                  |                     |          |        |
| Force Autojoin    |             |                  | : Disabled          |          |        |
| Autojoin          | Eligibility | Status:          | Not                 | Eligible |        |
| MAC Address       |             |                  | : 38:21:c7:5c:62:40 |          |        |
| Egress Shape      |             |                  | : Disabled          |          |        |
| Egress Shape      | Rate        |                  | : None              |          |        |
| Secondary         |             |                  | : 2                 |          |        |
| Topology          |             |                  | : Ring              |          |        |
| Status            |             |                  | : No                | Split    |        |
| Split Detection   | Method      |                  | : None              |          |        |
| Mbr Mac Address   |             |                  | type                |          | Status |
ID
| --- ------------------- |         |         | -------------- |                    | --------------- |
| ----------------------- | ------- | ------- | -------------- | ------------------ | --------------- |
| 1 38:21:c7:5c:62:40     |         |         | JL668A         |                    | Conductor       |
| 2 18:7a:3b:1b:68:c0     |         |         | R8S90A         |                    | Standby         |
| 3 38:21:c7:5c:57:c0     |         |         | JL668A         |                    | Member          |
| 4 18:7a:3b:1b:66:40     |         |         | S0E91A         |                    | Member          |
| Command History         |         |         |                |                    |                 |
| Release                 |         |         |                | Modification       |                 |
| 10.15                   |         |         |                | Commandintroduced. |                 |
| Command Information     |         |         |                |                    |                 |
| Platforms               | Command | context |                | Authority          |                 |
6300,except config Administratorsorlocalusergroupmemberswithexecution
| forS3L75A, |     |     |     | rightsforthiscommand. |     |
| ---------- | --- | --- | --- | --------------------- | --- |
S3L76A,
S3L77A.
vsf force-auto-join
vsf force-auto-join
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 82

Description
Forcestheswitchwithnon-factorydefaultconfigurationtojoinastack.Theswitchshouldnothaveany
existingVSFconfigurationsforforceauto-jointowork.IfVSFconfigurationsaremadeafterforceauto-
joinisenabled,theswitchwillnolongerbeeligibleforauto-join.
Examples
Forcingaswitchwithnon-factorydefaultconfigurationtojoinastack:
| switch(config)# | vsf | force-auto-join |                                             |
| --------------- | --- | --------------- | ------------------------------------------- |
| Command History |     |                 |                                             |
| Release         |     |                 | Modification                                |
| 10.16.1000      |     |                 | Commandintroducedon4100and6100Switchseries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
4100 config Administratorsorlocalusergroupmemberswithexecution
| 6100 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6200
6300
vsf member
| vsf member <MEMBER-ID> |             |     |     |
| ---------------------- | ----------- | --- | --- |
| no vsf member          | <MEMBER-ID> |     |     |
Description
CreatesVSFmembercontextintheswitchforthespecifiedmember.
Thenoformofthiscommandremovesthespecifiedmemberfromthestack.Allconfiguration
associatedwiththemember,aswellasthesubsystemsandinterfacesofthememberwillalsobe
removed.
Ifthememberisphysicallypresentinthestackatthetimeitisremoved,itwillrebootwiththedefault
configurationandloseitsidentityasamemberofthestackfromwhichitwasremoved.
Whenaphysicallypresentmemberisremoved,itmaycausethestacktosplit.
| Parameter   |     |     | Description          |
| ----------- | --- | --- | -------------------- |
| <MEMBER-ID> |     |     | VSFmemberidentifier. |
n Rangefor4100idevices:1to4.
n Rangefor6100devices:1to6.
n Rangefor6200Fdevices:1to8.
n Rangefor6300devices:1to10.
VSFcommands|83

Examples
ConfiguringaVSFmember:
switch(config)#
|     |     |     | vsf member | 2   |     |     |
| --- | --- | --- | ---------- | --- | --- | --- |
switch(vsf-member-2)#
Removinganon-conductormemberfromthestack:
| switch(config)# |           |             | no vsf | member 2        |     |              |
| --------------- | --------- | ----------- | ------ | --------------- | --- | ------------ |
| The             | specified | switch      | will   | be unconfigured |     | and rebooted |
| Do you          | want      | to continue |        | (y/n)?          | y   |              |
Removingtherunningconductorshouldbedonewithcautionasitcanmakethestackunusableifthereisno
standby.
| Command    | History |     |     |     |                                             |     |
| ---------- | ------- | --- | --- | --- | ------------------------------------------- | --- |
| Release    |         |     |     |     | Modification                                |     |
| 10.16.1000 |         |     |     |     | Commandintroducedon4100and6100Switchseries. |     |
10.07orearlier
| Command   | Information |         |         |     |           |     |
| --------- | ----------- | ------- | ------- | --- | --------- | --- |
| Platforms |             | Command | context |     | Authority |     |
4100 config Administratorsorlocalusergroupmemberswithexecution
| 6100 |     |     |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --- | --- | --------------------- | --- |
6200
6300
| vsf member |             | reboot |        |     |     |     |
| ---------- | ----------- | ------ | ------ | --- | --- | --- |
| vsf member | <MEMBER-ID> |        | reboot |     |     |     |
Description
RebootsthespecifiedVSFmember.Uponreboot,iftheconductorisreachable,thememberwillrejoin
thestack.
| Parameter   |     |     |     |     | Description                        |     |
| ----------- | --- | --- | --- | --- | ---------------------------------- | --- |
| <MEMBER-ID> |     |     |     |     | Membernumbertoberebooted.Required. |     |
n Rangefor4100idevices:1-4.
n Rangefor6100devices:1-6.
n Rangefor6200Fdevices:1-8.
n Rangefor6300devices:1-10.
Examples
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 84

Rebootingtheprimaryswitchofthestack:
| switch#   | vsf member       | 1 reboot  |              |         |           |
| --------- | ---------------- | --------- | ------------ | ------- | --------- |
| Rebooting | the conductor    | switch    | of the stack | without | a standby |
| will make | the stack        | unusable. |              |         |           |
| Do you    | want to continue | (y/n)?    | y            |         |           |
| switch#   | vsf member       | 1 reboot  |              |         |           |
The conductor switch will reboot and the standby will become the conductor.
| Do you     | want to continue | (y/n)?        | y                                           |     |     |
| ---------- | ---------------- | ------------- | ------------------------------------------- | --- | --- |
| switch#    | vsf member       | 2 reboot      |                                             |     |     |
| This will  | reboot           | the specified | switch.                                     |     |     |
| Do you     | want to continue | (y/n)?        | y                                           |     |     |
| Command    | History          |               |                                             |     |     |
| Release    |                  |               | Modification                                |     |     |
| 10.16.1000 |                  |               | Commandintroducedon4100and6100Switchseries. |     |     |
10.07orearlier
| Command   | Information |         |           |     |     |
| --------- | ----------- | ------- | --------- | --- | --- |
| Platforms | Command     | context | Authority |     |     |
4100 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6100 |     |     | rightsforthiscommand. |     |     |
| ---- | --- | --- | --------------------- | --- | --- |
6200
6300
vsf renumber-to
| vsf renumber-to | <MEMBER-ID> |     |     |     |     |
| --------------- | ----------- | --- | --- | --- | --- |
Description
RenumbersVSFmember1toavaluefrom2through10(for6300devices)and2through8(forthe
6200Fdevice).Changingthemembernumbercausestheswitchtorebootwiththenewmember
number.Onlymember1canberenumbered.
VSFlinksmustbeconfiguredbeforerenumberingaswitch.Renumberingwillbedisallowedifnolinksare
configuredorthereareprovisioned/physicallypresentmembers.
| Parameter   |     |     | Description                                   |     |     |
| ----------- | --- | --- | --------------------------------------------- | --- | --- |
| <MEMBER-ID> |     |     | Membernumbertowhichthememberwillberenumbered. |     |     |
Required.
n Rangefor4100idevices:2-4.
Rangefor6100devices:2-6.
n
n Rangefor6200Fdevices:2-8.
n Rangefor6300devices:2-10.
VSFcommands|85

Examples
RenumberingprimaryVSFmemberfrom1to2:
switch(config)#
|     |     | vsf | renumber-to | 2   |     |     |
| --- | --- | --- | ----------- | --- | --- | --- |
Member 1 cannot be renumbered until all other members are removed.
| switch(config)# |          | vsf           | renumber-to   | 2     |                                             |                |
| --------------- | -------- | ------------- | ------------- | ----- | ------------------------------------------- | -------------- |
| Member          | 1 cannot | be renumbered |               | until | a VSF link                                  | is configured. |
| switch(config)# |          | vsf           | renumber-to   | 2     |                                             |                |
| This will       | save     | the VSF       | configuration |       | and reboot                                  | the switch.    |
| Do you          | want to  | continue      | (y/n)?        | y     |                                             |                |
| Command         | History  |               |               |       |                                             |                |
| Release         |          |               |               |       | Modification                                |                |
| 10.16.1000      |          |               |               |       | Commandintroducedon4100and6100Switchseries. |                |
10.07orearlier
--
| Command   | Information |     |         |     |           |     |
| --------- | ----------- | --- | ------- | --- | --------- | --- |
| Platforms | Command     |     | context |     | Authority |     |
4100 config Administratorsorlocalusergroupmemberswithexecution
| 6100 |     |     |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --- | --- | --------------------- | --- |
6200
6300
vsf secondary-member
| vsf secondary-member    |     | <MEMBER-ID> |             |     |     |     |
| ----------------------- | --- | ----------- | ----------- | --- | --- | --- |
| no vsf secondary-member |     |             | <MEMBER-ID> |     |     |     |
Description
Configuresasecondarymemberfromtheavailablemembers.Thesecondarymemberwillnormally
operateastheStandbymemberofthestack.
Thenoformofthiscommandremovestheconfigurationofthesecondarymember.
Member1cannotbeconfiguredasthesecondarymember.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<MEMBER-ID>
Secondarymembernumber.Required.
n Rangefor4100idevices:2-4.
n Rangefor6100devices:2-6.
n Rangefor6200Fdevices:2-8.
n Rangefor6300devices:2-10.
Examples
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 86

Configuringandun-configuringasecondarymember:
| switch(config)# |     | vsf | secondary-member | 3   |
| --------------- | --- | --- | ---------------- | --- |
This will save the configuration and reboot the specified switch.
| Do you          | want to | continue | (y/n)?               | y         |
| --------------- | ------- | -------- | -------------------- | --------- |
| switch(config)# |         | no       | vsf secondary-member |           |
| The secondary   |         | member   | will go for          | a reboot. |
| Do you          | want to | continue | (y/n)?               |           |
y
Configuringasecondarymemberwhensecondarymemberisalreadyconfigured:
| switch(config)# |     | vsf | secondary-member | 3   |
| --------------- | --- | --- | ---------------- | --- |
This will save the configuration and reboot the specified switch.
| Do you | want to   | continue | (y/n)?           | y   |
| ------ | --------- | -------- | ---------------- | --- |
| switch | (config)# | vsf      | secondary-member | 4   |
A secondary member is already configured. Existing secondary member
will be unconfigured and rebooted to join the stack as a member. The
specified switch is then rebooted and will join the stack as the new
standby.
| Do you | want to | continue | (y/n)? | y   |
| ------ | ------- | -------- | ------ | --- |
Configuringasecondarymemberwhenoneormoremembersarebooting:
| switch(config)# |     | vsf | secondary-member | 3   |
| --------------- | --- | --- | ---------------- | --- |
One or more members are currently booting. Allowing this configuration
| may cause | stack   | to       | split leading | to traffic disruption. |
| --------- | ------- | -------- | ------------- | ---------------------- |
| Do you    | want to | continue | (y/n)?        | y                      |
This will save the configuration and reboot the specified switch.
| Do you | want to | continue | (y/n)? |     |
| ------ | ------- | -------- | ------ | --- |
y
| switch(config)#no |     | vsf | secondary-member |     |
| ----------------- | --- | --- | ---------------- | --- |
One or more members are currently booting. Allowing this configuration
| may cause      | stack       | to       | split leading | to traffic disruption.                      |
| -------------- | ----------- | -------- | ------------- | ------------------------------------------- |
| Do you         | want to     | continue | (y/n)?        | y                                           |
| The secondary  |             | member   | will go for   | a reboot.                                   |
| Do you         | want to     | continue | (y/n)?        | y                                           |
| Command        | History     |          |               |                                             |
| Release        |             |          |               | Modification                                |
| 10.16.1000     |             |          |               | Commandintroducedon4100and6100Switchseries. |
| 10.07orearlier |             |          |               | --                                          |
| Command        | Information |          |               |                                             |
| Platforms      | Command     |          | context       | Authority                                   |
4100 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6100
6200
6300
VSFcommands|87

| vsf split-detect |     | mgmt |     |
| ---------------- | --- | ---- | --- |
vsf split-detect
mgmt
no ...
Description
ConfigurestheVSFsplitdetectionmethodthatspecifiesthemechanismusedforstackfragment
discoverywhenthereisaVSFstacksplit.
Oncethestackfragmentsarediscovered,thefragmenthavingtheprimarymemberalwaystakes
precedence.Allnon-VSFinterfacesonthesecondarystackfragmentwillbebroughtdowntominimize
networkdisruptionduetoduplicateMAC/IPaddresses.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
mgmt
Configuresamanagementinterfaceasthesplitdetectionmethod
on6200and6300Switchseries.Themanagementinterfacesof
theprimaryandsecondarymembersshouldbeeitherconnected
tothesameL2networkordirectlyconnectedtoeachother.
| no ... |     |     | NegatesanyconfiguredparameterandremovestheVSF split |
| ------ | --- | --- | --------------------------------------------------- |
detectionconfiguration.
Examples
Configuringthemgmtinterfaceasthesplitdetectionmethod:
| switch(config)#      | vsf    | split-detect        | mgmt     |
| -------------------- | ------ | ------------------- | -------- |
| switch# sh           | vsf    |                     |          |
| Force Autojoin       |        | : Disabled          |          |
| Autojoin Eligibility |        | Status: Not         | Eligible |
| MAC Address          |        | : 4c:d5:87:30:26:80 |          |
| Egress Shape         |        | : Enabled           |          |
| Egress Shape         | Rate   | : None              |          |
| Secondary            |        | : 2                 |          |
| Topology             |        | : Ring              |          |
| Status               |        | : No                | Split    |
| Split Detection      | Method | : mgmt              |          |
| Mbr Mac Address      |        | type                | Status   |
ID
| --- ------------------- |     | -------------- | --------------- |
| ----------------------- | --- | -------------- | --------------- |
| 1 4c:d5:87:30:26:80     |     | JL660A         | Conductor       |
| 2 e4:de:40:9b:10:00     |     | JL659A         | Standby         |
| 3 14:ab:ec:eb:81:80     |     | R8S91A         | Member          |
| 4 14:ab:ec:eb:53:80     |     | R8S91A         | Member          |
Removingsplitdetectionfromthestack:
| switch(config)# | no  | vsf split-detect |     |
| --------------- | --- | ---------------- | --- |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 88

| switch# sh      | vsf         |         |                     |          |        |
| --------------- | ----------- | ------- | ------------------- | -------- | ------ |
| Force Autojoin  |             |         | : Disabled          |          |        |
| Autojoin        | Eligibility | Status: | Not                 | Eligible |        |
| MAC Address     |             |         | : 4c:d5:87:30:26:80 |          |        |
| Egress Shape    |             |         | : Enabled           |          |        |
| Egress Shape    | Rate        |         | : None              |          |        |
| Secondary       |             |         | : 2                 |          |        |
| Topology        |             |         | : Ring              |          |        |
| Status          |             |         | : No                | Split    |        |
| Split Detection | Method      |         | : None              |          |        |
| Mbr Mac Address |             |         | type                |          | Status |
ID
| --- ------------------- |         |         | -------------- |                    | --------------- |
| ----------------------- | ------- | ------- | -------------- | ------------------ | --------------- |
| 1 4c:d5:87:30:26:80     |         |         | JL660A         |                    | Conductor       |
| 2 e4:de:40:9b:10:00     |         |         | JL659A         |                    | Standby         |
| 3 14:ab:ec:eb:81:80     |         |         | R8S91A         |                    | Member          |
| 4 14:ab:ec:eb:53:80     |         |         | R8S91A         |                    | Member          |
| Command History         |         |         |                |                    |                 |
| Release                 |         |         |                | Modification       |                 |
| 10.16.1000              |         |         |                | Commandintroduced. |                 |
| Command Information     |         |         |                |                    |                 |
| Platforms               | Command | context |                | Authority          |                 |
6200 config Administratorsorlocalusergroupmemberswithexecution
| 6300             |     |      |     | rightsforthiscommand. |     |
| ---------------- | --- | ---- | --- | --------------------- | --- |
| vsf split-detect |     | vlan |     |                       |     |
vsf split-detect
vlan <VLAN_ID>
no ...
Description
ConfigurestheVSFsplitdetectionmethodthatspecifiesthemechanismusedforstackfragment
discoverywhenthereisaVSFstacksplit.
Oncethestackfragmentsarediscovered,thefragmenthavingtheprimarymemberalwaystakes
precedence.Allnon-VSFinterfacesonthesecondarystackfragmentwillbebroughtdowntominimize
networkdisruptionduetoduplicateMAC/IPaddresses.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
vlan <VLAN_ID> ConfiguresaVLANasthesplitdetectionmethodonsupported
switches.Thismethodusestwoaccessports,onefromthe
primarymemberandonefromthesecondarymember.These
portsshouldbeconnectedonthesameL2network,therefore,
shouldnotbepartofanotherVLAN.TheVLANidentifiershould
VSFcommands|89

| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
bereservedandnotbeusedtocarryanydatatraffic.Range:2-
4094.
no ...
NegatesanyconfiguredparameterandremovestheVSF split
detectionconfiguration.
Example
| 6100(config)#                  | vlan      | 100          |                     |          |            |     |
| ------------------------------ | --------- | ------------ | ------------------- | -------- | ---------- | --- |
| 6100(config-vlan-100)#         |           | exit         |                     |          |            |     |
| 6300(config)#                  | interface |              | 1/1/1,2/1/1         |          |            |     |
| 6300(config-if-<1/1/1,2/1/1>)# |           |              |                     | vlan     | access 100 |     |
| 6100(config)#                  | vsf       | split-detect |                     | vlan     | 100        |     |
| 6100# show                     | vsf       |              |                     |          |            |     |
| Force Autojoin                 |           |              | : Disabled          |          |            |     |
| Autojoin Eligibility           |           | Status:      | Not                 | Eligible |            |     |
| MAC Address                    |           |              | : 90:20:c2:05:30:c0 |          |            |     |
| Secondary                      |           |              | : 2                 |          |            |     |
| Topology                       |           |              | : Chain             |          |            |     |
| Status                         |           |              | : No                | Split    |            |     |
| Split Detection                | Method    |              | : vlan              |          |            |     |
| Split Detection                | VLAN      |              | : 100               |          |            |     |
| Mbr Mac Address                |           |              | type                |          | Status     |     |
ID
| --- ------------------- |                     |            | -------------- |        | --------------- |               |
| ----------------------- | ------------------- | ---------- | -------------- | ------ | --------------- | ------------- |
| 1 90:20:c2:05:30:c0     |                     |            | JL675A         |        | Conductor       |               |
| 2 90:20:c2:06:30:40     |                     |            | JL676A         |        | Standby         |               |
| switch# show            | vsf split-detection |            |                | status |                 |               |
| Split Detection         | Method              |            |                |        |                 | : vlan        |
| Split Detection         | VLAN                |            |                |        |                 | : 100         |
| Split Detection         | VLAN                | interfaces |                |        |                 | : 1/1/1,2/1/1 |
| Split Detection         | Operational         |            | status         |        |                 | : Up          |
Theuserisadvisedtoconnectonlyonefront-planeportbetweentheConductorandStandby.Only
theseportsshouldbepartofadedicatedsplitdetectionVLAN(MADVLAN)asAccessports.However,if
morethanoneportontheConductororStandbyisconfiguredwithMADVLAN,theportselection
processwilldependonthefollowingconditions:
| Ifthecommandvsf |       |        |     | <VLAN-ID>isissuedaftermultipleportshavebeen |     |     |
| --------------- | ----- | ------ | --- | ------------------------------------------- | --- | --- |
| n               | split | detect |     | vlan                                        |     |     |
configuredwithMADVLAN,theportwiththelowestnumberwillbeselectedonboththeConductor
andStandby.
n Ifthecommandvsf split detect vlan <VLAN-ID>isissuedbeforeconfiguringmultipleportswith
MADVLAN,theportsareselectedbasedontheorderinwhichtheywereaddedtothesplitdetection
VLAN.
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 90

SplitdetectionVLANconfigurationisapplicableonlyonaccessportsandisnotsupportedontrunkor
aggregationinterfaces.
Splitdetectionportsareautomaticallyenabledforspanning-tree bpdu-filterwheneveraportis
configuredaspartofMADVLAN.Thisconfigurationisdisplayedintheshow running-configCLIoutput,even
iftheenduserhasnotexplicitlyconfiguredit.WhentheportisremovedfromMADVLAN,thespanning-tree
bpdu-filterconfigurationisalsoremovedfromthatport.
OncetheMADVLANisenabledonaport,itisrecommendednottoconfigureanyotherfeaturesonthesame
port.Similarly,spanning-tree bpdu-filtershouldnotberemovedfromtheportwhichispartofMADVLAN.
ThesplitdetectionportwillbeinablockedstatewheneveraportisconfiguredaspartoftheMADVLAN,andno
dataplanetrafficwillbeallowed.TheportwillbeunblockedwhenitisremovedfromtheMADVLAN
configuration.
| Command   | Information |         |           |     |
| --------- | ----------- | ------- | --------- | --- |
| Platforms | Command     | context | Authority |     |
config
| 4100i |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ----- | --- | --- | -------------------------------------------------- | --- |
| 6100  |     |     | rightsforthiscommand.                              |     |
vsf start-auto-stacking
vsfstart-auto-stacking
Description
ConfiguresthesecondarymemberandVSF linksautomatically.Tousethiscommand,theswitchmust
beinthefactorydefaultconfiguration.
Thiscommandisapplicableonlyontheprimaryswitch.Theprimaryswitchmustbeinfactorydefaultcondition
andmustnothaveanyVSFconfiguration.
Examples
ConfiguringaVSFsecondarymemberandVSFlinkonconductor:
| switch(config)# | vsf              | start-auto-stacking |           |              |
| --------------- | ---------------- | ------------------- | --------- | ------------ |
| This will       | configure        | links and           | secondary | on conductor |
| Do you          | want to continue | (y/n)?              | y         |              |
Runningtheconfigurationonnon-factorydefaultswitch:
| switch(config)# | vsf | start-auto-stacking |     |     |
| --------------- | --- | ------------------- | --- | --- |
The switch is having non-factory default running configuration.
| Command | is not applicable |     |     |     |
| ------- | ----------------- | --- | --- | --- |
Runningtheconfigurationonnon-primaryswitch:
VSFcommands|91

| switch(config)#     | vsf           | start-auto-stacking |                                             |
| ------------------- | ------------- | ------------------- | ------------------------------------------- |
| The command         | is applicable | only                | on Primary switch                           |
| Command History     |               |                     |                                             |
| Release             |               |                     | Modification                                |
| 10.16.1000          |               |                     | Commandintroducedon4100and6100Switchseries. |
| 10.07orearlier      |               |                     | --                                          |
| Command Information |               |                     |                                             |
| Platforms           | Command       | context             | Authority                                   |
config
| 4100 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
| 6100 |     |     | rightsforthiscommand.                              |
6200
6300
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 92

Chapter 7
|               |     |                 |                 | Configuration | conflict | finder |
| ------------- | --- | --------------- | --------------- | ------------- | -------- | ------ |
| Configuration |     | conflict finder | recommendations |               |          |        |
ConfigurationConflictFinder(CCF)issupportedonlyon6200and6300platforms.
ConfigurationConflictFinder(CCF)isaconfigurationtroubleshootingsolutionthatallowsadminsand
supporttoautomaticallydetermineswitchconfigurationanomaliesusingasetoffeatureconfiguration
templates.Thisensuresspecificfeaturesareerror-freeandvalidatestheswitch'sconfiguration.CCFis
anespeciallyusefultoolforCXusers,supportpersonnel,andERT.
CCFdetectsmisconfigurationsincluding:
n Incompleteorinter-dependentconfigurations
Mutuallyexclusiveconfigurations
n
CCFprovidesthefollowingrecommendationsforVSFenvironments:
Secondary is not configured in a stack of size larger than one
IftheVSFswitchisnotstandalone,thentherecommendationistoconfigurethesecondaryfor
redundancy.IfthesecondaryisnotconfiguredthenaSecondary
|     |     |     |     | member | is recommended | for vsf |
| --- | --- | --- | --- | ------ | -------------- | ------- |
stack (vsf secondary-member <mem-id>)recommendationisdisplayed.
| switch# | sh running-config |                | | line |     |     |     |
| ------- | ----------------- | -------------- | ------ | --- | --- | --- |
|         | 1 Current         | configuration: |        |     |     |     |
2 !
|     | 3 !Version          | ArubaOS-CX | FL.10.10.0000T-62-gb03e61e2b788a |     |     |     |
| --- | ------------------- | ---------- | -------------------------------- | --- | --- | --- |
|     | 4 !export-password: |            | default                          |     |     |     |
5 cli-session
|     | 6   | timeout 0 |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- |
7 !
8 !
9 !
10 !
11 !
12 !
|     | 13 ssh  | server vrf  | default |     |     |     |
| --- | ------- | ----------- | ------- | --- | --- | --- |
|     | 14 ssh  | server vrf  | mgmt    |     |     |     |
|     | 15 vsf  | member 1    |         |     |     |     |
|     | 16      | type r8s92a |         |     |     |     |
|     | 17 vsf  | member 2    |         |     |     |     |
|     | 18      | type jl668a |         |     |     |     |
|     | 19 vlan | 1           |         |     |     |     |
20 spanning-tree
|         | 21 interface | mgmt             |             |     |     |     |
| ------- | ------------ | ---------------- | ----------- | --- | --- | --- |
|         | 22           | no shutdown      |             |     |     |     |
|         | 23           | ip dhcp          |             |     |     |     |
| switch# | switch       | config-validator | feature vsf |     |     |     |
Line number 15: Secondary member is recommended for vsf stack (vsf secondary-
| member | <mem-id>) |     |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- |
Secondary is configured and stack split mode is not configured
93
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries)

Wheneverthesecondaryisconfigured,itisrecommendedtoconfiguresplitdetectiontoavoidmultiple
stackfragmentsbeingactiveatthesametime.TheSplit detect (MAD) is recommended for vsf
stack (vsf split-detect mgmt)recommendationisdisplayedifsplitdetectionisnotconfigured.
| switch# |     | sh running-config |                | | line |     |
| ------- | --- | ----------------- | -------------- | ------ | --- |
|         | 1   | Current           | configuration: |        |     |
2 !
|     | 3   | !Version          | ArubaOS-CX | FL.10.10.0000T-62-gb03e61e2b788a |     |
| --- | --- | ----------------- | ---------- | -------------------------------- | --- |
|     | 4   | !export-password: |            | default                          |     |
5 cli-session
|     | 6   | timeout | 0   |     |     |
| --- | --- | ------- | --- | --- | --- |
7 !
8 !
9 !
10 !
11 !
12 !
|     | 13  | ssh server           | vrf    | default |     |
| --- | --- | -------------------- | ------ | ------- | --- |
|     | 14  | ssh server           | vrf    | mgmt    |     |
|     | 15  | vsf secondary-member |        |         | 2   |
|     | 16  | vsf member           | 1      |         |     |
|     | 17  | type                 | r8s92a |         |     |
|     | 18  | vsf member           | 2      |         |     |
|     | 19  | type                 | jl668a |         |     |
|     | 20  | vlan 1               |        |         |     |
21 spanning-tree
|         | 22  | interface | mgmt             |     |             |
| ------- | --- | --------- | ---------------- | --- | ----------- |
|         | 23  | no        | shutdown         |     |             |
|         | 24  | ip        | dhcp             |     |             |
| switch# |     | switch    | config-validator |     | feature vsf |
Line number 15: Split detect (MAD) is recommended for vsf stack (vsf split-detect
mgmt)
| VSF links | are | administratively |     | shutdown |     |
| --------- | --- | ---------------- | --- | -------- | --- |
AdministrativelyshuttingdowntheVSFlinkswillaffecttheconnectivitytoothermembersofthestack
andmayresultinsplittingofthestackintomultiplefragments.AVSF interface should be
administratively uprecommendationisdisplayedwhenanyVSFlinksareadministrativelyshutdown.
| switch# |     | sh running-config |                | | line |     |
| ------- | --- | ----------------- | -------------- | ------ | --- |
|         | 1   | Current           | configuration: |        |     |
2 !
|     | 3   | !Version          | ArubaOS-CX | FL.10.10.0000T-62-gb03e61e2b788a |     |
| --- | --- | ----------------- | ---------- | -------------------------------- | --- |
|     | 4   | !export-password: |            | default                          |     |
5 cli-session
|     | 6   | timeout | 0   |     |     |
| --- | --- | ------- | --- | --- | --- |
7 !
8 !
9 !
10 !
11 !
12 !
|     | 13  | ssh server           | vrf      | default |     |
| --- | --- | -------------------- | -------- | ------- | --- |
|     | 14  | ssh server           | vrf      | mgmt    |     |
|     | 15  | vsf split-detect     |          | mgmt    |     |
|     | 16  | vsf secondary-member |          |         | 2   |
|     | 17  | vsf member           | 1        |         |     |
|     | 18  | type                 | r8s92a   |         |     |
|     | 19  | link                 | 1 1/1/25 |         |     |
|     | 20  | vsf member           | 2        |         |     |
Configurationconflictfinderrecommendations|94

| 21               | type jl668a |     |     |     |
| ---------------- | ----------- | --- | --- | --- |
| 22 vlan          | 1           |     |     |     |
| 23 spanning-tree |             |     |     |     |
| 24 interface     | mgmt.       |     |     |     |
.
.
.
.
.
| 123 interface  | 1/1/25            |         |                     |     |
| -------------- | ----------------- | ------- | ------------------- | --- |
| 124            | shutdown          |         |                     |     |
| 125 interface  | 1/1/26            |         |                     |     |
| 126            | no shutdown       |         |                     |     |
| 127            | no routing        |         |                     |     |
| switch# switch | config-validator  | feature | vsf                 |     |
| Line number    | 19: VSF interface | should  | be administratively | up  |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 95

Considerations and best practices

Chapter 8

Considerations and best practices

The following recommendations and restrictions apply to VSF.

n Before applying a configuration on a stack through checkpoint restore or TFTP/SFTP/USB download,
make sure that current VSF-specific configurations and the intended configurations match exactly. In
other words, the VSF stack and the intended configuration must have the same:

o Total number of members

o Member types

o Member number/ID

o VSF link configurations

n A functional stack must be configured with a standby for redundancy purposes. If the conductor fails

and there is no standby, the stack will fail.

n If the conductor fails and there is a standby device, the standby becomes the new conductor and will
take over stack management. When the old conductor device is replaced, it seamlessly becomes the
standby device for the stack and there no disruption.

The MAC address of the stack will remain the same until the entire stack is rebooted, after which the
stack MAC address will be the MAC address of the new conductor. However, once recovered, it is not
advisable to use the removed conductor elsewhere in the same network until the stack is rebooted to
avoid MAC address conflicts.

n After downloading firmware to a stack, the stack must be rebooted to complete the upgrade process.
Adding or rebooting individual members before the upgrade process is completed can cause the
individual member to fail while joining the stack. A member with 10.07 software version cannot join a
stack running on earlier versions.

n If there is a discrepancy between a VSF member link configuration on the conductor and the VSF

member link configuration on the member, the link configuration on the member is used.

n If there is a split, failure in the connectivity between management interfaces of the conductor and

standby might result in two active fragments. This issue can occur even if management split-detect is
enabled.

n Replacing member 1 in a stack without a standby with a new switch booted as member 1 will reset all

configurations on the stack.

n Do not connect a renumbered member to multiple primary devices through VSF links.

n Before removing an individual interface from VSF link using the command no link <x> <interface>,

ensure that the interface is admin shutdown at both local and peer ends. For example: Interface
1/1/25 on member 1 link 1 is connected to 2/1/25 on member 2 link 2. The user intends to remove
1/1/25 from link 1 of member 1. Both the interfaces 1/1/25 and 2/1/25 have to be admin shutdown
before actually removing them from the link configuration. To delete the link completely using the no
link <x> command, all individual interfaces in the VSF link have to be admin shutdown both at local
and peer ends.

n There may be instances in which a conductor switch with vsf secondary <id> configuration is
unable to discover the standby switch. In such cases, the conductor switch will wait for up to 6
minutes to detect the standby switch.

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

96

n When applying a configuration on a stack from Central/NetEdit/ZTP/TFTP or through a checkpoint

restore to remove members from the stack, consider the following recommendations:

a.

If you are removing members that are physically present, it is recommended to remove one
member at a time. In the case of ring topology, once a single member is removed, the
topology will get transitioned to a chain topology. After that, members must be removed
starting from the farthest end.

b.

If you are removing provisioned members, then you can remove multiple members at the
same time.

Removing more than one member at a time through configuration restoration

(ZTP/Central/Checkpoint) might result in non-deterministic behavior. This might cause the members

to reboot and drop to the console.

n If the entire stack configuration needs to be provisioned manually using CLIs, ensure that the

conductor’s VSF link configuration is done at the last.

n For TFTP download, the recommended work-flow is to copy the configuration to startup first, and
then copy to running-configuration. The direct download of TFTP to running-configuration is not
recommended.

n It is not recommended to change the VSF configurations (links & secondary) on the conductor when

one or more members of the stack are booting.

n On 4100i and 6100 platforms, it is recommended to use VSF ports with the same speed across the

stack.

n For SKUs S4P41A, S4P42A, S4P45A, and S4P46A, which support dual-mode SmartRate VSF ports, it is

recommended not to change the port speed while the stack is up.

n With split detection MAD VLAN, it is recommended to use only one VLAN ID and one front-plane port
from both the Primary and Secondary switches. Additionally, it is recommended not to enable any
other features on this VLAN ID and front-plane ports used with split-detection.

Considerations and best practices | 97

Chapter 9
Debugging and troubleshooting
| Debugging and | troubleshooting |     |     |
| ------------- | --------------- | --- | --- |
ThefollowingsectiondescribesfailureandrecoveryscenariosforVSF stacks.
Stack split
| Step 1: Verify | split has | occurred |     |
| -------------- | --------- | -------- | --- |
Usetheshow vsfcommandfromtheprimaryandsecondarymemberstodeterminewhetherornota
splithasoccurred.
OutputfromtheprimarymemberwilldisplayastackstatusofActiveFragmentandmemberstatusof
anymembersontheothersideofthesplitasInOtherFragment:
| switch# show         | vsf    |                     |          |
| -------------------- | ------ | ------------------- | -------- |
| Force Autojoin       |        | : Disabled          |          |
| Autojoin Eligibility |        | Status: Not         | Eligible |
| MAC Address          |        | : 08:97:34:b0:0e:00 |          |
| Egress Shape         |        | : Enabled           |          |
| Egress Shape         | Rate   | : None              |          |
| Secondary            |        | : 2                 |          |
| Topology             |        | : Chain             |          |
| Status               |        | : Active            | Fragment |
| Split Detection      | Method | : mgmt              |          |
98
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries)

| Mbr Mac | Address |     |     | type |     | Status |
| ------- | ------- | --- | --- | ---- | --- | ------ |
ID
| --- ------------------- |     |     |     | -------------- |     | ---------------   |
| ----------------------- | --- | --- | --- | -------------- | --- | ----------------- |
| 1 38:21:c7:5c:f4:c0     |     |     |     | JL668A         |     | Conductor         |
| 2                       |     |     |     | JL668A         |     | In Other Fragment |
| 3                       |     |     |     | JL668A         |     | In Other Fragment |
| 4                       |     |     |     | JL668A         |     | In Other Fragment |
OutputfromthesecondarymemberwilldisplayastackstatusofInactiveFragment,withmemberson
theothersideofthesplitlistedasInOtherFragment:
| switch#         | show        | vsf    |         |                     |          |          |
| --------------- | ----------- | ------ | ------- | ------------------- | -------- | -------- |
| Force Autojoin  |             |        |         | : Disabled          |          |          |
| Autojoin        | Eligibility |        | Status: | Not                 | Eligible |          |
| MAC Address     |             |        |         | : 08:97:34:b0:0e:00 |          |          |
| Egress Shape    |             |        |         | : Enabled           |          |          |
| Egress Shape    |             | Rate   |         | : None              |          |          |
| Secondary       |             |        |         | : 2                 |          |          |
| Topology        |             |        |         | : Chain             |          |          |
| Status          |             |        |         | : Inactive          |          | Fragment |
| Split Detection |             | Method |         | : mgmt              |          |          |
| Mbr Mac         | Address     |        |         | type                |          | Status   |
ID
| --- ------------------- |     |        |         | -------------- |     | ---------------   |
| ----------------------- | --- | ------ | ------- | -------------- | --- | ----------------- |
| 1                       |     |        |         | JL668A         |     | In Other Fragment |
| 2 38:21:c7:5c:77:40     |     |        |         | JL668A         |     | Conductor         |
| 3 38:21:c7:5a:a5:80     |     |        |         | JL668A         |     | Member            |
| 4 38:21:c7:5c:b3:00     |     |        |         | JL668A         |     | Member            |
| Step 2: Identify        |     | failed | link or | member         |     |                   |
Symptomsmayinclude:
a. NolinklightsforVSF linkportsbetweenstackmembers
b. Nopowertooneormorestackmembers
c. Eventlogsindicatinglossofconnectivitytooneormoremembersand/orVSF linksgoingdown
Utilizeshowcommands,eventlogs,andphysicalinspectionofstackmembersandassociatedcablingto
determinewhichlink(s) ormember(s) havefailedtocausethesplit.
| 6300# show | events |     | -r -d | vsfd |     |     |
| ---------- | ------ | --- | ----- | ---- | --- | --- |
---------------------------------------------------
| Event logs | from | current |     | boot |     |     |
| ---------- | ---- | ------- | --- | ---- | --- | --- |
---------------------------------------------------
2021-11-23T20:08:01.173123+00:00 6300 vsfd[732]: Event|9927|LOG_
| INFO|CDTR|1|Fragment |     |     | with | conductor |     | 1 is Active |
| -------------------- | --- | --- | ---- | --------- | --- | ----------- |
2021-11-23T20:07:59.400936+00:00 6300 vsfd[732]: Event|9924|LOG_INFO|CDTR|1|VSF
| link 1 is | down |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
2021-11-23T20:07:59.400841+00:00 6300 vsfd[732]: Event|9913|LOG_WARN|CDTR|1|Lost
| member 2 | with | Loss | of communication |     |     |     |
| -------- | ---- | ---- | ---------------- | --- | --- | --- |
2021-11-23T20:07:59.400733+00:00 6300 vsfd[732]: Event|9908|LOG_
| INFO|CDTR|1|Topology |     |     | is  | Standalone |     |     |
| -------------------- | --- | --- | --- | ---------- | --- | --- |
2021-11-23T20:07:58.534186+00:00 6300 vsfd[732]: Event|9924|LOG_INFO|CDTR|1|VSF
Debuggingandtroubleshooting|99

| link 2          | is down |            |        |         |        |
| --------------- | ------- | ---------- | ------ | ------- | ------ |
| Step 3: Recover |         | or replace | failed | link or | member |
IfthesplitwascausedbythefailureofastackmemberorVSF linkcable,replacetheaffectedhardware.
Ifthesplitwascausedbyamisconfiguration,suchasinadvertentlydisablingoneormoreVSF linksor
otherwisemodifyingthestackconfiguration,reverttheapplicableconfigurationchanges.Ifthe
configurationchangeresultedinremovingmembersfromthestack,re-addthosemembersas
appropriate.
| Step 4: Verify | proper | stack | operation |     |     |
| -------------- | ------ | ----- | --------- | --- | --- |
Oncethecauseofthesplithasbeenidentifiedandcorrected,verifythatthestackisoperatingnormally.
| switch(config)# |             | show   | vsf                 |          |        |
| --------------- | ----------- | ------ | ------------------- | -------- | ------ |
| Force Autojoin  |             |        | : Disabled          |          |        |
| Autojoin        | Eligibility |        | Status: Not         | Eligible |        |
| MAC Address     |             |        | : 38:21:c7:5c:f4:c0 |          |        |
| Egress          | Shape       |        | : Enabled           |          |        |
| Egress          | Shape       | Rate   | : None              |          |        |
| Secondary       |             |        | : 2                 |          |        |
| Topology        |             |        | : Ring              |          |        |
| Status          |             |        | : No                | Split    |        |
| Split Detection |             | Method | : mgmt              |          |        |
| Mbr Mac         | Address     |        | type                |          | Status |
ID
| --- ------------------- |     |     | -------------- |     | --------------- |
| ----------------------- | --- | --- | -------------- | --- | --------------- |
| 1 38:21:c7:5c:f4:c0     |     |     | JL668A         |     | Conductor       |
| 2 38:21:c7:5c:77:40     |     |     | JL668A         |     | Standby         |
| 3 38:21:c7:5a:a5:80     |     |     | JL668A         |     | Member          |
| 4 38:21:c7:5c:b3:00     |     |     | JL668A         |     | Member          |
| Misconfiguration        |     |     | recovery       |     |                 |
Ifaswitchfailstojointhestack,orfailstorejoinafterareboot,duetomisconfiguration,usethe
followingproceduretorestoretheswitchbacktoafactorydefaultconfiguration.
Theusermusthavemanagementconnectivitytothefailedmemberforsupportfilesfromthememberin
recoverymode.
1. PressCtrl+Contheswitchconsole.
Ifthememberisnotabletoreachconductor,itwillgotorecoveryconsoleafter10minutes.You
canpressCtrl+Ctoredirecttheswitchtotherecoveryconsoleimmediately.
2. Loginusingadministratorcredentials.
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 100

3. At the prompt, issue the erase all zeroize command.

^C
Login: admin
Password:

recovery# erase all zeroize

4. This resets the member to factory-default settings and the switch will come up with a default

member ID of 1.

5. Now the user can reconfigure the VSF link and renumber it to the preferred member ID.

The no vsf member <id> command can also be used for switch recovery, if support files from lost members
must be preserved in a local copy.

VSF switchover behaviors

The following behaviors are expected during a VSF switchover event:

n The count of console login attempts is cleared (reset to 0).

n The count of login attempts for the aaa authentication limit-login-attempts feature is cleared

(reset to 0).

n The output of the command show authentication locked-out-users list is cleared of users locked

out via the console.

n The output of the command show authentication locked-out-users list is cleared of users locked

out via SSH, TELNET, or REST (verified on an SSH channel.)

Debugging and troubleshooting | 101

Chapter 10

Frequently asked questions

Frequently asked questions

General

What is VSF?

Virtual Switching Framework, or VSF, defines a single virtual switch comprised of multiple individual
physical switches that are interconnected through standard Ethernet links. These links are referred to as
VSF links.

These physical switches will function as one device with a unified control and management plane.

Multiport VSF links are supported.

What are the supported platforms for VSF?

The HPE Aruba Networking 4100, 6100, 6200F and 6300F/M/L Switch Series support VSF.

VSF can be formed with the following switch models:

n HPE Aruba Networking 6300F/M/L Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A,

JL664A, JL665A, JL666A, JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A, S0X44A,
S0G03A, S0G05A, S0F99A, S0G01A, S0G96A, S0G98A, S4P48A, S0G04A, S0G06A, S0G00A, S0G95A,
S0G97A, S0G02A, S3L75A, S3L76A, S3L77A, S4P41A,S4P42A, S4P43A, S4P44A, S4P45A, S4P46A,
S4P47A, S4P49A)

n HPE Aruba Networking 6200F Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A,

R8Q68A, R8Q69A, R8Q70A, R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8V13A, R8Q72A,
JL724B, JL725B, JL726B, JL727B, JL728B, S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,
S0M87A,  S0M88A,  S0M89A,  S0M90A, S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

n HPE Aruba Networking 4100i Switch series (JL817A, JL818A)

n HPE Aruba Networking 6100 Switch series (JL675A, JL676A, JL677A, JL678A, JL679A, R9Y04A)

HPE Aruba Networking 6200F Switch Series only supports fixed SKUs.

Can I create a stack with a mix of different switch models?

No, a VSF stack cannot be created with a mix of different switch families. The stack must be made up of
only a single switch model type. For example, a VSF stack can include either 4100i, 6100, 6200 or 6300
switches, but not a mix. Additionally:

n 6200 switch series models with SKUs R8Q72A and R8V13A can only stack with other R8Q72A and

R8V13A SKUs

n 6100 Switch series models with SKU JL679A can stack on with other JL679A SKUs

n 6300L switch series models with SKUs S3L75A, S3L76A, and S3L77A can only stack with other 6300L

S3L75A, S3L76A and S3L77A SKUs.

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

102

Can I form a stack with a mix of 6200 switch series such as R8Q72A and any other SKU
other than R8Q72A or R8V13A?

No, an R8Q72A SKU switch can stack only with switches of type RQ72A or R8V13A SKU.

Can I form a stack with a mix of 6100 switch series JL679A and any other 6100 SKU,
other than JL679A?

No, a 6100 JL679A SKU switch can stack only with switches of type JL679A .

Can I form a stack with S3L75A, S3L76A, S3L77A and any other 6300 switches?

No, S3L75A, S3L76A, and S3L77A SKUs can only stack with other S3L75A, S3L76A, and S3L77A SKUs and
cannot stack with other 6300 switches.

What port speeds do VSF links support?

n 4100: Connections between the switches must use 1G or 10G links.

n 6100: Connections between the switches must use 1G or 10G links.

n 6200F: Connections between the switches must use 1G SFP/SFP+ either with 1G copper downlink

ports, 10G links, or SmartRate ports.

n 6300: Connections between the switches must use 10G, 25G, or 50G links.

The VSF stack, containing only the S0E91A and S0X44A SKUs, supports 10G, 25G, and 100G speed
links. If a VSF stack includes a mix of S0E91A/S0X44A SKU and other SKUs, then it supports 10G, 25G
VSF links, SmartRate ports and only.

HPE Aruba Networking recommends that all VSF links be configured to run at the same speed.

On S4P41A, S4P42A, S4P45A, and S4P46A SKUs, can I change the speed of dual mode
smartRate ports when the stack is up with smartRate ports?

No, changing the speed of dual mode smartRate ports when the stack is up can cause the stack to split
and lead to network instability.

On S4P41A, S4P42A, S4P45A, and S4P46A SKUs, how do I change the speed of dual mode
smartRate VSF ports when the stack is up?

To change the speed of dual mode smartRate VSF ports on S4P41A, S4P42A, S4P45A, and S4P46A SKUs
when the stack is up, follow these steps:

1. The stack must first be dismantled using erase all zeroize command. This will reset all stack

members and bring them up as standalone units.

2. After dismantling, reconfigure the port group corresponding to the VSF links with desired port

speed using system interface-group <GROUP> member <MEMBER-ID> speed <SPEED> command.

3. Once reconfiguration is complete, bring the stack up again with the new port speed settings.

On S4P41A, S4P42A, S4P45A, and S4P46A SKUs, how do I change the speed of dual mode
smartRate VSF ports interconnected between 2 members when the stack is up?

To change the speed of dual mode smartRate VSF ports interconnected between 2 members when the
stack is up, follow these steps:

1. Unconfigure the desired members using no vsf member <member_id> command. This will reset

the desired members and bring them up as a standalone units.

Frequently asked questions | 103

2. >Once the units are up as a standalone, reconfigure the port group corresponding to the VSF links
with desired port speed using system interface-group <GROUP> member <MEMBER-ID> speed
<SPEED> command.

3. Once reconfiguration is complete, configure the members to join the stack back.

Can VSF be disabled?

Users cannot disable VSF. A factory default switch boots up as a VSF-enabled device with its Member ID
set to 1.

What is a primary switch in VSF stack? Is it configurable?

Only the switch with a Member ID of 1 will be the primary switch in a VSF stack. This switch will function
as the stack conductor and will drive the control and management plane for the stack.

What is a secondary switch in a VSF stack? Is it configurable?

The secondary switch will function as the standby in a stack. In the case of auto-stacking, secondary
member is automatically configured through button press or vsf start-auto-stacking command.

In addition, any member other than Member 1 can be configured manually as the secondary switch
using the vsf secondary-member <MEMBER-ID> command.

HPE Aruba Networking strongly recommends that you configure a secondary member (standby) for
stack high-availability.

How many secondary member switches are configurable in a VSF stack?

A VSF stack can be configured with one secondary member only.

Once it is configured, is it possible to change the secondary member?

Yes, a new secondary member can be configured using the vsf secondary-member <MEMBER-ID>
command. The old standby device will boot first and join the stack with the member role. Then, the
newly configured secondary member will go for boot and join the stack with the standby role.

The secondary member configuration can only be changed when Member 1 is conductor of the stack.

How are conductor and standby for a stack determined?

By default, the primary member (Member 1) becomes the conductor of the stack and the user-
configured secondary member becomes the standby.

The secondary member synchronizes all its states with the conductor. If the current conductor (Member
1) fails, the standby (secondary member) will seamlessly transition to the conductor role. In this state, if
Member 1 comes back up, it will take the standby role.

Only primary and secondary members can take up conductor and standby roles in a stack.

What is the role of other members in a stack?

All devices other than the conductor and standby are called members. These devices do not have any
network, control, or management plane functions. Their interfaces are directly controlled and managed
by the conductor switch.

Is there any restriction in the order of VSF member numbering?

There is no restriction on the order in which VSF members can be numbered. Each member, however,
must have a unique number in the range of 1-10 (for 6300 switches) or 1-8 (for 6200F switches).

What is the supported stack height and topology?

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

104

n 4100platformscanstackuptofourmembers.
n 6100platformscanstackuptosixmembers.
6200FplatformscanstackuptoeightmemberswithnomodularSKU(onlyfixedSKU).
n
n 6300F/Mand6300Lplatformscanstackuptotenmembersinachainorringtopology.
Ringistherecommendedtopology.Thistopologyrequiresthateachmemberisconfiguredwithtwo
VSFlinks,interconnectingeachmemberwithtwoothermembersinthestack.
| Can features | be configured |     | on a VSF | link? |     |
| ------------ | ------------- | --- | -------- | ----- | --- |
OnceaninterfacebecomespartofaVSFlink,nostandardnetworklayerprotocolorfeaturecanrunon
thatinterfacebecauseitispartoftheVSFstackfabric.
Will configurations in an individual member switch be retained after joining a stack?
Individualmemberdeviceconfigurationsarenotretainedaftertheswitchisrenumberedandbecomes
partofastack.
| How do | the consoles | of each | member | in a stack | work? |
| ------ | ------------ | ------- | ------ | ---------- | ----- |
TheconsoleoftheconductorswitchprovidesafullCLIthatcanbeusedtomanagethestack.Consoles
ofotherstackmembers,includingthestandby,havealimitedsetofCLIcommandsthatareusefulfor
troubleshootingthedevicefromastackingfunctionalitystandpoint.
| How does | an image | upgrade | for a stack | work? |     |
| -------- | -------- | ------- | ----------- | ----- | --- |
Toupgradeastacktoanewfirmwareimage,usethecopy <TFTP/SFTP> imagecommandtodownload
theimagetothedevice.Theimagewillbedownloadedtothestackconductorfirstandthensynced
withothermembersofthestackautomatically.
Afterdownloadingthefirmware,rebootthestackusingtheboot system <PRIMARY/SECONDARY>
command.Thisactioncompletestheupgradeprocess.
Addingorrebootingindividualmembersbeforetheupgradeprocessiscompletecancausethe
individualmembertofailwhilejoiningthestack.
| Is two-member | ring | supported | ?   |     |     |
| ------------- | ---- | --------- | --- | --- | --- |
Atwo-memberringtopologyisnotsupportedon4100and6100seriesswitches.Forlink-levelredundancyin
two-memberstacks,itisrecommendedtobundlemultipleinterfacesintoasingleVSFlinkusingachain
topology.
Yes.ItissupportedfromAOS-CX10.07onwards.
| show run        | vsf:             |          |     |     |     |
| --------------- | ---------------- | -------- | --- | --- | --- |
| switch(config)# |                  | show run | vsf |     |     |
| vsf             | secondary-member | 2        |     |     |     |
| vsf             | member 1         |          |     |     |     |
type jl668a
link 1 1/1/26
link 2 1/1/25
| vsf | member 2 |     |     |     |     |
| --- | -------- | --- | --- | --- | --- |
type jl668a
link 1 2/1/25
link 2 2/1/26
show vsf:
Frequentlyaskedquestions|105

| switch(config)# |             |             | show vsf |                     |          |        |     |
| --------------- | ----------- | ----------- | -------- | ------------------- | -------- | ------ | --- |
| Force           | Autojoin    |             |          | : Disabled          |          |        |     |
| Autojoin        |             | Eligibility | Status:  | Not                 | Eligible |        |     |
| MAC             | Address     |             |          | : 90:20:c2:20:a2:80 |          |        |     |
| Egress          | Shape       |             |          | : Enabled           |          |        |     |
| Egress          | Shape       | Rate        |          | : None              |          |        |     |
| Secondary       |             |             |          | : 2                 |          |        |     |
| Topology        |             |             |          | : Ring              |          |        |     |
| Status          |             |             |          | : No                | Split    |        |     |
| Split           | Detection   |             | Method   | : None              |          |        |     |
| Mbr             | Mac Address |             |          | type                |          | Status |     |
ID
| --- | ------------------- |     |     | -------------- |     | --------------- |     |
| --- | ------------------- | --- | --- | -------------- | --- | --------------- | --- |
| 1   | 90:20:c2:20:a2:80   |     |     | JL668A         |     | Conductor       |     |
| 2   | 38:21:c7:5a:a5:40   |     |     | JL668A         |     | Standby         |     |
topology:
show vsf
switch#
|           | sh       | vsf topology |     |     |     |     |     |
| --------- | -------- | ------------ | --- | --- | --- | --- | --- |
| Conductor |          | Standby      |     |     |     |     |     |
| +-------+ |          | +-------+    |     |     |     |     |     |
| |         | 1 |1==1| |              | 2 | |     |     |     |     |
| +-------+ |          | +-------+    |     |     |     |     |     |
|           | 2        |              | 2   |     |     |     |     |
+========+
Can I add a member to the VSF stack when the member is running an image with a
| different | version | than | the | stack? |     |     |     |
| --------- | ------- | ---- | --- | ------ | --- | --- | --- |
Whenadevicejoinsastackanditsfirmwareversionisdifferentfromtheversionontheconductor,the
conductorwillpushitsfirmwarecopytothedevice.Oncethedevicereceivesacopyofthefirmware,it
willrebootandrejointhestack,nowrunningthesameversionastheconductor.
Thisisnotsupportedifeithermembersortheconductorrunningonfirmwarepriorto10.07version.
| What | happens | when | the VSF | conductor |     | switch goes | down? |
| ---- | ------- | ---- | ------- | --------- | --- | ----------- | ----- |
Thestandbyswitch,ifpresent,willtaketheroleoftheconductor.Theoldconductorswitchwillboot
andjointhestackasthestandbyswitch.Thistransitionwillbeseamlesswithlimitednetworkimpact.
Intheabsenceofastandby(nosecondarymemberconfiguration),conductordevicefailurecausesthe
remainingVSFmemberstorebootandcomebackup.Atthispoint,memberswillenterastateinwhich
theyarewaitingfortheconductortocomebackup.Duringthistime,frontplaneportsofthemembers
willbedown.
How do I recover a device that has not joined a stack due to misconfiguration?
Thevsf renumber-tocommandisusedtotriggeradevicetotakeupitsnewmembernumberandlight
upitsVSFlinks.Thiscommandcausesthedevicetoreboot,comebackupandwaitformessagesfrom
thestackconductor.IftheVSFlinkisconfiguredincorrectlyorthemembernumberiswrong,thedevice
couldbewaitinginthisstateindefinitely.
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 106

To recover a device in this state, execute the following commands:

1. Execute the ctrl+c command on the device console. This action launches the recovery console.

2. Execute the erase all zeroize command on the recovery console.

This action resets the device to factory-default.

n The device will come back up as member ID 1 with no VSF link configuration.

n The device can be configured with the correct member number and VSF links.

n The vsf renumber-to command will trigger this configuration to take effect.

The recovery console also has commands that allow the user to copy support files to an external server.
This functionality is useful for troubleshooting stacking-related issues.

How do the management ports of each member in a stack work?

In a stack, only the conductor management interface is active. The management interface can be
assigned an IP address for device management purposes. When a conductor device fails, the standby
becomes conductor and activates its management interface.

How does replacing the conductor switch in a stack work?

The replacement device must be of the same part number as the switch being replaced. You must also
have a standby switch configured for replacing the conductor of a stack without losing configuration.

Complete the following steps:

1. Execute the vsf switchover command to trigger the standby switch to take over the conductor

role.

2. Once the stack is up with the new conductor, remove all physical connections from the old

conductor switch that is being replaced.

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

Frequently asked questions | 107

n Whenastacksplitsandtheconductorandstandbyofthestackbecomepartoftwodifferent
fragments,thestandbytakesuptheconductorroleforitsfragment.Networkdisruptioncanresult
becausethetwofragmentsaresimultaneouslyactive.HPEArubaNetworkinghighlyrecommends
enablingVSFsplit-detectiontogracefullyhandlesplitbrainscenarios.
Ifastacksplitsandtheconductorandstandbyareinthesamefragmentwiththeothermemberson
n
adifferentfragment,themembers-onlyfragmentwill:
o Reboot.
o Comebackup.
o Waitforcommunicationfromthestackconductor.
| What | is VSF split-detect? |     |     |     |     |     |
| ---- | -------------------- | --- | --- | --- | --- | --- |
Whenastacksplits,thesplit-detectfeatureprovidesamechanismforthefragmentstodiscovereach
other.
Oncethetwostackfragmentsarediscovered,thefragmentthathastheprimarymemberbecomesthe
activefragmentandkeepsitsfrontplane(non-VSF)interfacesupandrunning.Theotherfragment
becomesinactiveandallnon-VSFinterfacesontheinactivefragmentarebroughtdowntoavoid
networkdisruption.
| How do | I configure | split-detect? |     |     |     |     |
| ------ | ----------- | ------------- | --- | --- | --- | --- |
6200and6300switchseriessupportsplit-detectionthroughthemanagementinterface.
Connectthemanagementinterfacesoftheprimaryandsecondarymemberstothesamemanagement
VLAN/networkorconnectthemdirectlytooneanother.
| n TheCLIcommandtoenablesplitdetectionisvsf |             |              |     |           | split-detect | mgmt. |
| ------------------------------------------ | ----------- | ------------ | --- | --------- | ------------ | ----- |
| How do                                     | I configure | split-detect |     | using MAD | VLAN?        |       |
The4100iand6100platformssupportsplit-detectionusingadedicatedMulti-ActiveDetection(MAD)
VLANandfront-planeports.
Toenablesplit-detection:
n Physical Connection:Connectoneofthefront-planeportsoftheprimarymembertooneofthe
front-planeportsofthesecondarymember.Ensurebothportsareeither:Connectedtothesame
managementVLAN/network,orDirectlyconnectedtoeachother.
n VLAN Configuration:ReserveadedicatedVLAN(e.g.,VLANID100)forsplit-detection.
CLI Commands
Usethefollowingcommandstoenablesplit-detection:
| 6100(config)#                  |             | vlan      | 100          |                     |     |     |
| ------------------------------ | ----------- | --------- | ------------ | ------------------- | --- | --- |
| 6100(config-vlan-100)#         |             |           | exit         |                     |     |     |
| 6300(config)#                  |             | interface | 1/1/1,2/1/1  |                     |     |     |
| 6300(config-if-<1/1/1,2/1/1>)# |             |           |              | vlan access         | 100 |     |
| 6100(config)#                  |             | vsf       | split-detect | vlan 100            |     |     |
| 6100#                          | show        | vsf       |              |                     |     |     |
| Force                          | Autojoin    |           |              | : Disabled          |     |     |
| Autojoin                       | Eligibility |           | Status:      | Not Eligible        |     |     |
| MAC                            | Address     |           |              | : 90:20:c2:05:30:c0 |     |     |
| Secondary                      |             |           |              | : 2                 |     |     |
| Topology                       |             |           |              | : Chain             |     |     |
| Status                         |             |           |              | : No Split          |     |     |
AOS-CX10.16.xxxVirtualSwitchingFramework(VSF)Guide|(4100i,6100,6200,6300SwitchSeries) 108

| Split | Detection   |     | Method | : vlan |        |     |
| ----- | ----------- | --- | ------ | ------ | ------ | --- |
| Split | Detection   |     | VLAN   | : 100  |        |     |
| Mbr   | Mac Address |     |        | type   | Status |     |
ID
| ---     | ------------------- |     |                 | -------------- | --------------- |               |
| ------- | ------------------- | --- | --------------- | -------------- | --------------- | ------------- |
| 1       | 90:20:c2:05:30:c0   |     |                 | JL675A         | Conductor       |               |
| 2       | 90:20:c2:06:30:40   |     |                 | JL676A         | Standby         |               |
| switch# | show                | vsf | split-detection | status         |                 |               |
| Split   | Detection           |     | Method          |                |                 | : vlan        |
| Split   | Detection           |     | VLAN            |                |                 | : 100         |
| Split   | Detection           |     | VLAN interfaces |                |                 | : 1/1/1,2/1/1 |
| Split   | Detection           |     | Operational     | status         |                 | : Up          |
ReplaceinterfacenumbersandVLANIDasappropriateforyourdeployment.
| How do | I remove | the | non-VSF | configurations | in a stack? |     |
| ------ | -------- | --- | ------- | -------------- | ----------- | --- |
Usetheerase startup-configcommandontheVSFstack.Thisactionwillremoveallnon-VSFrelated
configurationsfromthestartup-config.Thenrebootthestack.
| Can a | VSF member |     | be removed | from a | stack? |     |
| ----- | ---------- | --- | ---------- | ------ | ------ | --- |
Yes,removeamemberfromthestackusingtheno vsf member <MEMBER-ID>command.All
configurationsassociatedwiththememberwillalsoberemoved.Thememberwillbootandcomeback
upwiththefactorydefaultconfiguration.
| How do | I remove | the | conductor | switch | from the stack? |     |
| ------ | -------- | --- | --------- | ------ | --------------- | --- |
HPEArubaNetworkingdoesnotrecommendremovingamemberthatisconductorofastack.
Iftheconductorswitchhastoberemoved,completeaswitchoverandwaitfor:
n thestandbytotakeuptheconductorrole,and
n theoldconductortorebootandjointhestackasstandby.
Thenuseamemberremovecommandtoremovethedevicefromthestack.
How can I boot the whole VSF stack and individual members using CLI?
| Theboot | systemcommandcanbeusedtobootthewholestack. |     |     |     |     |     |
| ------- | ------------------------------------------ | --- | --- | --- | --- | --- |
Tobootanindividualmember,usethevsf
member
rebootcommand.
<MEMBER-ID>
Is modifying the VSF-specific configuration using Checkpoint restore or TFTP/SFTP/USB
| download | supported? |     |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- | --- |
Thisfunctionalityisnotsupported.BeforeapplyingaconfigurationonastackthroughCheckpoint
restoreorTFTP/SFTP/USBdownload,youmustensurethatthefollowingconfigurationsmatchexactly:
n ThecurrentstackVSFconfigurations.
n TheVSFconfigurationsthatarepartoftheconfigurationfilethatisbeingrestoredordownloaded
fromtheserver.
Specifically,thecurrentVSFstackandtheCheckpoint/downloadedconfigurationthatwillbeappliedon
thestackmusthavethesame:
Frequentlyaskedquestions|109

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

The copy support-files all command executed on the conductor console will collect support and
troubleshooting information from all members that are part of the stack.

If a member is not part of the stack, you must run the same command from the recovery console of the
respective member.

If a stack has split into two fragments, both fragments will have a conductor. Execute the same
command on the conductor console of both fragments.

Can VSF configurations be changed when some of the members are booting?

No. It is recommended to change VSF configurations only when the stack is in steady state.

To ensure that there is no stack split , it is recommended to form the VSF stack in the ring topology
before changing the VSF configurations. This might result in reboot of some of the members.

Is there a way to troubleshoot if the members did not join the stack?

Yes. Use the show vsf link error-details command to check if any of the VSF links are down due to
error scenarios. For most of the error scenarios, corrective action is also recommended to resolve the
issue.

Does the command '[no] vsf egress-shape' have any effect on a stack that has no stack
members of type S0E91A & S0X44A?

No. VSF port shaping feature ensures seamless stacking between S0E91A/S0X44A SKU and other 6300
SKUs. The S0E91A and S0X44A SKU have a speed limit of 100G ports, while the speed limit of other 6300
SKUs are limited up to 50G ports. To ensure that all VSF interfaces run at the lowest common speed
supported by the entire VSF stack, port shaping is used when the stack has at least one member of type
S0E91A or S0X44A.

How does VSF port shaping apply when VSF link has multiple interfaces?

VSF port shaping will ensure VSF links to run at the lowest common speed irrespective of the number of
interfaces configured on a VSF link given that the stack consist one or more stack member of type
S0E91A or S0X44A. VSF port shaping will be calculated based on all the active VSF interfaces which
include multiple interfaces configured on a VSF link.

What happens to VSF port shaping when I remove a stack member of type S0E91A or
S0X44A from the stack?

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

110

When the stack consist of only one stack member of type S0E91A or S0X44A, the VSF port shaping will
be removed from all the active VSF interfaces and the VSF stack operates at the default speed of the VSF
interfaces. Whereas when the stack has more that one stack member of type S0E91A or S0X44A, VSF
port shaping will be applied on the active VSF interfaces based on the new lowest common speed
calculated.

Auto-stacking

Is it mandatory to connect the new switch in the direction of the higher-numbered
conductor port after configuring the VSF links on the conductor for auto-stacking?

Yes. Auto-stacking process always starts only in the direction of the higher-numbered VSF link port on
the conductor. If no switches are connected to the end of the stack connected to the higher-numbered
port, the auto-stacking process will not start.

If a new switch being added to the stack is connected in the direction of the lower-numbered port on
the conductor, the conductor will show it as an error. Use the show vsf link error-detail command
to see the error and its recommendation to fix the error.

In this example, Switch3 will join the stack only when it is connected in the direction of the higher-
numbered port on the conductor (i.e. to port 1/1/50 on Switch2) as shown in the following figure:

Can the size of the stack be extended in the direction of lower denomination port of
the conductor?

No. You can still renumber manually and add the members to the stack. But the newly added member
will not join the stack automatically through auto-stacking.

What are the different methods to designate the conductor to bring up a stack using
auto-stacking?

There are five different ways to designate the conductor and bring up the stack using auto-stacking. The
different ways are:

1. Configuring the VSF links manually on the conductor switch.

2. Executing the vsf start-auto-stacking command using CLI on the conductor switch.

3. Pressing the Stk LED mode button on the conductor switch.

4. Downloading full stack configuration using ZTP.

5. Downloading full stack using TFTP, SFTP, NetEdit, or REST.

Do all platforms support auto-stacking by pressing the Stk LED mode button on the
conductor switch?

No, Auto-stacking by pressing the Stk LED mode button on the conductor switch is supported only on
6200 and 6300 platforms. This feature is not available on other VSF supported platforms.

What happens when the conductor is designated manually by configuring the lower-
numbered port as VSF port first?

Frequently asked questions | 111

This can potentially lead to formation of out-of-order stack since auto stacking happens only in the
direction of highest denomination port. If physical connections are already made, the newly added
switch might not join the stack.

What is the eligibility criteria for a switch to be connected to an existing stack through
auto-stacking?

For a switch to connect to an existing stack, it must be in the auto-join eligible state. A switch in its
factory default state is considered to be auto-join eligible.

When will a switch become auto-join eligible? Is there a way to make a switch auto-
join eligible again to take part in the auto-join process to form the stack?

If a switch moves out of factory default configuration state, then the switch cannot join an existing stack.

In this case, use the vsf force-auto-join command to make a non-factory default switch to auto-join
eligible again. Once the user sets force auto-join in the switch configuration, the switch will be
considered as auto-join eligible and will join the stack even though the switch does not have factory
default configuration.

vsf force-auto-join command will only work if the switch does not have any pre-existing VSF
configurations such as secondary or VSF links. If the switch has VSF configurations already, then the
recommendation is to unconfigure and reconfigure vsf force-auto-join once all VSF configurations
are removed from the switch.

Is it mandatory to use only the internally reserved ports to bring up a stack through
auto-stacking ?

If you need to form a stack using vsf start-auto-stacking command or by pressing Stk LED mode
button, then it is mandatory to use the internally reserved VSF ports.

Based on the product type of a switch, the following two interfaces are reserved for the auto-stacking
process:

n 12-port switch models: 13 and 14

n 24-port switch models: 25 and 26

n 40-port switch models: 41 and 42

n 48-port switch models: 49 and 50

If auto-stacking via zero-touch provisioning is being used to build the stack, any of the four SFP ports on
each member can be used for VSF links.

Can a stack be formed through auto-stacking when the conductor is running on 10.07
firmware version and the newly added member is running on firmware version prior
to 10.07?

No. It is mandatory to have all the switches running on 10.7 or later releases to form a stack through
auto-stacking .

You cannot form a stack through auto-stacking if either conductor or the stack members running on
different firmware versions prior to 10.07.

Will a stack be formed if the Stk mode button is pressed on all the members before
physically connecting the cables?

No. Pressing the Stk mode button on all the members will configure VSF links and secondary on the
switches which will make the members not eligible for auto-join. The members will join with the stack
only when it becomes auto-join eligible again.

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

112

Pressing Stk LED mode button is to designate the conductor. So, press Stk LED mode button only on
the switch which is supposed to be the conductor of the stack. There should be only one conductor for a
VSF stack.

Will a stack be formed if vsf start-auto-stacking is executed on all the members before
connecting the cables physically?

No. Executing the vsf start-auto-stacking command will configure VSF links and secondary on a
switch which will make the switch not eligible for auto-join, The members will join with the stack only
when they become auto-join eligible again.

Executing vsf start-auto-stacking is to designate the conductor. So, execute the command on the
switch which is supposed to be the conductor of the stack. There should be only one conductor for a
VSF stack.

What will happen if Stk mode button is pressed on the conductor of an active stack?

Since the VSF configurations are already present , pressing the Stk mode button will not have any effect
on the stack configuration. But the LEDs of the stack will now glow to depict the state of the stack.

For more details on the LED states, Stack and Port LED states

What will happen if the vsf start-auto-stacking command is executed on the conductor
of an active stack?

Since the VSF configurations are already present , configuring vsf start-auto-stacking will not have
any effect on the stack configuration. An error message also will be displayed to show that the switch
does not have factory default configuration.

After downloading the VSF stack configuration to the conductor through
TFTP/ZTP/NetEdit, what happens if a new member added has a different SKU than the
one provisioned for that particular member-id through auto-stacking?

If the existing stack size configuration is less than maximum size supported (4 for 4100i switch series, 6
for 6100 switch series, 8 for 6200 switch series and 10 for 6300 switch series), the newly added member
will join the stack with the least member-id available, but not with the provisioned member id.

If the existing stack size configuration is already the maximum size supported, then the newly added
member will go for a reboot , but will not join the stack. This member will again come up with the
factory default configuration as there is a SKU mismatch.

What happens if the Stk mode button is pressed when the cables are not connected
properly on the reserved interfaces, later connected correctly on the reserved
interfaces?

Members switches go for a reboot and join the stack when the cables are connected on the reserved
interfaces correctly.

Is multi-port VSF configuration supported to bring up a VSF stack through auto-
stacking?

Forming a stack using auto-stacking with multi-ports can be done only when the configuration of all the
members are fully pre-provisioned on Member 1.

By default, Stk mode button press or vsf start-auto-stacking command configures only one port
per VSF link. So even if multiple ports were connected physically, stack will come up with single port per
VSF link only.

Frequently asked questions | 113

Can cables of different speed be connected to the members to form a stack through
auto-stacking?

Cables of different speed are only supported on 6200 and 6300 switch series.

It is always recommended to have the entire stack with cables of the same speed for VSF links.

Do 4100i and 6100 platforms support different port speeds for VSF links?

No, the 4100 and 6100 platforms do not support different port speeds for VSF links. All VSF member
links must operate at the same speed on these platforms.

Do 4100i and 6100 platforms support using 1G Copper port and 10G SFP+ port for VSF
links?

No, 4100i and 6100 platforms do not support using a 1G Copper port and a 10G SFP+ port for VSF links
to form a stack. Stack can be formed by either using 1G Copper port or 10G SFP+ for VSF links across the
stack.

On 4100i and 6100 platforms, how to recover a member that has entered recovery
mode due to using a VSF port with a different speed?

To recover a member that has entered recovery mode due to using a VSF port with a different speed,
follow these steps:

1. Use the erase all zeroize command from the recovery console of the affected member. This

will reset the device and bring it up as a standalone unit.

2. Once the device is up as a standalone, configure the VSF ports with desired port speed and then

bring up the member.

On 4100i and 6100 platforms, how do you change the speed of the VSF links from 1G to
10G (or vice versa) when the stack is up?

To change the speed of the VSF links from 1G to 10G (or vice versa) when stack is up, follow these steps:

1. The stack must first be dismantled using the erase all zeroize command. This will reset all the

members in the stack and bring them up as standalone units.

2. After dismantling, configure VSF links with desired port speed and bring the stack up again with

the new port speed.

What happens when non-reserved ports of the newly added switch is connected to the
auto-stacking reserved ports of member 1?

Newly added member will not go for a reboot unless there is a provisioned configuration of the member
matching with non-reserved ports on member 1.

To use Stk mode button or vsf start-auto-stacking command, the cables must be connected to the
reserved interfaces on the new switch to start the auto-stacking process. For more information on
reserved interfaces, see Reserved interfaces for auto-stacking

Can the Stk mode button or vsf start-auto-stacking command be used on a switch
which has some VSF configuration already?

No. To use Stk mode button or vsf start-auto-stacking command, the switch must be in factory-
default configuration.

Is there a way to download configuration automatically after forming a stack via Stk
mode button press?

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

114

Yes. Once the stack is formed , ztp force-provision will be automatically enabled on the stack. But
you must have an uplink connectivity to DHCP Server (which can provide the ZTP options) and TFTP
server to download the firmware and configuration files.

Can I download the full stack configuration via TFTP to the running configuration
directly?

Full stack configuration can be downloaded into the conductor of the stack. The recommendation is to
first download the configuration to the start-up and then move the startup to the running configuration.
Copying the configuration first to startup will help in detecting errors in the deployed configuration.
Once the configuration is copied to startup without any errors, then the startup configuration can be
applied to the running configuration. This will also ensure that auto-stacking process did not start
prematurely. The stacking process might start prematurely if the configuration is applied directly to the
running configuration.

How to check whether the switch is auto-join eligible or not?

Executing the show vsf or show vsf details command shows an entry called Autojoin Eligibility
Status which shows whether the switch is eligible or not eligible .

Is it possible to change the secondary member of the stack which is formed through
vsf start-auto-stacking or stk mode button press?

Yes. You can execute the vsf secondary-member <member-id> on the conductor to change the
secondary member. This will reboot the member 2 (default secondary) and make it to join the stack as
member. Then the newly configured secondary member will go for a reboot and joins the stack as
standby. Changing the secondary member can only be done from the primary switch (member 1).

Will the switch stay as auto-join eligible if any new VSF configurations are made after
executing the vsf force-auto-join command?

No. vsf force-auto-join is a command used to make an auto-join ineligible switch to auto-join eligible
again. If the VSF configuration of the switch gets changed again after executing the vsf force-auto-
join command, the switch will become auto-join ineligible again. When the VSF configurations are
removed , switch will automatically become auto-join eligible.

What happens if a member configuration is removed from the conductor of a stack
using the no vsf member <id> command?

If the member is part of the stack (not in “Not Present” state) and its ports are connected through
reserved auto-stacking ports, then the removed switch will join back the stack after it comes up as
standalone. This is because the auto-stacking starts on the reserved ports. So, after member removal,
make sure you immediately disconnect the cables physically as well.

Will both auto-stacking and ZTP process start simultaneously if the conductor is
designated using the configuration download through ZTP,?

No. The auto-stacking process will start only after the completion of ZTP process.

Is there any difference between forming the stack using the vsf start-auto-stacking
command and Stk mode button?

There is no difference in forming the stack. But the ztp force-provision configuration will be added in
addition to the VSF related configurations only when the stack is formed using the Stk mode button
press. If the stack has an uplink connectivity to DHCP server, then the configuration and firmware for
the stack can be downloaded from a TFTP server through ZTP.

Frequently asked questions | 115

Does auto-stacking support ring topology without the need for any configuration
changes?

Yes. By default, auto-stacking feature configures two links on each of the VSF members. In case, if there
is a need to change the stack from chain to ring topology, connect the first member with the last
member of the stack with a cable on the auto-stacking reserved ports.

For example, consider the three-member stack in a chain topology as shown in the following figure:

To change this into ring topology, connect Switch3 and Switch1 as shown in the following figure:

The three-member VSF Stack in chain topology can also be converted into a four-member VSF stack in
Ring topology by connecting the Switch4 to port 1/1/50 of Switch3 and port 1/1/49 of Switch1 as shown
in the following figure:

Can I use reserved auto-stacking interfaces as normal data ports?

Yes. The reserved auto-stacking interfaces can be used as normal data ports.

Can I form a 10G dual-mode SmartRate VSF using ZTP provisioning on the conductor?

No. When the conductor is provisioned with a configuration specifying 10G speed, it tries to establish a
10G link over the VSF ports. However, the member switch is not preconfigured for 10G and defaults to
its native speed of 5G. As a result, the VSF link operates at 5G instead of the intended 10G. To achieve
the desired 10G link, the member switch must be preconfigured with the appropriate speed settings
before provisioning.

What happens to the VLAN MAD status when performing a dynamic standby change?

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

116

When the standby role is assigned to a new member, the VLAN MAD configuration on the previous
standby is removed, causing the VLAN MAD interface to go down. To restore functionality, the VLAN
MAD interface must be reconfigured on the new standby member.

Frequently asked questions | 117

Chapter 11

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

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

118

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
SupportandOtherResources|119

(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.16.xxx Virtual Switching Framework (VSF) Guide | (4100i, 6100, 6200, 6300 Switch Series)

120