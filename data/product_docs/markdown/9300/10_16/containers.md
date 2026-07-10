| AOS-CX | 10.16.xxxx |     |     | Containers |     |
| ------ | ---------- | --- | --- | ---------- | --- |
Guide
| (6300F/M, | 6400, | 8xxx, | 9xxx, | 100xx | Switch |
| --------- | ----- | ----- | ----- | ----- | ------ |
Series)
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

For more information, see the KM Process Guide. ?>
Acknowledgments

Bluetooth is a trademark owned by its proprietor and used by Hewlett Packard Enterprise under license.

AOS-CX 10.16.xxxx Containers Guide | (6300F/M, 6400, 8xxx, 9xxx, 100xx Switch Series)

3

Contents
| About                                         | this document |           | 5   |
| --------------------------------------------- | ------------- | --------- | --- |
| Applicableproducts                            |               |           | 5   |
| Latestversionavailableonline                  |               |           | 5   |
| Commandsyntaxnotationconventions              |               |           | 5   |
| Abouttheexamples                              |               |           | 6   |
| Identifyingswitchportsandinterfaces           |               |           | 7   |
| Identifyingmodularswitchcomponents            |               |           | 8   |
| Container                                     | overview      |           | 9   |
| Supportedswitches                             |               |           | 9   |
| USBpersistentstorage                          |               |           | 10  |
| Restartprotection                             |               |           | 10  |
| vSphere                                       | agent         |           | 11  |
| InstallationandConfigurationofthevSphereagent |               |           | 11  |
| Showcommands                                  |               |           | 12  |
| Supportedswitches                             |               |           | 14  |
| USBpersistentstorage                          |               |           | 15  |
| Restartprotection                             |               |           | 15  |
| Container                                     | management    | commands  | 15  |
| container                                     |               |           | 15  |
| containerexec                                 |               |           | 16  |
| enable(containermanager)                      |               |           | 17  |
| env                                           |               |           | 18  |
| image-location                                |               |           | 20  |
| mount(containermanager)                       |               |           | 22  |
| networkvrf                                    |               |           | 23  |
| port-map(containermanager)                    |               |           | 24  |
| restrictcpu                                   |               |           | 26  |
| restrictmemory                                |               |           | 27  |
| showcontainer                                 |               |           | 28  |
| showcapacitiescontainers                      |               |           | 30  |
| showcapacities-statuscontainers               |               |           | 31  |
| showrunning-configcontainer                   |               |           | 31  |
| vrf(containermanager)                         |               |           | 33  |
| Support                                       | and Other     | Resources | 34  |
| AccessingHPEArubaNetworkingSupport            |               |           | 34  |
| AccessingUpdates                              |               |           | 35  |
| WarrantyInformation                           |               |           | 35  |
| RegulatoryInformation                         |               |           | 35  |
| DocumentationFeedback                         |               |           | 35  |
4
AOS-CX10.16.xxxxContainersGuide| (6300F/M,6400,8xxx,9xxx,100xxSwitchSeries)

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing HPE Aruba Networking switches on
a network.

Applicable products

This document applies to the following products:

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

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

AOS-CX 10.16.xxxx Containers Guide | (6300F/M, 6400, 8xxx, 9xxx, 100xx Switch Series)

5

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

About this document | 6

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

On the HPE Aruba Networking 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.
The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the HPE Aruba Networking 6400 Switch Series

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

AOS-CX 10.16.xxxx Containers Guide | (6300F/M, 6400, 8xxx, 9xxx, 100xx Switch Series)

7

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

Container overview
Container overview
TheContainerManagerfeatureallowscontainerstoruninsideanAOS-CXswitch.Itallowstheswitchto
launchmultiplecontainerimages,whetherHPE-signedorunsigned,andprovidestoolstomanage,
maintain,andmonitorthelifecycleoftheseimagesandcontainers.Applicationscanberunwithinthe
containerinfrastructure,turningthemintocontainerizedapplications.
TheAOS-CXcontainerinfrastructureisdesignedtosupportcontainersthatruninthebackgroundas
servicesorscheduledjobs.Thesecontainerseitherkeeprunningcontinuouslyorstopgracefullyafter
completingtheirtasks.ExamplesofsupportedworkloadsincludewebserverslikeNginxorApache,
applicationserversbuiltwithNode.js,Java,orPythonAPIs,andsystemmonitoringtools.
Thecontainerinfrastructuredoesnotsupportcontainersthatmustinteractusersinrealtimethrougha
command-lineinterface,suchasshells(bash,sh),interpreters(Python,Node.js),ortext-basedtools(like
vimortop)toacceptuserinputanddisplayoutputinteractively.Ifyoutrytodeployanunsupported
containerthatreliesonaninteractiveterminal,itmaystopimmediatelyorbehaveunpredictably.
| Supported | switches |     |
| --------- | -------- | --- |
Thefollowingswitchplatformsarevalidatedfordatacenterdeployments.Theagentitselfhasnocontext
abouttheswitchthatitisinstalledon,exceptthatthechipsetarchitecturemustbeeitherx86_64orarm.
Thecontainerimagesizeislimitedbyplatform.Acontainerinstancewilldisplayanerrorifyouattemptto
downloadacontainerimagethatexceedsthesupportedimagesize.
Chipset
Maximum Image
| Switch | Architecture |     |
| ------ | ------------ | --- |
size (MiB)
Type
| 6300  | arm    | 500  |
| ----- | ------ | ---- |
| 6400  | arm    | 500  |
| 8100  | arm    | 500  |
| 8320  | x86_64 | 1000 |
| 8325  | x86_64 | 1000 |
| 8325H | x86_64 | 1000 |
| 8325P | x86_64 | 1000 |
| 8360  | arm    | 500  |
| 8400  | x86_64 | 500  |
| 9300  | x86_64 | 1000 |
| 9300S | x86_64 | 1000 |
9
| AOS-CX10.16.xxxxContainersGuide| | (6300F/M,6400,8xxx,9xxx,100xxSwitchSeries) |     |
| -------------------------------- | ------------------------------------------ | --- |

Switch

10000

10040

Chipset
Architecture
Type

x86_64

x86_64

Maximum Image
size (MiB)

1000

1000

The HPE Aruba Networking CX vSphere agent is a containerized agent developed for data center applications.

The plugin consumes memory and CPU that would otherwise be allocated to the switch. Thus, the targeted

platforms have higher system resources. Those resources are capped to prevent its interference with

performance of the switch.

The solution was tested and qualified on the platforms listed here. Other platforms may work at low scale, but

they are not recommended outside of the lab or test environments due to the resource requirements for

vSphere.

USB persistent storage

Containers can mount additional persistent storage via a USB device using the mount, source and
destination commands to create a mount ID and specify the mount source and destination paths. Best
practices is to configure persistent storage via these commands. If a USB directory in the source
filesystem is deleted or renamed through shell commands, the container may not function correctly.

The USB persistent storage feature includes the following additional caveats.

n Containers are not aware if the configured USB device is unmounted, disabled or physically

removed. As a result, the container's correct functionality can't be guaranteed if these actions are
made without unconfiguring the container mount first.

n For containers using USB persistent storage functionality, data won't synchronize between the
management modules after a High Availability event, so the container deployed on the new
management module won't have access to the USB device connected to the previous management
module.

n If there is an issue with the USB device mount when the container boots up, there can be a potential

wait of up to two minutes before the container shows an error.

Restart protection

The HPE Aruba Networking switch can prevent a crashing containerized application from restarting
after three restarts within a brief period of time. Once the restart protection feature indicates that it has
stopped a crashing application in this manner, the container will display a run failed status in the
output of the show container command.

If the configured image has been downloaded and verified by container manager, in case of a restart,
the image will not need to be downloaded again unless the image location is modified. This also applies
when using the allow-unsigned parameter, if a re-download is required, modify the image location URL
or remove the command and add it again.

Container overview | 10

Chapter 3

vSphere agent

vSphere agent

The HPE Aruba Networking CX vSphere agent allows administrators to trace how Virtual Machines are
connected to the physical switches. The ability to visualize how a Virtual Machine connects to a CX port
helps to resolve connectivity issues. This functionality helps operators in several troubleshooting
scenarios, such as diagnosing a connectivity issue, or ensuring adequate distribution of VMs across the
physical infrastructure.

You can install the vSphere agent on one or many of the switches in the fabric. You can perform the
following tasks, from any switch where the agent is installed:

1. Run the show VMs command to list all the VMs managed by the vCenter Appliance integrated with
the agent. This functionality also helps to view VMs connections to the ports on other switches on
the fabric.

2. Search for a specific VM by name. To find the connection between the VM and a switch port,

attach the switch to at least one host managed by the integrated vCenter.

The show neighbors command examines the LLDP data that is advertised from any switch to a distributed virtual

switch and provides connection details for third-party switches.

For technical information on containers, including use cases, example configurations and best practices,
view the AOS-CX Container Enhancements video on the HPE Aruba Networking broadcasting channel on
YouTube. For more information about cloud capabilities of vSphere agent, refer to vSphere Integration.

Installation and Configuration of the vSphere agent

To install a container, perform the following steps:

1. Download the vSphere agent from the HPE Aruba Networking support portal and select the arm

or x86_64 architecture for the switch platform. Refer to the list of supported switches to select the
corresponding architecture.

2. Host the agent on a local network that can be accessed using the HTTP protocol. Limitations of

the container framework prevent usage of the HTTPs protocol. The HTTP server must be
reachable on the mgmt or any other configured VRF.

To create the container configuration:

1. Enter the config command to enter the config context.

2. Create and enter the config-container-<name> context using the container command.

3. From the config-container-<name> context, configure the container image location using the

image-location command. To create a container configuration that bypasses signature validation,
include the optional allow-unsigned parameter for the image-location command

4.

(Optional) Configure a container environment variable using the env command.

AOS-CX 10.16.xxxx Containers Guide | (6300F/M, 6400, 8xxx, 9xxx, 100xx Switch Series)

11

5. (Optional)TocreateaconfigurationwithVRFnetworkconnectivity,issuethenetworkvrf
command,thenconfigureportmappingusingtheport-mapcommand.
6. (Optional)TocreateaconfigurationthatlimitsCPUusagetoapercentageofthetotalswitchCPU,
usetherestrictcpucommand.
7. (Optional)Tocreateaconfigurationthatlimitsmemoryresourcestomaximumnumberof
megabytes(upto20%ofthetotalswitchmemory),usetherestrictmemorycommand.
8. (Optional)Tocreateaconfigurationwithmountedstorage,issuethemountcommand,thenuse
thesourceanddestinationparametersfromwithintheconfig-container-mount-<id>context
todefinethemountsourceanddestination.
9. Fromtheconfig-container-<name>context,enablethecontainerusingtheenablecommand.
10. Issuetheshowcontainercommandtovalidatethecontainerstatus.
Show commands
Therearefourtop-levelshowcommands.
n vms-showsvirtualmachineconnectioninformation.
n connection-status-showsinformationaboutconfiguredvSpherevCenters.
n neighbors-showslearnedneighborinformation(Note:ThisinformationislearnedfromLLDPon
vCenterdistributedvswitches,nottheswitch).
n help-showsagentversion,description,andconfigurableenvironmentvariables.
show vms
ThefollowingshowcommanddescribesthestatusoftheconnectiontovSphere,andshowtheVMsthat
areattachedtoswitches:
Atleastonecommandparametermustbeusediftheparametersareavailable.
Forexample,withtheshowvmscommand,weforceuseofthebriefoptionsotheuserisawareofall
availableoptions.
Ifnotspecified,allcommandsdefaulttobrief.
igor-sw-02# container vsphere exec show vms brief Hypervisor VM Name Physical
| Switch Connections |     |     | Interface |     |     |     |     |
| ------------------ | --- | --- | --------- | --- | --- | --- | --- |
laser-02-esxi.lab.plexxi.com vm4 laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/3 vm2 laser-
| sw-02 (b8:d4:e7:da:40:00) |     |     |     | 1/1/4 |     |     |     |
| ------------------------- | --- | --- | --- | ----- | --- | --- | --- |
laser-sw-02 (b8:d4:e7:da:40:00) 1/1/3 vm5 laser-sw-02 (b8:d4:e7:da:40:00) 1/1/4
laser-sw-02 (b8:d4:e7:da:40:00) 1/1/3 laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/3
laser-01-esxi.lab.plexxi.com vm1 laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/1 vm3 laser-
| sw-01 (b8:d4:e7:d9:af:00) |                     |     |     | 1/1/2 |     |     |     |
| ------------------------- | ------------------- | --- | --- | ----- | --- | --- | --- |
| laser-sw-02               | (b8:d4:e7:da:40:00) |     |     | 1/1/1 |     |     |     |
igor-sw-02# container vsphere exec show vms vm-name vm4 Hypervisor VM Name
| Physical | Switch | Connections |     | Interface |     |     |     |
| -------- | ------ | ----------- | --- | --------- | --- | --- | --- |
laser-02-esxi.lab.plexxi.com vm4 laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/3 igor-sw-02#
container vsphere exec show vms vm-name vm4 detailed VM Name : vm4
| Hypervisor  | :     | laser-02-esxi.lab.plexxi.com |         |          |           | Vendor | : vmware      |
| ----------- | ----- | ---------------------------- | ------- | -------- | --------- | ------ | ------------- |
| Hostname    | : vm4 |                              |         |          |           |        |               |
| OS : CentOS | 4/5   | or                           | later   | (64-bit) | VM status |        | : on          |
| Virtual     | NIC : | Network                      | adapter | 2 IP     | Address   | :      | 172.20.12.204 |
| MAC Address | :     | 00:50:56:89:3c:bf            |         | Virtual  |           | Switch | : dvs4        |
| Port Group  | :     | dpg4 Vlan                    | :       | 0        |           |        |               |
vSphereagent|12

| Physical | Switch | Connections       |     |     | Interface | :    | 1/1/3         |     |
| -------- | ------ | ----------------- | --- | --- | --------- | ---- | ------------- | --- |
| Chassis  | ID :   | b8:d4:e7:d9:af:00 |     |     | Switch    | Name | : laser-sw-01 |     |
Switch Description : HPE_ANW JL635A GL.10.12.0001G Management Address :
172.20.11.253
Container exec commands are top-level, and can be run in any CLI context.
igor-sw-02# container vsphere exec show connection-status brief Hypervisor Last
| Sync Connection |     | State |     |     |     |     |     |     |
| --------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
laser-vcsa.lab.plexxi.com 2023-03-17 23:30:03 connected igor-sw-02# config
igor-sw-02(config)# container vsphere exec show connection-status brief Hypervisor
| Last Sync | Connection |     | State |     |     |     |     |     |
| --------- | ---------- | --- | ----- | --- | --- | --- | --- | --- |
laser-vcsa.lab.plexxi.com 2023-03-17 23:30:07 connected igor-sw-02(config)#
| interface | 1/1/1 |     |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
igor-sw-02(config-if)# container vsphere exec show connection-status brief
| Hypervisor                | Last | Sync | Connection |            | State |          |           |     |
| ------------------------- | ---- | ---- | ---------- | ---------- | ----- | -------- | --------- | --- |
| laser-vcsa.lab.plexxi.com |      |      |            | 2023-03-17 |       | 23:30:15 | connected |     |
show vms
ThiscommanddisplaystheconnectivitystatusforthevSphereagent..
TheconnectiontimestampisupdatedwheneverasuccessfulconnectionismadewiththevSphere
agent.Thesynctimestampisupdatedwheneverafullsync,eventpoll,oreventprocessoccurs.
igor-sw-02(config-container-vsphere)# container vsphere exec show connection-
| status                    | brief | Hypervisor |     | Last       | Sync | Connection | State     |     |
| ------------------------- | ----- | ---------- | --- | ---------- | ---- | ---------- | --------- | --- |
| laser-vcsa.lab.plexxi.com |       |            |     | 2023-03-18 |      | 02:36:06   | connected |     |
igor-sw-02(config-container-vsphere)# container vsphere exec show connection-
| status          | detailed | Hypervisor |            | :   | laser-vcsa.lab.plexxi.com |        |            |          |
| --------------- | -------- | ---------- | ---------- | --- | ------------------------- | ------ | ---------- | -------- |
| Connection      | State    | :          | connected  |     | Last                      | Sync : | 2023-03-18 | 02:35:08 |
| Last Connection |          | :          | 2023-03-18 |     | 02:35:09                  |        |            |          |
igor-sw-02(config-container-vsphere)# container vsphere exec show connection-
| status | detailed | Hypervisor |     | :   | laser-vcsa.lab.plexxi.com |     |     |     |
| ------ | -------- | ---------- | --- | --- | ------------------------- | --- | --- | --- |
Connection State : disconnected Last Sync : 2023-03-18 02:04:05
| Last Connection |         | :   | 2023-03-18 |     | 02:09:30 |             |          |     |
| --------------- | ------- | --- | ---------- | --- | -------- | ----------- | -------- | --- |
| Connection      | Failure |     | Reason     | :   | Could    | Not Resolve | Hostname |     |
show neighbors
showneighborscommanddisplaysthevirtualnetworkadapterneighborinformation.
NeighborsarepulledfromdistributedvirtualswitchesofthevSphereandcachedlocally.Neighborsare
usedtomapVMstophysicalswitchports.
Ifyoudonotseeaneighborontheport,youwillnotseeanyVMconnectivityonthatporteither.
Detailedandbriefoptionsareavailable.Filteringcanbedoneonswitch-nameand/orinterface.
igor-sw-02(config-container-vsphere)# container vsphere exec show neighbors brief
| Chassis           | ID Switch |     | Name        | Interface |       |       |     |     |
| ----------------- | --------- | --- | ----------- | --------- | ----- | ----- | --- | --- |
| b8:d4:e7:da:40:00 |           |     | laser-sw-02 |           | 1/1/1 | 1/1/2 |     |     |
| b8:d4:e7:d9:af:00 |           |     | laser-sw-01 |           | 1/1/1 | 1/1/2 |     |     |
igor-sw-02(config-container-vsphere)# container vsphere exec show neighbors
| detailed | Chassis | ID  | : b8:d4:e7:da:40:00 |     |     |     |     |     |
| -------- | ------- | --- | ------------------- | --- | --- | --- | --- | --- |
AOS-CX10.16.xxxxContainersGuide|(6300F/M,6400,8xxx,9xxx,100xxSwitchSeries) 13

| Switch | Name : laser-sw-02 |     |     |
| ------ | ------------------ | --- | --- |
Switch Description : HPE_ANW JL635A GL.10.10.1000 Management Address :
192.168.200.1
| Interface | : 1/1/1 Advertisement  | Type : lldp | TTL : 102     |
| --------- | ---------------------- | ----------- | ------------- |
| Interface | : 1/1/2 Advertisement  | Type : lldp | TTL : 102     |
| Chassis   | ID : b8:d4:e7:d9:af:00 | Switch Name | : laser-sw-01 |
Switch Description : HPE_ANW JL635A GL.10.10.1000 Management Address :
192.168.200.0
| Interface | : 1/1/1 Advertisement | Type : lldp | TTL : 102 |
| --------- | --------------------- | ----------- | --------- |
| Interface | : 1/1/2 Advertisement | Type : lldp | TTL : 102 |
| Supported | switches              |             |           |
Thefollowingswitchplatformsarevalidatedfordatacenterdeployments.Theagentitselfhasno
contextabouttheswitchthatitisinstalledon,exceptthatthechipsetarchitecturemustbeeitherx86_
64orarm.Thecontainerimagesizeislimitedbyplatform.Acontainerinstancewilldisplayanerrorif
youattempttodownloadacontainerimagethatexceedsthesupportedimagesize.
Chipset
|        |              | Maximum | Image |
| ------ | ------------ | ------- | ----- |
| Switch | Architecture |         |       |
size (MiB)
Type
| 6300  | arm    | 500  |     |
| ----- | ------ | ---- | --- |
| 6400  | arm    | 500  |     |
| 8100  | arm    | 500  |     |
| 8320  | x86_64 | 1000 |     |
| 8325  | x86_64 | 1000 |     |
| 8325H | x86_64 | 1000 |     |
| 8325P | x86_64 | 1000 |     |
| 8360  | arm    | 500  |     |
| 8400  | x86_64 | 500  |     |
| 9300  | x86_64 | 1000 |     |
| 9300S | x86_64 | 1000 |     |
| 10000 | x86_64 | 1000 |     |
| 10040 | x86_64 | 1000 |     |
TheHPEArubaNetworkingCXvSphereagentisacontainerizedagentdevelopedfordatacenterapplications.
ThepluginconsumesmemoryandCPUthatwouldotherwisebeallocatedtotheswitch.Thus,thetargeted
platformshavehighersystemresources.Thoseresourcesarecappedtopreventitsinterferencewith
performanceoftheswitch.
vSphereagent|14

The solution was tested and qualified on the platforms listed here. Other platforms may work at low scale, but

they are not recommended outside of the lab or test environments due to the resource requirements for

vSphere.

USB persistent storage

Containers can mount additional persistent storage via a USB device using the mount, source and
destination commands to create a mount ID and specify the mount source and destination paths. Best
practices is to configure persistent storage via these commands. If a USB directory in the source
filesystem is deleted or renamed through shell commands, the container may not function correctly.

The USB persistent storage feature includes the following additional caveats.

n Containers are not aware if the configured USB device is unmounted, disabled or physically removed.

As a result, the container's correct functionality can't be guaranteed if these actions are made
without unconfiguring the container mount first.

n For containers using USB persistent storage functionality, data won't synchronize between the
management modules after a High Availability event, so the container deployed on the new
management module won't have access to the USB device connected to the previous management
module.

n If there is an issue with the USB device mount when the container boots up, there can be a potential

wait of up to two minutes before the container shows an error.

Restart protection

The HPE Aruba Networking switch can prevent a crashing containerized application from restarting after
three restarts within a brief period of time. Once the restart protection feature indicates that it has
stopped a crashing application in this manner, the container will display a run failed status in the
output of the show container command.

If the configured image has been downloaded and verified by container manager, in case of a restart,
the image will not need to be downloaded again unless the image location is modified. This also applies
when using the allow-unsigned parameter, if a re-download is required, modify the image location URL
or remove the command and add it again.

Container management commands

container
container <CONTAINER-NAME>
no container <CONTAINER-NAME>

Description

Enters into the container configuration context.

The no form of this command removes the existing configurations of the specified container.

AOS-CX 10.16.xxxx Containers Guide | (6300F/M, 6400, 8xxx, 9xxx, 100xx Switch Series)

15

Parameter

Description

<CONTAINER-NAME>

Example

Configures a new container:

The container name can contain up to 64 characters. Only
letters, numbers and underscore ( _ ) characters are
permitted

switch(config)# container app
The feature being used requires a AOS-CX Advanced Software Feature Pack.
For more information,refer to the AOS-CX Feature Pack Deployment Guide.

AOS-CX does not enforce the requirement to own a feature pack prior to using container features. This
warning message is displayed only during creation, subsequent calls to the container context will not
display the message.

Command History

Release

10.12

Command Information

Modification

Command introduced

Platforms

Command context

Authority

config
config-container-<CONTAINER-NAME>

Administrators or local user group members
with execution rights for this command.

6300, except
for S3L75A,
S3L76A and
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

container exec
container <NAME> exec <PARAMS>

Description

Allows the execution of an endpoint script in the container. The location of this endpoint is provided to
the container manager infrastructure through a manifest file in the image file system of the container.
This manifest file provides metadata related to the container application. When the exec command

Container management commands | 16

runs, the manifest information is used to determine the endpoint to execute and the user parameters
are passed directly to the endpoint. The output of such execution is provided directly to the user
through the CLI. In case the manifest information or the endpoint file are missing an error is presented
to the user. The user can interrupt the execution by pressing Ctrl+C.

If the container is not operational when the command is executed, the following error message is returned:

Failed to execute endpoint - The container is not operational.

Parameter

Description

<NAME>

exec

<PARAMS>

Command History

Release

10.12

Command Information

Specifies a container name up to 64 characters long.

Runs a container application command.

Specifies container command parameters.

Modification

Command introduced

Platforms

Command context

Authority

config-container-<CONTAINER-NAME>

Administrators or local user group members
with execution rights for this command.

6300, except
for S3L75A,
S3L76A and
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

enable (container manager)
enable
no enable

Description

A container is disabled by default when it is created. Use the enable command to enable the container.

AOS-CX 10.16.xxxx Containers Guide | (6300F/M, 6400, 8xxx, 9xxx, 100xx Switch Series)

17

The no version of this command disables the container. When an enabled container is disabled, system
resources are released but the container configuration settings are stored.

Example

Enabling and then disabling the container test:

switch(config-container-test)# enable
switch(config-container-test)# no enable

Command History

Release

10.16.1000

Command Information

Modification

Command introduced

Platforms

Command context

Authority

config-container-<CONTAINER-NAME>

Administrators or local user group members
with execution rights for this command.

6300, except
for S3L75A,
S3L76A and
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

env
env <NAME> {value <VALUE>}|{encrypted [plaintext <VALUE>|ciphertext <VALUE>]}
no env <NAME> {value <VALUE>}|{encrypted {plaintext|ciphertext}<VALUE>}

Description

Configures an environment variable for a container that is composed of a key and a value pair. The key-
value pair defines the behavior of the environment in a container and is used by the container
processes. The value of the environment variable can be stored in the host system as an encrypted
value. The container manager infrastructure provides the decrypted value to the container.

The no form of this command removes the configured environment variable from a container.

Configuring the env variable for an already operational container causes the container to restart if the container

has already been enabled.

Container management commands | 18

| Parameter     |     |     | Description                                         |     |
| ------------- | --- | --- | --------------------------------------------------- | --- |
| <NAME>        |     |     | Specifiesthenameofthecontainerenvironmentvariables. |     |
| value <VALUE> |     |     | Specifiesthevariablevalue.                          |     |
| encrypted     |     |     | Encryptstheenvironmentvariablevalue.Ifyoupress      |     |
<enter>aftertheencryptedparameter,youwillentera
variableconfigurationmodethatallowsyoutosecurely
enterahiddenvalue.Thisistherecommendedmethodfor
enteringanencryptedvariable
plaintext <VALUE> Optional.Specifiesthevariablevalueinplaintext.Not
recommendedforencryptedvariables.
ciphertext <VALUE> Optional.Specifiesthevariablevalueaspreviously
encryptedtext.Recommendedforencryptedvariables;specify
theencryptedvariablevalueaspreviouslyencryptedtext.
Example
Securelyenteringanencryptedvariable:
| 6300(config-container-test)# |          | env    | TEST encrypted                                  |     |
| ---------------------------- | -------- | ------ | ----------------------------------------------- | --- |
| Enter environment            | variable | value: | ********                                        |     |
| 6300(config-container-test)# |          | end    |                                                 |     |
| Command History              |          |        |                                                 |     |
| Release                      |          |        | Modification                                    |     |
| 10.13.1000                   |          |        | Theplaintextandciphertextoptionsfortheencrypted |     |
parameterarenowoptional.Startingwiththisrelease,youcan
usetheencryptedoptiontoencrypttheenvironmentvariable
andspecifythevalueinplaintexthiddenfromtheCLI.
| 10.12               |         |         | Commandintroduced |           |
| ------------------- | ------- | ------- | ----------------- | --------- |
| Command Information |         |         |                   |           |
| Platforms           | Command | context |                   | Authority |
6300,except config-container-<CONTAINER-NAME> Administratorsorlocalusergroupmembers
| forS3L75A, |     |     |     | withexecutionrightsforthiscommand. |
| ---------- | --- | --- | --- | ---------------------------------- |
S3L76Aand
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
AOS-CX10.16.xxxxContainersGuide|(6300F/M,6400,8xxx,9xxx,100xxSwitchSeries) 19

Platforms

Command context

Authority

8400
9300
9300S
10000
10040

image-location
image-location <URL> vrf <VRF-NAME> [allow-unsigned]
no image-location <URL> <VRF-NAME> [allow-unsigned]

Description

Configures the image location for a container. Modifying image location prompts an image upgrade.

The no form of this command removes the configured location of a container.

n If the user sets a location value which does not follow the standard URL format, the following error message

is returned: Failure to configure image location: Invalid URL

n If the user tries to use a VRF value that doesn't exist on the switch, the following error message is returned:

Failure to configure image location: Invalid VRF

n If the image of the container exceeds the maximum image size supported by the switch, the container won't

be deployed.

By default, only container images with a valid HPE signature are allowed. To bypass this signature check
and allow unsigned container images, include the allow-unsigned parameter when you define the
image location. The allow-unsigned parameter cannot be used if you have issued the secure-mode
enhanced command to set the switch to enhanced secure mode.

Parameter

image-location

URL

vrf <VRF-NAME>

allow-unsigned

Examples

Description

Configures the URL of the container application.

Specifies the URL of the container application. URL supports HTTP
protocol. The image-location URL can either be IPv4 or IPv6
address. The IPv6 address must be provided within square
brackets.

(Optional) Specifies the VRF of the image URL.

(Optional) Allow download and deployment of an unsigned
container image.

Configures the image location for the IPv4 setting:

switch(config-container-1)# image-location http://10.0.0.1/container.img vrf mgmt

Appends the port to the address if the image server is running on a port other than HTTP for an IPv4
setting:

Container management commands | 20

switch(config-container-1)# image-location http://10.0.0.1:9050/container.img vrf
mgmt
ConfiguresimagelocationforIPv6settingbywrappingIP addressbetweensquarebrackets:
switch(config-container-1)# image-location http://[2001::2]/container.img vrf mgmt
SpecifiesportnumberbyappendingitwiththeIPv6address:
switch(config-container-1)# image-location http://[2001::2]:9050/container.img vrf
mgmt
Whenyouincludetheallow-unsignedparameteronaswitchinstandardsecuremode,thefollowing
messagewillbedisplayedtoinformthiscanbeapotentialsecurityissue.
switch(config-container-1)# image-location http://10.0.0.1/container.img vrf mgmt
allow-unsigned
Allowing unsigned container images poses a potential security risk
that can impact both the current device and the entire network. By
allowing installation of unsigned applications you are acknowledging
and accepting these risks. HPE shall not be responsible for the
consequences of your actions and disclaims any and all liability.
| Continue | (y/n)? y |     |     |     |
| -------- | -------- | --- | --- | --- |
Whenyouattempttoincludetheallow-unsignedparameteronaswitchinenhancedsecuremode,the
followingmessagewillappeartoindicatethatthisparameterisnotsupported.
switch(config-container-1)# image-location http://10.0.0.1/container.img vrf mgmt
allow-unsigned
Unsigned images are not permitted in the current secure mode, using the
| allow-unsigned      | parameter | will have | no effect.                              |           |
| ------------------- | --------- | --------- | --------------------------------------- | --------- |
| Release             |           |           | Modification                            |           |
| 10.14               |           |           | Theallow-unsignedparameterisintroduced. |           |
| 10.12               |           |           | Commandintroduced.                      |           |
| Command Information |           |           |                                         |           |
| Platforms           | Command   | context   |                                         | Authority |
config-container-<CONTAINER-NAME>
| 6300,except |     |     |     | Administratorsorlocalusergroupmembers |
| ----------- | --- | --- | --- | ------------------------------------- |
| forS3L75A,  |     |     |     | withexecutionrightsforthiscommand.    |
S3L76Aand
S3L77A
6400
8100
8320
8325
AOS-CX10.16.xxxxContainersGuide|(6300F/M,6400,8xxx,9xxx,100xxSwitchSeries) 21

Platforms

Command context

Authority

8325H
8325P
8360
8400
9300
9300S
10000
10040

mount (container manager)
mount <id>

destination <path>
no ...
source <TYPE> <PATH>

Description

Mount persistent storage for a container application, and optionally indicate the mounted storage
source and destination paths.

Parameter

<ID>

destination <PATH>

no ...

source

<type>

<PATH>

Description

ID assigned to a mounted storage instance for a container
application. Range: <1-4294967295>

The destination path is a directory or file inside the container file
system. The path must use the syntax /{FILE|DIRECTORY}. Only
letters, numbers, slashes, underscores, dashes, and periods are
allowed.

Negates any configured parameter or removes a source or
destination path.

Define the mounted storage source.

This version of AOS-CX supports only a usb storage type.

NOTE: For containers using USB persistent storage functionality,
ext4 is the recommended formatting method for USB storage
devices. While FAT32 is currently supported, it may be deprecated
in future releases.

The mounted storage source path must be a valid file or directory
on the USB device and is relative to the root directory of the
device file system. The path must use the syntax /
{FILE|DIRECTORY}. Only letters, numbers, slashes, underscores,
dashes, and periods are allowed.

Example

Creating the mount ID 1 for the container test.

switch(config-container-test)# mount 1

Container management commands | 22

Configuringcontainermount1withaUSBsourceandthepath/app1-data.
| switch(config-container-mount-1)# |     |     | source usb | /app1-data |
| --------------------------------- | --- | --- | ---------- | ---------- |
Configuringcontainermount1withthedestinationpath/app1-data.
| switch(config-container-mount-1)# |         |         | destination       | /app1-data |
| --------------------------------- | ------- | ------- | ----------------- | ---------- |
| Command History                   |         |         |                   |            |
| Release                           |         |         | Modification      |            |
| 10.16.1000                        |         |         | Commandintroduced |            |
| Command Information               |         |         |                   |            |
| Platforms                         | Command | context |                   | Authority  |
8100 config-container-<CONTAINER-NAME> Administratorsorlocalusergroupmembers
| 8320 |     |     |     | withexecutionrightsforthiscommand. |
| ---- | --- | --- | --- | ---------------------------------- |
8325
8325H
8325P
8360
9300
9300S
10000
10040
| network        | vrf   |     |     |     |
| -------------- | ----- | --- | --- | --- |
| network vrf    | <VRF> |     |     |     |
| no network vrf | <VRF> |     |     |     |
Description
UsethiscommandtoassociateaVRFwiththecontainerandallowconnectivitythroughtheVRF.When
configured,theVRFwillbeaccessibletothecontainerthroughanetworknamespace.
Usage
OnlyonenetworkVRFcanbeconfiguredpercontainer.IfanadditionalVRFisconfigured,thecontainer
deploymentwillfailandgenerateanerrormessageindicatingthatthecontainerhasmorethanone
networkVRF.ModifyinganetworkcontainerVRFwillmodifythecontainernetworkconfigurationand
thecontainerwillberestartedtoapplythenewchangesifthecontainerhasalreadybeenenabled.
Examples
ThefollowingexampledefinestheVRFmgmtfortheappcontainer.
| switch(config-container-app)# |     | network | vrf | mgmt |
| ----------------------------- | --- | ------- | --- | ---- |
| Command History               |     |         |     |      |
AOS-CX10.16.xxxxContainersGuide|(6300F/M,6400,8xxx,9xxx,100xxSwitchSeries) 23

| Release   |             |         | Modification      |           |
| --------- | ----------- | ------- | ----------------- | --------- |
| 10.16     |             |         | Commandintroduced |           |
| Command   | Information |         |                   |           |
| Platforms | Command     | context |                   | Authority |
6300,except config-container-<CONTAINER-NAME> Administratorsorlocalusergroupmembers
| forS3L75A, |     |     |     | withexecutionrightsforthiscommand. |
| ---------- | --- | --- | --- | ---------------------------------- |
S3L76Aand
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
| port-map | (container | manager) |     |     |
| -------- | ---------- | -------- | --- | --- |
port-map host-port <PORT> container-port <PORT> protocol (tcp | udp)
Description
Issuethiscommandfromtheconfig-container-network-vrf-<name>contexttodefineaportmap
fromaportonthehostswitchtoaportonthecontainer.Thiswillallowcommunicationfromexternal
devicestoservicesprovidedbythecontainer.
| Parameter      |        |     | Description                           |     |
| -------------- | ------ | --- | ------------------------------------- | --- |
| host-port      | <port> |     | Thehostswitchportnumber.Range:1-65535 |     |
| container-port | <port> |     | Thecontainerportnumber.Range:1-65535  |     |
| tcp            |        |     | CommunicationswillusetheTCPprotocol.  |     |
| udp            |        |     | CommunicationswillusetheUDPprotocol.  |     |
Usage
AportmapisanoptionalconfigurationforacontainernetworkVRF,butaportmappingisrequiredto
exposethemappedporttotheoutsidenetwork.Thiscommandcanbeissuedmultipletimestodefine
morethanoneportmapforthecontainer.
Hostportconflictsarenotallowed.ThesamehostportcannotbeusedfordifferentcontainersinthesameVRF,
andthehostportusedfortheVRFcannotbereservedforanon-containerapplicationonthehostswitch.
Examples
Containermanagementcommands|24

ConfigureaportmapfromthehosttothecontainerforTCPtraffic,wheretraffictoTCPport8000on
theswitchwillbedirectedtoTCPport9000inthecontainer.
switch(config-container-network-vrf-mgmt)# port-map host-port 8000 container-port
| 9000 protocol | tcp |     |     |
| ------------- | --- | --- | --- |
ThefollowingexamplemapsdifferentportsonthehosttothesamecontainerportforTCPtraffic:
switch(config-container-network-vrf-mgmt)# port-map host-port 8000 container-port
| 9000 protocol | tcp |     |     |
| ------------- | --- | --- | --- |
switch(config-container-network-vrf-mgmt)# port-map host-port 8001 container-port
| 9000 protocol | tcp |     |     |
| ------------- | --- | --- | --- |
ThefollowingexamplemapsthesameportonthehostswitchtothesamecontainerportforTCPand
UDPtraffic:
switch(config-container-network-vrf-mgmt)# port-map host-port 8000 container-port
| 9000 protocol | tcp |     |     |
| ------------- | --- | --- | --- |
switch(config-container-network-vrf-mgmt)# port-map host-port 8000 container-port
| 9000 protocol | udp |     |     |
| ------------- | --- | --- | --- |
ThefollowingexamplemapsthesameportondifferentVRFsonthehostswitchtothesamecontainer
portforTCPtraffic:
switch(config-container-network-vrf-mgmt)# port-map host-port 8000 container-port
| 9000 protocol | tcp |     |     |
| ------------- | --- | --- | --- |
switch(config-container-network-vrf-default)# port-map host-port 8000 container-
| port 9000 | protocol | tcp |     |
| --------- | -------- | --- | --- |
Whenremovingaportmapping,ifthecommandparametersdonotmatchaconfiguredportmapping,
thecommandoutputdisplaysthefollowingmessage:
switch(config-container-network-vrf-mgmt)# no port-map host-port 8001 container-
| port 9000       | protocol | tcp                       |     |
| --------------- | -------- | ------------------------- | --- |
| The specified   | port     | mapping is not configured |     |
| Command History |          |                           |     |
Release Modification
10.16.1000 Commandintroduced
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-container-<CONTAINER-NAME>
| 6300,except |     |     | Administratorsorlocalusergroupmembers |
| ----------- | --- | --- | ------------------------------------- |
| forS3L75A,  |     |     | withexecutionrightsforthiscommand.    |
S3L76Aand
S3L77A
6400
AOS-CX10.16.xxxxContainersGuide|(6300F/M,6400,8xxx,9xxx,100xxSwitchSeries) 25

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
| restrict     | cpu          |     |     |
| ------------ | ------------ | --- | --- |
| restrict cpu | <PERCENTAGE> |     |     |
| no restrict  | cpu          |     |     |
Description
ConfigureslimitationsforthecontainerCPUusage.TheCPUconstraintissetasapercentageofthe
totalswitchCPUs.Onecontaineroranycombinationofcontainersconfiguredonaswitchcanuseupto
20%ofthetotalCPUcapacityofthedevice.
ConfiguringtheCPUconstraintforanalreadyoperationalcontainerwillcausethecontainertorestartifthe
containerhasalreadybeenenabled.
ThenoformofthiscommandremovesrestrictionsontheCPU usage,andrevertsbacktothedefault
limitationof10%.
Parameter Description
<PERCENTAGE>
SpecifiespercentageforthecontainerCPUusage,The
defaultvalueis10%.
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Release Modification
10.12 Commandintroduced
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6300,except config-container-<CONTAINER-NAME> Administratorsorlocalusergroupmembers
| forS3L75A, |     |     | withexecutionrightsforthiscommand. |
| ---------- | --- | --- | ---------------------------------- |
S3L76Aand
S3L77A
6400
8100
8320
Containermanagementcommands|26

Platforms

Command context

Authority

8325
8325H
8325P
8360
8400
9300
9300S
10000
10040

restrict memory
restrict memory <MB>
no restrict memory

Description

Configures limitations for memory usage of the container. The memory constraint is set in MB, and the
maximum 20% of the capacity of the device can be configured for any combination of containers
running on the switch. Configuring the memory constraint for an already operational container restarts
the container if the container has already been enabled.

The no form of this command removes restrictions on the memory usage and reverts back to the
default limitation of 256 MB.

Parameter

<MB>

Command History

Release

10.12

Command Information

Description

Specifies the maximum memory usage in MB.The default
value is 256 MB.

Modification

Command introduced

Platforms

Command context

Authority

config-container-<CONTAINER-NAME>

Administrators or local user group members
with execution rights for this command.

6300, except
for S3L75A,
S3L76A and
S3L77A
6400
8100
8320
8325
8325H
8325P
8360
8400

AOS-CX 10.16.xxxx Containers Guide | (6300F/M, 6400, 8xxx, 9xxx, 100xx Switch Series)

27

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
9300
9300S
10000
10040
show container
| show container | [<CONTAINER-NAME>] |     |     |
| -------------- | ------------------ | --- | --- |
Description
Showstheconfigurationandstatusinformationofthecontainersrunninginthesystem.Ifthecontainer
nameisnotspecified,displaysinformationofallthecontainers.Whenacontainernameisspecified,
displaysinformationspecifictothecontainer.
Parameter Description
<CONTAINER-NAME> Specifiesthenameofthecontainerforwhichinformation
needtobespecified.
Usage
TheContainer statusfieldintheoutputofthiscommandcandisplayanyofthefollowingstatus
values:
initializing:Containerinitializationandconfigurationverificationisinprogress.
n
n waiting:Containeriswaitingforconfigurationprerequisitestobemet.
n configurationfailed:User-specifiedcontainerconfigurationfailed.
n networkconfigurationfailed:Containernetworkprovisioningfailed.
n acquiring:Containerisacquiringanimage.
| n acquire failed:Containerfailedtoacquireanimage. |     |     |     |
| ------------------------------------------------- | --- | --- | --- |
n deploying:Containerisdeploying.
n operational:Containerisoperational(deployedandrunning).
n deployfailed:Containerfailedtodeploy.
n run failed:Containerfailedwhilerunning.
n exited:Containercompleteditsexecutionandexited.
Examples
ThefollowingexampleshowsinformationforaconfiguredcontainerwithanetworkVRFwithport
mappings:
| switch# show   | container |               |     |
| -------------- | --------- | ------------- | --- |
| Container      |           | : app1        |     |
| Container      | status    | : operational |     |
| Manifest       | status    | : success     |     |
| Image status   |           | : verified    |     |
| Image version  |           | : 1.0.0       |     |
| Image location | VRF       | : mgmt        |     |
Containermanagementcommands|28

| Image location |            | URL | : http://30.0.0.2:8000/container.img |     |     |     |
| -------------- | ---------- | --- | ------------------------------------ | --- | --- | --- |
| CPU limit      |            |     | : 10%                                |     |     |     |
| Memory         | limit      |     | : 512MB                              |     |     |     |
| Environment    | variables: |     |                                      |     |     |     |
PYP=/usr/bin/python3
| Encrypted | environment |     | variables: |     |     |     |
| --------- | ----------- | --- | ---------- | --- | --- | --- |
encryptedVar1
encryptedVar2
Network:
| VRF name | :     | default |     |     |     |     |
| -------- | ----- | ------- | --- | --- | --- | --- |
| Port     | map : |         |     |     |     |     |
8080:80/tcp
8080:8080/udp
Thefollowingexampleshowsadditionalerrormessages:
| switch# show | container |     |                 |     |        |     |
| ------------ | --------- | --- | --------------- | --- | ------ | --- |
| Container    |           |     | : app           |     |        |     |
| Container    | status    |     | : configuration |     | failed |     |
Config failure reason : Multiple definitions of environment variable PYP
| Manifest       | status    |        | : error                              |      |           |              |
| -------------- | --------- | ------ | ------------------------------------ | ---- | --------- | ------------ |
| Manifest       | status    | reason | : 'exec'                             | file | not found | in container |
| Image status   |           |        | : verified                           |      |           |              |
| Image version  |           |        | : 1.0.0                              |      |           |              |
| Image location |           | VRF    | : mgmt                               |      |           |              |
| Image location |           | URL    | : http://30.0.0.2:8000/container.img |      |           |              |
| CPU limit      |           |        | : 10%                                |      |           |              |
| Memory         | limit     |        | : 512                                | MB   |           |              |
| VRFs           |           |        | : mgmt                               |      |           |              |
| Environment    | variables |        | :                                    |      |           |              |
PYP=/usr/bin/python3
| Encrypted | environment |     | variables: |     |     |     |
| --------- | ----------- | --- | ---------- | --- | --- | --- |
PYP
encryptedVar2
Thefollowingexampleshowsaconfiguredcontainerwithoutsignaturevalidation:
| switch# show   | container  |     | app1                                 |         |           |     |
| -------------- | ---------- | --- | ------------------------------------ | ------- | --------- | --- |
| Container      |            |     | : app1                               |         |           |     |
| Container      | status     |     | : operational                        |         |           |     |
| Manifest       | status     |     | : success                            |         |           |     |
| Image status   |            |     | : allowed                            | without | signature |     |
| Image version  |            |     | : 1.0.0                              |         |           |     |
| Image location |            | VRF | : mgmt                               |         |           |     |
| Image location |            | URL | : http://30.0.0.2:8000/container.img |         |           |     |
| CPU limit      |            |     | : 10%                                |         |           |     |
| Memory         | limit      |     | : 512 MB                             |         |           |     |
| Environment    | variables: |     |                                      |         |           |     |
PYP=/usr/bin/python3
| Encrypted | environment |     | variables: |     |     |     |
| --------- | ----------- | --- | ---------- | --- | --- | --- |
encryptedVar1
encryptedVar2
Network:
| VRF name | :     | default |     |     |     |     |
| -------- | ----- | ------- | --- | --- | --- | --- |
| Port     | map : |         |     |     |     |     |
8080:80/tcp
8080:8080/udp
Thefollowingexampleshowsthecommandoutwhentherearenoconfiguredcontainers:
AOS-CX10.16.xxxxContainersGuide|(6300F/M,6400,8xxx,9xxx,100xxSwitchSeries) 29

| switch#                        | show container |                   |         |           |     |
| ------------------------------ | -------------- | ----------------- | ------- | --------- | --- |
| No containers                  | configured     |                   |         |           |     |
| Command                        | History        |                   |         |           |     |
| Release                        |                | Modification      |         |           |     |
| 10.12                          |                | Commandintroduced |         |           |     |
| Command                        | Information    |                   |         |           |     |
| Platforms                      |                | Command           | context | Authority |     |
| 6300,exceptforS3L75A,S3L76Aand |                | Operator(>)or     |         |           |     |
S3L77A
Manager(#)
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
| show capacities |            | containers |     |     |     |
| --------------- | ---------- | ---------- | --- | --- | --- |
| show capacities | containers |            |     |     |     |
Description
Showsthemaximumnumberofcontainerizedapplicationsthatcanbeconfiguredinthesystem.
Examples
Showsmaximumnumberofcontainerizedapplicationsthatcanbeconfigured:
| switch#            | show capacities | containers |     |     |       |
| ------------------ | --------------- | ---------- | --- | --- | ----- |
| System Capacities: | Filter          | CONTAINERS |     |     |       |
| Capacities         | Name            |            |     |     | Value |
----------------------------------------------------------------------------------
----
Maximum number of containerized applications configurable in the system 2
| Command | History     |                   |     |     |     |
| ------- | ----------- | ----------------- | --- | --- | --- |
| Release |             | Modification      |     |     |     |
| 10.12   |             | Commandintroduced |     |     |     |
| Command | Information |                   |     |     |     |
Containermanagementcommands|30

| Platforms                      | Command       | context | Authority |
| ------------------------------ | ------------- | ------- | --------- |
| 6300,exceptforS3L75A,S3L76Aand | Operator(>)or |         |           |
| S3L77A                         | Manager(#)    |         |           |
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
| show capacities-status | containers |     |     |
| ---------------------- | ---------- | --- | --- |
show capacities-status containers
Description
Reservedforfutureuse.
Command History
| Release | Modification      |     |     |
| ------- | ----------------- | --- | --- |
| 10.12   | Commandintroduced |     |     |
Command Information
| Platforms                      | Command       | context | Authority |
| ------------------------------ | ------------- | ------- | --------- |
| 6300,exceptforS3L75A,S3L76Aand | Operator(>)or |         |           |
| S3L77A                         | Manager(#)    |         |           |
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
| show running-config | container |     |     |
| ------------------- | --------- | --- | --- |
show running-config container
Description
Showstherunningconfigurationofallthecontainers.
AOS-CX10.16.xxxxContainersGuide|(6300F/M,6400,8xxx,9xxx,100xxSwitchSeries) 31

Parameter Description
container Specifiesthatcontainerrunningconfigurationmustbe
displayed.
Examples
Showstherunningconfigurationforthecontainer:
container app1
enable
| image-location  | http://30.0.0.2:8000/container.img |                     |     | vrf mgmt      |     |
| --------------- | ---------------------------------- | ------------------- | --- | ------------- | --- |
| restrict cpu    | 10                                 |                     |     |               |     |
| restrict memory | 512                                |                     |     |               |     |
| network vrf     | mgmt                               |                     |     |               |     |
| port-map        | host-port                          | 8000 container-port |     | 9000 protocol | tcp |
exit
mount 1
source usb /app1-data
destination /app-data
exit
| env PYP value     | /usr/bin/python3 |            |               |     |     |
| ----------------- | ---------------- | ---------- | ------------- | --- | --- |
| env encryptedVar1 | encrypted        | ciphertext | AQBapcmTCVdag |     |     |
container app2
enable
image-location http://[2001::2]:8000/changeValidation_x86_t.img vrf mgmt allow-
unsigned
| restrict cpu    | 5         |                     |     |               |     |
| --------------- | --------- | ------------------- | --- | ------------- | --- |
| restrict memory | 256       |                     |     |               |     |
| network vrf     | default   |                     |     |               |     |
| port-map        | host-port | 7819 container-port |     | 7819 protocol | udp |
exit
mount 1
source usb /app2-data1
destination /app-data1
exit
mount 2
source usb /app2-data2
destination /app-data2
exit
| env PYP value     | /usr/bin/python3 |            |                 |     |     |
| ----------------- | ---------------- | ---------- | --------------- | --- | --- |
| env encryptedVar1 | encrypted        | ciphertext | AQBapcmTCVdag   |     |     |
| env encryptedVar2 | encrypted        | ciphertext | AQpY4V4v9UtDa== |     |     |
Command History
Release Modification
10.16.1000 TheoutputofthiscommandincludesmountandnetworkVRF
details,ifconfigured.
10.12 Commandintroduced
Command Information
Containermanagementcommands|32

| Platforms |     | Command | context | Authority |
| --------- | --- | ------- | ------- | --------- |
6300,exceptforS3L75A,S3L76Aand Operator(>)or
S3L77A Manager(#)
6400
8100
8320
8325
8325H
8325P
8325P
8360
8400
9300
9300S
10000
10040
| vrf (container | manager) |     |     |     |
| -------------- | -------- | --- | --- | --- |
vrf <VRF-NAME>
Description
Thiscommandisdeprecated.UsethenetworkvrfcommandtodefineaVRFforacontainer.
| Command History     |         |                   |     |           |
| ------------------- | ------- | ----------------- | --- | --------- |
| Release             |         | Modification      |     |           |
| 10.12               |         | Commandintroduced |     |           |
| Command Information |         |                   |     |           |
| Platforms           | Command | context           |     | Authority |
6300,except config-container-<CONTAINER-NAME> Administratorsorlocalusergroupmembers
| forS3L75A, |     |     |     | withexecutionrightsforthiscommand. |
| ---------- | --- | --- | --- | ---------------------------------- |
S3L76Aand
S3L77A
6400
8100
8320
8325
8360
8400
9300
9300S
10000
10040
AOS-CX10.16.xxxxContainersGuide|(6300F/M,6400,8xxx,9xxx,100xxSwitchSeries) 33

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

AOS-CX 10.16.xxxx Containers Guide | (6300F/M, 6400, 8xxx, 9xxx, 100xx Switch Series)

34

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
SupportandOtherResources|35

(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.16.xxxx Containers Guide | (6300F/M, 6400, 8xxx, 9xxx, 100xx Switch Series)

36