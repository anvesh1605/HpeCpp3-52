AOS-CX 10.18.xxxx Containers Guide (6300F/M, 6400, 8xxx, 9xxx,
100xx Switch Series)

Published: May 2026

AOS-CX 10.18.xxxx Containers Guide (6300F/M, 6400, 8xxx, 9xxx,
100xx Switch Series)

Published: May 2026

© Copyright 2026 – Hewlett Packard Enterprise Development LP

Notices

The information provided here is subject to change without notice. Hewlett Packard Enterprise's products
and services are covered only by the express warranty statements that come with them. This document
does not constitute an additional warranty. Hewlett Packard Enterprise is not responsible for any technical
or editorial errors or omissions in this document.

Confidential computer software. You must have a valid license from Hewlett Packard Enterprise to possess,
use, or copy the software. In accordance with FAR 12.211 and 12.212, Commercial Computer Software,
Computer Software Documentation, and Technical Data for Commercial Items are licensed to the U.S.
Government under the vendor's standard commercial license.

Links to third-party websites will take you outside of the Hewlett Packard Enterprise website. Hewlett
Packard Enterprise has no control over and is not responsible for the information outside the Hewlett
Packard Enterprise website.

Open source code

This product includes code licensed under certain open source licenses which require source compliance.
The corresponding source for these components is available upon request. This offer is valid to anyone in
receipt of this information and shall expire three years following the date of the final distribution of this
product version by Hewlett Packard Enterprise Company. To obtain such source code, please check if the
code is available in the HPE Software Center at https://myenterpriselicense.hpe.com/cwp-ui/software
but, if not, send a written request for specific software version and product for which you want the open
source code. Along with the request, please send a check or money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company

Attn: General Counsel

WW Corporate Headquarters

1701 E Mossy Oaks Rd, Spring, TX 77389

United States of America.

Public

AOS-CX 10.18.xxxx Containers Guide (6300F/M, 6400,...

A
O
S
-
C
X

1
0
.
1
8
.
x
x
x
x

C
o
n
t
a
i
n
e
r
s

G
u
i
d
e

(
6
3
0
0
F
/
M
,

6
4
0
0
,
.
.
.

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX 10.18.xxxx Containers Guide (6300F/M, 6400,...

Table of contents

Container overview......................................................................................................................................................................................6

Supported switches........................................................................................................................................................................ 6

USB persistent storage.................................................................................................................................................................7

Restart protection............................................................................................................................................................................8

Network modes.................................................................................................................................................................................9

Configuring an isolated network.............................................................................................................................................9

vSphere agent..............................................................................................................................................................................................12

Installation and Configuration of the vSphere agent...............................................................................................13

vSphere show commands........................................................................................................................................................ 14

Container management commands................................................................................................................................................16

container ...........................................................................................................................................................................................17

container exec ............................................................................................................................................................................... 19

default-gateway ........................................................................................................................................................................... 20

enable .................................................................................................................................................................................................21

env ........................................................................................................................................................................................................23

image-location ...............................................................................................................................................................................25

ip address .........................................................................................................................................................................................28

mdns enable ................................................................................................................................................................................... 29

mount ................................................................................................................................................................................................. 30

network isolated-network .......................................................................................................................................................32

network vrf ...................................................................................................................................................................................... 33

port-map ...........................................................................................................................................................................................34

restrict cpu .......................................................................................................................................................................................37

restrict memory ............................................................................................................................................................................ 38

show container ..............................................................................................................................................................................40

show capacities containers .................................................................................................................................................... 44

show capacities-status containers .....................................................................................................................................46

show running-config container ........................................................................................................................................... 47

virtual-interface vlan ................................................................................................................................................................. 49

vrf ..........................................................................................................................................................................................................50

Support and Other Resources............................................................................................................................................................51

Accessing HPE Aruba Networking Support..................................................................................................................51

Accessing Updates.......................................................................................................................................................................52

Warranty Information................................................................................................................................................................. 53

Public

Table of contents 4

Regulatory Information............................................................................................................................................................. 53

Documentation Feedback........................................................................................................................................................53

Public

Table of contents 5

Container overview
The Container Manager feature allows containers to run inside an AOS-CX switch. It allows the switch to
launch multiple container images, whether HPE-signed or unsigned, and provides tools to manage, maintain,
and monitor the lifecycle of these images and containers. Applications can be run within the container
infrastructure, turning them into containerized applications.
The AOS-CX container infrastructure is designed to support containers that run in the background as
services or scheduled jobs. These containers either keep running continuously or stop gracefully after
completing their tasks. Examples of supported workloads include web servers like Nginx or Apache,
application servers built with Node.js, Java, or Python APIs, and system monitoring tools.
The container infrastructure does not support containers that must interact users in real time through a
command-line interface, such as shells (bash, sh), interpreters (Python, Node.js), or text-based tools (like vim
or top) to accept user input and display output interactively. If you try to deploy an unsupported container
that relies on an interactive terminal, it may stop immediately or behave unpredictably.
Subtopics
Supported switches
USB persistent storage
Restart protection
Network modes
Configuring an isolated network

Supported switches
The following switch platforms are validated for data center deployments. The agent itself has no context
about the switch that it is installed on, except that the chipset architecture must be either x86_64 or arm.
The container image size is limited by platform. A container instance will display an error if you attempt to
download a container image that exceeds the supported image size.
| Switch |        | Chipset Architecture Type | Maximum Image size (MiB) |                    |     |
| ------ | ------ | ------------------------- | ------------------------ | ------------------ | --- |
| 6300   |        | arm                       | 500                      |                    |     |
| 6400   |        | arm                       | 500                      |                    |     |
| 8100   |        | arm                       | 500                      |                    |     |
| 8320   |        | x86_64                    | 1000                     |                    |     |
| 8325   |        | x86_64                    | 1000                     |                    |     |
|        | Public |                           |                          | Container overview | 6   |

| Switch |     | Chipset Architecture Type | Maximum Image size (MiB) |     |
| ------ | --- | ------------------------- | ------------------------ | --- |
| 8325H  |     | x86_64                    | 1000                     |     |
| 8325P  |     | x86_64                    | 1000                     |     |
| 8360   |     | arm                       | 500                      |     |
| 8400   |     | x86_64                    | 500                      |     |
| 9300   |     | x86_64                    | 1000                     |     |
| 9300S  |     | x86_64                    | 1000                     |     |
| 10000  |     | x86_64                    | 1000                     |     |
NOTE
The HPE Aruba Networking CX vSphere agent is a containerized agent
developed for data center applications. The plugin consumes memory and CPU
that would otherwise be allocated to the switch. Thus, the targeted platforms
have higher system resources. Those resources are capped to prevent its
interference with performance of the switch.
NOTE
The solution was tested and qualified on the platforms listed here. Other
platforms may work at low scale, but they are not recommended outside of
the lab or test environments due to the resource requirements for vSphere.

USB persistent storage
About this task
Containers can mount additional persistent storage via a USB device using the mount, source and
destination commands to create a mount ID and specify the mount source and destination paths. Best
practices is to configure persistent storage via these commands. If a USB directory in the source filesystem is
deleted or renamed through shell commands, the container may not function correctly.
The USB persistent storage feature includes the following additional caveats.
•  Containers are not aware if the configured USB device is unmounted, disabled or physically removed.
As a result, the container's correct functionality can't be guaranteed if these actions are made without
unconfiguring the container mount first.
|     | Public |     | USB persistent storage | 7   |
| --- | ------ | --- | ---------------------- | --- |

•  For containers using USB persistent storage functionality, data won't synchronize between the
management modules after a High Availability event, so the container deployed on the new
management module won't have access to the USB device connected to the previous management
module.

•

If there is an issue with the USB device mount when the container boots up, there can be a potential wait
of up to two minutes before the container shows an error.

The following steps configure a container with USB persistant storage.

Procedure

1.  Create the container context

switch(config)# container <NAME>

2.  Configure the container image location

switch(config-container-<NAME>)# image-location <URL> vrf <VRF>

3.  Configure the container mount

switch(config-container-<NAME>)# mount <ID>

4.  Configure the container mount source

switch(config-container-mount-<ID>)# source usb /app1-data

5.  Configure the container mount destination

switch(config-container-mount-<ID>)# destination /app-data

6.  Enable the container

switch(config-container-<NAME>)# enable

7.  Validate the container status

show container <NAME>

Restart protection

The HPE Aruba Networking switch can prevent a crashing containerized application from restarting after
three restarts within a brief period of time. Once the restart protection feature indicates that it has stopped
a crashing application in this manner, the container will display a run failed status in the output of the show
container command.

Public

Restart protection 8

If the configured image has been downloaded and verified by container manager, in case of a restart, the
image will not need to be downloaded again unless the image location is modified. This also applies when
using the allow-unsigned parameter, if a re-download is required, modify the image location URL or remove
the command and add it again.

Network modes

Containers can be configured to run in one of three supported network modes:

•  Default mode. In the default mode there is no network connectivity. This option is used when there is no
network configuration specified, and does not allow the container network connectivity to reach external
devices.

•  VRF network mode. This mode allows network access through one of the switch VRFs. Communications
between container and the host switch are restricted to the default management interfaces ports (22
and 443).

•

Isolated network mode. The 8325, 8325H and 8325P Switch series support isolated network
mode, which allows network access through one or more configured VLANs. Containers using this
mode behave as hosts physically connected to the switch's front panel ports with a unique MAC
address assigned by the system. This allows the container configuration to support VLAN-aware
configurations and Ethernet traffic types (unicast, broadcast, multicast). Note that this mode does not
allow communication with the switch interfaces and services. For more information on configuring a
container in isolated network mode, see Configuring an isolated network.

Configuring an isolated network

Configuring an isolated network on a 8325, 8325H or 8325P Switch series is a two-part process. You must
create the isolated network first, then configure the container with isolated network connectivity.

Configuring the isolated network

1.

If it is not already created, create the VLAN to be used by the isolated network.
switch(config)# vlan 789

2.  Configure the isolated network.

switch(config)# container isolated-network test

3.  Create the virtual interface

switch(config-container-isolated-network-test)# virtual-interface vlan

test

Public

Network modes 9

4.  Set the IP address for the interface.

switch(config-container-isolated-network-virtual-interface)# ip address

90.0.0.1/30

5.  Enter exit to return to the config-container-isolated-network-<NAME> context, then configure the

default gateway.
switch(config-container-isolated-network-virtual-interface)# exit

switch(config-container-isolated-network-test)# default-gateway 90.0.0.2

6.  Enable mDNS.

switch(config-container-isolated-network-test)# mdns enable

7.  Exit the config-container-isolated-network context and validate the status of the isolated network.

The following example verifies an isolated network with virtual interface that uses VLAN 789,
switch(config-container-isolated-network-<NAME>)# exit

switch (config)# vlan 789

switch (config-vlan-789)# exit

switch(config)# container isolated-network test

switch (config-container-isolated-network-test)# virtual-interface vlan

789

switch (config-container-isolated-network-virtual-interface)# ip address

90.0.0.1/30

switch (config-container-isolated-network-virtual-interface)# exit

switch (config-container-isolated-network-test)# default-gateway 90.0.0.2

switch (config-container-isolated-network-test)# mdns enable

switch (config-container-isolated-network-test)# end

switch # show container isolated-network test

Isolated network        : test

Status                  : network_provisioned

Status reason           : n/a

Default gateway         : 90.0.0.2

mDNS                    : enabled

Virtual MAC             : 64:e8:81:1a:4f:07
Containers              : n/a

Virtual interfaces      :

------------------------

VLAN  IP address

------------------------

789   90.0.0.1/30

Connect the container to the isolated network

1.  Create the container context.

Public

Configuring an isolated network 10

switch(config)# container test

The feature being used requires a AOS-CX Advanced Software Feature Pack.

For more information, refer to the AOS-CX Feature Pack Deployment Guide.

2.  Configure the container network mode.

switch(config-container-test)# network isolated-network test

3.  Configure the container image location.

switch(config-container-test)# image-location http://117.0.0.2:8000/

vsphere_agent-1.3.0-96-x86_64.img vrf mgmt

4.  Enable the container, then exit the container context
switch(config-container-test)# enable

switch(config-container-test)# end

5.  Validate the container status.

switch # show container test

Container               : test

Container status        : operational

Manifest status         : success

Image status            : verified

Image version           : 1.3.0-96

Image location VRF      : mgmt

Image location URL      : http://117.0.0.2:8000/vsphere_agent-1.3.0-96-

x86_64.img

CPU limit               : 10%

Memory limit            : 256MB

VRFs                    :

Environment variables   :

Encrypted environment variables:

VRF networks: n/a

Isolated network: test

Mounts: n/a

Example configuration:

(switch)(config)# vlan 789

(switch)(config-vlan-789)# exit

(switch)(config)# container isolated-network test

(switch)(config-container-isolated-network-test)# virtual-interface vlan 789

(switch)(config-container-isolated-network-virtual-interface)# ip address
90.0.0.1/30
(switch)(config-container-isolated-network-virtual-interface)# exit

(switch)(config-container-isolated-network-test)# default-gateway 90.0.0.2

(switch)(config-container-isolated-network-test)# mdns enable

(switch)(config-container-isolated-network-test)# end

Public

Configuring an isolated network 11

(switch)# show container isolated-network test

Isolated network          : test

Status                  : network_provisioned

Status reason           : n/a

Default gateway         : 90.0.0.2

mDNS                    : enabled

Virtual MAC             : 64:e8:81:1a:4f:07

Containers              : n/a

Virtual interfaces      :

------------------------

VLAN  IP address

------------------------

789   90.0.0.1/30

vSphere agent

About this task

The HPE Aruba Networking CX vSphere agent allows administrators to trace how Virtual Machines are
connected to the physical switches. The ability to visualize how a Virtual Machine connects to a CX port
helps to resolve connectivity issues. This functionality helps operators in several troubleshooting scenarios,
such as diagnosing a connectivity issue, or ensuring adequate distribution of VMs across the physical
infrastructure.

You can install the vSphere agent on one or many of the switches in the fabric. You can perform the
following tasks, from any switch where the agent is installed:

Procedure

1.  Run the show VMs command to list all the VMs managed by the vCenter Appliance integrated with the

agent. This functionality also helps to view VMs connections to the ports on other switches on the fabric.

2.  Search for a specific VM by name. To find the connection between the VM and a switch port, attach the

switch to at least one host managed by the integrated vCenter.

Results

NOTE
The show neighbors command examines the LLDP data that is advertised from
any switch to a distributed virtual switch and provides connection details for
third-party switches.

For technical information on containers, including use cases, example configurations and best practices, view
the AOS-CX Container Enhancements video on the HPE Aruba Networking broadcasting channel on
YouTube. For more information about cloud capabilities of vSphere agent, refer to .

Public

vSphere agent 12

Subtopics

Installation and Configuration of the vSphere agent
vSphere show commands

Installation and Configuration of the vSphere agent

About this task

To install a container, perform the following steps:

Procedure

1.  Download the vSphere agent from the HPE Aruba Networking support portal and select the arm

or x86_64 architecture for the switch platform. Refer to the list of supported switches to select the
corresponding architecture.

2.  Host the agent on a local network that can be accessed using the HTTP protocol. Limitations of the

container framework prevent usage of the HTTPs protocol. The HTTP server must be reachable on the
mgmt or any other configured VRF.

Results

To create the container configuration:

1.  Enter the config command to enter the config context.

2.  Create and enter the config-container-<name> context using the container command.

3.  From the config-container-<name> context, configure the container image location using the image-
location command. To create a container configuration that bypasses signature validation, include the
optional allow-unsigned parameter for the image-location command

4.  (Optional) Configure a container environment variable using the env command.

5.  (Optional) To create a configuration with VRF network connectivity, issue the network vrf command,

then configure port mapping using the port-map command.

6.  (Optional) To create a configuration that limits CPU usage to a percentage of the total switch CPU, use

the restrict cpu command.

7.  (Optional) To create a configuration that limits memory resources to maximum number of megabytes

(up to 20% of the total switch memory), use the restrict memory command.

Public

Installation and Configuration of the vSphere agen... 13

I
n
s
t
a
l
l
a
t
i
o
n

a
n
d

C
o
n
fi
g
u
r
a
t
i
o
n

o
f

t
h
e

v
S
p
h
e
r
e

a
g
e
n
.
.
.

8.  (Optional) To create a configuration with mounted storage, issue the mount command, then use the

source and destination parameters from within the config-container-mount-<id> context to define the
mount source and destination.

9.  From the config-container-<name> context, enable the container using the enable command.

10.

Issue the show container command to validate the container status.

vSphere show commands

There are three top-level show commands.

•  vms - shows virtual machine connection information.

•  connection-status - shows information about configured vSphere vCenters.

•  neighbors - shows learned neighbor information (Note: This information is learned from LLDP on

vCenter distributed vswitches, not the switch).

show vms

The following show command describes the status of the connection to vSphere, and show the VMs
that are attached to switches:

At least one command parameter must be used if the parameters are available.

For example, with the show vms command, we force use of the brief option so the user is aware of all
available options.

If not specified, all commands default to brief.

igor-sw-02# container vsphere exec show vms brief Hypervisor VM Name

Physical Switch Connections Interface
laser-02-esxi.lab.plexxi.com vm4 laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/3 vm2

laser-sw-02 (b8:d4:e7:da:40:00) 1/1/4

laser-sw-02 (b8:d4:e7:da:40:00) 1/1/3 vm5 laser-sw-02 (b8:d4:e7:da:40:00)

1/1/4 laser-sw-02 (b8:d4:e7:da:40:00) 1/1/3 laser-sw-01 (b8:d4:e7:d9:af:00)

1/1/3

laser-01-esxi.lab.plexxi.com vm1 laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/1 vm3

laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/2

laser-sw-02 (b8:d4:e7:da:40:00) 1/1/1

igor-sw-02# container vsphere exec show vms vm-name vm4 Hypervisor VM Name

Physical Switch Connections Interface

laser-02-esxi.lab.plexxi.com vm4 laser-sw-01 (b8:d4:e7:d9:af:00) 1/1/3 igor-

sw-02# container vsphere exec show vms vm-name vm4 detailed VM Name : vm4

Public

vSphere show commands 14

Hypervisor : laser-02-esxi.lab.plexxi.com Vendor : vmware

Hostname : vm4

OS : CentOS 4/5 or later (64-bit) VM status : on

Virtual NIC : Network adapter 2 IP Address : 172.20.12.204

MAC Address : 00:50:56:89:3c:bf Virtual Switch : dvs4

Port Group : dpg4 Vlan : 0

Physical Switch Connections Interface : 1/1/3

Chassis ID : b8:d4:e7:d9:af:00 Switch Name : laser-sw-01

Switch Description : HPE_ANW JL635A GL.10.12.0001G Management Address :

172.20.11.253

Container exec commands are top-level, and can be run in any CLI context.

igor-sw-02# container vsphere exec show connection-status brief Hypervisor

Last Sync Connection State

laser-vcsa.lab.plexxi.com 2023-03-17 23:30:03 connected igor-sw-02# config

igor-sw-02(config)# container vsphere exec show connection-status brief

Hypervisor Last Sync Connection State

laser-vcsa.lab.plexxi.com 2023-03-17 23:30:07 connected igor-sw-02(config)#

interface 1/1/1

igor-sw-02(config-if)# container vsphere exec show connection-status brief

Hypervisor Last Sync Connection State

laser-vcsa.lab.plexxi.com 2023-03-17 23:30:15 connected

show connection-status

This command displays the connectivity status for the vSphere agent.

The connection timestamp is updated whenever a successful connection is made with the vSphere agent.
The sync timestamp is updated whenever a full sync, event poll, or event process occurs.

igor-sw-02(config-container-vsphere)# container vsphere exec show

connection-status brief Hypervisor Last Sync Connection State

laser-vcsa.lab.plexxi.com 2023-03-18 02:36:06 connected

igor-sw-02(config-container-vsphere)# container vsphere exec show

connection-status detailed Hypervisor : laser-vcsa.lab.plexxi.com
Connection State : connected Last Sync : 2023-03-18 02:35:08

Last Connection : 2023-03-18 02:35:09

igor-sw-02(config-container-vsphere)# container vsphere exec show

connection-status detailed Hypervisor : laser-vcsa.lab.plexxi.com

Connection State : disconnected Last Sync : 2023-03-18 02:04:05

Last Connection : 2023-03-18 02:09:30

Connection Failure Reason : Could Not Resolve Hostname
show neighbors

show neighbors command displays the virtual network adapter neighbor information.

Neighbors are pulled from distributed virtual switches of the vSphere and cached locally. Neighbors are used
to map VMs to physical switch ports.

Public

vSphere show commands 15

If you do not see a neighbor on the port, you will not see any VM connectivity on that port either. Detailed
and brief options are available. Filtering can be done on switch-name and/or interface.

igor-sw-02(config-container-vsphere)# container vsphere exec show neighbors

brief Chassis ID Switch Name Interface

b8:d4:e7:da:40:00 laser-sw-02 1/1/1 1/1/2

b8:d4:e7:d9:af:00 laser-sw-01 1/1/1 1/1/2

igor-sw-02(config-container-vsphere)# container vsphere exec show neighbors

detailed Chassis ID : b8:d4:e7:da:40:00

Switch Name : laser-sw-02

Switch Description : HPE_ANW JL635A GL.10.10.1000 Management Address :

192.168.200.1

Interface : 1/1/1 Advertisement Type : lldp TTL : 102

Interface : 1/1/2 Advertisement Type : lldp TTL : 102

Chassis ID : b8:d4:e7:d9:af:00 Switch Name : laser-sw-01

Switch Description : HPE_ANW JL635A GL.10.10.1000 Management Address :

192.168.200.0

Interface : 1/1/1 Advertisement Type : lldp TTL : 102

Interface : 1/1/2 Advertisement Type : lldp TTL : 102

Container management commands

Select a command from the list in the left navigation menu.

Subtopics

container
container exec
default-gateway
enable
env
image-location
ip address
mdns enable
mount
network isolated-network
network vrf
port-map
restrict cpu
restrict memory
show container
show capacities containers
show capacities-status containers
show running-config container

Public

Container management commands 16

virtual-interface vlan
vrf

container

Syntax

container <CONTAINER-NAME>|{isolated-network <name>}

no container <CONTAINER-NAME>

Description

Enters into the container configuration context. On 8325, 8325H and 8325P Switch series, include the
optional isolated-network parameter to configure containers using this network to appear as hosts physically
connected to the switch's front panel ports.

The no form of this command removes the existing configurations of the specified container.

Parameter

<CONTAINER‐NAME>

isolated‐network <name>

Description

The container name can contain up to 64 characters. Only l
etters, numbers and underscore ( _ ) characters are permitted
.

(For 8325, 8325H and 8325P Switch series) Use this paramete
r to configure a container isolated network supporting VLAN
‐aware configurations and unicast, broadcast, and multicast Et
hernet traffic types. The isolated network name can contain up
to 32 characters. Only letters, numbers and underscore ( _ ) cha
racters are permitted.

Usage

Note the following considerations when configuring an isolated network.

•  You can create only one isolated network configuration, and this configuration will apply to all containers

operating in isolated network mode.

•  Multicast traffic only works with the multicast DNS (mDNS) protocol.

•  Containers can use native ports, so you do not need to configure port mapping.

•  Be careful to avoid port conflicts between containers when running containers in this mode.

•

If you change the settings of an isolated network used by a container, the container will restart to apply
those changes.

Public

container 17

Example

Configures a new container:

switch(config)# container app

The feature being used requires a AOS-CX Advanced Software Feature Pack.

For more information,refer to the AOS-CX Feature Pack Deployment Guide.
AOS-CX does not enforce the requirement to own a feature pack prior to using container features. This
warning message is displayed only during creation, subsequent calls to the container context will not display
the message.

Setting the container configuration to isolated network mode:

switch(config)# container isolated-network net1

Command History

Release

10.12

Modification

Command introduced

Command Information

Platforms

Command context

Authority

Administrators or local user group members with execution righ
ts for this command.

config
config‐
container‐
<CONTAINER‐
NAME>

6300, except f
or S3L75A, S3
L76A and S3L
77A

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

Public

container 18

container exec

Syntax

container <NAME> exec <PARAMS>

Description

Allows the execution of an endpoint script in the container. The location of this endpoint is provided to
the container manager infrastructure through a manifest file in the image file system of the container. This
manifest file provides metadata related to the container application. When the exec command runs, the
manifest information is used to determine the endpoint to execute and the user parameters are passed
directly to the endpoint. The output of such execution is provided directly to the user through the CLI. In
case the manifest information or the endpoint file are missing an error is presented to the user. The user can
interrupt the execution by pressing Ctrl+C.

NOTE

If the container is not operational when the command is executed, the following
error message is returned: Failed to execute endpoint - The container is not
operational.

Parameter

Description

Specifies a container name up to 64 characters long.

<NAME>

exec

<PARAMS>

Command History

Runs a container application command.

Specifies container command parameters.

Release

10.12

Modification

Command introduced

Public

container exec 19

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

config‐
container‐
<CONTAINER‐
NAME>

Administrators or local user group members with execution righ
ts for this command.

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

default-gateway

Syntax

default-gateway <ip-addr>

no default-gateway [<ip-addr>]

Description

Configures a default gateway IP address for the isolated network. The default gateway is used by
containers to route traffic outside the local network provided by the virtual interfaces. After completing
the configuration, use the  show container isolated-network  command to verify that the
default gateway is valid. It will automatically check the IP address is within the subnet of at least one
configured virtual interface and report any error.

The no version of this command removes the default gateway configuration.

Public

default-gateway 20

Parameter

<ip‐addr>

Description

The default gateway used by a containers in isolated network m
ode to route traffic outside the local network provided by the vi
rtual interfaces.

Example

Configuring a default gateway:

switch(config-container-isolated-network-<name>)# default-gateway <ip-addr>

Command History

Release

10.17

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8325

8325H

8325P

config‐
container‐
isolated‐
network‐
<network‐name>

Administrators or local user group members with execution righ
ts for this command.

enable

Syntax

enable

no enable

Description

Enables the container. By default, a container is disabled when it is created, meaning it cannot execute.
Enabling the container allows it to start execution. Once a container is enabled, any subsequent
configuration change causes it to restart so the new configuration can be applied. For this reason, it is
considered best practice to complete as much configuration as possible before enabling the container.

Public

enable 21

If a container is enabled and the switch it is running on is restarted, the container will automatically start
again after the switch reboots, without requiring any additional user intervention.

The no version of this command disables the container. When an enabled container is disabled, system
resources are released but the container configuration settings are stored.

Example

Enabling and then disabling the container test:

switch(config-container-test)# enable

switch(config-container-test)# no enable

Command History

Release

10.17.1000

10.16.1000

Modification

Additional feature information.

Command introduced

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

config‐
container‐
<CONTAINER‐
NAME>

Administrators or local user group members with execution righ
ts for this command.

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

Public

enable 22

env

Syntax

env <NAME> {value <VALUE>}|{encrypted [plaintext <VALUE>|ciphertext

<VALUE>]}

no env <NAME> {value <VALUE>}|{encrypted {plaintext|ciphertext}<VALUE>}

Description

Configures an environment variable for a container that is composed of a key and a value pair. The key-value
pair defines the behavior of the environment in a container and is used by the container processes. The
value of the environment variable can be stored in the host system as an encrypted value. The container
manager infrastructure provides the decrypted value to the container.

The no form of this command removes the configured environment variable from a container.

NOTE
The predefined environmental variable CX-SERIAL is used to share for the switch
serial number to a container and is reserved for internal use only. Do not modify
this variable, or attempt to create another variable with the same name.
Configuring the env variable for an already operational container causes the
container to restart if the container has already been enabled.

Parameter

Description

Specifies the name of the container environment variables.

<NAME>

value <VALUE>

   encrypted

Specifies the variable value.

Encrypts the environment variable value. If you press <enter> a
fter the encrypted parameter, you will enter a variable configur
ation mode that allows you to securely enter a hidden value. Thi
s is the recommended method for entering an encrypted variabl
e

Public

env 23

Parameter

Description

plaintext <VALUE>

ciphertext <VALUE>

Optional. Specifies the variable value in plain text. Not recomm
ended for encrypted variables.

Optional. Specifies the variable value as previously encrypted
text. Recommended for encrypted variables; specify the encry
pted variable value as previously encrypted text.

Example

Securely entering an encrypted variable:

6300(config-container-test)# env TEST encrypted

Enter environment variable value: ********

6300(config-container-test)# end

Command History

Release

10.13.1000

Modification

The plaintext and ciphertext options for the encrypted parameter are now opti
onal. Starting with this release, you can use the encrypted option to encrypt the
environment variable and specify the value in plaintext hidden from the CLI.

10.12

Command introduced

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

config‐
container‐
<CONTAINER‐
NAME>

Administrators or local user group members with execution righ
ts for this command.

6400

8100

8320

8325

8325H

8325P

8360

Public

env 24

Platforms

Command context

Authority

8400

9300

9300S

10000

10040

image-location

Syntax

image-location <URL> vrf <VRF-NAME> [allow-unsigned]

no image-location <URL>

            <VRF-NAME> [allow-unsigned]

Description

Configures the image location for a container. Modifying image location prompts an image upgrade.

The no form of this command removes the configured location of a container.

NOTE

•

•

If the user sets a location value which does not follow the standard URL
format, the following error message is returned: Failure to configure image
location: Invalid URL

If the user tries to use a VRF value that doesn't exist on the switch, the
following error message is returned: Failure to configure image location:
Invalid VRF

•

If the image of the container exceeds the maximum image size supported by
the switch, the container won't be deployed.

By default, only container images with a valid HPE signature are allowed. To bypass this signature check
and allow unsigned container images, include the allow-unsigned parameter when you define the image
location. The allow-unsigned parameter cannot be used if you have issued the secure-mode enhanced
command to set the switch to enhanced secure mode.

Public

image-location 25

Parameter

URL

Description

Specifies the URL of the container application. URL supports H
TTP protocol. The image‐location URL can either be IPv4 or I
Pv6 address. The IPv6 address must be provided within square
brackets.

vrf <VRF‐NAME>

(Optional) Specifies the VRF of the image URL.

allow‐unsigned

(Optional) Allow download and deployment of an unsigned con
tainer image.

Examples

Configures the image location for the IPv4 setting:

switch(config-container-1)# image-location http://10.0.0.1/container.img

vrf mgmt

Appends the port to the address if the image server is running on a port other than HTTP for an IPv4
setting:

switch(config-container-1)# image-location http://10.0.0.1:9050/

container.img vrf mgmt

Configures image location for IPv6 setting by wrapping IP address between square brackets:

switch(config-container-1)# image-location http://[2001::2]/container.img

vrf mgmt

Specifies port number by appending it with the IPv6 address:

switch(config-container-1)# image-location http://[2001::2]:9050/

container.img vrf mgmt

When you include the allow-unsigned parameter on a switch in standard secure mode, the following
message will be displayed to inform this can be a potential security issue.

switch(config-container-1)# image-location http://10.0.0.1/container.img

vrf mgmt allow-unsigned

Allowing unsigned container images poses a potential security risk
that can impact both the current device and the entire network. By

allowing installation of unsigned applications you are acknowledging

and accepting these risks. HPE shall not be responsible for the

Public

image-location 26

consequences of your actions and disclaims any and all liability.

Continue (y/n)? y
When you attempt to include the allow-unsigned parameter on a switch in enhanced secure mode, the
following message will appear to indicate that this parameter is not supported.

switch(config-container-1)# image-location http://10.0.0.1/container.img

vrf mgmt allow-unsigned

            Unsigned images are not permitted in the current secure mode,

using the

allow-unsigned parameter will have no effect.

Release

10.14

10.12

Modification

The allow‐unsigned parameter is introduced.

Command introduced.

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

config‐
container‐
<CONTAINER‐
NAME>

Administrators or local user group members with execution righ
ts for this command.

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

Public

image-location 27

ip address

Syntax

ip address <ipaddr>/<submask>

no ip address <ipaddr>/<submask>

Description

Configures an IPv4 address and subnet mask for a virtual interface for an isolated network. Each virtual
interface must have a unique, non-overlapping subnet. After completing the configuration, use the  show-c
ontainer-isolated-network  command to verify that the subnet assignments are valid. This will
automatically check for overlapping or duplicate subnets and report any detected conflicts.

The no version of this command removes the IP address configuration from the virtual interface.

NOTE

Do not assign the same IP address to both a virtual interface and an SVI
(interface VLAN) in any VRF that uses the same VLAN. Doing so causes both
the SVI and the virtual interface will respond to ARP requests for that IP address
—potentially using different MAC addresses (the system MAC from the SVI or
the container MAC from the virtual interface). This can lead to non‑deterministic
behavior in the network, as devices may send traffic to either the SVI or the
container depending on which ARP reply they have cached. To ensure consistent
connectivity and routing, always assign each IP address uniquely to either the SVI
or the virtual interface, but not both.

Parameter

<ipaddr>

Example

Description

An IPv4 address for the virtual interface. The IP address must
be in CIDR notation ( or example 192.0.2.0/24).

Configuring the virtual interface with an IP address 10.0.0.2 and a subnet mask of /24.

switch(config-container-isolated-network-virtual-interface)# ip address

10.0.0.2/24

Command History

Release

Modification

10.17.1000

Additional description information.

Public

ip address 28

Release

10.17

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

8325

8325H

8325P

config‐
container‐
isolated‐
network‐
<network‐name>

Administrators or local user group members with execution righ
ts for this command.

mdns enable

Syntax

mdns enable

no mdns enable

Description

Allow a container in isolated network mode to use the multicast DNS (mDNS) protocol for the isolated
network. When mDNS is enabled, containers can look up names on a local network without a regular DNS
server. This allows devices on the same VLAN or subnet find container services and match hostnames to IP
addresses using multicast.

The no version of this command disables this feature.

Usage

This configuration is not required if the mDNS based service discovery (mDNS-SD) feature is already
configured globally and in the same VLANs used by the container.

Example

Enabling the mDNS

switch(config-container-isolated-network-net1)# mdns enable

Public

mdns enable 29

Command History

Release

10.17

Modification

Command introduced

Command Information

Platforms

Command context

Authority

Administrators or local user group members with execution righ
ts for this command.

8325

8325H

8325P

config‐
container‐
isolated‐
network‐
<network‐name>

mount

Syntax

mount <id>

   destination <path>

   no ...

   source <TYPE> <PATH>

Description

Mount persistent storage for a container application, and optionally indicate the mounted storage source
and destination paths.

Parameter

<ID>

destination <PATH>

Description

ID assigned to a mounted storage instance for a container appli
cation. Range: <1‐4294967295>

The destination path is a directory or file inside the container fil
e system. The path must use the syntax /{FILE|DIRECTORY}. O
nly letters, numbers, slashes, underscores, dashes, and periods
are allowed.

Public

mount 30

Parameter

no ...

source

   <type>

   <PATH>

Description

Negates any configured parameter or removes a source or desti
nation path.

Define the mounted storage source.

This version of AOS‐CX supports only a usb storage type.

NOTE

For containers using USB persistent storage fun
ctionality, ext4 is the recommended formatting
method for USB storage devices. While FAT32 is
currently supported, it may be deprecated in fut
ure releases.

The mounted storage source path must be a valid file or directo
ry on the USB device and is relative to the root directory of th
e device file system. The path must use the syntax /{FILE|DIRE
CTORY}. Only letters, numbers, slashes, underscores, dashes, a
nd periods are allowed.

Example

Creating the mount ID 1 for the container test.

switch(config-container-test)# mount 1
Configuring container mount 1 with a USB source and the path /app1-data.

switch(config-container-mount-1)# source usb /app1-data
Configuring container mount 1 with the destination path /app1-data.

switch(config-container-mount-1)# destination /app1-data

Command History

Release

Modification

10.16.1000

Command introduced

Command Information

Platforms

Command context

Authority

8100

config‐
container‐

Administrators or local user group members with execution righ
ts for this command.

Public

mount 31

Platforms

Command context

Authority

<CONTAINER‐
NAME>

8320

8325

8325H

8325P

8360

9300

9300S

10000

10040

network isolated-network

Syntax

network isolated-network <name>

no network isolated-network <name>

Description

Configure the isolated network to be used by the container application operating in isolated-network mode.
The no version of this command ensures that the container no longer uses the indicated isolated-network as
its network mode.

Parameter

<name>

Example

Description

Name of the new isolated network

Associate the container app with an isolated network named net1.

switch (config-container-app)# network isolated-network net1

Public

network isolated-network 32

Command History

Release

10.17

Modification

Command introduced

Command Information

Platforms

Command context

Authority

Administrators or local user group members with execution righ
ts for this command.

8325

8325H

8325P

config‐
container‐
isolated‐
network‐
<network‐name>

network vrf

Syntax

network vrf <VRF>

no network vrf <VRF>

Description

Use this command to associate a VRF with the container and allow connectivity through the VRF. When
configured, the VRF will be accessible to the container through a network namespace.

Usage

Only one network VRF can be configured per container. If an additional VRF is configured, the container
deployment will fail and generate an error message indicating that the container has more than one network
VRF. Modifying a network container VRF will modify the container network configuration and the container
will be restarted to apply the new changes if the container has already been enabled.

Examples

The following example defines the VRF mgmt for the app container.

switch(config-container-app)# network vrf mgmt

Public

network vrf 33

Command History

Release

10.16

Modification

Command introduced

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

config‐
container‐
<CONTAINER‐
NAME>

Administrators or local user group members with execution righ
ts for this command.

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

port-map

Syntax

port-map host-port <PORT> container-port <PORT> protocol (tcp | udp)

Public

port-map 34

Description

Issue this command from the config-container-network-vrf-<name> context to define a port map from a
port on the host switch to a port on the container. This will allow communication from external devices to
services provided by the container.

Parameter

Description

host‐port <port>

The host switch port number. Range: 1‐65535

container‐port <port>

The container port number. Range: 1‐65535

tcp

udp

Usage

Communications will use the TCP protocol.

Communications will use the UDP protocol.

A port map is an optional configuration for a container network VRF, but a port mapping is required to
expose the mapped port to the outside network. This command can be issued multiple times to define more
than one port map for the container.

NOTE

Host port conflicts are not allowed. The same host port cannot be used for
different containers in the same VRF, and the host port used for the VRF cannot
be reserved for a non-container application on the host switch.

Examples

Configure a port map from the host to the container for TCP traffic, where traffic to TCP port 8000 on the
switch will be directed to TCP port 9000 in the container.

switch(config-container-network-vrf-mgmt)# port-map host-port 8000
container-port 9000 protocol tcp
The following example maps different ports on the host to the same container port for TCP traffic:

switch(config-container-network-vrf-mgmt)# port-map host-port 8000

container-port 9000 protocol tcp

switch(config-container-network-vrf-mgmt)# port-map host-port 8001

container-port 9000 protocol tcp
The following example maps the same port on the host switch to the same container port for TCP and UDP
traffic:

switch(config-container-network-vrf-mgmt)# port-map host-port 8000

container-port 9000 protocol tcp

Public

port-map 35

switch(config-container-network-vrf-mgmt)# port-map host-port 8000

container-port 9000 protocol udp
The following example maps the same port on different VRFs on the host switch to the same container port
for TCP traffic:

switch(config-container-network-vrf-mgmt)# port-map host-port 8000

container-port 9000 protocol tcp

switch(config-container-network-vrf-default)# port-map host-port 8000

container-port 9000 protocol tcp
When removing a port mapping, if the command parameters do not match a configured port mapping, the
command output displays the following message:

switch(config-container-network-vrf-mgmt)# no port-map host-port 8001

container-port 9000 protocol tcp

The specified port mapping is not configured

Command History

Release

Modification

10.16.1000

Command introduced

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

config‐
container‐
<CONTAINER‐
NAME>

Administrators or local user group members with execution righ
ts for this command.

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

Public

port-map 36

Platforms

Command context

Authority

10040

restrict cpu

Syntax

restrict cpu <PERCENTAGE>

no restrict cpu

Description

Configures limitations for the container CPU usage. The CPU constraint is set as a percentage of the total
switch CPUs. One container or any combination of containers configured on a switch can use up to 20% of
the total CPU capacity of the device.

NOTE

Configuring the CPU constraint for an already operational container will cause
the container to restart if the container has already been enabled.

The no form of this command removes restrictions on the CPU usage, and reverts back to the default
limitation of 10%.

Parameter

Description

Specifies percentage for the container CPU usage, The default
value is 10%.

<PERCENTAGE>

Command History

Release

10.12

Modification

Command introduced

Public

restrict cpu 37

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

config‐
container‐
<CONTAINER‐
NAME>

Administrators or local user group members with execution righ
ts for this command.

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

restrict memory

Syntax

restrict memory <MB>

no restrict memory

Description

Configures limitations for memory usage of the container. The memory constraint is set in MB, and the
maximum 20% of the capacity of the device can be configured for any combination of containers running on
the switch. Configuring the memory constraint for an already operational container restarts the container if
the container has already been enabled.

The no form of this command removes restrictions on the memory usage and reverts back to the default
limitation of 256 MB.

Public

restrict memory 38

Parameter

Description

Specifies the maximum memory usage in MB.The default value i
s 256 MB.

<MB>

Command History

Release

10.12

Modification

Command introduced

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

config‐
container‐
<CONTAINER‐
NAME>

Administrators or local user group members with execution righ
ts for this command.

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

Public

restrict memory 39

show container

Syntax

show container [<CONTAINER-NAME>]|[isolated-network <name>]

Description

Shows the configuration and status information of the containers or container isolated networks running in
the system. If the container or isolated network name is not specified, the output of this displays information
for all containers or isolated networks. When a container name or isolated network name is specified, the
output displays information specific to that container or isolated network.

Parameter

Description

Specifies the name of the container for which information needs
to be displayed

<CONTAINER‐NAME>

isolated‐network <name>

(For 8325, 8325H or 8325P Switch series only) Specifies the n
ame of the isolated network for which information needs to be
displayed.

Usage

The Container status field in the output of this command can display any of the following status values:

•

initializing: Container initialization and configuration verification is in progress.

•  waiting: Container is waiting for configuration prerequisites to be met.

•  configuration failed: User-specified container configuration failed.

•  network configuration failed: Container network provisioning failed.

•  acquiring: Container is acquiring an image.

•  paused: Container has been paused.

•  acquire failed: Container failed to acquire an image.

•  deploying: Container is deploying.

•  operational: Container is operational (deployed and running).

•  deploy failed: Container failed to deploy.

•  run failed: Container failed while running.

Public

show container 40

•  exited: Container completed its execution and exited.

•  paused: Container has been paused.

Examples

The following example shows information for a configured container with a network VRF with port
mappings:

switch# show container

Container              : app1

  Container status     : operational

  Manifest status      : success

  Image status         : verified

  Image version        : 1.0.0

  Image location VRF   : mgmt

  Image location URL   : http://30.0.0.2:8000/container.img

  CPU limit            : 10%

  Memory limit         : 512MB

  Environment variables:

    PYP=/usr/bin/python3

  Encrypted environment variables:

    encryptedVar1

    encryptedVar2

  Vrf NetworkS:

    VRF name  : default

    Port map  :

        8080:80/tcp

        8080:8080/udp
The following example shows additional error messages:

switch# show container

Container                : app

  Container status       : configuration failed
  Config failure reason  : Multiple definitions of environment variable PYP

  Manifest status        : error

  Manifest status reason : 'exec' file not found in container

  Image status           : verified

  Image version          : 1.0.0

  Image location VRF     : mgmt

  Image location URL     : http://30.0.0.2:8000/container.img

  CPU limit              : 10%

  Memory limit           : 512 MB

  VRFs                   : mgmt

  Environment variables  :

    PYP=/usr/bin/python3

Public

show container 41

Encrypted environment variables:

    PYP

    encryptedVar2
The following example shows a configured container without signature validation:

switch# show container app1

Container              : app1

  Container status     : operational

  Manifest status      : success

  Image status         : allowed without signature

  Image version        : 1.0.0

  Image location VRF   : mgmt

  Image location URL   : http://30.0.0.2:8000/container.img

  CPU limit            : 10%

  Memory limit         : 512 MB

  Environment variables:

    PYP=/usr/bin/python3

  Encrypted environment variables:

    encryptedVar1

    encryptedVar2

  VRF Networks:

    VRF name  : default

    Port map  :

      8080:80/tcp

      8080:8080/udp
Sample output with a configured container on a 8325 Switch series using a VRF network. The output of
the show container command for an 8325/8325H/8325P switch series is slightly different than for other
AOS-CX switch series in that it can include information about an isolated network configuration.

switch# show container

Container              : app

Container status     : operational

Manifest status      : success
Image status         : verified

Image version        : 1.0.0

Image location VRF   : mgmt

Image location URL   : http://192.0.2.2:8000/container.img

CPU limit            : 10%

Memory limit         : 512MB

Environment variables:

  PYP=/usr/bin/python3

Encrypted environment variables:

  encryptedVar1

  encryptedVar2

VRF networks:

Public

show container 42

VRF name  : mgmt

  Port map  : n/a

Isolated network: net1

Mounts: n/a
The following example output for the show container isolated-network command shows details for
isolated network net1 with mDNS enabled, three virtual interfaces, and two containers, test1 and test2
using this isolated network. Note that only 8325, 8325H and 8325P switch series support containers in
isolated mode..

switch# show container isolated-network net1

Isolated network        : net1

Status                  : network_provisioned

Status reason           : n/a

Default gateway         : n/a

mDNS                    : enabled

Virtual MAC             : 00:55:00:A1:B2:C3

Containers              :

   test1

   test2

Virtual interfaces      :

------------------------

VLAN  IP address

-----------------------

10    10.0.0.1/24

20    20.0.0.1/24

4094  192.168.134.252/24
The following example shows the output of the show containers command out when there are no configured
containers:

switch# show container

No containers configured

Command History

Release

10.17

Modification

The output of this command can display information for isolated network config
urations on 8325, 8325H and 8325P Switch series.

10.12

Command introduced

Public

show container 43

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

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

show capacities containers

Syntax

show capacities containers

Description

Shows the maximum number of containerized applications that can be configured in the system.

Examples

Shows maximum number of containerized applications that can be configured:

switch# show capacities containers

System Capacities: Filter CONTAINERS

Capacities

Name

Public

show capacities containers 44

Value

----------------------------------------------------------------------------

-----------------

Maximum number of containerized applications configurable in the

system                     2

Maximum number of virtual interfaces in an isolated network configurable in

the system     64

Command History

Release

10.12

Modification

Command introduced

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

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

Public

show capacities containers 45

show capacities-status containers

Syntax

show capacities-status containers

Description

Reserved for future use.

Command History

Release

10.12

Modification

Command introduced

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

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

Public

show capacities-status containers 46

show running-config container

Syntax

show running-config container

Description

Shows the running configuration of all the containers.

Parameter

container

Examples

Description

Specifies that container running configuration must be displaye
d.

Shows the running configuration for the container:

   container app1

       enable

image-location http://30.0.0.2:8000/container.img vrf mgmt

restrict cpu 10

restrict memory 512

network vrf mgmt

port-map host-port 8000 container-port 9000 protocol tcp

exit

mount 1

source usb /app1-data

destination /app-data

exit

env PYP value /usr/bin/python3

env encryptedVar1 encrypted ciphertext AQBapcmTCVdag

container app2

enable

image-location http://[2001::2]:8000/changeValidation_x86_t.img vrf

mgmt allow-unsigned

restrict cpu 5

restrict memory 256

network vrf default

port-map host-port 7819 container-port 7819 protocol udp

exit

mount 1

source usb /app2-data1

destination /app-data1

Public

show running-config container 47

exit

mount 2

source usb /app2-data2

destination /app-data2

exit

env PYP value /usr/bin/python3

env encryptedVar1 encrypted ciphertext AQBapcmTCVdag

env encryptedVar2 encrypted ciphertext AQpY4V4v9UtDa==

Command History

Release

10.16.1000

Modification

The output of this command includes mount and network VRF details, if configu
red.

10.12

Command introduced

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

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

Public

show running-config container 48

virtual-interface vlan

Syntax

virtual-interface vlan <1-4094>

no virtual-interface vlan <1-4094>

Description

Sets up a virtual interface in an isolated network for a container in isolated-network mode. This virtual
interface is linked to a VLAN ID and works as a network connection for the isolated network. It lets
containers communicate with external devices connected to the switch's front panel ports within the same
VLAN.

Parameter

<1‐4094>

Description

A VLAN ID. Each isolated network virtual interface must be ass
ociated with unique VLAN ID, and that VLAN must already exist
on the switch.

Example

Configuring a virtual interface on vlan 10:

switch(config-container-isolated-network-<name>)# virtual-interface vlan 10

Command History

Release

10.17

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8325

8325H

8325P

config‐
container‐
isolated‐
network‐
<network‐name>

Administrators or local user group members with execution righ
ts for this command.

Public

virtual-interface vlan 49

vrf

Syntax

vrf <VRF-NAME>

Description

This command is deprecated. Use the network vrf command to define a VRF for a container.

Command History

Release

10.12

Modification

Command introduced

Command Information

Platforms

Command context

Authority

6300, except f
or S3L75A, S3
L76A and S3L
77A

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

Public

vrf 50

Support and Other Resources

Access HPE Aruba Networking support and updates, and view warranty and regulatory information

Subtopics

Accessing HPE Aruba Networking Support
Accessing Updates
Warranty Information
Regulatory Information
Documentation Feedback

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

https://www.hpe.com/us/en/networking/hpe‐aru
ba‐networking‐support‐services.html

AOS‐CX Switch Software Documentation Portal

HPE Aruba Networking Support Portal

https://networkingsupport.hpe.com/home

North America telephone

1‐800‐943‐4526 (US & Canada Toll‐Free Nu
mber)

+1‐650‐750‐0350 (Backup—Toll Number)

International telephone

https://www.hpe.com/psnow/doc/a50011948enw

Be sure to collect the following information before contacting Support:

•  Technical support registration number (if applicable)

•  Product name, model or version, and serial number

•  Operating system name and version

•  Firmware version

•  Error messages

•  Product-specific reports and logs

•  Add-on products or components

Public

Support and Other Resources 51

•  Third-party products or components

Other useful sites

Other websites that can be used to find information:

HPE Aruba Networking Developer Hub

https://developer.arubanetworks.com/hpe‐aruba
‐networking‐aoscx/docs/about

Airheads social forums and Knowledge Base

https://community.arubanetworks.com/

AOS‐CX Software Technical Update channel on You
Tube.

Videos on new features introduced in this release
: https://www.youtube.com/playlist?list=PLsYGHu
NuBZcbWPEjjHuVMqP‐Q_UL3CskS

HPE Aruba Networking Hardware Documentation an
d Translations Portal

HPE Aruba Networking software

https://networkingsupport.hpe.com/downloads h
ttps://networkingsupport.hpe.com/downloads

Software licensing and Feature Packs

https://licensemanagement.hpe.com/

End‐of‐Life information

https://networkingsupport.hpe.com/end‐of‐life

Accessing Updates

You can access updates from the HPE Aruba Networking Support Portal at https://
networkingsupport.hpe.com.

Some software products provide a mechanism for accessing software updates through the product interface.
Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://networkingsupport.hpe./notifications/subscriptions (requires an active HPE Aruba Networking
Support Portal account to manage subscriptions). Security notices are viewable without an HPE Aruba
Networking Support Portal account.

Public

Accessing Updates 52

Warranty Information

To view warranty information for your product, go to https://www.arubanetworks.com/support-services/
product-warranties/.

Regulatory Information

To view the regulatory information for your product, view the Safety and Compliance Information for
Server, Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

HPE Aruba Networking is committed to providing our customers with information about the chemical
substances in our products as needed to comply with legal requirements, environmental data (company
programs, product recycling, energy efficiency), and safety information and compliance data, (RoHS and
WEEE). For more information, see https://www.arubanetworks.com/company/about-us/environmental-
citizenship/.

Documentation Feedback

HPE Aruba Networking is committed to providing documentation that meets your needs. To help us improve
the documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition, and
publication date located on the front cover of the document. For online help content, include the product
name, product version, help edition, and publication date located on the legal notices page.

Public

Warranty Information 53